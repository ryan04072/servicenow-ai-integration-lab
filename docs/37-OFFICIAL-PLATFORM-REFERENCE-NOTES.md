# Official Platform Reference Notes

Validate these against current vendor documentation before implementation.

## GitHub Copilot custom agents

Current GitHub documentation describes repository custom agents as Markdown
agent profiles under `.github/agents/`, with YAML frontmatter. Agent profiles can
define description, tools, model/target in supported environments, and MCP server
configuration. Organization/enterprise agent promotion is also supported through
the relevant `.github` / `.github-private` repository structure.

## ServiceNow MCP Server Console — Zurich

ServiceNow documents MCP Server Console as the governed mechanism for external
MCP clients to access configured ServiceNow tools. Servers can expose bounded
capabilities and are connected to clients through OAuth/client authorization.

Current Zurich documentation includes tool categories such as REST API, Action,
Knowledge Graph, Subflow, and Now Assist skill; newer updates also document
Playbooks. Check exact patch/entitlement requirements before implementation.

## ServiceNow Build Agent

ServiceNow's guidance emphasizes:
- design before coding;
- explicit context in Markdown;
- precise ServiceNow terminology;
- early/frequent testing;
- ATF;
- version control;
- documented organizational standards.

## Azure DevOps history

Azure DevOps Analytics exposes historical work-item representations/revisions
suitable for deterministic trend and cycle-time analysis.

## Copilot Studio

Microsoft documents event-triggered agents and the ability to connect an agent to
an existing MCP server. Validate generative-orchestration, environment, licensing,
connection identity, and data-policy requirements before production use.

## Human approvals

Microsoft's Human in the loop connector can provide human input/approval in
supported agent/workflow scenarios. Treat preview features separately from
production architecture.
