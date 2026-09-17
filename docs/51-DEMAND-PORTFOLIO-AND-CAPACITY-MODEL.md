# Demand, Portfolio, and Capacity Model

## Intake does not equal backlog commitment

Use explicit states:

```text
Submitted
  ↓
Clarifying
  ↓
Evaluated
  ↓
Approved / Rejected / Duplicate
  ↓
Prioritized
  ↓
Planned
  ↓
Sprint Committed
  ↓
Delivered
```

## Work classifications

Use the approved enterprise/team model. Typical classes:

- roadmap;
- BAU;
- technical debt;
- compliance/security;
- expedite.

## Capacity

Define:
- roadmap target;
- BAU reserve;
- technical-debt capacity;
- expedite policy;
- WIP limits;
- validation/UAT capacity.

## AI role

AI may:
- summarize demand;
- find duplicates;
- map candidate roadmap themes;
- identify dependencies;
- calculate deterministic scoring inputs;
- surface aging/queue imbalance.

AI does not own:
- final priority;
- capacity allocation;
- sprint commitment;
- executive overrides.

## Portfolio review

At each sprint/period ask:

- Are we working on what we said matters?
- What displaced planned work?
- Where is capacity constrained?
- Which demand is aging without a decision?
- Which roadmap outcomes have no active work?
