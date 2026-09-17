from __future__ import annotations
import json, uuid
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List

def now():
    return datetime.now(timezone.utc).isoformat()

class SyntheticATFAdapter:
    """Fixture-backed ATF adapter proving the contract/state behavior."""
    def __init__(self, tests_path: str | Path):
        self.tests_path=Path(tests_path)

    def discover(self, acceptance_criteria: List[str]) -> Dict:
        tests=json.loads(self.tests_path.read_text(encoding="utf-8"))
        mapping=[]
        for criterion in acceptance_criteria:
            hits=[t for t in tests if t.get("criterion")==criterion]
            mapping.append({
                "criterion":criterion,
                "coverage":"existing_automated" if hits else "gap",
                "test_ids":[t["id"] for t in hits]
            })
        return {"coverage_map":mapping,"tests":tests}

    def execute(self, test_ids: List[str], correlation_id: str) -> Dict:
        tests=json.loads(self.tests_path.read_text(encoding="utf-8"))
        selected=[t for t in tests if t["id"] in test_ids]
        passed=sum(1 for t in selected if t["status"]=="pass")
        failed=sum(1 for t in selected if t["status"]=="fail")
        return {
            "execution_id":"ATF-"+uuid.uuid4().hex[:10],
            "correlation_id":correlation_id,
            "environment":"synthetic_dev",
            "started_at":now(),
            "completed_at":now(),
            "summary":{"total":len(selected),"passed":passed,"failed":failed,"status":"pass" if failed==0 else "fail"},
            "results":selected
        }
