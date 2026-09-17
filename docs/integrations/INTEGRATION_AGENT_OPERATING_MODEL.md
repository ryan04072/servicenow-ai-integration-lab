# Integration Agent Operating Model

## Example: "Connect ServiceNow to Microsoft Teams"

The Integration Agent should not immediately create a REST Message.

```text
Requirement
    ↓
Classify actual Teams outcome
    ↓
Current-instance discovery
    ↓
Product knowledge
    ↓
Capability Resolver
    ↓
Identity/authentication analysis
    ↓
Permission analysis
    ↓
Options
    ↓
Recommendation
    ↓
Human architecture/security decisions
    ↓
optional DEV implementation
```

## Step 1 — Clarify the Teams capability

"Teams integration" can mean:

- post message;
- Adaptive Card;
- approval/action response;
- chat;
- meeting/call;
- notification;
- Graph data access;
- bot/conversational experience;
- ServiceNow Virtual Agent / Teams integration;
- bidirectional work updates.

The requested outcome determines the API/app/spoke pattern.

## Step 2 — Inspect current environment

Search:

- installed Teams/Microsoft apps/spokes;
- existing IntegrationHub actions;
- existing app registrations;
- existing Connection & Credential Aliases;
- existing Teams flows;
- existing ServiceNow↔Microsoft patterns;
- tests;
- prior ADRs.

## Step 3 — Research official capability

Retrieve current official documentation and Store/app information.

Capture:

- release/version;
- supported operations;
- dependencies;
- entitlement/licensing;
- authentication requirements.

## Step 4 — Compare

```text
Existing approved integration
vs
OOB installed capability
vs
OOB capability not installed
vs
custom reusable action/spoke
vs
direct custom API/script
```

## Step 5 — Identity

Decide:

```text
human-present?
├─ yes → consider delegated/user-context
└─ no  → machine-to-machine/workload identity
```

Then determine the actual supported target-platform authorization pattern.

## Step 6 — Permissions

Derive exact ServiceNow and external-platform permissions from the operations
being performed.

## Step 7 — Reliability / support

Document correlation, retries, idempotency, timeouts, errors, monitoring,
kill switch, and ownership.

## Step 8 — Human decision

The Integration Agent may recommend.

Architecture/Security/Platform humans retain the approvals their processes
require.

## Step 9 — Implementation

After approval, the same specialist may implement in DEV through bounded tools,
then pass through Code Review, Instance Scan/static review, ATF/integration
tests, documentation, UAT, and normal release.
