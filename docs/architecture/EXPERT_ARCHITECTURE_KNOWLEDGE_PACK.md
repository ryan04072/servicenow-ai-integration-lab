# Expert Architecture Knowledge Pack

## Objective

Use scarce senior/MTA/architect time to improve the **system**, not manually
pre-review every low-risk story.

## Pack contents

```text
Approved engineering standards
Reference architectures
ADRs
Known anti-patterns
Exception patterns
Golden requirements/evals
Platform constraints
Integration patterns
Security/identity patterns
Reusable catalog/flow patterns
```

The Context Service makes the relevant subset available before architecture/build.

## Human expert escalation

Escalate when:
- no approved pattern fits;
- standards conflict;
- risk crosses policy threshold;
- context confidence is insufficient;
- agent proposes material net-new platform architecture;
- repeated review/test failure occurs.

## Feedback loop

Expert response:
1. resolves the case;
2. is captured as a Human Decision;
3. may become precedent;
4. can later be proposed as an ADR/standard/eval.

This approximates the value of expert architectural oversight without requiring
an expert to manually touch every low-risk task.
