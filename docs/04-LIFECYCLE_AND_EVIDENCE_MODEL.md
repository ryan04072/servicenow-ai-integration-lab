# Lifecycle & Evidence Model

## State Machine
The lifecycle is defined in `config/lifecycle/lifecycle.json`.

The LLM does not invent lifecycle state.

## Evidence Contract
Each meaningful work package captures:

```text
ServiceNow Intake
ADO Work Item
GitHub Branch
GitHub PR
Build / Test
ServiceNow Change
Release
As-Built
```

## Rule
Identifiers propagate forward. Later agents must not rediscover or guess relationships.

## Small Changes
Do not force trivial experiments through the full state machine. Use the model for changes where lifecycle evidence teaches something or protects quality.
