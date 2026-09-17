# Feedback, Precedent, and Organizational Learning

## Goal

Let the system improve from human decisions without allowing uncontrolled
self-modification.

## Capture loop

```text
Agent recommendation
      ↓
Human review
      ↓
Accepted / Modified / Rejected
      ↓
Reason + final decision
      ↓
Precedent store
      ↓
Future retrieval
```

## Do not

- rewrite prompts automatically after every rejection;
- infer a global policy from one review;
- retain sensitive free-form comments unnecessarily;
- allow precedent to override a newer approved standard.

## Promote precedent to policy

When a pattern repeats and should become standard:

```text
precedent
  ↓
human proposal
  ↓
ADR / standards PR
  ↓
review
  ↓
merge
```

That keeps learning governed and auditable.
