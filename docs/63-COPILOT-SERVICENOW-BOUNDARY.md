# Microsoft Copilot ↔ ServiceNow Boundary

## Microsoft 365 Copilot is valuable, but the connector is an index boundary

Current Microsoft ServiceNow connectors are useful for surfacing selected:
- tickets;
- catalog;
- knowledge

inside Microsoft 365 search/Copilot experiences.

They are not a complete ServiceNow runtime mirror.

## Example limitation

The Tickets connector does not represent every ServiceNow ACL behavior and does
not index comments/attachments.

Therefore:

```text
M365 Copilot connector
→ excellent for discovery/search/cross-M365 questions

ServiceNow native AI / MCP / API
→ preferred for deep ServiceNow context and ServiceNow actions
```

## Hybrid architecture

```text
Microsoft 365 Copilot
      │
      ├─ SharePoint / Teams / Outlook / Graph context
      ├─ ServiceNow indexed connector content
      │
      └─ Copilot Studio agent when action/orchestration is needed
                    │
                    ▼
             ServiceNow MCP/API
                    │
                    ▼
           governed ServiceNow action
```

## Cost principle

Use lower-cost/available enterprise AI where it satisfies the use case, but
do not move a ServiceNow-native workload out of ServiceNow solely to reduce AI
consumption if doing so loses required context, permissions, governance, or
native actions.

Evaluate total cost:
- AI consumption;
- connector/runtime licensing;
- implementation;
- support;
- human correction/rework.
