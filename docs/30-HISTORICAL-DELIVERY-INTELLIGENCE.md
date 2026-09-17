# Historical Delivery Intelligence

## Objective

Use actual work-item history to learn how the delivery system behaves.

## Source

Use Azure DevOps Analytics/history/revisions where available, not a current-state
snapshot alone.

## Deterministic analytics first

Compute:
- cycle time;
- state/stage aging;
- blocked duration;
- validation age;
- carryover;
- post-start sprint scope change;
- rework/reopen;
- roadmap allocation;
- throughput.

Then let the Historical Delivery Analyst explain the patterns.

## Example management questions

- Is validation our system constraint?
- Are stories entering sprints before they are ready?
- Which work types have the most carryover?
- Does roadmap work get displaced by BAU during the sprint?
- Is vendor work spending more time in review/validation?
- Are weak acceptance criteria associated with rework?

## Governance

Trend analysis should improve the process, not become an opaque individual
productivity score.
