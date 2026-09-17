# SLOs, Quality, and Promotion Metrics

## Principle

Autonomy is earned through evidence.

## Suggested metric families

### Accuracy
- factual accuracy;
- unsupported-claim rate;
- source/citation accuracy;
- missing-context detection.

### Review quality
- approved without edit;
- approved with minor edit;
- materially modified;
- rejected.

### Intake
- clarification cycles;
- duplicate-detection precision;
- acceptance-criteria quality;
- percent returned for missing information.

### Delivery intelligence
- executive-brief correction rate;
- blocker detection;
- roadmap-classification confidence/accuracy.

### Reliability
- tool-call success;
- timeout rate;
- duplicate-action rate;
- recovery success.

### Human impact
- reviewer time;
- cycle-time change;
- rework;
- manual steps removed.

## Promotion rule

Do not hard-code numeric thresholds until enough baseline data exists.

Use:

```text
Baseline
→ agreed target
→ observed performance
→ promotion decision
```

Document targets in `config/governance/slo-targets.template.yaml`.
