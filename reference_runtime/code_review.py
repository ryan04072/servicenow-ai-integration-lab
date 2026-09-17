from __future__ import annotations
import re, yaml
from pathlib import Path
from typing import List, Dict

class StaticServiceNowReviewer:
    def __init__(self, rules_path: str | Path):
        cfg=yaml.safe_load(Path(rules_path).read_text(encoding="utf-8"))
        self.rules=cfg.get("rules",[])

    def review_text(self, text: str, artifact: str="unknown") -> Dict:
        findings=[]
        for rule in self.rules:
            flags=re.MULTILINE
            try:
                matches=list(re.finditer(rule["pattern"],text,flags))
            except re.error:
                continue
            for match in matches:
                findings.append({
                    "rule_id":rule["id"],
                    "severity":rule["severity"],
                    "artifact":artifact,
                    "message":rule["message"],
                    "line":text[:match.start()].count("\n")+1
                })
        blockers={"BLOCKER","HIGH"}
        status="FAIL" if any(f["severity"] in blockers for f in findings) else ("PASS_WITH_FINDINGS" if findings else "PASS")
        return {"status":status,"findings":findings}

    def review_file(self, path: str | Path) -> Dict:
        p=Path(path)
        return self.review_text(p.read_text(encoding="utf-8"),str(p))
