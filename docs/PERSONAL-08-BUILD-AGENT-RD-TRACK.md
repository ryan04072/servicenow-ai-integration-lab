# Personal R&D — ServiceNow Build Agent Track

## Objective

Use ServiceNow Build Agent in the personal PDI as a **native R&D engineering
tool and benchmark**, precisely because it is not currently licensed in the work
enterprise environment.

The lab should answer:

> What could the ServiceNow-native approach do if we had it, and what portable
> ServiceNow artifacts can it produce today?

## Current separation

```text
PERSONAL PDI
Build Agent available for R&D
        ↓
prototype / build / test
        ↓
export ServiceNow-native artifact
        ↓
Promotion Reviewer
        ↓
Enterprise Candidate
        ↓
WORK DEV
normal SDLC

WORK
Build Agent itself is NOT assumed available
```

## PDI allowance

Current ServiceNow Australia-era PDI/trial material documents **25 free Build
Agent interactions per 30-day cycle**.

Treat this as:
- interactions/calls, not 25 guaranteed completed applications;
- a limited R&D budget;
- a product value that should be re-verified periodically.

## Use limited calls for evidence

Recommended emphasis:

```text
Build / modification benchmarks       ~60%
Repair / iteration                    ~20%
Testing / validation                  ~12%
Reserve / exploratory                 ~8%
```

Do not waste limited calls on basic documentation questions that can be answered
without invoking Build Agent.

## Primary experiments

1. Greenfield scoped app.
2. Catalog + Flow + approval.
3. Existing-artifact modification.
4. Employee Center UI/component.
5. ATF generation/repair.
6. Documentation.
7. Custom AI agent/tool where PDI entitlement supports it.
8. Update-set/application packaging.

## Capture

For every meaningful run:
- normalized requirement;
- acceptance criteria;
- starting state;
- prompt;
- interactions consumed;
- generated/changed artifacts;
- tests;
- human corrections;
- elapsed time;
- review findings;
- exported package;
- portability issues;
- final outcome.
