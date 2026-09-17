# Personal Runtime Quickstart

## Fast path

```bash
python -m pip install -r reference_runtime/requirements.txt
python -m unittest discover -s reference_runtime/tests -v
python -m reference_runtime.cli simulate --decision approve
```

## Optional API

```bash
pip install -r personal-lab/runtime-api/requirements.txt
python personal-lab/runtime-api/run.py
```

or:

```bash
docker compose -f docker-compose.agentic-lab.yml up --build
```

## Then connect real lab systems

Recommended order:
1. ServiceNow PDI read adapter
2. personal GitHub read adapter
3. personal ADO read adapter
4. architect model
5. Teams/human-action experiment
6. bounded writes
7. Build Agent / Claude / Codex implementation benchmarks
