"""auto_merger — orchestrates merge for approved bulk-ack candidates.

Called by the /wiki-bulk-ack skill (via tools/wiki_integration/cli.py shim).

Per PLAN.md §5:
  Tier A — match-to-existing → append edge to wiki/graph/edges.jsonl + log entry
  Tier B — same as A for selected indices
  Tier C — create new wiki entry from template + index entry + log entry +
           voice→new edge + (top-2 BM25 neighbor) related_to edges

Constitutional invariants enforced:
  - existing wiki entry frontmatter/body NEVER modified (Tier A/B = edge-only)
  - all writes append-only
  - Tier C strict frontmatter validation; rejects → discipline log
  - dry-run mode previews without writing

Reads candidates from a v2-format YAML/JSON sidecar produced by Stage 5 v2;
the sidecar is the machine-readable twin of 04-wiki-candidates-v2.md.
"""

import json
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

from tools.wiki_integration.edge_writer import (
    append_edges,
    make_neighbor_edge,
    make_voice_to_new_edge,
    make_voice_to_wiki_edge,
)
from tools.wiki_integration.index_log_appender import (
    append_index_entry,
    append_log_entry,
    make_log_block_match_to_existing,
    make_log_block_propose_new,
)
from tools.wiki_integration.template_filler import fill_template


WIKI_ROOT = Path("/home/ruslan/jetix-os/wiki")
EDGES_PATH = WIKI_ROOT / "graph" / "edges.jsonl"
INDEX_PATH = WIKI_ROOT / "index.md"
LOG_PATH = WIKI_ROOT / "log.md"


# ─── Sidecar loader ─────────────────────────────────────────────────────────

def load_sidecar(sidecar_path: Path) -> Dict[str, Any]:
    """Load JSON sidecar produced by Stage 5 v2 — see voice-pipeline-orchestrator.py."""
    if not sidecar_path.exists():
        raise FileNotFoundError(f"sidecar not found: {sidecar_path}")
    return json.loads(sidecar_path.read_text(encoding="utf-8"))


# ─── Selection parser ──────────────────────────────────────────────────────

def parse_selection(spec: str) -> Set[int]:
    """Parse '1,3,5,7-10' → {1,3,5,7,8,9,10}."""
    out: Set[int] = set()
    if not spec:
        return out
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if "-" in chunk:
            a, b = chunk.split("-", 1)
            a_i, b_i = int(a), int(b)
            for i in range(a_i, b_i + 1):
                out.add(i)
        elif chunk:
            out.add(int(chunk))
    return out


# ─── Merge actions ──────────────────────────────────────────────────────────

@dataclass
class MergeAction:
    kind: str               # "edge" | "new_entry" | "index" | "log" | "skip"
    detail: str
    target: Optional[str] = None


@dataclass
class MergeReport:
    tier: str
    dry_run: bool
    actions: List[MergeAction] = field(default_factory=list)
    edges_appended: int = 0
    edges_skipped_dup: int = 0
    edges_rejected: int = 0
    new_entries_created: int = 0
    index_entries_added: int = 0
    log_entries_added: int = 0
    skipped_validation: int = 0
    errors: List[str] = field(default_factory=list)

    def add(self, kind: str, detail: str, target: Optional[str] = None):
        self.actions.append(MergeAction(kind, detail, target))

    def summary(self) -> str:
        return (
            f"tier={self.tier} dry_run={self.dry_run} "
            f"edges +{self.edges_appended} (dup {self.edges_skipped_dup}, rej {self.edges_rejected}) "
            f"new_entries +{self.new_entries_created} "
            f"index +{self.index_entries_added} "
            f"log +{self.log_entries_added} "
            f"skipped_validation {self.skipped_validation} errors {len(self.errors)}"
        )


# ─── Tier A / B merger (edge-only) ─────────────────────────────────────────

def merge_match_to_existing(
    sidecar: Dict[str, Any],
    tier: str,                 # "A" or "B"
    selected_indices: Optional[Set[int]] = None,
    dry_run: bool = False,
    today: Optional[str] = None,
    edges_path: Path = EDGES_PATH,
    log_path: Path = LOG_PATH,
) -> MergeReport:
    """Merge approved match-to-existing candidates as edges.

    Args:
        sidecar: parsed JSON sidecar
        tier: "A" → all tier_A candidates; "B" → use selected_indices
        selected_indices: 1-based indices into the tier list (required for B)
    """
    today = today or date.today().isoformat()
    report = MergeReport(tier=f"{tier} (match-to-existing)", dry_run=dry_run)

    key = f"tier_{tier.lower()}"
    items = sidecar.get(key, [])
    if tier.upper() == "B" and selected_indices is None:
        report.errors.append("Tier B requires --select indices")
        return report
    if selected_indices:
        items = [it for i, it in enumerate(items, 1) if i in selected_indices]

    edges_to_append: List[Dict[str, Any]] = []
    log_summary_items: List[Dict[str, Any]] = []
    for it in items:
        memo_stem = (it.get("voice_memo") or it.get("appeared_in_memos", ["unknown"])[0])
        wiki_path = it.get("matched_path") or it.get("best_match")
        score = float(it.get("score", 0.0))
        bm25 = it.get("bm25")
        if not memo_stem or not wiki_path:
            report.errors.append(f"missing memo/path on item: {it.get('content', '')[:60]}")
            continue
        edge = make_voice_to_wiki_edge(
            memo_stem, wiki_path,
            predicate="mentions",
            created=today,
            score=score,
            bm25=bm25 if isinstance(bm25, (int, float)) else None,
        )
        edges_to_append.append(edge)
        log_summary_items.append({
            "voice_memo": memo_stem,
            "matched_path": wiki_path,
            "score": score,
        })
        report.add("edge",
                   f"voice/{memo_stem} → {wiki_path} (score={score:.2f})",
                   wiki_path)

    if dry_run:
        return report

    # Apply edges
    if edges_to_append:
        r = append_edges(edges_path, edges_to_append)
        report.edges_appended = r["appended"]
        report.edges_skipped_dup = r["skipped_dup"]
        report.edges_rejected = r["rejected"]

    # Append log entry
    if log_summary_items:
        block = make_log_block_match_to_existing(today, log_summary_items, tier.upper())
        append_log_entry(log_path, block, today=today)
        report.log_entries_added = 1

    return report


# ─── Tier C merger (new entry creation) ─────────────────────────────────────

def merge_propose_new(
    sidecar: Dict[str, Any],
    selected_indices: Optional[Set[int]] = None,
    dry_run: bool = False,
    today: Optional[str] = None,
    wiki_root: Path = WIKI_ROOT,
    edges_path: Path = EDGES_PATH,
    index_path: Path = INDEX_PATH,
    log_path: Path = LOG_PATH,
    strict: bool = True,
) -> MergeReport:
    """Create new wiki entries for selected Tier C candidates."""
    today = today or date.today().isoformat()
    report = MergeReport(tier="C (propose-new)", dry_run=dry_run)

    items = sidecar.get("tier_c", [])
    if selected_indices is None:
        report.errors.append("Tier C requires --select indices")
        return report
    items = [it for i, it in enumerate(items, 1) if i in selected_indices]

    edges_to_append: List[Dict[str, Any]] = []
    log_summary_items: List[Dict[str, Any]] = []
    for it in items:
        memo_stem = (it.get("voice_memo") or it.get("appeared_in_memos", ["unknown"])[0])
        # Build template from item dict (need original item shape)
        synthetic = {
            "category": it.get("category"),
            "content": it.get("content_full") or it.get("content", "") or it.get("content_preview"),
            "project": it.get("project"),
            "priority": it.get("priority"),
            "sources": it.get("sources") or [memo_stem + ".json"],
        }
        filled = fill_template(synthetic, wiki_root, today=today, strict=strict)
        if filled is None:
            report.add("skip", f"category={synthetic['category']} → routed elsewhere")
            continue
        if filled.errors:
            report.skipped_validation += 1
            report.errors.append(
                f"validation FAIL on {filled.rel_path}: {', '.join(filled.errors)}"
            )
            report.add("skip", f"validation_fail: {filled.rel_path}")
            continue

        target_path = wiki_root / filled.rel_path
        report.add("new_entry", f"create {filled.rel_path}", filled.rel_path)
        if not dry_run:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(filled.full_text, encoding="utf-8")
            report.new_entries_created += 1

            # Index entry
            ok = append_index_entry(
                index_path, filled.entity_type,
                filled.title, filled.rel_path,
                # Summary = first non-empty body line
                summary=_extract_summary(filled.full_text),
                niche=filled.niche,
                sources_count=1,
            )
            if ok:
                report.index_entries_added += 1
                report.add("index", f"+ {filled.rel_path}")

        # Edges
        edges_to_append.append(make_voice_to_new_edge(
            memo_stem, filled.rel_path, created=today
        ))
        for nb in (it.get("bm25_neighbors") or [])[:2]:
            edges_to_append.append(make_neighbor_edge(
                filled.rel_path, nb["path"], created=today, bm25=float(nb.get("bm25", 0.0))
            ))

        log_summary_items.append({
            "voice_memo": memo_stem,
            "rel_path": filled.rel_path,
            "entity_type": filled.entity_type,
        })

    if dry_run:
        return report

    if edges_to_append:
        r = append_edges(edges_path, edges_to_append)
        report.edges_appended = r["appended"]
        report.edges_skipped_dup = r["skipped_dup"]
        report.edges_rejected = r["rejected"]

    if log_summary_items:
        block = make_log_block_propose_new(today, log_summary_items)
        append_log_entry(log_path, block, today=today)
        report.log_entries_added = 1

    return report


def _extract_summary(full_text: str, max_chars: int = 100) -> str:
    """Pull short summary from filled template body (after first H1)."""
    import re
    # skip frontmatter
    body = re.sub(r"^---.*?---\s*\n", "", full_text, count=1, flags=re.DOTALL)
    body = re.sub(r"^#\s+.*$\n", "", body, count=1, flags=re.MULTILINE)
    # First non-blank, non-header line
    for ln in body.splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#") or ln.startswith(">"):
            continue
        # Strip "## Section" type prefixes
        if ln.startswith("##"):
            continue
        return ln[: max_chars - 1] + ("…" if len(ln) > max_chars else "")
    return "(no summary)"


# ─── Status helper for /wiki-bulk-status ────────────────────────────────────

def status_summary(sidecar_path: Path) -> Dict[str, Any]:
    sidecar = load_sidecar(sidecar_path)
    return {
        "tier_a_count": len(sidecar.get("tier_a", [])),
        "tier_b_count": len(sidecar.get("tier_b", [])),
        "tier_c_count": len(sidecar.get("tier_c", [])),
        "skipped_count": len(sidecar.get("skipped", [])),
        "total_candidates": sidecar.get("total_candidates", "?"),
        "match_rate": sidecar.get("match_rate", "?"),
        "generated_at": sidecar.get("generated_at", "?"),
    }


# ─── Smoke test ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import tempfile
    print("auto_merger smoke test")
    print("=" * 60)
    print(f"parse_selection('1,3,5,7-10') = {sorted(parse_selection('1,3,5,7-10'))}")

    # Build a minimal sidecar
    sidecar = {
        "total_candidates": 3,
        "tier_a": [
            {"voice_memo": "audio_587", "content": "Founder isolation",
             "matched_path": "concepts/founder-isolation-as-stopper-class.md",
             "score": 0.92, "bm25": 24.6},
        ],
        "tier_b": [
            {"voice_memo": "audio_588", "content": "Engineering faith — план + инструменты",
             "matched_path": "concepts/engineering-faith.md",
             "score": 0.78, "bm25": 19.5},
        ],
        "tier_c": [
            {"voice_memo": "audio_590", "category": "Идеи",
             "content_full": "«Мастерская» как геймифицированная Life OS",
             "priority": "high",
             "bm25_neighbors": [
                 {"path": "ideas/tools-feedback-community-flywheel.md", "bm25": 8.55},
             ]},
        ],
    }

    # Dry-run Tier A
    r1 = merge_match_to_existing(sidecar, "A", dry_run=True)
    print(f"DRY RUN Tier A: {r1.summary()}")
    for a in r1.actions:
        print(f"  - {a.kind}: {a.detail}")

    # Dry-run Tier C with selection
    r2 = merge_propose_new(sidecar, selected_indices={1}, dry_run=True,
                            wiki_root=Path("/home/ruslan/jetix-os/wiki"))
    print(f"\nDRY RUN Tier C: {r2.summary()}")
    for a in r2.actions:
        print(f"  - {a.kind}: {a.detail}")
    print("=" * 60)
