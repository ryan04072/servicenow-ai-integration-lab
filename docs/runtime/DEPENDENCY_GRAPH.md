# Dependency & Relationship Graph

## Purpose

Artifact similarity tells an agent **what looks related**.

The dependency graph tells it **what can be affected**.

## Node examples

```text
Catalog Item
Variable Set
Flow
Subflow
Script Include
Business Rule
Table
Field
ACL
Role
REST Message
Connection Alias
ATF Test
Knowledge/Architecture Doc
ADO Story
GitHub Path / PR
AI Capability
```

## Edge examples

```text
CATALOG_ITEM --uses--> VARIABLE_SET
CATALOG_ITEM --triggers--> FLOW
FLOW --calls--> SUBFLOW
FLOW --calls--> SCRIPT_INCLUDE
FLOW --invokes--> INTEGRATION
INTEGRATION --uses--> CONNECTION_ALIAS
SCRIPT --reads/writes--> TABLE
ACL --protects--> TABLE
ATF_TEST --covers--> CATALOG_ITEM
ADO_STORY --implements--> ARTIFACT
GITHUB_DOC --documents--> ARTIFACT
```

## Evidence

Edges are labeled:

- `discovered` — directly supported by source metadata/configuration;
- `inferred` — derived by analysis and should carry supporting evidence.

Never present an inferred dependency as certain.

## Use during architecture

For each high-confidence similar artifact:

1. inspect the artifact;
2. expand dependencies to an appropriate depth;
3. identify reusable components;
4. identify blast radius;
5. compare the pattern to approved standards;
6. return evidence to the architect.

## Use during change/review

The same graph can drive:
- regression-test selection;
- reviewer focus;
- documentation impact;
- release validation;
- downstream dependency warnings.
