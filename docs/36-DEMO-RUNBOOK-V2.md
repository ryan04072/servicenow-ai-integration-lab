# Demo Runbook v2

## Demo objective

Show the operating model, not a magic autonomous bot.

Target: 7–10 minutes.

## 1. Problem

"We are running lean while delivery can come from internal staff, partners, and AI.
I want all of those contributors operating against one roadmap, SDLC, architecture
standard, and approval model."

## 2. Show the control plane

Open:
- `agents/roles/`
- `context/`
- `config/risk/`
- `config/tools/`

Explain:
"Agents are specialists. The policies and evidence contracts are the system."

## 3. Show current-state vs best-practice separation

Open:
- `context/platform/`
- `context/reference/`

Explain:
"The agent is not allowed to assume our current configuration is the target architecture."

## 4. Show adaptive intake

Open:
- `docs/27-INTAKE-FRONT-DOOR.md`
- `config/intake/persona-routing.yaml`

Explain:
"Business, IT, and technical requesters get different questions, but all produce
the same downstream work package."

## 5. Show autonomous pre-work

Open:
`config/orchestration/autonomous-intake-preapproval.pipeline.yaml`

Explain:
"The automation does the research and draft work before the human triage point."

## 6. Show progressive autonomy

Open:
`config/risk/risk-policy.yaml`

Explain:
"We start read-only, then human-reviewed drafts, then only bounded writes after
the system proves itself."

## 7. Show executive intelligence

Open:
- `config/orchestration/executive-brief.pipeline.yaml`
- `docs/30-HISTORICAL-DELIVERY-INTELLIGENCE.md`

Explain:
"This isn't just current status. It can identify flow trends and whether we're
actually executing the roadmap."

## 8. Close

"The same contracts can be reused by another enterprise team with a different
platform specialist and connectors. The operating model stays consistent."

## Demo boundary

Do not make Friday depend on live MCP or autonomous production connectivity.
The architecture and repo framework are enough for the first demo.
