# AI Agent Placement Matrix

Use this matrix before building a new custom agent.

| Decision factor | ServiceNow Now Assist / AI Agent | Microsoft Copilot Studio / M365 Copilot | Salesforce Agentforce | GitHub Copilot |
|---|---|---|---|---|
| Primary system context | ServiceNow records, metadata, KB, workflows, CMDB/ITOM | Microsoft Graph, M365, connected enterprise sources | Salesforce CRM metadata/data/workflows, Data 360 | Repositories, code, PRs, CI |
| Best user surface | ServiceNow workspace / EC / VA | Teams, Outlook, M365 Copilot, custom agent surfaces | Salesforce UI/channels | GitHub / IDE |
| Native transactional actions | ServiceNow flows, subflows, actions, record operations, skills | Connectors, workflows, MCP tools, APIs | Flow, Apex, Agentforce actions | Repo/PR/code tools |
| Native permission semantics | ServiceNow ACL/roles + agent identity/role masking | Entra/Power Platform connector identity/DLP | Salesforce permissions/agent user/trust controls | GitHub repo/org permissions |
| Best for platform-specific reasoning | Strong | Depends on connector/tool depth | Strong | Strong for engineering |
| Best for cross-M365 productivity | Limited | Strong | Limited | Limited |
| Best for ServiceNow ITSM/ITOM action | Strong | Use ServiceNow tool/MCP rather than duplicate logic | Poor fit | Poor fit |
| Best for CRM action | Poor fit | Cross-platform orchestration possible | Strong | Poor fit |
| Best for code/PR workflows | Limited | General orchestration | Limited | Strong |
| Cross-platform orchestration | Via integrations/MCP; best when SN is process owner | Strong | Via MuleSoft/MCP/APIs | Not primary orchestration runtime |
| Cost basis | ServiceNow entitlement/assist/contract dependent | M365/Copilot Studio licensing/consumption dependent | Salesforce licensing/consumption dependent | GitHub licensing/usage dependent |

## Placement decision

### Choose ServiceNow when
- ServiceNow owns the record/process;
- the agent needs deep ACL-aware ServiceNow context;
- an OOB ServiceNow agent/skill exists;
- the action should appear in Now Assist/Workspace;
- ITSM/ITOM/CMDB semantics matter.

### Choose Copilot Studio when
- the user should stay in Teams/M365;
- the agent needs Graph plus multiple business systems;
- it is mainly a cross-platform orchestrator;
- ServiceNow can be exposed as a governed tool.

### Choose Agentforce when
- Salesforce owns the CRM/customer process;
- Salesforce Flow/Apex/actions are the execution layer;
- Data 360/Salesforce metadata are central.

### Choose GitHub Copilot when
- code, repository evidence, PRs, reviews, or CI are central.

## Tie breaker

When two platforms could do the same job:

1. Choose the system of record/action.
2. Reuse an existing OOB capability before building custom.
3. Prefer the surface where the primary user works.
4. Prefer the design with the stronger permission/audit model.
5. Compare total cost per successful outcome.
6. Expose the resulting capability to the other AI rather than duplicating it.
