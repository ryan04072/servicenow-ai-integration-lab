# Personal R&D — Build Agent vs Echelon Benchmark

## Purpose

Generate independent evidence about native ServiceNow Build Agent capability that
can later inform an enterprise Echelon evaluation.

## Do not treat this as an enterprise tool bake-off

Build Agent is being exercised in a personal PDI.

Echelon should only be evaluated against an enterprise-approved sandbox/POC when
that opportunity exists.

The comparison therefore has two evidence streams:

```text
Personal R&D evidence
Build Agent
        +
Enterprise POC evidence
Echelon
        ↓
Normalized benchmark dataset
        ↓
Gap / overlap analysis
```

## Evidence labels

Every comparison point must be labeled:

- `observed_build_agent`
- `observed_echelon`
- `servicenow_documented`
- `echelon_vendor_claim`
- `not_tested`

Do not convert vendor claims into observed results.

## Key questions

- Which tool asks better scoping questions?
- Which understands the existing instance more deeply?
- Which reuses existing artifacts instead of duplicating?
- Which produces more supportable ServiceNow-native results?
- Which generates better ATF coverage?
- Which detects defects/security issues?
- Which documents as-built changes better?
- Which produces a cleaner promotion artifact?
- Which needs less human correction?
- Which handles UI/Employee Center better?
- Which handles integrations better?
- Which handles ongoing operations/remediation beyond story development?
- What is the cost per accepted story/capability?

## Strategic output

The benchmark should be able to support statements such as:

> "For workload X, the native PDI experiment demonstrated A/B/C. In the Echelon
> POC we observed D/E/F. The remaining gaps are G/H."

That is much stronger than:

> "Vendor X says it is better than product Y."
