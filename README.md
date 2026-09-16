# ServiceNow Agentic Engineering Home Lab

A portable, professional-grade home lab for learning and demonstrating:

- ServiceNow administration, development, and architecture
- ServiceNow SDK / Fluent development
- Git / GitHub / pull-request workflows
- Azure DevOps planning integration
- AI-agent orchestration
- multi-provider engineering with GitHub Copilot, Claude Code, Codex, and Gemini
- risk-based testing and ATF planning
- DevOps Change Velocity / CAB evidence handoff
- release traceability and as-built documentation
- human-in-the-loop AI governance

## Repository Name

Recommended GitHub repository name:

```text
servicenow-agentic-engineering-lab
```

Recommended description:

> Multi-model ServiceNow engineering lab for agentic SDLC, SDK/Fluent development, GitHub/ADO orchestration, testing, change governance, and human-in-the-loop automation.

Keep the repository **private while building it**. Publish only sanitized portfolio projects later.

---

# Start Here

Read these in order:

1. [`docs/00-QUICKSTART.md`](docs/00-QUICKSTART.md)
2. [`docs/01-TARGET_ARCHITECTURE.md`](docs/01-TARGET_ARCHITECTURE.md)
3. [`docs/02-IMPLEMENTATION_ROADMAP.md`](docs/02-IMPLEMENTATION_ROADMAP.md)
4. [`docs/03-IMPLEMENTATION_RUNBOOK.md`](docs/03-IMPLEMENTATION_RUNBOOK.md)
5. [`docs/04-LIFECYCLE_AND_EVIDENCE_MODEL.md`](docs/04-LIFECYCLE_AND_EVIDENCE_MODEL.md)
6. [`docs/05-AGENT_CATALOG.md`](docs/05-AGENT_CATALOG.md)
7. [`docs/06-PROVIDER_STRATEGY.md`](docs/06-PROVIDER_STRATEGY.md)
8. [`docs/07-SERVICENOW_TOOLCHAIN.md`](docs/07-SERVICENOW_TOOLCHAIN.md)
9. [`docs/08-DEVOPS_CHANGE_VELOCITY.md`](docs/08-DEVOPS_CHANGE_VELOCITY.md)
10. [`docs/09-EVALUATION_STRATEGY.md`](docs/09-EVALUATION_STRATEGY.md)

Then run:

```bash
python scripts/validate_repo.py
python scripts/new_work_package.py LAB-001 "Build first scoped SDK app"
python -m orchestrator.cli status work-items/LAB-001/work-package.json
```

---

# What Already Exists in Your Home Environment

This starter assumes:

- your ServiceNow PDI is already integrated with GitHub,
- ServiceNow is already creating Azure DevOps work items/stories,
- VS Code is your primary local editor,
- you have GitHub Copilot,
- you have Claude Code,
- you have ChatGPT/Codex access,
- you have Gemini access.

This repository does not replace those integrations. It adds the control plane around them.

---

# Target Lifecycle

```text
ServiceNow Intake
    ↓
Azure DevOps work item
    ↓
AI intake / grooming
    ↓
Human requirement review
    ↓
Architecture agent
    ↓
Human architecture gate
    ↓
Implementation planning
    ↓
Code / ServiceNow native configuration
    ↓
GitHub branch + PR
    ↓
Code / PR review
    ↓
Automated + manual testing
    ↓
DevOps Change Velocity / change evidence
    ↓
CAB / human approval
    ↓
Scheduled / deployment
    ↓
Post-release validation
    ↓
As-built documentation PR
    ↓
Human merge
```

---

# Portable Architecture

The canonical, vendor-neutral layer is:

```text
AGENTS.md
agents/roles/
.agents/skills/
schemas/
config/
docs/
orchestrator/
evals/
```

Provider adapters are intentionally thin:

```text
.github/
.claude/
.gemini/
```

The engineering system should survive changing model vendors.

---

# Safety / Human-in-the-Loop

Even in a home lab:

- AI can analyze, plan, write code, create tests, and draft documentation.
- Human approval is required for architecture acceptance, destructive PDI changes, merge to main, credential changes, and final release acceptance.
- External/community skills are reviewed before they receive secrets or write permissions.
- Employer proprietary material must never be copied into this repository.
