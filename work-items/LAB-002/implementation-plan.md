# Implementation Plan — LAB-002

Implementation Plan — LAB-002
Status: Draft; baseline implementation is bounded and subject to the implementation-planning human gate.

1. Preconditions
   Confirm:

Accountable owner and final acceptance authority: Ryan Reese, personal lab owner.
Selected application scope and naming convention.
Connected PDI release.
SDK 4.12.1 support for the selected scoped application and table artifacts.
Authentication method and least-privilege permissions.
Approved recovery or reinstall procedure.
Do not invent scope identifiers, package configuration, or deployment commands.

2. Baseline implementation
   Create a new scoped learning application containing:

One simple custom table.
A small number of primitive fields.
Fluent metadata represented in .now.ts.
Only artifacts confirmed as supported by the installed SDK/toolchain.
The baseline must demonstrate:

Local project/application setup.
Local build and validation.
Metadata diff inspection.
Deployment to the connected PDI.
PDI metadata verification.
One subsequent source-controlled metadata change.
Redeployment or synchronization.
Git-visible history.
Reinstall, rollback, or recovery.
Documentation of SDK/Fluent and native-tooling boundaries. 3. Stretch scope
Only after the baseline succeeds and is reviewed:

One small server-side Business Rule.
One ATF test, if supported by the selected project and tooling path.
Stretch work is not required for baseline acceptance.

4. Existing components to reuse
   Reuse:

The proposed SDK basics scope in README.md.
The source-driven decision in ADR-0001-source-driven-development.md.
Existing Node.js v24.19.0, pnpm 10.34.5, SDK 4.12.1, Fluent tooling, Lux Lab tooling, connected PDI, and Git/GitHub setup.
Native ServiceNow tools for unsupported or instance-aware artifacts. 5. Native UI versus SDK/Fluent
Primary path: SDK/Fluent for supported source-driven scoped metadata.

Fallback: Native Studio, IDE, or other ServiceNow tooling when:

SDK support is absent.
The operation requires instance-aware behavior.
Native tooling provides safer validation or deployment.
Generated metadata cannot be adequately reviewed.
Do not force unsupported artifacts into SDK/Fluent.

6. Artifacts to create or change
   Expected repository artifacts:

SDK project configuration, using the actual installed toolchain.
.now.ts source metadata.
Project README or setup documentation.
Extended or updated source-driven ADR if implementation reveals a material decision.
Build/deployment/recovery evidence.
As-built notes after acceptance.
Potential PDI artifacts:

Scoped learning application.
One custom table and primitive fields.
Stretch Business Rule or ATF test only after baseline success.
Exact artifact names and identifiers must come from the SDK and PDI.

7. Source and branch grouping
   Use one focused feature branch for LAB-002.

Group changes as:

Project/source: SDK configuration and .now.ts metadata.
Documentation: README, ADR update, setup and recovery instructions.
Evidence: local validation, metadata diff, deployment, PDI verification, and Git history.
Do not create update sets or production deployment artifacts unless the actual selected toolchain requires them. No CI/CD, automated Azure DevOps integration, or MCP write access is in scope.

8. Validation and tests
   Required baseline checks:

Project creation or source load.
SDK metadata validation.
Build and lint.
Generated metadata inspection.
Secret and credential scan.
PDI deployment.
PDI metadata verification.
Controlled source change and redeployment.
Reinstall, rollback, or recovery.
Regression verification after reinstall or synchronization.
Git history review.
Record local validation separately from PDI validation. Do not mark a check passed without evidence.

Stretch checks:

Business Rule behavior.
ATF execution, if supported.
Negative behavior for unsupported metadata or invalid configuration. 9. Deployment and rollback
Before deployment:

Confirm authentication and permissions.
Obtain human approval for any destructive PDI action.
Review the generated metadata diff.
Capture the source commit before deployment.
Deployment evidence must record:

Tool versions.
PDI release.
Source commit.
Command actually used.
Deployment result.
PDI verification result.
Recovery must document:

Reinstall or rollback steps.
PDI cleanup.
Handling of partial deployment.
Restoration of the prior source or metadata state.
Credential revocation or tooling disablement if automation fails. 10. Security and operability
Keep credentials in native or approved local credential storage.
Keep environment-specific configuration ignored.
Never commit tokens, passwords, endpoints, or secrets.
Use least-privilege PDI access.
Keep the experiment scoped and reversible.
Record unsupported artifacts and native-tooling boundaries.
Do not enable broader PDI or MCP write access for convenience. 11. Documentation impact
Document:

Objective and approved scope.
Application scope and selected artifact.
SDK, Fluent, Node, pnpm, and PDI versions.
Project setup and validation commands.
Deployment and recovery procedure.
Authentication boundaries without exposing secrets.
Generated metadata review.
PDI verification results.
SDK/Fluent limitations.
Native-tooling fallback.
As-built results after acceptance.
Reuse or extend ADR-0001-source-driven-development.md rather than creating a duplicate ADR unless a materially different decision emerges.

12. Out of scope
    Production deployment
    Business-system integrations
    CMDB/ITOM behavior
    Catalog or complex workflow development
    CI/CD automation
    Automated Azure DevOps integration
    MCP write access
    Complex UI or LUX development
