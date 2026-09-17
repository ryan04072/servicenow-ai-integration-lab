# Reliability, Idempotency, and Failure Handling

## Goal

Autonomous workflows must be safe under retries, timeouts, duplicate events, and partial failures.

## Correlation ID

Create one correlation ID at the start of a workflow and propagate it across:

```text
ServiceNow request
Azure DevOps work item
GitHub branch/PR
agent run
approval
change/release evidence
```

where supported.

## Idempotency

Before any external write:

1. identify the logical action;
2. derive/store an idempotency key;
3. check whether the action already succeeded;
4. retry only when safe.

Example:

```text
Create ADO story for intake REQ0012345
```

must not create three stories because the orchestration layer timed out after the
first successful API call.

## Retry policy

Differentiate:
- transient error;
- rate limit;
- authentication error;
- validation error;
- authorization failure;
- business rejection.

Do not retry permanent failures indefinitely.

## Partial failure

Example:

```text
ADO item created
→ trace update fails
```

Recovery should locate the already-created ADO item using correlation metadata
before attempting another create.

## Dead-letter / exception queue

Unresolved failures should enter a human-review queue with:
- correlation ID;
- failed step;
- source payload reference;
- error;
- retries;
- recommended recovery.
