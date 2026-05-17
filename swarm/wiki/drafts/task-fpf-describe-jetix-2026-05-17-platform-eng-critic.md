---
title: "Jetix as Platform — Engineering Critic Pass (Doc 05)"
date: 2026-05-17
type: jetix-fpf-describe-critic
status: draft (eng × critic)
artefact_under_review: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-platform-eng-integrator.md
mode: critic
cell: engineering-expert × critic
task_id: task-fpf-describe-jetix-2026-05-17-platform-eng-critic
cycle_id: task-fpf-describe-jetix-2026-05-17
parent_draft: task-fpf-describe-jetix-2026-05-17-platform-eng-integrator
doc_series_position: "05 of 07 — Platform critic pass"
F: F4
G: jetix-fpf-describe-platform-critic
R: refuted_if_all_corrections_applied_and_no_new_violations_found_on_re-review
write_scope: swarm/wiki/drafts/
provenance:
  - path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-platform-eng-integrator.md
    range: "1-502"
  - path: raw/external/ailev-FPF/FPF-Spec.md
    range: "A.1.1:4.1-4.7, A.1.1:4.2, A.3.1:4.1-4.7, A.3.1:4.7, E.17 index row"
  - path: vision/jetix-fpf-describe/04-jetix-as-corporation.md
    range: "frontmatter, §0"
  - path: vision/jetix-fpf-describe/03-jetix-as-virtual-tribe-substrate.md
    range: "frontmatter"
---

# Engineering Critic Pass — Jetix as Platform (Doc 05)

> Critic mode: adversarial review. Every `FAIL` is a blocking correction unless explicitly tagged `NON-BLOCKING`. The artefact under review is the integrator draft at the path above.

---

## §C1 Conformance Checklist (8 binary checks)

| Check ID | Check | Result | Evidence |
|---|---|---|---|
| 1-deep-module | N/A — this is an FPF-describe markdown doc, not a code module. Check vacuously passes. | N/A-PASS | Doc is not a code artefact; deep-module metric does not apply. |
| 2-function-purpose | N/A — no public functions. | N/A-PASS | Markdown artefact. |
| 3-test-integrity | N/A — no tests in artefact. | N/A-PASS | Markdown artefact. |
| 4-premature-abstraction | **FAIL** | Platform BoundedContext is modeled as a *containing* context for workshop BoundedContexts — violating FPF BC-2 (Flat Context Map). The containment is asserted without abstraction-earns-its-weight via 3 concrete multi-party use cases (0 partner workshops exist today). |
| 5-external-dependency | PASS | External dep = FPF-Spec.md (A.1.1, A.3.1, E.17). Failure modes acknowledged (EP-2: no platform code; B.5.1 Exploration). Adequate. |
| 6-dry | PASS | EP-3 disclaimer is repeated in §0, §3.4, §4, §7 intentionally (mandatory per brief); not a DRY violation — repetition is constitutionally required. |
| 7-tool-eval-acceptance | N/A — not a tool-eval.md. | N/A-PASS | |
| 8-architecture-pattern | **FAIL** | §2.1 A.3.1 Method hosting row assigns a "hosting" semantics to the platform-as-U.System that has no FPF-grounded basis. FPF A.3.1:4.7 states U.Method is local to a U.BoundedContext; it is *enacted* by a U.System bearing a TransformerRole, not *hosted* by a supersystem. The word "hosting" imports an infrastructure metaphor that does not map to any FPF A.3.1 primitive. |

**Conformance result:** 2 FAIL on checks 4 and 8. Artefact does NOT satisfy the Acceptance Predicate in its current form.

---

## §C2 Acceptance Predicate (Hamel-binary)

`swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-platform-eng-integrator.md` passes Conformance checks 1-3 (N/A), 5, 6, 7 (N/A) AND fails Conformance checks 4 (BC-2 Flat Context Map violation) and 8 (A.3.1 Method hosting semantics undefined/incorrect) AND therefore does NOT satisfy the acceptance predicate in current form. Predicate flips to PASS when corrections R-1 and R-2 below are applied.

---

## §C3 Alternatives + status-quo + kill-conditions

| # | Alternative | Kill condition |
|---|---|---|
| A | Apply R-1 fix: replace platform-as-container-of-workshop-BoundedContexts with platform-as-U.System-with-Bridges-to-workshop-BoundedContexts (per BC-2 + BC-5). Platform coordination layer modeled as a separate U.BoundedContext `JetixPlatform:CoordinationLayer` with explicit Bridges to each `WorkshopOwner:BoundedContext`. | Fails if explicit Bridge records are missing (each cross-BoundedContext relation MUST have a Bridge per BC-5). |
| B | Apply R-2 fix: replace "Method hosting" framing with "Method enactment infrastructure" — platform provides the TransformerRole-bearing U.System substrate that allows workshop owners to enact their U.Methods; ownership stays with workshop (consistent with existing §2.1 C-3 per-claim). No new FPF primitive required. | Fails if the revised §2.1 A.3.1 row still uses "hosting" without referencing the enactment chain (TransformerRole → U.Method → U.Work per A.3.1:4.1). |
| C | Status-quo (leave BC-2 violation and A.3.1 hosting undefined). | Fails if phil-critic review or systems-integrator pass surfaces the same issues independently — triggering a quality-regression escalation (3 consecutive rejections on the same draft). |

---

## §C4 Anti-scope

- **Not evaluating L1 prototype priority.** Component sequencing (C1 first vs all 5 simultaneously) is mgmt territory per §1b. Engineering surfaces the spec correctness issue only.
- **Not evaluating capital impact.** «2 days CC» estimate is explicitly EP-3 / investor territory. Engineering accepts the EP-3 disclosure as adequate.
- **Not arbitrating Workshop = BoundedContext vs brand-layer (OQ-4).** That is an open question for Ruslan's ack (D-PLAT-1 anticipated dissent). Engineering only validates FPF correctness of the chosen modeling path IF Workshop is accepted as U.BoundedContext.
- **Not authoring the systems-expert cybernetic supplement.** D-PLAT-3 (Cluster 5 / feedback loops) is correctly routed to systems × integrator. Engineering does not resolve it.
- **Not optimizing.** This is a critic pass. Fixes are proposals; optimizer mode required for before/after LoC metrics.
- **Not strategizing.** Platform Phase 3 activation trigger (OQ-4 in §7) is Ruslan's decision.

---

## §C5 Specific Failures

### FAIL-1 (BLOCKING) — BC-2 Flat Context Map violation in §2.2 and §4

**AP code:** AP-ENG-9 (premature abstraction) + FPF CC-A1.1.2 violation

**Location:** §2.2 A.1.1 BoundedContext — Invariants item 3 ("Workshop isolation"), §4 FPF formal version `BoundedContext: WorkshopBoundedContext`, §3.2 Mermaid diagram (subgraph nesting)

**Evidence (verbatim from draft §4):**
```
Object: Jetix_Platform
  type: U.System (A.1 supersystem)
  composition: set_of(WorkshopBoundedContext_N)
```

```
BoundedContext: WorkshopBoundedContext
  defined_by: A.1.1
  elements: [Foundation_fork, ...]
```

**Defect:** FPF A.1.1 BC-2 (Flat Context Map) states: "No `U.BoundedContext` is modeled as inheriting from, containing, or being contained by another `U.BoundedContext`; cross-context relations MUST be expressed only via explicit `Bridges`." [src: raw/external/ailev-FPF/FPF-Spec.md line 1385]

The draft models `Jetix_Platform` as a `U.System (A.1 supersystem)` that has `composition: set_of(WorkshopBoundedContext_N)`. This means the platform U.System contains workshop U.BoundedContexts as composition members. This is NOT the same as a U.System containing other U.Systems (which would be valid holarchic composition under A.1). The problem is that `WorkshopBoundedContext` is typed as `U.BoundedContext` (A.1.1) — and a U.System cannot hold U.BoundedContexts as compositional parts under FPF, because BoundedContexts exist on a flat map and relate only via Bridges.

Additionally, the Mermaid diagram in §3.2 nests `subgraph WS1["Мастерская A (U.BoundedContext)"]` inside `subgraph Platform[...]` — visually encoding the containment that BC-2 forbids.

**Severity:** BLOCKING. The entire §2.2 BoundedContext structure is built on a containment assumption that violates FPF kernel constraints.

**Note on whether Workshop = U.System or U.BoundedContext matters here:** If Workshop is modeled as a U.System (not U.BoundedContext), then the platform-as-supersystem holarchic composition is valid. But the draft explicitly assigns `U.BoundedContext` as the type (§2.1, §4), which is what triggers BC-2. The fix (Alternative A) resolves this by either (a) treating each Workshop as a U.System sub-holon inside Platform (valid A.1 composition) with an associated U.BoundedContext per workshop that is bridged to the Platform context, or (b) modeling Platform and each Workshop as peer U.BoundedContexts connected by explicit Bridges.

---

### FAIL-2 (BLOCKING) — A.3.1 "Method hosting" has no FPF grounding

**AP code:** AP-ENG-12 (architecture pattern not declared / incorrectly declared)

**Location:** §2.1 table row "U.Method (A.3.1) — Method hosting", §4 FPF formal version `Method_hosting (A.3.1)`

**Evidence (verbatim from draft §2.1):**
> "Платформа хостит method occurrences: каждый мастер приносит свою methodology (свой способ работы с информацией). Платформа обеспечивает infrastructure for hosting + coordination между methods."

**Evidence (verbatim from draft §4):**
```
Method_hosting (A.3.1):
  platform_role: infrastructure_for_method_occurrence
  workshop_role: method_author + occurrence_owner
  not: platform_does_NOT_impose_single_method
```

**Defect:** FPF A.3.1:4.1 defines `U.Method` as "a context-defined abstract transformation type — the semantic 'way of doing' a kind of work." It is **described** by U.MethodDescriptions and **enacted** by a U.System bearing a TransformerRole to produce U.Work. [src: raw/external/ailev-FPF/FPF-Spec.md lines 5833-5837]

FPF A.3.1:4.7 states: "U.Method is local to a U.BoundedContext: terminology, admissible pre/postconditions, and non-functional constraints are interpreted inside that context." [src: raw/external/ailev-FPF/FPF-Spec.md line 5900]

"Hosting" is not an FPF primitive relationship. A U.System does not "host" U.Methods; it **enacts** them (produces U.Work). The platform can provide the U.System substrate in which workshop owners bear TransformerRoles to enact their U.Methods — but that is an enactment infrastructure, not a hosting relationship. The term "method occurrence" conflates U.Method (design-time abstract type) with U.Work (run-time enactment instance). Method occurrences in FPF are U.Work instances, not U.Method instances.

**Additional sub-defect:** The phrase "method occurrences" is FPF-incorrect. FPF has "method instances" only in the sense of MethodDescription versions; the run-time occurrence is U.Work. The draft introduces "method occurrence" as a new term without definition.

**Severity:** BLOCKING. The A.3.1 formal section misrepresents the FPF primitive.

---

### FAIL-3 (NON-BLOCKING — Recommended) — E.17 MVPK views lack source pins

**AP code:** AP-ENG-5 adapted (tool-eval acceptance check) — applied here as "E.17 source pin completeness"

**Location:** §2.1 E.17 MVPK row, §4 MVPK section

**Evidence (verbatim from draft §2.1):**
> "Multi-view publication platform: developer view (filesystem-as-SoT + CLI tools), partner view (Workshop interface + FPF CRUD), client view (deliverables + workflow results)."

**Evidence (verbatim from draft §4):**
```
MVPK (E.17):
  developer_view: filesystem-as-SoT + CLI tools + /ingest /search-kb /lint
  partner_view: FPF CRUD + cooperation_event_log + role_declaration_surface
  client_view: deliverable_output + workflow_results + tools_capabilities_of_workshop
```

**Defect:** Per FPF E.17 (index row): MVPK requires "source pins, admissible publication use, and no face becoming evidence, gate, decision, or work by presentation." [src: raw/external/ailev-FPF/FPF-Spec.md line 263]

The three views lack source-pin anchors. Each view should state: (a) what source artefact it is a projection of (the underlying episteme/U.System being described), and (b) the admissible use boundary (what the view cannot be treated as — evidence, gate, work). The doc's views are prose descriptions of what the platform *looks like* from each audience, not governed MVPK faces with source pins.

This is non-blocking because the doc is at F2 (O-14 vapor) and B.5.1 Exploration — a full MVPK face governance is premature. However, the claim in §2.1 that E.17 MVPK is applied should be qualified as "E.17-inspired / partial MVPK" to avoid a false governance claim.

**Recommended change:** Add to the E.17 MVPK row in §2.1: "Source: underlying described entity = Jetix_Platform U.System (O-14). Admissible use: didactic retelling (E.17.EFP class); NOT evidence, NOT gate, NOT work." — or soften the framing to "E.17-inspired multi-audience narrative, not a governed MVPK face (B.5.1 Exploration — no platform code)."

---

### FAIL-4 (NON-BLOCKING — Informational) — §2.2 BoundedContext: missing U.Boundary declaration

**AP code:** AP-ENG-10 (external-dep-without-failure-mode adapted) — here: FPF CC-A1.1.1 compliance gap

**Location:** §2.2 A.1.1 BoundedContext treatment

**Evidence:** FPF A.1.1 CC-A1.1.1 requires: "A `U.BoundedContext` MUST be modeled as a `U.Holon` with a defined `U.Boundary`." [src: raw/external/ailev-FPF/FPF-Spec.md line 1418]

The §2.2 treatment has Glossary + Invariants + Roles + Bridges — which is good and covers A.1.1:4.2 core components. However, there is no explicit `U.Boundary` declaration (what is inside vs outside the Platform BoundedContext's boundary as a holon). The Invariant #3 "Workshop isolation" gestures at a boundary but does not state it as a U.Boundary predicate.

**Non-blocking because:** The Glossary section implicitly demarcates boundary via Platform-scope vs Workshop-scope terminology. Adding a one-line `U.Boundary: "all artefacts, roles, and events whose lifecycle is governed by the platform coordination protocol"` in §2.2 or §4 would satisfy CC-A1.1.1 cleanly.

---

### PASS observations (with notes)

**Cross-doc consistency (focus area 5):** The bridges in §2.2 and §6.4 correctly reference Doc 01-04. Platform ↔ Corp bridge (both vapor) is accurate. Platform ↔ Tribe bridge is accurate (social vs technical layer). Platform-as-composition-of-Self-OS instances (Doc 01) is correctly flagged as "Partial (Ruslan's instance operational)". No cross-doc role conflicts detected relative to doc 03 (Virtual Tribe) and doc 04 (Corporation) pattern.

**EP-3 disclosure compliance:** Mandatory EP-3 disclosure is present in §0, §3.4, §4 (pre_conditions), and §7 (OQ-7). Passes the constitutional check.

**AP-6 dissent preservation:** Three anticipated dissents (D-PLAT-1, D-PLAT-2, D-PLAT-3) are preserved with (F, ClaimScope, R) triples. D-PLAT-2 is noted as partially integrated (EP-2 disclosure addresses it). No averaging detected. Passes.

**Mermaid palette compliance (focus area 6):** Color scheme uses `fill:#1e3a5f`, `fill:#1a3a2e`, `fill:#2d2d1e`, `fill:#2d1e3a`, `fill:#3a1e1e` — cool blues plus complementary darks. Text colors `color:#e8f4fd`, `color:#e8f5ef`, etc. provide high contrast. Variant A convention is satisfied. Passes. Structural validity of Mermaid syntax: `graph TB` with `subgraph` nesting and `classDef/class` directives is syntactically valid Mermaid. Sequence diagram uses valid participant/note/arrow syntax. No syntax failures detected.

**F-G-R per-claim table (§2.3):** 8 claims with F/G/R triples. All R predicates are falsifiable one-liners. F levels are appropriately conservative (F2 for EP-3 voiced intent, F4-F5 for LOCKED sources). Passes.

**Provenance density (§9):** 6 source entries cover all major sections. Verbatim quotes in §1 are source-attributed. Passes.

---

## §C6 Recommended Changes

| # | Change | AP code addressed | Estimated effort |
|---|---|---|---|
| R-1 | Replace `composition: set_of(WorkshopBoundedContext_N)` in §4 with `composition: set_of(WorkshopSubHolon_N)` where each WorkshopSubHolon is a U.System sub-holon (not a U.BoundedContext). Then state separately that each workshop sub-holon operates *within* its own `U.BoundedContext` (`WorkshopBC_N`) that is related to the Platform context via explicit Bridge records. Update §2.2 Bridges table to list these Bridges explicitly. Update the Mermaid diagram to remove subgraph nesting and instead use edge arrows between peer nodes. | AP-ENG-9 + FPF BC-2 | medium |
| R-2 | Replace "Method hosting" label and `infrastructure_for_method_occurrence` in §2.1 and §4 with "Method enactment substrate." Describe the platform as: "Platform provides the U.System substrate (TransformerRole-bearing) that enables workshop owners to enact their U.Methods (A.3.1), producing U.Work within each workshop's BoundedContext. Method ownership (design-time) stays with the workshop; Work ownership (run-time) also stays within the workshop's context." Remove the term "method occurrences" and replace with "U.Work instances" (run-time enactments) wherever the draft means the run-time execution. | AP-ENG-12 + FPF A.3.1:4.1 | small |
| R-3 | In the E.17 MVPK row in §2.1, add: "Source pin: underlying described entity = O-14 `Jetix_Platform` (conceptual). Admissible use: didactic/explanatory retelling (E.17.EFP); NOT evidence, gate, or work. Governed MVPK faces = Phase B design (no platform code today per EP-2)." | AP-ENG-5 adapted | small |
| R-4 | Add a one-line `U.Boundary` declaration in §2.2 or §4: "`U.Boundary: all artefacts, roles, events, and protocols whose lifecycle is governed by the Jetix Platform coordination layer (as opposed to individual workshop internals)."` | FPF CC-A1.1.1 | small |

---

## §C7 Proposed writes

```yaml
proposed_writes:
  - path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-platform-eng-critic.md
    frontmatter:
      title: "Jetix as Platform — Engineering Critic Pass (Doc 05)"
      date: 2026-05-17
      type: jetix-fpf-describe-critic
      status: draft (eng × critic)
      cell: engineering-expert × critic
    body: <this document>
    edges_to_add:
      - {type: critiques, from: this, to: task-fpf-describe-jetix-2026-05-17-platform-eng-integrator}
```

---

## §C8 Provenance

| Source | Range | Usage |
|---|---|---|
| swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-platform-eng-integrator.md | Lines 108-117 (§2.1 primitives table), 290-332 (§4 FPF formal), 340-362 (§5 sequence diagram) | Primary artefact under review |
| raw/external/ailev-FPF/FPF-Spec.md | Lines 1361-1390 (A.1.1:4.2 core components + BC-1..BC-7 admissibility constraints) | BC-2 Flat Context Map constraint verification |
| raw/external/ailev-FPF/FPF-Spec.md | Lines 5793-5903 (A.3.1:4.1-4.7 U.Method definition, enactment chain, context anchoring) | A.3.1 Method hosting semantics verification |
| raw/external/ailev-FPF/FPF-Spec.md | Line 263 (E.17 index row — source pins + admissible use requirement) | E.17 MVPK source-pin check |
| raw/external/ailev-FPF/FPF-Spec.md | Line 1418 (CC-A1.1.1 U.Boundary requirement) | BC-2 boundary declaration check |

---

## §C9 Output schema fields

```yaml
mode: critic
context:
  task_id: task-fpf-describe-jetix-2026-05-17-platform-eng-critic
  artefact_path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-platform-eng-integrator.md
  cycle_id: task-fpf-describe-jetix-2026-05-17
critique:
  conformance_checklist:
    - {check_id: "1-deep-module", result: "N/A", evidence: "Markdown artefact; no code modules"}
    - {check_id: "2-function-purpose", result: "N/A", evidence: "Markdown artefact; no functions"}
    - {check_id: "3-test-integrity", result: "N/A", evidence: "No tests"}
    - {check_id: "4-premature-abstraction", result: "fail", evidence: "Platform-as-container-of-BoundedContexts asserted with 0 real partner workshops; violates BC-2 flat map (FPF A.1.1:4.3)"}
    - {check_id: "5-external-dependency", result: "pass", evidence: "FPF-Spec.md dependency acknowledged with B.5.1 Exploration + EP-2 failure modes"}
    - {check_id: "6-dry", result: "pass", evidence: "EP-3 repetition is constitutional mandate, not DRY violation"}
    - {check_id: "7-tool-eval-acceptance", result: "N/A", evidence: "Not a tool-eval artefact"}
    - {check_id: "8-architecture-pattern", result: "fail", evidence: "A.3.1 'Method hosting' is not an FPF primitive; correct primitive is enactment (TransformerRole → U.Method → U.Work per A.3.1:4.1)"}
  acceptance_predicate: "artefact passes checks 1-3(N/A), 5, 6, 7(N/A) AND fails checks 4 and 8 — does NOT pass in current form; passes after R-1 and R-2 applied"
  alternatives:
    - {label: "A", description: "Fix BC-2: platform = peer U.BoundedContext with Bridges to workshop BoundedContexts (or platform = U.System with U.System sub-holons, each with their own BoundedContext)", kill_condition: "Fails if Bridge records remain implicit"}
    - {label: "B", description: "Fix A.3.1: replace 'hosting' with 'enactment substrate'; replace 'method occurrences' with 'U.Work instances'", kill_condition: "Fails if TransformerRole enactment chain not referenced"}
    - {label: "status-quo", description: "Leave BC-2 violation and A.3.1 hosting undefined", kill_condition: "Fails on phil-critic or sys-integrator independent re-surfacing — quality regression escalation"}
  anti_scope:
    - "Not evaluating L1 prototype component priority (mgmt territory)"
    - "Not arbitrating OQ-4 Workshop = BoundedContext vs brand-layer (Ruslan HITL decision)"
    - "Not authoring systems-expert cybernetic supplement (D-PLAT-3)"
    - "Not optimizing — critic pass only"
    - "Not strategizing on Platform Phase 3 activation trigger"
specific_failures_found:
  - {ap_code: "FPF-BC-2 + AP-ENG-9", location: "§4 FPF formal + §2.2 Invariants + §3.2 Mermaid", evidence: "composition: set_of(WorkshopBoundedContext_N) — BC-2 Flat Context Map violation; workshop BoundedContexts modeled as contained inside platform"}
  - {ap_code: "AP-ENG-12 + FPF A.3.1:4.1", location: "§2.1 A.3.1 row + §4 Method_hosting block", evidence: "platform_role: infrastructure_for_method_occurrence — 'hosting' not an FPF primitive; 'method occurrence' conflates U.Method (design-time) with U.Work (run-time)"}
recommended_changes:
  - {change: "R-1: Replace BoundedContext containment with Bridge-connected peer contexts or A.1 holarchic U.System composition", ap_code_addressed: "FPF-BC-2 + AP-ENG-9", estimated_effort: "medium"}
  - {change: "R-2: Replace 'Method hosting' / 'method occurrences' with enactment substrate + U.Work instances", ap_code_addressed: "AP-ENG-12 + FPF A.3.1:4.1", estimated_effort: "small"}
  - {change: "R-3: Add E.17 source pins + admissible-use boundary to MVPK rows", ap_code_addressed: "AP-ENG-5-adapted + FPF E.17", estimated_effort: "small"}
  - {change: "R-4: Add U.Boundary declaration to §2.2/§4", ap_code_addressed: "FPF CC-A1.1.1", estimated_effort: "small"}
confidence: high
confidence_method: rubric-pass-rate
escalations: []
dissents:
  - source_cell: "engineering × critic (self)"
    claim: "If OQ-4 resolves to Workshop = U.System (not U.BoundedContext), then FAIL-1 BC-2 violation is moot — the containment is valid holarchic U.System composition under A.1. This critic pass assumes Workshop = U.BoundedContext as declared in the draft."
    F: F4
    ClaimScope: "holds only under Workshop = U.BoundedContext assignment; reverts if OQ-4 resolves otherwise"
    R: {refuted_if: "Ruslan acks Workshop = U.System (not U.BoundedContext) in OQ-4 closure", accepted_if: "Ruslan acks Workshop = U.BoundedContext — then BC-2 fix is mandatory"}
```

---

## §C10 Strategies.md compound-step rule

New rule to be appended to `agents/engineering-expert/strategies.md` at Compound step:

**Rule slug:** `fpf-a11-bc2-no-bounded-context-containment`

FPF U.BoundedContext (A.1.1) instances MUST NOT be modeled as contained inside a U.System or another U.BoundedContext. Cross-BoundedContext relations are Bridges only (BC-2). A common error pattern: modeling a "platform supersystem" as compositionally containing workshop BoundedContexts. The correct modeling is: platform = a U.System whose sub-holons are U.System workshop instances, each of which *has an associated* U.BoundedContext that is peer-level to the Platform context via explicit Bridges. [src: FPF-Spec.md A.1.1:4.3 BC-2; detected cycle task-fpf-describe-jetix-2026-05-17]

**Rule slug:** `fpf-a31-method-is-enacted-not-hosted`

FPF U.Method (A.3.1) is enacted by a U.System bearing a TransformerRole to produce U.Work; it is not "hosted" by a platform. The phrase "method hosting" has no FPF grounding. The run-time occurrence is U.Work (not "method occurrence"). When writing architecture-proposal.md or FPF-described docs that reference A.3.1, always use the enactment chain: TransformerRole → enacts → U.Method (via MethodDescription) → produces → U.Work. [src: FPF-Spec.md A.3.1:4.1, A.3.1:4.7; detected cycle task-fpf-describe-jetix-2026-05-17]
