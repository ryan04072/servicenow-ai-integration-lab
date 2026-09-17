# Copilot Studio / Power Automate Orchestration

## Role in this architecture

Use an approved Microsoft automation runtime for event-driven coordination and
human approval when that fits enterprise standards.

Do not assume it directly "runs GitHub custom agents." Treat GitHub agents and
Copilot Studio agents as separate runtimes consuming the same canonical policies.

## First autonomous workflow — intake pre-approval

```text
ServiceNow intake record created
          ↓
Event trigger / approved flow
          ↓
Load normalized intake
          ↓
Retrieve live context
  ├─ ServiceNow MCP
  ├─ Azure DevOps
  ├─ roadmap/standards
  └─ GitHub where relevant
          ↓
AI clarification / analysis
          ↓
Draft triage packet
          ↓
HUMAN APPROVAL / REQUEST INFO
          ↓
Approved action:
create/update backlog item
          ↓
Trace result
```

## Implementation steps

1. Choose the authoritative intake-created event.
2. Create a service-owned connection strategy.
3. Create/read the intake payload.
4. Invoke only read-only tools during the analysis stage.
5. Generate normalized structured output.
6. Create a human review/approval step.
7. On approval, execute the bounded write action.
8. Store the correlation ID and resulting work item ID.
9. Handle reject / request-more-info / timeout.
10. Test with synthetic requests before production.

## Executive brief workflow

Use a scheduled/event flow to gather data and create a **draft** brief.

Initial state:

```text
Generate → human review → send/discuss
```

Do not start with automatic leadership email distribution.

## Security warning

Event-driven agents/flows must use an explicitly designed connection/service
identity model. Validate whose credentials are used at runtime and what those
credentials can access.
