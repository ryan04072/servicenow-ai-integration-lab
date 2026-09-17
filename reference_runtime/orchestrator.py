from __future__ import annotations
from typing import Dict, Optional
from .models import new_id, utc_now
from .context_service import ContextService
from .human_actions import HumanActionBroker
from .telemetry import JsonlTelemetry

class EnhancementOrchestrator:
    def __init__(self, context: ContextService, human: HumanActionBroker, telemetry: JsonlTelemetry):
        self.context = context
        self.human = human
        self.telemetry = telemetry
        self.runs: Dict[str, Dict] = {}

    def start(self, work_item: Dict, approver: str="platform_owner") -> Dict:
        run_id = new_id("RUN")
        correlation_id = work_item.get("id") or new_id("CORR")
        run = {
            "run_id":run_id,
            "correlation_id":correlation_id,
            "state":"SUBMITTED",
            "work_item":work_item,
            "state_history":[{"state":"SUBMITTED","at":utc_now()}],
            "context_envelope":None,
            "human_action_id":None,
            "recommendation":None,
            "status":"running"
        }
        self.runs[run_id] = run
        self.telemetry.emit("run.started",{"run_id":run_id,"correlation_id":correlation_id})
        self._transition(run,"INTAKE")
        self._transition(run,"CONTEXT_DISCOVERY")
        envelope = self.context.build_envelope(work_item)
        run["context_envelope"] = envelope
        self.telemetry.emit("context.built",{
            "run_id":run_id,"correlation_id":correlation_id,
            "artifact_ids":[a["id"] for a in envelope["artifacts"]],
            "relationship_count":len(envelope["relationships"]),
            "confidence":envelope["confidence"]
        })
        self._transition(run,"ARCHITECTURE_DRAFT")

        reuse = self._select_reuse_candidate(envelope)
        if reuse:
            run["recommendation"] = {
                "type":"extend_existing",
                "artifact_id":reuse["id"],
                "artifact_name":reuse["name"],
                "summary":f"Extend existing {reuse['name']} pattern rather than create a duplicate standalone implementation."
            }
        else:
            run["recommendation"] = {
                "type":"new_build",
                "summary":"No sufficiently relevant existing implementation was found; investigate a new implementation."
            }

        self._transition(run,"AWAITING_ARCHITECTURE_DECISION")
        action = self.human.create(
            correlation_id=correlation_id,
            action_type="approval",
            title=f"Architecture decision: {work_item.get('title','ServiceNow enhancement')}",
            summary=run["recommendation"]["summary"],
            requested_from=[approver],
            authoritative_system="servicenow",
            authoritative_record=correlation_id,
            allowed_responses=["approve","request_changes","reject"],
            recommended_response="approve" if reuse else None,
            risk="medium"
        )
        run["human_action_id"] = action.action_id
        self.telemetry.emit("human_action.created",{
            "run_id":run_id,"correlation_id":correlation_id,
            "action_id":action.action_id,"action_type":action.action_type
        })
        return run

    def resolve_architecture(self, run_id: str, responder: str, decision: str, comment: str="") -> Dict:
        run = self.runs[run_id]
        action = self.human.resolve(run["human_action_id"], responder, decision, comment)
        self.telemetry.emit("human_action.resolved",{
            "run_id":run_id,"correlation_id":run["correlation_id"],
            "action_id":action.action_id,"decision":decision,"responder":responder
        })
        if decision == "approve":
            self._transition(run,"BACKLOG_READY")
            run["status"]="waiting_for_delivery"
        elif decision == "request_changes":
            self._transition(run,"ARCHITECTURE_DRAFT")
            run["status"]="needs_rework"
        else:
            self._transition(run,"CANCELLED")
            run["status"]="cancelled"
        return run

    def _select_reuse_candidate(self, envelope: Dict) -> Optional[Dict]:
        cands = [
            a for a in envelope["artifacts"]
            if a["artifact_type"] in {"catalog_item","flow","script_include"}
            and a.get("retrieval_score",0) >= 0.15
        ]
        if not cands:
            # dependency-expanded artifacts may not carry retrieval scores; prefer catalog if present
            cands = [a for a in envelope["artifacts"] if a["artifact_type"]=="catalog_item"]
        return sorted(cands,key=lambda x:x.get("retrieval_score",0),reverse=True)[0] if cands else None

    def _transition(self, run: Dict, state: str):
        prior = run["state"]
        run["state"] = state
        run["state_history"].append({"state":state,"at":utc_now()})
        self.telemetry.emit("state.transition",{
            "run_id":run["run_id"],"correlation_id":run["correlation_id"],
            "from_state":prior,"to_state":state
        })
