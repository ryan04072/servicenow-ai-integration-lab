# Team Replication Kit

## What every adopting team provides

```text
TEAM_CONTEXT.md
ROADMAP.yaml
SOURCE_SYSTEM_MAP.yaml
TOOL_REGISTRY.yaml
RISK_OVERRIDES.yaml
SDLC_POLICY.md
REPOSITORY_MAP.yaml
BUSINESS_GLOSSARY.md
AGENT_ADAPTERS/
EVALS/
```

## What stays shared

- normalized intake contract;
- context-envelope contract;
- evidence model;
- risk model;
- human-gate model;
- observability schema;
- precedent schema;
- core control-plane roles.

## Example

ServiceNow team:

```text
Core Control Plane
     +
ServiceNow Architect
ServiceNow MCP
ADO mapping
ServiceNow SDLC
```

Microsoft team:

```text
Core Control Plane
     +
Microsoft Platform Architect
Microsoft connectors
ADO mapping
Microsoft SDLC extensions
```

## Promotion path

1. Prove in one ServiceNow repository.
2. Extract genuinely reusable pieces.
3. Test with second team.
4. Only then publish organization-level agents/policies.
