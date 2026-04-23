---
title: Wiki v3 Стадия C — Architecture Spec Execution Prompt
date: 2026-04-23
status: ready-for-launch
target_executor: Claude Code on server (Opus 4.7, 1M context, extended thinking max)
launch_branch: claude/jolly-margulis-915d34
estimated_duration: 3-6 hours
output: design/AWAITING-APPROVAL-wiki-v3-architecture-2026-04-XX.md
upstream:
  - decisions/WIKI-V3-MECHANICS-2026-04-23.md  (authoritative input — Q1..Q9 resolved)
  - design/ROY-WIKI-V3-GOALS-2026-04-23.md     (W-1..W-12 locked)
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md  (Part 4 alphas, Part 10)
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md  (§5.5 wiki baseline)
written_by: Claude Code on server (this prompt-writing pass)
prompt_pattern: stylistic kin to prompts/step-2-1-master-synthesis-2026-04-22.md
---

# WIKI v3 СТАДИЯ C — ARCHITECTURE SPEC

> **⚠️ READ THIS FIRST — CRITICAL FRAMING**
>
> You are about to write **the architectural backbone of the Jetix swarm's
> long-term memory.** Every domain expert (5 of them) will read from and
> write to `swarm/wiki/` for the lifetime of Jetix. Every coordination
> protocol routes through provenance written here. Every recursive
> self-improvement cycle (Phase B) compounds on the structure you specify
> in this document. Every retrieval, every cross-reference, every
> stale-fact tombstone, every skill that gets activated/retired — they all
> obey the rules you write down now.
>
> If the directory layout is sloppy, every page will be misfiled for years.
> If the edge enum is wrong, multi-hop retrieval will return garbage.
> If the alpha state machines drift from FPF Part 4, the swarm will execute
> tasks that no one can verify. If the shared-protocols write gate is
> hand-wavy, the brigadier will silently corrupt foundations. If the skill
> learning pipeline lacks owners, validated skills will rot in `learning/`
> while broken ones reach `active/`.
>
> **You are not writing a spec; you are writing the constitution of
> compounded memory.** Treat every deliverable as concrete contract, not
> commentary. Templates with exact field lists. State machines with exact
> transitions and movers. Rubrics with exact predicates. Skill diffs with
> exact line ranges. Depth over speed. Specificity over flexibility.
> Mechanics over rhetoric.

---

## 1. MISSION

Produce `design/AWAITING-APPROVAL-wiki-v3-architecture-<today>.md` — a
**concrete, 8,000–14,000 word architecture specification** that materialises
all 12 mandated deliverables of Стадия C, such that Стадия D (operational
buildout) can create every directory, template, edge type, alpha state
machine, shared protocol, parameterization config, skill diff, and health
skeleton **directly from the spec without re-research, re-decision, or
re-interpretation.**

The deliverable lands as `AWAITING-APPROVAL-*.md` because Ruslan must
approve before Стадия D files are written into the repo.

This document has three downstream consumers:

1. **Стадия D builders** — humans + Claude Code creating `swarm/wiki/`,
   `swarm/lib/`, `.claude/config/`, and modifying `.claude/skills/*` from
   this spec verbatim.
2. **Domain experts at runtime** — the 5 expert agents that read
   `swarm/wiki/foundations/swarm-alphas.md` and `swarm/lib/shared-protocols.md`
   on every Task invocation as ground truth.
3. **Phase B self-improvement** — when the swarm rewrites its own structure
   after consuming the 393-book Private Library, this document is the
   versioned baseline it diffs against.

---

## 2. WHAT YOU ARE NOT DOING

To prevent scope drift, be brutally clear:

- **You are not re-opening the 12 W-decisions** from `ROY-WIKI-V3-GOALS`.
  They are locked. Cite, don't re-debate.
- **You are not re-opening the 9 Q-resolutions or 8 R-items** from
  `WIKI-V3-MECHANICS`. They are approved. Cite, don't re-debate.
- **You are not re-opening the 5 swarm-alphas** (Task / Artefact /
  Strategies-Rule / Cycle / Direction) from `FPF-ENHANCEMENT` Part 4.
  Their identity, scope, and high-level purpose are fixed. You only
  materialise their **state graphs + transitions + movers + acceptance
  predicates** as Deliverable 5.
- **You are not re-opening §5.5 of master synthesis** (wiki write protocol
  baseline). You extend it for v3 specifics in Deliverable 6.
- **You are not re-opening the 24 Locks** from TENSIONS-RESOLVED files.
  Compatibility-check, don't re-derive.
- **You are not implementing.** No file in `swarm/wiki/` or `swarm/lib/`
  is created in this pass. You write the spec; Стадия D builds.
- **You are not reading the 393 books in `raw/books-md/`.** They are
  Phase B fuel, fully out of scope.
- **You are not running web searches.** All inputs are local; the corpus
  is already curated in Tier 1 / Tier 2.

If you find yourself wanting to re-debate any locked item, stop. Cite the
locking document and proceed.

---

## 3. INPUTS — PRECISE READING ORDER (ENFORCED VIA SUB-AGENTS)

### Tier 1 — PRIMARY (deep read, every word matters)

These define the constraints, vision, mechanics, and base protocol that the
architecture spec must materialise. **No deliverable may contradict any
Tier 1 source.**

```
decisions/WIKI-V3-MECHANICS-2026-04-23.md          (Q1..Q9 + R1..R8 — authoritative)
design/ROY-WIKI-V3-GOALS-2026-04-23.md             (W-1..W-12 locked)
decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md  (Part 4 alphas, Part 10 protocols)
design/ROY-BUILD-LOGIC-2026-04-23.md               (build sequencing constraints)
decisions/ROY-ALIGNMENT-2026-04-22.md              (matrix 5×4 pattern)
decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md  (§5.5 wiki protocol baseline)
```

### Tier 2 — RESEARCH GROUNDING (consult for any residual ambiguity in deliverables)

Use only to fill gaps; do not re-derive Q-resolutions from these.

```
raw/research/knowledge-architecture-deep-research-2026-04-19.md  (Parts A–F, H)
raw/articles/karpathy-llm-wiki-gist-2026-04.md
raw/research/step-2-2-3b-extractions/W-1-knowledge-architecture.md
raw/research/step-2-2-3b-extractions/W-2-locked-constraints.md
raw/research/step-2-2-3b-extractions/W-3-existing-wiki-audit.md
```

### Tier 3 — EXISTING INFRASTRUCTURE (audit for transplant + diff)

These are the v2 assets you must transplant or modify. **Read concretely:
field names, line counts, current behaviour. Your skill-edit diffs
(Deliverable 8) will reference exact lines.**

```
wiki/_templates/source.md
wiki/_templates/concept.md
wiki/_templates/entity.md
wiki/_templates/claim.md
wiki/_templates/idea.md
wiki/_templates/topic.md
wiki/_templates/experiment.md
wiki/_templates/summary.md
wiki/_templates/foundation.md
wiki/graph/edges.jsonl              (current edge type vocabulary, ~572 edges)
wiki/overview.md
wiki/index.md                       (current TOC mechanism)
wiki/log.md                         (append-only chronology pattern)
.claude/skills/ingest.md
.claude/skills/ask.md
.claude/skills/lint.md
.claude/skills/compile.md
.claude/skills/consolidate.md
.claude/skills/build-graph.md
.claude/skills/search-kb.md
.claude/skills/sweep-notion-bank.md
CLAUDE.md                            (Wiki Architecture v2 section, line counts)
.claude/rules/global.md
```

### Tier 4 — DO NOT READ (out of scope)

- `raw/books-md/` (393 books — Phase B fuel; do not open even if tempted)
- External web (no `WebSearch`, no `WebFetch`)
- Voice memos, Notion exports, business-strategy docs
- Architecture variants V1–V5 (legacy 12-agent pattern, disproven)
- Anything not enumerated in Tier 1/2/3

If a sub-agent asks to read Tier 4, refuse. If a deliverable seems to
require Tier 4 input, you are over-scoping — re-read the deliverable's
mandate in Section 6.

---

## 4. SUB-AGENT STRATEGY (MANDATORY — DO NOT WORK MONOLITHICALLY)

You have ~150K-200K words of Tier 1 + Tier 2 + Tier 3 content to absorb.
Working sequentially will exhaust context. **You MUST parallelise via the
Task tool, then integrate.**

### Phase 1 — Parallel deep reads (single message, 5 concurrent Task calls)

Spawn five sub-agents in **one batched message** with multiple Task tool
uses. Each returns a structured ≤2,500-word extraction.

#### Sub-agent A — Mechanics + Goals + Build-Logic Anchor

**Brief:** Read `decisions/WIKI-V3-MECHANICS-2026-04-23.md` (Parts 1, 2,
3, 4, 5 fully), `design/ROY-WIKI-V3-GOALS-2026-04-23.md` (W-1..W-12 + §2
+ §5), `design/ROY-BUILD-LOGIC-2026-04-23.md` (§1.2, §1.3, §2.1–§2.3, §3,
§4.2, §4.4). Extract:

- For each of Q1..Q9: the **Recommended answer**, **Applicability
  constraint**, and any **new variants found** — phrased as direct
  acceptance criteria for the architecture spec.
- For each of W-1..W-12: the locked constraint as a single sentence
  ("the spec MUST..."), with citation to the W-item.
- For each of R1..R8: the accepted-default position (all = Yes per
  Ruslan 2026-04-23) phrased as a precondition.
- For each of T1..T5 (Part 3 tensions): the resolution-shape that the
  spec must honour.
- Build-logic phasing: what must be Phase A vs deferrable to Phase B.

**Output file:** `raw/research/step-2-2-3c-extractions/A-mechanics-goals-buildlogic.md`.

#### Sub-agent B — FPF-Enhancement Alphas + Protocols

**Brief:** Read `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`
Part 4 (α-1..α-5 swarm-alphas in full) and Part 10 (§10.4–§10.8
preparatory specifications: shared-protocols.md, mode: writing-support,
tool-language abstractions, tool permission self-check, HITL escalation).
Extract:

- For each of 5 alphas: identity (who it represents), scope (what entity),
  proposed state names, proposed transitions, proposed movers per
  transition, acceptance predicates per state, integration points with
  other alphas, references to FPF-canonical alphas where relevant.
- For each Part 10 section: the verbatim mandate that must appear in
  Deliverable 6 (`swarm/lib/shared-protocols.md`), with citation.
- Specifically the **§5.5.5 provenance gate** mechanics: what counts as
  provenance, what the gate rejects, what the brigadier must verify.
- Specifically the **structured output schema**: what fields a Task
  return must carry.
- Specifically the **HITL escalation rules**: when to bounce to Ruslan,
  what the AWAITING-APPROVAL packet must contain.
- Specifically the **tool permission self-check** ritual.

**Output file:** `raw/research/step-2-2-3c-extractions/B-fpf-alphas-protocols.md`.

#### Sub-agent C — Knowledge-Architecture + Karpathy Patterns

**Brief:** Read `raw/research/knowledge-architecture-deep-research-2026-04-19.md`
(Parts A.1, A.3, A.6; B.1–B.5; C.1, C.3, C.4; D.1, D.3; E.1, E.2, E.3;
F.1, F.2, F.4; G.3, G.5; H.1, H.3, H.4, H.5, H.7, H.8; Anti-patterns
3, 6, 7, 8, 10) and `raw/articles/karpathy-llm-wiki-gist-2026-04.md` in
full. Extract:

- Retrieval-stack patterns relevant to the 4-tier Q1 answer (path
  lookup → index+grep → typed-BFS → long-context fallback): what
  configuration each tier needs to have at filesystem level.
- Cross-reference mechanics: triple-channel (YAML + inline wikilinks +
  edges.jsonl) implementation details — what each channel stores, when
  each is consulted, who writes each.
- Edge-type vocabulary precedents from research (the 9 intra + part_of +
  3 cross-layer = 12 enum). What definition / cardinality / inverse /
  example pattern best practices look like.
- Staleness mechanics (5-signal /lint orchestration): what signals look
  like at the data level — which fields, which thresholds, which
  observable changes.
- Skill-learning pipeline mechanics (golden-set ≥3, ≥3:1 ratio, ≥10
  uses) at the directory + file-naming level.
- Health metrics (FPAR, cycles, tombstone rate, cross-theme refs):
  exact computation formulas where research supports them.

**Output file:** `raw/research/step-2-2-3c-extractions/C-knowledge-arch-karpathy.md`.

#### Sub-agent D — Existing v2 Infrastructure Audit

**Brief:** Read every file in `wiki/_templates/` (9 templates), the first
50 lines of `wiki/graph/edges.jsonl` plus tail (to capture vocabulary +
volume), `wiki/overview.md`, `wiki/index.md` structure, `wiki/log.md`
structure, and **every skill spec line-by-line**:
`.claude/skills/{ingest,ask,lint,compile,consolidate,build-graph,search-kb,sweep-notion-bank}.md`.
For each, extract:

- For each v2 template: exact frontmatter fields (key + type + required/
  optional + default), body section list, lint constraints. This becomes
  the transplant baseline for Deliverable 4.
- For `edges.jsonl`: the live edge-type vocabulary actually used (count
  per type), so Deliverable 3's enum is grounded in current usage and
  documents which types are *new*.
- For each skill: total line count, the path-resolution pattern (where
  it currently hard-codes `wiki/`), the read/write surfaces, and the
  exact line ranges that would change if `$WIKI_ROOT` were parameterised.
  This grounds the ~85-line edit budget in Deliverable 8.
- Index/log conventions worth preserving.
- Anything in v2 that should NOT be transplanted (deadweight, deprecated
  fields).

**Output file:** `raw/research/step-2-2-3c-extractions/D-v2-infrastructure-audit.md`.

#### Sub-agent E — Master Synthesis §5.5–§5.10 Baseline + Matrix Compliance

**Brief:** Read `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
sections §5.5 (wiki protocol baseline incl. §5.5.1–§5.5.5), §5.6.2,
§5.7 (Max-subscription + cost), §5.10 (skills inventory), and
`decisions/ROY-ALIGNMENT-2026-04-22.md` in full (matrix 5×4 pattern). Extract:

- §5.5.1–§5.5.5 verbatim: the existing wiki write protocol that
  Deliverable 6 (`shared-protocols.md`) must extend, not replace.
  Specifically §5.5.5 provenance gate as the seed for v3's gate.
- §5.7 Max-subscription discipline: what every tool invocation in the
  spec must respect (no `ANTHROPIC_API_KEY`, no paid embeddings).
- §5.10 skills list: the 6 skills targeted for `$WIKI_ROOT` parameterisation
  (and which 2 are out — search-kb and sweep-notion-bank — verify).
- Matrix 5×4 implication: how the 5 domain experts × 4 role-modes pattern
  intersects with wiki write rights (single-writer brigadier per Q2;
  experts return via Task draft per §5.5.5).

**Output file:** `raw/research/step-2-2-3c-extractions/E-master-synthesis-matrix.md`.

### Sub-agent operational rules

- All 5 sub-agents must run **concurrently** in a single message. Do not
  serialise.
- Each must respect tier discipline: no Tier 4. If a sub-agent surfaces a
  request to read a book, refuse and re-brief.
- Each returns a **structured extraction file** (frontmatter + sections),
  committed to `raw/research/step-2-2-3c-extractions/` after Phase 1.
- Commit the 5 extractions as one commit:
  `[step-2-2-3c] 5 parallel extractions for wiki v3 architecture spec`.

### Phase 2 — Integration & drafting

After all 5 extractions return, you (orchestrator) integrate them into the
12 deliverables in the order specified in Section 6. Spawn targeted
follow-up sub-agents only if a deliverable surfaces a concrete gap (e.g.
"need exact field for stale-detection signal #3"). Do not spawn
follow-ups for stylistic polish.

### Phase 3 — Adversarial critic (mandatory pre-gate)

Before Gate 1 and again before Gate 2, spawn a critic sub-agent with this
adversarial brief:

> Read the draft spec. Adopt the role of a senior engineer who must
> implement Стадия D from this spec next week. Find every place where:
> (a) a deliverable is hand-wavy — "the system will support" instead of
>     "the system supports X by reading field Y from file Z";
> (b) a state machine has implicit transitions or undefined movers;
> (c) a rubric has predicates not testable from filesystem state alone;
> (d) an edge type lacks an inverse, a cardinality, or an example;
> (e) a frontmatter field is missing type, required/optional flag, or
>     default value;
> (f) a skill diff lacks exact line ranges or before/after snippets;
> (g) any locked decision (W-1..W-12, Q1..Q9, R1..R8, T1..T5, 24 Locks)
>     is contradicted, ignored, or silently re-opened;
> (h) the Max-subscription discipline is violated;
> (i) the spec depends on Tier 4 input it shouldn't have read;
> (j) a deliverable is missing entirely or merged unmarked into another.
>
> Return: 0 showstoppers / N high / N medium / N low. For each, cite
> exact line + minimal-fix suggestion. Be merciless.

Showstoppers + high findings MUST be fixed before the gate. Important
medium findings should be fixed. Low findings logged in spec appendix.

Commit the critic report to `raw/research/step-2-2-3c-extractions/critic-gate{1,2}.md`
before applying fixes.

---

## 5. STAGE-GATED 2-GATE PROTOCOL

You operate in **Stage-Gated mode**. Do not push past either gate without
Ruslan approval. Both gates land as `AWAITING-APPROVAL-*.md` files
committed and pushed to `claude/jolly-margulis-915d34`.

### Gate 1 — Structural core (Deliverables 1–6)

After Deliverables 1, 2, 3, 4, 5, 6 are drafted and adversarial-critic'd:

- Commit as `design/AWAITING-APPROVAL-wiki-v3-architecture-gate1-<today>.md`.
- Push immediately.
- **Pause.** Do not proceed to Deliverable 7 until Ruslan approves.
- If Ruslan flags inline changes, apply, re-commit (`AWAITING-APPROVAL-wiki-v3-architecture-gate1-rev1-<today>.md`),
  re-push, re-pause.

Gate 1 covers: directory layout, per-layer frontmatter templates, edge
enum, entity templates, swarm-alphas state machines, shared-protocols.
This is the **structural skeleton** — getting it right matters more than
speed. Approve before binding the parameterization + skill diffs to it.

### Gate 2 — Operational integration (Deliverables 7–12)

After Deliverables 7, 8, 9, 10, 11, 12 are drafted and adversarial-critic'd:

- Commit as `design/AWAITING-APPROVAL-wiki-v3-architecture-gate2-<today>.md`.
- Push immediately.
- **Pause.** Do not consolidate until Ruslan approves.

Gate 2 covers: parameterization config, skill edit diffs, symlink
convention, health.md skeleton, Q6 rubric, T5 strategies trio collapse.
This is the **integration surface** — touching live skills + live
filesystem semantics.

### Final consolidation (after both gates approved)

After both gates approved (inline or via separate ack):

- Consolidate into `design/AWAITING-APPROVAL-wiki-v3-architecture-<today>.md`
  containing all 12 deliverables in final form (Gate 1 + Gate 2 unified).
- Commit: `[design] AWAITING-APPROVAL wiki v3 architecture (Стадия C complete)`.
- Push.
- Halt. Stop without launching Стадия D.

### Commit cadence between gates

- Commit after each deliverable draft (small commits over big ones).
- Commit each adversarial-critic report separately.
- Push after every commit (Ruslan monitors via GitHub).
- Use commit message format `[step-2-2-3c] <action>: <subject>`.

### If stuck mid-gate

- If a sub-agent extraction is shallow → spawn replacement with tighter brief.
- If two locked decisions appear to conflict → cite both, propose
  reconciliation as new `AWAITING-APPROVAL-conflict-<id>.md`, do not
  resolve unilaterally.
- If Ruslan unresponsive after 12h on a gate → pause; do not work past it.
  Continue ONLY on non-blocking polish (e.g. critic-report formatting)
  until ack lands.

---

## 6. THE 12 DELIVERABLES — MANDATORY OUTPUT SECTIONS

Each deliverable below is a section in the architecture spec. **All 12 are
mandatory.** Each must meet the depth and concreteness criteria attached.
Cite the locking source(s) where applicable.

### Deliverable 1 — `swarm/wiki/` Directory Layout (across all 9 layers)

**Mandate:** Specify the full directory tree of `swarm/wiki/`, mapping
each of the 9 layers (per FPF Part 4 + WIKI-V3-MECHANICS Part 5) to
concrete directory paths. For each directory:

- **Path** — exact relative path from repo root (e.g.
  `swarm/wiki/foundations/`).
- **Layer #** — which of the 9 layers it belongs to.
- **Owner** — who writes (brigadier? expert? meta-agent? Ruslan?).
- **Permission** — read-only / brigadier-write / expert-via-Task.
- **Naming convention** — file name pattern (e.g.
  `<slug>.md`, `iter-vN.md`, `agent-improvements/<expert>-<date>.md`).
- **Cardinality** — single file? per-entity? per-cycle? per-skill?
- **Initial-state contents** — what files exist at Стадия D bootstrap
  (e.g. README, swarm-alphas.md, edge-types.md placeholder).

The 9 layers per the locked decisions cover at minimum:
foundations / concepts / entities / sources / topics / claims / experiments
/ summaries / ideas / meta / insights (Layer 9 placeholder per Q8) — verify
exact set against Tier-1 sources via Sub-agent A's extraction.

**Concreteness bar:** A new agent must be able to read this section and
produce `tree swarm/wiki/` output that matches exactly.

**Format:** ASCII tree + supporting per-directory table.

---

### Deliverable 2 — Per-Layer Frontmatter Template

**Mandate:** For each of the 9 layers (and any sub-tree with distinct
semantics like `meta/agent-improvements/`), specify the **required
frontmatter fields** every page in that layer must carry. For each field:

- **Field name** (snake_case).
- **Type** (string / list / enum / iso-date / int / bool / yaml-block).
- **Required vs optional** (with default for optional).
- **Validation rule** — what `/lint` checks (e.g. `confidence` ∈ [0,1],
  `superseded_by` is a valid wikilink).
- **Source** — which W-item, Q-resolution, or v2-template field it derives
  from.
- **Lifecycle integration** — which alpha state(s) reference this field.

Required cross-layer fields (always present):
`id`, `title`, `layer`, `created`, `last_modified`, `provenance` (sources[]
+ inline-cite map), `state` (one of α-2 Artefact states),
`confidence` (with method), `niche` (for cross-niche traversal),
`related[]`, `topics[]`, `pipeline` (carrying v2 convention forward).

Layer-specific additions (illustrative; verify exact set):
- `foundations/`: `binding_scope`, `supersedes_versions[]`.
- `concepts/`: `definition`, `examples[]`, `extends`.
- `entities/`: `entity_type`, `external_ids` (Notion ID, etc.).
- `sources/`: `source_type`, `url` or `local_path`, `ingested_date`,
  `coverage` (which topics/concepts it grounds).
- `topics/`: `MOC_for[]`.
- `claims/`: `support_count`, `contradiction_count`, `last_review_date`,
  `support_edges[]`, `contradiction_edges[]`.
- `experiments/`: `hypothesis`, `start_date`, `end_date`,
  `outcome` (open/won/lost), `cycle_id`.
- `summaries/`: `summary_window`, `community_id`.
- `ideas/`: `proposed_by`, `routing_target`.
- `meta/agent-improvements/`: `expert`, `improvement_target`,
  `validation_status` (per α-3 Strategies-Rule).

**Concreteness bar:** A page can be lint-validated by walking the
frontmatter against the per-layer schema.

**Format:** One subsection per layer + a master cross-layer table.

---

### Deliverable 3 — `swarm/wiki/_templates/edge-types.md` (12-type Edge Enum)

**Mandate:** Define the 12-type edge enum exactly:
**9 intra-layer types + `part_of` + 3 cross-layer types.**

For each edge type, specify:

- **Name** (snake_case, e.g. `supports`, `extends`, `contradicts`,
  `derived_from`, `superseded_by`, `references`, `examples_of`,
  `related_to`, `tombstoned_by` — verify exact set against Sub-agent C
  + D extractions and edges.jsonl current usage).
- **Definition** (1–2 sentences).
- **Cardinality** (1:1 / 1:N / N:M).
- **Directionality** (directed / bidirectional).
- **Inverse** (the opposite-direction edge type, or none).
- **Allowed source layers** (which layers can be on the `from` side).
- **Allowed target layers** (which layers can be on the `to` side).
- **Example** (concrete `{from: ..., to: ..., type: ..., metadata: {...}}`
  edge JSON record, drawn from a plausible swarm/wiki page).
- **Cross-layer flag** (yes/no — and for the 3 cross-layer types,
  precise allowed (source-layer, target-layer) pairs).
- **Lint rule** — when `/lint` would flag misuse (e.g. `superseded_by`
  must form a DAG; cycles are an error).

The `cross-tree-ref` edge (v2↔v3 bridge per Q9) is one of the 3
cross-layer types — specify it explicitly.

**Concreteness bar:** Every edge currently in `wiki/graph/edges.jsonl`
either maps to a type in this enum or is flagged for migration.

**Format:** Per-type subsection + master matrix table (rows = from-layer,
cols = to-layer, cells = allowed edge types).

---

### Deliverable 4 — Per-Entity-Type Templates (`swarm/wiki/_templates/<entity>.md`)

**Mandate:** For each of the 9 v2 entity types (concept / entity / source
/ claim / idea / topic / experiment / summary / foundation), produce the
v3 template by **transplanting the v2 template + adding layer-specific
fields from Deliverable 2 + adding alpha state field from Deliverable 5**.

For each template, write the actual file content as a fenced block:

```markdown
---
<frontmatter with all required fields, with default values or angle-bracket
 placeholders>
---

# <Title>

## <Section 1>

<placeholder body, mirrors v2 conventions where applicable>

## <Section 2>
...

## Provenance

<inline-citation map, per §5.5.5>

## Edges

<wikilink list mirrored to edges.jsonl, per Q3 triple-channel rule>
```

**Diff explicitly** what is new in v3 vs v2 (added fields, removed fields,
moved sections). Cite Sub-agent D's audit for v2 baseline.

**Concreteness bar:** Стадия D can `cp` each fenced block into
`swarm/wiki/_templates/<type>.md` without modification.

**Format:** One subsection per entity type, each containing the full
template file content + a v2→v3 diff table.

---

### Deliverable 5 — `swarm/wiki/foundations/swarm-alphas.md` (5 swarm-alphas)

**Mandate:** Materialise all 5 swarm-alphas from FPF-ENHANCEMENT Part 4
(α-1 Task / α-2 Artefact / α-3 Strategies-Rule / α-4 Cycle / α-5 Direction)
as **state machines with state graphs + transitions + movers + acceptance
predicates per state**.

For each alpha, write:

- **Identity** (1 paragraph) — what entity it tracks, why it exists,
  citation to FPF Part 4.
- **State graph** — exhaustive list of states with concise definition.
  For α-2 Artefact, include at minimum: `draft / proposed / accepted /
  superseded / retired / tombstoned`. For α-3 Strategies-Rule, include:
  `candidate / learning / active / retired / tombstoned`. For α-1 Task,
  include: `proposed / planning / in-progress / blocked / awaiting-review
  / done / abandoned`. For α-4 Cycle, include: `open / mid-cycle /
  closing / closed`. For α-5 Direction, include the FPF-canonical states.
  **Exact state names must be verified against Sub-agent B's extraction.**
- **Transitions table** — rows: (from-state, to-state, trigger condition,
  mover/role-with-write-rights, side-effects on filesystem).
- **Acceptance predicates per state** — what the entity must satisfy to
  be in that state (testable from filesystem alone where possible). E.g.
  for α-2 `accepted`: provenance gate passed, ≥1 supporting edge,
  brigadier signed off in commit metadata.
- **Cross-alpha integrations** — how this alpha references other alphas
  (e.g. α-3 active state moves driven by α-4 Cycle close events).
- **State diagram (ASCII)** — visualise the state graph.

**Concreteness bar:** Reading this section, an engineer can write a
state-machine validator that asserts the swarm's filesystem matches
the legal state set + transitions.

**Format:** One subsection per alpha, each with identity / state graph /
transitions table / acceptance predicates / cross-alpha integrations /
ASCII diagram.

---

### Deliverable 6 — `swarm/lib/shared-protocols.md` (Wiki Write Protocol + ancillaries)

**Mandate:** Write the complete content of `swarm/lib/shared-protocols.md`
extending §5.5 of master synthesis (specifically §5.5.5 provenance gate)
for v3 specifics, **and** including all FPF Part 10.4–10.8 mandates.
Sections required:

1. **Wiki write protocol (extends §5.5).**
   - Single-writer brigadier rule (per Q2): only the brigadier commits to
     `swarm/wiki/`. Experts return drafts via Task.
   - Per-layer write paths and the agents permitted to draft for each.
   - Pre-write checklist (reads required, edges-update required).
   - Commit message format for wiki writes.
2. **§5.5.5 provenance gate (v3 enforcement).**
   - What counts as provenance (sources[] non-empty, ≥1 inline `[src:…]`
     citation per non-trivial paragraph, traceable to a Tier-1 file or
     Layer 3 source in the wiki).
   - What the gate rejects (claim without source, source whose
     `pipeline:` is `raw`, claim contradicting an `accepted` foundation
     without a `contradicts` edge).
   - Brigadier verification ritual before `git add` of any Layer 1–8 page.
3. **Structured output schema** (Task return contract).
   - Required fields: `summary`, `proposed_writes[]` (each: `path`,
     `frontmatter_diff`, `body_diff`, `edges_to_add[]`), `provenance[]`,
     `confidence`, `escalations[]`.
   - JSON / markdown schema.
4. **HITL escalation rules.**
   - When to escalate (foundation revision, Layer 9 activation request,
     contradiction without resolution, budget overrun, > N retries).
   - AWAITING-APPROVAL packet contents (context / options / recommendation
     / risk / proposed file path).
   - Escalation file path convention.
5. **Tool permission self-check.**
   - Before invoking any tool, the agent verifies it has permission per
     its role (brigadier vs expert vs meta-agent).
   - Self-check ritual (1-line check at function entry).
   - Behaviour on permission deny.
6. **`mode: writing-support` clause.**
   - When a Task is invoked with `mode: writing-support`, the sub-agent
     produces drafts only — does not write to the wiki directly.
   - Output schema strictly the structured-output schema (item 3).
7. **Tool-language abstractions.**
   - Naming conventions for invoking sub-tools (per FPF §10.8).
   - Verb dictionary (e.g. `draft`, `verify`, `tombstone`, `cycle-close`).
8. **Max-subscription discipline.**
   - `unset ANTHROPIC_API_KEY` enforced at session start.
   - No paid embeddings, no third-party API.
   - Consumes Claude Code Max plan only.

**Concreteness bar:** This file becomes the runtime contract every domain
expert reads on every Task invocation. No ambiguity tolerated.

**Format:** Numbered sections matching the 8 items above.

---

### Deliverable 7 — `.claude/config/wiki-roots.yaml` (Parameterization Config)

**Mandate:** Specify the full content of `.claude/config/wiki-roots.yaml`,
implementing the Q9 coexist+parameterize decision.

Required keys:

```yaml
# .claude/config/wiki-roots.yaml
wiki_root_v2: wiki
wiki_root_v3: swarm/wiki
default_root: wiki_root_v3        # what new agents target unless overridden
bridge_edge_type: cross-tree-ref  # per Q9, edges spanning v2↔v3
v2_status: read-write              # untouched, still ingested into
v3_status: read-write              # primary going forward
migration_phase: A                 # decision deferred per WIKI-V3-MECHANICS
```

For each key: type, allowed values, behaviour at load time, what skills
read it. Specify the **`$WIKI_ROOT` resolution algorithm** that the 6
parameterised skills will run at startup (env var > config file >
hardcoded default).

**Concreteness bar:** Стадия D writes this file unchanged.

**Format:** Full YAML file as fenced block + per-key annotation table +
resolution-algorithm pseudo-code.

---

### Deliverable 8 — Skill Edit Diffs (6 Skills × ~85 line edits total)

**Mandate:** For each of the 6 skills targeted (`/ingest`, `/ask`,
`/lint`, `/compile`, `/consolidate`, `/build-graph`), produce a
**concrete edit diff** that implements `$WIKI_ROOT` parameterization per
Deliverable 7.

For each skill:

- **Current line count** (from Sub-agent D's audit).
- **Edit budget** (≈ 85 lines spread across 6; budget per skill).
- **Per-edit specification** (table or unified-diff style):
  - Line range (e.g. lines 12–14).
  - Before snippet.
  - After snippet.
  - Rationale (what `$WIKI_ROOT` use this enables).
- **Behaviour after edit** (1 sentence).
- **Test plan** (1 line — how to verify the skill resolves both v2 and
  v3 roots correctly post-edit).

Skills out of scope (verify against Sub-agent E extraction): `/search-kb`
(per master synthesis §5.10) and `/sweep-notion-bank` (Notion-only,
not wiki-bound). Document why.

**Concreteness bar:** Стадия D can apply each diff with `git apply` or
manual edit using the specified line ranges.

**Format:** Per-skill subsection with diff table + rationale + test plan.

---

### Deliverable 9 — `.claude/skills/` Symlink Convention for v3 `active/<slug>.md`

**Mandate:** Per Q6 skill-learning pipeline, when a skill candidate is
promoted from `swarm/wiki/skills/learning/` to `swarm/wiki/skills/active/`,
it must become live in `.claude/skills/`. Specify the convention:

- **Symlink rule:** `.claude/skills/<slug>.md → ../../swarm/wiki/skills/active/<slug>.md`
  (or absolute path; choose one and justify).
- **Filename normalisation** (slug rules — kebab-case, no spaces).
- **Symlink creation step** in the `learning → active` transition (per
  α-3 mover for that transition; cross-reference Deliverable 5).
- **Symlink removal step** in the `active → retired` and
  `active → tombstoned` transitions (per α-3 movers).
- **Conflict handling** when a v2 skill (`.claude/skills/<slug>.md`
  exists as regular file) collides with v3 promotion: the v2 file is
  preserved with a `_v2` suffix; the symlink takes precedence; document
  the migration note appended to v3 `active/<slug>.md`.
- **Audit signal:** how `/lint` detects broken symlinks or symlinks
  pointing to non-`active` files.

**Concreteness bar:** A skill promotion can be scripted from this section.

**Format:** Subsection with rules + worked example (one full
candidate→learning→active→retired symlink lifecycle).

---

### Deliverable 10 — `swarm/wiki/meta/health.md` Skeleton

**Mandate:** Specify the initial content of `swarm/wiki/meta/health.md`
as the swarm's self-monitoring dashboard. Required sections:

1. **FPAR (First-Pass Acceptance Rate)**
   - Definition: fraction of Task returns accepted by brigadier on first
     try (no rework) over a rolling window.
   - Window: rolling 20 invocations per agent, rolling 100 swarm-wide.
   - Computation source: Task invocation logs (per FPF Part 10.x).
   - Threshold for alert: <80% (per Q1 applicability constraint).
2. **Cycles**
   - Open cycles count + ages (per α-4 Cycle states).
   - Closed-cycle rate (per week).
   - Threshold for Q8 Layer 9 activation: ≥50 closed α-4 cycles.
3. **Cross-theme refs**
   - Count of `cross-tree-ref` and other cross-layer edges spanning
     niches.
   - Threshold for Q8 Layer 9 activation: ≥3 inter-theme refs across ≥2
     theme-wikis with ≥50 concepts each.
4. **Tombstone rate**
   - Tombstoned-page count per layer per week.
   - Per-layer thresholds (high tombstone in `claims/` may indicate
     contradiction noise; high in `skills/active/` indicates pipeline
     leak).
5. **Active-skills count**
   - Count of files in `swarm/wiki/skills/active/`.
   - Validation ratio (per α-3): must satisfy ≥3:1 success ratio + ≥10
     uses (per Q6).
6. **/lint findings summary**
   - Counts per signal class (structural / α-state / contradiction /
     stale-confidence-age / time-based).
7. **Brigadier load**
   - Pending Task draft count, average review latency.
8. **Update mechanism**
   - Who updates (meta-agent on cron? or `/lint` postruns?).
   - Update cadence (daily / weekly).
   - Append-only structured log under each section header.

**Concreteness bar:** Стадия D can populate this file with placeholders +
the structured log scaffold.

**Format:** Full markdown file as fenced block + computation-formula
table per metric.

---

### Deliverable 11 — Q6 Skill Activation-vs-Validation Rubric (resolves T3)

**Mandate:** Per Q6 + Tension T3, specify the **rubric** that decides
when a skill candidate moves from `learning/` to `active/`, and from
`active/` to `retired/`. Required components:

- **Activation predicate (learning → active):**
  - Golden-set ≥3 (per Q6) — exact definition of golden-set test.
  - Validated success ratio ≥3:1 (per Q6) — exact win/loss accounting.
  - Minimum N=10 uses recorded (per Q6).
  - Brigadier sign-off (per Q6 owners).
  - All four conditions ANDed.
- **Retirement predicate (active → retired):**
  - Success ratio drops <1:1 over rolling 10 uses.
  - OR: a superseding skill is activated.
  - OR: meta-agent or Ruslan invokes retirement.
- **Tombstoning predicate (active or retired → tombstoned):**
  - Skill is found to have caused a production incident or contradicts
    an updated foundation.
- **Worked examples** — one activation, one retirement, one tombstoning,
  each with the data (success/loss counts, golden-set results) that
  triggered the move.
- **Owner roles per transition** (per Q6):
  - propose: anyone (any agent or Ruslan).
  - draft: brigadier or owning expert (`mode: writing-support`).
  - eval: brigadier (against golden-set).
  - activate: brigadier.
  - audit: meta-agent.
  - retire: meta-agent or Ruslan.
- **Anti-T3 clause** — explicitly resolve the activation-vs-validation
  tension by stating: validation evidence must be filesystem-resident
  (committed golden-set + use logs) **before** activation. No verbal
  validation.

**Concreteness bar:** A skill's transition can be auto-checked from
filesystem state (logs + golden-set) by `/lint`.

**Format:** Subsection with predicates + worked examples + owners table +
anti-T3 clause.

---

### Deliverable 12 — Strategies.md Trio Collapse (resolves T5)

**Mandate:** Per Tension T5 + R6 (accepted), collapse the strategies-storage
trio into 2 venues:

- **KEEP:** `agents/<expert>/strategies.md` — per-expert System Prompt
  Learning accumulations (per CLAUDE.md per-agent memory section, layer
  "Strategies").
- **KEEP:** `swarm/wiki/meta/agent-improvements/<expert>-<date>.md` —
  swarm-wide cross-expert improvement records, governed by α-3
  Strategies-Rule and brigadier write protocol.
- **DROP:** `swarm/strategies/` — explicitly out. Document as "rejected
  venue per T5 + R6 collapse."

For each kept venue, specify:

- **Path + naming convention** (exact).
- **Owner write rights** (`agents/<expert>/strategies.md` writable by the
  expert directly without brigadier gate, since it's local memory; the
  `swarm/wiki/meta/agent-improvements/` venue is brigadier-write only,
  per single-writer Q2 rule).
- **Sync rule** — when a per-expert insight rises to swarm-wide:
  expert proposes via Task → brigadier evaluates (per α-3 candidate →
  learning) → on activation, written to
  `swarm/wiki/meta/agent-improvements/`.
- **Migration note** — if any data is currently in `swarm/strategies/`
  (Phase A bootstrap), migrate to the appropriate of the 2 kept venues
  before Стадия D completion.
- **Lint rule** — `/lint` flags any file under `swarm/strategies/` as a
  T5 violation.

**Concreteness bar:** A reader can trace any single piece of strategies
content to exactly one of the 2 kept venues.

**Format:** Subsection with the 2 kept venues + 1 dropped venue +
migration note + lint rule.

---

## 7. QUALITY CRITERIA — YOU ARE MEASURED AGAINST THESE

- **All 12 deliverables present and labelled** as section headers
  matching Section 6 verbatim.
- **8,000–14,000 words** total spec length. Not shorter. Depth over
  summary.
- **1000% depth (W-12 mandate):** every deliverable concrete, not
  hand-wavy. Templates with exact field lists. State machines with exact
  transitions and movers. Rubrics with exact predicates.
- **Provenance density:** every recommendation cites at least one of:
  W-1..W-12, Q1..Q9, R1..R8, T1..T5, FPF Part 4 / Part 10, master
  synthesis §5.5–§5.10, knowledge-architecture §A–§H, an existing v2
  template/skill, or a 24-Lock entry. Bare assertions are unacceptable.
- **Zero re-opened locks:** no W/Q/R/T/24-Lock decision is re-debated. If
  a tension surfaces, escalate via AWAITING-APPROVAL — do not resolve.
- **Tier discipline:** no Tier 4 input (no books, no web). Sub-agents
  policed.
- **Max-subscription compliant:** zero references to paid embeddings,
  third-party APIs, or anything that requires `ANTHROPIC_API_KEY`.
- **Single-writer brigadier honoured:** every write-path in the spec
  routes through brigadier (per Q2), even meta. Experts return via
  Task.
- **2-gate Stage-Gated:** Gate 1 (Deliverables 1–6) approved before Gate
  2 starts. Final consolidation only after both gates approved.
- **Adversarial critic applied at both gates:** showstoppers + high
  findings fixed pre-gate. Critic reports committed.
- **No marketing language:** no "cutting-edge", "robust", "elegant".
  Flat, technical, contractual register.
- **Russian permitted only for Ruslan voice anchors** (direct quotes); main
  spec text in English for technical precision.

---

## 8. OPERATIONAL PROTOCOL

### Launch (server-side)

```bash
ssh ruslan@100.99.156.28
cd ~/jetix-os
git pull origin claude/jolly-margulis-915d34
unset ANTHROPIC_API_KEY
tmux new -ds wiki-v3-arch
tmux send-keys -t wiki-v3-arch "claude --dangerously-skip-permissions" C-m
```

Then point Claude Code at this prompt:
`prompts/step-2-2-3c-wiki-v3-architecture-spec-2026-04-23.md`.

### Operating mode: STAGE-GATED

You operate in Stage-Gated mode for the entire session. Commit + push at
each logical chunk. Pause at each of the 2 gates.

### Commit cadence checklist

1. After Phase 1 (5 parallel sub-agent extractions):
   `[step-2-2-3c] 5 parallel extractions for wiki v3 architecture spec`.
2. After each Deliverable draft (1 through 6, then 7 through 12):
   `[step-2-2-3c] D<N> draft: <subject>` (one commit per deliverable).
3. After critic-gate-1 report:
   `[step-2-2-3c] critic gate1 report`.
4. After Gate 1 file:
   `[step-2-2-3c] AWAITING-APPROVAL gate1 (deliverables 1-6)`. Push. Pause.
5. After critic-gate-2 report:
   `[step-2-2-3c] critic gate2 report`.
6. After Gate 2 file:
   `[step-2-2-3c] AWAITING-APPROVAL gate2 (deliverables 7-12)`. Push. Pause.
7. After final consolidation:
   `[design] AWAITING-APPROVAL wiki v3 architecture (Стадия C complete)`.
   Push. Halt.

### Branch + push rules

- Branch: `claude/jolly-margulis-915d34` (do NOT branch off).
- Push after every commit.
- No force-push, no rebase, no destructive ops.

### Cost discipline

- `unset ANTHROPIC_API_KEY` before launch (Max-subscription only).
- No third-party APIs, no paid embeddings.
- Sub-agents inherit the same constraint; brief them explicitly.

### If stuck

- Sub-agent extraction shallow → spawn replacement with tighter brief +
  page/section anchors.
- Two locks appear to conflict → cite both, escalate as
  `design/AWAITING-APPROVAL-conflict-<id>.md`. Do not resolve unilaterally.
- Tier-1 file unexpectedly missing → flag, continue with available; note
  gap in spec appendix.
- Ruslan unresponsive >12h on a gate → pause; do not push past. Polish
  critic reports in the meantime.

---

## 9. ANTI-PATTERNS FOR YOU SPECIFICALLY

- **Do not write an essay.** This is an architecture spec. Tables,
  fenced code blocks, ASCII diagrams, structured prose welcome. Flowing
  narrative is not the goal.
- **Do not be aspirational.** "The system supports cross-references"
  is weaker than "The system stores cross-references in three channels:
  YAML `related[]`, inline `[[type/slug]]`, and `swarm/wiki/graph/edges.jsonl`
  records of shape `{from, to, type, metadata}` — written by the
  brigadier on every wiki-page commit per the wiki write protocol
  (Deliverable 6 §1)." Be the second sentence.
- **Do not avoid specificity.** If a state name can be named, name it.
  If a line range can be cited, cite it. If an edge cardinality can be
  resolved, resolve it.
- **Do not re-open locked decisions.** If you find yourself wanting to
  re-debate the 4-tier retrieval stack (Q1) or single-writer brigadier
  (Q2), stop. Cite WIKI-V3-MECHANICS and continue.
- **Do not hallucinate citations.** If you cite §5.5.5 of master
  synthesis, the section must exist (it does — verify). If you cite a
  Q-resolution, quote the resolution sentence.
- **Do not let sub-agents drift into Tier 4.** No books. Enforce in their
  briefs.
- **Do not collapse deliverables.** All 12 are mandatory. Merging
  Deliverable 8 (skill diffs) into Deliverable 7 (config) is an error;
  they are governed by separate decisions.
- **Do not skip adversarial review.** Both gates require critic pass.
- **Do not write Стадия D content.** No file in `swarm/wiki/`, `swarm/lib/`,
  `.claude/config/`, or `.claude/skills/` is created in this pass. Only
  the spec at `design/AWAITING-APPROVAL-wiki-v3-architecture-<today>.md`
  is written.
- **Do not push past gates.** Both gates require Ruslan approval before
  proceeding.
- **Do not over-summarise.** A "tl;dr" at the top of the spec is fine.
  A "tl;dr" replacing a deliverable is not.
- **Do not invent new alphas.** The 5 swarm-alphas are α-1..α-5. If you
  feel a 6th is needed, escalate via AWAITING-APPROVAL.
- **Do not invent new layers.** The 9 layers are locked. Layer 9
  activation is gated per Q8.

---

## 10. SUCCESS CRITERIA

You are done when **all 12 are met**:

1. ✅ `design/AWAITING-APPROVAL-wiki-v3-architecture-<today>.md` exists,
   8,000–14,000 words, all 12 deliverables present and labelled.
2. ✅ Sub-agent extractions preserved at
   `raw/research/step-2-2-3c-extractions/{A,B,C,D,E}-*.md`.
3. ✅ Two adversarial-critic reports preserved:
   `raw/research/step-2-2-3c-extractions/critic-gate{1,2}.md`.
4. ✅ Both Gate 1 and Gate 2 AWAITING-APPROVAL files committed,
   pushed, and Ruslan-approved (inline ack or separate ack).
5. ✅ Final consolidated spec committed and pushed; Стадия D may begin
   from this single source.
6. ✅ ≥40 distinct provenance citations across W/Q/R/T/24-Lock/§5.5/FPF/
   knowledge-arch/v2-templates.
7. ✅ Zero locked-decision re-openings (no W/Q/R/T/24-Lock contradicted).
8. ✅ All 9 layers covered in Deliverable 1 directory layout, with
   per-layer template in Deliverable 2.
9. ✅ All 12 edge types in Deliverable 3, each with definition +
   cardinality + inverse + example + cross-layer flag.
10. ✅ All 5 swarm-alphas in Deliverable 5, each with state graph +
    transitions + movers + acceptance predicates + ASCII diagram.
11. ✅ All 6 skills in Deliverable 8, each with concrete edit diff
    + line ranges + before/after + test plan.
12. ✅ Max-subscription discipline visible throughout (no API-key
    references, no paid-embedding mentions).

If any of the 12 is unmet, you are not done; iterate.

---

## 11. FINAL NOTE

This spec is not the wiki. This spec is the **constitution from which the
wiki is built and operated.** Every paragraph here becomes a contract
that the brigadier enforces, that the experts read, that `/lint` checks,
that Phase B compounds on. A vague directory path here becomes a misfiled
page next month. A missing edge inverse here becomes a broken multi-hop
query next quarter. A hand-wavy state machine here becomes a swarm that
no one can audit.

Write contracts, not commentary. Cite locks, not opinions. Specify
mechanisms, not aspirations. Treat the 1000% depth mandate as binding.

Begin with Phase 1: spawn the 5 parallel deep-read sub-agents in a single
message.

---

## 12. REFERENCES (for Ruslan's audit)

### Authoritative inputs
- `decisions/WIKI-V3-MECHANICS-2026-04-23.md` (Q1..Q9 + R1..R8 + T1..T5)
- `design/ROY-WIKI-V3-GOALS-2026-04-23.md` (W-1..W-12)
- `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` (Part 4 alphas, Part 10 protocols)
- `design/ROY-BUILD-LOGIC-2026-04-23.md` (build phasing)
- `decisions/ROY-ALIGNMENT-2026-04-22.md` (matrix 5×4 pattern)
- `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` (§5.5 baseline)

### Research grounding
- `raw/research/knowledge-architecture-deep-research-2026-04-19.md`
- `raw/articles/karpathy-llm-wiki-gist-2026-04.md`
- `raw/research/step-2-2-3b-extractions/W-{1,2,3}-*.md`

### Existing infrastructure
- `wiki/_templates/` (9 v2 entity templates)
- `wiki/graph/edges.jsonl` (current edge vocabulary)
- `wiki/{overview,index,log}.md` (v2 conventions)
- `.claude/skills/{ingest,ask,lint,compile,consolidate,build-graph,search-kb,sweep-notion-bank}.md`
- `CLAUDE.md` (Wiki Architecture v2 section)
- `.claude/rules/global.md`

### Stylistic kin (do not copy; reference only)
- `prompts/step-2-1-master-synthesis-2026-04-22.md` (tier list, sub-agents, gates, success-criteria patterns)

### Output target
- `design/AWAITING-APPROVAL-wiki-v3-architecture-<today>.md` (8K–14K words, 12 deliverables)

### Branch
- `claude/jolly-margulis-915d34`

### Notion parents (for Ruslan navigation)
- Parent page: https://www.notion.so/34a2496333bf817d93bff4cb66775587
