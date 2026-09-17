# Enterprise Repo Boundary Reference

This document is relevant when translating the personal project back into an
enterprise setting.

## Do not make the ServiceNow repository the enterprise AI policy repository

Recommended boundaries:

### 1. Enterprise AI Operating Model repository

Example:

```text
enterprise-ai-operating-model
```

Owned by the appropriate cross-functional governance/architecture function.

Contains:
- enterprise AI reference architecture;
- workload placement principles;
- governance/RACI;
- common schemas;
- capability standards;
- authentication/security standards;
- AI lifecycle;
- common eval expectations;
- cost/value model;
- Control Tower alignment.

### 2. ServiceNow Platform repository

Example:

```text
servicenow-platform
```

Contains:
- ServiceNow implementation;
- ServiceNow-specific agents;
- Now Assist/AI Agent patterns;
- ServiceNow MCP config/docs;
- ServiceNow auth adapters;
- ADO/GitHub delivery automation;
- ATF/tests;
- ServiceNow architecture decisions;
- ServiceNow mapping to enterprise AI controls.

Its language should be:

> "This is how ServiceNow implements and aligns to enterprise AI standards."

Not:

> "This repository defines enterprise AI governance."

### 3. Other platform repositories

Examples:

```text
microsoft-ai-platform
salesforce-ai-platform
identity-automation
```

Each consumes the shared enterprise standard and implements platform-specific
patterns.

## If no central enterprise repo exists yet

Keep the full framework in a separate **reference/proposal repository**.

Do not silently declare it company policy.

Suggested name:

```text
enterprise-ai-operating-model-reference
```

Suggested README language:

> This repository is a reference architecture and implementation proposal used
> to evaluate and align AI/automation patterns. Existing enterprise policy,
> Security, Privacy, Architecture, and governance processes remain authoritative.
