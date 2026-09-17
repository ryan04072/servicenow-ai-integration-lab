from __future__ import annotations
from typing import Dict, Optional
from .models import HumanAction, new_id, utc_now

class HumanActionBroker:
    def __init__(self):
        self.actions: Dict[str, HumanAction] = {}

    def create(self, correlation_id: str, action_type: str, title: str, summary: str,
               requested_from: list[str], authoritative_system: str,
               authoritative_record: Optional[str], allowed_responses: list[str],
               recommended_response: Optional[str]=None, risk: Optional[str]=None) -> HumanAction:
        action = HumanAction(
            action_id=new_id("HA"),
            correlation_id=correlation_id,
            action_type=action_type,
            status="open",
            title=title,
            summary=summary,
            requested_from=requested_from,
            authoritative_system=authoritative_system,
            authoritative_record=authoritative_record,
            allowed_responses=allowed_responses,
            recommended_response=recommended_response,
            risk=risk
        )
        self.actions[action.action_id] = action
        return action

    def resolve(self, action_id: str, responder: str, decision: str, comment: str="") -> HumanAction:
        action = self.actions[action_id]
        if action.status != "open":
            raise ValueError("Human action is not open.")
        if decision not in action.allowed_responses:
            raise ValueError(f"Decision {decision!r} is not allowed.")
        if responder not in action.requested_from and action.participant_mode == "single":
            raise PermissionError("Responder is not authorized for this action.")
        action.status = "resolved"
        action.resolved_at = utc_now()
        action.resolved_by = responder
        action.decision = decision
        action.comment = comment
        action.resume_event = {
            "event_id": new_id("EVT"),
            "event_type":"human_action.resolved",
            "source_system":"human_action_broker",
            "occurred_at": utc_now(),
            "correlation_id": action.correlation_id,
            "source_record": action.action_id,
            "source_version":"1",
            "actor": responder,
            "payload":{"action_id":action.action_id,"decision":decision,"comment":comment}
        }
        return action


    def create_expert_context_request(self, correlation_id: str, title: str, question: str,
                                      requested_from: list[str], authoritative_system: str,
                                      authoritative_record: Optional[str]=None) -> HumanAction:
        return self.create(
            correlation_id=correlation_id,
            action_type="clarification",
            title=title,
            summary=question,
            requested_from=requested_from,
            authoritative_system=authoritative_system,
            authoritative_record=authoritative_record,
            allowed_responses=["provide_context","needs_discussion"],
            recommended_response=None,
            risk="medium"
        )

    def adaptive_card(self, action: HumanAction) -> Dict:
        # Transport-neutral Adaptive Card. An enterprise adapter can post it to Teams.
        return {
            "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
            "type":"AdaptiveCard","version":"1.4",
            "body":[
                {"type":"TextBlock","size":"Medium","weight":"Bolder","text":action.title},
                {"type":"TextBlock","wrap":True,"text":action.summary},
                {"type":"FactSet","facts":[
                    {"title":"Action","value":action.action_id},
                    {"title":"Type","value":action.action_type},
                    {"title":"Risk","value":action.risk or "not set"},
                    {"title":"System of record","value":action.authoritative_system}
                ]},
                {"type":"Input.Text","id":"comment","isMultiline":True,"placeholder":"Optional comments"}
            ],
            "actions":[
                {"type":"Action.Submit","title":label.replace("_"," ").title(),
                 "data":{"action":"resolve_human_action","action_id":action.action_id,"decision":label}}
                for label in action.allowed_responses
            ]
        }
