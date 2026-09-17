# ServiceNow Authentication & Integration Checklist

## Outbound from ServiceNow

- [ ] Does target support OAuth 2.0?
- [ ] Does target have a stronger platform-specific application identity?
- [ ] Use Connection & Credential Alias.
- [ ] Keep credentials outside scripts/actions.
- [ ] Use environment-specific connection records.
- [ ] Confirm retry policy.
- [ ] Confirm TLS/network route/MID requirements.
- [ ] Confirm credential owner/rotation.

## Inbound REST to ServiceNow

For unattended backend access:

- [ ] Evaluate OAuth 2.0 client credentials.
- [ ] Use a dedicated application user where appropriate.
- [ ] Apply REST API Auth Scopes.
- [ ] Apply least-privileged roles/ACL access.
- [ ] Avoid `admin`.
- [ ] Test denied operations.

## External AI / MCP

- [ ] Use MCP Server Console for approved external AI context/actions.
- [ ] Create OAuth authorization per approved client.
- [ ] Expose only required servers/tools.
- [ ] Minimize tool inputs.
- [ ] Annotate/read-vs-write/destructive behavior where supported.
- [ ] Start in subproduction.
- [ ] Verify request tracing/audit.
- [ ] Keep production tools read-only initially.

## Basic Auth exception

- [ ] Target/source cannot reasonably support approved OAuth/application auth.
- [ ] Dedicated account is single-purpose.
- [ ] Noninteractive where possible.
- [ ] Least privilege.
- [ ] Password is vaulted/rotated.
- [ ] Exception owner and migration path documented.
