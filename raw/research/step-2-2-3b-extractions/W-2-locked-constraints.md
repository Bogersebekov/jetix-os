---
sources:
  - design/ROY-WIKI-V3-GOALS-2026-04-23.md
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md (§5.5 + adjacent §5.4/§5.6/§5.7/§5.10)
  - design/ROY-BUILD-LOGIC-2026-04-23.md (§1–§4)
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Part 4, Part 10)
extracted_by: W-2
date: 2026-04-23
scope: locked constraints for Q1..Q9
---

# W-2 extraction — locked constraints + resolved mechanics

## A. Locked W-decisions (W-1..W-12)

All from `design/ROY-WIKI-V3-GOALS-2026-04-23.md §3`. Approved by Ruslan 2026-04-23.

- **W-1 — Multi-layer architecture, not monolithic.** Wiki v3 = multiple specialized layers co-located under `swarm/wiki/` with defined boundaries + cross-referencing.
  - Touches: Q1, Q3, Q9
  - Constraint: retrieval must cross layers; cross-refs are between named layers (themes/, brigadier/, agents/, meta/, tasks/, operations/, global/, skills/, insights/); `swarm/wiki/` is the v3 root (not `wiki/`).

- **W-2 — Brigadier has own Wiki.** Layer 2 (`swarm/wiki/brigadier/`) mandatory; offloads orchestration state from context window.
  - Touches: Q2, Q4
  - Constraint: brigadier is a writing domain in its own right (own subtree); task-scoped context population can pull from brigadier's own "how-to-solve-problems" / "how-to-decompose-tasks" subfolders.

- **W-3 — Books→Wiki distillation: brigadier seeds (Phase A), experts deepen (Phase B).**
  - Touches: Q1, Q6 (skills about how to read/distill books)
  - Constraint: theme-wikis Layer 1 are populated from curated books (Ousterhout, Brooks, Cagan, Grove, Meadows, Popper, Buffett, etc.); provenance must cite book sources in `raw/books-md/`.

- **W-4 — Agent-improvement Wiki is separate dedicated layer (Layer 4).**
  - Touches: Q2, Q6, Q8
  - Constraint: meta-improvement content does NOT live inside strategies.md or task artefacts; dedicated `swarm/wiki/meta/agent-improvements/` subtree. Brigadier sweeps periodically and applies via system-prompt edits.

- **W-5 — Two-level Compounding Engineering.** Level 1 per-agent CE (§2.1.1 master); Level 2 system-level CE (brigadier + protocols improve themselves). Brigadier Level-2 CE output → Layer 4.
  - Touches: Q6, Q8
  - Constraint: skill/rule learning happens at both levels; Layer 4 is the sink for Level-2 outputs; crazy-agent (Q8) is NOT the Level-2 mechanism — brigadier is.

- **W-6 — Long-horizon projects use git branches for versions.** Per-iteration branch + fork for variants + rollback via git checkout.
  - Touches: Q7
  - Constraint: no novel versioning system; branch names follow `roy/<project-id>/main`, `roy/<project-id>/iter-vN`, `roy/<project-id>/fork-<variant>` (explicit scheme hypothesized in §2 Layer 6 but still flagged open in §5).

- **W-7 — Two parallel task layers.** Layer α = task-knowledge Wiki ("how-to-solve"); Layer β = operational Wiki (activity log, iterations, rollback). Kept separate, not fused.
  - Touches: Q4, Q9
  - Constraint: task-scoped context population (Q4) targets Layer α; Layer β (`swarm/wiki/operations/<project-id>/`) has its own structure (iterations/vN/, decisions-log.md, rollback-points.md, forks.md).

- **W-8 — Workflow standard = FPF + versioning + deep Wiki + 2-level CE.** Every swarm work follows this standard.
  - Touches: all Q's indirectly (quality bar)
  - Constraint: no shortcut retrieval, no shortcut writeback; all answers to Q1..Q9 must satisfy FPF discipline (past-participle states, provenance) + 2-level CE.

- **W-9 — Skill learning as first-class Wiki layer (Layer 8).** Candidate → eval → golden-set → activation.
  - Touches: Q6
  - Constraint: `swarm/wiki/skills/` has 4 subdirs (active/, candidates/, learning/, usage/); skill learning is a formal pipeline, not ad-hoc.

- **W-10 — Crazy-agent / insights generation deferred (Layer 9 placeholder).**
  - Touches: Q8
  - Constraint: Phase A creates Layer 9 placeholder `swarm/wiki/insights/` but does not instantiate agent; activation trigger is Phase B+.

- **W-11 — Wiki = central cognitive infrastructure, not storage.**
  - Touches: all Q's (framing)
  - Constraint: retrieval/write/cross-ref mechanics must treat wiki as "new memory architecture" (individual + collective + theme + orchestration + meta + episodic + creative + skill memory). Not a file dump.

- **W-12 — 1000% depth requirement.**
  - Touches: all Q's (quality bar)
  - Constraint: every page, cross-ref, provenance tag must be deep. Affects Q1 (cannot settle for grep-only), Q6 (cannot settle for "append to strategies.md"), Q3 (cannot settle for plain wikilinks — typed edges expected).

## B. ROY-BUILD-LOGIC constraints (§1–§4)

- **§1.2 swarm/ top-level folder.** Swarm runtime data in `swarm/` (not `wiki/`). `swarm/wiki/` already sketched with `tasks/<id>/` subdirs (context/, artefacts/, decisions/, open-questions.md), `global/`, `concepts/`, `graph/edges.jsonl`, `_templates/`. Touches Q9 (v2 `wiki/` vs v3 `swarm/wiki/` already structurally separated).

- **§1.3 what NOT touched.** `wiki/` top-level (existing Karpathy v2) NOT touched; `knowledge-base/` in migration; `.claude/agents/*.md` legacy untouched. Touches Q9: v2 `wiki/` must coexist with v3 `swarm/wiki/`, not be overwritten.

- **§2.1 Layer 1 Task tool PRIMARY.** Brigadier is single caller; experts spawn as sub-agents via Task. Touches Q2: cells return artefacts to brigadier, never write wiki directly.

- **§2.2 Layer 2 stigmergic wiki SHARED STATE.** Single-writer rule Phase A: only brigadier commits to `swarm/wiki/`. Provenance frontmatter mandatory: `source`, `captured_by`, `captured_date`, `task_id`, `commit_sha`. Touches Q2 (resolves direction: brigadier-only writes in Phase A) and Q3 (provenance pointers to paths).

- **§2.3 Layer 3 mailbox JSONL FALLBACK.** Minimized Phase A; stigmergic through wiki = 95% coordination. Touches Q2 (fallback only).

- **§3 single tmux session, brigadier as entry.** One task = one session = one git audit trail. Brigadier's context window holds orchestration state across turns; offloads to wiki regularly. Touches Q4 (brigadier does context population in-session) and Q8 (single-session ⇒ crazy-agent activation is out-of-band, not inside task session).

- **§4 task-scoped wiki assembly (core concept).** Wiki assembled under specific task; layers stack as tasks accumulate. §4.2 layering: brigadier initializes `swarm/wiki/tasks/T1/`, populates `context/` with domain-filtered slice from (a) Private Library books, (b) `decisions/`, (c) 24 Locks subset applicable to T1, (d) previous relevant global learnings. §4.3 compound effect: after T1, global wiki += learnings, T2 gets richer baseline. Touches Q4 directly. §4.4 EXPLICITLY OPEN: manual brigadier vs HippoRAG-PPR, promotion rules, retention, fusion heuristics — ALL deferred to Шаг 2.2.3 (this step).

## C. MASTER-SYNTHESIS §5.5 wiki protocol

§5.5 already partially resolves multiple Q's. Summary:

**§5.5.1 Filesystem layout** — inherits from CLAUDE.md wiki v2: `wiki/` root with `index.md`, `log.md`, 9 entity dirs (concepts/entities/sources/topics/ideas/experiments/claims/summaries/foundations/), `niches/` (per-agent symlinks), `comparisons/` (/ask output), `drafts/` (in-flight cell outputs), `proposals/` (brigadier decomposition artefacts), `_templates/`, `graph/edges.jsonl` (9 typed edge types). NOTE: §5.5.1 uses `wiki/` root, not `swarm/wiki/` — potential tension with W-1/BUILD §1.2 (see Tensions section F).

**§5.5.2 Single-writer rule (Phase A).** All writes flow through brigadier; cells return artefact-to-write, brigadier commits. Prevents AP-15 (handoff failures). Phase B TBD: switch to CRDT if contention (ALIGN §10). → **Directly resolves Q2 for Phase A.**

**§5.5.3 Provenance format.** YAML frontmatter mandatory fields: `id, title, date, type (concept|entity|source|topic|idea|experiment|claim|summary|foundation), pipeline (raw|ingested|compiled|linted|ready), sources[{path, range, quote}], tier (core|partner|member|public), produced_by (agent-mode or human), cycle_id`. Inline citation format: `[src:path#section]`. → **Directly resolves Q3 partially: frontmatter+inline format specified; typed-graph edges exist but edge-type vocabulary not enumerated here.**

**§5.5.4 Tier enforcement (Lock 13, Lock 3).** `tier` field authoritative; cells check tier on every `wiki_read` via MCP server; surface outputs cannot include stricter-tier content; outbound artefacts pass tier-check hook. Constrains Q2 (write) and Q1 (read filtering).

**§5.5.5 Compound-step provenance gate.** On write to `agents/<expert>/strategies.md`, entry must cite ≥1 source artefact (incident file + commit hash, or verbatim source + line range). No-provenance entries rejected. AP-18 prevention. → **Directly constrains Q6: skill/rule writeback requires provenance gate.**

**Adjacent sections touching Q's:**

- §5.6.2 PostToolUse hooks: `/lint` on every wiki write; reject if frontmatter invalid. Session log append to mailbox. → constrains Q2 (validation on write).
- §5.7 Tool matrix: brigadier has Task-spawn + Bash-write + HITL external-sends; experts are read-heavy + scoped Write only to `wiki/drafts/<task-id>-*` or `wiki/foundations/<domain>/*`. MCP wiki tools: brigadier read/write, experts read-only. → locks-in single-writer enforcement at permission layer (Q2).
- §5.10.1 orchestration skills (plan-cycle, invoke-cell, integrate-outputs, gate-decision, compound-cycle, close-cycle). §5.10.2 wiki skills: /ingest /ask /lint /consolidate /build-graph. §5.10.3 mode-skills per 20 matrix cells registered with `when_to_use`. → constrains Q6 (skill layer already has baseline registry; Phase A adds these).

## D. FPF-ENHANCEMENT Part 4 + Part 10

**Part 4 — Swarm alphas (α-1..α-5):**

- **α-1 Task** — submitted→intaked→decomposed→dispatched→integrated→gated→approved→compounded→archived (+ refused/rejected branches). Brigadier owns.
- **α-2 Artefact** — drafted→reviewed→revised⇄reviewed→accepted→referenced→superseded/retired. Producer owns drafts; brigadier owns accept. Acceptance needs frontmatter validity (source, captured_by, captured_date, task_id, commit_sha) + Conformance Checklist.
- **α-3 Strategies-Rule** — proposed→active→validated⇄active→tombstoned. 4-part DRR (context/decision/alternatives/review-checkpoint). Validated ✓/✗≥3:1 over ≥10 uses; tombstoned <1:1 or Ruslan-retire. Meta-agent does tombstoning audit; brigadier writes.
- **α-4 Cycle** — opened→running→integrating→gated→compounded→closed→tombstoned.
- **α-5 Direction** — hypothesized→under-validation→validated→activated→scaled→plateaued→invalidated→dropped→archived. **Human-owned**; AI tracks state only. Phase A lightweight (state enum); Phase B NQD-CAL+E/E-LOG+BLP deferred.

Part 4 touches: Q2 (α-2 Artefact acceptance via brigadier), Q6 (α-3 Strategies-Rule is the formal skill-learning pipeline with state-graph), Q5 (α-2 `superseded`/`retired` states give staleness vocabulary; α-3 `tombstoned` via ✓/✗ ratio gives quantitative staleness signal).

**Part 4.3 Hard AI-strategizing constraint** — AI cannot invent-mode strategize; adapt-mode requires HITL approve; only 1:1 method-known cells full auto. Constrains Q8 (crazy-agent "insights" are candidate-generation, NOT decisions).

**Part 10 — Preparatory artefacts:**

- **10.4** Must create `swarm/wiki/foundations/swarm-alphas.md` (α-1..α-5 full state graphs + movers + acceptance). Phase-A: α-1..α-4 machine-tracked; α-5 human-owned.
- **10.5** Must create `swarm/lib/shared-protocols.md` with: wiki write protocol (BUILD §2.2 provenance), structured output schema, HITL escalation protocol, cross-cell-reference protocol (read wiki, never call cell), tool-permission self-check, `mode: writing-support` clause (E-10), tool-language abstractions.
- **10.6** Clarifications: α-5 Phase A lightweight default; brigadier executor = Opus 4.7 default.
- **10.8** Success predicate: `swarm/wiki/foundations/swarm-alphas.md` must exist; `swarm/lib/shared-protocols.md` must exist and be imported from each expert's §7; no Tier-4 book read during Phase A construction.

Part 10 touches: Q2 (single-writer + cross-cell-reference protocol = read wiki never call cell), Q3 (A.14 typed edges used in cross-refs per 10.8 item 5), Q6 (α-3 DRR format = skill/rule format), Q9 (`swarm/wiki/foundations/` structure declared).

## E. Fully-resolved vs Partially-resolved vs Open matrix

| Q   | Already resolved (where) | Partially resolved | Open (needs answer) |
|-----|--------------------------|--------------------|---------------------|
| Q1 Retrieval primary | — | W-3 (books seed via brigadier); §5.5.1 filesystem-grep baseline implicit (existing /ask, /ingest) | W-5 open Q explicit: filesystem grep / semantic embeddings / graph traversal / HippoRAG PPR — which default |
| Q2 Write serialization | §5.5.2 (brigadier-only Phase A); §5.7 tool matrix enforces; BUILD §2.2 single-writer rule; §5.5.5 provenance gate; §5.6.2 /lint PostToolUse | Phase B CRDT switch condition (contention observed) mentioned but not specified | Phase B handoff (CRDT vs per-layer owners) not specified; W-4 meta-layer writer not explicitly assigned |
| Q3 Cross-reference format | §5.5.3 YAML provenance (sources[] + inline [src:path#section]); Part 10.8 "A.14 typed edges used in cross-refs"; edges.jsonl with "9 typed edge types" mentioned | Edge-type vocabulary hinted (9 types) but not enumerated here | Enumerated edge-type list; wikilinks vs HippoRAG vs Obsidian style final choice; how typed edges interact with inline [src:] citations |
| Q4 Task-scoped context population | W-7 (two layers α/β separated); BUILD §4.2 list of 4 sources (Private Library, decisions/, 24 Locks subset, global learnings) | Enumeration of sources given; brigadier is populator | Manual brigadier vs automatic retrieval (HippoRAG-PPR, tag-based, keyword-based, domain-expert lists) — BUILD §4.4 EXPLICITLY defers to Шаг 2.2.3 |
| Q5 Staleness detection | α-2 states (superseded/retired); α-3 tombstoning via ✓/✗<1:1 or explicit retirement; AP-3 (wiki rot) + AP-27 (KB rot) flagged as known failures | State vocabulary available but signals not unified | Time-based / version-based / contradiction-based / manual-tag / combination — which triggers which transition; who runs the sweep (meta-agent mentioned for α-3 only) |
| Q6 Skill learning pipeline | W-9 (Layer 8 candidate/active/learning/usage); α-3 DRR format + ✓/✗ threshold; §5.5.5 compound provenance gate; §5.10 skill roadmap (orchestration + wiki + mode skills); Compound step writes to strategies.md | Pipeline stages named (candidate→eval→golden-set→activation) but who owns which transition not fully specified | Concrete formal pipeline ownership (meta-agent does tombstoning; who does eval, golden-set, activation?); integration between α-3 and Layer 8 layout |
| Q7 Git branches naming | W-6 (git branches = version mechanism); §2 Layer 6 hypothesized scheme: `roy/<project-id>/main`, `roy/<project-id>/iter-vN`, `roy/<project-id>/fork-<variant>` | Scheme hypothesized but flagged §5 open | Final approval of scheme; interaction with current `claude/jolly-margulis-915d34` branch; per-task vs per-project granularity |
| Q8 Layer 9 crazy-agent activation | W-10 (deferred Phase B+); §1.7 future idea; Part 4.3 (AI cannot invent-mode strategize — crazy-agent outputs are candidates, not decisions) | Layer 9 placeholder location declared | Phase B trigger condition (N cycles? manual? eval-threshold?); who reviews candidates (critic mode?); promotion mechanism |
| Q9 Existing wiki/ v2 vs swarm/wiki/ v3 | W-1 (v3 under `swarm/wiki/`); BUILD §1.3 (v2 `wiki/` NOT touched); §5.5.1 inherits v2 layout into v3 (same 9 entity types, templates, edges.jsonl structure) | Structural coexistence locked; content migration not specified | Migrate / coexist / merge decision (goals doc §5 EXPLICIT open Q); how v2 content becomes v3 theme-wiki seed; whether `knowledge-base/` (in migration) lands in v2 or v3 |

## F. Tensions / contradictions noticed in locked material

1. **Wiki root location.** Master synthesis §5.5.1 describes layout rooted at `wiki/` (v2 top-level). BUILD §1.2 + W-1 put v3 under `swarm/wiki/`. §5.5.1 may have been drafted before `swarm/` decision — the template content is reusable but the root path differs. Flag for resolver: which root governs Phase A cell writes? (W-1 and BUILD §1.2 are later and more specific → likely win, but §5.5.1 entity-type layout is what cells would inherit.)

2. **Single-writer scaling vs multi-layer architecture.** W-1/W-4 define 9 layers; §5.5.2 mandates single-writer brigadier for Phase A. Goals doc §5 explicitly flags "scales ли single-writer при увеличении layers?" — tension acknowledged but unresolved. Q2 resolver must note this.

3. **Strategies.md location.** Master synthesis §5.5.5 writes to `agents/<expert>/strategies.md` (per CLAUDE.md per-agent layer); BUILD §1.2 puts strategies at `swarm/strategies/<expert>.md`; W-4 introduces `swarm/wiki/meta/agent-improvements/<agent>-improvements.md` as a meta layer separate from strategies. Three distinct files/locations for related content. Resolver must clarify.

4. **Skill registry location.** §5.10.3 registers mode-skills as Claude Code Skills (presumably `.claude/skills/`); W-9 declares Layer 8 `swarm/wiki/skills/`. Are these the same registry or parallel? If parallel, which is authoritative?

5. **Mailbox deprecation vs swarm alpha tracking.** BUILD §2.3 minimizes mailbox to edge-cases; FPF Part 4 α-1 Task state-transitions may benefit from mailbox events. Tension between "stigmergic-first" and "state-machine tracking" implementations.

## G. Additional locked constraints not tied to specific Q

- **Context-window discipline.** BUILD §3.6: brigadier offloads to wiki + new session per big task. Mechanics inflating brigadier context blocked.
- **Executor lock.** FPF 10.6: brigadier = Opus 4.7 (1M). Respect Rule-of-4 / context-rot (AP-7, AP-8).
- **Max-subscription discipline.** §5.7.3: no `ANTHROPIC_API_KEY`. No API-billed embeddings (Q1 impact — local-only if semantic).
- **24 Locks compliance.** §5.7.2 deny-list; §5.5.4 tier enforcement (Lock 13). Any wiki mechanism must pass Part 9 §9.8 table.
- **Frontmatter mandatory.** CLAUDE.md + FPF E-1/E-16: `granularity:` field (jetix-business / jetix-life-os / jetix-shared / task-scoped).
- **Past-participle state names.** FPF 10.8 item 4: all alpha states past-participle; Q5/Q2/Q6 must use this convention.
- **Conformance Checklist.** FPF E-3: every critic artefact carries it; Q2 gate integrates.
- **Reversibility.** BUILD §1.4: `rm -rf swarm/` must restore pre-swarm state; no v3→legacy cross-dependencies.
- **No Tier-4 book read Phase A** (FPF 10.8 item 8). Seed (W-3) limited to Tier 1-3.
- **Russian prose / English code** (CLAUDE.md rule 7). Frontmatter + edge-types in English.
