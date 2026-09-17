# Reference Scenario — New ServiceNow Enhancement

## Request

```text
Adobe Creative Cloud Access

Create an Employee Center request with manager approval and automated access
provisioning. Status must return to ServiceNow and the implementation needs
automated test coverage.
```

## 1. Trigger

The enhancement catalog request or ADO state change emits:

```text
enhancement.submitted
```

The orchestrator creates a correlation/run ID.

## 2. Intake

Intake confirms:
- target users;
- business outcome;
- required approval;
- expected fulfillment;
- acceptance criteria.

If a material answer is missing:

```text
WAITING_FOR_CLARIFICATION
→ Human Action Broker
→ Teams Adaptive Card
```

## 3. Context discovery

The Context Service searches current-state artifacts.

In the included synthetic fixture it finds:

```text
Application Access Request
  ├─ uses → Access Request Common Variables
  └─ triggers → Software Access Fulfillment
                   └─ invokes → Identity Orchestrator Integration

ATF - Application Access Request
  └─ covers → Application Access Request

Catalog Reuse Standard
  └─ governs → Application Access Request
```

## 4. Context Envelope

The architecture agent receives:
- normalized story;
- the catalog item;
- variables;
- flow;
- integration;
- test;
- approved reuse standard;
- evidence/relationship data.

It does **not** receive only the story description.

## 5. Architecture

The reference runtime produces:

```text
Recommendation:
Extend the existing Application Access Request pattern rather than create a
duplicate standalone implementation.
```

A real architecture agent would add:
- exact proposed extension;
- environment mappings;
- security implications;
- test plan;
- rollback;
- unresolved decisions.

## 6. Human gate

The orchestrator enters:

```text
AWAITING_ARCHITECTURE_DECISION
```

The Human Action Broker creates an approval and renders a Teams Adaptive Card.

You can:
- Approve
- Request Changes
- Reject
- Add comments

The authoritative decision is written to the ServiceNow/delivery record.

## 7. Resume

Approve:

```text
human_action.resolved
→ BACKLOG_READY
```

Request changes:

```text
human_action.resolved
→ ARCHITECTURE_DRAFT
```

Reject:

```text
human_action.resolved
→ CANCELLED
```

## 8. Delivery

After approval:
- ADO story/tasks can be created/updated;
- implementation planning runs;
- the approved enterprise build mechanism performs the work;
- review/test/UAT/release continue through the existing SDLC.

## 9. Telemetry

The runtime records:
- states;
- context retrieved;
- human action;
- decision;
- recommendation;
- errors;
- timing.

Golden evals verify that the context service found the expected reuse pattern
before evaluating model quality.

## Run it

```bash
python -m reference_runtime.cli simulate --decision approve
```
