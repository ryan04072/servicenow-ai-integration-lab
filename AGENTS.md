# Portable Agent Instructions

This repository is a personal ServiceNow engineering lab intended to model professional enterprise practices.

## Core Principles

Before material recommendations or edits:

1. inspect existing repository guidance,
2. locate applicable architecture, ADRs, skills, and project context,
3. reuse existing components where appropriate,
4. distinguish verified facts from assumptions,
5. prefer ServiceNow OOB before customization,
6. prefer configuration before code,
7. preserve maintainability, upgradeability, and security,
8. define testing and validation,
9. keep changes reviewable,
10. preserve human approval gates.

Never invent ServiceNow:
- tables,
- fields,
- roles,
- APIs,
- plugins,
- system properties,
- licensing,
- product behavior.

When uncertain, state what must be validated in the PDI or official documentation.

## Canonical Repository Areas

- `agents/roles/` — provider-neutral specialist role definitions
- `.agents/skills/` — provider-neutral reusable expertise
- `orchestrator/` — lifecycle routing and structured handoffs
- `schemas/` — machine-readable contracts between agents/stages
- `config/` — lifecycle/provider/MCP configuration
- `work-items/` — lab work-package evidence
- `labs/` — focused learning exercises
- `projects/` — end-to-end project implementations
- `evals/` — golden tasks and agent evaluations
- `docs/` — architecture and operating model

## Human Gates

Require explicit human approval before:
- final architecture acceptance,
- destructive PDI actions,
- secret/credential changes,
- merge to main,
- publication of a repository,
- promotion of an external skill to canonical,
- final release acceptance.

## Learning Requirement

For meaningful implementation, explain:
- why the design was chosen,
- what OOB options were considered,
- what was changed,
- what was tested,
- what remains uncertain.

Do not optimize only for speed if doing so removes the learning value.
