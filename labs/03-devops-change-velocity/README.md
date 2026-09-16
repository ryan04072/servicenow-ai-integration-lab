# Lab 03 — DevOps Change Velocity Closed Loop

## Goal
Exercise the evidence chain:

```text
ADO Work Item
→ GitHub Branch/PR
→ CI/Test Evidence
→ ServiceNow DevOps Change Velocity
→ Change Approval
→ Deployment
→ Release Manifest
→ As-Built Documentation
```

Use ServiceNow's native DevOps Change Velocity capabilities wherever possible rather than recreating change-control logic in custom agents.

## Validate
- work item traceability,
- commits/PR association,
- test evidence,
- automatic change creation where configured,
- pipeline pause/resume behavior,
- change result,
- documentation update.
