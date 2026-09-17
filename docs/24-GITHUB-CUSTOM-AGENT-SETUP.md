# GitHub Custom-Agent Setup

## Why GitHub agents

Use GitHub custom agents for repository-aware specialist work: code, PRs,
documentation, architecture files, tests, and repository evidence.

Do not use GitHub agents as the sole event-driven enterprise orchestration runtime.

## Repository-level setup

1. Create/checkout the feature branch.
2. Place agent profiles under:

```text
.github/agents/
```

3. Commit the canonical role under:

```text
agents/roles/
```

4. Keep the `.github/agents/*` file thin.
5. Put shared rules in:
   - `AGENTS.md`
   - `.github/copilot-instructions.md`
   - `.github/instructions/*.instructions.md` for path-specific rules.
6. Commit and merge to the default branch after review.
7. Refresh Copilot agents and test the agent against a controlled repository task.

## Organization-level reuse

When a role has proven useful across teams, promote it to the organization
`.github` or `.github-private` repository under `/agents`.

Do not start organization-wide. Prove repository-level behavior first.

## Tool restriction

Explicitly constrain tools for read-only reviewers.

Example:

```yaml
---
name: Policy & Standards Guardian
description: Reviews design against approved standards and evidence.
tools: ["read", "search"]
---
```

For an implementation agent, add edit capability only when the repository and
branch protections are ready for it.

## MCP

GitHub custom agent profiles can be configured with MCP servers/tools where the
enterprise GitHub configuration permits it.

Do not embed secrets in an agent profile.

## Acceptance test for every agent

- [ ] Correctly explains its scope.
- [ ] Refuses/defers work outside scope.
- [ ] Finds relevant repository standards.
- [ ] Does not invent missing company facts.
- [ ] Preserves evidence links/identifiers.
- [ ] Respects tool limitations.
- [ ] Produces output in the required schema/template.
- [ ] Passes golden-task evals.
