# Personal Sandbox → Enterprise Candidate

## Why this exists

The personal sandbox is allowed to use a much richer engineering toolchain than
a constrained corporate workstation.

Examples:
- Codex;
- Claude Code;
- GitHub agent skills;
- frontend/design agents;
- Figma-related tooling;
- Python;
- Docker;
- n8n;
- local MCP servers;
- multiple model providers;
- experimental SDKs.

Those tools can help produce a **ServiceNow-native solution**.

The external tooling does not need to become part of the enterprise runtime.

## Pattern

```text
Personal R&D toolchain
        ↓
Personal ServiceNow PDI
        ↓
Working generic ServiceNow prototype
        ↓
Tests / ATF / documentation
        ↓
Export update set / application package
        ↓
ServiceNow Promotion Reviewer
        ↓
Enterprise Candidate Package
        ↓
Human adoption decision
        ↓
Work enterprise DEV
        ↓
Normal SDLC
```

## Clean-room boundary

Use:
- generic requirements;
- synthetic/personal data;
- generic branding;
- personal credentials;
- public/product documentation.

Do not put into the personal lab:
- employer secrets;
- production records;
- confidential architecture;
- internal credentials;
- restricted source code;
- private internal endpoints;
- proprietary datasets unless company policy explicitly permits it.

## Design for portability

Prefer:
- properties over hard-coded environment values;
- aliases over embedded credentials;
- logical capability names;
- configuration tables/lookups;
- scoped apps when appropriate;
- documented dependencies;
- ATF/test artifacts.

Avoid:
- personal sys_ids as business logic;
- localhost dependencies with no translation path;
- personal tenant IDs embedded in scripts;
- fixed users/groups;
- personal tokens.

## Candidate output

A successful experiment can graduate to:

```text
enterprise-candidate/<project>/
├── README.md
├── REQUIREMENTS.md
├── ARCHITECTURE.md
├── DEPENDENCIES.md
├── PORTABILITY.md
├── PROVENANCE.md
├── TEST_EVIDENCE.md
├── PROMOTION_REVIEW.json
└── artifact/
    └── update-set-or-app-package.xml
```

This is an adoption candidate, not a deployment request.
