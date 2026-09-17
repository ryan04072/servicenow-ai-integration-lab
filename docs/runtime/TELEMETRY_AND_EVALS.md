# Agent Runtime Telemetry & Evals

## Every run should be traceable

Minimum trace:

```text
run_id
correlation_id
trigger
state transitions
agents invoked
context sources
tool calls
human actions
approvals
outputs
errors/retries
resulting artifacts
elapsed time
consumption/cost where available
```

## Operational metrics

Track:
- completion rate;
- blocked rate;
- human-intervention rate;
- retry rate;
- tool failure rate;
- average time in each state;
- time waiting for human;
- context freshness;
- stale/unknown dependency rate.

## Quality metrics

Track:
- accepted vs rejected recommendations;
- architecture-review corrections;
- duplicate-build avoidance;
- reuse recommendations accepted;
- ATF/test pass rate;
- escaped defects;
- documentation completeness.

## Context quality eval

A golden task can assert:

> Given requirement X, did the Context Service find existing catalog item Y,
> flow Z, and integration Q?

This isolates retrieval quality from model reasoning quality.

## Agent quality eval

Given a known Context Envelope:
- did the architect identify reuse?
- did it avoid known anti-patterns?
- did it request human clarification when evidence was missing?
- did it cite the correct evidence?

## Tool quality eval

For deterministic tools:
- correct output;
- no unauthorized side effects;
- idempotent replay;
- expected failure behavior.

## Human-action quality

Measure:
- actionable-card clarity;
- wrong-recipient rate;
- approval turnaround;
- duplicate notification rate;
- actions resolved without opening source system;
- overrides / corrections.

## Executive interpretation

Do not equate:
- agent activity with value;
- generated hours with hard-dollar savings;
- low human intervention with high quality.

Measure accepted outcomes.
