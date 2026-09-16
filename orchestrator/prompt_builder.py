from pathlib import Path

def build_prompt(work_package, role_name):
    role_path = Path("agents/roles") / f"{role_name}.md"
    if not role_path.exists():
        raise FileNotFoundError(f"Role not found: {role_path}")

    role = role_path.read_text(encoding="utf-8")
    return f"""# Agent Task

## Canonical Repository Rules
Read and follow `AGENTS.md`.

## Role
{role}

## Work Package
```json
{__import__('json').dumps(work_package, indent=2)}
```

## Instructions
- Use relevant skills from `.agents/skills/`.
- Ground conclusions in repository/PDI/ADO evidence available to you.
- Write structured evidence back to the work package area.
- Do not bypass human gates.
- If evidence is missing, return a blocked or needs-human result rather than inventing facts.
"""
