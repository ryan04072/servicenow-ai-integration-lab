
# Authentication Gate Added in v2.2

Before Phase 2 live connections:

- [ ] Read `docs/54-AUTHENTICATION-AND-MACHINE-IDENTITY-STANDARD.md`.
- [ ] Select authentication using `docs/55-AUTHENTICATION-DECISION-MATRIX.md`.
- [ ] Complete `checklists/NEW_INTEGRATION_SECURITY_GATE.md`.
- [ ] Submit `docs/58-SECURITY-REVIEW-REQUEST-PACKET.md` where required.
- [ ] Prefer application/workload identities over user-style service accounts.
- [ ] If the preferred mechanism is unavailable, use the documented fallback process.
- [ ] Do not create broad service accounts/PATs merely to accelerate the pilot.
- [ ] Keep the first live connection read-only in nonproduction.

---


# Operational-Control Prerequisites Added in v2.1

Before enabling **event-driven writes or production use**, complete the following
in addition to the phases below:

- [ ] Map the existing enterprise AI policy using `config/governance/ai-policy-map.template.yaml`.
- [ ] Define identity/service-account ownership.
- [ ] Complete the agentic security threat model.
- [ ] Map data classification and retention requirements.
- [ ] Define retry/idempotency behavior.
- [ ] Establish a kill switch and human fallback.
- [ ] Populate the decision-rights/RACI matrix.
- [ ] Establish baseline SLO/quality metrics.
- [ ] Define provider outage/fallback behavior.
- [ ] Define requester communication states.
- [ ] Define post-release outcome measurement for applicable work.

These are **implementation controls**, not a replacement for enterprise AI policy.

---

# Phased Implementation Runbook

Do not deploy the entire autonomous model in one release.

## Phase 0 — Repository foundation

Goal: make the operating model reviewable before connecting live systems.

Tasks:
- [ ] Create `feature/enterprise-agentic-operating-model-v2`.
- [ ] Merge canonical roles and schemas.
- [ ] Add source-authority policy.
- [ ] Add risk/approval policy.
- [ ] Populate initial ServiceNow engineering standards.
- [ ] Populate roadmap template.
- [ ] Populate Azure DevOps field map.
- [ ] Populate repository map.
- [ ] Review with platform owner / manager.
- [ ] Merge only after the operating model itself is accepted.

Exit:
- repository accurately describes how work should flow;
- no live autonomous integration required.

## Phase 1 — GitHub specialist bench

Goal: create useful, bounded repo specialists.

Start with:
- [ ] GitHub Expert
- [ ] Policy & Standards Guardian
- [ ] PR Reviewer / Code Reviewer
- [ ] Test Engineer
- [ ] Documentation Engineer
- [ ] Engineering Manager

Keep tool access conservative.

Exit:
- agents can review a synthetic/sample PR and cite repository standards;
- agents identify missing context instead of guessing.

## Phase 2 — Read-only enterprise context

Goal: connect live context without enabling writes.

### ServiceNow
- [ ] Confirm MCP Server Console availability/entitlement.
- [ ] Validate patch/support requirements for desired MCP tool categories.
- [ ] Create an engineering-context MCP server.
- [ ] Create read-only tools for bounded use cases.
- [ ] Configure client authorization/OAuth for approved client.
- [ ] Test tools in subproduction first.
- [ ] Record tools in the tool registry.

### Azure DevOps
- [ ] Configure approved read access.
- [ ] Map work-item/custom fields.
- [ ] Validate current-sprint query.
- [ ] Validate backlog/roadmap relationships.

### GitHub
- [ ] Configure repository/PR read access as approved.
- [ ] Test PR/CI evidence retrieval.

Exit:
- Context Curator can assemble a source-stamped context envelope.

## Phase 3 — Delivery intelligence

Goal: use read-only context for management and platform-owner leverage.

- [ ] Executive brief
- [ ] Roadmap alignment
- [ ] Delivery-flow analysis
- [ ] Validation queue analysis
- [ ] Historical delivery metrics
- [ ] Compare AI output to human summary for several sprints.
- [ ] Track factual errors and missing context.

Exit:
- agreed accuracy threshold;
- leadership brief is useful without manual rework beyond normal review.

## Phase 4 — Intelligent front door

Goal: AI performs clarification before work enters the backlog.

- [ ] Shared intake form/record.
- [ ] Intake Router.
- [ ] Business interview.
- [ ] IT interview.
- [ ] Technical interview.
- [ ] Duplicate search.
- [ ] Roadmap suggestion.
- [ ] Story/AC draft.
- [ ] Human approval before backlog entry.

Exit:
- intake quality measurably improves;
- no final priority is assigned autonomously.

## Phase 5 — Event-driven orchestration

Goal: stop relying on a human to manually start every analysis.

- [ ] Approved event trigger.
- [ ] Orchestrator invokes read-only context.
- [ ] Agent produces draft.
- [ ] Human-in-loop approval.
- [ ] Approved action writes to backlog / sends internal brief.
- [ ] Trace run and correlation ID.

Exit:
- autonomous pre-work, human-owned decisions.

## Phase 6 — Controlled nonproduction writes

Examples:
- create feature branch;
- create PR draft;
- draft/update ADO work item;
- approved DEV-only ServiceNow actions.

Apply R2/R3 gates.

Exit:
- write actions are auditable, reversible, and bounded.

## Phase 7 — Mature multi-team pattern

- [ ] Extract organization-level GitHub agents where appropriate.
- [ ] Publish shared schemas/policies as platform engineering standards.
- [ ] Add team-specific context adapters.
- [ ] Establish central eval suite.
- [ ] Establish change process for agent/policy updates.

## Phase 8 — Higher autonomy

Only after evidence.

Never interpret "higher autonomy" as removing accountability.
