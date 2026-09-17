# AI-Built ServiceNow Documentation & Explainability Standard

## Objective

Prevent a future state where:

> "The agents built it, but nobody knows why it was designed that way or how it works."

Every material AI-built change must be reconstructable from evidence.

## Four documentation layers

### 1. Build Record — "What happened?"

One record per material implementation.

Contains:
- requirement;
- context/evidence;
- chosen architecture;
- affected artifacts;
- quality/test evidence;
- human actions;
- documentation links.

### 2. Decision Record — "Why this design?"

Contains:
- options;
- evidence;
- tradeoffs;
- selected path;
- concise rationale;
- rejected alternatives;
- consequences.

Do **not** store private model chain-of-thought.

### 3. Technical As-Built — "How does it work?"

GitHub Markdown is the canonical home for deep technical/platform documentation:

- architecture;
- flow/data sequence;
- scripts/configuration;
- integrations/authentication;
- dependencies;
- test evidence;
- deployment;
- rollback;
- operational detail.

### 4. Audience documentation — "How do I use/support it?"

ServiceNow Knowledge/QRG/CRG/fulfiller documentation and operational runbooks are
derived from validated as-built behavior for the appropriate audience.

## Required traceability

```text
Request / ADO
   ↓
Context Envelope / evidence
   ↓
ADR / Decision Rationale
   ↓
Implementation manifest
   ↓
Code/config review
   ↓
ATF/test evidence
   ↓
Release/change
   ↓
Technical as-built
   ↓
KB/QRG/runbook
```

## GitHub documentation minimum for a material capability

- overview / purpose;
- requirement/outcome;
- architecture;
- why this design;
- options rejected;
- artifacts/components;
- dependencies;
- authentication/security;
- execution/data flow;
- configuration;
- testing;
- operations;
- rollback;
- known limitations;
- links to decision/test/release evidence.

## Reviewability

The Platform Owner should be able to open the repository months later and answer:

- what did we build?
- why?
- what does it depend on?
- why did we not use the other approach?
- what changed from the original architecture?
- how do I test it?
- how do I support it?
- how do I turn it off?
