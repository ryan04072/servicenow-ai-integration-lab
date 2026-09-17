# AI Control Tower Integration Model

## Recommended role of AI Control Tower

Treat AI Control Tower (AICT) as the enterprise AI governance system of record
where the product is adopted for that purpose.

Use it for:
- discovery and inventory;
- managed/unmanaged classification;
- lifecycle governance;
- ownership;
- risk/compliance integration;
- security posture;
- runtime monitoring;
- AI cases/issues;
- value and cost;
- retirement/offboarding.

Do not use GitHub Markdown as a competing enterprise AI inventory.

## Repository vs. Control Tower

### GitHub repository owns
- engineering standards;
- canonical agent instructions;
- schemas/evals;
- architecture decisions;
- orchestration definitions;
- capability contracts;
- implementation documentation.

### AI Control Tower owns
- enterprise AI asset record;
- asset owner;
- governance/lifecycle state;
- risk classification;
- assessment/approval tasks;
- monitoring/value configuration;
- AI cases;
- managed/unmanaged status.

## Cross-reference

Every material implementation should carry:

```yaml
ai_control_tower_asset_id:
capability_id:
runtime_platform:
runtime_asset_id:
repository:
repository_path:
work_item:
business_owner:
technical_owner:
risk_tier:
environment:
```

## Planned asset path

```text
AI use-case intake
→ duplication / placement review
→ AICT asset / lifecycle intake
→ owner assigned
→ assess
→ build & test
→ architecture/security/risk gates
→ deploy
→ monitor + measure
→ improve or retire
```

## Discovered asset path

```text
AICT connector / discovery
→ unmanaged AI asset
→ steward triage
   ├─ known/duplicate → reconcile
   ├─ approved candidate → managed lifecycle
   ├─ benign/out-of-scope → documented disposition
   └─ unauthorized/risky → investigate/contain
```

Discovery establishes visibility; it does not automatically establish approval.

## AICT + SDLC

Control Tower governance tasks should become gates/evidence in the normal SDLC:

```text
ADO work item ↔ AICT asset ↔ GitHub PR ↔ ServiceNow change/release
```
