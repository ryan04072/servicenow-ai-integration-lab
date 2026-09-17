from __future__ import annotations
import json
from pathlib import Path
from typing import Dict
from .models import utc_now

class JsonlTelemetry:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def emit(self, event_type: str, payload: Dict):
        row = {"timestamp":utc_now(),"event_type":event_type,**payload}
        with self.path.open("a",encoding="utf-8") as f:
            f.write(json.dumps(row, sort_keys=True) + "\n")
        return row
