from __future__ import annotations
import json, re
from pathlib import Path
from typing import Iterable, List, Optional, Dict
from .models import Artifact, Edge

STOP = {
    "a","an","the","to","for","of","and","or","with","in","on","is","are","be",
    "new","create","add","request","service","servicenow"
}

def tokens(text: str) -> set[str]:
    vals = re.findall(r"[a-z0-9_]+", (text or "").lower())
    return {v for v in vals if len(v) > 1 and v not in STOP}

class ArtifactStore:
    def __init__(self, artifacts: Iterable[Artifact], edges: Iterable[Edge]):
        self.artifacts = {a.id: a for a in artifacts}
        self.edges = list(edges)

    @classmethod
    def from_files(cls, artifacts_path: str | Path, edges_path: str | Path):
        ar = json.loads(Path(artifacts_path).read_text(encoding="utf-8"))
        ed = json.loads(Path(edges_path).read_text(encoding="utf-8"))
        return cls([Artifact(**x) for x in ar], [Edge(**x) for x in ed])

    def get(self, artifact_id: str) -> Optional[Artifact]:
        return self.artifacts.get(artifact_id)

    def search(self, query: str, artifact_types: Optional[List[str]]=None, limit: int=10) -> List[Dict]:
        q = tokens(query)
        results = []
        for a in self.artifacts.values():
            if artifact_types and a.artifact_type not in artifact_types:
                continue
            doc = " ".join([a.name, a.summary, " ".join(a.tags)])
            t = tokens(doc)
            overlap = len(q & t)
            if not overlap:
                continue
            union = len(q | t) or 1
            jaccard = overlap / union
            name_bonus = 0.15 if q & tokens(a.name) else 0
            tag_bonus = 0.10 if q & set(a.tags) else 0
            score = min(1.0, jaccard + name_bonus + tag_bonus)
            results.append({"score": round(score, 4), "artifact": a.to_dict()})
        results.sort(key=lambda x: (-x["score"], x["artifact"]["name"]))
        return results[:limit]

    def neighbors(self, artifact_id: str, depth: int=1) -> Dict:
        seen = {artifact_id}
        frontier = {artifact_id}
        selected_edges = []
        for _ in range(max(0, depth)):
            nxt = set()
            for e in self.edges:
                if e.from_id in frontier or e.to_id in frontier:
                    if e.to_dict() not in selected_edges:
                        selected_edges.append(e.to_dict())
                    if e.from_id not in seen:
                        nxt.add(e.from_id)
                    if e.to_id not in seen:
                        nxt.add(e.to_id)
            seen |= nxt
            frontier = nxt
            if not frontier:
                break
        nodes = [self.artifacts[x].to_dict() for x in seen if x in self.artifacts]
        return {"nodes": nodes, "edges": selected_edges}
