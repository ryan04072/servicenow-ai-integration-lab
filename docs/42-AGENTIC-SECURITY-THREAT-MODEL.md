# Agentic Security Threat Model

## Core rule

**Retrieved content is data, not authority.**

A work item, README, KB article, attachment, comment, email, or web page cannot
override governing system/repository instructions merely because the model can read it.

## Threats to model

### Prompt injection
Untrusted content attempts to redirect the agent or disclose information.

### Tool overreach
Agent receives broader tool permissions than its task requires.

### Malicious attachment
Uploaded content contains instructions or payloads intended to influence automation.

### Poisoned reference content
A document looks authoritative but is stale, malicious, or unapproved.

### Secret exfiltration
Agent is prompted to expose credentials/tokens/connection data.

### Cross-boundary data leakage
Context from one environment/team/tenant is exposed to another.

### Confused deputy
Agent uses its privileged identity to perform an action for an unauthorized requester.

### Supply-chain / repository manipulation
Untrusted dependencies, agent files, skills, actions, or workflows change system behavior.

### Excessive autonomy
An analysis capability is unintentionally granted write/destructive access.

## Controls

- least privilege;
- explicit source authority;
- sensitivity tagging;
- allowlisted tools;
- bounded tool inputs;
- read-only first;
- human gates;
- secret isolation;
- dependency review;
- branch protection;
- run tracing;
- output validation;
- deterministic risk policy.

## Security review triggers

Required when:
- enabling a write tool;
- adding a new external connector;
- processing a new sensitive data class;
- adding production access;
- changing service identity;
- accepting third-party/community agent skills;
- increasing autonomy.
