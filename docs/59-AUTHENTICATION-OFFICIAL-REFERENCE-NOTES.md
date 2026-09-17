# Authentication Official Reference Notes

Validate these references during implementation because product capabilities and
enterprise policies change.

## GitHub

GitHub recommends GitHub Apps for long-lived organization integrations. GitHub
Apps provide fine-grained permissions, repository selection, and short-lived
tokens. Fine-grained PATs are preferable to classic PATs when a PAT is needed.

References:
- GitHub Docs — Deciding when to build a GitHub App
- GitHub Docs — Best practices for creating a GitHub App
- GitHub Docs — Managing personal access tokens

## Azure DevOps Services

Microsoft recommends:
- managed identity for Azure-hosted automation;
- service principal for unattended automation outside Azure;
- Azure DevOps service connections/workload identity for pipeline scenarios;
- PATs primarily for temporary/personal/legacy compatibility.

References:
- Microsoft Learn — Authentication guidance for Azure DevOps
- Microsoft Learn — Authentication methods for Azure DevOps integrations
- Microsoft Learn — Use service principals and managed identities in Azure DevOps

## Microsoft Entra service principals

When a service-principal credential is necessary, Microsoft recommends
certificates over client secrets where possible. Workload/managed identity can
avoid a stored secret entirely in supported scenarios.

Reference:
- Microsoft Learn — Securing service principals in Microsoft Entra ID

## ServiceNow Zurich

ServiceNow supports OAuth 2.0 credentials and Connection & Credential Aliases for
integration credential abstraction.

For backend inbound integrations, Zurich supports OAuth client credentials with
an OAuth Application User and REST API Auth Scope controls.

MCP Server Console uses OAuth client authorization to secure approved external
MCP clients and lets administrators expose bounded tools.

References:
- ServiceNow Docs — OAuth 2.0 credentials
- ServiceNow Docs — Client credentials grant workflow
- ServiceNow Docs — Add the OAuth Application User
- ServiceNow Docs — MCP Server Console
- ServiceNow Docs — Create an OAuth inbound integration for an MCP client

## Power Automate

Microsoft supports service principal application users owning/running flows.
Microsoft also recommends solution-aware flows, connection references, and
generic/environment-specific configuration practices for ALM.

References:
- Microsoft Learn — Support for service principal owned flows
- Microsoft Learn — Keep flow configuration generic
- Microsoft Learn — Benefits of solution-aware cloud flows

## Copilot Studio

Current event-trigger documentation states that event-trigger connectors use the
agent maker's credentials. Treat that behavior as a specific security-review
item before privileged production automation.

References:
- Microsoft Learn — Add an event trigger
- Microsoft Learn — Create/connect MCP servers in Copilot Studio
