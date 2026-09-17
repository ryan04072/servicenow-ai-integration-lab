import unittest

from adapters.servicenow.normalizer import (
    normalize_record,
)


class NormalizerTests(unittest.TestCase):

    def test_normalizes_script_include(self):
        artifact = normalize_record(
            "script_include",
            {
                "sys_id": "abc123",
                "name": "ScheduledInstallService",
            },
            environment="pdi",
            instance_url=(
                "https://example.service-now.com"
            ),
        )

        self.assertEqual(
            artifact.id,
            "sn:script_include:abc123",
        )

        self.assertEqual(
            artifact.name,
            "ScheduledInstallService",
        )

        self.assertEqual(
            artifact.source,
            "servicenow",
        )

        self.assertEqual(
            artifact.environment,
            "pdi",
        )

        self.assertEqual(
            artifact.metadata["table"],
            "sys_script_include",
        )

        self.assertEqual(
            artifact.metadata["sys_id"],
            "abc123",
        )

    def test_dictionary_field_uses_table_and_element(self):
        artifact = normalize_record(
            "field",
            {
                "sys_id": "def456",
                "name": "incident",
                "element": "short_description",
            },
            environment="pdi",
            instance_url=(
                "https://example.service-now.com"
            ),
        )

        self.assertEqual(
            artifact.name,
            "incident.short_description",
        )

    def test_missing_sys_id_is_rejected(self):
        with self.assertRaises(ValueError):
            normalize_record(
                "business_rule",
                {
                    "name": "Test Rule",
                },
                environment="pdi",
                instance_url=(
                    "https://example.service-now.com"
                ),
            )


if __name__ == "__main__":
    unittest.main()
