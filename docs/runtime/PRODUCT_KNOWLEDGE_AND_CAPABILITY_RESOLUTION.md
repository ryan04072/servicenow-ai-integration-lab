# Product Knowledge & Capability Resolution

## Why this layer exists

Instance discovery answers:

> What do we have?

Product knowledge answers:

> What does ServiceNow support?

Capability resolution answers:

> Given both, what implementation paths should we consider?

All three are required to avoid automating poor architecture.

## Architecture

```text
Requirement
    ↓
Domain classifier
    ↓
┌─────────────────────────────────────┐
│ Live ServiceNow Context             │
│ - existing catalog/flows/scripts    │
│ - installed apps/spokes             │
│ - configured integrations           │
│ - existing tests                    │
└─────────────────────────────────────┘
    +
┌─────────────────────────────────────┐
│ Product Knowledge                   │
│ - official ServiceNow Docs          │
│ - Store / release notes             │
│ - Developer documentation           │
│ - approved vendor product docs      │
└─────────────────────────────────────┘
    +
┌─────────────────────────────────────┐
│ Enterprise Reference                │
│ - licensing/entitlement             │
│ - approved standards                │
│ - security constraints              │
│ - prior decisions                   │
└─────────────────────────────────────┘
    ↓
Capability Resolver
    ↓
Options + evidence + unknowns
    ↓
Architect
```

## SharePoint example

Requirement:

> Automate creation/management of content in SharePoint from ServiceNow.

The resolver should ask:

1. Do we already have a ServiceNow↔SharePoint integration?
2. Is the Microsoft SharePoint Online Spoke installed?
3. Is Integration Hub available/entitled for the target environment?
4. Which official spoke actions/subflows satisfy the requirement?
5. What version/release documentation supports that?
6. Is the spoke configured with an approved connection?
7. Are there internal standards requiring use of IntegrationHub/spokes?
8. Does the requirement exceed the OOB spoke's capabilities?

Possible result:

```text
Option A — Reuse existing configured SharePoint spoke action
Option B — Extend/build reusable action in approved spoke pattern
Option C — Custom REST implementation
```

The resolver should prefer A/B when they satisfy the requirement, but it must not
claim they are usable until entitlement/install/configuration are verified.

## Runtime implementation patterns

### Enterprise

Preferred:
- curated/indexed copy of approved official documentation;
- scheduled refresh;
- live target-instance inventory;
- approved web/product lookup only when permitted;
- citations/evidence persisted with the decision.

This reduces dependence on unrestricted internet browsing during every run.

### Personal lab

Can additionally use:
- live web search;
- local documentation index;
- embeddings/vector retrieval;
- experimental product-document crawlers;
- multiple vendor documentation sources.

The logical evidence contract stays the same.
