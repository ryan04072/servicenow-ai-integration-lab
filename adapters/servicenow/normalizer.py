from __future__ import annotations

from typing import Any, Dict
from urllib.parse import quote

from reference_runtime.models import Artifact, utc_now

from .artifact_registry import get_artifact_definition


def normalize_record(
    artifact_type: str,
    record: Dict[str, Any],
    environment: str,
    instance_url: str,
) -> Artifact:
    definition = get_artifact_definition(
        artifact_type
    )

    sys_id = str(
        record.get("sys_id") or ""
    ).strip()

    if not sys_id:
        raise ValueError(
            f"{artifact_type} record is missing sys_id"
        )

    if artifact_type == "field":
        table_name = str(
            record.get("name") or ""
        ).strip()

        element = str(
            record.get("element") or ""
        ).strip()

        if table_name and element:
            artifact_name = (
                f"{table_name}.{element}"
            )
        elif element:
            artifact_name = element
        elif table_name:
            artifact_name = table_name
        else:
            raise ValueError(
                "field record is missing "
                "name and element"
            )

    else:
        artifact_name = str(
            record.get("name") or ""
        ).strip()

        if not artifact_name:
            raise ValueError(
                f"{artifact_type} record "
                "is missing name"
            )

    base_url = instance_url.rstrip("/")

    evidence_locator = (
        f"{base_url}/"
        f"{definition.table}.do"
        f"?sys_id={quote(sys_id, safe='')}"
    )

    return Artifact(
        id=(
            f"sn:{artifact_type}:"
            f"{sys_id}"
        ),
        artifact_type=artifact_type,
        name=artifact_name,
        source="servicenow",
        environment=environment,
        summary="",
        scope=None,
        tags=[
            artifact_type,
            definition.table,
        ],
        evidence_locator=evidence_locator,
        retrieved_at=utc_now(),
        sensitivity="internal",
        metadata={
            "table": definition.table,
            "sys_id": sys_id,
        },
    )
