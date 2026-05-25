"""Rate limiting + retry/backoff for Notion API (~3 req/sec average).

Notion returns HTTP 429 with a Retry-After header when rate-limited, and
occasionally 502/503/504 on transient server errors. This module wraps any
callable with: (a) a minimum inter-request interval (token-bucket-lite), and
(b) exponential backoff with jitter on retryable errors.
"""

from __future__ import annotations

import random
import time
from typing import Any, Callable, TypeVar

T = TypeVar("T")

# Notion documents a ~3 requests/second average. We pace at ~2.8 req/s to leave headroom.
_MIN_INTERVAL_S = 0.36
_MAX_RETRIES = 6
_BASE_BACKOFF_S = 1.0
_MAX_BACKOFF_S = 30.0

_last_call_ts = 0.0


def _retryable(exc: Exception) -> tuple[bool, float]:
    """Return (is_retryable, suggested_wait_seconds) for a Notion API exception."""
    status = getattr(exc, "status", None) or getattr(exc, "code", None)
    # notion_client.errors.APIResponseError has .status (int) and .code (str)
    try:
        from notion_client.errors import APIResponseError, HTTPResponseError, RequestTimeoutError
    except Exception:  # pragma: no cover - import guard
        APIResponseError = HTTPResponseError = RequestTimeoutError = ()  # type: ignore

    if isinstance(exc, RequestTimeoutError):
        return True, _BASE_BACKOFF_S
    http_status = None
    if isinstance(exc, (APIResponseError, HTTPResponseError)):
        http_status = getattr(exc, "status", None)
    if http_status is None and isinstance(status, int):
        http_status = status
    if http_status == 429:
        # honor Retry-After header if present on the underlying response
        retry_after = 1.0
        resp = getattr(exc, "response", None) or getattr(exc, "raw_response", None)
        if resp is not None:
            try:
                retry_after = float(resp.headers.get("Retry-After", retry_after))
            except Exception:
                pass
        return True, retry_after
    if http_status in (500, 502, 503, 504):
        return True, _BASE_BACKOFF_S
    return False, 0.0


def pace() -> None:
    """Block until at least _MIN_INTERVAL_S has elapsed since the last paced call."""
    global _last_call_ts
    now = time.monotonic()
    delta = now - _last_call_ts
    if delta < _MIN_INTERVAL_S:
        time.sleep(_MIN_INTERVAL_S - delta)
    _last_call_ts = time.monotonic()


def with_retry(fn: Callable[..., T], *args: Any, **kwargs: Any) -> T:
    """Call fn(*args, **kwargs) with pacing + exponential backoff on retryable errors."""
    attempt = 0
    while True:
        pace()
        try:
            return fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001 - we classify below
            retryable, suggested = _retryable(exc)
            attempt += 1
            if not retryable or attempt > _MAX_RETRIES:
                raise
            backoff = min(_MAX_BACKOFF_S, max(suggested, _BASE_BACKOFF_S * (2 ** (attempt - 1))))
            backoff += random.uniform(0, 0.4)  # jitter
            time.sleep(backoff)
