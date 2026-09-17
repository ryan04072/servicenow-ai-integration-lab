# ServiceNow Instance Discovery Model

## Objective

Create a task-relevant evidence graph rather than granting an agent unrestricted
ability to browse the whole instance.

## Artifact classes

- table
- field
- catalog item / record producer
- flow
- subflow
- action
- business rule
- script include
- client script / UI policy where relevant
- REST/API artifact
- connection / alias metadata (never secret values)
- ACL
- role/group relationship where authorized
- application/scope
- scheduled job/event
- notification
- ATF/test artifact
- update/deployment evidence
- CMDB/application/service reference where relevant

## Dependency edge examples

```text
catalog_item --invokes--> flow
flow --invokes--> subflow
subflow --calls--> action
business_rule --calls--> script_include
integration_action --uses--> connection_alias
acl --requires--> role
feature --validated_by--> atf_test
```

## Discovery modes

### Targeted
Default. Start from the work item / artifact and expand dependencies to a bounded depth.

### Architecture review
Expand relevant upstream/downstream dependencies.

### Inventory
Explicitly authorized scheduled inventory job. Do not run by default per request.

## Evidence

Every node/edge should preserve source identifiers and retrieved timestamps.
Inferred edges must be marked inferred.
