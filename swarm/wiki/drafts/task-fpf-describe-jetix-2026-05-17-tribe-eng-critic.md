---
title: "Doc 03 Eng-Critic — Jetix as Virtual Tribe Substrate (FPF-Described)"
date: 2026-05-17
type: eng-critic-output
status: critic-draft
artefact_reviewed: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-integrator.md
critic_cell: engineering-expert × critic
mode: critic
task_id: task-fpf-describe-jetix-2026-05-17
cycle_id: cyc-fpf-describe-2026-05-17
parent_docs:
  - vision/jetix-fpf-describe/01-jetix-as-self-os-substrate.md
  - vision/jetix-fpf-describe/02-jetix-as-methodology.md
F: F4
G: eng-critic-fpf-primitive-correctness
R: refuted_if_FPF_Spec_B1.6_definition_found_to_encompass_capability_composition
language: russian (narrative) + english (FPF primitives + code)
---

# Doc 03 Eng-Critic — Jetix as Virtual Tribe Substrate

---

## §1 Conformance Checklist (8 binary checks)

| check_id | result | evidence |
|---|---|---|
| 1-deep-module | N/A | Not a code artefact; check applied to FPF-primitive surface area: primitive table is thin and references primitives, not implementations — shallow-module analogue not triggered |
| 2-function-purpose | pass | Every section has a declared purpose; §2 primitive table has per-row role declarations; no ambiguous sections |
| 3-test-integrity | N/A | No test cases; frontmatter has Hamel-binary R-conditions per claim — equivalent obligation met |
| 4-premature-abstraction | fail | «Γ_work = composition of capabilities» used as if this were Γ_work's correct scope — an abstraction-level error. This is a category misapplication of B.1.6 before the correct primitive (Γ_method or Γ_sys) is validated; premature assignment. AP-ENG-9 trigger. |
| 5-external-dependency | pass | All external sources (text_004, H8, Charter, FPF primitives) cited with inline src-tags; failure modes for aspirational claims declared via R-conditions |
| 6-dry | pass | No repeated definitions across sections; §4 formal section and §2 primitive table use distinct registers (formal vs descriptive), no duplicate prose |
| 7-tool-eval-acceptance | N/A | Not a tool-eval draft |
| 8-architecture-pattern | N/A | Not an architecture-proposal draft; however, the Γ_work misapplication is functionally an architecture-pattern error (wrong composition operator declared) — flagged in §6 specific failures |

**Overall: 7 of 8 applicable checks pass. Check 4 fails (critical — wrong FPF primitive selected).**

---

## §2 Acceptance Predicate (Hamel-binary)

`swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-integrator.md` passes Conformance checks 1 (N/A), 2 (pass), 3 (N/A), 5 (pass), 6 (pass), 7 (N/A), 8 (N/A) BUT FAILS check 4 (Γ_work category error — wrong aggregation primitive for capability composition) AND has one A.2.9 conditional clause missing (context-policy dependency for instituting tribal relation) AND has no formal A.1.1 BoundedContext declaration for the Clan context.

**Current predicate result: DOES NOT PASS.** Three corrective actions required before promotion to canonical:

1. Replace Γ_work with the correct FPF aggregation primitive for capability composition (Γ_method B.1.5 or Γ_sys B.1.2 — see §6).
2. Add A.2.9 context-policy dependency clause to U.SpeechAct use (normative caveat from FPF A.2.9:4.1).
3. Add A.1.1 BoundedContext formal section for the Clan/VirtualTribe context (Glossary + Invariants + Roles + Bridges).

---

## §3 Alternatives (≥2 + status-quo + kill-conditions)

| # | Alternative | Kill condition |
|---|---|---|
| A | Replace Γ_work with Γ_sys (B.1.2) for structural capability aggregation: «Virtual tribe = aggregate U.System(A.1) whose capabilities compose via Γ_sys under a Clan boundary» | Fails if Γ_sys's WLNK constraint (weakest-link bound) is too restrictive for capability synergies — Clan member capabilities are not simply bounded by the weakest member; they may be super-additive (which is precisely when B.2 MHT should fire) |
| B | Replace Γ_work with Γ_method (B.1.5) for ordered capability composition: «Mutual instrumentation = Γ_method composition of role-bearers' MethodDescriptions under a shared Quest» | Fails if the composition is not order-sensitive (if any role-bearer's capability can be combined in any order); but for most real Quests, order matters (Hunter prospects before Scholar validates), so Γ_method is likely correct for Quest-scoped cooperation |
| C | Status-quo (retain Γ_work, defend as cost-of-cooperation accounting) | Fails because FPF B.1.6 defines Γ_work strictly as a resource-ledger algebra for spent resources (joules, kg, bits, time-delta). The FPF Spec body explicitly states: «Γ_work neither schedules nor orders steps; it composes resource deltas attached to Work». Capability composition ≠ resource delta accounting. Category error survives under status-quo. |

**Recommendation: Alternative B (Γ_method) is likely most correct for Quest-scoped cooperation; Γ_sys for the aggregate holon structure. Both may be needed simultaneously — Γ_sys for the Clan-as-system, Γ_method for the cooperation protocol within a Quest. Brigadier surfaces to Ruslan; not a decision this critic makes.**

---

## §4 Anti-scope

- Не оцениваю стратегический вопрос о том, является ли mutual instrumentation правильной концепцией для Jetix. Это α-5 Direction, Ruslan decides.
- Не оцениваю культурную и этическую достаточность R12 + E.5 как safeguard механизма — это `philosophy × critic` territory. D-DOC03-ENG-1 dissent preserved; не расширяю его здесь.
- Не оцениваю является ли virtual tribe структурно отличным от DAO — это OQ-D03-4 surface, comparative analysis не моя domain.
- Не оцениваю нарратив §3 (plain language sections) — они intentionally not-formal и правильно атрибутированы к Ruslan voice.
- Не оцениваю roadmap-correctness L0→L6 ladder — это mgmt territory.
- Не оцениваю являются ли 9 L1 candidates правильным выбором — это Ruslan strategic judgment.

---

## §5 Cross-doc consistency check

**Doc 01 § 4.1 declares:**
- `Ruslan#OwnerRole:Self-OS-substrate-BoundedContext`
- `ROY-swarm#AIScribeRole:Self-OS-substrate-BoundedContext`
- Bridge: `Self-OS ↔ Tribe (Doc 03) Bridge — individual substrate = atomic unit People-NS via mutual instrumentation`

**Doc 03 compatibility:**

| Item | Status | Notes |
|---|---|---|
| Ruslan's role in Doc 03 | Consistent | Doc 03 references Ruslan as Architect#системный-дизайн + founder; different bounded context (Clan-context vs Self-OS-BoundedContext) = correct per IP-1 + A.2.1; no conflation of identity across contexts |
| Self-OS as atomic unit | Consistent | Doc 03 §6.3 explicitly declares «individual substrate prerequisite для tribal trust» and «← doc 01» dependency; Bridge declared in both docs |
| F-G-R floor | Consistent | Both docs at F2 document-level floor; per-claim grades compatible |
| R1 attribution | Consistent | Both docs carry `prose_authored_by: ruslan-via-voice-dictation+brigadier-structured` |
| EP-5 disclosure | Consistent | Both carry identical EP-5 disclosure text |
| BoundedContext formal section | **INCONSISTENCY** | Doc 01 has full A.1.1 BoundedContext (Glossary + Invariants + Roles + Bridges in §4.1). Doc 03 has NO formal A.1.1 BoundedContext section for the Clan/VirtualTribe context. Mentioned in §2 primitive table as concept but never formally declared. |
| A.2.1 RoleAssignments | **INCONSISTENCY** | Doc 01 §4.1 declares formal RoleAssignment tokens. Doc 03 mentions role-patterns (Scholar#методология, Hunter#продажи) only in narrative examples, never as formal A.2.1 declarations |

**Cross-doc verdict: Compatible in substance, one structural gap (A.1.1 BoundedContext absent in Doc 03).**

---

## §6 Specific Failures Found

### FAIL-1 (Critical): Γ_work misapplication — wrong aggregation primitive

**AP code:** AP-ENG-4 analogue (category-level error in primitive assignment, not a method-change but a primitive-scope violation)

**Location:** §2.1 Primitive map row Γ_work; §3.5 narrative «Clan = новое качество: коллективная Γ_work (B.1.6)»; §4.1 formal definition `Γ_work := Capability_set_A ∪ Capability_set_B`; §5 mermaid diagram node `GW["Γ_work (B.1.6)"]`

**Evidence (verbatim from FPF Spec B.1.6:5 body):**
> «Γ_work : (S : Set[U.Work], M_spec : U.MethodDescription?) → W_tot : U.Work»
> «Work is the dated run-time occurrence of enacting a MethodDescription by a performer under a U.RoleAssignment. In this pattern we treat Work under its **spent-resource facet**: the typed delta we can account for across a declared boundary and time window.»
> «Γ_work neither schedules nor orders steps; it composes **resource deltas attached to Work**.»
> From B.1.5:11 Rationale: «Γ_method composes behaviour; Γ_work accounts resources; B.3 assesses quality»

**Analysis:** Doc 03 defines `Γ_work := Capability_set_A ∪ Capability_set_B [when compositions active under shared Quest]`. FPF B.1.6 defines Γ_work as a resource-ledger algebra operating on U.Work instances (spent time, energy, money, bits). Capability sets are U.Capability (A.2.2) objects — dispositional properties, not Work records. Union of capability sets is not a resource-delta accounting operation. The category error: Capabilities are design-time dispositional properties; Work is a run-time occurrence record with resource deltas.

**Correct primitive candidates:**
- **Γ_sys (B.1.2)** — for structural capability aggregation: composing the Clan-as-system from individual U.System role-bearing humans with their capabilities as structural properties
- **Γ_method (B.1.5)** — for ordered capability composition inside a Quest: the cooperation protocol is a Method whose steps are role-bearer contributions; Γ_method composes those ordered/concurrent steps

**Impact:** The formal definition in §4.1 inherits the error: `Γ_work := Capability_set_A ∪ Capability_set_B` is not a valid Γ_work expression. The mermaid diagram node label is incorrect. The §2.1 row rationale is incorrect.

**Severity: Critical.** Γ_work is the primary novel FPF primitive in this doc beyond the basic Role/Capability/Commitment cluster. Its misapplication propagates through §2.1, §3.5, §4.1, and §5.

---

### FAIL-2 (Moderate): U.SpeechAct (A.2.9) missing normative context-policy dependency

**AP code:** AP-ENG-10 analogue (external dependency — FPF A.2.9 — without failure-mode declared)

**Location:** §2.1 Primitive map row U.SpeechAct; §3.6 «Активация — это момент, когда U.SpeechAct (A.2.9) "signing" институирует tribal relation»; §4.1 `SpeechAct(A, declare(Role_A, Capability_set_A, Commitment_A))`

**Evidence (verbatim from FPF Spec A.2.9:4.1, normative):**
> «Whether a given actType institutes commitments/permissions/status changes is **entirely context-policy dependent**. Absent an explicit policy, treat a U.SpeechAct as a communicative Work occurrence with observable provenance only; **do not infer deontic bindings from the act by default**.»

**Analysis:** FPF A.2.9 supports the «institutes» claim — the spec includes `institutes: optional<InstitutedEffects>` field with CommitmentIdRef, RoleAssignmentRef, statusClaims. The signing-as-tribal-institution IS possible under A.2.9. However, the normative constraint is that institutional effects are context-policy dependent. Doc 03 does not declare the Clan-context policy that licenses «SpeechAct institutes tribal relation». Without this policy declaration, the institutional claim is not FPF-normative. The spirit of the claim is correct; the structural grounding is missing.

**Required addition:** A context-policy declaration such as «Clan-BoundedContext policy: U.SpeechAct of actType="Charter-signing" institutes: {commitments: R12-Commitment, roleAssignments: Holder#ClanMember:Clan-context, statusClaims: Charter-signatory-status}». This policy belongs in the A.1.1 BoundedContext section (which is also missing — FAIL-3).

**Severity: Moderate.** The claim is directionally correct but FPF-normatively underspecified. Fixable by adding context-policy in the A.1.1 BoundedContext section.

---

### FAIL-3 (Moderate): A.1.1 BoundedContext absent for Clan/VirtualTribe context

**AP code:** AP-ENG-12 analogue (architecture-without-structure declaration)

**Location:** §2 header, §4 formal version — no §4.1 BoundedContext subsection equivalent to Doc 01 §4.1

**Evidence (Doc 01 §4.1 cross-reference):** Doc 01 has formal A.1.1 BoundedContext with: Glossary (deyatel, zapasnichok, logic-loop, loop labels), Invariants (I-1 through I-5), Roles (Ruslan#OwnerRole, ROY-swarm#AIScribeRole, Part6b#ConstitutionalEnforcerRole), Bridges (4 declared bridge types)

**Analysis:** Doc 03 uses bounded-context terminology throughout («Bounded context» column in §2.1 primitive table, «Clan-context» in narrative) but never formally declares the Clan/VirtualTribe BoundedContext with:
- **Glossary:** «mutual instrumentation», «agreed share», «tribal relation», «Quest», «Season», «fork-and-leave» — all used without formal glossary entry
- **Invariants:** R12 constraint is mentioned but not listed as a formal Invariant of the Clan BoundedContext
- **Roles:** Charter signatories described in narrative but no formal A.2.1 RoleAssignment declarations
- **Bridges:** Doc 01 ↔ Doc 03 bridge is declared in Doc 01 but not reciprocally in Doc 03; Doc 03 ↔ Doc 06 (trust mechanism) bridge is named as cross-link but not formally declared as a Bridge

**Severity: Moderate.** Without A.1.1 formal section, A.2.9 context-policy (FAIL-2) cannot be properly grounded, and the «context-bounded» claims in §2.1 are prose rather than FPF-normative declarations.

---

### FAIL-4 (Minor): B.2 trigger predicate underspecified — Clan count threshold not mapped to BOSC-A-T-X

**AP code:** Structural gap (not a code-review AP but a FPF-primitive precision gap)

**Location:** §2.1 row B.2; §3.5 «B.2 Meta-Holon Transition»; §4.1 formal `VirtualTribe(Clan) := B.2_MetaHolon_Transition({...}, trigger = (|signatures| ≥ 5 ∧ Quest_count ≥ 1))`

**Evidence (verbatim from FPF Spec B.2:4.2):**
> «Declare MHT when one or more of the following **observable triggers** occur (measurements are recorded in the promotion record): B — Boundary closure/opening [...] O — Objective emergence [...] S — Structural re-organization for supervision [...] C — Capability super-additivity [...] A — Agency threshold crossing [...] T — Temporal consolidation [...] X — Context rebase [...]»
> «Any **two** of these together almost always warrant MHT.»

**Analysis:** D-DOC03-ENG-3 (eng-integrator self-dissent) correctly anticipates this: «FPF B.2 Meta-Holon Transition не специфицирует численный threshold». The FPF Spec confirms: B.2 trigger requires at least one BOSC-A-T-X observable trigger, not a count. Charter «≥5 signatures + 1 Quest» can be understood as approximating:
- **T (Temporal consolidation):** Phase Promotion event — «commissioning → operational service» (signing → activated Clan)
- **S (Structural re-organization):** New coordination channels emerge (Charter-based role assignments, Quest protocol)

But this mapping is not declared in the doc. The formal expression `trigger = (|signatures| ≥ 5 ∧ Quest_count ≥ 1)` is a Jetix-operational threshold, not a BOSC-A-T-X observable. An FPF-normative B.2 declaration would say: «B.2 MHT fires when: T-trigger (Phase Promotion: pre-Clan → Clan activation) evidenced by {signatures ≥ 5 acting as commission event} AND S-trigger (new coordination channels: Charter-role assignments, shared-Quest protocol active)».

**Severity: Minor.** Eng-integrator self-dissent D-DOC03-ENG-3 already surfaces this; the fix is additive (mapping, not replacement). Does not invalidate the conceptual use of B.2.

---

## §7 Recommended Changes

| # | Change | AP addressed | Estimated effort |
|---|---|---|---|
| RC-1 (Critical) | In §2.1 primitive table: replace Γ_work row with two rows — (a) Γ_sys (B.1.2) for «Clan-as-system structural aggregation of role-bearing humans» + (b) Γ_method (B.1.5) for «ordered capability composition within a Quest». In §3.5 narrative: replace «коллективная Γ_work (B.1.6)» with «Γ_sys структурная агрегация + Γ_method упорядоченная композиция в рамках Quest». In §4.1 formal section: replace `Γ_work := Capability_set_A ∪ Capability_set_B` with `Γ_sys := Clan_as_System(members) [structural]` and optionally `Γ_method := Quest_protocol(Role_A, Role_B, ordered_steps) [operational]`. In §5 mermaid: rename node from `Γ_work (B.1.6)` to `Γ_sys + Γ_method (B.1.2 / B.1.5)`. | FAIL-1 | Medium (touches §2.1 + §3.5 + §4.1 + §5) |
| RC-2 (Moderate) | Add §4.0 A.1.1 BoundedContext (Clan/VirtualTribe) with: Glossary (mutual instrumentation, agreed share, tribal relation, Quest, Season, fork-and-leave), Invariants (R12 no-extraction, fork-and-leave right, context-bounded RoleAssignment, SpeechAct-context-policy), Roles (Holder#ClanMember:Clan-context per Charter archetype, Ruslan#Architect:Clan-founding-context, ROY-swarm#AIScribeRole:Clan-context), Bridges (Doc01-Self-OS ↔ Doc03-Clan, Doc03-Clan ↔ Doc06-TrustMechanism) | FAIL-3 | Medium (new subsection; content exists in narrative, needs formal structure) |
| RC-3 (Moderate) | In §2.1 U.SpeechAct row and §3.6: add normative caveat — «A.2.9:4.1 constraint: SpeechAct institutes tribal relation ONLY under declared Clan-context policy. Policy: U.SpeechAct of actType="Charter-signing" institutes {R12-Commitment, Holder#ClanMember:Clan-context, Charter-signatory-status} — declared in Clan-BoundedContext §4.0 (RC-2).» | FAIL-2 | Small (one paragraph addition; depends on RC-2) |
| RC-4 (Minor) | In §2.1 B.2 row and §4.1 formal section: add BOSC-A-T-X mapping — «B.2 trigger: T-trigger (Phase Promotion; commission event = Charter signing activates temporal phase change pre-Clan → Clan) + S-trigger (new coordination channels: Charter-role assignments + Quest protocol). Charter threshold ≥5 signatures + 1 Quest = Jetix-operational approximation of T+S triggers.» | FAIL-4 | Small (additive; does not change the B.2 claim, adds FPF grounding) |

---

## §8 Dissents (new, from this critic pass)

**D-DOC03-ENG-4 (this pass, eng-critic).** Γ_work category error — the correct FPF primitive for capability composition is Γ_method (B.1.5) or Γ_sys (B.1.2), not Γ_work (B.1.6). Γ_work aggregates spent resources (resource deltas on U.Work records), not capabilities (U.Capability dispositional properties).
- F: F5 (codified in FPF Spec B.1.6 body, operator signature, explicit separation from Γ_method)
- ClaimScope: holds for FPF B.1.6 as-specified; unknown if Levenchuk extends Γ_work semantics in FPF extensions not visible in this Spec version
- R: {refuted_if: FPF Spec B.1.6 body found to extend to capability aggregation in a section not grepped; accepted_if: FPF Spec body confirms resource-delta-only scope — which it does in B.1.6:5 and B.1.5:11 Rationale}

**D-DOC03-ENG-5 (this pass, eng-critic).** U.SpeechAct «institutes» claim is directionally correct but missing FPF-normative context-policy declaration. Without the Clan-context policy, A.2.9:4.1 normative constraint means the SpeechAct should be treated as «communicative Work occurrence with observable provenance only», not as an institution-creating act.
- F: F4 (codified in FPF A.2.9:4.1 normative text; context-policy gap is an FPF structural requirement)
- ClaimScope: holds for FPF A.2.9 as-specified; Clan-context policy, once declared (RC-3), would satisfy the constraint
- R: {refuted_if: FPF A.2.9 found to have weaker context-policy requirement in other sections; accepted_if: no Clan-context policy is added and institutional claim is retained verbatim}

**D-DOC03-ENG-6 (this pass, eng-critic, convergent with D-DOC03-ENG-3).** B.2 trigger predicate «≥5 signatures + 1 Quest» is a Jetix-operational approximation, not an FPF B.2 BOSC-A-T-X observable. The mapping to T-trigger (Phase Promotion) + S-trigger (structural reorganization) is implicit, not declared. Convergent with eng-integrator self-dissent D-DOC03-ENG-3.
- F: F4 (FPF B.2:4.2 BOSC-A-T-X trigger list is normative; count-threshold is not in the trigger list)
- ClaimScope: holds for FPF B.2 as-specified; Jetix-operational threshold is valid as an approximation if BOSC-A-T-X mapping is declared
- R: {refuted_if: FPF B.2 found to permit pure count-based triggers; accepted_if: mapping to T+S triggers is added as RC-4}

---

## §9 Proposed Writes

```yaml
proposed_writes:
  - path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-critic.md
    status: this file — critic output
    action: Write (complete)
    frontmatter:
      title: "Doc 03 Eng-Critic — Jetix as Virtual Tribe Substrate (FPF-Described)"
      date: 2026-05-17
      type: eng-critic-output
      status: critic-draft
    body: this document
    edges_to_add:
      - {type: critiques, from: this, to: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-integrator.md}
      - {type: grounded-in, from: this, to: raw/external/ailev-FPF/FPF-Spec.md, sections: [B.1.6, A.2.9, B.2]}
      - {type: cross-ref, from: this, to: vision/jetix-fpf-describe/01-jetix-as-self-os-substrate.md, section: §4.1}
```

---

## §10 Output Schema (structured)

```yaml
mode: critic
context:
  task_id: task-fpf-describe-jetix-2026-05-17
  artefact_path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-integrator.md
  cycle_id: cyc-fpf-describe-2026-05-17
critique:
  conformance_checklist:
    - {check_id: "1-deep-module", result: N/A, evidence: "Not a code artefact"}
    - {check_id: "2-function-purpose", result: pass, evidence: "Every section has declared purpose; §2 primitive table has per-row role declarations"}
    - {check_id: "3-test-integrity", result: N/A, evidence: "No test cases; R-conditions serve equivalent function"}
    - {check_id: "4-premature-abstraction", result: fail, evidence: "Γ_work used for capability composition — abstraction misassigned to wrong primitive before validation against FPF Spec"}
    - {check_id: "5-external-dependency", result: pass, evidence: "All FPF primitives and source docs cited with src-tags; failure modes declared via R-conditions"}
    - {check_id: "6-dry", result: pass, evidence: "No duplicated definitions across sections; §4 and §2 use distinct registers"}
    - {check_id: "7-tool-eval-acceptance", result: N/A, evidence: "Not a tool-eval draft"}
    - {check_id: "8-architecture-pattern", result: N/A, evidence: "Not architecture-proposal; Γ_work error flagged separately in specific-failures"}
  acceptance_predicate: "artefact DOES NOT PASS — fails check 4 (Γ_work category error) AND missing A.2.9 context-policy AND missing A.1.1 BoundedContext for Clan context"
  alternatives:
    - {label: A, description: "Replace Γ_work with Γ_sys (structural aggregation)", kill_condition: "Γ_sys WLNK constraint too restrictive for super-additive capability synergies"}
    - {label: B, description: "Replace Γ_work with Γ_method (ordered capability composition per Quest)", kill_condition: "Fails if cooperation is order-independent; unlikely for real Quests"}
    - {label: status-quo, description: "Retain Γ_work and argue capability = spent resource", kill_condition: "Fails because FPF B.1.6 body explicitly excludes non-resource-delta operations; Γ_work operator signature is Set[U.Work] → U.Work, not Set[U.Capability] → U.Capability"}
  anti_scope:
    - "Not evaluating strategic validity of mutual instrumentation concept"
    - "Not evaluating cultural sufficiency of R12 + E.5 (philosophy territory)"
    - "Not evaluating DAO comparative differentiation (OQ-D03-4; comparative analysis not performed)"
    - "Not evaluating L0→L6 ladder roadmap (mgmt territory)"
    - "Not evaluating Ruslan voice narrative (intentionally informal; attributed correctly)"
specific_failures_found:
  - {ap_code: "FAIL-1-Γ_work-category-error", location: "§2.1 primitive table row Γ_work; §3.5; §4.1; §5 mermaid", evidence: "FPF B.1.6:5 operator signature Set[U.Work]→U.Work; B.1.5:11 Rationale: Γ_work accounts resources, Γ_method composes behaviour"}
  - {ap_code: "FAIL-2-A.2.9-context-policy-missing", location: "§2.1 U.SpeechAct row; §3.6; §4.1", evidence: "FPF A.2.9:4.1 normative: 'Absent an explicit policy, treat as communicative Work occurrence with observable provenance only'"}
  - {ap_code: "FAIL-3-A.1.1-BoundedContext-absent", location: "§4 formal version — no A.1.1 subsection", evidence: "Doc 01 §4.1 has full Glossary+Invariants+Roles+Bridges; Doc 03 has none for Clan context"}
  - {ap_code: "FAIL-4-B.2-trigger-not-BOSC-mapped", location: "§2.1 B.2 row; §4.1 formal VirtualTribe definition", evidence: "FPF B.2:4.2 requires BOSC-A-T-X observable triggers; count threshold not mapped to triggers"}
recommended_changes:
  - {change: "Replace Γ_work (B.1.6) with Γ_sys (B.1.2) + Γ_method (B.1.5) throughout §2.1 + §3.5 + §4.1 + §5", ap_code_addressed: "FAIL-1", estimated_effort: medium}
  - {change: "Add §4.0 A.1.1 BoundedContext for Clan/VirtualTribe (Glossary + Invariants + Roles + Bridges)", ap_code_addressed: "FAIL-3 + FAIL-2", estimated_effort: medium}
  - {change: "Add A.2.9 context-policy declaration for Charter-signing SpeechAct instituting tribal relation", ap_code_addressed: "FAIL-2", estimated_effort: small}
  - {change: "Map Charter threshold ≥5+1 to BOSC-A-T-X (T-trigger Phase Promotion + S-trigger structural reorganization)", ap_code_addressed: "FAIL-4", estimated_effort: small}
provenance:
  - {path: raw/external/ailev-FPF/FPF-Spec.md, range: "lines 29193-29294 (B.1.6 body)", quote: "Γ_work neither schedules nor orders steps; it composes resource deltas attached to Work"}
  - {path: raw/external/ailev-FPF/FPF-Spec.md, range: "lines 5287-5406 (A.2.9 body)", quote: "Absent an explicit policy, treat a U.SpeechAct as a communicative Work occurrence with observable provenance only; do not infer deontic bindings from the act by default"}
  - {path: raw/external/ailev-FPF/FPF-Spec.md, range: "lines 29473-29592 (B.2 body)", quote: "Declare MHT when one or more of the following observable triggers occur [BOSC-A-T-X list]"}
  - {path: vision/jetix-fpf-describe/01-jetix-as-self-os-substrate.md, range: "lines 249-267 (§4.1)", quote: "Ruslan#OwnerRole:Self-OS-substrate-BoundedContext"}
confidence: high
confidence_method: rubric-pass-rate
escalations: []
dissents:
  - D-DOC03-ENG-4 (Γ_work category error — new this pass)
  - D-DOC03-ENG-5 (A.2.9 context-policy missing — new this pass)
  - D-DOC03-ENG-6 (B.2 count-threshold not BOSC-mapped — convergent with D-DOC03-ENG-3)
  - D-DOC03-ENG-1 (R12 + E.5 sufficiency — preserved from eng-integrator; philosophy territory, not resolved here)
  - D-DOC03-ENG-2 (DAO differentiation — preserved from eng-integrator; comparative analysis pending)
  - D-DOC03-ENG-3 (B.2 count trigger — preserved from eng-integrator; CONVERGENT with D-DOC03-ENG-6)
```

---

*Eng-critic pass complete. 4 specific failures found. 3 critical/moderate (FAIL-1 Γ_work, FAIL-2 A.2.9 policy, FAIL-3 BoundedContext), 1 minor (FAIL-4 B.2 mapping). Primary novel primitive Γ_work (B.1.6) is wrong category — correct primitive is Γ_method (B.1.5) or Γ_sys (B.1.2). All prior eng-integrator dissents preserved. 3 new dissents added (D-DOC03-ENG-4, -5, -6). Brigadier integrates.*
