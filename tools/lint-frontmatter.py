#!/usr/bin/env python3
"""Minimal frontmatter validator for Jetix OS v1-beta.

Checks YAML frontmatter of markdown files against a per-type required-field
schema. Baseline for /lint — extend coverage in v1-final.

Usage:
    python3 tools/lint-frontmatter.py <file-or-dir> [...]
    python3 tools/lint-frontmatter.py templates/
    python3 tools/lint-frontmatter.py design/SYSTEM-DESIGN-TECH.md

Exit codes:
    0  — все проверенные файлы прошли
    1  — как минимум один файл не прошёл
    2  — ошибка вызова (не указан путь и т.п.)

Baseline rules (соответствуют §2.3.2 и §11 SYSTEM-DESIGN-TECH.md):
    - Все .md файлы (кроме whitelist exceptions) ДОЛЖНЫ иметь frontmatter
    - Каждая frontmatter секция ДОЛЖНА содержать: type, created
    - Для конкретных type: — дополнительные required fields (см. TYPE_SCHEMA).

Безопасно для placeholder-значений {{date:YYYY-MM-DD}} — они считаются valid
нестрогими как наличие поля (шаблоны проходят).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Files excluded from frontmatter requirement (I-02 exceptions).
WHITELIST = {
    "README.md",
    "HOME.md",
    "MIGRATION.md",
    "ARCHITECTURE.md",
    "CLAUDE.md",
    "test-sync.md",
}

# Baseline для ВСЕХ типов.
BASE_REQUIRED = {"type", "created"}

# Type-specific required поля (кроме BASE_REQUIRED).
# Синхронизировано с IMPLEMENTATION-PLAN §3.1 и TECH §2.3.2 + §11.
TYPE_SCHEMA: dict[str, set[str]] = {
    # T-01: §11.8 I-23 — timeboxing обязательно
    "project-overview": {"status", "project-slug", "budget-hours",
                         "budget-weeks", "kill-criterion", "next_action", "owner"},
    # T-02: §11.5 I-12 — decision schema
    "decision": {"status", "context", "alternatives", "decision",
                 "evidence", "replay-check", "relevant-agents", "owner"},
    # T-03: hypothesis
    "hypothesis": {"status", "tested-with", "success-criterion", "owner-project", "owner"},
    # T-04: strategy-life
    "strategy-life": {"level", "period", "north-star", "focus-blocks",
                      "budget-resources", "metric-50k-contribution", "owner", "status"},
    # T-05: strategy-project
    "strategy-project": {"project-slug", "point-a", "point-b", "horizon",
                         "metric-50k-contribution", "resources-allocated", "owner", "status"},
    # T-06: task
    "task": {"status", "project-slug", "estimate", "next_action", "owner", "priority"},
    # T-07: tool
    "tool": {"category", "purpose", "install-ref", "usage-example", "status", "owner"},
    # T-08: daily-log
    "daily-log": {"date", "weekday", "plan", "work-blocks", "reflection", "drafts", "owner"},
    # T-09: draft
    "draft": {"topic", "parent-day", "promoted-to", "status", "owner"},
    # T-10: reflection
    "reflection": {"date", "trigger", "insights", "owner"},
    # T-11: contact (CRM)
    "contact": {"category", "name", "stage", "last-touch", "owner"},
    # T-12: adr
    "adr": {"number", "title", "status", "date", "context", "decision", "consequences", "owner"},
    # Design documents (TECH, HUMAN и др.) — status обязательно
    "design-document": {"status", "owner"},
    "design-summary": {"status", "owner"},
    "architecture-target": {"status", "owner"},
    "implementation-plan": {"status", "owner"},
    "synthesis-report": {"status"},
}

FM_BOUNDARY = re.compile(r"^---\s*$")
KEY_PATTERN = re.compile(r"^([A-Za-z0-9_-][A-Za-z0-9_.\s-]*?):\s*(.*)$")


def extract_frontmatter(path: Path) -> tuple[dict[str, str] | None, str | None]:
    """Return (fields_dict, error_message). fields_dict=None when no FM found."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        return None, f"unreadable: {exc}"

    lines = text.splitlines()
    if not lines or not FM_BOUNDARY.match(lines[0]):
        return None, None  # no frontmatter

    end_idx = None
    for idx in range(1, len(lines)):
        if FM_BOUNDARY.match(lines[idx]):
            end_idx = idx
            break
    if end_idx is None:
        return None, "frontmatter opened with --- but not closed"

    fields: dict[str, str] = {}
    for raw in lines[1:end_idx]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        # top-level keys only (ignore indented nested YAML)
        if raw[0] in (" ", "\t", "-"):
            continue
        match = KEY_PATTERN.match(raw)
        if match:
            fields[match.group(1).strip()] = match.group(2).strip()
    return fields, None


def check_file(path: Path, root: Path) -> list[str]:
    """Return list of error strings (empty = ok)."""
    rel = path.relative_to(root) if root in path.parents or root == path.parent else path
    if path.name in WHITELIST:
        return []
    if path.suffix != ".md":
        return []

    fields, err = extract_frontmatter(path)
    errors: list[str] = []

    if err:
        errors.append(f"{rel}: {err}")
        return errors

    if fields is None:
        errors.append(f"{rel}: missing YAML frontmatter (I-02)")
        return errors

    missing_base = BASE_REQUIRED - fields.keys()
    if missing_base:
        errors.append(f"{rel}: missing base fields {sorted(missing_base)}")

    type_value = fields.get("type", "").strip().strip('"').strip("'")
    schema = TYPE_SCHEMA.get(type_value)
    if schema:
        missing_typed = schema - fields.keys()
        if missing_typed:
            errors.append(
                f"{rel}: type='{type_value}' missing {sorted(missing_typed)}"
            )

    return errors


def walk(target: Path, root: Path) -> list[Path]:
    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(target.rglob("*.md"))
    return []


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: lint-frontmatter.py <file-or-dir> [...]", file=sys.stderr)
        return 2

    root = Path(__file__).resolve().parent.parent
    all_errors: list[str] = []
    checked = 0

    for arg in argv[1:]:
        target = Path(arg).resolve()
        for md in walk(target, root):
            checked += 1
            all_errors.extend(check_file(md, root))

    if all_errors:
        print(f"lint-frontmatter: {len(all_errors)} error(s) in {checked} file(s)")
        for err in all_errors:
            print(f"  ✗ {err}")
        return 1

    print(f"lint-frontmatter: OK — {checked} file(s) passed")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
