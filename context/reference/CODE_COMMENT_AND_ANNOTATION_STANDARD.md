# Code Comment & Implementation Annotation Standard

## Goal

Make generated code understandable without turning every script into prose.

## Comments should explain

- **why** a non-obvious approach was chosen;
- ServiceNow platform nuance that would surprise a maintainer;
- correlation/idempotency assumptions;
- workarounds and their review trigger;
- security/authorization assumptions;
- unusual performance choices;
- environment/configuration dependency that is intentionally abstracted;
- link/reference to a material ADR when the design is not self-evident.

## Comments should not

- restate obvious syntax;
- preserve private AI reasoning;
- include credentials/secrets;
- copy the entire user story into source;
- become the only place where architecture is documented.

## Example

```javascript
// The external source can resend the same event. Correlation ID is used as the
// stable idempotency key so retries update existing work instead of duplicating it.
var existing = helper.findByCorrelationId(correlationId);
```

## Traceability annotation

For material reusable components, an implementation may include a short
non-sensitive reference such as:

```text
ADO-4821 / ADR-014
```

when that aligns with enterprise source-code conventions.

The canonical explanation remains in the AI Build Record / ADR / technical
as-built.
