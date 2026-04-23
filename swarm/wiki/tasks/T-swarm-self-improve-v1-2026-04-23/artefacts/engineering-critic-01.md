---
id: engineering-critic-01
title: "Engineering critic — Phase-A swarm self-improvement (T-swarm-self-improve-v1)"
type: artefact
layer: tasks
niche: meta
created: 2026-04-23
last_modified: 2026-04-23
last_reviewed: 2026-04-23
pipeline: ingested
state: drafted
confidence: medium
confidence_method: rubric-pass-rate
tier: core
produced_by: engineering-expert-critic
mode: critic
task_id: T-swarm-self-improve-v1-2026-04-23
cycle_id: cyc-swarm-self-improve-v1-2026-04-23
sources:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "1-126"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/beta-current-agents.md", range: "1-538"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md", range: "1-372"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/delta-memory-sota.md", range: "1-291"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md", range: "1-306"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "1-204"}
  - {path: "swarm/lib/shared-protocols.md", range: "1-60"}
related: []
tags: ["#type/artefact", "#status/drafted", "#topic/swarm-engineering", "#priority/P1"]
acceptance_predicate: >
  This artefact passes all 8 §3.1 Conformance checks (N/A rows
  explicitly declared) AND carries ≥2 alternatives in §5 AND has §6
  anti-scope AND ≥8 hypotheses in §4 each with source citation,
  current-state, proposed improvement, impact/effort/risk/locks.
---

# Engineering critic — Phase-A swarm self-improvement

## §1 TL;DR

The Jetix Phase-A swarm is **over-specified and under-executed**
[context/zeta:93-99]. Six agent files (8077 lines) are structurally
sound; the wiki v3 infrastructure (53 dirs, 10 templates) is on disk;
shared-protocols.md (274 L) holds the runtime contract. What is absent
is the *execution layer*: every hook is a stub, every gate is prose,
every metric is a placeholder frozen at zero. Eight engineering
hypotheses below name the weakest surfaces and quantify the 2×
improvement potential. The top three by combined impact×effort ratio
are: (H-1) wiring the `UserPromptSubmit`/`PostToolUse` hook layer,
(H-2) canonicalising the `§§6.2–6.10` off-by-one across all five
expert §7 stubs, and (H-3) building the α-3 skill-promotion pipeline
end-to-end. All three are feasible inside Phase A with no paid
tooling.

---

## §2 Conformance Checklist (≥5 binary checks)

The artefacts under review are the 6 agent files + wiki v3
infrastructure + shared-protocols.md + skill files. Checks are applied
to those artefacts, not to this critic draft itself.

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | **Deep-module check (Ousterhout).** Shallow-module count ≤2 per agent file: count public interfaces whose implementation body ≤ 2× declaration size. Proxy: §7 import-stub is 14 lines of prose that restates shared-protocols.md — the stub IS the interface; the body is the same text. Shallow-module count = 5 (five experts each carry an identical shallow stub instead of one deep import). | FAIL | [context/beta:243-254] — §7 stub body is "9 bullets × ~12 words = ~5-line identical prose across 5 experts"; 5 shallow stubs exist where 1 deep import + per-expert delta would suffice. AP-ENG-2 triggered. |
| 2 | **Function-purpose check (Martin).** Every public mode-activation gate (§3.0..§6.0) carries a one-sentence "why" comment, not just "what". | PARTIAL/FAIL | [context/beta:325-341] — three distinct Soft/Hard activation styles exist; philosophy §3.0 has no Soft/Hard sub-headers; investor uses blockquote form. The purpose of the gate is not uniformly stated in a "why" sentence. AP-ENG-7 triggered for philosophy + investor. |
| 3 | **Test-integrity check (Kent Beck).** No hook or skill deletes tests to make pipeline green. | N/A | No test suite exists Phase A; `/lint` is advisory-only and has never run [context/gamma:76]. This check is vacuously N/A — but the absence of any test harness is itself an AP-ENG-5 surface (see H-5). |
| 4 | **Premature-abstraction check (Brooks).** Every abstraction has ≥3 concrete uses. Check: `role_tool_matrix` in shared-protocols §5 is an abstraction over tool permissions; it is referenced by all 6 agents but has no runtime enforcement — zero executed uses [context/gamma:73]. | FAIL | The `role_tool_matrix` is a 20-line YAML-in-prose abstraction cited by every agent §7 stub but with zero runtime uses (no hook calls it; no Bash enforces it). Abstraction with 0 executed uses fails the ≥3-concrete-uses floor. AP-ENG-9 triggered. |
| 5 | **External-dependency check (Hunt/Thomas).** Every external-dep call site has explicit failure-mode (timeout, retry, fallback) declared. Check: `/ask` skill is an external dependency from the brigade perspective; `/lint` is invoked on-demand without timeout/fallback [context/epsilon:108-110]. | FAIL | `.claude/skills/lint.md` carries no timeout, no retry policy, no fallback if `/lint` produces no output. Same for `/ask`: no fallback path if Tier-2 grep returns empty [context/epsilon:103]. AP-ENG-10 triggered. |
| 6 | **DRY check (Hunt/Thomas).** Same logic copied ≥3 times. Check: the "Non-consultation is a defect logged" preamble appears 5× near-identical [context/beta:233-242]; the §7 import-stub prose appears 5× [context/beta:243-254]; the refusal JSON schema appears 20× (5 experts × 4 modes) [context/beta:426-428]. | FAIL | Three separate blocks of logic are each copied ≥5× across agent files. AP-ENG-11 triggered (x3 DRY violations at system scope). |
| 7 | **Tool-eval acceptance check (AP-ENG-5).** Every tool-eval.md draft carries eval-dataset + Hamel-binary predicate. Check: no tool-eval.md drafts exist; golden-set paths are placeholders; eval-dataset paths are null across all 20 cells [context/alpha:50]. | FAIL | `swarm/wiki/skills/candidates/` is empty; zero golden-set JSONL files exist; activation-predicate evaluator is unwired [context/epsilon:238-249]. AP-ENG-5 triggered. |
| 8 | **Architecture-pattern declaration check (Anthropic).** Every architecture-proposal.md names the orchestration pattern explicitly and justifies ≤200 words. Check: shared-protocols.md §6 cross-cell-reference names "Orchestrator-Workers / hub-and-spoke" implicitly but no architecture-proposal.md exists in drafts/ or canonical wiki listing the pattern + justification. | FAIL | [context/gamma:56] — `swarm/wiki/brigadier/` exists but all 4 buckets are empty; no architecture-proposal.md with explicit pattern + justification on disk. AP-ENG-12 triggered. |

**Summary.** 6 FAIL / 1 FAIL-partial / 1 N/A (vacuously). All 8 checks surfaced failures. This artefact meets the ≥5 binary checks floor with 7 active failures.

---

## §3 Acceptance Predicate (Hamel-binary)

`The Phase-A Jetix swarm infrastructure (6 agent files + shared-protocols.md + wiki v3 + skill files) passes engineering Conformance checks 1-8 only when: (1) the 5× shallow §7 import-stub is collapsed to a single deep import + per-expert delta, (2) all 5 expert §7 headers read "SPEC D6 §§6.1..§6.10", (3) role_tool_matrix has ≥1 runtime enforcement call in .claude/settings.json hooks, (4) the α-3 skill-promotion pipeline has ≥1 wired step (proposed → learning mover), (5) ≥1 golden-set JSONL file exists per cell, (6) /lint is wired as a PostToolUse hook, (7) at least the top 2 DRY violations are extracted to shared-protocols.md references, AND (8) every mode-activation gate uses uniform Soft/Hard sub-headers across all 5 experts.`

---

## §4 Hypotheses (≥8, ranked by impact×effort⁻¹)

Each hypothesis: one-line statement | source citation | current-state | proposed improvement (concrete file + change) | impact 1-5 | effort 1-5 | risk 1-5 | touched locks.

---

### H-1: Hook layer absent — UserPromptSubmit + PostToolUse stubs shipped but not installed

**Statement.** The `UserPromptSubmit` and `PostToolUse` hook layer,
cited in all 6 agent §3.0..§6.0 activation gates as the "Hard" gate
enforcer, does not exist in `.claude/settings.json`; every mode-prefix
guard and every provenance-gate enforcement is soft-only, making AP-5
(mode-confusion) and Q2 (single-writer) structurally unenforceable.

**Source.** [context/alpha:48] "Hook enforcement is recommended as
Option A but only scaffolded, not built"; [context/gamma:193-196]
"Pseudo-code 'brigadier verification ritual' exists but there is no
Bash/Python/hook that runs it"; [context/epsilon:108-110] "`/lint` …
no hook binding → it's advisory like CLAUDE.md (~80% compliance per
Builder.io tip #38)"; [context/zeta:57] "AP-5 drops from ~6 surfaces
to 1 deterministic gate".

**Current state.** `.claude/settings.json` carries no `hooks` key.
All 20 mode-activation "Hard" gates reference a "UserPromptSubmit hook
(Phase B stub)" — every one is a stub. The provenance gate §5.5.5
(shared-protocols §2) is narrative pseudocode; no PostToolUse hook
intercepts a Write to `swarm/wiki/*.md` and runs §5.5.5.

**Proposed improvement.**
- File: `.claude/settings.json`
- Change: Add `"hooks"` key with two entries: (a) `UserPromptSubmit`
  hook running a `mode-prefix-validator.sh` that greps the prompt's
  first non-blank line against `^mode: (critic|optimizer|integrator|scalability)$`
  and returns a structured refusal JSON if no match AND the target
  agent is in `mode_allowlist`; (b) `PostToolUse` hook on `Write` that
  runs `/lint --dry-run` against any path matching `swarm/wiki/*.md`
  excluding `drafts/`, emitting a rejection record to
  `swarm/wiki/tasks/<task-id>/decisions/<ts>-rejection.md` on failure.
- Additional file: `swarm/lib/hooks/mode-prefix-validator.sh` (~20
  lines; pure Bash; no SDK; no paid API).

**Impact.** 5/5 — Converts AP-5 (mode-confusion) from a
~6-surface structural vulnerability to a single deterministic gate;
converts provenance-gate from "brigadier discipline" to "enforced on
every Write". Unblocks Q2, Q5, checks 1/3/4 of §3.1.

**Effort.** 2/5 — Two small Bash scripts (~40 lines total) + one JSON
key. No new dependencies. Claude Code `.claude/settings.json` hook API
is documented and available.

**Risk.** 2/5 — Regex false-positives on malformed `mode:` lines
(e.g. `mode: critic ` with trailing space) could block valid prompts.
Mitigate: validate regex against the 20 known cell prefixes before
enabling; add `--dry-run` flag to validator for testing.

**Touched locks.** W-8 (workflow = FPF + hooks), Q2 (single-writer),
Q5 (/lint enforcement), D6 (shared-protocols §5), E-3 (critic hard
gate), E-4 (optimizer hard gate), AP-ENG-3 (optimization-violates-
invariant), AP-ENG-4 (method-change-without-escalation).

---

### H-2: §7 import-stub SPEC-numbering off-by-one (5 of 6 files wrong)

**Statement.** All five expert §7 headers cite `SPEC D6 §§6.2–6.10`
while the canonical SPEC ordering is §6.1..§6.10 (brigadier alone is
correct); the off-by-one implies §6.1 (wiki-write protocol) is not
imported, though the body bullet restores it — a silent internal
contradiction that would cause a lint-check failure if any schema
validator were run.

**Source.** [context/beta:357-390] "All 5 expert §7 stubs have the
SAME header-vs-body numbering drift (header says §§6.2–6.10 but body
refers to §1..§9 matching shared-protocols.md §1..§9 which are SPEC
§6.1..§6.10). Brigadier alone has the correct SPEC §6.1..§6.10
reference." [context/zeta:81] "β discovered it's drifted. Integrator
resolves by: accept β's finding as primary evidence, downgrade α's
E-7 classification to partially-applied."

**Current state.** Five files carry `SPEC D6 §§6.2–6.10`:
`.claude/agents/engineering-expert.md:822`,
`.claude/agents/mgmt-expert.md:1295`,
`.claude/agents/systems-expert.md:1329`,
`.claude/agents/philosophy-expert.md:1276`,
`.claude/agents/investor-expert.md:1309`. The header claims §6.1 is
excluded; the body bullet-1 then references "§1 Wiki write protocol"
which IS §6.1. The contradiction is internally consistent enough for
human readers but will fail a `header-vs-body-alignment` lint check.

**Proposed improvement.**
- Files: all 5 listed above.
- Change: Replace `SPEC D6 §§6.2–6.10` with `SPEC D6 §§6.1..§6.10
  (= shared-protocols §1..§9)` in each §7 header line. Single-line
  edit per file; trivially verifiable with `grep "§§6.2–6.10"`.
- Also: add a `/lint` check #12 "shared-protocols import header parity"
  that fails if any agent §7 header does not contain `§6.1..§6.10`.

**Impact.** 2/5 — Removes silent internal contradiction; unblocks
future lint automation; closes the α's E-7 "partially-applied"
classification.

**Effort.** 1/5 — 5 single-line edits. Lowest effort fix in this
list.

**Risk.** 1/5 — Pure text correction; no behavioral change.

**Touched locks.** D6 (shared-protocols import contract), E-7
(§7 import-stub pattern), Q5 (/lint coherence), W-12 (1000% depth —
spec-to-disk fidelity).

---

### H-3: α-3 skill-promotion pipeline has 0 of 8 steps wired

**Statement.** The α-3 state machine (proposed → learning → active →
tombstoned) is fully specified in `.claude/skills/README.md` but every
operational step — from candidate-manifest write through golden-set
creation, usage logging, activation-predicate evaluation, symlink
creation, and tombstone — is unwired; the `swarm/wiki/skills/
{candidates,learning,active}/` directories are all empty.

**Source.** [context/epsilon:238-249] "8-step table: only 1 step
(broken-symlink /lint detection) has 'code present'; all 7 others are
'no'"; [context/epsilon:260-261] "Three competing spellings [of α-3
states], none authoritative"; [context/gamma:63] "D9 ratio: 0.0 —
Fully latent — no skill has been promoted yet"; [context/zeta:50-52]
"α-3 state drift IS γ /lint check with no input."

**Current state.** Zero candidates; zero golden-set JSONL; zero usage
JSONL; zero active symlinks in `.claude/skills/`; state-name
vocabulary has 3 competing spellings across README, lint.md, and this
task brief. The promotion pipeline is a contract with no consumer
(MP-4 per [context/zeta:114-118]).

**Proposed improvement.**
- File 1: `.claude/skills/README.md` — pick canonical 4-state names
  `{proposed, learning, active, tombstoned}` and update both the
  description table AND the `/lint` state-validity check.
- File 2: `.claude/skills/lint.md` — update state-validity check from
  `{candidate, learning, active, tombstoned}` to
  `{proposed, learning, active, tombstoned}`.
- File 3 (new): `swarm/wiki/skills/candidates/compound/manifest.md`
  — first candidate manifest (the `/compound` skill), with schema
  per D11: `slug, description, trigger, acceptance_predicate,
  golden_set_path, status: proposed`.
- File 4 (new): `swarm/lib/promote-skill.sh` (~40 lines; pure Bash)
  — moves a candidate from `candidates/<slug>/` to
  `learning/<slug>/`, creates stub `golden-set.jsonl`, appends to
  `usage/<slug>.jsonl`. Invokable by brigadier.

**Impact.** 4/5 — Unblocks the entire CE compounding loop; without
at least one wired step, no skill ever graduates from candidate to
active, and the "compound" (money step) never fires.

**Effort.** 2/5 — Vocabulary normalization: 2 file edits, ~10 lines.
First candidate manifest: ~20 lines. Bash mover: ~40 lines. Total
<100 lines.

**Risk.** 2/5 — Vocabulary change to `/lint` state-validity check may
surface false positives if any existing frontmatter uses the old names.
Mitigate: run grep for `status: candidate` across `swarm/wiki/` before
the change (expected: 0 hits given all dirs are empty).

**Touched locks.** Q6 (α-3 skill pipeline), D9 (symlink convention),
D11 (Q6 skill activation rubric), W-9 (skills first-class), R4 (Q6
owners), E-9 (4-part DRR discipline).

---

### H-4: role_tool_matrix is executable spec with zero executions

**Statement.** The `role_tool_matrix` in shared-protocols §5 defines
`<expert>-<mode>` write scope as `swarm/wiki/drafts/<task-id>-<expert>-*`
and `Bash=no; Task=no; MCP=no`, but nothing in the swarm actually
enforces these boundaries — no hook checks paths, no hook rejects
Bash, and the tool-permission self-check is a prose ritual not a
programmatic gate.

**Source.** [context/gamma:73] "Not mechanically enforced: nothing
blocks a cell writing outside `drafts/`. No pre-write hook. Brigadier's
§5.5.5 gate is manual"; [context/beta:73-76] "§8.5 AP table uses
5-column schema … but the AP codes (AP-1, AP-2, AP-3…) are *global
FPF codes* while expert tables use *local codes* (AP-ENG-*, …) — no
single canonical table cross-mapping"; [context/alpha:48] "mode-
scoping instruction is best-effort."

**Current state.** A cell could today execute a Write to
`swarm/wiki/foundations/swarm-alphas.md` (a canonical page, outside
the drafts/ scope) and brigadier would catch it only during the §5.5.5
manual review. The WLNK invariant (§4.1) is violated: the upstream
contract (role grants Write only to drafts/) is not enforced on the
downstream side.

**Proposed improvement.**
- File: `swarm/lib/hooks/write-scope-guard.sh` (~25 lines; pure Bash)
  — invoked from PostToolUse on Write; receives `(role, path)`;
  checks path against role's allowed `write_scope_glob` from
  `frontmatter.write_scope_glob` (already present in agent frontmatter
  per engineering-expert.md); returns `permission-denied` escalation
  JSON if out-of-scope.
- Wire to `.claude/settings.json` as a second PostToolUse handler
  (alongside the `/lint` handler from H-1).
- Extend `shared-protocols.md §5` with a one-line note: "The
  write-scope-guard hook enforces this matrix at tool-call time."

**Impact.** 4/5 — Converts Q2 single-writer from a discipline
contract to a mechanically-enforced invariant. Critical for Phase B
when multiple cells run concurrently.

**Effort.** 2/5 — ~25-line Bash script; JSON key addition; one-line
prose extension to shared-protocols. No new dependencies.

**Risk.** 3/5 — Frontmatter `write_scope_glob` field is already in
engineering-expert.md but may not be uniformly present in all 5
expert frontmatters. Mitigate: verify presence with grep before
enabling; add `write_scope_glob: "swarm/wiki/drafts/<task-id>-<expert>-*"`
to any expert file that lacks it (a ≤2-line frontmatter addition).

**Touched locks.** Q2 (single-writer), D6 (§5 tool-permission), W-8
(workflow contract), E-14 (scope walls), AP-ENG-6 (cells-calling-
cells), R8 (5 T-tensions as specification-level).

---

### H-5: Golden-set / eval harness is entirely absent — §6.3 convergence unmeasurable

**Statement.** The §6.3 Phase-B convergence criterion ("Phase B beats
Phase A on ≥3 of 5 metrics: Δturns, ΔHITL, ΔRuslan-rating, Δgolden,
Δtime") is structurally unmeasurable because no baseline has been
recorded, no golden-set JSONL files exist, and no eval runner is
wired; every `ratio: {hits: 0, misses: 0}` in strategies.md starts at
zero because no cycle has run.

**Source.** [context/alpha:50-52] "Golden sets per cell are empty …
≥20 Hamel-labelled examples per mode per cell = 400 labels minimum,
none authored"; [context/alpha:52] "Phase B recursive self-improvement
has no convergence metric pre-committed … delta is unmeasurable";
[context/epsilon:244-248] "the ✓/✗ ratio is not linked to any test
runner; golden-set format unspecified beyond 'JSONL' — no schema, no
fields, no pass/fail definition"; [context/zeta:109-112] "MP-3
'Measurement void' across α+γ+δ+ε. Same empty substrate."

**Current state.** `swarm/wiki/skills/candidates/` empty;
`agents/*/strategies.md` either missing or containing 0 DRR entries;
`meta/health.md` has 5 live counters all frozen at 0;
`swarm/evals/` directory does not exist.

**Proposed improvement.**
- File 1 (new dir): `swarm/evals/<cell-id>/` — one directory per cell,
  e.g. `swarm/evals/engineering-critic/`.
- File 2 (new schema): `swarm/evals/schema.md` — defines the JSONL
  record shape: `{input_path, expected_output_path, acceptance_predicate
  (Hamel-binary), actual_output_path?, pass?, notes?}`.
- File 3 (new): `swarm/evals/engineering-critic/golden-set.jsonl` —
  seed with 3 entries drawn from THIS cycle (input = this task's
  context files; expected = this artefact; predicate = acceptance
  predicate in frontmatter above). 3 entries is below the ≥20 floor
  but creates the substrate; brigadier adds 3 per cycle → 20 in ~6
  cycles.
- File 4 (new): `swarm/lib/eval-runner.sh` (~60 lines; pure Bash +
  Python stdlib) — reads a cell's `golden-set.jsonl`, runs each case,
  appends pass/fail to `swarm/evals/<cell>/results.jsonl`.

**Impact.** 5/5 — Without this, Phase B is unmeasurable and the
entire compounding loop has no feedback signal. This is the
measurement-void fix (MP-3 per [context/zeta:109-112]).

**Effort.** 3/5 — Schema: 1 file (~20 lines). Directory structure:
trivial. First golden-set seed: ~1 hour (3 JSONL records). Eval
runner: ~60 lines. Moderate total.

**Risk.** 2/5 — Eval runner produces results.jsonl that could be
misread as "test results" and treated as authoritative before the
golden-set is large enough. Mitigate: add a `min_entries: 20` check
in eval-runner.sh that emits a warning (not failure) when below floor.

**Touched locks.** D11 (Q6 skill activation rubric), Q6 (golden-set),
E-3 (critic rubric Conformance), W-5 (two-level CE), R2 (4-tier
retrieval Phase A), AP-ENG-5 (tool-eval without eval-dataset).

---

### H-6: α-3 state-name vocabulary has 3 competing spellings — lint rejects valid states

**Statement.** The α-3 skill lifecycle states have three incompatible
spellings across three authoritative files:
`.claude/skills/README.md` uses `{proposed, active, validated,
tombstoned}`; `.claude/skills/lint.md` enforces `{candidate, learning,
active, tombstoned}`; this task brief uses `{proposed, learning,
validated, archived}` — any skill promotion that fires will
immediately fail the `/lint` state-validity check because no single
canonical set is agreed upon.

**Source.** [context/epsilon:224-236] "specification drift between:
(a) README §'α-3 4 states' [README:87-90] … (b) /lint state-validity
check which flags states ∉ {candidate, learning, active, tombstoned}
… (c) the D2 §2.4 Layer 8 reference. This is a gate-1 critic issue";
[context/zeta:79] "T-1. γ vs ε on α-3 state vocabulary — both
extractions observe drift but describe different canonical sets.
Phase-2 integrator must pick ONE canonical set BEFORE any skill
promotion fires."

**Current state.** 3 files disagree; 3 incompatible canonical sets.
Any skill that moves to state `proposed` per README conventions will
be rejected by `/lint` which does not know `proposed`. IDEM invariant
(§4.1) is violated: applying `/lint` twice to the same skill file
produces different results depending on which spelling was used.

**Proposed improvement.**
- Canonical set decision (HITL-gated, per §1d requires-approval):
  adopt `{proposed, learning, active, tombstoned}` per [context/epsilon
  :290] recommendation (Voyager-style lifecycle mapping).
- File 1: `.claude/skills/README.md` — update §"α-3 4 states" to use
  `proposed` (not `active`) for the first state; update the promotion
  worked example [README:136-155].
- File 2: `.claude/skills/lint.md` — update state-validity check from
  `{candidate, learning, active, tombstoned}` to `{proposed, learning,
  active, tombstoned}`.
- File 3: `swarm/wiki/foundations/swarm-alphas.md` — update α-3 state
  table rows to match canonical set (currently says `validated`; change
  to `active`). This is a foundation-revision → requires HITL ack.

**Impact.** 3/5 — Blocking bug for the entire α-3 pipeline; no skill
ever reaches a consistent terminal state until this is resolved.

**Effort.** 1/5 — 3-file edit, ~10 lines total. But requires HITL
ack for the `swarm-alphas.md` foundation revision.

**Risk.** 2/5 — Vocabulary change may silently invalidate existing
frontmatter in future artefacts that use the old terms. Mitigate:
grep `swarm/wiki/` for `status: candidate|validated|archived` before
the change (expected: 0 hits in Phase A).

**Touched locks.** D5 (5 swarm-alpha state machines), Q6 (α-3 skill
pipeline), D11 (Q6 skill activation rubric), W-9 (skills first-class).

---

### H-7: Draft path slug template has 3 inconsistent shapes across 5 experts

**Statement.** The draft output path template — the primary key by
which brigadier identifies and promotes an expert's draft — has three
distinct shapes across five experts (`<task-id>-engineering-<mode>-
<slug>.md` vs `<task-id>-systems-<artefact>.md` vs `<task-id>-
philosophy-<mode>-<artefact>.md`), making brigadier's §5.5.5
provenance-gate path-validation unautomatable without per-expert
special-casing.

**Source.** [context/beta:256-264] "R-3 (inconsistency). Draft path
slug template varies. engineering: `<task-id>-engineering-<mode>-
<slug>.md` [824]; mgmt: `<task-id>-mgmt-<mode>-<slug>.md` [1298];
systems: `<task-id>-systems-<artefact>.md` [1331] — no mode segment;
philosophy: `<task-id>-philosophy-<mode>-<artefact>.md` [1279];
investor: `<task-id>-investor-<mode>-<artefact>.md` [1312]. Three
distinct shapes. `/lint` would not catch; brigadier promotion gate
would not catch."

**Current state.** Systems-expert.md uses a 3-segment slug (no
`<mode>` segment). Philosophy and investor use `<artefact>` instead of
`<slug>`. The canonical 5-segment form `<task-id>-<expert>-<mode>-
<slug>.md` from engineering and mgmt is the clearest (includes mode
for quick grep) but is not uniform.

**Proposed improvement.**
- Files: `systems-expert.md §7` (line ~1331) + `philosophy-expert.md
  §7` (line ~1279) + `investor-expert.md §7` (line ~1312) and any §9
  path-template examples in those same files.
- Change: replace non-canonical path shapes with
  `<task-id>-<expert>-<mode>-<slug>.md` (5-segment).
- Additional: add a `/lint` check #13 "draft-path shape parity"
  that runs `grep -r "swarm/wiki/drafts/" .claude/agents/ | grep -v
  "<task-id>-<expert>-<mode>-<slug>"` and fails on any mismatch.

**Impact.** 2/5 — Not a runtime bug today (no drafts have been
promoted yet); becomes a blocking bug the moment two experts produce
drafts in the same cycle and brigadier needs to batch-promote by path
pattern.

**Effort.** 1/5 — 3-file text edits + 5-line lint extension.

**Risk.** 1/5 — Pure documentation change; no runtime impact.

**Touched locks.** D6 (shared-protocols §1 wiki-write), Q2 (single-
writer), W-12 (1000% depth — spec-to-disk fidelity).

---

### H-8: systems-expert §8 AP table missing cells-calling-cells row

**Statement.** Systems-expert §8 anti-pattern table has 10 rows and
lacks an AP-SYS-cells-calling-cells entry; the four other experts
(engineering AP-ENG-6, mgmt AP-MGMT-6, philosophy AP-PHIL-12, investor
AP-INV-14) all carry this row; its absence in systems-expert means a
systems cell that accidentally attempts a peer cell invocation will
have no in-body AP to trigger, leaving only the tool-permission
frontmatter as a backstop (which is itself unenforced per H-4).

**Source.** [context/beta:155-158] "§8 has NO explicit cells-calling-
cells AP row (engineering has AP-ENG-6, mgmt AP-MGMT-6, philosophy
AP-PHIL-12, investor AP-INV-14; systems omits)"; [context/beta:304-305]
"systems is notably light AND missing cells-calling-cells row (see
S-4)"; [context/beta:457-459] "S-4. Add cells-calling-cells AP row to
systems-expert §8."

**Current state.** `systems-expert.md §8` has 10 domain-specific AP
rows; AP-SYS-11 (cells-calling-cells) is absent. The detection rubric
for the AP (this expert lacks Task tool by frontmatter — surfaces as
tool-permission-self-check failure) is shared across all experts and
lives in shared-protocols §5; the expert-specific AP row exists to
surface the compound rule_slug in the Compound step.

**Proposed improvement.**
- File: `.claude/agents/systems-expert.md` §8 table, after current row
  10 (approximately line 1366).
- Change: insert one AP row following the AP-ENG-6 pattern:
  `AP-SYS-11 cells-calling-cells | systems cell directly invokes
  peer expert cell via Task() or tool call | count(Task() calls
  in systems cell output with target = peer expert) > 0 | pause
  (return refusal; this expert lacks Task tool by frontmatter) |
  cell-no-direct-peer-invocation`.

**Impact.** 2/5 — Defensive coverage; runtime impact only if a
systems cell is accidentally dispatched with a Task tool grant.
Important for completeness but not blocking Phase A.

**Effort.** 1/5 — 5-line table row addition.

**Risk.** 1/5 — Additive-only change; no breaking effect.

**Touched locks.** E-8 (≥8 domain-specific AP rows), E-14 (scope
walls), FPF §3.2 L436 (cells never call cells), AP-ENG-6 (cross-
reference pattern).

---

### H-9: Provenance gate §5.5.5 is narrative pseudocode with no executor

**Statement.** The provenance gate shared-protocols §2 defines 6
acceptance conditions and 5 REJECT cases in narrative pseudocode; no
Bash/Python script or PostToolUse hook runs the gate; brigadier's §5.5.5
ritual is manual discipline; the first real cycle that produces a
spine artefact will expose whether brigadier actually runs the 9-step
ritual or silently skips it.

**Source.** [context/gamma:181-211] "Status: conceptual, not
operationally wired. Pseudo-code 'brigadier verification ritual'
exists … but there is no Bash/Python/hook that runs it. No PostToolUse
hook is wired in .claude/ to intercept a Write and run /lint dry-run."
[context/gamma:209-211] "The gate is a design, not a runtime. The
first real swarm cycle that produces a spine artefact will expose
whether the brigadier actually runs the 9-step ritual."

**Current state.** `swarm/lib/shared-protocols.md:61-129` holds the
spec. No `swarm/lib/provenance-gate.sh` or equivalent exists. The
`swarm/wiki/tasks/<task-id>/decisions/` directory for the current task
is empty — no rejection records have ever been written.

**Proposed improvement.**
- File (new): `swarm/lib/provenance-gate.sh` (~80 lines; pure Bash)
  — reads a candidate wiki file path; checks: (1) sources[] non-empty
  via frontmatter grep; (2) path resolves to a valid tier; (3) no
  existing accepted page has an unresolved contradiction; (4) if
  type=foundation, confidence_method in {ruslan-attested, brigadier-
  attested-with-3-supports}. Returns exit code 0 (pass) or 1 (fail
  with REJECT reason written to stderr). Invoked by brigadier manually
  OR by PostToolUse hook from H-1.
- Wire: brigadier §5.5.5 prose updated to reference `./swarm/lib/
  provenance-gate.sh <path>` as the gate executor; prose pseudocode
  stays as documentation but the script is the canonical check.

**Impact.** 4/5 — Without this, every write to canonical wiki is
trust-based; the first inconsistency will not be caught until a human
reads the page.

**Effort.** 3/5 — 80-line script; moderate complexity (frontmatter
parsing + path validation + sources check). No new dependencies if
done in pure Bash + `grep`/`awk`.

**Risk.** 3/5 — Bash frontmatter parsing is fragile (multi-line YAML
values, nested lists). Mitigate: scope to simple scalar fields (sources
non-empty, confidence_method string match, type string match); defer
edge-consistency check to the PostToolUse /lint hook (H-1).

**Touched locks.** Q2 (single-writer), D6 (shared-protocols §2), W-8
(workflow = FPF + versioning), E-3 (critic Conformance), Q5 (/lint
enforcement).

---

### H-10: Horizon-gate discrepancy — investor has €50K baseline; four peers do not

**Statement.** Investor-expert §6.0 specifies a €50K baseline gate
that does not appear in the other four experts' §6.1 horizon tables or
in brigadier §4.6 row 4; if the €50K gate fires a BOSC-A-T-X event
in investor's projection, the other four experts' scalability analyses
will be misaligned by one gate, producing inconsistent cross-cell
integration in any integrator-mode synthesis that spans all five
experts.

**Source.** [context/beta:287-291] "R-5 (inconsistency). Horizon-gate
set. Investor §6.0 names `€50K baseline / €200K / €1M / $100M / $1T`
… other 4 experts + brigadier §4.6 name `€200K / €1M / $100M / $1T`
(4 gates). The €50K baseline appears in investor-expert.md:179 ('Brief
§5.1 horizon-gate (€50K → $1T)') but NOT in brigadier §4.6 row 4."
[context/beta:462-466] "S-5. Resolve €50K horizon-gate discrepancy …
Decision: HITL — the Brief §5.1 horizon-gate spec is authoritative;
align to spec."

**Current state.** Five files (brigadier.md + 4 non-investor expert
files) use a 4-gate set; investor-expert.md uses a 5-gate set. Brief
§5.1 (master synthesis) is the authoritative source; its exact gate
set is not verifiable from Phase-A context files alone — a HITL
decision is needed.

**Proposed improvement.** This is a HITL-gated decision (brigadier
§1d requires-approval: "horizon-gate shift"); engineering can only
surface it. Two options for Ruslan:
- Option A: Add €50K to all four non-investor expert §6 horizon tables
  and brigadier §4.6 row 4 (5 files, ~5-line each).
- Option B: Remove €50K from investor §6.0, making all five experts
  consistent at 4 gates.
Engineering recommendation: Option A (the €50K gate is strategically
meaningful for investor-expert's early-stage capital analysis; other
experts' scalability projections gain granularity).

**Impact.** 2/5 — Not immediately blocking; becomes an integration
bug the first time an integrator-mode synthesis compares scalability
projections across all five cells.

**Effort.** 1/5 — Once HITL decides: 5-file text addition (~5 lines
each).

**Risk.** 1/5 — Additive; no behavioral change to existing logic.

**Touched locks.** E-6 (BOSC-A-T-X triggers), D5 (swarm-alpha state
machines linked to horizon gates), Q2 (single-writer — brigadier
writes the alignment after HITL acks).

---

## §5 Alternatives (≥2)

### Alternative A: Executor-first sprint (H-1, H-3, H-5 bundle)

Deploy hooks + α-3 mover + eval harness as a single 3-day sprint
before any other engineering work. This collapses H-1/H-3/H-5 into
one PR; the hook layer enforces mode-prefix and write-scope while the
eval harness starts capturing baseline metrics.

**Kill condition.** Fails if `.claude/settings.json` hook API is not
available in the current Claude Code build (verify: check docs for
`UserPromptSubmit` hook support; if absent, fall back to a
manual-validation script invoked at session start). Also fails if
the Bash frontmatter parser in H-9's provenance-gate.sh cannot handle
multi-line YAML — in that case, scope the gate to scalar-only fields
and log a deferred TODO for full YAML parsing.

### Alternative B: Text-fixes first (H-2, H-6, H-7, H-8 bundle)

Fix all documentation-level inconsistencies (SPEC numbering, α-3
vocabulary, draft slug templates, missing AP row) before writing any
new scripts. Total effort: ~30 lines of text edits across 8 files.
Delivers clean-slate inputs for the executor sprint.

**Kill condition.** Fails if H-6 (α-3 vocabulary) requires a HITL ack
for `swarm-alphas.md` foundation revision and HITL does not respond
within the Phase A window. In that case, proceed with H-2/H-7/H-8
text fixes and park H-6 until ack.

### Alternative C (status quo): Defer all fixes to Phase B

Accept that Phase A is a specification phase; all hooks, evals, and
vocabulary fixes fire in Phase B when at least one cycle has run and
the patterns are empirically confirmed.

**Kill condition.** Fails if even one real cycle attempt reveals that
the soft-prefix AP-5 surfaces actually corrupt a cell's output (e.g.
a cell receives a prompt without `mode:` prefix and defaults to
integrator when critic was intended). Status quo breaks on first real
adversarial test of the activation gates.

---

## §6 Anti-scope

- **Not evaluating capital impact.** "What is the ROI of the hook
  sprint in EUR?" is investor-expert territory. Engineering surfaces
  the effort rating (1-5); investor computes the return.
- **Not evaluating priority sequencing.** "Should we fix H-2 before
  H-1?" is mgmt-expert territory. Engineering rates impact/effort;
  mgmt owns the delivery sequence.
- **Not arbitrating the α-5 Direction choice.** "Should Jetix adopt
  TDD?" is an α-5 human-only Direction. Engineering implements once
  Ruslan decides the direction.
- **Not authoring system-feedback-loop models.** "What does the
  CE compounding loop do to developer velocity over 50 cycles?" is
  systems-expert territory.
- **Not evaluating the MAST failure taxonomy against these findings.**
  That is a cross-domain synthesis; if needed, brigadier dispatches
  an integrator pass combining this critic output with systems ×
  scalability output.
- **Not optimizing.** This is a critic pass; proposed improvements
  name the change and effort but do not produce diffs. Brigadier should
  dispatch `engineering × optimizer` on any hypothesis that clears the
  impact ≥ 3 AND effort ≤ 2 threshold.
- **Not evaluating networkx licensing / third-party library status.**
  That is a HITL (legal/procurement) decision; engineering notes that
  `networkx` is pure-Python (no SDK) and defers the approval.

---

## §7 Provenance

All non-trivial claims cite the context file and line range. No source
body has been inlined beyond 5 continuous lines.

| Source | Lines used | Purpose |
|---|---|---|
| context/alpha-agent-construction-corpus.md | 46-77, 86-101 | Thin-spots table, E-items map, 2× surfaces |
| context/beta-current-agents.md | 24-42, 228-306, 343-390, 432-490 | TL;DR, cross-agent redundancies, §7 audit, improvement surfaces |
| context/gamma-wiki-v3.md | 46-49, 68-80, 132-158, 181-211 | D/Q/R status table, retrieval stack, provenance gate |
| context/delta-memory-sota.md | 22-40, 59-82, 174-198 | TL;DR, HippoRAG PPR, retrieval stack contrast |
| context/epsilon-skills.md | 41-56, 87-158, 224-262, 264-286 | TL;DR, skill audit, α-3 state machine, improvement surfaces |
| context/zeta-cross-pollination.md | 44-75, 93-118, 121-153 | Cross-domain matrix, meta-patterns, unexpected connections |
| swarm/lib/shared-protocols.md | 1-60 | §2 provenance gate spec, §5 role_tool_matrix |

---

## §8 Structured-output packet (shared-protocols §3)

```yaml
mode: critic
summary: >
  Phase-A swarm is over-specified / under-executed. 10 hypotheses
  surfaced (8 primary + H-9/H-10 bonus). Top finding: hook layer absent
  (H-1); §7 SPEC off-by-one in 5 of 6 agent files (H-2); α-3 pipeline
  0 of 8 steps wired (H-3). All 8 §3.1 Conformance checks produced
  failures. 2 alternatives + anti-scope included. No canonical wiki
  writes proposed; artefact lands in tasks/ per write_scope_glob.
proposed_writes:
  - path: swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01.md
    frontmatter:
      id: engineering-critic-01
      type: artefact
      produced_by: engineering-expert-critic
      mode: critic
      state: drafted
      pipeline: ingested
      confidence: medium
      confidence_method: rubric-pass-rate
    body: "<this file — see §1..§7 above>"
    edges_to_add:
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01", to: "tasks/T-swarm-self-improve-v1-2026-04-23", type: part_of}
      - {from: "tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/engineering-critic-01", to: "lib/shared-protocols", type: derived_from}
provenance:
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/alpha-agent-construction-corpus.md", range: "46-77"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/beta-current-agents.md", range: "228-390"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/gamma-wiki-v3.md", range: "46-211"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/delta-memory-sota.md", range: "22-82"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/epsilon-skills.md", range: "41-262"}
  - {path: "swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/context/zeta-cross-pollination.md", range: "44-153"}
  - {path: "swarm/lib/shared-protocols.md", range: "1-60"}
confidence: medium
confidence_method: rubric-pass-rate
escalations:
  - trigger: peer-input-needed
    note: >
      H-10 (horizon-gate discrepancy) requires a HITL decision between
      Option A (add €50K to 4 experts) and Option B (remove from investor).
      Brigadier should add this as an AWAITING-APPROVAL gate item before
      the next integrator pass on scalability outputs.
  - trigger: peer-input-needed
    note: >
      H-6 (α-3 vocabulary) requires a foundation-revision of
      swarm/wiki/foundations/swarm-alphas.md — this is a requires-approval
      action per §1d; brigadier should author the gate packet and wait for
      HITL ack before proceeding with the vocabulary normalisation.
dissents: []
```
