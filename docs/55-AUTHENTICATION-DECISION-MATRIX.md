# Authentication Decision Matrix

Use this before creating any new integration or agent tool.

| Scenario | Preferred | Secondary | Exception / fallback |
|---|---|---|---|
| Human using app interactively | Delegated OAuth / SSO | Platform-native interactive auth | Avoid shared accounts |
| Azure-hosted workload → supported target | Managed identity | Service principal | Scoped token only if required |
| External/background app → Azure DevOps Services | Entra service principal | Managed identity if Azure-hosted | PAT only for temporary/legacy cases |
| Azure Pipeline automation | Service connection / workload identity federation | Service principal | PAT only when required |
| Long-lived GitHub org integration | GitHub App | Fine-grained PAT for constrained transitional case | User/service-account PAT only by exception |
| ServiceNow → OAuth-capable SaaS/API | OAuth 2.0 via Connection & Credential Alias | Platform-specific app auth | API key / Basic only when target requires |
| Backend client → ServiceNow REST | OAuth client credentials + scoped application user | Other approved OAuth flow | Basic only by exception |
| External AI client → ServiceNow | MCP Server Console + OAuth + bounded tools | Approved REST integration | Avoid broad admin API account |
| Power Automate mission-critical flow | Service principal application user where supported | Managed organizational owner pattern | Individual maker account only with documented lifecycle risk |
| Copilot Studio event trigger | Validate current product credential behavior and DLP | Use approved orchestration alternative if identity model is unacceptable | Do not silently accept author credentials for privileged production automation |
| Legacy target supports only API key | API key in approved credential store | — | Scope/rotate/monitor |
| Legacy target supports only Basic | Dedicated least-privileged service identity | — | Document exception and remediation path |

## Selection rule

Choose the first option that:
1. the platforms support;
2. Security approves;
3. provides sufficient least privilege;
4. is operationally supportable;
5. is auditable.

If the preferred mechanism is unsupported, document why and move down the
fallback path. Do not silently downgrade.
