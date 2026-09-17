# Personal Governance Lite

## Keep

- Git/version history;
- secrets out of source;
- scoped credentials;
- tests/evals;
- run trace;
- bounded tools;
- idempotency for writes;
- rollback;
- kill switch/disable path;
- capability ownership;
- one capability / many surfaces;
- cost awareness;
- failure testing.

## Drop or simplify

You do not need:
- steering committee approval;
- separate AI steward;
- Procurement review;
- formal CAB for PDI;
- multi-person RACI;
- quarterly governance council;
- formal residual-risk acceptance;
- AI Control Tower as a prerequisite;
- production SLA/SLO for disposable experiments.

## One-person RACI

You are normally:
- asset owner;
- business owner;
- platform owner;
- architect;
- engineer;
- tester;
- approver;
- support.

Instead of simulating bureaucracy, explicitly switch mental hats:

```text
Builder: "Can I make it work?"
Architect: "Is this the right design?"
Security reviewer: "What can it access/do?"
Tester: "How does it fail?"
Product owner: "Did it solve the problem?"
Operator: "Can I detect, stop, and recover it?"
```
