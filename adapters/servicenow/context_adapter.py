from __future__ import annotations

import re
from typing import Dict, List, Optional, Sequence, Set

from reference_runtime.models import Artifact
from reference_runtime.store import STOP

from .artifact_registry import (
    get_artifact_definition,
    list_artifact_types,
)
from .client import ServiceNowClient
from .normalizer import normalize_record


MAX_SEARCH_TOKENS = 8
MAX_CANDIDATES_PER_TYPE = 50


def _search_tokens(text: str) -> Set[str]:
    """
    Tokenize requirements and artifact names.

    Handles ServiceNow-style names such as:
        ScheduledInstallService
        sys_script_include
    """

    expanded = re.sub(
        r"([a-z0-9])([A-Z])",
        r"\1 \2",
        text or "",
    )

    expanded = expanded.replace("_", " ")

    values = re.findall(
        r"[a-z0-9]+",
        expanded.lower(),
    )

    return {
        value
        for value in values
        if len(value) > 1
        and value not in STOP
    }


def _score(
    query: str,
    artifact: Artifact,
) -> float:
    """
    Preserve the reference runtime's deterministic lexical scoring
    model while improving tokenization for ServiceNow naming.
    """

    query_tokens = _search_tokens(query)

    document = " ".join(
        [
            artifact.name,
            artifact.summary,
            " ".join(artifact.tags),
        ]
    )

    document_tokens = _search_tokens(document)

    overlap = len(
        query_tokens & document_tokens
    )

    if not overlap:
        return 0.0

    union = len(
        query_tokens | document_tokens
    ) or 1

    jaccard = overlap / union

    name_bonus = (
        0.15
        if query_tokens
        & _search_tokens(artifact.name)
        else 0.0
    )

    tag_tokens: Set[str] = set()

    for tag in artifact.tags:
        tag_tokens |= _search_tokens(tag)

    tag_bonus = (
        0.10
        if query_tokens & tag_tokens
        else 0.0
    )

    return round(
        min(
            1.0,
            jaccard
            + name_bonus
            + tag_bonus,
        ),
        4,
    )


class ServiceNowContextAdapter:
    """
    Live read-only ServiceNow context discovery adapter.

    Raw arbitrary Table API access is intentionally not exposed.
    """

    def __init__(
        self,
        client: ServiceNowClient,
        environment: str = "pdi",
    ):
        self.client = client
        self.environment = environment

    @staticmethod
    def _build_encoded_query(
        query: str,
        search_fields: Sequence[str],
    ) -> str:
        tokens = sorted(
            _search_tokens(query)
        )[:MAX_SEARCH_TOKENS]

        if not tokens:
            return ""

        clauses = []

        for token in tokens:
            for field in search_fields:
                clauses.append(
                    f"{field}LIKE{token}"
                )

        return "^OR".join(clauses)

    def find_similar_artifacts(
        self,
        query: str,
        artifact_types: Optional[List[str]] = None,
        limit: int = 5,
    ) -> List[Dict]:
        """
        Find relevant approved ServiceNow artifacts.

        Contract:
            query:
                non-empty requirement text

            artifact_types:
                optional subset of approved registry types

            limit:
                1-100, matching ContextQuery schema

        Returns:
            [
                {
                    "score": 0.65,
                    "artifact": {...}
                }
            ]
        """

        if (
            not isinstance(query, str)
            or not query.strip()
        ):
            raise ValueError(
                "query must be a non-empty string"
            )

        if limit < 1 or limit > 100:
            raise ValueError(
                "limit must be between 1 and 100"
            )

        if artifact_types is None:
            selected_types = list(
                list_artifact_types()
            )
        else:
            # Preserve order while removing duplicates.
            selected_types = list(
                dict.fromkeys(artifact_types)
            )

        for artifact_type in selected_types:
            get_artifact_definition(
                artifact_type
            )

        if not selected_types:
            return []

        candidate_limit = min(
            MAX_CANDIDATES_PER_TYPE,
            max(
                10,
                limit * 5,
            ),
        )

        matches: List[Dict] = []

        for artifact_type in selected_types:
            definition = (
                get_artifact_definition(
                    artifact_type
                )
            )

            encoded_query = (
                self._build_encoded_query(
                    query,
                    definition.search_fields,
                )
            )

            # Prevent empty / stop-word-only input
            # from becoming a broad metadata dump.
            if not encoded_query:
                continue

            records = self.client.fetch_records(
                artifact_type=artifact_type,
                encoded_query=encoded_query,
                limit=candidate_limit,
            )

            for record in records:
                artifact = normalize_record(
                    artifact_type=artifact_type,
                    record=record,
                    environment=self.environment,
                    instance_url=(
                        self.client.instance_url
                    ),
                )

                score = _score(
                    query,
                    artifact,
                )

                if score <= 0:
                    continue

                matches.append(
                    {
                        "score": score,
                        "artifact": (
                            artifact.to_dict()
                        ),
                    }
                )

        matches.sort(
            key=lambda item: (
                -item["score"],
                item["artifact"][
                    "name"
                ].lower(),
                item["artifact"]["id"],
            )
        )

        return matches[:limit]
