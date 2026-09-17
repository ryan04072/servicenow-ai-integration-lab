# AI Workload Placement — Personal Lab Edition

Do not optimize prematurely.

Use the platform that gives the experiment the best learning value.

## Default placement

### ServiceNow
Use for:
- ServiceNow data/configuration;
- ITSM/ITOM;
- Flow Designer;
- Now Assist;
- ServiceNow agents;
- ServiceNow MCP experiments.

### GitHub Copilot / coding agents
Use for:
- code;
- PRs;
- repo analysis;
- tests;
- docs.

### ChatGPT / Claude / Gemini
Use for:
- architecture comparison;
- independent review;
- research;
- reasoning;
- adversarial critique.

### Microsoft Copilot / Copilot Studio
Use for:
- Teams/M365 experience;
- Power Platform;
- cross-platform orchestration experiments.

### n8n / Python
Use for:
- provider-neutral orchestration;
- API experiments;
- deterministic glue;
- scheduled/event workflows.

## Rule

Do not build the same business capability independently in multiple AI platforms.

Build:

```text
Capability
→ tool/API
→ multiple agent surfaces
```

That lesson transfers directly to enterprise architecture.
