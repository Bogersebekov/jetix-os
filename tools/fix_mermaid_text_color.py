#!/usr/bin/env python3
"""
fix_mermaid_text_color.py — добавить theme init line в каждый ```mermaid блок
чтобы текст рендерился чёрным на любом background.

Idempotent: skip blocks где init уже добавлен.

Usage: python3 tools/fix_mermaid_text_color.py [--dry]
"""

import re
import sys
from pathlib import Path

INIT_LINE = (
    "%%{init: {'theme':'base', 'themeVariables': "
    "{'primaryTextColor':'#000000','textColor':'#000000',"
    "'lineColor':'#333333','primaryBorderColor':'#333333',"
    "'primaryColor':'#fafafa','noteTextColor':'#000000',"
    "'noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%"
)

# Skip directories
SKIP_PARTS = {
    ".git", "_archived", "archive", "inbox", "inbox-reocr",
    "node_modules", "external",
}
SKIP_PATH_FRAGMENTS = [".claude/worktrees/"]


def should_skip(path: Path, repo: Path) -> bool:
    rel = path.relative_to(repo)
    rel_str = str(rel).replace("\\", "/")
    if any(fragment in rel_str for fragment in SKIP_PATH_FRAGMENTS):
        return True
    if any(part in SKIP_PARTS for part in rel.parts):
        return True
    return False


def fix_file(path: Path, dry: bool) -> int:
    """Return count of mermaid blocks updated."""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return 0
    # Match opening ```mermaid line + optional newline; insert init unless next non-empty line starts with %%{init
    pattern = re.compile(r"(^```mermaid[^\n]*\n)(?!%%\{init)", re.MULTILINE)
    new_text, n = pattern.subn(r"\1" + INIT_LINE + "\n", text)
    if n > 0 and not dry:
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return n


def main():
    dry = "--dry" in sys.argv
    repo = Path(__file__).resolve().parent.parent
    total_files = 0
    total_blocks = 0
    changed_files = []
    for md in repo.rglob("*.md"):
        if should_skip(md, repo):
            continue
        n = fix_file(md, dry)
        if n > 0:
            total_files += 1
            total_blocks += n
            changed_files.append((str(md.relative_to(repo)), n))
    mode = "DRY-RUN" if dry else "APPLIED"
    print(f"[{mode}] Files updated: {total_files} / Blocks patched: {total_blocks}")
    for path, n in sorted(changed_files):
        print(f"  {path}  ({n})")


if __name__ == "__main__":
    main()
