from __future__ import annotations
from pathlib import Path
from typing import Dict, List
from .code_review import StaticServiceNowReviewer
from .atf_adapter import SyntheticATFAdapter

class QualityGate:
    def __init__(self, reviewer: StaticServiceNowReviewer, atf: SyntheticATFAdapter):
        self.reviewer=reviewer
        self.atf=atf

    def run(self, code_files: List[str], work_item: Dict) -> Dict:
        reviews=[self.reviewer.review_file(p) for p in code_files]
        blocker_findings=[
            f for r in reviews for f in r["findings"]
            if f["severity"] in {"BLOCKER","HIGH"}
        ]
        if blocker_findings:
            return {
                "status":"fail_review",
                "reviews":reviews,
                "tests":None,
                "human_action_required":False,
                "reason":"Resolve blocker/high deterministic findings before ATF."
            }

        coverage=self.atf.discover(work_item.get("acceptance_criteria",[]))
        test_ids=[tid for row in coverage["coverage_map"] for tid in row["test_ids"]]
        gaps=[row for row in coverage["coverage_map"] if row["coverage"]=="gap"]
        if gaps:
            return {
                "status":"blocked_test_gap",
                "reviews":reviews,
                "coverage":coverage,
                "tests":None,
                "human_action_required":True,
                "reason":"One or more acceptance criteria have no automated coverage in the reference adapter."
            }

        execution=self.atf.execute(test_ids,work_item.get("id","unknown"))
        return {
            "status":"pass" if execution["summary"]["status"]=="pass" else "fail_test",
            "reviews":reviews,
            "coverage":coverage,
            "tests":execution,
            "human_action_required":execution["summary"]["status"]!="pass"
        }
