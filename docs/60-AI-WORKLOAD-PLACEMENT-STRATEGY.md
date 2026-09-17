# AI Workload Placement Strategy

## Principle

Do not select an AI platform only because it is available or inexpensive.

Place the workload where the combination of:
- authoritative context;
- permissions;
- native actions;
- user experience;
- governance;
- cost;
- latency;
- maintainability

is strongest.

## Recommended placement

| Workload | Primary home | Why |
|---|---|---|
| Employee self-service for ServiceNow | Employee Center + Now Assist / Virtual Agent | Native knowledge, catalog, request/incident actions |
| IT fulfiller conversational assistant | Service Operations Workspace + Now Assist Panel | Native incident/change/problem/alert context and ServiceNow actions |
| ServiceNow analytics questions | Platform Analytics + Now Assist / Analytics Q&A | Native semantic/query layer over ServiceNow data |
| ITOM alert/impact investigation | Now Assist for ITOM / ITOM AI agents | Native alert, CI, observability and event context |
| Cross-M365 employee productivity | Microsoft 365 Copilot | Native Microsoft Graph/productivity context |
| Cross-platform orchestration | Copilot Studio / Power Automate or approved orchestrator | Eventing, workflow, connectors, approvals |
| Repository/code/PR assistance | GitHub Copilot custom agents | Native repository, PR and CI context |
| ServiceNow source-driven app development | ServiceNow Build Agent and/or SDK/Fluent | Native ServiceNow development lifecycle |
| AI governance | AI Control Tower + enterprise AI/security controls | Inventory, governance, model/tool oversight |

## Routing rule

Prefer **ServiceNow AI** when:
- ServiceNow is the authoritative system;
- the task requires ServiceNow record/configuration context;
- native ServiceNow actions or agentic workflows are needed;
- the user works primarily in ServiceNow.

Prefer **Microsoft Copilot** when:
- the question spans Microsoft 365 content and productivity tools;
- ServiceNow is supplementary context rather than the system of action;
- users should remain in Teams/Outlook/M365.

Prefer **GitHub Copilot** when:
- repository/source/PR context is primary.

Prefer an **orchestration runtime** when:
- an event must invoke multiple systems;
- human approval is required between steps;
- the flow must run without an interactive user.

## Important boundary

A search/index connector is not equivalent to full platform context.

For example, a Microsoft 365 ServiceNow connector can make selected ServiceNow
content searchable in Copilot, but it should not be assumed to represent all
ServiceNow tables, ACL semantics, comments, attachments, runtime configuration,
or native actions.

Use ServiceNow MCP/API/tools when deeper ServiceNow context or action is required.
