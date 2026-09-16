Portfolio Recommendation — LAB-002
Status: Sequencing recommendation only; not a final priority decision.

Recommended sequence
Complete human architecture acceptance, already recorded.
Confirm the owner and final acceptance authority.
Confirm the selected scoped application, naming convention, SDK configuration, and authentication method.
Validate SDK 4.12.1 support for the selected table and .now.ts artifacts.
Execute the approved baseline:
local project setup,
Fluent source,
build/validation,
PDI deployment,
PDI metadata verification,
one source-controlled metadata change,
redeployment or synchronization,
Git history,
reinstall, rollback, or recovery evidence.
Record SDK/native-tooling boundaries and update the existing source-driven ADR if needed.
Add the Business Rule or ATF test only after the baseline succeeds.
Proceed to independent review, testing, and as-built evidence.
Dependencies and blockers
Owner and acceptance authority are not confirmed.
Selected artifact and application scope are not confirmed.
SDK support for the selected artifact is not validated.
Exact authentication and project configuration remain unresolved.
Deployment and rollback/reinstall procedures are not yet demonstrated.
CI/CD and Azure DevOps integration are out of scope unless separately approved.
Destructive PDI actions and credential changes require human approval.
Roadmap alignment
LAB-002 directly aligns with Phase 2 — SDK / PDI Engineering, which includes scoped SDK work, Fluent tooling, Git workflow, and tests.

It also matches the repository’s next-build sequence: complete SDK Basics before multi-provider review, orchestrator validation, SDK CI, and broader automation.

Sources: 02-IMPLEMENTATION_ROADMAP.md, 15-NEXT_BUILD_SEQUENCE.md, 03-IMPLEMENTATION_RUNBOOK.md

Expedite tradeoffs
Expediting is reasonable only as a tightly bounded learning experiment. It could defer:

native-tool comparison,
stretch Business Rule work,
ATF evaluation,
CI/CD,
Azure DevOps integration.
The baseline should not be expanded while the selected artifact, authentication, or recovery path is unresolved.

What would be displaced
No competing backlog, capacity plan, roadmap commitment, urgency, or displacement data is present in the repository. Therefore, no displaced initiative can be identified without inventing facts.

Leadership decisions required
Confirm the accountable owner and final acceptance authority.
Approve the selected scoped application and artifact.
Approve least-privilege PDI access and authentication handling.
Decide whether native-tool comparison is required.
Confirm that CI/CD and Azure DevOps integration remain out of scope.
Approve any destructive PDI action.
Accept the baseline-versus-stretch scope boundary.
