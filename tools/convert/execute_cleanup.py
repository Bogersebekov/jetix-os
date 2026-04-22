#!/usr/bin/env python3
"""Execute cleanup per tmp/cleanup_plan.json; write _DELETED-LOG.md."""
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

REPO = Path("/home/ruslan/jetix-os")
plan = json.loads((REPO / "tmp" / "cleanup_plan.json").read_text())
deletes = plan["delete"]
unclear = plan["unclear"]

# Safety re-check: no failed books should be in delete list
FAILED = {
    "raw/books-md/cybernetics/beer-brain-of-the-firm-1972.md",
    "raw/books-md/cybernetics/wiener-cybernetics-2ed-1961.md",
    "raw/books-md/mgmt/grove-only-paranoid-survive-1996.md",
    "raw/books-md/mgmt/drucker-effective-executive-2006.md",
    "raw/books-md/pdm/cagan-inspired-2ed-2017.md",
    "raw/books-md/philosophy-science/popper-conjectures-and-refutations-1963.md",
    "raw/books-md/engineering-foundations/vincenti-what-engineers-know-1990.md",
    "raw/books-md/clean-code/brooks-mythical-man-month-1995.md",
}
violations = [e for e in deletes if e["path"] in FAILED]
if violations:
    raise SystemExit(f"ABORT: failed books in delete list: {violations}")

# Pre/post subcat counts
root = REPO / "raw" / "books-md"
before_counts = {}
for sc in sorted(root.iterdir()):
    if sc.is_dir():
        before_counts[sc.name] = sum(1 for p in sc.iterdir()
                                     if p.is_file() and p.suffix == ".md")

# Delete
deleted = 0
failed = []
for e in deletes:
    p = REPO / e["path"]
    if not p.exists():
        failed.append(f"missing: {e['path']}")
        continue
    p.unlink()
    deleted += 1

# After counts
after_counts = {}
for sc in sorted(root.iterdir()):
    if sc.is_dir():
        after_counts[sc.name] = sum(1 for p in sc.iterdir()
                                    if p.is_file() and p.suffix == ".md")

# Write _DELETED-LOG.md
log_path = REPO / "raw" / "books-md" / "_DELETED-LOG.md"
now = datetime.now().strftime("%Y-%m-%d %H:%M")
rule_counts = Counter(e["reason"].split(":")[0] for e in deletes)
by_subcat = defaultdict(list)
for e in deletes:
    by_subcat[e["path"].split("/")[2]].append(e)

lines = [
    "---",
    "title: Deleted files log",
    f"generated: '{now}'",
    "type: cleanup-log",
    "---",
    "",
    "# raw/books-md/ cleanup — deleted files",
    "",
    f"**Run:** {now}",
    f"**Deleted:** {deleted}",
    f"**Unclear (kept, flagged):** {len(unclear)}",
    "",
    "## By rule",
    "",
]
for rule, count in rule_counts.most_common():
    lines.append(f"- `{rule}`: {count}")
lines.append("")

lines.append("## By subcategory")
lines.append("")
lines.append("| Subcat | Before | After | Deleted |")
lines.append("|---|---:|---:|---:|")
for sc in sorted(before_counts):
    b, a = before_counts[sc], after_counts[sc]
    lines.append(f"| {sc} | {b} | {a} | {b - a} |")
total_before = sum(before_counts.values())
total_after = sum(after_counts.values())
lines.append(f"| **TOTAL** | **{total_before}** | **{total_after}** | "
             f"**{total_before - total_after}** |")
lines.append("")

lines.append("## Deleted files (per subcat)")
lines.append("")
for sc in sorted(by_subcat):
    lines.append(f"### {sc} ({len(by_subcat[sc])})")
    lines.append("")
    lines.append("| Path | Size | wc | grade | Reason |")
    lines.append("|---|---:|---:|:---:|---|")
    for e in sorted(by_subcat[sc], key=lambda x: x["path"]):
        wc = e.get("word_count", "")
        grade = e.get("quality_grade", "") or ""
        reason = e["reason"].replace("|", "\\|")
        lines.append(f"| `{e['path']}` | {e['size']} | {wc} | {grade} | "
                     f"{reason} |")
    lines.append("")

if unclear:
    lines.append("## Unclear (kept, flagged for review)")
    lines.append("")
    for e in unclear:
        lines.append(f"- `{e['path']}` — {e['reason']}")
    lines.append("")
else:
    lines.append("## Unclear")
    lines.append("")
    lines.append("_None — scan had zero unclear candidates._")
    lines.append("")

lines.append("## Failed books (NOT deleted, awaiting re-OCR)")
lines.append("")
for fb in sorted(FAILED):
    lines.append(f"- `{fb}`")
lines.append("")

log_path.write_text("\n".join(lines))
print(f"deleted {deleted} files")
print(f"wrote {log_path}")
if failed:
    print("non-fatal issues:")
    for f in failed:
        print(f"  {f}")
