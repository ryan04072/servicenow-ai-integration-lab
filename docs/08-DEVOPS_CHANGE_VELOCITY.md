# DevOps Change Velocity

## Principle
Do not custom-build a change-control agent when ServiceNow DevOps Change Velocity already provides the governed lifecycle you need.

Use native capabilities where available to:
- integrate planning/coding/orchestration tools,
- capture work items / commits / tests / artifacts,
- create change requests from the delivery pipeline,
- pause/resume execution based on approval,
- maintain audit evidence.

## Agent Role
`Change Prep` should check evidence completeness and prepare context.

It should not replace:
- ServiceNow Change Management,
- CAB,
- change approval policy,
- pipeline release gates.

## Lab Evidence Chain
```text
ADO Story
→ GitHub PR
→ Test/Build Evidence
→ ServiceNow Change
→ CAB
→ Scheduled/Implement
→ Deployment
→ Release Manifest
```
