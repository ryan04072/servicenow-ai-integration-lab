# Architecture Review — LAB-002

Architecture Review — LAB-002
Status: Draft; ready for human architecture review, not implementation approval.

ServiceNow’s role
ServiceNow is the target runtime and PDI validation platform. The proof of concept should demonstrate a small scoped application developed from source, deployed to the PDI, validated there, and recoverable through reinstall or rollback.

The repository does not require every artifact to use SDK/Fluent. Unsupported or instance-aware work may remain in native ServiceNow tooling.

Sources: servicenow-architect.md, SKILL.md, 07-SERVICENOW_TOOLCHAIN.md

System-of-record boundaries
For this proof of concept:

Git should be the durable source of truth for source-driven project artifacts and history.
The ServiceNow PDI is the runtime and deployment-validation authority.
The SDK/Fluent toolchain is the local build and deployment mechanism, subject to supported artifact coverage.
Native ServiceNow tooling is the authority for artifacts that SDK/Fluent cannot safely represent.
VS Code is the local engineering environment, not a production system of record.
Azure DevOps and GitHub provide planning and engineering traceability if included in the delivery workflow.
The exact source/deployment relationship, package configuration, and PDI project mapping still require validation.

Sources: ADR-0001-source-driven-development.md, 01-TARGET_ARCHITECTURE.md, requirements.md

OOB and existing capabilities to evaluate first
This is a proof of concept rather than a business workflow, so the relevant OOB decision is tool choice:

Confirm the installed ServiceNow SDK and Fluent tooling can create, build, deploy, and reinstall the selected scoped artifact.
Confirm the selected artifact type is supported by SDK 4.12.1 and the connected PDI release.
Compare SDK/Fluent with native Studio, IDE, or other ServiceNow tooling for any unsupported or instance-specific metadata.
Use existing local build, lint, test, Git, and PDI tooling where available.
Do not introduce custom automation or MCP write access unless the basic workflow cannot be demonstrated with the existing toolchain.
The repository’s proposed minimum is a small scoped application with one custom table, one role/security decision, one small server-side behavior, and one testable function. This is a candidate scope, not yet an approved artifact list.

Sources: README.md, 07-SERVICENOW_TOOLCHAIN.md, requirements.md

Configuration versus customization
Prefer the smallest source-driven scoped application that proves the toolchain. Avoid designing a reusable production application or adding unrelated workflow behavior.

Use SDK/Fluent for artifacts only where:

support is confirmed,
the metadata is reviewable in source,
deployment is reproducible,
rollback or reinstall is understood.
Use native ServiceNow tooling where:

the artifact is unsupported,
the operation requires instance-aware behavior,
native tooling provides safer deployment or validation,
the generated metadata cannot be adequately reviewed.
Do not invent artifact names, application scopes, tables, roles, APIs, package configuration, or deployment commands before validating them.

Sources: AGENTS.md, ADR-0001-source-driven-development.md, SKILL.md

SDK/Fluent recommendation
Recommendation: Proceed with a bounded SDK/Fluent proof of concept, conditional on confirming the selected artifact type and project configuration.

The local environment provides useful evidence:

Windows workstation
Node.js v24.19.0
pnpm 10.34.5
ServiceNow SDK 4.12.1
Fluent Language tooling
Lux Lab tooling
Connected ServiceNow PDI
Operational Git/GitHub source control
These are intake-reported environment facts, not yet deployment success evidence.

Sources: requirements.md, README.md

Integration boundaries
Keep the first proof of concept isolated:

Local workstation to SDK/Fluent toolchain
SDK/Fluent toolchain to the connected PDI
Git repository to source history
Optional Azure DevOps/GitHub linkage for delivery evidence
No business-system integration is required by the current requirements. CI automation, provider-specific tooling, and Azure DevOps integration are explicitly unresolved and should not be added to the initial scope without approval.

Sources: requirements.md, 01-TARGET_ARCHITECTURE.md, 08-DEVOPS_CHANGE_VELOCITY.md

Security
Use:

Native credential storage or the approved local authentication mechanism.
Least-privilege PDI access.
Read-only validation where possible.
Ignored local configuration for provider or environment-specific settings.
No credentials, tokens, endpoints, or secrets in source.
Human approval before credential changes or destructive PDI actions.
A documented disablement or recovery path for failed deployment automation.
Do not enable broader PDI write tools or MCP writes merely to accelerate the proof of concept.

Sources: 14-SECURITY_AND_SECRETS.md, 12-HUMAN_GATES.md, AGENTS.md

Lifecycle ownership
The implementation evidence should remain traceable across:

Requirements → architecture review → human architecture acceptance → backlog → priority → implementation plan → implementation → review → testing → UAT → change/release → as-built

The current work package is at architecture_required. The next lifecycle step is human architecture review. No implementation should begin until that gate is accepted.

Sources: lifecycle.json, 04-LIFECYCLE_AND_EVIDENCE_MODEL.md, 12-HUMAN_GATES.md

CMDB and ITOM implications
CMDB/ITOM impact appears low for the proposed isolated proof of concept, because no infrastructure or operational configuration-management use case is currently defined.

Validate that the selected artifact does not:

create or alter CMDB data,
create discovery or monitoring behavior,
require production configuration items,
introduce operational dependencies beyond the PDI.
If the proof of concept expands into operational platform behavior, its CMDB/ITOM impact must be reassessed.

Upgradeability
Keep the experiment small, scoped, and reversible. Record:

SDK version,
Fluent tooling version,
Node and package-manager versions,
PDI release,
generated metadata,
build/deploy commands,
unsupported artifact findings.
Revisit the design if the selected artifact is unsupported by the chosen SDK version.

Source: ADR-0001-source-driven-development.md

Operability
The proof of concept should have:

repeatable setup instructions,
deterministic local validation,
deployment result capture,
reinstall or rollback procedure,
PDI cleanup procedure,
failure and recovery notes,
clear ownership for credentials and PDI access,
a record of which steps require native tooling.
It should not be treated as production-ready solely because it deploys successfully.

Sources: README.md, 03-IMPLEMENTATION_RUNBOOK.md

Testing
Required evidence should cover:

project creation or source load,
build and lint,
metadata inspection,
deployment to the PDI,
runtime or artifact validation,
reinstall or rollback,
source-history review,
negative behavior for unsupported artifacts or invalid configuration,
credential and secret scanning,
regression after reinstall.
The test result must distinguish local success from PDI deployment success. No test should be marked passed without evidence.

Sources: SKILL.md, README.md

ADR recommendation
An ADR is warranted, but the existing proposed ADR-0001 may be reusable or extended rather than creating an unnecessary duplicate.

The ADR should record:

selected artifact and scope,
SDK/Fluent versions,
why source-driven development is appropriate,
native-tooling fallback,
authentication and security boundaries,
deployment and rollback approach,
PDI validation evidence,
limitations and revisit triggers.
Open questions requiring validation
What is the exact selected artifact for the proof of concept?
What application scope and naming convention will be used?
Does SDK 4.12.1 support the selected artifact type?
Which PDI release is connected?
What project configuration and authentication method should be used?
Does deployment require human approval or a destructive PDI action?
What is the approved rollback or reinstall procedure?
Are CI automation and Azure DevOps integration in scope?
Must native tooling be evaluated comparatively?
Who owns final architecture and proof-of-concept acceptance?
What evidence format is required for build, deployment, runtime validation, and rollback?
Does the selected artifact create any CMDB, ITOM, security, or operational impact?
Decision
Conditional recommendation: proceed to human architecture review with a bounded SDK/Fluent proof-of-concept scope.

Not approved: implementation, destructive PDI actions, credential changes, or final acceptance.

## Human Architecture Decision

Architecture approved for a bounded SDK/Fluent proof of concept.

### Approved baseline scope

Create a new scoped ServiceNow learning application and use ServiceNow SDK/Fluent to define and manage one simple custom table with a small number of primitive fields.

The baseline proof of concept must demonstrate:

1. Local SDK project/application setup.
2. Fluent source represented in `.now.ts`.
3. Local validation/build.
4. Deployment to the connected ServiceNow PDI.
5. Verification of the deployed metadata in the PDI.
6. A subsequent source-controlled metadata change.
7. Redeployment or synchronization of that change.
8. Git-visible change history.
9. A documented reinstall, rollback, or recovery procedure.
10. Identification of any SDK/Fluent versus native-tooling boundaries encountered.

### Stretch scope

Only after the baseline succeeds:

- Add one small server-side Business Rule.
- Add one Automated Test Framework test if supported by the selected project/tooling path.

### Explicitly out of scope

- Production deployment
- Business-system integrations
- CMDB/ITOM behavior
- Catalog or complex workflow development
- CI/CD automation
- Automated Azure DevOps integration
- MCP write access
- Complex UI or LUX development

### Architecture constraints

- Git remains the durable source for source-driven artifacts.
- The PDI is the runtime validation environment.
- Native ServiceNow tooling remains an approved fallback for unsupported or instance-aware metadata.
- No credentials or secrets may be committed.
- Destructive PDI actions remain human-gated.
- Exact application scope identifiers and deployment commands must come from the actual ServiceNow tooling rather than being invented.

### ADR

Use or extend the existing source-driven-development ADR rather than creating a duplicate ADR unless implementation reveals a materially different architectural decision.
