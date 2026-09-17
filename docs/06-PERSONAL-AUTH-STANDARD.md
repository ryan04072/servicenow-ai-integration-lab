# Personal Authentication Standard

## Goal

Follow good habits without spending a week creating enterprise identity architecture
for every disposable lab.

## Preferred personal-lab order

### GitHub

Prototype:
- fine-grained PAT is acceptable;
- shortest practical lifetime;
- only required repos/scopes.

Mature reusable integration:
- GitHub App.

### Azure DevOps

Prototype:
- scoped personal PAT is acceptable.

Mature automation:
- Entra service principal / managed identity when the runtime makes that useful.

### ServiceNow PDI

Use:
- OAuth when learning OAuth is part of the experiment;
- personal integration user/basic credentials can be acceptable for a PDI-only
  disposable experiment if securely stored.

Do not use broad credentials in public code.

### External APIs

Prefer:
- OAuth/application credentials;
- API keys only in `.env`, vault, platform secret store, or connection records.

## Rules

- no secrets in Git;
- no employer credentials;
- no production credentials;
- rotate/revoke after abandoned experiments;
- use separate credentials for public demos where practical.
