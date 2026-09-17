# Event-Driven Delivery Orchestration

## Orchestration is a state machine

The orchestrator does not simply "call all agents."

It evaluates:

```text
current state
+ triggering event
+ available evidence
+ risk/policy
+ unresolved human actions
= allowed next transition
```

## Common triggers

```text
ServiceNow enhancement submitted
ADO work item changes state
GitHub PR opened/updated
test completed
approval resolved
deployment completed
scheduled portfolio review
human chat request
```

## Reference enhancement lifecycle

```text
SUBMITTED
  ↓
INTAKE
  ↓
CONTEXT_DISCOVERY
  ↓
ARCHITECTURE_DRAFT
  ↓
AWAITING_ARCHITECTURE_DECISION
  ├─ changes requested → ARCHITECTURE_DRAFT
  └─ approved
       ↓
BACKLOG_READY
       ↓
READY_FOR_DEVELOPMENT
       ↓
IMPLEMENTATION
       ↓
TECHNICAL_REVIEW
       ↓
VALIDATION
       ↓
UAT
       ↓
RELEASE_READY
       ↓
DEPLOYED
       ↓
POST_RELEASE_VALIDATION
       ↓
DOCUMENTATION
       ↓
COMPLETE
```

Any state can transition to:
- `WAITING_FOR_CLARIFICATION`;
- `BLOCKED`;
- `FAILED`;
- `CANCELLED`;

when policy permits.

## Idempotency

Every trigger carries:
- event ID;
- correlation ID;
- source record/version where possible.

Before executing a write, check whether the same event/action has already been
successfully processed.

## Retry

Retries are allowed only for known transient conditions.

After the configured retry budget is exhausted:
- create a Human Action;
- preserve error evidence;
- stop the affected branch;
- do not silently skip the failed step.

## Human resume

A human decision produces a new event:

```text
human_action.resolved
```

The orchestrator validates:
- action is still open;
- responder is authorized;
- decision matches allowed values;
- underlying record version is still current.

Then it resumes from the stored checkpoint.
