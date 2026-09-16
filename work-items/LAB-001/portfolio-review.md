Portfolio Recommendation — LAB-001
Status: Sequencing recommendation only; not a final priority decision.

Recommended sequence
Resolve business ownership, current-state process, volume, timing, SLA, and manager-visibility requirements.
Validate ServiceNow PDI capabilities, asset ownership, asset states, endpoint integrations, and security boundaries.
Confirm ADO hierarchy, area path, iteration, and delivery capacity.
Create the ADR and implementation plan.
Implement the smallest OOB/configuration-first slice:
HR initiation
multi-asset tracking
IT fulfillment
manager completion visibility
Add integrations, exception handling, reconciliation, and operational reporting only after ownership and return-state semantics are confirmed.
Complete testing, UAT, change approval, release, and as-built documentation.
Dependencies and blockers
Business/process owner is not confirmed.
Current offboarding and return processes are undocumented.
Employee and asset system-of-record boundaries are unresolved.
“Returned” and valid asset-state transitions are undefined.
Lost, damaged, missing, shared, and disputed asset handling is unresolved.
Security, privacy, retention, SLA, escalation, and manager-access requirements are unresolved.
ADO area path, iteration, priority, and capacity are unknown.
Required PDI capabilities and integrations are unverified.
These are sequencing blockers, not merely implementation details.

Roadmap alignment
The work aligns with the repository’s sequence:

Phase 1: manual agent lifecycle and human transitions.
Phase 2: SDK/PDI engineering and testing after architecture and requirements validation.
Phase 5: DevOps Change Velocity evidence linking ADO, GitHub, tests, ServiceNow change, CAB, deployment, and release.
The next practical portfolio step is validation and planning, not implementation.

Expedite tradeoffs
Expediting could deliver a narrow workflow sooner, but would require explicitly accepting temporary limitations such as:

manual asset reconciliation,
limited exception handling,
deferred endpoint-management integration,
reduced reporting,
narrower manager visibility.
Those limitations could create inaccurate asset states, privacy issues, fulfillment gaps, or operational rework. Expediting should therefore require leadership acceptance of scope and residual risk.

What would be displaced
No competing backlog, roadmap, capacity, or active initiative evidence is present in the repository. Therefore, displacement cannot be identified without inventing facts.

Leadership should compare LAB-001 against:

legally or policy-mandated offboarding work,
security and asset-loss risk,
employee volume and operational burden,
integration dependencies,
available HR, IT, Asset Management, and ServiceNow capacity.
Leadership decisions required
Confirm accountable business/process owner.
Decide whether the work is mandatory, risk-reduction, or improvement work.
Set target timing and priority relative to competing work.
Approve MVP scope versus full integration scope.
Assign HR, IT fulfillment, Asset Management, security, and platform owners.
Confirm acceptable interim manual controls.
Confirm ADO placement, iteration, and capacity.
Approve the implementation start after these dependencies are resolved.
