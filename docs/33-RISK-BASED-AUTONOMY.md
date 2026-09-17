# Risk-Based Autonomy

## Principle

Autonomy should increase based on evidence and risk, not enthusiasm.

## R0 — read-only
Automatic analysis is acceptable.

## R1 — draft
AI can create drafts; human approves distribution/write.

## R2 — controlled nonproduction
AI can perform bounded writes in approved DEV/repository boundaries with review.

## R3 — security / architecture sensitive
AI analyzes/plans; explicit owners approve.

## R4 — production / destructive
No autonomous write.

## Why deterministic policy

An LLM may help classify risk, but the workflow must enforce the gate using
configuration/policy.

The model cannot waive its own approval requirement.
