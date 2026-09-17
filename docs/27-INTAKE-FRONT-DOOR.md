# Agnostic Intake Front Door

## Recommendation

Use **one canonical intake record** with adaptive AI clarification.

Do not require every requester to complete a technical attachment.

Attachments are optional supporting evidence.

## Shared front-door questions

Ask only:

1. What problem/opportunity are you trying to address?
2. What outcome do you want?
3. Who/process is affected?
4. Is there a required date or constraint?
5. How will we know it worked?

The Intake Router then selects:

```text
Business
IT
Technical
```

## Business route

Ask about:
- current process;
- pain/opportunity;
- business impact;
- users;
- sponsor;
- success measure.

Do not ask for implementation.

## IT route

Ask about:
- systems;
- environment;
- dependencies;
- access/security;
- operational impact.

## Technical route

Ask about:
- current vs desired behavior;
- component/table/API;
- logs/evidence;
- dependencies;
- compatibility;
- tests.

## Normalization

Every route ends in `schemas/normalized-intake.schema.json`.

That canonical contract drives:
- duplicate search;
- roadmap analysis;
- architecture review;
- backlog draft;
- acceptance criteria;
- risk tier;
- human triage.

## Optional complex-change attachment

Use `intake/ARCHITECTURE_ATTACHMENT.template.md` only when warranted.
