#!/usr/bin/env python3
"""Aggregate subagent verdicts, execute deletions, write _DELETED-LOG-DEEP.md."""
import json
import os
from pathlib import Path
from datetime import datetime

REPO = Path("/home/ruslan/jetix-os")
VERDICT_DIR = REPO / "tools/convert/deep-cleanup-verdicts"
LOG_PATH = REPO / "raw/books-md/_DELETED-LOG-DEEP.md"

ALLOWED_PREFIXES = ("raw/books-md/meta/", "raw/books-md/philosophy/")

# Safety: never delete files whose slug matches canonical works even if flagged
CANONICAL_GUARDS = [
    "naval-almanack", "almanack-of-naval",
    "paul-graham-essays", "paul-graham-essays-all",
    "how-to-get-rich",
    "greene-48-laws",
    "holiday-daily-stoic",
    "carse-finite-and-infinite",
    "holiday-ego-is-the-enemy",
    "holiday-obstacle-is-the-way",
    "ferriss-4-hour-work-week",
    "ferriss-tools-of-titans",
]


def is_guarded(path: str) -> bool:
    p = path.lower()
    return any(g in p for g in CANONICAL_GUARDS)


def main():
    all_verdicts = []
    for vf in sorted(VERDICT_DIR.glob("*.json")):
        batch = json.loads(vf.read_text())
        for entry in batch:
            entry["_batch"] = vf.stem
            all_verdicts.append(entry)

    by_verdict = {"KEEP": [], "DELETE": [], "UNCERTAIN": []}
    for e in all_verdicts:
        v = e["verdict"].upper()
        if v in by_verdict:
            by_verdict[v].append(e)

    print(f"Total: {len(all_verdicts)}")
    print(f"  KEEP: {len(by_verdict['KEEP'])}")
    print(f"  DELETE: {len(by_verdict['DELETE'])}")
    print(f"  UNCERTAIN: {len(by_verdict['UNCERTAIN'])}")

    # safety filter for DELETEs
    to_delete = []
    skipped_guard = []
    skipped_scope = []
    skipped_missing = []

    for e in by_verdict["DELETE"]:
        path = e["path"]
        # sanity: must be inside allowed prefixes
        if not any(path.startswith(p) for p in ALLOWED_PREFIXES):
            skipped_scope.append(e)
            continue
        if is_guarded(path):
            skipped_guard.append(e)
            continue
        abs_path = REPO / path
        if not abs_path.exists():
            skipped_missing.append(e)
            continue
        to_delete.append(e)

    print(f"\nDeleting: {len(to_delete)}")
    print(f"  Skipped (out of scope): {len(skipped_scope)}")
    print(f"  Skipped (canonical guard): {len(skipped_guard)}")
    print(f"  Skipped (missing): {len(skipped_missing)}")

    # Execute deletions
    deleted_records = []
    for e in to_delete:
        abs_path = REPO / e["path"]
        size = abs_path.stat().st_size
        abs_path.unlink()
        deleted_records.append({
            "path": e["path"],
            "size_bytes": size,
            "reason": e.get("reason", ""),
            "batch": e.get("_batch", ""),
        })

    # Write deletion log
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "---",
        "title: Deleted files log — deep multi-agent cleanup",
        f"generated: '{now}'",
        "type: cleanup-log",
        "mode: deep-substance-review",
        "---",
        "",
        "# raw/books-md/ deep cleanup — multi-agent content review",
        "",
        f"**Run:** {now}",
        f"**Scope:** raw/books-md/meta/ + raw/books-md/philosophy/",
        f"**Total reviewed:** {len(all_verdicts)}",
        f"**KEEP:** {len(by_verdict['KEEP'])}",
        f"**DELETE:** {len(by_verdict['DELETE'])} (executed: {len(deleted_records)})",
        f"**UNCERTAIN (kept, flagged):** {len(by_verdict['UNCERTAIN'])}",
        "",
        "## By subcategory",
        "",
    ]

    for subcat in ("meta", "philosophy"):
        total = sum(1 for e in all_verdicts if f"/{subcat}/" in e["path"])
        kept = sum(1 for e in by_verdict["KEEP"] if f"/{subcat}/" in e["path"])
        deleted = sum(1 for e in deleted_records if f"/{subcat}/" in e["path"])
        uncertain = sum(1 for e in by_verdict["UNCERTAIN"] if f"/{subcat}/" in e["path"])
        lines.append(f"- **{subcat}/**: {total} → {total - deleted} (deleted {deleted}, uncertain-kept {uncertain})")

    lines += [
        "",
        "## Deleted files",
        "",
        "| Path | Size | Reason | Batch |",
        "|---|---:|---|---|",
    ]
    for r in sorted(deleted_records, key=lambda x: x["path"]):
        reason_short = r["reason"].replace("|", "/")[:100]
        lines.append(f"| `{r['path']}` | {r['size_bytes']:,} | {reason_short} | {r['batch']} |")

    if by_verdict["UNCERTAIN"]:
        lines += [
            "",
            "## Uncertain (kept, flagged)",
            "",
            "| Path | Reason | Batch |",
            "|---|---|---|",
        ]
        for e in sorted(by_verdict["UNCERTAIN"], key=lambda x: x["path"]):
            lines.append(f"| `{e['path']}` | {e['reason'].replace('|','/')[:120]} | {e.get('_batch','')} |")

    if skipped_guard:
        lines += [
            "",
            "## Skipped (canonical guard)",
            "",
        ]
        for e in skipped_guard:
            lines.append(f"- `{e['path']}` — {e['reason']}")

    LOG_PATH.write_text("\n".join(lines) + "\n")
    print(f"\nLog written: {LOG_PATH}")


if __name__ == "__main__":
    main()
