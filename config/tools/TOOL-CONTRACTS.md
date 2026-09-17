# Tool Contracts

## Goal

Keep canonical agent behavior independent from the mechanism used to access enterprise systems.

Agents reason against capability contracts such as:

```text
work.search
work.get
work.query_sprint
roadmap.get
repo.search
repo.get_pr
repo.get_ci
platform.search_configuration
platform.get_schema
docs.search
message.create_draft
```

A runtime may implement those capabilities through:

- native product connectors;
- approved MCP servers/tools;
- REST APIs;
- ServiceNow IntegrationHub/Workflow Studio;
- Microsoft enterprise automation;
- GitHub applications;
- other sanctioned enterprise services.

## Read before write

The first enterprise release should be read-only except for user-reviewed draft generation.

## Tool metadata

Every registered capability should declare:

- system
- operation
- read/write
- environments
- allowed records/repos
- authentication method
- human gate
- sensitivity
- audit destination
- owner
