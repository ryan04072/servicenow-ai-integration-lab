# ServiceNow Engineering Standards — Review Baseline

Status: REFERENCE BASELINE — tailor and formally approve for the enterprise.
Owner: ServiceNow Platform Owner / Architecture
Review cadence: at least each major platform/release standard review.

## Core principles

- OOB/configuration before customization when requirements permit.
- Reuse approved capabilities before creating parallel implementations.
- Keep business rules deterministic; do not hide policy in prompts.
- Prefer small cohesive reusable server logic.
- Parameterize environment-specific configuration.
- Treat credentials/secrets as managed platform credentials, never code/config text.
- Design for upgradeability, security, observability, rollback, and support.
- Preserve traceability requirement → architecture → implementation → test → release.

## JavaScript / server logic

### Required / preferred
- use descriptive names;
- keep functions small enough to understand/test;
- favor reusable Script Includes for shared server logic;
- constrain GlideRecord queries intentionally;
- use aggregation/query APIs appropriate to the operation;
- handle null/missing values and integration failures;
- make event/integration handlers idempotent where duplicate delivery is possible;
- log useful correlation identifiers without sensitive data;
- document non-obvious platform behavior.

### Review carefully
- queries inside loops;
- large unbounded table scans;
- synchronous work in latency-sensitive transactions;
- current.update()/recursive Business Rule patterns;
- broad updateMultiple/deleteMultiple operations;
- dynamic evaluation;
- direct manipulation that bypasses intended platform APIs/security;
- duplicate logic already available elsewhere;
- cross-scope calls;
- code that assumes a specific instance/sys_id/user/group.

## Client logic / UX

- avoid synchronous client/server interactions;
- keep authoritative validation server-side;
- use supported client/server interfaces;
- avoid duplicating server business logic;
- follow accessibility and responsive-design expectations;
- do not hard-code environment-specific values.

## Integrations

- use connection/credential abstractions;
- define timeout/retry behavior;
- use correlation/idempotency keys when appropriate;
- distinguish retryable vs terminal failure;
- protect secrets and sensitive payloads;
- produce actionable errors;
- document ownership and dependency.

## Security

Explicit review required for:
- ACL changes;
- role/elevated privilege changes;
- Scripted REST APIs;
- cross-scope access;
- impersonation/delegation;
- sensitive data;
- destructive/bulk operations.

## Testing

- changed behavior must map to acceptance criteria;
- reuse regression tests for affected dependencies;
- add ATF where stable/valuable;
- cover negative/failure behavior;
- test integrations with safe non-production endpoints/stubs where appropriate;
- preserve test evidence with the change.

## Documentation

Every material change answers:
- what changed;
- why;
- dependencies;
- how tested;
- how to support;
- how to disable/rollback;
- where canonical documentation lives.
