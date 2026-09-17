# AI Governance Responsibility Model

## Principle

Responsibility is layered. The person who built an agent is not automatically
the person accountable for every business outcome, and a human approval does not
erase the platform owner's responsibility for system quality.

## Core roles

### Executive sponsor / CIO / VP
Accountable for enterprise risk tolerance, investment direction, major platform
strategy, and unresolved material-risk escalation.

### AI governance / AI steward
Responsible for inventory completeness, lifecycle governance, managed/unmanaged
disposition, governance tasks, portfolio visibility, and exceptions.

### AI asset owner / product owner
Accountable for why the asset exists, intended outcome, lifecycle progression,
deployment/retirement decisions subject to controls, and value realization.

### Business / process owner
Accountable for business rules, process outcomes, and acceptance criteria.

### Platform owner
Accountable for architecture, integration/runtime configuration, technical standards,
supportability, and platform-specific monitoring.

### Capability owner
Accountable for deterministic capability input/output contract, authorization,
validation, idempotency, audit, and versioning.

### Builder / maintainer
Responsible for implementation, testing, documentation, monitoring setup, and remediation.

### Security / Privacy / Risk / Data
Provide independent control ownership and review under enterprise policy.

### Human approver
Accountable for the specific decision they are authorized to approve; approval does
not transfer ownership of the underlying AI asset.

### Vendor
Responsible within contracted scope/SLA; enterprise accountability remains internal.

## Minimum ownership rule

No production AI asset should lack:
- AI asset owner;
- technical/platform owner;
- support owner;
- data/process owner where applicable;
- escalation path.
