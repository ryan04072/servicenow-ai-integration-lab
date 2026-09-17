from pathlib import Path
import json, sys

# Run from repository root or set PYTHONPATH to repo root.
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from reference_runtime.store import ArtifactStore
from reference_runtime.context_service import ContextService
from reference_runtime.human_actions import HumanActionBroker
from reference_runtime.telemetry import JsonlTelemetry
from reference_runtime.orchestrator import EnhancementOrchestrator

FIX=ROOT/"reference_runtime"/"fixtures"
store=ArtifactStore.from_files(FIX/"artifacts.json",FIX/"edges.json")
context=ContextService(store)
human=HumanActionBroker()
telemetry=JsonlTelemetry(ROOT/"personal-lab"/"runtime-api"/"data"/"trace.jsonl")
orch=EnhancementOrchestrator(context,human,telemetry)

app=FastAPI(title="Personal Agentic ServiceNow Runtime",version="3.0")

class WorkItem(BaseModel):
    id: str
    title: str
    description: str = ""
    acceptance_criteria: list[str] = []

class Decision(BaseModel):
    responder: str
    decision: str
    comment: str = ""

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/context")
def build_context(item: WorkItem):
    return context.build_envelope(item.model_dump())

@app.post("/runs")
def start_run(item: WorkItem):
    return orch.start(item.model_dump(),approver="platform_owner")

@app.get("/human-actions/{action_id}")
def get_action(action_id: str):
    action=human.actions.get(action_id)
    if not action:
        raise HTTPException(404,"Action not found")
    return action.to_dict()

@app.get("/human-actions/{action_id}/card")
def get_card(action_id: str):
    action=human.actions.get(action_id)
    if not action:
        raise HTTPException(404,"Action not found")
    return human.adaptive_card(action)

@app.post("/runs/{run_id}/architecture-decision")
def resolve(run_id: str, decision: Decision):
    if run_id not in orch.runs:
        raise HTTPException(404,"Run not found")
    return orch.resolve_architecture(run_id,decision.responder,decision.decision,decision.comment)
