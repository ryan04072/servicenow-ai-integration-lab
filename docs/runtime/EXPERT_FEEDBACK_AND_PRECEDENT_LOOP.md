# Expert Feedback → Context → Precedent Loop

## Case-level behavior

```text
Agent uncertainty
      ↓
specific question
      ↓
Human Action Broker
      ↓
Teams free-text card
      ↓
expert response
      ↓
validate responder
      ↓
write response to authoritative record
      ↓
append normalized human decision/fact to Context Envelope
      ↓
resume agent from checkpoint
```

## Example

Agent asks:

> I found two existing approval patterns. Is application-owner approval required
> for this software family, or should the standard manager-only path be used?

You respond in Teams:

> Use manager approval only when the user already has an Adobe entitlement;
> otherwise require both manager and application owner.

The response becomes **case context**.

It does not automatically become a permanent standard.

## Learning after the case

After completion, Feedback/Precedent Curator evaluates whether the response is:

- one-off;
- reusable precedent;
- candidate architecture standard;
- candidate eval case.

If repeated/material:

```text
precedent
→ proposed ADR/standard
→ human review
→ merge
→ future Context Envelopes
```

This gives the system durable expert knowledge without uncontrolled self-modification.
