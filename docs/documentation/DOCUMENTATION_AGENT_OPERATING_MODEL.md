# Documentation Agent Operating Model

## Goal

AI-generated implementation is not complete until the appropriate audiences can
understand, support, and reproduce it.

Do not use one "documentation agent" to write every artifact.

## Specialists

### Markdown & GitHub Documentation Specialist
Canonical technical truth:
- architecture;
- as-built;
- ADRs;
- integration details;
- implementation details;
- test evidence;
- deep admin/developer runbooks.

### Fulfiller Knowledge Specialist
Operational ServiceNow Knowledge:
- Tier 1/Tier 2 support;
- fulfillment procedures;
- QRGs;
- Agent Assist / AI Search content;
- symptoms/basic checks/escalation.

### Operational Runbook Specialist
Platform operations:
- health checks;
- diagnostics;
- retry/recovery;
- kill switch;
- rollback;
- escalation.

### Decision & Rationale Recorder
Decision history:
- options;
- evidence;
- tradeoffs;
- chosen path;
- rejected alternatives;
- consequences;
- human input.

## Documentation router

```text
Change completed
      ↓
Documentation impact analysis
      ↓
      ├─ architecture/code changed → GitHub specialist
      ├─ fulfiller behavior changed → KB specialist
      ├─ support/recovery changed → runbook specialist
      └─ material design decision → decision recorder
```

Several specialists can run for the same change.

## Definition of done

A material change is not "documented" merely because an AI generated text.

Documentation is complete when:
- correct canonical location selected;
- source evidence linked;
- reviewed where required;
- version/implementation linked;
- stale predecessor identified;
- publication/update is traceable.
