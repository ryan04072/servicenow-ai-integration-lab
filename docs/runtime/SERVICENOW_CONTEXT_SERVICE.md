# ServiceNow Context Service

## Goal

Give every authorized agent a consistent, bounded way to answer questions such as:

- What catalog items already implement something similar?
- Which flows/scripts/integrations are related?
- What depends on this artifact?
- What tests already cover it?
- What architectural standard applies?
- Is the existing pattern approved or merely common?

## Logical service boundary

Agents do **not** receive unrestricted table-query capability by default.

They receive purpose-built tools such as:

```text
find_similar_artifacts(requirement, artifact_types?)
inspect_artifact(artifact_id)
get_dependencies(artifact_id, depth?)
find_pattern(pattern_name)
find_existing_tests(artifact_id)
get_architecture_standards(topic)
```

## Suggested ServiceNow source domains

Start read-only and expand deliberately.

| Domain | Typical artifact examples |
|---|---|
| Catalog | catalog items, variable sets, categories |
| Automation | flows, subflows, actions, legacy workflow where applicable |
| Server logic | Business Rules, Script Includes, scheduled logic |
| Client/UI | client scripts, UI policies/actions, Employee Center/UI artifacts |
| Data model | tables, dictionary/fields, relationships |
| Security | ACLs, roles and scoped security metadata |
| Integration | REST messages, connection aliases, integration definitions |
| Testing | ATF tests/suites and related evidence |
| AI | AI agents, skills/tools/capabilities where exposed |
| Documentation | approved repo documentation and support references |

Exact tables/APIs must be validated for the target ServiceNow release and the
identity used by the context service.

## Retrieval model

```text
Requirement
    ↓
lexical/semantic candidate retrieval
    ↓
artifact candidates
    ↓
dependency expansion
    ↓
standards / precedent lookup
    ↓
evidence-ranked context
```

The reference runtime uses deterministic lexical matching for portability.
An enterprise implementation can add AI Search, embeddings, vector retrieval, or
another approved retrieval mechanism without changing the tool contract.

## Output contract

Each artifact should include:
- stable logical ID;
- artifact type;
- name;
- scope;
- source system;
- environment;
- evidence locator;
- retrieved timestamp;
- summary;
- tags;
- sensitivity;
- metadata needed for dependency resolution.

## Live PDI implementation

The first live implementation is the read-only ServiceNow PDI adapter under `adapters/servicenow/`.

Validated target: ServiceNow Australia PDI.

The first implemented capability is `find_similar_artifacts(query, artifact_types?, limit)`.

The live security boundary is:

- OAuth 2.0 Client Credentials;
- dedicated `svc_agentic_context` machine identity;
- `agentic_context_read` OAuth scope;
- ServiceNow Table API restricted to GET;
- dedicated `agentic_context_reader` role;
- explicit table and field ACLs;
- Python artifact-type allowlist;
- no arbitrary table-query capability exposed to agents.

Version 1 currently supports:

| Artifact type | ServiceNow table | Readable fields |
|---|---|---|
| `catalog_item` | `sc_cat_item` | `sys_id`, `name` |
| `script_include` | `sys_script_include` | `sys_id`, `name` |
| `business_rule` | `sys_script` | `sys_id`, `name` |
| `client_script` | `sys_script_client` | `sys_id`, `name` |
| `table` | `sys_db_object` | `sys_id`, `name` |
| `field` | `sys_dictionary` | `sys_id`, `name`, `element` |

Live records are normalized into the existing `reference_runtime.models.Artifact` model and returned using the same scored-result shape as the reference runtime.

The live PDI vertical slice has been validated through OAuth token issuance, GET-only Table API access, least-privilege ACL evaluation, real artifact retrieval, normalization, and deterministic relevance scoring.

The implementation deliberately does not yet retrieve executable script bodies, dependencies, ATF tests, flows, integration metadata, or perform ServiceNow writes.

See `adapters/servicenow/README.md` for the implementation and local smoke-test runbook.

## Freshness

Do not silently mix stale snapshots with live implementation data.

Every context source records:
- `retrieved_at`;
- freshness status;
- environment;
- source authority.

If required context is stale, the orchestrator can create a Human Action or force
a refresh before architecture proceeds.
