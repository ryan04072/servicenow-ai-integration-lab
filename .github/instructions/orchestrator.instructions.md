---
applyTo: "orchestrator/**/*.py,config/lifecycle/**,schemas/**"
---
# Orchestration Code

The orchestrator is a control plane, not a super-agent.

- state transitions must be deterministic,
- provider routing must be explicit/configurable,
- evidence contracts must be machine-readable,
- human gates must fail closed,
- provider-specific logic belongs behind adapters.
