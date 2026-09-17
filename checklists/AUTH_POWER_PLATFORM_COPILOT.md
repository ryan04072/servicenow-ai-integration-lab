# Power Platform / Power Automate / Copilot Studio Checklist

## Power Automate

- [ ] Build production flows as solution-aware flows where appropriate.
- [ ] Use connection references instead of hard-coded connections where applicable.
- [ ] Keep environment-specific values in supported environment/configuration mechanisms.
- [ ] Evaluate service principal application user ownership for mission-critical flows.
- [ ] Verify connector-specific support for service principals.
- [ ] Document licensing/request-limit implications.
- [ ] Avoid permanent dependency on a single employee/maker account.
- [ ] Define DEV/Test/PROD promotion process.

## Copilot Studio

- [ ] Determine authentication model for each action/tool.
- [ ] Apply Power Platform DLP/data policies.
- [ ] Validate MCP server authentication.
- [ ] Review event-trigger credential behavior before production.
- [ ] If event triggers use maker/author credentials, review the risk explicitly.
- [ ] Do not allow a low-privilege user to indirectly exercise the maker's privileged connection.
- [ ] Prefer bounded actions/tools over general-purpose privileged connectors.
- [ ] Record Activity/run evidence.

## Autonomous workflow

- [ ] Analysis stage is read-only first.
- [ ] Human approval precedes external write during pilot.
- [ ] Service identity/ownership is durable.
- [ ] Kill switch is documented.
