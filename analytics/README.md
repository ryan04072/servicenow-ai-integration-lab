# Historical Delivery Intelligence

Use Azure DevOps Analytics/history as the preferred source for historical work-item
state and revision analysis.

The analytics layer should compute metrics deterministically and provide the
result to the Historical Delivery Analyst for interpretation.

## Initial questions

- How long does work spend in validation?
- Where does WIP accumulate?
- How often does committed work carry over?
- How much work enters after sprint start?
- Which classifications create the most rework?
- Are poorly defined intake items correlated with later churn?
- Do vendor-owned items exhibit different handoff/aging patterns?

## Suggested implementation

```text
Azure DevOps Analytics / revisions
            ↓
deterministic query / data model
            ↓
metric snapshot
            ↓
Historical Delivery Analyst
            ↓
trend explanation + recommendations
```

Do not ask an LLM to reconstruct state history from a prose dump if the source
system can calculate it.
