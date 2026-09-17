from __future__ import annotations
from typing import Dict, List, Optional
from .store import ArtifactStore
from .models import utc_now

class ContextService:
    def __init__(self, store: ArtifactStore):
        self.store = store

    def find_similar_artifacts(self, requirement: str, limit: int=5) -> List[Dict]:
        return self.store.search(requirement, limit=limit)

    def get_dependencies(self, artifact_id: str, depth: int=2) -> Dict:
        return self.store.neighbors(artifact_id, depth=depth)

    def build_envelope(self, work_item: Dict, task_type: str="servicenow_enhancement",
                       environment: str="synthetic") -> Dict:
        requirement = " ".join([
            work_item.get("title",""),
            work_item.get("description",""),
            " ".join(work_item.get("acceptance_criteria",[]))
        ])
        matches = self.find_similar_artifacts(requirement, limit=5)
        artifacts = []
        relationships = []
        ids = set()
        for m in matches:
            a = m["artifact"]
            if a["id"] not in ids:
                a = dict(a)
                a["retrieval_score"] = m["score"]
                artifacts.append(a)
                ids.add(a["id"])
            dep = self.get_dependencies(a["id"], depth=2)
            for node in dep["nodes"]:
                if node["id"] not in ids:
                    artifacts.append(node)
                    ids.add(node["id"])
            for edge in dep["edges"]:
                if edge not in relationships:
                    relationships.append(edge)

        standards = [a for a in artifacts if a["artifact_type"] == "architecture_doc"]
        tests = [a for a in artifacts if a["artifact_type"] == "atf_test"]

        facts = []
        if matches:
            facts.append(f"Found {len(matches)} directly relevant existing artifact candidate(s).")
        if tests:
            facts.append(f"Found {len(tests)} related test artifact(s).")
        if standards:
            facts.append(f"Found {len(standards)} relevant approved/reference standard artifact(s).")

        return {
            "task_id": work_item.get("id","unknown"),
            "task_type": task_type,
            "generated_at": utc_now(),
            "environment": environment,
            "requirement": work_item,
            "sources":[
                {"system":"servicenow","id":"synthetic-artifact-store","authority":"current_state","retrieved_at":utc_now()},
                {"system":"github","id":"synthetic-standard-store","authority":"approved_reference","retrieved_at":utc_now()}
            ],
            "artifacts": artifacts,
            "relationships": relationships,
            "standards": standards,
            "precedent": [],
            "delivery_context": [],
            "facts": facts,
            "constraints": ["Reference runtime uses synthetic data and read-only context."],
            "human_decisions": [],
            "unresolved_questions": [],
            "tool_permissions":{"read":True,"write":False},
            "confidence": round(sum(m["score"] for m in matches[:3]) / max(1,min(3,len(matches))), 4) if matches else 0
        }
