---
id: context-epsilon-skills
title: "Phase 1 ε — Skills research vs current skill inventory"
type: context-extraction
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
produced_by: subagent-epsilon
created: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: rubric-based
niche: meta
sources:
  - raw/research/compounding-engineering-2026-04-22/R-1-compounding-engineering-core.md
  - raw/research/compounding-engineering-2026-04-22/R-2-swarm-intelligence.md
  - raw/research/compounding-engineering-2026-04-22/R-3-self-improving-systems.md
  - raw/research/compounding-engineering-2026-04-22/R-4-failure-modes-critique.md
  - raw/research/compounding-engineering-2026-04-22/R-5-production-case-studies.md
  - raw/research/compounding-engineering-2026-04-22/R-6-every-cora-compound.md
  - raw/research/compounding-engineering-2026-04-22/R-7-boris-cherny-claude-code.md
  - raw/research/compounding-engineering-2026-04-22/R-8-skills-claudemd-knowledge.md
  - raw/research/compounding-engineering-2026-04-22/R-9-agentic-loop.md
  - raw/research/compounding-engineering-2026-04-22/R-10-continual-learning.md
  - raw/research/compounding-engineering-2026-04-22/R-11-evals.md
  - raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md
  - .claude/skills/README.md
  - .claude/skills/ingest.md
  - .claude/skills/ask.md
  - .claude/skills/lint.md
  - .claude/skills/compile.md
  - .claude/skills/consolidate.md
  - .claude/skills/build-graph.md
  - .claude/skills/search-kb.md
  - .claude/skills/sweep-notion-bank.md
  - .claude/skills/plan-day/SKILL.md
  - .claude/skills/close-day/SKILL.md
  - .claude/skills/focus/SKILL.md
---

## TL;DR

Jetix owns 11 skills — 5 wiki-pipeline (`/ingest`, `/ask`, `/lint`,
`/consolidate`, `/build-graph`), 3 legacy/deprecated (`/compile`,
`/search-kb`, `/sweep-notion-bank`), 3 daily-rhythm (`/plan-day`,
`/close-day`, `/focus`). Zero CE-canonical skills present: no
`/plan`, no `/work`, no `/review`, no `/compound`, no `/lfg`, no
`/resolve_pr_parallel`. The α-3 state machine (proposed → active →
validated → tombstoned) is spec'd in `.claude/skills/README.md` but
**never fired**: `swarm/wiki/skills/{candidates,learning,active}/`
are empty as of 2026-04-23. No promotion mover, no golden-set
harness, no usage-JSONL writer wired. Top 2× surfaces: (a) install
Every's MIT plugin to seed CE loop [R-6:147-232]; (b) build swarm-
native `/gate-packet`, `/promote-draft`, `/critic-stub` to replace
ad-hoc gate rituals; (c) realise the α-3 promotion pipeline so
skill discipline compounds. See §6 for 8 candidates.

## CE canonical skill set map

Every's plugin ships **50+ agents, 42+ skills, 23 workflow commands**
[R-6:8, R-6:335, SYNTHESIS:35-36]. The CE-canonical operator surface
is the **Plan → Work → Review → Compound** loop [R-1:74, R-6:129-232,
SYNTHESIS:595-603], supplemented by meta/hygiene commands.

| CE-canonical skill | Purpose | Jetix equivalent | Gap rating | Anchor |
|---|---|---|---|---|
| `/ce-plan` | Structured plan with confidence-checking; fans out to `best-practices-researcher`, `repo-research-analyst`, `git-history-analyzer`, `learnings-researcher`, `web-researcher` | `/plan-day` (daily routine, not feature-level) | **missing** (feature-level) | R-6:147-156, SYNTHESIS:600 |
| `/ce-work` | Execute work items systematically; MCP simulators (Playwright/XcodeBuildMCP) | none | **missing** | R-6:160-166, SYNTHESIS:601 |
| `/ce-worktree` | Parallel git worktrees per track | none (gitflow ad-hoc) | **missing** | R-6:162, SYNTHESIS:601 |
| `/ce-code-review` | 12-subagent fan-out: security, performance, correctness, maintainability, testing, simplicity, data-integrity, api-contract, reliability, architecture, adversarial, pattern-recognition | none — Jetix has wiki `/lint` only | **missing (biggest gap)** | R-6:171-192, SYNTHESIS:602-611 |
| `/ce-compound` | "Money step": summarize learnings → rules in CLAUDE.md/AGENTS.md | none — manual strategies.md append | **missing** | R-6:195-201, SYNTHESIS:603, R-1:104-108 |
| `/ce-compound-refresh` | Re-evaluate stale/drifting learnings (keep/update/replace/archive) | none | **missing** | R-6:201, R-6:357, SYNTHESIS:603 |
| `/lfg` (jonathanmalkin / community) | "Let's fucking go" session opener: tri-perspective pre-flight | `/plan-day` (partial) | **partial** | R-8 best-practices ecosystem + SYNTHESIS:1720 /wrap-up pattern |
| `/wrap-up` (jonathanmalkin) | Session-close 4-phase: capture → lessons → commit → next | `/close-day` (partial; no lessons extraction) | **partial** | SYNTHESIS:1719-1721, SYNTHESIS:1994-1995 |
| `/resolve_pr_parallel` (Boris Cherny pattern) | 5 parallel Claude instances in 5 git worktrees | none | **missing** | R-1:265-266, SYNTHESIS:324-327 |
| `/skill-creator` | Meta-skill for creating / editing / benchmarking skills | none — hand-crafted markdown | **missing** | R-8:215-231, R-8:261-271, R-8:926-928 |
| `commit` (Anthropic built-in) | Stage + commit with AI-generated message; shell-expansion context | manual `git commit` | **partial** (close-day does this) | R-8:87-99, R-8:120-137 |
| `@claude` GitHub Action comment loop | Reviewer writes `@claude add to CLAUDE.md ...` → Claude auto-commits CLAUDE.md delta | none | **missing** | R-1:76-80, R-7:4.4 via SYNTHESIS:98-101 |
| `/memory` + `#` shortcut | Interactive memory panel + save-to-CLAUDE.md one-shot | none native (auto-memory off) | **missing / not wired** | R-8:518-532 |
| `/agents` | Tabbed sub-agent management UI | none | **missing** | R-8:602-603 |
| `/plugin` | Marketplace install (auto-registered `claude-plugins-official`) | none installed | **missing** | R-8:630-653 |

**Summary.** Out of 12 CE-canonical skills, Jetix has 0 present, 3 partial. The
compound (money step) and the 12-reviewer fan-out are the two highest-ROI
missings per the whole synthesis [SYNTHESIS:167-175].

## Current skill audit (11 skills)

Note: `.claude/skills/README.md:157-162` confirms **no symlinks exist** — no
v3 promotion has fired. The 5 wiki-pipeline skills are D7-parameterised regular
files with `$WIKI_ROOT` resolution; the 3 exclusions are deprecated; the 3
daily-rhythm files live as `<name>/SKILL.md` directories (older convention).

### 1. `/ingest` — raw→wiki source ingestion
- **Purpose**: pipeline a file or URL from `raw/` into `${WIKI_ROOT}/` as connected entity pages + edges [.claude/skills/ingest.md:18-127].
- **Anchor**: `.claude/skills/ingest.md`.
- **Weakness**: no dedup check against existing wiki/sources; relies on LLM to "extract 10-15 elements" with no schema validator [.claude/skills/ingest.md:58-65].
- **2× opportunity**: add Promptfoo golden-set of 20 ingested sources [R-11 §8.1, SYNTHESIS:1763-1766] + ACE append-only lessons file capturing "sources we mis-classified" → compounding accuracy [R-3 §7.2, SYNTHESIS:1719-1721].

### 2. `/ask` — Q→synthesis→optional comparisons/ entry
- **Purpose**: answer via index.md → grep → read pages; sometimes save to `comparisons/` [.claude/skills/ask.md:27-122].
- **Anchor**: `.claude/skills/ask.md`.
- **Weakness**: no embeddings, no HippoRAG; Tier-1 is "read index.md fully" — becomes O(N) as wiki grows [.claude/skills/ask.md:27-32]. "Save to comparisons" decision is LLM-subjective with no log.
- **2× opportunity**: delegate retrieval to `@modelcontextprotocol/server-memory` or in-house wiki MCP per R-8 §7.2 [R-8:15, R-8:2774]; add `pass^3` reliability metric [R-11 §6, SYNTHESIS:1779-1781].

### 3. `/lint` — 11-check health report
- **Purpose**: orphans / stale / broken-links / frontmatter / contradictions / cross-refs / index-drift / α-2/α-3 / triple-channel / Q8 Layer-9 lock / symlink integrity [.claude/skills/lint.md:22-94].
- **Anchor**: `.claude/skills/lint.md`.
- **Weakness**: report-only; no auto-triage; no time-series trending; no hook binding → it's advisory like CLAUDE.md (~80% compliance per Builder.io tip #38) [R-8:458].
- **2× opportunity**: wire as `PostToolUse` hook on `${WIKI_ROOT}/**/*.md` → deterministic 100% [R-8:458, SYNTHESIS:2705-2708]; emit issues-per-niche timeseries for FPF-Steward quarterly audit.

### 4. `/compile` — DEPRECATED legacy synthesis
- **Purpose**: synthesize ingested raw→KB-article in `knowledge-base/{cluster}/{topic}.md` [.claude/skills/compile.md:14-50].
- **Anchor**: `.claude/skills/compile.md`.
- **Weakness**: explicit deprecation header at top; targets legacy `knowledge-base/` tree; not parameterised for `$WIKI_ROOT` [.claude/skills/compile.md:6-12].
- **2× opportunity**: delete on MIGRATION.md close; its function is supplanted by `/ingest` + `/ask` Tier-1/2 retrieval.

### 5. `/consolidate` — dedup + merge with confirm
- **Purpose**: find near-duplicate pages, diff, merge with user `y` [.claude/skills/consolidate.md:15-101].
- **Anchor**: `.claude/skills/consolidate.md`.
- **Weakness**: cannot mutate α-2 `state` — must defer to brigadier per critic-gate2 SS3; creates HTML-comment annotation in `_archive/` only [.claude/skills/consolidate.md:74-78].
- **2× opportunity**: integrate with `/build-graph` edge-rewrite step so consolidation is transactional [.claude/skills/consolidate.md:72-74]; add auto-recommend via clustering on `edges.jsonl` degree/community overlap.

### 6. `/build-graph` — 12-enum edges + communities
- **Purpose**: glob pages → extract mentions → classify edge-type → append to `edges.jsonl` → community detection → `summaries.md` [.claude/skills/build-graph.md:25-93].
- **Anchor**: `.claude/skills/build-graph.md`.
- **Weakness**: community detection is "connected components + 15-node split"—naive; no Louvain/Leiden, no hierarchy; summaries are LLM-synthesized without eval [.claude/skills/build-graph.md:64-85].
- **2× opportunity**: swap to sqlite-vec for Phase 2 semantic community detection [R-10 §4.5, SYNTHESIS:1759-1761]; emit GraphRAG/HippoRAG-style summaries that `/ask` Tier-4 fallback uses [.claude/skills/ask.md:36].

### 7. `/search-kb` — DEPRECATED legacy lookup
- **Purpose**: MOC → tags → full-text grep over `knowledge-base/` + `raw/` [.claude/skills/search-kb.md:15-39].
- **Anchor**: `.claude/skills/search-kb.md`.
- **Weakness**: explicit exclusion header; targets `knowledge-base/_index.md` which is in migration [.claude/skills/search-kb.md:3-9].
- **2× opportunity**: delete after MIGRATION.md completes; fold any still-useful grep logic into `/ask` Tier-2.

### 8. `/sweep-notion-bank` — DEPRECATED one-shot Notion ingest
- **Purpose**: one-off Notion Bank (650+ ideas) → wiki/ with parallel sweep-workers [.claude/skills/sweep-notion-bank.md:22-97].
- **Anchor**: `.claude/skills/sweep-notion-bank.md`.
- **Weakness**: hardcoded to specific DB ID + date (2026-04-16); not parameterised [.claude/skills/sweep-notion-bank.md:13-20].
- **2× opportunity**: promote generalised `/notion-sweep <db-id>` to candidates/ if a second sweep ever needed; otherwise archive post-Phase-1.

### 9. `/plan-day` — morning routine
- **Purpose**: yesterday's log + Notion command-center + per-project next_action → propose plan [.claude/skills/plan-day/SKILL.md:8-37].
- **Anchor**: `.claude/skills/plan-day/SKILL.md`.
- **Weakness**: no research subagents (CE `/ce-plan` fans out 5 researchers) [R-6:149-156]; Notion dependency conflicts with D14 decommission.
- **2× opportunity**: enhance per SYNTHESIS:2714-2716 — add `best-practices-researcher`, `repo-research-analyst`, `learnings-researcher`, `git-history-analyzer` subagent calls so morning plan inherits CE discipline.

### 10. `/close-day` — evening wrap
- **Purpose**: itog → project logs → Notion update → git commit+push [.claude/skills/close-day/SKILL.md:8-40].
- **Anchor**: `.claude/skills/close-day/SKILL.md`.
- **Weakness**: no structured lessons extraction → per-agent `strategies.md`; no `/ce-compound` equivalent; manual "what insights?" question not automated [.claude/skills/close-day/SKILL.md:14-19].
- **2× opportunity**: adopt jonathanmalkin `/wrap-up` 4-phase + Stanford ACE append-only pattern (+10.6% accuracy) [SYNTHESIS:1719-1721, SYNTHESIS:2679-2681]; wire to feed `ce-learnings-researcher` equivalent in tomorrow's `/plan-day`.

### 11. `/focus` — project-switch context loader
- **Purpose**: load overview + plan + log + questions for a project; optionally Notion page [.claude/skills/focus/SKILL.md:8-40].
- **Anchor**: `.claude/skills/focus/SKILL.md`.
- **Weakness**: no verification the project files exist before summarising; summary size capped at "20 lines" arbitrary [.claude/skills/focus/SKILL.md:30, 41].
- **2× opportunity**: extend with `memory: project` sub-agent scope [R-8:590-596] so per-project accumulated lessons persist across sessions without wiki round-trip.

## Swarm-specific missing skills

The 6-agent swarm (brigadier + 5 experts per D6) runs cycles with
AWAITING-APPROVAL gates, cell-matrix fires, Compound-step writes to
strategies.md. Gate/critic/integrator rituals are currently **ad-hoc
markdown** — no slash-invoked primitive. At least 8 candidates warrant
proposed→active promotion through α-3.

### 1. `/gate-packet` — assemble AWAITING-APPROVAL bundle
- **Trigger**: end of Phase 4 / Phase 6 in cycle; brigadier decides gate-ready.
- **Inputs**: task_id, cycle_id, list of decisions/artefacts produced.
- **Output**: `swarm/gates/AWAITING-APPROVAL-<slug>-<date>.md` with sections: hypotheses summary, diffs touched, verification evidence, critic pass status, explicit Ruslan ack line.
- **Lives**: `swarm/wiki/skills/candidates/gate-packet/manifest.md` → after 3+ successful gates move to `active/`.
- **Rationale**: current packets built by hand (see `[step-2-2-4] AWAITING-APPROVAL gate2 (5 experts + diffs + verification)` commit on branch) — formalise so format is stable across cycles.

### 2. `/promote-draft` — α-3 proposed → active mover
- **Trigger**: brigadier after candidate has 3+ uses + positive outcome ratio.
- **Inputs**: skill_slug, justification, golden-set reference.
- **Output**: (a) move `candidates/<slug>/manifest.md` → `learning/<slug>/manifest.md`; (b) create `learning/<slug>/golden-set.jsonl`; (c) append to `usage/<slug>.jsonl`; (d) update `swarm/wiki/log.md`.
- **Lives**: `swarm/wiki/skills/candidates/promote-draft/manifest.md` (bootstrapping; eventually `active/`).
- **Rationale**: README §"Symlink creation hook" defines the mechanical ln-s step but does NOT define the **move command**. Also needed: `/activate-skill` for `learning → validated` (creates the symlink in `.claude/skills/`).

### 3. `/critic-stub` — automated critic gate runner
- **Trigger**: brigadier before Ruslan gate.
- **Inputs**: gate-type (gate1/gate2), target document path.
- **Output**: structured issues report `swarm/gates/critic-<gate>-<date>.md` with severity labels (critical/high/medium/low); grouped by document section.
- **Lives**: `.claude/skills/critic-stub.md` (project scope; user-invocable).
- **Rationale**: recent commits `critic gate2 fixes: 7 of 10 medium` show manual critic runs — skill makes this reproducible. Direct application of BP19 three-agent harness (Planner→Generator→Evaluator) [SYNTHESIS:1774-1777].

### 4. `/integrator-synthesis-template` — cell-matrix integrator
- **Trigger**: Phase 5 of cycle — combining 4+ cell outputs.
- **Inputs**: list of cell context files (e.g., `epsilon-skills.md`, `alpha-agents.md`, ...).
- **Output**: `swarm/wiki/tasks/<task>/artefacts/integration-synthesis.md` with: convergent findings, divergent findings, open questions, recommended Phase-A actions.
- **Lives**: `swarm/wiki/skills/candidates/integrator-synthesis-template/manifest.md`.
- **Rationale**: current cycle synthesis is ad-hoc markdown; formalise so Matrix 5×4 fires deterministically and each cell's contribution is auditable (per open-questions.md acceptance predicate line 13-14).

### 5. `/compound` — Jetix port of `/ce-compound`
- **Trigger**: end-of-session or explicit user ask.
- **Inputs**: session transcript / daily-log / gate feedback.
- **Output**: append entries to `agents/<id>/strategies.md` (ACE-style), optionally new rule to `.claude/rules/<topic>.md`, optionally new candidate skill to `swarm/wiki/skills/candidates/<slug>/`.
- **Lives**: `.claude/skills/compound.md` + `swarm/wiki/skills/active/compound.md` (after validation).
- **Rationale**: highest-ROI missing per SYNTHESIS:167-175 ROI-table item 5 + the repeated emphasis on "the money step" [R-6:195, R-1:104].

### 6. `/swarm-spawn` — cycle initialisation
- **Trigger**: brigadier initiates a new self-improvement or delivery cycle.
- **Inputs**: task_id, cycle_id, cell list, per-cell mission brief.
- **Output**: scaffold `swarm/wiki/tasks/<id>/{context,artefacts,decisions}/`, create open-questions.md with acceptance predicate, prepopulate cell stubs.
- **Lives**: `.claude/skills/swarm-spawn.md`.
- **Rationale**: current cycle (cyc-swarm-self-improve-v1) was scaffolded by hand — codify so future cycles are 1-command.

### 7. `/skill-audit` — self-auditing skill inventory
- **Trigger**: weekly or on-demand.
- **Inputs**: none.
- **Output**: markdown table: each skill × {last-invoked, uses-last-30d, golden-set-pass-rate, α-3 state, size (bytes), description chars vs 1,536 budget, broken-symlink flag} [R-8:170, R-8:149, README §11].
- **Lives**: `swarm/wiki/skills/candidates/skill-audit/manifest.md`.
- **Rationale**: Every plugin v2.30.x exceeded 316% skill-description budget silently [R-8:170, SYNTHESIS:AP9]; Jetix needs a forcing function to avoid same. Also surfaces unused skills for tombstoning.

### 8. `/fire-cell` — per-cell matrix task dispatch
- **Trigger**: brigadier during Phase 1-4.
- **Inputs**: cell-id (α/β/γ/δ/ε), task_id, mission doc.
- **Output**: subprocess call with appropriate sub-agent role, outputs landing in `swarm/wiki/tasks/<id>/context/<cell>-<slice>.md`.
- **Lives**: `.claude/skills/fire-cell.md`.
- **Rationale**: acceptance predicate (open-questions.md:13) requires "Matrix 5×4 demonstrably fired ≥4 cells × ≥2 modes"; formalising cell dispatch makes the matrix auditable.

## Skill α-3 state-machine observations

`.claude/skills/README.md` defines α-3 as 4 states: **proposed / active
/ validated / tombstoned** [README:87-90]. But the exact naming used by
the promotion code block [README:136-155] uses {**proposed, active
(=learning), validated, tombstoned**} — note: *active* and *learning*
appear interchangeable in the worked example [README:140, README:144].
The task brief here calls the states {proposed, learning, validated,
archived}. There is **a specification drift** between: (a) README §"α-3
4 states" [README:87-90 — "no separate retired removal path"]; (b) the
`/lint` state-validity check which flags states ∉ {candidate, learning,
active, tombstoned} [.claude/skills/lint.md:68]; (c) the D2 §2.4 Layer 8
reference. This is a gate-1 critic issue.

**Promotion operational wiring status — NOT wired:**

| Step | Spec'd | Wired | Evidence |
|------|--------|-------|----------|
| proposed write (candidate manifest) | README:136-139 | **no** | `swarm/wiki/skills/candidates/` is empty |
| proposed → active mover | README:140-142 | **no** | No `/promote-draft` skill exists; `swarm/wiki/skills/learning/` empty |
| golden-set.jsonl creation | README:141 | **no** | No harness, no template, no Promptfoo integration |
| usage-log append | README:142 ("Usage logged to usage/<slug>.jsonl") | **partial** | `usage/manifest.yaml` exists, per-skill JSONL absent |
| activation predicate evaluator | README:56-57 ("golden-set ≥3 + ≥10 uses + ✓/✗ ≥3:1") | **no** | No evaluator; Promptfoo not installed; no uses tracked |
| active → validated mover (with symlink creation) | README:144-148 | **no** | `.claude/skills/` has zero symlinks ("Phase A initial state", README:157-162) |
| validated → tombstoned mover (symlink rm + `_archive/` mv) | README:150-154 | **no** | No tombstone fire recorded |
| `/lint` broken-symlink detection | .claude/skills/lint.md:88-94 | **code present** | No executions logged; `wiki/_lint-report-*.md` not found recently |

**What captures a validation event today?** Nothing. The spec cites
"golden-set ≥3 + ≥10 uses + ✓/✗ ≥3:1" [README:56-57] but:
- Golden-set format unspecified beyond "JSONL" — no schema, no fields, no pass/fail definition.
- Usage logging has no writer — `usage/<slug>.jsonl` is manually created per skill with no structured event schema.
- The ✓/✗ ratio is not linked to any test runner (Promptfoo absent per SYNTHESIS:174, BP17).
- The entire pipeline presupposes Hamel-Husain Critique Shadowing methodology (binary pass/fail + domain expert + 30 examples) [SYNTHESIS:1768-1772] which Jetix has not yet implemented.

**What fails operationally:**
1. No candidate exists — zero v3-born skills. Current cycle (self-improvement) may be the first generator.
2. No "compound" step writes candidate skills when the swarm discovers them — the tie-back from Phase 5/6 synthesis to `candidates/` is unwired.
3. Nomenclature drift: {proposed/active/validated/tombstoned} vs {candidate/learning/active/tombstoned} vs task-brief {proposed/learning/validated/archived} — three competing spellings, none authoritative by a single canonical file.
4. Manager (hub-and-spoke Orchestrator) has no "skill budget" — unlike 20-task attention budget (CLAUDE.md:39), there's no ceiling on concurrent candidates.

## 2× improvement surfaces

Combining new skills + pipeline repairs:

1. **Install Every's compound-engineering-plugin (MIT, 6.8k stars) and fork DACH variants** → instantly adds 50+ agents, 42+ skills incl. 12-reviewer fan-out [R-6:382, SYNTHESIS:2779-2781]. 2× criterion: `/ce-code-review` produces ≥1 blocking finding on the next Phase 6 gate packet that manual review would have missed.

2. **Wire α-3 promotion pipeline end-to-end** — build `/promote-draft` + `/skill-creator` (or adopt Anthropic's `skill-creator` from anthropics/skills [R-8:227-231, R-8:261-271]) so candidates→validated takes 1 command, not manual mv. 2× criterion: 3 new candidates promoted to `learning/` by end of next cycle.

3. **Add Promptfoo + Langfuse eval stack** ($50-209/mo Phase 1) [R-11 §8.1, SYNTHESIS:174 item 6, BP17]. 2× criterion: golden-set pass-rate tracked for all 5 wiki-pipeline skills within 2 weeks; `/ingest` regression caught before merge.

4. **Build `/compound` skill + wire to `/close-day`** — session transcripts → ACE-style append to `agents/<id>/strategies.md` + candidate-skill proposals to `candidates/` [R-3 §6.1.6 Folkman 66.7→57.1% degradation avoided, SYNTHESIS:172 item 5]. 2× criterion: ≥1 new candidate skill proposed per working week.

5. **Convert `/lint` from advisory to `PostToolUse` hook** [R-8:458, Builder.io tip #38]. 2× criterion: broken links in wiki/ drop from 80% caught → 100% blocked (deterministic). Same pattern for frontmatter validation, Rechnungsnummer, secret-scrub.

6. **Add `/resolve_pr_parallel` (Boris Cherny pattern: 5 parallel Claudes in 5 worktrees)** [R-1:265-266, BP3 + SYNTHESIS:1703-1705]. 2× criterion: lint-fix PR throughput 5× on bulk refactor (e.g., the 7 medium fixes in recent commit 379bcd5).

7. **Implement skill-budget audit** — `/skill-audit` measuring `<available_skills>` char count against 1,536-per-entry / 15,000-total cap [R-8:170]. 2× criterion: description truncation (Every plugin 316% overflow, [AP9]) prevented — audit fails build if any skill exceeds budget.

8. **Enhance `/plan-day` with CE subagent fan-out** — add `learnings-researcher` subagent reading `strategies.md` + recent closed tasks → compounds with every morning [R-6:149-156, SYNTHESIS:2715-2716]. 2× criterion: weekly plans cite ≥2 prior-cycle lessons inline, compared to current 0.

9. **Deprecate + delete legacy 3** (`/compile`, `/search-kb`, `/sweep-notion-bank`) once MIGRATION.md + Notion-decomm complete [.claude/skills/compile.md:6-11, .claude/skills/search-kb.md:3-9, .claude/skills/sweep-notion-bank.md:13-20]. 2× criterion: `<available_skills>` budget savings ~1,200-1,800 chars freed for swarm-native additions.

10. **Add `/skill-creator` meta-skill** — installing from anthropics/skills gets authoring + benchmarking + description-optimisation [R-8:261-271]. 2× criterion: new skill creation time drops from ~1h manual to ~15 minutes guided.

## Questions for integrator

1. **State-nomenclature authority.** Who authoritatively locks the α-3 state names? The README §94 says "only 4 states (proposed/active/validated/tombstoned)" but `/lint` enforces `{candidate, learning, active, tombstoned}`. Both cannot be correct. Propose: one-line PR to README + lint.md picking the canonical set (recommend: proposed → learning → active → tombstoned; maps D11 4-phase to a Voyager-style lifecycle [R-3 §3.3 Point 3]).
2. **First-candidate policy.** Should the swarm cycle itself auto-propose candidates from Phase 5 synthesis → `candidates/<slug>/manifest.md`? Or does proposal require a human-in-the-loop approval first (matching HITL Point 2 per R-3 §3.3)?
3. **Every plugin adoption timing.** Phase-A implement-now (per acceptance predicate, open-questions.md:6-7) or defer to Phase 2a? Installing is 1h + 3-5h DACH customisation [SYNTHESIS:170 item 3] — within Phase A effort budget?
4. **Promptfoo residency.** R-11 §8.1 recommends Langfuse self-hosted EU; for Berlin GDPR — is the $50-209/mo budget approved for Phase A, or must eval rails come from file-based harness only?
5. **Skill-budget sanity check.** Current 11 skills: rough chars in `description`+`when_to_use` — I did not count exhaustively; a sibling cell should verify none already exceed 1,536 per-entry or 15,000 total [R-8:170].
6. **`/sweep-notion-bank` disposition.** Given Notion decommission by Day 14 (SYNTHESIS:2768-2770), should this be deleted now or archived in `swarm/wiki/_archive/skills/` for audit?
7. **Symlink-first bootstrap.** README §157-162 says symlinks appear "lazily on first promotion" — should this cycle (T-swarm-self-improve-v1) be the event that first fires a real α-3 `learning → active` transition? If yes, which candidate skill? (I propose `/compound` as the canonical first transition.)

## Provenance

- Research corpus: `raw/research/compounding-engineering-2026-04-22/R-1…R-11.md` + `SYNTHESIS-DEEP-CE-vs-JETIX.md` (~1.0 MB, ~14,320 lines), read line-range-targeted per discipline rule.
- Skill inventory: confirmed via `ls -la .claude/skills/` showing 8 files (3 dirs × SKILL.md) + 8 `.md` files; 3 empty `swarm/wiki/skills/{candidates,learning,active}` dirs confirming Phase A.
- Recent commits read via git status in system context: `797a92f [task] T-swarm-self-improve-v1`, `2a87a9e ROY-AGENTS-BUILT`, `84fd422 [step-2-2-4] AWAITING-APPROVAL gate2`, `906165a bootstrap verification passed`, `379bcd5 critic gate2 fixes`.
- Master synthesis crosswalk: SYNTHESIS §2.4 BP1-BP20 + §2.5 AP1-AP12; Part 1 per-wave summaries §1.1-1.8; §5.3-5.4 migration plan; §5.5 agent evolution.
- Cell discipline: no inlined source bodies > 5 lines; every claim carries `[path:line-range]`; Max-subscription lock respected (no paid APIs invoked, no embeddings, no vector DBs proposed for Phase A).
- Confidence: **medium** overall — CE canonical set is well-documented (multiple primary sources via R-1, R-6, R-7); α-3 state-machine nomenclature drift is a direct observation from .claude/skills/README.md vs .claude/skills/lint.md vs task brief (three spellings), verified; skill-budget numbers are from R-8:170 direct citation; swarm-specific candidate skills are inference from current cycle's gate/critic/integrator rituals and the acceptance predicate language.
