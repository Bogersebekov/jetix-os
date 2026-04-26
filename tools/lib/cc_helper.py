#!/usr/bin/env python3
"""Shared LLM call helper for the voice-pipeline (extract/filter/summarize).

Default backend = CC headless (subprocess `claude -p`), routed through the
Max subscription auth — works without ANTHROPIC_API_KEY. This is the
post-cycle-11 default; survives Anthropic API hard caps and zero-budget runs.

Backward-compat backend = anthropic SDK (legacy), enabled via
`JETIX_LLM_BACKEND=api` env var. Requires ANTHROPIC_API_KEY.

Usage:
    from tools.lib.cc_helper import claude_call
    text = claude_call(system="...", user="...", model="claude-sonnet-4-6")

Both backends accept the same {system, user, model} interface and return
the assistant's text response (with optional JSON-fence stripping).
"""

import os
import re
import subprocess
from typing import Optional

# ─── Configuration ───────────────────────────────────────────────────────────

BACKEND = os.environ.get("JETIX_LLM_BACKEND", "cc-headless").lower()
DEFAULT_TIMEOUT = int(os.environ.get("JETIX_LLM_TIMEOUT_SEC", "900"))  # 15 min
DEFAULT_MODEL = "claude-sonnet-4-6"

# Map legacy model names → current aliases (CC headless accepts both).
_MODEL_ALIASES = {
    "claude-sonnet-4-20250514": "claude-sonnet-4-6",
    "claude-3-5-sonnet-20241022": "claude-sonnet-4-6",
    "claude-3-5-sonnet-latest": "claude-sonnet-4-6",
}


def _normalize_model(model: Optional[str]) -> str:
    if not model:
        return DEFAULT_MODEL
    return _MODEL_ALIASES.get(model, model)


# ─── Public API ──────────────────────────────────────────────────────────────


def claude_call(
    system: str,
    user: str,
    model: Optional[str] = None,
    timeout: int = DEFAULT_TIMEOUT,
    expect_json: bool = False,
) -> str:
    """Call Claude with system + user message. Returns raw text.

    Args:
        system: system prompt (passed via --system-prompt or `system=` arg)
        user: user message content (sent via stdin in CC mode, message in API mode)
        model: model alias or full ID. None → DEFAULT_MODEL.
        timeout: subprocess timeout in seconds (CC backend only).
        expect_json: if True, strips surrounding ```json …``` fences from output.

    Backend selection:
        - default (cc-headless): subprocess `claude -p` via Max-sub auth, no API key
        - JETIX_LLM_BACKEND=api: anthropic SDK direct, requires ANTHROPIC_API_KEY
    """
    model = _normalize_model(model)
    if BACKEND == "api":
        out = _call_via_api(system, user, model)
    else:
        out = _call_via_cc(system, user, model, timeout)
    if expect_json:
        out = _strip_fences(out)
    return out


# ─── Internals ───────────────────────────────────────────────────────────────


def _strip_fences(text: str) -> str:
    """Strip ```json …``` or ```…``` fences if present (CC headless often wraps)."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json|markdown|md|text)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return text.strip()


def _call_via_cc(system: str, user: str, model: str, timeout: int) -> str:
    """Call `claude -p` as subprocess. User message via stdin (avoids ARG_MAX)."""
    cmd = [
        "claude", "-p",
        "--system-prompt", system,
        "--model", model,
        "--output-format", "text",
        "--no-session-persistence",
        "--disable-slash-commands",
        "--tools", "",  # disable tool use; pure text-in/text-out
    ]
    # Force CC headless (Max sub) — drop API key from child env so CC doesn't
    # accidentally route through the API path. The shell may still have the
    # key set, but CC respects the child env.
    env = os.environ.copy()
    env.pop("ANTHROPIC_API_KEY", None)

    try:
        proc = subprocess.run(
            cmd,
            input=user,
            text=True,
            capture_output=True,
            env=env,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as e:
        raise RuntimeError(f"claude headless timed out after {timeout}s") from e
    except FileNotFoundError as e:
        raise RuntimeError("claude binary not found in PATH (install Claude Code)") from e

    if proc.returncode != 0:
        raise RuntimeError(
            f"claude headless exit {proc.returncode}\n"
            f"stderr: {(proc.stderr or '')[-1000:]}\n"
            f"stdout-tail: {(proc.stdout or '')[-300:]}"
        )
    return proc.stdout


def _call_via_api(system: str, user: str, model: str) -> str:
    """Legacy backend: anthropic SDK direct. Requires ANTHROPIC_API_KEY."""
    try:
        from anthropic import Anthropic
    except ImportError as e:
        raise RuntimeError(
            "anthropic SDK not installed (JETIX_LLM_BACKEND=api). pip install anthropic"
        ) from e
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("JETIX_LLM_BACKEND=api but ANTHROPIC_API_KEY not set")

    client = Anthropic(api_key=api_key)
    # Pick max_tokens defensively per model family.
    max_tok = 64000 if "opus" in model.lower() else 32000
    resp = client.messages.create(
        model=model,
        max_tokens=max_tok,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")


def backend_info() -> str:
    """Return a one-line description of the active backend (for logging)."""
    if BACKEND == "api":
        has_key = bool(os.environ.get("ANTHROPIC_API_KEY"))
        return f"backend=api anthropic-sdk key={'set' if has_key else 'MISSING'}"
    return "backend=cc-headless (Max sub via `claude -p`)"
