# AI-Native ServiceNow Engineering Lifecycle

## Target operating model

```text
Human / event
    ↓
Intake
    ↓
Context Service + Dependency Graph
    ↓
ServiceNow Architect
    ↕
Expert Feedback via Teams when needed
    ↓
Architecture Human Gate
    ↓
Decision & Rationale Record
    ↓
Implementation Planner
    ↓
Builder
    ↓
ServiceNow Code Reviewer
    ↓
Static / Instance Scan
    ↓
ATF/Test Engineer
    ↓
    ┌──────────── fail ─────────────┐
    │                               ↓
    │                         Builder repair
    │                               ↓
    └──────────── re-review / retest
                  (bounded loop)
    ↓ pass
Human Technical Gate
    ↓
UAT
    ↓
Change / Release
    ↓
Post-release Validation
    ↓
Documentation Router
    ├─ GitHub technical/as-built
    ├─ Fulfiller KB/QRG
    ├─ Operational runbook
    └─ Decision/ADR update
    ↓
Telemetry / Outcome / Precedent
    ↓
Standards/Evals improvement proposal
```

## Human intervention

Humans should normally enter for:

- unresolved requirements;
- material architecture choices;
- security/identity exceptions;
- repeated quality/test failures;
- technical acceptance when required;
- UAT/business acceptance;
- production change/release authority;
- promotion of precedent into standards.

Everything else is eligible for automation when evidence supports it.

## "Manager of agents" experience

Your attention surface should show exceptions and decisions rather than every run.

Example:

```text
Architecture input needed       2
Architecture approval           1
Quality gate exception          1
PR review                       1
Waiting on business UAT         3
Running autonomously            7
Completed today                12
```

Teams can be the attention plane, while ServiceNow/ADO/GitHub remain authoritative
for their respective records.
