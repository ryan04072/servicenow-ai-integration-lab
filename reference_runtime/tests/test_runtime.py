import json, tempfile, unittest
from pathlib import Path

from reference_runtime.store import ArtifactStore
from reference_runtime.context_service import ContextService
from reference_runtime.human_actions import HumanActionBroker
from reference_runtime.telemetry import JsonlTelemetry
from reference_runtime.orchestrator import EnhancementOrchestrator
from reference_runtime.evals import evaluate_context, evaluate_recommendation

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "fixtures"

class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.scenario = json.loads((FIX/"enhancement_request.json").read_text())
        store = ArtifactStore.from_files(FIX/"artifacts.json", FIX/"edges.json")
        self.context = ContextService(store)

    def test_context_finds_reuse_and_dependencies(self):
        env = self.context.build_envelope(self.scenario["work_item"])
        result = evaluate_context(env,self.scenario["expected_reuse_candidate"],self.scenario["expected_related"])
        self.assertEqual(result["status"],"pass",result)

    def test_orchestrator_pauses_and_resumes(self):
        with tempfile.TemporaryDirectory() as td:
            human=HumanActionBroker()
            telemetry=JsonlTelemetry(Path(td)/"trace.jsonl")
            orch=EnhancementOrchestrator(self.context,human,telemetry)
            run=orch.start(self.scenario["work_item"],approver="platform_owner")
            self.assertEqual(run["state"],"AWAITING_ARCHITECTURE_DECISION")
            self.assertIn(run["human_action_id"],human.actions)
            result=evaluate_recommendation(run,self.scenario["expected_reuse_candidate"])
            self.assertEqual(result["status"],"pass",result)
            run=orch.resolve_architecture(run["run_id"],"platform_owner","approve","looks good")
            self.assertEqual(run["state"],"BACKLOG_READY")

    def test_unauthorized_responder_rejected(self):
        human=HumanActionBroker()
        action=human.create(
            "C1","approval","Test","Test",["owner"],"servicenow","REC1",["approve","reject"]
        )
        with self.assertRaises(PermissionError):
            human.resolve(action.action_id,"someone_else","approve")

if __name__ == "__main__":
    unittest.main()
