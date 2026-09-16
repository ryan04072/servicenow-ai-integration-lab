# Lab 04 — Local Orchestrator

## Goal
Use the included Python state machine to coordinate work packages.

Try:

```bash
python scripts/new_work_package.py LAB-004 "Orchestrator smoke test"
python -m orchestrator.cli status work-items/LAB-004/work-package.json
python -m orchestrator.cli dispatch work-items/LAB-004/work-package.json
```

Manual dispatch produces a prompt under `runs/`.

After reviewing agent output, advance the state explicitly.

The orchestrator must never silently cross human gates.
