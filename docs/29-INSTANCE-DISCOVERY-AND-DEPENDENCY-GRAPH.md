# Instance Discovery and Dependency Graph

## Why this matters

A useful ServiceNow engineering agent needs more than table reads.
It needs enough relationship context to understand blast radius.

Example:

```text
Catalog Item
   ↓
Flow
   ↓
Subflow
   ↓
Custom Action
   ↓
REST Integration
   ↓
Connection Alias
```

A change to one component can affect several layers.

## Build sequence

### Step 1 — targeted discovery
Start with a known artifact/work item and retrieve a bounded dependency set.

### Step 2 — normalized graph
Convert discovered components into:
- instance artifact nodes;
- dependency edges.

### Step 3 — architecture query
Let the ServiceNow Architect ask:
- what calls this?
- what does this call?
- what tests cover it?
- what integrations depend on it?
- what security boundary applies?

### Step 4 — optional periodic inventory
Only after the targeted model works, consider scheduled broader discovery.

## Safety

Discovery remains read-only.
Secrets are represented only by references/metadata, never secret values.
