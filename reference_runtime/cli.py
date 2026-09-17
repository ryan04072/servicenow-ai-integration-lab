from __future__ import annotations
import argparse, json, tempfile
from pathlib import Path
from .store import ArtifactStore
from .context_service import ContextService
from .human_actions import HumanActionBroker
from .telemetry import JsonlTelemetry
from .orchestrator import EnhancementOrchestrator
from .evals import evaluate_context, evaluate_recommendation

ROOT = Path(__file__).resolve().parent
FIX = ROOT / "fixtures"

def make_runtime(trace_path: str | None=None):
    store = ArtifactStore.from_files(FIX/"artifacts.json", FIX/"edges.json")
    context = ContextService(store)
    human = HumanActionBroker()
    telemetry = JsonlTelemetry(trace_path or (ROOT/"output"/"trace.jsonl"))
    orch = EnhancementOrchestrator(context,human,telemetry)
    return context,human,orch

def cmd_context():
    scenario = json.loads((FIX/"enhancement_request.json").read_text())
    context,_,_ = make_runtime()
    env = context.build_envelope(scenario["work_item"])
    print(json.dumps(env,indent=2))

def cmd_simulate(decision: str):
    scenario = json.loads((FIX/"enhancement_request.json").read_text())
    context,human,orch = make_runtime()
    run = orch.start(scenario["work_item"],approver="platform_owner")
    action = human.actions[run["human_action_id"]]
    print("=== ARCHITECTURE RECOMMENDATION ===")
    print(json.dumps(run["recommendation"],indent=2))
    print("=== ADAPTIVE CARD ===")
    print(json.dumps(human.adaptive_card(action),indent=2))
    print("=== HUMAN DECISION ===")
    run = orch.resolve_architecture(run["run_id"],"platform_owner",decision,"CLI simulation")
    print(json.dumps({"state":run["state"],"status":run["status"]},indent=2))
    print("=== EVALS ===")
    print(json.dumps([
        evaluate_context(run["context_envelope"],scenario["expected_reuse_candidate"],scenario["expected_related"]),
        evaluate_recommendation(run,scenario["expected_reuse_candidate"])
    ],indent=2))

def cmd_quality(kind: str):
    from .code_review import StaticServiceNowReviewer
    from .atf_adapter import SyntheticATFAdapter
    from .quality_gate import QualityGate
    scenario=json.loads((FIX/"enhancement_request.json").read_text())
    rules=ROOT.parent/"config"/"quality"/"servicenow-static-review-rules.yaml"
    reviewer=StaticServiceNowReviewer(rules)
    atf=SyntheticATFAdapter(FIX/"atf_tests.json")
    gate=QualityGate(reviewer,atf)
    code=FIX/"code"/("good_script_include.js" if kind=="good" else "bad_business_rule.js")
    result=gate.run([str(code)],scenario["work_item"])
    print(json.dumps(result,indent=2))

def main():
    p=argparse.ArgumentParser()
    sp=p.add_subparsers(dest="cmd",required=True)
    sp.add_parser("context")
    sim=sp.add_parser("simulate")
    sim.add_argument("--decision",choices=["approve","request_changes","reject"],default="approve")
    q=sp.add_parser("quality")
    q.add_argument("--fixture",choices=["good","bad"],default="good")
    args=p.parse_args()
    if args.cmd=="context":
        cmd_context()
    elif args.cmd=="quality":
        cmd_quality(args.fixture)
    else:
        cmd_simulate(args.decision)

if __name__ == "__main__":
    main()
