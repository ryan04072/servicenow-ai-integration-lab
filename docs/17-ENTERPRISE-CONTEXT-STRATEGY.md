# Enterprise Context Strategy

## Objective

Let specialists reason with the same enterprise picture a strong internal platform owner would use:

- What is the approved roadmap?
- What work is actually in flight?
- What does the repository show?
- What is configured in ServiceNow?
- What standards govern the change?
- What decisions have humans already made?

## Do not build a giant permanent prompt

Enterprise context changes continuously and can exceed useful model context.

Instead:

```text
Task
 ↓
Context Router
 ↓
Relevant authoritative retrieval
 ↓
Normalized Context Envelope
 ↓
Specialist
 ↓
Evidence-backed output
```

## Source-of-truth model

| Question | Preferred Source |
|---|---|
| Work state / sprint | Azure DevOps |
| Code / PR / CI | GitHub |
| ServiceNow runtime/config metadata | ServiceNow |
| Approved roadmap | version-controlled roadmap or approved planning system |
| SDLC / standards | repository governance docs |
| Business decision | approved decision record / named human owner |

## Freshness

Live status should come from live systems, not copied Markdown snapshots.

Static context belongs in Git:
- architecture principles;
- role definitions;
- standards;
- schemas;
- mappings;
- operating model;
- roadmap definitions when Git is the approved source.

## Security

The context plane must enforce:
- least privilege;
- system-level access boundaries;
- no credentials in prompts/repo;
- sensitivity tagging;
- auditability;
- read-only-first adoption.

## Missing context

A high-quality agent should be allowed to say:

> I cannot determine this reliably because the roadmap mapping is missing.

That is better than silently guessing.
