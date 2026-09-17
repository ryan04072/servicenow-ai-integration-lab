# Data Classification and Retention

## Objective

Define what data agents may retrieve, process, retain, and expose.

Do not invent a second enterprise classification system.
Map this implementation to the organization's existing classification/privacy policy.

## For each source document

- classification;
- permitted AI provider/runtime;
- permitted environments;
- allowed agent roles;
- retention requirement;
- masking/redaction rules;
- export restrictions;
- audit requirements.

## Context minimization

The Context Curator should retrieve the minimum data required for the task.

Avoid:
- entire tables when a few records are sufficient;
- full attachments when a relevant section is sufficient;
- unnecessary PII;
- secrets;
- production data in development tests.

## Retention

Separate:
- source-system retention;
- model/provider retention;
- agent-run trace retention;
- cached context;
- generated drafts;
- decision precedent.

Use the enterprise AI/data policies as the authority.

## Synthetic test data

Prefer synthetic/non-sensitive data for:
- agent evals;
- demos;
- personal portfolio;
- development of new workflows.
