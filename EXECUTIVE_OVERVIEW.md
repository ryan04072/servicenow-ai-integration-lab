# Enterprise AI & Automation Operating Model — Executive Overview

## Purpose

This repository is a reference operating model for governing, designing, building,
operating, measuring, and continuously improving enterprise AI and automation.

ServiceNow is the primary reference implementation, but the model is designed to
extend to Microsoft, Salesforce, GitHub, identity platforms, and other enterprise systems.

## Executive design principles

1. **One governed AI portfolio** — AI systems, agents, models, prompts, tools, and
   material workflows should be inventoried and owned.
2. **One business capability, many AI surfaces** — deterministic business logic
   belongs in the authoritative platform; assistants invoke it rather than duplicate it.
3. **Federated ownership with centralized standards** — enterprise AI/Security
   establishes guardrails while platform and business owners own their assets/outcomes.
4. **Native context first** — use platform-native AI where platform metadata,
   permissions, actions, and transaction context materially improve safety or quality.
5. **Progressive autonomy** — read → recommend → supervised action → policy-bounded automation.
6. **AI is part of the SDLC** — not a parallel SDLC.
7. **Value must be measurable** — adoption, quality, reliability, cost, capacity,
   realized financial value, and risk reduction.
8. **Every asset has an accountable owner** — AI itself is never accountable.
9. **Security and observability are runtime requirements** — identity, permissions,
   audit, kill switch, incident response, and rollback are designed before autonomy.
10. **Retire what no longer provides value** — offboarding is part of the lifecycle.

## System-of-record boundaries

```text
Enterprise AI policy / risk tolerance
              │
              ▼
      AI Control Tower / Governance
  inventory • lifecycle • risk • security
     monitoring • value • ownership
              │
              ▼
      AI & Automation Operating Model
 standards • placement • capability contracts
     risk tiers • SDLC • evals • runbooks
              │
     ┌────────┼───────────┬───────────┐
     ▼        ▼           ▼           ▼
ServiceNow  Microsoft   Salesforce   GitHub
 AI/runtime  AI/runtime   AI/runtime  engineering
     │        │           │           │
     └────────┴───────────┴───────────┘
              ▼
     Shared governed capabilities
              ▼
       Systems of record/action
```

## Closed loop

```text
Demand → Intake → Portfolio/Placement → Risk/Architecture → Build/Test
→ Deploy → Observe/Secure → Measure Cost/Value → Improve/Retire → next cycle
```
