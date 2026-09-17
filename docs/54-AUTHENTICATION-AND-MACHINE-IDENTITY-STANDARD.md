# Authentication and Machine Identity Standard

## Purpose

Define a consistent enterprise preference order for unattended automation,
integrations, AI agents, MCP clients, CI/CD, and application-to-application access.

This document does **not** override enterprise Security/Identity policy.
It is the proposed platform-engineering standard to review with Security.

## Core principle

Use a dedicated **non-human workload/application identity** for unattended
automation.

A traditional user-style service account is acceptable only when the target
platform or enterprise control plane does not support a stronger workload identity.

## Decision order

Ask these questions in order:

1. Is a human actively using the integration?
2. Is the automation unattended?
3. Is the workload Azure-hosted?
4. Does the target platform provide an application-specific identity model?
5. Can long-lived secrets be avoided?
6. Can the identity be scoped to only the required repositories/projects/tools?
7. Can credentials be centrally rotated/revoked and audited?

## Preferred patterns

### Interactive human action

Prefer:

```text
Delegated OAuth / SSO
```

The action should execute with the user's identity and effective permissions
when the application is genuinely acting for that person.

### Azure-hosted unattended automation

Prefer:

```text
Managed Identity
```

when the target resource supports it.

Benefits:
- no stored client secret;
- short-lived tokens;
- lifecycle managed by Azure;
- centralized Entra governance.

### Non-Azure unattended Microsoft automation

Prefer:

```text
Microsoft Entra Service Principal
```

Authentication preference:

```text
Federated credential / workload identity
        ↓
Certificate credential
        ↓
Client secret
```

Use only the mechanisms supported by the source/target platform and approved
by enterprise Identity/Security.

### GitHub long-lived organization integration

Prefer:

```text
GitHub App
```

over a user PAT.

Use:
- minimum repository selection;
- minimum app permissions;
- installation access tokens for app-owned automation;
- user access tokens when the app is explicitly acting on behalf of a user.

### ServiceNow external AI access

Prefer:

```text
ServiceNow MCP Server Console
        +
OAuth client authorization
        +
bounded MCP tools
```

for approved external AI clients.

### ServiceNow API integrations

Prefer:

```text
OAuth 2.0
        +
Connection & Credential Alias
```

where the target/source supports OAuth.

For backend inbound access, use an approved client-credentials pattern with a
dedicated application user and REST API scopes as appropriate.

## Exception / fallback ladder

Use the strongest supported option.

```text
1. Managed identity / workload federation
2. Platform application identity
   - GitHub App
   - Entra service principal
3. OAuth 2.0 client credentials
4. OAuth 2.0 delegated user flow
   (when the action truly represents a user)
5. Short-lived/scoped API token
6. Fine-grained PAT
7. Dedicated user-style service account + token
8. Basic username/password
```

This is a decision aid, not a universal ranking. Platform-native mechanisms may
change the order.

Basic username/password should be a documented compatibility exception, not the
default for new cloud integrations.

## Required properties for every machine identity

- explicit owner;
- business/technical purpose;
- source system;
- target system;
- DEV/UAT/PROD scope;
- permissions;
- credential type;
- credential storage location;
- rotation/revocation method;
- expiration/review date;
- audit/logging location;
- emergency disable process;
- backup owner;
- security approval where required.

## Separation of duties

Do not create one omnipotent `svc_ai` identity.

Prefer bounded identities such as:

```text
sn-ado-intake-writer
sn-github-read-review
sn-mcp-engineering-read
sn-executive-brief-reader
```

or equivalent enterprise naming standards.

A logical AI agent should be separately traceable even when several agents
execute through the same approved service principal.

## No embedded secrets

Never store:
- PATs;
- client secrets;
- private keys;
- passwords;
- API keys

in:
- Git repositories;
- agent profiles;
- prompt files;
- source code;
- work item descriptions;
- logs.

Use approved credential stores and runtime connections.
