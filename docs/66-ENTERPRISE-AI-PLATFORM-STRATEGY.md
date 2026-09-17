# Enterprise AI Platform Strategy

## Goal

Use the best AI surface for each job without duplicating business logic across
Microsoft, ServiceNow, Salesforce, GitHub, and future platforms.

## Enterprise pattern

```text
                   ENTERPRISE AI EXPERIENCE LAYER
                         Microsoft 365 Copilot
                                 │
             ┌───────────────────┼───────────────────┐
             │                   │                   │
             ▼                   ▼                   ▼
      ServiceNow AI        Salesforce AI       GitHub Copilot
       Now Assist           Agentforce          Custom Agents
             │                   │                   │
             └───────────────────┼───────────────────┘
                                 ▼
                       SHARED CAPABILITY LAYER
              APIs / Flows / Subflows / Actions / MCP
                                 │
             ┌───────────────────┼───────────────────┐
             ▼                   ▼                   ▼
         ServiceNow         Identity / IGA        Salesforce
        workflows/data      Entra / Saviynt       workflows/data
                                 │
                                 ▼
                          SYSTEMS OF RECORD
```

## Core rule

**The conversational surface does not own the business capability.**

Build deterministic capabilities in the system that owns the process/data, then
expose them as governed tools to one or more AI experiences.

Examples:

```text
Terminate access
→ identity/IGA capability
→ exposed to Now Assist and/or Copilot

Create ServiceNow change
→ ServiceNow workflow capability
→ exposed to Now Assist and/or Copilot

Update Salesforce opportunity
→ Salesforce capability
→ exposed to Agentforce and/or Copilot
```

## Microsoft 365 Copilot

Treat as the broad enterprise assistant when:
- users live in Teams/Outlook/M365;
- Microsoft Graph context is important;
- the question spans multiple enterprise knowledge sources;
- the user should not have to navigate into a domain platform.

Do not assume synced/index connectors provide full transactional context.

## Platform-native AI

Use platform-native AI when:
- the platform is the system of record/action;
- platform metadata/security semantics matter;
- native workflows/actions/agents already exist;
- users perform the work inside the platform;
- auditability is strongest natively.

## Cross-platform agents

Use Copilot Studio or another approved orchestrator when:
- a single intent spans multiple systems;
- the workflow needs cross-platform approvals;
- no one platform clearly owns the entire transaction.

Even then, call shared platform capabilities rather than reimplementing them.
