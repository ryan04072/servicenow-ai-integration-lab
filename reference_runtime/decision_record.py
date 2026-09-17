from __future__ import annotations
from datetime import datetime, timezone
from typing import Dict, List
import uuid

def create_decision_record(title: str, context: str, options: List[Dict], decision: str,
                           rationale: str, evidence: List[str], human_inputs=None,
                           rejected_alternatives=None) -> Dict:
    return {
        "decision_id":"ADR-"+uuid.uuid4().hex[:8],
        "title":title,
        "status":"approved",
        "context":context,
        "options":options,
        "decision":decision,
        "rationale":rationale,
        "rejected_alternatives":rejected_alternatives or [],
        "assumptions":[],
        "uncertainty":[],
        "human_inputs":human_inputs or [],
        "consequences":[],
        "evidence":evidence,
        "requirement_refs":[],
        "artifact_refs":[],
        "test_refs":[],
        "review_trigger":None,
        "created_at":datetime.now(timezone.utc).isoformat(),
        "updated_at":None
    }
