from pathlib import Path
import json

files = list(Path("evals/golden-tasks").glob("*.json"))
if not files:
    raise SystemExit("No golden tasks found.")

required = {"id","name","role","prompt","success_criteria"}
for p in files:
    data = json.loads(p.read_text(encoding="utf-8"))
    missing = required - set(data)
    if missing:
        raise SystemExit(f"{p}: missing {sorted(missing)}")

print(f"Validated {len(files)} golden tasks.")
