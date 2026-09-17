# Human Action Broker — Teams Attention Plane

## Problem

Agentic delivery fails operationally if humans must monitor every execution log,
ADO board, ServiceNow queue, and GitHub repository to discover when AI needs help.

The Human Action Broker converts agent pauses into clear human work.

## Action classes

### Clarification
The system is missing a fact.

Examples:
- which population?
- which approval model?
- which existing pattern should be followed?

### Approval
The system knows the proposed action but a human must authorize it.

Examples:
- architecture approval;
- promotion/adoption approval;
- release/deployment approval where applicable.

### Exception
Automation failed or confidence fell below policy.

Examples:
- access failure;
- dependency conflict;
- repeated tool failure;
- stale context.

### Review
A human must inspect a specialist artifact.

Examples:
- PR review;
- security finding;
- complex technical review.

### FYI
No action is required. Prefer digesting these.

## Teams design

Teams is the **attention surface**, not necessarily the system of record.

```text
Agent/orchestrator pauses
        ↓
Human Action record created
        ↓
routing policy chooses person/channel
        ↓
Adaptive Card sent to Teams
        ↓
Approve / Reject / Request Changes / Add Context / Retry
        ↓
Broker validates response
        ↓
authoritative system updated
        ↓
human_action.resolved event
        ↓
orchestrator resumes
```

## Card requirements

Every actionable card should show:
- what is waiting;
- why it paused;
- requested action;
- recommendation when appropriate;
- evidence summary;
- risk/impact;
- source record;
- age/due time;
- `Open Details` link/identifier.

Do not put secrets or sensitive payloads in a Teams card.

## Authoritative decision examples

| Decision | Authoritative record |
|---|---|
| ServiceNow architecture gate | ServiceNow approval / architecture record |
| requirement clarification | enhancement/intake record |
| ADO prioritization | Azure DevOps work item |
| code approval | GitHub PR review |
| production change | ServiceNow Change |
| agent exception | orchestration/human-action record + relevant incident/task |

## Routing

Suggested default:
- FYI → digest;
- clarification → direct Teams card;
- approval → actionable direct Teams card;
- exception → direct Teams card, escalate based on severity;
- critical production failure → existing operational incident/escalation process.

## Multi-person support

The action schema supports:
- one approver;
- any-of group;
- all-of group;
- ordered approval;
- informational participants.

Do not infer organizational approval authority from chat membership.
