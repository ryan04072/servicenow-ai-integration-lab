import json, unittest
from pathlib import Path

from reference_runtime.code_review import StaticServiceNowReviewer
from reference_runtime.atf_adapter import SyntheticATFAdapter
from reference_runtime.quality_gate import QualityGate
from reference_runtime.human_actions import HumanActionBroker
from reference_runtime.decision_record import create_decision_record

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent
FIX=ROOT/"fixtures"

class QualityAndDocumentationTests(unittest.TestCase):
    def setUp(self):
        self.scenario=json.loads((FIX/"enhancement_request.json").read_text())
        self.reviewer=StaticServiceNowReviewer(REPO/"config"/"quality"/"servicenow-static-review-rules.yaml")
        self.atf=SyntheticATFAdapter(FIX/"atf_tests.json")

    def test_bad_code_is_blocked_before_atf(self):
        gate=QualityGate(self.reviewer,self.atf)
        result=gate.run([str(FIX/"code"/"bad_business_rule.js")],self.scenario["work_item"])
        self.assertEqual(result["status"],"fail_review")
        ids={f["rule_id"] for r in result["reviews"] for f in r["findings"]}
        self.assertIn("SN-JS-002",ids)
        self.assertIn("SN-JS-004",ids)

    def test_good_code_runs_all_synthetic_atf(self):
        gate=QualityGate(self.reviewer,self.atf)
        result=gate.run([str(FIX/"code"/"good_script_include.js")],self.scenario["work_item"])
        self.assertEqual(result["status"],"pass",result)
        self.assertEqual(result["tests"]["summary"]["failed"],0)

    def test_free_text_expert_context_is_captured(self):
        human=HumanActionBroker()
        action=human.create_expert_context_request(
            "ADO-4821","Architecture context needed",
            "Which approval rule should govern this case?",
            ["platform_owner"],"servicenow","ADO-4821"
        )
        resolved=human.resolve(action.action_id,"platform_owner","provide_context",
                               "Use both approvals for net-new licensed access.")
        self.assertEqual(resolved.comment,"Use both approvals for net-new licensed access.")
        self.assertEqual(resolved.resume_event["event_type"],"human_action.resolved")

    def test_decision_record_captures_rationale_not_chain_of_thought(self):
        record=create_decision_record(
            "Choose implementation path",
            "Need correlation-aware monitoring intake.",
            [{"name":"Direct incident","pros":["simple"],"cons":["no native event lifecycle"],"evidence":["E1"]},
             {"name":"Event management","pros":["correlation"],"cons":["more components"],"evidence":["E2"]}],
            "Event management",
            "The requirement needs correlation and signal lifecycle before incident creation.",
            ["E1","E2"]
        )
        self.assertIn("correlation",record["rationale"].lower())
        self.assertIn("options",record)

if __name__=="__main__":
    unittest.main()
