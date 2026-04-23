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

