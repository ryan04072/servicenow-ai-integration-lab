# Reference Runtime

This directory is a runnable, dependency-light proof of the operating model.

It uses synthetic ServiceNow artifacts and implements:

- artifact/context retrieval;
- dependency graph expansion;
- Context Envelope assembly;
- enhancement state machine;
- Human Action Broker;
- Teams-style Adaptive Card rendering;
- telemetry;
- golden evals.

## Run

From the repository root:

```bash
python -m pip install -r reference_runtime/requirements.txt
python -m reference_runtime.cli context
python -m reference_runtime.cli simulate --decision approve
python -m unittest discover -s reference_runtime/tests -v
```

No external credentials are required.

## Important

This runtime is a **contract/reference implementation**.

Replace fixture-backed adapters with authorized enterprise/personal adapters
rather than embedding credentials or environment assumptions into agents.
