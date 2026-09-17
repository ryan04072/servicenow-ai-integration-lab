# Credential Storage and Secret Handling Standard

## Rule

Authentication architecture and secret storage are separate decisions.

Even a modern application identity can be implemented poorly if its secret is
embedded in code.

## Approved storage categories

Use enterprise-approved stores such as:
- ServiceNow Credentials / Connection & Credential Alias;
- approved external vault integration;
- Microsoft/Azure secret-management services;
- managed platform connections;
- GitHub encrypted secret mechanisms where appropriate.

Actual approved store is determined by enterprise Security.

## Never store secrets in

- Git;
- Markdown;
- Azure DevOps work items;
- comments;
- prompt text;
- agent configuration;
- logs;
- screenshots;
- email;
- Teams chat;
- source code.

## Prefer no secret when possible

Order of preference:

```text
Managed/federated identity
        ↓
Certificate/private-key mechanism with secure storage
        ↓
Client secret in approved vault
        ↓
Scoped token in approved vault
```

## Secret operational controls

- inventory;
- owner;
- purpose;
- last rotation;
- next rotation/expiry;
- revoke procedure;
- emergency owner;
- environment.
