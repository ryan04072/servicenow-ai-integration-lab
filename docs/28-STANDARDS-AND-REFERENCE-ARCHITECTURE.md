# Standards and Reference Architecture

## The most important distinction

```text
CURRENT STATE ≠ BEST PRACTICE
```

The platform may contain legacy customization, vendor decisions, or temporary
patterns.

The architecture system must evaluate two parallel evidence sets:

### Current-state evidence
What is actually configured now?

### Reference / approved architecture
What should we prefer now?

## ServiceNow-specific design review

For material changes the Standards Guardian should evaluate:

- OOB capability;
- configuration option;
- extension/customization;
- data model;
- security;
- integration pattern;
- scope;
- upgrade impact;
- supportability;
- maintainability;
- observability;
- testability;
- licensing/entitlement;
- rollback.

## Build Agent alignment

When Build Agent is used:
- design before coding;
- give it explicit Markdown context;
- use precise ServiceNow terminology;
- review the plan;
- test early/often;
- use ATF where appropriate;
- use version control;
- maintain project standards/instructions.

Do not treat Build Agent as an architecture approval authority.

## Output contract

Every material architecture review should state:

```text
Requirement
Current State
Approved/Reference Standard
Gap
Options
Tradeoffs
Recommendation
Risk
Evidence
Human Decision
```
