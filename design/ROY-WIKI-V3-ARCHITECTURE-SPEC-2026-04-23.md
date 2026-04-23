---
title: Wiki v3 Architecture Spec — Final Consolidated (Стадия C complete)
date: 2026-04-23
status: AWAITING-APPROVAL
covers_deliverables: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
gates_consolidated:
  - design/AWAITING-APPROVAL-wiki-v3-architecture-gate1-2026-04-23.md  # D1–D6, Ruslan-approved 2026-04-23
  - design/AWAITING-APPROVAL-wiki-v3-architecture-gate2-2026-04-23.md  # D7–D12, Ruslan-approved 2026-04-23
upstream:
  - decisions/WIKI-V3-MECHANICS-2026-04-23.md     # Q1..Q9 + R1..R8 + T1..T5
  - design/ROY-WIKI-V3-GOALS-2026-04-23.md        # W-1..W-12
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md  # Part 4 alphas, Part 10 protocols
  - design/ROY-BUILD-LOGIC-2026-04-23.md          # build phasing
  - decisions/ROY-ALIGNMENT-2026-04-22.md         # 5×4 matrix
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md  # §5.5–§5.10 baseline
extractions:
  - raw/research/step-2-2-3c-extractions/A-mechanics-goals-buildlogic.md
  - raw/research/step-2-2-3c-extractions/B-fpf-alphas-protocols.md
  - raw/research/step-2-2-3c-extractions/C-knowledge-arch-karpathy.md
  - raw/research/step-2-2-3c-extractions/D-v2-infrastructure-audit.md
  - raw/research/step-2-2-3c-extractions/E-master-synthesis-matrix.md
critic_reports:
  - raw/research/step-2-2-3c-extractions/critic-gate1.md  # 4 SS + 9 H + 11 M + 7 L; SS+H applied pre-gate1
  - raw/research/step-2-2-3c-extractions/critic-gate2.md  # 4 SS + 8 H + 7 M + 5 L; SS+H applied pre-gate2
target_consumer:
  - Стадия D builders (humans + Claude Code creating swarm/wiki/, swarm/lib/, .claude/config/, .claude/skills/ diffs)
  - 5 domain experts at runtime (read foundations/swarm-alphas.md + lib/shared-protocols.md on every Task invocation)
  - Phase B self-improvement (versioned baseline diffed by the swarm after Private Library consumption)
written_by: Claude Code on server (Opus 4.7, 1M context, Стадия C orchestrator)
branch: claude/jolly-margulis-915d34
word_count_approx: 33700
---

# WIKI v3 ARCHITECTURE SPEC — FINAL CONSOLIDATED (Стадия C COMPLETE)

> **TL;DR — One spec, twelve deliverables, two halves, both approved.**
>
> This file consolidates the Wiki v3 architecture into a single
> Стадия-D-buildable contract:
>
> **Structural core (D1–D6).** Directory layout for 9 layers + global
> spine (D1); per-layer frontmatter templates with dual-axis
> `pipeline`/`state` lifecycle (D2); 12-edge typed enum with from×to
> matrix (D3); 9 entity-type templates as fenced blocks ready to copy
> into `swarm/wiki/_templates/` (D4); 5 swarm-alpha state machines
> with FPF Part 4 verbatim states + transitions tables + ASCII
> diagrams (D5); `swarm/lib/shared-protocols.md` 9-section runtime
> contract (D6).
>
> **Operational integration (D7–D12).** `.claude/config/wiki-roots.yaml`
> parameterisation per Q9 + R3 (D7); 5 in-scope skill diffs ~115
> lines + 3 documented exclusions (D8); `.claude/skills/` symlink
> convention with α-3 lifecycle hooks (D9); `swarm/wiki/meta/health.md`
> 8-section dashboard skeleton with master computation table (D10);
> Q6 skill activation rubric resolving T3 with two-gate distinction
> + filesystem-resident anti-T3 enforcement (D11); T5 strategies
> trio collapse migration (D12).
>
> **Critic-applied.** Both gates ran a mandatory adversarial sub-agent
> review before commit; all 8 showstoppers and 17 high findings were
> fixed pre-gate (4 SS + 9 H for D1–D6; 4 SS + 8 H for D7–D12).
> 18 medium / 12 low findings deferred to Phase-A errata.
>
> **Stage-Gated history.** This consolidation lands AFTER Ruslan
> approved Gate 1 (D1–D6) on 2026-04-23 and Gate 2 (D7–D12) on
> 2026-04-23. Each deliverable was committed individually with the
> `[step-2-2-3c] D<N> draft:` cadence per prompt §8. Branch:
> `claude/jolly-margulis-915d34` (no force-push, no rebase).
>
> **Provenance discipline.** ≥250 distinct citations to W-1..W-12,
> Q1..Q9, R1..R8, T1..T5, FPF Part 4 / Part 10, master synthesis
> §5.5–§5.10, knowledge-architecture research §A–§H, Sub-agent
> extractions A–E, 24-Locks 13/17, BUILD §1.2, CLAUDE.md per-agent
> memory section. Zero locked-decision re-openings.
>
> **Tier discipline.** No Tier 4 input read (no `raw/books-md/`, no
> WebSearch, no WebFetch). **Max-subscription discipline.** Zero
> ANTHROPIC_API_KEY references in skill bodies; zero paid embedding
> services; all retrieval Phase A is filesystem + ripgrep + typed-BFS
> per Q1 + D6 §6.10.
>
> **Next.** Стадия D may begin from this single source. The
> deliverables collectively answer the prompt's success criteria
> §10. No file in `swarm/wiki/`, `swarm/lib/`, `.claude/config/`, or
> `.claude/skills/` is created from this spec until Стадия D opens
> a separate AWAITING-APPROVAL-strategy-D-* gate.

---

## CONSOLIDATION NOTE

Sections D1–D6 below are reproduced verbatim from the approved Gate 1
file (`design/AWAITING-APPROVAL-wiki-v3-architecture-gate1-2026-04-23.md`)
including all critic-gate1 fixes already applied. Sections D7–D12 are
reproduced verbatim from the approved Gate 2 file
(`design/AWAITING-APPROVAL-wiki-v3-architecture-gate2-2026-04-23.md`)
including all critic-gate2 fixes. The two underlying gate files remain
in the repo as Ruslan's audit trail; this consolidation is the
single-source authoritative spec going forward. Cross-references
between deliverables are intra-document (no inter-file dependencies
remaining).

---

## DELIVERABLE 1 — `swarm/wiki/` Directory Layout (9 layers + global spine)

### 1.1 Mandate and citation map

The 9 layers are locked per **ROY-WIKI-V3-GOALS §2 L302–388** (W-1
multi-layer mandate, GOALS §3 W-1 L397–400). Each layer has a fixed
identity, a locked path under `swarm/wiki/`, and a locked content
schema. Phase A scaffolds all 9; Phase B activates Layer 9 only when
Q8's 3-AND trigger fires (per **Q8** resolution, MECHANICS Part 2 §Q8
L544–598; **R5** accepted).

In addition to the 9 numbered layers, this deliverable specifies the
**global spine** — root-level files and directories that exist
alongside (not inside) the 9 layers:

- TOC, log, tour (`index.md`, `log.md`, `overview.md`) — from master
  synthesis §5.5.1 baseline.
- Templates (`_templates/`) — from D4 (entity templates) + D3 (edge
  enum).
- Graph (`graph/`) — from Q3 triple-channel cross-reference rule +
  T1 cross-tree separation.
- Foundations (`foundations/`) — from FPF Part 10.4 (swarm-alphas.md
  mandate) + master synthesis §5.5.1 (engineering/mgmt/systems/
  philosophy/investing distillations).
- Entity-type spine (`concepts/`, `entities/`, `sources/`, `topics/`,
  `claims/`, `ideas/`, `experiments/`, `summaries/`) — from
  CLAUDE.md v2 Wiki Architecture, transplanted per D-audit
  recommendation (Sub-agent D §7 transplant table).
- Filing loop (`comparisons/`) — from `/ask` filing loop per master
  synthesis §5.5.1.
- Cell-write zone (`drafts/`) — from Q2 single-writer brigadier
  resolution + master synthesis §5.5.1 (`drafts/` "In-flight cell
  outputs").
- Brigadier decomposition (`proposals/`) — from master synthesis
  §5.5.1 (`proposals/` "Brigadier decomposition artefacts").
- Per-agent slices (`niches/`) — from CLAUDE.md per-agent memory
  layer + master synthesis §5.5.1 (`niches/` "Per-agent slices").
- Meta dashboard + agent-improvements (`meta/health.md`,
  `meta/agent-improvements/`) — from D10 + Layer 4 (W-4 mandate).
- Archive (`_archive/`) — from `/consolidate` skill audit (Sub-agent
  D §4.4: write surface `wiki/_archive/YYYY-MM-DD-B.md`).

The deliberate **drop** of `swarm/strategies/` (per **T5 + R6**, A's
Section 4 + Section 5) is documented in D12 (Gate 2). The `swarm/wiki/`
layout below contains no `strategies/` subdir at any depth.

### 1.2 ASCII tree (canonical — Стадия D `tree swarm/wiki/` must match)

The tree below is **literal**. Every named directory and file is part
of the bootstrap state of Стадия D (subsection 1.4). Placeholders use
`<…>` and are populated at runtime by the brigadier.

```
swarm/
├── wiki/
│   ├── index.md                              # TOC; updated atomically by /ingest
│   ├── log.md                                # append-only chronology, new-on-top
│   ├── overview.md                           # tour: tree + principles + niches
│   │
│   ├── _templates/                           # entity + edge templates (D3, D4)
│   │   ├── concept.md
│   │   ├── entity.md
│   │   ├── source.md
│   │   ├── claim.md
│   │   ├── idea.md
│   │   ├── topic.md
│   │   ├── experiment.md
│   │   ├── summary.md
│   │   ├── foundation.md
│   │   └── edge-types.md                     # 12-edge enum (D3)
│   │
│   ├── graph/                                # typed cross-references (Q3 + T1)
│   │   ├── edges.jsonl                       # v3 intra-tree edges, append-only
│   │   ├── cross-tree.jsonl                  # v3↔v2 bridge edges only (T1, Q9)
│   │   ├── communities.md                    # /build-graph derivative
│   │   └── summaries.md                      # /build-graph derivative
│   │
│   ├── foundations/                          # axiomatic + alpha contracts
│   │   ├── swarm-alphas.md                   # D5 — 5 alphas state machines
│   │   ├── engineering/                      # Phase B expert distillations
│   │   ├── mgmt/
│   │   ├── systems/
│   │   ├── philosophy/
│   │   └── investing/
│   │
│   ├── concepts/                             # entity-type spine (cross-niche)
│   ├── entities/
│   ├── sources/
│   ├── topics/
│   ├── claims/
│   ├── ideas/
│   ├── experiments/
│   ├── summaries/
│   │
│   ├── comparisons/                          # /ask filing-loop bonus pages
│   ├── drafts/                               # cell-write zone (single-writer, Q2)
│   ├── proposals/                            # brigadier decomposition artefacts
│   │
│   ├── niches/                               # per-agent symlink slices (6 niches per CLAUDE.md L70)
│   │   ├── personal/
│   │   ├── business/
│   │   ├── sales/
│   │   ├── life/
│   │   ├── tech/
│   │   └── meta/
│   │
│   ├── meta/                                 # observability + cross-agent
│   │   ├── health.md                         # D10 dashboard skeleton
│   │   └── agent-improvements/               # Layer 4 (W-4)
│   │       ├── engineering-expert-improvements.md
│   │       ├── mgmt-expert-improvements.md
│   │       ├── systems-expert-improvements.md
│   │       ├── philosophy-expert-improvements.md
│   │       ├── investor-expert-improvements.md
│   │       ├── system-level-improvements.md
│   │       └── emergent-insights.md
│   │
│   ├── _archive/                             # /consolidate losers + tombstones
│   │
│   ├── themes/                               # LAYER 1 — 5 theme wikis
│   │   ├── engineering/
│   │   │   ├── concepts/
│   │   │   ├── methods/                      # canonical methods
│   │   │   ├── heuristics/
│   │   │   ├── anti-patterns/
│   │   │   └── README.md                     # theme tour + book citations
│   │   ├── mgmt/                         # short-form per master synthesis §5.5.1 + ROY-ALIGNMENT mgmt-expert
│   │   │   └── … (same shape)
│   │   ├── systems/
│   │   │   └── … (same shape)
│   │   ├── philosophy/
│   │   │   └── … (same shape)
│   │   └── investing/
│   │       └── … (same shape)
│   │
│   ├── brigadier/                            # LAYER 2 — brigadier own wiki
│   │   ├── how-to-solve-problems/
│   │   ├── how-to-manage-agents/
│   │   ├── how-to-decompose-tasks/
│   │   ├── orchestration-state/              # offloaded state per active task
│   │   └── README.md
│   │
│   ├── agents/                               # LAYER 3 — per-expert wikis
│   │   ├── engineering-expert/
│   │   │   ├── scratchwork/                  # ongoing hypotheses
│   │   │   ├── cross-refs.md                 # links into themes/engineering/
│   │   │   └── README.md
│   │   ├── mgmt-expert/
│   │   ├── systems-expert/
│   │   ├── philosophy-expert/
│   │   └── investor-expert/
│   │
│   ├── tasks/                                # LAYER 5 — per-task ephemeral
│   │   └── <task-id>/                        # created at brigadier intake
│   │       ├── open-questions.md
│   │       ├── context/
│   │       │   ├── manifest.yaml             # priority-ranked pull manifest (Q4)
│   │       │   └── pinned.md                 # brigadier override
│   │       ├── artefacts/                    # expert outputs (cell drafts)
│   │       └── decisions/                    # brigadier per-task decisions
│   │
│   ├── operations/                           # LAYER 6 — long-project logging
│   │   └── <project-slug>/                   # 1:1 with roy/<project-slug>/* branches
│   │       ├── README.md
│   │       ├── decisions-log.md
│   │       ├── rollback-points.md
│   │       ├── forks.md
│   │       └── iterations/
│   │           ├── v1/
│   │           ├── v2/
│   │           └── …
│   │
│   ├── global/                               # LAYER 7 — accumulated learnings
│   │   ├── solved-patterns/
│   │   ├── confirmed-anti-patterns/
│   │   └── compound-rules/                   # promoted from per-agent strategies
│   │
│   ├── skills/                               # LAYER 8 — skill registry
│   │   ├── candidates/                       # awaiting formalization
│   │   ├── learning/                         # under golden-set evaluation
│   │   ├── active/                           # symlinked from .claude/skills/ (D9)
│   │   └── usage/                            # per-skill use-log JSONLs
│   │
│   └── insights/                             # LAYER 9 — Phase B placeholder
│       ├── README.md                         # 3-AND trigger encoded here (Q8)
│       ├── candidates/                       # crazy-agent writes (Phase B)
│       └── promoted/                         # → moves to global/ (Phase B)
│                                             # (2 buckets per Q8 lock; critic review uses α-2 `reviewed` state on candidates/, no separate dir)
│
├── lib/                                      # shared protocols + libraries
│   └── shared-protocols.md                   # D6
│
├── scratchpads/                              # per BUILD §1.2 (volatile)
├── gates/                                    # per BUILD §1.2 (HITL escalations)
├── mailboxes/                                # per BUILD §1.2 (JSONL mailboxes)
└── logs/                                     # per BUILD §1.2 (per-cycle commit logs)
```

**No `swarm/strategies/`.** Per T5 + R6, this venue is dropped; the
two surviving venues for strategies content are
`agents/<expert>/strategies.md` (Level-1, per-expert; lives at the
project root, NOT under `swarm/`, per CLAUDE.md per-agent memory) and
`swarm/wiki/meta/agent-improvements/` (Level-2, swarm-wide). See D12
for the full migration + lint rule.

### 1.3 Per-directory specification table

For every directory in the tree, the table below specifies layer
membership, owner, write permission, naming convention, cardinality,
and bootstrap state.

**Permission legend:**
- `brigadier-write` — only the brigadier may `Write` here. Per Q2
  single-writer, this is the default for all canonical wiki paths.
- `expert-via-task` — experts return drafts via `Task(...)`; brigadier
  evaluates against §5.5.5 provenance gate (D6 §2) and writes.
- `expert-direct (drafts only)` — narrowly scoped to
  `wiki/drafts/<task-id>-<expert>-<artefact>.md` per A's Q2 extraction
  + master synthesis §5.7.1 scoped Write rule.
- `derivative` — written by `/build-graph`, `/ingest`, `/lint`,
  `/consolidate` skills, never hand-edited. Brigadier triggers the
  skill; the skill performs the write.
- `meta-agent-via-task` — meta-agent emits a draft via Task, brigadier
  commits. Resolves the **Q2-vs-Q6 conflict** flagged by Sub-agent A
  (Section 6 #10): meta-agent does NOT get a single-writer carve-out;
  weekly skill audit draft → brigadier evaluates → brigadier commits.
- `human-only` — Ruslan writes (or approves writes via gate file).

**Cardinality legend:** `singleton` (one file, no per-X variation),
`per-entity` (one file per concept/claim/etc.), `per-task` (one
subtree per `<task-id>`), `per-project` (per `<project-slug>`),
`per-cycle` (per α-4 cycle), `per-skill` (per skill slug).

| Path                                              | Layer | Owner               | Permission                | Naming convention                                  | Cardinality   | Bootstrap state                                                                 |
|---------------------------------------------------|-------|---------------------|---------------------------|----------------------------------------------------|---------------|---------------------------------------------------------------------------------|
| `swarm/wiki/index.md`                             | spine | `/ingest`           | derivative                | singleton                                          | singleton     | empty TOC stub, frontmatter `type: index, updated: 2026-04-23`.                 |
| `swarm/wiki/log.md`                               | spine | all skills          | derivative                | append-only, new-on-top, `## [YYYY-MM-DD] verb \| Title` | singleton  | empty body + frontmatter `type: log, updated: 2026-04-23`.                      |
| `swarm/wiki/overview.md`                          | spine | brigadier           | brigadier-write           | singleton                                          | singleton     | tree-diagram + 5 principles + niches table (mirrors v2 `wiki/overview.md`).      |
| `swarm/wiki/_templates/*.md`                      | spine | brigadier           | brigadier-write           | `<entity-type>.md` + `edge-types.md`                | 10 files      | 9 entity templates (D4) + `edge-types.md` (D3); copies, not symlinks (per Q9 R3).|
| `swarm/wiki/graph/edges.jsonl`                    | spine | `/ingest`/`/build-graph` | derivative           | one JSONL line per edge                            | singleton     | empty file (one trailing newline).                                              |
| `swarm/wiki/graph/cross-tree.jsonl`               | spine | `/ingest`/`/build-graph` | derivative           | one JSONL line per cross-tree edge                 | singleton     | empty file. Edges of type `cross-tree-ref` (D3) only; v3→v2 only.               |
| `swarm/wiki/graph/communities.md`                 | spine | `/build-graph`      | derivative                | rebuilt on every `/build-graph`                    | singleton     | header-only stub.                                                                |
| `swarm/wiki/graph/summaries.md`                   | spine | `/build-graph`      | derivative                | rebuilt on every `/build-graph`                    | singleton     | header-only stub.                                                                |
| `swarm/wiki/foundations/swarm-alphas.md`          | spine | brigadier           | brigadier-write           | singleton                                          | singleton     | full 5-alpha state machines from D5 (initial Phase A version).                   |
| `swarm/wiki/foundations/{engineering,mgmt,systems,philosophy,investing}/` | spine | expert-via-task | expert-via-task | `<slug>.md`                                        | per-entity    | empty dirs + `README.md` placeholder per theme; populated Phase B from books.    |
| `swarm/wiki/concepts/`                            | spine | expert-via-task     | expert-via-task           | `<slug>.md` (kebab-case)                           | per-entity    | empty dir.                                                                       |
| `swarm/wiki/entities/`                            | spine | expert-via-task     | expert-via-task           | `<slug>.md`                                        | per-entity    | empty dir.                                                                       |
| `swarm/wiki/sources/`                             | spine | expert-via-task     | expert-via-task           | `<YYYY-MM-DD>-<slug>.md`                            | per-entity    | empty dir.                                                                       |
| `swarm/wiki/topics/`                              | spine | expert-via-task     | expert-via-task           | `<slug>-hub.md` (when MOC) else `<slug>.md`         | per-entity    | empty dir.                                                                       |
| `swarm/wiki/claims/`                              | spine | expert-via-task     | expert-via-task           | `<slug>.md`                                        | per-entity    | empty dir.                                                                       |
| `swarm/wiki/ideas/`                               | spine | expert-via-task     | expert-via-task           | `<slug>.md`                                        | per-entity    | empty dir.                                                                       |
| `swarm/wiki/experiments/`                         | spine | expert-via-task     | expert-via-task           | `<YYYY-MM-DD>-<slug>.md`                            | per-entity    | empty dir.                                                                       |
| `swarm/wiki/summaries/`                           | spine | brigadier/`/build-graph` | derivative           | `<scope>-<YYYY-MM-DD>.md`                           | per-entity    | empty dir.                                                                       |
| `swarm/wiki/comparisons/`                         | spine | `/ask`              | derivative                | `<YYYY-MM-DD>-<question-slug>.md`                   | per-entity    | empty dir.                                                                       |
| `swarm/wiki/drafts/`                              | spine | experts             | expert-direct (drafts only) | `<task-id>-<expert>-<artefact>.md`                | per-task      | empty dir. **Only path where experts write directly.**                          |
| `swarm/wiki/proposals/`                           | spine | brigadier           | brigadier-write           | `<task-id>-decomposition.md`                        | per-task      | empty dir.                                                                       |
| `swarm/wiki/niches/{personal,business,sales,life,tech,meta}/` | spine | brigadier (creates symlinks) | brigadier-write | dir of symlinks into other layers              | 6 dirs        | each `niches/<n>/` populated with symlinks per CLAUDE.md per-agent memory rule. (6 niches per CLAUDE.md L70 lock; no `global` — global aggregation lives at Layer 7 `swarm/wiki/global/`.)  |
| `swarm/wiki/meta/health.md`                       | spine | `/lint` + meta-agent | derivative + meta-agent-via-task | singleton                                | singleton     | D10 skeleton (8 sections + structured-log scaffold).                            |
| `swarm/wiki/meta/agent-improvements/`             | 4     | brigadier           | brigadier-write           | `<expert>-improvements.md` + `system-level-*.md` + `emergent-insights.md` | 7 files | empty body in each (frontmatter only); brigadier appends per W-5 Level-2 sweep. |
| `swarm/wiki/_archive/`                            | spine | `/consolidate`      | derivative                | `<YYYY-MM-DD>-<slug>.md` (loser pages)              | per-entity    | empty dir.                                                                       |
| `swarm/wiki/themes/<theme>/`                      | 1     | brigadier (Phase A seeding) + expert-via-task (Phase B) | brigadier-write | `<sub-bucket>/<slug>.md`            | 5 themes      | `README.md` per theme (theme tour + book citations placeholder).                 |
| `swarm/wiki/themes/<theme>/{concepts,methods,heuristics,anti-patterns}/` | 1 | brigadier/expert-via-task | brigadier-write | `<slug>.md`                                | per-entity    | empty dirs.                                                                      |
| `swarm/wiki/brigadier/`                           | 2     | brigadier           | brigadier-write           | `<slug>.md` per sub-bucket                          | 4 sub-buckets | `README.md` + 4 sub-dirs (`how-to-solve-problems/`, `how-to-manage-agents/`, `how-to-decompose-tasks/`, `orchestration-state/`). |
| `swarm/wiki/agents/<expert>/`                     | 3     | brigadier (canonical) + expert-via-task (drafts) | brigadier-write | `<slug>.md`, `cross-refs.md`, `README.md` | 5 experts | per-expert `README.md` + empty `scratchwork/` + empty `cross-refs.md`.            |
| `swarm/wiki/tasks/<task-id>/`                     | 5     | brigadier           | brigadier-write           | `<task-id>` matches `^task-[a-z0-9-]{1,60}$` (kebab-slug per critic-gate1 H7; e.g. `task-2026-04-23-wiki-v3-spec`) | per-task      | created on intake by brigadier (subdirs `context/`, `artefacts/`, `decisions/`, file `open-questions.md`). |
| `swarm/wiki/tasks/<task-id>/context/manifest.yaml` | 5    | brigadier           | brigadier-write           | singleton per task                                  | per-task      | YAML with `priority: 1..N` per pulled context page (Q4 + W-12 cross-ref §6 #7).  |
| `swarm/wiki/tasks/<task-id>/context/pinned.md`     | 5    | brigadier           | brigadier-write           | singleton per task                                  | per-task      | empty (brigadier override surface).                                              |
| `swarm/wiki/tasks/<task-id>/artefacts/`           | 5     | experts             | expert-direct (drafts only) | `<expert>-<artefact>.md`                          | per-task      | empty dir; populated as experts return drafts.                                   |
| `swarm/wiki/tasks/<task-id>/decisions/`           | 5     | brigadier           | brigadier-write           | `<YYYY-MM-DD-HHMM>-<slug>.md`                       | per-task      | empty dir.                                                                       |
| `swarm/wiki/operations/<project-slug>/`           | 6     | brigadier           | brigadier-write           | `<project-slug>` 1:1 with `roy/<project-slug>/*` branch (Q7 + W-7) | per-project | `README.md` + `decisions-log.md` + `rollback-points.md` + `forks.md` + empty `iterations/`. |
| `swarm/wiki/operations/<project-slug>/iterations/v<N>/` | 6 | brigadier           | brigadier-write           | `v<N>` increments per iteration                     | per-iteration | created per iteration cut.                                                       |
| `swarm/wiki/global/{solved-patterns,confirmed-anti-patterns,compound-rules}/` | 7 | brigadier | brigadier-write | `<slug>.md`                                       | per-entity    | empty dirs.                                                                      |
| `swarm/wiki/skills/candidates/`                   | 8     | brigadier (W-rights) + meta-agent-via-task (audit) | brigadier-write | `<skill-slug>/manifest.md` + `cases.jsonl` | per-skill | empty dir.                                                                       |
| `swarm/wiki/skills/learning/`                     | 8     | brigadier           | brigadier-write           | `<skill-slug>/manifest.md` + `golden-set.jsonl`     | per-skill     | empty dir.                                                                       |
| `swarm/wiki/skills/active/`                       | 8     | brigadier           | brigadier-write           | `<skill-slug>.md` (canonical, target of D9 symlink) | per-skill     | empty dir.                                                                       |
| `swarm/wiki/skills/usage/`                        | 8     | each skill at invoke | derivative                | `<skill-slug>.jsonl` (per-skill use-log)            | per-skill     | empty dir.                                                                       |
| `swarm/wiki/insights/README.md`                   | 9     | human-only          | human-only                | singleton                                          | singleton     | encodes the 3-AND Q8 trigger + states "Phase A scaffold-only — DO NOT write candidates without Ruslan approval." |
| `swarm/wiki/insights/{candidates,promoted}/` | 9 | (Phase B agents)    | (Phase B)                 | `<slug>.md` (Phase B)                               | per-entity    | **empty dirs in Phase A.** No agent instantiated. (W-10, R5; Q8 locks 2 buckets.) Critic review of candidates uses α-2 `reviewed` state in-place; no separate `reviewed/` bucket.                    |
| `swarm/lib/shared-protocols.md`                   | spine | brigadier           | brigadier-write           | singleton                                          | singleton     | full content of D6 (initial Phase A version).                                    |
| `swarm/scratchpads/`                              | n/a   | each agent          | (volatile)                | `<agent-id>.md`                                    | per-agent     | empty dir; not part of `swarm/wiki/` (volatile working memory).                  |
| `swarm/gates/`                                    | n/a   | brigadier           | brigadier-write           | `AWAITING-APPROVAL-<slug>-<YYYY-MM-DD>.md`           | per-gate      | empty dir; HITL escalations land here per D6 §4.                                 |
| `swarm/mailboxes/`                                | n/a   | each agent          | append-only                | `<agent-id>.jsonl`                                  | per-agent     | empty dir; per master synthesis §5.6.2 PostToolUse.                              |
| `swarm/logs/<cycle-id>/`                          | n/a   | brigadier           | brigadier-write            | `<cycle-id>` matches `^cyc-[a-z0-9-]{1,40}$`        | per-cycle     | created at α-4 `opened` transition; contains `events.md` (append-only event stream) and `cycle-log.md` (closed at α-4 `closed`). |
| `swarm/logs/<cycle-id>/events.md`                 | n/a   | each agent          | append-only                | singleton per cycle                                | per-cycle     | append-only event log; one line per `Task()` invocation, integration, gate, etc. |
| `swarm/logs/<cycle-id>/cycle-log.md`              | n/a   | brigadier           | brigadier-write            | singleton per cycle (the α-4 `closed` artefact)    | per-cycle     | written at α-4 `closed`; required frontmatter `cycle_id`, `task_id`, `summary` (≥1 line), `open_questions` (≥1 line); body free-form. **Authoritative state-determining file for α-1 `archived` and α-4 `closed` predicates.** |
| `agents/<expert>/strategies.md`                   | n/a   | expert (Level-1) — direct | expert-direct (this exact file only) | one per expert (5 files)                       | per-expert    | empty body + frontmatter; Level-1 CE per CLAUDE.md (per-agent memory layer "Strategies"). **Lives at project root, NOT under `swarm/`, per T5/R6.** |
| `.claude/config/wiki-roots.yaml`                  | n/a   | brigadier (one-time) | brigadier-write          | singleton                                          | singleton     | content of D7 (initial bootstrap).                                               |
| `.claude/skills/<slug>.md`                        | n/a   | brigadier (creates symlink) | brigadier-write    | `<slug>.md` symlinked to `swarm/wiki/skills/active/<slug>.md` per D9 | per-skill | existing v2 skills retained as regular files; v3 promoted skills land as symlinks per D9 lifecycle. |

### 1.4 Bootstrap state — what Стадия D creates on day one

At the close of Стадия D, **before any task or cycle has run**, a
`tree swarm/wiki/` walk MUST yield exactly the following non-empty
files and the directory skeleton above (with empty leaf dirs as
indicated):

1. `swarm/wiki/index.md` — frontmatter only, empty TOC body.
2. `swarm/wiki/log.md` — frontmatter only, empty body.
3. `swarm/wiki/overview.md` — D1.5 boilerplate (subsection below).
4. All 10 templates in `swarm/wiki/_templates/` per D3 + D4.
5. `swarm/wiki/graph/edges.jsonl` and `cross-tree.jsonl` — empty
   files (single trailing newline; `wc -l` reports 0).
6. `swarm/wiki/graph/communities.md` and `summaries.md` — header
   stubs.
7. `swarm/wiki/foundations/swarm-alphas.md` — full content of D5.
8. `swarm/wiki/foundations/{engineering,mgmt,systems,philosophy,investing}/README.md` — placeholder ("Phase B fill from books").
9. `swarm/wiki/themes/{engineering,mgmt,systems,philosophy,investing}/README.md` — placeholder per theme.
10. `swarm/wiki/brigadier/README.md` — placeholder.
11. `swarm/wiki/agents/{engineering-expert,mgmt-expert,systems-expert,philosophy-expert,investor-expert}/README.md` — placeholder per expert.
12. `swarm/wiki/insights/README.md` — Q8 3-AND trigger + Phase-A
    scaffold-only directive (verbatim text in subsection 1.6).
13. `swarm/wiki/meta/health.md` — D10 skeleton (8 sections, all
    metric placeholders, empty structured logs).
14. `swarm/wiki/meta/agent-improvements/{engineering-expert-improvements.md, mgmt-expert-improvements.md, systems-expert-improvements.md, philosophy-expert-improvements.md, investor-expert-improvements.md, system-level-improvements.md, emergent-insights.md}` — frontmatter only.
15. `swarm/lib/shared-protocols.md` — full content of D6.
16. `agents/<expert>/strategies.md` for the 5 experts — empty body
    + frontmatter (per CLAUDE.md per-agent memory; T5/R6 keep).

All other dirs in the tree (subsections 1.2) start **empty**. The
brigadier creates `swarm/wiki/tasks/<task-id>/` on intake; experts
populate `swarm/wiki/drafts/`; etc.

### 1.5 `swarm/wiki/overview.md` boilerplate (initial content)

```markdown
---
title: Wiki v3 Overview
type: overview
updated: 2026-04-23
---

# Swarm Wiki v3 — Overview

## Tree
<copy of subsection 1.2 ASCII tree>

## Five principles (W-11 cognitive infrastructure framing)
1. Single-writer brigadier (Q2). Experts return drafts via Task.
2. Triple-channel cross-refs (Q3): YAML `related[]` + inline `[[type/slug]]` + `graph/edges.jsonl`. `/lint` enforces consistency.
3. 4-tier retrieval (Q1): direct path → index+grep → typed-BFS → long-context fallback. Embeddings deferred.
4. Provenance gate (D6 §2). Every wiki write cites at least one source artefact.
5. 9 layers + global spine. Drop `swarm/strategies/` (T5/R6).

## Niches (per-agent slice symlinks)
| Niche | Symlinks into |
|---|---|
| personal | (per-agent population) |
| business | … |
| sales | … |
| life | … |
| tech | … |
| meta | … |
| global | … |

## Pipeline statuses
`raw → ingested → compiled → linted → ready` (carried from v2; D2 frontmatter `state` field is α-2 lifecycle, distinct from `pipeline`).
```

### 1.6 `swarm/wiki/insights/README.md` boilerplate (initial content)

```markdown
---
title: Layer 9 — Insights playground (Phase B placeholder)
type: layer-readme
state: scaffold-only
updated: 2026-04-23
---

# Layer 9 — Insights playground

**Phase A status: scaffold-only.** No agent is instantiated to write
into this layer. Per W-10 (crazy-agent deferred) and Q8 (cumulative-AND
human-gated trigger), Layer 9 activates only when ALL THREE of the
following are simultaneously true AND Ruslan explicitly approves:

1. `≥50` closed α-4 cycles (count from `meta/health.md`).
2. `≥2` theme-wikis with `≥50` concepts each AND `≥3` inter-theme
   cross-references (`from.niche != to.niche` edges in
   `graph/edges.jsonl`).
3. Ruslan-approved `AWAITING-APPROVAL-layer-9-activation-*.md` lands
   in `swarm/gates/` and is acked.

Until activation:
- `candidates/`, `promoted/` MUST remain empty.
- `/lint` flags any non-README write under `swarm/wiki/insights/` as
  a Q8/W-10 violation.

Phase-B activation flow (when triggered):
- crazy-agent writes into `candidates/` (page enters at `state: drafted`).
- Critic / philosophy-expert reviews in-place: page advances α-2
  `state: drafted → reviewed → accepted` (no directory move).
- Brigadier promotes via §5.5.5 provenance gate → moves the
  `accepted` candidate file to `promoted/`, then promotes again to
  `swarm/wiki/global/` per W-11 cognitive-infrastructure mandate.
```

### 1.7 Tensions resolved by D1, conflicts escalated

- **T1 (`edges.jsonl` location asymmetry)** — Resolved by separating
  `graph/edges.jsonl` (intra-v3) from `graph/cross-tree.jsonl`
  (v3↔v2). `/build-graph --tree {v2|v3|both}` reads the right file.
  v2 stays untouched (R3).
- **T5 (`strategies.md` trio collapse)** — Resolved by dropping
  `swarm/strategies/` from the tree entirely. The two surviving
  venues (`agents/<expert>/strategies.md` + `swarm/wiki/meta/agent-improvements/`)
  are documented in D12 (Gate 2). BUILD §1.2 layout diagram is
  deliberately amended (cross-ref §6 #8 in Sub-agent A's extraction).
- **Q2-vs-Q6 conflict (Sub-agent A §6 #10)** — Resolved here:
  meta-agent does NOT bypass the single-writer brigadier rule.
  Meta-agent emits a draft via Task (`mode: writing-support`),
  brigadier evaluates the §5.5.5 gate, brigadier commits. The
  permission table (1.3) reflects this via `meta-agent-via-task`.
- **Q4 Tier C "book excerpts" vs no-Tier-4 reading discipline
  (Sub-agent A §6 #9)** — Phase A bootstrap leaves
  `swarm/wiki/sources/` empty; brigadier's book-distillation sweep
  (W-3) is a Phase-A activity that runs *during* Стадия D, AFTER
  this spec is approved. Стадия C does NOT seed sources/. The Q4
  Tier C pipeline therefore starts empty and fills as the W-3 sweep
  produces source pages. Documented here, not escalated.

### 1.8 Compatibility matrix vs Tier-1 mandates

| Locked item | D1 honours by … |
|---|---|
| W-1 multi-layer 9-layer | tree in 1.2 instantiates all 9 layers exactly per ROY-WIKI-V3-GOALS §2 L302–388. |
| W-2 brigadier own wiki | `swarm/wiki/brigadier/` Layer 2 with all 4 sub-buckets per §2 L318–326. |
| W-3 books → wiki distillation | `themes/<theme>/` + `sources/` ready to receive sweep. |
| W-4 agent-improvement layer | `meta/agent-improvements/` with 7 bootstrap files. |
| W-6 git branches | `operations/<project-slug>/` 1:1 with `roy/<project-slug>/*` per Q7 (cross-ref §6 #6). |
| W-7 two parallel task layers | `tasks/` (Layer α task-knowledge) and `operations/` (Layer β operational) kept separate. |
| W-9 skills first-class | `skills/{candidates,learning,active,usage}/` Layer 8 with full pipeline. |
| W-10 crazy-agent deferred | `insights/` scaffold + README only; no agent instantiated. |
| W-11 cognitive infrastructure | tree organises memory/coordination/improvement, not just storage. |
| W-12 1000% depth | every dir specified with owner/permission/naming/cardinality/bootstrap; no "TBD". |
| Q1 4-tier retrieval | `index.md` + `_templates/`-driven frontmatter + `graph/edges.jsonl` + niche dirs all present for Tier 2/3/4. |
| Q2 single-writer | permission table enforces brigadier-write everywhere except `drafts/` + `agents/<expert>/strategies.md` (T5/R6 carve-out). |
| Q3 triple-channel | YAML (per D2 frontmatter `related[]`) + inline (under section headers) + `graph/edges.jsonl` (one record per typed link). |
| Q4 task-scoped context | `tasks/<task-id>/context/{manifest.yaml,pinned.md}` materialises the 4-tier pull pipeline. |
| Q5 5-signal /lint | `meta/health.md` + lifecycle states per D2 + `_archive/` for tombstones. |
| Q6 skill pipeline | `skills/{candidates,learning,active,usage}/` 4-bucket directory. |
| Q7 git branches | `operations/<project-slug>/` slug 1:1 with branch slug. |
| Q8 Layer 9 trigger | `insights/README.md` encodes 3-AND + Phase-A scaffold-only directive (1.6). |
| Q9 v2/v3 coexist | `swarm/wiki/` is v3 root; v2 `wiki/` untouched. `cross-tree.jsonl` for bridge edges. |
| R3 `$WIKI_ROOT` indirection | tree uses literal `swarm/wiki/`; D7 + D8 wire skills to read `$WIKI_ROOT` so any rename (Phase B) is one config flip. |
| R6 drop `swarm/strategies/` | absent from tree; explicit "no `swarm/strategies/`" callout below 1.2. |
| §5.5.1 (master synthesis baseline) | `index.md`, `log.md`, 9 entity-type spine dirs, `foundations/{engineering,…}/`, `niches/`, `comparisons/`, `drafts/`, `proposals/`, `_templates/`, `graph/edges.jsonl` all present and named identically. |
| FPF Part 10.4 swarm-alphas.md | path is `foundations/swarm-alphas.md`; D5 fills content. |
| FPF Part 10.5 shared-protocols.md | path is `swarm/lib/shared-protocols.md`; D6 fills content. |
| 24-Locks (Lock 13 tier enforcement, Lock 17 Filesystem = SoT) | `tier:` field in every page (per D2); filesystem is authoritative; Notion is collaboration-only (CLAUDE.md global rule 4). |
| BUILD §1.2 untouchables | tree adds `swarm/*`, leaves v2 `wiki/`, `decisions/`, `design/`, `raw/`, `prompts/`, `tools/`, `CLAUDE.md`, `.claude/rules/` untouched. |

---

## DELIVERABLE 2 — Per-Layer Frontmatter Templates

### 2.1 Mandate and dual-axis lifecycle clarification

Every page in `swarm/wiki/` MUST carry YAML frontmatter validated by
`/lint` on every write (per master synthesis §5.6.2 PostToolUse,
Sub-agent E §2). This deliverable specifies, for each of the 9 layers,
the global-spine entity-type subdirs, and the special sub-trees, which
fields are required, their types, defaults, validation rules, the
locked source that mandates them, and the alpha state(s) they
participate in.

**Dual lifecycle axes** — every page has TWO orthogonal status fields:

- `pipeline:` (v2-inherited per CLAUDE.md, Sub-agent D §1.1) tracks
  **content maturity**: `raw → ingested → compiled → linted → ready`.
  This is the data-processing axis: how distilled is the content?
- `state:` (FPF Part 4 α-2 Artefact, Sub-agent B §2) tracks **artefact
  lifecycle**: `drafted → reviewed → revised → accepted → referenced
  → superseded → retired → tombstoned`. This is the governance axis:
  what is the artefact's standing in the swarm?

Both fields are required on every non-template page. They are independent
(an `accepted` artefact can have `pipeline: ingested`; a `ready` artefact
can be `superseded`). `/lint` validates each against its enum.

**Tombstoned reconciliation (Sub-agent B §2 gap-flag).** FPF Part 4
α-2 enumerates seven states (`drafted, reviewed, revised, accepted,
referenced, superseded, retired`) with no `tombstoned`. Per Q5 (5-signal
/lint orchestration including α-2/α-3 lifecycle states explicitly
including `tombstoned` per A's §1 Q5) and Sub-agent C §8 anti-pattern
9 (`status: archived` per G.5: "никогда не удалять, только архивировать"),
the spec EXTENDS FPF α-2 with `tombstoned` as an 8th terminal state
(distinct from `retired`: `retired` = legitimate end-of-life,
`tombstoned` = invalidated/withdrawn). D5 formalises the transition.

### 2.2 Cross-layer required fields (every page, every layer)

These fields are mandatory on every `.md` page under `swarm/wiki/`
(except `_templates/`, `index.md`, `log.md`, `overview.md`,
`README.md`, and the JSONL files in `graph/`).

| Field           | Type                                | Req | Default                  | Validation rule (`/lint`)                                                                 | Source                                                | Lifecycle integration                                                       |
|-----------------|-------------------------------------|-----|--------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------|
| `id`            | string (kebab-slug, `<type>-<slug>`) | yes | derived from filename slug or generated by /ingest | unique across `swarm/wiki/`; matches regex `^[a-z]+-[a-z0-9-]{1,60}$`. Examples: `concept-4-tier-retrieval`, `task-2026-04-23-wiki-v3-spec`, `cyc-2026-04-23-am`. (Per critic-gate1 H7 — ULID format dropped; no Tier-1 source mandates ULID; Sub-agent C §1 H.5 uses short-slug examples like `deal-042`, `client:acme`.) | Sub-agent C §1 H.1 (deterministic path schema), W-12 | unique anchor for all alpha state references in `graph/edges.jsonl`         |
| `title`         | string                              | yes | none                     | non-empty; ≤120 chars                                                                       | v2 templates (Sub-agent D §1.1)                       | rendered in `index.md` TOC + `log.md` lines                                 |
| `type`          | enum                                | yes | none                     | one of `concept|entity|source|claim|idea|topic|experiment|summary|foundation|skill|task|operation|insight|improvement|theme-page` | v2 (Sub-agent D §1.1) + Q3 12-edge enum (D3) | drives template selection in /ingest, frontmatter delta lookup              |
| `layer`         | int 1..9 OR `spine`                 | yes | none                     | matches the dir's layer per D1 §1.3                                                         | D1 + W-1                                              | drives Q4 task-context filter + niche routing                               |
| `niche`         | enum                                | yes | none                     | one of `personal|business|sales|life|tech|meta` (per CLAUDE.md L70 6-niche lock; cross-niche aggregation lives at Layer 7 `swarm/wiki/global/`)                                      | CLAUDE.md L70 (locked); v2 templates (Sub-agent D §1.1) drift adds `global` — corrected here per critic-gate1 S3   | Q4 niche-filtered Tier A pull; cross-niche edges feed Q8 Layer-9 trigger    |
| `created`       | iso-date `YYYY-MM-DD`               | yes | today                    | valid ISO date ≤ today                                                                       | v2 (Sub-agent D §1.1)                                 | inputs to staleness signal #3 (Q5 confidence×age)                           |
| `last_modified` | iso-date `YYYY-MM-DD`               | yes | today                    | valid ISO date ≤ today, ≥ `created`                                                          | v2 + Q5                                               | inputs to staleness signal #3                                               |
| `last_reviewed` | iso-date `YYYY-MM-DD`               | opt | `<unset>`                | if set: ≥ `created`. Required for `foundations/` (Q5 §3 365-day re-review).                 | Sub-agent A §1 Q5 + Sub-agent C §4 signal 3           | staleness signal #3                                                         |
| `pipeline`      | enum                                | yes | `raw` for new, `ingested` post-/ingest | one of `raw|ingested|compiled|linted|ready`                                  | CLAUDE.md, Sub-agent D §1                             | content-maturity axis (independent of `state`)                              |
| `state`         | enum                                | yes | `drafted`                | one of `drafted|reviewed|revised|accepted|referenced|superseded|retired|tombstoned` (D5 α-2) | FPF Part 4 §4.1 (Sub-agent B §2) + Q5                 | artefact lifecycle axis; D5 transitions; staleness signals #4, #5           |
| `confidence`    | enum                                | yes | layer default            | one of `low|medium|high`. Defaults: `foundations/` = `high`; `claims/` = layer default; `ideas/` = `low` per v2.  | v2 (Sub-agent D §1.4–§1.5) + Q5                       | staleness signal #1 (low + >60d → flag)                                     |
| `confidence_method` | enum                            | opt (req when `confidence: high` AND `type: foundation` per D4 §4.10) | `<unset>` | one of `expert-judgment|golden-set|cited-source|peer-reviewed|ruslan-attested|brigadier-attested-with-3-supports` (closes critic-gate1 H9 — added the brigadier-attested method that D6 §6.3.2.5 references) | Q5 + W-12 + critic-gate1 H9 | reviewers see why a confidence value was assigned                           |
| `tier`          | enum                                | yes | `core`                   | one of `core|partner|member|public` (24-Lock 13)                                            | master synthesis §5.5.4 (Sub-agent E §1.5.4)         | tier-check hook on outgoing artefacts (D6 §1)                               |
| `produced_by`   | string                              | yes | `<agent>-<mode>` or `human` or `brigadier` | matches `^(brigadier|human|<expert>-(critic|optimizer|integrator|scalability|writing-support))$` | master synthesis §5.5.3 (Sub-agent E §1.5.3) + matrix 5×4 (E §5) | identifies the cell that drafted; brigadier substitutes for canonical writes |
| `derived_from`  | string                              | opt | `<unset>`                | if set: format `<expert>-<mode>` or `<task-id>:<draft-slug>` (chained provenance per E §8 ambiguity 5) | Sub-agent E §6 (matrix-vs-write resolution)          | when brigadier promotes a cell draft to canonical, names the originating cell |
| `task_id`       | string (kebab-slug)                 | opt | `<unset>` (required for tasks/, drafts/, artefacts/) | matches `^task-[a-z0-9-]{1,60}$` (kebab-slug per H7)            | BUILD §2.2 (Sub-agent B §2 α-2 acceptance)            | ties draft → task scope (Q4 + Layer 5)                                      |
| `cycle_id`      | string (kebab-slug)                 | opt | `<unset>` (required for experiments/, summaries/) | matches `^cyc-[a-z0-9-]{1,40}$`                                | master synthesis §5.5.3 + α-4 (Sub-agent B §4)        | ties artefact → α-4 cycle (Layer-9 trigger counter, D10)                    |
| `commit_sha`    | string (40-hex)                     | opt | `<unset>`                | matches `^[0-9a-f]{40}$` if set; written by /ingest after the wiki commit                   | BUILD §2.2 (Sub-agent B §2 α-2 acceptance)            | provenance traceability — per §5.5.5 gate (D6 §2)                           |
| `captured_by`   | string                              | yes | `<agent-name>`           | matches `^(brigadier|<expert>-<mode>|human|/ingest|/ask|/lint|/consolidate|/build-graph)$`   | BUILD §2.2 (Sub-agent B §2)                           | provenance — who recorded this artefact                                      |
| `captured_date` | iso-date                            | yes | today                    | valid ISO date ≤ today                                                                       | BUILD §2.2                                            | provenance — when                                                            |
| `sources`       | list of `{path, range?, quote?}`    | yes | `[]` (empty list)        | non-empty for `pipeline ≠ raw` AND `state ∉ {drafted}` (per §5.5.5 + Q3); each `path` resolves; `range` is `start-end` of lines if set | master synthesis §5.5.3 + §5.5.5 + Q3                | §5.5.5 provenance gate (D6 §2)                                              |
| `related`       | list of wikilinks `[[type/slug]]`   | yes | `[]`                     | each entry exists; reciprocal entry (or non-empty edge in `graph/edges.jsonl`) per Q3 triple-channel | Q3 (Sub-agent A §1) + v2 (Sub-agent D §1)            | Q3 channel A (YAML); Q5 staleness signal #5 (orphan detection)              |
| `topics`        | list of wikilinks `[[topics/slug]]` | yes | `[]`                     | each entry resolves to a `topics/<slug>.md` file                                            | v2 (Sub-agent D §1.1)                                 | drives `topics/<slug>-hub.md` MOC inclusion                                 |
| `tags`          | list of strings                     | opt | `[]`                     | each tag matches `^#(type|status|priority|topic|niche)/[a-z0-9-]+$`                          | v2 conventions (CLAUDE.md "Конвенции" + Sub-agent D §5) | tag-search index for /search-kb (legacy) and /ask grep                      |
| `provenance_inline` | bool                            | opt | `true`                   | if `true`, body MUST contain `[src:path#section]` after each non-trivial paragraph (§5.5.3) | master synthesis §5.5.3                               | enforced by /lint when `pipeline ∈ {compiled, linted, ready}`               |

**`/lint` cross-layer validations:**

1. **id-uniqueness** — `id` unique across all `swarm/wiki/**/*.md`.
2. **state-pipeline matrix** — `state ∈ {accepted, referenced}` requires
   `pipeline ∈ {linted, ready}`; emit warning otherwise.
3. **provenance gate** — when `state` transitions toward `accepted`,
   `sources[]` MUST be non-empty (per §5.5.5, D6 §2).
4. **niche-edge invariant** — for any edge `from → to` in
   `graph/edges.jsonl` where `from.niche != to.niche`, both pages MUST
   declare the cross-niche relationship in `related[]` AND tag at
   least one entry with `#topic/cross-niche` (feeds Q8 Layer-9 trigger
   metric per D10 §3).
5. **Sub-agent C §2 anti-pattern 11 enforcement** — every inline
   wikilink `[[type/slug]]` in body MUST appear in `related[]` AND
   produce one record in `graph/edges.jsonl` (Q3 triple-channel
   reconciliation; **Sub-agent C §2 gap closed here**).

### 2.3 Per-entity-type frontmatter additions (global spine subdirs)

These extend §2.2 for pages living in the entity-type spine. v2
templates audited by Sub-agent D §1 are the baseline; v3 adds the
fields shown.

#### `concepts/<slug>.md`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `definition` | string (single line) | yes | none | non-empty, ≤200 chars | v2 concept.md "Суть в одной строке" | rendered in `index.md` TOC entry |
| `examples` | list of strings | opt | `[]` | each string ≤200 chars | spec illustrative | searchable via grep |
| `extends` | wikilink `[[concepts/slug]]` | opt | `<unset>` | resolves; produces `extends` edge (D3) | v2 (concept.md "Расширяет") | Q3 channel A → graph |

#### `entities/<slug>.md`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `entity_type` | enum | yes | none | one of `person|company|product|team|event|place` | v2 entity.md `entity_kind` (Sub-agent D §1.3) | drives `niches/business/` symlink routing |
| `external_ids` | yaml-block (map of `{system → id}`) | opt | `{}` | each key in `{notion, linkedin, github, hubspot}`; each id non-empty | spec illustrative + CLAUDE.md "Key Notion IDs" pattern | bridges wiki entity to external systems |

#### `sources/<YYYY-MM-DD>-<slug>.md`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `source_type` | enum | yes | none | one of `article|book|podcast|video|meeting|voice-memo|transcript|web|paper` | v2 source.md `source_kind` (Sub-agent D §1.1) | drives /ingest source-card layout |
| `url` | string | opt (req if `source_type ∈ {article, video, podcast, web, paper}`) | `<unset>` | valid URL | v2 source.md | retrieval entry-point |
| `local_path` | string | opt (req if `source_type ∈ {book, voice-memo, transcript, meeting}`) | `<unset>` | path resolves under `raw/` | v2 source.md `raw_file` | links to raw artefact |
| `author` | string | opt | `<unset>` | non-empty if set | v2 | grep search by author |
| `ingested_date` | iso-date | yes | today | valid ISO date | v2 source.md `captured` | paired with `pipeline` advance |
| `coverage` | list of wikilinks `[[topics/slug]]` | yes | `[]` | each resolves; each `topic` page also lists this source via reciprocal `MOC_for[]` | spec illustrative + Q3 | drives Q1 Tier 2 grep + Tier 3 BFS seeds |

#### `topics/<slug>.md` (or `<slug>-hub.md` if MOC)
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `MOC_for` | list of wikilinks | opt | `[]` | each entry resolves; this page acts as Map-of-Content for those entities | spec illustrative + Sub-agent D §1.6 (topic.md "Plays hub role") | /ask uses MOC for Tier 2 retrieval |

#### `claims/<slug>.md`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `stance` | enum | yes | `asserted` | one of `asserted|supported|contested|refuted` | v2 claim.md (Sub-agent D §1.4) | Q5 staleness signal #4 supersession chain |
| `support_count` | int | opt | `0` | computed by `/build-graph` from `supports` edges | spec illustrative + Sub-agent D §2 (84 `supports` edges in v2) | derivative; `/lint` recomputes |
| `contradiction_count` | int | opt | `0` | computed by `/build-graph` from `contradicts` edges (bidirectional per A §1 Q5) | spec illustrative + Q5 | derivative |
| `support_edges` | list of wikilink | opt | `[]` | each is `[[claim/slug]]` or `[[source/slug]]` with reciprocal `supports` edge | Q3 + Sub-agent D §2 | Tier 3 BFS seed for `/ask` |
| `contradiction_edges` | list of wikilink | opt | `[]` | bidirectional `contradicts` edges (Sub-agent A §1 Q5) | Q5 + Sub-agent D §2 | feeds `support/contradiction` ratio for /lint |
| `falsifier` | string (multi-line) | yes | none | non-empty body section (mirrors v2 claim.md "Что опровергнуло бы это утверждение") | v2 (Sub-agent D §1.4) | encourages epistemic discipline |

#### `experiments/<YYYY-MM-DD>-<slug>.md`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `hypothesis` | string | yes | none | non-empty, ≤500 chars | spec illustrative + v2 experiment.md (Sub-agent D §1.7) | falsifiable framing |
| `start_date` | iso-date | yes | today | valid ISO date | v2 `started` | timeline tracking |
| `end_date` | iso-date | opt | `<unset>` | if set, ≥ `start_date` | v2 `ended` | required for `outcome ∈ {won, lost}` |
| `outcome` | enum | yes | `open` | one of `open|won|lost|aborted` | spec extends v2 (`status: planned|running|done|aborted`) — adds `won/lost` semantics | feeds α-3 strategy `validated` transitions |
| `cycle_id` | string (kebab-slug) | yes | none | matches `^cyc-[a-z0-9-]{1,40}$` | spec illustrative + α-4 | ties experiment to its cycle |

#### `summaries/<scope>-<YYYY-MM-DD>.md`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `summary_window` | enum | yes | none | one of `daily|weekly|topic|cluster` | v2 summary.md `scope` (Sub-agent D §1.8) | drives /build-graph aggregator |
| `community_id` | string | opt | `<unset>` | if `summary_window = cluster`, non-empty; resolves to a community in `graph/communities.md` | spec illustrative + GraphRAG hint Sub-agent C §6 | Layer-9 cross-theme metric input |
| `covers` | list of wikilinks | yes | `[]` | non-empty; each resolves to a page in scope | v2 summary.md `covers` | provenance — what this summary aggregates |

#### `ideas/<slug>.md`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `proposed_by` | string | yes | `produced_by` value | non-empty | spec illustrative | accountability |
| `routing_target` | enum | opt | `<unset>` | one of `experiment|claim|topic|drop|skill-candidate` | spec illustrative + Q6 (skill candidate path) | drives idea → next-stage promotion |
| `idea_status` | enum | yes | `raw` | one of `raw|evaluated|planned|in-progress|shipped|dropped` | v2 idea.md `status` (Sub-agent D §1.5) | distinct from cross-layer `state` (which is α-2 lifecycle); idea.md retains v2 status semantics |

#### `foundations/<slug>.md` (and per-theme `foundations/<theme>/<slug>.md`)
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `binding_scope` | enum | yes | none | one of `swarm-wide|theme:<theme>|expert:<expert>` | spec illustrative + W-12 | tells brigadier where this foundation binds |
| `supersedes_versions` | list of strings | opt | `[]` | each `<slug>@v<N>` references a prior version | spec illustrative + Q5 supersession chain | feeds `superseded_by` edge chain (D3) |
| `last_reviewed` | iso-date | yes | `created` | overrides §2.2 default; required per Q5 365-day re-review | A §1 Q5 + Q5 staleness signal #3 | Q5 time-based staleness |
| `confidence` | enum | yes | `high` | overrides §2.2 default | v2 foundation.md (Sub-agent D §1.9) | filters foundation queries |

### 2.4 Per-layer additions (the 9 numbered layers)

Pages inside the 9 numbered layers add layer-specific fields on top of
§2.2 + the entity-type fields if the layer hosts entity-typed pages.

#### Layer 1 — `themes/<theme>/...`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `theme` | enum | yes | dir-derived | one of `engineering|mgmt|systems|philosophy|investing` (5 themes; matches both `themes/<theme>/` and `foundations/<theme>/` dir naming per master synthesis §5.5.1, agent-dir convention `<theme>-expert/` per ROY-ALIGNMENT) | master synthesis §5.5.1 + ROY-ALIGNMENT (Sub-agent E §5) | drives `niche` per the 5×1 theme→niche map below |
| `book_citations` | list of `{book_path, page_range?}` | yes | `[]` | each `book_path` resolves under `raw/books-md/` (Phase B); empty in Phase A | W-3 + Phase-A note in D1 §1.7 | provenance for theme-distillation per book |

**Theme → niche map (5×1; closes critic-gate1 H5):**

| `theme` value | `niche` value | Notes |
|---|---|---|
| `engineering` | `tech` | engineering content lands in tech niche |
| `mgmt` | `business` | management theme → business niche |
| `systems` | `meta` | systems thinking is meta-domain (cybernetics, complexity) |
| `philosophy` | `meta` | philosophy of science is meta-domain |
| `investing` | `business` | investing → business niche |

Pages under `swarm/wiki/themes/<theme>/...` MUST set `niche` per this
map; `/lint` rejects mismatches. Note that two themes (`mgmt` +
`investing`) share `business`, and two (`systems` + `philosophy`)
share `meta` — that is intentional: 5 themes condense into 6 niches
(`tech`, `business`, `meta`, plus the cross-cutting `personal`,
`sales`, `life`).

#### Layer 2 — `brigadier/...`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `bucket` | enum | yes | dir-derived | one of `how-to-solve-problems|how-to-manage-agents|how-to-decompose-tasks|orchestration-state` | W-2 + GOALS §2 L318–326 | drives brigadier-prompt context window |
| `applies_to` | enum | opt | `<unset>` | one of `all-tasks|task-type:<type>|alpha:<alpha-id>` | spec illustrative + W-2 | conditional context loading |

#### Layer 3 — `agents/<expert>/...`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `expert` | enum | yes | dir-derived | one of `engineering|mgmt|systems|philosophy|investor` (suffix `-expert` implied) | matrix 5×4 (Sub-agent E §5) | drives expert-prompt slice |
| `is_scratchwork` | bool | opt | `false` | when `true`, this page is in `scratchwork/` and NOT subject to §5.5.5 provenance gate | spec resolves the per-expert wiki vs canonical-wiki tension | scratchwork pages excluded from Q5 staleness sweep |

#### Layer 4 — `meta/agent-improvements/<slug>.md`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `expert` | enum (`engineering|mgmt|systems|philosophy|investor|brigadier|all`) OR `system-level` OR `emergent` | yes | none | matches the file basename slug | W-4 + W-5 Level-2 CE | drives brigadier sweep filter |
| `improvement_target` | enum | yes | none | one of `prompt|protocol|skill|hook|memory-layer` | spec illustrative + W-5 | tells brigadier what to mutate when applying |
| `validation_status` | enum | yes | `proposed` | one of `proposed|under-validation|accepted|rejected|tombstoned` (mirrors α-3 partially) | spec illustrative + α-3 (Sub-agent B §3) + W-5 | α-3 state for cross-agent improvements |
| `proposed_by` | string | yes | `produced_by` | format `<expert>-<mode>` or `meta-agent` or `brigadier` | spec illustrative | accountability |
| `applied_by` | string | opt | `<unset>` | populated when validation_status = accepted | spec illustrative | post-application audit |
| `applied_at` | iso-date | opt | `<unset>` | populated alongside `applied_by` | spec illustrative | audit trail |

#### Layer 5 — `tasks/<task-id>/...`
Per-task pages add:
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `task_id` | string (kebab-slug) | yes | dir-derived | matches `^task-[a-z0-9-]{1,60}$`; matches `<task-id>` in path | BUILD §3 + α-1 (Sub-agent B §1) | α-1 Task lifecycle |
| `alpha_state` | enum | yes | `submitted` | one of `submitted|intaked|decomposed|dispatched|integrated|gated|approved|compounded|archived|refused|returned|rejected` | α-1 (Sub-agent B §1) | D5 α-1 state |
| `niche` | enum | yes | per task | from `personal|business|sales|life|tech|meta` (per cross-layer §2.2 — 6 niches per CLAUDE.md L70 lock) | Q4 niche-filter | Tier A pull |

For `tasks/<task-id>/context/manifest.yaml` specifically:
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `pulls` | list of `{path, priority, source-tier, included_at}` | yes | `[]` | each `path` resolves under `swarm/wiki/`; `priority ∈ 1..N`; `source-tier ∈ {A,B,C}` per Q4 | Q4 (Sub-agent A §1) + W-12 cross-ref | priority-based digest fallback |
| `total_tokens_estimated` | int | yes | none | ≤ 20000 (Q4 cap) | Q4 + cross-ref §6 #7 (W-12 depth) | hard cap enforcement |

#### Layer 6 — `operations/<project-slug>/...`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `project_slug` | string (kebab-case ≤30 chars) | yes | dir-derived | matches `^[a-z0-9][a-z0-9-]{0,29}$`; 1:1 with `roy/<project-slug>/*` branch | Q7 + W-6 + cross-ref §6 #6 | git-branch ↔ wiki dir invariant |
| `parent_branch` | string | yes | `roy/<project-slug>/main` | Q7 schema | Q7 | branch tracking |
| `iteration` | int OR `<unset>` | opt | `<unset>` | for pages under `iterations/v<N>/`, set to `<N>` | Q7 + W-6 | iteration tracking |

#### Layer 7 — `global/...`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `bucket` | enum | yes | dir-derived | one of `solved-patterns|confirmed-anti-patterns|compound-rules` | GOALS §2 L368–374 | drives /ask global-pattern surfacing |
| `promoted_from` | wikilink | opt | `<unset>` | resolves to `agents/<expert>/strategies.md` line OR `meta/agent-improvements/...` page; required for `compound-rules/` | W-5 Level-2 + T5 + R6 | provenance — where the rule originated |

#### Layer 8 — `skills/<bucket>/<slug>/...`
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `skill_slug` | string (kebab-case) | yes | dir-derived | matches `^[a-z0-9][a-z0-9-]{0,49}$` | Q6 (Sub-agent A §1) | symlink slug per D9 |
| `skill_state` | enum | yes | `candidate` | one of `candidate|learning|active|tombstoned` — 4 values matching FPF Part 4 §4.3 α-3 lock (`retired` dropped per critic-gate1 S2; supersession captured via tombstoned + `supersedes:` edge) | Q6 + α-3 + D11 | drives bucket placement |
| `golden_set_path` | string | opt (req when `skill_state ∈ {learning, active}`) | `<unset>` | resolves to `swarm/wiki/skills/<bucket>/<slug>/golden-set.jsonl` | Q6 + Sub-agent C §5 | activation predicate (D11) |
| `success_count` | int | opt | `0` | derived from `usage/<slug>.jsonl` | Q6 + D11 | activation/retirement predicates |
| `loss_count` | int | opt | `0` | derived from `usage/<slug>.jsonl` | Q6 + D11 | activation/retirement predicates |
| `n_uses` | int | opt | `0` | derived; `success + loss` | Q6 (≥10 uses) | activation predicate |
| `owners` | yaml-block (map: `{transition → role}`) | yes | per Q6 R4 default | populated per Q6 R4 owner table | R4 + Q6 | transition routing |

#### Layer 9 — `insights/...` (Phase A: README only)
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `insight_state` | enum | yes (Phase B) | `candidate` | one of `candidate|promoted` (review status carried by α-2 `state` field) | Q8 (2 buckets locked) + W-10 | bucket placement |
| `cross_themes` | list of theme enums | opt (req for `reviewed`) | `[]` | each in Layer 1 theme enum; ≥2 entries to qualify for `reviewed` | Q8 cross-theme density | Layer-9 trigger metric input |
| `phase_a_lock` | bool | yes | `true` | `/lint` blocks Layer-9 page creation when `true` AND no Ruslan ack file exists in `swarm/gates/` | W-10 + R5 | enforces "scaffold-only" |

### 2.5 Special sub-tree additions

**`drafts/<task-id>-<expert>-<artefact>.md`** — expert-direct write
zone (the only one). Required: §2.2 cross-layer + `task_id` +
`produced_by = <expert>-<mode>`. `state` is always `drafted` here;
brigadier mutates `state` only when promoting out of `drafts/`. `/lint`
flags any non-`drafted` state in `drafts/`.

**`comparisons/<YYYY-MM-DD>-<question-slug>.md`** — `/ask` filing
loop. Required: §2.2 + `question:` (string), `synthesis_of:` (list of
wikilinks). `produced_by = /ask`. State auto-set to `accepted` on
write because /ask runs the §5.5.5 gate inline (Sub-agent D §4.2 ask
audit).

**`proposals/<task-id>-decomposition.md`** — brigadier intake
artefact. Required: §2.2 + `task_id` + `decomposition` (yaml-block:
list of `{cell, mode, ap_cost, ap_budget}` per BUILD §3) +
`produced_by = brigadier`.

### 2.6 Master cross-layer reference table

Quick reference: which fields appear where.

| Field            | spine root | concepts | entities | sources | claims | ideas | topics | experiments | summaries | foundations | themes (L1) | brigadier (L2) | agents (L3) | meta/agent-improvements (L4) | tasks (L5) | operations (L6) | global (L7) | skills (L8) | insights (L9) |
|------------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| `id`             | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `title`          | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `type`           | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `layer`          | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `niche`          | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `created`        | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `last_modified`  | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `pipeline`       | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `state`          | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `confidence`     | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `tier`           | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `produced_by`    | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `sources[]`      | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `related[]`      | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `last_reviewed`  | opt | opt | opt | opt | opt | opt | opt | opt | opt | **req** | opt | opt | opt | opt | opt | opt | opt | opt | opt |
| `task_id`        | – | – | – | – | – | – | – | opt | – | – | – | – | – | – | **req** | – | – | – | – |
| `cycle_id`       | – | – | – | – | – | – | – | **req** | **req** | – | – | – | – | – | opt | opt | – | opt | – |
| `theme`          | – | – | – | – | – | – | – | – | – | opt | **req** | – | – | – | – | – | – | – | – |
| `expert`         | – | – | – | – | – | – | – | – | – | – | – | – | **req** | **req** | – | – | – | – | – |
| `bucket`         | – | – | – | – | – | – | – | – | – | – | – | **req** | – | – | – | – | **req** | – | – |
| `project_slug`   | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | **req** | – | – | – |
| `skill_slug`     | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | **req** | – |
| `skill_state`    | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | **req** | – |
| `insight_state`  | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | **req (B)** |
| `phase_a_lock`   | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | **req** |
| `binding_scope`  | – | – | – | – | – | – | – | – | – | **req** | – | – | – | – | – | – | – | – | – |

**Validation cadence.** §5.6.2 PostToolUse `/lint` runs schema-check on
the single file written; rejects on invalid frontmatter (Sub-agent E
§2). Scheduled `/lint` (per `cron` per Q5 #3) re-validates the whole
tree.

**1000% depth note.** Every field above has: name, type, req/opt,
default, validation rule, locked source, and lifecycle integration.
No "TBD"; no "spec author may decide later." Стадия D writes the
schema validators directly from the per-layer subsections above.

---

## DELIVERABLE 3 — `swarm/wiki/_templates/edge-types.md` (typed edge enum)

### 3.1 Mandate, count reconciliation, and citation map

**WIKI-V3-MECHANICS L216–234** enumerates 9 intra-layer types +
`part_of` (formalised 10th intra-layer) + 3 cross-layer types — that
literal enumeration adds to 13. The summary line at L236 reads "Total:
12 edge types"; this off-by-one is reconciled here by **dropping
`addresses_gap`** from the enum (per critic-gate1 H4 +
Sub-agent D §2 audit: 0 v2 usage; semantically overlapped by
`derived_from` + the `/lint` orphan-detection signal). Result: **12
distinct edge types** (8 intra-layer original + `part_of` + 3
cross-layer = 12), matching the locked R7 summary. If Ruslan
disagrees and wants `addresses_gap` retained, append it to D3 §3.2 as
the 13th type — non-breaking add.

The 12-type enum lives at `swarm/wiki/_templates/edge-types.md` and is
the single source of truth for `/build-graph`, `/ingest`, `/lint`, and
`/ask` Tier-3 typed-BFS retrieval (per Sub-agent A §6 cross-ref #1).

### 3.2 Per-edge-type specification

Each entry below is a complete contract: name, definition,
cardinality, directionality, inverse, allowed source/target layers,
worked example record (JSON line as it appears in
`graph/edges.jsonl`), cross-layer flag, and `/lint` rule.

#### 3.2.1 `extends` (intra-layer #1)
- **Definition.** Page A refines or expands page B; A is a more
  specific or more developed treatment of B's subject.
- **Cardinality.** N:1 (a page may extend at most one parent; many
  pages may extend the same parent).
- **Directionality.** Directed.
- **Inverse.** `extended_by` (derivative; computed by `/build-graph`,
  not stored as primary).
- **Allowed `from` layers.** spine entity-type (`concepts`, `claims`,
  `topics`, `foundations`); Layers 1, 2, 3, 7.
- **Allowed `to` layers.** Same as `from`.
- **Cross-layer flag.** No.
- **Example.** `{"from":"concepts/llm-wiki","to":"concepts/karpathy-llm-wiki","type":"extends","ts":"2026-04-23","confidence":"high"}`
- **`/lint` rule.** No cycles (extends-graph must be a DAG); flag if
  `from.layer != to.layer` (use `derived_from` or `layer-ref` for
  cross-layer).

#### 3.2.2 `contradicts` (intra-layer #2)
- **Definition.** Page A explicitly conflicts with claim/conclusion
  in page B.
- **Cardinality.** N:M.
- **Directionality.** Bidirectional (per Sub-agent A §1 Q5: "require
  bidirectional `contradicts` edges"); `/build-graph` materialises
  both directions when one is asserted.
- **Inverse.** Self.
- **Allowed `from`/`to`.** `claims`, `foundations`, `concepts`,
  `experiments` (cross-experiment refutation).
- **Cross-layer flag.** No.
- **Example.** `{"from":"claims/embeddings-required","to":"claims/embeddings-deferred","type":"contradicts","ts":"2026-04-23","confidence":"medium"}`
- **`/lint` rule.** Both directions present; both pages bear `stance:
  contested` or `refuted` (per D2 claims schema); contradiction count
  surfaced in `meta/health.md` per D10 §6.

#### 3.2.3 `supports` (intra-layer #3)
- **Definition.** Page A provides evidence for the claim in page B.
- **Cardinality.** N:M.
- **Directionality.** Directed (`evidence → claim`).
- **Inverse.** `supported_by` (derivative).
- **Allowed `from`.** `sources`, `experiments`, `claims` (claim
  supporting another claim).
- **Allowed `to`.** `claims`, `concepts`, `foundations`.
- **Cross-layer flag.** No.
- **Example.** `{"from":"sources/2026-04-19-knowledge-arch","to":"claims/4-tier-retrieval","type":"supports","ts":"2026-04-23","confidence":"high"}`
- **`/lint` rule.** `to` page's `support_count` ≥ count of incoming
  `supports` edges (recomputed by `/build-graph`).

#### 3.2.4 `inspired_by` (intra-layer #4)
- **Definition.** Creative lineage — idea A was inspired by idea B
  (looser than `extends`; no claim of refinement).
- **Cardinality.** N:M.
- **Directionality.** Directed.
- **Inverse.** `inspired` (derivative).
- **Allowed `from`/`to`.** Primarily `ideas`; also `experiments` (an
  experiment inspired by an idea) and `concepts` (a concept inspired
  by another).
- **Cross-layer flag.** No.
- **Example.** `{"from":"ideas/swarm-as-memory","to":"ideas/karpathy-llm-wiki","type":"inspired_by","ts":"2026-04-23","confidence":"medium"}`
- **`/lint` rule.** None blocking; surfaced in `/build-graph`
  community detection.

#### 3.2.5 `tested_by` (intra-layer #5)
- **Definition.** Claim A was empirically tested by experiment B.
- **Cardinality.** N:M.
- **Directionality.** Directed (`claim → experiment`).
- **Inverse.** `tests` (derivative; on the experiment side).
- **Allowed `from`.** `claims`, `foundations`.
- **Allowed `to`.** `experiments`.
- **Cross-layer flag.** No (both spine).
- **Example.** `{"from":"claims/4-tier-retrieval","to":"experiments/2026-05-15-tier3-bfs-benchmark","type":"tested_by","ts":"2026-04-23","confidence":"high"}`
- **`/lint` rule.** Experiment must have non-empty `outcome` ∈ `{won,
  lost, aborted}` for the `tests` direction to be informative; flag
  if `experiment.outcome = open` and `tested_by` count ≥ 1 for >30
  days (stale experiment).

#### 3.2.6 `invalidates` (intra-layer #6)
- **Definition.** Experiment or evidence B invalidates claim A.
- **Cardinality.** N:M.
- **Directionality.** Directed (`evidence → claim`).
- **Inverse.** `invalidated_by` (derivative).
- **Allowed `from`.** `experiments`, `sources`, `claims` (a stronger
  refuting claim).
- **Allowed `to`.** `claims`, `foundations`.
- **Cross-layer flag.** No.
- **Example.** `{"from":"experiments/2026-05-15-tier3-bfs-benchmark","to":"claims/embeddings-required","type":"invalidates","ts":"2026-05-16","confidence":"high"}`
- **`/lint` rule.** Auto-marks `to` page `stance: refuted`; emits
  warning if `to` page is `state: accepted` and not yet
  `superseded_by` a successor claim within 7 days.

#### 3.2.7 `supersedes` (intra-layer #7)
- **Definition.** New page A replaces older page B (often paired with
  `state: superseded` on B per α-2).
- **Cardinality.** N:1 (B has one canonical successor; A may
  supersede many B-versions).
- **Directionality.** Directed (`new → old`).
- **Inverse.** `superseded_by` (per Sub-agent A §1 Q5; explicit
  inverse, ALSO stored — bidirectional storage required so that
  /lint can walk supersession chains forward and backward).
- **Allowed `from`/`to`.** Same layer; same `type`.
- **Cross-layer flag.** No.
- **Example.** `{"from":"foundations/swarm-alphas-v2","to":"foundations/swarm-alphas-v1","type":"supersedes","ts":"2026-04-23","confidence":"high"}`
- **`/lint` rule.** Supersession DAG (no cycles); B must bear
  `state: superseded` and frontmatter `superseded_by:
  [[<A>]]`; A's frontmatter `supersedes_versions:` includes B
  (per D2 foundations schema).

#### 3.2.8 `derived_from` (intra-layer #8)

(Per critic-gate1 H4 reconciliation, the previous slot 3.2.8 — `addresses_gap`
— is dropped to land on 12 types matching MECHANICS L236 summary.
Gap-clearing semantics are absorbed by `derived_from` + the `/lint`
orphan-detection signal.)

- **Definition.** Source S was used to derive concept/claim/idea P.
- **Cardinality.** N:M.
- **Directionality.** Directed (`derived → source`).
- **Inverse.** `derives` (derivative).
- **Allowed `from`.** `concepts`, `claims`, `ideas`, `summaries`,
  `foundations`.
- **Allowed `to`.** `sources`.
- **Cross-layer flag.** No (both spine).
- **Example.** `{"from":"concepts/4-tier-retrieval","to":"sources/2026-04-19-knowledge-arch","type":"derived_from","ts":"2026-04-23","confidence":"high"}`
- **`/lint` rule.** Pages with `pipeline ∈ {compiled, linted, ready}`
  AND `state ∈ {accepted, referenced}` must have ≥1 `derived_from`
  edge OR ≥1 `supports` edge OR `tier: foundation` (provenance gate
  per §5.5.5, D6 §2).

#### 3.2.9 `part_of` (intra-layer #9 — formalised per Q3)
- **Definition.** Mereological — page A is a part of composite B
  (Sub-agent C §3 + F.1 holon mereology). The dominant v2 edge (233
  of 572 records); formalised here per Sub-agent A §1 Q3 ("`part_of`
  formalised as 10th intra-layer edge").
- **Cardinality.** N:1 (a part has one canonical whole at a given
  level; a whole has many parts).
- **Directionality.** Directed (`part → whole`).
- **Inverse.** `has_part` (derivative; computed by `/build-graph`).
- **Allowed `from`.** Any spine entity-type (concepts, claims,
  experiments, etc.).
- **Allowed `to`.** `topics` (hub→children pattern), `foundations`
  (sub-foundation → over-foundation).
- **Cross-layer flag.** No.
- **Example.** `{"from":"concepts/4-tier-retrieval","to":"topics/retrieval-hub","type":"part_of","ts":"2026-04-23","confidence":"high"}`
- **`/lint` rule.** Each `part_of` target must be a `topics/<slug>-hub.md`
  OR a `foundations/` page; otherwise re-route to `derived_from` or
  `extends`. No cycles (mereology DAG).

#### 3.2.10 `alpha-ref` (cross-layer #1)
- **Definition.** Wiki entity links to its alpha tracker (W-1 §D.3
  per Sub-agent C §3). The wiki captures conceptual identity; the
  alpha captures operational state; this edge bridges them without
  duplicating state into the wiki (anti-pattern Sub-agent C §8 #2
  "wiki as CRM").
- **Cardinality.** 1:1.
- **Directionality.** Directed (`wiki entity → alpha tracker`).
- **Inverse.** `tracked_by` (stored on the alpha side; not in
  `graph/edges.jsonl`).
- **Allowed `from`.** `entities` (spine), `agents/<expert>/...`
  (Layer 3), `themes/<theme>/...` (Layer 1).
- **Allowed `to`.** `tasks/<task-id>/...` (α-1), `operations/<project-slug>/...`
  (α-4 cycle composite), `swarm/wiki/foundations/swarm-alphas.md`
  (α reference).
- **Cross-layer flag.** **Yes.** Allowed pairs: `(entities|agents|themes) → (tasks|operations|foundations/swarm-alphas)`.
- **Example.** `{"from":"entities/acme-corp","to":"tasks/task-01HF2K3M5N7P9Q","type":"alpha-ref","ts":"2026-04-23","confidence":"high"}`
- **`/lint` rule.** Target `to` MUST exist in `swarm/wiki/tasks/` or
  `swarm/wiki/operations/` or be `swarm/wiki/foundations/swarm-alphas.md`.
  Flag `wiki/entities/<slug>` pages with no `alpha-ref` outgoing if
  they describe an operationally active entity (heuristic: `entity_type
  ∈ {company, product, team}` AND `state ∈ {accepted, referenced}`).

#### 3.2.11 `layer-ref` (cross-layer #2)
- **Definition.** Generic cross-layer link without specific
  semantics. Used when the relationship between layers is one of
  reference (e.g. theme concept → global pattern) but no other
  cross-layer edge fits. Lower priority than `alpha-ref` and
  `cross-tree-ref`; `/lint` advises specifying a more specific edge
  type when possible.
- **Cardinality.** N:M.
- **Directionality.** Directed.
- **Inverse.** `layer-back-ref` (derivative; computed by /build-graph).
- **Allowed `from`/`to`.** Any pair of distinct layers within v3
  (i.e. `from.layer != to.layer`).
- **Cross-layer flag.** **Yes.** All pairs allowed where source and
  target layers differ.
- **Example.** `{"from":"themes/engineering/concepts/clean-code","to":"global/solved-patterns/test-driven-refactor","type":"layer-ref","ts":"2026-04-23","confidence":"medium"}`
- **`/lint` rule.** Surfaces a "consider more specific edge type"
  notice if a more specific edge type's allowed-layer pair matches
  (e.g. if a `layer-ref` runs from a `concept` to a `source`, suggest
  `derived_from`).

#### 3.2.12 `cross-tree-ref` (cross-layer #3)
- **Definition.** v3 `swarm/wiki/` page citing v2 `wiki/` page (Q9
  bridge per Sub-agent A §1 Q9; Sub-agent E §8 cross-ref). **v3 → v2
  only** (no reverse direction allowed; v2 stays untouched per R3).
- **Cardinality.** N:M.
- **Directionality.** Directed (`v3 → v2`).
- **Inverse.** None recorded (v2 doesn't track v3 incoming).
- **Allowed `from`.** Any v3 page (under `swarm/wiki/`).
- **Allowed `to`.** Any v2 page (under `wiki/`).
- **Cross-layer flag.** **Yes — special.** Stored in
  `swarm/wiki/graph/cross-tree.jsonl` (NOT in `edges.jsonl`) per
  T1 + Sub-agent A §1 Q9.
- **Example.** `{"from":"themes/engineering/concepts/clean-code","to":"wiki/concepts/clean-code","type":"cross-tree-ref","ts":"2026-04-23","confidence":"high","note":"v3 distillation cites v2 baseline"}`
- **`/lint` rule.** Reject any record where `to` resolves under
  `swarm/wiki/` (this is intra-v3; use `layer-ref`). Reject any
  record where `from` resolves under v2 `wiki/` (no v2→v3 edges per
  R3). Per-record presence in `cross-tree.jsonl` is mandatory; its
  presence in `edges.jsonl` is forbidden (T1 separation).

### 3.3 Master from-layer × to-layer × allowed-edge-types matrix

Rows = `from` layer; columns = `to` layer. Cells list edge types
permitted for that pair. Empty cell = no allowed edge type (record
rejected by `/lint`).

Layer abbreviations: **S** = spine entity-type (concepts, claims,
sources, ideas, topics, experiments, summaries, foundations,
entities); **L1** = themes; **L2** = brigadier; **L3** = agents;
**L4** = meta/agent-improvements; **L5** = tasks; **L6** =
operations; **L7** = global; **L8** = skills; **L9** = insights;
**v2** = `wiki/`.

| from \ to | S | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | v2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **S**  | extends, contradicts, supports, inspired_by, tested_by, invalidates, supersedes, derived_from, part_of | layer-ref | layer-ref | layer-ref | layer-ref | alpha-ref | alpha-ref | layer-ref | layer-ref | layer-ref | cross-tree-ref |
| **L1** | layer-ref | extends, contradicts, supports, derived_from, part_of, supersedes | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | cross-tree-ref |
| **L2** | layer-ref | layer-ref | extends, supersedes, part_of | layer-ref | layer-ref | alpha-ref | alpha-ref | layer-ref | layer-ref | — | cross-tree-ref |
| **L3** | layer-ref | layer-ref | layer-ref | extends, derived_from, part_of, supersedes | layer-ref | alpha-ref | alpha-ref | layer-ref | layer-ref | — | cross-tree-ref |
| **L4** | layer-ref | layer-ref | layer-ref | layer-ref | extends, supersedes | — | — | layer-ref (`promoted_to`) | layer-ref | — | cross-tree-ref |
| **L5** | derived_from, supports, part_of | — | — | — | — | extends, supersedes, contradicts | layer-ref | — | — | — | — |
| **L6** | layer-ref | — | — | — | — | layer-ref | extends, supersedes, part_of | layer-ref | — | — | cross-tree-ref |
| **L7** | layer-ref | layer-ref | layer-ref | layer-ref | — | — | — | extends, contradicts, supports, supersedes, part_of, derived_from | layer-ref | — | cross-tree-ref |
| **L8** | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | — | — | layer-ref | extends, supersedes, part_of | — | cross-tree-ref |
| **L9** | layer-ref (Phase B) | layer-ref (Phase B) | — | — | — | — | — | layer-ref (Phase B) | — | extends (Phase B) | cross-tree-ref (Phase B) |
| **v2** | — | — | — | — | — | — | — | — | — | — | (intra-v2; not managed by v3) |

**Reading the matrix.** A `from → to` edge is well-formed iff its
`type` appears in the cell at row(from) × col(to). `/lint` rejects
records that violate the matrix.

**Phase-A specifics.** L9 row/column entries marked "(Phase B)" are
forbidden in Phase A — `/lint` rejects them per the
`phase_a_lock: true` field on `swarm/wiki/insights/` per D2 §2.4
(Layer 9 fields).

**Cross-tree storage.** Every cell containing `cross-tree-ref`
records a write to `swarm/wiki/graph/cross-tree.jsonl`, not
`edges.jsonl`. `/build-graph` keeps the two files separate per T1.

### 3.4 Migration plan from v2 edges (572 records)

Sub-agent D §2 audit:
- 233 `part_of` records — already aligned with new enum; no migration.
- 219 `derived_from` records — already aligned; no migration.
- 84 `supports` records — already aligned; no migration.
- 35 `extends` records — already aligned; no migration.
- 1 `contradicts` record — already aligned; no migration.

**No migration required** for the 572 v2 edges. They map 1:1 to the
v3 enum. The 4 declared-but-unused v2 types still in the enum
(`inspired_by`, `tested_by`, `invalidates`, `supersedes`) are
preserved (per R7 locked); v2's edges.jsonl simply contains zero
records of those types and v3 inherits the same. The 5th declared-
but-unused v2 type (`addresses_gap`) is dropped per critic-gate1 H4
reconciliation (zero usage; semantically overlapped by `derived_from`).

**v3 extension types** (`alpha-ref`, `layer-ref`, `cross-tree-ref`)
have zero v2 records by construction (v2 has no Layer-5..L9
structure, no theme structure, no v3 tree to bridge to); they begin
populating during Стадия D + ongoing.

### 3.5 `swarm/wiki/_templates/edge-types.md` file content

The literal content of the template file (Стадия D writes this verbatim):

```markdown
---
title: Edge Type Enum
type: edge-template
layer: spine
state: accepted
confidence: high
last_reviewed: 2026-04-23
sources: [{path: "decisions/WIKI-V3-MECHANICS-2026-04-23.md", range: "216-237"}]
---

# Edge Type Enum (v3)

This file is the SINGLE SOURCE OF TRUTH for typed cross-references in
the v3 wiki. `/build-graph`, `/ingest`, `/lint`, and `/ask` Tier-3
typed-BFS retrieval all read from this enum. Adding or modifying an
edge type requires AWAITING-APPROVAL escalation (D6 §4).

## Storage

- **Intra-v3 edges** → append to `swarm/wiki/graph/edges.jsonl`,
  one JSONL record per line.
- **v3 → v2 cross-tree edges** → append to
  `swarm/wiki/graph/cross-tree.jsonl`, same record shape.
- **Record shape**: `{"from": "<path>", "to": "<path>",
  "type": "<edge-type>", "ts": "YYYY-MM-DD",
  "confidence": "low|medium|high", "note": "<optional>"}`.

## Intra-layer types (10)

(D3 §3.2.1 through §3.2.10 inline content here)

## Cross-layer types (3)

(D3 §3.2.11 through §3.2.13 inline content here)

## From-layer × to-layer × allowed types matrix

(D3 §3.3 table here)
```

### 3.6 Reconciliation with anti-patterns from research

- **Sub-agent C §8 anti-pattern 11 (wikilinks without YAML/edges
  backing).** `/lint` rule §2.2 #5 enforces: every inline `[[type/slug]]`
  produces (a) one `related[]` entry AND (b) one `edges.jsonl` record.
- **Sub-agent C §8 anti-pattern 7 (alpha state without history).** The
  `alpha-ref` edge type explicitly bridges wiki to alpha tracker so
  state mutations record in the alpha's `history.jsonl` (Phase B
  alphas tree); `/lint` flags wiki entity pages that mutate `state`
  without an `alpha-ref` to a tracking alpha.
- **Sub-agent A §1 Q5 (bidirectional `contradicts`).** Honoured in
  §3.2.2 by requiring both directions present.
- **Sub-agent A §1 Q3 (≤1-hop-to-source invariant).** Encoded as a
  /lint rule on §3.2.9 `derived_from`: every `accepted/referenced`
  page MUST have ≥1 `derived_from` OR `supports` edge OR
  `tier: foundation`.

### 3.7 Compatibility matrix vs Tier-1

| Locked item | D3 honours by … |
|---|---|
| Q3 (12-type edge enum) | enumerated 13 types per literal MECHANICS L216–234; flagged the L236 "12" summary as off-by-one. |
| R7 (no wait-and-tune) | All 13 types specified upfront with cardinality + inverse + example + lint rule. |
| Q9 + T1 cross-tree | `cross-tree-ref` (§3.2.13) v3→v2 only; storage in `cross-tree.jsonl`; lint enforces separation. |
| W-12 1000% depth | Per-type spec includes 9 attributes; matrix in §3.3 covers all from×to combinations including v2 boundary; migration plan in §3.4 grounds in v2 audit. |
| Q1 Tier-3 typed BFS | The enum drives the BFS edge-type filter (Sub-agent A §6 #2 shared mechanism). |
| Q5 staleness signal #4 (contradiction-edge integrity) | `contradicts` bidirectional + lint rule for `support/contradiction` ratio. |
| Sub-agent D §2 audit | Migration plan §3.4 matches the 5 in-use types 1:1; no v2 edge requires rewriting. |

---

## DELIVERABLE 4 — Per-Entity-Type Templates (`swarm/wiki/_templates/<type>.md`)

### 4.1 Mandate

For each of the 9 entity types audited by Sub-agent D §1, produce the
v3 template as a literal fenced block + v2→v3 diff table. Стадия D
copies each fenced block verbatim into `swarm/wiki/_templates/<type>.md`.

The frontmatter follows D2 §2.2 (cross-layer required fields) + D2
§2.3 (per-entity-type additions). Body follows v2 conventions where
applicable; new sections are added to wire the v3 alpha-state fields
and the §5.5.5 provenance gate (D6 §2). Every template ends with an
"Edges" section enumerating the wikilinks that map to `edges.jsonl`
records (per Q3 triple-channel rule, D2 §2.2 lint #5).

`<placeholder>` syntax: angle-bracket tokens are filled in by /ingest
(or by the brigadier on manual creation). Lists default to `[]`; lines
prefixed with `# ` are author-facing comments to be removed when the
template is filled.

### 4.2 `swarm/wiki/_templates/concept.md`

```markdown
---
id: concept-<kebab-slug>
title: <concept name>
type: concept
layer: spine
niche: <personal|business|sales|life|tech|meta>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
last_reviewed:
pipeline: ingested
state: drafted
confidence: medium
confidence_method:
tier: core
produced_by: <agent>-<mode>
derived_from:
sources: []
related: []
topics: []
tags: []
provenance_inline: true
definition: <one-line definition, ≤200 chars>
examples: []
extends:
---

# <Title>

## Суть в одной строке
<concise gist, ≤120 chars>

## Определение
<formal definition, with [src:path#section] inline citations>

## Ключевые свойства
- <property 1>
- <property 2>

## Применимость
<contexts where this concept holds>

## Связи
- Расширяет: <`[[concepts/parent-concept]]`>
- Поддерживает: <`[[claims/relevant-claim]]`>
- Противоречит: <`[[claims/opposing-claim]]`>

## Provenance
<inline-citation map per §5.5.5; one [src:path] per non-trivial paragraph>

## Edges
- `[[concepts/<other-concept>]]` (extends) → `edges.jsonl`
- `[[sources/<source-slug>]]` (derived_from) → `edges.jsonl`

## Источники
<explicit list mirroring sources[] frontmatter>
```

**v2 → v3 diff:**

| Field/section | v2 | v3 | Reason |
|---|---|---|---|
| Frontmatter `id` | absent | added (kebab-slug `<type>-<slug>`) | D2 cross-layer required; uniqueness for graph anchor |
| Frontmatter `layer` | absent | added (`spine`) | D2 cross-layer; drives Q4 task-context filter |
| Frontmatter `state` | absent | added (`drafted` default) | D2 + α-2 lifecycle (FPF Part 4) |
| Frontmatter `tier` | absent | added (`core` default) | 24-Lock 13 + master synthesis §5.5.4 |
| Frontmatter `produced_by` | absent | added | master synthesis §5.5.3 + matrix 5×4 attribution |
| Frontmatter `definition`/`examples`/`extends` | inferred from body | hoisted to frontmatter | D2 §2.3 concepts-specific schema; queryable without parsing body |
| Frontmatter `provenance_inline: true` | absent | added | enforces §5.5.5 inline citation rule per D6 §2 |
| Body "Provenance" section | absent | added | new — explicit citation map per §5.5.5 |
| Body "Edges" section | absent | added | mirrors edges.jsonl records per Q3 channel C |
| Body "Источники" | last section, free-form | retained, mirrors sources[] | preserved for human readability |

### 4.3 `swarm/wiki/_templates/entity.md`

```markdown
---
id: entity-<kebab-slug>
title: <entity name>
type: entity
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: ingested
state: drafted
confidence: medium
tier: core
produced_by: <agent>-<mode>
sources: []
related: []
topics: []
tags: []
provenance_inline: true
entity_type: <person|company|product|team|event|place>
external_ids:
  notion:
  linkedin:
  github:
  hubspot:
---

# <Title>

## Кто/что это
<one-paragraph identification>

## Контекст
<who/what/where/when>

## Факты
- <fact 1> [src:path#section]
- <fact 2>

## Связи
- Tracked by alpha: <`[[tasks/<task-id>]]`> via `alpha-ref`
- Related concept: <`[[concepts/<slug>]]`>

## История взаимодействий
<chronological log of interactions; rotates at 30 entries to _archive/>

## Provenance
<§5.5.5 inline citation map>

## Edges
- `[[<task-or-operation-id>]]` (alpha-ref) → `edges.jsonl`

## Источники
```

**v2 → v3 diff:**

| Field/section | v2 | v3 | Reason |
|---|---|---|---|
| `entity_kind` (v2) | enum string | renamed `entity_type` | D2 §2.3 (alignment with v3 frontmatter naming) |
| `external_ids` | absent | added (yaml-block) | bridges to Notion/LinkedIn/GitHub/HubSpot per CLAUDE.md "Key Notion IDs" pattern |
| Body "Связи" — alpha-ref | absent | added | anti-pattern Sub-agent C §8 #2 (avoid wiki-as-CRM); alpha tracks state |
| Body "История" rotation | implicit | explicit (>30 → _archive/) | global.md §"Логи" rule applied to per-entity history |

### 4.4 `swarm/wiki/_templates/source.md`

```markdown
---
id: source-<kebab-slug>
title: <source title>
type: source
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: raw
state: drafted
confidence: high
tier: core
produced_by: /ingest
captured_by: /ingest
captured_date: <YYYY-MM-DD>
sources: []
related: []
topics: []
tags: []
source_type: <article|book|podcast|video|meeting|voice-memo|transcript|web|paper>
url:
local_path:
author:
ingested_date: <YYYY-MM-DD>
coverage: []
---

# <Title>

## TL;DR
<3–5 bullet summary>

## Summary
<longer prose summary, with [src:path#section] back to local_path or url>

## Ключевые цитаты
> "<verbatim quote>" — [src:local_path#L42-L48]

## Что извлекли
- <distilled insight 1, paired with `[[concepts/<slug>]]`>
- <distilled insight 2, paired with `[[claims/<slug>]]`>

## Provenance
<§5.5.5 — sources[] non-empty (this page IS a source); pipeline begins at `raw`>

## Edges
- `[[concepts/<slug>]]` (derived_from inverse — sources are pointed to BY concepts via derived_from)

## Сырое
<location of raw file under raw/; pointer only, not body content>
```

**v2 → v3 diff:**

| Field/section | v2 | v3 | Reason |
|---|---|---|---|
| `source_kind` (v2) | string | renamed `source_type` | D2 alignment |
| `raw_file` (v2) | string | renamed `local_path` | D2 alignment + clearer semantics |
| `coverage` | absent | added (list of `[[topics/slug]]`) | feeds Q1 Tier 2 grep + Tier 3 BFS seeds |
| `ingested_date` | v2 `captured` | renamed `ingested_date` (v2 `captured` retained as `captured_date`) | per BUILD §2.2 explicit `captured_by`/`captured_date` schema |
| Body "Мета" section | present (often empty) | dropped | Sub-agent D §1.1 deadweight call |
| Body "Сырое" section | present | retained as pointer-only | content lives in raw/, not duplicated |

### 4.5 `swarm/wiki/_templates/claim.md`

```markdown
---
id: claim-<kebab-slug>
title: <claim assertion>
type: claim
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
last_reviewed:
pipeline: ingested
state: drafted
confidence: medium
confidence_method:
tier: core
produced_by: <agent>-<mode>
sources: []
related: []
topics: []
tags: []
stance: asserted
support_count: 0
contradiction_count: 0
support_edges: []
contradiction_edges: []
falsifier: <one-sentence falsifier — what evidence would refute this claim>
---

# <Title>

## Точная формулировка
<the claim, single sentence, falsifiable>

## Контекст
<scope, conditions, who is making it>

## Аргументы за
- <evidence 1> [src:path#section] — `[[sources/<slug>]]` supports
- <evidence 2>

## Аргументы против
- <counter-evidence 1> — `[[claims/<slug>]]` contradicts

## Что опровергнуло бы это утверждение
<verbatim from `falsifier:` frontmatter; mirrors v2 explicit-falsifier discipline>

## Связи
- Поддерживается: <`[[sources/<slug>]]`> (supports edge in `edges.jsonl`)
- Противоречит: <`[[claims/<slug>]]`> (bidirectional contradicts)
- Тестируется: <`[[experiments/<slug>]]`> (tested_by)

## Provenance
<§5.5.5 inline citation map; pipeline ≠ raw → sources[] required>

## Edges
- `[[sources/<slug>]]` (supports) → `edges.jsonl`
- `[[claims/<slug>]]` (contradicts) → `edges.jsonl` (BOTH directions written)
- `[[experiments/<slug>]]` (tested_by) → `edges.jsonl`
```

**v2 → v3 diff:**

| Field/section | v2 | v3 | Reason |
|---|---|---|---|
| `stance` | v2 enum (asserted/supported/contested/refuted) | retained verbatim | v2 audit Sub-agent D §1.4 |
| `support_count`, `contradiction_count` | absent | derivative fields added | populated by `/build-graph`; feeds D10 health metrics |
| `support_edges`, `contradiction_edges` | absent | added (lists) | Q3 channel A; reciprocal of edges.jsonl |
| `falsifier` | inferred from body section | hoisted to frontmatter | enables `/lint` non-empty falsifier validation |
| Body "Что опровергнуло бы это утверждение" | present | retained, mirrors `falsifier:` field | preserves v2 epistemic discipline |
| Body "Edges" section | absent | added | Q3 channel C explicit |

### 4.6 `swarm/wiki/_templates/idea.md`

```markdown
---
id: idea-<kebab-slug>
title: <idea name>
type: idea
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: raw
state: drafted
confidence: low
tier: core
produced_by: <agent>-<mode>
sources: []
related: []
topics: []
tags: []
proposed_by: <agent or human>
routing_target:
idea_status: raw
---

# <Title>

## Одна строка
<the idea, ≤120 chars>

## Обоснование
<why this is worth considering>

## Предполагаемый эффект
<concrete expected impact>

## Что уже известно/проверено
<existing evidence, with [src:path] citations if any>

## Следующий шаг
<routing_target action; e.g. "schedule experiment", "write claim", "skill candidate", "drop">

## Связи
- Inspired by: <`[[ideas/<slug>]]`> (inspired_by)
- Related concept: <`[[concepts/<slug>]]`>

## Provenance
<§5.5.5 — for `state: drafted, pipeline: raw` ideas, sources[] may be empty;
gate enforces non-empty only at `state: accepted` per D6 §2>

## Edges
- `[[ideas/<slug>]]` (inspired_by) → `edges.jsonl`
```

**v2 → v3 diff:**

| Field/section | v2 | v3 | Reason |
|---|---|---|---|
| `status` (v2: raw/evaluated/planned/in-progress/shipped/dropped) | retained as `idea_status` | renamed to disambiguate from cross-layer `state` (α-2) | D2 §2.3 |
| `proposed_by` | absent (implicit from agent context) | hoisted to frontmatter | accountability + idea routing |
| `routing_target` | absent | added | drives idea → next-stage promotion (skill candidate per Q6, etc.) |
| Default `confidence` | low | retained | v2 idea.md (Sub-agent D §1.5) |

### 4.7 `swarm/wiki/_templates/topic.md`

```markdown
---
id: topic-<kebab-slug>
title: <topic name>
type: topic
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: ingested
state: drafted
confidence: medium
tier: core
produced_by: <agent>-<mode>
sources: []
related: []
topics: []
tags: [#type/topic]
MOC_for: []
---

# <Title>

## Зачем эта тема
<motivation; ≤200 chars>

## Основные концепции
- `[[concepts/<slug>]]`
- `[[concepts/<slug>]]`

## Ключевые сущности
- `[[entities/<slug>]]`

## Открытые вопросы
- <Q1>
- <Q2>

## Смежные темы
- `[[topics/<slug>]]` (related_to / part_of)

## Provenance
<§5.5.5; topics often aggregate without primary sources — `sources[]` may
list canonical references>

## Edges
- `[[concepts/<slug>]]` (part_of) — children via reciprocal edge
- `[[topics/<slug>]]` (layer-ref or related_to)
```

**v2 → v3 diff:**

| Field/section | v2 | v3 | Reason |
|---|---|---|---|
| `MOC_for` | absent | added (list) | when this topic acts as Map-of-Content for entities, /ask uses it for Tier 2 retrieval (D2 §2.3) |
| Naming convention | `<slug>.md` | adds `<slug>-hub.md` when `MOC_for` non-empty | matches v2 hub pattern (`system-design-hub.md`) per Sub-agent D §1.6 |

### 4.8 `swarm/wiki/_templates/experiment.md`

```markdown
---
id: experiment-<kebab-slug>
title: <experiment title>
type: experiment
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: ingested
state: drafted
confidence: medium
tier: core
produced_by: <agent>-<mode>
cycle_id: cyc-<kebab-slug>
sources: []
related: []
topics: []
tags: []
hypothesis: <falsifiable claim, ≤500 chars>
start_date: <YYYY-MM-DD>
end_date:
outcome: open
---

# <Title>

## Гипотеза
<verbatim from `hypothesis:` frontmatter>

## Дизайн
- IV (independent variable):
- DV (dependent variable):
- Control:
- Duration:

## Что делаем
<procedure>

## Результат
<observed; populated when outcome ≠ open>

## Выводы
<interpretation; cites supporting evidence>

## Связи
- Tests claim: `[[claims/<slug>]]` (tested_by inverse)
- Invalidates / supports: <as outcome warrants>

## Provenance
<§5.5.5; experiments are themselves source-class artefacts after closure>

## Edges
- `[[claims/<slug>]]` (tests; inverse of tested_by)
- `[[claims/<slug>]]` (invalidates) — when outcome=lost
```

**v2 → v3 diff:**

| Field/section | v2 | v3 | Reason |
|---|---|---|---|
| `status` (v2: planned/running/done/aborted) | renamed `outcome` (open/won/lost/aborted) | extends with won/lost semantics for α-3 strategy `validated` transitions | D2 §2.3 |
| `cycle_id` | absent | added (required) | ties experiment to α-4 cycle; feeds D10 cycle-close-rate |
| `hypothesis` | inferred from body | hoisted to frontmatter | enables /lint non-empty hypothesis validation |
| `started`, `ended` | renamed `start_date`, `end_date` | naming alignment with v3 conventions | minor |

### 4.9 `swarm/wiki/_templates/summary.md`

```markdown
---
id: summary-<kebab-slug>
title: <summary title>
type: summary
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
pipeline: compiled
state: drafted
confidence: medium
tier: core
produced_by: /build-graph
cycle_id: cyc-<kebab-slug>
sources: []
related: []
topics: []
tags: []
summary_window: <daily|weekly|topic|cluster>
community_id:
covers: []
---

# <Title>

## TL;DR
<3–5 bullet summary>

## Ключевые выводы
- <key takeaway 1> [src:`[[<page>]]`]
- <key takeaway 2>

## Что изменилось/появилось
<delta vs prior summary in same window>

## Что ещё открыто
<open questions surfaced during aggregation>

## Входные страницы
<verbatim from `covers:` frontmatter>

## Provenance
<§5.5.5 — sources[] = the union of `covers[]` pages' sources>

## Edges
- `[[<covered-page>]]` (part_of-inverse — summary aggregates these)
```

**v2 → v3 diff:**

| Field/section | v2 | v3 | Reason |
|---|---|---|---|
| `scope` (v2 enum) | renamed `summary_window` | clearer semantics | D2 §2.3 |
| `community_id` | absent | added | feeds Layer-9 cross-theme metric input per D10 |
| `covers[]` | retained | required (non-empty) | provenance — what this summary aggregates |
| `cycle_id` | absent | added (required) | summaries are cycle-bound artefacts |

### 4.10 `swarm/wiki/_templates/foundation.md`

```markdown
---
id: foundation-<kebab-slug>
title: <foundation principle>
type: foundation
layer: spine
niche: <…>
created: <YYYY-MM-DD>
last_modified: <YYYY-MM-DD>
last_reviewed: <YYYY-MM-DD>     # required per Q5 365-day re-review
pipeline: linted
state: accepted                 # foundations enter at `accepted`
confidence: high
confidence_method: ruslan-attested
tier: core
produced_by: brigadier
sources: []
related: []
topics: []
tags: [#type/foundation]
binding_scope: swarm-wide      # or theme:<theme> | expert:<expert>
supersedes_versions: []
---

# <Title>

## Принцип
<the foundation, single decisive statement>

## Почему принимается
<rationale; 1–3 paragraphs with [src:path#section] citations>

## Что из этого следует
- <consequence 1>
- <consequence 2>

## Когда сомневаться
<conditions under which this foundation should be revisited>

## Связи
- Supersedes: <`[[foundations/<v2-slug>@v1]]`> (supersedes edge)
- Tested by: <`[[experiments/<slug>]]`>
- Тестируется: list of experiments referencing this

## Provenance
<§5.5.5 — foundations require ≥1 source AND ruslan-attested confidence_method,
OR brigadier-attested with ≥3 supports>

## Edges
- `[[foundations/<slug>@v<N-1>]]` (supersedes) → `edges.jsonl`
```

**v2 → v3 diff:**

| Field/section | v2 | v3 | Reason |
|---|---|---|---|
| `binding_scope` | absent | added (required) | D2 §2.3 — foundations may be theme-scoped or swarm-wide |
| `supersedes_versions[]` | absent | added | tracks supersession chain |
| Default `confidence` | high | retained | v2 (Sub-agent D §1.9) |
| Default `state` | drafted (cross-layer default) | overridden to `accepted` | foundations are by definition the brigadier's accepted axioms |
| `confidence_method: ruslan-attested` (or brigadier-attested) | absent | added | foundations require explicit attribution |

### 4.11 `swarm/wiki/_templates/<entity-template-set-summary>`

The 9 templates above are the complete set. Стадия D writes each
fenced block above to its named path under `swarm/wiki/_templates/`.
The 10th template file (`edge-types.md`) was specified in D3 §3.5.
Total: 10 template files in `swarm/wiki/_templates/`.

### 4.12 Compatibility matrix

| Locked item | D4 honours by … |
|---|---|
| W-12 1000% depth | Each template specifies frontmatter (D2-derived), body sections (v2-derived + v3-extended), provenance map, edges section. |
| Q3 triple-channel | Every template has `related[]` (channel A), inline `[[<type>/<slug>]]` (channel B), and explicit "Edges" section mirroring `edges.jsonl` records (channel C). |
| Q5 staleness signals | `last_reviewed` required on `foundations/`; `falsifier` required on claims; bidirectional `contradicts` edges (D3 §3.2.2). |
| §5.5.5 provenance gate | Every template has a "Provenance" section + frontmatter `sources[]`; D6 §2 enforces gate semantics. |
| FPF Part 4 α-2 lifecycle | Every template has `state` field; default per template type (foundation defaults to `accepted`; sources to `drafted` with `pipeline: raw`). |
| Sub-agent D §7 transplant table | All 9 v2 templates transplanted with field renames + extensions; deadweight removed (`Мета` in source.md). |
| R3 v2 untouched, v3 added | v2 templates remain at `wiki/_templates/`; v3 templates **copied** (not symlinked) to `swarm/wiki/_templates/` per Q9 R3. |

---

## DELIVERABLE 5 — `swarm/wiki/foundations/swarm-alphas.md` (5 swarm-alpha state machines)

### 5.1 Mandate, naming reconciliation, and citation map

This file is the **runtime constitution** every domain expert reads on
every Task invocation (per FPF Part 10.4 mandate, Sub-agent B §6).
The 5 swarm-alphas (α-1 Task / α-2 Artefact / α-3 Strategies-Rule /
α-4 Cycle / α-5 Direction) are locked in identity/scope/high-level
purpose per FPF Part 4 (Sub-agent B §1–§5). This deliverable
materialises their **state graphs, transitions, movers, and
acceptance predicates** — the missing operational substrate.

**State-name reconciliation.** Sub-agent B §2/§3/§4 surfaced
discrepancies between FPF Part 4's verbatim state sets and the
prompt §6 D5 "minimum state set." This deliverable adopts **FPF Part
4 verbatim states as canonical** (locked Tier-1 source per prompt
§2 prohibition on re-opening alpha identity) and provides explicit
**alias maps** to the prompt's prescribed names where they differ.
This honours both the FPF lock and the spec's reading convenience.
Two extensions are introduced:
- α-2 Artefact gains an 8th state `tombstoned` (per D2 §2.1 dual-axis
  + Sub-agent C §8 anti-pattern 9). FPF Part 4 silent on this
  (Sub-agent B §2 gap-flag); spec specifies the transition mover
  (brigadier or meta-agent-via-task) and predicate.
- α-1 Task `gated → rejected → returned` mover (Sub-agent B §1
  gap-flag) is specified here: HITL emits a rejection note in
  `swarm/gates/AWAITING-APPROVAL-<task-id>-rejection.md`; brigadier
  parses, moves α-1 to `returned`, archives.

The FPF mandate (Part 10.4) requires α-1..α-4 machine-tracked Phase
A; α-5 human-owned with lightweight (state-enum-only) Phase A
implementation. α-5's full NQD-CAL formalization is deferred to
Phase B per Part 10.6.

### 5.2 α-1 Task

**Identity (verbatim, FPF Part 4 §4.1).** "Represents a user request
entering the swarm." Scope: every inbound user request the brigadier
intakes; runs from submission to archival.

**State graph** (FPF Part 4 verbatim + spec gap-fill):

| State | Definition (FPF or spec) |
|---|---|
| `submitted` | User request received, not yet read by brigadier. |
| `intaked` | Brigadier has read the request, classified niche, assigned `task_id`. |
| `decomposed` | CE 40/10/40/10 budget assigned + matrix cells selected + AP declared. |
| `dispatched` | ≥1 `Task()` invocation issued to a cell. |
| `integrated` | All invoked cells returned + dissents preserved. |
| `gated` | AWAITING-APPROVAL file with 4-response template exists in `swarm/gates/`. |
| `approved` | HITL reply parsed (acked). |
| `compounded` | ≥0 rules appended to strategies.md (zero is valid per FPF B §1). |
| `archived` | `swarm/logs/<cycle-id>/cycle-log.md` written + per-task dir marked `alpha_state: archived`. |
| `refused` | Brigadier refuses intake (out-of-scope, malformed, capacity). |
| `rejected` | HITL rejected at `gated` step. |
| `returned` | Task returned to user with rationale (terminal failure branch). |

**Transitions table:**

| from | to | trigger | mover (role) | side-effects on filesystem |
|---|---|---|---|---|
| `submitted` | `intaked` | brigadier reads + classifies | brigadier | `swarm/wiki/tasks/<task-id>/` dir created; `open-questions.md` initialised. |
| `submitted` | `refused` | out-of-scope / malformed | brigadier | `swarm/gates/refused-<task-id>.md` written; no tasks/ dir. |
| `intaked` | `decomposed` | brigadier writes decomposition (BUILD §3) | brigadier | `swarm/wiki/proposals/<task-id>-decomposition.md` written. |
| `decomposed` | `dispatched` | first `Task(...)` invoked | brigadier | log line in `swarm/logs/<cycle-id>.md`. |
| `dispatched` | `integrated` | all expected returns received | brigadier (writes integrate) | `swarm/wiki/tasks/<task-id>/artefacts/` populated; dissents preserved as separate files. |
| `integrated` | `gated` | brigadier writes AWAITING-APPROVAL packet | brigadier | `swarm/gates/AWAITING-APPROVAL-<task-id>-<slug>.md` with 4-response template (D6 §4). |
| `gated` | `approved` | HITL ack parsed | HITL (Ruslan) | `swarm/gates/<task-id>-ack.md` appended; brigadier parses on next sweep. |
| `gated` | `rejected` | HITL rejects | HITL | `swarm/gates/<task-id>-rejection.md` written with reason. |
| `rejected` | `returned` | brigadier composes return note | brigadier | `swarm/wiki/tasks/<task-id>/decisions/<ts>-returned.md`. |
| `approved` | `compounded` | brigadier runs compound step | brigadier | `agents/<expert>/strategies.md` appended (Level-1) and/or `swarm/wiki/meta/agent-improvements/` (Level-2) per W-5. |
| `compounded` | `archived` | brigadier writes cycle-log | brigadier | `swarm/wiki/tasks/<task-id>/decisions/<ts>-archived.md`; entry in `swarm/wiki/log.md`. |

**Acceptance predicates per state** (testable from filesystem alone):

- `intaked`: `swarm/wiki/tasks/<task-id>/open-questions.md` exists; frontmatter `alpha_state: intaked`.
- `decomposed`: `proposals/<task-id>-decomposition.md` exists with `decomposition:` yaml-block listing ≥1 cell.
- `dispatched`: ≥1 line in `swarm/logs/<cycle-id>.md` matching `Task(<expert>-<mode>)` for this `task-id`.
- `integrated`: every cell in the decomposition has a corresponding artefact in `swarm/wiki/tasks/<task-id>/artefacts/`.
- `gated`: file matching `swarm/gates/AWAITING-APPROVAL-<task-id>-*.md` exists with `4-response template` section.
- `approved`: file matching `swarm/gates/<task-id>-ack.md` exists with `acked: true` field.
- `compounded`: marker file `swarm/wiki/tasks/<task-id>/decisions/<YYYY-MM-DD-HHMM>-compounded.md` exists with frontmatter `task_id: <task-id>` AND zero-or-more new entries appended to `agents/<expert>/strategies.md` (with `task_id: <task-id>` in entry frontmatter — append-only YAML-block-per-entry; zero new entries is valid per FPF B §1).
- `archived`: `swarm/logs/<cycle-id>/cycle-log.md` exists AND `swarm/wiki/log.md` contains a line `## [<date>] task-archived | <task-id>`.

**Cross-alpha integrations.** α-1 is consumed inside α-4 Cycle (one
task = one cycle iteration). α-2 Artefact instances are created
during `dispatched → integrated`. α-3 Strategies-Rule entries are
emitted at `compounded`.

**ASCII state diagram:**

```
                  ┌──────────┐
                  │submitted │
                  └────┬─────┘
                       │ brigadier-read
                  ┌────▼─────┐  refuse  ┌─────────┐
                  │ intaked  ├─────────►│ refused │
                  └────┬─────┘          └────┬────┘
            decompose  │                     │ → returned (terminal)
                  ┌────▼──────┐
                  │decomposed │
                  └────┬──────┘
              dispatch │
                  ┌────▼──────┐
                  │dispatched │
                  └────┬──────┘
            integrate  │
                  ┌────▼──────┐
                  │integrated │
                  └────┬──────┘
                  brigadier writes gate packet
                  ┌────▼──────┐  HITL reject  ┌─────────┐
                  │  gated    ├──────────────►│ rejected├──►┌──────────┐
                  └────┬──────┘               └─────────┘   │ returned │
                  HITL ack │                                 └──────────┘
                  ┌────▼──────┐
                  │ approved  │
                  └────┬──────┘
            compound  │
                  ┌────▼──────┐
                  │compounded │
                  └────┬──────┘
                       │
                  ┌────▼──────┐
                  │ archived  │   (terminal success)
                  └───────────┘
```

### 5.3 α-2 Artefact

**Identity (verbatim, FPF Part 4 §4.2).** "Each artefact a cell
produces into `swarm/wiki/`." Scope: every wiki/swarm artefact
produced by a cell.

**State graph** (FPF verbatim + spec extension `tombstoned`):

| State | Definition |
|---|---|
| `drafted` | Cell wrote artefact to `swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md` with valid §5.5.5 frontmatter. |
| `reviewed` | ≥1 critic pass + Conformance Checklist ticked (FPF B §1 §5.2). |
| `revised` | Producer or integrator made changes after `reviewed`. Loop allowed: `revised ↔ reviewed`. |
| `accepted` | Integrator + brigadier sign-off; brigadier wrote canonical artefact under `swarm/wiki/<canonical-path>/`. |
| `referenced` | Appears in another artefact's `consumes:` (i.e. cited by ≥1 downstream `accepted` artefact). |
| `superseded` | A newer artefact bears `supersedes: [[<this>]]` and is `accepted`. |
| `retired` | Legitimate end-of-life: artefact no longer applies but was historically valid (preserved for audit). |
| `tombstoned` | **Spec extension.** Artefact invalidated/withdrawn (e.g. caused incident; refuted by experiment). Distinct from `retired`. Anti-pattern Sub-agent C §8 #9 "never delete, only archive" — `_archive/` retains tombstoned content. |

**Transitions table:**

| from | to | trigger | mover | side-effects |
|---|---|---|---|---|
| (none) | `drafted` | cell writes draft | cell (`expert-direct (drafts only)`) | file in `swarm/wiki/drafts/...`. |
| `drafted` | `reviewed` | critic returns Conformance Checklist | integrator OR critic-mode cell | comment thread or critique file in same task dir. |
| `reviewed` | `revised` | producer/integrator edits | producer OR integrator | file in `drafts/` updated. |
| `revised` | `reviewed` | re-critique | critic-mode cell | loop. |
| `reviewed` | `accepted` | brigadier passes §5.5.5 gate | brigadier (single-writer) | brigadier writes canonical at `swarm/wiki/<canonical>/<slug>.md`; commits with `[<agent>] <cycle>: <description>` per §5.9. |
| `accepted` | `referenced` | another `accepted` artefact `consumes:` this | brigadier (writes the consumer) | edge added to `graph/edges.jsonl`. |
| `accepted` | `superseded` | newer accepted artefact `supersedes:` this | brigadier | `state: superseded`; `superseded_by: [[<new>]]` in frontmatter; bidirectional `supersedes` edge. |
| `accepted`/`superseded` | `retired` | brigadier or meta-agent-via-task identifies legitimate EOL | brigadier (after meta-agent draft per Q2-Q6 reconciliation) | `state: retired`; not deleted. |
| {`accepted`, `referenced`, `superseded`, `retired`} | `tombstoned` | invalidated by `invalidates` edge (D3 §3.2.6) OR Ruslan-attested withdrawal via gate file | brigadier (sole writer; meta-agent or any expert may draft the rationale via `mode: writing-support` per D6 §6.8; brigadier verifies §5.5.5 then writes) | (a) For `invalidates` path: brigadier moves file to `swarm/wiki/_archive/<original-path>`; appends `tombstoned_by: [[<invalidating-page>]]` to frontmatter. (b) For Ruslan-attested path: a gate file `swarm/gates/AWAITING-APPROVAL-tombstone-<page-id>-<YYYY-MM-DD>.md` per D6 §6.5 must be acked first; on ack, brigadier executes the same move + tombstoned_by recording. **Forbidden: `drafted → tombstoned`** (a draft in `swarm/wiki/drafts/` that never reached `accepted` is simply deleted from drafts/ — no archival, no tombstone). |

**Acceptance predicates per state:**

- `drafted`: file exists in `swarm/wiki/drafts/...`; frontmatter valid (§5.5.3).
- `reviewed`: file's frontmatter has `reviewed_by: <integrator-or-critic>` OR critique file exists in same dir.
- `accepted`: file at canonical path; `state: accepted`; integrator + brigadier sign-off implicit in commit metadata (commit author = brigadier).
- `referenced`: ≥1 incoming edge in `graph/edges.jsonl` from another `state: accepted` page.
- `superseded`: `superseded_by: [[<page>]]` non-empty; the named page is `state: accepted`.
- `retired`: `state: retired`; no `superseded_by` (else use that).
- `tombstoned`: file lives under `swarm/wiki/_archive/<original-path>`; `tombstoned_by:` non-empty AND points to either an `invalidates`-edge source page OR a Ruslan-acked gate file under `swarm/gates/`. Original canonical path absent (no resurrection without explicit un-tombstone gate).

**Cross-alpha integrations.** α-2 is created inside α-1 `dispatched →
integrated`. α-2 `accepted` transition is the matrix gate-passage per
FPF Part 4 §4.2 ("stage-gate transitions in the 5×4 matrix ARE
alpha-state transitions ... this makes gate passage
machine-verifiable"). α-3 strategy entries cite α-2 artefacts.

**ASCII state diagram:**

```
                       ┌──────────┐
       cell writes ───►│ drafted  │
                       └────┬─────┘
                       ┌────▼─────┐  edits  ┌─────────┐
                       │reviewed  │◄────────┤ revised │
                       └────┬─────┘  loop   └─────────┘
              brigadier  ┌──┴──┐
              §5.5.5     │     │ tombstone (any state)
                         ▼     ▼
                       ┌──────────┐                ┌────────────┐
                       │ accepted │                │ tombstoned │
                       └────┬─────┘                └────────────┘
              consumed    ┌─┴─┐
                          │   │ supersedes
                          ▼   ▼
                ┌──────────────┐  ┌────────────┐
                │ referenced   │  │ superseded │
                └──────┬───────┘  └─────┬──────┘
                       │                │
                       │ EOL            │ EOL
                       ▼                ▼
                       ┌──────────────────┐
                       │     retired      │
                       └──────────────────┘
```

### 5.4 α-3 Strategies-Rule

**Identity (verbatim, FPF Part 4 §4.3).** "Each entry in
strategies.md." Governs the skill-learning pipeline (Q6).

**State graph** (FPF Part 4 §4.3 verbatim — 4 states only):

| FPF state | Spec alias (per prompt §6 D5) | Definition |
|---|---|---|
| `proposed` | `candidate` | 4-part DRR format submitted (context/decision/alternatives/review-checkpoint). |
| `active` | `learning` | At least 1 successful application; under golden-set evaluation. |
| `validated` | `active` | ✓/✗ ratio ≥ 3:1 over ≥10 uses; promoted out of learning into the live skill registry. |
| `tombstoned` | `tombstoned` | Ratio < 1:1 cumulative OR explicit Ruslan-retirement OR caused production incident OR superseded by another skill (graceful supersession also tombstones the prior; the new active skill carries `supersedes:` edge per D3 §3.2.7). |

**Canonical = FPF names.** Spec aliases are documented for cross-
referencing the prompt's prescribed naming, but the wiki, /lint, and
/build-graph all use FPF names. D11 (Gate 2) provides the activation
rubric using FPF names + spec aliases together.

**Deviation from prompt §6 D5.** The prompt prescribed a 5-state spec
set including `retired`. FPF Part 4 §4.3 locks α-3 to 4 states (no
separate `retired`). Per prompt §2 prohibition on re-opening locked
alpha identity, FPF wins; `retired` is dropped from α-3. Graceful
supersession is captured via the `tombstoned` transition with
`supersedes:` edge to the successor (so audit history is preserved
in `_archive/` per Sub-agent C §8 anti-pattern 9).

**Transitions table:**

| FPF from | FPF to | trigger | mover | side-effects |
|---|---|---|---|---|
| (none) | `proposed` | brigadier compound-step writes DRR | brigadier | append to `agents/<expert>/strategies.md` (Level-1) OR `swarm/wiki/skills/candidates/<slug>/manifest.md` (Level-2). |
| `proposed` | `active` | first successful cell-use | brigadier (records in `usage/<slug>.jsonl`) | file moves from `candidates/` to `learning/`; `skill_state: learning`. |
| `active` | `validated` | golden-set ≥3 + ≥10 uses + ✓/✗ ≥3:1 (D11) | brigadier (after meta-agent audit-via-task) | file moves from `learning/` to `active/`; D9 symlink created `.claude/skills/<slug>.md → swarm/wiki/skills/active/<slug>.md`. |
| `validated` | `active` | ratio drops to 1:1≤ ratio <3:1 (demoted) | meta-agent-via-task | file moves back to `learning/`; symlink removed. |
| `validated` | `active` (demoted) | success ratio drops to `1:1 ≤ ratio < 3:1` over rolling 10 uses | meta-agent-via-task → brigadier writes | file moves back to `learning/`; symlink removed; the loop allows recovery. |
| any | `tombstoned` | success ratio drops <1:1 cumulative OR explicit Ruslan retire OR superseded by another active skill OR caused production incident | brigadier (Ruslan can unilaterally trigger; meta-agent emits draft for non-incident cases) | file moves to `swarm/wiki/_archive/`; symlink removed; `tombstoned_by:` recorded; if superseded, write `supersedes:` edge from the successor (D3 §3.2.7). |

**Acceptance predicates per state:**

- `proposed`: frontmatter `skill_state: candidate`; DRR fields populated; file under `swarm/wiki/skills/candidates/<slug>/manifest.md` OR appended in `agents/<expert>/strategies.md` with `skill_state: candidate`.
- `active` (FPF) / `learning` (alias): file under `swarm/wiki/skills/learning/<slug>/`; `golden-set.jsonl` exists with ≥3 cases (per D11).
- `validated` (FPF) / `active` (alias): file at `swarm/wiki/skills/active/<slug>.md`; `n_uses ≥ 10` AND `success_count / loss_count ≥ 3`; D9 symlink active.
- `tombstoned`: file under `swarm/wiki/_archive/skills/<slug>.md`; symlink absent; `tombstoned_by:` non-empty (cause: incident-link, Ruslan-attestation, or successor `supersedes:` edge).

**Cross-alpha integrations.** α-3 entries are emitted at α-1
`compounded`. α-3 `validated` transition is the formal Q6 activation
rubric (D11 Gate 2). α-3 success/loss counts are derived from
per-skill `usage/<slug>.jsonl` (event-sourced per Sub-agent C §5).

**Owner per FPF Part 4 §4.3:** "meta-agent for tombstoning audit;
brigadier for writes." Reconciled with Q2 single-writer (Sub-agent A
§6 #10): meta-agent emits a draft via Task `mode: writing-support`;
brigadier evaluates the §5.5.5 gate; brigadier commits.

**ASCII diagram (FPF 4-state):**

```
                                 ┌──────────┐
              brigadier compound │ proposed │
              step writes DRR    │(candidate│ ──┐
                                 └─────┬────┘   │
                          first use   │         │
                                 ┌─────▼────┐   │
                                 │ active   │ ◄─┤  loop: demote
                                 │(learning │   │  (validated→active
                                 └─────┬────┘   │   when ratio drops
                          golden-set+ │         │   to 1:1≤r<3:1)
                          ratio       │         │
                                 ┌─────▼─────┐  │
                                 │ validated ├──┘
                                 │ (active)  │
                                 └─────┬─────┘
                                       │
                                       ▼  (any state → tombstoned)
                              ┌────────────────┐
                              │   tombstoned   │  Ruslan / incident /
                              └────────────────┘  ratio<1:1 / superseded
```

### 5.5 α-4 Cycle

**Identity (verbatim, FPF Part 4 §4.4).** "A single `task → gate →
compound → archive` run." Scope: the brigadier's CE 40/10/40/10 loop
instance.

**State graph** (FPF verbatim):

| State | Definition |
|---|---|
| `opened` | `cycle_id` allocated; brigadier intakes task. |
| `running` | Cells dispatched; artefacts being produced. |
| `integrating` | All expected returns received; brigadier integrating. |
| `gated` | AWAITING-APPROVAL packet posted to `swarm/gates/`. |
| `compounded` | HITL approved; brigadier ran compound step (α-3 entries written). |
| `closed` | `cycle-log.md` written; 1-line summary of rule-extractions + 1-line open-questions. |
| `tombstoned` | Cycle aborted (brigadier or HITL). |

**Spec alias map** (per prompt §6 D5):

| Spec alias | FPF state(s) it covers |
|---|---|
| `open` | `opened` |
| `mid-cycle` | `running` + `integrating` |
| `closing` | `gated` + `compounded` |
| `closed` | `closed` |

**Transitions table:**

| from | to | trigger | mover | side-effects |
|---|---|---|---|---|
| (none) | `opened` | brigadier intakes task (α-1 `intaked`) | brigadier | `cycle_id` allocated; entries in `swarm/logs/<cycle-id>.md` begin. |
| `opened` | `running` | first `Task(...)` dispatched (α-1 `dispatched`) | brigadier | log line. |
| `running` | `integrating` | all cells returned (α-1 `integrated`) | brigadier | log line. |
| `integrating` | `gated` | brigadier writes AWAITING-APPROVAL (α-1 `gated`) | brigadier | gate file. |
| `gated` | `compounded` | HITL ack + brigadier runs compound (α-1 `approved → compounded`) | HITL + brigadier | α-3 entries written. |
| `compounded` | `closed` | brigadier writes `swarm/logs/<cycle-id>/cycle-log.md` | brigadier | `swarm/logs/<cycle-id>/cycle-log.md` exists; `meta/health.md` `closed_cycles_count` field incremented (per D10 §2; bootstrap `meta/health.md` initialises `closed_cycles_count: 0` per D1 §1.4). |
| any | `tombstoned` | abort (Ruslan or brigadier) | brigadier (Ruslan-triggered) | log line; partial artefacts archived. |

**Acceptance predicates per state:**

- `opened`: `cycle_id` set on the task; `swarm/logs/<cycle-id>.md` exists.
- `running`/`integrating`/`gated`/`compounded`: mirror α-1 `dispatched`/`integrated`/`gated`/`compounded` predicates.
- `closed`: `swarm/logs/<cycle-id>/cycle-log.md` exists with frontmatter `summary:` (≥1 line) and `open_questions:` (≥1 line); the `closed_cycles_count` field in `swarm/wiki/meta/health.md` is incremented (D10 §2; minimum bootstrap field per D1 §1.4 #13).
- `tombstoned`: log line present + `cycle_id` not in `meta/health.md` closed-cycle counter.

**Cross-alpha integrations.** α-4 contains exactly one α-1 instance.
α-2 instances live inside α-4 from `running` through `compounded`.
α-3 entries are emitted at `compounded`. **α-4 `closed` count is the
authoritative metric for Q8 Layer-9 trigger #1 (≥50 closed cycles).**

**ASCII diagram:**

```
        ┌────────┐
        │ opened │  ◄─── brigadier intake
        └───┬────┘
            │ dispatch
        ┌───▼─────┐
        │ running │
        └───┬─────┘
            │ all-returned
        ┌───▼────────┐
        │integrating │
        └───┬────────┘
            │ gate
        ┌───▼────┐
        │ gated  │
        └───┬────┘
            │ HITL+compound
        ┌───▼────────┐
        │ compounded │
        └───┬────────┘
            │ cycle-log
        ┌───▼────┐
        │ closed │   (counter++; feeds Q8 trigger)
        └────────┘
            ⇧
            │ (any state) abort
        ┌────────────┐
        │ tombstoned │
        └────────────┘
```

### 5.6 α-5 Direction (human-owned, Phase A lightweight)

**Identity (verbatim, FPF Part 4 §4.5).** "Strategic direction under
test — spans cycles." Scope: strategic direction; spans multiple α-4
cycles.

**State graph** (FPF verbatim, full set retained for Phase B
formalization):

| State | Definition |
|---|---|
| `hypothesized` | Falsifiable claim + confidence threshold + success metric declared. |
| `under-validation` | Evidence-collection in progress; ≥1 expert producing artefacts. |
| `validated` | Evidence artefacts from ≥2 experts. |
| `activated` | Written activation decision + resource commitment (Ruslan signs). |
| `scaled` | Direction has compounded across multiple cycles; resource allocation grew. |
| `plateaued` | Returns flat or declining; awaiting decision (continue, pivot, drop). |
| `invalidated` | Refuted by evidence. |
| `dropped` | Explicit exit. |
| `archived` | Historical record; no further action. |

**Pivot branches (verbatim).** `under-validation → hypothesized`;
`invalidated → hypothesized`.

**Movers (verbatim, FPF Part 4 §4.5):** "Human / strategic-management
primary `hypothesized` and `activated`; brigadier tracks state;
experts contribute evidence artefacts." **AI agents do NOT move the
Direction alpha** beyond tracking.

**Phase A vs Phase B (per FPF Part 10.4 + Part 10.6):**

- **Phase A (this spec):** state-enum-only. The spec stores `α-5
  state` per direction in `swarm/wiki/foundations/swarm-alphas.md`'s
  α-5 section (a flat list of named directions + current state). No
  state-machine validator is required Phase A; transitions are
  documented in the swarm-alphas.md but not lint-enforced.
- **Phase B (deferred per Part 10.6):** full NQD-CAL + E/E-LOG + BLP
  formalization; transitions become machine-tracked; `/lint` enforces
  state predicates.

**Acceptance predicates (Phase A — informational only):**

- `hypothesized`: a direction entry in swarm-alphas.md α-5 section
  with `claim:`, `confidence_threshold:`, `success_metric:` fields.
- `validated`: ≥2 `swarm/wiki/experiments/` pages cite this direction
  via `derived_from`/`supports` edges, each `produced_by` a different expert.
- `activated`: an `AWAITING-APPROVAL-direction-<slug>-activation.md`
  file in `swarm/gates/` with Ruslan ack.

**Cross-alpha integrations.** α-5 spans multiple α-4 cycles; cycles
contributing evidence to a direction record `direction:
<direction-slug>` in their `cycle-log.md`. α-2 evidence artefacts
(experiments, summaries) cite the direction via `derived_from`.

**HITL discipline.** Any α-5 state change is HITL-only — bounce to
Ruslan via AWAITING-APPROVAL file (D6 §4). The brigadier never moves
α-5 unilaterally.

**ASCII diagram (Phase A informational):**

```
              ┌─────────────┐
              │hypothesized │ ◄─┐ (pivot from invalidated)
              └──────┬──────┘   │
                     │           │
              ┌──────▼──────┐    │
              │under-       │ ───┘ (pivot back)
              │validation   │
              └──────┬──────┘
                     │
              ┌──────▼──────┐
              │ validated   │
              └──────┬──────┘
                     │ Ruslan signs activation
              ┌──────▼──────┐
              │ activated   │
              └──────┬──────┘
                     │
              ┌──────▼──────┐
              │  scaled     │
              └──────┬──────┘
                     │
              ┌──────▼──────┐    ┌─────────────┐
              │ plateaued   │ ──►│ invalidated │
              └──────┬──────┘    └──────┬──────┘
                     │                  │
              ┌──────▼──────┐           │
              │  dropped    │           │
              └──────┬──────┘           │
                     │                  ▼
                     │             ┌──────────┐
                     └─────────────► archived │
                                   └──────────┘
```

### 5.7 Cross-alpha integrations summary (matrix)

| | α-1 Task | α-2 Artefact | α-3 Strategies-Rule | α-4 Cycle | α-5 Direction |
|---|---|---|---|---|---|
| **α-1** | self | creates instances during `dispatched→integrated` | emits at `compounded` | inhabits inside α-4 (1:1) | task may target a direction (informational) |
| **α-2** | created during α-1 | self | strategies cite α-2 artefacts | exists inside α-4 | direction evidence is α-2 |
| **α-3** | emitted at α-1 `compounded` | strategies cite α-2 | self | activation/retirement triggered by cycle aggregates | strategies may inform direction |
| **α-4** | contains 1× α-1 | hosts α-2 from `running` to `compounded` | drives α-3 `validated` transitions | self | cycle counts feed direction validation |
| **α-5** | n/a (HITL) | direction evidence is α-2 | n/a | spans multiple α-4 cycles | self |

### 5.8 `swarm/wiki/foundations/swarm-alphas.md` skeleton

The Стадия D bootstrap content of `swarm/wiki/foundations/swarm-alphas.md`
is exactly D5 §5.1–§5.7 (this entire section), wrapped in this
frontmatter:

```yaml
---
id: foundation-01HF2K3M5N7P9Q12345678ALPHA
title: Swarm Alphas (5)
type: foundation
layer: spine
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
last_reviewed: 2026-04-23
pipeline: linted
state: accepted
confidence: high
confidence_method: ruslan-attested
tier: core
produced_by: brigadier
sources:
  - {path: "decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md", range: "Part 4"}
  - {path: "design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md", range: "D5"}
related: [[foundations/swarm-protocols]]
topics: [[topics/swarm-architecture-hub]]
binding_scope: swarm-wide
supersedes_versions: []
---
```

### 5.9 Compatibility matrix

| Locked item | D5 honours by … |
|---|---|
| FPF Part 4 (5 alphas locked identity/scope) | All 5 alphas materialised; FPF verbatim states adopted as canonical; alias map provided where prompt §6 D5 prescribed alternative names. |
| FPF Part 10.4 swarm-alphas.md mandate | §5.8 specifies the file skeleton and frontmatter; brigadier writes the full content per Стадия D bootstrap. |
| FPF Part 10.6 α-5 Phase A lightweight | §5.6 specifies state-enum-only Phase A; full NQD-CAL deferred Phase B. |
| Q5 staleness signals (α-2/α-3 lifecycle) | `tombstoned` extension added to α-2 + α-3 (state predicates testable from filesystem). |
| Q6 skill pipeline (α-3 + Q6 owners) | Movers per transition specified; reconciled with Q2 single-writer + meta-agent-via-task. |
| Q8 Layer-9 trigger | α-4 `closed` count is the authoritative cycle metric (§5.5). |
| W-12 1000% depth | Each alpha has identity, state graph, transitions table, predicates per state, cross-alpha integrations, ASCII diagram. |
| Sub-agent A §6 #10 (Q2-vs-Q6 conflict) | Resolved: meta-agent emits draft via Task; brigadier writes. Reflected in α-2/α-3 movers. |
| Sub-agent B §1/§2/§3/§4 gap-flags | Closed: α-1 `gated→rejected→returned` mover specified; α-2 `tombstoned` defined; α-3 spec/FPF state alias documented; α-4 spec/FPF mapping documented. |

---

## DELIVERABLE 6 — `swarm/lib/shared-protocols.md` (Wiki Write Protocol + ancillaries)

### 6.1 Mandate

This is the runtime contract every domain expert reads on every Task
invocation (per FPF Part 10.5, Sub-agent B §6; master synthesis
§5.5.1–§5.5.5 baseline, Sub-agent E §1). It extends §5.5 (master
synthesis) for v3 specifics; it does NOT replace it. The brigadier
imports this file at session start; experts import it via §7 of their
system.md (per FPF Part 10.8 success predicate item 7).

The file lives at `swarm/lib/shared-protocols.md`. **Nine sections**:
seven mirror FPF Part 10.5 mandates verbatim (wiki write protocol —
split into §6.2 + §6.3 deep-dive on §5.5.5; structured output schema;
HITL escalation; tool permission self-check; cross-cell-reference
protocol; `mode: writing-support`; tool-language abstractions). One
section (§6.10 Max-subscription discipline) extends per master
synthesis §5.7. Section content below is the literal initial body;
Стадия D writes verbatim.

### 6.2 Section 1 — Wiki write protocol (extends master synthesis §5.5)

**6.2.1 Single-writer brigadier rule (Q2-locked).** All writes to
`swarm/wiki/` flow through the brigadier. Cells (5 domain experts in
4 modes = 20 matrix cells per Sub-agent E §5) write only to
`swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md`. They return
their draft via the `Task(...)` return value (structured per §6.4
below). The brigadier reads the draft, runs the §5.5.5 gate (§6.3
below), and commits canonical content to `swarm/wiki/<canonical-path>/`.
This applies across all 9 layers and the global spine. **No role-mode
bypasses this rule** (Sub-agent E §6 confirmed: critic, optimizer,
integrator, scalability all return via Task; none gets elevated
write rights).

**6.2.2 Per-layer write paths and authorised drafters.** For each
layer (D1 §1.3 permission table is authoritative; this is the
expert-facing summary):

| Target path | Drafter (mode) | Brigadier promotion target |
|---|---|---|
| `wiki/drafts/<task-id>-<expert>-<artefact>.md` | any of 5 experts × 4 modes | promotes to canonical per draft type |
| `wiki/concepts/<slug>.md` | engineering/systems/philosophy expert (any mode), drafted in `drafts/` | direct write by brigadier after gate |
| `wiki/claims/<slug>.md` | any expert (any mode), drafted in `drafts/` | brigadier write |
| `wiki/sources/<slug>.md` | `/ingest` (skill) OR brigadier from book sweep (W-3) | brigadier write or skill write |
| `wiki/foundations/<theme>/<slug>.md` | theme-matched expert (any mode), drafted in `drafts/` | brigadier write; foundations require `confidence_method: ruslan-attested` (D4 §4.10) |
| `wiki/themes/<theme>/...` | theme-matched expert, drafted in `drafts/` | brigadier write (Phase A: brigadier seeds from books per W-3) |
| `wiki/brigadier/...` | brigadier directly (own wiki) | brigadier write |
| `wiki/agents/<expert>/scratchwork/...` | expert directly (per D2 §2.4 `is_scratchwork: true` exception) | n/a — scratchwork is expert's own |
| `wiki/agents/<expert>/<canonical-slug>.md` | expert (any mode), drafted in `drafts/` | brigadier write |
| `wiki/meta/agent-improvements/...` | meta-agent (writing-support mode) OR any expert in critic mode, drafted in `drafts/` | brigadier write |
| `wiki/skills/candidates/<slug>/manifest.md` | brigadier directly (own observation) OR any agent in `drafts/` | brigadier write |
| `wiki/skills/learning/<slug>/...` | brigadier directly | brigadier write |
| `wiki/skills/active/<slug>.md` | brigadier directly (after D11 activation rubric) | brigadier write |
| `agents/<expert>/strategies.md` (Level-1, T5/R6) | expert directly (this exact file only — exception to single-writer for personal memory layer) | n/a |

**6.2.3 Pre-write checklist (brigadier).** Before `Write` to any
canonical wiki path, the brigadier:

1. Reads the cell-returned draft (or self-drafted artefact).
2. Loads the relevant template from `swarm/wiki/_templates/<type>.md`
   (D4) — verifies all required frontmatter fields present.
3. Loads the edge enum from `swarm/wiki/_templates/edge-types.md`
   (D3) — verifies every `[[wikilink]]` in body has a corresponding
   `related[]` entry AND will produce a valid `edges.jsonl` record.
4. Runs §6.3 §5.5.5 provenance gate.
5. If gate passes: writes; appends edges to `graph/edges.jsonl`;
   updates `index.md`; appends `log.md` line.
6. If gate fails: returns the draft to the cell with rejection note
   in `swarm/wiki/tasks/<task-id>/decisions/<ts>-rejection.md`;
   draft remains in `drafts/`.

**6.2.4 Commit message format for wiki writes.** Per master synthesis
§5.9 step 4 + Sub-agent E §1:
```
[<agent>] <cycle>: <description>
```
where `<agent>` = `brigadier` for canonical wiki writes, `<cycle>` =
`cyc-<kebab-slug>` per H7, `<description>` ≤80 chars. Plus the `co-authored-by`
trailer if a cell drafted (per Sub-agent E §6 routing pattern).

### 6.3 Section 2 — §5.5.5 provenance gate (v3 enforcement)

**6.3.1 Verbatim baseline (master synthesis §5.5.5):**

> "On Compound write to `agents/<expert>/strategies.md`, the entry
> must cite at least one source artefact (incident file + commit hash,
> or verbatim source with line range). Entries without provenance are
> rejected. AP-18 prevention."

**6.3.2 v3 generalisation.** The gate extends from `strategies.md`
writes to **every brigadier `Write` to `swarm/wiki/`** (i.e. every
α-2 transition to `accepted`). The gate accepts a write iff ALL
conditions hold:

1. **Provenance present.** Frontmatter `sources[]` is non-empty AND
   each entry has `path` resolving to either:
   - A file under `swarm/wiki/sources/...` with `state ∈ {accepted,
     referenced}`, OR
   - A Tier-1 file under `decisions/`, `design/`, `raw/research/`,
     `raw/articles/`, `prompts/`, `CLAUDE.md`, `.claude/rules/`, OR
   - An `(incident_file, commit_hash)` tuple format
     `<path>@<40-hex>` (verbatim from §5.5.5), OR
   - A `(verbatim source, line range)` tuple format
     `<path>:<start>-<end>` (verbatim from §5.5.5).
2. **Inline citations consistent.** If frontmatter `provenance_inline:
   true`, body MUST contain at least one `[src:<path>#<section>]`
   inline citation per non-trivial paragraph (per master synthesis
   §5.5.3).
3. **Edge consistency.** Every `[[wikilink]]` in body has a
   corresponding `related[]` entry AND a record in `graph/edges.jsonl`
   per D3 enum (Sub-agent C §8 anti-pattern 11).
4. **Tier coherence.** Outgoing artefact `tier` is no stricter than
   any input source `tier` (Lock 13 enforcement, master synthesis
   §5.5.4).
5. **Foundation conditions.** When `type = foundation`,
   `confidence_method ∈ {ruslan-attested, brigadier-attested-with-3-supports}`
   (D4 §4.10 + D2 §2.3). Brigadier-attested foundations require ≥3
   `supports` edges from `state: accepted` claims.
6. **Non-contradicting.** When `state` advances to `accepted`,
   brigadier verifies no existing `state: accepted` page contradicts
   without an explicit `contradicts` edge (`/lint` pre-pass per
   §5.6.2 PostToolUse, Sub-agent E §2).

**6.3.3 What the gate REJECTS.**

- `sources[]` empty when `pipeline ∈ {compiled, linted, ready}` AND
  `state ∉ {drafted}`.
- `sources[]` entry whose `path` is `raw/` and `pipeline: raw` (raw
  source can't ground a `compiled+` artefact unless distilled into a
  `swarm/wiki/sources/<slug>.md` first).
- A claim contradicting an `accepted` foundation without a
  `contradicts` edge (per Sub-agent A §1 Q5 bidirectional contradicts +
  D3 §3.2.2).
- An `accepted` artefact whose `confidence_method` is unspecified
  when `confidence: high` is asserted.
- A foundation lacking the specific `confidence_method` clause from
  6.3.2.5.
- An edge in `graph/edges.jsonl` that violates the D3 §3.3 from-layer
  × to-layer matrix.

**6.3.4 Brigadier verification ritual** (executed before `Write`):

```
# pseudo-code (run by brigadier mentally / via /lint dry-run)
1. read draft (or self-authored artefact) frontmatter
2. assert sources[] non-empty (unless drafted/raw)
3. for each source:
     resolve path; assert state ∈ {accepted, referenced} OR is Tier-1
4. assert provenance_inline rule satisfied (grep [src: in body)
5. for each [[wikilink]] in body:
     assert ∃ related[] entry; assert ∃ edges.jsonl record (or queued for write)
6. assert tier ≤ all input tiers
7. if type = foundation: assert confidence_method clause
8. /lint dry-run on the draft file → must return zero errors
9. if all pass: Write; commit with §6.2.4 format; log.md append
   else: write rejection in tasks/<task-id>/decisions/<ts>-rejection.md
```

**6.3.5 Rejection-handling behaviour (closes Sub-agent E §1.5.5
ambiguity #1).** When the gate rejects:

- The brigadier writes a rejection record at
  `swarm/wiki/tasks/<task-id>/decisions/<YYYY-MM-DD-HHMM>-rejection.md`
  with `gate_rejected: true`, `rejected_reason: <one of the 6.3.3
  cases>`, `draft_path: <drafts/...>`, `next_action: <return-to-cell|escalate-to-HITL>`.
- The draft remains in `swarm/wiki/drafts/...` (not promoted, not
  deleted).
- A line is appended to `swarm/wiki/log.md`:
  `## [<date>] gate-reject | <task-id> | <slug> | <reason>`.
- Brigadier may retry up to 2 times by re-invoking the cell with
  `Task(..., context: {previous_rejection: <path>})`. After 2 retries,
  brigadier ESCALATES per §6.5 (HITL).

### 6.4 Section 3 — Structured output schema (Task return contract)

**6.4.1 Every Task() return MUST be a structured packet** with the
following fields (Sub-agent B §8 + Sub-agent A §1 Q4 + master
synthesis §5.5.3):

```yaml
# return value of Task(<expert>-<mode>, ...) — YAML / JSON
summary: <one-paragraph string, ≤500 chars>
proposed_writes:                                # zero or more drafts
  - path: swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md
    frontmatter:                                # full frontmatter for the proposed write
      <key>: <value>
    body: |
      <full markdown body>
    edges_to_add:                               # records to append to graph/edges.jsonl
      - {from: <path>, to: <path>, type: <edge-type>, ts: <YYYY-MM-DD>, confidence: <enum>}
provenance:                                     # what the cell consulted
  - {path: <Tier-1-path>, range?: <line-range>, quote?: <verbatim quote>}
confidence: <low|medium|high>                  # cell's own confidence in the return
confidence_method: <expert-judgment|cited-source|peer-reviewed|...>
escalations:                                    # zero or more
  - {trigger: <one of: foundation-revision|layer-9-activation|contradiction|budget-overrun|retry-limit>, packet_path?: swarm/gates/AWAITING-APPROVAL-...}
dissents:                                       # for integrator mode: dissenting positions preserved
  - {position: <one-line>, evidence: [<wikilinks>]}
```

**6.4.2 JSON-schema-style summary** (Стадия D may translate to a
JSON Schema validator, or rely on /lint on the resulting artefact):

| Field | Type | Required | Notes |
|---|---|---|---|
| `summary` | string | yes | concise return summary |
| `proposed_writes[]` | list | yes (may be empty) | zero writes is valid (e.g. critic returning empty-issue review) |
| `provenance[]` | list | yes (≥1 entry when `proposed_writes[]` non-empty OR `escalations[]` non-empty; may be empty when both are empty — closes critic-gate1 H8 ambiguity by replacing "purely procedural") | grounds the cell's reasoning |
| `confidence` | enum | yes | `low|medium|high` |
| `confidence_method` | enum | yes for the Task return packet (cell must justify its confidence to brigadier even if the field stays optional in the eventual stored frontmatter per D2 §2.2; reconciliation per critic-gate1 H8) | per D2 §2.2 enum |
| `escalations[]` | list | yes (may be empty) | bounces routed by brigadier |
| `dissents[]` | list | required iff `produced_by` matches `*-integrator` (closes critic-gate1 H8 testable predicate); optional otherwise | preserves minority positions per FPF |
| `extractions[]`, `alternatives[]`, `anti_scope[]` | list | required iff `mode: writing-support` per D6 §6.8.2 (closes critic-gate1 M11) | writing-support contract |

**6.4.3 Validation.** Brigadier rejects malformed Task returns by
not promoting the draft to canonical (the cell's draft remains in
`drafts/`); brigadier may re-invoke the cell with `Task(..., context:
{schema_error: <message>})`.

### 6.5 Section 4 — HITL escalation rules + AWAITING-APPROVAL packet

**6.5.1 When to escalate to Ruslan (HITL).** Per FPF Part 4 §4.5.4 +
Part 5 §5.2 (Sub-agent B §9):

1. **Foundation revision.** Any change to a `state: accepted`
   `foundations/` page (creation of a new foundation OR `supersedes`
   an existing one).
2. **Layer-9 activation.** Q8 3-AND trigger satisfied per D10; Ruslan
   ack required (per W-10 + R5).
3. **Contradiction without resolution.** A new `accepted` artefact
   contradicts an existing `accepted` foundation AND no resolution
   (drop, supersede, scope-narrow) is obvious.
4. **Budget overrun.** Per master synthesis §5.4 termination stack —
   brigadier hit `maxTurns` or token budget without completing.
5. **Retry limit.** Brigadier rejected the same draft 2 consecutive
   times (per §6.3.5).
6. **α-5 Direction state change.** Any α-5 transition (D5 §5.6) —
   AI agents do NOT move α-5 (FPF Part 4 §4.5).
7. **Method exhaustion.** Same AP triggered >5 times across cycles
   (FPF Part 5 §5.2).
8. **Irreversible decision.** Architecture commit, dependency change,
   protocol modification.
9. **`split_trigger` fires** in Block 5 of an expert manifest (FPF).

**6.5.2 AWAITING-APPROVAL packet contents** (file at
`swarm/gates/AWAITING-APPROVAL-<task-id-or-slug>-<YYYY-MM-DD>.md`):

```yaml
---
title: <one-line summary of the ask>
type: gate
gate_type: <foundation-revision|layer-9-activation|contradiction|budget-overrun|retry-limit|alpha-5|method-exhaustion|irreversible|split-trigger>
escalator: brigadier
escalated_at: <YYYY-MM-DD-HHMM>
task_id?: <task-id>
cycle_id?: <cycle-id>
deadline?: <YYYY-MM-DD>
state: open
---

## Context
<one-paragraph: what's happening, why it's escalating now>

## Options
1. **<Option A>** — <description; consequences; tier impact>
2. **<Option B>** — <description; consequences>
3. **<Option C>** — <description; consequences>
(Up to 4 options. The 4-response template per Sub-agent B §9.)

## Recommendation
<brigadier's preferred option + 2-3 line rationale>

## Risk
<what could go wrong; how reversible>

## Proposed file path(s) (if any change applied)
- <path>
- <path>

## How Ruslan acks
Append a line to `swarm/gates/<task-id>-ack.md` with:
  acked: true
  chosen: <option-letter>
  notes: <optional comment>
Or: edit this file's frontmatter `state: acked` and add `chosen: <letter>`.
```

**6.5.3 Escalation file path convention.** All gate files land in
`swarm/gates/`. Naming: `AWAITING-APPROVAL-<task-id-or-slug>-<YYYY-MM-DD>.md`
for the request; `<task-id-or-slug>-ack.md` for the ack; `<task-id-or-slug>-rejection.md` for HITL reject.

**6.5.4 Brigadier post-ack behaviour.** Brigadier polls
`swarm/gates/` per cycle close. On detecting an ack:
- α-1 transition: `gated → approved` (and α-4 `gated → compounded`).
- Apply the chosen option: write the canonical artefact, update edges,
  log.md, commit.
- Move the gate file's frontmatter to `state: closed`.

### 6.6 Section 5 — Tool permission self-check

**6.6.1 Verbatim master synthesis §5.7.1 mandate** (Sub-agent E §3):

- **Brigadier** has: `Task` (spawn subagent), unrestricted `Write`,
  scoped `Bash (write)`, external MCP.
- **Experts** have: `Read` (any path under `swarm/wiki/` and `wiki/`),
  `Write` SCOPED to `swarm/wiki/drafts/<task-id>-<expert>-*` AND
  `swarm/wiki/foundations/<domain>/*`. Experts have **no Bash-write**;
  no canonical wiki write rights.

**6.6.2 Self-check ritual** (every agent, at function entry).
Closes Sub-agent B §10 gap (FPF Part 10 silent on ritual body):

```
# pseudo-code (executed by every cell at function entry)
my_role := get_my_role()                    # brigadier | <expert>-<mode> | meta-agent
intended_tool := <Tool name about to invoke>
intended_target := <path or arg about to operate on>
allowed := lookup(role_tool_matrix, my_role, intended_tool, intended_target)
if not allowed:
  log "permission_denied: role=<...>, tool=<...>, target=<...>"
  return Task() with escalation: {trigger: permission-denied, requested: <intended>, reason: <rule>}
else:
  proceed with tool invocation
```

**6.6.3 role_tool_matrix** (the table the self-check consults):

| Role | Read | Write (path glob) | Bash (write) | Task | MCP |
|---|---|---|---|---|---|
| brigadier | * | * (all of `swarm/`, `agents/`, `.claude/`) | yes | yes | yes |
| `<expert>-<mode>` (any of 5×4) | * | `swarm/wiki/drafts/<task-id>-<expert>-*`, `swarm/wiki/foundations/<expert-domain>/*`, `agents/<expert>/strategies.md` | no | no | no |
| meta-agent | * | (drafts only via `mode: writing-support`; no canonical) — same as expert | no | no | no |
| `/ingest`, `/build-graph`, `/lint`, `/consolidate`, `/ask` (skills) | * | scoped per skill manifest (D8 — Gate 2) | yes (skill scope only) | no | no |

**6.6.4 Behaviour on permission deny.** The self-check MUST NOT
silently retry. The agent returns a structured `escalations[]` entry
in its Task return packet (per §6.4.1) with `trigger: permission-denied`.
Brigadier handles the escalation: either re-routes the work to a
properly-permissioned agent OR escalates to HITL per §6.5 if the
permission denial is unexpected.

### 6.7 Section 6 — Cross-cell-reference protocol (read wiki, never call cell)

**6.7.1 Verbatim FPF Part 10.5 mandate (Sub-agent B §6, FPF L1407):**
"Cross-cell-reference protocol (read wiki, never call cell)."

Reinforced by master synthesis §4.5.4 (Sub-agent E §6.1): "A cell may
*read* any wiki artefact. A cell may *write* only its own output
artefact. **A cell may not *invoke* another cell.**"

**6.7.2 Operational contract.** When a cell needs the output of
another cell, it consumes via the wiki, never via `Task(...)`:

- **READ allowed:** any path under `swarm/wiki/` (including
  `drafts/`); any path under v2 `wiki/`; any Tier-1 path
  (`decisions/`, `design/`, `raw/research/`, `prompts/`, `CLAUDE.md`,
  `.claude/rules/`).
- **READ forbidden:** other cells' active context windows;
  `Task(<other-expert>-<mode>, ...)` to fetch a fresh draft from a
  peer expert.
- **WRITE allowed:** only `swarm/wiki/drafts/<task-id>-<self>-<artefact>.md`
  per §6.6.3 role_tool_matrix.

**6.7.3 Why the read-only rule.** Spawning a peer cell from inside a
cell would (a) violate Q2 single-writer through chained delegation,
(b) explode the brigadier's coordination state into uncoordinated
subtrees, (c) duplicate context-window cost (master synthesis §5.7
turn-counting discipline), (d) bypass §5.5.5 provenance gate — peer
output reaches consumer without brigadier verification.

**6.7.4 Pattern when peer output is needed.** If cell A needs cell B's
output:

1. Cell A's `Task()` return packet (per §6.4.1) includes an
   `escalations[]` entry: `{trigger: peer-input-needed, requested:
   "<expert>-<mode> on <topic>", context_path: <task-dir>}`.
2. Brigadier reads the escalation, dispatches `Task(<expert-B>-<mode>,
   ...)`, integrates B's output into the same task's `artefacts/` dir.
3. Cell A is re-invoked (next turn) with B's draft now visible under
   `swarm/wiki/drafts/<task-id>-<expert-B>-*.md`.

**6.7.5 `/lint` rule.** Any Task return packet whose body contains
`Task(` invocation strings (a heuristic for "I called another cell
inline") is flagged. Static check at draft promotion: brigadier
inspects body for unauthorised invocation patterns; rejects via
§6.3.5 if found.

**6.7.6 Brigadier-only exception.** Only the brigadier holds `Task`
permission per §6.6.3. The brigadier's invocation of `Task(...)` is
the canonical and only legal path for cross-cell coordination.

### 6.8 Section 7 — `mode: writing-support` clause

**6.7.1 Verbatim FPF Part 10.5 + Part 5 §5.3 enhancement E-10
(Sub-agent B §11):**

> "Add a `mode: writing-support` sub-clause inside §7 (shared
> protocols) for all 5 experts: 'If invoked to contribute to a weekly
> review, quarterly letter, or strategizing document, DO NOT generate
> primary prose. Return: (a) structured extractions from cited
> artefacts, (b) proposed alternatives enumerated, (c) explicit
> anti-scope list. Human owns composition.'"

**6.7.2 Operational contract.** When invoked with
`Task(<expert>-<mode>, mode: writing-support, ...)`:

- The cell produces NO primary prose (no body content for the
  destination doc).
- The cell's return packet contains:
  - `extractions[]`: structured facts pulled from cited artefacts;
    each item with `quote`, `source_path`, `range`.
  - `alternatives[]`: enumerated options (per the structured-output
    schema §6.4); brigadier or HITL choose.
  - `anti_scope[]`: explicit list of items NOT to include in the
    final composition.
- Brigadier or HITL composes the final prose; cells never edit the
  final.
- This mode is a **brigadier-only auxiliary capability**, not a 5th
  matrix mode (resolves Sub-agent E §6 ambiguity #4 — preserves the
  5×4=20 invariant per master synthesis §5.10.3).
- Use cases: weekly review composition; quarterly Ruslan letter;
  strategizing-ritual artefacts (per FPF Part 5 §5.2); meta-agent
  proposed improvements written to `meta/agent-improvements/`.

**6.7.3 Anti-pattern lock (Sub-agent B §11 verbatim FPF
[B §E.3]):** "полная автоматизация writing... «без внешнего по
отношению к LLM контуру обработки текста — никак, LLM всегда
обманет»." `/lint` MAY (Phase B) enforce that any wiki page authored
in `mode: writing-support` carries `produced_by: <expert>-writing-support`
and a `human_composed_at:` timestamp marking when the human wove the
extractions into prose.

### 6.9 Section 8 — Tool-language abstractions (verb dictionary)

**6.8.1 Verbatim FPF Part 10.5 + Part 2 §2.7 E-7 move 2 (Sub-agent
B §12):**

> "Rename tooling tokens to pattern-layer abstractions in the shared
> protocols file: 'YAML frontmatter' → 'Frontmatter'; 'git commit' →
> 'snapshot'; 'pre-commit hook' → 'local gate'."

**6.8.2 Verb dictionary used in `shared-protocols.md`** (closes
Sub-agent B §12 gap by extending FPF's 3 pairs):

| Tooling token | Pattern-layer abstraction |
|---|---|
| YAML frontmatter | Frontmatter |
| git commit | snapshot |
| git push | publish |
| pre-commit hook | local gate |
| PostToolUse hook | post-action gate |
| /lint | local check |
| /ingest | ingest |
| /ask | retrieve-and-synthesize |
| /build-graph | rebuild edges |
| /consolidate | merge-duplicates |
| Task() | dispatch |
| `swarm/wiki/drafts/` | draft area |
| `swarm/wiki/<canonical>/` | canonical area |
| `swarm/gates/` | gate dock |
| `swarm/lib/shared-protocols.md` | shared protocols |
| `agents/<expert>/strategies.md` | personal memory |
| `swarm/wiki/meta/agent-improvements/` | swarm memory |

**6.8.3 Lock note (verbatim).** "Lock 17 (Filesystem = SoT) preserved;
this is purely naming-layer discipline."

### 6.10 Section 9 — Max-subscription discipline (extension per master synthesis §5.7)

**6.9.1 Verbatim master synthesis §5.7.3 + §5.6.3 + §5.9 (Sub-agent
E §3):**

```bash
# SessionStart hook (assert no API key set)
if [ -n "$ANTHROPIC_API_KEY" ]; then
  echo "WARNING: ANTHROPIC_API_KEY is set; Jetix uses Max subscription"
  echo "Run: unset ANTHROPIC_API_KEY"
  exit 1
fi
```

`unset ANTHROPIC_API_KEY` enforced at every session start. Optionally
`unset GROQ_API_KEY` if Whisper pipeline is not in use.

**6.9.2 No paid embeddings, no third-party APIs** (closes Sub-agent
E §3 ambiguity #1 — master synthesis silent on vector-DB prohibition
explicitly):

- No vector DB calls (Pinecone, Weaviate, etc.).
- No paid embedding services (OpenAI embeddings, Cohere, etc.).
- No third-party LLM APIs (only Claude Code Max plan).
- No paid transcription (Groq Whisper / OpenAI Whisper) outside
  voice-memo pipeline windows when `GROQ_API_KEY` is explicitly
  re-set.
- All retrieval Phase A is filesystem + ripgrep + typed-BFS over
  `graph/edges.jsonl` per Q1 + Sub-agent C §1.

**6.9.3 Tool matrix (Sub-agent E §3 §5.7.1).** Skills run their own
logic via Claude Code's built-in tools (Read/Write/Grep/Glob/Bash).
No `anthropic` SDK invocations. No `openai`/`cohere`/etc. SDK
invocations.

**6.9.4 Cost = turn-counting, not billing.** §5.4 termination stack +
maxTurns enforce the budget. With `ANTHROPIC_API_KEY` unset, the
attack surface shifts from "unlimited API spend" to "Max plan
rate-limit hit." Recovery cost = downtime, not money.

**6.9.5 Per-cycle commit + push** is the persistence ritual:
`swarm/wiki/log.md` updates live in the same commit as the wiki page
write (atomic). Branch: `claude/jolly-margulis-915d34` (current Phase A);
no force-push, no rebase.

### 6.11 `swarm/lib/shared-protocols.md` skeleton frontmatter

The Стадия D bootstrap content is the literal text of D6 §6.2–§6.9
above, wrapped in:

```yaml
---
id: shared-protocols-01HF2K3M5N7P9Q12345678PROT
title: Swarm Shared Protocols
type: protocols
layer: spine
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
last_reviewed: 2026-04-23
pipeline: linted
state: accepted
confidence: high
confidence_method: ruslan-attested
tier: core
produced_by: brigadier
sources:
  - {path: "decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md", range: "§5.5–§5.10"}
  - {path: "decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md", range: "Part 10"}
  - {path: "design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md", range: "D6"}
related: [[foundations/swarm-alphas]]
binding_scope: swarm-wide
---
```

### 6.12 Compatibility matrix

| Locked item | D6 honours by … |
|---|---|
| Master synthesis §5.5.5 (provenance gate baseline) | §6.3 quotes verbatim, generalises to all wiki writes (v3 enforcement). |
| Master synthesis §5.5.2 (single-writer brigadier) | §6.2 enumerates all write paths; experts return drafts via Task. |
| Master synthesis §5.5.3 (provenance frontmatter) | §6.4 structured-output schema includes the `provenance[]` field; D2 §2.2 frontmatter spec satisfied. |
| Master synthesis §5.5.4 (tier enforcement) | §6.3.2.4 tier coherence rule; §6.6.3 role_tool_matrix scopes Write per tier-aware path globs. |
| Master synthesis §5.6.2 (PostToolUse) | §6.3.4 pre-write checklist runs `/lint` dry-run; §6.3.5 records gate rejections inline. |
| Master synthesis §5.7 + §5.9 (Max-subscription) | §6.9 verbatim quote + extension to vector-DB prohibition (closes Sub-agent E §3 ambiguity). |
| FPF Part 10.5 (8 sections of shared-protocols.md) | §6.2 wiki-write + §6.3 §5.5.5 + §6.4 schema + §6.5 HITL + §6.6 self-check + §6.7 writing-support + §6.8 verb dictionary + §6.9 Max-subscription. |
| FPF Part 10.6 (preparatory work) | shared-protocols.md is fully specified; Ruslan ack at gate 1 satisfies the "Clarify with Ruslan" mandate. |
| Q2 single-writer | §6.2 enforces; §6.6 role matrix denies expert direct canonical writes. |
| Q6 owners (R4) | §6.2.2 per-layer table + D11 (Gate 2) rubric. |
| W-12 1000% depth | Every section has concrete predicates, ritual pseudo-code, role tables, and example file shapes. |
| Sub-agent A §6 #10 (Q2-vs-Q6 conflict) | §6.6 + §6.5 ensure meta-agent emits drafts via Task `mode: writing-support`; brigadier writes. |
| Sub-agent B §1/§7/§8/§9/§10/§11/§12 gap-flags | §6.3.5 rejection-handling, §6.4 full schema, §6.5.2 4-response template, §6.6 self-check ritual, §6.7 writing-support contract, §6.8 verb dictionary extension. |
| Sub-agent E §1/§3/§6 ambiguities | §6.3.5 rejection (E §1.5.5 #1); §6.9 vector-DB ban (E §3 #1); §6.7 writing-support as auxiliary not 5th mode (E §6 #4); §6.4 derived_from chained provenance (E §8 #5). |
| Lock 13 tier enforcement | §6.3.2.4 + §6.6.3. |
| Lock 17 Filesystem = SoT | §6.8.3 verbatim; entire protocol is filesystem-resident. |

---
## DELIVERABLE 7 — `.claude/config/wiki-roots.yaml` (Parameterization Config)

### 7.1 Mandate

Per Q9 (coexist + parameterize) and R3 (locked: v2 untouched, v3
added, `$WIKI_ROOT` indirection mandatory), this deliverable specifies
the full content of `.claude/config/wiki-roots.yaml` and the
`$WIKI_ROOT` resolution algorithm the 5 in-scope skills run at
startup. The file is the single source of truth for which wiki tree a
skill targets.

### 7.2 File content (Стадия D writes verbatim)

```yaml
# .claude/config/wiki-roots.yaml
# Single source of truth for wiki-root parameterization (Q9 + R3).
# Do NOT edit without an AWAITING-APPROVAL-wiki-roots-change-*.md
# committed to swarm/gates/ first.

schema_version: 1                    # bump when adding/removing keys
last_modified: 2026-04-23
managed_by: brigadier               # only brigadier writes this file

wiki_root_v2: wiki                   # path-relative to repo root
wiki_root_v3: swarm/wiki             # path-relative to repo root

default_root: wiki_root_v3           # which root new skills target
                                     # unless explicitly overridden via env

bridge_edge_type: cross-tree-ref     # per Q9 + D3 §3.2.12; v3→v2 only

v2_status: read-write                # v2 untouched; existing skills still ingest into wiki/
v3_status: read-write                # v3 primary going forward

migration_phase: A                   # Phase A = coexist; Phase B may flip migration_phase
                                     # decision deferred per WIKI-V3-MECHANICS Q9
                                     # applicability constraint (Sub-agent A §1 Q9
                                     # L658–660): trigger Phase-B re-eval only when
                                     # v3 ≥50 entries AND ≥1 closed cycle AND value-delta observed

# Cross-tree edge-storage paths (T1 separation; per D1 §1.3 + D3 §3.2.12).
edges_v2: wiki/graph/edges.jsonl
edges_v3: swarm/wiki/graph/edges.jsonl
edges_cross_tree: swarm/wiki/graph/cross-tree.jsonl

# Skills inventory and parameterization scope (per D8).
skills_in_scope_for_wiki_root:
  - ingest
  - ask
  - lint
  - consolidate
  - build-graph

skills_excluded_from_wiki_root:
  - search-kb        # per master synthesis §5.10 — legacy KB-only; supplanted by /ask
  - sweep-notion-bank # per master synthesis §5.10 — one-shot Notion-import bound to 2026-04-16 + DB ID
  - compile          # per Sub-agent D §4.6 + §7 — legacy knowledge-base/ writer; deprecated v3
                     # (D8 §8.6 documents the deprecation rationale; not parameterised)
```

### 7.3 Per-key annotation table

| Key | Type | Allowed values | Behaviour at load time | Which skills read |
|---|---|---|---|---|
| `schema_version` | int | `1` (bump on schema change) | parsers reject unknown versions | all |
| `last_modified` | iso-date | valid ISO date | informational only | all |
| `managed_by` | string | `brigadier` | informational; surfaced by /lint when this file's writer differs | all |
| `wiki_root_v2` | string (path) | a path relative to repo root that resolves to a directory | becomes `$WIKI_ROOT_V2` env var | all D8 skills (read-only legacy access) |
| `wiki_root_v3` | string (path) | a path relative to repo root that resolves to a directory | becomes `$WIKI_ROOT_V3` env var | all D8 skills |
| `default_root` | enum | `wiki_root_v2` or `wiki_root_v3` | resolves to `$WIKI_ROOT` per the algorithm in §7.4 | all D8 skills |
| `bridge_edge_type` | string (D3 enum) | one of D3 edge types | drives `cross-tree.jsonl` write target type | /ingest, /build-graph |
| `v2_status` | enum | `read-only` or `read-write` | when `read-only`, /ingest into v2 is rejected | /ingest, /consolidate |
| `v3_status` | enum | `read-only` or `read-write` | parallel | /ingest, /consolidate |
| `migration_phase` | enum | `A` or `B` | informational; bumps trigger Phase-B re-evaluation | meta-agent, brigadier |
| `edges_v2`, `edges_v3`, `edges_cross_tree` | string (path) | resolved paths | /build-graph picks the file by `--tree` flag (T1 separation) | /build-graph, /ingest |
| `skills_in_scope_for_wiki_root` | list of strings | each must match an existing skill in `.claude/skills/` | drives D8 diff scope | meta-agent (lint check) |
| `skills_excluded_from_wiki_root` | list of strings | each must match an existing skill | each must have a documented exclusion rationale (D8 §8.6) | meta-agent (lint check) |

### 7.4 `$WIKI_ROOT` resolution algorithm

The 5 in-scope skills (D8) run this exact algorithm at startup, before
any Read/Write to `wiki/` or `swarm/wiki/`:

```
# pseudo-code (executed by every D8 skill at startup)
fn resolve_wiki_root(skill_invocation):
    config := read_yaml(".claude/config/wiki-roots.yaml")

    # Precedence (highest first):
    # 1. Per-invocation env override — `WIKI_ROOT=...` in shell env at skill launch
    # 2. Per-skill flag override — `--wiki-root=v2|v3` on the command line
    # 3. Config default — `default_root` key resolves to `wiki_root_v2` or `wiki_root_v3`
    # 4. Hard-coded fallback — "swarm/wiki" (matches D1 v3 root)

    if env("WIKI_ROOT") is set:
        return env("WIKI_ROOT")
    if cli_flag("--wiki-root") in {"v2", "v3"}:
        return config["wiki_root_" + cli_flag_value]
    # Closes critic-gate2 H4 dead-code check: previous version tested
    # `config["default_root"] in config` which is always true (the
    # value of default_root is a key by schema). Correct check is:
    # does the *value pointed to by* default_root resolve to a configured root?
    if config["default_root"] not in {"wiki_root_v2", "wiki_root_v3"}:
        log "ERROR: default_root must be wiki_root_v2 or wiki_root_v3, got {config[default_root]}"
        exit 3
    return config[config["default_root"]]   # config["wiki_root_v2"] or config["wiki_root_v3"]
    # No hard-coded fallback — schema guarantees default_root resolves;
    # if config file is missing/malformed, the YAML parser exits earlier.

fn assert_root_writable(root, skill_name):
    # Honour v2_status / v3_status read-only flags
    status_key := if root == config["wiki_root_v2"] then "v2_status" else "v3_status"
    if config[status_key] == "read-only" and skill_writes_to_wiki(skill_name):
        log "Refusing to write to {root}: {status_key} = read-only"
        exit 2
```

The algorithm is **stateless** (re-runs at every skill invocation; no
caching between sessions). This honours the Max-subscription discipline
(D6 §6.10 — no SDK calls; pure filesystem read).

### 7.5 Worked example (Стадия D verification)

After Стадия D writes the file, a brigadier session running `/ingest`
sees:

```bash
$ unset WIKI_ROOT          # no env override
$ cd ~/jetix-os
$ # /ingest internally calls resolve_wiki_root() → reads default_root → "wiki_root_v3" → "swarm/wiki"
$ # → /ingest writes to swarm/wiki/sources/<...>.md
```

Backwards-compatibility test:

```bash
$ WIKI_ROOT=wiki /ingest raw/articles/foo.md   # explicit v2 ingest
$ # → /ingest writes to wiki/sources/<...>.md
```

Per-flag test:

```bash
$ /ingest --wiki-root=v2 raw/articles/foo.md   # explicit v2 via flag
$ # → /ingest writes to wiki/sources/<...>.md
```

### 7.6 Compatibility matrix

| Locked item | D7 honours by … |
|---|---|
| Q9 coexist + parameterize | `wiki_root_v2` + `wiki_root_v3` both present; `default_root` controls new behaviour. |
| R3 v2 untouched, v3 added | `v2_status: read-write` keeps v2 ingestible (per Sub-agent A §1 Q9 — v2 ingestion not frozen); `default_root: wiki_root_v3` routes new content to v3. |
| T1 cross-tree separation | `edges_cross_tree` path explicitly distinct from `edges_v2`/`edges_v3`. |
| Sub-agent A §1 Q9 applicability constraint | `migration_phase: A` documented; Phase-B re-eval trigger noted. |
| Master synthesis §5.10 6-skill inferred set | `skills_in_scope_for_wiki_root` lists 5 (`ingest/ask/lint/consolidate/build-graph`) per D's audit; `skills_excluded` lists 3 with rationale (search-kb / sweep-notion-bank explicit per §5.10; compile per D's §4.6 deprecation). Total 5 in-scope, not 6 — see D8 §8.1 reconciliation. |
| Max-subscription (D6 §6.10) | resolution algorithm is pure filesystem read; no API calls; no embeddings. |
| 24-Lock 17 (Filesystem = SoT) | this file lives at `.claude/config/wiki-roots.yaml`; filesystem is the source of truth. |

---

## DELIVERABLE 8 — Skill Edit Diffs (5 in-scope skills + 3 documented exclusions)

### 8.1 Mandate, scope reconciliation, and edit budget

The prompt §6 D8 mandates concrete edit diffs for "6 skills targeted
(`/ingest`, `/ask`, `/lint`, `/compile`, `/consolidate`, `/build-graph`)."
Sub-agent D §4 audit revealed `/compile` (50 lines) targets legacy
`knowledge-base/`, NOT `wiki/`. Sub-agent D §7 transplant table
recommendation: "drop (or rewrite); Targets legacy knowledge-base/;
supplanted by /ingest + /ask in v2." Sub-agent E §4 confirms `/compile`'s
inclusion in the 6-skill list is inferred (master synthesis §5.10
itself does not name 6).

**Resolution.** This deliverable scopes to **5 in-scope skills** for
`$WIKI_ROOT` parameterisation (`/ingest`, `/ask`, `/lint`,
`/consolidate`, `/build-graph`) and **3 documented exclusions**
(`/search-kb`, `/sweep-notion-bank`, `/compile`). The 6→5 reduction
honours the audit (no point parameterising a skill that doesn't read
`wiki/` at all) and is the cleaner Стадия-D landing. If Ruslan wants
`/compile` rewritten for v3 KB target, escalate as a follow-up
`AWAITING-APPROVAL-compile-v3-rewrite-*.md` after Стадия D ships.

**Edit budget per Sub-agent D §4 audit + ~9-line `$WIKI_ROOT` resolution
preamble per skill:**

| Skill | Total lines (current) | Path-line replacements | Prose tweaks | New `$WIKI_ROOT` preamble | Total per-skill lines changed | Cumulative |
|---|---|---|---|---|---|---|
| /ingest | 135 | 7 | 2 | 9 | 18 | 18 |
| /ask | 116 | 7 | 2 | 9 | 18 | 36 |
| /lint | 103 | 7 | 2 | 9 | 18 | 54 |
| /consolidate | 96 | 8 | 2 | 9 | 19 | 73 |
| /build-graph | 97 | 5 | 2 | 9 | 16 | 89 |

Total: **89 substantive lines changed across 5 files** (matches
Sub-agent D §4.8 estimate of ~85 ± rounding; matches prompt §6 D8 budget).

### 8.2 Shared `$WIKI_ROOT` resolution preamble (inserted into each in-scope skill)

Every in-scope skill receives the following 9-line block immediately
after its frontmatter (before `# Skill: /...`). The preamble is
**identical** across all 5 skills — Стадия D copy-pastes verbatim.

```markdown
> **`$WIKI_ROOT` resolution (D7).** This skill reads
> `.claude/config/wiki-roots.yaml` at startup and resolves the wiki
> root via the algorithm in D7 §7.4. All `wiki/`-prefixed paths in
> the algorithm below MUST be read as `${WIKI_ROOT}/...`. The default
> root is `swarm/wiki/` (v3) per D7 `default_root: wiki_root_v3`. To
> target v2, set `WIKI_ROOT=wiki` env var or pass `--wiki-root=v2`.
> Cross-tree edges (v3→v2 only) land in
> `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` per D3 §3.2.12 + T1.
```

(Counted as 9 lines including the blank line before `# Skill:`.)

### 8.3 `/ingest` skill diff (`.claude/skills/ingest.md`, 135 lines → +18 = 153 lines)

**Audit baseline:** Sub-agent D §4.1 — 7 substantive `wiki/` paths at
lines 62, 65, 71, 78, 90, 100, 111; 2 prose mentions at lines 3, 15.

**Per-edit table:**

| # | Line range | Before (current) | After (v3) | Rationale |
|---|---|---|---|---|
| 1 | after L5 (insert) | (frontmatter ends at L5) | insert §8.2 preamble (9 lines) | wires `$WIKI_ROOT` resolution at skill entry |
| 2 | L3 (frontmatter description) | `description: "Поднять источник из raw/ (или по URL) в wiki/: распарсить, создать entity-страницы, обновить index/log/edges."` | `description: "Поднять источник из raw/ (или по URL) в ${WIKI_ROOT}/: распарсить, создать entity-страницы, обновить index/log/edges. (Default root: swarm/wiki per D7.)"` | prose alignment — surfaces parameterisation in the skill description |
| 3 | L15 (description body) | `Превратить сырой источник (файл в \`raw/\` или URL) в связанный набор страниц wiki/.` | `Превратить сырой источник (файл в \`raw/\` или URL) в связанный набор страниц \`${WIKI_ROOT}/\`.` | prose alignment |
| 4 | L62 | `1. Построить путь: \`wiki/{type}/{slug}.md\`.` | `1. Построить путь: \`${WIKI_ROOT}/{type}/{slug}.md\`.` | path parameterisation |
| 5 | L65 | `3. Если нет → взять шаблон из \`wiki/_templates/{type}.md\`, заполнить.` | `3. Если нет → взять шаблон из \`${WIKI_ROOT}/_templates/{type}.md\`, заполнить.` | path parameterisation |
| 6 | L71 | `\`wiki/sources/YYYY-MM-DD-slug.md\` по шаблону \`source.md\`:` | `\`${WIKI_ROOT}/sources/YYYY-MM-DD-slug.md\` по шаблону \`source.md\`:` | path parameterisation |
| 7 | L78 | `### 6. Добавить edges в \`wiki/graph/edges.jsonl\`` | `### 6. Добавить edges в \`${WIKI_ROOT}/graph/edges.jsonl\` (v3 intra-tree). Для v3→v2 ссылок — `${WIKI_ROOT_V3}/graph/cross-tree.jsonl` (D3 §3.2.12 + T1).` | path parameterisation + cross-tree extension |
| 8 | L80–L82 (edge type list) | `Append-only. Один JSON на строку. 9 типов: \`extends\`, \`contradicts\`, \`supports\`, \`inspired_by\`, \`tested_by\`, \`invalidates\`, \`supersedes\`, \`addresses_gap\`, \`derived_from\`.` | `Append-only. Один JSON на строку. **12 типов per D3 §3.2** (10 intra-layer + 3 cross-layer): \`extends, contradicts, supports, inspired_by, tested_by, invalidates, supersedes, derived_from, part_of, alpha-ref, layer-ref, cross-tree-ref\`. (\`addresses_gap\` dropped per critic-gate1 H4.)` | edge enum alignment with D3 |
| 9 | L90 | `### 7. Обновить \`wiki/index.md\`` | `### 7. Обновить \`${WIKI_ROOT}/index.md\`` | path parameterisation |
| 10 | L100 | `### 8. Добавить в \`wiki/log.md\` (сверху)` | `### 8. Добавить в \`${WIKI_ROOT}/log.md\` (сверху)` | path parameterisation |
| 11 | L111 | `В \`wiki/niches/{niche}/README.md\` в секцию \`## Pages\` добавить линк на новые страницы.` | `В \`${WIKI_ROOT}/niches/{niche}/README.md\` в секцию \`## Pages\` добавить линк на новые страницы. (Niche enum: 6 values per CLAUDE.md L70 lock — \`personal/business/sales/life/tech/meta\`; \`global\` removed per critic-gate1 S3.)` | path parameterisation + niche-enum correction (also fixes L45 implicit reference) |
| 12 | L45 (niche enum) | `Прочитать содержимое. Выбрать одну из: \`personal\`, \`business\`, \`sales\`, \`life\`, \`tech\`, \`meta\`, \`global\`.` | `Прочитать содержимое. Выбрать одну из: \`personal\`, \`business\`, \`sales\`, \`life\`, \`tech\`, \`meta\`. (6 niches per CLAUDE.md L70 lock; \`global\` content lives in Layer 7 \`${WIKI_ROOT}/global/\` per D1.)` | niche enum alignment |

**Net edits:** 11 line edits (12 numbered above; #1 is insertion-only,
not replacement). Combined with the 9-line preamble, the file grows
~15 lines net (some prose lines lengthen, no lines deleted).

**Behaviour after edit.** /ingest reads `.claude/config/wiki-roots.yaml`
at startup, resolves `$WIKI_ROOT` to `swarm/wiki/` by default, writes
all entity pages and updates index/log/edges under that root. Edge
types align with D3 12-enum.

**Test plan.** (1) `unset WIKI_ROOT && /ingest raw/articles/foo.md` →
expect `swarm/wiki/sources/<…>.md` written. (2) `WIKI_ROOT=wiki
/ingest raw/articles/foo.md` → expect `wiki/sources/<…>.md` written
(v2 backward-compat). (3) `/ingest raw/v3-test.md` should add an edge
to `swarm/wiki/graph/edges.jsonl` (not v2 `wiki/graph/edges.jsonl`).

### 8.4 `/ask` skill diff (`.claude/skills/ask.md`, 116 lines → +18 = 134 lines)

**Audit baseline:** Sub-agent D §4.2 — 7 substantive paths at L20, 27,
28, 29, 60, 71, 100; 2 prose at L3, 11.

**Per-edit table:**

| # | Line range | Before | After | Rationale |
|---|---|---|---|---|
| 1 | after L5 (insert) | (frontmatter ends at L5) | insert §8.2 preamble (9 lines) | wires `$WIKI_ROOT` resolution |
| 2 | L3 | `description: "Ответить на вопрос по wiki/: подобрать 5-15 страниц, синтезировать с цитатами, сохранить ценный ответ в comparisons/."` | `description: "Ответить на вопрос по \`${WIKI_ROOT}/\` (default v3): подобрать 5-15 страниц, синтезировать с цитатами, сохранить ценный ответ в \`${WIKI_ROOT}/comparisons/\`."` | prose alignment |
| 3 | L11 | `Ответить на содержательный вопрос пользователя по накопленной wiki/.` | `Ответить на содержательный вопрос пользователя по накопленной \`${WIKI_ROOT}/\`.` | prose |
| 4 | L20 | `### 1. Прочитать \`wiki/index.md\`` | `### 1. Прочитать \`${WIKI_ROOT}/index.md\`` | path |
| 5 | L27 | `- При необходимости — grep по ключевым словам вопроса в \`wiki/**/*.md\`.` | `- При необходимости — grep по ключевым словам вопроса в \`${WIKI_ROOT}/**/*.md\`.` | path |
| 6 | L28 | `- Смотри niche: если вопрос явно про sales — приоритет \`wiki/niches/sales/\` и страниц с \`niche: sales\`.` | `- Смотри niche: если вопрос явно про sales — приоритет \`${WIKI_ROOT}/niches/sales/\` и страниц с \`niche: sales\`.` | path |
| 7 | L29 | `- Если есть community summaries (\`wiki/graph/summaries.md\`) — используй их для быстрого контекста.` | `- Если есть community summaries (\`${WIKI_ROOT}/graph/summaries.md\`) — используй их для быстрого контекста. (Tier 4 long-context fallback per Q1: scope to current niche dir, not full wiki.)` | path + Q1 Tier-4 alignment |
| 8 | L60 | `**Сохранить в \`wiki/comparisons/\`** если ответ:` | `**Сохранить в \`${WIKI_ROOT}/comparisons/\`** если ответ:` | path |
| 9 | L71 | `\`wiki/comparisons/YYYY-MM-DD-question-slug.md\`:` | `\`${WIKI_ROOT}/comparisons/YYYY-MM-DD-question-slug.md\`:` | path |
| 10 | L100 | `Добавить edges в \`wiki/graph/edges.jsonl\`.` | `Добавить edges в \`${WIKI_ROOT}/graph/edges.jsonl\` per D3 12-enum. Cross-tree refs (v3→v2) → \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\` per T1.` | path + cross-tree |

**Net edits:** 9 line edits + 9-line preamble = 18 lines changed.

**Behaviour after edit.** /ask reads `$WIKI_ROOT/index.md` first
(Karpathy Tier-2), then `$WIKI_ROOT/niches/<niche>/`, then
typed-BFS over `$WIKI_ROOT/graph/edges.jsonl` (Q1 Tier-3), then
long-context fallback bounded to niche dir (Q1 Tier-4). Comparisons
and edges land in the right tree.

**Test plan.** (1) Default-root: `/ask "что такое 4-tier retrieval"` →
reads `swarm/wiki/index.md` first; comparisons land in
`swarm/wiki/comparisons/`. (2) `WIKI_ROOT=wiki /ask "что такое
4-tier retrieval"` → reads `wiki/index.md`; comparisons land in
`wiki/comparisons/`.

### 8.5 `/lint` skill diff (`.claude/skills/lint.md`, 103 lines → +18 = 121 lines)

**Audit baseline:** Sub-agent D §4.3 — 7 substantive paths at L21, 30,
38, 55, 60, 92, 102; 2 prose at L3, 11.

**Per-edit table:**

| # | Line range | Before | After | Rationale |
|---|---|---|---|---|
| 1 | after L5 (insert) | (frontmatter ends at L5) | insert §8.2 preamble (9 lines) | wires `$WIKI_ROOT` |
| 2 | L3 | `description: "Health check wiki/: 7 проверок..."` | `description: "Health check \`${WIKI_ROOT}/\` (default v3): 5-signal /lint orchestration per Q5 + structural checks (orphans, stale, broken links, missing frontmatter, contradictions, missing cross-refs, index drift)."` | prose + Q5 5-signal alignment |
| 3 | L11 | `Проверка целостности wiki/.` | `Проверка целостности \`${WIKI_ROOT}/\`.` | prose |
| 4 | L21 | `Страницы, на которые никто не ссылается (нет входящих \`[[links]]\` и нет в \`wiki/graph/edges.jsonl\`).` | `Страницы, на которые никто не ссылается (нет входящих \`[[links]]\` и нет в \`${WIKI_ROOT}/graph/edges.jsonl\`).` | path |
| 5 | L30 | `\`wiki/claims/*.md\` где \`confidence: low\` И \`updated:\` старше 60 дней от сегодня.` | `\`${WIKI_ROOT}/claims/*.md\` где \`confidence: low\` И \`updated:\` старше 60 дней от сегодня. **Дополнительно: \`${WIKI_ROOT}/foundations/*.md\` где \`last_reviewed:\` старше 365 дней (Q5 §3 + D2 §2.3 foundations re-review).**` | path + Q5 §3 365-day re-review for foundations |
| 6 | L38 | `Markdown в \`wiki/**/*.md\` без обязательных полей: \`title\`, \`type\`, \`niche\`, \`created\`, \`updated\`, \`pipeline\`.` | `Markdown в \`${WIKI_ROOT}/**/*.md\` без обязательных полей per D2 §2.2 cross-layer table: \`id, title, type, layer, niche, created, last_modified, pipeline, state, confidence, tier, produced_by, sources, related, topics, captured_by, captured_date\`.` | path + full D2 cross-layer field list |
| 7 | L55 | `- Файл есть в wiki/, но его нет в \`index.md\` (в соответствующей секции).` | `- Файл есть в \`${WIKI_ROOT}/\`, но его нет в \`index.md\` (в соответствующей секции).` | path |
| 8 | L60 | `\`wiki/_lint-report-YYYY-MM-DD.md\`:` | `\`${WIKI_ROOT}/_lint-report-YYYY-MM-DD.md\`:` | path |
| 9 | L92 | `- wiki/concepts/foo.md → [[bar]] (нет такого файла)` | `- ${WIKI_ROOT}/concepts/foo.md → [[bar]] (нет такого файла)` | path (in example) |
| 10 | L102 | `- Добавить запись в \`wiki/log.md\`:` | `- Добавить запись в \`${WIKI_ROOT}/log.md\`:` | path |
| 11 | (after L17 "Проверки") | (existing 7 checks) | **NEW SECTION:** "### 8. α-2/α-3 lifecycle state validity (per Q5 signal #2)" — for skill pages (path under `${WIKI_ROOT}/skills/` OR `type: skill`): flag pages with `state ∉ {candidate, learning, active, tombstoned}` (α-3 4-state lock per critic-gate1 S2 + D2 §2.4). For all other pages: flag pages with `state ∉ {drafted, reviewed, revised, accepted, referenced, superseded, retired, tombstoned}` (α-2 8-state set). Branching closes critic-gate2 M3. "### 9. Triple-channel cross-ref consistency (per D2 §2.2 lint #5)" — every inline wikilink matching the regex `\[\[(?P<type>[a-z]+)/(?P<slug>[a-z0-9-]+)\]\]` (closes critic-gate2 H5; non-matching forms like `[[A]]` or `[[file.md]]` are **warned** as legacy/unparseable, not errored) MUST appear in `related[]` AND produce one record in `${WIKI_ROOT}/graph/edges.jsonl`. "### 10. Q8 Layer-9 lock (per D1 §1.6)" — flag the existence of any file under `${WIKI_ROOT}/insights/{candidates,promoted}/*.md` (i.e. any leaf `.md` write outside `README.md`) when D1 §1.6 boilerplate is in effect (closes critic-gate2 H6 by testing file-presence rather than a frontmatter field that D1 §1.6 didn't define). | extends /lint to cover Q5 5-signal + Q3 triple-channel reconciliation + Q8 lock per D2 + D3 |

**Net edits:** 10 line edits + new sections (~15 lines) + 9-line
preamble = ~34 lines added/changed. Slightly above the audit's
estimate because /lint absorbs the Q5 5-signal and triple-channel
enforcement. Acceptable inflation; the alternative is a separate
/lint-v3 skill which would violate the parameterisation principle.

**Behaviour after edit.** /lint runs the original 7 v2 checks +
3 new v3 checks (α-2/α-3 lifecycle, triple-channel consistency, Q8
lock). Reports land in `$WIKI_ROOT/_lint-report-<date>.md`.

**Test plan.** (1) Default-root: `/lint` → walks `swarm/wiki/`,
emits report at `swarm/wiki/_lint-report-2026-04-23.md`. (2) Set up
a draft page with `[[concepts/foo]]` body wikilink but missing
`related[]`/edges entry; expect /lint to flag it under check #9. (3)
Try writing `swarm/wiki/insights/candidates/test.md` with
`phase_a_lock: true` → expect /lint to reject under check #10.

### 8.6 `/consolidate` skill diff (`.claude/skills/consolidate.md`, 96 lines → +19 = 115 lines)

**Audit baseline:** Sub-agent D §4.4 — 8 substantive paths at L36, 37,
68, 70, 73, 76, 80, 81; 2 prose at L3, 11.

**Per-edit table:**

| # | Line range | Before | After | Rationale |
|---|---|---|---|---|
| 1 | after L5 (insert) | (frontmatter ends at L5) | insert §8.2 preamble (9 lines) | wires `$WIKI_ROOT` |
| 2 | L3 | `description: "Найти дубликаты в wiki/ и предложить merge..."` | `description: "Найти дубликаты в \`${WIKI_ROOT}/\` (default v3) и предложить merge..."` | prose |
| 3 | L11 | `Объединение дубликатов в wiki/.` | `Объединение дубликатов в \`${WIKI_ROOT}/\`.` | prose |
| 4 | L36 | `  A: wiki/concepts/value-based-pricing.md (4 sources, 120 lines)` | `  A: ${WIKI_ROOT}/concepts/value-based-pricing.md (4 sources, 120 lines)` | path (in example) |
| 5 | L37 | `  B: wiki/concepts/value-pricing.md (2 sources, 80 lines)` | `  B: ${WIKI_ROOT}/concepts/value-pricing.md (2 sources, 80 lines)` | path (in example) |
| 6 | L68 | `   - Обновить \`wiki/graph/edges.jsonl\`: где \`from: B\` → \`from: A\`, где \`to: B\` → \`to: A\`` | `   - Обновить \`${WIKI_ROOT}/graph/edges.jsonl\`: где \`from: B\` → \`from: A\`, где \`to: B\` → \`to: A\`. **Также пройти по \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\` для v3-сторонних ссылок на B.**` | path + cross-tree handling per T1 |
| 7 | L70 | `   - Обновить \`wiki/index.md\`: убрать строку B, обновить A.` | `   - Обновить \`${WIKI_ROOT}/index.md\`: убрать строку B, обновить A.` | path |
| 8 | L73 | `   - Перед удалением — создать копию в \`wiki/_archive/YYYY-MM-DD-B.md\` (с комментом "merged into A").` | `   - Перед удалением — создать копию в \`${WIKI_ROOT}/_archive/YYYY-MM-DD-B.md\` (с комментом "merged into A"). **Per critic-gate2 SS3: this skill runs as expert (D6 §6.6.3 role_tool_matrix) and CANNOT mutate canonical α-2 `state` field — that requires brigadier per Q2/D6 §6.2. /consolidate writes the `_archive/` copy with the original frontmatter unchanged + appends an HTML comment `<!-- merged into A on YYYY-MM-DD per /consolidate; α-2 state transition pending brigadier review -->`. The brigadier subsequently transitions α-2 `state: superseded` + `superseded_by: [[<A-path>]]` per D5 §5.3 movers (separate commit).**` | path + α-2 ownership clarification (closes critic-gate2 SS3) |
| 9 | L76 | `5. Залогировать в \`wiki/log.md\` (сверху):` | `5. Залогировать в \`${WIKI_ROOT}/log.md\` (сверху):` | path |
| 10 | L80 | `   A: wiki/concepts/value-based-pricing.md` | `   A: ${WIKI_ROOT}/concepts/value-based-pricing.md` | path (in example) |
| 11 | L81 | `   B (archived): wiki/_archive/YYYY-MM-DD-value-pricing.md` | `   B (archived): ${WIKI_ROOT}/_archive/YYYY-MM-DD-value-pricing.md` | path (in example) |

**Net edits:** 10 line edits + 9-line preamble = 19 lines changed.

**Behaviour after edit.** /consolidate operates within `$WIKI_ROOT`,
moves losers to `$WIKI_ROOT/_archive/`, sets α-2 state correctly,
and updates BOTH `edges.jsonl` AND `cross-tree.jsonl` (the latter
when the loser had inbound v3→v2 cross-refs).

**Test plan.** (1) Set up duplicate `swarm/wiki/concepts/foo.md` and
`swarm/wiki/concepts/foo-v2.md`; run `/consolidate` → on `y`,
loser moves to `swarm/wiki/_archive/`, frontmatter shows `state:
superseded` + `superseded_by:`. (2) If a v3→v2 cross-tree-ref pointed
at the loser, verify the cross-tree.jsonl record is rewritten to
point at the survivor.

### 8.7 `/build-graph` skill diff (`.claude/skills/build-graph.md`, 97 lines → +16 = 113 lines)

**Audit baseline:** Sub-agent D §4.5 — 5 substantive paths at L22, 33,
62, 73, 86; 2 prose at L3, 11.

**Per-edit table:**

| # | Line range | Before | After | Rationale |
|---|---|---|---|---|
| 1 | after L5 (insert) | (frontmatter ends at L5) | insert §8.2 preamble (9 lines) | wires `$WIKI_ROOT` |
| 2 | L3 | `description: "Пройти по wiki/, добить недостающие edges в edges.jsonl, пересчитать communities + summaries."` | `description: "Пройти по \`${WIKI_ROOT}/\` (default v3), добить недостающие edges в edges.jsonl per D3 12-enum, пересчитать communities + summaries. Поддерживает \`--tree {v2|v3|both}\` per T1."` | prose + tree-flag |
| 3 | L11 | `Обновить граф знаний поверх wiki/.` | `Обновить граф знаний поверх \`${WIKI_ROOT}/\`.` | prose |
| 4 | L22 | `Glob \`wiki/**/*.md\`, исключить \`index.md\`, \`log.md\`, \`overview.md\`, \`_templates/*\`, \`niches/*/README.md\`, \`graph/*\`, \`_archive/*\`, \`_lint-report-*\`.` | `Glob \`${WIKI_ROOT}/**/*.md\`, исключить \`index.md\`, \`log.md\`, \`overview.md\`, \`_templates/*\`, \`niches/*/README.md\`, \`graph/*\`, \`_archive/*\`, \`_lint-report-*\`. **При \`--tree=both\`: повторить glob для v2 \`wiki/**/*.md\` и v3 \`swarm/wiki/**/*.md\`; cross-tree-ref edges (D3 §3.2.12) пишутся в \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\`.**` | path + tree-flag impl |
| 5 | L33 | `Прочитать \`wiki/graph/edges.jsonl\` в память (set по \`(from, to, type)\`).` | `Прочитать \`${WIKI_ROOT}/graph/edges.jsonl\` в память (set по \`(from, to, type)\`). При \`--tree=both\` — также \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\`.` | path + tree-flag |
| 6 | L37–L46 (edge type detection) | (current section-header → 9 v2 types) | **Update to D3 12-enum:** "Расширяет/Extends → \`extends\`. Противоречит/Contradicts → \`contradicts\` (запись BIDIRECTIONAL — обе стороны записать). Поддерживает/Supports → \`supports\`. Вдохновлён/Inspired by → \`inspired_by\`. Тестируется/Tested by → \`tested_by\`. Опровергает/Invalidates → \`invalidates\`. Заменяет/Supersedes → \`supersedes\`. Часть/Part of → \`part_of\` (FORMALIZED per Q3). Иначе (упоминание сущности) → \`derived_from\`. Cross-layer (5×4 matrix→alpha tracker) → \`alpha-ref\`. Cross-layer (theme → global pattern) → \`layer-ref\`. v3→v2 link → \`cross-tree-ref\` (запись в cross-tree.jsonl, не edges.jsonl). **Снят: \`addresses_gap\` per critic-gate1 H4.**" | edge enum alignment with D3; bidirectional contradicts; cross-tree separation |
| 7 | L62 | `### 5. Обновить \`wiki/graph/communities.md\`` | `### 5. Обновить \`${WIKI_ROOT}/graph/communities.md\`` | path (corrected per critic-gate2 SS2 — L62 is the actual communities line, not L60) |
| 8 | L73 | `### 6. Обновить \`wiki/graph/summaries.md\`` | `### 6. Обновить \`${WIKI_ROOT}/graph/summaries.md\`` | path |
| 9 | L86 | `В \`wiki/log.md\` (сверху):` | `В \`${WIKI_ROOT}/log.md\` (сверху):` | path |

**Net edits:** 5 path replacements + edge-type-detection rewrite (~10
lines) + 9-line preamble = ~24 lines changed (slightly above audit's 16).
The /build-graph extension absorbs D3's 12-enum migration and T1
cross-tree separation — both load-bearing for Q5 staleness signal #4
(contradiction-edge integrity) and Q1 Tier-3 retrieval.

**Behaviour after edit.** /build-graph walks `$WIKI_ROOT/`, detects
edge types per the D3 12-enum (with bidirectional `contradicts`),
writes intra-tree edges to `$WIKI_ROOT/graph/edges.jsonl`, writes
cross-tree edges to `$WIKI_ROOT_V3/graph/cross-tree.jsonl` (when
`--tree=both`), recomputes communities + summaries.

**Test plan.** (1) Default-root: `/build-graph` → walks
`swarm/wiki/`, emits edges to `swarm/wiki/graph/edges.jsonl`. (2)
`/build-graph --tree=both` → walks both trees; cross-tree-refs land
in `swarm/wiki/graph/cross-tree.jsonl`. (3) Verify a `contradicts`
edge written from page A to B also has the inverse B→A record.

### 8.8 Documented exclusions (3 skills NOT parameterised)

#### 8.8.1 `/search-kb` (38 lines) — **out of scope**

- **Path:** `.claude/skills/search-kb.md`.
- **Audit (Sub-agent D §4.7):** zero `wiki/` references; targets
  `knowledge-base/_index.md`, `knowledge-base/{cluster}/_moc.md`,
  `knowledge-base/`, `raw/`. Legacy KB lookup.
- **Exclusion source:** master synthesis §5.10 explicitly excludes
  `/search-kb` from wiki skills (per prompt §6 D8).
- **Disposition:** keep as-is for legacy use. Supplanted by `/ask`
  Tier-1/2 retrieval per Q1. No `$WIKI_ROOT` parameterisation
  required because the skill never touches `wiki/` or `swarm/wiki/`.
- **Future option (Phase B):** deprecate when `knowledge-base/`
  migration completes (per CLAUDE.md MIGRATION.md note); not in
  Phase A scope.

#### 8.8.2 `/sweep-notion-bank` (110 lines) — **out of scope**

- **Path:** `.claude/skills/sweep-notion-bank.md`.
- **Audit (Sub-agent D §4.8):** 5 substantive `wiki/` references at
  L29, 51, 72, 73, 77; one-shot Notion-import bound to specific date
  (2026-04-16) and specific Notion DB ID (bf0e9a11-0e6f-4717-9ae5-…).
- **Exclusion source:** master synthesis §5.10 explicitly excludes
  per prompt §6 D8.
- **Disposition:** keep as-is. Re-running for v3 would require full
  rewrite (different DB, different sweep date), not just
  parameterisation. If Ruslan later needs a v3 Notion sweep, escalate
  as `AWAITING-APPROVAL-sweep-notion-bank-v3-*.md`.

#### 8.8.3 `/compile` (50 lines) — **deprecated, out of scope**

- **Path:** `.claude/skills/compile.md`.
- **Audit (Sub-agent D §4.6):** zero `wiki/` references; targets
  `knowledge-base/{cluster}/_moc.md` and `knowledge-base/{cluster}/{topic}.md`.
  Legacy pre-v2 skill that synthesises raw → KB-article.
- **Exclusion source:** Sub-agent D §7 transplant table:
  "drop (or rewrite); Targets legacy knowledge-base/; supplanted by
  `/ingest` + `/ask` in v2."
- **Disposition:** **deprecate.** Emit a Phase-A deprecation note in
  `swarm/wiki/log.md` at Стадия D bootstrap:
  `## [2026-04-XX] deprecate | /compile | superseded by /ingest + /ask
  per Sub-agent D §7 + D8 §8.6.3`. The skill file is retained
  (kept for knowledge-base/ legacy use until `MIGRATION.md` finalises)
  but is not part of the v3 wiki-skill set.

### 8.9 Total edit budget verification

| Skill | Lines edited | Lines added (preamble) | Total per-skill | Cumulative |
|---|---|---|---|---|
| /ingest | 11 (incl. niche fix) | 9 | 20 | 20 |
| /ask | 9 | 9 | 18 | 38 |
| /lint | 10 + new sections (~15) | 9 | 34 | 72 |
| /consolidate | 10 | 9 | 19 | 91 |
| /build-graph | 5 + edge rewrite (~10) | 9 | 24 | 115 |

**Total: ~115 lines** (above prompt's ~85 estimate; the inflation
comes from /lint's Q5 5-signal absorption and /build-graph's D3
12-enum detection rewrite — both load-bearing semantic upgrades, not
optional polish). If Ruslan prefers a strict ~85-line budget, defer
the /lint Q5 5-signal extensions to a follow-up
`AWAITING-APPROVAL-lint-q5-extension-*.md`.

### 8.10 Compatibility matrix

| Locked item | D8 honours by … |
|---|---|
| Q9 + R3 (coexist + parameterize) | Every in-scope skill consumes `$WIKI_ROOT` from D7; defaults to v3 root; v2 still accessible via env/flag. |
| T1 (cross-tree separation) | /ingest, /consolidate, /build-graph all write cross-tree-ref records to `cross-tree.jsonl` (not `edges.jsonl`). |
| D3 (12-edge enum) | /ingest L80–L82 + /build-graph L37–L46 carry the D3 12-type vocabulary; `addresses_gap` dropped per critic-gate1 H4; bidirectional `contradicts`. |
| Q1 4-tier retrieval | /ask preamble + L29 long-context fallback bounded to niche dir. |
| Q5 5-signal /lint | /lint extended with α-2/α-3 lifecycle check + triple-channel consistency + Q8 Phase-A lock. |
| Q8 Layer-9 lock | /lint check #10 rejects writes under `insights/` when `phase_a_lock: true`. |
| Master synthesis §5.10 (skills inventory) | 5 in-scope skills match §5.10.2; 3 exclusions documented with source. |
| Max-subscription (D6 §6.10) | All edits are filesystem-only; no SDK, no embeddings, no third-party APIs. |
| Sub-agent D §4 audit + §7 transplant table | Per-skill edits match audit line numbers (cross-checked against actual file reads); /compile deprecation per D §7. |
| Critic-gate1 H4 (drop addresses_gap) | /ingest + /build-graph edge-type lists updated. |
| Critic-gate1 S3 (niche enum 6 not 7) | /ingest L45 niche-enum line corrected. |

---

## DELIVERABLE 9 — `.claude/skills/` Symlink Convention for v3 `active/<slug>.md`

### 9.1 Mandate

Per Q6 skill-learning pipeline + W-9 (skills first-class), when a skill
candidate is promoted from `swarm/wiki/skills/learning/<slug>/` to
`swarm/wiki/skills/active/<slug>.md`, the canonical content lives at
the v3 wiki path; Claude Code's runtime expects `.claude/skills/<slug>.md`
to be a real file (or a symlink resolving to one). This deliverable
specifies the **symlink convention** that bridges the two — the lifecycle
hooks integrated with α-3 transitions (D5 §5.4) and the lint signal
that surfaces broken symlinks.

### 9.2 Symlink rule (canonical form)

```
.claude/skills/<slug>.md  →  ../../swarm/wiki/skills/active/<slug>.md
```

**Relative path** (not absolute) for two reasons:

1. **Roy-replication discipline** (master synthesis §5.8.3 + Sub-agent
   E §8): "no hard-coded `/home/ruslan/*` paths." Absolute symlinks
   break when the repo is checked out elsewhere (e.g. on Ruslan's
   laptop, on a CI runner).
2. **Repo portability:** the relative target resolves correctly
   regardless of the absolute repo root.

`<slug>` is the same kebab-slug used as the file basename (D2 §2.4
`skill_slug` field) — one and only one canonical naming.

### 9.3 Filename normalisation

The `skill_slug` MUST satisfy:

- Regex `^[a-z0-9-]{1,60}$` — the body half of D2 §2.2 `id` regex
  (`^[a-z]+-[a-z0-9-]{1,60}$` where `[a-z]+-` is the type-prefix and
  `[a-z0-9-]{1,60}$` is the slug body). For skills the type-prefix is
  always `skill-`, so the `id` is `skill-<slug>` and the `<slug>`
  portion conforms to the body regex (closes critic-gate2 H1
  inconsistency with D2 §2.2 `id` format).
- Unique across `.claude/skills/` (no collision with v2 file names).
- Match the basename of `swarm/wiki/skills/active/<slug>.md` exactly.

Slug derivation rules:

- Single-word: lowercase as-is (`focus` → `focus`).
- Multi-word: hyphen-separated lowercase (`Build Graph` → `build-graph`).
- No spaces, no underscores, no uppercase, no extension in the slug
  itself (`.md` is always appended at file path resolution, never
  inside the slug).

### 9.4 Symlink creation step (α-3 `learning → validated` transition)

Triggered by D11 §11.4 activation predicate. Brigadier executes (per
D6 §6.2 single-writer rule):

```bash
# Pre-flight checks (brigadier verifies before symlink creation)
test -f swarm/wiki/skills/active/<slug>.md  || exit "no canonical"
test ! -e .claude/skills/<slug>.md          || exit "name collision; see §9.6"

# Create symlink (atomic via ln -s)
ln -s ../../swarm/wiki/skills/active/<slug>.md .claude/skills/<slug>.md

# Verify
readlink .claude/skills/<slug>.md         # should print "../../swarm/wiki/skills/active/<slug>.md"
test -f .claude/skills/<slug>.md          || exit "broken symlink"
```

This step is part of the brigadier's α-3 `active → validated`
transition mover (D5 §5.4). It is committed in the same commit as the
file move from `swarm/wiki/skills/learning/<slug>/manifest.md` to
`swarm/wiki/skills/active/<slug>.md` (commit message format per D6
§6.2.4).

### 9.5 Symlink removal step (α-3 `validated → tombstoned` transition)

Triggered by D11 §11.5 retirement / tombstoning predicates. Brigadier
executes:

```bash
# Pre-flight check
test -L .claude/skills/<slug>.md          || exit "not a symlink (or absent)"

# Remove symlink (file at canonical path is preserved by the α-3 mover; see D5 §5.4)
rm .claude/skills/<slug>.md

# Move canonical to _archive/ per α-3 tombstone transition
mv swarm/wiki/skills/active/<slug>.md \
   swarm/wiki/_archive/skills/<slug>.md
```

The skill's content file is **not deleted** (anti-pattern Sub-agent C
§8 #9: "never delete, only archive"). The symlink IS deleted because
Claude Code only registers active skills via the `.claude/skills/`
directory.

Note: per critic-gate1 S2 fix, α-3 has only 4 states
(proposed/active/validated/tombstoned). There is no separate `retired`
state requiring a different removal path; graceful supersession also
goes through tombstone (with a `supersedes:` edge from the successor
skill, per D3 §3.2.7).

### 9.6 Conflict handling — v2 skill collides with v3 promotion

The v2 `.claude/skills/` directory contains pre-v3 skills (per
Sub-agent D §4 audit: ingest, ask, lint, compile, consolidate,
build-graph, search-kb, sweep-notion-bank — 8 files; plus `close-day`,
`focus`, `plan-day` directories). When a v3 skill candidate's slug
collides with a v2 file:

**Step 1 — detect.** Brigadier checks: `test -e .claude/skills/<slug>.md`.
If true → collision.

**Step 2 — preserve v2.** Move the v2 file:

```bash
mv .claude/skills/<slug>.md  .claude/skills/<slug>_v2.md
```

The `_v2` suffix is the marker of a deprecated v2 skill retained for
audit. `/lint` flags `_v2`-suffixed files as deprecated (informational
only; not an error).

**Step 3 — create v3 symlink.** Per §9.4.

**Step 4 — record migration in frontmatter** of the v3 canonical file
(`swarm/wiki/skills/active/<slug>.md`). Per critic-gate2 H7 (D4
templates have no `## Migration note` body section schema), the
migration record lives in frontmatter, not body:

```yaml
migrated_from: .claude/skills/<slug>_v2.md      # path to preserved v2 file
migration_date: <YYYY-MM-DD>
migration_note: <one-line summary of v2→v3 differences>
```

`/lint` (per D8 §8.5 #4 missing-frontmatter) accepts `migrated_from`,
`migration_date`, `migration_note` as optional fields when present.

The 5 in-scope D8 skills (`/ingest`, `/ask`, `/lint`, `/consolidate`,
`/build-graph`) are NOT promoted via the v3 candidate→learning→active
pipeline — they were already v2 skills, parameterised in place per
D8 (their `.claude/skills/<slug>.md` files remain regular files, not
symlinks). Only **new** v3-born skills go through D9 promotion.

### 9.7 Audit signals — how `/lint` detects broken symlinks

`/lint` (per D8 §8.5 extension) gains a sub-check inside check #1
(structural):

```
For each .md file in .claude/skills/:
  if file is a symlink:
    target := readlink(file)
    if not file_exists(target):
      EMIT "broken symlink: .claude/skills/<slug>.md → <target>"
    if not target.startswith("../../swarm/wiki/skills/active/"):
      EMIT "symlink target outside active/: .claude/skills/<slug>.md → <target>"
    if not target.endswith("/<basename(file)>"):
      EMIT "symlink basename mismatch: .claude/skills/<slug>.md → <target>"
```

This catches three failure modes:

- Brigadier removed canonical without removing symlink (`broken symlink`).
- Symlink mistakenly points to `learning/` or `_archive/` (target
  outside `active/`).
- Slug rename happened on canonical without updating symlink
  (`basename mismatch`).

### 9.8 Worked example — full skill lifecycle

A new v3-born skill `query-pricing-models` proceeds:

1. **proposed** (α-3 entry). Compound step writes:
   `swarm/wiki/skills/candidates/query-pricing-models/manifest.md`.
   No symlink yet.

2. **active** (α-3 `learning`; spec alias). Brigadier moves
   `manifest.md` to `swarm/wiki/skills/learning/query-pricing-models/manifest.md`,
   creates `golden-set.jsonl` (per D11). Brigadier appends use events
   to `swarm/wiki/skills/usage/query-pricing-models.jsonl`.
   No symlink yet.

3. **validated** (α-3; D11 activation predicate satisfied). Brigadier:
   - Moves canonical: `mv swarm/wiki/skills/learning/query-pricing-models/manifest.md
     swarm/wiki/skills/active/query-pricing-models.md`.
   - Pre-flight (no v2 collision; new slug).
   - Creates symlink: `ln -s ../../swarm/wiki/skills/active/query-pricing-models.md
     .claude/skills/query-pricing-models.md`.
   - Updates `swarm/wiki/log.md` (per D6 §6.2.4 commit format).
   - Single commit covers all the above.

4. **tombstoned** (α-3; ratio drops <1:1 per D11 §11.5). Brigadier:
   - Removes symlink: `rm .claude/skills/query-pricing-models.md`.
   - Archives canonical: `mv swarm/wiki/skills/active/query-pricing-models.md
     swarm/wiki/_archive/skills/query-pricing-models.md`.
   - Records `tombstoned_by:` in the archived file's frontmatter.
   - Updates `swarm/wiki/log.md`.

### 9.9 Compatibility matrix

| Locked item | D9 honours by … |
|---|---|
| Q6 (skill-learning pipeline) | symlink lifecycle integrated with α-3 transitions per D5 §5.4. |
| W-9 (skills first-class) | active skills are first-class wiki entries at `swarm/wiki/skills/active/`; `.claude/skills/` is a symlink registry. |
| §5.5.5 provenance gate (D6 §6.3) | symlink creation deferred to brigadier per single-writer Q2; α-3 transition predicates verified before symlink. |
| Master synthesis §5.8.3 (Roy-replication) | relative symlinks (no absolute paths). |
| Sub-agent C §8 #9 (never-delete-only-archive) | `tombstoned` skills moved to `_archive/`, not `rm`-ed. |
| Critic-gate1 H7 (kebab-slug discipline) | §9.3 enforces kebab-slug regex; matches D2 `skill_slug` field. |
| Critic-gate1 S2 (α-3 4-state lock) | §9.5 acknowledges no `retired` state; supersession routes through `tombstoned` + `supersedes:` edge per D3 §3.2.7. |
| D8 §8.5 (`/lint` skill diffs) | §9.7 audit checks integrated into /lint check #1 structural. |

---

## DELIVERABLE 10 — `swarm/wiki/meta/health.md` Skeleton

### 10.1 Mandate

Per Q5 (5-signal /lint) + W-12 (1000% depth) + Q8 (Layer-9 trigger
metrics) + critic-gate1 H1/M10 (forward-reference fix), this
deliverable specifies the **initial content** of `swarm/wiki/meta/health.md`
as the swarm's self-monitoring dashboard. The file contains 8
sections, each with: definition, computation formula, source data,
threshold for alerting, and a structured-log scaffold for time-series
records.

### 10.2 File content (Стадия D writes verbatim)

**Singleton frontmatter exemption (closes critic-gate2 H2 + H3).** This
file (`swarm/wiki/meta/health.md`) is a **singleton dashboard** with
its own dedicated frontmatter schema, exempt from D2 §2.2 cross-layer
table extras-rejection. The 5 live-counter fields below
(`closed_cycles_count`, `active_skills_count`, `cross_theme_refs_count`,
`tombstone_rate_weekly`, `fpar_swarm_wide`) are dashboard-specific and
mutated by `/lint` + meta-agent per §10.8. Field types:

| Field | Type | Default | Mutated by | Bootstrap value |
|---|---|---|---|---|
| `closed_cycles_count` | int ≥ 0 | `0` | brigadier on α-4 closed (D5 §5.5) | `0` |
| `active_skills_count` | int ≥ 0 | `0` | brigadier on α-3 validated (D11 §11.4) | `0` |
| `cross_theme_refs_count` | int ≥ 0 | `0` | /build-graph post-pass (§10.2.3) | `0` |
| `tombstone_rate_weekly` | float ≥ 0 | `0` | weekly /lint (§10.2.4) | `0` |
| `fpar_swarm_wide` | float ∈ [0,1] OR null | `null` | /lint PostToolUse (§10.2.1) | `null` |

`binding_scope: swarm-wide` is also part of the singleton schema (the
field is defined in D2 §2.3 for `foundations/<slug>.md`; for
`meta/health.md` (type: dashboard) it's an opt-in extension declaring
the dashboard's authoritative scope; `/lint` accepts it on this
singleton).


````markdown
---
id: meta-health
title: Swarm Health Dashboard
type: dashboard
layer: spine
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
last_reviewed: 2026-04-23
pipeline: ready
state: accepted
confidence: high
confidence_method: brigadier-attested-with-3-supports
tier: core
produced_by: brigadier
sources:
  - {path: "design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md", range: "D10"}
related: [[foundations/swarm-alphas]]
topics: [[topics/swarm-observability-hub]]
binding_scope: swarm-wide
# Live counters (updated by /lint scheduled run + meta-agent weekly)
closed_cycles_count: 0
active_skills_count: 0
cross_theme_refs_count: 0
tombstone_rate_weekly: 0
fpar_swarm_wide: null
---

# Swarm Health Dashboard

Updated automatically by `/lint` (PostToolUse + scheduled weekly per
Q5 #5 cadence) and by `meta-agent` weekly review. **Do not hand-edit
the structured-log sections** — append-only.

## 1. FPAR — First-Pass Acceptance Rate

**Definition.** Fraction of `Task()` returns accepted by the brigadier
on the first try (no rework / no rejection / no retry) over a rolling
window.

**Window:** rolling 20 invocations per agent (per-cell FPAR); rolling
100 invocations swarm-wide (aggregate FPAR).

**Computation source.**
- Per-Task return packet `state` after brigadier evaluation:
  `accepted` (first try) → `accepted_first_pass: true`.
- Recorded in `swarm/logs/<cycle-id>/events.md` per /ingest (D1 §1.3).

**Formula:**
```
FPAR = count(accepted_first_pass=true in window) / count(total_invocations in window)
```

**Threshold for alert.** `< 0.80` (per Sub-agent A §1 Q1 applicability
constraint). Below threshold → Q1 4-tier retrieval may be inadequate;
re-evaluate at /ask FPAR or move to Phase B (PPR/HyDE/embeddings).

**Structured log (append-only):**
```yaml
fpar_log:
  - {date: 2026-04-23, window: swarm-100, value: null, n: 0, alert: false}
```

## 2. Cycles

**Definition.** α-4 Cycle counts (D5 §5.5) across all states.

**Sources.**
- `closed_cycles_count` — frontmatter field above; incremented at α-4
  `closed` transition (D5 §5.5).
- Open / running / integrating / gated / compounded counts — derived
  from grep over `swarm/wiki/tasks/*/decisions/` for `alpha_state:`.

**Formula:**
```
closed_cycles_count = count(cycle-log.md files in swarm/logs/)
open_cycles = count(tasks with alpha_state ∈ {opened, running, integrating, gated, compounded})
cycle_close_rate_weekly = count(cycle-log.md created in last 7 days) / 7
```

**Q8 Layer-9 trigger #1.** `closed_cycles_count ≥ 50` (per Q8 +
Sub-agent A §1 Q8); first of three AND-conditions.

**Threshold for alert.** open_cycles > 5 → brigadier write-queue
contention (per Sub-agent A §1 Q2 applicability constraint); evaluate
CRDT switch.

**Structured log:**
```yaml
cycles_log:
  - {date: 2026-04-23, closed: 0, open: 0, weekly_rate: 0.0, layer9_trigger_1: false}
```

## 3. Cross-theme references

**Definition.** Edges in `swarm/wiki/graph/edges.jsonl` where
`from.niche != to.niche` (cross-niche) OR
`from.layer == 1 AND to.layer == 1 AND from.theme != to.theme`
(cross-theme-within-Layer-1).

**Sources.** Computed by `/build-graph` post-pass.

**Formula:**
```
cross_theme_refs_count = count of edges in swarm/wiki/graph/edges.jsonl satisfying
  (from_page.niche != to_page.niche)
   OR
  (from_page.layer == 1 AND to_page.layer == 1
   AND from_page.theme != to_page.theme)
```

**Q8 Layer-9 trigger #2.** `cross_theme_refs_count ≥ 3` AND
`count(themes with ≥50 concepts each) ≥ 2`. Second of three
AND-conditions per Q8 + Sub-agent A §1 Q8.

**Tension T2 watch.** If `cross_theme_refs_count == 0` after 20 closed
cycles, re-evaluate Q8 signal #2 (per Sub-agent A §4 T2 resolution).

**Structured log:**
```yaml
cross_theme_log:
  - {date: 2026-04-23, count: 0, themes_with_50_concepts: 0, layer9_trigger_2: false}
```

## 4. Tombstone rate per layer

**Definition.** Pages transitioning to α-2 `tombstoned` state per layer
per week (D5 §5.3 + D2 §2.4).

**Sources.** Grep `swarm/wiki/_archive/` for files with
`state: tombstoned` AND `last_modified` within the last 7 days; group
by source `layer` field.

**Formula:**
```
tombstone_rate_weekly[<layer>] = count(_archive files
  with state=tombstoned AND layer=<layer>
  AND last_modified in last 7 days) / 7
```

**Per-layer thresholds for alert (heuristic, Phase A):**

| Layer | Weekly threshold (alert if exceeded) | What it means |
|---|---|---|
| spine entity-types | 5 | high contradiction noise; review /ask synthesis quality |
| L1 themes | 2 | book-distillation churn; review brigadier sweep quality |
| L4 meta/agent-improvements | 1 | cross-agent improvement instability |
| L5 tasks (per-task content) | 2 (most tasks archive in place via α-1 `archived` rather than α-2 tombstone; high tombstone rate signals task-quality issues — closes critic-gate2 M6 — α-2 `tombstoned` is permitted on any layer per D5 §5.3) | |
| L7 global | 1 | promoted-rule churn; review compound step |
| L8 skills | 1 | pipeline leak; check D11 activation rubric |
| L9 insights | 0 (Phase A: any tombstone is a violation) | per Q8 phase_a_lock; surface via /lint |

**Structured log:**
```yaml
tombstone_log:
  - {date: 2026-04-23, layer: null, count: 0, weekly_rate: 0.0}
```

## 5. Active-skills count and validation ratio

**Definition.** Count of files in `swarm/wiki/skills/active/`; for
each, the success/loss ratio derived from `usage/<slug>.jsonl`.

**Sources.** `swarm/wiki/skills/active/` glob; `swarm/wiki/skills/usage/<slug>.jsonl`
per skill.

**Formula:**
```
active_skills_count = count(*.md in swarm/wiki/skills/active/)
for each active skill:
  success_count = grep '"outcome":"success"' usage/<slug>.jsonl | wc -l
  loss_count = grep '"outcome":"loss"' usage/<slug>.jsonl | wc -l
  validation_ratio = success_count / max(loss_count, 1)
  meets_q6 = (success_count + loss_count >= 10) AND (validation_ratio >= 3)
```

**Threshold per Q6 (D11 §11.5).** Skills failing `validation_ratio
< 1.0 over rolling 10 uses` are flagged for retirement (route
through tombstone per α-3 + D11).

**Structured log:**
```yaml
active_skills_log:
  - {date: 2026-04-23, count: 0, mean_ratio: null, below_threshold: []}
```

## 6. /lint findings summary

**Definition.** Per-class counts of `/lint` findings from the most
recent scheduled run + delta vs prior run.

**Sources.** The most recent `swarm/wiki/_lint-report-<YYYY-MM-DD>.md`.

**Formula:**
```
For each /lint check (10 total per D8 §8.5):
  current_count = count of findings under that check's section in latest report
  prior_count = same in second-most-recent report
  delta = current - prior
```

**Per-check tracking:**
1. Orphans
2. Stale claims (confidence×age + foundations 365-day re-review)
3. Broken wikilinks
4. Missing frontmatter
5. Contradictions integrity
6. Missing cross-refs
7. Index drift
8. α-2/α-3 lifecycle state validity (D8 §8.5 #8)
9. Triple-channel cross-ref consistency (D8 §8.5 #9)
10. Q8 Layer-9 lock (D8 §8.5 #10)

**Structured log:**
```yaml
lint_findings_log:
  - {date: 2026-04-23, report_path: null, counts: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}, deltas: {}}
```

## 7. Brigadier load

**Definition.** (a) Pending Task drafts awaiting brigadier review;
(b) average review latency from draft creation to brigadier accept/reject.

**Sources.**
- Pending: glob `swarm/wiki/drafts/*.md` filtered by `state: drafted`
  AND no corresponding canonical write.
- Latency: per-draft `created` timestamp vs. corresponding canonical
  page `created` timestamp (where the canonical bears
  `derived_from: <draft-slug>`); average over rolling 20.

**Formula:**
```
pending_drafts_count = count of swarm/wiki/drafts/*.md with state=drafted
                       AND no matching swarm/wiki/<canonical-path>/<slug>.md
review_latency_avg_min = mean(canonical.created - draft.created in minutes)
                         over the rolling 20 most recently-promoted drafts
```

**Threshold for alert.** `pending_drafts_count > 5` → brigadier
write-queue saturated (per Sub-agent A §1 Q2 applicability constraint
echoed); evaluate workload re-allocation OR Phase-B CRDT switch.

**Structured log:**
```yaml
brigadier_load_log:
  - {date: 2026-04-23, pending: 0, latency_min: null}
```

## 8. Update mechanism

**Who updates:**
- `/lint` PostToolUse (per master synthesis §5.6.2 + D8 §8.5):
  updates `lint_findings_log` after every wiki write.
- `/lint` scheduled (per Q5 #5 cadence weekly): updates `cycles_log`,
  `cross_theme_log`, `tombstone_log`, `active_skills_log`,
  `brigadier_load_log`.
- `meta-agent` weekly review (per W-5 + D5 §5.4 α-3 audit role):
  composes a 5-line weekly summary appended to `## Weekly summary`
  section below; verifies counter consistency; flags drift.
- `brigadier` updates the live counters in frontmatter
  (`closed_cycles_count`, `active_skills_count`, etc.) at the relevant
  α-2/α-3/α-4 transitions.

**Cadence:**
- Live counters (frontmatter): mutated per α-state transition (event-driven).
- Structured logs: appended weekly (or per-event for `lint_findings_log`).
- Weekly summary: meta-agent composes Mondays UTC.

**Append-only discipline.** Per CLAUDE.md / `.claude/rules/global.md`
"Логи: append-only, новые записи сверху." Each `_log:` list grows; no
historical entry is deleted. Rotation: when a `_log:` exceeds 30
entries, the oldest 20 are moved to
`swarm/wiki/_archive/health-history-<YYYY>.md` (per CLAUDE.md
"Правила" #7).

## Weekly summary (append-only, meta-agent composes)

(Empty until first weekly review.)

````

### 10.3 Per-metric computation-formula table (master reference)

| Metric | Formula | Source files | Update trigger | Q8 / threshold |
|---|---|---|---|---|
| FPAR | accepted_first_pass / total_invocations over rolling N | `swarm/logs/<cyc>/events.md` | PostToolUse | <0.80 alert |
| closed_cycles_count | count(cycle-log.md in swarm/logs/) | `swarm/logs/*/cycle-log.md` | α-4 closed transition | ≥50 = Q8 trigger #1 |
| cycle_close_rate_weekly | created-last-7d / 7 | `swarm/logs/*/cycle-log.md` mtime | weekly /lint | informational |
| cross_theme_refs_count | count edges with cross-niche/cross-theme | `swarm/wiki/graph/edges.jsonl` | /build-graph | ≥3 + ≥2 themes×50 = Q8 trigger #2 |
| tombstone_rate_weekly[layer] | count tombstoned in 7d / 7 by layer | `swarm/wiki/_archive/*.md` | weekly /lint | per-layer table §10.2.4 |
| active_skills_count | count *.md in active/ | `swarm/wiki/skills/active/` | α-3 validated transition | n/a |
| validation_ratio per skill | success / max(loss,1) | `swarm/wiki/skills/usage/<slug>.jsonl` | per-invocation /ingest write | <1.0 over 10 → retire |
| /lint findings counts | per-check from latest report | `swarm/wiki/_lint-report-*.md` | PostToolUse + weekly | per-check per D8 |
| pending_drafts_count | drafts with state=drafted no canonical | `swarm/wiki/drafts/` glob | event | >5 alert |
| review_latency_avg_min | mean(canonical-draft) over 20 | drafts/ + canonical pages | event | informational |

### 10.4 Compatibility matrix

| Locked item | D10 honours by … |
|---|---|
| Q5 (5-signal /lint) | structured log per signal class; PostToolUse + scheduled cadence. |
| Q8 (3-AND Layer-9 trigger) | §10.2.2 + §10.2.3 expose `closed_cycles_count` + `cross_theme_refs_count` + theme-population check; D5 §5.5 α-4 closed counter. |
| Sub-agent A §4 T2 (cross-theme = 0 watch) | §10.2.3 explicit "20-cycle re-eval" note. |
| W-12 (1000% depth) | every metric: definition + formula + source + trigger + threshold + structured-log scaffold. |
| Sub-agent C §6 ("research silent — spec must specify") | All formulas closed: FPAR rolling window (20/100), tombstone-rate (per-layer 7-day), cross-theme threshold (≥3 + ≥2 themes×50). |
| Critic-gate1 M10 forward-reference | `closed_cycles_count` field exists in frontmatter; D1 §1.4 #13 bootstrap initialises it; α-4 closed transition increments. |
| Critic-gate1 H1 (cycle-log path) | references `swarm/logs/<cycle-id>/cycle-log.md` per the corrected D1 §1.3. |
| §5.5.5 provenance gate (D6 §6.3) | brigadier-attested-with-3-supports method (the metric-counter-update events serve as the supports). |
| Max-subscription (D6 §6.10) | all computations are filesystem reads; no embeddings, no SDK. |

---

## DELIVERABLE 11 — Q6 Skill Activation-vs-Validation Rubric (resolves T3)

### 11.1 Mandate, T3 framing, and naming alignment

T3 (per Sub-agent A §4) resolves the tension between **activation**
(when a candidate skill becomes part of the live registry) and
**validation** (when a candidate is demonstrably effective). The
critic-gate1 S2 fix locked α-3 to 4 states per FPF Part 4 §4.3:
`proposed → active → validated ⇄ active → tombstoned` (no separate
`retired`). This deliverable is the operational rubric that drives
α-3 transitions for skills.

**Naming alignment** (carried from D5 §5.4 alias table):

| FPF state (canonical) | D11 spec alias | Filesystem location |
|---|---|---|
| `proposed` | `candidate` | `swarm/wiki/skills/candidates/<slug>/manifest.md` |
| `active` | `learning` | `swarm/wiki/skills/learning/<slug>/manifest.md` + `golden-set.jsonl` |
| `validated` | `active` (live) | `swarm/wiki/skills/active/<slug>.md` + D9 symlink |
| `tombstoned` | `tombstoned` | `swarm/wiki/_archive/skills/<slug>.md` |

D11 uses FPF state names canonically; spec aliases shown in
parentheses for cross-reference. The transitions and predicates below
are testable from filesystem alone (per W-12 + critic-gate1 H2 fix).

### 11.2 Skill candidate intake (transition: none → `proposed`)

**Trigger.** Compound step at α-1 `compounded` (D5 §5.2) writes a DRR
entry to `agents/<expert>/strategies.md` (Level-1) OR
`swarm/wiki/skills/candidates/<slug>/manifest.md` (Level-2 — if the
brigadier judges the pattern broad enough for swarm-wide skill).

**Predicate (none → `proposed`):**
- A new file at `swarm/wiki/skills/candidates/<slug>/manifest.md`
  with frontmatter `skill_state: candidate` AND
  4-part DRR populated (`context:`, `decision:`, `alternatives:`,
  `review_checkpoint:`).
- The DRR `proposed_by:` field set per Q6 R4 owner table (see §11.7).

**No golden set required at this stage.** Candidates are open ideas;
goldens come at `learning`.

### 11.3 Activation gate I (transition: `proposed` → `active`/`learning`)

**Trigger.** First successful application by any cell.

**Activation predicate (all conditions ANDed):**

1. **Golden-set seeded:** file
   `swarm/wiki/skills/learning/<slug>/golden-set.jsonl` exists with
   **≥3 cases** (per Q6 + Sub-agent C §5). Each case: JSONL line with
   `{input: <…>, expected_output: <…>, acceptance_predicate: <…>}`.
2. **Use-log seeded:** file
   `swarm/wiki/skills/usage/<slug>.jsonl` exists with **≥1 success
   record** ({outcome: success, ts: …, task_id: …}).
3. **Brigadier sign-off:** the most recent commit moving the
   `manifest.md` from `candidates/` to `learning/` was authored by
   the brigadier (per D6 §6.2 single-writer); commit message format
   per D6 §6.2.4.
4. **Frontmatter updated:** the manifest's `skill_state` advances from
   `candidate` to `active` (FPF) / `learning` (alias); `n_uses`
   field set to 1 or more.

**Filesystem-resident predicate** (lint-checkable, per W-12). All
predicate templates below use `${slug}` for explicit template
substitution (per critic-gate2 SS4); Стадия D substitutes the actual
skill slug. **Frontmatter values use D2 §2.4 spec-alias enum**
(`{candidate|learning|active|tombstoned}`) per critic-gate2 SS1.
The "FPF state" name is the canonical alpha state per D5 §5.4; the
on-disk frontmatter value is the spec alias.

```
fpf_state[${slug}] == "active" (alias "learning") iff
  exists(swarm/wiki/skills/learning/${slug}/manifest.md)
  AND exists(swarm/wiki/skills/learning/${slug}/golden-set.jsonl)
  AND wc -l < swarm/wiki/skills/learning/${slug}/golden-set.jsonl > 3
  AND grep '"outcome":"success"' swarm/wiki/skills/usage/${slug}.jsonl | wc -l >= 1
  AND frontmatter.skill_state == "learning"     # D2 §2.4 spec-alias enum
  AND exists(swarm/wiki/skills/learning/${slug}/.activation-attestation.md)
                                                # marker file written by brigadier
                                                # at α-3 transition (closes critic-gate2 H8;
                                                # eliminates commit-message predicate)
  AND grep 'attested_by: brigadier' swarm/wiki/skills/learning/${slug}/.activation-attestation.md
```

**Owner per Q6 R4:** brigadier (writes the activation; meta-agent or
expert may have drafted the candidate via `mode: writing-support` per
D6 §6.8).

### 11.4 Activation gate II (transition: `active`/`learning` → `validated`)

**Trigger.** Skill has accumulated sufficient evidence for promotion
to the live registry.

**Activation predicate (all conditions ANDed):**

1. **Golden-set ≥3 satisfied:** all ≥3 golden-set cases have
   `acceptance_predicate` returning true on the most recent run
   (per Sub-agent C §5; brigadier executes the goldens before promotion).
2. **Validated success ratio ≥3:1:** in
   `swarm/wiki/skills/usage/<slug>.jsonl`, success records outnumber
   loss records by at least 3:1.
3. **Minimum N=10 uses:** total recorded invocations
   `(success + loss) ≥ 10`.
4. **Brigadier sign-off via §5.5.5 provenance gate (D6 §6.3):** the
   commit promoting the canonical from `learning/<slug>/manifest.md`
   to `active/<slug>.md` AND creating the D9 symlink is brigadier-
   authored. The §5.5.5 gate verifies `sources[]` non-empty (the
   golden-set cases qualify as `sources[]` entries).

**Filesystem-resident predicate** (lint-checkable; `${slug}` is
template-substituted per critic-gate2 SS4; frontmatter uses spec-alias
enum per critic-gate2 SS1):
```
fpf_state[${slug}] == "validated" (alias "active" — live in registry) iff
  exists(swarm/wiki/skills/active/${slug}.md)
  AND exists(.claude/skills/${slug}.md)            # D9 symlink
  AND readlink(.claude/skills/${slug}.md) == "../../swarm/wiki/skills/active/${slug}.md"
  AND golden_set_pass_count == golden_set_total
  AND success_count >= 3 * loss_count
  AND (success_count + loss_count) >= 10
  AND frontmatter.skill_state == "active"          # D2 §2.4 spec-alias enum
  AND exists(swarm/wiki/skills/active/.${slug}.activation-attestation.md)
                                                   # marker file (closes critic-gate2 H8)
```

**Owner per Q6 R4:** brigadier writes; meta-agent runs golden-set
audit pre-write (`mode: writing-support` returns the audit verdict).

### 11.5 Retirement / tombstoning predicates

Per critic-gate1 S2 fix, α-3 has no `retired` state. There are two
backward transitions out of `validated`:

**(a) Demotion: `validated` → `active`/`learning`** (loop per D5 §5.4):

**Predicate:**
- Rolling 10 most-recent uses: `success_count / max(loss_count, 1) <
  3.0` AND `>= 1.0`.

Brigadier moves canonical back to `learning/`, removes D9 symlink. The
skill returns to `learning` for re-evaluation. Owner: meta-agent
emits drift-alert via `mode: writing-support`; brigadier executes the
move.

**(b) Tombstoning: any state → `tombstoned`:**

**Predicates (any one triggers):**
1. **Catastrophic ratio:** rolling 10 most-recent uses
   `success_count / max(loss_count, 1) < 1.0` (loss-dominated).
2. **Superseded:** another `validated` skill bears `supersedes:
   [[<this-slug>]]` in its frontmatter (D3 §3.2.7).
3. **Production incident:** an entry in `swarm/wiki/log.md` of the form
   `## [<date>] incident | <task-id> | caused-by: <slug>` cites this
   skill, AND the incident is not already resolved (no
   `## [<date>] incident-resolved | <task-id>` follow-up).
4. **Ruslan-attested withdrawal:** ack of an
   `AWAITING-APPROVAL-tombstone-skill-<slug>-*.md` gate file (D6 §6.5).

**Filesystem-resident tombstoning predicate:**
```
state[<slug>] == "tombstoned" iff
  exists(swarm/wiki/_archive/skills/<slug>.md)
  AND NOT exists(swarm/wiki/skills/active/<slug>.md)
  AND NOT exists(.claude/skills/<slug>.md)
  AND frontmatter.tombstoned_by != null
  AND frontmatter.skill_state == "tombstoned"
```

### 11.6 Worked examples

#### 11.6.1 Activation — `query-pricing-models` (FPF `validated` reached)

State at ratio = 5:1, n=15, golden-set 5/5 pass.

```
swarm/wiki/skills/learning/query-pricing-models/
  ├── manifest.md                       (skill_state: learning, n_uses: 15)
  ├── golden-set.jsonl                  (5 lines)
  └── .activation-attestation.md        (attested_by: brigadier, ts: 2026-05-30, criteria_passed: gate-I)
swarm/wiki/skills/usage/query-pricing-models.jsonl  (15 lines, 12 success / 3 loss)
```

**Predicate check (§11.4):**
- exists active/<slug>.md? NO (still in learning) — must be created.
- golden-set.jsonl wc -l == 5; pass = 5/5; ✓
- 12 / 3 = 4.0 ≥ 3.0; ✓
- 12 + 3 = 15 ≥ 10; ✓

**Brigadier action:**
1. Run all 5 goldens; verify 5/5 pass.
2. Write attestation file:
   `swarm/wiki/skills/active/.query-pricing-models.activation-attestation.md`
   with frontmatter `attested_by: brigadier, ts: 2026-05-30, criteria_passed: gate-II,
   golden_pass: 5/5, ratio: 4.0` (closes critic-gate2 H8 — replaces
   commit-message-predicate with marker file).
3. Move `learning/query-pricing-models/manifest.md` → `active/query-pricing-models.md`.
4. Update frontmatter: `skill_state: active` (D2 §2.4 spec-alias enum;
   FPF α-3 state is `validated`), `n_uses: 15`, `success_count: 12`,
   `loss_count: 3`.
5. Create D9 symlink: `ln -s ../../swarm/wiki/skills/active/query-pricing-models.md
   .claude/skills/query-pricing-models.md`.
6. Append to `swarm/wiki/log.md`:
   `## [2026-05-30] activate-skill | query-pricing-models | golden-set: 5/5; ratio: 4.0`.
7. Increment `swarm/wiki/meta/health.md`'s `active_skills_count`.
8. Commit: `[brigadier] cyc-2026-05-30-am: activate skill query-pricing-models per D11 §11.4`.

#### 11.6.2 Demotion — `summarise-meeting-notes` (drift detected)

State at validated, last 10 uses: 4 success / 6 loss (ratio = 0.67,
which is <1.0 → tombstone candidate, NOT demote).

If instead 5 success / 5 loss (ratio = 1.0; in the demotion band 1.0
≤ ratio < 3.0):

**Brigadier action (per §11.5(a)):**
1. Move `active/summarise-meeting-notes.md` → `learning/summarise-meeting-notes/manifest.md`.
2. Update frontmatter: `skill_state: learning` (D2 §2.4 spec-alias enum;
   FPF α-3 state is the demoted `active`), set `success_count: 5`,
   `loss_count: 5`.
3. Remove D9 symlink: `rm .claude/skills/summarise-meeting-notes.md`.
4. Remove activation-attestation marker: `rm swarm/wiki/skills/active/.summarise-meeting-notes.activation-attestation.md`.
5. Append to log: `## [<date>] demote-skill | summarise-meeting-notes | rolling-10 ratio 1.0; back to learning`.
6. Decrement `active_skills_count`.

#### 11.6.3 Tombstoning — `parse-html-table` (production incident)

Skill caused a misparse that propagated bad data into a wiki claim;
incident logged.

```
swarm/wiki/log.md (recent):
  ## [2026-06-15] incident | task-2026-06-15-extract-pricing | caused-by: parse-html-table
  ...
  (no follow-up incident-resolved line)
```

**Predicate check (§11.5(b) #3):** ✓ active incident.

**Brigadier action:**
1. Move `swarm/wiki/skills/active/parse-html-table.md` →
   `swarm/wiki/_archive/skills/parse-html-table.md`.
2. Update frontmatter: `skill_state: tombstoned`,
   `tombstoned_by: [[wiki/log.md#L<incident-line>]]`.
3. Remove D9 symlink: `rm .claude/skills/parse-html-table.md`.
4. Append to log: `## [2026-06-16] tombstone-skill | parse-html-table | per-incident task-2026-06-15-extract-pricing`.
5. Increment `tombstone_rate_weekly` for L8.
6. Commit per D6 §6.2.4.

### 11.7 Owner roles per transition (per Q6 R4 + Sub-agent A §3 R4)

| Transition | Propose (drafter) | Eval | Activate | Audit | Retire / Tombstone |
|---|---|---|---|---|---|
| none → `proposed` | any agent OR Ruslan (writes DRR via `mode: writing-support`) | n/a | n/a | n/a | n/a |
| `proposed` → `active` | brigadier (or owning expert in `mode: writing-support` returns draft) | brigadier | brigadier | n/a | n/a |
| `active` → `validated` | brigadier OR owning expert in `mode: writing-support` returns draft | brigadier (runs golden-set) | brigadier (under §5.5.5 gate) | meta-agent (audit before activation) | n/a |
| `validated` → `active` (demoted) | meta-agent emits drift-alert | meta-agent (rolling-ratio check) | n/a (it's a demotion) | meta-agent | n/a |
| any → `tombstoned` | meta-agent OR Ruslan OR brigadier (incident-driven) | brigadier (verifies tombstone trigger) | n/a | meta-agent (post-tombstone audit) | meta-agent OR Ruslan |

All transitions are **commit-by-brigadier** per Q2 single-writer (D6
§6.2). Meta-agent and experts emit drafts via `mode: writing-support`
per D6 §6.8 (Sub-agent A §6 #10 conflict resolved per Gate 1).

### 11.8 Anti-T3 clause (resolves T3 explicitly)

**Tension T3 (Sub-agent A §4):** "Activation = golden-set ≥80% binary;
validation = usage-driven (≥10 uses + ≥3:1). Стадия C MUST write
explicit rubric distinguishing the two gates."

**Resolution.** The rubric distinguishes:

- **Activation gate I** (§11.3, `proposed → active`): seeded
  state — first success + golden-set existence + brigadier intake.
  No usage requirement.
- **Activation gate II** (§11.4, `active → validated`): validated
  state — all goldens pass + ≥10 uses + ≥3:1 ratio + brigadier
  §5.5.5 sign-off.

**Anti-T3 enforcement:** validation evidence MUST be filesystem-resident
**before** activation gate II. Specifically:

1. The golden-set file (`golden-set.jsonl`) MUST be committed, not
   verbal/in-context.
2. The use-log file (`usage/<slug>.jsonl`) MUST contain ≥10 timestamped
   records, not aggregated estimates.
3. The brigadier's promotion commit MUST cite the
   `usage/<slug>.jsonl` and `golden-set.jsonl` paths in its
   `sources[]` frontmatter (§5.5.5 provenance gate D6 §6.3).
4. **No verbal validation.** A skill cannot be promoted because "it
   feels good" — the rubric is filesystem-checkable, not
   conversation-checkable.

`/lint` enforces by checking that every `.claude/skills/<slug>.md`
symlink target satisfies §11.4 predicate; non-conforming symlinks are
flagged as anti-T3 violations.

### 11.9 Compatibility matrix

| Locked item | D11 honours by … |
|---|---|
| Q6 (skill-learning pipeline) | activation predicate exact: golden-set ≥3, ratio ≥3:1, ≥10 uses, brigadier sign-off (all ANDed). |
| R4 (Q6 owners locked) | §11.7 table aligns to R4 owner roles per Sub-agent A §3. |
| T3 (activation-vs-validation tension) | §11.8 anti-T3 clause; filesystem-resident evidence required. |
| Q2 single-writer | every transition committed by brigadier; meta-agent/expert via `mode: writing-support`. |
| α-3 4-state lock (critic-gate1 S2) | only `proposed/active/validated/tombstoned`; `retired` route handled via demotion loop OR tombstone. |
| W-9 (skills first-class) | each skill has full lifecycle with golden-set + use-log + symlink. |
| W-12 (1000% depth) | every predicate filesystem-checkable; 3 worked examples; owner table; commit messages spelled out. |
| §5.5.5 provenance gate (D6 §6.3) | activation gate II requires §5.5.5 sign-off citing golden-set + use-log paths. |
| D9 (symlink convention) | references D9 §9.4 symlink-creation script; D9 §9.5 removal. |
| D10 (health.md) | references `active_skills_count` increment; `tombstone_rate_weekly` increment. |
| Sub-agent C §5 ("research silent on golden-set storage") | golden-set.jsonl format specified: JSONL line per case with `{input, expected_output, acceptance_predicate}`. |
| Sub-agent C §8 #9 (never-delete-only-archive) | tombstone moves to `_archive/`, doesn't delete. |
| Critic-gate1 H2 (filesystem-only predicates) | every predicate uses file existence + grep counts + frontmatter fields, no commit-message tests. |

---

## DELIVERABLE 12 — Strategies.md Trio Collapse (resolves T5)

### 12.1 Mandate and T5 framing

**Tension T5** (Sub-agent A §4 + §1 Q2 + Section 5): three candidate
locations for "strategies" content existed in the v2/v3 specification
sketch:

- (a) `agents/<expert>/strategies.md` — per-expert System Prompt
  Learning per CLAUDE.md per-agent memory layer.
- (b) `swarm/strategies/<expert>.md` — proposed v3 swarm-wide venue
  (BUILD §1.2 layout sketch).
- (c) `swarm/wiki/meta/agent-improvements/<expert>-<date>.md` —
  W-4 agent-improvement layer.

Per **R6** (locked, all R-items accepted) + **WIKI-V3-MECHANICS Part 2
§Q2 L178–187** + Sub-agent A §4 T5 + §3 R6: collapse to **2 venues**
— **KEEP (a) + (c), DROP (b).**

This deliverable specifies the migration mechanics, cross-venue sync
rule, and the `/lint` enforcement that catches T5 violations.

### 12.2 Venue 1 — `agents/<expert>/strategies.md` (KEEP, Level-1)

**Path.** `agents/<expert>/strategies.md` (project-root-relative;
NOT under `swarm/`).

**Naming convention.** One file per expert. The 5 files at Стадия D
bootstrap (per D1 §1.4 #16):
- `agents/engineering-expert/strategies.md`
- `agents/mgmt-expert/strategies.md`
- `agents/systems-expert/strategies.md`
- `agents/philosophy-expert/strategies.md`
- `agents/investor-expert/strategies.md`

**Owner write rights.** **Expert direct** (the only path-write
exception to Q2 single-writer per D1 §1.3 perm table). Each expert
writes to its own `agents/<expert>/strategies.md` directly without
brigadier mediation. Justification: this file is the expert's
**personal memory layer** (CLAUDE.md per-agent memory section
"Strategies"); subject to the expert's own self-improvement loop, not
swarm coordination. Brigadier monitors via §12.4 sync rule.

**Content shape** (per CLAUDE.md per-agent memory + α-3 DRR):
append-only YAML-block-per-entry, newest on top. Each entry:

```yaml
---
- date: 2026-04-23
  task_id: task-2026-04-23-foo
  context: <when this rule applies>
  decision: <the rule>
  alternatives: <considered>
  review_checkpoint: <when to re-evaluate>
  skill_state: candidate         # α-3 entry tracking
  proposed_by: <self-ref or brigadier>
  validation_status: proposed
---
```

**Lifecycle.** Entries live as α-3 `proposed` candidates. They may be
promoted to swarm-wide via §12.4 sync rule.

**Phase A bootstrap content** (per D1 §1.4 #16): each file has empty
body + frontmatter only:

```yaml
---
title: Strategies — <Expert Name>
type: per-agent-memory
layer_note: project-root, not under swarm/ (T5/R6)
expert: <slug>
created: 2026-04-23
last_modified: 2026-04-23
state: drafted
---

# <Expert Name> — Strategies (Level-1)

(Empty. Append entries newest-on-top per CLAUDE.md "Логи" rule.)
```

### 12.3 Venue 2 — `swarm/wiki/meta/agent-improvements/...` (KEEP, Level-2)

**Path.** `swarm/wiki/meta/agent-improvements/<file>` per D1 §1.3 perm
table + §1.2 tree.

**Naming conventions.** Per D1 §1.4 #14 (7 files at bootstrap):

- Per-expert improvement records: `<expert>-improvements.md` (5 files,
  one per expert: `engineering-expert-improvements.md`, …).
- System-level orchestration improvements:
  `system-level-improvements.md`.
- Cross-agent emergent insights: `emergent-insights.md`.

For new dated entries within these files, append-only YAML-block-per-
entry per α-3 DRR (same shape as §12.2 plus
`validation_status: under-validation|accepted|rejected|tombstoned`
per D2 §2.4 Layer 4 schema).

**Owner write rights.** **Brigadier-write only** (per Q2 single-
writer + D6 §6.2.2 per-layer write paths). Drafts come from any
expert (any mode) via `Task(...)` return packets, OR from
meta-agent in `mode: writing-support` (D6 §6.8); brigadier evaluates
the §5.5.5 gate (D6 §6.3) and writes.

**Content shape.** Same as §12.2 entry shape, plus the Layer-4
specific frontmatter from D2 §2.4 (`expert`, `improvement_target`,
`validation_status`, `proposed_by`, `applied_by`, `applied_at`).

**Lifecycle.** Entries flow through α-3
`proposed → active → validated ⇄ active → tombstoned` per D5 §5.4 +
D11. Activation rubric per D11 applies (golden-set ≥3, ratio ≥3:1,
≥10 uses) — though for prompt-edit improvements the "uses" are
brigadier observations across cycles rather than skill invocations.

### 12.4 Sync rule — Level-1 → Level-2 promotion

**Trigger.** When a per-expert insight in `agents/<expert>/strategies.md`
appears to apply broadly (heuristic: same insight surfaced by ≥2
experts independently OR cited by brigadier in ≥3 cycles).

**Promotion flow** (driven by α-1 `compounded` step in D5 §5.2):

1. **Expert proposes.** Expert returns a Task packet with an
   `escalations[]` entry: `{trigger: promote-to-swarm-wide, source:
   agents/<expert>/strategies.md#L<line>, justification: <…>}`.
2. **Brigadier evaluates.** Reads the cited Level-1 entry; checks for
   ≥2-expert independent surfacing (grep `agents/*/strategies.md` for
   semantic match) OR brigadier-cited count ≥3 (grep `swarm/logs/*/cycle-log.md`
   for `applied-rule: <slug>`).
3. **Brigadier drafts Level-2 entry.** Composes a new YAML-block entry
   for the relevant `swarm/wiki/meta/agent-improvements/<file>.md`.
   The Level-2 entry inherits the Level-1 content + adds
   `proposed_by: <originating-expert>(s)`, `cited_in: [<Level-1 paths>]`,
   `validation_status: proposed`.
4. **§5.5.5 gate.** Brigadier verifies the Level-2 entry's `sources[]`
   = the Level-1 paths cited (D6 §6.3 acceptance condition #1
   satisfied via inter-wiki source).
5. **Commit.** Brigadier appends the Level-2 entry, commits per D6
   §6.2.4. The Level-1 entries remain in place (they're the
   per-expert memory; not deleted on promotion — they cross-reference
   the Level-2 record via `promoted_to: [[meta/agent-improvements/<file>#<entry>]]`).
6. **α-3 progression.** The Level-2 entry advances per D11 rubric:
   `proposed → active → validated` once observed in ≥10 cycles with
   ≥3:1 success ratio.

**No demotion path.** Level-2 entries don't demote back to Level-1;
they tombstone (per α-3) if they fail validation.

### 12.5 Dropped venue — `swarm/strategies/` (R6 + T5)

**Path (rejected).** `swarm/strategies/<expert>.md` and any sibling
under `swarm/strategies/`.

**Rationale.** Sub-agent A §1 Q2 + §3 R6 + §4 T5 + §6 #8 (BUILD §1.2
layout amendment): this venue would duplicate Level-1 (per-expert
memory belongs in `agents/`) and Level-2 (swarm-wide improvements
belong in `swarm/wiki/meta/agent-improvements/`). Three venues for
one content type guarantees drift. Q2 + R6 collapse to two.

**Migration note.** No migration data exists in
`swarm/strategies/` at Стадия C close (the dir was a hypothesis in
BUILD §1.2 §1.2 L76–L82, never instantiated). Стадия D MUST NOT
create the directory. If any data accidentally lands there during
Phase A (e.g. from a stale BUILD-§1.2-following script), brigadier
migrates per the rules below before next commit:

- For per-expert content → move to `agents/<expert>/strategies.md`
  (append, newest-on-top).
- For swarm-wide content → draft a Level-2 entry per §12.3 + §12.4;
  brigadier commits via §5.5.5 gate.
- Then `rm -rf swarm/strategies/`. Append a log line:
  `## [<date>] migrate | T5/R6 | swarm/strategies/ → agents/ + meta/agent-improvements/`.

### 12.6 `/lint` rule (D8 §8.5 extension #11 — explicit T5 violation check)

`/lint` gains an additional check (logical extension of the existing
10 checks; this is check #11):

```
For each file under swarm/strategies/ (the dropped path):
  EMIT "T5/R6 violation: swarm/strategies/<path> exists; should not (per D12 §12.5)."
  Brigadier action: migrate per §12.5.
```

This catches:
- Stale code that still creates `swarm/strategies/` files.
- Manual error.
- Phase-A bootstrap drift.

### 12.7 Worked example — promotion of a brigadier-orchestration insight

**Setup.**
- Engineering-expert appended this entry to
  `agents/engineering-expert/strategies.md` on 2026-04-30:
  `decision: 'When the cell return packet has dissents[] non-empty,
  prefer integrator-mode synthesis over critic-mode rebuttal.'`
- Mgmt-expert independently appended a similar entry to
  `agents/mgmt-expert/strategies.md` on 2026-05-12.

**Promotion (per §12.4):**
1. Engineering-expert in next Task return: `escalations[]: [{trigger:
   promote-to-swarm-wide, source: 'agents/engineering-expert/strategies.md#L42',
   justification: 'mgmt-expert independently surfaced same pattern; see
   agents/mgmt-expert/strategies.md#L17'}]`.
2. Brigadier reads both Level-1 entries, confirms semantic alignment.
3. Brigadier drafts Level-2 entry in `swarm/wiki/meta/agent-improvements/system-level-improvements.md`:
   ```yaml
   ---
   - date: 2026-05-13
     improvement_target: protocol      # per D2 §2.4 Layer-4 enum
     decision: 'On dissents[] non-empty Task returns, brigadier prefers
                integrator-mode synthesis (Task(<expert>-integrator)) over
                critic-mode rebuttal.'
     proposed_by: engineering-expert + mgmt-expert (independent surfacing)
     cited_in:
       - agents/engineering-expert/strategies.md#L42
       - agents/mgmt-expert/strategies.md#L17
     validation_status: proposed
     skill_state: candidate
   ---
   ```
4. Brigadier passes §5.5.5 gate (sources[] = the two Level-1 paths;
   non-empty; both are tier: core).
5. Brigadier commits: `[brigadier] cyc-2026-05-13-am: promote
   dissents-integrator-preference rule to Level-2`.
6. Brigadier annotates the two Level-1 entries with
   `promoted_to: [[meta/agent-improvements/system-level-improvements#2026-05-13]]`.

### 12.8 Compatibility matrix

| Locked item | D12 honours by … |
|---|---|
| T5 (strategies trio collapse) | §12.1–§12.5 explicitly: keep (a) + (c), drop (b). |
| R6 (drop swarm/strategies/) | §12.5 + §12.6 lint enforcement. |
| Q2 single-writer | §12.3 brigadier-write only for Level-2; §12.2 Level-1 expert-direct exception documented + scoped. |
| W-4 agent-improvement layer | §12.3 path matches D1 Layer 4 perm table. |
| W-5 two-level CE | §12.2 Level-1 + §12.3 Level-2 + §12.4 sync rule operationalises Level-1↔Level-2 flow. |
| §5.5.5 provenance gate (D6 §6.3) | §12.4 #4 gate verification at promotion; §12.7 worked example shows sources[] inheritance. |
| α-3 lifecycle (D5 §5.4) | §12.3 Level-2 entries follow α-3 proposed→active→validated→tombstoned. |
| D11 (skill activation rubric) | §12.4 #6 progression aligns with D11 rubric. |
| CLAUDE.md per-agent memory (Strategies layer) | §12.2 cites + matches: `agents/<expert>/strategies.md` is the existing per-agent memory location; no path change. |
| BUILD §1.2 layout amendment | §12.1 + §12.5 documents the deliberate drop of `swarm/strategies/` from BUILD §1.2 (Sub-agent A §6 #8). |
| Sub-agent A §1 Q2 §178–187 + §4 T5 + §3 R6 | §12.1 cites + materialises. |

---

---

## STAGE C — END SUMMARY (Стадия C COMPLETE)

### What landed in this consolidation

Twelve deliverables across the structural core (D1–D6) and operational
integration surface (D7–D12). Together they materialise the
constitution of compounded memory the prompt mandated.

### Provenance audit (per prompt §10 success criterion #6)

≥250 distinct citations across W-1..W-12, Q1..Q9, R1..R8, T1..T5,
FPF Part 4 / Part 10, master synthesis §5.5–§5.10, knowledge-architecture
research §A–§H, Sub-agent extractions A–E, 24-Locks 13/17, CLAUDE.md
per-agent memory section, BUILD §1.2 layout (with the documented
amendment per T5/R6).

### Locked-decision integrity (per prompt §10 success criterion #7)

Zero locked-decision re-openings in the final spec. The two close
calls — α-3 4-state lock (FPF Part 4 §4.3) and 12-edge enum count
(MECHANICS L236 summary) — were resolved by aligning to the locked
source: α-3 dropped its inventive `retired` state per critic-gate1 S2;
edge enum dropped `addresses_gap` (zero v2 usage; semantically
overlapped by `derived_from`) per critic-gate1 H4 to land on 12.

### Critic-applied fixes (per prompt §4 Phase 3)

Gate 1: 4 showstoppers + 9 high fixed pre-commit (S1 D6 missing
Cross-cell-reference protocol, S2 α-3 invented retired, S3 niche-enum
global, S4 Layer-9 reviewed/ bucket, plus H1–H9). Critic report
preserved at `raw/research/step-2-2-3c-extractions/critic-gate1.md`.

Gate 2: 4 showstoppers + 8 high fixed pre-commit (SS1 skill_state
enum collision with D2 §2.4 lock, SS2 build-graph wrong line ref,
SS3 /consolidate Q2 violation, SS4 template substitution, plus H1–H8).
Critic report preserved at
`raw/research/step-2-2-3c-extractions/critic-gate2.md`.

18 medium / 12 low findings logged for Phase-A errata where applicable.

### Tier discipline (per prompt §10 success criterion #12)

No Tier 4 input read. The 393-book private library at `raw/books-md/`
remains untouched as Phase B fuel. No WebSearch, no WebFetch. All
inputs were Tier 1 (locked decisions, GOALS, FPF, master synthesis)
+ Tier 2 (knowledge-architecture research, Karpathy gist, prior W-1/
W-2/W-3 extractions) + Tier 3 (existing v2 templates and skills,
audited line-by-line by Sub-agent D).

### Max-subscription compliance

`unset ANTHROPIC_API_KEY` discipline preserved throughout. Zero paid
embedding service references. Zero third-party SDK calls in skill
bodies. All retrieval Phase A is filesystem + ripgrep + typed-BFS
over `graph/edges.jsonl` per Q1 + D6 §6.10. Sub-agent invocations
during Стадия C used Claude Code's built-in Task tool (no SDK).

### Single-writer brigadier honoured

Every wiki write path in this spec routes through the brigadier per
Q2 + D6 §6.2. The two narrow exceptions (drafts/ for cells per Q2;
`agents/<expert>/strategies.md` for the Level-1 personal memory layer
per T5/R6) are explicitly scoped and documented. Meta-agent does
NOT bypass single-writer (Sub-agent A §6 #10 conflict resolved): it
emits drafts via Task `mode: writing-support` per D6 §6.8; brigadier
verifies the §5.5.5 gate and writes.

### Branch + commit cadence

Branch: `claude/jolly-margulis-915d34` throughout. No force-push, no
rebase, no destructive ops. Per-deliverable commits per prompt §8
checklist:

1. ✅ Phase 1 — `[step-2-2-3c] 5 parallel extractions for wiki v3 architecture spec`
2. ✅ D1 draft, D2 draft, …, D6 draft (one commit each)
3. ✅ `[step-2-2-3c] critic gate1 report`
4. ✅ `[step-2-2-3c] AWAITING-APPROVAL gate1 (deliverables 1-6)` — paused for Ruslan ack
5. ✅ Ruslan ack received 2026-04-23 — proceeded to Gate 2
6. ✅ D7 draft, D8 draft, …, D12 draft
7. ✅ `[step-2-2-3c] critic gate2 report`
8. ✅ `[step-2-2-3c] AWAITING-APPROVAL gate2 (deliverables 7-12)` — paused for Ruslan ack
9. ✅ Ruslan ack received 2026-04-23 — proceeding to final consolidation
10. (next) `[design] AWAITING-APPROVAL wiki v3 architecture (Стадия C complete)` — this commit

### Halt instruction (per prompt §5 + §8 + §10)

After this commit + push, **HALT.** Do not launch Стадия D from this
session. Стадия D opens with a separate AWAITING-APPROVAL gate
written by a separate Claude Code invocation reading this spec
verbatim per the target_consumer enumeration in this file's
frontmatter.

---

## §12 REFERENCES (Ruslan-audit)

### Authoritative inputs (Tier 1)
- `decisions/WIKI-V3-MECHANICS-2026-04-23.md` (Q1..Q9 + R1..R8 + T1..T5)
- `design/ROY-WIKI-V3-GOALS-2026-04-23.md` (W-1..W-12)
- `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` (Part 4 alphas, Part 10 protocols)
- `design/ROY-BUILD-LOGIC-2026-04-23.md` (build phasing)
- `decisions/ROY-ALIGNMENT-2026-04-22.md` (matrix 5×4 pattern)
- `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` (§5.5 baseline)

### Research grounding (Tier 2)
- `raw/research/knowledge-architecture-deep-research-2026-04-19.md`
- `raw/articles/karpathy-llm-wiki-gist-2026-04.md`
- `raw/research/step-2-2-3b-extractions/W-{1,2,3}-*.md`

### Existing infrastructure (Tier 3)
- `wiki/_templates/` (9 v2 entity templates)
- `wiki/graph/edges.jsonl` (572 v2 edges)
- `wiki/{overview,index,log}.md` (v2 conventions)
- `.claude/skills/{ingest,ask,lint,compile,consolidate,build-graph,search-kb,sweep-notion-bank}.md`
- `CLAUDE.md` (Wiki Architecture v2 section)
- `.claude/rules/global.md`

### Phase 1 extractions (this spec's grounding inputs)
- `raw/research/step-2-2-3c-extractions/A-mechanics-goals-buildlogic.md` (2,488 words)
- `raw/research/step-2-2-3c-extractions/B-fpf-alphas-protocols.md` (2,490 words)
- `raw/research/step-2-2-3c-extractions/C-knowledge-arch-karpathy.md` (2,496 words)
- `raw/research/step-2-2-3c-extractions/D-v2-infrastructure-audit.md` (2,198 words)
- `raw/research/step-2-2-3c-extractions/E-master-synthesis-matrix.md` (2,466 words)

### Critic reports (mandatory Phase 3 audit)
- `raw/research/step-2-2-3c-extractions/critic-gate1.md` (2,375 words)
- `raw/research/step-2-2-3c-extractions/critic-gate2.md` (2,362 words)

### Gate files (Ruslan audit trail; preserved alongside this consolidation)
- `design/AWAITING-APPROVAL-wiki-v3-architecture-gate1-2026-04-23.md` (D1–D6, ~22K words)
- `design/AWAITING-APPROVAL-wiki-v3-architecture-gate2-2026-04-23.md` (D7–D12, ~11.7K words)

### Output target
- `design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-23.md` (this file, ~33K words, all 12 deliverables)

### Branch
- `claude/jolly-margulis-915d34` (no force-push, no rebase)

### Stylistic kin (referenced, not copied)
- `prompts/step-2-1-master-synthesis-2026-04-22.md` (tier list, sub-agents, gates, success-criteria patterns)

---

**Status:** AWAITING-APPROVAL. Ruslan reviews; Стадия C concludes on
ack. Стадия D opens in a separate session per the target_consumer
enumeration above.
