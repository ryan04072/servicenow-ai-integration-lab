# ServiceNow MCP Setup — Read-Only First

## Purpose

Use ServiceNow MCP Server Console as the governed boundary between external AI
clients and ServiceNow capabilities.

This is separate from ServiceNow SDK / Fluent:

- MCP = context/tool boundary for AI clients.
- SDK/Fluent = source-driven scoped application development.

Use both where appropriate.

## Phase A — prerequisites

- [ ] Confirm MCP Server Console is installed/available.
- [ ] Confirm roles/administration ownership.
- [ ] Confirm the current Zurich patch supports the desired tool categories.
- [ ] Decide which AI client will connect first.
- [ ] Define data/environment boundaries.
- [ ] Start in DEV/UAT or another subproduction context.

## Phase B — create bounded engineering-context server

Suggested logical server:

```text
ServiceNow Engineering Context
```

Do not expose broad admin capabilities.

Initial read-oriented tools should support only the context needed for:

- targeted configuration discovery;
- schema/table metadata;
- relevant records;
- approved architecture evidence;
- test/evidence lookup.

Tool implementations may use supported MCP tool categories such as approved REST
APIs, Actions, Subflows, Knowledge Graph, Now Assist skills, or Playbooks where
supported and appropriate.

## Phase C — OAuth/client authorization

- [ ] Create one client authorization/inbound OAuth integration per approved client.
- [ ] Use a dedicated identity where enterprise architecture requires it.
- [ ] Do not reuse interactive admin credentials as the long-term service model.
- [ ] Register the client/server in the enterprise tool registry.

## Phase D — tool annotations and safety

For each tool document:
- read-only / write;
- destructive potential;
- environment;
- exposed inputs;
- owner;
- data sensitivity;
- approval requirement.

Only expose the inputs the client needs.

## Phase E — test

- [ ] Test in-console where supported.
- [ ] Test from the approved client.
- [ ] Verify correct OAuth identity.
- [ ] Verify denied access is actually denied.
- [ ] Verify audit/request tracing.
- [ ] Verify no secret fields are returned.
- [ ] Verify the agent reports missing data rather than widening access.

## First useful capabilities

1. Look up relevant application/table metadata.
2. Discover a bounded set of configuration artifacts.
3. Retrieve evidence needed by the ServiceNow Architect.
4. Retrieve ATF/test evidence.
5. Retrieve deployment/change evidence where authorized.

## Do not start with

- unrestricted table API;
- arbitrary script execution;
- broad production writes;
- admin impersonation;
- write-capable tools merely because the protocol supports them.
