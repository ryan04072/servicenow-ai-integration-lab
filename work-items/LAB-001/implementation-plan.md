# Implementation Plan — LAB-001

Status: Draft; implementation remains blocked until the defined PDI, ownership, security, and return-state validations are complete.

1. Preconditions
   Resolve before implementation:

Confirm business/process owner.
Document current offboarding and equipment-return processes.
Validate ServiceNow OOB HR, fulfillment, asset, approval, notification, reporting, and integration capabilities.
Confirm authoritative systems for employee status, assigned assets, asset state, and endpoint disposition.
Define “returned,” inspection, wipe, reconciliation, exception, and closure criteria.
Confirm asset lifecycle states and handling for lost, damaged, missing, shared, disputed, or duplicate assets.
Confirm security, privacy, retention, SLA, escalation, and manager-visibility requirements.
Confirm ADO work item and GitHub traceability identifiers. 2. OOB evaluation sequence
Evaluate in this order:

Existing HR/offboarding capability and intake pattern.
Existing request/catalog and fulfillment-task pattern.
Existing employee-to-asset relationship and asset lifecycle behavior.
Existing approvals, assignment, notifications, SLAs, escalations, and audit history.
Existing manager workspace, portal, reporting, or dashboard capabilities.
Existing HR, inventory, endpoint-management, identity, and change integrations.
Existing ServiceNow DevOps/change evidence path.
Select configuration and reuse where the OOB behavior satisfies the approved acceptance criteria.

3. Bounded solution shape
   Subject to validation, configure a workflow that:

Accepts an HR-initiated offboarding equipment-return request.
Resolves the employee’s applicable assigned assets.
Tracks each asset independently.
Creates IT fulfillment work.
Supports return and exception statuses.
Updates the authoritative asset state only after the confirmed return condition.
Exposes completion status to authorized managers.
Preserves audit history and supports reconciliation.
Do not create custom tables, fields, roles, APIs, or scripts until the OOB gap is demonstrated and documented.

4. Artifacts to create or change
   Repository and delivery evidence:

implementation-plan.md
ADR for ownership, OOB evaluation, asset-state semantics, security, integrations, operations, and rollback
Test plan
ADO story/tasks and dependency links
GitHub branch and PR
ServiceNow change evidence
Release manifest
As-built documentation
Support/reconciliation runbook
ServiceNow artifacts:

Existing OOB configuration, where sufficient
Native workflow/flow/subflow/action configuration only after capability validation
Minimal additional configuration for per-asset tracking or exceptions if required
Integration configuration only where an existing supported boundary is insufficient
Exact ServiceNow artifact names must be determined from the target PDI and official documentation.

5. Reuse boundaries
   Reuse:

Existing HR/offboarding intake.
Existing fulfillment task model.
Existing asset relationships and lifecycle states.
Existing assignment rules, approvals, notifications, SLAs, reporting, and audit features.
Existing integration actions or subflows.
Existing ServiceNow change and release evidence mechanisms.
Do not duplicate employee, asset, endpoint, or change records when another system is authoritative.

6. Native UI versus SDK/Fluent
   Default path: native ServiceNow configuration through Studio, IDE, or Workflow Studio where appropriate.

SDK/Fluent: not selected yet. Evaluate only if:

The target artifacts are supported.
The scope and metadata are supported.
Source-driven development provides a clear benefit.
The native instance-aware path is insufficient or less maintainable.
Avoid forcing every artifact into SDK/Fluent.

7. Source and deployment grouping
   Group changes by responsibility:

Workflow/configuration: HR intake, fulfillment, asset tracking, approvals, notifications, visibility.
Integration: HR, asset inventory, endpoint-management, identity, and reconciliation boundaries.
Security: least-privilege access, manager visibility, credential handling, audit.
Documentation: ADR, runbook, test evidence, release and as-built records.
Use the approved source-control/update-set strategy for the selected ServiceNow development path. Record the GitHub branch and PR, build/test evidence, and ServiceNow change identifier in the work package.

8. Test plan obligations
   Cover:

Single and multiple assigned assets.
Laptops, monitors, phones, and other supported equipment.
No assigned assets.
Partial, late, lost, damaged, missing, shared, disputed, and duplicate assets.
IT assignment, reassignment, escalation, and closure.
Correct asset-state transition timing.
Manager authorization and unauthorized-access denial.
Notifications, SLAs, audit history, and reports.
Integration timeout, retry, duplicate-event, and reconciliation behavior.
Changed or cancelled offboarding.
Regression of existing HR, fulfillment, asset, and change processes.
Human UAT with HR, IT, Asset Management, security, and manager personas. 9. Deployment and rollback
Before deployment:

Complete build/lint and applicable ServiceNow validation.
Complete independent code/configuration review.
Complete UAT and record acceptance.
Verify release traceability from ADO through GitHub, tests, ServiceNow change, and release.
Obtain required change/CAB approval.
Rollback must provide:

Workflow disablement or kill switch.
Reversal or correction procedure for configuration.
Prevention of duplicate fulfillment or asset-state updates.
Reconciliation of requests and assets processed during rollback.
Support ownership and incident escalation. 10. Documentation impact
Required documentation:

ADR.
Configuration and integration design.
Security and access model.
Test plan and UAT evidence.
Operational support, exception, retry, and reconciliation runbook.
Deployment and rollback instructions.
Release manifest.
As-built documentation after actual implementation. 11. Recommended next state
Remain in implementation_planning until the implementation plan is reviewed and accepted at the human planning gate. Do not advance to implementation while the PDI capability and system-of-record questions remain unresolved.
