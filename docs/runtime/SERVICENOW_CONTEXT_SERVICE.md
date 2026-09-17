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

## Freshness

Do not silently mix stale snapshots with live implementation data.

Every context source records:
- `retrieved_at`;
- freshness status;
- environment;
- source authority.

If required context is stale, the orchestrator can create a Human Action or force
a refresh before architecture proceeds.
