# Merge Guide — v2

Recommended branch:

```text
feature/enterprise-agentic-operating-model-v2
```

This package is additive. Extract at the existing repository root and review
conflicts before committing.

## 1. Add canonical roles

Copy new files from:

```text
agents/roles/
```

Do not replace existing role files unless intentionally updating them.

## 2. Add GitHub custom-agent adapters

Copy:

```text
.github/agents/
```

The v2 adapters use current GitHub custom-agent profile conventions:
YAML frontmatter plus a Markdown instruction body.

Tool names and MCP server tool IDs are environment-specific; configure those
after enterprise tool approval.

## 3. Add context and policy configuration

Copy:

```text
context/
config/context/
config/tools/
config/risk/
config/intake/
config/analytics/
config/orchestration/
schemas/
```

## 4. Add runbooks

Copy `docs/22-*` through `docs/36-*`.

## 5. Update AGENTS.md

Append:

```markdown
## Enterprise agentic operating model

For enterprise delivery tasks:

1. Load `context/README.md`.
2. Load `config/context/source-authority.yaml`.
3. Load `config/risk/risk-policy.yaml`.
4. Build a context envelope before material recommendations.
5. Use the Standards Guardian when platform/configuration decisions are involved.
6. Treat current-state instance configuration and reference architecture as separate evidence.
7. Preserve source identifiers and freshness.
8. Follow the configured human approval gates.
9. Record material agent decisions and tool activity in the run trace.
```

## 6. Update .github/copilot-instructions.md

Incorporate:

```markdown
### Enterprise context
Do not rely on model memory for company-specific facts.
Use approved repository context and live tools when available.

### ServiceNow design
For ServiceNow architecture or implementation:
- compare current state with approved standards and official platform guidance;
- prefer OOB/configuration before customization where requirements permit;
- identify security, upgrade, supportability, and maintainability impact;
- require evidence for claims about existing configuration;
- test early and use ATF where appropriate.

### Risk
Never bypass configured human gates.
Production changes and security-sensitive actions require explicit human approval.
```

## 7. Commit

Suggested commit:

```text
Add v2 enterprise agentic operating model and progressive autonomy
```

## 8. Do not connect write-capable tools yet

Finish Phase 0–2 in the implementation runbook first.


# v2.1 Operational Controls

Also copy:

```text
config/governance/
config/reliability/
config/communications/
checklists/AI_POLICY_MAPPING.md
checklists/IDENTITY_AND_ACCESS_READINESS.md
checklists/PRODUCTION_READINESS.md
checklists/RELIABILITY_TESTS.md
docs/38-* through docs/53-*
```

Before production autonomy, the existing enterprise AI policy must be mapped to
these implementation controls. Do not substitute repository guidance for formal
enterprise policy.


# v2.2 Authentication/Security Addendum

Also copy:

```text
config/security/
checklists/AUTH_*.md
checklists/NEW_INTEGRATION_SECURITY_GATE.md
templates/SECURITY_*.md
templates/SECURITY_ARCHITECTURE_INTAKE.yaml
templates/AUTHENTICATION_DECISION_RECORD.md
docs/54-* through docs/59-*
```

Treat `config/security/authentication-standard.yaml` as **proposed for Security
review** until the enterprise Identity/Security owners approve or modify it.


# v2.3 AI Placement Addendum

Also copy:

```text
docs/60-* through docs/65-*
checklists/AI_WORKLOAD_PLACEMENT.md
checklists/NOW_ASSIST_INTERNAL_IT_SETUP.md
context/analytics/
.agents/skills/analytics-trust/
.agents/skills/ai-workload-routing/
templates/AI_USE_CASE_PLACEMENT_RECORD.md
```

No new agent personas are introduced in v2.3. These capabilities are added as
shared skills, context, and experience architecture.


# v2.4 Enterprise AI Portfolio Addendum

Also copy:

```text
docs/66-* through docs/72-*
checklists/CROSS_PLATFORM_AGENT_DESIGN.md
context/ai-capabilities/
```

Before creating any new custom agent, check the AI capability registry and agent
registry for an existing reusable capability or overlapping agent.
