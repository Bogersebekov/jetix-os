---
title: "Eng-critic review — Doc 02 Jetix as Methodology"
date: 2026-05-17
type: eng-critic-review
status: draft
artefact_under_review: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-methodology-eng-integrator.md
reviewer_cell: engineering-expert × critic
cycle_id: task-fpf-describe-jetix-2026-05-17
F: F4
G: eng-critic-review-methodology
R: refuted_if_conformance_checklist_passes_are_incorrect_upon_recheck
prose_authored_by: engineering-expert-cell
---

# Eng-critic review — Doc 02 Jetix as Methodology

> **Scope.** Adversarial review of `swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-methodology-eng-integrator.md` per §3 critic rubric. Focus areas per brief: U.WorkPlan A.15.2 correctness, ШСМ/МИМ overlay typing, E.17 MVPK application, A.1.1 BoundedContext, cross-doc consistency with Doc 01.

---

## §1 Acceptance predicate verdict

**Acceptance predicate (Hamel-binary):**

`task-fpf-describe-jetix-2026-05-17-methodology-eng-integrator.md` passes Conformance checks 1 (deep-module N/A), 2 (function-purpose N/A), 3 (test-integrity N/A), 4 (premature-abstraction pass), 5 (external-dep N/A), 6 (DRY pass), 7 (tool-eval N/A), 8 (architecture-pattern N/A for narrative doc) AND has ≥2 alternatives AND has anti-scope declarable.

**Verdict: CONDITIONAL PASS with 3 specific failures requiring revision before canonical promotion.**

The document is substantially correct — the U.MethodDescription assignment (A.3.2) is sound, the F-G-R floor is honest, the EP-5/EP-2 disclosures are present and correctly placed. Three failures are blocking: (1) U.WorkPlan A.15.2 misapplication — the §2.3 claim of correct application is premature; (2) A.1.1 BoundedContext declaration absent for Doc 02 — Doc 01 has it (§4.1 with Glossary/Invariants/Roles/Bridges), Doc 02 has no equivalent; (3) ШСМ/МИМ typing left unresolved without explicit out-of-scope declaration. All three are fixable in a revision pass without structural rewrite.

---

## §2 Conformance Checklist

| Check | ID | Result | Evidence |
|---|---|---|---|
| 1 | deep-module | N/A | Non-code artefact — §1b check inapplicable |
| 2 | function-purpose | N/A | Non-code artefact |
| 3 | test-integrity | N/A | No tests in scope |
| 4 | premature-abstraction | PASS | U.Episteme (A.16), U.MethodDescription (A.3.2), U.Method (A.3.1) all have ≥3 concrete uses cited in §2 and §4 formal block; B.5.1 tagged as candidate; no ungrounded abstractions |
| 5 | external-dep | N/A | No external call sites |
| 6 | DRY | PASS | No substantive logic duplicated across sections; §2.3 / §4 formal block are complementary (different grain), not copied |
| 7 | tool-eval | N/A | Not a tool-eval.md artefact |
| 8 | architecture-pattern | N/A | Not an architecture-proposal.md artefact |

**Domain-specific checks for FPF primitive assignment documents (per this critic's scope):**

| Check | ID | Result | Evidence |
|---|---|---|---|
| FPF-1 | A.3.2 MethodDescription assignment | PASS | §2.1 correctly applies A.3.2 — Jetix-MethodDescription has steps, performers, input/output format; sector-agnostic usage is coherent with FPF Spec «domain-agnostic primitives» |
| FPF-2 | A.15.2 WorkPlan application | **FAIL** | §2.3 claims correct application but Fork guide v0 satisfies only 2 of 5 A.15.2:4.1 required fields — see §3 below |
| FPF-3 | A.1.1 BoundedContext declaration | **FAIL** | Doc 02 declares no BoundedContext block — Doc 01 §4.1 has full Glossary/Invariants/Roles/Bridges; Doc 02 §4 formal block lacks equivalent; §6 cross-ref table is not a BoundedContext declaration |
| FPF-4 | ШСМ/МИМ typing completeness | **FAIL (soft)** | OQ-D02-2 raises the question but §2.4 and the formal block do not resolve it; ШСМ/МИМ appears in §3.3 narrative and mermaid as «онтологический субстрат» without FPF primitive assignment or explicit out-of-scope declaration |
| FPF-5 | E.17 MVPK application | PASS (with dissent — see §7) | Three views present (§3 narrative, §4 formal, §5 mermaid); single source-of-truth (this document) → views architecture is coherent with E.17 intent |
| FPF-6 | Cross-doc role declaration consistency | PARTIAL FAIL | Doc 01 §4.1 declares Ruslan#OwnerRole + ROY-swarm#AIScribeRole scoped to Self-OS-substrate-BoundedContext; Doc 02 §8 reaffirms R1 but does NOT declare U.RoleAssignment scoped to a Doc-02 BoundedContext |
| FPF-7 | F-G-R completeness | PASS | Every §2 claim has F/G/R triple; F floor F2 is correct and honest; per-claim grades F2–F5 are plausible given source strength |
| FPF-8 | EP-5 / EP-2 disclosure | PASS | Both disclosures present in frontmatter, §0 callout block, and §3.7 |

---

## §3 Specific failures found

### FAIL-1 — U.WorkPlan A.15.2 misapplication (AP-ENG primary claim)

**Location:** §2.3 (lines 130–143), §4 formal block U.WorkPlan section (lines 306–315)

**Evidence from FPF Spec A.15.2:4.1 (verbatim):**

> `U.WorkPlan` is a `U.Episteme` that **declares intended `U.Work` occurrences** over a horizon, with **planned windows**, **dependencies**, **intended performers** (as role kinds or proposed RoleAssignings), **resource budgets/reservations**, and **acceptance targets** — within a `U.BoundedContext`.

Five required fields per A.15.2:4.1: (1) planned windows, (2) dependencies, (3) intended performers, (4) resource budgets/reservations, (5) acceptance targets.

**Doc 02 §4 formal block audit:**

```
U.WorkPlan [A.15.2] «Jetix-methodology-workplan»
  planned_occurrences:           ✓ present (daily / weekly / per-cycle / per-forker)
  performers_planned:            ✓ present (Ruslan confirmed; forker-N aspirational)
  temporal_windows:
    daily_window: Part 9 cadence (spec; runtime enforcement STUB)   ← STUB, not a window
    forker_onboarding_window: undefined in v0 (LIVE-FLAG)           ← explicitly absent
  dependencies:                  ✗ ABSENT (no dependency graph between occurrences)
  resource_budgets:              ✗ ABSENT (no budget/reservation declared)
  acceptance_targets:            ✗ ABSENT (no acceptance criteria for occurrence completion)
```

**Score: 2 of 5 required fields satisfied.** The draft's claim that «U.WorkPlan применяется правомерно» (§2.3) is incorrect against the spec. The R-condition in the frontmatter — `refuted_if_Fork_guide_v0_lacks_temporal_windows_upon_detailed_audit` — is itself refuted by this audit: the daily window is a spec stub, the forker window is undefined, dependencies are absent, budgets absent, acceptance targets absent.

**What §2.3 correctly identifies:** the *intent* to use U.WorkPlan is sound — methodology occurrences (daily Ruslan application, per-cycle compound, per-forker activation) are genuinely planned occurrences in the A.15.2 sense. The primitive is correctly chosen for the ontological category. The problem is that Fork guide v0 does NOT yet satisfy the A.15.2:4.1 structural requirements.

**Recommended resolution:** Relabel as «proto-WorkPlan» or «U.WorkPlan candidate» — same relabeling discipline as Doc 01 used for U.MethodDescription. Adjust F grade from F4 to F2 (aspirational: correct primitive, missing 3/5 required fields). Add a note: «U.WorkPlan v1.0 requires: defined temporal windows per occurrence type + dependency graph + resource budget + acceptance targets. Fork guide v1.0 activation trigger per OQ-D02-1.»

**F correction:** F4 → F2 on the WorkPlan claim specifically.

---

### FAIL-2 — A.1.1 BoundedContext declaration absent in Doc 02

**Location:** §4 FPF formal block — no BoundedContext section

**Evidence:** FPF Spec CC-A1.1.2 (flat context map) + A.1.1 table entry «One context carries one perspective with explicit Glossary, Invariants, Roles, and optional Bridges». Doc 01 §4.1 correctly declared a full BoundedContext with Glossary, Invariants (I-1..I-5), Roles (Ruslan#OwnerRole, ROY-swarm#AIScribeRole, Part6b#ConstitutionalEnforcerRole), and Bridges (3 declared).

Doc 02 is a separate FPF-described document covering a distinct primary described entity (O-05 Methodology, not O-01 Substrate). It needs its own BoundedContext declaration or an explicit statement that it operates within the same BoundedContext as Doc 01 — but if the latter, the Bridge from Self-OS-substrate context to Methodology-distribution context must be named.

**The §6 cross-ref table** is not a BoundedContext. It lists connections; it does not declare invariants, glossary terms, roles, or bridges.

**Recommended resolution:** Add a `§4.0 U.BoundedContext (A.1.1) — Doc 02` block before the U.MethodDescription formal declaration. Minimum viable content:
- Glossary: «MethodDescription», «forker», «Fork-and-Leave», «proto-WorkPlan», «ШСМ overlay (pending OQ-D02-2)»
- Invariants: at minimum I-1 (filesystem SoT), I-3 (Pillar C applies), and new I-doc02-1 (Fork-and-Leave without penalty = R12 constitutional constraint applies to all forker occurrences)
- Roles: at minimum Ruslan#MethodologistRole:O-05-Methodology-BoundedContext, ROY-swarm#AIScribeRole:O-05-Methodology-BoundedContext
- Bridge to Doc 01: «O-05 Methodology BoundedContext ↔ O-01 Substrate BoundedContext: MethodDescription is executed on Substrate (U.Method A.3.1 occurrences); bridge = U.Method occurrence runs inside Substrate BoundedContext, described by MethodDescription in Methodology BoundedContext»

Alternative: explicitly defer to Doc 01 BoundedContext with a note «operating within same BoundedContext as Doc 01; cross-doc bridge: Doc 01 hosts execution environment, Doc 02 describes the recipe».

---

### FAIL-3 (soft) — ШСМ/МИМ typing unresolved without explicit out-of-scope declaration

**Location:** §3.3, §4 formal block (ONTOSUBSTRATE node in mermaid), OQ-D02-2

**Evidence:** §3.3 states «Jetix строится на онтологическом фундаменте Анатолия Левенчука: ШСМ и МИМ» and the mermaid diagram shows «Онтологический субстрат / FPF (Левенчук) + ШСМ + МИМ». But ШСМ/МИМ has no FPF primitive assignment anywhere in the document. The brief identifies this as an anticipated dissent — is it U.MethodDescription (Anatoly's recipe) or U.Episteme (epistemic substrate)?

The document raises OQ-D02-2 in §7 but does not resolve it OR declare it explicitly out-of-scope for Doc 02. This violates the anti-scope discipline: if the doc mentions ШСМ/МИМ as a substantive architectural element (it appears in the mermaid as a direct dependency of the primary U.MethodDescription), it must either type it or declare it deferred.

**Assessment of the typing question:** ШСМ (Школа Системного Менеджмента) as an institution/educational program is most naturally a U.System (A.1) or U.MethodDescription (A.3.2) depending on what aspect is being referenced. МИМ (Мастер Информационного Моделирования) as a practitioner role is U.Role (A.2) or U.RoleAssignment (A.2.1). FPF itself as the formal spec is U.Episteme (A.16). The mermaid conflates all three under «Онтологический субстрат» — this is a category-mix that an L1 audience (Anatoly + Tseren) would notice.

**Recommended resolution:** Choose one of:
- (A) Add stub FPF typing: «ШСМ = U.MethodDescription (A.3.2) candidate [Anatoly's methodology-as-recipe]; МИМ = U.Role (A.2) [practitioner role kind]; FPF spec = U.Episteme (A.16) [governing episteme]» — grade F2 for all three (pending Ruslan ack)
- (B) Declare explicitly out-of-scope: add anti-scope bullet «§3.3 ШСМ/МИМ overlay is referenced as narrative context for the ontological substrate claim; formal FPF primitive assignment deferred to O-22 stub (OQ-D02-2 pending Ruslan decision)»

Option B is lighter and safer given B.5.1 Exploration state. Option A risks over-typing before Ruslan ack.

---

## §4 Acceptance Predicate (Hamel-binary)

`task-fpf-describe-jetix-2026-05-17-methodology-eng-integrator.md` passes if and only if: (a) U.WorkPlan §2.3 claim is relabeled «proto-WorkPlan candidate» with F2 grade and OQ-D02-1 as blocking for v1.0; AND (b) A.1.1 BoundedContext block for Doc 02 is added to §4 formal section; AND (c) ШСМ/МИМ is either stub-typed (F2) or explicitly declared out-of-scope with deferred reference to OQ-D02-2; AND the remaining §2 content (U.MethodDescription F5, U.Method F5, U.Episteme F5, E.17 F4, B.5.1 F4) is unchanged.

---

## §5 Alternatives + status-quo + kill-conditions

| # | Alternative | Kill condition |
|---|---|---|
| A | Revision pass: fix 3 failures per §3 recommendations — relabel WorkPlan as proto-WorkPlan (F2), add Doc-02 BoundedContext block, add ШСМ/МИМ out-of-scope declaration | Fails if added BoundedContext block introduces new contradictions with Doc 01 BoundedContext (e.g. role conflict between Ruslan#OwnerRole:Self-OS-substrate vs Ruslan#MethodologistRole:O-05-Methodology — must verify they are not the same context) |
| B | Defer U.WorkPlan claim entirely — drop §2.3 from this doc, move to OQ-D02-1, add footnote «WorkPlan application deferred to Fork guide v1.0» | Fails if Ruslan considers the planned-occurrence framing (daily application, per-cycle compound) important enough to preserve in this doc for L1 audience |
| C | Status-quo (promote as-is) | Fails immediately: L1 audience (Anatoly) is a FPF spec author — he will notice the A.15.2:4.1 non-compliance and the missing BoundedContext; this would undermine the doc's credibility with the target audience before §3 narrative is even read |

**Recommendation: Alternative A.** Revision is tractable (adds ~100 words to §2.3, ~150 words to §4, one anti-scope bullet). All primary value in the doc (U.MethodDescription assignment, B.5.1 honest state, E.17 MVPK structure, R12 constitutional framing) is preserved.

---

## §6 Anti-scope

- **Not evaluating strategic value of FPF adoption.** Whether Jetix should use FPF at all = α-5 Direction, HITL only.
- **Not evaluating the R12 principle content.** R12 anti-extraction constitutional guarantee is Ruslan-authored; this critic reviews FPF primitive correctness only.
- **Not comparing ШСМ/МИМ vs other ontological substrates.** Alternative ontologies (TOGAF, Zachman, etc.) are outside this review scope.
- **Not evaluating §3 narrative prose quality for L1 audience.** Whether the plain-Russian narrative is persuasive to Anatoly/Tseren = content judgment (HITL); this critic evaluates FPF structural correctness only.
- **Not optimizing.** This is critic-only mode. Proposed revision text in §3 is illustrative, not prescriptive; brigadier dispatches optimizer if needed.
- **Not evaluating Doc 01 ↔ Doc 02 strategic sequencing.** Order of presentation to Anatoly = mgmt territory.

---

## §7 Anticipated dissents — verification + new dissents

### Anticipated dissent 1 (from §8 of reviewed doc): U.WorkPlan A.15.2 strict applicability

**Claim in reviewed doc:** «Phil-critic likely dissent — Fork guide v0 may not satisfy strict A.15.2 temporal windows requirement.»

**Eng-critic verdict: CONFIRMED and EXTENDED.** The dissent is understated. It is not just temporal windows — dependencies, resource budgets, and acceptance targets are also absent (3 of 5 required fields, not 1 of 5). The reviewed doc grades this F4 and conditions the R on «audit of Fork guide v0» — that audit is now complete. R condition fires: U.WorkPlan is not correctly applied at F4.

**Disposition:** FAIL-1 above. Downgrade to F2 proto-WorkPlan candidate.

---

### Anticipated dissent 2 (from §8 of reviewed doc): ШСМ/МИМ overlay not FPF-typed

**Claim in reviewed doc:** «Eng-critic or phil-critic may request O-22 stub or explicit out-of-scope declaration.»

**Eng-critic verdict: CONFIRMED.** The typing gap is real. The mermaid shows ШСМ/МИМ as a direct architectural dependency of the primary U.MethodDescription (ONTOSUBSTRATE node connected to MD node with «MD → ONTOSUBSTRATE» edge). An architectural dependency of a typed FPF object that is itself untyped is an incompleteness. Severity: soft-fail, not blocking promotion if out-of-scope declaration is added.

**Disposition:** FAIL-3 (soft) above.

---

### Anticipated dissent 3 (from §8 of reviewed doc): §3.6 mutual instrumentation — use vs mention

**Claim in reviewed doc:** «Phil-critic may flag whether §3.6 is use or mention of mutual instrumentation.»

**Eng-critic verdict: NOT THIS CRITIC'S SCOPE.** Use/mention distinction is EP-2 (epistemological) territory — this is a philosophy-expert × critic question. From engineering's view, §3.6 is correctly framed as a cross-link (mention), not a claim about the current operational state of mutual instrumentation in Jetix. The EP-2 qualifier is absent from §3.6 but that is an editorial gap, not an FPF primitive error.

**Disposition:** Route to philosophy-expert × critic. Not FAIL in this review.

---

### New dissent D-DOC02-ENG-1: §6 O-03 Vision mistyped as U.WorkPlan

**Location:** §6 connections table, row «O-03 Vision | FUNDAMENTAL | is-WorkPlan-of»

**Evidence:** The §6 table states «O-03 Vision = U.WorkPlan (A.15.2) describing future MethodDescription applications». This is the same mistyping corrected in Doc 01 for P-1..P-10. A vision document (O-03) is more naturally U.Episteme (A.16) or U.MethodDescription (A.3.2) — it describes intent and principles, not a schedule of planned occurrences with windows/dependencies/budgets/acceptance-targets.

```
F: F4
ClaimScope: applies to §6 cross-ref table row O-03 only; not valid if O-03 Vision has explicit temporal windows + performers declared in its own document
R:
  refuted_if: O-03 FUNDAMENTAL document contains explicit planned occurrence windows + named performers + resource budgets (then U.WorkPlan would apply)
  accepted_if: O-03 Vision is a forward-looking description without temporal windows (standard for vision documents)
```

**Recommended resolution:** Retype O-03 as `is-MethodDescription-of` or `is-Episteme-of`; Vision documents describe the recipe for future states (U.MethodDescription candidate) or are knowledge artefacts (U.Episteme) — they are not schedules.

---

### New dissent D-DOC02-ENG-2: U.Episteme §2.4 conflates two distinct A.16 concepts

**Location:** §2.4 (lines 145–151)

**Evidence:** §2.4 states «Методология Jetix = U.Episteme: систематизированное знание о том, как работать с информацией. В FPF A.16 language-state — LOCKED как arteff.»

This conflates two distinct things:

1. **The methodology document** (this doc, the FPF formal block, the pattern library) = U.Episteme (A.16) artefact. Correct.
2. **The methodology itself** (the abstract way of working) = U.MethodDescription (A.3.2), which is ALSO a U.Episteme (A.3.2 is defined as «a U.Episteme describing a U.Method»).

Both are U.Episteme at different levels. The §2.4 claim conflates the two and applies the «language-state LOCKED» attribute to the methodology as a whole rather than specifically to the artefact layer (the docs). This is the same EP-5 confusion the disclosure warns against — but the confusion is occurring in the body of §2.4, not just in the external reader's mind.

The §4 formal block correctly distinguishes these (U.MethodDescription [A.3.2] as the recipe-level object + U.Episteme [A.16] as the artefact-level object with language-state). §2.4 blurs the distinction that §4 maintains.

```
F: F4
ClaimScope: applies to §2.4 paragraph; §4 formal block correctly separates the layers
R:
  refuted_if: FPF A.3.2 definition does not describe U.MethodDescription as a U.Episteme (contradicts spec: «U.MethodDescription: A U.Episteme describing a U.Method» per FPF Spec A.15.1 section)
  accepted_if: §2.4 is revised to explicitly say «U.Episteme here = the artefact carrying the MethodDescription; the LOCK applies to this artefact, not to the methodology as an abstract object»
```

**Recommended resolution:** Add one clarifying sentence to §2.4: «Важно: U.Episteme здесь = носитель (этот документ + pattern library); именно он получает language-state LOCK. Сама методология как абстрактный объект = U.MethodDescription (A.3.2), который тоже является U.Episteme, но с другой функцией (рецепт vs. носитель рецепта).»

---

### New dissent D-DOC02-ENG-3: E.17 MVPK applied as narrative metaphor, not formal typed publication

**Location:** §2.5 (lines 153–163), §4 formal block E.17 MVPK section (lines 329–332)

**Evidence:** FPF E.17 «Multi-View Publication Kit» is described in the spec as: «Publication discipline for generic publication faces and governed MVPK faces; U.View, publication form, carrier and front-end, source pins, admissible publication use, and no face becoming evidence, gate, decision, or work by presentation.»

The doc's §2.5 treatment is: «Three views (§3 narrative, §4 formal, §5 mermaid) = one source of truth → different views.» This is structurally correct as a high-level description. The dissent is:

**E.17 requires «source pins»** — each view must be explicitly pinned to the source episteme it renders. The doc has inline `[src:...]` citations at the claim level in §3, but §4 and §5 do not have explicit «this view renders claims C-X..C-Y from the source episteme» source-pin declarations. The FPF spec explicitly requires «no face becoming evidence, gate, decision, or work by presentation» — which means readers must be able to trace each view's claims back to the source.

**Severity assessment: low.** The doc achieves the functional intent of MVPK (multiple views, one source). The source-pin discipline gap is a formalism deficit, not a conceptual error. For an F4 grade this is acceptable. If promoted to F5 or beyond, source-pin declarations would be required.

```
F: F3 (low confidence — assessing MVPK conformance requires deeper E.17 body read)
ClaimScope: applies to §2.5 E.17 MVPK claim; not a blocking failure at F4 grade
R:
  refuted_if: E.17 formal body does not require source pins at view level
  accepted_if: adding explicit per-view source-pin declarations satisfies the requirement
```

**Disposition:** Non-blocking dissent. Surface to phil-critic for E.17 formal body check. Grade the MVPK claim F3, not F4, until source-pin discipline is verified.

---

## §8 Structural and template check

| Check | Status | Note |
|---|---|---|
| YAML frontmatter present | PASS | All required fields present; `prose_authored_by` correctly set |
| EP-5 disclosure | PASS | Present in frontmatter, §0 callout, §3.7 — triple-presence is correct |
| EP-2 disclosure | PASS | Present in frontmatter, §0 callout, §3.7 |
| LIVE-FLAG declared | PASS | B2 (Aisystant) LIVE-FLAG in frontmatter and §0 callout |
| §0 TL;DR ≤200 words | PASS | Counted: ~140 words |
| §1 verbatim anchors (≥5 citations) | PASS | 5 anchors present with path + paragraph references |
| §2 F-G-R triples on each claim | PASS | All §2 subsections have F/G/R |
| §3 narrative 800-1200 words | PASS | Estimated ~1050 words across §3.1–§3.7 |
| §4 FPF formal block | PARTIAL FAIL | Missing A.1.1 BoundedContext (FAIL-2) |
| §5 Mermaid diagram | PASS (with note — see mermaid section §9) | Cool blues + #1a202c colors present |
| §6 cross-refs table | PASS (with D-DOC02-ENG-1 on O-03 row) | Table present and substantially correct |
| §7 Open questions (R1-only) | PASS | 6 OQs; all correctly framed as surfaces not decisions |
| §8 R1 reaffirmation + AP-6 | PASS | R1 correctly maintained; anticipated dissents declared |
| §9 proposed_writes + provenance | PASS | provenance block has 6 sources with range + quote |

---

## §9 Mermaid validity check

Colors and style are compliant with the cool-blues + #1a202c brief:
- `primaryColor: #e3f2fd` — light blue, correct
- `primaryTextColor: #1a202c` — dark charcoal, correct
- `primaryBorderColor: #1565c0` — deep blue, correct
- `lineColor: #2196f3` — medium blue, correct

One structural note: the DISTRIBUTION subgraph has nodes FORKER1 and FORKER2 connected to R12 with `---` (undirected) rather than `-->` (directed). This is semantically odd — the relationship is directional (forkers are constrained-by R12, or R12 guarantees forkers). Not a validity failure but a precision deficit.

The EPISTEME → WORKPLAN, EPISTEME → DISTRIBUTION, EPISTEME → EXPLORATION, EPISTEME → MVPK edges (using `==>` heavy arrows) are correct directionally. The FPFLANG → EPISTEME heavy arrow is correct.

The `wpaspirate` classDef (stroke-dasharray:5 5) for the forker occurrence node is a good visual distinction for aspirational items — consistent with the honest-status theme.

**Mermaid verdict: VALID.** No syntax errors detectable from inspection; colors compliant; structure coherent.

---

## §10 Net recommendation

**Verdict: REVISION REQUIRED before canonical promotion.**

**Blocking failures (must fix):**
1. FAIL-1: Relabel U.WorkPlan §2.3 as proto-WorkPlan candidate, downgrade F4→F2, cite 3 missing A.15.2:4.1 fields, add OQ-D02-1 as blocking
2. FAIL-2: Add U.BoundedContext (A.1.1) block to §4 formal section for Doc 02 (Glossary + Invariants + Roles minimum; Bridges optional)
3. FAIL-3: Add explicit out-of-scope declaration for ШСМ/МИМ typing OR add F2 stub typing

**Non-blocking dissents (surface, not blocking):**
- D-DOC02-ENG-1: Retype O-03 Vision row in §6 from `is-WorkPlan-of` to `is-MethodDescription-of` or `is-Episteme-of`
- D-DOC02-ENG-2: Add EP-5 clarifying sentence to §2.4 distinguishing artefact U.Episteme from recipe U.MethodDescription
- D-DOC02-ENG-3: Downgrade MVPK claim from F4 to F3 pending phil-critic E.17 body check on source-pin requirement

**What holds and should not change:**
- U.MethodDescription (A.3.2) assignment = correct, grade F5 warranted
- U.Method (A.3.1) assignment = correct
- B.5.1 Exploration state = honest and correct
- E.17 MVPK architecture (three views, one source) = functionally correct
- F floor F2 document-level = correct given O-05 aspirational status
- §3 narrative quality for L1 audience = strong
- EP-5 / EP-2 / R1 / R12 handling = exemplary
- §1 verbatim anchors = strong provenance

**Estimated revision effort:** small (≤2 hours; adds ~300 words across 3 locations; no structural rewrite needed).

---

## Output packet

```yaml
mode: critic
context:
  task_id: task-fpf-describe-jetix-2026-05-17
  artefact_path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-methodology-eng-integrator.md
  cycle_id: task-fpf-describe-jetix-2026-05-17

critique:
  conformance_checklist:
    - {check_id: "1-deep-module", result: "N/A", evidence: "non-code artefact"}
    - {check_id: "2-function-purpose", result: "N/A", evidence: "non-code artefact"}
    - {check_id: "3-test-integrity", result: "N/A", evidence: "no tests in scope"}
    - {check_id: "4-premature-abstraction", result: "pass", evidence: "all primitives have ≥3 concrete uses cited; B.5.1 candidate correctly tagged"}
    - {check_id: "5-external-dependency", result: "N/A", evidence: "no external call sites"}
    - {check_id: "6-dry", result: "pass", evidence: "no logic duplicated across sections; §2.3/§4 are complementary grain"}
    - {check_id: "7-tool-eval", result: "N/A", evidence: "not a tool-eval artefact"}
    - {check_id: "8-architecture-pattern", result: "N/A", evidence: "not an architecture-proposal artefact"}
    - {check_id: "FPF-1-a3.2-assignment", result: "pass", evidence: "U.MethodDescription correctly assigned with steps/performers/I-O format"}
    - {check_id: "FPF-2-a15.2-workplan", result: "fail", evidence: "§2.3 claims correct application; audit shows 2/5 A.15.2:4.1 fields satisfied; dependencies/budgets/acceptance-targets absent"}
    - {check_id: "FPF-3-a1.1-boundedcontext", result: "fail", evidence: "no BoundedContext block in Doc 02; Doc 01 has full §4.1 declaration"}
    - {check_id: "FPF-4-shsm-mim-typing", result: "fail-soft", evidence: "ШСМ/МИМ in mermaid ONTOSUBSTRATE node untyped; OQ-D02-2 raised but no out-of-scope declaration"}
    - {check_id: "FPF-5-e17-mvpk", result: "pass-with-dissent", evidence: "3 views present; single source-of-truth architecture correct; source-pin discipline gap (D-DOC02-ENG-3)"}
    - {check_id: "FPF-6-role-declaration", result: "partial-fail", evidence: "R1 reaffirmed in §8 but no U.RoleAssignment scoped to Doc-02 BoundedContext"}
    - {check_id: "FPF-7-fgr-completeness", result: "pass", evidence: "F/G/R triples on all §2 claims; F floor F2 correct"}
    - {check_id: "FPF-8-ep5-ep2", result: "pass", evidence: "both disclosures present in frontmatter + §0 + §3.7"}

  acceptance_predicate: "passes if and only if: (a) U.WorkPlan §2.3 relabeled proto-WorkPlan candidate with F2 and 3 missing fields cited; AND (b) A.1.1 BoundedContext block added to §4; AND (c) ШСМ/МИМ out-of-scope declared or stub-typed; remaining §2 claims unchanged"

  alternatives:
    - {label: A, description: "revision pass fixing 3 failures per §3 recommendations", kill_condition: "fails if Doc-02 BoundedContext block contradicts Doc-01 BoundedContext on role scope"}
    - {label: B, description: "drop U.WorkPlan §2.3 entirely; move to OQ-D02-1", kill_condition: "fails if planned-occurrence framing is needed for L1 audience"}
    - {label: status-quo, description: "promote as-is", kill_condition: "fails immediately: L1 audience (Anatoly = FPF spec author) will detect A.15.2:4.1 non-compliance"}

  anti_scope:
    - "not evaluating strategic value of FPF adoption (HITL)"
    - "not evaluating R12 principle content (Ruslan-authored)"
    - "not comparing ШСМ/МИМ vs alternative ontologies"
    - "not evaluating §3 narrative persuasiveness for L1 audience"
    - "not optimizing (critic-only mode)"
    - "not evaluating Doc 01 ↔ Doc 02 strategic sequencing (mgmt territory)"

specific_failures_found:
  - {ap_code: "FAIL-1", location: "§2.3 + §4 U.WorkPlan formal block", evidence: "A.15.2:4.1 requires 5 fields; Fork guide v0 satisfies 2; dependencies/budgets/acceptance-targets absent"}
  - {ap_code: "FAIL-2", location: "§4 FPF formal block (no BoundedContext section)", evidence: "Doc 01 §4.1 has Glossary/Invariants/Roles/Bridges; Doc 02 §4 has none; CC-A1.1.2 requires explicit BoundedContext"}
  - {ap_code: "FAIL-3-soft", location: "§3.3 narrative + §5 mermaid ONTOSUBSTRATE node + OQ-D02-2", evidence: "ШСМ/МИМ referenced as architectural dependency; untyped without out-of-scope declaration"}
  - {ap_code: "D-DOC02-ENG-1", location: "§6 connections table row O-03 Vision", evidence: "O-03 typed as U.WorkPlan; vision documents lack A.15.2:4.1 required fields; should be U.MethodDescription or U.Episteme"}
  - {ap_code: "D-DOC02-ENG-2", location: "§2.4 U.Episteme paragraph", evidence: "conflates artefact U.Episteme with recipe U.MethodDescription; LOCK applies to artefact not to methodology as abstract object"}
  - {ap_code: "D-DOC02-ENG-3", location: "§2.5 E.17 MVPK claim grade F4", evidence: "E.17 requires source-pin declarations per view; §4 and §5 lack per-view source pins; recommend F3 pending phil-critic E.17 check"}

recommended_changes:
  - {change: "Relabel §2.3 U.WorkPlan as proto-WorkPlan candidate; downgrade F4→F2; cite 3 missing fields; add OQ-D02-1 reference as blocking for v1.0", ap_code_addressed: "FAIL-1", estimated_effort: small}
  - {change: "Add §4.0 U.BoundedContext (A.1.1) block to §4 formal section with minimum Glossary/Invariants/Roles and Bridge to Doc 01", ap_code_addressed: "FAIL-2", estimated_effort: small}
  - {change: "Add anti-scope bullet or F2 stub typing for ШСМ/МИМ; reference OQ-D02-2 as pending", ap_code_addressed: "FAIL-3-soft", estimated_effort: small}
  - {change: "Retype §6 O-03 Vision row from is-WorkPlan-of to is-MethodDescription-of or is-Episteme-of", ap_code_addressed: "D-DOC02-ENG-1", estimated_effort: small}
  - {change: "Add clarifying sentence to §2.4 distinguishing artefact U.Episteme (LOCK) from recipe U.MethodDescription (abstract object)", ap_code_addressed: "D-DOC02-ENG-2", estimated_effort: small}
  - {change: "Downgrade §2.5 E.17 MVPK grade from F4 to F3; add note pending phil-critic E.17 source-pin check", ap_code_addressed: "D-DOC02-ENG-3", estimated_effort: small}

proposed_writes:
  - path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-methodology-eng-critic.md
    status: written (this file)
    frontmatter_valid: true
    body_length: ">3000 words"

provenance:
  - path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-methodology-eng-integrator.md
    range: "§2.3 lines 130-143; §4 U.WorkPlan block lines 306-315; §2.4 lines 145-151; §2.5 lines 153-163; §6 table O-03 row line 419"
    quote: "Fork guide v0 = proto-WorkPlan с шагами для forker (временные окна + исполнитель = forker-instance)"
  - path: raw/external/ailev-FPF/FPF-Spec.md
    range: "A.15.2:4.1 definition (line ~20141)"
    quote: "U.WorkPlan is a U.Episteme that declares intended U.Work occurrences over a horizon, with planned windows, dependencies, intended performers (as role kinds or proposed RoleAssignings), resource budgets/reservations, and acceptance targets — within a U.BoundedContext"
  - path: raw/external/ailev-FPF/FPF-Spec.md
    range: "A.1.1 table + CC-A1.1.2 (line ~1342, ~1419)"
    quote: "One context carries one perspective with explicit Glossary, Invariants, Roles, and optional Bridges"
  - path: raw/external/ailev-FPF/FPF-Spec.md
    range: "E.17 table entry (line ~263)"
    quote: "Multi-View Publication Kit — Publication discipline for generic publication faces and governed MVPK faces; source pins, admissible publication use"
  - path: vision/jetix-fpf-describe/01-jetix-as-self-os-substrate.md
    range: "§4.1 BoundedContext declarations (lines 249-271)"
    quote: "Glossary / Invariants (I-1..I-5) / Roles (Ruslan#OwnerRole, ROY-swarm#AIScribeRole) / Bridges (3 declared)"

confidence: high
confidence_method: rubric-pass-rate
escalations:
  - trigger: peer-input-needed
    target: philosophy-expert × critic
    reason: "D-DOC02-ENG-3 E.17 source-pin formal requirement; §3.6 use-vs-mention EP-2 check; ШСМ/МИМ epistemic classification if Option A chosen for FAIL-3"
dissents:
  - source_cell: "engineering-expert × critic (this cell, self-dissent on D-DOC02-ENG-3)"
    claim: "E.17 MVPK source-pin requirement may not apply at F4 grade for an exploratory doc"
    F: F3
    ClaimScope: "applies to §2.5 E.17 claim grade only; not blocking"
    R: {refuted_if: "E.17 formal body shows source-pin is required at all MVPK grades", accepted_if: "source-pin only required at F6+ publication grade"}
```

---

*Critic pass complete. 3 blocking failures identified. 3 non-blocking dissents registered. Primary value of draft confirmed as sound (U.MethodDescription A.3.2 assignment, B.5.1 honest state, E.17 MVPK structure, R12 constitutional framing). Estimated revision effort: small. Pending: phil-critic × critic pass + brigadier integration.*
