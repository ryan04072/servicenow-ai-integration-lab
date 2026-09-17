# Personal Lab — Full Agentic Runtime

## Goal

Turn the personal sandbox into a working R&D implementation of the enterprise
operating model.

Unlike the corporate workstation, the home lab can install dependencies and try
multiple runtimes.

## Reference stack

```text
ServiceNow PDI
Azure DevOps personal org
GitHub
optional Microsoft tenant / Teams
        │
        ▼
Local Context + Orchestration Runtime
Python / FastAPI
        │
        ├─ ServiceNow adapter
        ├─ ADO adapter
        ├─ GitHub adapter
        ├─ local/mock adapter
        └─ Teams/human-action adapter
```

You are free to add:
- Docker;
- PostgreSQL/pgvector;
- Redis;
- n8n;
- OpenTelemetry;
- MCP SDKs;
- agent frameworks;
- multiple model providers.

The logical contracts should stay stable.

## Recommended build order

1. Run the fixture runtime.
2. Connect read-only to PDI.
3. Build artifact inventory.
4. Resolve deterministic dependencies.
5. Add GitHub/ADO reads.
6. Build Context Envelope.
7. Add one LLM architect.
8. Add Teams/personal approval transport.
9. Add bounded writes.
10. Add more agents only when a measured gap appears.
