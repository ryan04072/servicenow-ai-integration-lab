import json, sys
from datetime import datetime, timezone
from pathlib import Path

if len(sys.argv) < 3:
    raise SystemExit('Usage: python scripts/new_work_package.py <ID> "<title>"')

work_id = sys.argv[1]
title = sys.argv[2]
root = Path("work-items") / work_id
root.mkdir(parents=True, exist_ok=True)

now = datetime.now(timezone.utc).isoformat()
package = {
    "id": work_id,
    "title": title,
    "state": "intake_received",
    "human_gate": False,
    "created_at": now,
    "updated_at": now,
    "links": {
        "servicenow_intake": None,
        "ado_work_item": None,
        "github_branch": None,
        "github_pr": None,
        "change_request": None,
        "release": None
    },
    "classifications": {
        "architecture_impact": "unknown",
        "integration_impact": "unknown",
        "code_impact": "unknown",
        "security_impact": "unknown",
        "documentation_impact": "unknown",
        "adr_required": "review"
    },
    "evidence": {
        "requirements": None,
        "architecture_review": None,
        "implementation_plan": None,
        "test_plan": None,
        "pr_review": None,
        "change_readiness": None,
        "release_manifest": None,
        "as_built": None
    },
    "history": [{
        "at": now,
        "event": "work_package_created",
        "details": {}
    }]
}

(root / "work-package.json").write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")

for name, heading in [
    ("requirements.md", "Requirements"),
    ("architecture-review.md", "Architecture Review"),
    ("implementation-plan.md", "Implementation Plan"),
    ("test-plan.md", "Test Plan"),
    ("pr-review.md", "PR Review"),
    ("change-readiness.md", "Change Readiness"),
    ("as-built.md", "As-Built"),
]:
    (root / name).write_text(
        f"# {heading} — {work_id}\n\nStatus: Draft\n\n",
        encoding="utf-8"
    )

print(f"Created {root}")
