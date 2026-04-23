---
title: Sub-agent D — Matrix 5 × 4 Mode Mechanics + Rubric Enhancements
date: 2026-04-23
extraction_for: prompts/step-2-2-4-agent-construction-2026-04-23.md
sources:
  - decisions/ROY-ALIGNMENT-2026-04-22.md (full)
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md (§5.2 — note: orchestrator brief referenced §5.3, but §5.2 is where the per-mode base rubric structure lives; §5.3 is coordination protocol)
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (E-3..E-6, plus E-11 Janus backfill for §6)
status: ready-for-orchestrator-consumption
sub_agent: D
---

# Matrix 5 × 4 — mode mechanics + rubric enhancements

This extraction fixes the **mechanics** of the 5 × 4 matrix — how modes
activate, how they refuse, what predicates they enforce, what schemas
they emit. The **content** per (expert × mode) cell is left for the
drafter + Sub-agent E's canonical-source allocation (§9 of this file).

---

## 1. The 5 × 4 matrix at a glance

Rows = 5 experts; columns = 4 modes. Cell = one-sentence "what this
expert in this mode produces". Synthesized from ROY-ALIGNMENT §3
(mode definitions) + §2 (canonical sources) + master synthesis §5.2.

| Expert \ Mode | critic | optimizer | integrator | scalability |
|---|---|---|---|---|
| **engineering** | Adversarial review of architecture proposal — over-engineering, premature abstraction, fragile pattern flags (Ousterhout / Martin lens) | Refactor / simplification delta with preserved invariants (Fowler / Ousterhout deep-module / Boris do-simple-thing) | Coherent architecture synthesis across code / infra / AI-native tool choices (Karpathy / Anthropic eng) | ≤30% refactor-at-10× gate assessment + degraded-mode for software system (Shape Up scope hammering + Brooks no-silver-bullet) |
| **mgmt** | Challenge roadmap / process bloat via empowered-team lens (Cagan / Shape Up minimalism) | Priority-ranking / delivery-plan compression (Grove HOM leverage + Drucker effectiveness) | Stakeholder-map + strategy-tactics synthesis (Cagan vision-strategy-tactics, Horowitz) | Org horizon projection (solo → small team → phase-2 manager) + Laloux evolutionary stage gates |
| **systems** | Feedback-loop / leverage-point critique (Meadows / Senge 11 laws) — spot structural fragility | Cybernetic simplification (Ashby requisite variety, Beer VSM redundancy removal) | Unified system model — boundary, feedback, emergence — across sub-systems (Meadows + Kauffman) | Emergence / phase-change projections across scale thresholds (West scaling, Beer VSM recursion, Kelly out-of-control) |
| **philosophy** | Epistemic audit — claim status, falsifiability, hidden-assumption flag (Popper / Munger) | First-principles reset — strip prose to invariants (Descartes / Koen / Altshuller TRIZ) | Meta-decision synthesis — reconcile framings through epistemic coherence (Kuhn paradigm alignment + Naval) | Long-horizon mental-model stress test — which paradigms break under scale (Kuhn + Stoics via-negativa) |
| **investor** | Capital-allocation critique — unit-econ / moat / risk-of-ruin flag (Buffett / Graham / Marks) | Portfolio / resource simplification via margin-of-safety + opportunity-cost pruning (Graham + Munger) | Capital-structure synthesis — allocate across bets consistently with long-term compounding (Buffett letters + Marks) | Horizon projection €50K → $1T + antifragility ledger (Taleb antifragile / skin-in-the-game) |

Brigadier sits OUTSIDE this matrix (ROY-ALIGNMENT §2). Every matrix
cell is reachable only through brigadier's Task() dispatch (master
synthesis §5.3.1).

---

## 2. §3 Critic mode — base rubric + E-3 rows

### 2.1 Base rubric (master synthesis §5.2.1)

Critic mode activates when `mode == "critic"`. Skeleton (300–500 lines
per expert):

- Activation check; adversarial rubric (Hamel-binary criteria).
- Failure-pattern library (domain-specific from §2 + MAST + AP-1..26).
- 3–5 domain few-shot critique examples.
- Escalation conditions (when critic defers to HITL).
- Output schema: `{context, critique, specific-failures-found,
  recommended-changes, acceptance-test}`.

**Intent.** Critic is the **Conformance-Checklist enforcer** for the
domain (FPF §2.3). Adversarial lens. Not cheerleader. Not integrator —
its job is to surface weakness, not patch it.

### 2.2 E-3 enhancement rows (FPF §2.3 / Appendix A)

Critic rubric MUST have 4 explicit rows, applied to every critic
output:

1. **Conformance Checklist** — ≥ 5 domain-specific checks the artefact
   must satisfy. Each check is a binary predicate (pass / fail) tied
   to the expert's canonical patterns (e.g. engineering → Ousterhout
   deep-module; philosophy → Popper falsifiability). The checklist is
   the negation-space of known APs; failing a check surfaces an AP.

2. **Acceptance Predicate** — a single boolean predicate stated in
   Hamel-binary form (not prose). Format: a one-line condition that
   either holds or does not hold over the artefact. MS §5.2.1 AP-25
   already requires an acceptance-test in the output schema; E-3
   sharpens "must be Hamel-binary, not prose" (FPF §2.3).

3. **≥ 2 Alternatives** — critic enumerates ≥ 2 viable alternatives
   to the proposed artefact plus status-quo, each with an explicit
   kill-condition (FPF §2.3 citing `[A §1.4, R-B §4.5]`). Surfacing
   one alternative only = fail the critic's own rubric.

4. **Anti-scope** — explicit enumeration of what the artefact is NOT
   trying to do. Prevents scope-creep in the critique itself and in
   the critiqued artefact.

### 2.3 §3 agent-file template (generic)

```markdown
## §3 Mode: critic (activated when mode == "critic")

### 3.0 Activation gate
Read `mode` from prefix. If != "critic", jump to §7.

### 3.1 Conformance Checklist (≥ 5 domain-specific binary checks)
[drafter supplies 5+ checks rooted in Sub-agent E's canonical-source
allocation for this expert. Each check = one-line predicate.]

### 3.2 Acceptance Predicate
Produce exactly one Hamel-binary predicate over the artefact-under-
review. Prose predicates are rejected by the verifier.

### 3.3 ≥ 2 Alternatives + kill-conditions
Enumerate ≥ 2 viable alternatives + status-quo. Each carries a
kill-condition ("this alternative fails when X"). One-alternative
outputs = critic self-failure → retry or escalate.

### 3.4 Anti-scope
Bulleted list: "this artefact is NOT trying to do Y". Surfaces drift
into adjacent experts' territory (reroute via brigadier).
```

Each subsection is 2–3 sentences of mechanism here; the drafter fills
content per-expert using Sub-agent E's allocations.

---

## 3. §4 Optimizer mode — base rubric + E-4 invariants

### 3.1 Base rubric (master synthesis §5.2.1)

Optimizer activates when `mode == "optimizer"`. Skeleton:

- Optimization rubric (measurable delta: turns / tokens / complexity /
  LoC).
- Simplification heuristics (Ousterhout deep-modules / Boris
  do-simple-thing / Poppendieck waste-elimination).
- 3–5 optimizer few-shots.
- Refusal conditions ("I cannot optimize a design that lacks
  acceptance criteria — defer to critic").
- Output schema: `{baseline, proposed, delta, justification, risks}`.

### 3.2 E-4 invariants (FPF §2.4 / Appendix A)

Five invariants gate every proposed optimization. Letter expansions
that are not literally spelled out in FPF §2.4 are flagged.

1. **WLNK** — `[E-4 says only "WLNK"; expansion not specified in FPF
   §2.4 beyond listing it with the other Γ-operator invariants]`.
   Convention: treat as a link/workflow-preservation invariant tied
   to the Γ-operator consumer role (FPF §2.4). Check predicate:
   "Does the proposed delta preserve workflow links / upstream-
   downstream contract points?" Failure consequence: silent contract
   violation.

2. **MONO** — monotonicity. `[FPF §2.4 lists MONO in the Γ-operator
   invariant set without a one-line definition]`. Convention: check
   that the optimization does not flip direction of an ordered
   quality (e.g. does not turn a monotone-decreasing cost curve
   non-monotone). Check: "Is every invariant-scored quality still
   monotone in the intended direction after the delta?" Failure:
   regression injected under "optimization" framing.

3. **IDEM** — idempotency. Check: "Is re-applying the optimized
   step equivalent to applying it once?" Failure: drift under repeat
   invocation.

4. **COMM** — commutativity. Check: "Does the order of this
   optimization relative to adjacent steps change output?" Failure:
   order-dependent fragility.

5. **LOC** — locality. Check: "Does the delta touch only the
   artefact's intended scope, or does it reach beyond?" Failure:
   scope-leak optimization.

For each invariant: (a) definition / convention (verbatim where FPF
gives it, flagged where it does not), (b) check predicate, (c) failure
consequence.

**Hard refusal (E-4 verbatim).** Optimizer CANNOT optimize a **Method**
(capital-M). "If the proposed optimization changes the method itself,
not only the execution parameters, escalate — this is strategizing
territory." Strategizing is human-only (FPF §2.4 citing `[A §1.4, R-B
§4.3 L510-524]`).

### 3.3 §4 agent-file template (generic)

```markdown
## §4 Mode: optimizer (activated when mode == "optimizer")

### 4.0 Activation gate

### 4.1 Invariant-check row (PRECONDITION — before any delta)
For each of WLNK / MONO / IDEM / COMM / LOC, state: (a) does this
invariant apply to the artefact, (b) does the proposed delta preserve
it. If unclear on any — defer to integrator mode. No delta ships with
unresolved invariants.

### 4.2 Before/after snapshot (REQUIRED)
Baseline and proposed, with measurable delta (turns / tokens /
complexity / LoC) in a single table.

### 4.3 Method-change refusal
If the proposed optimization changes the Method (not merely execution
parameters), refuse per shared-protocols §4 HITL-bounce.

### 4.4–4.5 domain heuristics + few-shots
[drafter fills per-expert]
```

---

## 4. §5 Integrator mode — base rubric + E-5 schema

### 4.1 Base rubric (master synthesis §5.2.1)

Integrator activates when `mode == "integrator"`. Skeleton:

- Integration rubric (all inputs accounted; dissents surfaced;
  synthesis verifiable).
- Synthesis heuristics (Cagan vision-strategy-tactics; Senge 11 laws;
  Anthropic Orchestrator-Workers pattern).
- Dissent-preservation (AP-6 prevention).
- Output schema: `{inputs, synthesis, dissents-flagged,
  residual-open-questions, recommended-next-step}`.

### 4.2 E-5 per-claim F / ClaimScope / R schema (FPF §2.5)

Integrator is the swarm's **F-G-R** (Formality × ClaimScope ×
Reliability) gate-keeper (FPF §2.5). Every claim in the integrator's
synthesis MUST carry three fields in frontmatter:

- **F (Formality)** — level on a scale F0 (rumor) … F9 (formal
  proof). Phase-A lightweight: integrator **declares** the level; does
  not compute machinery. Compound step harvests mismatches (FPF §2.5
  citing `[E §Part 1.1 G2]`).

- **ClaimScope** — which bounded context the claim holds in (e.g.
  "holds for solo-founder phase-A; unknown for phase-B managed team").
  Where does it NOT apply (explicit).

- **R (Reliability / Refutation-Receipt)** — pathwise reliability,
  not a point estimate. States: under what conditions the claim would
  be refuted (receipt of rejection); under what conditions it is
  currently accepted (receipt of acceptance).

**Dissent-record typing (FPF §2.5).** When two experts disagree with
different F-levels, integrator preserves both dissents rather than
averaging. Each dissenting claim tagged with its own (F, ClaimScope,
R) triple.

### 4.3 §5 agent-file template (generic)

```markdown
## §5 Mode: integrator (activated when mode == "integrator")

### 5.0 Activation gate

### 5.1 Per-claim F / ClaimScope / R declaration (REQUIRED)
Every claim in the synthesis carries three fields:
  F: F0 | F1 | ... | F9
  ClaimScope: <where holds / where does not>
  R: <refutation condition / acceptance receipt>

### 5.2 Dissent preservation
Contradicting claims from different experts → both retained, each
with its own (F, ClaimScope, R) triple.

### 5.3 Worked example (template)
claim: "Single-writer wiki Phase A is sufficient"
F: F4 (operational convention, no proof)
ClaimScope: holds for Phase-A 1 human + 6 agents; NOT valid Phase-C
  (multi-region replication).
R: refuted if write-conflict observed once in first 50 cycles;
   accepted if 50 cycles conflict-free (receipt = cycle-log hash).

### 5.4 Output schema (MS §5.2.1 §5 + E-5 extension)
{inputs, synthesis, dissents-flagged[(F,ClaimScope,R)],
 residual-open-questions, recommended-next-step}
```

---

## 5. §6 Scalability mode — base rubric + E-6 BOSC-A-T-X + Janus

### 5.1 Base rubric (master synthesis §5.2.1)

Scalability-architect activates when `mode == "scalability"`.
Skeleton:

- Scalability rubric (≤ 30% refactor per 10× gate per Brief §5.1;
  antifragility check; degraded-mode spec).
- Long-horizon heuristics (West scaling, Beer VSM recursion, Taleb
  via-negativa).
- Horizon projection template €50K → €200K → €1M → $100M → $1T.
- Output schema: `{horizon, projection, gate-risk-table,
  degraded-mode-spec, antifragility-check}`.

### 5.2 E-6 BOSC-A-T-X trigger (FPF §2.6)

FPF §2.6: `B.2 BOSC-A-T-X` triggers "(Boundary / Operation / Scale /
Composition / Agency / Time / eXternal)" — verbatim from FPF L271-272.
Per-letter expansion:

- **B = Boundary** — the system's boundary definition changes (what's
  in / out of the holon).
- **O = Operation** — the primary operation (core verb) of the system
  changes at this scale.
- **S = Scale** — pure magnitude threshold (10× / 100× / 10000×).
- **C = Composition** — internal part-structure changes (new
  sub-holons, sub-holon removal).
- **A = Agency** — who decides / who acts shifts (e.g. single-founder
  → managed team → board).
- **T = Time** — cycle time or horizon changes (daily → quarterly →
  multi-year).
- **X = eXternal** — external-environment shift (market / regulatory
  / technological).

**Trigger observables.** Scalability-mode's rubric must list, per
horizon gate (€200K / €1M / $100M / $1T), which of BOSC-A-T-X is
expected to fire first and what **MHT event** (Fission / Phase
Promotion / Role-Lift / Fusion / Context Reframe — FPF §2.6 citing
`[E §3.3 Rec-06]`) the swarm must undergo when it fires. Explicit
named events, not prose.

### 5.3 E-6 Janus degraded-mode spec (FPF §2.6 + §8.1 Rule A)

Janus duality (FPF Rule A, §8.1, L1032–1054): every holon is
whole-inward and part-outward. Two swarm-level failure modes:

- **9.4 S-A excess** — self-assertive excess — expert "monopolizes
  functions, to the detriment of the whole" (e.g. critic-mode expert
  always critiques, never defers to integrator).
- **9.5 INT excess** — integrative excess — expert "erodes autonomy,
  defers everything to brigadier" (e.g. never holds a position).

The Janus **degraded-mode spec**: when the system cannot sustain full
mode operation (e.g. one expert is budget-capped or rate-limited),
scalability-mode declares a **dual-faced contingency** — for each
expert, what the swarm does when that expert is S-A-excess
constrained vs INT-excess constrained. Degraded path is explicit, not
improvised.

### 5.4 §6 agent-file template (generic)

```markdown
## §6 Mode: scalability-architect (activated when mode == "scalability")

### 6.0 Activation gate

### 6.1 BOSC-A-T-X trigger predicates (per horizon gate)
For each of {€200K, €1M, $100M, $1T}:
  trigger: <which of B/O/S/C/A/T/X fires first>
  MHT-event: <Fission | Phase-Promotion | Role-Lift | Fusion |
              Context-Reframe>
  observable: <what we see when the trigger fires>

### 6.2 Janus degraded-mode procedure
For each containing holon + contained holon relation, spec the
contingency:
  S-A-excess path: <behaviour when expert monopolizes — brigadier
    bounces to HITL per Rule A §8.1>
  INT-excess path: <behaviour when expert over-defers — prompt
    re-issued with forcing clause>

### 6.3 Recovery condition
Binary predicate: under what observable does the swarm return from
degraded → full mode?

### 6.4 Output schema (MS §5.2.1 §6 + E-6 extensions)
{horizon, BOSC-A-T-X-trigger-table, MHT-events, degraded-mode-spec,
 antifragility-check, recovery-predicate}
```

---

## 6. Soft activation — `mode: <name>` prompt prefix

**Rule.** Every Task() invocation to an expert MUST begin with a
one-line prefix:

```
mode: critic
```
(or `optimizer` / `integrator` / `scalability`).

The expert reads the prefix from the first line of its prompt body
and switches behaviour. Source: MS §5.2.2 "mode activation mechanic
(the gate)" + §5.3.1 task invocation schema showing `mode:` field.

**Agent-file contract for §§3–6.** Each §§3–6 opening paragraph MUST
read:

> "When this agent is invoked with prefix `mode: <name>`, it activates
> the §N rubric below. The expert reads §1 identity + §2 domain
> knowledge + §N (this section) + §7 shared protocols + §§8–9
> metadata. Other modes (§§ not matching the prefix) are SKIPPED."

MS §5.2.2: "This is a prompt-level soft constraint, not an
enforceable gate." Therefore hard enforcement is layered on top —
see §7 below.

Default-mode rule (MS §5.2.2): "If `mode` in context is not set →
treat as `integrator` (default for summaries and single-domain
queries)." Stated verbatim in each expert's activation-gate line.

---

## 7. Hard enforcement — UserPromptSubmit hook scaffold

The Claude Code UserPromptSubmit hook (MS §5.6.4 + §5.2.2 option A)
provides the hard gate. Three checks at the tool layer:

1. **Frontmatter mode declaration consistency** — the invoked expert
   declares supported modes in its YAML frontmatter; hook compares
   declared modes vs prefix mode.
2. **Prefix presence + validity** — first line must match
   `^mode: (critic|optimizer|integrator|scalability)$`.
3. **Per-expert mode allowlist** — if the prefix mode is NOT in the
   expert's frontmatter-declared supported modes, refuse (see §8).

**Agent-file contract for §§3–6.** Each §§3–6 MUST contain a boxed
paragraph:

> "A UserPromptSubmit hook (registered in `.claude/settings.json` —
> implementation deferred to Phase B) validates: prefix matches
> `^mode: <this-mode>$` AND this mode is listed in the agent's
> frontmatter `supports_modes:` array. If the predicate fails, the
> hook blocks the prompt with structured refusal per §8."

**Stub vs contract boundary (explicit).** The agent file documents
the **contract** (what the hook guarantees + what failure looks
like). The **hook implementation itself is a STUB** — a Phase-B /
next-pass deliverable registered in `.claude/settings.json`. Phase A
ships the contract + expert-side refusal logic; Phase B ships the
hook code. This bifurcation is non-negotiable — Шаг 2.2.4 delivers
contract, not hook.

---

## 8. Refusal behaviour for unsupported modes

Example: `mgmt-expert` invoked with `mode: scalability` on a purely
engineering artefact not assigned to mgmt × scalability by the matrix.
The expert refuses via HITL bounce per shared-protocols §4 (MS §5.3.2
output schema supports `"status": "refused"`).

**Refusal template (structured JSON the expert returns on refusal):**

```json
{
  "status": "refusal",
  "reason": "mode:<requested> not in this expert's supports_modes OR
             artefact scope not within matrix cell (<expert>×<mode>)",
  "escalation": "HITL",
  "alternative_routing": "suggest <other-expert>:<mode> OR re-issue
                         as <this-expert>:<different-mode>",
  "artefact_path": null,
  "turns_used": 1,
  "verifier_result": null
}
```

This schema is the refused-variant of MS §5.3.2's canonical cell
return. Brigadier receives the refusal, logs it, re-routes or
escalates to HITL per resume protocol §5.3.4.

---

## 9. Mode-content vs mode-mechanics separation (for the drafter)

This extraction defines the **MECHANICS** — activation (§6), hard
enforcement (§7), refusal (§8), predicates (§§2.2, 3.2, 4.2, 5.2–3),
output schemas (§§ 2.3, 3.3, 4.3, 5.4), rubric row requirements
(§§ 2.2, 3.2, 4.2, 5.2–3).

The **CONTENT** per (expert × mode) cell — what specifically
critic-mode looks like for engineering vs philosophy, which canonical
quotes anchor optimizer for investor vs systems, which checklist
items populate the engineering critic's Conformance Checklist —
comes from:

- Sub-agent E's canonical-source allocation (per ROY-ALIGNMENT §2 +
  MS §5.2.3 table).
- Drafter creativity within these locked schemas (choose the 5+
  binary checks; compose the 3–5 few-shots; write the specific
  Acceptance Predicate grammar for this domain).

The drafter MUST NOT alter: schema field names, invariant letter
codes (WLNK / MONO / IDEM / COMM / LOC), BOSC-A-T-X letter codes, F /
ClaimScope / R codes, refusal JSON shape, or the mode-prefix
grammar. The drafter MAY freely choose: domain-specific check wording,
few-shot examples, heuristic chains, canonical quotes, horizon-
specific BOSC-A-T-X predictions per expert.

This separation is what lets Шаг 2.2.4 keep all 5 experts consistent
at the mechanics layer while each expert reads maximally different
at the content layer.
