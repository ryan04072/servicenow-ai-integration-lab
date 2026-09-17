# Personal Mode

This repository is the **complete personal/home-lab edition** of the enterprise
AI & automation operating model.

It intentionally retains the architecture, agents, schemas, orchestration,
security concepts, evaluation patterns, and enterprise reference material so the
lab can teach production-grade thinking.

However, `personal_dev_lab` is the default operating mode.

## Personal mode precedence

When personal mode is active:

1. `config/personal-lab/lab-policy.yaml` controls lab autonomy.
2. Enterprise governance material under this repository is **reference material**,
   not a required approval workflow.
3. You may wear all organizational roles yourself.
4. Personal DEV writes can be automated.
5. Feature branches and PRs can be created automatically.
6. Destructive actions require confirmation and must stay inside disposable
   personal resources.
7. Employer data, credentials, internal URLs, private source code, and production
   environments are prohibited.
8. Keep source control, tests/evals, traces, rollback, and secret hygiene.

## Why retain the enterprise material?

Because the lab should teach both:

```text
How to build fast
        +
How this would need to be governed in an enterprise
```

The enterprise documents are there to compare against, not to slow down every
personal experiment.


## Enterprise simulation mode

The personal lab also includes an optional enterprise-simulation track.

Use it when you want to practice:
- AI Control Tower;
- Copilot discovery/reconciliation;
- AI asset lifecycle;
- ownership;
- risk classification;
- cost/value;
- incident/retirement motions.

These activities are **learning exercises**, not blockers for normal personal
experimentation.

See:
- `docs/PERSONAL-05-ENTERPRISE-SIMULATION-TRACK.md`
- `docs/PERSONAL-06-AI-CONTROL-TOWER-LAB-ROADMAP.md`

## Sandbox → Enterprise Candidate

Successful personal ServiceNow prototypes may graduate into a portable
**Enterprise Candidate**.

The lab may use unrestricted personal engineering tools to build the prototype.
The enterprise candidate contains the resulting ServiceNow-native artifacts,
tests, architecture, dependencies, portability notes, and provenance—not an
assumption that the personal toolchain is allowed or required at work.

See:
- `docs/PERSONAL-07-SANDBOX-TO-ENTERPRISE-CANDIDATE.md`
- `agents/roles/servicenow-promotion-reviewer.md`
- `labs/personal/LAB-09-SANDBOX-TO-ENTERPRISE-CANDIDATE.md`

## Build Agent R&D

ServiceNow Build Agent is an explicit native-tool learning track.

Use it alongside the open personal engineering sandbox, not instead of other
tools.

See:
- `docs/PERSONAL-08-BUILD-AGENT-RD-TRACK.md`
- `docs/PERSONAL-09-BUILD-AGENT-VENDOR-BENCHMARK.md`
- `docs/PERSONAL-10-LAB-APPROVAL-PATTERN.md`
