# Cross-System Context Envelope

## Why an envelope?

Specialists should not independently query every system in different ways.

The Context Router assembles a bounded, evidence-backed envelope for the current
decision.

## Standard envelope

```text
Identity
- request / story / run / correlation IDs

Requirement
- normalized request
- acceptance criteria
- unresolved questions

Current State
- relevant ServiceNow artifacts
- dependency neighborhood
- live evidence / freshness

Approved Reference
- platform standards
- ADRs
- approved architecture/documentation

Delivery Context
- relevant ADO history
- GitHub implementation/docs
- roadmap/dependencies

Precedent
- prior decisions
- accepted/rejected patterns

Constraints
- risk tier
- permissions
- tool availability
- licensing
- environment

Human Decisions
- approvals / clarifications already made

Evidence
- source IDs / locators / timestamps

Uncertainty
- unresolved questions
- confidence
```

## Context minimization

The goal is:

> maximum **relevant authoritative** context, not maximum volume.

Large raw instance dumps should not be pushed into model context.

The context service retrieves candidates, ranks them, expands only relevant
dependencies, and includes source references.

## Required architecture behavior

Before proposing a design, the architect should explicitly state:

- current implementation evidence;
- approved standard/reference;
- gap;
- reuse/extend/new-build options;
- tradeoffs;
- recommendation;
- unresolved questions;
- human decision required.
