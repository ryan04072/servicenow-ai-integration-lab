# Security Policy

Do not commit:
- ServiceNow credentials,
- Azure DevOps PATs,
- GitHub tokens,
- provider API keys,
- production/employer secrets.

If a secret is committed:
1. revoke/rotate it,
2. remove it from future history as appropriate,
3. investigate access,
4. update the relevant credential source.

Community skills/plugins must be reviewed before receiving secrets or write access.
