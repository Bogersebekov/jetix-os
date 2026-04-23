---
id: context-gamma-wiki-v3
title: "Phase 1 γ — Wiki v3 architecture vs on-disk state"
type: context-extraction
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: subagent-gamma
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: rubric-based
niche: meta
sources:
  - {path: "design/ROY-WIKI-V3-GOALS-2026-04-23.md", range: "1-537"}
  - {path: "decisions/WIKI-V3-MECHANICS-2026-04-23.md", range: "1-848"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "1-4730"}
  - {path: "swarm/wiki/foundations/swarm-alphas.md", range: "1-181"}
  - {path: "swarm/lib/shared-protocols.md", range: "1-274"}
  - {path: "swarm/wiki/_templates/edge-types.md", range: "1-136"}
  - {path: "swarm/wiki/meta/health.md", range: "1-275"}
  - {path: "swarm/wiki/graph/edges.jsonl", range: "1-4"}
  - {path: "swarm/wiki/graph/cross-tree.jsonl", range: "1-4"}
  - {path: ".claude/config/wiki-roots.yaml", range: "1-45"}
  - {path: ".claude/skills/ingest.md", range: "1-30"}
  - {path: ".claude/skills/ask.md", range: "1-30"}
  - {path: ".claude/skills/lint.md", range: "1-25"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/open-questions.md", range: "1-26"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/manifest.yaml", range: "1-60"}
---

# Phase 1 γ — Wiki v3 architecture vs on-disk state

## TL;DR

Wiki v3 bootstrap (Шаг 2.2.4 Phase 2.1) has landed skeletally:
all 9 layers + global spine directories exist
[`find swarm/wiki`], all 10 templates are in place, `foundations/swarm-alphas.md` (181 L)
and `swarm/lib/shared-protocols.md` (274 L) are committed as accepted
artefacts, and 5 of 6 wiki skills carry the `$WIKI_ROOT` preamble
[grep WIKI_ROOT in .claude/skills/]. D1–D12 are specified in
unprecedented depth (4730 L) but most D7–D12 operational surfaces are
conceptual — there are no populated spine entries, no edges, no
candidate skills, no drafts, no active α-1/α-4 closed cycles, no
`/lint` hook wiring, no Tier-3 typed-BFS executor and no
`closed_cycles_count`-incrementing mover code. The architecture is a
contract, not a running machine. Highest-leverage 2× surfaces:
Tier-3 typed-BFS executor, provenance-gate automation, α-4 close
automation, niche-symlink population, theme-wiki seeding.

## D1..D12 deliverable status table

| Deliverable | Spec path:line-range | On-disk evidence (path + status) | Ratio | Gap |
|---|---|---|---|---|
| D1 — 9-layer dir layout + global spine | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:105-556` | `swarm/wiki/{foundations,themes,brigadier,agents,meta,tasks,operations,global,skills,insights}/` all present + `{concepts,entities,sources,topics,claims,ideas,experiments,summaries,comparisons,drafts,proposals,niches,_archive,_templates,graph}/` spine all present [`find swarm/wiki -type d`]; 27 top-level dirs | 0.95 | Leaf dirs largely empty (`themes/*/concepts/`, `brigadier/how-to-*/`, `niches/meta/`, all empty); only structural skeleton, no populated content |
| D2 — Per-layer frontmatter templates | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:558-876` | Dual-axis `pipeline`/`state` encoded in the 10 template files under `swarm/wiki/_templates/` [`ls swarm/wiki/_templates/`]; `meta/health.md` singleton carries 5 live counters per D10 spec | 0.7 | Per-layer additions (`theme`, `bucket`, `expert`, `project_slug`, `skill_slug`, `insight_state`, `phase_a_lock`) not yet appearing in any real page because no real pages exist; `/lint` doesn't enforce the D2 cross-layer schema on disk |
| D3 — 12-type edge enum + from×to matrix | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:879-1248` | `swarm/wiki/_templates/edge-types.md` (136 L) carries full enum + matrix [`Read`]; `swarm/wiki/graph/edges.jsonl` exists but contains zero data records (4 L, all are # comments) [`wc -l graph/edges.jsonl` + `cat`] | 0.55 | Enum specified but no edges populated — zero `extends`, zero `supports`, zero `contradicts`, zero `derived_from`, zero `part_of`; Tier-3 BFS executor not implemented; `/build-graph` still reads v2 `wiki/` not `swarm/wiki/` by default |
| D4 — 9 entity-type templates | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:1251-1882` | All 10 files present in `swarm/wiki/_templates/` (9 entity types + edge-types) [`ls -la swarm/wiki/_templates/`] | 0.9 | Templates exist but are never consumed by `/ingest` to produce a page — no `concepts/*.md`, no `claims/*.md`, no `sources/*.md` on disk; template→page pipeline operationally untested |
| D5 — 5 swarm-alpha state machines | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:1885-2406` | `swarm/wiki/foundations/swarm-alphas.md` (181 L) written with α-1..α-5 states + transitions + ASCII diagrams + predicates [`Read`] | 0.65 | File exists but is **documentation only** — α-1 `submitted→intaked→decomposed→dispatched→integrated→gated→approved→compounded→archived` transitions have no programmatic mover; `closed_cycles_count` stays `0` because no code increments it; α-2 `tombstoned` predicates depend on `/lint` that doesn't run automatically |
| D6 — shared-protocols.md runtime contract | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:2409-2971` | `swarm/lib/shared-protocols.md` (274 L) carries all 9 sections [`Read`]; agents import by §7 stub; verb dictionary + role_tool_matrix present | 0.8 | Provenance gate §5.5.5 (§6.3) is narrative pseudocode, no validator script; tool-permission self-check lives in prose only; SessionStart hook for `$ANTHROPIC_API_KEY` described but not installed in `.claude/` |
| D7 — `.claude/config/wiki-roots.yaml` | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:2973-3131` | `.claude/config/wiki-roots.yaml` (45 L) committed with `schema_version: 1`, `wiki_root_v3: swarm/wiki`, 5 in-scope + 3 excluded skills [`Read`] | 1.0 | Fully landed; the one gap is that `resolve_wiki_root()` pseudocode has no implementation — skills use `${WIKI_ROOT}` string substitution in prose, not a resolved runtime var |
| D8 — 5 skill edit diffs | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:3134-3447` | `/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph` each carry the 9-line `$WIKI_ROOT` preamble [grep: 12–16 hits per file]; `/compile`, `/search-kb`, `/sweep-notion-bank` untouched as spec'd | 0.85 | Prose updated but skills still behave like v2 — there is no runtime code; `${WIKI_ROOT}` appears in markdown prose only, so actual filesystem targets depend on Claude Code's string interpretation at invocation time |
| D9 — `.claude/skills/` symlink convention | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:3449-3665` | No symlinks exist in `.claude/skills/` yet [`ls -la .claude/skills/` shows 8 regular files + 3 v2 dirs]; `swarm/wiki/skills/active/` is empty | 0.0 | Fully latent — no skill has been promoted yet; α-3 `validated` transition is entirely theoretical |
| D10 — `meta/health.md` skeleton | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:3668-4015` | `swarm/wiki/meta/health.md` (275 L) committed with 8 sections + 5 live counters (all `0`/`null`) [`Read`] | 0.7 | Dashboard skeleton is pristine; no FPAR computation, no `/lint` scheduled cron, no meta-agent weekly sweep — every counter will remain at bootstrap until wired |
| D11 — Q6 skill activation rubric | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:4019-4333` | Specification only; no candidate skills in `swarm/wiki/skills/candidates/`, no `golden-set.jsonl`, no `usage/*.jsonl` [`find swarm/wiki/skills`] | 0.1 | Zero skills have entered the pipeline; anti-T3 clause (§11.8) has nothing to enforce |
| D12 — Strategies trio collapse (T5/R6) | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md:4336-4580` | Venue (a) `agents/<expert>/strategies.md` — I did not verify these exist at project root; Venue (c) `swarm/wiki/meta/agent-improvements/` — 8 files present (6 per-expert incl. brigadier + `system-level-improvements.md` + `emergent-insights.md`) [`ls swarm/wiki/meta/agent-improvements/`]; Venue (b) `swarm/strategies/` correctly absent | 0.6 | `brigadier-improvements.md` exists on disk even though D1 §1.4 lists only 7 bootstrap files (5 experts + system + emergent) — spec drift already; sync rule (§12.4) lacks executor |

## Q1..Q9 lock status

| Q | Principle | Operational mechanism present? | Gap |
|---|---|---|---|
| Q1 | 4-tier retrieval (direct→index+grep→typed-BFS→long-context fallback) | Tier 1 (Read) + Tier 2 (index.md stub exists, grep available) operational. Tiers 3 & 4 absent. | `swarm/wiki/graph/edges.jsonl` empty → Tier-3 BFS has nothing to traverse. No typed-BFS implementation in `/ask`. Tier-4 "long-context fallback" has no niche-scoped budget enforcer. |
| Q2 | Single-writer brigadier | Permission matrix encoded in D6 §6.6.3 (prose); D1 §1.3 table asserts rule. | Not mechanically enforced: nothing blocks a cell writing outside `drafts/`. No pre-write hook. Brigadier's §5.5.5 gate is manual. |
| Q3 | Triple-channel cross-refs (YAML `related[]` + inline `[[type/slug]]` + `edges.jsonl`) | Template stubs present; `/lint` check #9 specified. | `/lint` does not run. No page on disk actually has all three channels instantiated. The consistency rule is un-executed. |
| Q4 | Hybrid auto-pull task context (niche→decisions→24-Locks→typed-BFS→books, 20K cap) | Manifest YAML exists for the current task [`swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/manifest.yaml` 6406 B] and shows Tier-1 corpus list with token estimates. | Manifest is brigadier-hand-written, not auto-pulled. No BFS seeding. No book-excerpt auto-include. No priority-based digest compaction. |
| Q5 | 5-signal /lint orchestration (structural / α-2-α-3 state / confidence×age / contradiction / time-based) | 11 checks documented in `/lint` prose [grep `/lint` description]. | `/lint` has zero automated runs. No PostToolUse hook wired. No weekly cron. `meta/health.md`'s `lint_findings_log` remains empty scaffold. |
| Q6 | α-3 skill pipeline (candidates→learning→active→usage + 4-state α-3) | Dir scaffold exists (`swarm/wiki/skills/{candidates,learning,active,usage}/`). | All 4 dirs empty; no DRR, no golden-set, no usage JSONL, no `.claude/skills/` symlink. Activation rubric (D11) untested. |
| Q7 | `roy/<project-slug>/{main,iter-vN,fork-X,exp-Y}` git branches | Spec'd; current branch is `claude/jolly-margulis-915d34`. | Zero `roy/*` branches. `swarm/wiki/operations/` empty — no 1:1 branch↔operations mapping exercised. |
| Q8 | Layer-9 3-AND trigger (≥50 α-4 closed + ≥2 themes×50 + Ruslan ack) | `swarm/wiki/insights/README.md` encodes the 3-AND text; `meta/health.md` §2 + §3 carry `closed_cycles_count` + `cross_theme_refs_count` counters. | Counters frozen at `0`; no increment path. `/lint` check #10 (reject non-README writes under insights/) not running. |
| Q9 | v2/v3 coexist + parameterize via `$WIKI_ROOT` | `.claude/config/wiki-roots.yaml` landed; skills carry preamble referring to it. | `$WIKI_ROOT` is a pseudo-variable in prose, not a runtime resolution. No test in place to verify a skill invocation with `WIKI_ROOT=wiki` actually diverts writes to v2. |

## R1..R8 lock status

| R | Decision | Operational mechanism present? | Gap |
|---|---|---|---|
| R1 | Accept `roy/<project-slug>/{tag}` branch schema | Defaulted Yes; no R1-specific artefact needed on disk. | No `roy/` branches exist. Schema untested. |
| R2 | 4-tier filesystem+typed-BFS retrieval Phase A, PPR deferred | Defaulted Yes; R2 is about R1 of Q1. | Typed-BFS not implemented (same as Q1 gap). PPR placeholder condition "revisit at >2K edges OR FPAR<0.8" has no measurement wiring. |
| R3 | Parameterize + coexist (Q9) | `.claude/config/wiki-roots.yaml` landed. | (same as Q9) — execution layer missing. |
| R4 | Q6 owners (propose=anyone, draft=brigadier/expert, eval=brigadier, audit=meta-agent, retire=meta-agent/Ruslan) | Owner table in D11 §11.7 and D6 §6.2.2. | No roles exercised. Meta-agent exists as a `.claude/agents/` file but has not run a skill audit. |
| R5 | Q8 3-AND + Ruslan-gated Layer-9 activation | README.md encodes it. | No gate file ever written; trigger never evaluated. |
| R6 | Drop `swarm/strategies/` (T5 collapse) | `swarm/strategies/` correctly absent from `ls swarm/`. | `/lint` check #11 (flag stale `swarm/strategies/`) not running. |
| R7 | 12-type edge enum | `_templates/edge-types.md` enumerates all 12 with from×to matrix. | No edges written. Enum untested. |
| R8 | Accept 5 T-tensions as specification-level | All 5 addressed inline in spec. | T2 ("cross_theme_refs_count == 0 after 20 cycles → re-eval") unmeasurable because counter frozen at 0. |

## T1..T5 lock status

| T | Tension | Operational mechanism present? | Gap |
|---|---|---|---|
| T1 | `edges.jsonl` asymmetry: 3 files (v2, v3, cross-tree) | Both `swarm/wiki/graph/edges.jsonl` + `swarm/wiki/graph/cross-tree.jsonl` exist, comment-only; v2 `wiki/graph/edges.jsonl` untouched. | `/build-graph --tree {v2|v3|both}` flag specified only in prose. No executor. |
| T2 | Niche-filtered tasks may never generate cross-theme refs → Q8 trigger #2 may never fire | `meta/health.md` §3 carries a "20-cycle re-eval" note; `cross_theme_refs_count` counter frozen at 0. | No counter-update path. |
| T3 | Activation (golden-set binary) vs validation (usage-driven) rubric tension | D11 §11.8 anti-T3 clause; explicit Gate-I + Gate-II predicates. | No skill has gone through either gate. |
| T4 | Edge-type enum has empty types (`inspired_by`, `tested_by`, `invalidates`, `supersedes`) | Acceptable per spec; `/lint` per-type count surfaced in health. | Not yet surfaced because no edges. |
| T5 | Strategies trio collapse | Verified: `swarm/strategies/` absent; Venue (a) + (c) retained. | Sync rule §12.4 (Level-1 → Level-2 promotion) lacks executor. |

## W1..W12 goal status

| W | Goal | Operational mechanism present? | Gap |
|---|---|---|---|
| W-1 | Multi-layer architecture (9 layers) | All 9 layers present as dirs. | 8 of 9 layers empty of canonical content. |
| W-2 | Brigadier has own Wiki (Layer 2) | `swarm/wiki/brigadier/{how-to-solve-problems, how-to-manage-agents, how-to-decompose-tasks, orchestration-state}/` + README.md. | All 4 buckets empty. Brigadier continues to hold coordination state in system prompt + session context. |
| W-3 | Books → Wiki distillation | `swarm/wiki/foundations/<theme>/README.md` placeholders + `themes/<theme>/README.md` scaffolds; Private Library at `raw/books-md/` untouched per Tier discipline. | Zero book excerpts distilled. No `sources/book-*.md` pages. Phase B fuel. |
| W-4 | Agent-improvement layer (shared meta) | `swarm/wiki/meta/agent-improvements/` with 8 files (1 per expert + brigadier + system-level + emergent). | Each file is frontmatter + narrative only; no α-3 DRR entries. Brigadier sweep never run. |
| W-5 | Two-level Compound Engineering (per-agent + system-level) | Level-1 = `agents/<expert>/strategies.md` (not verified to exist); Level-2 = meta/agent-improvements/. | No CE loop has fired. |
| W-6 | Git branches as version control | No `roy/*` branch exists. | Zero iterations, zero forks, zero rollback points. |
| W-7 | Two parallel task layers (task-knowledge α + operational β) | `swarm/wiki/tasks/<task-id>/` (Layer α) and `swarm/wiki/operations/<project-slug>/` (Layer β) both scaffolded. | Only 1 task instantiated (the current cycle); `operations/` empty. |
| W-8 | Workflow = FPF + versioning + deep wiki + 2-level CE | Spec encodes all 4. | No workflow execution has happened. |
| W-9 | Skills first-class | `swarm/wiki/skills/{candidates,learning,active,usage}/` + D11 rubric. | Zero skills populated. |
| W-10 | Crazy-agent / Layer-9 deferred Phase B+ | `swarm/wiki/insights/` scaffold-only. | `/lint` check #10 not running; lock depends on manual discipline. |
| W-11 | Wiki as central cognitive infrastructure (not storage) | `overview.md` + `swarm-alphas.md` + `shared-protocols.md` framed this way. | Without operational retrieval + write loops, wiki currently behaves as dormant storage, not cognition. |
| W-12 | 1000% depth | Spec is 4730 L; D1 §1.3 permission table, D3 12-enum matrix, D5 state diagrams meet depth bar. | Depth is in the spec; depth in the **artefacts** is near-zero. |

## Retrieval stack observations (Q1 4-tier)

- **Tier 1 — Direct path lookup.** Fully operational (Read tool).
  Native to Claude Code. No work needed.
- **Tier 2 — Index + niche/topic filter + grep.** `swarm/wiki/index.md`
  exists (63 L) listing foundations/templates/meta/layer-READMEs but
  **no spine entries** yet [`Read swarm/wiki/index.md`]. Niche
  filtering: `niches/<n>/` dirs exist but are **all empty** — no
  symlinks populated [`ls -la swarm/wiki/niches/meta`]. So Tier-2
  falls back to plain grep over `swarm/wiki/**/*.md`.
- **Tier 3 — Typed-BFS over `graph/edges.jsonl`.** Critical gap.
  `swarm/wiki/graph/edges.jsonl` is **4 lines, all `#` comments**
  [`cat swarm/wiki/graph/edges.jsonl`]. No executor exists anywhere
  in the repo for typed-BFS. The spec mandates "Top-k=10, max 2 hops,
  edge-type filter per task" but there's no Python/bash/bash-function
  that implements this. `/ask` skill carries only prose referring to
  Tier-3. This is the #1 highest-leverage implementation gap.
- **Tier 4 — Long-context fallback.** Spec says "bounded to current
  niche dir, not full wiki." The bounding depends on niche-symlink
  population (niches/ all empty) so fallback is effectively "grep
  whole `swarm/wiki/`." No token-budget enforcer.

**What's missing for Tier-3:**
1. A deterministic BFS implementation (could be a ~60-line Python
   script invoked from `/ask` via Bash — no SDK needed).
2. A seed-selection rule: how to pick the starting nodes from
   task.keywords in `manifest.yaml`.
3. Edge-type allowlist per query class (e.g., exclude `contradicts`
   unless contradiction-scan mode).
4. Top-k truncation + deduplication.
5. Output shaping: result pages pulled + tokens accounted against the
   20K cap per Q4.

**Tier-4 fallback bounds that are missing:**
- Per-niche token budget.
- Stop-early heuristic when Tiers 1-3 returned ≥3 acceptable results.
- Dedup vs Tier-2 results.

## Edge enum observations (D3, 12-edge types)

- **`swarm/wiki/graph/edges.jsonl`:** 4 lines, all `#` comments, zero
  data records [`wc -l`]. Bootstrap empty.
- **`swarm/wiki/graph/cross-tree.jsonl`:** 4 lines, all `#` comments,
  zero v3→v2 bridge edges [`wc -l`].
- **`swarm/wiki/graph/communities.md` + `summaries.md`:** 11 L each,
  likely header stubs; `/build-graph` has never run against v3.
- **Enum spec (`_templates/edge-types.md`, 136 L):** all 12 types
  fully documented with cardinality / directionality / inverse /
  allowed from×to / example / lint rule. Matrix at §3.3 covers all
  layer pairs.
- **v2 baseline** `wiki/graph/edges.jsonl`: spec says 572 records; I
  did not re-count but the audit figure quoted in mechanics Part 2
  §Q3 + D3 §3.4 seems solid (233 `part_of`, 219 `derived_from`, 84
  `supports`, 35 `extends`, 1 `contradicts`).
- **`addresses_gap` dropped:** `_templates/edge-types.md` footnote
  confirms per critic-gate1 H4.
- **No `alpha-ref`, `layer-ref`, `cross-tree-ref` edges on disk** —
  these are the v3-born types; zero exercise.

## Provenance gate §5.5.5 observations

**Status:** conceptual, not operationally wired.

- **Spec.** `swarm/lib/shared-protocols.md:61-129` defines the 6
  acceptance conditions (provenance present / inline citations /
  edge consistency / tier coherence / foundation conditions /
  non-contradicting) + 5 REJECT cases.
- **Execution.** Pseudo-code "brigadier verification ritual" exists
  (`shared-protocols.md:55-77`) but there is **no Bash/Python/hook
  that runs it**. No `PostToolUse` hook is wired in `.claude/` to
  intercept a Write and run `/lint` dry-run. The `/lint` skill itself
  (despite its v3 preamble) runs only on manual invocation.
- **Evidence the gate is not enforced:** `swarm/wiki/meta/health.md`
  and `swarm/wiki/foundations/swarm-alphas.md` bear
  `confidence_method: ruslan-attested` or `brigadier-attested-with-3-supports`
  but their `sources[]` each have only 1-3 Tier-1 design-doc paths —
  the foundation-condition clause "≥3 supports edges from accepted
  claims" is vacuously true (there are no claims at all), and no
  verification ran.
- **Contradiction detection:** zero contradictions possible today
  because there is nothing to contradict. First real exercise will be
  the first two spine entries that disagree.
- **Tier coherence rule** (outgoing tier ≤ all input source tiers)
  never tested.
- **Rejection-handling behaviour** (`swarm/wiki/tasks/<task-id>/decisions/<ts>-rejection.md`)
  has an empty `decisions/` dir for the current task.

The gate is a design, not a runtime. The first real swarm cycle that
produces a spine artefact will expose whether the brigadier actually
runs the 9-step ritual from §6.3.4 or silently skips it.

## 2× improvement surfaces

A 2× candidate = change that doubles either (i) retrieval recall/latency,
(ii) writes landed per cycle without quality loss, or (iii) error-detection
coverage of the gate. Eight concrete candidates below, ordered by
estimated impact × feasibility:

1. **Typed-BFS Tier-3 executor** (Q1 + D3). Implement a ~60-line
   Python/Bash function that reads `swarm/wiki/graph/edges.jsonl`,
   takes `(seed_paths, edge_type_allowlist, max_hops=2, top_k=10)`
   and returns ranked page paths. Invoked by `/ask` between Tier-2
   and Tier-4. 2× = unlocks multi-hop recall for cross-niche
   questions; also unblocks T2 measurement. No paid-API cost.

2. **Provenance-gate auto-runner.** Wire `PostToolUse` hook on every
   Write to `swarm/wiki/*.md` (excluding `drafts/`, `_archive/`,
   `_templates/`). The hook runs `/lint` dry-run on the written file
   and on failure (a) prepends a rejection log line to
   `swarm/wiki/log.md`, (b) moves the file to
   `swarm/wiki/_rejected/` with original path preserved. 2× =
   enforces §5.5.5 without relying on brigadier discipline.

3. **α-4 `closed` mover script.** A simple Bash hook on
   `swarm/logs/<cycle-id>/cycle-log.md` creation: (a) increment
   `closed_cycles_count` in `swarm/wiki/meta/health.md` frontmatter,
   (b) append to `cycles_log`, (c) check Q8 trigger #1. Unblocks W-6,
   D10, Q8 measurement. Today the counter is frozen at 0 regardless
   of actual cycles.

4. **Niche-symlink populator.** A one-shot script that walks
   `swarm/wiki/<layer>/**/*.md` and populates
   `swarm/wiki/niches/<niche>/` symlinks based on `niche:` frontmatter
   (deterministic per D2 §2.2). Run on every `/ingest` post-pass. 2×
   Tier-4 fallback (bounded niche dir instead of whole wiki) and
   makes Q4 Tier-A pull actually work.

5. **Theme-wiki seeding from Private Library (W-3).** Start with one
   theme (systems/ or philosophy/, shortest reading list) + 3 books.
   Brigadier runs distillation per W-3: reads book → produces
   `swarm/wiki/themes/<theme>/concepts/<slug>.md` + `methods/` +
   `heuristics/` + `anti-patterns/` + `sources/<book-slug>.md`. First
   real concrete wiki content. Establishes the distillation template
   under D4 v2→v3 diff; feeds Tier-3 edges. 2× = first non-empty
   theme → unblocks Q8 trigger #2 path and gives `/ask` actual
   content to synthesise over.

6. **Skill candidate harvester from `meta/agent-improvements/`.**
   A sweep that reads the 8 agent-improvements files, looks for
   DRR-shaped entries appearing ≥2× independently, and emits
   `swarm/wiki/skills/candidates/<slug>/manifest.md` drafts for
   brigadier approval. Unblocks D11/Q6 pipeline. 2× = first skills
   enter the funnel → D9 symlink convention gets exercised.

7. **Golden-set protocol for the 5 expert agents.** Each expert's
   first skill-candidate gets 3 golden-set cases
   (`{input, expected_output, acceptance_predicate}` JSONL) sourced
   from the current task's artefacts. Unblocks D11 Gate I. 2× = first
   real α-3 `learning → validated` transition becomes feasible within
   ~10 cycles.

8. **`/build-graph` migration + first run.** Port the v2
   `/build-graph` algorithm to read `swarm/wiki/` per D7 +
   `--tree=v3`, run once against whatever content lands from W-3
   seeding. Populates `edges.jsonl` + `communities.md` + `summaries.md`.
   2× = Tier-3 BFS becomes meaningful because the graph has edges.

9. **Cross-tree bridge edge generator.** When a v3 theme page's
   `sources[]` cites a v2 `wiki/` path (which will be common during
   W-3 distillation), auto-emit a `cross-tree-ref` record into
   `cross-tree.jsonl`. Makes Q9 coexist mode actually produce
   navigable bridges.

10. **`meta/health.md` live-counter updater.** A tiny cron script
    (5-min interval or PostToolUse) that recomputes the 5 live
    counters from filesystem truth
    (`closed_cycles_count = count(swarm/logs/*/cycle-log.md)`,
    `active_skills_count = count(swarm/wiki/skills/active/*.md)`, etc.)
    and writes them back to the frontmatter. 2× = observability
    latency drops from "undefined" to "5 minutes."

## Questions for integrator

1. **Tier-3 executor language.** The Max-subscription discipline (D6
   §6.10) prohibits paid APIs but is silent on local Python. Is a
   pure-Python BFS acceptable, or must it be Bash/grep? A
   reference implementation would clarify Стадия D vs runtime
   boundary.

2. **Hook wiring location.** `.claude/settings.json` hooks vs a tmux
   script vs a manual brigadier discipline — which is the authorised
   host for the `PostToolUse /lint` runner and the `closed_cycles_count`
   incrementer?

3. **α-3 `retired` absence.** D5 §5.4 locks α-3 to 4 states
   (no `retired`). D12 §12.3 Layer-4 improvements still use
   `validation_status ∈ {proposed, under-validation, accepted, rejected, tombstoned}`
   per D2 §2.4 Layer-4 table — this has 5 states including a
   `rejected` that has no α-3 counterpart. Is Layer-4 a separate
   lifecycle, or should it mirror α-3 exactly?

4. **`brigadier-improvements.md` provenance.** D1 §1.4 lists 7
   bootstrap files under `meta/agent-improvements/` but on-disk there
   are 8 (adds `brigadier-improvements.md`). Is this an intentional
   Phase-A drift or a violation?

5. **Scratchwork exemption scope.** D2 §2.4 Layer-3 introduces
   `is_scratchwork: true` to exempt from §5.5.5. Should the same
   exemption apply to `meta/agent-improvements/<expert>-improvements.md`
   for brigadier-observed-but-unverified hypotheses?

6. **Q4 auto-pull vs manual.** The current task's `manifest.yaml` was
   written by the brigadier by hand (6406 B). Is this the intended
   steady-state (brigadier always hand-picks) or should there be a
   keyword→typed-BFS auto-generator by Phase A close?

7. **2×-measurement discipline.** Spec says 2× candidates should have
   "measurable 2× criterion" (per the current open-questions acceptance
   predicate). For a retrieval change, what's the baseline measurement
   and how is it logged — `meta/health.md` `fpar_log`, or a separate
   benchmark log?

8. **Edge write discipline on manifest.yaml.** `manifest.yaml` is YAML
   not markdown — it has no `related[]` field. Should its internal
   tier_1 / tier_2 / tier_3 path lists auto-emit `part_of` edges to
   the `swarm/wiki/tasks/<task-id>/` hub?

## Provenance

All claims above are grounded in:

- Three spec/decision docs read in full:
  `design/ROY-WIKI-V3-GOALS-2026-04-23.md`,
  `decisions/WIKI-V3-MECHANICS-2026-04-23.md`,
  `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`.
- Nine on-disk artefacts inspected:
  `swarm/wiki/foundations/swarm-alphas.md`,
  `swarm/lib/shared-protocols.md`,
  `swarm/wiki/_templates/edge-types.md`,
  `swarm/wiki/meta/health.md`,
  `swarm/wiki/graph/{edges.jsonl, cross-tree.jsonl, communities.md, summaries.md}`,
  `swarm/wiki/{index.md, log.md, overview.md, insights/README.md}`.
- 5 skill files head-read:
  `.claude/skills/{ingest, ask, lint, consolidate, build-graph}.md`.
- Config: `.claude/config/wiki-roots.yaml` in full (45 L).
- Task artefacts:
  `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/open-questions.md`,
  `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/manifest.yaml`,
  `swarm/logs/cyc-swarm-self-improve-v1-2026-04-23/events.md`.
- Structural surveys via `find`, `ls -la`, `wc -l`, `grep -c`
  (not inlined as code snippets here; see bracketed `[find…]`,
  `[wc -l…]`, `[grep…]` anchors throughout §2–§8).

**Confidence: medium.** High where claims are deterministic file
existence / line counts / grep output (D1 surface, D3 edge count,
D6/D5 file line counts, skill preamble presence). Medium where they
concern run-time behaviour inferred from absence of executor code
(Tier-3 BFS, provenance-gate automation, hook wiring). No Tier-4
sources consulted (no `raw/books-md/`, no WebSearch/WebFetch). No
paid embeddings, no SDKs invoked.
