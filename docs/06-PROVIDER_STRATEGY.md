# Provider Strategy

## Canonical Layer
Provider-neutral:
- `AGENTS.md`
- `agents/roles`
- `.agents/skills`
- schemas
- work packages
- evals

## Suggested Starting Roles
- Copilot: repository-native assistant / PR / GitHub workflows
- Claude Code: implementation / long-horizon codebase work / ServiceNow SDK experiments
- Codex: implementation and independent review
- Gemini: independent critique, test design, research

Rotate providers during evals. Do not hard-code one model as permanently best.

## Independence
Preferred:
Provider A builds → Provider B reviews → human decides.
