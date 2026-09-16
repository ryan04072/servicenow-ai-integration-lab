from pathlib import Path
import json, py_compile, sys

required = [
    "AGENTS.md",
    "README.md",
    "config/lifecycle/lifecycle.json",
    "config/providers/providers.example.json",
    "schemas/work-package.schema.json",
    "schemas/release-manifest.schema.json",
    "orchestrator/cli.py",
]

missing = [p for p in required if not Path(p).exists()]
if missing:
    print("Missing required files:")
    for p in missing:
        print(" -", p)
    raise SystemExit(1)

# Validate JSON
for p in Path("config").rglob("*.json"):
    json.loads(p.read_text(encoding="utf-8"))
for p in Path("schemas").rglob("*.json"):
    json.loads(p.read_text(encoding="utf-8"))

# Validate Python syntax
for root in ["orchestrator", "scripts"]:
    for p in Path(root).rglob("*.py"):
        if p.name == "validate_repo.py":
            continue
        py_compile.compile(str(p), doraise=True)

skills = list(Path(".agents/skills").glob("*/SKILL.md"))
roles = list(Path("agents/roles").glob("*.md"))
agents = list(Path(".github/agents").glob("*.agent.md"))

print("Repository foundation valid.")
print(f"Canonical roles: {len(roles)}")
print(f"Canonical skills: {len(skills)}")
print(f"GitHub agent adapters: {len(agents)}")
