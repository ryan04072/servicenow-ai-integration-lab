# Observability and Audit

## Requirement

You cannot responsibly increase autonomy if you cannot reconstruct what happened.

## Trace model

Each material run should have:

- correlation ID;
- trigger;
- roles;
- source context;
- tools;
- decisions;
- risk tier;
- approvals;
- output artifacts;
- failures/retries;
- final outcome.

## Dashboards later

Useful operational measures:
- runs by workflow;
- approval rate;
- rejection/modification rate;
- factual error rate;
- missing-context rate;
- tool failures;
- time saved;
- cycle-time impact;
- cost/usage where available.

## Redaction

Never put credentials, secrets, or unnecessary sensitive content into traces.
