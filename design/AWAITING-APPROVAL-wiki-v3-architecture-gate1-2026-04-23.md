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
| `id`            | string (ULID, `<type>-<26-char>`)   | yes | generated by /ingest     | unique across `swarm/wiki/`; matches regex `^[a-z]+-[0-9A-Z]{26}$`                          | Sub-agent C §1 H.1 (deterministic path schema), W-12 | unique anchor for all alpha state references in `graph/edges.jsonl`         |
| `title`         | string                              | yes | none                     | non-empty; ≤120 chars                                                                       | v2 templates (Sub-agent D §1.1)                       | rendered in `index.md` TOC + `log.md` lines                                 |
| `type`          | enum                                | yes | none                     | one of `concept|entity|source|claim|idea|topic|experiment|summary|foundation|skill|task|operation|insight|improvement|theme-page` | v2 (Sub-agent D §1.1) + Q3 12-edge enum (D3) | drives template selection in /ingest, frontmatter delta lookup              |
| `layer`         | int 1..9 OR `spine`                 | yes | none                     | matches the dir's layer per D1 §1.3                                                         | D1 + W-1                                              | drives Q4 task-context filter + niche routing                               |
| `niche`         | enum                                | yes | none                     | one of `personal|business|sales|life|tech|meta|global`                                      | v2 (Sub-agent D §1.1) + CLAUDE.md per-agent memory   | Q4 niche-filtered Tier A pull; cross-niche edges feed Q8 Layer-9 trigger    |
| `created`       | iso-date `YYYY-MM-DD`               | yes | today                    | valid ISO date ≤ today                                                                       | v2 (Sub-agent D §1.1)                                 | inputs to staleness signal #3 (Q5 confidence×age)                           |
| `last_modified` | iso-date `YYYY-MM-DD`               | yes | today                    | valid ISO date ≤ today, ≥ `created`                                                          | v2 + Q5                                               | inputs to staleness signal #3                                               |
| `last_reviewed` | iso-date `YYYY-MM-DD`               | opt | `<unset>`                | if set: ≥ `created`. Required for `foundations/` (Q5 §3 365-day re-review).                 | Sub-agent A §1 Q5 + Sub-agent C §4 signal 3           | staleness signal #3                                                         |
| `pipeline`      | enum                                | yes | `raw` for new, `ingested` post-/ingest | one of `raw|ingested|compiled|linted|ready`                                  | CLAUDE.md, Sub-agent D §1                             | content-maturity axis (independent of `state`)                              |
| `state`         | enum                                | yes | `drafted`                | one of `drafted|reviewed|revised|accepted|referenced|superseded|retired|tombstoned` (D5 α-2) | FPF Part 4 §4.1 (Sub-agent B §2) + Q5                 | artefact lifecycle axis; D5 transitions; staleness signals #4, #5           |
| `confidence`    | enum                                | yes | layer default            | one of `low|medium|high`. Defaults: `foundations/` = `high`; `claims/` = layer default; `ideas/` = `low` per v2.  | v2 (Sub-agent D §1.4–§1.5) + Q5                       | staleness signal #1 (low + >60d → flag)                                     |
| `confidence_method` | enum                            | opt | `<unset>`                | one of `expert-judgment|golden-set|cited-source|peer-reviewed|ruslan-attested` (W-12 depth) | Q5 + W-12                                             | reviewers see why a confidence value was assigned                           |
| `tier`          | enum                                | yes | `core`                   | one of `core|partner|member|public` (24-Lock 13)                                            | master synthesis §5.5.4 (Sub-agent E §1.5.4)         | tier-check hook on outgoing artefacts (D6 §1)                               |
| `produced_by`   | string                              | yes | `<agent>-<mode>` or `human` or `brigadier` | matches `^(brigadier|human|<expert>-(critic|optimizer|integrator|scalability|writing-support))$` | master synthesis §5.5.3 (Sub-agent E §1.5.3) + matrix 5×4 (E §5) | identifies the cell that drafted; brigadier substitutes for canonical writes |
| `derived_from`  | string                              | opt | `<unset>`                | if set: format `<expert>-<mode>` or `<task-id>:<draft-slug>` (chained provenance per E §8 ambiguity 5) | Sub-agent E §6 (matrix-vs-write resolution)          | when brigadier promotes a cell draft to canonical, names the originating cell |
| `task_id`       | string (ULID)                       | opt | `<unset>` (required for tasks/, drafts/, artefacts/) | matches `^task-[0-9A-Z]{26}$`                                | BUILD §2.2 (Sub-agent B §2 α-2 acceptance)            | ties draft → task scope (Q4 + Layer 5)                                      |
| `cycle_id`      | string                              | opt | `<unset>` (required for experiments/, summaries/) | matches `^cyc-[0-9A-Z]{26}$`                                  | master synthesis §5.5.3 + α-4 (Sub-agent B §4)        | ties artefact → α-4 cycle (Layer-9 trigger counter, D10)                    |
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
| `cycle_id` | string ULID | yes | none | matches regex above | spec illustrative + α-4 | ties experiment to its cycle |

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
| `theme` | enum | yes | dir-derived | one of `engineering|management|systems|philosophy|investing` | W-1 + GOALS §2 L307–316 | constrains `niche` to one of `tech|business|systems-meta|meta|business` mapping |
| `book_citations` | list of `{book_path, page_range?}` | yes | `[]` | each `book_path` resolves under `raw/books-md/` (Phase B); empty in Phase A | W-3 + Phase-A note in D1 §1.7 | provenance for theme-distillation per book |

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
| `task_id` | string ULID | yes | dir-derived | matches `^task-[0-9A-Z]{26}$`; matches `<task-id>` in path | BUILD §3 + α-1 (Sub-agent B §1) | α-1 Task lifecycle |
| `alpha_state` | enum | yes | `submitted` | one of `submitted|intaked|decomposed|dispatched|integrated|gated|approved|compounded|archived|refused|returned|rejected` | α-1 (Sub-agent B §1) | D5 α-1 state |
| `niche` | enum | yes | per task | from `personal|business|sales|life|tech|meta|global` | Q4 niche-filter | Tier A pull |

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
| `skill_state` | enum | yes | `candidate` | one of `candidate|learning|active|retired|tombstoned` (α-3 spec set, Sub-agent B §3 mapping) | Q6 + α-3 + D11 | drives bucket placement |
| `golden_set_path` | string | opt (req when `skill_state ∈ {learning, active}`) | `<unset>` | resolves to `swarm/wiki/skills/<bucket>/<slug>/golden-set.jsonl` | Q6 + Sub-agent C §5 | activation predicate (D11) |
| `success_count` | int | opt | `0` | derived from `usage/<slug>.jsonl` | Q6 + D11 | activation/retirement predicates |
| `loss_count` | int | opt | `0` | derived from `usage/<slug>.jsonl` | Q6 + D11 | activation/retirement predicates |
| `n_uses` | int | opt | `0` | derived; `success + loss` | Q6 (≥10 uses) | activation predicate |
| `owners` | yaml-block (map: `{transition → role}`) | yes | per Q6 R4 default | populated per Q6 R4 owner table | R4 + Q6 | transition routing |

#### Layer 9 — `insights/...` (Phase A: README only)
| Field | Type | Req | Default | Validation | Source | Lifecycle |
|---|---|---|---|---|---|---|
| `insight_state` | enum | yes (Phase B) | `candidate` | one of `candidate|reviewed|promoted` | Q8 + W-10 | bucket placement |
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

The locked enumeration in **WIKI-V3-MECHANICS L216–234** specifies 9
intra-layer types + `part_of` (formalised 10th intra-layer) + 3
cross-layer types. The summary line at L236 reads "Total: 12 edge
types" — this **undercounts the explicit enumeration by one** (the
summary did not count `part_of` separately). Per Q3 + R7 (locked) and
Sub-agent A §1 Q3 + Sub-agent C §3 + Sub-agent D §2 (audit confirmed
`part_of` as the dominant edge in v2 with 233 of 572 records), this
spec adopts the **enumerated list** as authoritative — **13 distinct
edge types**. The summary "12" is treated as a clerical error. (If
Ruslan prefers a strict 12-type bundle, the most defensible cut is
`addresses_gap` — 0 usage in v2 per Sub-agent D §2, semantically
overlapped by `derived_from`. Deferred to gate review.)

The 13-type enum lives at `swarm/wiki/_templates/edge-types.md` and is
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

#### 3.2.8 `addresses_gap` (intra-layer #8)
- **Definition.** Page A is created to fill a gap previously
  flagged by `/lint` (e.g. orphan reference, missing concept).
- **Cardinality.** N:M.
- **Directionality.** Directed (`new → gap-marker`).
- **Inverse.** `gap_filled_by` (derivative).
- **Allowed `from`.** Any spine entity-type.
- **Allowed `to`.** `topics`, `claims` (where the gap was lint-flagged).
- **Cross-layer flag.** No.
- **Example.** `{"from":"concepts/edge-cardinality","to":"topics/edge-types-hub","type":"addresses_gap","ts":"2026-04-23","confidence":"medium"}`
- **`/lint` rule.** Used to clear `/lint`-emitted gap warnings —
  presence of an `addresses_gap` edge to a topic with a previously
  reported "missing concept" closes that warning.
- **Note on usage.** Zero v2 usage (Sub-agent D §2). Retained per
  R7 locked enum; if Ruslan prefers a 12-type bundle this is the
  best drop candidate.

#### 3.2.9 `derived_from` (intra-layer #9)
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

#### 3.2.10 `part_of` (intra-layer #10 — formalised per Q3)
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

#### 3.2.11 `alpha-ref` (cross-layer #1)
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

#### 3.2.12 `layer-ref` (cross-layer #2)
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

#### 3.2.13 `cross-tree-ref` (cross-layer #3)
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
| **S**  | extends, contradicts, supports, inspired_by, tested_by, invalidates, supersedes, addresses_gap, derived_from, part_of | layer-ref | layer-ref | layer-ref | layer-ref | alpha-ref | alpha-ref | layer-ref | layer-ref | layer-ref | cross-tree-ref |
| **L1** | layer-ref | extends, contradicts, supports, derived_from, part_of, supersedes | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | cross-tree-ref |
| **L2** | layer-ref | layer-ref | extends, supersedes, part_of | layer-ref | layer-ref | alpha-ref | alpha-ref | layer-ref | layer-ref | — | cross-tree-ref |
| **L3** | layer-ref | layer-ref | layer-ref | extends, derived_from, part_of, supersedes | layer-ref | alpha-ref | alpha-ref | layer-ref | layer-ref | — | cross-tree-ref |
| **L4** | layer-ref | layer-ref | layer-ref | layer-ref | extends, supersedes | — | — | layer-ref (`promoted_to`) | layer-ref | — | cross-tree-ref |
| **L5** | derived_from, supports, part_of | — | — | — | — | extends, supersedes, contradicts | layer-ref | — | — | — | — |
| **L6** | layer-ref | — | — | — | — | layer-ref | extends, supersedes, part_of | layer-ref | — | — | cross-tree-ref |
| **L7** | layer-ref | layer-ref | layer-ref | layer-ref | — | — | — | extends, contradicts, supports, supersedes, part_of, derived_from | layer-ref | — | cross-tree-ref |
| **L8** | layer-ref | layer-ref | layer-ref | layer-ref | layer-ref | — | — | layer-ref | extends, supersedes, part_of, addresses_gap | — | cross-tree-ref |
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
v3 enum. The 5 declared-but-unused v2 types (`inspired_by`,
`tested_by`, `invalidates`, `supersedes`, `addresses_gap`) are
preserved in the v3 enum (per R7 locked); v2's edges.jsonl simply
contains zero records of those types and v3 inherits the same.

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
id: concept-<26-char-ULID>
title: <concept name>
type: concept
layer: spine
niche: <personal|business|sales|life|tech|meta|global>
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
| Frontmatter `id` | absent | added (ULID) | D2 cross-layer required; uniqueness for graph anchor |
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
id: entity-<26-char-ULID>
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
id: source-<26-char-ULID>
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
id: claim-<26-char-ULID>
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
id: idea-<26-char-ULID>
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
id: topic-<26-char-ULID>
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
id: experiment-<26-char-ULID>
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
cycle_id: cyc-<26-char-ULID>
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
id: summary-<26-char-ULID>
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
cycle_id: cyc-<26-char-ULID>
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
id: foundation-<26-char-ULID>
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



