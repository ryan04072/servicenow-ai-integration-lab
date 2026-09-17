# Agent and Configuration Lifecycle

## Treat agents as software

The following are configuration/code artifacts:

- agent role definitions;
- prompts;
- tool definitions;
- MCP server configuration;
- schemas;
- risk policy;
- routing rules;
- evaluation cases;
- reference standards;
- orchestration pipelines.

Changes should follow:

```text
Issue / Requirement
      ↓
Feature Branch
      ↓
Change
      ↓
Eval / Test
      ↓
Pull Request
      ↓
Human Review
      ↓
Merge
      ↓
Promotion
      ↓
Observe
```

## Versioning

Material agent behavior changes should be traceable to:
- repository commit;
- agent/profile version where available;
- model/provider configuration;
- tool version;
- prompt/role version;
- evaluation result.

## Change classes

### Documentation only
Normal PR.

### Behavioral change
PR + relevant golden-task evals.

### Tool/permission change
PR + security/tool-governance review.

### Risk-policy change
PR + platform/governance approval.

### Production autonomy change
Formal promotion review.

## Rollback

Every deployed behavior change must have a documented rollback path:
- prior repository version;
- prior runtime configuration;
- disabled workflow;
- removed tool permission.
