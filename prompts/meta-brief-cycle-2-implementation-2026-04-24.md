---
title: Meta-Brief — Write the Cycle-2 Implementation Execution Prompt (OPP-01 + OPP-02 + OPP-04 + HD-01 + HD-02)
date: 2026-04-24
type: meta-brief
author: Cloud Cowork (short brief; deep prompt to be written by Claude Code on server)
target_executor_this_pass: Claude Code on server (writes the deep execution prompt)
target_executor_next_pass: separate Claude Code session (executes the written prompt → implements 5 approved items physically in repo)
output: prompts/cycle-2-implementation-2026-04-XX.md
estimated_duration_this_pass: 1-2 hours (prompt-writing only, NOT execution)
precedes: T-cycle-2-implementation-2026-04-XX (next-pass executes this)
defers: M3 solo-vs-matrix experiment (runs AFTER OPP-01 ships, separate task)
---

# META-BRIEF — Write the Cycle-2 Implementation Execution Prompt

## Your task in this session

Write a **deep, long, research-grounded execution prompt** that will be used in a **separate next Claude Code session** to PHYSICALLY IMPLEMENT 5 approved swarm self-improvement items in the repo. You are NOT implementing them in this session. You are writing the prompt which another CC session will use to implement.

**Output file:** `prompts/cycle-2-implementation-2026-04-<XX>.md`

**Stop after this prompt is committed and pushed.** Do not execute OPP-01/02/04/HD-01/HD-02 yourself in this session.

## Why this split

Per Ruslan's durable rule 2026-04-23: Cloud Cowork specifies short briefs; Claude Code on server writes deep prompts (1M context, sub-agents, full repo access). Then a fresh CC session executes the written prompt.

## Ruslan's Gate-2 decisions (2026-04-24, durable)

The cycle-1 brigadier surfaced 4 implement-now opportunities + 2 HITL decisions. Ruslan's per-item acks:

| ID | Ruslan decision | Rationale |
|---|---|---|
| **OPP-01** eval harness | **APPROVE** | Root infra; M3 depends on it |
| **OPP-02** hook layer | **APPROVE** | Ruslan overrode Cloud Cowork's "defer" recommendation and chose to implement now — honor his decision |
| **OPP-04** cell_acceptance_predicate | **APPROVE FIRST** | Cheapest (3 turns), true-antifragile, highest-quality improvement from cycle |
| **M3** solo-vs-matrix baseline | **DEFER to separate next task** | Approved in principle; runs AFTER OPP-01 ships in a dedicated task |
| **HD-01** horizon gate divergence | **Option C** (Ruslan: "делай как лучше" = preferred = C) | Adds €50K gate to all 5 agents + scalability §6.1 tables |
| **HD-02** M-class rate limiter | **Option A (N=2 per cycle)** | 1 structural fix + 1 measurement fix max per cycle; protects Ruslan's attention budget |
| **OPP-03 / OPP-05 / OPP-06** | **Cycle-2 queue** (for a later cycle after this implementation lands) | Per original deferral, unchanged |

The execution prompt you write must implement items 1, 2, 3, 5, 6 (OPP-01 / OPP-02 / OPP-04 / HD-01 / HD-02). It must NOT run M3. It must NOT touch OPP-03/05/06.

## Critical framing to propagate into the written prompt

> **This implementation session is THE validation moment for Phase A swarm.** Every OPP you implement shapes whether Cycle-3+ measurements produce signal or noise. Shallow wiring = broken signal forever. 1000% depth on each implementation. Ruslan's standing directive: ебейший нахуй на 1000% проработанный. No "good enough"; every hook script, every schema field, every horizon table entry is load-bearing for months of downstream cycles.

Make this framing §1 of the written execution prompt.

## What the execution prompt (which you write in this session) must make its future executor deliver

### Part A — OPP-01 eval harness (6-8 turns)

Physical deliverables per OPPORTUNITIES §2 + artefact `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md` (781 lines, treat as authoritative spec):

1. `swarm/evals/` directory with 6 subdirs: `schema.md`, `run.sh`, `cells/`, `golden/`, `health-hooks/`, plus subfolder `golden/solo-vs-matrix/` as stub (M3 substrate)
2. `swarm/evals/schema.md` — 6 required fields + optional versioned fields (Fowler Extract Class reference)
3. `swarm/evals/run.sh` — walks `*/results.jsonl`, aggregates, exits 0/1
4. `swarm/evals/cells/<cell-id>/results.jsonl` — per-cell results skeleton (empty but validating)
5. `swarm/evals/health-hooks/count-closed-cycles.sh` + `count-lint-findings.sh` + `compute-fpar.sh` — bash scripts that update `swarm/wiki/meta/health.md` from results.jsonl
6. Smoke-pass verification: dir exists / schema.md present / run.sh exits 0 on empty corpus / 3 health-hook scripts lint-clean

**Anti-scope:** NO PostToolUse lint hook (OPP-02 territory), NO /compound skill (OPP-03 Cycle-2+), NO execution of solo-vs-matrix comparison (M3 separate task).

### Part B — OPP-02 hook layer (6 turns)

Physical deliverables per OPPORTUNITIES §3 + artefact `opportunity-02-hook-layer.md` (725 lines):

1. **Pre-check: verify Claude Code hook API availability** (first step of Part B). If available → hook-native implementation. If not → Bash-wrapper fallback with same logic. Report decision explicitly in the execution report.
2. `.claude/hooks/mode-prefix.sh` — regex check for `^mode: (critic|optimizer|integrator|scalability)$`; Cycle-2 = log-only (warn, exit 0); Cycle-3 upgrade = blocking exit 1
3. `.claude/hooks/role-matrix.sh` — parses `shared-protocols.md §5 role_tool_matrix`; denies cross-role tool access; Cycle-2 = log-only
4. `.claude/hooks/verify-packet.sh` — reads last Task() return; rejects `sources:[]` + body > 500 chars (AP-1 lock); Cycle-2 = log-only
5. `swarm/lib/hooks/parse-frontmatter-field.sh` — shared helper (Fowler Extract)
6. `.claude/settings.json` — adds UserPromptSubmit + PostToolUse hook entries (or Bash-wrapper instructions if fallback)
7. Log substrate = writes events to `swarm/evals/` (OPP-01 substrate; hard dependency)
8. Explicit allowlist for 5 known legitimate patterns (prevents false positives in cycle-2 logs)

**Anti-scope:** NO expert system prompt edits (that's OPP-04 / A5 text-fix), NO eval harness scaffolding (OPP-01 owns it), NO blocking exit in Cycle-2 (upgrade to blocking happens in Cycle-3+ only after OPP-01 health-counter signal).

### Part C — OPP-04 cell_acceptance_predicate (3 turns, DO THIS FIRST — cheapest + no deps)

Physical deliverables per OPPORTUNITIES §4 + artefact `opportunity-04-cell-acceptance-predicate.md` (655 lines):

1. **brigadier.md §3.3 WBS schema diff** — add `cell_acceptance_predicate:` field (string, 20-200 chars, regex-checkable). Upgrade path to structured block at €1M horizon flagged in comment (natural antifragile evolution per systems-scal §3).
2. **`/lint` check #13** — two slugs:
   - `cell-ap-missing` — field absent in ≥1 cell row
   - `cell-ap-trivial` — field present but fails length regex (20-200) OR matches anti-regex (e.g., "artefact exists", "is non-empty", "returns output")
3. **5 test WBS files** in `swarm/wiki/tasks/_tests/` with predicates that pass + 2 that should fail (anti-regex test fixtures)
4. Explicit non-deletion: **OPP-05 `falsifier:` field is NOT in this scope** — parallel pattern declared in comment so OPP-05 is trivial lift in a later cycle.

**Anti-scope:** NO falsifier: field on hypothesis artefacts (OPP-05), NO DRR Kelly fields (M2 memory deferred), NO Bash pre-dispatch hook (that's OPP-02 coordination).

### Part D — HD-01 horizon gate alignment, Option C (1-2 turns)

Per OPPORTUNITIES §6 HD-01 Option C:

1. **Add €50K gate to all 5 agent files** (brigadier + engineering-expert + mgmt-expert + systems-expert + philosophy-expert + investor-expert) — investor already has 5 gates; other 4 agents + brigadier need €50K added as first gate
2. **Update scalability §6.1 tables in each agent file** — every OPP/decision now has a named home gate at €50K / €200K / €1M / $100M / $1T
3. Verify convergence — S-06 convergence metric in `swarm/wiki/meta/` (if exists) now shows 5 agents aligned on 5 gates
4. **Ruslan rationale in comment:** €50K is Ruslan's single committed absolute date (Q2 2026) per JETIX-PLAN D3. Must be represented in every scalability projection.

**Anti-scope:** DO NOT touch investor-expert's existing €50K row (already correct); do not modify gate values ($100M → $100B etc).

### Part E — HD-02 M-class rate limiter, Option A N=2 (1-2 turns)

Per OPPORTUNITIES §6 HD-02 Option A:

1. **Add rate-limiter rule to `brigadier.md`** — in §3.3 WBS schema or adjacent section: per cycle, brigadier may dispatch MAXIMUM 2 Method-class tasks (1 structural fix + 1 measurement fix). Any 3rd+ M-class task gets rejected with explicit reason.
2. **Classification rule for M-class** — brigadier must tag each decomposed cell with `class: M | B | O` (Method / Business / Operational). Rate-limiter applies only to M.
3. **Counter in `swarm/wiki/meta/health.md`** — `m_class_dispatched_this_cycle: N/2` tracked per cycle.
4. **Failure mode doc** — brigadier §6 (or dedicated section) documents what happens when M-limit hit mid-cycle: queue for next cycle, explicit log entry in `swarm/wiki/operations/<cycle>/m-class-overflow.md`.

**Anti-scope:** NO automatic M-task generation (brigadier never spawns without task brief), NO cost-accounting field (Option C path, not selected).

### Part F — Bootstrap verification + execution report

After all Parts A-E created:

1. `ls swarm/evals/` shows 6 expected items
2. `bash swarm/evals/run.sh` exits 0 on empty corpus
3. `.claude/hooks/*.sh` all exist + bash -n passes + executable bit set
4. `grep -c "cell_acceptance_predicate" .claude/agents/brigadier.md` ≥ 2 (schema + anti-regex example)
5. `grep -c "€50K" .claude/agents/*.md` = 6 (all 5 experts + brigadier reference it)
6. `grep "m_class_dispatched_this_cycle" .claude/agents/brigadier.md swarm/wiki/meta/health.md` both match
7. `/lint` runs clean — no new failures, check #13 reports correctly on 5 test WBS files

### Part G — Deep execution report (MANDATORY, ≥2000 words)

The executor MUST produce a final report at `decisions/CYCLE-2-IMPLEMENTATION-REPORT-2026-04-XX.md` covering:

- **Per-part summary** — what was implemented, where (file paths), how verified
- **Hook API pre-check verdict** (Part B step 1) — native or Bash-wrapper, with evidence
- **Tradeoffs encountered** — any place where the spec was ambiguous and executor made a judgment call, with rationale
- **Emergent issues** — anything surprising, any honest doubts about whether the implementation matches spirit of the OPP
- **Verification matrix** — table of Part F check outputs (pass/fail + evidence)
- **Lessons for Cycle-3** — 3-5 points learned that should inform next task brief
- **Next-step recommendations** — what the logical next launch is (hint: M3 on OPP-01 substrate, task T-B unit-econ arithmetic)

## Artefact sources the executor MUST read (treat as authoritative)

1. `decisions/SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md` (398 lines) — the approved spec
2. `decisions/SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md` (355 lines) — upstream hypothesis context
3. `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-01-eval-harness.md` (781 lines)
4. `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-02-hook-layer.md` (725 lines)
5. `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/opportunity-04-cell-acceptance-predicate.md` (655 lines)
6. `swarm/wiki/tasks/T-swarm-self-improve-v1-2026-04-23/artefacts/systems-scalability-01.md` (horizon gate context for HD-01)
7. `swarm/lib/shared-protocols.md` (226 lines, 9-section runtime contract)
8. `swarm/wiki/operations/T-swarm-self-improve-v1-2026-04-23/cycle-01.md` (cycle log)
9. `.claude/agents/brigadier.md` (1005 lines — §3.3 WBS schema gets the OPP-04 + HD-02 edits)
10. All 5 expert agent files for HD-01 €50K row addition

## Locked decisions to respect (NON-NEGOTIABLE)

All 24 Locks (D1-D24). Especially:
- **D17** — Filesystem = SoT. Every change committed to git; Notion reflects, does not originate.
- **D11** — Продюсерский центр parallel revenue; this swarm work is Method-class, not revenue-generating directly.
- **D19** — $1T trajectory; every scalability table must include all 5 gates post-HD-01.
- **W-5** — Two-level Compounding Engineering; OPP-01 eval harness is Level-2 substrate.

Plus: W-1..W-12 (wiki goals), 8 R-items + 5 T-resolutions (wiki mechanics), FPF E-1..E-18, shared-protocols.md 9-section contract.

**Legacy coexistence:** 14 legacy agents + v2 `wiki/` are untouched. All new work goes to `swarm/` + new 6 agents only.

## Operating mode

**Stage-Gated.** Between Part F verification and Part G report writing, the executor writes an `AWAITING-APPROVAL-cycle-2-implementation-<date>.md` file and pauses for Ruslan review. Ruslan acks → executor writes Part G report → commits + pushes → done.

Full-Auto is NOT authorized for this implementation (Ruslan's Stage-Gated default per ROY-ALIGNMENT).

## Max-subscription discipline

**`unset ANTHROPIC_API_KEY`** before `claude --dangerously-skip-permissions`. Max subscription 20× active. No paid API usage. This is hard constraint — violation = $47K incident vector.

## Commit cadence

Per `swarm/lib/shared-protocols.md §1 wiki write protocol` — incremental commits per-part, not one monolithic commit. Commit messages:
- `[cycle-2-impl] OPP-04 cell_acceptance_predicate landed`
- `[cycle-2-impl] OPP-01 eval harness infrastructure`
- `[cycle-2-impl] OPP-02 hook layer (log-only mode)`
- `[cycle-2-impl] HD-01 €50K gate propagated to all agents`
- `[cycle-2-impl] HD-02 M-class rate limiter N=2 in brigadier`
- `[cycle-2-impl] Part F verification passed`
- `[cycle-2-impl] Part G execution report`

Push after each commit.

## What the written execution prompt should look like (guidance for this session)

- **Length:** 700-1200 lines. Not shorter — this is 5 deliverables + verification + report. Not longer than 1500 — avoid padding.
- **Style:** Imperative, numbered, specific. File paths in backticks. Bash snippets where relevant.
- **Structure:** §1 Mission + critical framing / §2 Scope (Parts A-G) / §3 Artefact sources / §4 Locked decisions / §5 Operating mode / §6 Commit cadence / §7 Definition of done / §8 Escalation (if you hit ambiguity, write AWAITING-APPROVAL, don't guess).
- **Tone:** Treat executor as competent but context-blind. Give file:line references. Never say "figure it out" — say "check X at path Y".

## Definition of done for THIS session (Cloud Cowork brief)

1. `prompts/cycle-2-implementation-2026-04-<XX>.md` written (700-1200 lines)
2. Committed to `claude/jolly-margulis-915d34` + pushed to origin
3. Brief summary reply to Ruslan: file path + line count + 1-paragraph overview + ready-to-launch command snippet

## Escalation

If while writing the execution prompt you encounter:
- Spec contradictions between OPPORTUNITIES §X and artefact file §Y
- Unclear dependency between OPP-01 substrate and OPP-02 hook logging
- Ambiguity on whether HD-02 class tag belongs in WBS schema or elsewhere

→ Stop, write `prompts/AMBIGUITY-cycle-2-implementation-<date>.md` with the contradiction, notify Ruslan via commit message. Do NOT guess. Ruslan resolves, then you continue.

---

*End of meta-brief. Execute.*
