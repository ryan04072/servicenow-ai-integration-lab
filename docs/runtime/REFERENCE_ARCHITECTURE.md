# Agentic Delivery Runtime — Complete Reference Architecture

## Purpose

This package now contains a concrete reference implementation for the missing
runtime layer between **agent definitions** and **real platform work**.

The design answers seven questions:

1. How do agents know what exists in the ServiceNow instance?
2. How are relationships/dependencies represented?
3. How is ServiceNow + Azure DevOps + GitHub + standards context assembled?
4. What starts an orchestration and how does it progress?
5. How does a human learn that an agent needs a decision?
6. What tools can agents actually invoke?
7. How do we measure whether the system is working well?

## Runtime architecture

```text
TRIGGERS
Catalog / ADO / GitHub / Event / Schedule / Chat
                         │
                         ▼
                 EVENT NORMALIZER
                         │
                         ▼
                DELIVERY ORCHESTRATOR
                 state + policy + risk
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
   CONTEXT SERVICE   SPECIALISTS     HUMAN ACTION
          │            / TOOLS          BROKER
          │                               │
          ▼                               ▼
   DEPENDENCY GRAPH                    TEAMS
          │                               │
          ├──────────────┐                │
          ▼              ▼                ▼
   ServiceNow       ADO / GitHub      AUTHORITATIVE
   live context      context           WRITEBACK
          │              │                │
          └──────────────┼────────────────┘
                         ▼
                  CONTEXT ENVELOPE
                         │
                         ▼
               AGENT / TOOL EXECUTION
                         │
                         ▼
                 TELEMETRY + EVALS
```

## Core rule

No architecture agent should reason from an isolated user story when relevant
platform context is available.

The normal sequence is:

```text
Requirement
→ discover current state
→ discover dependencies
→ retrieve delivery/standards context
→ assemble Context Envelope
→ reason
→ request human action when required
→ execute bounded tools
→ trace/evaluate
```

## Source authority

Current implementation and approved design intent are separate concepts.

```text
Current State
  live instance / executable artifacts

Approved Reference
  architecture standards / ADRs / approved documentation

Delivery History
  ADO / GitHub / prior changes

Human Facts
  explicitly supplied information

Model Analysis
  derived reasoning
```

The agent must identify conflicts rather than blindly copying prevalent technical
debt.

## This is a reference runtime

The included Python runtime is deliberately dependency-light and runnable against
synthetic fixtures. It proves the contracts, state machine, context assembly,
human-action model, and telemetry.

Production adapters still require the organization's actual:
- credentials;
- endpoints;
- scopes;
- connection mechanisms;
- table/API decisions;
- Teams/Copilot implementation;
- ADO/GitHub authorization.

Those environment-specific values are not embedded in this repository.
