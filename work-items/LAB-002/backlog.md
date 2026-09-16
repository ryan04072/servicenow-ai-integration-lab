Backlog Draft — LAB-002
Status: Draft; requires ADO placement and backlog acceptance.

Proposed hierarchy
ServiceNow Engineering / SDK and Fluent / Proof of Concept

Exact Azure DevOps area path, iteration, and work-item identifiers require validation.

User story
As a ServiceNow developer, I want to create and manage a small scoped application through SDK/Fluent so that the repository can demonstrate source-driven development, PDI deployment, metadata validation, change synchronization, and recovery.

Learning value
Validate SDK/Fluent suitability for supported scoped artifacts.
Establish a repeatable local-to-PDI workflow.
Make metadata changes reviewable through Git.
Identify boundaries where native ServiceNow tooling is required.
Produce evidence for future SDK-based work.
Acceptance criteria
A new scoped learning application is created with the selected scope documented.
One simple custom table with a small number of primitive fields is represented in .now.ts.
The selected SDK/Fluent and PDI versions are recorded.
The project passes the agreed local validation/build checks.
The project deploys to the connected PDI using the approved authentication method.
The deployed metadata is verified in the PDI.
A subsequent source-controlled metadata change is made and redeployed or synchronized.
Git history clearly shows the source changes.
A documented reinstall, rollback, or recovery procedure is demonstrated.
Any SDK/Fluent limitations and native-tooling boundaries are recorded.
No credentials or secrets are committed.
Destructive PDI actions receive human approval.
Implementation tasks
Confirm the accountable owner and final acceptance authority.
Confirm the selected application scope and naming convention.
Record Node.js, pnpm, SDK, Fluent tooling, and PDI versions.
Confirm SDK 4.12.1 support for the selected scoped application and table artifacts.
Establish the project configuration using the actual installed tooling.
Create the minimal scoped application and .now.ts metadata.
Run local build and validation.
Review the generated metadata diff.
Deploy to the connected PDI after required human approval.
Verify the deployed metadata in the PDI.
Make one controlled metadata change and redeploy or synchronize it.
Capture Git, local validation, deployment, and PDI verification evidence.
Test reinstall, rollback, or recovery.
Document unsupported artifacts and native-tooling fallback.
Evaluate the server-side Business Rule and ATF items only as stretch work after the baseline succeeds.
Explicitly out of scope
Production deployment
Business-system integrations
CMDB/ITOM behavior
Catalog or complex workflow development
CI/CD automation
Automated Azure DevOps integration
MCP write access
Complex UI or LUX development
Dependencies and blockers
Confirmed owner and acceptance authority.
Connected PDI access.
Approved least-privilege authentication configuration.
SDK 4.12.1 support for the selected artifact types.
Application scope and naming decision.
Approved deployment and recovery procedure.
Human approval for credentials and destructive PDI actions.
ADO area path, iteration, and work-item assignment.
Testing obligations
Project creation or source load.
Build and lint.
.now.ts metadata inspection.
Deployment to the PDI.
PDI metadata verification.
Controlled source change and redeployment.
Reinstall, rollback, or recovery.
Unsupported-artifact and invalid-configuration behavior.
Credential and secret scanning.
Regression verification after reinstall or synchronization.
Local success and PDI deployment success must be recorded separately.

Documentation obligations
Extend or reuse the existing source-driven development ADR.
Document application scope and selected artifact.
Record tool and PDI versions.
Document setup, build, deployment, and recovery commands.
Record authentication and security boundaries without exposing secrets.
Capture metadata limitations and native-tooling fallback.
Record Git, build, deployment, and PDI verification evidence.
Add as-built notes after the proof of concept is accepted.
