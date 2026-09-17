# Safe Connection Implementation Pattern

## Goal

Move toward modern machine identities without accidentally weakening the current
enterprise security posture.

## Phase A — Design only

No new credentials.

Document:
- use case;
- source;
- target;
- read/write operations;
- environments;
- data classifications;
- preferred identity;
- fallback identity;
- required permissions.

Send the security review packet.

## Phase B — DEV read-only proof

After approval:

- create the lowest-risk identity;
- configure only DEV/nonproduction;
- permit read-only capability;
- test authentication;
- test authorization denial;
- test audit;
- test kill switch.

Do not add write merely because read succeeds.

## Phase C — DEV bounded write

Add only one explicit capability, for example:

```text
Create Azure DevOps draft work item
```

Do not grant broad project administration.

Test:
- valid write;
- denied write;
- duplicate retry;
- expired credential;
- revocation.

## Phase D — UAT / pilot

Repeat with production-like identity boundaries.

Use:
- human approval;
- real process owners;
- controlled data;
- run tracing.

## Phase E — production

Only after:
- Security/Identity approval;
- platform owner approval;
- data policy mapping;
- support/owner model;
- production readiness checklist;
- rollback/disable test.

## Fallback principle

If preferred auth cannot be implemented:

```text
Preferred identity fails/support unavailable
        ↓
Stop
        ↓
Document technical reason
        ↓
Select next approved fallback
        ↓
Reduce permissions/lifetime
        ↓
Add compensating controls
        ↓
Security approval
```

Do not silently swap OAuth for Basic or a PAT.

## Example fallback

Preferred:

```text
ServiceNow → Entra service principal → Azure DevOps
```

If enterprise constraints temporarily block the service-principal path:

```text
ServiceNow → dedicated service identity + minimal short-lived PAT → Azure DevOps
```

Compensating controls:
- smallest PAT scope;
- short expiration;
- vault storage;
- rotation owner;
- monitoring;
- explicit migration backlog item.
