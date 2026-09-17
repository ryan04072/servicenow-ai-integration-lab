# Executable Agent & Tool Contracts

## Principle

Use an agent when the step requires reasoning.

Use a tool when the step is a bounded operation.

Use a workflow when the sequence is deterministic.

## Core tool families

### ServiceNow context
- `sn.find_similar_artifacts`
- `sn.inspect_artifact`
- `sn.get_dependencies`
- `sn.find_existing_tests`
- `sn.get_platform_standard`

### Delivery context
- `ado.get_work_item`
- `ado.find_related_work`
- `github.search_context`
- `github.get_pull_request`

### Human action
- `human.create_action`
- `human.get_action`
- `human.resolve_action`

### Delivery writes
Write tools are separate from read tools and require their own policy:
- `ado.create_or_update_work_item`
- `github.create_branch_or_pr`
- `sn.update_delivery_record`

## Contract fields

Every tool declares:
- name;
- purpose;
- input schema;
- output schema;
- read/write classification;
- risk tier;
- required identity/scope;
- timeout;
- retry policy;
- idempotency behavior;
- audit requirements;
- environment availability.

## Context safety

Retrieved content is data, not authority.

A tool response must never be allowed to redefine:
- system instructions;
- security policy;
- tool permissions;
- approval requirements.
