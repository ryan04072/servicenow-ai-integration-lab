# ServiceNow Automated Testing Strategy

## Test layers

Use the cheapest reliable layer that proves the behavior.

```text
Static / deterministic checks
        ↓
Unit-like server logic tests where practical
        ↓
ATF targeted functional tests
        ↓
ATF regression suite
        ↓
Integration verification
        ↓
Business UAT
```

## ATF Agent responsibilities

The Test Engineer should:

1. map every acceptance criterion to a test disposition:
   - existing automated coverage;
   - new automated coverage;
   - manual UAT;
   - not testable / rationale.
2. inspect dependency graph for regression scope.
3. reuse/extend existing tests before duplicating.
4. generate/propose new ATF.
5. execute approved tests in DEV.
6. collect result evidence.
7. classify failures.
8. initiate bounded repair loops for implementation defects.
9. stop/escalate ambiguous or repeated failures.

## Test evidence bundle

Capture:
- suite/test IDs;
- build/version;
- environment;
- started/completed;
- pass/fail/skip/error;
- failed step;
- screenshots/log references where available;
- repair attempt;
- final disposition;
- mapped acceptance criterion.

## Test data

Tests must:
- use synthetic/non-sensitive data;
- create identifiable test records;
- clean up when practical;
- avoid relying on uncontrolled personal/user records;
- avoid production except where an explicit production-safe validation pattern exists.

## Bounded autonomy

Default reference behavior:

```text
max automatic implementation-repair attempts = 2
```

After that:
- create Human Action;
- attach failure evidence;
- request a decision/investigation.
