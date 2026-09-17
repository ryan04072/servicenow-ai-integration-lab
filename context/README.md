# Enterprise Context Plane

## Principle

"Give the agent the full picture" does **not** mean paste every document,
work item, PR, and ServiceNow record into every prompt.

It means the agent can retrieve the **right authoritative context on demand**.

## Context layers

### 1. Platform context
ServiceNow:
- platform scope and licensed capabilities;
- architectural patterns;
- key integrations;
- CMDB/CSDM conventions;
- application/service ownership;
- relevant configuration metadata.

### 2. Delivery context
Azure DevOps:
- Epics, Features, Stories, Tasks;
- sprint/iteration;
- state and aging;
- blocked reason;
- assigned owner/vendor;
- acceptance criteria;
- roadmap linkage;
- validation/UAT status.

### 3. Repository context
GitHub:
- code;
- documentation;
- ADRs;
- PRs;
- reviews;
- CI results;
- changed files;
- release evidence.

### 4. Roadmap context
- objectives;
- themes;
- target outcomes;
- priority;
- target quarter/time horizon;
- dependencies;
- roadmap/BAU/technical-debt classification.

### 5. Operating-model context
- SDLC;
- human gates;
- Definition of Ready;
- Definition of Done;
- vendor process;
- change/release policy;
- security constraints.

### 6. Business context
- glossary;
- owners;
- decision records;
- known business constraints;
- explicitly approved priorities.

## Context rules

Every dynamic source should carry:

- source system;
- source identifier;
- retrieved timestamp;
- data owner when known;
- authority level;
- sensitivity;
- freshness expectation;
- read/write scope;
- evidence locator.

The agent must state when required context is unavailable or stale.

## Context assembly

Use `CONTEXT_ENVELOPE.md` as the normalized contract presented to specialist agents.
