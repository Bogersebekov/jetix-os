"""cli — argparse entry-point for /wiki-bulk-ack skill.

Usage:
    python3 -m tools.wiki_integration.cli --tier A [--dry-run]
    python3 -m tools.wiki_integration.cli --tier B --select 1,3,5,7-10 [--dry-run]
    python3 -m tools.wiki_integration.cli --tier C --select N,M,P --as-new [--dry-run]
    python3 -m tools.wiki_integration.cli --status
    python3 -m tools.wiki_integration.cli --reject 1,2 --reason "low quality"
    python3 -m tools.wiki_integration.cli --defer-backlog 5,6,7

Sidecar default: reports/voice-pipeline-<latest-date>/04-wiki-candidates-v2.json
Override with --sidecar.
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Optional

from tools.wiki_integration.auto_merger import (
    EDGES_PATH, INDEX_PATH, LOG_PATH, WIKI_ROOT,
    load_sidecar, merge_match_to_existing, merge_propose_new,
    parse_selection, status_summary,
)


def _find_default_sidecar() -> Optional[Path]:
    root = Path("/home/ruslan/jetix-os/reports")
    candidates = sorted(root.glob("voice-pipeline-*/04-wiki-candidates-v2.json"))
    return candidates[-1] if candidates else None


def main(argv=None):
    p = argparse.ArgumentParser(description="Wiki bulk-ack CLI for voice→wiki Stage 5 v2")
    p.add_argument("--tier", choices=["A", "B", "C"], help="Tier to process")
    p.add_argument("--select", help="Indices to process: '1,3,5,7-10'")
    p.add_argument("--as-new", action="store_true", help="(Tier C) create new entries")
    p.add_argument("--dry-run", action="store_true", help="Preview without writes")
    p.add_argument("--status", action="store_true", help="Print sidecar status summary")
    p.add_argument("--reject", help="Indices to mark rejected (no wiki write)")
    p.add_argument("--defer-backlog", help="Indices to move to backlog (no wiki write)")
    p.add_argument("--reason", default="", help="Free-text reason for reject/defer")
    p.add_argument("--sidecar", help="Override sidecar JSON path")
    p.add_argument("--today", help="Override today's date YYYY-MM-DD")

    args = p.parse_args(argv)
    sidecar_path = Path(args.sidecar) if args.sidecar else _find_default_sidecar()
    if not sidecar_path or not sidecar_path.exists():
        print(f"ERROR: sidecar not found ({sidecar_path}). Run voice pipeline Stage 5 v2 first.")
        return 2

    if args.status:
        s = status_summary(sidecar_path)
        print(json.dumps(s, ensure_ascii=False, indent=2))
        return 0

    if args.reject:
        indices = parse_selection(args.reject)
        print(f"Rejected {len(indices)} indices: {sorted(indices)}")
        print(f"Reason: {args.reason or '(none)'}")
        # No-op on disk — log to sidecar's discipline log
        return 0

    if args.defer_backlog:
        indices = parse_selection(args.defer_backlog)
        print(f"Deferred {len(indices)} indices to backlog: {sorted(indices)}")
        return 0

    if not args.tier:
        p.print_help()
        return 1

    sidecar = load_sidecar(sidecar_path)
    today = args.today or date.today().isoformat()

    if args.tier == "A":
        report = merge_match_to_existing(sidecar, "A", dry_run=args.dry_run, today=today)
    elif args.tier == "B":
        if not args.select:
            print("ERROR: --tier B requires --select")
            return 2
        report = merge_match_to_existing(
            sidecar, "B", parse_selection(args.select),
            dry_run=args.dry_run, today=today,
        )
    elif args.tier == "C":
        if not args.select:
            print("ERROR: --tier C requires --select")
            return 2
        report = merge_propose_new(
            sidecar, parse_selection(args.select),
            dry_run=args.dry_run, today=today,
        )
    else:
        print(f"unknown tier: {args.tier}")
        return 1

    print(report.summary())
    print()
    for a in report.actions[:30]:
        print(f"  - {a.kind}: {a.detail}")
    if len(report.actions) > 30:
        print(f"  - … +{len(report.actions) - 30} more")
    if report.errors:
        print(f"\nErrors ({len(report.errors)}):")
        for e in report.errors[:10]:
            print(f"  ! {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
