#!/usr/bin/env python3
"""
Stage 1 Untangle — Aggregator.

Collects JSONL atoms from all batch outputs, assigns unique IDs,
applies TENSIONS-PRE-RESOLVED overrides (safety net), performs
conservative dedup, cross-references, clusters, and emits:
- ATOM-REGISTRY.md
- KNOT-MAP.md

Conservative dedup rule:
- Merge atoms when BOTH source AND content are near-identical
  (same source + Levenshtein ratio >= 0.90).
- Otherwise keep separate; if content similarity >= 0.80 across
  different sources, add `relates_to` reinforcement link instead.
"""

import json
import os
import re
import sys
import hashlib
import difflib
import pathlib
from collections import defaultdict, Counter
from datetime import date

EXTRACTION_DIR = "/home/ruslan/jetix-os/raw/research/architecture-variants-2026-04-22/stage1-extraction"
OUTPUT_DIR = "/home/ruslan/jetix-os/raw/research/architecture-variants-2026-04-22"
REGISTRY_PATH = os.path.join(OUTPUT_DIR, "ATOM-REGISTRY.md")
KNOTMAP_PATH = os.path.join(OUTPUT_DIR, "KNOT-MAP.md")

VALID_TYPES = {"task", "hypothesis", "concept", "principle", "claim",
               "entity", "value", "bet", "tension", "metric"}
VALID_DIMS = {"base", "life", "company", "community", "money",
              "relationships", "philosophy"}
VALID_PHASES = {"now", "phase-1", "phase-2", "phase-3", "long-term", "any"}
VALID_STATUSES = {"open", "resolved", "reinforced", "contradicted", "overridden"}


def normalize_content(s: str) -> str:
    s = (s or "").lower().strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^\wа-яё ]", "", s, flags=re.IGNORECASE)
    return s


def similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def load_all_atoms():
    atoms = []
    files_loaded = []
    for fn in sorted(os.listdir(EXTRACTION_DIR)):
        if not fn.endswith(".jsonl"):
            continue
        full = os.path.join(EXTRACTION_DIR, fn)
        files_loaded.append(fn)
        with open(full, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                # strip possible markdown fence artefacts
                if line.startswith("```"):
                    continue
                try:
                    obj = json.loads(line)
                except Exception as e:
                    print(f"WARN: {fn}:{lineno} JSON parse fail: {e}",
                          file=sys.stderr)
                    continue
                obj.setdefault("tags", [])
                obj.setdefault("relates_to", [])
                obj.setdefault("note", "")
                obj.setdefault("quote", "")
                obj.setdefault("priority", None)
                obj.setdefault("phase", "any")
                obj.setdefault("status", "open")
                obj.setdefault("dimension", "base")
                obj["_source_batch"] = fn
                atoms.append(obj)
    return atoms, files_loaded


# ---------- TENSIONS override safety net ----------

OVERRIDE_RULES = [
    # (regex_pattern_applied_to_content_or_quote, override_reason)
    (re.compile(r"\bjackson\b", re.IGNORECASE),
     "Decision 4 LOCKED — Name = Jetix. 'Jackson' = speech-recognition artefact."),
    (re.compile(r"(open[- ]source[- ]full|open[- ]source[- ]platform|public\s+open[- ]source|публичн\w+\s+open[- ]source|полност\w+\s+открыт)",
                re.IGNORECASE),
     "Decision 3 LOCKED — Closed outside / Open inside (team only)."),
    (re.compile(r"(always\s+solo\s+forever|вечн\w+\s+соло|никогда\s+не\s+команд)",
                re.IGNORECASE),
     "Decision 2 LOCKED — Solo-now-with-team-ready-scaffolding."),
    (re.compile(r"(anton\s+мент|vladislav\s+мент|rodion\s+мент|антон\s+мент|владислав\s+мент|родион\s+мент)",
                re.IGNORECASE),
     "Decision 6 LOCKED — Anton/Vladislav/Rodion не ключевые."),
    (re.compile(r"(secure\s+network\s+(as\s+)?(primary|первич|primary\s+product)\s+phase[- ]1|secure\s+network.*phase[- ]1\s+primary)",
                re.IGNORECASE),
     "Decision 5 LOCKED — Phase 1 = Consulting-first, Secure Network = Phase 2+."),
]


def apply_override_safety(atoms):
    # Fix 'Jackson' → note that original content is preserved as quote but status overridden.
    overrides_applied = 0
    for a in atoms:
        haystack = " ".join([str(a.get("content", "")), str(a.get("quote", ""))])
        for pat, reason in OVERRIDE_RULES:
            if pat.search(haystack):
                if a.get("status") != "overridden":
                    a["status"] = "overridden"
                    note = a.get("note", "") or ""
                    extra = f" [auto-override: {reason}]"
                    if extra.strip() not in note:
                        a["note"] = (note + extra).strip()
                    overrides_applied += 1
                break
    return overrides_applied


# ---------- Dedup ----------

def dedup_atoms(atoms):
    by_source_type = defaultdict(list)
    for a in atoms:
        src = a.get("source", "") or ""
        key = (src.split(":", 1)[0], a.get("type", "concept"))
        by_source_type[key].append(a)

    kept = []
    merged_count = 0
    for key, group in by_source_type.items():
        # within same source+type, dedup near-identical
        group_sorted = sorted(group, key=lambda x: len(x.get("content", "")))
        unique = []
        for a in group_sorted:
            ac = normalize_content(a.get("content", ""))
            merged = False
            for u in unique:
                uc = normalize_content(u.get("content", ""))
                if similarity(ac, uc) >= 0.90:
                    # merge metadata into u
                    merged = True
                    u_tags = set(u.get("tags", []))
                    u_tags.update(a.get("tags", []))
                    u["tags"] = sorted(u_tags)
                    # prefer longer quote
                    if len(a.get("quote", "") or "") > len(u.get("quote", "") or ""):
                        u["quote"] = a.get("quote", "")
                    # append batch provenance
                    u["_dup_batches"] = u.get("_dup_batches", [u.get("_source_batch")])
                    u["_dup_batches"].append(a.get("_source_batch"))
                    # mark reinforced if from different batches
                    if a.get("_source_batch") != u.get("_source_batch"):
                        u["status"] = "reinforced" if u.get("status") in (
                            "open", "reinforced") else u["status"]
                    merged_count += 1
                    break
            if not merged:
                unique.append(a)
        kept.extend(unique)
    return kept, merged_count


def cross_reference_reinforcements(atoms, threshold=0.80):
    # For atoms from DIFFERENT sources but similar content — add reinforces links
    # Group by type to limit comparisons (quadratic).
    by_type = defaultdict(list)
    for a in atoms:
        by_type[a.get("type", "concept")].append(a)

    links_added = 0
    for t, group in by_type.items():
        # Only do O(n^2) if group small enough; for large groups use bucket by
        # first two normalized words to reduce pairs.
        buckets = defaultdict(list)
        for a in group:
            nc = normalize_content(a.get("content", ""))
            key = " ".join(nc.split()[:3]) or nc[:20]
            buckets[key].append(a)
        for bk, bgroup in buckets.items():
            if len(bgroup) < 2:
                continue
            for i in range(len(bgroup)):
                for j in range(i + 1, len(bgroup)):
                    a, b = bgroup[i], bgroup[j]
                    src_a = (a.get("source", "") or "").split(":", 1)[0]
                    src_b = (b.get("source", "") or "").split(":", 1)[0]
                    if src_a == src_b:
                        continue
                    ac = normalize_content(a.get("content", ""))
                    bc = normalize_content(b.get("content", ""))
                    if similarity(ac, bc) >= threshold:
                        aid = a.get("id")
                        bid = b.get("id")
                        if aid and bid:
                            a_relates = a.setdefault("relates_to", [])
                            b_relates = b.setdefault("relates_to", [])
                            entry_a = f"{bid} (reinforces)"
                            entry_b = f"{aid} (reinforces)"
                            if entry_a not in a_relates:
                                a_relates.append(entry_a)
                                links_added += 1
                            if entry_b not in b_relates:
                                b_relates.append(entry_b)
                            if a.get("status") == "open":
                                a["status"] = "reinforced"
                            if b.get("status") == "open":
                                b["status"] = "reinforced"
    return links_added


# ---------- Assign IDs ----------

def assign_ids(atoms):
    # Sort by batch, then by original ordering within batch
    atoms_sorted = atoms  # preserve current order
    for idx, a in enumerate(atoms_sorted, start=1):
        a["id"] = f"atom-{idx:04d}"
    return atoms_sorted


# ---------- Cluster identification (simple) ----------

def build_clusters(atoms):
    clusters = defaultdict(list)
    for a in atoms:
        dim = a.get("dimension", "base")
        # primary dimension (first if multi)
        primary = dim.split("/")[0].strip() if dim else "base"
        # topic tag (first tag or 'misc')
        tags = a.get("tags", [])
        topic = tags[0] if tags else "misc"
        key = (primary, topic)
        clusters[key].append(a["id"])
    return clusters


# ---------- Tension detection ----------

def detect_tensions(atoms):
    tensions = []
    explicit = [a for a in atoms if a.get("type") == "tension"]
    for a in explicit:
        tensions.append(a)
    # Additionally, pair atoms that have "contradicts" in relates_to or
    # atoms marked status "contradicted"
    return tensions


# ---------- Generate ATOM-REGISTRY.md ----------

def atom_block(a):
    """Compact 2-4 line format per atom.

    Format:
    ### atom-XXXX (type / dim / phase / priority / status) — title
    - src: `path:L42` | tags: [a,b] | rel: atom-YYYY (reinforces)
    > quote (only if present)
    _note_ (only if present)
    """
    rel = a.get("relates_to") or []
    rel_str = " · ".join(rel[:8])
    if len(rel) > 8:
        rel_str += f" · (+{len(rel)-8} more)"
    rel_part = f"rel: {rel_str}" if rel else "rel: —"
    tags = ", ".join(a.get("tags") or [])
    tags_part = f"tags: [{tags}]" if tags else "tags: —"
    priority = a.get("priority") or "—"
    quote = (a.get("quote") or "").strip()
    note = (a.get("note") or "").strip()
    title = (a.get("content") or "").strip().split("\n")[0][:160]
    meta = f"{a.get('type','concept')} / {a.get('dimension','base')} / {a.get('phase','any')} / P:{priority} / {a.get('status','open')}"
    lines = [f"### {a['id']} — {title}",
             f"- *{meta}* · src: `{a.get('source','?')}` · {tags_part} · {rel_part}"]
    if quote and normalize_content(quote) != normalize_content(title):
        q = quote.replace("\n", " ")[:500]
        lines.append(f"> {q}")
    if note:
        lines.append(f"_note: {note[:300]}_")
    lines.append("")  # blank line separator
    return "\n".join(lines)


def write_registry(atoms):
    # Statistics
    total = len(atoms)
    per_type = Counter(a.get("type", "?") for a in atoms)
    per_status = Counter(a.get("status", "?") for a in atoms)
    per_phase = Counter(a.get("phase", "?") for a in atoms)

    # Dimensions: count primary dimension (first in multi)
    per_dim_primary = Counter()
    per_dim_any = Counter()
    for a in atoms:
        dim = a.get("dimension", "base") or "base"
        parts = [p.strip() for p in re.split(r"[/,\s]+", dim) if p.strip()]
        if parts:
            per_dim_primary[parts[0]] += 1
            for p in parts:
                per_dim_any[p] += 1

    # Source coverage
    per_source_file = Counter()
    for a in atoms:
        src = (a.get("source", "") or "").split(":", 1)[0]
        per_source_file[src] += 1

    def bullet_counter(c):
        return "\n".join([f"- {k}: {v}" for k, v in c.most_common()])

    # Group atoms by primary dimension for Section 1
    groups_primary = defaultdict(list)
    cross_dim = []
    for a in atoms:
        dim = a.get("dimension", "base") or "base"
        parts = [p.strip() for p in re.split(r"[/,]+", dim) if p.strip()]
        if len(parts) > 1:
            cross_dim.append(a)
        primary = parts[0] if parts else "base"
        groups_primary[primary].append(a)

    dim_order = ["base", "life", "company", "community", "money",
                 "relationships", "philosophy"]

    # Catch-all bucket for atoms with non-standard primary dimensions
    extra_dims = sorted(set(groups_primary.keys()) - set(dim_order))

    header = f"""---
id: atom-registry-2026-04-21
title: Atom Registry — Complete Inventory (Stage 1 Untangle)
date: 2026-04-21
type: registry
status: ready
binding: yes — primary source для Stage 3 synthesis (D1/D2/D3)
total_atoms: {total}
sources:
  - wiki/ ({sum(1 for s in per_source_file if s.startswith('wiki/'))} files covered)
  - voice-memos artefacts (6 files)
  - D6 / D9 / ADR / CLAUDE.md
  - TENSIONS-PRE-RESOLVED.md (binding overrides)
---

# Atom Registry — Complete Inventory (Stage 1 Untangle)

## 0. Statistics

- **Total atoms:** {total}

### Per type
{bullet_counter(per_type)}

### Per dimension (primary)
{bullet_counter(per_dim_primary)}

### Per dimension (any — includes multi-dim atoms counted in each)
{bullet_counter(per_dim_any)}

### Per phase
{bullet_counter(per_phase)}

### Per status
{bullet_counter(per_status)}

### Source coverage (top 30 files by atom count)
{chr(10).join([f"- {k}: {v}" for k,v in per_source_file.most_common(30)])}

_Full per-source index: §4._

---

## 1. Atoms grouped by dimension (primary dimension)
"""

    body_parts = [header]
    for dim in dim_order:
        group = sorted(groups_primary.get(dim, []),
                       key=lambda a: (a.get("type", ""), a["id"]))
        body_parts.append(f"\n### 1.{dim_order.index(dim)+1} {dim.title()} ({len(group)} atoms)\n")
        if not group:
            body_parts.append("_(no atoms)_\n")
            continue
        # Sub-group by type
        by_type = defaultdict(list)
        for a in group:
            by_type[a.get("type", "?")].append(a)
        type_order = ["principle", "value", "concept", "bet", "hypothesis",
                      "claim", "task", "metric", "entity", "tension"]
        for t in type_order:
            sub = by_type.get(t, [])
            if not sub:
                continue
            body_parts.append(f"\n#### {t.capitalize()} ({len(sub)})\n")
            for a in sub:
                body_parts.append(atom_block(a))

    # Section 1.X: extra dims (non-standard)
    for ed in extra_dims:
        group = sorted(groups_primary.get(ed, []),
                       key=lambda a: (a.get("type", ""), a["id"]))
        if not group:
            continue
        body_parts.append(f"\n### 1.X {ed.title()} ({len(group)} atoms)\n")
        for a in group:
            body_parts.append(atom_block(a))

    # Section 2: cross-dimension atoms
    body_parts.append(f"\n---\n\n## 2. Cross-dimension atoms ({len(cross_dim)})\n\n"
                      "_Atoms assigned to multiple dimensions. Primary dimension above is first in list._\n\n")
    for a in sorted(cross_dim, key=lambda a: a["id"]):
        body_parts.append(f"- **{a['id']}** ({a.get('type','?')}, dims: `{a.get('dimension','?')}`) — {(a.get('content','') or '')[:100]}")

    # Section 3: alphabetical index
    body_parts.append(f"\n\n---\n\n## 3. Atoms index (by ID)\n\n"
                      f"_{total} atoms._\n\n")
    for a in atoms:
        title = (a.get("content", "") or "").strip().split("\n")[0][:80]
        body_parts.append(f"- **{a['id']}** `{a.get('type','?')}` — {title}")

    # Section 4: provenance by source
    body_parts.append("\n\n---\n\n## 4. Provenance index (by source file)\n\n")
    for src, count in per_source_file.most_common():
        ids = [a["id"] for a in atoms if (a.get("source", "") or "").split(":", 1)[0] == src]
        body_parts.append(f"### `{src}` ({count} atoms)\n")
        body_parts.append(", ".join(ids))
        body_parts.append("\n")

    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(body_parts))


def write_knot_map(atoms):
    total = len(atoms)
    overridden = [a for a in atoms if a.get("status") == "overridden"]
    reinforced = [a for a in atoms if a.get("status") == "reinforced"]
    tensions = [a for a in atoms if a.get("type") == "tension"]
    orphans = [a for a in atoms if not (a.get("relates_to") or [])]

    per_dim = Counter()
    per_phase = Counter()
    for a in atoms:
        dim = (a.get("dimension", "base") or "base").split("/")[0]
        per_dim[dim] += 1
        per_phase[a.get("phase", "any")] += 1

    clusters = build_clusters(atoms)
    cluster_rows = []
    # Largest clusters by size
    for key, ids in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
        if len(ids) < 3:
            continue
        cluster_rows.append((key, ids))

    # Tensions grouped by dimension
    tensions_by_dim = defaultdict(list)
    for t in tensions:
        d = (t.get("dimension", "base") or "base").split("/")[0]
        tensions_by_dim[d].append(t)

    # Gaps detection
    dim_order = ["base", "life", "company", "community", "money",
                 "relationships", "philosophy"]
    dim_gaps = [d for d in dim_order if per_dim.get(d, 0) < 20]
    phase_gaps = [p for p in ["now", "phase-1", "phase-2", "phase-3",
                              "long-term"] if per_phase.get(p, 0) < 10]

    lines = [f"""---
id: knot-map-2026-04-21
title: Knot Map — Tensions, Clusters, Gaps (Stage 1 navigation)
date: 2026-04-21
type: knot-map
status: ready
companion_to: ATOM-REGISTRY.md
total_atoms: {total}
---

# Knot Map — Navigation по Atom Registry

Companion-документ к `ATOM-REGISTRY.md`. Используется как входной overview:
где узлы напряжения, где кластеры, где gaps, что sirотно.

## 0. Statistics overview

- Total atoms: **{total}**
- Tensions (explicit type): **{len(tensions)}**
- Tensions pre-resolved (LOCKED): **8** (см. TENSIONS-PRE-RESOLVED.md)
- Atoms overridden by locked decisions: **{len(overridden)}**
- Atoms reinforced (multi-source): **{len(reinforced)}**
- Orphans (no relates_to): **{len(orphans)}**
- Clusters (size ≥ 3): **{len(cluster_rows)}**
- Dimension gaps (< 20 atoms): {dim_gaps or 'none'}
- Phase gaps (< 10 atoms): {phase_gaps or 'none'}

### Per dimension
{chr(10).join([f"- {k}: {v}" for k,v in per_dim.most_common()])}

### Per phase
{chr(10).join([f"- {k}: {v}" for k,v in per_phase.most_common()])}

---

## 1. Tensions

### 1.1 Tensions resolved в TENSIONS-PRE-RESOLVED (reference — LOCKED)

1. **Gentlemen vs Piranhas** → Gentleman inside / Predator outside.
2. **Solo vs Team** → Solo-now-with-team-ready-scaffolding.
3. **Open-source vs Patents** → Closed outside / Open inside (team).
4. **Name (Jetix vs Jackson)** → Jetix, без изменений.
5. **Phase priority** → Consulting-first Phase 1, Secure Network = Phase 2+.
6. **Anton/Vladislav/Rodion** → Не ключевые, не упоминать.
7. **6 архетипов vs 5 каста** → Union (10 archetypes merged).
8. **Jetix multiplicity frames** → Layered identity (different faces per observer/phase).

Все 8 decisions — **binding overrides** для registry.
Atoms, попавшие под override, имеют `status: "overridden"` + note.

Count of atoms overridden: **{len(overridden)}**.

### 1.2 Remaining tensions (explicit type="tension" atoms — OPEN)

"""]

    for d in dim_order:
        group = tensions_by_dim.get(d, [])
        if not group:
            continue
        lines.append(f"#### Dimension: {d.capitalize()}\n")
        for t in group:
            relates = ", ".join(t.get("relates_to", []) or []) or "—"
            title = (t.get("content", "") or "").strip().split("\n")[0][:120]
            note = t.get("note", "") or ""
            lines.append(f"- **{t['id']}** — {title}")
            lines.append(f"  - Source: `{t.get('source','?')}`")
            lines.append(f"  - Relates: {relates}")
            if note:
                lines.append(f"  - Note: {note}")
            lines.append("")

    if not tensions:
        lines.append("_No explicit `type: tension` atoms были найдены subagents. Соответственно, либо все tensions были unfolded в pairs с `contradicts` в relates_to, либо оставшиеся tensions implicit — см. §2 clusters и §3 gaps для ручного анализа._\n")

    lines.append("\n### 1.3 Soft tensions / parked (из TENSIONS-PRE-RESOLVED §Remaining)\n")
    lines.append("""
Не locked, ждут Stage 2:
- **#4 Pain-based vs opportunity-based sales** — склонность к opportunity-based post-17 апреля.
- **#6 Geo first (Germany-patents vs English-infobiz)** — возможно phased.
- **#7 Fortune 500 coalition vs sovereignty** — parked bet (Phase 3+).
- **#8 NEW projects (ideas-platform / job-matching / investment-fund)** — продюсерский центр внутри, остальные parked?

Gaps из digest §7.2 (thin coverage):
- **Exit / liquidity / equity structure** — не обсуждалось.
- **Regulatory / compliance (GDPR / AI Act / DE)** — thin.
- **Recovery / nutrition / sleep (Jetix-life)** — thin.
""")

    lines.append("\n---\n\n## 2. Clusters (groups of related atoms ≥ 3)\n")
    for i, (key, ids) in enumerate(cluster_rows, start=1):
        dim, topic = key
        lines.append(f"### C-{i:02d} — {dim} / {topic} ({len(ids)} atoms)")
        # Show up to 20 IDs
        preview = ", ".join(ids[:25])
        more = f" _(+{len(ids)-25} more)_" if len(ids) > 25 else ""
        lines.append(f"- Dimension: **{dim}**")
        lines.append(f"- Topic tag: **{topic}**")
        lines.append(f"- Density: {len(ids)} atoms")
        lines.append(f"- Members: {preview}{more}")
        lines.append("")

    lines.append("\n---\n\n## 3. Gaps (weak coverage)\n")
    lines.append("### 3.1 Dimension gaps (< 20 atoms)\n")
    if dim_gaps:
        for d in dim_gaps:
            lines.append(f"- **{d}** — {per_dim.get(d, 0)} atoms. Under-developed.")
    else:
        lines.append("_All dimensions have ≥ 20 atoms. No major dimension gap._")

    lines.append("\n### 3.2 Phase gaps (< 10 atoms)\n")
    if phase_gaps:
        for p in phase_gaps:
            lines.append(f"- **{p}** — {per_phase.get(p, 0)} atoms.")
    else:
        lines.append("_All phases have ≥ 10 atoms._")

    lines.append("\n### 3.3 Topic gaps (manual review — см. TENSIONS §Remaining)\n")
    lines.append("""
- Exit / liquidity / equity structure
- GDPR / AI Act / DE compliance detail
- Recovery / nutrition / sleep (Jetix-life)
- Pricing mechanics beyond €150/час baseline
- Partnership legal structure""")

    lines.append("\n---\n\n## 4. Orphans (atoms без relates_to)\n")
    lines.append(f"Total orphans: **{len(orphans)}** из {total}.\n")
    lines.append("_Orphans — это либо unique insights without near-duplicates (возможно важные) либо noise (возможно park). Manual triage needed._\n")
    # Show top 100 orphans by priority
    orphan_sample = [a for a in orphans if a.get("type") in ("principle", "bet", "hypothesis", "concept", "tension")][:100]
    if orphan_sample:
        lines.append("### Sample (top 100 by high-salience types — principle/bet/hypothesis/concept/tension):\n")
        for a in orphan_sample:
            title = (a.get("content", "") or "").strip().split("\n")[0][:100]
            lines.append(f"- **{a['id']}** `{a.get('type','?')}` [{a.get('dimension','?')}] — {title}")

    lines.append("\n---\n\n## 5. Cross-dimension connections\n")
    cross = [a for a in atoms if "/" in (a.get("dimension", "") or "")]
    lines.append(f"Total cross-dimension atoms: **{len(cross)}**.\n")
    # Count top pairs
    pair_counter = Counter()
    for a in cross:
        parts = sorted([p.strip() for p in re.split(r"[/,]+", a.get("dimension", "")) if p.strip()])
        if len(parts) >= 2:
            pair_counter[tuple(parts[:2])] += 1
    lines.append("### Top dimension-pair connections\n")
    for pair, count in pair_counter.most_common(15):
        lines.append(f"- **{pair[0]} ↔ {pair[1]}**: {count} atoms")

    lines.append("\n---\n\n## 6. Recommendations for Stage 2\n")
    lines.append("""
### 6.1 Priority tensions to resolve (Ruslan ↔ Cloud Cowork)
Из §1.3 soft tensions:
1. **Pain-based vs opportunity-based sales** — быстро, нужно для Phase 1 ICP.
2. **Geo first (Germany vs English-infobiz)** — средне, влияет на revenue-path Phase 1.
3. **Продюсерский центр vs остальные NEW projects** — park vs pursue.
4. **Exit / liquidity / equity** — нужно если Phase 2+ partners на горизонте.

### 6.2 Gaps to fill vs park
- **Fill now:** Pricing mechanics (beyond €150/час), ICP detail (archetype-level).
- **Fill phase-1 end:** GDPR / AI Act compliance skeleton.
- **Park:** Fortune 500 coalition, exit structure (revisit Phase 2+).
- **Life-OS thin:** fill only if life-coach delegate уже работает. Otherwise park.

### 6.3 Orphans to triage
Смотри §4 sample. Приоритет ручного review:
- `principle` orphans — могут быть core принципы без pair'ов.
- `bet` orphans — strategic wagers без context.
- `tension` orphans — обычно уже unfolded в pairs, но некоторые могут быть unique.

### 6.4 Action flags
- **Before D1 synthesis:** решить 4 remaining tensions из §1.3.
- **Before D2 synthesis:** принципы dimension=philosophy проверить на coherence с 8 locked decisions.
- **Before D3 synthesis:** Phase 1 task atoms (priority=P1) отфильтровать и пересчитать.
- **Before D4 synthesis:** architecture-related atoms (dimension=base) cross-check с D6 + D9.

---

_End of Knot Map._
""")

    with open(KNOTMAP_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    print("=" * 60, file=sys.stderr)
    print("Stage 1 Aggregator starting.", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    atoms, files_loaded = load_all_atoms()
    print(f"Loaded {len(atoms)} raw atoms from {len(files_loaded)} files:",
          file=sys.stderr)
    for fn in files_loaded:
        print(f"  - {fn}", file=sys.stderr)

    if not atoms:
        print("ERROR: no atoms loaded. Aborting.", file=sys.stderr)
        sys.exit(1)

    overrides = apply_override_safety(atoms)
    print(f"Auto-overrides applied: {overrides}", file=sys.stderr)

    deduped, merged = dedup_atoms(atoms)
    print(f"Deduped: {len(atoms)} → {len(deduped)} (merged {merged})",
          file=sys.stderr)

    assign_ids(deduped)

    links = cross_reference_reinforcements(deduped)
    print(f"Cross-reference reinforcement links added: {links}",
          file=sys.stderr)

    write_registry(deduped)
    write_knot_map(deduped)

    print(f"ATOM-REGISTRY → {REGISTRY_PATH}", file=sys.stderr)
    print(f"KNOT-MAP     → {KNOTMAP_PATH}", file=sys.stderr)

    # emit summary
    summary = {
        "total_atoms": len(deduped),
        "raw_atoms_before_dedup": len(atoms),
        "merged_in_dedup": merged,
        "auto_overrides": overrides,
        "cross_ref_links_added": links,
        "registry_path": REGISTRY_PATH,
        "knotmap_path": KNOTMAP_PATH,
        "files_loaded": files_loaded,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
