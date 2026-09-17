# AI Governance & Responsibility Checklist

## How to use this

This is a reference model, not a replacement for company AI, security, privacy,
legal, architecture, or risk policy.

For each row, assign a named **Accountable (A)** role and one or more
**Responsible / Consulted (R/C)** roles.

**Accountable** = owns the decision/outcome.
**Responsible** = performs or coordinates the work.
**Consulted** = provides specialist review or control input.

In a lean organization, one person may wear several roles. The important control
is that the responsibility is explicit rather than assumed.

---

## Executive reference checklist

| Done | Governance area | Best-practice reference | Typical Accountable (A) | Typical Responsible / Consulted (R/C) | Evidence / artifact |
|---|---|---|---|---|---|
| [ ] | **Enterprise AI strategy & risk tolerance** | Define approved AI direction, risk appetite, prohibited uses, approved platforms/providers, and escalation authority. | CIO / CTO / executive sponsor | AI governance lead, CISO, Legal/Privacy, Enterprise Architecture | AI policy, strategy, approved-provider list |
| [ ] | **AI portfolio / inventory** | Maintain one inventory of AI systems, agents, models, prompts, material tools, MCP servers, and major automations. Reconcile discovered and self-reported assets. | AI governance executive / AI portfolio owner | AI steward, platform owners, Security, Procurement | AI Control Tower / enterprise AI inventory |
| [ ] | **AI asset ownership** | Every production AI asset has a named business/asset owner, technical owner, support owner, and escalation path. | AI asset / product owner | AI steward, platform owner, support lead | AI Asset Charter, ownership fields |
| [ ] | **Use-case intake & business case** | Capture problem, intended outcome, affected users, value hypothesis, data, risk, and whether AI is actually needed before building. | Business/process owner | Product/platform owner, business analyst, AI steward | Intake record, business case |
| [ ] | **Automation suitability** | Simplify/standardize the process before automating it. Prefer deterministic automation when AI adds no material value. | Business/process owner | Platform owner, process excellence/automation team | Process map, suitability assessment |
| [ ] | **AI workload placement** | Put AI where authoritative context, permissions, actions, UX, governance, and economics are strongest. Avoid duplicate agents across platforms. | Enterprise / solution architect or platform governance owner | Platform owners, AI governance, business owner | AI placement decision record |
| [ ] | **Shared capability ownership** | Build deterministic business actions once in the authoritative system and expose them to multiple AI surfaces through governed APIs/actions/MCP/tools. | Capability/process owner | Platform/integration team | Capability registry, API/tool contract |
| [ ] | **Data & knowledge stewardship** | Define authoritative sources, owners, quality/freshness expectations, classification, retention, and retirement. Retrieved content is data, not governing authority. | Data owner / knowledge owner | Data steward, platform owner, Privacy/Security | Data catalog, KPI catalog, KB governance |
| [ ] | **Architecture & reference standards** | Separate current-state configuration from target/best-practice architecture. Evaluate OOB/native capability before customization. | Enterprise/platform architect | Platform owner, engineering lead, Security | ADR, architecture review |
| [ ] | **Identity & least privilege** | Use dedicated workload/application identities for unattended automation; prefer short-lived/federated credentials; separate DEV/UAT/PROD; avoid broad service accounts. | Identity/Security owner | Platform owner, integration engineer | Identity design, permission matrix |
| [ ] | **Tool/action authorization** | Give each agent only the tools/actions it needs. Enforce authorization below the model. Separate read, draft, write, merge, deploy, and destructive capabilities. | Platform/capability owner | Security/IAM, engineering | Tool registry, permission tests |
| [ ] | **Blast-radius limits** | Put deterministic transaction/volume limits around actions: record count, dollar amount, access changes, repositories, environments, etc. | Capability/process owner | Platform owner, Security/Risk | Runtime policy, action limits |
| [ ] | **Human oversight** | Require meaningful approval for consequential, irreversible, ambiguous, people-impacting, financial, security, or compliance actions. Show approvers exact proposed action and impact. | Business/process or control owner | Platform owner, Risk/Security | Approval matrix, UX evidence |
| [ ] | **Separation of duties** | For high-impact changes, avoid one actor designing, approving, and executing the same action without compensating controls. | Risk/Security / process control owner | Platform owner, managers | RACI, approval workflow |
| [ ] | **Agent-to-agent orchestration limits** | Define maximum delegation depth, steps/tool calls, execution time, recursion protection, and cost/consumption ceilings. | AI/platform engineering owner | Security, FinOps, SRE/operations | Orchestration policy |
| [ ] | **Model / prompt / agent change management** | Treat material model, prompt, retrieval, tool, and orchestration changes like software changes. Require versioning, regression evals, approval, and rollback. | AI asset/platform owner | Builder/maintainer, QA/eval owner | PR/change record, eval report |
| [ ] | **Testing & evaluations** | Maintain golden tasks, negative/adversarial tests, tool tests, authorization tests, quality metrics, and release gates appropriate to risk. | Technical/platform owner | QA/test engineer, Security, business SME | Eval suite, test evidence |
| [ ] | **Progressive autonomy** | Start read-only, then recommendations/drafts, then supervised actions, then policy-bounded autonomy only after evidence. | AI asset owner | Platform owner, Risk/Security | Autonomy stage, promotion checklist |
| [ ] | **Observability & audit** | Trace trigger → context → agent/model → tool calls → approvals → action → result. Preserve correlation IDs and redact secrets. | Platform/operations owner | SRE/operations, Security, AI steward | Run trace, audit logs |
| [ ] | **Incident / failure response** | Use existing incident, security, privacy, and major-incident processes. Correlate AI-specific cases. Define kill switch, containment, rollback, and human fallback. | Relevant incident/process owner | AI asset owner, platform owner, Security/Privacy | Incident runbook, AI case |
| [ ] | **Business continuity** | Define graceful degradation, manual fallback, critical dependencies, recovery expectations, and what happens when a provider/connector is unavailable. | Business/service owner | Platform owner, BCP/DR, operations | BCP/fallback runbook |
| [ ] | **Provider / vendor governance** | Review data use, retention, subprocessors, residency, security, model changes, portability, exit strategy, and contractual obligations. | Procurement / vendor owner | Legal, Privacy, Security, AI governance | Vendor assessment, contract |
| [ ] | **Usage / adoption** | Measure active users, actions, skills/tools used, repeat use, personas, and underused paid capability. Usage is not value by itself. | AI asset/product owner | AI steward, analytics owner | Adoption dashboard |
| [ ] | **Quality / reliability** | Measure task success, acceptance/edit/rejection, error rate, grounded accuracy, action failure, rework, and user feedback. | AI asset/platform owner | QA/eval owner, operations | Quality scorecard |
| [ ] | **Cost / FinOps** | Track model/assist/token cost, platform licenses, connector/runtime cost, support, maintenance, and human review. | Technology/AI portfolio owner | FinOps, Finance, Procurement, platform owners | Cost dashboard |
| [ ] | **Value / outcome realization** | Distinguish capacity released from hard-dollar savings. Track cycle-time, quality, revenue/experience, risk reduction, and outcome achievement. | Business/AI asset owner | Finance, analytics, process owner | Value template, outcome review |
| [ ] | **Governance cadence** | Run a defined portfolio rhythm: operational monitoring continuously, portfolio/value review periodically, risk/control review on cadence and material change. | AI governance lead / executive sponsor | AI steward, platform owners, Security, Finance | Governance calendar, review minutes |
| [ ] | **Training & adoption** | Train users, builders, approvers, executives, and support teams on intended use, limitations, verification, escalation, and platform choice. | Business/product owner | Change management, L&D, AI governance | Training plan, completion/adoption |
| [ ] | **Retirement / offboarding** | Disable triggers, revoke credentials/tools, remove user entry points, update inventory, apply retention, close licenses/vendor spend, and capture lessons. | AI asset owner | AI steward, platform owner, IAM, Procurement | Retirement checklist |
| [ ] | **Internal audit / independent assurance** | Periodically test whether controls operate as designed, especially for high-risk AI and automation. | Internal Audit / Risk governance | Security, AI governance, control owners | Audit/control testing results |

---

## Typical role map

### Executive / leadership
**CIO / CTO / VP / AI steering committee**
- Sets strategic direction and risk tolerance.
- Resolves material cross-functional decisions.
- Sponsors major investments.
- Does not normally administer individual agents.

### AI Governance / AI Steward
- Maintains portfolio visibility and lifecycle governance.
- Coordinates assessments, governance tasks, and managed/unmanaged disposition.
- Provides standards and escalation.
- Should not become the sole technical owner of every AI system.

### AI Asset / Product Owner
- Owns the business purpose, success criteria, lifecycle, adoption, and value.
- Accountable for whether the capability should continue to exist.

### Business / Process Owner
- Owns business rules and process outcomes.
- Decides what the automation should accomplish.
- Owns consequential business-policy decisions.

### Platform Owner / Architect
- Owns platform architecture, integration patterns, configuration standards,
  technical health, and platform-specific controls.
- Typically owns the technical implementation pattern for ServiceNow,
  Microsoft, Salesforce, GitHub, etc.

### Capability Owner
- Owns reusable deterministic actions such as `remove_user_access`,
  `create_change_draft`, or `provision_license`.
- Defines inputs, outputs, authorization, idempotency, audit, and versioning.

### Security / IAM / Privacy / Legal / Risk
- Own independent controls in their disciplines.
- Security/IAM: identities, permissions, threat controls.
- Privacy/Data: lawful/approved data handling.
- Legal: contractual/regulatory interpretation.
- Risk: control/risk assessment and acceptance processes.

### Engineering / Builder / Maintainer
- Implements, tests, monitors, documents, and remediates.
- Does not unilaterally set enterprise risk tolerance.

### Operations / SRE / Support
- Monitors runtime health.
- Handles operational incidents and failover/fallback.
- Maintains operational runbooks.

### Finance / FinOps / Procurement
- Validates cost, licensing, vendor economics, and realized financial value.
- Helps distinguish capacity savings from budget savings.

### Internal Audit
- Independently tests whether governance and controls operate as designed.

---

## Recommended governance cadence

| Cadence | Review | Typical participants |
|---|---|---|
| Continuous | Security/runtime monitoring, failures, spend anomalies | Operations, Security, platform owner |
| Per release/material change | Architecture, risk, evals, permissions, deployment approval | Asset owner, platform owner, Security/Risk as required |
| Monthly | AI portfolio, adoption, incidents, cost, duplicate capabilities | AI steward, platform owners, asset owners |
| Quarterly | Value, strategic placement, vendor/license optimization, risk posture | CIO/VP, AI governance, Finance, Security, platform leaders |
| Annually / policy change | Policy, standards, approved providers, control effectiveness | Executive sponsor, Security, Legal/Privacy, AI governance, Audit |
| Event-driven | Material incident, new sensitive data, autonomy increase, model/provider change | Relevant control owners |

---

## Lean-team interpretation

A small organization does **not** need a separate employee for every role.

For example, one platform owner might be:
- Responsible for architecture and implementation;
- the technical owner of the AI asset;
- the maintainer.

Their manager or business owner can still be:
- Accountable for business outcome and priority.

Security/IAM can remain:
- Accountable/consulted for identity and security controls.

The important practice is **explicit decision rights**, not organizational headcount.

---

## Reference principles

This checklist is designed to be consistent with broadly used enterprise AI
governance patterns:

- inventory AI systems and assign clear roles;
- govern the full lifecycle, including retirement;
- use named human accountability;
- make human oversight meaningful for consequential actions;
- continuously monitor after deployment;
- use risk-appropriate controls and independent specialist review.

Map the checklist to the organization's own AI policy, Security/Privacy standards,
AI Control Tower roles, and existing SDLC/change/incident processes before using
it as a production standard.
