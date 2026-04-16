#!/usr/bin/env python3
"""
Phase 5 of system-design sweep — bulk-tag wiki pages with topics: [system-design].

Reads YAML frontmatter, adds `topics: [system-design]` if not present.
Does not modify body. Idempotent.
"""
import sys
from pathlib import Path
import re

WIKI = Path(__file__).parent.parent / "wiki"

UNCLEAR_IDEAS = {
    "cannabis-refusal-beast-mode-orientation",      # личная практика без явной system-связки
    "safe-hedonism-personal-motivation",            # личная мотивация Ruslana, не system principle
    "money-value-mindset-pre-launch",               # mindset работа, перед запуском, не system
    "urgent-search-ai-analyst-communities",         # operational task, не system design
}

UNCLEAR_CLAIMS = {
    "ai-agents-market-size-2026",
    "business-vulnerability-via-ai-default",
    "mittelstand-opportunity-window",
    "orchestration-layer-will-be-absorbed",
}

UNCLEAR_ENTITIES = {
    "github",
    "linux",
}


def has_system_design_topic(text: str) -> bool:
    """Return True if frontmatter already mentions topics: [system-design]."""
    fm_end = text.find("\n---", 4)
    if fm_end == -1:
        return False
    fm = text[:fm_end]
    return bool(re.search(r"^\s*topics:\s*\[.*system-design.*\]", fm, re.MULTILINE)) \
        or bool(re.search(r"^\s*topics:\s*\n(\s*-.*\n)*\s*-\s*system-design", fm, re.MULTILINE))


def tag_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return "no-frontmatter"
    fm_end = text.find("\n---", 4)
    if fm_end == -1:
        return "broken-frontmatter"
    if has_system_design_topic(text):
        return "already-tagged"

    fm = text[:fm_end]
    rest = text[fm_end:]

    # Insert `topics: [system-design]` right after `tags:` line if exists,
    # else right after `niche:` line, else right before closing of frontmatter.
    insert_line = "topics: [system-design]"
    new_fm = None

    # Try after tags: ...
    m = re.search(r"^tags:.*$", fm, re.MULTILINE)
    if m:
        idx = m.end()
        new_fm = fm[:idx] + "\n" + insert_line + fm[idx:]
    else:
        m = re.search(r"^niche:.*$", fm, re.MULTILINE)
        if m:
            idx = m.end()
            new_fm = fm[:idx] + "\n" + insert_line + fm[idx:]
        else:
            new_fm = fm + "\n" + insert_line

    path.write_text(new_fm + rest, encoding="utf-8")
    return "tagged"


def process(dir_name: str, exclude: set) -> dict:
    counts = {"tagged": 0, "skipped-unclear": 0, "already-tagged": 0,
              "no-frontmatter": 0, "broken-frontmatter": 0}
    target = WIKI / dir_name
    if not target.exists():
        return counts
    for f in sorted(target.glob("*.md")):
        slug = f.stem
        if slug in exclude:
            counts["skipped-unclear"] += 1
            continue
        result = tag_file(f)
        counts[result] = counts.get(result, 0) + 1
    return counts


def main():
    print("=== Phase 5 tagging ===")
    print(f"ideas/ : {process('ideas', UNCLEAR_IDEAS)}")
    print(f"concepts/ : {process('concepts', set())}")
    print(f"claims/ : {process('claims', UNCLEAR_CLAIMS)}")
    print(f"entities/ : {process('entities', UNCLEAR_ENTITIES)}")


if __name__ == "__main__":
    main()
