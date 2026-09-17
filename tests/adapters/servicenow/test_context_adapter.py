import unittest

from adapters.servicenow.context_adapter import (
    ServiceNowContextAdapter,
)


class FakeClient:
    instance_url = (
        "https://example.service-now.com"
    )

    def __init__(self):
        self.calls = []

        self.records = {
            "script_include": [
                {
                    "sys_id": "1",
                    "name": (
                        "ScheduledInstallService"
                    ),
                },
                {
                    "sys_id": "2",
                    "name": "VAUtils",
                },
            ],
            "business_rule": [
                {
                    "sys_id": "3",
                    "name": (
                        "Validate duplicate "
                        "search source"
                    ),
                }
            ],
            "catalog_item": [],
            "client_script": [],
            "table": [],
            "field": [],
        }

    def fetch_records(
        self,
        artifact_type,
        encoded_query,
        limit,
    ):
        self.calls.append(
            {
                "artifact_type":
                    artifact_type,
                "encoded_query":
                    encoded_query,
                "limit":
                    limit,
            }
        )

        return self.records.get(
            artifact_type,
            [],
        )[:limit]


class ContextAdapterTests(
    unittest.TestCase
):

    def setUp(self):
        self.client = FakeClient()

        self.adapter = (
            ServiceNowContextAdapter(
                self.client,
                environment="pdi",
            )
        )

    def test_finds_camel_case_name(self):
        results = (
            self.adapter
            .find_similar_artifacts(
                "scheduled install",
                artifact_types=[
                    "script_include"
                ],
                limit=5,
            )
        )

        self.assertEqual(
            len(results),
            1,
        )

        self.assertEqual(
            results[0]["artifact"]["name"],
            "ScheduledInstallService",
        )

        self.assertGreater(
            results[0]["score"],
            0,
        )

    def test_artifact_filter_controls_source(
        self,
    ):
        self.adapter.find_similar_artifacts(
            "validate duplicate",
            artifact_types=[
                "business_rule"
            ],
            limit=5,
        )

        self.assertEqual(
            len(self.client.calls),
            1,
        )

        self.assertEqual(
            self.client.calls[0][
                "artifact_type"
            ],
            "business_rule",
        )

    def test_unknown_type_rejected(self):
        with self.assertRaises(
            ValueError
        ):
            self.adapter.find_similar_artifacts(
                "test",
                artifact_types=[
                    "anything_table"
                ],
                limit=5,
            )

    def test_invalid_limit_rejected(self):
        with self.assertRaises(
            ValueError
        ):
            self.adapter.find_similar_artifacts(
                "test",
                limit=101,
            )

    def test_empty_query_rejected(self):
        with self.assertRaises(
            ValueError
        ):
            self.adapter.find_similar_artifacts(
                "",
                limit=5,
            )

    def test_stop_words_do_not_dump_tables(
        self,
    ):
        results = (
            self.adapter
            .find_similar_artifacts(
                (
                    "create a new "
                    "servicenow request"
                ),
                artifact_types=[
                    "script_include"
                ],
                limit=5,
            )
        )

        self.assertEqual(
            results,
            [],
        )

        self.assertEqual(
            self.client.calls,
            [],
        )

    def test_duplicate_types_are_deduped(
        self,
    ):
        self.adapter.find_similar_artifacts(
            "scheduled install",
            artifact_types=[
                "script_include",
                "script_include",
            ],
            limit=5,
        )

        self.assertEqual(
            len(self.client.calls),
            1,
        )


if __name__ == "__main__":
    unittest.main()
