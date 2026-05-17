---
title: "Doc 04 Eng-Critic — Jetix as Corporation (FPF-Described)"
date: 2026-05-17
type: eng-critic-output
status: critic-draft
artefact_reviewed: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-corporation-eng-integrator.md
critic_cell: engineering-expert × critic
mode: critic
task_id: task-fpf-describe-jetix-2026-05-17
cycle_id: cyc-fpf-describe-2026-05-17
F: F4
G: eng-critic-fpf-primitive-correctness
R: refuted_if_FPF_Spec_A.2.3_definition_found_to_cover_design-only_PromiseContent_without_A.2.8_Commitment_AND_brief_focus_questions_resolved_differently_by_philosophy-expert-critic
language: russian (narrative) + english (FPF primitives + code)
provenance:
  - path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-corporation-eng-integrator.md
    range: "1-479"
    quote: "full artefact reviewed"
  - path: raw/external/ailev-FPF/FPF-Spec.md
    range: "A.2.3:4 definition + A.2.8:4.1 normative + A.1.1:4.2 core components + B.2:4.2 BOSC-A-T-X"
    quote: "FPF canonical definitions consulted for all four focus areas"
  - path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-self-os-eng-critic.md
    range: "§1 acceptance table, §2.1 A.4 pass, §3 A.1.1 audit"
    quote: "Doc 01 precedent for role consistency check + A.1.1 template"
  - path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-critic.md
    range: "§2 CC, §4 anti-scope, §5 cross-doc, §6 specific failures FAIL-4 B.2 BOSC-A-T-X"
    quote: "Doc 03 precedent for B.2 trigger mapping + cross-doc consistency template"
---

# Doc 04 Eng-Critic — Jetix as Corporation (FPF-Described)

---

## §1 Conformance Checklist (8 binary checks)

| check_id | result | evidence |
|---|---|---|
| 1-deep-module | N/A | Not a code artefact; FPF-primitive surface area is medium-depth — §2 table maps 8 primitives, §4 unpacks 5 formally. Surface area proportional to complexity; no shallow-module analogue triggered |
| 2-function-purpose | pass | Every section has declared purpose; §2 primitive table has per-row role + ClaimScope + F-G-R declarations; §4 subsections (§4.1–§4.5) each named by primitive. No ambiguous sections |
| 3-test-integrity | N/A | No test cases; frontmatter R-condition is falsifiable; per-claim F-G-R register in §2.1 serves equivalent obligation |
| 4-premature-abstraction | fail | U.PromiseContent (A.2.3) applied to TRM ladder at design-level — structurally an epistemic promise-clause spec — without declaring the A.2.8 U.Commitment binding that makes it deontic. The doc's own §2.1 row (A.2.8) and §4.1 note the adjudication gap but then continues labelling TRM as U.PromiseContent without flagging the category-layering consequence. This is not strictly a premature-abstraction in the Ousterhout/Brooks sense, but it IS a primitive-level category issue warranting AP-ENG-9 analogue: the «PromiseContent = what Jetix promises» abstraction is applied before validating whether an A.2.8 Commitment binding is required for any claim beyond design-level. See FAIL-1 |
| 5-external-dependency | pass | All external sources cited with inline [src:] tags; R-conditions declared; LIVE-FLAG-ICP disclosed as active blocker in §3 + §7; B.5.1 Explore state disclosed with git evidence |
| 6-dry | pass | No repeated definitions; §2 primitive table, §4 formal version, and §3 narrative use distinct registers without duplicating content |
| 7-tool-eval-acceptance | N/A | Not a tool-eval draft |
| 8-architecture-pattern | partial-fail | §4.3 B.2 MHT section names the Phase 1→2→3 sequence but does NOT map the triggers to BOSC-A-T-X observable predicates (same gap flagged in Doc 03 eng-critic FAIL-4; established pattern in this series). The Phase 1→2 trigger «Foundation LOCKED» and the Phase 2→3 trigger «10+ curated makers + tasks > 1 workshop» are Jetix-operational thresholds, not declared against B.2:4.2 BOSC-A-T-X taxonomy. See FAIL-4 |

**Overall: 6 of 8 applicable checks pass (2 N/A). Check 4 = fail; check 8 = partial-fail. Both fixable without structural rewrite.**

---

## §2 Acceptance Predicate (Hamel-binary)

`swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-corporation-eng-integrator.md` passes Conformance checks 1 (N/A), 2 (pass), 3 (N/A), 5 (pass), 6 (pass), 7 (N/A) BUT FAILS check 4 (U.PromiseContent used without A.2.8 Commitment binding clarification — category-layering gap), PARTIAL-FAILS check 8 (B.2 MHT trigger predicates not mapped to BOSC-A-T-X), AND has A.1.1 BoundedContext declared at concept-level only (§2.2) without the Glossary + Invariants + Roles + Bridges four-part structure required by FPF A.1.1:4.2 (same gap as Doc 03 FAIL-3).

**Current predicate result: APPROVE-WITH-EDITS.** Three corrective actions required before promotion:

1. Clarify U.PromiseContent / U.WorkPlan / U.Commitment layering: TRM ladder design-artefact = U.PromiseContent (correct as design episteme). Add explicit note that until A.2.8 U.Commitment is instantiated with a named client + adjudication path, the TRM PromiseContent does NOT carry deontic obligation (see FAIL-1).
2. Add A.1.1 BoundedContext formal section for Corp-context (Glossary + Invariants + Roles + Bridges) — currently §2.2 is a bullet list, not an A.1.1 declaration per FPF A.1.1:4.2 (see FAIL-3).
3. Map Phase 1→2 and Phase 2→3 B.2 MHT triggers to BOSC-A-T-X observable predicates (see FAIL-4).

---

## §3 Alternatives (≥2 + status-quo + kill-conditions)

| # | Alternative | Kill condition |
|---|---|---|
| A | Keep U.PromiseContent for TRM ladder; add a single normative sentence: «U.PromiseContent at design-level. Deontic obligation arises ONLY when a U.Commitment (A.2.8) is instantiated with a named Client + adjudication path. Until then, TRM = U.Episteme describing intended offering — not a binding promise.» | Fails if philosophy-expert × critic determines that even design-level PromiseContent carries implicit deontic claims in the FPF reading; then A would need to be demoted to U.WorkPlan for pre-contract state |
| B | Replace U.PromiseContent with U.WorkPlan (A.15.2) for TRM ladder in pre-contract state. U.WorkPlan = «intended Work occurrences over a horizon with planned windows and dependencies». TRM L0-L5 = schedule of intended offerings. Bind to U.PromiseContent only on first signed contract. | Fails if U.WorkPlan's required fields (planned windows, dependencies, intended performers, resource budgets, acceptance targets) cannot be filled for TRM ladder — the ladder is a general offering shape, not a project schedule; U.WorkPlan would be over-specific in the wrong dimension |
| C | Status-quo — keep U.PromiseContent without A.2.8 Commitment or WorkPlan clarification | Fails because FPF A.2.3:4 explicitly states: «U.PromiseContent is promise content (U.Episteme), not a deontic binding. One or more explicit U.Commitment objects (A.2.8) MAY reference a U.PromiseContent as payload to bind an accountable principal/role-assignment; the clause itself does not "obligate" anyone until such a commitment is represented.» Status-quo leaves this critical spec-normative caveat invisible to the L1 reader. |

**Engineering recommendation: Alternative A is correct.** U.PromiseContent IS the right primitive for TRM at design-level. The gap is not primitive misuse — it is a missing normative caveat about the design/run distinction. A.2.3 explicitly says «not a deontic binding» — that sentence needs to surface in the doc. Alternative B (U.WorkPlan) would be incorrect: WorkPlan requires planned windows and resource budgets per A.15.2, which TRM ladder as a general offering structure does not have.

---

## §4 Anti-scope

- Не оцениваю стратегический вопрос о правильности TRM как бизнес-модели. Это α-5 Direction, Ruslan decides.
- Не оцениваю ICP choice (Mittelstand vs Online-first vs 2-оси portrait) — Ruslan strategic judgment. LIVE-FLAG-ICP корректно раскрыт в §7; resolution не входит в engineering domain.
- Не оцениваю Phase 3 take-rate economics (§7 OQ-CORP-5) — это investor-expert × critic territory. OQ-CORP-5 правильно surface'ит этот вопрос.
- Не оцениваю «portable accumulation» механизм для Работников (§7 OQ-CORP-4) — mgmt-expert × integrator (4th cell) территория, как корректно указано в OQ-CORP-4.
- Не оцениваю A.2.8 adjudication path содержательно (какие условия термина, dispute resolution, default clauses) — это legal + mgmt territory, не engineering craft.
- Не оцениваю нарратив §3 (plain Russian sections) — intentionally informal and attributed to Ruslan voice.
- Не оцениваю Reed's Law moat claim epistemic validity — это philosophy-expert × critic territory (falsifiability of the 2^N moat claim at F2 grade).

---

## §5 Cross-doc consistency check

### Doc 01 (Self-OS) role declarations

Doc 01 §4.1 (eng-critic verified) declares:
- `Ruslan#OwnerRole:Self-OS-substrate-BoundedContext`
- `ROY-swarm#AIScribeRole:Self-OS-substrate-BoundedContext`
- Bridge: `Self-OS ↔ Tribe (Doc 03) Bridge — individual substrate = atomic unit People-NS`

### Doc 03 (Virtual Tribe) role declarations

Doc 03 (eng-critic FAIL-3) has NO formal A.1.1 BoundedContext. Roles are narrative only.
Doc 03 references Ruslan as «Architect#системный-дизайн + founder» in different bounded context (Clan-context vs Self-OS-BoundedContext) — consistent per IP-1 + A.2.1.

### Doc 04 (Corporation) role declarations

Doc 04 §4.2 declares three tiers via Holder#Role:Context tokens:
- `Partner#PartnerRole:JetixPlatform`
- `Client#ClientRole:TRMengagement`
- `Employee#EmployeeRole:JetixInternalTeam`

§4.3 B.2 MHT declares Ruslan as `solo founder` at Level 0 and `Ruslan + ROY AI swarm` at Level 1.

### Cross-doc consistency verdict

| Item | Status | Notes |
|---|---|---|
| Ruslan's role in Doc 04 | **Partial gap** | Doc 01 = Ruslan#OwnerRole:Self-OS-substrate-BoundedContext (formal token); Doc 03 = Ruslan#Architect (narrative, no formal token per FAIL-3); Doc 04 = Ruslan as «solo founder» (narrative in §4.3) + «sole strategist» (§8 R1). No formal A.2.1 token declared for Corp-context. Missing: `Ruslan#FounderRole:JetixCorp-BoundedContext` (parallel to Doc 01 OwnerRole). This is the Doc 01#OwnerRole / Doc 03#FounderRole / Doc 04 gap the brief asks to check — see FAIL-2 below |
| F-G-R floor | Consistent | All three docs at F2 document-level floor; per-claim grades compatible (Doc 04 B.5.1 Explore at F5 = strongest claim, correctly sourced from git evidence) |
| R1 attribution | Consistent | All three docs carry `prose_authored_by: ruslan-via-voice-dictation+brigadier-structured`; §8 R1 reaffirmation explicit |
| EP-5 disclosure | Consistent | All three carry EP-5 disclosure; Doc 04 adds EP-2 (vapor status) and LIVE-FLAG-ICP |
| BoundedContext formal section | **GAP** | Doc 01 has full A.1.1 (Glossary+Invariants+Roles+Bridges in §4.1). Doc 03 has none (FAIL-3). Doc 04 has §2.2 bullet-list «что включено / что НЕ включено» — this is scope declaration prose, NOT an A.1.1 BoundedContext with Glossary+Invariants+Roles+Bridges. Same structural gap as Doc 03 |
| B.2 MHT trigger mapping | **INCONSISTENCY** | Doc 03 eng-critic surfaced FAIL-4 (B.2 trigger not mapped to BOSC-A-T-X). Doc 04 has the same gap — Phase 1→2 trigger «Foundation LOCKED» is an artefact event, not a declared BOSC-A-T-X observable. Same fix applies |

---

## §6 Specific Failures Found

### FAIL-1 (Moderate): U.PromiseContent/U.Commitment layering — missing normative caveat

**AP code:** AP-ENG-9 analogue (abstraction applied before validating boundary conditions of primitive)

**Location:** §2.1 row U.PromiseContent; §4.1 formal section; §0 TL;DR «структура U.PromiseContent (A.2.3)»

**Evidence (verbatim from FPF Spec A.2.3:4, normative):**
> «U.PromiseContent is promise content (U.Episteme), not a deontic binding. One or more explicit U.Commitment objects (A.2.8) MAY reference a U.PromiseContent as payload to bind an accountable principal/role-assignment; the clause itself does not "obligate" anyone until such a commitment is represented.»

And from A.2.3:4.1 structure:
> `providerRole: U.Role` — role KIND, not a person/system; `acceptanceSpec: U.Episteme` — targets; adjudication is NOT embedded in U.PromiseContent itself (it belongs in U.Commitment A.2.8).

**Analysis:** The doc's usage of U.PromiseContent for TRM is CORRECT as a design-level promise-clause episteme. The primitive is not misused — TRM ladder IS the correct candidate for U.PromiseContent. The gap is that the doc presents the TRM ladder as U.PromiseContent (A.2.3) without surfacing the FPF-normative caveat: until a U.Commitment (A.2.8) is instantiated with a named Client + adjudication path, the PromiseContent does NOT bind Jetix to deliver. This distinction matters enormously for the L1 audience (Levenchuk, Tseren): they may read §4.1 and §0 as Jetix having operational obligations, when it is a design episteme.

The doc acknowledges this in §2.1 row A.2.8: «A.2.8 adjudication path = absent (informal)» and in OQ-CORP-3. But that acknowledgment is buried in the primitive table, not surfaced at the point of U.PromiseContent use in §0, §2.1 row, and §4.1.

**D-CORP-1 anticipated (§8) partially addresses this** by noting the philosophy-expert anticipated counter-claim (U.WorkPlan vs U.PromiseContent). This critic's verdict: U.PromiseContent is correct at design-level; what is missing is the explicit deontic-gap declaration at §4.1 and §0. The anticipated counter-claim in D-CORP-1 is directionally right but frames the fix as primitive replacement; the fix is a normative caveat, not a replacement.

**Brief focus question #1 answer:** U.PromiseContent IS the correct primitive for TRM ladder at design-level. U.WorkPlan (A.15.2) would be incorrect — WorkPlan requires planned windows + resource budgets + dependencies + acceptance targets (per A.15.2 definition), which TRM as a generic offering shape does not have. U.Commitment (A.2.8) should be declared as the BINDING object that MAY reference this PromiseContent — but only at contract-signing with a named client. The composite structure is: `U.PromiseContent (design episteme) → referenced by → U.Commitment (A.2.8) once contract signed`. Doc 04 should declare this explicitly in §4.1.

**Severity: Moderate.** Primitive is correct; caveat is missing. Fixable by adding one normative sentence to §0, §2.1 row U.PromiseContent, and §4.1.

---

### FAIL-2 (Minor): Ruslan's Corp-context role not declared as formal A.2.1 token

**AP code:** Structural gap (cross-doc consistency gap; §1b integrative obligation)

**Location:** §4.3 B.2 MHT («Level 0: Ruslan (solo founder) — pre-holon»); §8 R1 reaffirmation («Ruslan = sole strategist»)

**Evidence (cross-doc):**
- Doc 01: `Ruslan#OwnerRole:Self-OS-substrate-BoundedContext` (formal token, eng-critic verified)
- Doc 03: Ruslan as «Architect#системный-дизайн» (narrative only; FAIL-3 in Doc 03 eng-critic noted A.2.1 tokens absent)
- Doc 04: Ruslan as «solo founder» in §4.3 (narrative); «sole strategist» in §8 (R1 reaffirmation). No formal `Ruslan#FounderRole:JetixCorp-BoundedContext` token declared.

**Analysis:** FPF A.2.1 U.RoleAssignment pattern requires `Holder#Role:Context` token for formal role declarations. Doc 01 established the template correctly. Docs 03 and 04 fall short — roles are named in narrative but not declared as A.2.1 tokens in the Corp BoundedContext. The brief specifically asks to check Doc 01#OwnerRole + Doc 03#FounderRole + Doc 04 consistency. Current state: Doc 04 does NOT declare a formal `Ruslan#FounderRole:JetixCorp-BoundedContext` token (or equivalent). Doc 03 has the same gap. Both docs name Ruslan in different roles in different bounded contexts — this is correct per IP-1 (role ≠ identity) — but the tokens are not formally declared.

Note: this is LESS critical than Doc 03's FAIL-3 (where the entire A.1.1 BoundedContext is missing). Here the roles ARE present in §4.2 for the three engagement tiers; what is missing is Ruslan's own formal token in the Corp-BoundedContext.

**Severity: Minor.** Additive fix — one line in §4.2 or in a new §4.0 A.1.1 BoundedContext section (which is required anyway per FAIL-3).

---

### FAIL-3 (Moderate): A.1.1 BoundedContext absent for Corp-context

**AP code:** AP-ENG-12 analogue (architecture-without-structure declaration; same as Doc 03 FAIL-3)

**Location:** §2.2 «Bounded context (A.1.1 scope declaration)» — is a prose bullet list, not a formal A.1.1 BoundedContext

**Evidence (FPF Spec A.1.1:4.2, normative):**
A U.BoundedContext MUST include:
- **Glossary (Local Lexicon):** U.Lexeme entries defining local vocabulary
- **Invariants (Local Rules):** U.ConstraintRule set that must hold within the context
- **Roles (Local Taxonomy):** partial order of U.Role valid within this context
- **Bridges (Optional alignments):** explicit cross-context U.Alignment records

Doc 04 §2.2 provides a bullet-list declaring what is included / not included in O-02 Corporation. This is a scope-declaration in plain language, not an FPF A.1.1 BoundedContext. Specifically missing:
- **Glossary:** «TRM», «land-and-expand», «portable accumulation», «vapor», «mета-мастерская» — all used as technical terms without formal local glossary entries
- **Invariants:** R12 anti-extraction is declared as constitutional posture but not listed as a formal Invariant of the Corp-BoundedContext; B.5.1 Explore state is mentioned as a status but not as a local invariant (e.g. «Within Corp-BoundedContext: revenue = 0 until Phase 2 trigger fires; legal entity = not registered until HITL ack»)
- **Roles:** §4.2 declares three engagement tiers correctly as A.2.1 tokens (Partner#PartnerRole, Client#ClientRole, Employee#EmployeeRole). This is the strongest role declaration in Docs 03-04. But Ruslan's own role is absent (FAIL-2).
- **Bridges:** Doc 04 ↔ Doc 01 (Self-OS as substrate) bridge is named in §6.3 (Foundation Parts) and §6.4 (cross-refs), but not formally declared as U.Alignment per A.1.1:4.2. Doc 04 ↔ Doc 03 (Clan = constitutional layer) bridge is named in §6.4 but not formally declared.

**Positive note:** §4.2 is the strongest formal role declaration across all four docs reviewed — three A.2.1 Holder#Role:Context tokens explicitly named. This is Doc 04's structural strength.

**Severity: Moderate.** §2.2 exists and conveys the intent; it needs restructuring into the four A.1.1 components. Substantial content already present in §2.2 + §4.2 + §6.

---

### FAIL-4 (Minor): B.2 MHT trigger predicates not mapped to BOSC-A-T-X

**AP code:** Structural gap (same as Doc 03 FAIL-4; established pattern in this series)

**Location:** §4.3 B.2 MHT formal section; §3 narrative «Фазы эволюции»

**Evidence (FPF Spec B.2:4.2 BOSC-A-T-X, normative):**
> «Declare MHT when one or more of the following observable triggers occur: B — Boundary closure/opening; O — Objective emergence; S — Structural re-organization; C — Capability super-additivity; A — Agency threshold crossing; T — Temporal consolidation; X — Context rebase. Any two together almost always warrant MHT.»

Doc 04 §4.3 states:
```
Phase 1→2: Foundation LOCKED (fired 2026-04-28) + first paying partner joins
Phase 2→3: task complexity > single workshop + curated community of 10+ makers with track record
```

These are Jetix-operational triggers, not BOSC-A-T-X observable predicates. Brief focus question #2 asks whether this should use the same BOSC-A-T-X framework as Doc 03 §4.5 — yes, it should (same B.2 pattern, same FPF requirement).

**Mapping analysis:**

Phase 1→2 triggers map to:
- **T (Temporal consolidation):** Foundation LOCKED = phase-commissioning event (design → operation; Tᴰ → Tᴿ for Foundation v1.0)
- **S (Structural re-organization):** First human team member joins (coordination channels expand beyond solo-founder + AI-swarm)
- **A (Agency threshold):** First paying partner = external agency with commitments enters the Corp-holon

Phase 2→3 triggers map to:
- **C (Capability super-additivity):** «tasks > single workshop» = capability synergy exceeds additive; super-additivity threshold reached
- **S (Structural re-organization):** Community of workshops = new inter-workshop coordination channels emerge (meta-holon coordination)
- **T (Temporal consolidation):** «2028-2029 earliest» = temporal phase commissioning

Neither Phase trigger set is declared against BOSC-A-T-X in the doc. The D-CORP-2 anticipated dissent (mgmt × integrator) correctly notes «Foundation LOCKED = necessary NOT sufficient» — this is equivalent to saying the T-trigger alone does not warrant MHT per B.2 («any two... almost always warrant»).

**Severity: Minor.** Same as Doc 03 FAIL-4. Additive fix — map triggers to BOSC-A-T-X. Does not invalidate B.2 claim; adds FPF grounding.

---

## §7 Recommended Changes

| # | Change | FAIL addressed | Estimated effort |
|---|---|---|---|
| RC-1 (Moderate) | In §4.1 U.PromiseContent formal section: add normative caveat paragraph — «Per FPF A.2.3:4: U.PromiseContent is an episteme describing the intended offering (design-time). It does NOT carry deontic obligation by itself. Obligation arises ONLY when a U.Commitment (A.2.8) is instantiated with a named Client, explicit adjudication path, and validity window. Until first TRM contract signed: TRM ladder = U.PromiseContent (design episteme). First contract signed: instantiate U.Commitment referencing this PromiseContent.» In §0 TL;DR: add «(episteme, not deontic binding per FPF A.2.3:4)» inline after first U.PromiseContent mention. In §2.1 row U.PromiseContent: update ClaimScope note. | FAIL-1 | Small (three inline additions; no structural change) |
| RC-2 (Minor) | In §4.2 (or in a new §4.0 A.1.1 BoundedContext subsection per RC-3): add formal A.2.1 token for Ruslan — `Ruslan#FounderRole:JetixCorp-BoundedContext` + `Ruslan#SoleStrategistRole:JetixCorp-BoundedContext`. Cross-reference to Doc 01 `Ruslan#OwnerRole:Self-OS-substrate-BoundedContext` as Bridge (different bounded contexts, same person — IP-1 compliant). | FAIL-2 | Small (one to two lines; depends on RC-3 for placement) |
| RC-3 (Moderate) | Replace §2.2 prose bullet list with a formal A.1.1 BoundedContext section. Structure: (a) Glossary — define TRM, land-and-expand, portable accumulation, vapor, мета-мастерская as local Lexeme entries. (b) Invariants — R12 anti-extraction as I-1; B.5.1 Explore state conditions as I-2 («revenue = 0 AND no registered entity» is invariant of the BoundedContext until Phase 2); «no active client contracts» as I-3. (c) Roles — three engagement tier roles already in §4.2 (migrate here) + Ruslan#FounderRole from RC-2. (d) Bridges — Corp ↔ Self-OS (Doc 01): «JetixCorp-BoundedContext uses Self-OS-substrate-BoundedContext as operational substrate; bridge: Foundation Parts 1/4/7/9/10 are shared under Corp boundary». Corp ↔ Clan (Doc 03): «JetixCorp participants ⊆ Clan members per R12 constitutional layer; bridge: R12-Commitment applies to all Corp-Partner contracts». | FAIL-3 | Medium (new formal subsection; content exists across §2.2 + §4.2 + §6; requires structural reorganization not content invention) |
| RC-4 (Minor) | In §4.3 B.2 MHT formal section: add BOSC-A-T-X mapping — «Phase 1→2: T-trigger (Foundation LOCKED = temporal phase commissioning; design → operation) + S-trigger (first human team member: new coordination channel) + A-trigger (first paying partner: external agency with commitments). Phase 1→2 = T+S+A together. Phase 2→3: C-trigger (capability super-additivity: task complexity > single workshop) + S-trigger (meta-holon coordination channels emerge). Phase 2→3 = C+S. Jetix operational thresholds (Foundation LOCKED event / 10+ makers / first paying partner) = local approximations of BOSC-A-T-X predicates.» | FAIL-4 | Small (additive mapping; does not change the B.2 claim) |

---

## §8 Dissents (new, from this critic pass)

**D-CORP-04-ENG-1 (this pass, eng-critic).** U.PromiseContent is the correct FPF primitive for TRM ladder at design-level. The anticipated counter-claim in D-CORP-1 (philosophy-expert anticipated: U.WorkPlan is more accurate) is partially correct but overstates the case. U.WorkPlan (A.15.2) requires planned windows + resource budgets + dependencies + acceptance targets as STRUCTURAL fields. TRM L0-L5 ladder has acceptance targets (MRR goals) and duration horizons but not project-specific planned windows or performer dependencies. U.PromiseContent is more accurate for a generic service offering; U.WorkPlan is accurate for a specific project schedule. The design-document TRM ladder is not a project schedule.

- F: F5 (codified in FPF A.15.2 definition + A.2.3:4 definition; both unambiguous about what each primitive covers)
- ClaimScope: holds for TRM ladder as generic multi-level offering description; may not hold if TRM is operationalized as a specific project-plan document per client
- R: {refuted_if: FPF A.2.3 found to require instantiated performers as mandatory field (it does not — providerRole is a role KIND, not a named performer); accepted_if: A.2.3:4.1 structure confirms role as kind (which it does)}

**D-CORP-04-ENG-2 (this pass, eng-critic).** B.2 MHT trigger «Foundation LOCKED» (Phase 1→2) is necessary but NOT sufficient per FPF B.2:4.2. «Any two [BOSC-A-T-X triggers] together almost always warrant MHT.» Foundation LOCKED = T-trigger alone. MHT at Phase 1→2 requires at minimum T+S (Foundation LOCKED + first human team member / first coordination channel change). This converges with D-CORP-2 anticipated (mgmt × integrator): «Foundation LOCKED = artefact trigger; operational readiness = ещё нет.»

- F: F5 (codified in FPF B.2:4.2 — «any two» normative language; T-alone is insufficient)
- ClaimScope: holds for B.2 as specified; Phase 1→2 is not yet MHT unless S-trigger also fires
- R: {refuted_if: FPF B.2 found to permit single-trigger MHT in specific cases; accepted_if: B.2:4.2 «any two» reading confirmed — which it is in the Spec text}

**D-CORP-04-ENG-3 (this pass, eng-critic — structural dissent).** §2.2 current form is an adequate scope declaration for human readers (L1 audience) but is NOT a valid A.1.1 BoundedContext per FPF A.1.1:4.2. This does not block the document for L1 outreach (human readers can parse it), but it blocks formal FPF compliance. Resolution: RC-3 is recommended but brigadier may gate this as «Phase B — formal FPF compliance» if Ruslan's L1 outreach deadline takes priority. The structural gap should be flagged to Ruslan as a timeline trade-off, not a blocker on L1 outreach.

- F: F4 (operational convention — based on Doc 01/03 eng-critic precedent establishing A.1.1 as required structure)
- ClaimScope: holds for FPF formal compliance; does not hold for «is the doc useful for L1 audience» (the doc IS useful without formal A.1.1)
- R: {refuted_if: brigadier decides A.1.1 formal section is Phase B scope per Ruslan's L1 deadline; accepted_if: brigadier adds RC-3 to the promotion checklist}

---

## §9 Proposed Writes

```yaml
proposed_writes:
  - path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-corporation-eng-critic.md
    status: this file — critic output
    action: Write (complete)
    frontmatter:
      title: "Doc 04 Eng-Critic — Jetix as Corporation (FPF-Described)"
      date: 2026-05-17
      type: eng-critic-output
      status: critic-draft
    body: this document
    edges_to_add:
      - {type: critiques, from: this, to: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-corporation-eng-integrator.md}
      - {type: grounded-in, from: this, to: raw/external/ailev-FPF/FPF-Spec.md, sections: [A.2.3, A.2.8, A.1.1, B.2]}
      - {type: cross-ref, from: this, to: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-self-os-eng-critic.md, section: §3}
      - {type: cross-ref, from: this, to: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-critic.md, section: §6 FAIL-3 + FAIL-4}
```

---

## §10 Output Schema (structured)

```yaml
mode: critic
context:
  task_id: task-fpf-describe-jetix-2026-05-17
  artefact_path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-corporation-eng-integrator.md
  cycle_id: cyc-fpf-describe-2026-05-17
critique:
  conformance_checklist:
    - {check_id: "1-deep-module", result: N/A, evidence: "Not a code artefact"}
    - {check_id: "2-function-purpose", result: pass, evidence: "All sections named by primitive; §2.1 per-row roles; §4 subsections purposeful"}
    - {check_id: "3-test-integrity", result: N/A, evidence: "No test cases; R-conditions serve equivalent obligation"}
    - {check_id: "4-premature-abstraction", result: fail, evidence: "U.PromiseContent applied without surfacing FPF A.2.3:4 normative caveat — clause does not bind until U.Commitment (A.2.8) instantiated"}
    - {check_id: "5-external-dependency", result: pass, evidence: "All sources cited with [src:] tags; LIVE-FLAG-ICP disclosed; B.5.1 Explore evidenced by git state"}
    - {check_id: "6-dry", result: pass, evidence: "No repeated definitions; §2 + §4 + §3 use distinct registers"}
    - {check_id: "7-tool-eval-acceptance", result: N/A, evidence: "Not a tool-eval draft"}
    - {check_id: "8-architecture-pattern", result: partial-fail, evidence: "B.2 MHT Phase 1→2 and 2→3 triggers not mapped to BOSC-A-T-X observable predicates per FPF B.2:4.2"}
  acceptance_predicate: "artefact APPROVE-WITH-EDITS — fails check 4 (U.PromiseContent/U.Commitment layering caveat absent) AND partial-fails check 8 (B.2 BOSC-A-T-X mapping absent) AND A.1.1 BoundedContext §2.2 is scope-prose not formal Glossary+Invariants+Roles+Bridges declaration"
  alternatives:
    - {label: A, description: "Keep U.PromiseContent; add normative deontic-gap caveat in §0 + §2.1 + §4.1", kill_condition: "Fails if philosophy-expert determines even design-level PromiseContent implies deontic obligation in FPF reading"}
    - {label: B, description: "Replace U.PromiseContent with U.WorkPlan for pre-contract TRM state", kill_condition: "Fails because U.WorkPlan requires planned windows + resource budgets per A.15.2 — incompatible with TRM as generic offering structure"}
    - {label: status-quo, description: "Retain U.PromiseContent without deontic-gap caveat", kill_condition: "Fails because FPF A.2.3:4 normative text explicitly states clause does not bind until U.Commitment instantiated — L1 reader may misread as operational obligation"}
  anti_scope:
    - "Not evaluating TRM as business model (strategic judgment — Ruslan)"
    - "Not evaluating ICP choice resolution (LIVE-FLAG-ICP — Ruslan)"
    - "Not evaluating Phase 3 take-rate economics (investor-expert territory)"
    - "Not evaluating portable accumulation mechanism (mgmt territory)"
    - "Not evaluating A.2.8 adjudication path content (legal + mgmt)"
    - "Not evaluating Reed's Law moat epistemic validity (philosophy-expert territory)"
specific_failures_found:
  - {ap_code: "FAIL-1-PromiseContent-deontic-gap", location: "§0 TL;DR; §2.1 U.PromiseContent row; §4.1 formal section", evidence: "FPF A.2.3:4: 'clause itself does not obligate anyone until U.Commitment (A.2.8) represented'"}
  - {ap_code: "FAIL-2-Ruslan-FounderRole-token-absent", location: "§4.2 + §4.3 — Ruslan as 'solo founder' narrative only", evidence: "Doc 01 precedent: Ruslan#OwnerRole:Self-OS-substrate-BoundedContext; Doc 04 lacks parallel Corp-context token"}
  - {ap_code: "FAIL-3-A.1.1-BoundedContext-absent", location: "§2.2 — prose scope declaration only", evidence: "FPF A.1.1:4.2 requires Glossary+Invariants+Roles+Bridges; §2.2 is scope bullet list, not formal BoundedContext"}
  - {ap_code: "FAIL-4-B.2-trigger-not-BOSC-mapped", location: "§4.3 B.2 MHT formal section", evidence: "FPF B.2:4.2: triggers must be BOSC-A-T-X observables; 'Foundation LOCKED' is Jetix artefact event, not declared BOSC-A-T-X predicate"}
recommended_changes:
  - {change: "Add normative deontic-gap caveat in §4.1 + §0 + §2.1 U.PromiseContent row: 'episteme not deontic binding per FPF A.2.3:4; obligation arises only when U.Commitment (A.2.8) instantiated with named Client'", ap_code_addressed: "FAIL-1", estimated_effort: small}
  - {change: "Add Ruslan#FounderRole:JetixCorp-BoundedContext token to §4.2 (or §4.0 per RC-3)", ap_code_addressed: "FAIL-2", estimated_effort: small}
  - {change: "Restructure §2.2 into formal A.1.1 BoundedContext: Glossary (TRM, land-and-expand, portable accumulation, vapor, мета-мастерская) + Invariants (R12 I-1, B.5.1 conditions I-2) + Roles (three tier roles + Ruslan#Founder) + Bridges (Corp↔Self-OS, Corp↔Clan)", ap_code_addressed: "FAIL-3", estimated_effort: medium}
  - {change: "Map Phase 1→2 triggers to T+S+A BOSC predicates; Phase 2→3 to C+S BOSC predicates in §4.3", ap_code_addressed: "FAIL-4", estimated_effort: small}
provenance:
  - {path: raw/external/ailev-FPF/FPF-Spec.md, range: "A.2.3:4 + A.2.3:4.1 (lines ~2588-2616)", quote: "U.PromiseContent is promise content (U.Episteme), not a deontic binding"}
  - {path: raw/external/ailev-FPF/FPF-Spec.md, range: "A.1.1:4.2 (lines ~1362-1371)", quote: "Glossary, Invariants, Roles, Bridges — core components normative shape"}
  - {path: raw/external/ailev-FPF/FPF-Spec.md, range: "A.15.2 header row (line ~92)", quote: "U.WorkPlan: plan, schedule, intent, forecast — planned windows, dependencies, intended performers, resource budgets"}
  - {path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-tribe-eng-critic.md, range: "§6 FAIL-3 + FAIL-4 (lines ~143-176)", quote: "Doc 03 A.1.1 BoundedContext absent; B.2 trigger predicate underspecified — same pattern"}
confidence: high
confidence_method: rubric-pass-rate
escalations: []
dissents:
  - D-CORP-04-ENG-1
  - D-CORP-04-ENG-2
  - D-CORP-04-ENG-3
```
