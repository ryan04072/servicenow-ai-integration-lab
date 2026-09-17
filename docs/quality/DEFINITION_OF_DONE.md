# Definition of Done — AI-Assisted ServiceNow Change

A change is not complete because an agent says "done."

## Required evidence

### Requirement
- acceptance criteria are explicit;
- unresolved material questions are closed or accepted.

### Context
- relevant current-state artifacts retrieved;
- dependency/blast-radius analysis performed;
- approved standards considered.

### Architecture
- decision recorded;
- material alternatives/tradeoffs captured;
- required human approval recorded.

### Implementation
- traceable changed artifacts;
- no unresolved blocker/high code review findings;
- deterministic scan evidence.

### Test
- acceptance criteria mapped to coverage;
- relevant regression tests run;
- ATF/result evidence retained;
- repeated failures escalated.

### Security / portability
- no embedded secrets;
- environment mappings identified;
- security-impacting changes reviewed.

### Delivery
- work item/PR/change traceability;
- UAT where required;
- release/rollback plan.

### Documentation
- technical as-built updated;
- fulfiller KB/QRG evaluated;
- operational runbook evaluated;
- decision record updated.

### Outcome
- post-release validation complete;
- telemetry/outcome measurement scheduled where material.

The orchestrator can automate evidence collection, but it cannot fabricate missing
evidence.


## AI-built change explainability

For material AI-built changes:
- [ ] AI Build Record exists
- [ ] GitHub technical as-built exists
- [ ] decision rationale exists for material architecture choices
- [ ] human decisions/clarifications are linked
- [ ] KB/QRG/CRG impact evaluated
- [ ] operational runbook impact evaluated
