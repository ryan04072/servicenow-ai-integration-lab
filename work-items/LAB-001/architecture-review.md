# Architecture Review — LAB-001

Architecture review completed for LAB-001. Per the Architect role, this remains blocked pending human/PDI validation; no implementation or lifecycle transition is authorized.

Architecture Review
Status: Needs human validation
Recommendation: Proceed only after confirming OOB capabilities, ownership boundaries, and asset-state semantics.

ServiceNow role
ServiceNow should orchestrate the offboarding equipment-return process:

Receive the HR request.
Identify applicable assigned assets.
Create and track IT fulfillment work.
Track each asset’s return and exception status.
Provide authorized manager visibility.
Record the audit trail.
Update or invoke the authoritative asset system after verified return.
ServiceNow must not be assumed to own HR employment data, endpoint security state, or asset inventory until validated.

OOB capabilities to evaluate first
Evaluate these capabilities in the target PDI and applicable product documentation:

HR offboarding or employee lifecycle processes.
Service catalog/request fulfillment.
Existing fulfillment task and assignment mechanisms.
Asset Management and employee-to-asset relationships.
Asset lifecycle states and state transitions.
Approvals, notifications, SLAs, escalation, and audit history.
Manager-facing workspace, portal, reporting, or dashboards.
Existing HR, endpoint-management, identity, and inventory integrations.
Existing change-management integration.
Do not invent specific tables, fields, roles, APIs, plugins, or licensing assumptions.

System-of-record boundaries
Domain Proposed authority
Employment/offboarding status HR system or validated ServiceNow HR capability
Request and fulfillment status ServiceNow
Assigned assets and lifecycle state Validated authoritative asset/inventory system
Device wipe or security disposition Endpoint-management/security platform
Change governance ServiceNow change process
Engineering and release evidence Azure DevOps and GitHub according to repository lifecycle
The workflow must not mark an asset returned merely because an IT task is closed. The organization must define whether return means physical receipt, inspection, wipe, reconciliation, or another verified event.

Configuration versus customization
Prefer configuration and reuse:

Existing offboarding and request patterns.
Existing fulfillment tasks and assignment rules.
Existing asset relationships and state models.
Existing notifications, SLAs, approvals, and reporting.
Existing integration actions or subflows.
Customization may be justified for multi-asset tracking, per-asset exceptions, reconciliation, or manager visibility only where OOB capability cannot satisfy the requirement.

SDK/Fluent applicability is currently unknown. Validate supported metadata and scope first. Native ServiceNow tooling may be more appropriate for instance-aware configuration.

Security and lifecycle concerns
Validate and enforce:

Least-privilege access for HR, IT, asset managers, and managers.
Separation between HR-sensitive data and completion visibility.
Separate authority to confirm physical receipt, update asset state, and close the overall process.
Protection of integration credentials.
Auditability for initiation, assignment, receipt, reconciliation, exceptions, and closure.
Handling of lost, damaged, disputed, shared, missing, or duplicate assets.
Retention and privacy requirements.
Kill switch and recovery path for faulty automation.
The implementation lifecycle requires architecture acceptance, priority approval, implementation review, testing, UAT, change/CAB approval, release acceptance, and post-release validation.

CMDB/ITOM implications
The workflow should distinguish configuration items, hardware assets, consumables, and other assigned equipment according to the validated ServiceNow data model.

Validate:

Whether each equipment type is represented in the authoritative asset model.
Whether asset-to-user relationships are complete and current.
Whether asset state changes affect CMDB relationships or downstream discovery.
Whether returned devices require wipe, quarantine, inspection, reassignment, retirement, or disposal.
Whether reconciliation with endpoint or inventory systems is required.
Testing and operability
Test:

One and multiple assets.
Laptop, monitor, phone, and other equipment.
No assigned assets.
Partial, late, lost, damaged, disputed, and duplicate returns.
Unauthorized manager access.
Asset-state changes only after the defined return condition.
Assignment, reassignment, escalation, notification, and closure.
Integration timeout, retry, duplicate event, and reconciliation behavior.
Changed or cancelled offboarding.
Audit history, reporting, and SLA behavior.
Operate with reporting for overdue returns, exceptions, failed integrations, and mismatched workflow versus asset state. Define support ownership, reconciliation, retry, rollback, and disablement procedures.

ADR
An ADR is warranted because the design crosses HR, fulfillment, Asset Management, endpoint security, access control, and change governance.

The ADR should document:

OOB capabilities evaluated.
System-of-record ownership.
Definition of “returned.”
Asset-state mapping.
Configuration versus customization decisions.
Security and manager visibility boundaries.
Integration and reconciliation behavior.
Operational ownership.
Testing, rollout, rollback, and approval gates.
Open validation questions
Which system owns employee offboarding status and termination dates?
Which system owns assigned asset inventory?
Which ServiceNow HR, fulfillment, and Asset Management capabilities are enabled?
What does “returned” mean operationally?
Which asset states are valid after receipt, inspection, wipe, and reconciliation?
How are lost, damaged, shared, missing, and disputed assets handled?
What manager data may be exposed?
What SLAs, reminders, and escalations apply?
Which systems must be integrated?
What are the retry and reconciliation rules?
What are the retention and privacy requirements?
Which changes require a ServiceNow change record or CAB approval?
Repository evidence used
servicenow-architect.md
SKILL.md
requirements.md
work-package.json
AGENTS.md
01-TARGET_ARCHITECTURE.md
07-SERVICENOW_TOOLCHAIN.md
12-HUMAN_GATES.md
14-SECURITY_AND_SECRETS.md
lifecycle.json
