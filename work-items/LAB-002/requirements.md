# Requirements — LAB-002

Status: Draft; requires owner and environment validation.

Desired outcome
Evaluate whether a small, scoped ServiceNow development proof of concept can be developed, tested, deployed to a PDI, and tracked through Git using the ServiceNow SDK and Fluent toolchain.

The proof of concept should produce evidence about:

project setup and source structure,
supported metadata/artifacts,
local validation,
PDI deployment and reinstall or rollback,
Git-based change history,
limitations requiring native ServiceNow tooling.
Owner
Not confirmed.

Likely stakeholders include the ServiceNow platform owner, developer, and engineering lead, but accountable ownership must be validated.

Users and volume
Potential users:

ServiceNow developer
Platform administrator
Code reviewer
Test engineer
Architecture reviewer
Expected proof-of-concept volume is not provided. The scope should remain small and bounded to one learning application or equivalent test artifact.

Current state
The repository contains a proposed SDK basics lab, but no LAB-002 implementation or SDK project configuration.

Existing repository guidance proposes:

a small scoped application,
source-driven artifacts where supported,
validation in a PDI,
Git history,
build/lint,
rollback or reinstall,
architecture review before implementation.
The current SDK version, Fluent version, PDI availability, authentication method, and supported artifact types are unknown.

Business and learning value
Expected value:

Determine whether SDK/Fluent is suitable for supported ServiceNow development.
Establish a repeatable VS Code-to-PDI-to-Git workflow.
Make metadata changes reviewable through source control.
Identify SDK limitations and native-tooling boundaries.
Provide evidence for future project-specific SDK workflows and CI.
These outcomes require validation with the accountable owner.

Date and reason
Date: Not provided.
Reason: Repository context indicates this is part of the SDK/PDI engineering learning sequence, but the delivery target and urgency are not specified.

Systems and tools involved
Confirmed or proposed by repository evidence:

ServiceNow PDI
ServiceNow SDK/Fluent toolchain
VS Code
Git/GitHub
Local build and lint tooling
Potentially involved:

ServiceNow native Studio/IDE/Workflow Studio
CI or build automation
Provider-specific development tools
Azure DevOps for planning and work-item traceability
No specific SDK version, package manager, project configuration, PDI endpoint, or authentication mechanism has been established.

Dependencies
ServiceNow PDI access.
Supported SDK/Fluent version and documentation.
Valid authentication and least-privilege credentials.
Confirmed artifact type for the proof of concept.
Local SDK project configuration.
Ability to build, lint, deploy, reinstall, and validate in the PDI.
Git repository and branch strategy.
Architecture review before implementation.
Human approval for destructive PDI actions and credential changes.
Implementation-neutral acceptance criteria
The proof of concept has a documented objective, scope, owner, and selected artifact type.
The selected SDK/Fluent version and project prerequisites are recorded.
A minimal scoped project can be created or loaded from source.
Local validation results are captured.
The project can be deployed to the target PDI, subject to available tooling and permissions.
Deployment results and any unsupported artifact limitations are documented.
The proof of concept can be reinstalled, rolled back, or otherwise restored using a documented procedure.
Source changes are reviewable through Git history.
Relevant tests or validation checks are executed and their evidence is recorded.
The proof of concept identifies which work remains better suited to native ServiceNow tooling.
No credentials or secrets are committed to the repository.
Human approval is obtained before destructive PDI actions or final acceptance.
Missing information
Accountable business or learning owner.
Exact learning objective and success definition.
Target SDK and Fluent versions.
Target ServiceNow release and PDI availability.
Supported artifact type for the proof of concept.
Required application scope and naming convention.
Authentication and credential-storage approach.
Local operating-system and runtime prerequisites.
Build, lint, and test commands.
Deployment and rollback mechanism.
Whether GitHub Actions or another CI system is in scope.
Whether Azure DevOps work-item integration is required.
Required security and least-privilege permissions.
Whether native-tool comparison is mandatory.
Expected evidence format and final acceptance owner.
Whether an ADR is required for this isolated proof of concept.

### Validated environment facts

The following have already been verified in the local development environment:

- Windows development workstation is available.
- VS Code is configured for the repository.
- Node.js `v24.19.0` is installed.
- pnpm `10.34.5` is installed.
- ServiceNow SDK `4.12.1` is installed.
- ServiceNow Fluent Language tooling is installed in VS Code.
- ServiceNow Lux Lab tooling is installed and configured.
- A ServiceNow PDI is available and has been connected to the local development tooling.
- Git and GitHub source control are operational for this repository.

The following remain unvalidated:

- Exact SDK authentication/configuration to use for this proof of concept.
- Selected scoped application and naming convention.
- Specific metadata/artifact type to implement.
- Exact SDK/Fluent support for that artifact type.
- Deployment and rollback procedure for the selected project.
- Whether CI automation is in scope for LAB-002.
