# Personal Sandbox → Enterprise Translation

The personal lab can implement the complete runtime with tools unavailable at
work.

That is intentional.

## Personal implementation may use

- local Python;
- Docker;
- local databases/vector stores;
- Codex;
- Claude Code;
- GitHub skills;
- MCP servers;
- experimental agent frameworks;
- Build Agent in the PDI;
- other personal services.

## Enterprise candidate must describe

```text
Capability
Personal implementation
Enterprise-compatible implementation option
Runtime dependencies
Portable ServiceNow artifacts
What must be rebuilt/configured at work
```

The personal implementation is an R&D reference, not an assumption that the same
runtime/tooling can be installed in the enterprise.

Preserve the logical contracts:
- Context Service;
- tool names;
- Human Action;
- Context Envelope;
- orchestration events;
- evals.

Swap the adapters/runtime.
