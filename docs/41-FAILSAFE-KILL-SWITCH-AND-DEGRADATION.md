# Failsafe, Kill Switch, and Graceful Degradation

## Principle

The business process must continue when AI is unavailable.

AI is an accelerator/control layer, not a single point of failure.

## Required kill switches

Each production workflow should support at least one deterministic disable method:

- disable event trigger;
- disable agent workflow;
- remove/disable tool;
- revoke service identity permission;
- route all work to human triage.

Document the exact owner and action.

## Graceful degradation

### Intake
If AI fails:
- keep the request;
- mark it `AI Review Pending/Unavailable`;
- route to normal human triage.

### Executive brief
If AI fails:
- use source-system dashboards / human summary;
- do not delay the meeting.

### PR review
If AI fails:
- use standard human PR review.

### ServiceNow discovery
If MCP/tool fails:
- stop automated architecture conclusion;
- retrieve manually through approved methods.

## Circuit breaker

Repeated tool failures, authentication failures, malformed output, or unexpected
write attempts should pause the workflow rather than retry indefinitely.

## Recovery

After re-enable:
- process only safe queued work;
- prevent duplicate actions;
- preserve original correlation IDs.
