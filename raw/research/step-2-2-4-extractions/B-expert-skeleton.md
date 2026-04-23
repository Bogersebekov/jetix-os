---
title: Sub-agent B — Expert 9-Section Skeleton + FPF 8-Block Structural Enhancement
date: 2026-04-23
extraction_for: prompts/step-2-2-4-agent-construction-2026-04-23.md
sources:
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md (§5.2.1, §5.3, §5.5, §5.6)
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Part 1 E-1..E-11, Part 10 §10.1, §10.2)
status: ready-for-orchestrator-consumption
sub_agent: B
---

## 1. The 9-section expert skeleton (verbatim from §5.2.1)

File: `agents/<expert>/system.md`. Total target ≤ 2,500 lines (FPF Gate-2 cap, FPF Part 9 §9.7); base directive 1,500–3,000 (MS §5.2 header). Per-section budgets verbatim from MS §5.2.1:

| § | Name | Mandate (one-sentence) | Budget (lines) |
|---|---|---|---|
| §1 | Identity + canonical domain | Declare expert as `<domain>`-expert, list canonical sources verbatim from ALIGN §2, declare what is OWNED vs NOT-OWNED. | 80–120 |
| §2 | Primary domain knowledge | Frameworks (deep), decision heuristics, canonical quotes (verbatim, sourced), known failure modes, cross-reference table. | 800–1,200 |
| §3 | Mode: critic | Activation check on `mode=="critic"`; adversarial Hamel-binary rubric; failure-pattern library; 3–5 few-shots; escalation conditions; output schema {context, critique, specific-failures, recommended-changes, acceptance-test}. | 300–500 |
| §4 | Mode: optimizer | Activation check; measurable-delta rubric (turns / tokens / complexity / LoC); Ousterhout / Boris / Poppendieck simplification heuristics; 3–5 few-shots; refusal conditions; schema {baseline, proposed, delta, justification, risks}. | 300–500 |
| §5 | Mode: integrator | Activation check; integration rubric (all inputs accounted, dissents surfaced, synthesis verifiable); Cagan / Senge / Anthropic Orchestrator-Workers heuristics; dissent-preservation (AP-6); schema {inputs, synthesis, dissents-flagged, residual-open-questions, recommended-next-step}. | 300–500 |
| §6 | Mode: scalability-architect | Activation check; ≤30 % refactor / 10× gate; West scaling laws / Beer VSM / Taleb; horizon table €50K → €200K → €1M → $100M → $1T; schema {horizon, projection, gate-risk-table, degraded-mode-spec, antifragility-check}. | 300–500 |
| §7 | Shared protocols | How to write to wiki (§5.5), structured-output rules (§5.3), HITL escalation, cross-cell reference, tool-permission self-check; identical text across all 5 experts (always active). | 150–200 |
| §8 | Anti-pattern awareness | Domain-specific APs from §2 + cross-cutting AP-1..AP-26; what to emit on detection. | 100–150 |
| §9 | strategies.md reading protocol | On every invocation read `agents/<expert>/strategies.md` first; prioritise by ✓/✗ ratio; ignore tombstoned rules. | 30–50 |

Lower-bound sum 2,460 lines / upper-bound 4,520. The FPF enhancements below trim §2's upper bound and absorb new structure inside existing budgets, holding total ≤ 2,500.

## 2. The FPF 8-block structure mapped onto the 9 sections

The 8-block FPF manifest (Blocks 1a, 1b, 2-as-method-body, 3-as-rubric-bodies, 4 graph-of-creation, 5 seniority, 6 implementation-AI, 7 implementation-human, 8 evolution) is woven into the 9-section frame as follows. Per FPF Part 10 §10.1 + §10.2.

- **§1a Identity (frontmatter, Block 1)** — sits at top of file, machine-parseable. Contents: `name`, `description`, `model`, `granularity` (jetix-business / jetix-life-os / jetix-shared / task-scoped — E-16), `owner`, `created`, `version` (SemVer). E-1 + E-16 lock this block. Good looks like: a YAML head identical-shape across all 5 experts so meta-agent can `grep -A 8 '^---'` and parse without per-file logic.

- **§1b Ontological (frontmatter, Block 2)** — directly under §1a, still in frontmatter. Fields: `primary_alpha`, `secondary_alphas[]`, `self_assertive_scope`, `integrative_obligation` (Janus pair, E-11), `possible_tasks[]`, `out_of_scope_tasks[]` (constructor-theory cut, E-14), `purpose`, `target_system`, `accountabilities[]` (≤7), `acceptance_criteria[]`. E-1 + E-11 + E-14 + E-16 lock this block. Good looks like: every field declarative and verifiable from `swarm/wiki/foundations/swarm-alphas.md`; method-signature, not job blurb.

- **§1c Graph-of-Creation (after §1 identity body, Block 4)** — `produces:` and `consumes:` arrays declaring artefacts (with `states`, `consumers`, `produced_by`, `required` flags) plus `artefacts-produced` typed list (Framework / Heuristic / Quote-set / Rubric / Template). E-12 locks the brigadier instantiation; the same shape is mandated for all experts by FPF §10.1 / §10.2 item 3. Good looks like: `grep -r "produces:\|consumes:" .claude/agents/ | parse_to_dot` regenerates the swarm dependency DAG without any prose.

- **§1d Seniority/Scale (after §1c, Block 5)** — `current_level`, `decision_rights: {autonomous, requires-approval, never}`, `escalation_trigger`, `split_trigger`. All Phase-A experts at `phase1-solo`. Universal `never:` — direct wiki commit, external comms, edit `.claude/agents/`, call another cell, perform strategizing. FPF §10.1 [E-12 envelope] + §10.2 item 4 lock this. Good looks like: an explicit "what I will refuse autonomously" list that the brigadier can quote when bouncing scope-creep.

- **§2 Primary Domain — augmented with Ontological-Spine sub-section per E-2** — 50–80 lines (out of the 800–1,200 §2 budget) that declare: (a) primary alpha of this domain with state graph (past-participle states, transitions-with-movers, per-state acceptance checklist), (b) 5–10 domain-critical concepts as `U.Kind` or `U.Episteme.SlotGraph` anchors with Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did precedence, (c) cross-ref table using **typed A.14 edges** (`ComponentOf` / `ConstituentOf` / `PortionOf` / `PhaseOf` / `MemberOf`) instead of flat "part-of". Middle-path discipline (E-18): do NOT bolt on the full A.17–A.21 Characteristic Space cluster — Phase B only.

- **§§3–6 Four Modes — augmented with E-3 / E-4 / E-5 / E-6** — each of the four mode-bodies retains its existing 300–500-line budget but inserts a small structured rubric block at the top:
  - §3 critic gets the 4-row mandatory rubric (Conformance Checklist / Acceptance Predicate / ≥2 Alternatives / Anti-scope) plus stripped-down D.5 BA-Cycle (BA-0..BA-3) for mgmt-expert + investor-expert.
  - §4 optimizer gets the invariant-check row (WLNK / MONO / IDEM / COMM / LOC) above proposed-delta, plus method-change refusal clause.
  - §5 integrator augments output schema with per-claim `F:` (formality F0..F9), `ClaimScope:`, `R:` (pathwise reliability) declarations, plus dissent-record typing.
  - §6 scalability adds BOSC-A-T-X trigger check per horizon and Janus-keyed degraded-mode spec (Koestler 9.4 S-A excess + 9.5 INT excess).

- **§7 Shared Protocols — 20-line import stub (E-7)** — body shrinks from 150–200 lines of duplicated text to a 20-line stub that imports `swarm/lib/shared-protocols.md`. NO content duplication. Tool tokens renamed: "YAML frontmatter" → "Frontmatter"; "git commit" → "snapshot"; "pre-commit hook" → "local gate". E-7 + E-10 lock. Good looks like: a literal 20-line block that 5 experts share verbatim and any change ships from the library file.

- **§8 Anti-patterns — 5-column table with ≥ 8 rows (E-8)** — replaces the 100–150-line prose section with a structured table. Columns: AP code / Trigger signal (observable, past-participle) / Detection rubric (binary) / Response action (pause / escalate / integrate / tombstone) / strategies.md compound-step rule-slug. Minimum 8 domain-specific rows in addition to global AP-1..AP-26 cross-reference. Good looks like: every row pasteable into a hook-actionable detector.

- **§9 Strategies.md protocol — 4-part DRR (E-9) + Block 6 + Block 7 + Block 8** — body lists the DRR entry shape (context / decision / alternatives-considered / review-checkpoint), then end-of-§9 hosts:
  - Block 6 Implementation AI sub-block (`current-executor`, `prompt-file`, `eval-dataset`, `eval-passing-threshold`, `tools-allowed`, `forbidden-tools`, `context-window-budget`, `memory-strategy`, `upgrade-policy`).
  - Block 7 Implementation Human sub-block (`hired-person: null`, `onboarding-path`, `reporting-to`, `performance-kpis`, `handoff_from_ai.triggers`).
  - Block 8 Evolution sub-block at end-of-file (`created-at`, `last-updated`, `changelog[]` SemVer, `expected-evolution` for cycle-10/50/200, `last_review`).

All 8 blocks present + the 9 sections mapped — yields the FPF success predicate (FPF §10.8 item 2: "Each file has all 7 structural blocks (1a, 1b, 2, 3–6 modes, 7, 8, 9)").

## 3. E-1..E-11 detailed insertion map

| ID | Source (FPF §) | Summary (≤ 60 words) | Insertion site in 9-section skeleton |
|---|---|---|---|
| E-1 | §2.1 | Split §1 into §1a Identity (slug, version, layer, status) + §1b Ontological (purpose, target-system, primary-alpha, secondary-alphas, accountabilities ≤7, out-of-scope, acceptance-criteria). Identity becomes machine-parseable; ontological becomes a method signature. | Frontmatter (top of file, before §1 prose). |
| E-2 | §2.2 | Add a 50–80-line Ontological-Spine sub-section inside §2: domain primary-alpha with past-participle state graph + 5–10 U.Kind/U.Episteme.SlotGraph anchors + cross-ref table using typed A.14 edges (ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf). | Inside §2 Primary domain knowledge, opening sub-section. |
| E-3 | §2.3 | Critic rubric MUST have 4 explicit rows: Pattern-contract Conformance Checklist; Acceptance Predicate (Hamel-binary); ≥2 Alternatives + status quo with kill-conditions; Anti-scope. For mgmt-expert + investor-expert add stripped D.5 BA-Cycle (BA-0..BA-3) sub-rubric. | Top of §3 Mode: critic, before failure-pattern library. |
| E-4 | §2.4 | Optimizer rubric adds invariant-check row (WLNK / MONO / IDEM / COMM / LOC) before any proposed delta + explicit refusal: cannot optimize a Method (capital-M) — that is strategizing, escalate. | Top of §4 Mode: optimizer, before simplification heuristics. |
| E-5 | §2.5 | Integrator output schema adds per-claim `F:` (formality F0 rumour … F9 formal proof), `ClaimScope:` (bounded context), `R:` (pathwise reliability). Phase-A: integrator declares them, does not compute. Dissent-record typing: tag each dissent (F, ClaimScope, R) and preserve rather than average when F-levels diverge. | Inside §5 Mode: integrator output schema; dissent sub-block. |
| E-6 | §2.6 | Scalability rubric adds MHT-trigger check: for each horizon (€200K, €1M, $100M, $1T) name BOSC-A-T-X trigger that activates + the MHT event the swarm undergoes (Fission / Phase Promotion / Role-Lift / Fusion / Context Reframe) + degraded-mode spec keyed to Janus failure modes (Koestler 9.4 S-A excess; 9.5 INT excess). | Inside §6 Mode: scalability-architect rubric + degraded-mode block. |
| E-7 | §2.7 | Extract §7 to single canonical `swarm/lib/shared-protocols.md`; each expert's §7 = 20-line import stub (kills 5-copy maintenance). Rename tooling tokens to pattern-layer abstractions (Frontmatter / snapshot / local gate) — Core/Tooling soft split. | §7 Shared protocols, replaces prose body. |
| E-8 | §2.8 | §8 becomes structured 5-column table (AP code / Trigger / Detection rubric / Response action / strategies.md slug). Mandatory minimum 8 domain-specific APs per expert in addition to the global AP-1..AP-26 cross-reference. | §8 Anti-pattern awareness, replaces summary prose. |
| E-9 | §2.9 | Standardize strategies.md entries to 4-part DRR (context / decision / alternatives-considered / review-checkpoint). Add Evolution sub-block in §9: changelog SemVer-per-entry, `last_review`, `expected-evolution` milestones (10 / 50 / 200 cycle forecasts). | §9 strategies.md protocol — entry-format spec + Evolution sub-block at end. |
| E-10 | §5.3 | Add `mode: writing-support` clause inside §7 (shared protocols) for all 5 experts. Refuses primary-prose generation in weekly-review / quarterly-letter / strategizing artefacts. Returns: structured extractions, enumerated alternatives, anti-scope. Human owns composition. | §7 Shared protocols, sub-clause. |
| E-11 | §10.1 (per Janus / R-E §7.1 A) | §1b adds explicit Janus pair: `self_assertive_scope` (autonomous decision envelope) and `integrative_obligation` (what this expert MUST surface to brigadier / other cells). Prevents both S-A excess (monopoly) and INT excess (groupthink). | Frontmatter §1b Ontological. |

## 4. Mode activation mechanic (soft + hard)

Per MS §5.2.2 + FPF E-3..E-6, mode activation has two channels:

**Soft (prompt-prefix, in-model).** First line of §1 body reads: "If `mode` in context is not set → treat as `integrator` (default). Read only §1 + §2 + §<matching mode> + §7 + §8 + §9. Skip other modes." Brigadier always concatenates an explicit mode-selector prefix (e.g. `[mode: critic]`) into the Task() invocation; the model honours it via the §1 directive. This is best-effort — AP-5 forbids relying on prompt-level prohibitions alone.

**Hard (UserPromptSubmit hook, out-of-model).** Per MS §5.2.2 Option-A and §5.6.4: a Claude Code `UserPromptSubmit` hook scaffolded in `.claude/settings.json` inspects the incoming prompt: (a) parses the leading `[mode: <enum>]` token; (b) verifies it against the expert's frontmatter `accountabilities[]` + `possible_tasks[]`; (c) refuses launch if the mode is unsupported for that expert (e.g. `mgmt-expert + mode: scalability` on a pure-engineering artefact) — refusal returns an HITL bounce per shared-protocols §4 rather than executing.

**What §§3–6 of each agent file MUST SAY about mode activation.** Each mode body opens with a fixed three-line contract (NOT the hook implementation — the hook is a `.claude/settings.json` stub):

1. **Activates when:** `mode == "<this-mode>"` AND artefact-type ∈ {<applicable types from §1b possible_tasks>}.
2. **Predicate:** "<one-line acceptance test the output must pass — Hamel-binary>".
3. **Refuses with:** "Mode `<X>` not supported for artefact `<Y>` — bouncing to HITL via shared-protocols §4." (Refusal payload includes the cycle_id + the unsupported (mode, artefact) pair so brigadier can reroute.)

This contract is identical-shape across all 4 modes and all 5 experts — only the predicate text differs by mode/expert.

## 5. §7 Shared Protocols — 20-line import stub template

Every expert's §7 uses this template verbatim — 20 lines, no content duplication. Numbered references match `swarm/lib/shared-protocols.md` sections.

```
## §7 Shared Protocols (import stub, do not edit per-expert)

Authoritative source: swarm/lib/shared-protocols.md (load first on every invocation).
This stub names imported semantics + spec section; full text lives in the library.

  1. Wiki write protocol — single-writer brigadier (Phase A). See: shared-protocols.md §1.
  2. Provenance gate — every wiki entry carries sources[] + tier (Lock 13). See: §2.
  3. Structured output schema — Task() return shape with cycle_id + dissents. See: §3.
  4. HITL escalation — when to bounce, refusal payload format. See: §4.
  5. Tool permission self-check — refuse forbidden-tools without invoking. See: §5.
  6. mode: writing-support — no primary prose in rituals (E-10). See: §6.
  7. Tool-language abstractions — Frontmatter / snapshot / local gate (E-7). See: §7.
  8. Max-subscription discipline — no direct API calls; only built-in tools. See: §8.
  9. Retrieval stack — agentic search > RAG; wiki-first; no auto-fetch. See: §9.

Refusal: if any clause above is violated by the proposed action, halt and return
HITL bounce (clause 4) with the violated clause-id quoted verbatim.
```

## 6. §8 anti-patterns — 5-column table schema

Per FPF E-8 (§2.8) + MS §3.30 (baseline 4-col table replaced). Header row + minimum row count:

| AP code | Trigger (observable, past-participle) | Detection rubric (binary) | Response action | Strategies.md rule-slug |
|---|---|---|---|---|
| AP-15-handoff-domain | Cell-output-emitted-without-acceptance-contract | Schema-validator: missing `acceptance-test` field → fail | escalate (brigadier) | rule-domain-handoff-v1 |
| ... ≥ 7 more domain-specific rows | ... | ... | ... | ... |

Row-count requirement (E-8): minimum 8 domain-specific rows per expert, in addition to a separate global cross-reference to AP-1..AP-26 (one row each, Response-action column may say "see global"). Response-action enum: `pause | escalate | integrate | tombstone`. Per-expert row content comes from Sub-agent E + drafter creativity within this locked schema. The example row above anchors shape only — the drafter substitutes domain-specific content.

Note on column-naming reconciliation: FPF E-8 (§2.8) names columns "AP code / trigger signal / detection rubric / response action / compound-step rule-slug"; MS §3.30 baseline used 4 columns (#, AP, Prevention, Part 5 §ref). The FPF 5-col schema supersedes — drafter MUST use the 5 headers above.

## 7. §9 Strategies.md protocol — 4-part DRR entry format

Per FPF E-9 (§2.9) + Part 10 §10.1 [E-9, E-13] + §10.2 item 5/6/7 (Block 6 / Block 7 / Block 8). Every entry in `agents/<expert>/strategies.md` MUST follow this YAML+markdown template:

```yaml
---
rule_slug: <kebab-case-unique>
version: 0.1.0  # SemVer; bump on any edit
created: YYYY-MM-DD
last_review: YYYY-MM-DD
status: active | tombstoned
ratio: { hits: 0, misses: 0 }  # ✓/✗ counter, harvested by Compound step
expected_evolution:
  cycle_10: <forecast>
  cycle_50: <forecast>
  cycle_200: <forecast>
---

## Context
<one paragraph: what cycle / artefact / signal triggered this rule>

## Decision
<the rule itself, imperative voice, one sentence if possible>

## Alternatives considered
- <alt-1> — kill condition: <why rejected>
- <alt-2> — kill condition: <why rejected>
- status quo — kill condition: <why insufficient>

## Review checkpoint
<when to re-evaluate this rule (event or date) + criterion that would tombstone it>

---

## Appendix: Block 6 Implementation AI (file-level, once per expert)
- current-executor: claude-sonnet-4-6  # brigadier: claude-opus-4-7
- tools-allowed / forbidden-tools / context-window-budget / memory-strategy / upgrade-policy

## Appendix: Block 7 Implementation Human (file-level, once)
- hired-person: null  # Phase A
- onboarding-path / reporting-to / performance-kpis / handoff_from_ai.triggers

## Appendix: Block 8 Evolution (file-level, once, end of file)
- changelog[] (SemVer-per-entry) / last_review / expected_evolution (cycle-10/50/200)
```

The 4-part DRR (Context / Decision / Alternatives / Review-checkpoint) is per-rule. The three Block 6/7/8 appendices are per-file (declared once at file top or end). Compound step writes new DRR entries; meta-agent quarterly audit harvests `ratio` and tombstones below threshold.

## 8. Cross-reference table

| ID | Section enhanced | FPF block enhanced | Locks/anchors |
|---|---|---|---|
| E-1 | §1 → §1a + §1b | Block 1 + Block 2 | FPF §2.1; §10.1 |
| E-2 | §2 (Ontological-Spine sub-section) | Block 2 (extended into body) | FPF §2.2; A.14 typed edges |
| E-3 | §3 critic | Block 3 (rubric body) | FPF §2.3; Hamel-binary AP-25 |
| E-4 | §4 optimizer | Block 3 (rubric body) | FPF §2.4; Γ-operator invariants |
| E-5 | §5 integrator | Block 3 (rubric body) | FPF §2.5; F-G-R B.3 |
| E-6 | §6 scalability | Block 3 (rubric body) | FPF §2.6; BOSC-A-T-X; Janus 9.4/9.5 |
| E-7 | §7 shared protocols | Block 3 (extracted to library) | FPF §2.7; Lock 17; E.5.3 |
| E-8 | §8 anti-patterns | Block 3 (negation-of-Conformance) | FPF §2.8; supersedes MS §3.30 |
| E-9 | §9 strategies.md | Block 8 (Evolution / DRR) | FPF §2.9; E.9 DRR |
| E-10 | §7 (sub-clause) | Block 3 (writing-support guard) | FPF §5.3 anti-pattern lock |
| E-11 | §1b (Janus pair) | Block 2 (Ontological) | FPF §10.1; R-E §7.1 A |

---

**Cited section anchors used:** MS §5.2 (header), §5.2.1 (skeleton), §5.2.2 (mode gate), §5.2.3 (canonical sources), §5.3.1–§5.3.2 (Task() schema + structured output), §5.5.1–§5.5.5 (wiki protocol), §5.6.4 (UserPromptSubmit hook), §3.30 (baseline AP table superseded). FPF §1.1 (baseline 9-section), §2.1–§2.9 (E-1..E-9 derivations), §3.1–§3.5 (Block 4–8), §5.3 (E-10), §10.1–§10.2 (shopping list), §10.8 (success predicate), §6.2.1 (brigadier ontological — referenced for E-12 envelope), Appendix A (E-1..E-18 summary).
