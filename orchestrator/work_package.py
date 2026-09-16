import json
from datetime import datetime, timezone
from pathlib import Path

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def load(path):
    path = Path(path)
    return json.loads(path.read_text(encoding="utf-8"))

def save(path, data):
    path = Path(path)
    data["updated_at"] = utc_now()
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

def append_history(data, event, details=None):
    data.setdefault("history", []).append({
        "at": utc_now(),
        "event": event,
        "details": details or {}
    })
