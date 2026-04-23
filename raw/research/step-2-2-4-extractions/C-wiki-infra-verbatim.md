---
title: Sub-agent C — Wiki v3 Infrastructure D1..D10 Verbatim Extraction
date: 2026-04-23
extraction_for: prompts/step-2-2-4-agent-construction-2026-04-23.md
sources:
  - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md (D1..D10)
status: ready-for-orchestrator-paste
sub_agent: C
---

# Sub-agent C — Wiki v3 Infrastructure Verbatim Extraction

This file carries verbatim content for deliverables D1 through D10 from
`design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`. Every fenced block
below is ready for orchestrator paste at Стадия D. Gaps (items the spec
defers or does not specify concretely) are marked
`[GAP — orchestrator must fill]`.

---

## D1 — `swarm/wiki/` directory tree (ASCII, verbatim)

**Source:** spec §1.2 (lines 151–301). Literal, canonical ASCII tree.
Orchestrator runs `mkdir -p` against every named directory and `touch`
against every named file at the bootstrap state per §1.4.

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
│   │   ├── mgmt/
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
│
├── lib/                                      # shared protocols + libraries
│   └── shared-protocols.md                   # D6
│
├── scratchpads/                              # per BUILD §1.2 (volatile)
├── gates/                                    # per BUILD §1.2 (HITL escalations)
├── mailboxes/                                # per BUILD §1.2 (JSONL mailboxes)
└── logs/                                     # per BUILD §1.2 (per-cycle commit logs)
```

### D1 bootstrap non-empty files (§1.4)

Day-one populated (non-empty) files:

1. `swarm/wiki/index.md` (frontmatter-only stub)
2. `swarm/wiki/log.md` (frontmatter-only stub)
3. `swarm/wiki/overview.md` (D1 §1.5 boilerplate — see below)
4. `swarm/wiki/_templates/*.md` (10 files per D3 + D4)
5. `swarm/wiki/graph/edges.jsonl` + `cross-tree.jsonl` (empty, single newline)
6. `swarm/wiki/graph/communities.md` + `summaries.md` (header stubs)
7. `swarm/wiki/foundations/swarm-alphas.md` (full D5 content)
8. `swarm/wiki/foundations/{engineering,mgmt,systems,philosophy,investing}/README.md` ("Phase B fill from books")
9. `swarm/wiki/themes/{engineering,mgmt,systems,philosophy,investing}/README.md`
10. `swarm/wiki/brigadier/README.md`
11. `swarm/wiki/agents/{engineering-expert,mgmt-expert,systems-expert,philosophy-expert,investor-expert}/README.md`
12. `swarm/wiki/insights/README.md` (§1.6 boilerplate)
13. `swarm/wiki/meta/health.md` (D10 skeleton)
14. `swarm/wiki/meta/agent-improvements/{7 files}` (frontmatter only)
15. `swarm/lib/shared-protocols.md` (full D6 content)
16. `agents/<expert>/strategies.md` for 5 experts (empty body + frontmatter)

### D1 §1.5 — `swarm/wiki/overview.md` initial content

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

## Pipeline statuses
`raw → ingested → compiled → linted → ready` (carried from v2; D2 frontmatter `state` field is α-2 lifecycle, distinct from `pipeline`).
```

### D1 §1.6 — `swarm/wiki/insights/README.md` initial content

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

---

## D2 — Per-layer frontmatter schemas

**Source:** spec §2.2 (cross-layer required fields), §2.3 (per-entity
additions), §2.4 (per-numbered-layer additions). Complete extract below.

### D2.1 — Cross-layer required fields (every page, every layer)

Applies to every `.md` page under `swarm/wiki/` except `_templates/`,
`index.md`, `log.md`, `overview.md`, `README.md`, and JSONL files.

```yaml
# Cross-layer required fields (from spec §2.2)
id:                    # string, kebab-slug, regex ^[a-z]+-[a-z0-9-]{1,60}$; unique across swarm/wiki/
title:                 # string, non-empty, ≤120 chars
type:                  # enum: concept|entity|source|claim|idea|topic|experiment|summary|foundation|skill|task|operation|insight|improvement|theme-page
layer:                 # int 1..9 OR 'spine'; matches dir layer per D1 §1.3
niche:                 # enum: personal|business|sales|life|tech|meta (6-niche lock)
created:               # iso-date YYYY-MM-DD; ≤ today
last_modified:         # iso-date YYYY-MM-DD; ≥ created, ≤ today
last_reviewed:         # iso-date (opt; required for foundations/ per Q5 365-day re-review)
pipeline:              # enum: raw|ingested|compiled|linted|ready; default raw/ingested
state:                 # enum: drafted|reviewed|revised|accepted|referenced|superseded|retired|tombstoned (α-2); default drafted
confidence:            # enum: low|medium|high; defaults: foundations=high, ideas=low, else medium
confidence_method:     # enum (opt; req when confidence: high AND type: foundation): expert-judgment|golden-set|cited-source|peer-reviewed|ruslan-attested|brigadier-attested-with-3-supports
tier:                  # enum: core|partner|member|public (24-Lock 13); default core
produced_by:           # string, regex ^(brigadier|human|<expert>-(critic|optimizer|integrator|scalability|writing-support))$
derived_from:          # opt; format <expert>-<mode> or <task-id>:<draft-slug> (chained provenance)
task_id:               # string kebab-slug (opt; req for tasks/, drafts/, artefacts/): ^task-[a-z0-9-]{1,60}$
cycle_id:              # string kebab-slug (opt; req for experiments/, summaries/): ^cyc-[a-z0-9-]{1,40}$
commit_sha:            # string 40-hex (opt); written by /ingest post-commit
captured_by:           # string, regex ^(brigadier|<expert>-<mode>|human|/ingest|/ask|/lint|/consolidate|/build-graph)$
captured_date:         # iso-date ≤ today
sources: []            # list of {path, range?, quote?}; non-empty when pipeline≠raw AND state∉{drafted}
related: []            # list of wikilinks [[type/slug]]; each resolves with reciprocal
topics: []             # list of wikilinks [[topics/slug]]; each resolves
tags: []               # opt; each matches ^#(type|status|priority|topic|niche)/[a-z0-9-]+$
provenance_inline: true  # bool opt; if true, body must contain [src:path#section] per non-trivial paragraph
```

### D2.2 — Per-entity-type additions (§2.3)

#### `concepts/<slug>.md`
```yaml
definition:            # string, single line, non-empty ≤200 chars
examples: []           # list of strings, each ≤200 chars
extends:               # wikilink [[concepts/slug]] opt; produces extends edge (D3)
```

#### `entities/<slug>.md`
```yaml
entity_type:           # enum: person|company|product|team|event|place (required)
external_ids:          # yaml-map (opt): {notion, linkedin, github, hubspot}
  notion:
  linkedin:
  github:
  hubspot:
```

#### `sources/<YYYY-MM-DD>-<slug>.md`
```yaml
source_type:           # enum: article|book|podcast|video|meeting|voice-memo|transcript|web|paper (required)
url:                   # string (req if source_type ∈ {article,video,podcast,web,paper})
local_path:            # string resolves under raw/ (req if source_type ∈ {book,voice-memo,transcript,meeting})
author:                # string opt
ingested_date:         # iso-date (required; today default)
coverage: []           # list of wikilinks [[topics/slug]] (required, may be empty)
```

#### `topics/<slug>.md` (or `<slug>-hub.md` if MOC)
```yaml
MOC_for: []            # list of wikilinks opt; marks Map-of-Content role
```

#### `claims/<slug>.md`
```yaml
stance:                # enum: asserted|supported|contested|refuted (default asserted)
support_count: 0       # int, computed by /build-graph
contradiction_count: 0 # int, computed by /build-graph (bidirectional)
support_edges: []      # list of wikilinks [[claim/slug]] or [[source/slug]]
contradiction_edges: []# list of wikilinks; bidirectional
falsifier:             # string multi-line, non-empty (required)
```

#### `experiments/<YYYY-MM-DD>-<slug>.md`
```yaml
hypothesis:            # string, non-empty, ≤500 chars (required)
start_date:            # iso-date (required; today default)
end_date:              # iso-date opt; ≥ start_date; required for outcome ∈ {won, lost}
outcome:               # enum: open|won|lost|aborted (default open)
cycle_id:              # string kebab-slug ^cyc-[a-z0-9-]{1,40}$ (required)
```

#### `summaries/<scope>-<YYYY-MM-DD>.md`
```yaml
summary_window:        # enum: daily|weekly|topic|cluster (required)
community_id:          # string opt; required when summary_window=cluster
covers: []             # list of wikilinks (required; non-empty)
```

#### `ideas/<slug>.md`
```yaml
proposed_by:           # string (required; default produced_by value)
routing_target:        # enum opt: experiment|claim|topic|drop|skill-candidate
idea_status:           # enum: raw|evaluated|planned|in-progress|shipped|dropped (default raw)
```

#### `foundations/<slug>.md` (and per-theme `foundations/<theme>/<slug>.md`)
```yaml
binding_scope:         # enum (required): swarm-wide | theme:<theme> | expert:<expert>
supersedes_versions: []# list of strings; each <slug>@v<N>
last_reviewed:         # iso-date (required; overrides §2.2 default)
confidence:            # enum (required; override default=high): low|medium|high
```

### D2.3 — Per-layer additions (§2.4, layers 1..9)

#### Layer 1 — `themes/<theme>/...`
```yaml
theme:                 # enum (required, dir-derived): engineering|mgmt|systems|philosophy|investing
book_citations: []     # list of {book_path, page_range?}; book_path resolves under raw/books-md/; empty in Phase A
# Theme → niche mapping (§2.4 table):
#   engineering → tech; mgmt → business; systems → meta; philosophy → meta; investing → business
```

#### Layer 2 — `brigadier/...`
```yaml
bucket:                # enum (required, dir-derived): how-to-solve-problems|how-to-manage-agents|how-to-decompose-tasks|orchestration-state
applies_to:            # enum opt: all-tasks|task-type:<type>|alpha:<alpha-id>
```

#### Layer 3 — `agents/<expert>/...`
```yaml
expert:                # enum (required, dir-derived): engineering|mgmt|systems|philosophy|investor
is_scratchwork: false  # bool opt; when true, page is in scratchwork/ and NOT subject to §5.5.5 gate
```

#### Layer 4 — `meta/agent-improvements/<slug>.md`
```yaml
expert:                # enum (required): engineering|mgmt|systems|philosophy|investor|brigadier|all OR system-level OR emergent
improvement_target:    # enum (required): prompt|protocol|skill|hook|memory-layer
validation_status:     # enum (required): proposed|under-validation|accepted|rejected|tombstoned (default proposed)
proposed_by:           # string (required; default produced_by); <expert>-<mode> or meta-agent or brigadier
applied_by:            # string opt; populated when validation_status=accepted
applied_at:            # iso-date opt; populated with applied_by
```

#### Layer 5 — `tasks/<task-id>/...`
```yaml
task_id:               # string kebab-slug ^task-[a-z0-9-]{1,60}$ (required, dir-derived)
alpha_state:           # enum (required; default submitted): submitted|intaked|decomposed|dispatched|integrated|gated|approved|compounded|archived|refused|returned|rejected
niche:                 # enum (required, per task): personal|business|sales|life|tech|meta
# For tasks/<task-id>/context/manifest.yaml:
pulls: []              # list of {path, priority, source-tier, included_at}; each path resolves; priority 1..N; source-tier ∈ {A,B,C}
total_tokens_estimated:# int (required); ≤ 20000 (Q4 cap)
```

#### Layer 6 — `operations/<project-slug>/...`
```yaml
project_slug:          # string kebab-case ≤30 chars (required, dir-derived); regex ^[a-z0-9][a-z0-9-]{0,29}$; 1:1 with roy/<project-slug>/*
parent_branch:         # string (required; default roy/<project-slug>/main)
iteration:             # int or <unset>; for pages under iterations/v<N>/, set to <N>
```

#### Layer 7 — `global/...`
```yaml
bucket:                # enum (required, dir-derived): solved-patterns|confirmed-anti-patterns|compound-rules
promoted_from:         # wikilink opt; required for compound-rules/; resolves to agents/<expert>/strategies.md line OR meta/agent-improvements/...
```

#### Layer 8 — `skills/<bucket>/<slug>/...`
```yaml
skill_slug:            # string kebab-case (required, dir-derived); regex ^[a-z0-9][a-z0-9-]{0,49}$
skill_state:           # enum (required; default candidate): candidate|learning|active|tombstoned (4 values per α-3 lock)
golden_set_path:       # string opt; required when skill_state ∈ {learning, active}; resolves to swarm/wiki/skills/<bucket>/<slug>/golden-set.jsonl
success_count: 0       # int opt; derived from usage/<slug>.jsonl
loss_count: 0          # int opt; derived
n_uses: 0              # int opt; success+loss
owners:                # yaml-map (required; per Q6 R4 defaults): {transition → role}
```

#### Layer 9 — `insights/...` (Phase A: README only)
```yaml
insight_state:         # enum (req Phase B; default candidate): candidate|promoted
cross_themes: []       # list of theme enums; ≥2 entries to qualify for reviewed
phase_a_lock: true     # bool (required; default true); /lint blocks Layer-9 creation when true AND no Ruslan ack file
```

### D2.4 — Special sub-tree additions (§2.5)

#### `drafts/<task-id>-<expert>-<artefact>.md`
- Required: §2.2 cross-layer + `task_id` + `produced_by = <expert>-<mode>`
- `state` is always `drafted` here; `/lint` flags non-drafted state in drafts/

#### `comparisons/<YYYY-MM-DD>-<question-slug>.md`
- Required: §2.2 + `question:` (string), `synthesis_of:` (list of wikilinks)
- `produced_by = /ask`; state auto-set to `accepted` on write

#### `proposals/<task-id>-decomposition.md`
- Required: §2.2 + `task_id` + `decomposition` (yaml-block: list of `{cell, mode, ap_cost, ap_budget}`) + `produced_by = brigadier`

---

## D3 — `swarm/wiki/_templates/edge-types.md` (full file content)

**Source:** spec §3.5 (file content skeleton) + §3.2 (12 types) + §3.3
(from×to matrix). The spec indicates the file embeds §3.2 entries
inline and the §3.3 matrix. Orchestrator writes this file verbatim
(with §3.2 entries and §3.3 matrix inserted into the placeholders).

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

## Intra-layer types (9 intra-layer — §3.2.1..§3.2.9)

### 1. `extends` (N:1, directed; inverse `extended_by`)
- Definition: Page A refines/expands page B; A is more specific treatment.
- Allowed from/to: spine entity-type (concepts, claims, topics, foundations); Layers 1, 2, 3, 7.
- Lint: no cycles (DAG); flag if `from.layer != to.layer`.
- Example: `{"from":"concepts/llm-wiki","to":"concepts/karpathy-llm-wiki","type":"extends","ts":"2026-04-23","confidence":"high"}`

### 2. `contradicts` (N:M, bidirectional; inverse self)
- Definition: Page A explicitly conflicts with claim/conclusion in B.
- Allowed: claims, foundations, concepts, experiments.
- Lint: both directions present; both pages bear `stance: contested|refuted`.
- Example: `{"from":"claims/embeddings-required","to":"claims/embeddings-deferred","type":"contradicts","ts":"2026-04-23","confidence":"medium"}`

### 3. `supports` (N:M, directed; inverse `supported_by`)
- Definition: Page A provides evidence for claim in B.
- Allowed from: sources, experiments, claims. Allowed to: claims, concepts, foundations.
- Lint: target `support_count` ≥ incoming supports edges.
- Example: `{"from":"sources/2026-04-19-knowledge-arch","to":"claims/4-tier-retrieval","type":"supports","ts":"2026-04-23","confidence":"high"}`

### 4. `inspired_by` (N:M, directed; inverse `inspired`)
- Definition: Creative lineage — idea A inspired by B; looser than extends.
- Allowed from/to: primarily ideas; also experiments, concepts.
- Lint: none blocking; surfaced in /build-graph community detection.
- Example: `{"from":"ideas/swarm-as-memory","to":"ideas/karpathy-llm-wiki","type":"inspired_by","ts":"2026-04-23","confidence":"medium"}`

### 5. `tested_by` (N:M, directed; inverse `tests`)
- Definition: Claim A was empirically tested by experiment B.
- Allowed from: claims, foundations. Allowed to: experiments.
- Lint: experiment must have outcome ∈ {won, lost, aborted} for tests direction; flag open outcome >30d with tested_by ≥1.
- Example: `{"from":"claims/4-tier-retrieval","to":"experiments/2026-05-15-tier3-bfs-benchmark","type":"tested_by","ts":"2026-04-23","confidence":"high"}`

### 6. `invalidates` (N:M, directed; inverse `invalidated_by`)
- Definition: Experiment/evidence B invalidates claim A.
- Allowed from: experiments, sources, claims. Allowed to: claims, foundations.
- Lint: auto-marks `to` page `stance: refuted`; warn if `to` is accepted and not `superseded_by` within 7 days.
- Example: `{"from":"experiments/2026-05-15-tier3-bfs-benchmark","to":"claims/embeddings-required","type":"invalidates","ts":"2026-05-16","confidence":"high"}`

### 7. `supersedes` (N:1, directed new→old; inverse `superseded_by` ALSO stored bidirectionally)
- Definition: New page A replaces older B (often paired with state: superseded on B).
- Allowed from/to: same layer, same type.
- Lint: supersession DAG (no cycles); B bears `state: superseded` and `superseded_by: [[A]]`; A's `supersedes_versions:` includes B.
- Example: `{"from":"foundations/swarm-alphas-v2","to":"foundations/swarm-alphas-v1","type":"supersedes","ts":"2026-04-23","confidence":"high"}`

### 8. `derived_from` (N:M, directed derived→source; inverse `derives`)
- Definition: Source S was used to derive concept/claim/idea P.
- Allowed from: concepts, claims, ideas, summaries, foundations. Allowed to: sources.
- Lint: pages with pipeline ∈ {compiled,linted,ready} AND state ∈ {accepted,referenced} must have ≥1 derived_from OR supports edge OR tier: foundation.
- Example: `{"from":"concepts/4-tier-retrieval","to":"sources/2026-04-19-knowledge-arch","type":"derived_from","ts":"2026-04-23","confidence":"high"}`

### 9. `part_of` (N:1 part→whole, directed; inverse `has_part`) — formalised per Q3
- Definition: Mereological — page A is part of composite B. Dominant v2 edge (233/572 records).
- Allowed from: any spine entity-type. Allowed to: topics (hub→children), foundations (sub → over).
- Lint: target must be topics/<slug>-hub.md OR foundations/ page; re-route otherwise; no cycles (mereology DAG).
- Example: `{"from":"concepts/4-tier-retrieval","to":"topics/retrieval-hub","type":"part_of","ts":"2026-04-23","confidence":"high"}`

## Cross-layer types (3 — §3.2.10..§3.2.12)

### 10. `alpha-ref` (1:1, directed wiki→alpha; inverse `tracked_by` on alpha side)
- Definition: Wiki entity links to alpha tracker (W-1 §D.3).
- Allowed from: entities (spine), agents/<expert>/ (L3), themes/<theme>/ (L1).
- Allowed to: tasks/<task-id>/ (α-1), operations/<project-slug>/ (α-4 composite), swarm/wiki/foundations/swarm-alphas.md.
- Lint: target must exist; flag entities without alpha-ref when entity_type ∈ {company, product, team} AND state ∈ {accepted, referenced}.
- Example: `{"from":"entities/acme-corp","to":"tasks/task-01HF2K3M5N7P9Q","type":"alpha-ref","ts":"2026-04-23","confidence":"high"}`

### 11. `layer-ref` (N:M, directed; inverse `layer-back-ref` derivative)
- Definition: Generic cross-layer link when no specific edge fits. Lower priority than alpha-ref and cross-tree-ref.
- Allowed from/to: any distinct v3 layer pair.
- Lint: "consider more specific edge type" notice when a specific edge matches the from/to pair.
- Example: `{"from":"themes/engineering/concepts/clean-code","to":"global/solved-patterns/test-driven-refactor","type":"layer-ref","ts":"2026-04-23","confidence":"medium"}`

### 12. `cross-tree-ref` (N:M, directed v3→v2 only; no inverse recorded)
- Definition: v3 page citing v2 page (Q9 bridge). v3 → v2 only.
- Allowed from: any v3 page. Allowed to: any v2 page.
- Storage: `swarm/wiki/graph/cross-tree.jsonl` (NOT edges.jsonl).
- Lint: reject `to` under swarm/wiki/ (use layer-ref); reject `from` under v2 wiki/; presence in cross-tree.jsonl mandatory; forbidden in edges.jsonl.
- Example: `{"from":"themes/engineering/concepts/clean-code","to":"wiki/concepts/clean-code","type":"cross-tree-ref","ts":"2026-04-23","confidence":"high","note":"v3 distillation cites v2 baseline"}`

## From-layer × to-layer × allowed types matrix (§3.3)

Rows = `from` layer; columns = `to` layer. Empty cell = rejected by /lint.

Layer abbreviations: **S** = spine entity-type; **L1**=themes;
**L2**=brigadier; **L3**=agents; **L4**=meta/agent-improvements;
**L5**=tasks; **L6**=operations; **L7**=global; **L8**=skills;
**L9**=insights; **v2**=`wiki/`.

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

Phase-A specifics: L9 cells marked "(Phase B)" are rejected in Phase A
per `phase_a_lock: true`.

`addresses_gap` dropped per critic-gate1 H4 — gap-clearing semantics
absorbed by `derived_from` + `/lint` orphan-detection signal.
```

---

## D4 — 9 entity templates (full file content for each)

**Source:** spec §4.2..§4.10. Each fenced block is the literal content
for `swarm/wiki/_templates/<type>.md`.

### D4.1 — `swarm/wiki/_templates/concept.md`

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

### D4.2 — `swarm/wiki/_templates/entity.md`

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

### D4.3 — `swarm/wiki/_templates/source.md`

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

### D4.4 — `swarm/wiki/_templates/claim.md`

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

### D4.5 — `swarm/wiki/_templates/idea.md`

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

### D4.6 — `swarm/wiki/_templates/topic.md`

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

### D4.7 — `swarm/wiki/_templates/experiment.md`

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

### D4.8 — `swarm/wiki/_templates/summary.md`

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

### D4.9 — `swarm/wiki/_templates/foundation.md`

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

---

## D5 — `swarm/wiki/foundations/swarm-alphas.md` (full file, verbatim)

**Source:** spec §5.1..§5.8. The file's Стадия-D bootstrap content is
exactly §5.1..§5.7, wrapped in the §5.8 frontmatter.

### D5 frontmatter (§5.8)

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

### D5 body — α-1 Task

**States:** `submitted | intaked | decomposed | dispatched | integrated | gated | approved | compounded | archived | refused | rejected | returned`

**Transitions:**
| from | to | trigger | mover | side-effects |
|---|---|---|---|---|
| submitted | intaked | brigadier reads+classifies | brigadier | `swarm/wiki/tasks/<task-id>/` dir + `open-questions.md` |
| submitted | refused | out-of-scope/malformed | brigadier | `swarm/gates/refused-<task-id>.md` |
| intaked | decomposed | brigadier writes decomposition | brigadier | `swarm/wiki/proposals/<task-id>-decomposition.md` |
| decomposed | dispatched | first Task() invoked | brigadier | log line in `swarm/logs/<cycle-id>.md` |
| dispatched | integrated | all returns received | brigadier | `artefacts/` populated; dissents preserved |
| integrated | gated | brigadier writes AWAITING-APPROVAL | brigadier | `swarm/gates/AWAITING-APPROVAL-<task-id>-<slug>.md` |
| gated | approved | HITL ack parsed | HITL | `swarm/gates/<task-id>-ack.md` appended |
| gated | rejected | HITL rejects | HITL | `swarm/gates/<task-id>-rejection.md` |
| rejected | returned | brigadier composes return note | brigadier | `tasks/<task-id>/decisions/<ts>-returned.md` |
| approved | compounded | brigadier compound-step | brigadier | `agents/<expert>/strategies.md` and/or `meta/agent-improvements/` |
| compounded | archived | brigadier writes cycle-log | brigadier | `decisions/<ts>-archived.md`; log.md entry |

**Acceptance predicates** (filesystem-testable):
- `intaked`: `tasks/<task-id>/open-questions.md` exists; `alpha_state: intaked`
- `decomposed`: `proposals/<task-id>-decomposition.md` with `decomposition:` ≥1 cell
- `dispatched`: ≥1 line `Task(<expert>-<mode>)` for this task-id in `swarm/logs/<cycle-id>.md`
- `integrated`: every decomposition cell has artefact in `artefacts/`
- `gated`: `AWAITING-APPROVAL-<task-id>-*.md` with 4-response template
- `approved`: `<task-id>-ack.md` with `acked: true`
- `compounded`: marker `<ts>-compounded.md` with `task_id: <task-id>`; zero-or-more new strategies entries
- `archived`: `swarm/logs/<cycle-id>/cycle-log.md` exists AND log.md has `task-archived | <task-id>`

**ASCII diagram** (§5.2): see spec lines 1976–2012.

### D5 body — α-2 Artefact

**States:** `drafted | reviewed | revised | accepted | referenced | superseded | retired | tombstoned` (spec extension: `tombstoned` 8th terminal state).

**Transitions** (highlights):
| from | to | trigger | mover |
|---|---|---|---|
| (none) | drafted | cell writes draft | cell (expert-direct drafts/ only) |
| drafted | reviewed | critic returns Conformance Checklist | integrator or critic-mode cell |
| reviewed | revised | producer/integrator edits | producer or integrator |
| revised ↔ reviewed | re-critique loop | critic-mode cell |
| reviewed | accepted | brigadier passes §5.5.5 gate | brigadier |
| accepted | referenced | another accepted artefact consumes this | brigadier |
| accepted | superseded | newer accepted supersedes | brigadier |
| accepted/superseded | retired | EOL identification | brigadier (after meta-agent draft) |
| any (non-drafted) | tombstoned | invalidated OR Ruslan-attested withdrawal | brigadier (via gate-file-ack for Ruslan path) |

**Forbidden:** `drafted → tombstoned` (unpromoted drafts are simply deleted; no archive/tombstone).

**Acceptance predicates** — see spec §5.3 (lines 2047–2056).

**ASCII diagram:** spec lines 2065–2090.

### D5 body — α-3 Strategies-Rule (4 states, FPF-canonical)

| FPF state | Spec alias | Definition |
|---|---|---|
| proposed | candidate | 4-part DRR submitted |
| active | learning | ≥1 successful use; under golden-set eval |
| validated | active | ✓/✗ ≥ 3:1 over ≥10 uses; live skill registry |
| tombstoned | tombstoned | ratio <1:1 cumulative OR Ruslan-retire OR incident OR superseded |

**Canonical = FPF names.** Wiki/lint/build-graph all use FPF names.

**Transitions:**
| from | to | trigger | mover |
|---|---|---|---|
| (none) | proposed | brigadier compound writes DRR | brigadier |
| proposed | active | first successful cell-use | brigadier (records in usage/<slug>.jsonl) |
| active | validated | golden-set ≥3 + ≥10 uses + ✓/✗ ≥3:1 (D11) | brigadier (after meta-agent audit-via-task) |
| validated | active (demoted) | ratio drops to 1:1 ≤ r < 3:1 over rolling 10 | meta-agent-via-task → brigadier writes |
| any | tombstoned | <1:1 cumulative OR Ruslan retire OR incident OR superseded | brigadier |

**ASCII diagram:** spec lines 2149–2170.

### D5 body — α-4 Cycle

**States:** `opened | running | integrating | gated | compounded | closed | tombstoned`.

**Spec alias map:** open→opened; mid-cycle→running+integrating; closing→gated+compounded; closed→closed.

**Transitions:** see spec §5.5 (lines 2201–2209). Key: α-4 `closed` count is the authoritative metric for Q8 Layer-9 trigger #1 (≥50 closed cycles).

**Acceptance predicates** — `closed`: `swarm/logs/<cycle-id>/cycle-log.md` exists with frontmatter `summary:` (≥1 line) and `open_questions:` (≥1 line); `closed_cycles_count` in `meta/health.md` incremented.

**ASCII diagram:** spec lines 2226–2253.

### D5 body — α-5 Direction (human-owned, Phase A lightweight)

**States:** `hypothesized | under-validation | validated | activated | scaled | plateaued | invalidated | dropped | archived`. Pivot branches: `under-validation → hypothesized`; `invalidated → hypothesized`.

**Movers:** human/strategic-management for hypothesized+activated; brigadier tracks state; experts contribute evidence artefacts. **AI agents do NOT move α-5** beyond tracking.

**Phase A vs B:** Phase A = state-enum-only, flat list in swarm-alphas.md α-5 section; no machine validator required. Phase B defers NQD-CAL+E/E-LOG+BLP formalization per FPF Part 10.6.

**HITL discipline:** any α-5 state change is HITL-only (AWAITING-APPROVAL file).

**ASCII diagram:** spec lines 2316–2349.

### D5 §5.7 — Cross-alpha integrations summary matrix

| | α-1 Task | α-2 Artefact | α-3 Strategies | α-4 Cycle | α-5 Direction |
|---|---|---|---|---|---|
| α-1 | self | creates instances dispatched→integrated | emits at compounded | inhabits α-4 (1:1) | task may target direction (info) |
| α-2 | created during α-1 | self | strategies cite α-2 artefacts | exists inside α-4 | direction evidence is α-2 |
| α-3 | emitted at α-1 compounded | strategies cite α-2 | self | activation/retirement triggered by cycle aggregates | strategies may inform direction |
| α-4 | contains 1× α-1 | hosts α-2 from running→compounded | drives α-3 validated | self | cycle counts feed direction validation |
| α-5 | n/a (HITL) | direction evidence is α-2 | n/a | spans multiple α-4 | self |

---

## D6 — `swarm/lib/shared-protocols.md` (full file, 9 sections, verbatim)

**Source:** spec §6.1..§6.11. Each of 9 sections below is ≤25-line
fenced block suitable for `swarm/lib/shared-protocols.md` body.
Frontmatter at §6.11 is the file header.

### D6 frontmatter (§6.11)

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

### Section 1 — Wiki write protocol (single-writer brigadier)

```markdown
## 1. Wiki write protocol (Q2 single-writer brigadier)

All writes to `swarm/wiki/` flow through the brigadier. Cells (5×4=20)
write only to `swarm/wiki/drafts/<task-id>-<expert>-<artefact>.md` and
return drafts via `Task()` structured return (see §3). Brigadier reads,
runs §5.5.5 gate (§2), commits canonical. No role-mode bypasses this.
Exception: `agents/<expert>/strategies.md` — expert writes directly (Level-1
personal memory per CLAUDE.md T5/R6).

Pre-write checklist (brigadier):
1. Read cell-returned draft.
2. Load template from `_templates/<type>.md` (D4); verify frontmatter complete.
3. Load edge enum `_templates/edge-types.md` (D3); verify wikilinks→related[]→edges.jsonl triple.
4. Run §5.5.5 provenance gate (§2).
5. On pass: Write; append edges.jsonl; update index.md; prepend log.md.
6. On fail: write rejection in `tasks/<task-id>/decisions/<ts>-rejection.md`;
   draft stays in `drafts/`.

Commit message: `[<agent>] <cycle>: <description>` per master synthesis §5.9.
```

### Section 2 — Provenance gate (§5.5.5 v3 enforcement)

```markdown
## 2. Provenance gate (§5.5.5 v3 enforcement)

Every brigadier Write to `swarm/wiki/` must satisfy ALL:

1. Provenance present. sources[] non-empty AND each path resolves to
   one of: sources/* with state ∈ {accepted, referenced}; Tier-1 file
   (decisions/, design/, raw/research/, raw/articles/, prompts/,
   CLAUDE.md, .claude/rules/); `(incident_file, commit_hash)` tuple
   `<path>@<40-hex>`; `(verbatim, line-range)` `<path>:<start>-<end>`.
2. Inline citations consistent. If `provenance_inline: true`, body
   contains ≥1 `[src:<path>#<section>]` per non-trivial paragraph.
3. Edge consistency. Every [[wikilink]] in body has related[] entry
   AND edges.jsonl record per D3.
4. Tier coherence. Outgoing tier no stricter than any input source tier.
5. Foundation conditions. type=foundation requires confidence_method ∈
   {ruslan-attested, brigadier-attested-with-3-supports}; brigadier-
   attested requires ≥3 supports edges from accepted claims.
6. Non-contradicting. On state→accepted, no existing accepted page
   contradicts without explicit contradicts edge.

REJECT cases: empty sources[] when pipeline ∈ {compiled,linted,ready}
AND state ∉ {drafted}; raw/ source with pipeline:raw grounding compiled+;
matrix-violating edge in edges.jsonl.
```

### Section 3 — Structured output schema (Task return contract)

```markdown
## 3. Structured output schema (Task return contract)

Every Task() return is a structured YAML packet:

- summary: string ≤500 chars (required)
- proposed_writes[]: {path, frontmatter, body, edges_to_add[]} — may be empty
- provenance[]: {path, range?, quote?} — required ≥1 when proposed_writes
  or escalations non-empty; may be empty when both empty
- confidence: low|medium|high (required)
- confidence_method: enum (required) — justify confidence to brigadier
- escalations[]: {trigger, packet_path?} — may be empty; trigger ∈
  {foundation-revision, layer-9-activation, contradiction,
   budget-overrun, retry-limit, peer-input-needed, permission-denied}
- dissents[]: {position, evidence[]} — required iff produced_by matches
  `*-integrator`
- extractions[], alternatives[], anti_scope[]: required iff mode:
  writing-support (§6.7)

Validation: brigadier rejects malformed returns; cell's draft stays in
drafts/; brigadier may re-invoke with Task(..., context:{schema_error}).
```

### Section 4 — HITL escalation + AWAITING-APPROVAL packet

```markdown
## 4. HITL escalation rules + AWAITING-APPROVAL packet

Escalate to Ruslan when ANY:
1. Foundation revision (create or supersede accepted foundations/).
2. Layer-9 activation (Q8 3-AND trigger per D10).
3. Contradiction with accepted foundation without obvious resolution.
4. Budget overrun (maxTurns or token budget hit).
5. Retry limit (draft rejected 2× consecutively per §2).
6. α-5 Direction state change (AI agents never move α-5).
7. Method exhaustion (same AP >5× across cycles).
8. Irreversible decision (architecture commit, dep change, protocol mod).
9. split_trigger fires in Block 5 of an expert manifest.

Packet file: `swarm/gates/AWAITING-APPROVAL-<id>-<YYYY-MM-DD>.md` with
frontmatter {title, type: gate, gate_type, escalator: brigadier,
escalated_at, task_id?, cycle_id?, deadline?, state: open}. Body sections:
Context, Options (1-4), Recommendation, Risk, Proposed file path(s),
How Ruslan acks.

Ack mechanism: `<id>-ack.md` with `acked: true`, `chosen: <letter>`, `notes:`.
Or frontmatter mutation `state: acked` + `chosen: <letter>`. On ack
detection, brigadier moves α-1 gated→approved and α-4 gated→compounded.
```

### Section 5 — Tool permission self-check

```markdown
## 5. Tool permission self-check

Ritual executed by every cell at function entry (pseudo-code):

  my_role := get_my_role()  # brigadier | <expert>-<mode> | meta-agent | /skill
  intended_tool := <Tool name>
  intended_target := <path or arg>
  allowed := lookup(role_tool_matrix, my_role, intended_tool, intended_target)
  if not allowed:
    log "permission_denied: role=..., tool=..., target=..."
    return Task() with escalations: [{trigger: permission-denied, ...}]
  else: proceed

role_tool_matrix:
- brigadier: Read=*; Write=*(swarm/, agents/, .claude/); Bash=yes;
  Task=yes; MCP=yes
- <expert>-<mode>: Read=*; Write=swarm/wiki/drafts/<task-id>-<expert>-*,
  swarm/wiki/foundations/<expert-domain>/*, agents/<expert>/strategies.md;
  Bash=no; Task=no; MCP=no
- meta-agent: same as expert (drafts only via writing-support)
- skills (/ingest, /ask, /lint, /consolidate, /build-graph): Read=*;
  Write=per skill manifest (D8); Bash=yes (scoped); Task=no; MCP=no

On permission deny: NEVER silently retry. Return escalations[] entry.
Brigadier re-routes OR escalates to HITL.
```

### Section 6 — Cross-cell-reference protocol (read wiki, never call cell)

```markdown
## 6. Cross-cell-reference protocol (read wiki, never call cell)

FPF Part 10.5 mandate (verbatim): "Cross-cell-reference protocol (read
wiki, never call cell)." Master synthesis §4.5.4: "A cell may read any
wiki artefact. A cell may write only its own output artefact. A cell
may NOT invoke another cell."

Operational contract:
- READ allowed: any path under swarm/wiki/ (incl. drafts/), any v2 wiki/,
  any Tier-1 (decisions/, design/, raw/research/, prompts/, CLAUDE.md,
  .claude/rules/).
- READ forbidden: other cells' context windows; Task(<peer-expert>, ...)
  to fetch a fresh draft from a peer expert.
- WRITE allowed: only swarm/wiki/drafts/<task-id>-<self>-<artefact>.md.

If cell A needs cell B's output: A returns escalations[] entry
{trigger: peer-input-needed, requested: "<expert>-<mode> on <topic>",
context_path: <task-dir>}. Brigadier dispatches Task(<B>, ...), integrates
B's draft. A is re-invoked with B's draft visible under drafts/.

/lint rule: Task return body containing `Task(` invocation strings is
flagged. Static check at draft promotion. Rejects via §2 if found.
```

### Section 7 — `mode: writing-support`

```markdown
## 7. mode: writing-support

Verbatim FPF Part 10.5 + Part 5 §5.3 E-10: "Add a mode: writing-support
sub-clause inside §7 (shared protocols) for all 5 experts: If invoked
to contribute to a weekly review, quarterly letter, or strategizing
document, DO NOT generate primary prose. Return: (a) structured
extractions from cited artefacts, (b) proposed alternatives enumerated,
(c) explicit anti-scope list. Human owns composition."

Contract when invoked `Task(<expert>-<mode>, mode: writing-support, ...)`:
- Cell produces NO primary prose.
- Return packet contains:
  - extractions[]: {quote, source_path, range} structured facts
  - alternatives[]: enumerated options per §3 schema
  - anti_scope[]: explicit list of items NOT to include
- Brigadier or HITL composes final; cells never edit final.
- writing-support is a brigadier-only auxiliary capability — NOT a 5th
  matrix mode (preserves 5×4=20 invariant per master synthesis §5.10.3).
- Use cases: weekly review; quarterly Ruslan letter; strategizing
  artefacts; meta-agent improvements to meta/agent-improvements/.

Anti-pattern lock (FPF [B §E.3]): "полная автоматизация writing... LLM
всегда обманет." Phase B: /lint may enforce `produced_by:
<expert>-writing-support` + `human_composed_at:` timestamp.
```

### Section 8 — Tool-language abstractions (verb dictionary)

```markdown
## 8. Tool-language abstractions (verb dictionary)

FPF Part 10.5 + Part 2 §2.7 E-7 move 2: rename tooling tokens to
pattern-layer abstractions in shared protocols.

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
| swarm/wiki/drafts/ | draft area |
| swarm/wiki/<canonical>/ | canonical area |
| swarm/gates/ | gate dock |
| swarm/lib/shared-protocols.md | shared protocols |
| agents/<expert>/strategies.md | personal memory |
| swarm/wiki/meta/agent-improvements/ | swarm memory |

Lock 17 (Filesystem = SoT) preserved; purely naming-layer discipline.
```

### Section 9 — Max-subscription discipline

```markdown
## 9. Max-subscription discipline (extension per master synthesis §5.7)

SessionStart hook (assert no API key set):

  if [ -n "$ANTHROPIC_API_KEY" ]; then
    echo "WARNING: ANTHROPIC_API_KEY is set; Jetix uses Max subscription"
    echo "Run: unset ANTHROPIC_API_KEY"
    exit 1
  fi

`unset ANTHROPIC_API_KEY` enforced at every session start. Optionally
`unset GROQ_API_KEY` if Whisper pipeline not in use.

Prohibited (closes §5.7 ambiguity #1):
- No vector DB (Pinecone, Weaviate, etc.).
- No paid embeddings (OpenAI, Cohere, etc.).
- No third-party LLM APIs (Claude Code Max only).
- No paid transcription outside voice-memo pipeline windows.

Retrieval Phase A = filesystem + ripgrep + typed-BFS over
`graph/edges.jsonl` (Q1 4-tier).

Tool matrix: skills run via Read/Write/Grep/Glob/Bash only. No SDK
invocations.

Cost = turn-counting, not billing. With ANTHROPIC_API_KEY unset, attack
surface shifts to "Max plan rate-limit hit" — recovery = downtime, not money.

Per-cycle commit+push ritual: log.md updates atomic with wiki write.
Branch: claude/jolly-margulis-915d34 (current Phase A); no force-push.
```

### D6 — Section 9 is §6.10 in spec (Retrieval stack)

**Note on prompt's 9-section ordering vs spec.** The prompt requests
9 sections in the order: (1) wiki write protocol, (2) provenance gate,
(3) structured output schema, (4) HITL escalation, (5) tool permission
self-check, (6) writing-support, (7) tool-language abstractions, (8)
Max-subscription discipline, (9) retrieval stack. The spec orders them
slightly differently: §6.2 wiki-write, §6.3 §5.5.5 gate, §6.4 schema,
§6.5 HITL, §6.6 permission, §6.7 cross-cell-ref, §6.8 writing-support,
§6.9 verb dictionary, §6.10 Max-subscription. The prompt's section 9
"Retrieval stack" is not a distinct D6 section in the spec —
`[GAP — orchestrator must fill]` if prompt's 9-section ordering is
load-bearing. The shared-protocols.md body above uses spec ordering.
The retrieval stack content (Q1 4-tier) is covered tangentially in §9
above; a dedicated §Retrieval section would restate: Tier 1 direct
path → Tier 2 index+grep → Tier 3 typed-BFS over graph/edges.jsonl →
Tier 4 long-context fallback bounded to current-niche dir.

---

## D7 — `.claude/config/wiki-roots.yaml` (full file, verbatim)

**Source:** spec §7.2. Orchestrator writes verbatim.

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

---

## D8 — 5 in-scope skill diffs + 3 documented exclusions

### D8 shared preamble (§8.2) — inserted into each of 5 in-scope skills

Inserted immediately after the frontmatter closing `---` (before `# Skill: /...`):

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

### D8.1 — `/ingest` (`.claude/skills/ingest.md`, 135 → 153 lines)

**Current file verified** (Read): 135 lines matching audit baseline;
substantive wiki/ references at L62 (wiki/{type}/{slug}.md), L65
(wiki/_templates/), L71 (wiki/sources/), L78 (wiki/graph/edges.jsonl),
L90 (wiki/index.md), L100 (wiki/log.md), L111 (wiki/niches/); prose
at L3 (description), L15 (body). Niche-enum at L45 carries `global`
(to be removed per critic-gate1 S3).

**Edit #1 — insert preamble after L5.** No before; insert §8.2 preamble
(9 lines).

**Edit #2 — L3 description.**
- Before: `description: "Поднять источник из raw/ (или по URL) в wiki/: распарсить, создать entity-страницы, обновить index/log/edges."`
- After: `description: "Поднять источник из raw/ (или по URL) в ${WIKI_ROOT}/: распарсить, создать entity-страницы, обновить index/log/edges. (Default root: swarm/wiki per D7.)"`

**Edit #3 — L15.**
- Before: `Превратить сырой источник (файл в \`raw/\` или URL) в связанный набор страниц wiki/.`
- After: `Превратить сырой источник (файл в \`raw/\` или URL) в связанный набор страниц \`${WIKI_ROOT}/\`.`

**Edit #4 — L45 niche enum.**
- Before: `Прочитать содержимое. Выбрать одну из: \`personal\`, \`business\`, \`sales\`, \`life\`, \`tech\`, \`meta\`, \`global\`.`
- After: `Прочитать содержимое. Выбрать одну из: \`personal\`, \`business\`, \`sales\`, \`life\`, \`tech\`, \`meta\`. (6 niches per CLAUDE.md L70 lock; \`global\` content lives in Layer 7 \`${WIKI_ROOT}/global/\` per D1.)`

**Edit #5 — L62.**
- Before: `1. Построить путь: \`wiki/{type}/{slug}.md\`.`
- After: `1. Построить путь: \`${WIKI_ROOT}/{type}/{slug}.md\`.`

**Edit #6 — L65.**
- Before: `3. Если нет → взять шаблон из \`wiki/_templates/{type}.md\`, заполнить.`
- After: `3. Если нет → взять шаблон из \`${WIKI_ROOT}/_templates/{type}.md\`, заполнить.`

**Edit #7 — L71.**
- Before: `\`wiki/sources/YYYY-MM-DD-slug.md\` по шаблону \`source.md\`:`
- After: `\`${WIKI_ROOT}/sources/YYYY-MM-DD-slug.md\` по шаблону \`source.md\`:`

**Edit #8 — L78.**
- Before: `### 6. Добавить edges в \`wiki/graph/edges.jsonl\``
- After: `### 6. Добавить edges в \`${WIKI_ROOT}/graph/edges.jsonl\` (v3 intra-tree). Для v3→v2 ссылок — \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\` (D3 §3.2.12 + T1).`

**Edit #9 — L80-L82 edge-type list.**
- Before: `Append-only. Один JSON на строку. 9 типов: \`extends\`, \`contradicts\`, \`supports\`, \`inspired_by\`, \`tested_by\`, \`invalidates\`, \`supersedes\`, \`addresses_gap\`, \`derived_from\`.`
- After: `Append-only. Один JSON на строку. **12 типов per D3 §3.2** (9 intra-layer + 3 cross-layer): \`extends, contradicts, supports, inspired_by, tested_by, invalidates, supersedes, derived_from, part_of, alpha-ref, layer-ref, cross-tree-ref\`. (\`addresses_gap\` dropped per critic-gate1 H4.)`

**Edit #10 — L90.** `wiki/index.md` → `${WIKI_ROOT}/index.md`.

**Edit #11 — L100.** `wiki/log.md` → `${WIKI_ROOT}/log.md`.

**Edit #12 — L111.**
- Before: `В \`wiki/niches/{niche}/README.md\` в секцию \`## Pages\` добавить линк на новые страницы.`
- After: `В \`${WIKI_ROOT}/niches/{niche}/README.md\` в секцию \`## Pages\` добавить линк на новые страницы. (Niche enum: 6 values per CLAUDE.md L70 lock — \`personal/business/sales/life/tech/meta\`; \`global\` removed per critic-gate1 S3.)`

**Rationale.** Wires `$WIKI_ROOT` per D7; aligns edge enum with D3 12-type list (drops `addresses_gap`); aligns niche enum with 6-lock; adds cross-tree handoff.

**Test plan.**
1. `unset WIKI_ROOT && /ingest raw/articles/foo.md` → expect `swarm/wiki/sources/<…>.md` written.
2. `WIKI_ROOT=wiki /ingest raw/articles/foo.md` → expect `wiki/sources/<…>.md` (backward-compat).
3. `/ingest raw/v3-test.md` → expect edge in `swarm/wiki/graph/edges.jsonl`, not v2.

### D8.2 — `/ask` (`.claude/skills/ask.md`, 116 → 134 lines)

**Current file verified.** Substantive paths at L20, L27, L28, L29, L60,
L71, L100; prose at L3, L11.

**Edit #1** — insert preamble after L5.

**Edit #2 — L3.**
- Before: `description: "Ответить на вопрос по wiki/: подобрать 5-15 страниц, синтезировать с цитатами, сохранить ценный ответ в comparisons/."`
- After: `description: "Ответить на вопрос по \`${WIKI_ROOT}/\` (default v3): подобрать 5-15 страниц, синтезировать с цитатами, сохранить ценный ответ в \`${WIKI_ROOT}/comparisons/\`."`

**Edit #3 — L11.** `wiki/` → `${WIKI_ROOT}/`.

**Edit #4 — L20.** `wiki/index.md` → `${WIKI_ROOT}/index.md`.

**Edit #5 — L27.** `wiki/**/*.md` → `${WIKI_ROOT}/**/*.md`.

**Edit #6 — L28.** `wiki/niches/sales/` → `${WIKI_ROOT}/niches/sales/`.

**Edit #7 — L29.**
- Before: `- Если есть community summaries (\`wiki/graph/summaries.md\`) — используй их для быстрого контекста.`
- After: `- Если есть community summaries (\`${WIKI_ROOT}/graph/summaries.md\`) — используй их для быстрого контекста. (Tier 4 long-context fallback per Q1: scope to current niche dir, not full wiki.)`

**Edit #8 — L60.** `wiki/comparisons/` → `${WIKI_ROOT}/comparisons/`.

**Edit #9 — L71.** `wiki/comparisons/...` → `${WIKI_ROOT}/comparisons/...`.

**Edit #10 — L100.**
- Before: `Добавить edges в \`wiki/graph/edges.jsonl\`.`
- After: `Добавить edges в \`${WIKI_ROOT}/graph/edges.jsonl\` per D3 12-enum. Cross-tree refs (v3→v2) → \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\` per T1.`

**Rationale.** Parameterises all paths; aligns with Q1 4-tier retrieval + D3 edges + T1 cross-tree.

**Test plan.**
1. Default-root: `/ask "что такое 4-tier retrieval"` → reads `swarm/wiki/index.md`; comparisons land in `swarm/wiki/comparisons/`.
2. `WIKI_ROOT=wiki /ask ...` → reads `wiki/index.md`; comparisons in `wiki/comparisons/`.

### D8.3 — `/lint` (`.claude/skills/lint.md`, 103 → 121 lines + new sections)

**Current file verified.** Paths at L21, L30, L38, L55, L60, L92, L102;
prose at L3, L11. Currently 7 checks.

**Edit #1** — insert preamble after L5.

**Edit #2 — L3.**
- Before: `description: "Health check wiki/: 7 проверок..."`
- After: `description: "Health check \`${WIKI_ROOT}/\` (default v3): 5-signal /lint orchestration per Q5 + structural checks (orphans, stale, broken links, missing frontmatter, contradictions, missing cross-refs, index drift)."`

**Edit #3 — L11.** `wiki/` → `${WIKI_ROOT}/`.

**Edit #4 — L21.** `wiki/graph/edges.jsonl` → `${WIKI_ROOT}/graph/edges.jsonl`.

**Edit #5 — L30.**
- Before: `\`wiki/claims/*.md\` где \`confidence: low\` И \`updated:\` старше 60 дней от сегодня.`
- After: `\`${WIKI_ROOT}/claims/*.md\` где \`confidence: low\` И \`updated:\` старше 60 дней от сегодня. **Дополнительно: \`${WIKI_ROOT}/foundations/*.md\` где \`last_reviewed:\` старше 365 дней (Q5 §3 + D2 §2.3 foundations re-review).**`

**Edit #6 — L38.**
- Before: `Markdown в \`wiki/**/*.md\` без обязательных полей: \`title\`, \`type\`, \`niche\`, \`created\`, \`updated\`, \`pipeline\`.`
- After: `Markdown в \`${WIKI_ROOT}/**/*.md\` без обязательных полей per D2 §2.2 cross-layer table: \`id, title, type, layer, niche, created, last_modified, pipeline, state, confidence, tier, produced_by, sources, related, topics, captured_by, captured_date\`.`

**Edit #7 — L55.** `wiki/` → `${WIKI_ROOT}/`.

**Edit #8 — L60.** `wiki/_lint-report-YYYY-MM-DD.md` → `${WIKI_ROOT}/_lint-report-YYYY-MM-DD.md`.

**Edit #9 — L92.** path in example → use `${WIKI_ROOT}/`.

**Edit #10 — L102.** `wiki/log.md` → `${WIKI_ROOT}/log.md`.

**Edit #11 — insert NEW sections after L17 "Проверки":**

```markdown
### 8. α-2/α-3 lifecycle state validity (per Q5 signal #2)

For pages under `${WIKI_ROOT}/skills/` OR with `type: skill`:
flag pages with `state ∉ {candidate, learning, active, tombstoned}`
(α-3 4-state lock per critic-gate1 S2 + D2 §2.4 Layer 8).

For all other pages: flag pages with
`state ∉ {drafted, reviewed, revised, accepted, referenced, superseded, retired, tombstoned}`
(α-2 8-state set per D5 §5.3).

### 9. Triple-channel cross-ref consistency (per D2 §2.2 lint #5)

Every inline wikilink matching `\[\[(?P<type>[a-z]+)/(?P<slug>[a-z0-9-]+)\]\]`
(non-matching forms like `[[A]]` or `[[file.md]]` are **warned** as
legacy/unparseable, not errored) MUST appear in `related[]` AND
produce one record in `${WIKI_ROOT}/graph/edges.jsonl`.

### 10. Q8 Layer-9 lock (per D1 §1.6)

Flag the existence of any file under `${WIKI_ROOT}/insights/{candidates,promoted}/*.md`
(any leaf `.md` write outside `README.md`) when D1 §1.6 boilerplate is
in effect. Per Q8 `phase_a_lock: true`.

### 11. Symlink integrity (per D9 §9.7)

For each .md file in `.claude/skills/`:
- if file is a symlink:
  - EMIT "broken symlink" if target doesn't exist
  - EMIT "symlink target outside active/" if not `../../swarm/wiki/skills/active/`
  - EMIT "symlink basename mismatch" if target basename != file basename
```

**Rationale.** /lint absorbs Q5 5-signal orchestration, triple-channel
consistency, Q8 Phase-A lock, and D9 symlink audit. Substantive semantic
upgrades; slight line-budget inflation vs ~18-line audit estimate.

**Test plan.**
1. Default-root: `/lint` → walks `swarm/wiki/`; emits `swarm/wiki/_lint-report-2026-04-23.md`.
2. Draft page with `[[concepts/foo]]` body but missing `related[]`/edges → flagged under check #9.
3. Try writing `swarm/wiki/insights/candidates/test.md` with `phase_a_lock: true` → rejected under check #10.
4. Create broken symlink in `.claude/skills/` → flagged under check #11.

### D8.4 — `/consolidate` (`.claude/skills/consolidate.md`, 96 → 115 lines)

**Current file verified.** Paths at L36, L37, L68, L70, L73, L76, L80, L81; prose at L3, L11.

**Edit #1** — insert preamble after L5.

**Edit #2 — L3.** `wiki/` → `${WIKI_ROOT}/`.

**Edit #3 — L11.** `wiki/` → `${WIKI_ROOT}/`.

**Edit #4 — L36.** `wiki/concepts/value-based-pricing.md` → `${WIKI_ROOT}/concepts/value-based-pricing.md`.

**Edit #5 — L37.** `wiki/concepts/value-pricing.md` → `${WIKI_ROOT}/concepts/value-pricing.md`.

**Edit #6 — L68.**
- Before: `   - Обновить \`wiki/graph/edges.jsonl\`: где \`from: B\` → \`from: A\`, где \`to: B\` → \`to: A\``
- After: `   - Обновить \`${WIKI_ROOT}/graph/edges.jsonl\`: где \`from: B\` → \`from: A\`, где \`to: B\` → \`to: A\`. **Также пройти по \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\` для v3-сторонних ссылок на B.**`

**Edit #7 — L70.** `wiki/index.md` → `${WIKI_ROOT}/index.md`.

**Edit #8 — L73.**
- Before: `   - Перед удалением — создать копию в \`wiki/_archive/YYYY-MM-DD-B.md\` (с комментом "merged into A").`
- After: `   - Перед удалением — создать копию в \`${WIKI_ROOT}/_archive/YYYY-MM-DD-B.md\` (с комментом "merged into A"). **Per critic-gate2 SS3: this skill runs as expert (D6 §6.6.3 role_tool_matrix) and CANNOT mutate canonical α-2 \`state\` field — that requires brigadier per Q2/D6 §6.2. /consolidate writes the \`_archive/\` copy with the original frontmatter unchanged + appends an HTML comment \`<!-- merged into A on YYYY-MM-DD per /consolidate; α-2 state transition pending brigadier review -->\`. The brigadier subsequently transitions α-2 \`state: superseded\` + \`superseded_by: [[<A-path>]]\` per D5 §5.3 movers (separate commit).**`

**Edit #9 — L76.** `wiki/log.md` → `${WIKI_ROOT}/log.md`.

**Edit #10 — L80.** example path → `${WIKI_ROOT}/`.

**Edit #11 — L81.** example path → `${WIKI_ROOT}/_archive/`.

**Rationale.** Parameterises paths; clarifies α-2 ownership (brigadier mutates state, not /consolidate); wires cross-tree handoff.

**Test plan.**
1. Set up duplicate `swarm/wiki/concepts/foo.md` and `swarm/wiki/concepts/foo-v2.md`; run `/consolidate` → on `y`, loser in `swarm/wiki/_archive/`; frontmatter has comment but no state mutation.
2. v3→v2 cross-tree-ref to loser → cross-tree.jsonl record rewritten to survivor.

### D8.5 — `/build-graph` (`.claude/skills/build-graph.md`, 97 → 113 lines)

**Current file verified.** Paths at L22, L33, L62, L73, L86; prose at L3, L11.

**Edit #1** — insert preamble after L5.

**Edit #2 — L3.**
- Before: `description: "Пройти по wiki/, добить недостающие edges в edges.jsonl, пересчитать communities + summaries."`
- After: `description: "Пройти по \`${WIKI_ROOT}/\` (default v3), добить недостающие edges в edges.jsonl per D3 12-enum, пересчитать communities + summaries. Поддерживает \`--tree {v2|v3|both}\` per T1."`

**Edit #3 — L11.** `wiki/` → `${WIKI_ROOT}/`.

**Edit #4 — L22.**
- Before: `Glob \`wiki/**/*.md\`, исключить \`index.md\`, \`log.md\`, \`overview.md\`, \`_templates/*\`, \`niches/*/README.md\`, \`graph/*\`, \`_archive/*\`, \`_lint-report-*\`.`
- After: `Glob \`${WIKI_ROOT}/**/*.md\`, исключить \`index.md\`, \`log.md\`, \`overview.md\`, \`_templates/*\`, \`niches/*/README.md\`, \`graph/*\`, \`_archive/*\`, \`_lint-report-*\`. **При \`--tree=both\`: повторить glob для v2 \`wiki/**/*.md\` и v3 \`swarm/wiki/**/*.md\`; cross-tree-ref edges (D3 §3.2.12) пишутся в \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\`.**`

**Edit #5 — L33.**
- Before: `Прочитать \`wiki/graph/edges.jsonl\` в память (set по \`(from, to, type)\`).`
- After: `Прочитать \`${WIKI_ROOT}/graph/edges.jsonl\` в память. При \`--tree=both\` — также \`${WIKI_ROOT_V3}/graph/cross-tree.jsonl\`.`

**Edit #6 — L37-L46 (edge type detection rewrite):**

```markdown
1. Определить тип edge per D3 12-enum:
   - Расширяет/Extends → `extends`.
   - Противоречит/Contradicts → `contradicts` (запись BIDIRECTIONAL — обе стороны записать).
   - Поддерживает/Supports → `supports`.
   - Вдохновлён/Inspired by → `inspired_by`.
   - Тестируется/Tested by → `tested_by`.
   - Опровергает/Invalidates → `invalidates`.
   - Заменяет/Supersedes → `supersedes`.
   - Часть/Part of → `part_of` (FORMALIZED per Q3).
   - Иначе (упоминание сущности) → `derived_from`.
   - Cross-layer (5×4 matrix → alpha tracker) → `alpha-ref`.
   - Cross-layer (theme → global pattern) → `layer-ref`.
   - v3→v2 link → `cross-tree-ref` (запись в cross-tree.jsonl, НЕ edges.jsonl).
   - **Снят: `addresses_gap` per critic-gate1 H4.**
```

**Edit #7 — L62.** `wiki/graph/communities.md` → `${WIKI_ROOT}/graph/communities.md`.

**Edit #8 — L73.** `wiki/graph/summaries.md` → `${WIKI_ROOT}/graph/summaries.md`.

**Edit #9 — L86.** `wiki/log.md` → `${WIKI_ROOT}/log.md`.

**Rationale.** D3 12-enum migration; bidirectional contradicts; T1 cross-tree separation; --tree=both flag for combined passes.

**Test plan.**
1. Default-root: `/build-graph` → edges in `swarm/wiki/graph/edges.jsonl`.
2. `/build-graph --tree=both` → cross-tree-refs in `swarm/wiki/graph/cross-tree.jsonl`.
3. Verify `contradicts` edge A→B also has inverse B→A record.

### D8.6 — Documented exclusions (3 skills NOT parameterised)

Brief comment blocks inserted at top of each file (after frontmatter,
before `# Skill:`). Do NOT modify behaviour.

#### D8.6.1 `/search-kb` (.claude/skills/search-kb.md, 38 lines)

Insert after frontmatter:

```markdown
> **Exclusion (per D7 + D8 §8.8.1).** This skill is NOT parameterised for
> `$WIKI_ROOT`. Rationale: zero `wiki/` references; targets
> `knowledge-base/_index.md`, `knowledge-base/{cluster}/_moc.md`, and
> `raw/`. Legacy KB lookup supplanted by `/ask` Tier-1/2 retrieval (Q1).
> Per master synthesis §5.10 exclusion. Phase B: deprecate when
> `knowledge-base/` migration completes per MIGRATION.md.
```

#### D8.6.2 `/sweep-notion-bank` (.claude/skills/sweep-notion-bank.md, 110 lines)

Insert after frontmatter:

```markdown
> **Exclusion (per D7 + D8 §8.8.2).** This skill is NOT parameterised for
> `$WIKI_ROOT`. Rationale: one-shot Notion-import bound to specific date
> (2026-04-16) and specific Notion DB ID (bf0e9a11-0e6f-4717-9ae5-…).
> Re-running for v3 would require full rewrite (different DB, different
> sweep date), not parameterisation. Per master synthesis §5.10
> exclusion. If Ruslan later needs a v3 Notion sweep, escalate as
> `AWAITING-APPROVAL-sweep-notion-bank-v3-*.md`.
```

#### D8.6.3 `/compile` (.claude/skills/compile.md, 50 lines)

Insert after frontmatter:

```markdown
> **Exclusion (per D7 + D8 §8.8.3) — DEPRECATED.** This skill is NOT
> parameterised for `$WIKI_ROOT`. Rationale: zero `wiki/` references;
> targets `knowledge-base/{cluster}/_moc.md` and
> `knowledge-base/{cluster}/{topic}.md`. Legacy pre-v2 skill that
> synthesises raw → KB-article. Per Sub-agent D §7 transplant table:
> "drop (or rewrite); Targets legacy knowledge-base/; supplanted by
> `/ingest` + `/ask` in v2." Phase-A deprecation note added to
> `swarm/wiki/log.md`: `## [2026-04-XX] deprecate | /compile |
> superseded by /ingest + /ask per Sub-agent D §7 + D8 §8.6.3`.
> File retained for legacy knowledge-base/ use until MIGRATION.md
> finalises; NOT part of v3 wiki-skill set.
```

---

## D9 — `.claude/skills/README.md` (full file, verbatim)

**Source:** spec §9.2..§9.8. The spec does not contain a fully-prewritten
`.claude/skills/README.md` file — it specifies the rules that README
must encode. Orchestrator composes the README from the rules below,
verbatim from spec §9. This section reproduces the rules as the README's
body content.

```markdown
---
title: .claude/skills/ — Symlink Convention (v3)
type: readme
updated: 2026-04-23
---

# `.claude/skills/` — Symlink Convention

This directory hosts Claude Code skill entrypoints. In the v3 swarm wiki
architecture, active skills' canonical content lives under
`swarm/wiki/skills/active/<slug>.md` per Layer 8 (D1). The files here
are **symlinks** (for v3-born skills) pointing back to that canonical
location.

## Canonical symlink rule

    .claude/skills/<slug>.md  →  ../../swarm/wiki/skills/active/<slug>.md

**Relative path** (not absolute):
1. Roy-replication discipline (master synthesis §5.8.3): no hard-coded
   `/home/ruslan/*` paths.
2. Repo portability: relative target resolves correctly regardless of
   absolute repo root.

`<slug>` matches the `skill_slug` field per D2 §2.4 Layer 8 — one
canonical naming.

## Filename normalisation

The `skill_slug` MUST satisfy:

- Regex `^[a-z0-9-]{1,60}$` — body half of D2 §2.2 `id` regex
  (`^[a-z]+-[a-z0-9-]{1,60}$` where `[a-z]+-` is the type-prefix
  `skill-`).
- Unique across `.claude/skills/` (no collision with v2 names).
- Match the basename of `swarm/wiki/skills/active/<slug>.md` exactly.

Slug derivation:
- Single-word: lowercase as-is (`focus` → `focus`).
- Multi-word: hyphen-separated lowercase (`Build Graph` → `build-graph`).
- No spaces, underscores, uppercase, or extension inside the slug.

## Symlink creation hook (α-3 `learning → validated` transition)

Triggered by D11 activation predicate. Brigadier executes:

```bash
# Pre-flight
test -f swarm/wiki/skills/active/<slug>.md  || exit "no canonical"
test ! -e .claude/skills/<slug>.md          || exit "name collision; see Conflict handling"

# Create symlink (atomic)
ln -s ../../swarm/wiki/skills/active/<slug>.md .claude/skills/<slug>.md

# Verify
readlink .claude/skills/<slug>.md
test -f .claude/skills/<slug>.md  || exit "broken symlink"
```

Part of α-3 `active → validated` mover (D5 §5.4). Committed in the same
commit as the file move `learning/<slug>/manifest.md` → `active/<slug>.md`.

## Symlink removal hook (α-3 `validated → tombstoned` transition)

```bash
test -L .claude/skills/<slug>.md          || exit "not a symlink (or absent)"
rm .claude/skills/<slug>.md
mv swarm/wiki/skills/active/<slug>.md \
   swarm/wiki/_archive/skills/<slug>.md
```

Skill content file is **not deleted** (Sub-agent C §8 #9: never delete,
only archive). Symlink IS deleted (Claude Code registers skills via
`.claude/skills/`).

Per critic-gate1 S2 — α-3 has only 4 states (proposed/active/validated/
tombstoned). No separate `retired` removal path; graceful supersession
routes through tombstone with `supersedes:` edge from successor (D3 §3.2.7).

## Conflict handling — v2 skill collides with v3 promotion

When a v3 skill candidate's slug collides with a v2 file:

1. **Detect.** `test -e .claude/skills/<slug>.md` → collision.
2. **Preserve v2.** `mv .claude/skills/<slug>.md .claude/skills/<slug>_v2.md`.
   `_v2` suffix marks deprecated v2 skill retained for audit. `/lint`
   flags `_v2`-suffixed files as deprecated (informational only).
3. **Create v3 symlink.** Per §Symlink creation hook.
4. **Record migration in frontmatter** of `swarm/wiki/skills/active/<slug>.md`:

    migrated_from: .claude/skills/<slug>_v2.md
    migration_date: <YYYY-MM-DD>
    migration_note: <one-line summary of v2→v3 differences>

The 5 in-scope D8 skills (/ingest, /ask, /lint, /consolidate, /build-graph)
are NOT promoted via candidate→learning→active pipeline — they are v2
skills parameterised in place per D8 (remain regular files, not symlinks).
Only **new** v3-born skills go through D9 promotion.

## `/lint` broken-symlink detection

`/lint` (per D8 check #11) walks `.claude/skills/`:

    For each .md in .claude/skills/:
      if is_symlink:
        target := readlink
        if not file_exists(target):
          EMIT "broken symlink: .claude/skills/<slug>.md → <target>"
        if not target.startswith("../../swarm/wiki/skills/active/"):
          EMIT "symlink target outside active/"
        if not target.endswith("/<basename>"):
          EMIT "symlink basename mismatch"

Catches: (a) canonical removed without symlink removal; (b) symlink to
learning/ or _archive/; (c) canonical renamed without symlink update.

## Worked example — `query-pricing-models`

1. **proposed** (α-3). Compound-step writes
   `swarm/wiki/skills/candidates/query-pricing-models/manifest.md`.
   No symlink yet.
2. **active** (α-3 learning). Brigadier moves manifest to
   `swarm/wiki/skills/learning/query-pricing-models/manifest.md`,
   creates `golden-set.jsonl`. Usage logged to
   `swarm/wiki/skills/usage/query-pricing-models.jsonl`.
   No symlink yet.
3. **validated** (α-3). D11 predicate satisfied. Brigadier:
   - `mv swarm/wiki/skills/learning/query-pricing-models/manifest.md
        swarm/wiki/skills/active/query-pricing-models.md`
   - Pre-flight (no v2 collision).
   - `ln -s ../../swarm/wiki/skills/active/query-pricing-models.md
        .claude/skills/query-pricing-models.md`
   - Update `swarm/wiki/log.md`. Single commit.
4. **tombstoned** (α-3). Ratio drops <1:1. Brigadier:
   - `rm .claude/skills/query-pricing-models.md`
   - `mv swarm/wiki/skills/active/query-pricing-models.md
        swarm/wiki/_archive/skills/query-pricing-models.md`
   - Records `tombstoned_by:` in archived frontmatter.
   - Updates log.md.
```

---

## D10 — `swarm/wiki/meta/health.md` (full file, 8-section skeleton)

**Source:** spec §10.2 — the file content skeleton (lines 3705–3986) +
singleton frontmatter exemption (§10.2 prelude). Orchestrator writes
verbatim.

`````markdown
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

**Threshold for alert.** `< 0.80`. Below → Q1 4-tier retrieval may be
inadequate; re-evaluate at /ask FPAR or move to Phase B
(PPR/HyDE/embeddings).

**Structured log (append-only):**
```yaml
fpar_log:
  - {date: 2026-04-23, window: swarm-100, value: null, n: 0, alert: false}
```

## 2. Cycles

**Definition.** α-4 Cycle counts (D5 §5.5) across all states.

**Sources.**
- `closed_cycles_count` — frontmatter field above; incremented at α-4
  `closed` transition.
- Open / running / integrating / gated / compounded counts — derived
  from grep over `swarm/wiki/tasks/*/decisions/` for `alpha_state:`.

**Formula:**
```
closed_cycles_count = count(cycle-log.md files in swarm/logs/)
open_cycles = count(tasks with alpha_state ∈ {opened, running, integrating, gated, compounded})
cycle_close_rate_weekly = count(cycle-log.md created in last 7 days) / 7
```

**Q8 Layer-9 trigger #1.** `closed_cycles_count ≥ 50`; first of three
AND-conditions.

**Threshold for alert.** `open_cycles > 5` → brigadier write-queue
contention; evaluate CRDT switch.

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
`count(themes with ≥50 concepts each) ≥ 2`. Second of three AND-conditions.

**Tension T2 watch.** If `cross_theme_refs_count == 0` after 20 closed
cycles, re-evaluate Q8 signal #2.

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

**Per-layer thresholds for alert (Phase A):**

| Layer | Weekly threshold | What it means |
|---|---|---|
| spine entity-types | 5 | high contradiction noise; review /ask synthesis quality |
| L1 themes | 2 | book-distillation churn; review brigadier sweep quality |
| L4 meta/agent-improvements | 1 | cross-agent improvement instability |
| L5 tasks | 2 | task-quality issues |
| L7 global | 1 | promoted-rule churn; review compound step |
| L8 skills | 1 | pipeline leak; check D11 activation rubric |
| L9 insights | 0 (Phase A: any tombstone is a violation) | per Q8 phase_a_lock |

**Structured log:**
```yaml
tombstone_log:
  - {date: 2026-04-23, layer: null, count: 0, weekly_rate: 0.0}
```

## 5. Active-skills count and validation ratio

**Definition.** Count of files in `swarm/wiki/skills/active/`; for
each, the success/loss ratio derived from `usage/<slug>.jsonl`.

**Sources.** `swarm/wiki/skills/active/` glob; `swarm/wiki/skills/usage/<slug>.jsonl`.

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
< 1.0` over rolling 10 uses are flagged for retirement (route through
tombstone per α-3 + D11).

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
  page `created` timestamp; average over rolling 20.

**Formula:**
```
pending_drafts_count = count of swarm/wiki/drafts/*.md with state=drafted
                       AND no matching swarm/wiki/<canonical-path>/<slug>.md
review_latency_avg_min = mean(canonical.created - draft.created in minutes)
                         over the rolling 20 most recently-promoted drafts
```

**Threshold for alert.** `pending_drafts_count > 5` → brigadier
write-queue saturated.

**Structured log:**
```yaml
brigadier_load_log:
  - {date: 2026-04-23, pending: 0, latency_min: null}
```

## 8. Update mechanism

**Who updates:**
- `/lint` PostToolUse: updates `lint_findings_log` after every wiki write.
- `/lint` scheduled (weekly Q5 #5): updates `cycles_log`, `cross_theme_log`,
  `tombstone_log`, `active_skills_log`, `brigadier_load_log`.
- `meta-agent` weekly review (W-5): composes 5-line weekly summary
  appended below; verifies counter consistency; flags drift.
- `brigadier` updates live counters in frontmatter
  (`closed_cycles_count`, `active_skills_count`, etc.) at relevant
  α-2/α-3/α-4 transitions.

**Cadence:**
- Live counters (frontmatter): per α-state transition (event-driven).
- Structured logs: appended weekly (or per-event for `lint_findings_log`).
- Weekly summary: meta-agent composes Mondays UTC.

**Append-only discipline.** Per CLAUDE.md / `.claude/rules/global.md`:
"Логи — append-only, новые записи сверху." Rotation: when a `_log:`
exceeds 30 entries, oldest 20 moved to
`swarm/wiki/_archive/health-history-<YYYY>.md`.

## Weekly summary (append-only, meta-agent composes)

(Empty until first weekly review.)
`````

---

## End of extraction

All 10 deliverables extracted. Orchestrator consumes this file by
reading each section and writing the fenced-block contents to the named
paths per D1 bootstrap list.
