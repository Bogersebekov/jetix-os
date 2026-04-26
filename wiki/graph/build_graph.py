#!/usr/bin/env python3
"""Edges validator + graph builder for wiki/graph/edges.jsonl.

Two main commands:

    python3 wiki/graph/build_graph.py lint
        Validate every edge in edges.jsonl. Checks:
          (1) JSON parsing OK
          (2) Required fields present (from, to, type, created)
          (3) `type` ∈ enum from edge-types.md
          (4) `from` and `to` paths resolve to existing files
          (5) `created` is YYYY-MM-DD
          (6) `confidence` (if present) ∈ {high, medium, low}
        Exit 0 if clean; exit 1 if any errors.

    python3 wiki/graph/build_graph.py stats
        Print quick summary (total edges, by type, dangling targets).

Idempotent. Read-only — never mutates edges.jsonl. Safe to run anytime.

Per cycle-10 follow-up F-2.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parents[2]
WIKI_ROOT = REPO_ROOT / "wiki"
EDGES_PATH = REPO_ROOT / "wiki" / "graph" / "edges.jsonl"
EDGE_TYPES_PATH = REPO_ROOT / "wiki" / "graph" / "edge-types.md"


def _resolve_edge_path(rel: str) -> Path | None:
    """Resolve an edge path. Existing wiki edges use paths relative to wiki/
    (e.g. `ideas/foo.md` → `wiki/ideas/foo.md`). New CRM edges use repo-root
    paths (e.g. `crm/people/foo.md`). Try both; return first that exists, or
    None.
    """
    candidates = [REPO_ROOT / rel, WIKI_ROOT / rel]
    for c in candidates:
        if c.exists():
            return c
    return None

REQUIRED_FIELDS = ("from", "to", "type", "created")
VALID_CONFIDENCE = {"high", "medium", "low"}
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_edge_types(md_path: Path = EDGE_TYPES_PATH) -> set[str]:
    """Extract edge type identifiers from edge-types.md tables.

    Looks for backtick-quoted ids in the leftmost cell of each markdown row
    that follows a header divider. Tolerates variations in spacing.
    """
    if not md_path.exists():
        return set()
    types: set[str] = set()
    in_table = False
    for line in md_path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("|") and "---" in s:
            in_table = True
            continue
        if in_table:
            if not s.startswith("|"):
                in_table = False
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not cells:
                continue
            m = re.match(r"`([a-z][a-z0-9_-]*)`", cells[0])
            if m:
                types.add(m.group(1))
    return types


def _load_edges(path: Path = EDGES_PATH) -> tuple[list[dict], list[str]]:
    """Returns (edges, parse_errors). parse_errors are formatted strings."""
    if not path.exists():
        return [], [f"edges file not found: {path}"]
    edges: list[dict] = []
    errors: list[str] = []
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as e:
            errors.append(f"line {n}: JSON parse error — {e}")
            continue
        if not isinstance(obj, dict):
            errors.append(f"line {n}: edge is not a JSON object")
            continue
        obj["_line"] = n
        edges.append(obj)
    return edges, errors


def lint(verbose: bool = False) -> tuple[int, list[str], dict]:
    """Returns (error_count, error_messages, summary)."""
    edges, parse_errors = _load_edges()
    errors: list[str] = list(parse_errors)
    valid_types = parse_edge_types()
    if not valid_types:
        errors.append(f"no edge types parsed from {EDGE_TYPES_PATH} — broken or missing")

    summary = {
        "total_lines": len(edges) + len(parse_errors),
        "parsed_edges": len(edges),
        "valid_types_count": len(valid_types),
        "missing_files_from": 0,
        "missing_files_to": 0,
        "unknown_types": 0,
        "missing_required": 0,
        "bad_dates": 0,
        "bad_confidence": 0,
    }

    for e in edges:
        ln = e.get("_line", "?")

        # required fields
        missing = [f for f in REQUIRED_FIELDS if f not in e or e.get(f) in (None, "")]
        if missing:
            errors.append(f"line {ln}: missing required field(s): {missing}")
            summary["missing_required"] += 1
            continue  # skip further checks if required missing

        # type enum
        if e["type"] not in valid_types:
            errors.append(f"line {ln}: unknown edge type {e['type']!r} — not in edge-types.md "
                          f"(valid: {sorted(valid_types)[:6]}…)")
            summary["unknown_types"] += 1

        # paths must resolve to files (try repo-root then wiki/-relative)
        if _resolve_edge_path(e["from"]) is None:
            errors.append(f"line {ln}: `from` path does not exist (tried repo-root and wiki/): {e['from']}")
            summary["missing_files_from"] += 1
        if _resolve_edge_path(e["to"]) is None:
            errors.append(f"line {ln}: `to` path does not exist (tried repo-root and wiki/): {e['to']}")
            summary["missing_files_to"] += 1

        # date format
        if not _DATE_RE.match(str(e["created"])):
            errors.append(f"line {ln}: `created` not YYYY-MM-DD: {e['created']!r}")
            summary["bad_dates"] += 1

        # confidence (optional)
        if "confidence" in e and e["confidence"] not in VALID_CONFIDENCE:
            errors.append(f"line {ln}: invalid `confidence` {e['confidence']!r} "
                          f"(must be one of {sorted(VALID_CONFIDENCE)})")
            summary["bad_confidence"] += 1

    return len(errors), errors, summary


def stats() -> None:
    edges, parse_errors = _load_edges()
    by_type: Counter = Counter()
    for e in edges:
        by_type[e.get("type", "?")] += 1
    print(f"edges.jsonl: {len(edges)} parsed edges, {len(parse_errors)} parse errors")
    print()
    print("By type:")
    for t, n in sorted(by_type.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {t:32s} {n:>5d}")


def main(argv: list[str] | None = None) -> int:
    args = (argv if argv is not None else sys.argv[1:]) or ["lint"]
    cmd = args[0]
    if cmd == "lint":
        verbose = "-v" in args or "--verbose" in args
        n_errors, errors, summary = lint(verbose=verbose)
        if n_errors:
            print(f"FAIL: {n_errors} error(s) in {EDGES_PATH.relative_to(REPO_ROOT)}")
            print()
            for err in errors[:50]:  # cap output
                print(f"  - {err}")
            if len(errors) > 50:
                print(f"  ... ({len(errors) - 50} more)")
            print()
            print(f"Summary: {summary}")
            return 1
        print(f"OK: {summary['parsed_edges']} edges, "
              f"{summary['valid_types_count']} valid edge types, no errors.")
        return 0
    if cmd == "stats":
        stats()
        return 0
    print(f"Usage: build_graph.py {{lint|stats}}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
