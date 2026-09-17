import json
import unittest

from adapters.servicenow.client import (
    ServiceNowClient,
)


class FakeResponse:
    def __init__(self, payload):
        self.body = json.dumps(
            payload
        ).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ):
        return False

    def read(self):
        return self.body


class ClientTests(unittest.TestCase):

    def test_oauth_then_get_approved_table(self):
        calls = []

        def opener(request, timeout):
            calls.append(request)

            if request.full_url.endswith(
                "/oauth_token.do"
            ):
                return FakeResponse(
                    {
                        "access_token":
                            "test-token",
                        "expires_in":
                            1799,
                        "scope":
                            "agentic_context_read",
                    }
                )

            return FakeResponse(
                {
                    "result": [
                        {
                            "sys_id": "123",
                            "name": "VAUtils",
                        }
                    ]
                }
            )

        client = ServiceNowClient(
            instance_url=(
                "https://example.service-now.com"
            ),
            client_id="client-id",
            client_secret="client-secret",
            opener=opener,
        )

        records = client.fetch_records(
            artifact_type="script_include",
            encoded_query="nameLIKEVA",
            limit=3,
        )

        self.assertEqual(
            records[0]["name"],
            "VAUtils",
        )

        self.assertEqual(
            len(calls),
            2,
        )

        token_request = calls[0]
        table_request = calls[1]

        self.assertEqual(
            token_request.get_method(),
            "POST",
        )

        self.assertEqual(
            table_request.get_method(),
            "GET",
        )

        self.assertIn(
            (
                "/api/now/table/"
                "sys_script_include"
            ),
            table_request.full_url,
        )

        self.assertIn(
            "sysparm_fields=sys_id%2Cname",
            table_request.full_url,
        )

        self.assertEqual(
            table_request.get_header(
                "Authorization"
            ),
            "Bearer test-token",
        )

    def test_token_is_reused(self):
        calls = []

        def opener(request, timeout):
            calls.append(request)

            if request.full_url.endswith(
                "/oauth_token.do"
            ):
                return FakeResponse(
                    {
                        "access_token":
                            "cached-token",
                        "expires_in":
                            1799,
                    }
                )

            return FakeResponse(
                {
                    "result": []
                }
            )

        client = ServiceNowClient(
            instance_url=(
                "https://example.service-now.com"
            ),
            client_id="client-id",
            client_secret="client-secret",
            opener=opener,
        )

        client.fetch_records(
            "script_include",
            "nameLIKEVA",
            3,
        )

        client.fetch_records(
            "business_rule",
            "nameLIKEValidate",
            3,
        )

        token_calls = [
            request
            for request in calls
            if request.full_url.endswith(
                "/oauth_token.do"
            )
        ]

        self.assertEqual(
            len(token_calls),
            1,
        )

    def test_unknown_type_makes_no_network_call(
        self,
    ):
        def opener(request, timeout):
            raise AssertionError(
                "Network should not be called"
            )

        client = ServiceNowClient(
            instance_url=(
                "https://example.service-now.com"
            ),
            client_id="client-id",
            client_secret="client-secret",
            opener=opener,
        )

        with self.assertRaises(ValueError):
            client.fetch_records(
                artifact_type="sys_user",
                encoded_query="",
                limit=1,
            )

    def test_invalid_limit_rejected_before_network(
        self,
    ):
        def opener(request, timeout):
            raise AssertionError(
                "Network should not be called"
            )

        client = ServiceNowClient(
            instance_url=(
                "https://example.service-now.com"
            ),
            client_id="client-id",
            client_secret="client-secret",
            opener=opener,
        )

        with self.assertRaises(ValueError):
            client.fetch_records(
                artifact_type="script_include",
                encoded_query="",
                limit=101,
            )


if __name__ == "__main__":
    unittest.main()
