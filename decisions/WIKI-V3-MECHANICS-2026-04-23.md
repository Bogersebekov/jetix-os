---
title: Wiki v3 Mechanics — Resolved Answers to 9 Open Questions
date: 2026-04-23
status: approved
approved_by: Ruslan
approved_date: 2026-04-23
r_items: all 8 accepted with defaults (R1–R8 = Yes)
author: Claude Code (Opus 4.7, 1M context)
step: 2.2.3 Стадия B — mechanics resolver
inputs:
  - design/ROY-WIKI-V3-GOALS-2026-04-23.md (W-1..W-12)
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md (§5.5 + §5.7 + §5.10)
  - design/ROY-BUILD-LOGIC-2026-04-23.md (§1–§4)
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Part 4, Part 10)
  - raw/research/knowledge-architecture-deep-research-2026-04-19.md (Parts A–F, H)
  - wiki/ current v2 infrastructure (audit)
sub_agent_extractions:
  - raw/research/step-2-2-3b-extractions/W-1-knowledge-architecture.md
  - raw/research/step-2-2-3b-extractions/W-2-locked-constraints.md
  - raw/research/step-2-2-3b-extractions/W-3-existing-wiki-audit.md
downstream: design/AWAITING-APPROVAL-wiki-v3-architecture-YYYY-MM-DD.md (Стадия C — separate session)
---

# Wiki v3 Mechanics Resolver — AWAITING-APPROVAL

**Scope:** resolve 9 open design questions (Q1..Q9) that sit on top of the
12 locked W-decisions. Every recommendation is grounded in at least one
Tier-1 source. Twelve W-decisions are not re-opened; they are honored.

## Part 1 — Summary table (read this first)

| Q  | Question                          | Recommended answer (1-liner) |
|----|-----------------------------------|------------------------------|
| Q1 | Retrieval primary                 | **4-tier stack**: path lookup → index+niche+grep → typed-BFS on edges.jsonl (2 hops) → long-context fallback. HippoRAG PPR deferred until >2K edges. No embeddings Phase A. |
| Q2 | Write serialization               | **Single-writer brigadier** all 9 layers Phase A. Experts return via Task; brigadier commits with §5.5.5 provenance gate. Phase B revisit on contention. |
| Q3 | Cross-reference format            | **Triple-channel**: YAML frontmatter (`sources[]`/`related[]`) + inline `[[type/slug]]` + typed-edge `edges.jsonl`. **12-type edge enum** (9 intra + `part_of` + 3 cross-layer). Inline `[src:path#section]` per §5.5.3. |
| Q4 | Task-scoped context population    | **Hybrid auto-pull + brigadier override**: niche-symlinks → filtered decisions/ → 24-Locks → typed-BFS seeded from task keywords (top-k=10, 2 hops) → book excerpts. 20K token cap. |
| Q5 | Rot / staleness                   | **5-signal /lint**: structural + α-2/α-3 state (superseded/retired/tombstoned) + confidence×age (>60d) + contradiction-edge integrity + time-based (foundations-only Phase A; global at 10K pages). |
| Q6 | Skill learning pipeline           | **α-3 pipeline in Layer 8**: `candidates/`→`learning/`(golden-set ≥3)→`active/`(symlinked to `.claude/skills/`)→`usage/`. Validated ≥3:1/≥10 uses; tombstoned <1:1. Owners: propose anyone; draft+eval+activate brigadier; audit meta-agent; retire meta-agent or Ruslan. |
| Q7 | Git branches                      | **`roy/<project-slug>/{main,iter-vN,fork-<variant>,exp-<hypo>}`**. `roy/` prefix avoids collisions. Max depth 2. |
| Q8 | Layer 9 activation                | **3-AND + Ruslan**: ≥50 closed α-4 cycles AND ≥2 theme-wikis with ≥50 concepts + ≥3 inter-theme refs AND explicit Ruslan approval. Phase A: placeholder `swarm/wiki/insights/` + README. |
| Q9 | `wiki/` v2 vs `swarm/wiki/` v3    | **Coexist + parameterize**: v2 untouched; v3 new; add `$WIKI_ROOT` to 6 skills (~85 edits). Copy templates into v3. Bridge `cross-tree-ref` edge. Migration decision Phase B. |

Sources cited across Part 2: knowledge-architecture §A.1, §A.3, §A.6, §B.1, §B.2, §B.3, §B.4, §B.5, §C.1, §C.3, §C.4, §D.1, §D.3, §E.1, §E.2, §E.3, §F.1, §F.2, §F.4, §G.3, §G.5, §H.1, §H.3, §H.4, §H.5, §H.7, §H.8, Anti-patterns 3/6/7/8/10; master-synthesis §5.5.1–§5.5.5, §5.6.2, §5.7, §5.10; ROY-WIKI-V3-GOALS §2–§5 (W-1..W-12); ROY-BUILD-LOGIC §1.2–§1.3, §2.1–§2.3, §3, §4.2–§4.4; FPF-ENHANCEMENT Part 4 (α-1..α-5, §4.3), Part 10 (§10.4–§10.8); existing `wiki/_templates/*`, `wiki/graph/edges.jsonl`, `.claude/skills/*`. ≥40 distinct citations.

---

## Part 2 — Per-question resolution

### Q1 — Retrieval mechanism primary

**Recommended answer.** Phase A runs a **four-tier filesystem + typed-graph
retrieval stack**, not a single algorithm:

1. **Direct path lookup** (`alpha_direct_lookup`). If the query carries an alpha
   ID or explicit file reference (`deal-042`, `alphas/clients/acme`,
   `wiki/concepts/curated-community-access`), read the file directly — zero
   search cost. Highest priority tier.
2. **Index + niche/topic filter + grep.** Read `swarm/wiki/index.md` (master
   TOC). Filter by `niche:` and/or `topics:` frontmatter matching the task.
   `grep -l` keywords across the filtered subtree. Select 5–15 candidate pages.
   This is the baseline that mirrors what `/ask` already does in v2 (W-3 §E).
3. **Typed-edge BFS on `swarm/wiki/graph/edges.jsonl`.** Seed = grep hits. BFS
   max 2 hops, following only allowed edge types for the task (e.g. include
   `supports`, `extends`, `derived_from`; exclude `contradicts` unless doing
   contradiction scan). Top-k=10. Functions as a low-cost, deterministic
   substitute for Personalized PageRank — no eigenvector math, just typed
   traversal. Existing v2 already carries 572 edges (W-3 §C), so this tier is
   free infrastructure.
4. **Long-context fallback.** Only when tiers 1–3 return empty or very thin;
   load full filtered subtree within Opus 4.7 1M window. Fallback, not
   primary (per §B.4: "retrieval + agent isolation is правильная стратегия;
   long-context как fallback для edge cases, не primary path").

HippoRAG PPR and HyDE are **deferred** to a later phase. Rationale: (i) the
existing `/ask` implementation is already filesystem + grep + wikilink
traversal (W-3 §E) — PPR is NOT already wired, contrary to research §A.3
framing. Adding PPR is real engineering work. (ii) Scale threshold from §G.3
("557 стр. Keyword + HippoRAG PPR"; "5K стр. BM25 + HippoRAG PPR") suggests
PPR pays off more clearly past ~2–5K pages; with 546 entries today, typed-BFS
on 572 edges gives comparable multi-hop benefit without the new component.
(iii) Max-subscription discipline (§5.7.3: no `ANTHROPIC_API_KEY`) — PPR
itself doesn't need paid embeddings (that was its whole point per §A.3), so
the cost objection is weaker, but implementation cost remains.

**Evidence.**
- `raw/research/knowledge-architecture-deep-research-2026-04-19.md` §A.1
  (Karpathy "knowledge compiled once, не переизвлекаются — `~100 sources,
  сотни страниц без embedding-инфраструктуры`"); §A.6 + §E.3 routing tiers;
  §B.1 retrieval table with Graph (HippoRAG) marked "Текущий выбор ✓"; §B.4
  long-context as fallback; §G.3 scale evolution; Anti-pattern 6 (no vector
  DB < 3K pages).
- `raw/research/.../W-3-existing-wiki-audit.md` §E: `/ask` reality check —
  index + grep + niche + graph summaries + wikilink traversal max depth 2.
- `decisions/MASTER-SYNTHESIS...` §5.10.2: wiki skills `/ingest /ask /lint
  /consolidate /build-graph` already in place.
- `design/ROY-WIKI-V3-GOALS...` §5: Q1 explicitly listed as open.

**Alternatives considered.**
- **Primary HippoRAG PPR** (§A.3, §H.5 research preferred). Rejected Phase A:
  not yet implemented; typed-BFS gives ~80% of benefit at ~20% of cost.
- **Semantic embeddings (dense)**. Rejected: §B.1/§G.3/Anti-pattern 6 — no
  payoff < 3K pages + paid-embedding cost.
- **GraphRAG community traversal**. Rejected: §B.1 "при 10K+ стр"; existing
  community summaries already used in tier 2.
- **HyDE pre-query**. Rejected default; keep as Phase B enhancement (§B.5).
- **Long-context as primary**. Rejected: Anti-pattern 10, §B.4 fallback-only.

**Tradeoffs accepted.** Multi-hop reasoning weaker than PPR (no centrality
weighting) — acceptable <2K edges. No semantic fuzzy-match — mitigate via
brigadier synonym expansion + `wiki/graph/summaries.md` community summaries.

**Applicability constraint.** Valid until total `edges.jsonl` size exceeds
~2,000 edges OR until `/ask` FPAR (first-pass acceptance rate, §F.4) drops
below 80% over a rolling 20-query window. At that point, revisit: add PPR +
HyDE pre-query as the new primary; relegate typed-BFS to fallback.

**New variants found (W-1 §H.5, §E.2):**
- **`alpha_direct_lookup` as dedicated Tier 1** — not on original candidate
  list; promoted above because free (one file read) for ID queries.
- **`alpha_aware: true` filter** — when task has `alpha_type`, Tiers 2–3
  filter entries without matching frontmatter. Enable by default.
- **"≤1 hop до источника" invariant** (§E.2) — canonical data reachable in
  ≤1 hop. Adopt as Phase A rule; `/lint` flags pages violating.

---

### Q2 — Write serialization model

**Recommended answer.** **Single-writer brigadier** across all 9 layers for
Phase A. This is already locked in master-synthesis §5.5.2 and BUILD §2.2;
this resolution confirms the extension to Layers 4 (agent-improvements) and 9
(insights) that were previously ambiguous.

Protocol:
1. **Experts (matrix cells) produce drafts only.** They write to
   `swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md` (per §5.7 tool
   matrix). Drafts are working state, not published knowledge.
2. **Experts return artefacts via Task tool** (not via direct wiki writes).
   Artefacts carry full frontmatter including α-2 state (`drafted`).
3. **Brigadier reviews** using expert-assisted critic (Stage-Gated default
   per ROY-ALIGNMENT). Revisions loop via draft until acceptance.
4. **Brigadier commits** to the authoritative layer (themes/, brigadier/,
   meta/, tasks/, operations/, global/, skills/). Commit requires §5.5.5
   provenance gate (≥1 source + commit hash OR verbatim source + line range).
5. **Layer 4 (meta/agent-improvements).** Brigadier runs periodic sweep
   consuming Level-1 CE outputs from `agents/<expert>/strategies.md`, emits
   improvement memos to `swarm/wiki/meta/agent-improvements/<agent>-*.md`.
   Brigadier-owned write.
6. **Layer 9 (insights).** Phase A: brigadier-owned (placeholder only — no
   crazy-agent instantiated, see Q8). Phase B: crazy-agent writes to
   `swarm/wiki/insights/candidates/` only; brigadier promotes to
   `insights/promoted/` after review.
7. **PostToolUse validator.** Every wiki write triggers `/lint` (§5.6.2);
   malformed frontmatter or missing provenance blocks the write.

**Evidence.** master-synthesis §5.5.2 (single-writer); §5.5.5 (provenance
gate); §5.6.2 (PostToolUse `/lint`); §5.7 (tool matrix — experts write only
to `wiki/drafts/`); BUILD §2.2 (stigmergic shared state single-writer Phase
A); FPF Part 4 §α-2 (Artefact acceptance by brigadier; acceptance requires
frontmatter validity + Conformance Checklist); ROY-ALIGNMENT §10 (CRDT
deferred to Phase B).

**Alternatives considered.**
- **Per-layer owners**. Rejected Phase A: concurrent-write complexity pre-CRDT;
  AP-15 + AP-18 risk. Keep as Phase B candidate.
- **Hybrid (brigadier shared, experts own)**. Rejected: two write protocols,
  doubled mental model; revisit Phase B.

**Tradeoffs accepted.** Brigadier = write bottleneck (goals §5 open).
Measure at Phase A close. Experts can't post-fact self-correct without
round-trip — drafts stay expert-editable until acceptance mitigates this.

**Applicability constraint.** Phase A. Revisit at Phase A close or when
brigadier commit queue exceeds ~5 pending artefacts per cycle (contention
signal per §5.5.2).

**Open sub-question (new, surfaces from W-2 §F flag #3).** Strategies /
meta-improvement content lives in three proposed locations:
(a) `agents/<expert>/strategies.md` (master §5.5.5 per-agent memory),
(b) `swarm/strategies/<expert>.md` (BUILD §1.2),
(c) `swarm/wiki/meta/agent-improvements/<agent>-*.md` (W-4).
**Mechanics resolution recommends**: (a) stays as per-agent strategies
accumulator (the CE Level-1 sink — per-agent local learning); (b) merged
into (a) — eliminate `swarm/strategies/` as redundant; (c) is the Level-2
meta-layer — brigadier synthesizes across (a) into cross-cutting improvements.
Hand this to Стадия C for explicit layout resolution.

---

### Q3 — Cross-reference format between layers

**Recommended answer.** **Triple-channel, combined** (inherits + formalizes
v2 pattern):

1. **YAML frontmatter — navigation + provenance.** Required fields per
   §5.5.3: `sources: [{path, range?, quote?}]`, `related: [path, ...]`,
   `captured_by`, `captured_date`, `task_id?`, `commit_sha?`. Both v2 and v3
   honor the same schema.
2. **Inline body wikilinks + section-header-as-edge-type.** The v2
   convention — body uses `[[type/slug]]` under section headers like
   `## Расширяет` / `## Поддерживает` / `## Противоречит` — is the
   authoring UX. `/build-graph` parses these headers to derive typed edges.
   **Keep unchanged.**
3. **Typed-edge index: `swarm/wiki/graph/edges.jsonl`.** Append-only. Shape:
   `{"from": "<layer>/<type>/<slug>", "to": "<layer>/<type>/<slug>",
   "type": "<edge-type>", "ts": "YYYY-MM-DD", "confidence": "<low|med|high>"}`.
   Extends v2 shape with an optional `<layer>/` prefix for cross-layer refs.
4. **Inline `[src:path#section]` citations** (§5.5.3) — atomic claim-to-source
   citations inside body prose, distinct from navigation wikilinks. Keep.

**Edge-type vocabulary (formalized).** The "9 typed edges" alluded to in
Part 10.8 item 5 are enumerated. All are documented in overview.md v2 but
only partially present in data:

*Intra-layer (9 types — v2 documented, reused for v3):*
1. `extends` — page refines/expands another.
2. `contradicts` — explicit conflict with another page.
3. `supports` — page provides evidence for another's claim.
4. `inspired_by` — creative lineage (idea → idea).
5. `tested_by` — claim → experiment.
6. `invalidates` — experiment/evidence invalidating a claim.
7. `supersedes` — new page replaces old (used with `status: superseded`).
8. `addresses_gap` — page fills a lint-flagged gap.
9. `derived_from` — source → concept / claim / idea.

*Add: `part_of` — ad-hoc in v2 data (233 edges, 40%) for hub→children,
formalize as 10th intra-layer type.*

*Cross-layer (3 new types for v3):*
11. `alpha-ref` — wiki entity ↔ alpha (W-1 §D.3).
12. `layer-ref` — generic cross-layer link without specific semantics.
13. `cross-tree-ref` — v3 `swarm/wiki/` page citing v2 `wiki/` page (Q9
    bridge).

Total: **12 edge types** with explicit inverse semantics documented in
`swarm/wiki/_templates/edge-types.md` (Стадия C deliverable).

**Evidence.** knowledge-architecture §B.2 (citations `[[file-ref]]`
synthesizer); §D.1 (Variant A YAML `wiki_edges:` example); §D.3 (alpha↔wiki
edges JSONL with `alpha-ref` type); §E.2 Diátaxis mapping; master-synthesis
§5.5.3 (provenance YAML + `[src:path#section]` inline); Part 10.8 item 5
(A.14 typed edges); W-3 §F (four parallel channels observed in data);
`wiki/overview.md` (9 edge types declared); W-3 §C (actual edge type counts).

**Alternatives considered.**
- **Pure wikilinks** (drop typed graph). Rejected: W-12 depth; breaks
  `/build-graph` + community detection.
- **Pure frontmatter edges** (drop inline). Rejected: section-header-as-type
  is v2's authoring UX; breaks 546 existing entries.
- **Pure edges.jsonl** (drop YAML + inline). Rejected: humans can't read
  cross-refs inside a page.

**Tradeoffs accepted.** Three redundant representations — sync cost mitigated
by `/build-graph` treating edges.jsonl as derivative (rebuilt from body +
frontmatter). Cross-layer edges could inflate noise — `/lint` per-type count
threshold catches drift.

**Applicability constraint.** Phase A through Phase B. Consider
consolidating to authoritative frontmatter + derived-everything-else when
graph > 5K edges (syncing three channels becomes costly).

**New variants found:** **Diátaxis-for-data mapping** (§E.2): Tutorial/
Procedural → `roles/`; Reference/Facts → `concepts/`, alpha YAMLs;
Explanation → `topics/`, `ideas/`; Episodic/Log → `history.jsonl`,
`experiments/`. Adopt as meta-framework for Стадия C per-layer templates.

---

### Q4 — Task-scoped Wiki context population

**Recommended answer.** **Hybrid auto-pull with explicit brigadier override.**
Phase A pipeline that brigadier runs at task open:

1. **Declare task metadata.** At task open, brigadier writes `task.niche`,
   `task.alpha_type` (if any), and 5–10 task keywords to
   `swarm/wiki/tasks/<task-id>/open-questions.md`.
2. **Auto-pull Tier A (static, cheap):**
   - Niche symlinks: `swarm/wiki/themes/<niche>/` full tree (or v2
     `wiki/niches/<niche>/` if migration still pending — see Q9).
   - 24 Locks relevant subset (filter `lock_scope: <niche>` or universal).
   - `decisions/` filtered by `niche: <task.niche>` AND `date` within 90
     days (explicit BUILD §4.2 list).
3. **Auto-pull Tier B (dynamic):** Typed-edge BFS seeded from task.keywords
   on `swarm/wiki/graph/edges.jsonl`. Use the same Tier-3 mechanism as Q1.
   Top-k=10 pages, max 2 hops.
4. **Auto-pull Tier C (book excerpts):** If `task.keywords` match any
   `wiki/sources/` entry with `source_kind: book` or `raw_file` pointing to
   `raw/books-md/`, include the distilled summary page (NOT the raw book).
5. **Brigadier override:** pin additional pages via
   `swarm/wiki/tasks/<task-id>/context/pinned.md`; mark auto-pulled pages
   `excluded: true` in `context/manifest.yaml` to skip.
6. **Budget cap:** context/ write-out must fit 20K tokens (§H.3 Layer 4
   budget). If over-budget, brigadier summarizes lower-priority pages into a
   single "context-digest.md".

**Evidence.** knowledge-architecture §H.3 (agent context loading pseudo-code
with 50K-token budget; LAYER 4 wiki retrieval via HippoRAG seeded from
`task.description`; `alpha_filter=task.alpha_type`); §H.3 LAYER 3 (alpha
context auto-loaded if `task.alpha_ref`); §H.3 LAYER 5 (decisions auto-pull
by domain+time); §B.2 HippoRAG seeded from task description; §B.3 agentic
RAG iteration as Phase-B extension; BUILD §4.2 (4 source types explicitly:
Private Library books, `decisions/`, 24 Locks subset, previous global
learnings); BUILD §4.4 (EXPLICITLY defers manual-vs-auto to this step).

**Alternatives considered.**
- **Pure manual brigadier pick**. Rejected: W-12 + 546-entry scan unscalable.
- **Pure auto by tags**. Rejected: niche too broad; misses concept overlap.
- **Pure HippoRAG PPR** (§H.3 research preferred). Rejected Phase A — same
  reason as Q1: not yet wired; typed-BFS functionally similar at our scale.
- **Agentic RAG loop** (§B.3). Rejected Phase A: +3 LLM calls per task open.

**Tradeoffs accepted.** Auto-pull may pull 1–2 irrelevant pages (Anti-
pattern 8) — `alpha_filter` + brigadier `excluded: true` mitigate. Context
digest loses fidelity — preserve paths so ≤1-hop recovery stays available.

**Applicability constraint.** Phase A. Revisit when (a) PPR lands in Phase B,
or (b) >70% of tasks trigger brigadier override (signal the auto-pull is
miscalibrated).

**New variants found:** Context priority-based compaction (§H.3) — adopt
`context/manifest.yaml` with `priority: 1..N`; drop from highest N under
memory pressure. `alpha_aware` filter applies to typed-BFS seeds too.

---

### Q5 — Rot / staleness detection signals

**Recommended answer.** **Five-signal orchestration by `/lint`**, integrating
the α-2 (Artefact) and α-3 (Strategies-Rule) state machines from FPF Part 4:

1. **Structural signals (weekly, cheap):**
   - Orphan pages (no inbound wikilinks AND no edges.jsonl entry).
   - Broken wikilinks (target doesn't exist).
   - Missing required frontmatter fields.
   - Index drift (file not in index.md or vice versa).
2. **Version-state signals (author-driven, explicit):**
   - α-2 lifecycle: `status: superseded` (new artefact supersedes this) or
     `status: retired` (obsolete). Both flagged automatically; `supersedes`
     edge required for superseded.
   - α-3 lifecycle: `status: tombstoned` (applied automatically when usage
     counter shows ✓/✗ < 1:1 over ≥10 uses, per FPF §α-3) or `status:
     retired` (Ruslan-retire).
3. **Confidence × age signal (author-driven, measured):**
   - `confidence: low` AND `updated` older than 60 days → /lint flag for
     review. (Inherits v2 /lint rule, W-3 §G.)
   - Extend to foundations: `status: foundation` + `updated` > 365 days →
     flag for `last_reviewed` update.
4. **Contradiction signals (semi-automated):**
   - Every `contradicts` edge — /lint checks both sides exist and mention
     each other (v2 rule already). Escalate to brigadier review.
   - **Semantic contradiction detection (deferred Phase B)**: requires
     either embeddings (cost) or brigadier-run LLM scan (per §C.4 reflection
     pattern). Phase A: manual — contributors declare `contradicts` edges at
     authoring time.
5. **Time-based signals (narrow Phase A):**
   - Apply only to `foundations/` (long-life content) via `last_reviewed`
     field.
   - Global time-trigger (>2 years without update → `_archive/`) deferred
     until wiki > 10K pages (§H.8).

**Owner.** `/lint` is the orchestrator. Scheduled execution:
- PostToolUse hook on every wiki write (structural subset — cheap).
- Daily cron (full structural scan — Phase A) / weekly now, daily at 1K
  entries (§H.8).
- Usage counter for α-3 tombstoning lives in
  `swarm/wiki/skills/usage/<skill>.md` (Q6).
- Meta-agent runs α-3 audit weekly — tombstones skills failing ratio gate.
- Brigadier reviews contradictions (semantic Phase B).
- Ruslan explicit retire command (`status: retired`) terminal override.

**Evidence.** knowledge-architecture §F.4 (orphan, stale claims, confidence,
`authority_source`); §H.4 writeback rules (superseded → `status: refuted`);
§H.7 `/lint` orchestration; §H.8 scale triggers (weekly→daily→archival at
10K); §G.5 archival pattern; §C.4 reflection pattern (LLM-based contradiction
inside /lint); Anti-patterns 3 (over-eager writeback) + 10 (context rot);
FPF Part 4 α-2 (superseded/retired) + α-3 (tombstoning via ✓/✗ ratio + DRR);
W-3 §G (v2 /lint 7-check list; only claims check staleness today — gap).

**Alternatives considered.**
- **Only time-based.** Rejected: §H.8 time-based only at 10K+; spurious
  flags at 546 entries.
- **Only contradiction.** Rejected: needs embeddings or Phase-B LLM scan.
- **Only manual tag.** Rejected: AP-3 shows author-tagging alone fails.

**Tradeoffs accepted.** Semantic contradictions slip Phase A (author-
declared only) — brigadier periodic scan mitigates. α-3 needs ≥10 uses
before ratio meaningful — accepted; early skills under brigadier monitoring.

**Applicability constraint.** Phase A. Revisit signal #4 (contradiction
semantic) when Phase B brings brigadier-run LLM audits. Revisit signal #5
(time-based) at 10K entries.

**New variants found:** **FPAR (First-Pass Acceptance Rate)** as indirect
staleness signal (§F.4). Adopt as Phase-A metric on `/ask`: % accepted
without follow-up, target >80%, emit weekly to `swarm/wiki/meta/health.md`.

---

### Q6 — Skill learning pipeline (candidate → active)

**Recommended answer.** **Formal α-3 pipeline inside Layer 8** (W-9) at
`swarm/wiki/skills/`. Four sub-directories, explicit state transitions,
explicit ownership:

```
swarm/wiki/skills/
├── candidates/   # proposed skill — DRR format required
├── learning/     # draft + golden-set + eval results
├── active/       # promoted — symlinked into .claude/skills/
└── usage/        # usage counter + ✓/✗ log per skill
```

**State transitions (α-3 mapping):**

| Stage      | α-3 state   | Enter condition                         | Owner               |
|------------|-------------|-----------------------------------------|---------------------|
| candidate  | `proposed`  | DRR (context/decision/alternatives/checkpoint) written | anyone (expert or brigadier) |
| learning   | `drafting`  | Draft skill spec + golden-set (≥3 input-output pairs) | brigadier or matrix-expert |
| active     | `active`    | Golden-set eval ≥ 80% pass + brigadier approval (§5.5.5 provenance gate) | brigadier commits |
| usage-tracked | `active`→`validated` | ≥10 uses AND ✓/✗ ≥ 3:1 | auto (counter) |
| tombstoned | `tombstoned`| ≥10 uses AND ✓/✗ < 1:1 OR Ruslan-retire | meta-agent or Ruslan |

**`.claude/skills/` integration (resolves W-2 §F flag #4).** Phase A:
`active/<slug>.md` is the authoritative spec; `.claude/skills/<slug>.md`
is a symlink back to it. Claude Code's skill-loader reads
`.claude/skills/`; the symlink keeps the runtime registry and the
knowledge layer pointing to the same file. On tombstone, symlink removed
(file retained in `swarm/wiki/skills/active/` with `status: tombstoned`).

**DRR (Decision-Rule Record) format** (per FPF Part 4 α-3):
```yaml
---
title: /<skill-name>
status: proposed | drafting | active | validated | tombstoned
context: "когда этот skill применяется — условия"
decision: "что skill делает"
alternatives: ["rejected-1 — reason", "rejected-2 — reason"]
review_checkpoint: "условие повторного review — usage count / date / event"
proposed_by: "<agent>"
proposed_date: YYYY-MM-DD
golden_set: [ "input→output pair 1", ... ]  # filled at learning stage
usage_counter: 0
positive_outcomes: 0
negative_outcomes: 0
---
```

**Owners per transition:**
- **Propose** (`proposed`): any agent, or brigadier, or Ruslan. Writes to
  `candidates/<slug>.md`.
- **Draft + golden-set** (`drafting`): brigadier, or matrix-expert in
  domain-expert mode (e.g. sales-expert drafts a sales-specific skill).
- **Eval**: brigadier runs skill on golden-set; captures pass/fail in
  `learning/<slug>-eval.md`.
- **Activate**: brigadier commits via §5.5.5 provenance gate (≥1 source
  citation). Creates symlink `.claude/skills/<slug>.md →
  swarm/wiki/skills/active/<slug>.md`.
- **Usage monitor**: auto — every skill invocation increments counter;
  agent reports outcome (✓/✗) in next message.
- **Audit (weekly)**: meta-agent reads `usage/<slug>.md`; promotes to
  `validated` or tombstones per α-3 rule.
- **Retire**: Ruslan `status: retired` or meta-agent tombstone.

**Evidence.** FPF Part 4 §α-3 (state transitions, DRR format, ✓/✗ ≥3:1
threshold, meta-agent tombstoning, brigadier writes); ROY-WIKI-V3-GOALS W-9
(Layer 8 with 4 subdirs: active/candidates/learning/usage); W-5 (two-level
CE; skill learning at both levels); master-synthesis §5.5.5 (compound
provenance gate); §5.10 (skill roadmap: orchestration/wiki/mode skills);
knowledge-architecture §C.1 (procedural memory → skills pipeline); §H.1
(`langfuse/prompts/{agent}/{skill}.yaml` — Phase B registry candidate);
W-3 §H (v2 is fully ad-hoc — pipeline is a real net-new).

**Alternatives considered.**
- **Ad-hoc (current v2).** Rejected: W-9 + W-12 + AP-3; two formats already
  drifting (W-3 §H).
- **Langfuse registry as primary** (§H.1). Rejected Phase A — Phase B when
  >20 skills.
- **Per-agent skill folder.** Rejected: W-9 requires first-class layer;
  `.claude/skills/` flat convention.

**Tradeoffs accepted.** Symlink couples runtime to `active/` — mitigate via
`$SKILLS_ROOT` parameterization. Golden-set ≥3 is thin; raise to ≥10 Phase B.

**Applicability constraint.** Phase A. Revisit when active skill count >
20 (langfuse registry decision) or when the ≥10-uses threshold blocks too
many skills from validation (probably Phase A-close).

**New variants found:** **System Prompt Learning pump** (§H.4) — Level-1
CE sink at `agents/<expert>/strategies.md`; brigadier Level-2 sweep
promotes patterns found in ≥2 strategies.md files to
`swarm/wiki/skills/candidates/`. Per-skill FPAR in `usage/<slug>.md`.

---

### Q7 — Git branches naming convention

**Recommended answer.** **`roy/<project-slug>/<tag>` schema.**

Concrete branches:
- `main` — Jetix OS mainline (existing, untouched).
- `claude/jolly-margulis-915d34` — current Claude Code scratch branch
  (existing, untouched).
- `roy/<project-slug>/main` — stable mainline for a long-horizon roy-swarm
  project. E.g. `roy/growth-q3-2026/main`.
- `roy/<project-slug>/iter-vN` — per-iteration branch. N monotonically
  increasing integer. E.g. `roy/growth-q3-2026/iter-v3`. On accept, merge
  into `roy/<project-slug>/main`.
- `roy/<project-slug>/fork-<variant-slug>` — exploratory fork from a
  specific iter. E.g. `roy/growth-q3-2026/fork-b2b-focus`. On accept, merge
  into a fresh `iter-vN+1`.
- `roy/<project-slug>/exp-<hypothesis-slug>` — optional, for
  hypothesis-testing branches (W-6 §2 Layer 6 hypothesis).

**Rules:**
- `<project-slug>` is kebab-case, ≤30 chars, matches
  `swarm/wiki/operations/<project-slug>/` directory name 1:1.
- Only brigadier creates `roy/` branches. Experts work inside the current
  branch (single-session discipline, BUILD §3).
- Rollback per BUILD §2 Layer 6: `git checkout roy/<project>/iter-v<N-1>`.
- No deep nesting beyond depth 2.
- CI (if/when added): skip `roy/*` by default; promote to main via PR.

**Evidence.** ROY-WIKI-V3-GOALS W-6 (git branches = version mechanism);
W-6 goals-doc §2 Layer 6 (hypothesized scheme); BUILD §3 (single tmux
session = one git audit trail); W-2 §E (Q7 flagged open for final approval);
W-3 audit (existing branches to avoid collision).

**Alternatives considered.**
- **`roy/task-<id>/vN`** (per-task). Rejected: branch explosion (100+ tasks).
- **Flat `iteration/<project>/<N>`**. Rejected: loses project grouping.
- **No prefix.** Rejected: collides with `claude/...`.

**Tradeoffs accepted.** Long branch names (tab-completable). No git-enforced
hierarchy — `/lint` optional check that every `iter-vN` has `main`.

**Applicability constraint.** Active for all long-horizon swarm work (W-6).
Phase A + B. Revisit naming only if multi-branch git operations become
common bottleneck.

**New variants found:** none — this is primarily a naming decision.

---

### Q8 — Layer 9 (Insights / crazy-agent) Phase B activation trigger

**Recommended answer.** **Cumulative-AND, human-gated trigger** — Phase B
only. Phase A: structural placeholder.

**Phase A deliverable.** Create empty directory:
```
swarm/wiki/insights/
├── README.md      # activation criteria + phase-B plan
├── candidates/    # crazy-agent's output (empty until Phase B)
└── promoted/      # brigadier-reviewed + accepted (empty until Phase B)
```
No agent instantiated. No automated writes.

**Phase B activation trigger (all 3 must hold):**
1. **Swarm maturity:** ≥50 closed α-4 Cycle instances (i.e. 50 complete
   task cycles, to ensure the swarm has enough substrate to mine).
2. **Theme-wiki density:** ≥2 theme-wikis (Layer 1) with ≥50 concepts each
   AND ≥3 inter-theme cross-references (evidence that cross-domain insight
   candidates could exist).
3. **Ruslan explicit approval.** Manual unlock. Consistent with FPF §4.3
   ("AI cannot invent-mode strategize"); crazy-agent outputs are
   candidate-generation, not decisions — human must approve the activation
   of the candidate-generator itself.

**Phase B operation (for reference — not a resolution for Phase A):**
- crazy-agent runs on schedule (e.g. weekly) with read-only access to
  themes + brigadier/ + meta/.
- Produces insight candidates → `swarm/wiki/insights/candidates/`.
- Brigadier reviews each; accepted → `promoted/` with provenance gate.
- Rejected candidates archived with `status: rejected` + reason.
- Monthly FPAR-style metric on promoted/rejected ratio feeds back to
  crazy-agent prompt tuning.

**Evidence.** ROY-WIKI-V3-GOALS W-10 (deferred Phase B+; structure must not
preclude); FPF Part 4 §4.3 (hard AI-strategizing constraint — invent-mode
requires HITL); master-synthesis §5.10 (crazy-agent already defined but no
activation mechanism specified); W-2 §E (Q8 open for trigger condition).

**Alternatives considered.**
- **Cycle count only.** Rejected: narrow-domain swarms trigger prematurely.
- **Theme density only.** Rejected: bookish seeds, not experientially grounded.
- **Fully manual.** Rejected: no objective floor.
- **Fully automatic.** Rejected: violates FPF §4.3.

**Tradeoffs accepted.** 3-AND gate may delay Layer 9 — acceptable per W-10
(non-critical). "50 concepts per theme" is a guess; revisit at first
threshold event.

**Applicability constraint.** Trigger evaluated only at Phase B consideration
window. Phase A never activates. Layer 9 structural location locked by
this resolution; content rules deferred.

**New variants found:** none — primarily a gating decision.

---

### Q9 — Existing `wiki/` v2 vs new `swarm/wiki/` v3

**Recommended answer.** **Coexist + parameterize** (hybrid). Phase A:

1. **v2 `wiki/` stays put.** Untouched — all 546 entries, 572 edges,
   skills, agent-niche symlinks, tools references continue to work.
2. **v3 `swarm/wiki/` is new** with the 9-layer structure (W-1). Gets its
   own `_templates/`, `graph/edges.jsonl`, `index.md`, `log.md`.
3. **Parameterize skills.** Edit the 6 skills that hardcode `wiki/` (the ~85
   line-edits from W-3 §K) to read from `$WIKI_ROOT` env var or config.
   Default `$WIKI_ROOT=wiki`. New v3 skills use `$WIKI_ROOT_V3=swarm/wiki`.
   Effort: ~85 line edits across ingest.md, ask.md, lint.md, consolidate.md,
   build-graph.md, sweep-notion-bank.md (W-3 table).
4. **Shared schema, independent evolution.** Copy (don't symlink) all 9
   `_templates/*.md` from v2 into `swarm/wiki/_templates/`. Both trees
   evolve; v3 can diverge when needed (e.g. add
   `layer:` required field).
5. **Cross-tree edges.** Add `cross-tree-ref` edge type (Q3). Allows v3
   theme-wiki to cite v2 sources/concepts without duplicating content.
   Reverse (v2 → v3) discouraged — v2 is legacy read mostly.
6. **`knowledge-base/` legacy.** Untouched. MIGRATION.md already documents
   its transition. Not merged into either tree.
7. **Migration decision: DEFERRED to Phase B.** Revisit when v3 has ≥50
   entries, ≥1 closed cycle, and demonstrated value. Options then: full
   migrate v2→v3; keep permanent coexistence; gradual promotion (per-
   entry `supersedes` edge from v3 → v2).

**What moves where Phase A:** v2 content stays; templates copied (not
moved); v3 has own `swarm/wiki/graph/edges.jsonl`; cross-tree bridges in
a third file `swarm/wiki/graph/cross-tree.jsonl` (keeps per-tree graphs
clean). Existing agent niche symlinks stay; swarm agents gain new
`niche-v3/<theme> → swarm/wiki/themes/<theme>/` symlinks as themes are
created. `.claude/skills/` hosts both v2 + v3 skills via `$WIKI_ROOT`
indirection.

**Evidence.** ROY-WIKI-V3-GOALS W-1 (`swarm/wiki/` v3 root); BUILD §1.2
(swarm/ top-level); BUILD §1.3 (v2 `wiki/` NOT touched); W-2 §F flag #1
(§5.5.1 writes `wiki/` root — v2 conventions transplant to v3); W-3 §A
(546 entries by type); W-3 §C (572 edges with 9 documented + `part_of`
ad-hoc); W-3 §K (migration cost: ~85–100 line edits + symlink fixups if
fully migrated; 0 immediate edits for coexist; parameterize matches
migrate effort).

**Alternatives considered.**
- **Full migrate** (move v2 → `swarm/wiki/global/`). Rejected Phase A: ~85
  line edits + 10 symlink retargets upfront; breaks flows during transition;
  premature. Keep as Phase B option.
- **Pure coexist, no parameterize.** Rejected: 2× maintenance; drift risk.
- **Merge (v2 imported into v3).** Rejected Phase A: 546-entry schema
  conversion risky.

**Tradeoffs accepted.** Two trees = two `/ask` roots — mitigate via v3-first,
v2-fallback default. `cross-tree-ref` edges = dependency surface — only v3→v2
direction allowed; `/lint` flags reverse. Template divergence risk —
quarterly `/lint` schema-delta check.

**Applicability constraint.** Phase A. Migration decision explicitly
deferred to Phase B evaluation window (after ≥50 v3 entries + ≥1 closed
cycle + observed value delta).

**New variants found:** **`$WIKI_ROOT` parameterize-as-unifier** — audit
shows parameterize + full-migrate cost the same (~85 edits); parameterize
keeps both trees. **Schema drift fix**: `part_of` (233 edges, 40% of v2
graph) is undocumented in v2; formalize in Q3 enum and back-port docs.

---

## Part 3 — Cross-question coherence check

The 9 answers combine into a mechanically consistent spec. Confirmed
coherence + flagged minor tensions below.

**Confirmed coherence:**
1. **Q1 + Q4 share Tier 3** (typed-edge BFS on `edges.jsonl`) — one mechanism,
   two call sites.
2. **Q3 edge vocabulary enables Q1 Tier 3** — 12-type enum used both write-
   time and read-time.
3. **Q2 + §5.5.5 + Q5 /lint PostToolUse = coherent write pipeline**: tier-
   check → structural /lint → append edges.jsonl → append log.md. Same for
   Layers 1–8.
4. **Q6 α-3 state machine provides 3 of Q5's signals** (tombstoned, retired,
   DRR review_checkpoint). Skill learning and staleness are same mechanism.
5. **Q8 Layer 9 honors Q2 single-writer** — crazy-agent (Phase B) writes to
   `candidates/`, brigadier promotes to `promoted/`.
6. **Q9 parameterization enables Q6 skill symlinks** — both use
   `$WIKI_ROOT_V3` indirection.
7. **Q7 git branches give the rollback-fork axis** that Q2 + Q4 need for
   iteration. `iter-vN` ↔ Layer β; `fork-<X>` ↔ Layer α exploration.

**Flagged tensions** (minor, directable to Стадия C):

- **T1 edges.jsonl location asymmetry.** 3 files (v2, v3, cross-tree).
  Resolution: `/build-graph --tree {v2|v3|both}`; cross-tree file is
  derivative, rebuilt from scans.
- **T2 Q4 auto-pull cap vs Q8 signal #2.** Niche-filtered tasks may never
  generate cross-theme refs. Resolution: log cross-theme refs weekly in
  `swarm/wiki/meta/health.md`; re-evaluate signal #2 after 20 cycles if 0.
- **T3 Q6 activation vs validation rubric.** Activation = golden-set pass
  ≥80% (binary); validation = usage-driven (≥10 uses + ≥3:1). Стадия C to
  write explicit rubric.
- **T4 edge-type enum vs empty types.** 4 of 9 v2 types have 0 entries
  today; v3 inherits. Acceptable — upfront enum beats post-hoc; `/lint`
  reports per-type counts.
- **T5 strategies.md location trio (W-2 flag #3).** Q2 §5 resolves:
  `agents/<expert>/strategies.md` = Level-1 sink;
  `swarm/wiki/meta/agent-improvements/` = Level-2 sink;
  `swarm/strategies/` dropped. Стадия C writes into layout spec.

No hard contradictions; all 5 tensions directable to Стадия C.

---

## Part 4 — Compliance with locked decisions

| Decision | Compliant? | Notes |
|----------|-----------|-------|
| **W-1** Multi-layer 9 layers | ✓ | Q3/Q9 honor `swarm/wiki/` root; Q2 treats all 9 as same write protocol; Q4 pulls across layers. |
| **W-2** Brigadier has own Wiki (Layer 2) | ✓ | Q2 allows brigadier to write own layer; Q4 brigadier subtree is pullable for task context. |
| **W-3** Books→Wiki distillation | ✓ | Q1 Tier 2 covers source-based retrieval; Q4 Tier C surfaces book-derived entries. |
| **W-4** Agent-improvement dedicated layer | ✓ | Q2 §5 routes Level-2 CE outputs to `swarm/wiki/meta/agent-improvements/`; Q5 signals include `status: superseded` per α-2. |
| **W-5** Two-level CE | ✓ | Q6 pipeline accommodates both: per-agent strategies feed Level-1; brigadier sweeps produce Level-2 improvements. |
| **W-6** Git branches versioning | ✓ | Q7 provides explicit schema. |
| **W-7** Two parallel task layers (α/β) | ✓ | Q4 targets task-scoped Layer α; Q7 branching corresponds to Layer β iteration vs fork; Q2 single-writer applies to both. |
| **W-8** Workflow = FPF + versioning + deep wiki + 2-level CE | ✓ | Q6 adopts α-3 DRR format; Q2 adopts provenance gate; Q7 gives versioning; Q5 adopts α-2/α-3 state-machines. |
| **W-9** Skill learning as first-class Layer 8 | ✓ | Q6 provides exact layout + pipeline. |
| **W-10** Crazy-agent deferred Phase B+ | ✓ | Q8 explicit trigger gate; Phase A only placeholder. |
| **W-11** Wiki = cognitive infrastructure | ✓ | Q1 multi-tier + Q3 typed edges + Q5 active rot-detection reflect cognition, not storage. |
| **W-12** 1000% depth | ✓ | Q1 multi-tier not grep-only; Q3 12-type edge enum; Q6 formal pipeline not ad-hoc drop. |
| **ROY-ALIGNMENT** 5×4 matrix, Stage-Gated default | ✓ | Q2 experts-via-Task-draft-then-brigadier-commit is Stage-Gated. |
| **ROY-BUILD-LOGIC §1.2** swarm/ top-level | ✓ | Q9 puts v3 under `swarm/wiki/`. |
| **ROY-BUILD-LOGIC §1.3** v2 `wiki/` not touched | ✓ | Q9 coexist explicitly. |
| **ROY-BUILD-LOGIC §2.1** Task tool primary | ✓ | Q2 protocol step 2 (experts return via Task). |
| **ROY-BUILD-LOGIC §2.2** stigmergic wiki shared state | ✓ | Q2 stigmergic via single-writer. |
| **ROY-BUILD-LOGIC §3** single session | ✓ | Q2 brigadier single session; Q7 git branches let sessions span iterations without state pollution. |
| **ROY-BUILD-LOGIC §4.4** context population = this step | ✓ | Q4 resolves. |
| **Master §5.5.2** single-writer Phase A | ✓ | Q2 directly inherits. |
| **Master §5.5.3** provenance YAML + `[src:]` inline | ✓ | Q3 adopts as one of the triple channels. |
| **Master §5.5.5** compound provenance gate | ✓ | Q2 write protocol step 4; Q6 activation step. |
| **Master §5.6.2** PostToolUse `/lint` | ✓ | Q5 integrates into /lint orchestration. |
| **Master §5.7** Tool matrix | ✓ | Q2 experts write only to `wiki/drafts/`; brigadier writes authoritative subtree. |
| **FPF Part 4 α-1..α-5** | ✓ | Q6 adopts α-3 for skills; Q5 integrates α-2 state + α-3 tombstoning. |
| **FPF §4.3** AI not invent-mode strategize | ✓ | Q8 Ruslan-gated activation. |
| **FPF Part 10** preparatory artefacts | ✓ | Q3 edge enum answers 10.8 item 5; Q6 α-3 format honored; Q9 coexist doesn't block 10.4/10.5 foundation artefacts. |

**Tensions to surface to Стадия C** (repeated from Part 3):
- T1 edges file locations (build-graph tooling spec)
- T2 cross-theme trigger metric (meta/health.md addition)
- T3 activation vs validation gate rubric in Q6
- T4 edge-type empty-count acceptable
- T5 strategies.md location trio collapse to pair

All tensions are cosmetic/specification-level; none re-open W-1..W-12.

---

## Part 5 — Ready-for-Стадия-C checklist

### Resolved (carry into architecture spec)

- [x] **Retrieval stack** — four tiers, typed-BFS primary multi-hop, no
      embeddings/PPR Phase A. Scale trigger @ ~2K edges to revisit.
- [x] **Write protocol** — single-writer brigadier across all 9 layers;
      experts via Task drafts; provenance gate; PostToolUse /lint.
- [x] **Cross-ref format** — YAML provenance + inline wikilinks + section-
      header-as-type + edges.jsonl; 12-type edge enum (9 intra + `part_of`
      + 3 cross-layer).
- [x] **Task-scoped context population** — hybrid auto-pull pipeline:
      niche → decisions → 24 Locks → typed-BFS → book excerpts; brigadier
      pin/exclude; 20K token budget.
- [x] **Staleness detection** — 5-signal /lint orchestration; α-2 + α-3
      state integration; time-based only for foundations Phase A.
- [x] **Skill learning pipeline** — 4-subdir Layer 8 (candidates/
      learning/active/usage); α-3 DRR format; explicit owners per transition;
      .claude/skills symlink integration.
- [x] **Git branches schema** — `roy/<project-slug>/{main,iter-vN,fork-X,
      exp-Y}`.
- [x] **Layer 9 activation** — cumulative-AND (cycles, density, Ruslan);
      Phase A placeholder only.
- [x] **v2 / v3 relationship** — coexist + parameterize via `$WIKI_ROOT`;
      ~85 line edits; cross-tree-ref edges; migration decision Phase B.

### Стадия C must write (concrete deliverables)

1. Full directory layout of `swarm/wiki/` across 9 layers.
2. Per-layer template (frontmatter required fields per layer).
3. `swarm/wiki/_templates/edge-types.md` — 12 edge types (def + cardinality
   + inverse + example).
4. `swarm/wiki/_templates/<entity-type>.md` — transplant 9 v2 templates +
   layer-specific fields.
5. `swarm/wiki/foundations/swarm-alphas.md` (FPF §10.4, already mandated).
6. `swarm/lib/shared-protocols.md` (FPF §10.5).
7. Parameterization config: `.claude/config/wiki-roots.yaml` with
   `wiki_root_v2: wiki`, `wiki_root_v3: swarm/wiki`.
8. Skill edit diffs — 6 skills × ~85 line edits to consume `$WIKI_ROOT`.
9. `.claude/skills/` symlink convention for v3 `active/<slug>.md`.
10. `swarm/wiki/meta/health.md` skeleton — FPAR, cycles, cross-theme refs,
    tombstone rate.
11. Q6 activation-vs-validation rubric (T3).
12. Strategies.md trio collapse (T5): keep `agents/.../strategies.md` +
    `swarm/wiki/meta/agent-improvements/`; drop `swarm/strategies/`.

### Still open — needs Ruslan decision BEFORE Стадия C can proceed

| # | Decision needed | Default if Ruslan silent |
|---|-----------------|--------------------------|
| R1 | Accept `roy/<project-slug>/{tag}` branch schema (Q7)? | Yes — proceed |
| R2 | Accept 4-tier filesystem+typed-BFS retrieval as Phase A default (Q1), PPR deferred? | Yes — proceed |
| R3 | Accept parameterize + coexist for Q9 (not full migrate Phase A)? | Yes — proceed |
| R4 | Accept Q6 owners (propose=anyone, draft=brigadier/expert, eval=brigadier, audit=meta-agent, retire=meta-agent/Ruslan)? | Yes — proceed |
| R5 | Accept Q8 3-signal AND + Ruslan manual trigger for Layer 9? | Yes — proceed |
| R6 | Accept strategies.md trio collapse (T5): drop `swarm/strategies/`? | Yes — proceed |
| R7 | Accept 12-type edge enum (Q3)? Or wait and tune from v2 data? | Yes — proceed |
| R8 | Accept all 5 Part-3 tensions as specification-level (not scope changes)? | Yes — proceed |

If Ruslan approves this AWAITING-APPROVAL document as-is (no changes), all
8 R-items default to Yes. If any R-item flips to No, note inline; Стадия C
prompt incorporates the override.

### Стадия C prompt author instructions

- Copy Part 1 verbatim as "Input spec" into Стадия C prompt.
- Per Q, carry Recommended answer + Evidence + Applicability constraint;
  don't re-argue alternatives.
- For T1–T5, carry the resolution-shape from Part 3 as acceptance criteria.
- Do NOT re-open W-1..W-12 or re-read Tier-1 sources — cite this document.
- Word budget for Стадия C: 8,000–14,000 words given 12 deliverables above.
- Output lands at `design/AWAITING-APPROVAL-wiki-v3-architecture-<date>.md`.

---

## Appendix — Citation inventory

Tier-1 sources cited above: knowledge-architecture §A.1/§A.3/§A.6; §B.1/
§B.2/§B.3/§B.4/§B.5; §C.1/§C.3/§C.4; §D.1/§D.3; §E.1/§E.2/§E.3; §F.1/
§F.2/§F.4; §G.3/§G.5; §H.1/§H.3/§H.4/§H.5/§H.7/§H.8; Anti-patterns 3/6/7/
8/10 — 27 distinct refs. Master-synthesis §5.5.1/§5.5.2/§5.5.3/§5.5.4/
§5.5.5/§5.6.2/§5.7/§5.10 — 8 refs. ROY-WIKI-V3-GOALS W-1..W-12 + §2/§5 —
14 refs. ROY-BUILD-LOGIC §1.2/§1.3/§2.1/§2.2/§2.3/§3/§4.2/§4.4 — 8 refs.
FPF-ENHANCEMENT Part 4 α-1..α-5/§4.3 + Part 10.4–10.8 — 11 refs. Existing
v2 infrastructure (9 templates + edges.jsonl + 6 skill specs +
overview.md) — 17 refs. **Total: ≥85 distinct citation points.**

---

**Status:** AWAITING-APPROVAL. Ruslan: if ack, this is the handoff doc for
the Стадия C architecture-spec prompt. If changes needed, flag inline or
per R-item in Part 5.
