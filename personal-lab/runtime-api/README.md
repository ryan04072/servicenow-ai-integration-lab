# Local Runtime API

Optional FastAPI wrapper over the dependency-light `reference_runtime`.

## Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r personal-lab/runtime-api/requirements.txt
python personal-lab/runtime-api/run.py
```

Then open:

```text
http://localhost:8080/docs
```

## Docker

```bash
docker compose -f docker-compose.agentic-lab.yml up --build
```

This starts with synthetic fixtures. Replace the fixture adapter with your PDI
adapter only after the local state machine/evals work.
