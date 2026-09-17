# Personal Lab Approval Pattern

## Why use a real approval?

If the purpose is to learn enterprise workflow mechanics, manually setting:

```text
approval = approved
```

skips the most useful parts:
- approver record;
- approval reason;
- approval history;
- audit trail;
- approve/reject behavior;
- state transition.

Use a real approval for **promotion gates**, not every experiment.

## Recommended lightweight model

Create a custom lab table:

```text
Lab Promotion Candidate
extends: Task
```

Suggested fields:
- Number
- Short description
- Experiment / capability ID
- Source environment
- Package / repository reference
- Promotion Review result
- Risk / autonomy level
- Approval
- State
- Approval reason
- Work notes
- Candidate package attachment/reference

Suggested states:

```text
Draft
→ Ready for Review
→ Approved
→ Enterprise Candidate
→ Retired

or

Ready for Review
→ Rejected
→ Rework
```

## Flow Designer

Trigger:

```text
Lab Promotion Candidate
State changes to Ready for Review
```

Then:

1. **Ask for Approval**
   - Record: current Lab Promotion Candidate
   - Approver: you (for lab simulation)
   - Approval reason: include candidate/review summary
2. If Approved:
   - set State = Approved
   - record approval timestamp
   - optionally create Enterprise Candidate package task
3. If Rejected:
   - set State = Rework / Rejected
   - preserve comments/reason

The Ask for Approval action creates the actual approval record in
`sysapproval_approver`.

## Self-approval in the lab

You are intentionally wearing multiple roles:
- builder;
- architect;
- reviewer;
- approver.

That is acceptable for a personal simulation.

The value is learning the workflow and audit mechanics.

Do not infer from this that enterprise self-approval is appropriate.

## Build Agent approvals are different

Build Agent itself requires approval before executing generated scripts.

That is a **runtime safety approval**.

Your Lab Promotion Candidate approval is a **lifecycle/promotion approval**.

They serve different purposes.

## Enterprise translation

For real application deployment, prefer the organization's native deployment
governance.

Where App Engine Management Center / Pipelines & Deployments is used, deployment
requests support actual review and approve/reject actions and can integrate with
Change Management.

Do not recreate a parallel enterprise approval process unless needed.
