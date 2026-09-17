# Enterprise Runtime Constraints

This framework intentionally assumes the corporate workstation may block:

- local Git CLI;
- PowerShell;
- arbitrary shells;
- local package installation;
- local MCP servers;
- direct unmanaged API credentials.

These are implementation constraints, not architecture constraints.

## Runtime selection criteria

Choose enterprise-approved mechanisms that provide:
- authenticated read access;
- least privilege;
- audit logs;
- controllable write scope;
- human approval;
- service identity;
- secret storage;
- data-boundary compliance.

## Preferred rollout

1. Repository knowledge only.
2. Read-only live connectors.
3. Human-reviewed drafts.
4. Limited approved writes.
5. Higher autonomy only after eval evidence.

The role definitions and schemas should not change merely because the runtime changes.
