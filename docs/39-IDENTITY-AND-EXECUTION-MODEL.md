# Identity and Execution Model

## Objective

Every autonomous or semi-autonomous action must have an explicit execution identity.

Do not allow "the AI" to become an unnamed security principal.

## Identity classes

### Human identity
Interactive user acting directly.

### Service identity
Non-human identity used by an approved workflow or integration.

### Agent identity
Logical agent identity used for traceability. It may execute through a service
identity but must still be recorded separately in the run trace.

### Vendor identity
Third-party human/service identity with explicit scope and expiry.

## Required attributes

For every runtime/tool connection document:

- identity name;
- identity type;
- owner;
- system;
- environments;
- roles/permissions;
- credential storage;
- rotation process;
- expiry/review date;
- allowed operations;
- prohibited operations;
- audit location;
- offboarding process.

## Environment separation

Prefer separate identities or explicitly isolated credentials for:

```text
DEV
UAT
PROD
```

Do not let a development agent inherit production access simply because one
integration account can technically reach both.

## Service ownership

A workflow must not depend permanently on a single employee's interactive account.

Before production:
- assign a durable service owner;
- assign a backup owner;
- document credential rotation;
- document offboarding;
- test denied permissions.
