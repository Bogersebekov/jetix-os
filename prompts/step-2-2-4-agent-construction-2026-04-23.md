---
title: Шаг 2.2.4 — Agent Construction Execution Prompt (Brigadier + 5 Experts + Wiki v3 Infra)
date: 2026-04-23
status: ready-for-launch
target_executor: Claude Code on server (Opus 4.7, 1M context, extended thinking max)
launch_branch: claude/jolly-margulis-915d34
estimated_duration: 6-12 hours (two gates included)
output_primary:
  - .claude/agents/brigadier.md
  - .claude/agents/engineering-expert.md
  - .claude/agents/mgmt-expert.md
  - .claude/agents/systems-expert.md
  - .claude/agents/philosophy-expert.md
  - .claude/agents/investor-expert.md
output_secondary:
  - swarm/wiki/**                                  # 9 layers + global spine + templates + graph
  - swarm/lib/shared-protocols.md                  # runtime contract imported by all 5 experts
  - .claude/config/wiki-roots.yaml                 # Q9 parameterisation
  - .claude/skills/*.md                            # 5 in-scope diffs per D8
  - .claude/skills/README.md                       # symlink convention per D9
upstream_authoritative:
  - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md          # final consolidated spec (D1–D12, 33K words)
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md  # §5.1 brigadier skeleton, §5.2 expert skeleton
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md  # 18 E-items, 5 alphas, Part 10 shopping list
  - decisions/WIKI-V3-MECHANICS-2026-04-23.md                   # Q1..Q9 + R1..R8 + T1..T5
  - design/ROY-WIKI-V3-GOALS-2026-04-23.md                      # W-1..W-12
  - design/ROY-BUILD-LOGIC-2026-04-23.md                        # build phasing + file locations
  - decisions/ROY-ALIGNMENT-2026-04-22.md                       # 5×4 matrix
upstream_constraints:
  - raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md     # Locks D1–D8
  - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md         # Locks D9–D18
  - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md # Locks D19–D24
  - CLAUDE.md
  - .claude/rules/global.md
written_by: Claude Code on server (prompt-writing pass, 2026-04-23)
meta_brief: prompts/meta-brief-step-2-2-4-agent-construction-2026-04-23.md
prompt_pattern: stylistic kin to prompts/step-2-2-3c-wiki-v3-architecture-spec-2026-04-23.md
---

# ШАГ 2.2.4 — AGENT CONSTRUCTION (BRIGADIER + 5 EXPERTS + WIKI v3 INFRA)

> **⚠️ READ THIS FIRST — THE FRAMING IS LOAD-BEARING**
>
> **This is the most important writing task of your existence as this
> Claude Code instance.** Every line of every agent system prompt you
> produce becomes seed code that compounds over months — across every
> task the swarm executes, every critic pass, every strategies.md
> accrual, every Phase B self-improvement cycle. Shallow here = shallow
> agents forever. A missing FPF block here = a silent bias running for
> a decade. A hand-wavy mode section here = a critic that never fires,
> an integrator that never converges, a scalability rubric that flags
> nothing. The quality of every downstream artefact of Jetix is
> capped by the quality you commit to today.
>
> 1000% depth (W-12 mandate). No shortcuts. No skipping sections. No
> "good enough". Every rubric has predicates. Every mode has an
> activation mechanic. Every frontmatter field has type + default +
> validation rule. Every §7 import stub references the exact path in
> `swarm/lib/shared-protocols.md`. Every §8 anti-pattern is
> domain-specific, not generic. Every §9 strategies.md entry format
> follows the 4-part DRR standard (per E-9).
>
> **Ruslan's explicit directive (2026-04-23):**
> *«ебейший нахуй на 1000% проработанный, самая глубокая и качественная
> prompt для реализации этого всего проекта.»*
>
> You are obligated to produce this at the highest level humanly
> possible. Not the level that "ships". The level where you read it
> back six months from now and the agents still feel like they were
> designed by someone who took the task more seriously than it
> deserved. Depth over speed. Specificity over flexibility. Contracts
> over commentary. Mechanics over rhetoric.
>
> This is the capstone of Phase A. The 6 files you produce under
> `.claude/agents/` are the swarm. Everything Phase B onward compounds
> on them. Write them as if every character matters. Because it does.

---

## 1. MISSION

Produce **6 production-ready agent system prompts** under
`.claude/agents/` — one brigadier + five domain experts — and the full
**wiki v3 infrastructure** under `swarm/wiki/`, `swarm/lib/`,
`.claude/config/`, and `.claude/skills/` such that:

1. The six `.claude/agents/*.md` files execute against the runtime
   contract defined in `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`
   (Deliverable 6 — `swarm/lib/shared-protocols.md`) on their very next
   Task invocation.
2. Every expert agent implements the **5 × 4 matrix** (5 domain experts
   × 4 role-modes — critic / optimizer / integrator / scalability) from
   `decisions/ROY-ALIGNMENT-2026-04-22.md`, with **soft activation**
   (mode prompt-prefix) and **hard-enforcement hook scaffolding**
   (UserPromptSubmit hook stub, per E-4/E-6 rubric rows).
3. Every expert agent has the **FPF 8-block structure** (§1a Identity
   / §1b Ontological / §1c Graph-of-Creation / §1d Seniority / §2
   Primary Domain / §§3–6 Four Modes / §7 Shared import-stub / §8
   Anti-patterns / §9 Strategies.md protocol + Implementation AI +
   Implementation Human + Evolution) per FPF Part 10 §10.2.
4. The brigadier has the **11-section master-synthesis §5.1 skeleton**
   augmented with the six FPF §10.3 brigadier-specific additions
   (ontological block; PMBOK / Grove / Cagan / Drucker / Anthropic / CE
   named primary_frameworks; decision-rights matrix with an explicit
   `never` list; "Orchestration authority, not domain authority"
   identity clause; Decompose-or-Chat gate; 3-level creation graph).
5. Every piece of wiki v3 infrastructure that Deliverables 1–10 of the
   consolidated spec mandate is physically on disk, lint-valid, and
   tree-shaped exactly as D1's ASCII layout.
6. Per-expert + swarm-wide **strategies scaffolding** is in place
   (`agents/<expert>/strategies.md` + `swarm/wiki/meta/agent-improvements/<expert>-improvements.md`)
   per T5 + R6 collapse (D12); `swarm/strategies/` is explicitly **not
   created** and any accidental occurrence is deleted.
7. A final **bootstrap verification** pass confirms file counts, tree
   shape, 8-block conformance, YAML validity, and a round-trip
   symlink test (create candidate → promote α-3 → symlink resolves).

The deliverable set lands as two `AWAITING-APPROVAL-*` commits (Gate 1
after brigadier + infrastructure complete; Gate 2 after all 6 agents +
diffs + verification) before final consolidation as
`[decisions] ROY-AGENTS-BUILT — 6 agents + wiki v3 infra live (Шаг 2.2.4 complete)`.

Downstream consumers of this output:

1. **The swarm itself at runtime** — brigadier + 5 experts coordinate
   every real Jetix task from this point forward.
2. **Phase B self-improvement** — the swarm ingests the 393-book
   Private Library and rewrites **these** files as v2 of itself.
3. **Ruslan's oversight** — Stage-Gated HITL at Gate 1 and Gate 2
   before Phase A closes.

---

## 2. WHAT YOU ARE NOT DOING

Scope discipline is non-negotiable. Be brutally clear:

- **You are not re-designing anything.** The architecture is locked by
  12 W-items, 9 Q-resolutions, 8 R-items, 24 Locks (D1–D24), 18 FPF
  E-items, and the 12 wiki-v3 deliverables. Cite — do not re-debate.
- **You are not reading the 393 books in `raw/books-md/`.** That is
  Phase B fuel, period. An expert's §1b / §9 lists the books it
  **will** read in Phase B, but it does **not** distil them now.
- **You are not running `WebSearch` or `WebFetch`.** All inputs are
  local. The curated corpus is already in Tier 1 + Tier 2 + Tier 3.
- **You are not touching the 14 legacy agents** under `.claude/agents/`
  (crazy-agent / inbox-processor / knowledge-synth / life-coach /
  manager / meta-agent / personal-assistant / sales-lead /
  sales-outreach / sales-researcher / staging-writer / strategist /
  sweep-worker / system-admin). They coexist unchanged alongside the
  new 6 files. After Phase A you will have **20** total agent files.
- **You are not touching the existing `wiki/` v2 tree.** The new
  infrastructure lives under `swarm/wiki/` per the Q9 coexist+parameterise
  resolution. `wiki/` stays live through Phase A; the v2↔v3 bridge is
  expressed only through the `cross-tree-ref` edge type (D3) and the
  parameterised skills (D8).
- **You are not writing a brand-new shared-protocols contract.** D6 of
  the final spec **is** the contract (9 sections verbatim). You copy
  it into `swarm/lib/shared-protocols.md`. You do not edit its semantics.
- **You are not inventing an `AWAITING-APPROVAL-wiki-v3-*` file.** The
  spec was approved at both gates on 2026-04-23 and is consolidated at
  `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`. That file is
  final; build from it.
- **You are not generating agents for domains outside the 5 experts.**
  The matrix is 5 × 4 — engineering / mgmt / systems / philosophy /
  investor. No sales-expert, no brand-expert, no life-expert exists in
  Phase A. Ruslan decides Phase B additions.
- **You are not implementing Phase B self-improvement.** You are
  building the swarm that will later self-improve. Every expert's §9
  Evolution block names 10 / 50 / 200 cycle milestones — you do not
  execute any of them here.
- **You are not exceeding 2500 lines per agent file.** FPF Enhancement
  Gate 2 resolved the master-synthesis 1500–3000 tension to **≤ 2500
  hard cap**. Over-cap is a showstopper, not a style issue.

If you feel the urge to re-open any of the above, stop. Cite the
locking document and proceed.

---

## 3. INPUTS — PRECISE READING ORDER (ENFORCED VIA SUB-AGENTS)

### Tier 1 — PRIMARY (deep read, cite extensively)

Every deliverable must trace back to one or more of these. No output
paragraph may contradict any Tier 1 source.

```
# The architecture spec (wiki v3 physical contract — D1..D12 ~33K words)
design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md

# The agent skeletons (brigadier §5.1, expert 9-section §5.2)
decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md
  # deep-read: §5.1 (brigadier), §5.2.1 (expert 9-section),
  #            §5.3 (mode rubrics), §5.5 (wiki protocol baseline),
  #            §5.6 (anti-patterns), §5.7 (max-subscription),
  #            §5.10 (skills inventory)

# The FPF enhancement (18 E-items, 5 alphas verbatim, Part 10 shopping list)
decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md
  # deep-read: Part 1 (E-1..E-11 rubrics), Part 4 (α-1..α-5 alphas),
  #            Part 6 (brigadier block), Part 10 (§10.1..§10.7)

# The locked mechanics (Q1..Q9 + R1..R8 + T1..T5)
decisions/WIKI-V3-MECHANICS-2026-04-23.md

# The locked goals (W-1..W-12)
design/ROY-WIKI-V3-GOALS-2026-04-23.md

# Build logic (file locations, Phase A vs B phasing)
design/ROY-BUILD-LOGIC-2026-04-23.md
  # deep-read: §1.2 (file locations — .claude/agents/ for agents, swarm/ for data),
  #            §1.3 (Max-subscription ops), §2 (Phase-A scope), §4 (phasing)

# The matrix pattern (5 × 4 alignment)
decisions/ROY-ALIGNMENT-2026-04-22.md
```

### Tier 2 — LOCKED DECISIONS (compliance-check; cite, do not re-derive)

Read fully the first pass, then keep open during drafting as compliance
reference.

```
raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md         # Locks D1..D8
raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md             # Locks D9..D18
raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md    # Locks D19..D24
CLAUDE.md                                                                       # per-agent memory 5-layer spec, wiki v2 conventions
.claude/rules/global.md                                                         # repo-wide invariants
```

### Tier 3 — EXISTING INFRASTRUCTURE (audit + do not break)

These are inspected for transplant semantics and line-accurate diffs.
Do NOT overwrite any of them; only produce new files alongside and
apply the D8 skill diffs line-by-line.

```
.claude/agents/                 # 14 legacy files — ENUMERATE (do not touch):
                                #   crazy-agent.md, inbox-processor.md,
                                #   knowledge-synth.md, life-coach.md,
                                #   manager.md, meta-agent.md,
                                #   personal-assistant.md, sales-lead.md,
                                #   sales-outreach.md, sales-researcher.md,
                                #   staging-writer.md, strategist.md,
                                #   sweep-worker.md, system-admin.md
.claude/skills/ingest.md        # D8 target — apply line-accurate diff
.claude/skills/ask.md           # D8 target
.claude/skills/lint.md          # D8 target
.claude/skills/consolidate.md   # D8 target
.claude/skills/build-graph.md   # D8 target
.claude/skills/compile.md       # documented exclusion (D8 rationale)
.claude/skills/search-kb.md     # documented exclusion (D8 rationale)
.claude/skills/sweep-notion-bank.md  # documented exclusion (D8 rationale)
wiki/                           # existing v2 — coexist per Q9, never mutate
wiki/_templates/                # read for v2 baseline, do not modify
wiki/graph/edges.jsonl          # current vocabulary reference
```

### Tier 4 — DO NOT READ (out of scope, enforced)

- `raw/books-md/` — 393 books, Phase B fuel. The experts name their
  book lists in §1b / §9 but do not distil. If a sub-agent asks to
  open any book, refuse and re-brief.
- `WebSearch`, `WebFetch`, any third-party API — all retrieval is
  local + Max-subscription only. `ANTHROPIC_API_KEY` is unset at
  session start.
- Architecture variants V1–V5 — legacy 12-agent pattern, disproven by
  research. Not relevant.
- Business-strategy research (consulting / agency / CRM / community /
  holding / platform-os / product / software) — not agent-design input.
- Voice memos, Notion exports, ATOM-REGISTRY, KNOT-MAP — not relevant
  to agent construction.
- Anything not enumerated in Tier 1 / Tier 2 / Tier 3.

If a sub-agent surfaces a deliverable that seems to require Tier 4
input, you are over-scoping — re-read the deliverable mandate in §6.

---

## 4. SUB-AGENT STRATEGY (MANDATORY — DO NOT WORK MONOLITHICALLY)

Tier 1 alone is ~250K tokens of prose. Working sequentially will
exhaust context and produce shallow output. **You parallelise via the
Task tool, then integrate. Single message, multiple Task tool uses.**

### Phase 1 — Parallel deep-read extractions (spawn six concurrent sub-agents)

Each sub-agent returns a **structured extraction** (frontmatter +
sections, ≤ 3,000 words) committed to
`raw/research/step-2-2-4-extractions/`.

#### Sub-agent A — Brigadier Skeleton + FPF §10.3 Brigadier Additions

**Brief.** Read `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
§5.1 in full and `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`
Part 6 (Brigadier) + §10.3 (Brigadier-specific additions) + E-12
(3-level creation graph) + E-15 (Orchestration authority clause) +
E-17 (Decompose-or-Chat gate). Extract:

- The 11-section brigadier skeleton, per-section line budget, and each
  section's mandate.
- For each FPF brigadier addition: the verbatim phrasing that must
  appear in `.claude/agents/brigadier.md`, anchored to the section it
  augments.
- The PMBOK / Grove / Cagan / Drucker / Anthropic / CE primary_frameworks
  list with exactly one-sentence-per-framework relevance note (why this
  framework belongs in a brigadier's method block).
- Decision-rights matrix: the specific `never` list (what brigadier
  never does unilaterally — e.g. override an expert's §8 anti-pattern
  refusal without HITL).
- Tool permissions per §5.7: exactly which Claude Code tools the
  brigadier gets (Read / Write / Edit / Bash / Grep / Glob / Task).

**Output:** `raw/research/step-2-2-4-extractions/A-brigadier-skeleton.md`.

#### Sub-agent B — Expert 9-Section Skeleton + FPF 5-Block Enhancement

**Brief.** Read `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
§5.2.1 (expert 9-section) + §5.3 (mode rubrics per mode) and
`decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` Part 1
(E-1..E-11) + Part 10 §10.1 (structural shopping list) + §10.2
(per-expert block additions). Extract:

- The 9-section expert skeleton (§1 Identity / §2 Primary Domain / §3
  Critic / §4 Optimizer / §5 Integrator / §6 Scalability / §7 Shared
  Protocols / §8 Anti-patterns / §9 Strategies.md protocol).
- For each of E-1..E-11: the exact insertion point inside the 9-section
  skeleton + the concrete sub-field list that must be added.
- The FPF 8-block structure as instantiated inside the 9 sections:
  §1a Identity (frontmatter), §1b Ontological (frontmatter), §1c
  Graph-of-Creation (after identity), §1d Seniority/Scale (decision
  rights + escalation trigger + split trigger), §§3–6 four modes with
  E-3..E-6 rubric enhancements, §7 20-line import stub (E-7), §8
  5-column anti-pattern table with ≥ 8 rows (E-8), §9 4-part DRR entry
  format + Evolution sub-block (E-9) + Implementation AI (Block 6) +
  Implementation Human (Block 7) + Evolution (Block 8).
- Matrix 5 × 4 mode-switching mechanic: soft (prompt-prefix `mode:
  critic` / `mode: optimizer` / `mode: integrator` / `mode:
  scalability`) + hard (UserPromptSubmit hook scaffolding per Tier 2
  §5.3). The stub hook is a placeholder; the **section in each agent
  must describe** exactly how mode activation works, what the hook
  checks, and the refusal behaviour when an unsupported mode is
  requested.

**Output:** `raw/research/step-2-2-4-extractions/B-expert-skeleton.md`.

#### Sub-agent C — Wiki v3 Infrastructure Deliverables (D1–D10 Verbatim)

**Brief.** Read `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`
Deliverables 1 through 10. Extract, for each deliverable, the **exact
file content that must be created** in Стадия D terms (i.e. right now):

- **D1** — `swarm/wiki/` directory tree ASCII. Copy verbatim. This is
  the ground truth for Part D's `tree` verification.
- **D2** — per-layer frontmatter schemas (9 layers + `meta/agent-improvements/`
  sub-tree). Each schema rendered as a YAML block that can be pasted
  into the corresponding `_templates/<layer>.md` file.
- **D3** — `swarm/wiki/_templates/edge-types.md` (12-type enum). Full
  file content as a fenced markdown block.
- **D4** — 9 entity templates (concept / entity / source / claim / idea
  / topic / experiment / summary / foundation). Each as a fenced
  markdown block ready to copy into `swarm/wiki/_templates/<type>.md`.
- **D5** — `swarm/wiki/foundations/swarm-alphas.md`. α-1 Task / α-2
  Artefact / α-3 Strategies-Rule / α-4 Cycle / α-5 Direction — state
  graphs + transitions tables + movers + acceptance predicates +
  ASCII diagrams — verbatim from the spec.
- **D6** — `swarm/lib/shared-protocols.md` nine sections (Wiki write
  protocol / Provenance gate / Structured output schema / HITL
  escalation / Tool permission self-check / `mode: writing-support` /
  Tool-language abstractions / Max-subscription discipline / retrieval
  stack). Full file content as a fenced markdown block.
- **D7** — `.claude/config/wiki-roots.yaml` YAML. Full file content.
- **D8** — 5 in-scope skill diffs (`/ingest`, `/ask`, `/lint`,
  `/consolidate`, `/build-graph`) with exact line ranges + before /
  after snippets + rationale + test plan. Plus 3 documented exclusions
  (`/compile`, `/search-kb`, `/sweep-notion-bank`) with exclusion
  rationale.
- **D9** — `.claude/skills/` symlink convention, worked example,
  `README.md` content.
- **D10** — `swarm/wiki/meta/health.md` 8-section skeleton. Full file
  content.

**Output:** `raw/research/step-2-2-4-extractions/C-wiki-infra-verbatim.md`.

#### Sub-agent D — Matrix 5 × 4 Mode Mechanics + Rubric Enhancements

**Brief.** Read `decisions/ROY-ALIGNMENT-2026-04-22.md` in full,
`decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
§5.3 (per-mode rubrics), and `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`
E-3 (critic rubric rows) / E-4 (optimizer invariants) / E-5 (integrator
F/ClaimScope/R schema) / E-6 (scalability BOSC-A-T-X + Janus degraded-mode).
Extract:

- For each of the 4 modes — the base rubric from §5.3 + the E-3..E-6
  enhancement rows that must appear in every expert's §§3–6.
- Concrete predicate forms: **Conformance Checklist** (critic),
  **Acceptance Predicate** (critic), **≥ 2 Alternatives** (critic),
  **Anti-scope** (critic); **Invariant check** with WLNK / MONO /
  IDEM / COMM / LOC abbrevs (optimizer); **F / ClaimScope / R** per
  claim (integrator); **BOSC-A-T-X trigger** + **Janus degraded-mode
  spec** (scalability).
- The soft activation rule (prompt-prefix `mode: <name>`) and the
  hard-enforcement hook scaffold (Claude Code UserPromptSubmit hook
  checking frontmatter + prefix + refusing unsupported modes).
- Refusal behaviour when an expert is asked to operate in a mode it
  cannot support (e.g. mgmt-expert invoked `mode: scalability` on a
  pure-engineering artefact — must bounce via HITL per D6 §4).

**Output:** `raw/research/step-2-2-4-extractions/D-matrix-mode-mechanics.md`.

#### Sub-agent E — Per-Expert Canonical-Source Allocation + Strategies Template

**Brief.** Read `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`
Part 10 §10.2 (per-expert blocks) + §5.2.3 of master synthesis
(book allocation per expert) + §9 strategies.md 4-part DRR format (E-9).
Extract:

- For each of the 5 experts: (a) Phase-A Tier 1–3 distillation list (3
  canonical sources max per expert, already-digested, no raw book
  content); (b) Phase-B Tier 4 book list (the books this expert reads
  during self-improvement); (c) granularity tag (jetix-business /
  jetix-life-os / jetix-shared / task-scoped per E-16).
- The 5-expert canonical allocation matrix (engineering / mgmt /
  systems / philosophy / investor → primary-alpha + secondary-alphas +
  possible-tasks + out-of-scope-tasks per E-14 / §10.2).
- The strategies.md template for `.claude/agents/<expert>/strategies.md`:
  the 4-part DRR entry format (Decision / Reasoning / Result / Review)
  + Evolution sub-block (changelog / last-review / expected-evolution
  at 10 / 50 / 200 cycles per E-9).
- The agent-improvements/<expert>-improvements.md template for
  `swarm/wiki/meta/agent-improvements/`: same DRR format but with
  cross-expert scope + brigadier-write enforcement per D12.

**Output:** `raw/research/step-2-2-4-extractions/E-expert-allocation-strategies.md`.

#### Sub-agent F — Shared-Protocols Import-Stub Content + BUILD Location Constraints

**Brief.** Read `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`
Deliverable 6 (shared-protocols) + `design/ROY-BUILD-LOGIC-2026-04-23.md`
§1.2 (file locations) + §1.3 (Max-subscription ops) + CLAUDE.md
per-agent memory section. Extract:

- The **20-line import-stub** template that every expert's §7 will
  use: exact lines referencing `swarm/lib/shared-protocols.md` section
  numbers, with the imported semantics named (write gate / provenance /
  structured-output / HITL / tool-permission self-check / writing-support
  / tool-language / max-subscription). No duplication of content —
  just a pointer index.
- BUILD §1.2 location constraints: `.claude/agents/*.md` is the agent
  prompt; `swarm/wiki/**` is the data; `swarm/lib/**` is the runtime
  contract; `.claude/config/**` is parameterisation; `.claude/skills/**`
  is the skill registry. No data under `.claude/agents/`.
- BUILD §1.3 ops: `unset ANTHROPIC_API_KEY`, `--dangerously-skip-permissions`
  in tmux, branch `claude/jolly-margulis-915d34`, commit-as-you-go.
- CLAUDE.md per-agent memory: the 5 layers (Core / Strategies /
  Working / Niche / Recall) and where strategies.md sits in that
  stack (layer 2, expert-owned). This keeps `.claude/agents/<expert>/strategies.md`
  architecturally aligned with Ruslan's existing per-agent memory spec.

**Output:** `raw/research/step-2-2-4-extractions/F-shared-protocols-build-locations.md`.

### Sub-agent operational rules

- All six sub-agents run **concurrently** in a single message (six
  Task tool uses batched). Do not serialise.
- Each respects tier discipline: no Tier 4. If a sub-agent asks to
  read a book, refuse and re-brief.
- Each returns a **structured extraction file** committed under
  `raw/research/step-2-2-4-extractions/` as one commit:
  `[step-2-2-4] 6 parallel extractions for agent construction`.
- Sub-agents do **not** write any file outside
  `raw/research/step-2-2-4-extractions/` in Phase 1. The main
  orchestrator integrates.

### Phase 2 — Integration (orchestrator, sequential)

See §5 for the drafting sequence. Spawn targeted follow-up sub-agents
**only** on concrete gaps (e.g. "need exact line 42 of
`.claude/skills/ingest.md` to write the D8 diff cleanly"). Do not
spawn follow-ups for stylistic polish.

### Phase 3 — Adversarial critic (mandatory at both gates)

See §5.

---

## 5. SEQUENCE — PHASE 1 → PHASE 5

Commit cadence is small and frequent. Each numbered step below is one
commit minimum. If an API error interrupts mid-step, previous commits
preserve progress.

### Phase 1 — Parallel extractions

Single message, 6 concurrent Task calls (Sub-agents A–F per §4).

**Commit:** `[step-2-2-4] 6 parallel extractions for agent construction`.

### Phase 2 — Drafting (strictly ordered, not parallel)

Each of the following is a separate commit. Push after each.

#### 2.1 — Infrastructure first (so agents can reference it)

Build the wiki v3 infrastructure **before** drafting any agent system
prompt. This lets the brigadier's §7 import stub reference an existing
`swarm/lib/shared-protocols.md`.

1. `mkdir -p swarm/wiki/{foundations,concepts,entities,sources,topics,ideas,claims,experiments,summaries,meta,insights,skills/{candidates,learning,active,retired},graph,_templates}`
   — exact directories per D1. Plus:
   `mkdir -p swarm/wiki/themes/{brigadier,engineering,mgmt,systems,philosophy,investor}/`
   (per-expert theme shards if D1 mandates; verify against Sub-agent
   C's D1 extraction).
2. Write every file from Sub-agent C's verbatim content list:
   - `swarm/wiki/_templates/concept.md` … `foundation.md` (9 templates from D4)
   - `swarm/wiki/_templates/edge-types.md` (D3)
   - `swarm/wiki/foundations/swarm-alphas.md` (D5, verbatim from spec)
   - `swarm/wiki/overview.md`, `swarm/wiki/index.md`, `swarm/wiki/log.md`
     (bootstrap files, minimal placeholders following v2 structure)
   - `swarm/wiki/insights/README.md` (Phase B+ placeholder, single
     paragraph stating Layer 9 is inactive until Q8 activation gate)
   - `swarm/wiki/meta/health.md` (D10 skeleton, 8 sections)
   - `swarm/wiki/graph/edges.jsonl` (empty file with header comment)
3. Write `swarm/lib/shared-protocols.md` — D6 nine sections verbatim.
4. Write `.claude/config/wiki-roots.yaml` — D7 YAML verbatim.
5. **Validate** as you go: `python -c "import yaml; yaml.safe_load(open('.claude/config/wiki-roots.yaml'))"`
   for wiki-roots.yaml; `tree swarm/wiki/` compared against D1 ASCII.

**Commit:** `[step-2-2-4] wiki v3 infrastructure created (D1..D10 files)`.

#### 2.2 — Brigadier draft

Write `.claude/agents/brigadier.md` using:

- Sub-agent A's 11-section skeleton + FPF §10.3 additions.
- Sub-agent F's 20-line §7 import stub.
- Sub-agent D's 4-mode rubric content **as consumed** (brigadier
  orchestrates matrix invocations; it does not operate the 4 modes
  itself — its §3..§6 equivalent is the **Decompose-or-Chat gate** +
  routing table).
- The E-12 three-level creation graph, the E-15 "Orchestration
  authority, not domain authority" identity clause, the E-17
  Decompose-or-Chat gate, the decision-rights matrix with explicit
  `never` list.
- Tool permissions: Read / Write / Edit / Bash / Grep / Glob / Task
  (brigadier is the single wiki-writer per Q2 — Write permission is
  brigadier-exclusive among the 6 new agents).
- **Length: ≤ 2500 lines.** Sections concrete; no aspirational prose.

**Commit:** `[step-2-2-4] brigadier.md draft (11 sections + FPF 10.3 adds)`.

#### 2.3 — Adversarial critic — Gate 1 draft (brigadier + infra)

Spawn critic sub-agent with the adversarial brief in §4 applied to
brigadier + all Phase 2.1 files. See §5-critic below.

**Commit:** `[step-2-2-4] critic gate1 report`.

Apply showstoppers + high findings. Re-commit fixes before opening
Gate 1.

#### 2.4 — Gate 1 — AWAITING-APPROVAL (brigadier + infra)

Produce `design/AWAITING-APPROVAL-step-2-2-4-gate1-2026-04-23.md` —
a summary file pointing at the on-disk artefacts for Ruslan's review:

- Brigadier file path + line count + 11-section TOC
- All infra file paths + byte sizes + `tree swarm/wiki/` output
- Critic-gate1 report location + fix status
- Outstanding medium / low findings deferred to Gate 2 errata

**Commit + push:** `[step-2-2-4] AWAITING-APPROVAL gate1 (brigadier + infra)`.

**Pause.** Do not begin Phase 2.5 until Ruslan approves inline or via
separate ack.

#### 2.5 — 5 expert drafts in parallel (post-Gate-1 approval)

Spawn **5 concurrent sub-agent Task calls** in a single message —
one per expert. Each sub-agent writes exactly one file using:

- Sub-agent B's expert 9-section skeleton + FPF 8-block enhancements
- Sub-agent D's 4-mode rubric content (each expert operates all 4
  modes, per the matrix)
- Sub-agent E's per-expert canonical-source allocation + strategies
  template
- Sub-agent F's 20-line §7 import stub (shared across all 5)
- The expert's specific Part 10 §10.2 block additions (1a / 1b / 1c /
  1d / 4 / 5 / 6 / 7 / 8 plus the §2 ontological-spine sub-section per
  E-2)

The 5 experts to produce:

| File | Domain focus (from ROY-ALIGNMENT + master §5.2) |
|------|--------------------------------------------------|
| `.claude/agents/engineering-expert.md` | CE + clean code + Unix philosophy + AI-native + software architecture |
| `.claude/agents/mgmt-expert.md`        | PM + Product Mgmt + management philosophy (Grove / Drucker / Cagan / Shape Up / OKR) |
| `.claude/agents/systems-expert.md`     | systems thinking + cybernetics + complexity + biology |
| `.claude/agents/philosophy-expert.md`  | philosophy of science + mental models + stoic epistemology + engineering foundations |
| `.claude/agents/investor-expert.md`    | investing + capital allocation + long-term compounding |

Per-expert constraints:

- **≤ 2500 lines** (FPF Enhancement Gate 2 cap).
- **FPF 8-block** present: 1a Identity / 1b Ontological / 1c
  Graph-of-Creation / 1d Seniority-Scale / 2 Primary Domain (with
  ontological-spine per E-2) / §3 Critic (with E-3 rows) / §4
  Optimizer (with E-4 invariants) / §5 Integrator (with E-5 schema) /
  §6 Scalability (with E-6 BOSC-A-T-X + Janus) / §7 Shared Protocols
  (20-line import stub, no duplication) / §8 Anti-patterns (5-column
  table, ≥ 8 domain-specific APs) / §9 Strategies.md protocol (4-part
  DRR + Evolution sub-block + Implementation AI + Implementation
  Human + Evolution changelog).
- **Mode activation** specified: soft (prompt-prefix) + hard
  (UserPromptSubmit hook scaffold; the hook implementation may be a
  ticket stub, but the section must name the trigger, predicate, and
  refusal behaviour concretely).
- **§7 import-stub, not duplication** — if any shared-protocol content
  is copied into the agent file, the critic will flag it as a
  showstopper.

Each sub-agent writes its assigned file, returns a return-receipt, and
stops. The orchestrator verifies file existence + line count per sub-agent.

**Commit:** `[step-2-2-4] 5 experts drafted (parallel)`.

#### 2.6 — Skill diffs + symlink scaffolding

Apply D8 and D9 from Sub-agent C's extraction:

1. **5 skill diffs** — edit `.claude/skills/{ingest,ask,lint,consolidate,build-graph}.md`
   with the exact line-range diffs from D8. Each diff implements
   `$WIKI_ROOT` parameterisation per D7. Before committing, run the
   D8 per-skill test plan.
2. **3 documented exclusions** — add a brief comment block at the top
   of `.claude/skills/{compile,search-kb,sweep-notion-bank}.md` citing
   the D8 exclusion rationale (do NOT modify skill behaviour).
3. **Symlink README** — write `.claude/skills/README.md` per D9
   convention: the symlink rule `.claude/skills/<slug>.md →
   ../../swarm/wiki/skills/active/<slug>.md`, filename normalisation,
   creation hook in α-3 `learning → active`, removal hook in `active →
   retired` / `active → tombstoned`, conflict handling (`_v2` suffix),
   `/lint` broken-symlink detection. Include the worked example from D9.
4. **Initial symlink setup** — do NOT create any symlinks yet (no
   skill has been promoted through α-3 learning). The README is the
   contract; symlinks are created lazily on future promotions.

**Commit:** `[step-2-2-4] skill diffs + symlink README applied (D8 + D9)`.

#### 2.7 — Strategies + agent-improvements scaffolding (Part C)

Per D12 + CLAUDE.md per-agent memory:

1. `mkdir -p agents/{brigadier,engineering-expert,mgmt-expert,systems-expert,philosophy-expert,investor-expert}/`
2. For each agent: write `agents/<agent>/strategies.md` — empty-but-structured
   per Sub-agent E's template (4-part DRR + Evolution sub-block, with
   a one-line placeholder entry dated 2026-04-23 so the file is valid
   YAML-frontmatter + non-empty markdown).
3. `mkdir -p swarm/wiki/meta/agent-improvements/`
4. For each agent: write `swarm/wiki/meta/agent-improvements/<agent>-improvements.md`
   — empty-but-structured with the same DRR template, brigadier-write
   comment, one-line placeholder.
5. **Explicit deletion check:** `test ! -d swarm/strategies` must pass.
   If `swarm/strategies/` exists for any reason, `rm -rf` it and add a
   `/lint` rule stub calling it out as a T5 violation.

**Commit:** `[step-2-2-4] strategies + agent-improvements scaffolding (T5 compliance)`.

#### 2.8 — Adversarial critic — Gate 2 draft (5 experts + diffs + scaffolding)

Spawn critic sub-agent against all artefacts since Gate 1.

**Commit:** `[step-2-2-4] critic gate2 report`.

Apply showstoppers + high. Re-commit fixes.

#### 2.9 — Bootstrap verification (Part D)

Run these checks; each failure is a showstopper:

1. `tree swarm/wiki/` — diff against D1 ASCII. Must match exactly
   (empty files acceptable; missing files are failures).
2. `ls .claude/agents/*.md | wc -l` — must equal **20** (14 legacy + 6
   new).
3. For each of the 6 new agent files: grep for each of the mandated
   FPF 8 blocks / 9 sections. All 8 × 5 + 11 × 1 required anchors
   must resolve.
4. `python -c "import yaml; yaml.safe_load(open('.claude/config/wiki-roots.yaml'))"`
   — exit code 0.
5. **Symlink round-trip test:** create a dummy candidate
   `swarm/wiki/skills/candidates/roy-dummy-test.md`, simulate α-3
   promotion (move to `active/` + `ln -s`), confirm
   `cat .claude/skills/roy-dummy-test.md` resolves to the v3 file,
   then tear down (rm file + symlink). Log in critic-gate2 report
   appendix.
6. `grep -rE "ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY" .claude/agents/ swarm/lib/ swarm/wiki/`
   — zero matches (Max-subscription discipline per §5.7 master
   synthesis).

**Commit:** `[step-2-2-4] bootstrap verification passed (Part D)`.

#### 2.10 — Gate 2 — AWAITING-APPROVAL (final pre-consolidation)

Produce `design/AWAITING-APPROVAL-step-2-2-4-gate2-2026-04-23.md` —
summary + artefact list + critic-gate2 report pointer + Part D
verification output.

**Commit + push:** `[step-2-2-4] AWAITING-APPROVAL gate2 (5 experts + diffs + verification)`.

**Pause.** Do not consolidate until Ruslan approves.

### Phase 3 — Critic adversarial brief (mandatory, both gates)

Reused at 2.3 and 2.8. Brief verbatim:

> Adopt the role of a senior swarm engineer who inherits this repo on
> Monday and must execute the next real Jetix task using these 6
> agents + this infrastructure. You did not design them. Read them
> cold. Find every place where:
>
> (a) an agent file is missing a FPF 8-block element (1a/1b/1c/1d or
>     E-items E-1..E-18) — cite the block + the line-neighbourhood where
>     it should appear;
> (b) a mode activation mechanic (§§3–6) lacks a predicate, activation
>     trigger, refusal behaviour, or test case;
> (c) a §7 Shared Protocols section duplicates content from
>     `swarm/lib/shared-protocols.md` instead of importing it via the
>     20-line stub;
> (d) a §8 anti-pattern table has fewer than 8 domain-specific rows or
>     any row is generic (e.g. "don't hallucinate" without domain
>     grounding);
> (e) a §9 strategies.md entry format diverges from the 4-part DRR
>     standard or is missing the Evolution sub-block;
> (f) any agent file exceeds **2500 lines** (showstopper);
> (g) the brigadier's decision-rights matrix lacks the explicit `never`
>     list, or the Decompose-or-Chat gate is missing predicates;
> (h) any wiki v3 infrastructure file diverges from D1–D10 verbatim
>     (tree shape / template fields / edge enum / alpha state graphs /
>     shared-protocols 9 sections / wiki-roots.yaml keys / health 8
>     sections);
> (i) any skill diff diverges from D8 exact line range or test plan;
> (j) a locked decision (W-1..W-12, Q1..Q9, R1..R8, T1..T5, 24 Locks
>     D1..D24, FPF E-1..E-18) is silently re-opened;
> (k) the Max-subscription discipline is violated (any API-key env-var
>     reference, any paid embedding, any third-party API);
> (l) a Tier 4 input was consulted (books / web / out-of-scope files);
> (m) a deliverable from Parts A/B/C is missing entirely.
>
> For each finding, classify as **showstopper / high / medium / low**,
> cite **exact file + line range**, and propose a **minimal-fix
> suggestion**. Be merciless. This is production code.

Showstoppers + high → fix pre-gate. Medium → fix if ≤ 30 min; otherwise
log in errata appendix of the gate file. Low → log in errata.

### Phase 4 — Stage-Gated protocol (2 gates)

- **Gate 1** at step 2.4 — brigadier + infrastructure.
- **Gate 2** at step 2.10 — 5 experts + diffs + verification.
- No push past either gate without Ruslan's inline or separate ack.
- If Ruslan is unresponsive > 12 h on a gate, pause non-blocking work
  and continue only on critic-report polish.

### Phase 5 — Final consolidation

After both gates approved:

1. Remove or archive the two `AWAITING-APPROVAL-step-2-2-4-gate*.md`
   files by renaming to `design/step-2-2-4-gate{1,2}-2026-04-23.md`
   (Ruslan audit trail) — do NOT delete.
2. Write `decisions/ROY-AGENTS-BUILT-2026-04-23.md` — a one-page
   consolidation stating: Phase A swarm construction complete; 6
   agents + wiki v3 infra live; critic-gate1 + critic-gate2 fixes
   applied; Max-subscription discipline verified; 24 Locks + 18 FPF
   E-items + 12 wiki deliverables satisfied.
3. **Commit + push:** `[decisions] ROY-AGENTS-BUILT — 6 agents + wiki v3 infra live (Шаг 2.2.4 complete)`.

### Phase 6 — Halt

Do not launch the swarm. Do not execute a real task. The next step is
Ruslan's decision, not yours.

---

## 6. THE 4 DELIVERABLE GROUPS — EXACT FILE MANIFEST

### Part A — 6 agent system prompts (in `.claude/agents/`)

| # | File | Role | Required structure | Line cap |
|---|------|------|---------------------|----------|
| A1 | `.claude/agents/brigadier.md` | Orchestrator (single wiki-writer per Q2) | 11-section §5.1 skeleton + FPF §10.3 brigadier additions (ontological block, PMBOK/Grove/Cagan/Drucker/Anthropic/CE primary_frameworks, decision-rights matrix with explicit `never` list, "Orchestration authority, not domain authority" identity clause, Decompose-or-Chat gate, 3-level creation graph) + §7 20-line import stub | ≤ 2500 |
| A2 | `.claude/agents/engineering-expert.md` | Domain expert — CE + clean code + Unix + AI-native + software architecture | FPF 8-block within §5.2 9-section + E-1..E-11 + §10.2 per-expert additions + matrix 5×4 modes soft+hard + canonical-source list (Phase A Tier 1–3 distillation + Phase B Tier 4 book list per §5.2.3) | ≤ 2500 |
| A3 | `.claude/agents/mgmt-expert.md` | Domain expert — PM + Product Mgmt + management philosophy | same 8-block / 9-section / modes structure as A2 | ≤ 2500 |
| A4 | `.claude/agents/systems-expert.md` | Domain expert — systems thinking + cybernetics + complexity + biology | same | ≤ 2500 |
| A5 | `.claude/agents/philosophy-expert.md` | Domain expert — philosophy of science + mental models + stoic + epistemology + engineering foundations | same | ≤ 2500 |
| A6 | `.claude/agents/investor-expert.md` | Domain expert — investing + capital allocation + long-term compounding | same | ≤ 2500 |

**Concreteness bar.** Any of the six files can be read cold by a new
engineer on Monday and produce a correct output from a Task invocation
without needing to open the master synthesis, FPF, or wiki spec as a
sidebar.

### Part B — Wiki v3 infrastructure (physical files)

| # | Path | Source (verbatim) | Note |
|---|------|-------------------|------|
| B1 | `swarm/wiki/` (full tree per D1) | D1 ASCII | all 9 layers + global spine (themes/brigadier/agents/meta/tasks/operations/global/skills/insights/foundations/_templates/graph) |
| B2 | `swarm/wiki/_templates/{concept,entity,source,claim,idea,topic,experiment,summary,foundation}.md` | D4 | 9 entity templates as fenced blocks |
| B3 | `swarm/wiki/_templates/edge-types.md` | D3 | 12-type enum + from×to matrix |
| B4 | `swarm/wiki/foundations/swarm-alphas.md` | D5 | α-1..α-5 state machines verbatim |
| B5 | `swarm/wiki/overview.md` + `swarm/wiki/index.md` + `swarm/wiki/log.md` | D1 bootstrap | minimal placeholders following v2 structure |
| B6 | `swarm/wiki/insights/README.md` | D1 + Q8 | Layer 9 inactive placeholder |
| B7 | `swarm/wiki/meta/health.md` | D10 | 8-section dashboard skeleton |
| B8 | `swarm/wiki/graph/edges.jsonl` | D1 | empty file with header comment |
| B9 | `swarm/lib/shared-protocols.md` | D6 | 9-section runtime contract verbatim |
| B10 | `.claude/config/wiki-roots.yaml` | D7 | parameterisation YAML |
| B11 | 5 in-scope skill diffs: `.claude/skills/{ingest,ask,lint,consolidate,build-graph}.md` | D8 | line-accurate edits; total ≈ 85–115 lines |
| B12 | 3 documented exclusions: `.claude/skills/{compile,search-kb,sweep-notion-bank}.md` | D8 | top-of-file rationale comment only; behaviour unchanged |
| B13 | `.claude/skills/README.md` | D9 | symlink convention + worked example |

**Concreteness bar.** `tree swarm/wiki/` matches D1 ASCII byte-for-byte
(modulo whitespace). Every `_templates/*.md` file validates against its
D2 schema. `wiki-roots.yaml` passes `yaml.safe_load`.

### Part C — Strategies + agent-improvements scaffolding (T5 + R6 collapse)

| # | Path | Cardinality | Owner write rights |
|---|------|-------------|---------------------|
| C1 | `agents/brigadier/strategies.md` | per-agent | brigadier direct |
| C2 | `agents/engineering-expert/strategies.md` | per-agent | engineering-expert direct |
| C3 | `agents/mgmt-expert/strategies.md` | per-agent | mgmt-expert direct |
| C4 | `agents/systems-expert/strategies.md` | per-agent | systems-expert direct |
| C5 | `agents/philosophy-expert/strategies.md` | per-agent | philosophy-expert direct |
| C6 | `agents/investor-expert/strategies.md` | per-agent | investor-expert direct |
| C7 | `swarm/wiki/meta/agent-improvements/brigadier-improvements.md` | swarm-wide | brigadier only (single-writer Q2) |
| C8 | `swarm/wiki/meta/agent-improvements/engineering-expert-improvements.md` | swarm-wide | brigadier only |
| C9 | `swarm/wiki/meta/agent-improvements/mgmt-expert-improvements.md` | swarm-wide | brigadier only |
| C10 | `swarm/wiki/meta/agent-improvements/systems-expert-improvements.md` | swarm-wide | brigadier only |
| C11 | `swarm/wiki/meta/agent-improvements/philosophy-expert-improvements.md` | swarm-wide | brigadier only |
| C12 | `swarm/wiki/meta/agent-improvements/investor-expert-improvements.md` | swarm-wide | brigadier only |

Each file is **empty-but-structured**: YAML frontmatter (title / agent
/ created / last_modified / state=draft / confidence=N/A-scaffolding),
a section header, and exactly one placeholder DRR entry dated
2026-04-23 so the file is non-empty and lint-valid.

**Explicit deletion check:** `test ! -d swarm/strategies` passes. If
the directory exists, `rm -rf` it and log the removal in the Gate 2
AWAITING-APPROVAL summary with "T5 violation prevented: directory
found and removed during Part C step 5".

### Part D — Bootstrap verification

| # | Check | Predicate | Failure = |
|---|-------|-----------|-----------|
| D1 | `tree swarm/wiki/` matches D1 ASCII | `diff <(tree swarm/wiki/) <(cat spec-d1-tree.txt)` exit 0 (modulo whitespace) | showstopper |
| D2 | Agent file count = 20 | `ls .claude/agents/*.md \| wc -l == 20` | showstopper |
| D3 | All 6 new agents have FPF 8-block + 9-section anchors | `grep -c '^## §1a\|^## §1b\|^## §1c\|^## §1d\|^## §2\|^## §3\|^## §4\|^## §5\|^## §6\|^## §7\|^## §8\|^## §9' <file> >= 11` (brigadier) / `>= 12` (experts) | showstopper |
| D4 | `wiki-roots.yaml` valid YAML | `yaml.safe_load` exit 0 | showstopper |
| D5 | Symlink round-trip test passes | candidate → active symlink resolves via `.claude/skills/` | showstopper |
| D6 | No API-key env-vars referenced | `grep -rE "ANTHROPIC_API_KEY\|OPENAI_API_KEY\|GROQ_API_KEY" .claude/agents/ swarm/lib/ swarm/wiki/` → 0 matches | showstopper |
| D7 | No file exceeds 2500 lines under `.claude/agents/` (new six only) | `wc -l <file>` ≤ 2500 | showstopper |
| D8 | No Tier 4 file referenced in new agent bodies | `grep -l 'raw/books-md/' .claude/agents/brigadier.md .claude/agents/*expert.md` → 0 files | showstopper |
| D9 | `swarm/strategies/` does not exist | `test ! -d swarm/strategies` | showstopper |
| D10 | Each `§7 Shared Protocols` is ≤ 25 lines (import-stub, not duplication) | `awk '/^## §7/,/^## §8/' <file> \| wc -l` ≤ 25 | showstopper |

Log all check results in the Gate 2 AWAITING-APPROVAL summary + the
critic-gate2 report appendix.

---

## 7. QUALITY CRITERIA — YOU ARE MEASURED AGAINST THESE

- **All 4 Parts (A, B, C, D) complete** with every numbered row above
  on disk, lint-valid, and verified.
- **FPF 8-block present in all 5 experts + brigadier variant** — any
  missing block is a showstopper. The brigadier uses the master
  synthesis §5.1 11-section skeleton but **must still** have the §1b
  ontological block and §1c creation graph (per E-12 + §10.3).
- **Matrix 5 × 4 soft + hard enforcement scaffold** visible in every
  expert's §§3–6 — activation trigger, predicate, refusal behaviour
  for each mode.
- **Shared-protocols imported, not duplicated** — each expert's §7 is
  ≤ 25 lines and references `swarm/lib/shared-protocols.md` section
  numbers, not content. Brigadier §7 same.
- **Provenance density** — every recommendation inside an agent file
  cites at least one of: W-1..W-12, Q1..Q9, R1..R8, T1..T5, 24 Locks
  D1..D24, FPF E-1..E-18, master synthesis §5.1–§5.10, wiki v3 spec
  D1..D12, knowledge-architecture §A–§H, Sub-agent extractions A–F.
  Bare assertions are rejected.
- **Zero re-opened locks** — no W/Q/R/T/24-Lock/FPF-E decision is
  re-debated. If tension surfaces, escalate via AWAITING-APPROVAL —
  do not resolve.
- **Tier discipline** — no Tier 4 input. Sub-agents policed.
- **Max-subscription compliance** — `unset ANTHROPIC_API_KEY` at
  session start, no paid embeddings, no third-party APIs. Zero env-var
  strings in agent bodies.
- **Single-writer brigadier honoured** — only `.claude/agents/brigadier.md`
  carries Write permission for `swarm/wiki/`. The 5 experts describe
  their writes as **returns via Task under `mode: writing-support`**
  (per E-10), not direct filesystem mutation.
- **2-gate Stage-Gated** — Gate 1 approved before Gate 2 begins; final
  consolidation only after both gates approved.
- **Adversarial critic applied at both gates** — showstoppers + high
  fixed pre-gate. Reports committed under
  `raw/research/step-2-2-4-extractions/critic-gate{1,2}.md`.
- **No marketing language** — no "cutting-edge", "robust", "elegant",
  "unlocks". Flat, technical, contractual register.
- **Russian only for Ruslan voice anchors** (direct quotes). Agent
  bodies in English for technical precision. The directive quote in
  §1 framing may remain Russian.
- **Commit cadence** — one commit per numbered step in §5. Push after
  every commit. Small commits > big commits.

---

## 8. OPERATIONAL PROTOCOL

### Launch (server-side)

```bash
ssh ruslan@100.99.156.28
cd ~/jetix-os
git pull origin claude/jolly-margulis-915d34
unset ANTHROPIC_API_KEY
unset OPENAI_API_KEY
unset GROQ_API_KEY
tmux new -ds agent-construction
tmux send-keys -t agent-construction "claude --dangerously-skip-permissions" C-m
```

Then point Claude Code at this prompt:
`prompts/step-2-2-4-agent-construction-2026-04-23.md`.

### Operating mode: STAGE-GATED

Stage-Gated throughout. Commit + push at every numbered step in §5.
Pause at Gate 1 and Gate 2. Do not push past either gate without ack.

### Commit cadence checklist

1. After Phase 1 (6 parallel extractions):
   `[step-2-2-4] 6 parallel extractions for agent construction`.
2. After step 2.1 (infrastructure):
   `[step-2-2-4] wiki v3 infrastructure created (D1..D10 files)`.
3. After step 2.2 (brigadier draft):
   `[step-2-2-4] brigadier.md draft (11 sections + FPF 10.3 adds)`.
4. After step 2.3 (critic gate1):
   `[step-2-2-4] critic gate1 report`. Then fix commits as
   `[step-2-2-4] critic gate1 fixes: <subject>` (one commit per fix
   cluster).
5. After step 2.4 (Gate 1 AWAITING-APPROVAL):
   `[step-2-2-4] AWAITING-APPROVAL gate1 (brigadier + infra)`. Push.
   Pause.
6. After step 2.5 (5 experts parallel):
   `[step-2-2-4] 5 experts drafted (parallel)`.
7. After step 2.6 (skill diffs + symlink README):
   `[step-2-2-4] skill diffs + symlink README applied (D8 + D9)`.
8. After step 2.7 (strategies + agent-improvements scaffolding):
   `[step-2-2-4] strategies + agent-improvements scaffolding (T5 compliance)`.
9. After step 2.8 (critic gate2):
   `[step-2-2-4] critic gate2 report`. Then fix commits as above.
10. After step 2.9 (bootstrap verification):
    `[step-2-2-4] bootstrap verification passed (Part D)`.
11. After step 2.10 (Gate 2 AWAITING-APPROVAL):
    `[step-2-2-4] AWAITING-APPROVAL gate2 (5 experts + diffs + verification)`.
    Push. Pause.
12. After Phase 5 consolidation:
    `[decisions] ROY-AGENTS-BUILT — 6 agents + wiki v3 infra live (Шаг 2.2.4 complete)`.
    Push. Halt.

### Branch + push rules

- Branch: `claude/jolly-margulis-915d34`. Do not branch off. Do not
  rebase. Do not force-push.
- Push after every commit — Ruslan monitors via GitHub.
- If a pre-commit hook fails, fix the underlying issue and create a
  NEW commit. Do not `--amend`, do not `--no-verify`.

### Cost discipline

- `unset ANTHROPIC_API_KEY` before launch. Max-subscription only.
- No third-party APIs, no paid embeddings, no `Groq`/`OpenAI`
  fallbacks. Sub-agents inherit the same constraint — brief them
  explicitly in every Task call.
- Never mention `WebSearch` or `WebFetch` in any agent body.

### If stuck mid-work

- **Sub-agent extraction shallow** → spawn replacement with tighter
  brief + exact section anchors.
- **Two locks appear to conflict** → cite both, escalate as
  `design/AWAITING-APPROVAL-step-2-2-4-conflict-<id>.md`; do not
  resolve unilaterally.
- **Tier-1 file unexpectedly missing** → flag in critic report; use
  available data; do not invent.
- **API error / Internal Server Error mid-work** → commit whatever you
  have immediately (`[step-2-2-4] partial: <state>`), push, then
  retry. Do not let an outage waste completed work.
- **Ruslan unresponsive > 12 h on a gate** → pause; polish critic
  reports; do not push past the gate.

### Logging

Every Phase 1 extraction + every critic report is committed to
`raw/research/step-2-2-4-extractions/` and becomes part of the Ruslan
audit trail. Do not delete or rewrite them.

---

## 9. ANTI-PATTERNS FOR YOU SPECIFICALLY

- **Do not write generic agent content.** "The engineering expert
  values correctness" is weaker than "The engineering-expert §1b
  declares primary-alpha=artefact, secondary=[task, strategies-rule];
  §2 ontological-spine lists [drafted / reviewed / merged /
  superseded] as the artefact-alpha state sub-graph aligned with α-2
  Artefact; §3 critic activation trigger is `mode: critic` prompt
  prefix + UserPromptSubmit hook predicate `frontmatter.mode ==
  critic`; refusal fires if prefix and hook disagree." Be the second
  sentence, every time.
- **Do not skip the shared-protocols import stub.** If you copy any
  of §§1–8 of `swarm/lib/shared-protocols.md` into an agent file,
  the critic will flag it as a showstopper. The stub references. It
  does not repeat.
- **Do not exceed 2500 lines per agent file.** If a section is
  growing unbounded, tighten it — do not overflow into a second file.
- **Do not add a 6th expert.** The matrix is 5 × 4. If you think a
  6th is needed, escalate as AWAITING-APPROVAL — do not act.
- **Do not let any expert carry Write permission for `swarm/wiki/`.**
  The brigadier is the single wiki-writer per Q2. Experts return via
  Task draft under `mode: writing-support`.
- **Do not duplicate the swarm-alphas.** α-1..α-5 live exactly once,
  at `swarm/wiki/foundations/swarm-alphas.md` (D5). Agent files
  reference by section number, not content.
- **Do not re-open locks.** If you feel the urge to re-debate W-7 or
  Q3 or the 4-mode count, stop. Cite the locking doc and proceed.
- **Do not hallucinate citations.** If you cite §5.1 of master
  synthesis, the section must exist. Verify before committing. An
  honest `[verify]` is better than a fabricated anchor.
- **Do not let sub-agents drift into Tier 4.** No books. No web.
  Enforce in briefs. Refuse if a sub-agent asks.
- **Do not collapse Part A / Part B / Part C / Part D.** All four
  are mandatory. Merging Part C into Part B is a showstopper.
- **Do not write skill diffs as prose.** D8 specifies exact line
  ranges + before / after snippets. Apply as diffs, not as
  descriptions.
- **Do not create any symlink in step 2.6.** The README is the
  contract; the first real symlink is created only when the first
  skill is promoted through α-3 `learning → active`. Creating a
  symlink early invalidates the lint rule.
- **Do not push past gates.** Both gates require Ruslan approval.
- **Do not over-summarise.** A tl;dr at the top of an agent file is
  fine. A tl;dr replacing a mode rubric is not.
- **Do not touch the 14 legacy agents.** Read them for context only.
  Never edit, never rename, never move.
- **Do not touch `wiki/` v2.** The v2↔v3 bridge is the
  `cross-tree-ref` edge (D3) and the parameterised skills (D8).
  Nothing else.
- **Do not declare Phase A done prematurely.** Phase A is done when
  Phase 5 final consolidation commit is pushed and the
  `ROY-AGENTS-BUILT` file exists. Not before.

---

## 10. SUCCESS CRITERIA

You are done when **all 14 are met**:

1. ✅ `.claude/agents/brigadier.md` exists, ≤ 2500 lines, 11-section
   §5.1 skeleton + all six FPF §10.3 brigadier additions present.
2. ✅ `.claude/agents/{engineering,mgmt,systems,philosophy,investor}-expert.md`
   all exist, each ≤ 2500 lines, each carrying the FPF 8-block × 9-section
   structure with all E-1..E-11 enhancements and the §10.2 per-expert
   blocks.
3. ✅ Matrix 5 × 4 mode-switching implemented in every expert (soft
   prompt-prefix + hard UserPromptSubmit hook scaffold), with concrete
   activation triggers, predicates, refusal behaviour.
4. ✅ Every expert's §7 Shared Protocols is a ≤ 25-line import stub
   referencing `swarm/lib/shared-protocols.md` by section number. No
   duplication of protocol content.
5. ✅ Every Part B file on disk (B1..B13) — D1 tree, 9 templates,
   edge-types.md, swarm-alphas.md verbatim, overview/index/log,
   insights/README.md, meta/health.md, graph/edges.jsonl, shared-protocols.md,
   wiki-roots.yaml, 5 skill diffs applied, 3 skill exclusions
   documented, skills/README.md.
6. ✅ Every Part C file on disk (C1..C12) — 6 per-agent `strategies.md`
   + 6 `agent-improvements/<agent>-improvements.md`, each
   empty-but-structured per Sub-agent E's template.
7. ✅ `swarm/strategies/` does not exist (T5 violation prevented).
8. ✅ Part D bootstrap verification passes all 10 checks.
9. ✅ Both critic reports committed at
   `raw/research/step-2-2-4-extractions/critic-gate{1,2}.md`.
10. ✅ Both `AWAITING-APPROVAL-step-2-2-4-gate{1,2}-2026-04-23.md`
    committed, pushed, and Ruslan-approved.
11. ✅ Final consolidation commit
    `[decisions] ROY-AGENTS-BUILT — 6 agents + wiki v3 infra live (Шаг 2.2.4 complete)`
    pushed to `claude/jolly-margulis-915d34`.
12. ✅ Max-subscription discipline verified — zero API-key env-var
    strings under `.claude/agents/`, `swarm/lib/`, `swarm/wiki/`.
13. ✅ Legacy 14 agents + existing `wiki/` v2 tree untouched (diff
    against `HEAD~N` shows no changes under those paths).
14. ✅ 6 parallel sub-agent extractions preserved at
    `raw/research/step-2-2-4-extractions/{A..F}-*.md` for audit.

If any of the 14 is unmet, you are not done; iterate.

---

## 11. REFERENCES (for Ruslan's audit)

### Authoritative inputs (Tier 1)

- `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` (final consolidated, D1..D12, ~33K words)
- `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` (§5.1 brigadier, §5.2 expert, §5.3 modes, §5.5 wiki, §5.7 ops, §5.10 skills)
- `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` (E-1..E-18, α-1..α-5, Part 10 shopping list)
- `decisions/WIKI-V3-MECHANICS-2026-04-23.md` (Q1..Q9, R1..R8, T1..T5)
- `design/ROY-WIKI-V3-GOALS-2026-04-23.md` (W-1..W-12)
- `design/ROY-BUILD-LOGIC-2026-04-23.md` (file locations, Phase-A ops)
- `decisions/ROY-ALIGNMENT-2026-04-22.md` (5 × 4 matrix)

### Locked constraints (Tier 2)

- `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md` (Locks D1..D8)
- `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md` (Locks D9..D18)
- `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md` (Locks D19..D24)
- `CLAUDE.md` (per-agent memory 5-layer spec, v2 wiki conventions)
- `.claude/rules/global.md`

### Existing infrastructure (Tier 3, do not break)

- `.claude/agents/` (14 legacy files — enumerated in §3 Tier 3)
- `.claude/skills/` (11 existing skills — 5 D8 edits + 3 D8 exclusions + plan-day/close-day/focus untouched)
- `wiki/` (existing v2 — coexist, never mutate)

### Sibling prompts (stylistic kin, do not copy content)

- `prompts/step-2-1-master-synthesis-2026-04-22.md` (set the bar for deep prompts: sub-agent strategy, gates, success predicates)
- `prompts/step-2-2-3c-wiki-v3-architecture-spec-2026-04-23.md` (closest analogue: precise deliverable list, 2-gate protocol, critic brief)
- `prompts/meta-brief-step-2-2-4-agent-construction-2026-04-23.md` (this prompt's upstream brief)

### Output targets (this prompt produces, next session builds)

- `.claude/agents/brigadier.md`
- `.claude/agents/engineering-expert.md`
- `.claude/agents/mgmt-expert.md`
- `.claude/agents/systems-expert.md`
- `.claude/agents/philosophy-expert.md`
- `.claude/agents/investor-expert.md`
- `swarm/wiki/**` (per D1 ASCII tree, all Part B1..B8 files)
- `swarm/lib/shared-protocols.md`
- `.claude/config/wiki-roots.yaml`
- `.claude/skills/{ingest,ask,lint,consolidate,build-graph}.md` (5 diffs applied)
- `.claude/skills/{compile,search-kb,sweep-notion-bank}.md` (3 exclusion comments)
- `.claude/skills/README.md` (symlink convention)
- `agents/<6 agents>/strategies.md`
- `swarm/wiki/meta/agent-improvements/<6 agents>-improvements.md`
- `design/AWAITING-APPROVAL-step-2-2-4-gate{1,2}-2026-04-23.md` (audit trail)
- `decisions/ROY-AGENTS-BUILT-2026-04-23.md` (final consolidation)

### Branch

- `claude/jolly-margulis-915d34`

### Notion parents (for Ruslan navigation, not read by Claude)

- Parent page: https://www.notion.so/34a2496333bf817d93bff4cb66775587

---

## 12. FINAL NOTE

The 6 agent files you produce are the swarm. The
`swarm/lib/shared-protocols.md` is the runtime contract. The
`swarm/wiki/foundations/swarm-alphas.md` is the state language every
task flows through. The wiki-roots.yaml lets the skills coexist with
v2 without fratricide. The strategies scaffolding is where System
Prompt Learning accrues for the lifetime of Jetix.

Every line here becomes seed code that compounds for months. A
shallow §3 critic rubric becomes a critic that never flags the right
thing, for a year. A missing §1b ontological block becomes an expert
that silently misfires on scope boundaries, for a decade. A hand-wavy
§9 strategies.md format becomes evolution entries that drift into
noise, eroding the entire compounding premise of Jetix.

Write contracts, not commentary. Cite locks, not opinions. Specify
mechanisms, not aspirations. Treat the 1000% depth mandate as
binding. Ship commits frequently; the next API glitch is already
coming.

Begin with Phase 1: spawn the 6 parallel deep-read sub-agents in a
single message.

---
