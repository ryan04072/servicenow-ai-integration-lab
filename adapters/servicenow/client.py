from __future__ import annotations

import json
import os
import time
from typing import Any, Dict, List, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .artifact_registry import get_artifact_definition


TRANSIENT_HTTP_STATUS = {429, 500, 502, 503, 504}


class ServiceNowApiError(RuntimeError):
    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        body: str = "",
    ):
        super().__init__(message)
        self.status_code = status_code
        self.body = body


class ServiceNowClient:
    """
    Read-only ServiceNow client for the Agentic Context Service.

    Public callers provide an approved artifact type rather than
    an arbitrary ServiceNow table name.
    """

    def __init__(
        self,
        instance_url: str,
        client_id: str,
        client_secret: str,
        timeout_seconds: int = 30,
        max_attempts: int = 2,
        opener=urlopen,
    ):
        if not instance_url:
            raise ValueError("instance_url is required")

        if not client_id:
            raise ValueError("client_id is required")

        if not client_secret:
            raise ValueError("client_secret is required")

        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")

        if max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")

        self.instance_url = instance_url.rstrip("/")
        self.client_id = client_id
        self.client_secret = client_secret
        self.timeout_seconds = timeout_seconds
        self.max_attempts = max_attempts
        self._opener = opener

        self._access_token: Optional[str] = None
        self._token_expiry: float = 0.0

    @classmethod
    def from_env(cls) -> "ServiceNowClient":
        instance_url = os.getenv("SERVICENOW_INSTANCE_URL")
        client_id = os.getenv("SERVICENOW_CLIENT_ID")
        client_secret = os.getenv("SERVICENOW_CLIENT_SECRET")

        missing = []

        if not instance_url:
            missing.append("SERVICENOW_INSTANCE_URL")

        if not client_id:
            missing.append("SERVICENOW_CLIENT_ID")

        if not client_secret:
            missing.append("SERVICENOW_CLIENT_SECRET")

        if missing:
            raise ValueError(
                "Missing required environment variable(s): "
                + ", ".join(missing)
            )

        return cls(
            instance_url=instance_url,
            client_id=client_id,
            client_secret=client_secret,
        )

    def _request_json(
        self,
        request: Request,
    ) -> Dict[str, Any]:
        for attempt in range(1, self.max_attempts + 1):
            try:
                with self._opener(
                    request,
                    timeout=self.timeout_seconds,
                ) as response:
                    raw = response.read()

                if not raw:
                    return {}

                return json.loads(raw.decode("utf-8"))

            except HTTPError as exc:
                try:
                    body = exc.read().decode(
                        "utf-8",
                        errors="replace",
                    )
                except Exception:
                    body = ""

                if (
                    exc.code in TRANSIENT_HTTP_STATUS
                    and attempt < self.max_attempts
                ):
                    time.sleep(min(2 ** (attempt - 1), 4))
                    continue

                raise ServiceNowApiError(
                    f"ServiceNow returned HTTP {exc.code}",
                    status_code=exc.code,
                    body=body,
                ) from exc

            except URLError as exc:
                if attempt < self.max_attempts:
                    time.sleep(min(2 ** (attempt - 1), 4))
                    continue

                raise ServiceNowApiError(
                    f"Unable to reach ServiceNow: {exc.reason}"
                ) from exc

            except json.JSONDecodeError as exc:
                raise ServiceNowApiError(
                    "ServiceNow returned invalid JSON"
                ) from exc

        raise ServiceNowApiError(
            "ServiceNow request failed"
        )

    def _get_access_token(self) -> str:
        now = time.monotonic()

        if (
            self._access_token
            and now < self._token_expiry - 30
        ):
            return self._access_token

        form = urlencode(
            {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
        ).encode("utf-8")

        request = Request(
            f"{self.instance_url}/oauth_token.do",
            data=form,
            method="POST",
            headers={
                "Accept": "application/json",
                "Content-Type": (
                    "application/x-www-form-urlencoded"
                ),
            },
        )

        payload = self._request_json(request)

        access_token = payload.get("access_token")

        if not access_token:
            raise ServiceNowApiError(
                "OAuth token response did not contain access_token"
            )

        try:
            expires_in = int(
                payload.get("expires_in", 1800)
            )
        except (TypeError, ValueError):
            expires_in = 1800

        self._access_token = str(access_token)
        self._token_expiry = now + expires_in

        return self._access_token

    def fetch_records(
        self,
        artifact_type: str,
        encoded_query: str,
        limit: int,
    ) -> List[Dict[str, Any]]:
        if limit < 1 or limit > 100:
            raise ValueError(
                "limit must be between 1 and 100"
            )

        definition = get_artifact_definition(
            artifact_type
        )

        params = {
            "sysparm_limit": str(limit),
            "sysparm_fields": ",".join(
                definition.fields
            ),
            "sysparm_exclude_reference_link": "true",
        }

        if encoded_query:
            params["sysparm_query"] = encoded_query

        url = (
            f"{self.instance_url}"
            f"/api/now/table/{definition.table}"
            f"?{urlencode(params)}"
        )

        request = Request(
            url,
            method="GET",
            headers={
                "Accept": "application/json",
                "Authorization": (
                    f"Bearer {self._get_access_token()}"
                ),
            },
        )

        payload = self._request_json(request)
        result = payload.get("result", [])

        if not isinstance(result, list):
            raise ServiceNowApiError(
                "Unexpected Table API response: "
                "result is not a list"
            )

        return result
