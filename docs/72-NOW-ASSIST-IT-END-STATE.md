# Now Assist for Internal IT — End State

## User experience

An authorized IT fulfiller opens the Now Assist panel and speaks in task language,
not product-feature language.

Examples:

```text
"Summarize this incident."
"Find similar incidents and relevant knowledge."
"Show me what's driving our VPN incident volume."
"Investigate the alerts related to this CI."
"Prepare a major incident status update."
"Run the approved user termination access-removal workflow."
"Draft a change based on the work we just completed."
```

## Behind the panel

```text
Natural-language intent
        ↓
ServiceNow orchestrator / agentic workflow routing
        ↓
┌──────────────┬───────────────┬───────────────┬───────────────┐
│ OOB ITSM     │ Platform      │ ITOM agents   │ Custom gap    │
│ skills       │ Analytics     │ / observability│ workflows     │
└──────────────┴───────────────┴───────────────┴───────────────┘
        ↓
Approved deterministic tools / platform actions
        ↓
Supervision based on risk
        ↓
Audit / analytics
```

## Agent catalog policy

Do not expose dozens of overlapping agents directly to users.

Group capabilities around jobs/outcomes.

Use dynamic orchestration/routing where appropriate and keep individual tools
well named and distinct.

## Recommended initial jobs

### Service Desk Copilot
- summarize;
- knowledge;
- similar work;
- resolution support;
- queue analytics.

### Operations Investigator
- alert/context investigation;
- CI/service impact;
- observability evidence;
- incident/change context.

### Platform Delivery Assistant
- sprint/delivery status;
- roadmap alignment;
- validation queues;
- executive brief.

### Identity Operations Assistant
- access investigation;
- supervised policy-bounded identity actions.

## Autonomy

Start user-invoked and supervised.
Automate triggers only after the workflow has demonstrated reliable results.
