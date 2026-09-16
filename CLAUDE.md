# Claude Code Adapter

Read `AGENTS.md` first.

Use:
- canonical roles from `agents/roles/`,
- canonical skills from `.agents/skills/`,
- structured work packages from `work-items/`.

Use subagents for meaningful isolated workstreams, not trivial tasks.

For ServiceNow SDK / Fluent:
- inspect the project SDK configuration,
- use installed ServiceNow/Fluent skills where available,
- validate metadata support before generating it,
- run build/lint/test validation before declaring success.

Do not bypass human gates defined in `AGENTS.md`.
