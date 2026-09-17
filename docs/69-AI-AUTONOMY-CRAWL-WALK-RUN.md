# AI Autonomy — Crawl / Walk / Run

Use this sequence for every new agentic capability.

## Crawl — Assist

Human explicitly invokes AI.

AI can:
- retrieve context;
- summarize;
- recommend;
- draft;
- explain proposed actions.

No external write without the human performing/approving it.

Example:
IdM analyst asks:
> "Show me the user's current group memberships and recommend what should be removed."

## Walk — Supervised action

Human invokes AI; AI can execute bounded tools only after approval.

```text
User request
→ agent plan
→ show impacted access
→ HUMAN APPROVAL
→ deterministic tool executes
→ result/audit
```

Use ServiceNow supervised execution or equivalent runtime approval controls.

Example:
> "Remove Jordan from all access governed by the termination policy."

Agent identifies exact actions and requests approval before execution.

## Run — Event-driven supervised autonomy

An authoritative event starts the workflow automatically.

```text
Termination event
→ agent gathers context
→ policy evaluates scope
→ plan produced
→ approval if policy requires
→ deterministic action
→ validation
→ audit
```

## Advanced run — policy-bounded autonomy

Only after evidence, and only for low/known-risk actions.

```text
Authoritative event
→ deterministic policy confirms eligibility
→ agent performs contextual reasoning
→ bounded action executes
→ verification
→ exception escalation
```

High-risk exceptions still route to people.

## Promotion requirements

Before moving a capability to the next stage:
- eval accuracy established;
- identity/security approved;
- audit works;
- kill switch works;
- idempotency tested;
- failure recovery tested;
- human override works;
- business/process owner accepts the change.
