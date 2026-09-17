# Identity Management Agent — Reference Pattern

## Example use case

An authorized Identity Management analyst in the Now Assist panel says:

> "I need to remove Jane Doe from all security groups as part of an immediate termination."

## Important architecture principle

Do **not** make the LLM the identity-governance engine.

The agent interprets intent and gathers context.
The authoritative identity system and deterministic policy decide what can
actually be changed.

If Saviynt is the organization's IGA/orchestration layer, prefer invoking the
approved Saviynt capability rather than creating a parallel direct Entra group
removal path solely for AI.

## Recommended supervised design

```text
IdM analyst
    ↓
Now Assist Panel
    ↓
Identity Access Agent
    ↓
Validate invoker / role / workflow ACL
    ↓
Resolve target identity
    ↓
Retrieve governed access / group memberships
    ↓
Apply termination policy
    ↓
Generate exact proposed removal plan
    ↓
HUMAN CONFIRMATION
    ↓
Identity capability
(Saviynt / approved Entra automation)
    ↓
Verify resulting access
    ↓
Write audit result / task notes
```

## Agent responsibilities

- understand natural-language request;
- resolve user safely;
- retrieve current access;
- identify policy-governed vs exception access;
- explain actions;
- invoke only approved tools;
- verify outcome;
- escalate uncertainty.

## Agent must not

- guess which Jane Doe is intended;
- remove access outside approved scope;
- bypass IGA approval/governance;
- directly grant itself broader Entra permissions;
- treat "remove everything" as literal if policy has exceptions;
- hide failed removals.

## ServiceNow security

For user-invoked workflows:
- restrict discover/invoke ACLs to appropriate IdM roles;
- prefer dynamic-user execution where the action should respect the analyst's permissions;
- apply role masking;
- use supervised execution on sensitive tools.

For event-driven termination:
- evaluate dedicated AI/workload identity separately;
- limit its tools/permissions to the termination capability.

## Crawl / Walk / Run

### Crawl
Read-only:
- retrieve memberships;
- identify termination actions;
- draft checklist.

### Walk
Manual Now Assist invocation:
- propose exact removal plan;
- analyst approves;
- action runs through authoritative identity capability.

### Run
Authoritative termination event triggers workflow:
- agent gathers context;
- deterministic policy determines eligible removal;
- approval remains for exceptions/high-risk conditions.

### Mature
Fully autonomous only for clearly policy-bounded actions with deterministic
verification and exception routing.
