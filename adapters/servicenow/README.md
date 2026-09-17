# ServiceNow Read-Only Context Adapter

## Purpose

This adapter provides bounded, read-only ServiceNow artifact discovery for the Personal Agentic AI Platform.

The initial live capability is:

```text
find_similar_artifacts(query, artifact_types?, limit)
```

It complements the synthetic `reference_runtime` implementation without replacing or modifying it.

## Architecture

```text
Agent / Orchestrator
        |
        v
ServiceNowContextAdapter
        |
        v
Approved Artifact Registry
        |
        v
ServiceNowClient
        |
        v
OAuth Client Credentials
        |
        v
ServiceNow Table API - GET only
        |
        v
Dedicated Machine Identity
```

The adapter does not expose arbitrary ServiceNow table querying to agents.

## Authentication

The adapter uses OAuth 2.0 Client Credentials.

Required environment variables:

```text
SERVICENOW_INSTANCE_URL
SERVICENOW_CLIENT_ID
SERVICENOW_CLIENT_SECRET
```

Secrets must never be committed to Git.

The current PDI implementation uses:

```text
OAuth machine identity
        ->
agentic_context_read OAuth scope
        ->
Table API GET only
        ->
agentic_context_reader ServiceNow role
```

## Approved Artifact Types

| Artifact Type | ServiceNow Table | Readable Fields |
|---|---|---|
| `catalog_item` | `sc_cat_item` | `sys_id`, `name` |
| `script_include` | `sys_script_include` | `sys_id`, `name` |
| `business_rule` | `sys_script` | `sys_id`, `name` |
| `client_script` | `sys_script_client` | `sys_id`, `name` |
| `table` | `sys_db_object` | `sys_id`, `name` |
| `field` | `sys_dictionary` | `sys_id`, `name`, `element` |

The adapter intentionally does not retrieve executable script bodies, descriptions, credentials, or unrestricted platform metadata.

## Security Boundary

Security is enforced in multiple layers:

1. OAuth authorization is restricted to the ServiceNow Table API.
2. The OAuth REST API scope permits GET only.
3. A dedicated ServiceNow machine identity is used.
4. The machine identity receives only the custom `agentic_context_reader` role.
5. ServiceNow ACLs restrict readable tables and fields.
6. The Python artifact registry hard-allowlists supported artifact types.
7. The Python client accepts artifact types, not arbitrary table names.
8. Query and result limits are bounded.

The ServiceNow API remains the authoritative enforcement point. Python-side controls provide an additional application boundary.

## Normalization

ServiceNow records are normalized into the existing canonical:

```python
reference_runtime.models.Artifact
```

IDs use:

```text
sn:<artifact_type>:<sys_id>
```

For example:

```text
sn:script_include:<sys_id>
```

Dictionary fields are represented as:

```text
<table>.<element>
```

For example:

```text
incident.short_description
```

## Retrieval

Version 1 uses deterministic lexical retrieval.

The adapter:

1. tokenizes the requirement,
2. constructs bounded ServiceNow `LIKE` queries against approved search fields,
3. retrieves candidate records,
4. normalizes them into canonical artifacts,
5. scores candidates locally,
6. returns the highest-ranking matches.

Future retrieval implementations may add AI Search, embeddings, or vector retrieval without changing the external Context Service contract.

## Local Smoke Test

Set credentials only in the current shell:

```powershell
$env:SERVICENOW_INSTANCE_URL = "https://your-pdi.service-now.com"
$env:SERVICENOW_CLIENT_ID = Read-Host "OAuth Client ID"

$clientSecretSecure = Read-Host "OAuth Client Secret" -AsSecureString

$env:SERVICENOW_CLIENT_SECRET = (
    [System.Net.NetworkCredential]::new(
        "",
        $clientSecretSecure
    ).Password
)
```

Run a bounded search:

```powershell
python -c "from adapters.servicenow import ServiceNowClient, ServiceNowContextAdapter; c=ServiceNowClient.from_env(); a=ServiceNowContextAdapter(c, environment='pdi'); print(a.find_similar_artifacts('ScheduledInstallService', artifact_types=['script_include'], limit=5))"
```

After testing:

```powershell
Remove-Item Env:SERVICENOW_CLIENT_ID
Remove-Item Env:SERVICENOW_CLIENT_SECRET
```

## Validation

Adapter tests:

```powershell
python -m unittest discover -s tests -t . -p "test_*.py" -v
```

Reference runtime tests:

```powershell
python -m unittest discover -s .\reference_runtime\tests -p "test_*.py" -v
```

Golden-task validation:

```powershell
python .\scripts\validate_evals.py
```

Python syntax:

```powershell
python -m compileall .\adapters .\tests
```

Git whitespace:

```powershell
git diff --check
```

## Current Status

The first live PDI vertical slice has been validated end to end:

```text
Python
  ->
OAuth Client Credentials
  ->
GET-only ServiceNow Table API
  ->
least-privilege machine identity
  ->
approved artifact metadata
  ->
canonical Artifact normalization
  ->
deterministic relevance scoring
  ->
find_similar_artifacts()
```

The live implementation has successfully retrieved and ranked real PDI Script Include records.

## Current Limitations

Version 1 intentionally does not yet provide:

- script body retrieval,
- dependency traversal,
- existing test discovery,
- flow/subflow discovery,
- integration metadata discovery,
- semantic/vector retrieval,
- writes or ServiceNow changes.

Those capabilities should be added incrementally behind the same governed Context Service boundary.
