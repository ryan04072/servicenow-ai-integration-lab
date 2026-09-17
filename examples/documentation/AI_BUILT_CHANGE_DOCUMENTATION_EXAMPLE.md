# Example — AI-Built Enhancement Documentation Trail

## User story

> Add Adobe Creative Cloud access to the existing Employee Center access-request
> experience with approval and governed fulfillment.

## Discovery

The Context Service found:
- existing Application Access Request;
- common variable set;
- existing software-access fulfillment flow;
- identity orchestration integration;
- existing ATF.

## Best-practice validation

- reuse/extend existing capability before creating a duplicate request;
- preserve credential abstraction;
- keep environment mapping/configuration outside hard-coded scripts.

## Options

### A — New standalone Adobe request
Rejected because it duplicates the established access-request framework.

### B — Extend Application Access Request
Selected because the existing pattern satisfies most requirements and already
uses the approved fulfillment/integration pattern.

## Decision rationale

Extend the existing access-request framework with Adobe-specific configuration
and entitlement mapping.

This explanation is a concise decision rationale. It is not private model
chain-of-thought.

## Implementation

Changed:
- catalog configuration;
- entitlement mapping;
- reusable flow configuration;
- ATF coverage.

## Code/config annotation

Where code is required, comments explain non-obvious behavior:

```javascript
// Preserve the entitlement correlation key so callback retries update the
// existing fulfillment task rather than creating duplicate requests.
```

## Quality

- Code/Configuration Reviewer: PASS
- deterministic scan: PASS
- related ATF: PASS
- new Adobe path ATF: PASS
- UAT: pending/approved as applicable

## Documentation outputs

- GitHub: `docs/access/adobe-access-as-built.md`
- ADR: `docs/decisions/ADR-xxx-adobe-access.md`
- Fulfiller QRG: `KBxxxxxxx`
- Operational runbook: only if the support/recovery model changed
- AI Build Record: `BUILD-xxxx`
