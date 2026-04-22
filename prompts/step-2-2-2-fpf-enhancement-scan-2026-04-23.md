---
title: FPF Enhancement Scan — recommendations to 10× domain-expert structure
date: 2026-04-23
status: ready-for-launch
target_executor: Claude Code on server (Opus 4.7 1M, extended thinking)
estimated_duration: 1.5-3 hours
output: decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md
context_artefact: prompts/step-2-1-master-synthesis-2026-04-22.md (completed Шаг 2.1)
---

# FPF ENHANCEMENT SCAN — 10× domain-expert structure

## Mission

Read Jetix's FPF + Levenchuk research corpus in this repo (34 files),
compare against the domain-expert skeleton already locked in
`decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` Part 5
§5.2, and produce a **concrete recommendations document** for how to
enhance the 6-agent swarm's domain-expert structure using FPF / ШСМ /
holonic / alpha-based concepts. The goal is 10× more rigorous, 10× more
aligned with systems-thinking discipline, and 10× more ready to handle
Phase B self-improvement loops.

You are **not** replacing the master synthesis. You are producing an
**enhancement delta** that will be merged into the Шаг 2.2.4 agent
construction prompt.

## Critical framing

This output directly affects how 5 domain-expert system prompts
(1,500–3,000 lines each) will be structured. Shallow enhancement =
shallow agents for the next year+. Deep enhancement = agents that
operate with Levenchuk-grade systems discipline. Write accordingly.

## Inputs — PRIORITY READ ORDER

### Tier 1 — PRIMARY (deep, every word)

**FPF-Spec + Levenchuk-for-AI research (the main two):**
```
raw/external/ailev-FPF/FPF-Spec.md
raw/external/ailev-FPF/Readme.md
raw/external/ailev-FPF/ATTRIBUTION.md
raw/research/levenchuk-for-ai-deep-research-2026-04-19.md  (1041 lines — CORE)
```

**5 primitives deep dive:**
```
raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-full-body-of-work.md
raw/research/levenchuk-fpf-research-2026-04-20/R-B-shsm-5-primitives-deep.md
raw/research/levenchuk-fpf-research-2026-04-20/R-C-17-trans-disciplines-mapping.md
raw/research/levenchuk-fpf-research-2026-04-20/R-D-essence-kernel-shsm-relation.md
raw/research/levenchuk-fpf-research-2026-04-20/R-E-mereology-holon-hierarchy.md
```

**Constitutional reference:**
```
raw/research/levenchuk-deep-research-2026-04-18.md
raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md
raw/research/fpf-gap-analysis-2026-04-20.md
```

### Tier 2 — COMPARISON TARGET (what we're enhancing)

```
decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md
  Part 5 §5.1 — brigadier skeleton
  Part 5 §5.2 — domain-expert skeleton (9 sections — primary comparison target)
  Part 5 §5.2.3 — per-expert canonical-source allocation
decisions/ROY-ALIGNMENT-2026-04-22.md
  §2 — 5 domain experts roster
  §3 — matrix 5×4 pattern
design/ROY-BUILD-LOGIC-2026-04-23.md
  §1 — location of files
  §2 — communication protocol
```

### Tier 3 — CONTEXT (skim)

```
design/JETIX-FPF.md  (3758 lines — skim TOC, spot-read relevant sections)
prompts/d6-jetix-fpf-2026-04-20/  (directory — method-of-work for FPF reviews)
raw/research/d6-reviews/reviewer-1-levenchuk-purist.md
raw/research/stage2-review/review-levenchuk.md
prompts/stage2-review/04-levenchuk-role.md
prompts/architecture-research-2026-04-19/R3-levenchuk-ai-prompt.md
```

### Tier 4 — OUT OF SCOPE (do not read)

- `raw/books-md/` (393 books) — use for Phase B
- All other deep research files not listed above
- Business-domain research (consulting / agency / CRM etc.)

## Sub-agent strategy (mandatory)

Do NOT read Tier 1+2 sequentially. Parallelize:

**Sub-agent A** — read `FPF-Spec.md` + `R-A-levenchuk-full-body-of-work.md` +
`R-B-shsm-5-primitives-deep.md`. Extract: the 5 ШСМ primitives with
precise definitions, their interrelationships, and concrete protocols
each primitive implies for an AI agent.

**Sub-agent B** — read `levenchuk-for-ai-deep-research-2026-04-19.md`
(the 1041-line main document). Extract: (a) the 8-block role-manifest
format in Part C with all sub-fields and rationale; (b) the 10 core
alphas in Part D; (c) the rituals in Part E; (d) B.4 "FPF как протокол
для AI-агентов" in full.

**Sub-agent C** — read `R-C-17-trans-disciplines-mapping.md` +
`R-D-essence-kernel-shsm-relation.md` + `R-E-mereology-holon-hierarchy.md`.
Extract: (a) the 17 trans-disciplines and how each maps to a domain-expert
slot in our 5-agent roster; (b) the holon/mereology structure and how
it applies to the 6-agent swarm hierarchy; (c) the Essence kernel and
its relation to alphas.

**Sub-agent D** — read master synthesis Part 5 §5.1–§5.2 + ROY-ALIGNMENT
in full. Extract: (a) exact current 9-section skeleton of domain expert
per the blueprint; (b) brigadier's 11-section skeleton; (c) any gaps
or weak spots in the current design; (d) what's explicitly out-of-scope
(to respect boundaries).

**Sub-agent E** — read `fpf-gap-analysis-2026-04-20.md` +
`levenchuk-fpf-knowledge-base-2026-04-20.md`. Extract: previously
identified gaps between Jetix and FPF, with prior remediation proposals
if present.

Each returns a structured extraction (≤3,000 words) with findings,
citations, and applicability notes.

Then you (main agent) integrate and produce the final document.

## Output structure

Target: `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`
(8,000–14,000 words; deep enough to fully inform agent construction).

### Part 1 — Current baseline (what master synthesis §5.2 has)

Brief summary of the 9-section skeleton as-is (from sub-agent D). No
critique yet. This part establishes the baseline.

### Part 2 — FPF / ШСМ lens applied to each current section

Walk through master synthesis §5.2's 9 sections one-by-one. For each:
- What the current section says
- What FPF / ШСМ adds or sharpens (citing Tier 1 sources)
- Concrete enhancement proposal (what to add, what to restructure)
- Do NOT propose enhancements that contradict 24 Locks (check compliance)

### Part 3 — New FPF-derived blocks to add

The main delta. At minimum, cover the 8 blocks from C.1–C.8 in
`levenchuk-for-ai-deep-research-2026-04-19.md`:

1. **Ontological block** (Levenchuk): purpose / target-system /
   primary-alpha / secondary-alphas / domains / accountabilities /
   out_of_scope / acceptance-criteria. For each of our 5 experts,
   propose concrete values.
2. **Graph of Creation**: produces / consumes — for each of 5 experts,
   propose concrete artefacts-produced and artefacts-consumed with
   cross-refs. This becomes the auto-buildable dependency graph of
   the swarm.
3. **Seniority / Decision-rights**: autonomous / requires-approval /
   never + escalation-trigger + split_trigger. For each of 5 experts,
   calibrate under 24 Locks + stage-gated protocol.
4. **Implementation AI block**: tools-allowed (scoped) / memory-strategy /
   context-window-budget / eval-dataset / eval-passing-threshold /
   upgrade-policy. Per expert.
5. **Implementation Human**: migration path AI → hybrid → human +
   handoff triggers + KPIs per expert.
6. **Evolution / Audit trail**: changelog + expected-evolution
   milestones per expert (10 / 50 / 200 cycle milestones).

For each new block: explicit mapping to which of the 5 ШСМ primitives
it implements; explicit mapping to which of the 17 trans-disciplines
it leans on.

### Part 4 — Alpha set for swarm operation

Per `levenchuk-for-ai-deep-research-2026-04-19.md` Part D — 10 core
alphas. Propose **which alphas the swarm itself operates on** (not
Jetix business alphas, but the swarm's own alphas: e.g., Task-alpha,
Learning-alpha, Strategy-alpha, Artefact-alpha, Cycle-alpha). For each:
states, transitions, ownership (which expert moves it).

### Part 5 — Rituals inherited into swarm operation

Per Part E — strategizing ritual + thinking-by-writing. How does
brigadier's Plan-Work-Review-Compound loop map to these rituals?
Where do they enhance vs duplicate CE's loop?

### Part 6 — Brigadier-specific enhancements

Brigadier's 11-section skeleton (master synthesis §5.1). What FPF /
ШСМ adds:
- Ontological block for brigadier (what alpha does brigadier own?)
- Graph of Creation for brigadier (inputs/outputs at orchestration level)
- Decision-rights matrix (what brigadier can auto-decide, what escalates)
- Method sub-block with PMBOK + management-of-work reference
  (Ruslan flagged: "brigadier надо надрочить на PMBOK и management books")
- Reconcile with Levenchuk's view of leadership / orchestration role

### Part 7 — 17 trans-disciplines mapping to 5 experts

For each of the 17 trans-disciplines (from R-C research), map which
of our 5 domain experts (or brigadier) owns it. Some may be shared;
some may need a note. This gives us a coverage check: do our 5 experts
fully span the ШСМ-required cognitive layers, or are there holes?

### Part 8 — Holon / mereology integration (from R-E)

How does the swarm hierarchy map to holonic structure? Brigadier as
holon over 5 expert sub-holons; each expert as holon over own strategies +
wiki slice + scratchpad. What changes in our current design to respect
holon rules (upward / downward cohesion)?

### Part 9 — Critical tensions + recommended resolutions

Places where FPF / ШСМ conflicts with master synthesis or 24 Locks.
Honest list. For each: recommend resolution (keep master synthesis /
adopt FPF / synthesize).

### Part 10 — Concrete shopping list for Шаг 2.2.4 master prompt

Explicit bullet list: what must be added to the Шаг 2.2.4 prompt so
that when Claude Code constructs the 6 agent system prompts, it does
NOT miss these FPF enhancements.

## Quality criteria

- Every FPF / ШСМ claim has a citation (file + section). This is a
  Russian-source-heavy research area; avoid English-only summaries.
- Every enhancement proposal is actionable — a prompt-writer can turn
  it into system-prompt sections without further research.
- Do NOT propose enhancements that conflict with 24 Locks without
  flagging the conflict.
- Prefer integration over replacement: current 9-section skeleton has
  been reviewed twice (gate 1 + gate 2); don't undo that work.
- No marketing language. No hype about FPF / ШСМ. Technical, evidence-
  based prose only.
- Russian terms preserved verbatim where they are technical
  (альфа-состояния, мышление письмом, role-ontology — not translated).
- Length 8,000–14,000 words. Not shorter.

## Operational protocol — Stage-Gated

Single gate at the end (this is shorter than Шаг 2.1, one gate sufficient):

1. Spawn parallel sub-agents (A, B, C, D, E) — commit extractions
   separately to `raw/research/step-2-2-2-extractions/`
2. Integrate and draft Parts 1–10
3. Commit as `decisions/AWAITING-APPROVAL-fpf-enhancement-2026-04-23.md`
4. Pause. Push. Await Ruslan approval.

No pre-gate adversarial review mandated for this scope (master
synthesis already has adversarial review discipline; this is a
focused delta).

## Launch reminders

- `unset ANTHROPIC_API_KEY` — Max subscription discipline
- Branch: `claude/jolly-margulis-915d34`
- Tmux session: `fpf-scan`
- Commit cadence: after each extraction + at final draft

## Scope discipline

Do NOT:
- Try to rewrite master synthesis
- Re-run adversarial review of master synthesis
- Generate the actual 6 agent system prompts (that's Шаг 2.2.4)
- Read Tier 4 books from `raw/books-md/` (Phase B fuel)
- Draft wiki v3 spec (that's Шаг 2.2.3)

DO:
- Produce a focused enhancement delta document
- Make it precise enough that Шаг 2.2.4 prompt can cite specific
  sections of this document
- Flag any required preparatory work (e.g., alpha state files to
  create before agent construction can start)

## Success criteria — you are done when

1. `decisions/AWAITING-APPROVAL-fpf-enhancement-2026-04-23.md` exists
   at 8,000–14,000 words.
2. All 10 output parts present.
3. ≥40 FPF / ШСМ citations to Tier 1 sources.
4. Compliance check against 24 Locks explicit.
5. Shopping list (Part 10) actionable (prompt-writer can use it directly).
6. Sub-agent extractions preserved in `raw/research/step-2-2-2-extractions/`.
7. Commit pushed; gate file waiting for Ruslan approval.

---

Begin with Phase 1: spawn parallel sub-agents A, B, C, D, E with the
extraction briefs defined above.
