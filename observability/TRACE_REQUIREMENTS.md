# Agent Run Trace Requirements

Material enterprise agent runs should be traceable by a correlation ID.

Minimum trace:

```text
trigger
→ task / requester
→ roles invoked
→ context retrieved
→ tools invoked
→ output
→ risk classification
→ approvals
→ resulting ADO/GitHub/ServiceNow artifact
→ final outcome
```

Never log secrets or raw credential material.

The trace should support:
- audit;
- troubleshooting;
- agent evaluation;
- security review;
- cost/usage analysis;
- process improvement.
