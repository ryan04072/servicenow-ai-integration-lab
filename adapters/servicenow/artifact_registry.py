from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class ArtifactDefinition:
    artifact_type: str
    table: str
    fields: Tuple[str, ...]
    search_fields: Tuple[str, ...]


ARTIFACT_REGISTRY: Dict[str, ArtifactDefinition] = {
    "catalog_item": ArtifactDefinition(
        artifact_type="catalog_item",
        table="sc_cat_item",
        fields=("sys_id", "name"),
        search_fields=("name",),
    ),
    "script_include": ArtifactDefinition(
        artifact_type="script_include",
        table="sys_script_include",
        fields=("sys_id", "name"),
        search_fields=("name",),
    ),
    "business_rule": ArtifactDefinition(
        artifact_type="business_rule",
        table="sys_script",
        fields=("sys_id", "name"),
        search_fields=("name",),
    ),
    "client_script": ArtifactDefinition(
        artifact_type="client_script",
        table="sys_script_client",
        fields=("sys_id", "name"),
        search_fields=("name",),
    ),
    "table": ArtifactDefinition(
        artifact_type="table",
        table="sys_db_object",
        fields=("sys_id", "name"),
        search_fields=("name",),
    ),
    "field": ArtifactDefinition(
        artifact_type="field",
        table="sys_dictionary",
        fields=("sys_id", "name", "element"),
        search_fields=("name", "element"),
    ),
}


def get_artifact_definition(artifact_type: str) -> ArtifactDefinition:
    try:
        return ARTIFACT_REGISTRY[artifact_type]
    except KeyError as exc:
        allowed = ", ".join(sorted(ARTIFACT_REGISTRY))
        raise ValueError(
            f"Unsupported artifact type '{artifact_type}'. "
            f"Allowed types: {allowed}"
        ) from exc


def list_artifact_types() -> Tuple[str, ...]:
    return tuple(ARTIFACT_REGISTRY.keys())
