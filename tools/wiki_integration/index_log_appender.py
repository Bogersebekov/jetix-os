"""index_log_appender — sentinel-aware append to wiki/index.md and wiki/log.md.

Per PLAN.md §5.2:
  - wiki/index.md is structured by ## section headers (## Concepts, ## Ideas, …)
    Insert new bullet for new entry under correct section, before next section header.
    Preserve all hand-curated formatting (no rewrite, just an insertion).
  - wiki/log.md is append-only, newest entries on top per CLAUDE.md global rules.
    Insert new entries after the H1 header / opening prose, on top.
"""

import re
from datetime import date
from pathlib import Path
from typing import Iterable, List, Optional


# ─── index.md section names per entity_type ─────────────────────────────────

ENTITY_TO_SECTION_HEADER = {
    "concepts":    "Concepts",
    "ideas":       "Ideas",
    "claims":      "Claims",
    "topics":      "Topics",
    "entities":    "Entities",
    "sources":     "Sources",
    "summaries":   "Summaries",
    "experiments": "Experiments",
    "foundations": "Foundations",
}


def _ensure_section(text: str, section_name: str) -> str:
    """Ensure '## <section_name>' exists. If not, append at end of file."""
    pattern = re.compile(rf"^##\s+{re.escape(section_name)}\s*$", re.MULTILINE)
    if pattern.search(text):
        return text
    addition = f"\n## {section_name}\n"
    return text.rstrip() + addition + "\n"


def _insert_under_section(
    text: str, section_name: str, new_lines: List[str]
) -> str:
    """Insert new_lines under '## <section_name>', before next ## or end-of-file.

    Inserts AT THE END of the section (before the next ## or EOF).
    """
    text = _ensure_section(text, section_name)
    # Find section start
    section_re = re.compile(rf"^##\s+{re.escape(section_name)}\s*$", re.MULTILINE)
    sm = section_re.search(text)
    assert sm is not None
    # Find next section start after this one (or EOF)
    next_re = re.compile(r"^##\s+", re.MULTILINE)
    nm = next_re.search(text, sm.end())
    insert_at = nm.start() if nm else len(text)
    # If insert_at is preceded by blank line, keep it; else add one
    prefix = text[:insert_at]
    suffix = text[insert_at:]
    block = "\n".join(new_lines).rstrip() + "\n"
    if not prefix.endswith("\n"):
        block = "\n" + block
    if suffix and not block.endswith("\n\n"):
        block = block + "\n"
    return prefix + block + suffix


def append_index_entry(
    index_path: Path,
    entity_type: str,
    title: str,
    rel_path: str,
    summary: str,
    niche: Optional[str] = None,
    sources_count: Optional[int] = None,
) -> bool:
    """Append a single bullet to wiki/index.md under the appropriate section.

    Returns True if inserted, False if duplicate path detected.
    """
    section = ENTITY_TO_SECTION_HEADER.get(entity_type, "Other")
    text = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    # Dedup: skip if (rel_path) already linked anywhere
    if f"({rel_path})" in text:
        return False
    bullet = f"- [{title}]({rel_path}) — {summary}"
    if niche:
        bullet += f" [{niche}]"
    if sources_count is not None:
        bullet += f" [sources: {sources_count}]"
    new_text = _insert_under_section(text, section, [bullet])
    index_path.write_text(new_text, encoding="utf-8")
    return True


def append_log_entry(
    log_path: Path,
    text_block: str,
    today: Optional[str] = None,
) -> None:
    """Append a new log entry on top (newest first) per CLAUDE.md convention.

    text_block should be a full markdown block including the `## [DATE] [agent] ...`
    header line — caller composes per project convention.
    """
    today = today or date.today().isoformat()
    if log_path.exists():
        original = log_path.read_text(encoding="utf-8")
    else:
        original = (
            "---\n"
            "type: log\n"
            f"updated: {today}\n"
            "---\n"
            "# Log — Jetix OS Wiki\n\n"
            "Append-only хронология. Новые записи сверху.\n\n"
        )

    # Detect frontmatter end + locate insertion point: after any leading
    # `# Log` header + intro paragraph
    fm_match = re.match(r"^---\s*\n.*?\n---\s*\n", original, re.DOTALL)
    fm = fm_match.group(0) if fm_match else ""
    rest = original[len(fm):]

    # Find first '## ' header (existing entries) — insert before it
    h2 = re.search(r"^##\s+", rest, re.MULTILINE)
    if h2:
        intro = rest[: h2.start()]
        body = rest[h2.start():]
    else:
        # No existing entries — append at end
        intro = rest
        body = ""

    # Update `updated:` field in frontmatter if present
    if fm:
        new_fm = re.sub(r"^updated:\s*.+$", f"updated: {today}", fm,
                        count=1, flags=re.MULTILINE)
    else:
        new_fm = ""

    if not text_block.endswith("\n"):
        text_block += "\n"
    if intro and not intro.endswith("\n\n"):
        intro = intro.rstrip() + "\n\n"
    new_text = new_fm + intro + text_block + ("\n" if body else "") + body
    log_path.write_text(new_text, encoding="utf-8")


def make_log_block_match_to_existing(
    today: str, candidates: List[dict], tier: str
) -> str:
    """Compose a wiki/log.md block for a Tier A or B bulk-ack run."""
    n = len(candidates)
    lines = [
        f"## [{today}] [voice-bulk-ack] match-to-existing Tier {tier}: {n} edges appended | edges: +{n}",
    ]
    for c in candidates[:8]:
        memo = c.get("voice_memo", "?")
        path = c.get("matched_path", "?")
        score = c.get("score", 0.0)
        lines.append(f"- {memo} → {path} (score={score:.2f})")
    if n > 8:
        lines.append(f"- _… +{n - 8} more — see edges.jsonl_")
    return "\n".join(lines)


def make_log_block_propose_new(
    today: str, candidates: List[dict]
) -> str:
    """Compose a wiki/log.md block for a Tier C bulk-ack (new entries)."""
    n = len(candidates)
    by_type: dict = {}
    for c in candidates:
        et = c.get("entity_type", "?")
        by_type[et] = by_type.get(et, 0) + 1
    type_counts = " | ".join(f"{k}: +{v}" for k, v in sorted(by_type.items()))
    lines = [
        f"## [{today}] [voice-bulk-ack] propose-new Tier C: {n} new wiki entries created | {type_counts}",
    ]
    for c in candidates[:8]:
        memo = c.get("voice_memo", "?")
        path = c.get("rel_path", "?")
        lines.append(f"- {memo} → wiki/{path}")
    if n > 8:
        lines.append(f"- _… +{n - 8} more — see wiki/index.md_")
    return "\n".join(lines)


# ─── Smoke test ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import tempfile
    print("index_log_appender smoke test")
    print("=" * 60)
    with tempfile.TemporaryDirectory() as tmpdir:
        idx = Path(tmpdir) / "index.md"
        idx.write_text(
            "---\ntype: index\n---\n"
            "# Index\n\n"
            "## Concepts\n"
            "- [Old concept](concepts/old.md) — existing entry\n\n"
            "## Ideas\n"
            "- [Old idea](ideas/old.md) — existing entry\n",
            encoding="utf-8"
        )
        # Test append concept
        ok1 = append_index_entry(idx, "concepts", "New concept", "concepts/new.md",
                                  "first new entry test", niche="business")
        # Test append idea (different section)
        ok2 = append_index_entry(idx, "ideas", "Some new idea", "ideas/some-new.md",
                                  "second test", niche="meta")
        # Test dedup
        ok3 = append_index_entry(idx, "concepts", "Dup", "concepts/new.md",
                                  "duplicate test")
        # Test brand-new section
        ok4 = append_index_entry(idx, "claims", "New claim", "claims/c.md",
                                  "claim test", niche="business")
        print(f"appended results: concept={ok1}, idea={ok2}, dup={ok3}, claim={ok4}")
        print()
        print("=== final index.md ===")
        print(idx.read_text())

        # Test log
        log = Path(tmpdir) / "log.md"
        log.write_text(
            "---\ntype: log\nupdated: 2026-04-30\n---\n"
            "# Log — Jetix OS Wiki\n\n"
            "Append-only.\n\n"
            "## [2026-04-30] previous entry\nbody\n",
            encoding="utf-8"
        )
        block = make_log_block_match_to_existing(
            "2026-05-10",
            [{"voice_memo": "audio_587", "matched_path": "concepts/x.md", "score": 0.92}],
            "A"
        )
        append_log_entry(log, block, today="2026-05-10")
        print("=== final log.md ===")
        print(log.read_text())
    print("=" * 60)
