# Internal IT Now Assist Blueprint

## Goal

Create a conversational IT cockpit inside ServiceNow that feels closer to a
general-purpose assistant while remaining grounded in ServiceNow context,
permissions, skills, analytics, and approved agentic workflows.

## Primary experience

```text
Service Operations Workspace
        ↓
Now Assist Panel
        ↓
Intent / orchestration
        │
        ├─ ITSM skills
        ├─ AI Search / RAG
        ├─ Platform Analytics
        ├─ ITOM agents
        ├─ custom Skill Kit skills
        └─ approved agentic workflows
```

Users should be able to ask in natural language rather than memorize feature names.

Examples:

- "Summarize this incident and tell me what we know so far."
- "Draft resolution notes from the work performed."
- "Are there similar recent incidents?"
- "What knowledge should I use?"
- "Show me open P1/P2 incidents by assignment group."
- "What changed in incident volume this month?"
- "What alerts are likely related to this outage?"
- "What are the biggest aging queues for the service desk?"

## Build principle

Start with OOB skills and agents.

Add custom capabilities only when:
1. the OOB capability cannot satisfy the requirement;
2. the gap is repeatable;
3. the data/tool boundary is understood;
4. the capability can be evaluated.

## Capability layers

### Layer 1 — Record assistance

ITSM:
- incident summarization;
- change summarization;
- chat summarization;
- resolution-note generation;
- knowledge drafting;
- recommended actions.

### Layer 2 — Knowledge and precedent

- AI Search / grounded Q&A;
- similar incidents/problems;
- approved KB;
- prior resolution context.

### Layer 3 — Analytics

- Analytics Q&A;
- Platform Analytics visualization generation;
- approved Performance Analytics indicators;
- trend/queue exploration.

### Layer 4 — ITOM

- alert analysis;
- impact investigation;
- observability-agent tools;
- CI/service reliability context;
- approved ITOM agentic workflows.

### Layer 5 — Action

Use AI agents/agentic workflows for bounded repeatable actions.

Examples:
- gather diagnostic context;
- draft problem candidate;
- prepare outage summary;
- identify knowledge gap;
- perform approved read-only investigation;
- create a human-reviewable action plan.

## Do not create one giant custom agent

Use the Now Assist Panel as the experience and let specialized native skills,
tools, and agentic workflows handle the work behind it.
