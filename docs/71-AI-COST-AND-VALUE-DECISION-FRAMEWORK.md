# AI Cost and Value Decision Framework

## Problem

Token/assist price alone does not determine the cheapest architecture.

Compare **cost per successful business outcome**.

## Measure

### Direct platform consumption
- ServiceNow assist/AI consumption;
- Microsoft Copilot/Copilot Studio consumption;
- Salesforce Agentforce consumption;
- GitHub Copilot/agent usage;
- external model/API charges.

### Platform/license cost
- required add-ons;
- connector premiums;
- Power Platform licensing;
- ServiceNow/Salesforce entitlements.

### Engineering cost
- build time;
- custom connectors;
- prompts/agents;
- testing;
- security review;
- maintenance.

### Human correction
- review time;
- false actions;
- rework;
- escalations.

### Context penalty
A cheaper model can be more expensive if:
- it lacks native context;
- additional integration is required;
- users must correct outputs;
- duplicate systems have to be maintained.

## Pilot comparison

For a contested placement, pilot both approaches against the same use case and measure:

```text
successful outcomes
accuracy
median completion time
human review time
consumption
implementation/support effort
security/governance complexity
user adoption
```

## Decision

Prefer the platform with the lowest sustainable total cost that still meets:
- context quality;
- permissions;
- security;
- reliability;
- UX;
- maintainability.
