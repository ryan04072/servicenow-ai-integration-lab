# Implementation Sequence — From Repository to Working Pilot

## Phase 0 — Reference runtime

Run the included synthetic example locally/CI.

Success:
- context query finds existing artifacts;
- dependency graph expands relationships;
- Context Envelope is generated;
- orchestrator pauses for architecture approval;
- Teams-style Adaptive Card is rendered;
- human decision resumes the run;
- trace/eval output is recorded.

## Phase 1 — Read-only ServiceNow context

Implement approved read-only adapters.

Start with a small artifact inventory:
- catalog items;
- flows/subflows;
- Script Includes / Business Rules;
- tables/fields;
- integrations;
- ATF;
- approved architecture docs.

Do not begin with unrestricted arbitrary table access.

## Phase 2 — Dependency graph

Create deterministic discovered edges first.

Examples:
- catalog → flow;
- flow → subflow/action;
- script → table;
- integration → alias;
- ATF → covered artifact.

Add inferred relationships only after evidence labeling is implemented.

## Phase 3 — ADO + GitHub context

Read-only:
- work item;
- related/prior items;
- repo docs;
- PR/commit evidence.

Assemble a real cross-system Context Envelope.

## Phase 4 — Architecture pilot

Trigger from one synthetic or noncritical enhancement.

Agent output:
- current state;
- reusable artifacts;
- standard;
- options;
- recommendation;
- evidence.

Human approves architecture manually.

## Phase 5 — Human Action Broker / Teams

Create actionable cards for:
- clarification;
- architecture approval;
- exceptions.

Write the decision back to the authoritative record and emit resume event.

## Phase 6 — Bounded writes

Enable one write at a time:
1. create/update ADO story;
2. update a ServiceNow delivery record;
3. create GitHub PR/branch if approved.

Every write requires idempotency and traceability.

## Phase 7 — Validation / observability

Add:
- golden retrieval tests;
- agent evals;
- run traces;
- human-action metrics;
- failure/retry dashboards.

## Phase 8 — Expand workloads

Only after evidence:
- implementation planning;
- automated review;
- test generation;
- release evidence;
- documentation drift;
- operations/remediation.

## Pilot success criteria

A pilot is successful when it reliably:

1. receives an enhancement;
2. finds relevant existing ServiceNow artifacts;
3. explains reuse vs new build;
4. pauses for a real human decision;
5. resumes correctly;
6. creates traceable delivery outputs;
7. can be replayed/audited.
