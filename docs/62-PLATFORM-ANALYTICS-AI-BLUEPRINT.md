# Platform Analytics + AI Blueprint

## Problem

Conversational analytics cannot repair an undefined metric model.

Before leadership asks AI:

> "Are incidents getting better?"

the platform must know what "better" means.

## Foundation first

Create a certified metric layer.

For each important KPI document:
- name;
- business definition;
- owner;
- source table/indicator;
- filters;
- exclusions;
- time grain;
- breakdowns;
- target;
- certification status.

Examples:
- incident volume;
- MTTR;
- first-contact resolution;
- reopen rate;
- backlog aging;
- SLA attainment;
- assignment-group load;
- major incident count;
- problem recurrence;
- change success/failure;
- alert volume/noise;
- service availability/reliability;
- knowledge attachment/usage;
- self-service/deflection.

## Native conversational analytics

Use:

```text
Platform Analytics
     +
Analytics Q&A / Query Generation
     +
Now Assist Panel
     +
Performance Analytics indicators
```

for natural-language ServiceNow analytics.

The native analytics layer is preferable to asking a generic LLM to create raw
GlideRecord/database queries from ambiguous questions.

## Executive analytics pattern

```text
Certified metrics
       ↓
Deterministic calculation
       ↓
Trend / anomaly context
       ↓
AI narrative
       ↓
Executive brief / visualization
```

AI explains the numbers; the metric layer produces the numbers.

## Example executive questions

- "How has incident volume changed over the last 90 days?"
- "Which assignment groups have the largest aging backlog?"
- "What services are generating the most repeat incidents?"
- "Are P1/P2 incidents increasing?"
- "Where is validation or fulfillment work accumulating?"
- "What changed materially since last month's review?"

## AI Data Explorer

Where entitled/enabled, use AI Data Explorer for deeper conversational analysis,
explorations, recommendations, and collaborative analysis.

## Guardrails

- only expose authorized facts/tables;
- prefer certified KPIs over ad-hoc counts;
- show metric definition and date range;
- disclose incomplete/low-quality data;
- never let narrative override the underlying visualization/indicator.
