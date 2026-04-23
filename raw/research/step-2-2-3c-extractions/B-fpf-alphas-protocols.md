---
sub_agent: B
title: FPF-Enhancement Alphas + Protocols Extraction for Wiki v3 Стадия C
date: 2026-04-23
sources_read:
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Part 4 + Part 10)
word_count_target: ≤2500
purpose: Feed Deliverable 5 (swarm-alphas state machines) and Deliverable 6 (shared-protocols.md)
---

# Extraction — FPF Enhancement Part 4 (Alphas) + Part 10 (Preparatory Specs)

Source: `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`. All
verbatim unless marked as gap-flag. Part 4 preamble: swarm-alpha set is
separate from the 10 Jetix-business alphas; schema = "past-participle
states + transition-with-mover + checklist".

---

## Section 1 — α-1 Task swarm-alpha

- **Identity (verbatim):** "Represents a user request entering the swarm."
- **Scope:** every inbound user request the brigadier intakes; runs from
  submission to archival.
- **States (verbatim):** `submitted → intaked → decomposed → dispatched →
  integrated → gated → approved → compounded → archived`. Failure
  branches: `refused → returned` (brigadier refuses intake); `gated →
  rejected → returned` (HITL reject).
- **Movers (verbatim):** brigadier primary. `submitted→intaked`
  (brigadier); `intaked→decomposed` (brigadier §3); `decomposed→dispatched`
  (brigadier §4); `dispatched→integrated` (experts → brigadier §5);
  `integrated→gated` (brigadier §6); `gated→approved` (HITL);
  `approved→compounded` (brigadier §7); `compounded→archived` (brigadier
  §9).
- **Acceptance per state (verbatim):** `decomposed`: CE 40/10/40/10
  budget assigned + matrix cells selected + AP declared; `dispatched`:
  ≥1 Task() invocation issued; `integrated`: all invoked cells returned
  + dissents preserved; `gated`: AWAITING-APPROVAL file exists with
  4-response template; `approved`: HITL reply parsed; `compounded`: ≥0
  rules appended to strategies.md (zero is valid); `archived`:
  cycle-log.md written.
- **Metrics (verbatim):** time-in-state per state; dispatch-to-integrate
  fan-out; gate-approval rate; compound-rule-extraction rate.
- **Owner:** brigadier.
- **Integration with α-4 Cycle:** α-1 is consumed inside α-4 (the
  brigadier's `task → gate → compound → archive` run). α-2 created
  during `dispatched→integrated`. α-3 entries emitted at `compounded`.
- **FPF-canonical refs:** [A §1.2] Альфа; BUILD §2.2; brigadier §3–§9.
- **Gap-flag:** Part 4 silent on the mover/predicate for
  `gated→rejected→returned` reentry — orchestrator must specify in
  Deliverable 5.

---

## Section 2 — α-2 Artefact swarm-alpha

- **Identity (verbatim):** "Each artefact a cell produces into swarm/wiki."
- **Scope:** every wiki/swarm artefact produced by a cell.
- **States (verbatim):** `drafted → reviewed → revised → accepted →
  referenced → superseded / retired`. Loop allowed: `revised ↔ reviewed`.
- **Movers (verbatim):** "cell produces `drafted`; integrator/critic moves
  `→reviewed`; producer or integrator `→revised`; brigadier `→accepted`;
  downstream cell referencing `→referenced`; replacement produces
  `→superseded`; obsolescence `→retired`."
- **Acceptance per state (verbatim):** `drafted`: frontmatter valid
  (source, captured_by, captured_date, task_id, commit_sha per BUILD
  §2.2); `reviewed`: ≥1 critic pass + Conformance Checklist ticked;
  `accepted`: integrator + brigadier signoff; `referenced`: appears in
  another artefact's consumes.
- **Owner:** producing cell primary; brigadier for accept-transition.
- **Matrix-gate integration (verbatim):** "stage-gate transitions in the
  5×4 matrix ARE alpha-state transitions [A §5.2] — this makes gate
  passage machine-verifiable."
- **Delta vs. spec set (`draft/proposed/accepted/superseded/retired/
  tombstoned`):** FPF names `drafted, reviewed, revised, accepted,
  referenced, superseded, retired` — no `proposed`, no `tombstoned`.
  Mapping: FPF `drafted` ≈ spec `draft`; `reviewed/revised` ≈ spec
  `proposed`. FPF Part 4 silent on `tombstoned` for artefacts —
  orchestrator must reconcile in Deliverable 5.
- **FPF refs:** [A §5.2]; BUILD §2.2.

---

## Section 3 — α-3 Strategies-Rule swarm-alpha

- **Identity (verbatim):** "Each entry in strategies.md." Governs
  skill-learning pipeline (Q6).
- **Scope:** every learned rule in `strategies.md` across the swarm.
- **States (verbatim):** `proposed → active → validated ⇄ active →
  tombstoned`.
- **Movers (verbatim):** "compound step (brigadier) `→proposed → active`;
  cell-use tracking `→validated`; fail-rate threshold `→tombstoned`."
- **Acceptance per state (verbatim):** `proposed`: 4-part DRR format
  (context / decision / alternatives / review-checkpoint); `active`: at
  least 1 successful application; `validated`: ✓/✗ ratio ≥ 3:1 over ≥
  10 uses; `tombstoned`: ratio < 1:1 OR explicit Ruslan-retirement.
- **Owner (verbatim):** "meta-agent for tombstoning audit; brigadier for
  writes."
- **Delta vs. spec set (`candidate/learning/active/retired/tombstoned`):**
  FPF names `proposed, active, validated, tombstoned`. Mapping (Sub-
  agent B): spec `candidate` ≈ FPF `proposed`; spec `learning` ≈ FPF
  `active`; spec `active` ≈ FPF `validated`; spec `retired` ≈ FPF
  `tombstoned` partially. Orchestrator must reconcile in Deliverable 5.
- **Integration:** consumes α-1 `compounded` output; 4-part DRR ties to
  E-9 Evolution sub-block (changelog/last-review/expected-evolution at
  10/50/200 cycle milestones).
- **FPF refs:** [B §Block 8]; [E §Part 2.4] DRR.

---

## Section 4 — α-4 Cycle swarm-alpha

- **Identity (verbatim):** "A single `task → gate → compound → archive`
  run."
- **Scope:** the brigadier's CE 40/10/40/10 loop instance.
- **States (verbatim):** `opened → running → integrating → gated →
  compounded → closed → tombstoned` (if aborted).
- **Movers (verbatim):** "brigadier throughout; HITL on
  `gated→compounded`."
- **Acceptance (verbatim):** `closed`: cycle-log.md exists + 1-line
  summary of rule-extractions + 1-line open-questions.
- **Owner:** brigadier.
- **Delta vs. spec set (`open/mid-cycle/closing/closed`):** Mapping
  (Sub-agent B): spec `open` ≈ FPF `opened`; spec `mid-cycle` ≈ FPF
  `running`+`integrating`; spec `closing` ≈ FPF `gated`+`compounded`;
  spec `closed` ≈ FPF `closed`. FPF adds `tombstoned` for aborts.
  Orchestrator must reconcile in Deliverable 5.
- **Q8 dependency:** "≥50 closed cycles is one Layer-9 activation
  criterion" maps to the FPF `closed` state count. Acceptance predicate
  is the machine-verifiable test for incrementing the Layer-9 counter.
- **Integration:** α-1 inbound trigger; α-2 produced inside; α-3
  emitted at `compounded`. Cycle boundary operationalizes
  Стратегирование triggers.
- **FPF refs:** [A §1.2]; brigadier §7/§9; CE 40/10/40/10 [D §Part 1 §3].

---

## Section 5 — α-5 Direction swarm-alpha

- **Identity (verbatim):** "α-5 Direction alpha (Jetix innovation, [E
  §3.2 P3.G]) — Strategic direction under test — spans cycles."
- **Scope:** strategic direction; spans multiple α-4 Cycles.
- **States (verbatim):** `hypothesized → under-validation → validated →
  activated → scaled → plateaued → invalidated → dropped → archived`.
  Pivot branches: `under-validation → hypothesized`; `invalidated →
  hypothesized` (pivot).
- **Movers (verbatim):** "Human / strategic-management primary
  `hypothesized` and `activated`; brigadier tracks state; experts
  contribute evidence artefacts."
- **Acceptance (verbatim):** `hypothesized`: falsifiable claim +
  confidence threshold + success metric declared; `validated`:
  evidence artefacts from ≥ 2 experts; `activated`: written activation
  decision + resource commitment.
- **Owner (verbatim):** "human (strategizing). **AI agents do NOT move
  the Direction alpha** beyond tracking [A §1.4]."
- **FPF formalization (verbatim):** "Rec-07 P2 ... maps this to `C.18
  NQD-CAL` + `C.19 E/E-LOG` + `C.19.1 BLP` for full formalization [E
  §3.2 P3.G]."
- **Phase-A note (Part 10.4/10.6 verbatim):** "α-1..α-4 only machine-
  tracked; α-5 human-owned. Default Phase A lightweight (state enum
  only)."
- **Integration:** consumes evidence artefacts (α-2) from ≥2 experts;
  state changes trigger full strategizing ritual (Part 5 §5.2).

---

## Section 6 — `shared-protocols.md` mandates from Part 10

The architecture spec's Deliverable 6 must include all of the following
verbatim mandates from Part 10:

**§10.4 (verbatim):** Create `swarm/wiki/foundations/swarm-alphas.md`
containing α-1 Task (full state graph + transitions-with-movers +
acceptance per state), α-2 Artefact, α-3 Strategies-Rule, α-4 Cycle,
α-5 Direction (human-owned; Rec-07 NQD-CAL formalization deferred Phase
B). Phase-A simplification: α-1..α-4 only machine-tracked; α-5
human-owned.

**§10.5 (verbatim):** Create `swarm/lib/shared-protocols.md` containing:
- Wiki write protocol (BUILD §2.2 provenance)
- Structured output schema
- HITL escalation protocol
- Cross-cell-reference protocol (read wiki, never call cell)
- Tool-permission self-check protocol
- `mode: writing-support` clause (E-10)
- Tool-language abstractions (Frontmatter / snapshot / local gate)

**§10.6 (verbatim):** Required preparatory work — `swarm/wiki/
foundations/swarm-alphas.md` (Part 4 draft above — can be produced by
Шаг 2.2.4 as first sub-artefact); `swarm/lib/shared-protocols.md` (10.5
above); Clarify with Ruslan: Rec-07 NQD-CAL formalization for α-5
Direction — Phase A lightweight (state enum only) vs Phase B full
(NQD-CAL + E/E-LOG + BLP). **Default Phase A lightweight.** Clarify
with Ruslan: executor choice for brigadier — Opus 4.7 (current
recommendation) vs Opus 4.6 vs Sonnet 4.6. **Default: Opus 4.7 (per
Anthropic orchestrator pattern).**

**§10.7 (verbatim):** Citations Шаг 2.2.4 must keep intact — [A §1.1–§1.5];
[B §Block 1–8]; [B §D.1] Client alpha; [B §E.1–E.3] rituals; [C §Part 1]
16 trans-disciplines; [C §Part 3] Essence Language/Kernel; [C §Part 4
R-E §7.1] 6 mereology rules; [E §Part 5] Phase A R/D split; [D §Part 9]
24 Locks; this document's E-1..E-18.

**§10.8 (verbatim) — Success predicate for Шаг 2.2.4 output:** Step
2.2.4 agent-construction is successful when: (1) 6 system.md files
exist in `.claude/agents/` (brigadier + 5 experts); (2) Each file has
all 7 structural blocks (1a, 1b, 2, 3–6 modes, 7, 8, 9); (3) Each file
has Blocks 4, 5, 6, 7, 8 as defined above; (4) All past-participle
state names used; (5) All typed A.14 edges used in cross-refs; (6)
`swarm/wiki/foundations/swarm-alphas.md` exists; (7) `swarm/lib/
shared-protocols.md` exists and is imported from each expert's §7;
(8) No Tier-4 book read during construction (Phase A discipline); (9)
No content that violates 24 Locks posture (Part 9 §9.8 table); (10)
Each manifest <2,500 lines.

---

## Section 7 — §5.5.5 provenance gate mechanics

§5.5.5 is NOT located in the FPF-Enhancement document. Part 10.5 only
references "Wiki write protocol (BUILD §2.2 provenance)" as the
shorthand for the gate.

What FPF-Enhancement says about provenance (verbatim, Part 4 α-2
acceptance for `drafted`): "frontmatter valid (source, captured_by,
captured_date, task_id, commit_sha per BUILD §2.2)." This is the
machine-verifiable provenance contract per artefact at draft time.

For the brigadier-side gate ("what the brigadier must verify before
allowing a wiki commit"), Part 4 α-2 mover for `→accepted` is
"brigadier" with acceptance predicate "integrator + brigadier signoff",
and this is the alpha-state transition that doubles as the matrix
gate-passage check ([A §5.2]: "stage-gate transitions in the 5×4
matrix ARE alpha-state transitions ... this makes gate passage
machine-verifiable").

**Cross-reference flag:** §5.5.5 itself lives in `decisions/MASTER-
SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`. Sub-agent E should
mine that file for the canonical text of (a) what counts as
provenance, (b) what the gate rejects, (c) brigadier's verification
checklist before allowing a wiki commit. FPF-Enhancement only supplies
the BUILD §2.2 frontmatter contract above.

---

## Section 8 — Structured output schema for Task returns

Part 10.5 mandates "Structured output schema" inside `shared-
protocols.md`. The most concrete schema in the FPF-Enhancement
document is the integrator E-5 output schema (verbatim, §2.5):

"Integrator output schema adds three frontmatter fields per claim in
the synthesis: `F:` formality level (F0 rumor … F9 formal proof);
`ClaimScope:` which bounded context the claim holds in; `R:`
reliability (pathwise, not point estimate)."

Combined with α-2 `drafted` acceptance (verbatim): every artefact
return must carry frontmatter with `source, captured_by,
captured_date, task_id, commit_sha`.

**Gap-flag:** FPF-Enhancement Part 10 does NOT define a complete
sub-agent return-packet schema beyond the above. Part 10.5 names the
slot ("Structured output schema") but defers the body. Orchestrator
must compose Deliverable 6's full schema from these primitives plus
α-1 acceptance fields (e.g., `dispatched` requires "≥1 Task()
invocation issued"; `integrated` requires "all invoked cells returned
+ dissents preserved"). FPF Part 10 silent on full return-packet
fields — orchestrator must specify in Deliverable 6.

---

## Section 9 — HITL escalation rules

Part 10.5 mandates a "HITL escalation protocol" inside `shared-
protocols.md`. The verbatim hooks from FPF-Enhancement:

- **α-1 acceptance (verbatim):** "`gated`: AWAITING-APPROVAL file
  exists with 4-response template" — this is the AWAITING-APPROVAL
  packet contract.
- **α-1 movers (verbatim):** "`gated→approved` (HITL)"; failure
  branch "`gated → rejected → returned` (HITL reject)."
- **α-4 movers (verbatim):** "HITL on `gated→compounded`."
- **α-5 ownership (verbatim):** "AI agents do NOT move the Direction
  alpha beyond tracking [A §1.4]" — therefore any α-5 transition
  bounces to Ruslan.
- **AI-strategizing constraint (verbatim, §4.3):** "AI CAN: SoTA
  research, draft alternatives, devil's-advocate, anti-scope
  checklist, **adapt-mode method selection with founder oversight**.
  AI CANNOT: choose method (invent-mode), accept decision, bear
  responsibility."
- **Matrix implication (verbatim):** "cells classified '1:1' (method
  known, no change) → full AI auto; 'adapt' (method known, needs
  tuning) → AI draft + HITL approve; 'invent' (method unknown) →
  HITL only, experts may surface alternatives [A §5.4]."
- **Strategizing-ritual escalation triggers (verbatim, Part 5 §5.2):**
  "New direction activation (α-5 state change) → full strategizing
  ritual. Method exhaustion (same AP triggered >5 times across cycles)
  → strategizing. Irreversible decision (e.g., architecture commit) →
  strategizing. `split_trigger` fires in Block 5 → strategizing."

**Gap-flag:** FPF-Enhancement names the "AWAITING-APPROVAL file ...
4-response template" but does NOT enumerate the four response
templates' fields. FPF Part 10 silent on AWAITING-APPROVAL packet
field list — orchestrator must specify in Deliverable 6.

---

## Section 10 — Tool permission self-check

Part 10.5 mandates a "Tool-permission self-check protocol" inside
`shared-protocols.md`. FPF-Enhancement names the slot but does NOT
supply the verbatim ritual body in Part 10. The closest support text
is §2.7 (verbatim): "Same 150–200 lines duplicated across all 5
experts (wiki write, structured output, HITL, cross-ref, tool self-
check) [D §Part 2 §7]" — confirming the protocol exists in legacy
expert prompts. The mandate (E-7) is to extract it, not redefine it.

**Gap-flag:** FPF Part 10 silent on the tool-permission self-check
ritual body — orchestrator must extract from existing expert system
prompts (legacy §7 source) when composing Deliverable 6, or flag for
Sub-agent E to mine MASTER-SYNTHESIS.

---

## Section 11 — `mode: writing-support`

Part 10.5 mandates a "`mode: writing-support` clause (E-10)" inside
`shared-protocols.md`. The verbatim contract (Part 5 §5.3 enhancement
E-10):

"Add a `mode: writing-support` sub-clause inside §7 (shared
protocols) for all 5 experts: 'If invoked to contribute to a weekly
review, quarterly letter, or strategizing document, DO NOT generate
primary prose. Return: (a) structured extractions from cited
artefacts, (b) proposed alternatives enumerated, (c) explicit
anti-scope list. Human owns composition.'"

Reinforcing Block 5 `never:` list (verbatim, §5.3): "No agent writes
the weekly review primary text. No agent writes the quarterly letter
primary text. Meta-agent may EDIT-CHECK (sections missing?) but not
REWRITE."

Anti-pattern lock (verbatim, [B §E.3]): "полная автоматизация
writing... «без внешнего по отношению к LLM контуру обработки текста
— никак, LLM всегда обманет». Если и сам текст пишет LLM — исчезает
«мышление письмом» как когнитивный процесс."

Architecture-spec mandate: when invoked with `mode: writing-support`
the sub-agent produces drafts (extractions + alternatives + anti-
scope) only and never writes primary prose to the wiki directly.

---

## Section 12 — Tool-language abstractions

Part 10.5 mandates "Tool-language abstractions (Frontmatter /
snapshot / local gate)" inside `shared-protocols.md`. The verbatim
verb dictionary (Part 2 §2.7 enhancement E-7 move 2):

"Rename tooling tokens to pattern-layer abstractions in the shared
protocols file: 'YAML frontmatter' → 'Frontmatter'; 'git commit' →
'snapshot'; 'pre-commit hook' → 'local gate'. This is Rec-13 P2
scoped down [E §3.4 Rec-13] — Core/Tooling soft split."

Rationale (verbatim, §2.7): "`E.5.3 Unidirectional Dependency`
(Core→Tooling→Pedagogy) [E §Part 1.3] is the canonical rule for such
shared layers. Currently 'not enforced'; Jetix actively violates
`E.5.1 DevOps Lexical Firewall` (uses 'yaml', 'git', 'pre-commit' in
Core) [E §T6]."

Lock note (verbatim): "Lock 17 (Filesystem = SoT) preserved; this is
purely naming-layer discipline."

**Gap-flag:** FPF Part 10 lists only three rename pairs (yaml→
Frontmatter, git commit→snapshot, pre-commit hook→local gate). The
full verb dictionary for the shared-protocols file is not supplied —
orchestrator may extend in Deliverable 6 or defer.

---

## Appendix — Alpha ownership matrix (verbatim, §4.2)

| Alpha | Primary owner | Secondary touchers | Transition gate |
|---|---|---|---|
| α-1 Task | brigadier | All experts (consume) | Human HITL at `gated→approved` |
| α-2 Artefact | producing cell | integrator, brigadier | Conformance Checklist |
| α-3 Strategies-Rule | meta-agent (tombstoning) | brigadier, all experts | ✓/✗ ratio threshold |
| α-4 Cycle | brigadier | meta-agent (audit) | HITL approval |
| α-5 Direction | human | All experts (evidence) | Human activation authority |

ШСМ-primitive mapping (verbatim): "all 5 alphas operationalize **Альфа**
[A §1.2]; α-4 additionally operationalizes **Стратегирование** triggers.
Transdisciplinary home: **Методология** (α-1..α-4) + **Системная
инженерия** (α-5) [C §Part 1]."
