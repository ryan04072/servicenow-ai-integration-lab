# Reference Architecture Context

This folder represents **how the platform should be designed**, distinct from
`context/platform/`, which represents **how the current instance is configured**.

Never merge the two concepts.

## Evidence categories

- approved internal standards;
- approved architecture decision records;
- official ServiceNow documentation for the applicable release;
- security requirements;
- upgrade/supportability requirements;
- licensing/entitlement constraints;
- validated internal patterns;
- deprecated/forbidden patterns.

## Decision pattern

```text
Current instance evidence
        +
Approved internal standards
        +
Authoritative platform guidance
        +
Requirement / constraints
        ↓
Options + tradeoffs
        ↓
Human architecture decision
```
