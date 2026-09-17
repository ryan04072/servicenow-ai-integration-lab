# Target Operating Model v2

## Purpose

Create one replicable enterprise delivery system that can support:

- ServiceNow;
- Microsoft/platform teams;
- future enterprise applications;
- vendors;
- internal engineers;
- AI-assisted delivery.

## Shared control plane

Every team implementation supplies:

```text
1. Platform context
2. Roadmap context
3. SDLC/policies
4. Tool registry
5. Risk/approval matrix
6. Agent catalog
7. Source-system adapters
8. Evaluation suite
```

The team-specific agents are adapters around this shared control plane.

## Work lifecycle

```text
Front Door
  ↓
AI clarification / normalization
  ↓
Human intake approval
  ↓
Backlog / roadmap classification
  ↓
Architecture / standards review
  ↓
Human architecture gate
  ↓
Implementation
  ↓
PR / technical review
  ↓
Testing / validation
  ↓
Change / release
  ↓
Post-release validation
  ↓
As-built / precedent / metrics
```

## Control-plane agents

These should remain broadly reusable:

- Context Curator
- Intake Router
- Policy & Standards Guardian
- Tool Governance Advisor
- Engineering Manager
- Historical Delivery Analyst
- Run Observability Auditor
- Feedback & Precedent Curator

## Platform specialists

Examples:
- ServiceNow Architect
- Azure DevOps Expert
- GitHub Expert
- Microsoft Platform Architect
- Salesforce Architect

## Principle

Replicate **interfaces and governance**, not blindly copy prompts.

A Microsoft team can consume the same intake, risk, evidence, approval, and
observability contracts while using different platform specialists.
