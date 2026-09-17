# Evidence-First / Anti-Hallucination Policy

## Principle

The model is a reasoning engine, not the source of truth.

For architecture and implementation decisions:

```text
RETRIEVE
→ VERIFY
→ REASON
→ CITE EVIDENCE
→ ACT
```

not:

```text
REMEMBER
→ ASSUME
→ BUILD
```

## Claims requiring evidence

The following may not be asserted from model memory alone:

- a ServiceNow spoke/app/feature exists;
- a capability is available in a particular release;
- a capability is licensed/entitled;
- an app/plugin is installed;
- an action/subflow/tool exists;
- an API is supported;
- a role/permission is required;
- a capability is deprecated;
- an existing enterprise artifact already implements the requirement;
- an integration endpoint/auth pattern is approved.

## Evidence classes

### A — Live executable evidence
Target-instance metadata/configuration.

### B — Official product evidence
ServiceNow Docs / Store / Developer docs for the applicable release/version.

### C — Approved internal reference
Architecture standards, ADRs, catalogs, approved documentation.

### D — Delivery history
ADO/GitHub/change/test evidence.

### E — Human fact/decision
Explicitly supplied, attributable input.

### F — Model analysis
Derived reasoning only.

Architecture recommendations should normally include A/B/C evidence where relevant.

## Insufficient evidence behavior

If a material recommendation depends on an unverified capability:

```text
status = INSUFFICIENT_EVIDENCE
```

Then either:
- retrieve another source;
- refresh the source;
- ask a human;
- present the option as unverified.

Do not fabricate.

## Product vs environment

Always distinguish:

```text
Product supports X
```

from:

```text
Our enterprise can use X
```

The second requires environment evidence.

## Release/version awareness

Official product evidence must capture:
- ServiceNow family/release;
- Store app version if applicable;
- retrieval date.

If evidence applies to a different release, label the mismatch explicitly.

## Citation behavior

Architecture output should identify the evidence used for each material claim.

A recommendation with no supporting evidence is lower confidence and must not be
presented as established fact.
