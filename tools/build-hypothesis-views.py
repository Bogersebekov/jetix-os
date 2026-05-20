#!/usr/bin/env python3
"""
tools/build-hypothesis-views.py — CRM-style hypothesis overlay aggregation (Layer 3).

Aggregates hypothesis-linked content across all markdown files в repo.
Walks repo для frontmatter `linked_hypotheses: [H-NNN]` field.

Builds:
- crm/hypothesis-views/by-hypothesis.md (H-NNN → list of linked artefacts)
- crm/hypothesis-views/by-artefact-type.md (group by path-prefix)
- crm/hypothesis-views/orphans.md (hypotheses без linked_artefacts)

Usage:
  cd ~/jetix-os
  python3 tools/build-hypothesis-views.py

Filesystem-authoritative: source = MD frontmatter; views = derived.
Idempotent + safe re-run.
"""
import os
import sys
import re
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("FAIL: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", "venv", ".venv",
                ".claude/worktrees", "raw/external", "archive"}
OUT_DIR = REPO_ROOT / "crm" / "hypothesis-views"
HYPOTHESES_DIR = REPO_ROOT / "hypotheses"

H_NNN_PATTERN = re.compile(r"^H-\d{3}$")


def parse_frontmatter(md_path):
    try:
        with open(md_path, encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return None
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 4)
    if end == -1:
        return None
    try:
        return yaml.safe_load(content[4:end])
    except yaml.YAMLError:
        return None


def is_excluded(path):
    parts = path.parts
    for excl in EXCLUDE_DIRS:
        excl_parts = excl.split("/")
        # Check if any consecutive parts match excluded segments
        for i in range(len(parts) - len(excl_parts) + 1):
            if list(parts[i:i + len(excl_parts)]) == excl_parts:
                return True
    return False


def walk_repo():
    """Walk all .md files; collect linked_hypotheses + hypothesis files themselves."""
    hypothesis_to_artefacts = defaultdict(list)
    hypothesis_files = {}  # H-NNN → file path (for hypothesis-side index)

    for md_file in REPO_ROOT.rglob("*.md"):
        rel = md_file.relative_to(REPO_ROOT)
        if is_excluded(rel):
            continue

        fm = parse_frontmatter(md_file)
        if not fm or not isinstance(fm, dict):
            continue

        # Hypothesis file itself — capture its linked_artefacts going *out*
        h_id = fm.get("id", "")
        if isinstance(h_id, str) and H_NNN_PATTERN.match(h_id):
            hypothesis_files[h_id] = str(rel)
            linked_arts = fm.get("linked_artefacts", []) or []
            if isinstance(linked_arts, list):
                for art in linked_arts:
                    if art:
                        hypothesis_to_artefacts[h_id].append({
                            "path": str(art),
                            "source": "hypothesis-side"
                        })

        # External artefact pointing к hypothesis
        linked = fm.get("linked_hypotheses", []) or []
        if isinstance(linked, list):
            for h in linked:
                if isinstance(h, str) and H_NNN_PATTERN.match(h):
                    hypothesis_to_artefacts[h].append({
                        "path": str(rel),
                        "source": "artefact-side"
                    })

    return hypothesis_to_artefacts, hypothesis_files


def write_by_hypothesis(mapping, hypothesis_files):
    out_file = OUT_DIR / "by-hypothesis.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("title: Hypotheses → Linked Artefacts (CRM-style overlay)\n")
        f.write("type: auto-generated-view\n")
        f.write("generated_by: tools/build-hypothesis-views.py\n")
        f.write(f"hypothesis_count: {len(mapping)}\n")
        f.write("---\n\n")
        f.write("# Hypotheses → Linked Artefacts\n\n")
        f.write("> Auto-generated. Hypothesis ID → all MD files cross-linked.\n")
        f.write("> Source: frontmatter `linked_artefacts` (hypothesis-side) + `linked_hypotheses` (artefact-side).\n\n")

        all_keys = sorted(set(mapping.keys()) | set(hypothesis_files.keys()))
        for h_id in all_keys:
            f.write(f"## {h_id}\n")
            hyp_file = hypothesis_files.get(h_id)
            if hyp_file:
                f.write(f"- **Hypothesis file:** [{hyp_file}](/{hyp_file})\n")
            arts = mapping.get(h_id, [])
            if arts:
                # Deduplicate
                seen = set()
                for a in arts:
                    key = (a["path"], a["source"])
                    if key in seen:
                        continue
                    seen.add(key)
                    f.write(f"- {a['path']} _(via {a['source']})_\n")
            else:
                f.write("- *(no linked artefacts)*\n")
            f.write("\n")


def write_by_artefact_type(mapping):
    """Group linked artefacts by top-level dir."""
    by_type = defaultdict(lambda: defaultdict(set))
    for h_id, arts in mapping.items():
        for a in arts:
            top = a["path"].split("/", 1)[0] if "/" in a["path"] else a["path"]
            by_type[top][h_id].add(a["path"])

    out_file = OUT_DIR / "by-artefact-type.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("title: Hypotheses grouped by Artefact Type\n")
        f.write("type: auto-generated-view\n")
        f.write("generated_by: tools/build-hypothesis-views.py\n")
        f.write("---\n\n")
        f.write("# Linked Artefacts by Type\n\n")
        f.write("> Group by top-level directory (wiki/concepts, decisions/, reports/, etc.).\n\n")

        for top in sorted(by_type.keys()):
            f.write(f"## {top}/\n\n")
            for h_id in sorted(by_type[top].keys()):
                f.write(f"- **{h_id}**\n")
                for p in sorted(by_type[top][h_id]):
                    f.write(f"  - {p}\n")
            f.write("\n")


def write_orphans(mapping, hypothesis_files):
    """Hypotheses без any linked_artefacts (neither side)."""
    out_file = OUT_DIR / "orphans.md"
    orphans = [h_id for h_id in hypothesis_files if not mapping.get(h_id)]

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("title: Orphan Hypotheses (no linked artefacts)\n")
        f.write("type: auto-generated-view\n")
        f.write("generated_by: tools/build-hypothesis-views.py\n")
        f.write(f"orphan_count: {len(orphans)}\n")
        f.write("---\n\n")
        f.write("# Orphan Hypotheses\n\n")
        f.write("> Hypotheses без cross-links к артефактам в repo.\n")
        f.write("> Action: review whether artefact creation pending OR hypothesis genuinely isolated.\n\n")

        if not orphans:
            f.write("*No orphans.*\n")
        else:
            for h_id in sorted(orphans):
                f.write(f"- {h_id} — {hypothesis_files[h_id]}\n")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    mapping, hypothesis_files = walk_repo()

    print(f"Found {len(hypothesis_files)} hypothesis files (with H-NNN id)")
    print(f"Found cross-links для {len(mapping)} hypotheses")

    write_by_hypothesis(mapping, hypothesis_files)
    write_by_artefact_type(mapping)
    write_orphans(mapping, hypothesis_files)

    print(f"Wrote {OUT_DIR}/by-hypothesis.md")
    print(f"Wrote {OUT_DIR}/by-artefact-type.md")
    print(f"Wrote {OUT_DIR}/orphans.md")


if __name__ == "__main__":
    main()
