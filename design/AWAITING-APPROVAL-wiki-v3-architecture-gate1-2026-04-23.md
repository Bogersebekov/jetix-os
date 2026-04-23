---
title: Wiki v3 Architecture Spec — Gate 1 (Deliverables 1–6, structural core)
date: 2026-04-23
status: AWAITING-APPROVAL
gate: 1-of-2
covers_deliverables: [1, 2, 3, 4, 5, 6]
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
target_consumer:
  - Стадия D builders (humans + Claude Code creating swarm/wiki/, swarm/lib/, .claude/config/, .claude/skills/ diffs)
  - 5 domain experts at runtime (read foundations/swarm-alphas.md + lib/shared-protocols.md on every Task invocation)
  - Phase B self-improvement (versioned baseline diffed by the swarm after Private Library consumption)
written_by: Claude Code on server (Opus 4.7, 1M context, Стадия C orchestrator)
branch: claude/jolly-margulis-915d34
---

# WIKI v3 ARCHITECTURE SPEC — GATE 1 (DELIVERABLES 1–6)

> **TL;DR** — This is the **structural core** of the Wiki v3 constitution.
> Six deliverables: directory layout (D1), per-layer frontmatter (D2),
> 12-edge enum (D3), per-entity-type templates (D4), 5 swarm-alpha state
> machines (D5), shared-protocols.md (D6). Gate 2 covers the operational
> integration surface (D7–D12). This file is **AWAITING-APPROVAL**: no
> file in `swarm/wiki/`, `swarm/lib/`, `.claude/config/`, or
> `.claude/skills/` is created from this spec until Ruslan approves both
> gates and the consolidated final spec ships.
>
> Citations are everywhere — every `MUST` traces to a locked W-item,
> Q-resolution, R-item, T-resolution, FPF Part 4 / Part 10 mandate,
> master synthesis §5.5–§5.10 baseline, knowledge-architecture research
> finding, or a 24-Lock entry. Re-debate is out of scope.

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
│   ├── niches/                               # per-agent symlink slices
│   │   ├── personal/
│   │   ├── business/
│   │   ├── sales/
│   │   ├── life/
│   │   ├── tech/
│   │   ├── meta/
│   │   └── global/
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
│   │   ├── management/
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
│       ├── reviewed/                         # critic-reviewed (Phase B)
│       └── promoted/                         # → moves to global/ (Phase B)
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
| `swarm/wiki/niches/{personal,business,sales,life,tech,meta,global}/` | spine | brigadier (creates symlinks) | brigadier-write | dir of symlinks into other layers              | 7 dirs        | each `niches/<n>/` populated with symlinks per CLAUDE.md per-agent memory rule.  |
| `swarm/wiki/meta/health.md`                       | spine | `/lint` + meta-agent | derivative + meta-agent-via-task | singleton                                | singleton     | D10 skeleton (8 sections + structured-log scaffold).                            |
| `swarm/wiki/meta/agent-improvements/`             | 4     | brigadier           | brigadier-write           | `<expert>-improvements.md` + `system-level-*.md` + `emergent-insights.md` | 7 files | empty body in each (frontmatter only); brigadier appends per W-5 Level-2 sweep. |
| `swarm/wiki/_archive/`                            | spine | `/consolidate`      | derivative                | `<YYYY-MM-DD>-<slug>.md` (loser pages)              | per-entity    | empty dir.                                                                       |
| `swarm/wiki/themes/<theme>/`                      | 1     | brigadier (Phase A seeding) + expert-via-task (Phase B) | brigadier-write | `<sub-bucket>/<slug>.md`            | 5 themes      | `README.md` per theme (theme tour + book citations placeholder).                 |
| `swarm/wiki/themes/<theme>/{concepts,methods,heuristics,anti-patterns}/` | 1 | brigadier/expert-via-task | brigadier-write | `<slug>.md`                                | per-entity    | empty dirs.                                                                      |
| `swarm/wiki/brigadier/`                           | 2     | brigadier           | brigadier-write           | `<slug>.md` per sub-bucket                          | 4 sub-buckets | `README.md` + 4 sub-dirs (`how-to-solve-problems/`, `how-to-manage-agents/`, `how-to-decompose-tasks/`, `orchestration-state/`). |
| `swarm/wiki/agents/<expert>/`                     | 3     | brigadier (canonical) + expert-via-task (drafts) | brigadier-write | `<slug>.md`, `cross-refs.md`, `README.md` | 5 experts | per-expert `README.md` + empty `scratchwork/` + empty `cross-refs.md`.            |
| `swarm/wiki/tasks/<task-id>/`                     | 5     | brigadier           | brigadier-write           | `<task-id>` = ULID per BUILD §3                     | per-task      | created on intake by brigadier (subdirs `context/`, `artefacts/`, `decisions/`, file `open-questions.md`). |
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
| `swarm/wiki/insights/{candidates,reviewed,promoted}/` | 9 | (Phase B agents)    | (Phase B)                 | `<slug>.md` (Phase B)                               | per-entity    | **empty dirs in Phase A.** No agent instantiated. (W-10, R5.)                    |
| `swarm/lib/shared-protocols.md`                   | spine | brigadier           | brigadier-write           | singleton                                          | singleton     | full content of D6 (initial Phase A version).                                    |
| `swarm/scratchpads/`                              | n/a   | each agent          | (volatile)                | `<agent-id>.md`                                    | per-agent     | empty dir; not part of `swarm/wiki/` (volatile working memory).                  |
| `swarm/gates/`                                    | n/a   | brigadier           | brigadier-write           | `AWAITING-APPROVAL-<slug>-<YYYY-MM-DD>.md`           | per-gate      | empty dir; HITL escalations land here per D6 §4.                                 |
| `swarm/mailboxes/`                                | n/a   | each agent          | append-only                | `<agent-id>.jsonl`                                  | per-agent     | empty dir; per master synthesis §5.6.2 PostToolUse.                              |
| `swarm/logs/`                                     | n/a   | each agent          | append-only                | `<cycle-id>.md`                                    | per-cycle     | empty dir.                                                                       |
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
9. `swarm/wiki/themes/{engineering,management,systems,philosophy,investing}/README.md` — placeholder per theme.
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
- `candidates/`, `reviewed/`, `promoted/` MUST remain empty.
- `/lint` flags any non-README write under `swarm/wiki/insights/` as
  a Q8/W-10 violation.

Phase-B activation flow (when triggered):
- crazy-agent writes into `candidates/`.
- Critic / philosophy-expert reviews → moves to `reviewed/`.
- Brigadier promotes via §5.5.5 provenance gate → moves to
  `promoted/`, then promotes again to `swarm/wiki/global/` per W-11
  cognitive-infrastructure mandate.
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
