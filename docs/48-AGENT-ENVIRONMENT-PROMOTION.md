# Agent Environment Promotion

## Treat the AI operating model like a production platform

Suggested stages:

```text
Development
   ↓
Evaluation
   ↓
Pilot
   ↓
Production
```

## Development

- synthetic data;
- local/repository changes;
- limited tools;
- no production write.

## Evaluation

- golden tasks;
- adversarial/security tests;
- controlled real examples where policy permits;
- reviewer comparison.

## Pilot

- bounded audience;
- human-reviewed output;
- limited data/tool scope;
- explicit support owner.

## Production

- approved identity;
- approved data classification;
- run tracing;
- kill switch;
- SLOs;
- support model;
- incident process;
- rollback.

## Promotion artifact

Every promotion should record:
- version/commit;
- model/runtime;
- tools;
- permissions;
- eval result;
- risks;
- owner;
- approval.
