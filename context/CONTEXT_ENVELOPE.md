# Context Envelope

A context envelope is the normalized task packet supplied to a specialist.

## Header

```yaml
task_id:
task_type:
requested_by:
generated_at:
environment:
sensitivity:
```

## Objective

What question must the agent answer?

## Required decisions

What decision(s), if any, must be made by a human?

## Context sources

For each source:

```yaml
- system:
  id:
  title:
  authority:
  retrieved_at:
  freshness:
  evidence_locator:
  allowed_use:
```

## Relevant facts

Facts extracted from authoritative sources.

Do not insert unsupported model assumptions here.

## Known constraints

- security
- licensing
- architecture
- roadmap
- capacity
- business deadlines
- human gates

## Unresolved questions

Questions that block a reliable recommendation.

## Output contract

Reference the schema expected from the agent.

## Tool permissions

```yaml
read:
write:
approval_required:
forbidden:
```
