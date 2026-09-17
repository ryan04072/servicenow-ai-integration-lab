# Lab 11 — Real Promotion Approval

## Objective

Replace a manually-set `Approved` value with a real ServiceNow approval flow.

## Build

Create a `Lab Promotion Candidate` Task-derived table.

Configure:
- states;
- approval field;
- work notes;
- candidate package reference;
- Promotion Review result.

Build a Flow:

```text
Ready for Review
→ Ask for Approval
→ Approved?
   ├─ yes → Approved → Enterprise Candidate
   └─ no  → Rework
```

Approve the request yourself for the personal simulation.

## Validate

Confirm:
- `sysapproval_approver` record exists;
- approval reason is stored;
- comments/history are visible;
- record state changes correctly;
- rejection path works;
- resubmission works.

## Learning

Compare:
- manually setting a field;
- actual approval framework;
- Build Agent script approval;
- AEMC deployment approval.

Document why they are different controls.
