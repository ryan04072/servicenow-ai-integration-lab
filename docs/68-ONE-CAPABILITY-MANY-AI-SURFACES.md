# One Capability, Many AI Surfaces

## Problem to avoid

```text
Now Assist custom agent
  └─ custom group-removal logic

Copilot Studio agent
  └─ different group-removal logic

Power Automate
  └─ third version

Identity platform
  └─ fourth version
```

This creates:
- inconsistent controls;
- duplicated maintenance;
- audit gaps;
- drift;
- conflicting business rules.

## Preferred pattern

```text
Authoritative capability
        ↓
Stable contract
        ↓
Governed tools/adapters
   ┌────┼─────┐
   ▼    ▼     ▼
Now   Copilot Agentforce
Assist Studio
```

## Capability contract

Every reusable enterprise action should define:
- name;
- purpose;
- authoritative owner;
- inputs;
- outputs;
- validation;
- idempotency;
- authorization;
- approval;
- audit;
- failure behavior;
- version.

## Examples

### Identity

Capability:
`remove_user_access`

Owner:
IGA/Identity team.

Potential implementation:
Saviynt workflow/API, Entra automation, or approved identity orchestration.

Consumers:
- ServiceNow Now Assist;
- ServiceNow automated termination;
- Copilot Studio;
- human workflow.

### ServiceNow

Capability:
`create_standard_change_draft`

Owner:
ServiceNow platform.

Implementation:
ServiceNow subflow/action.

Consumers:
- Now Assist;
- Copilot Studio via ServiceNow MCP;
- another internal integration.

## Benefit

Changing the business logic once updates every AI surface.
