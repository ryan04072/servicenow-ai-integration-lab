# Internal IT AI Capability Roadmap

## Phase 0 — Inventory and entitlements

- [ ] Inventory installed Now Assist/AI applications.
- [ ] Inventory available OOB skills.
- [ ] Inventory available OOB AI agents/agentic workflows.
- [ ] Inventory ITOM agents and observability integrations.
- [ ] Confirm Now Assist Panel availability in SOW.
- [ ] Confirm Platform Analytics / Analytics Q&A capabilities.
- [ ] Confirm AI Data Explorer entitlement/version.
- [ ] Confirm AI Control Tower coverage.
- [ ] Identify unused entitlements before building custom agents.

## Phase 1 — Fulfiller cockpit

Goal: make Now Assist useful every day for service desk/IT fulfillers.

Enable/validate:
- incident summarization;
- change summarization;
- resolution-note generation;
- knowledge generation;
- recommended actions;
- AI Search;
- contextual Now Assist Panel.

Measure:
- adoption;
- assist usage;
- time saved;
- correction rate.

## Phase 2 — Trusted analytics foundation

- [ ] Build KPI catalog.
- [ ] Certify top executive/service-desk metrics.
- [ ] Define owners.
- [ ] Validate Platform Analytics dashboards.
- [ ] Resolve known data-quality disagreements.
- [ ] Train users on metric definitions.

## Phase 3 — Conversational analytics

- [ ] Validate Analytics Q&A.
- [ ] Validate Query Generation supported tables/facts.
- [ ] Enable visualization generation in Now Assist Panel.
- [ ] Test executive questions.
- [ ] Test assignment-group/service-level questions.
- [ ] Evaluate AI Data Explorer.

## Phase 4 — IT operations intelligence

- [ ] Expand Now Assist for ITOM.
- [ ] Validate alert analysis.
- [ ] Validate impact/investigation workflows.
- [ ] Review observability-agent integrations.
- [ ] Review ITOM MCP capabilities if available in deployed patch/app version.
- [ ] Correlate incidents, alerts, CIs and services where source data supports it.

## Phase 5 — Custom agents only for proven gaps

Candidates:
- Service Desk Queue Analyst;
- Major Incident Briefing workflow;
- Problem Candidate / recurrence analysis;
- Knowledge Gap workflow;
- Platform Delivery Executive Brief;
- Service Health investigator.

For each:
- requirement;
- OOB gap;
- context/tools;
- output schema;
- human gate;
- evals;
- owner.

## Phase 6 — Cross-platform orchestration

Use Microsoft/Copilot Studio or another approved orchestrator only where the
workflow genuinely spans systems.

Example:

```text
Teams / Copilot
     ↓
Cross-platform intent
     ↓
Copilot Studio
     ├─ Microsoft context
     └─ ServiceNow MCP
              ↓
        ServiceNow action
```

## Phase 7 — Executive IT intelligence

Create a leadership experience built on certified metrics:

```text
Platform Analytics / PA
        +
ITOM / CMDB / incidents / changes
        +
delivery metrics
        ↓
Executive narrative / visualizations
        ↓
decisions / actions
```
