# Enterprise AI Policy Integration

## Purpose

This repository does **not** replace the organization's existing AI policy.

It translates approved enterprise policy into implementation-level controls for
the ServiceNow agentic delivery operating model.

## Policy hierarchy

```text
Enterprise AI Policy
        ↓
Security / Privacy / Legal / Architecture Standards
        ↓
Platform Governance
        ↓
Repository Controls
        ↓
Agent / Tool Configuration
        ↓
Runtime Enforcement
```

If repository guidance conflicts with enterprise policy, enterprise policy wins.

## Map, do not duplicate

Populate:

```text
config/governance/ai-policy-map.template.yaml
```

Map each relevant policy requirement to:

- repository control;
- runtime control;
- human owner;
- evidence;
- review cadence.

## Example

```text
Policy requirement:
Sensitive data may only be processed by approved enterprise AI services.

Implementation:
- Tool registry marks data classification.
- Context Curator excludes prohibited sources.
- Runtime connection uses approved provider only.
- Run trace records provider/runtime.
- Production-readiness checklist verifies the control.
```

## Review triggers

Review the mapping when:
- enterprise AI policy changes;
- a model/provider changes;
- a new connector/tool is introduced;
- a new data class is used;
- autonomy level increases;
- the workflow is promoted to another team.
