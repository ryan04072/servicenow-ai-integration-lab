from __future__ import annotations
from typing import Dict, List

def evaluate_context(envelope: Dict, expected_reuse: str, expected_related: List[str]) -> Dict:
    ids = {a["id"] for a in envelope.get("artifacts",[])}
    reuse_ok = expected_reuse in ids
    related_hits = [x for x in expected_related if x in ids]
    coverage = len(related_hits) / max(1,len(expected_related))
    score = (1.0 if reuse_ok else 0.0) * 0.5 + coverage * 0.5
    return {
        "eval_id":"context-reuse-golden",
        "dimension":"context_retrieval",
        "status":"pass" if score >= 0.8 else "fail",
        "score":round(score,4),
        "evidence":[
            f"reuse_candidate_found={reuse_ok}",
            f"related_hits={len(related_hits)}/{len(expected_related)}"
        ],
        "notes":[]
    }

def evaluate_recommendation(run: Dict, expected_reuse: str) -> Dict:
    rec = run.get("recommendation") or {}
    ok = rec.get("type") == "extend_existing" and rec.get("artifact_id") == expected_reuse
    return {
        "eval_id":"architecture-reuse-golden",
        "dimension":"architecture_reuse",
        "status":"pass" if ok else "fail",
        "score":1.0 if ok else 0.0,
        "evidence":[f"recommendation={rec}"],
        "notes":[]
    }
