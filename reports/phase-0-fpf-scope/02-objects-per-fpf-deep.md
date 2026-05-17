---
title: Per-Object FPF-Typed Deep Description — Phase 0 Task 2
date: 2026-05-17
phase: Phase 0 Task 2
type: integrated-per-object-deep
status: brigadier-integrated (3 cells: eng × integrator + systems × integrator + phil × critic)
parent: reports/phase-0-fpf-scope/01-jetix-objects-inventory.md
F: F4
G: phase-0-per-object-deep
R: refuted_if_object_missing_OR_anti_scope_absent_OR_F-G-R_per_claim_absent_OR_VSM_mapping_missing
language: russian + english (FPF primitives)
audience: Ruslan + L1 (Levenchuk / Tseren)
cell_drafts:
  - swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-engineering-integrator-per-object-deep.md
  - swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-systems-integrator-per-object-loops.md
  - swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-philosophy-critic-per-object-epistemic.md
constitutional_posture: R1 surface-only + R2 Foundation read-only + R6 provenance + append-only
---

# Per-Object FPF-Typed Deep Description — Phase 0 Task 2

> **Scope.** Brigadier integration of 3 cell drafts. Per object из 14 main (O-01..O-14): FPF-typed deep + feedback loops + epistemic critique → uniform per-object sections (~50-80 lines each, ≤1 page). Dissents preserved per AP-6. Critical 5 epistemic patterns (EP-1..EP-5 from phil) и 5 systemic patterns (Pattern 1-5 from systems) surface'нуты в §15-16.

> **Default.** Tier 1 ack для приходящего читателя: prefer **Task 1 inventory** для quick scan; этот файл = deep dive per object. Each object section is self-contained — можно читать выборочно.

---

## §0 Brigadier integration summary

**3-cell convergence on patterns across all 14 objects:**

**EP-1 (Artefact-system gap, ubiquitous; phil).** 10 of 14 objects carry LOCKED artefact status (document language-state per A.16) while operational status is F2-F4 or vapor. **Most critical pattern.** Each affected object's top claim needs split: Claim-as-document vs Claim-as-operational-system. Falsifier discipline missing для operational face.

**EP-2 (Use-mention drift; phil).** Workshop / Clan / Meta-workshop metaphor names initially mentioned as frames, then used as structural claims без declaration. UM-1..UM-4 в Task 1 + extended per object.

**EP-3 (Role/executor conflation, cross-object; phil).** CE-2 IP-1 split declared but not consistently applied в prose. «12 agents» язык persists across O-01 / O-04 / O-07 / O-12.

**EP-4 (Promise без commitment machinery; phil).** O-02 / O-10 / O-11 / O-13 contain promise-shaped language без unpacked U.Commitment (A.2.8): no adjudication path, no holder-of-obligation, no receipt mechanism.

**EP-5 (F-G-R applied to wrong subject; phil).** F8/F5 labels apply to document LOCK status, not claim truth-grade. Foundation «F8» = «approved via 8 RUSLAN-ACK» NOT «independently tested 8 times». Single-author approval ≠ FPF B.3 standard F8.

**Systems patterns (across 14 objects):**

- **Pattern 1 (Spec-to-Operations Gap Loop):** Reinforcing spec→spec без balancing operations→spec. Senge Law 3.
- **Pattern 2 (VSM Inversion):** Jetix has System 5/3 richer than System 1. Risk if operations don't materialize; advantage when they do.
- **Pattern 3 (Adjacent-Possible Concentration):** 5 of 14 objects находятся в «edge of chaos» — один шаг from emergence: O-01 (auto-KB), O-04 (first client), O-09 (NQD-CAL), O-10 (ICP fix), O-11 (R12 ack).
- **Pattern 4 (Dual Reinforcing/Collapsing Loop on revenue):** Loop A (spec → credibility → partnership → revenue) vs Loop B (no revenue → internal metrics substitute → complexity grows). Loop B dominates until first client.
- **Pattern 5 (Meadows level clustering):** L1-L2 (paradigm) = developed; L9-L12 (operations) = vapor. Confirms Pattern 2.

**Dissents preserved (NOT averaged) per AP-6:** D-2 / D-PHIL-SCOPE-2 / D-mgmt-2 / D-3 / D-1 (carried) + 3 systems-lens-specific (SYS-OQ-1..4) + 5 epistemic (AEC-1..5).

**Total claims:** 14 objects × avg 3-5 claims = ~60 F-G-R-tagged claims with falsifiers.

---

## §1 — O-01 — Jetix как оперативный субстрат (information management system)

**FPF primitive (eng):** U.System (A.1) + U.BoundedContext (A.1.1)
**Phil alternative typing:** U.System operating on information (NOT filesystem-repo which is carrier per A.10)
**FPF Part hosting:** Part A Kernel — Cluster A.I
**Applicable FPF mechanisms:** A.1 Holonic Foundation · A.1.1 U.BoundedContext · A.2 Role Taxonomy · A.4 Temporal Duality · A.15 Role-Method-Work · A.10 Evidence carrier (not the system itself)
**VSM mapping (systems):** System 1 (operations) — первичная operational unit; обеспечивает baseline (filesystem, voice pipeline, wiki, CRM, git)

**Что есть (concrete, evidenced):**

- Filesystem-canonical state + git-native rollback operational [F5 · jetix-operational · R-high] [src: CLAUDE.md §Global Rules «Filesystem = source of truth»]
- Voice pipeline (transcribe → extract → filter → review): 11 voice reviews active [F4 · R-medium] [src: 06-honest-self-audit §5]
- Wiki v2 substrate: 551 records; ROY swarm dispatching active [F4 · R-medium] [src: 01-inventory §2 O-01]
- Holonic structure: brigadier orchestrates 5 ROY experts × 4 modes [F4 · R-medium] [src: CLAUDE.md §Agent Roster]
- `shared/state/` JSON stale (last 2026-04-14); state-persistence partial [F3 · R-medium] [src: 01-inventory §3 O-01]

**Что задумано (aspirational):**

- Full auto-KB distribution (distribute.py.bak архивирован — manual-only сейчас) [F2 · R-low]
- Part 3 Methodology Library operational (сейчас memory-dominant substrate) [F2 · R-low]
- Method-signature enforcement via A.15 (RUSLAN-LAYER overlay incomplete) [F2 · R-low]

**Top claims with falsifier (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «Jetix = U.System operating on information as single-owner AI OS» | F4 | Refuted if owner scope expands OR filesystem-SoT rule violated без AWAITING-APPROVAL |
| «Filesystem = SoT; Notion = view» | F5 | Refuted if any state change canonical в Notion без filesystem counterpart |
| «12 specialized agents × 6 departments» | **F3 (phil-revised; CE-2 IP-1 conflation)** | Refuted as «12 running processes» by Phase column (Phase 3-4 not operational) |

**Anti-scope:**
- NOT filesystem-repo itself (= carrier per A.10; A.7 Strict Distinction)
- NOT юрлицо / корпорация (→ O-02)
- NOT vision/aspirational state (→ O-03; A.4 Temporal Duality)
- NOT Phase B managed team or enterprise clients
- NOT Notion as co-equal SoT

**Conflation traps (phil):** (1) Type-token: «12 agents» = evidence of complexity while 8 Phase-2..4 = type-declarations only. (2) Language-state vs operational: «working system» while state JSON stale. (3) Carrier/content: A.10 carrier ≠ U.System.

**Hidden assumptions (phil):** Single-owner stable. Filesystem monotonic (no destructive deletes; risk with Генеральная чистка). «Operating on information» = full activity (actually: LLM calls + filesystem I/O + HITL).

**Leverage point (systems, Meadows L6):** Замкнуть voice-pipeline → wiki/KB auto loop (one automation step, big variety gain).

**Feedback loops (systems):**
- R: Voice → review → ideas → more voice. Loop пока не closes auto через KB distribution.
- B: ROY swarm dispatches → drafts → integration → quality. Balancing через information quality.
- R: Git commits → state proxy → better dispatches. Loop works через git but не через state JSON.

**Cross-refs:**
- → O-04 (hosts): substrate carries working product
- → O-06b (operates-within): ROY swarm runs within substrate
- → O-07 (governed-by): Foundation specifies substrate governance
- → O-08 (constrained-by): Pillar C applies to all substrate actions

**Cross-object boundary disputes (phil):**
- vs O-04: citing O-01 substrate maturity (Foundation LOCKED) ≠ evidence of O-04 product maturity. Different falsifiers.
- vs O-07: Foundation Parts 1/3/5/9/11 memory-dominant — does O-07 actually constitute O-01 or merely describe intended architecture?

---

## §2 — O-02 — Jetix как юр.лицо / корпорация (in-progress)

**FPF primitive (eng):** U.RoleAssignment (A.2.1) + U.PromiseContent (A.2.3)
**Phil alternative:** U.System subtype BUT vapor as instantiated; conceptual U.System describing future U.System (not itself a system)
**FPF Part hosting:** Part A Cluster A.I
**Applicable FPF mechanisms:** A.2.1 RoleAssignment · A.2.3 PromiseContent · A.2.8 Commitment (NOT formally applied) · A.6.C Contract Unpacking (not applied)
**VSM mapping (systems):** System 5 (identity/policy) — vapor instantiation; identity-level purpose declared без operational entity

**Что есть:**
- Doc 1B LOCKED v1.0 = conceptual document (партнёры / клиенты / работники) [F5 · R-high] [src: JETIX-CORPORATION-2026-05-05.md frontmatter]
- TRM model LOCKED v1.0: 6-resource + L0-L5 ladder [F5 · R-high] [src: JETIX-TRM-MODEL-2026-04-30.md]
- Ruslan = физлицо Berlin; no GmbH/UG; no entity-incorporation.md [F4 · R-high] [src: 01-inventory §2 O-02]

**Что задумано:**
- GmbH/UG/Ltd инкорпорация + formal A.2.8 partner commitments [F2 · R-low]
- A.6.C Contract Unpacking applied (promise/utterance/commitment/work separation) [F2 · R-low]
- 3 engagement levels operational (Partners + Clients TRM + Workers salary) [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «Jetix Corp = applied use case Базовой Системы» | F3 (logical relationship; single doc grounding) | Refuted if Doc 1B revised to drop framing OR Base-Mgmt-System applied to different entity first |
| «TRM controls 6 resource classes» | F2 (only 2 of 6 tracked: capital + attention) | Refuted if resource tracking logs show <6 actually tracked |
| «Doc 1B = conceptual doc для partners/investors» | F5 (frontmatter explicit) | Refuted if Doc 1B cited as evidence of operational legal entity |

**Anti-scope:**
- NOT current operational entity (vapor; CE-3 trap)
- NOT active contracts today (revenue = 0)
- NOT the OS/software (→ O-01)
- NOT role-type taxonomy (→ O-06a)

**Conflation traps (phil):** (1) Concept-as-instance: Doc 1B exists ≠ corp exists. A.4 Temporal Duality. (2) Promise-as-commitment: TRM ladder = U.PromiseContent at best; no A.2.8 U.Commitment with adjudication path. (3) Present-tense language: Doc 1B §0 «Jetix is a meta-workshop» — present-tense use в concept-only document = use-mention slip.

**Hidden assumptions (phil):** Incorporation will happen on unspecified timeline (no falsifier). Doc 1B framing appropriate для L1 audience (not reviewed by L1). TRM LOCKED still current ICP (contradicted by ACTION-PLAN).

**Leverage point (systems, Meadows L9 Goals):** Goal shift «опишем corporation» → «registрируем legal entity» меняет всё system behavior. Это change цели, не параметра.

**Feedback loops (systems):**
- R: Corp concept clarity → partner trust → engagement → more clarity. Works only если partners receive Doc 1B.
- B: Vapor state → no legal commitments → no external accountability → vapor persists. Balancing decay loop.

**Cross-refs:**
- → O-10 (implements): TRM = commercial implementation
- → O-03 (refines): Corp concept is vision-derived
- → O-14 (targets): meta-workshop = Phase B+ corp form

**Boundary disputes (phil):**
- vs O-10: TRM is commercial implementation of corp concept. If TRM changes (ICP updated), does O-02 require revision?
- vs O-14: O-02 «today/near» vs O-14 «platform-for-others» — different horizons; sometimes cited interchangeably.

---

## §3 — O-03 — Jetix как задумка / vision (future state target)

**FPF primitive (eng):** U.WorkPlan (A.15.2) + U.MethodDescription (A.3.2)
**Phil alternative:** U.Episteme describing future U.System; LOCKED-as-artefact ≠ realised
**FPF Part hosting:** Part A Cluster A.III; Part 11 (Strategic Direction)
**Applicable FPF mechanisms:** A.4 Temporal Duality · A.15.2 WorkPlan · A.3.2 MethodDescription · E.9 DRR · B.5.1 Explore→Operate (state = «Explore»)
**VSM mapping (systems):** System 4 (intelligence/futures) — model of future environment

**Что есть:**
- FUNDAMENTAL LOCKED v1.0 (2026-04-27): 35 UC × 12 categories [F8 (artefact) · R-high]
- Two-layer arch: Layer 1 universal + Layer 2 Ruslan-specific [F5 · R-high]
- Part 11 hosts vision artefacts (6 strategic doc types + Decisions DB) [F5 · R-high]
- 8 RUSLAN-ACK; git-tagged «foundation-architecture-locked-2026-04-28» [F5 · R-high]

**Что задумано:**
- Vision realised в client-facing product (revenue = 0; B.5.1 «Explore») [F2 · R-low]
- 100-200 year marathon timeline (Clan §1.7) [F2 · unfalsifiable over horizon]
- FPF-grade intelligence amplification level [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «35 UC × 12 categories = complete vision encoding» | F4 («complete» unverified — UC-coverage asserted) | Refuted if domain-expert review finds missing UC OR Ruslan adds UC-36+ |
| «100-200 year ambition» | F2 (**unfalsifiable over 100y horizon — normative not predictive**) | Per Popper: not scientific claim about future; normative commitment. Different epistemic category. |
| «Part 11 correctly hosts vision» | F4 for hosting; F2 for «correctly» (Part 11 memory-dominant per audit §2.1; MVPK not enforced) | Refuted if Part 11 audit shows no multi-view publication enforced |

**Anti-scope:**
- NOT current operational reality (A.4 design ≠ run)
- NOT revenue OR commercial activity (revenue = 0)
- NOT FPF-grade claims (F2-F4 max; not verified)
- NOT the corporation as entity (→ O-02)
- NOT Ruslan-specific LAYER (Layer 2 separate)

**Conflation traps (phil):** (1) Lock-as-realised: «Foundation LOCKED» proximity creates illusion vision = realised. A.16 lock ≠ A.4 enactment. (2) Normative-as-predictive: 100-200y framing presents aspirations as predictions; different falsifiability structures.

**Hidden assumptions (phil):** Ruslan's ownership + commitment stable over multi-decade horizon (no succession articulated). FUNDAMENTAL Layer 1 sector-agnosticism unverified by alternative-domain stress-test.

**Leverage point (systems, Meadows L3 Goals):** Add explicit feedback loop от operations → vision revision cadence. Part 9 monthly strategic reflection = designed connector, не реализован (daily-log dir absent).

**Feedback loops (systems):**
- R: Vision LOCKED → Hexagon refines → vision more articulate. Works ONLY если Hexagon inputs from operational reality.
- B: Vision-to-reality gap (revenue = 0) → feedback loop disconnected. Balancing без sensor.

**Cross-refs:**
- → O-04 (targeted-by): working product = partial realization
- → O-09 (refined-by): Hexagon insights refine
- → O-12 (publication-of): brand = MVPK view

**Boundary disputes (phil):**
- vs O-04: gap = honest statement of O-03 realisation status. «Building toward» valid; «realised» needs evidence.
- vs O-09: H1-H7 generated 2026-05-10..12; FUNDAMENTAL LOCKED 2026-04-27. **Temporal order inverted** — vision predates insights. Whether insights «refine» vision OR constitute evidence for vision revision = unstated.

---

## §4 — O-04 — Jetix как работающий продукт (что РЕАЛЬНО работает СЕЙЧАС)

**FPF primitive (eng):** U.Work (A.15.1) + U.Capability (A.2.2)
**Phil alternative:** U.Work records + partial U.System (instantiation evidenced)
**FPF Part hosting:** Part A Cluster A.II–A.V; multiple Parts operational
**Applicable FPF mechanisms:** A.15.1 Work (Record of Occurrence) · A.2.2 Capability · B.3 F-G-R · A.10 Evidence Graph · A.2.5 RoleStateGraph
**VSM mapping (systems):** System 1 (operations) + System 3 (control/audit)

**Что есть:**
- Foundation v1.0 LOCKED (F8): 11 Parts + 8 RUSLAN-ACK; git-tagged [F8 (artefact) · R-high]
- ROY swarm dispatching: 15 Phase-B cell drafts [F4 · R-medium]
- Per audit §12: ~27 components; ~12 intelligence/FPF-derivative; ~15 memory+automation [F4 · R-high]
- 6 outreach files (2026-05-12..17); Tseren/Levenchuk в CRM [F4 · R-medium]
- **Revenue = 0 confirmed; no external deliverables** [F5 · R-high]

**Что задумано:**
- Phase B managed team + enterprise clients at TRM scale [F2 · R-low]
- Full FPF-grade intelligence (не «memory + automation» dominant) [F2 · R-low]
- Foundation enforcement operational (Halt-Log-Alert не STUB) [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «Foundation + ROY swarm + voice pipeline = working product» | F4 (3 different objects under one label) | Refuted if ROY swarm stops dispatching OR voice pipeline produces no outputs in 2 cycles |
| «~27 components; ~12 intelligence-bearing» | F4 (Ruslan-assessed, not independently validated) | Refuted if independent FPF audit reclassifies counts |
| «Revenue = 0» | F5 (verifiable observable) | Refuted immediately when first closed_won в CRM with invoice |

**Anti-scope:**
- NOT Phase B managed team (no team member besides Ruslan)
- NOT enterprise clients
- NOT TRM at scale (TRM = model O-10, not operational at any scale)
- NOT FPF-grade intelligence («memory + automation + ~25% structural + ~10% FPF-derivative»)

**Conflation traps (phil):** (1) **Internal-external conflation:** product exists internally (Foundation docs, cell drafts) but zero external commercial evidence. «Jetix works» needs internal/external distinction. (2) Substrate=product: Foundation = infrastructure for delivering, not what clients buy.

**Hidden assumptions (phil):** ROY swarm cycles producing drafts = «product delivery» (true for internal; not for external clients). 06-honest-self-audit §2 classification stable (Ruslan-assessed; epistemically suspect for self-assessment).

**Leverage point (systems, Meadows L5 Information flows):** Самый мощный рычаг — добавить **one external feedback loop** (first paying conversation). Не goal change, не structural — добавление feedback sensor в open-loop system.

**Feedback loops (systems):**
- R: Working product → stakeholder reads → feedback → swarm improves. **NOT closed: L1 feedback нет structured path back into swarm.**
- B: ROY cycles → drafts → brigadier gates → RUSLAN-ACK → quality floor. Balancing через AWAITING-APPROVAL.
- R: Internal artefact quality → Foundation compliance → higher F-G-R → confident external publishing. **Не closes externally пока revenue = 0.**

**Cross-refs:**
- → O-07 (built-on)
- → O-01 (runs-on)
- → O-09 (produces Hexagon insights)
- → O-10 (commercialised-by)

**Boundary disputes (phil):**
- vs O-07: Foundation Parts 1/3/5/9/11 memory-dominant. «Foundation constitutes working product» needs per-Part qualification.
- vs O-01: substrate (O-01) ≠ outputs (O-04). Working system ≠ working outputs; distinction collapsed в Phase B prose.

---

## §5 — O-05 — Jetix как методология / pattern language (forkable)

**FPF primitive (eng):** U.MethodDescription (A.3.2) + U.Method (A.3.1)
**Phil alternative:** U.Episteme of methodology + recipe-frame (NOT itself U.Method — the doing)
**FPF Part hosting:** Part A Cluster A.II (Transformation Engine)
**Applicable FPF mechanisms:** A.3.2 MethodDescription · A.3.1 Method (not yet instantiated beyond Ruslan) · A.5 Kernel Modularity · A.8 Universal Core · B.4 Canonical Evolution Loop
**VSM mapping (systems):** System 4 (intelligence/futures) — codified intelligence; HOW to instantiate Jetix elsewhere

**Что есть:**
- FUNDAMENTAL Layer 1 (sector-agnostic) LOCKED v1.0 [F5 · R-high]
- Fork guide v0 (§11 working file): 6-step minimal viable instance [F2 · R-low]
- Two-layer architecture (FUNDAMENTAL + RUSLAN-LAYER overlay) [F4 · R-medium]

**Что задумано:**
- Distributed Jetix-as-Pack format — Phase C remit [F2 · R-low]
- First external forker instantiates methodology [F2 · R-low]
- Cooperation Plan Tier 3 activation enables distribution [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «FUNDAMENTAL Layer 1 = sector-agnostic pattern» | F2 (sector-agnosticism non-testable — only 1 instance) | Refuted if first external fork requires significant domain-specific modifications |
| «Fork guide v0 (6 steps) enables instantiation» | F2 (6-step outline ≠ engineering «guide»; U.WorkPlan, не U.Method) | Refuted if first attempt fails без additional guidance |
| «Phase C remit для distribution» | F2 (unfalsifiable as stated — Phase C undefined) | Unfalsifiable: «Phase C» has no defined start condition |

**Anti-scope:**
- NOT distributable format today (vapor; no forkers)
- NOT specific Jetix instance (→ O-01)
- NOT IWE Pack (different unit: IWE = single intellectual worker; Jetix = multi-agent business OS)
- NOT Phase C activations (no cooperation plan finalised)

**Conflation traps (phil):** (1) Existence-by-description: detailed methodology description ≠ tested method. A.4 description ≠ enactment. (2) Unique-because-described: «forkable + sector-agnostic» = design intentions, not verified properties.

**Hidden assumptions (phil):** Market exists для fork-and-instantiate pattern adoption (zero market validation). FUNDAMENTAL Layer 1 achieves sector-agnostic status by design intent (no stress-test). Phase C activates до methodology obsolescence.

**Leverage point (systems, Meadows L4 Self-organisation):** Первый fork = точка где методология самоорганизуется через real users. Fork guide v0 = initiation tool. До первого fork = theory.

**Feedback loops (systems):**
- R: Methodology articulation → forkable → first fork → real-world feedback → improves. **Not closed: no first forker.**
- B: Complexity → higher fork barrier → fewer forkers → less simplification pressure → complexity persists.

**Cross-refs:**
- → O-14 (enables): methodology → meta-workshop partner instantiation
- → O-03 (derived-from): vision-derived
- → O-12 (distinct-from): brand ≠ methodology (conflation trap)

**Boundary disputes (phil):**
- vs O-03: O-05 effectively sub-claim of O-03 vision (35 UC includes pattern-language aspiration). Separation operational but epistemic dependence undeclared.
- vs O-14: O-14 vapor → O-05 forkable vapor (cascade dependency).

---

## §6 — O-06a — Jetix-as-12-role-types (type-level, IP-1 split A)

**FPF primitive (eng):** U.Role set (A.2 type-level)
**Phil:** 12 × U.Role per A.2; type-level abstract functional assignments
**FPF Part hosting:** Part A Cluster A.I; Part 4 Role Taxonomy
**Applicable FPF mechanisms:** A.2 Role Taxonomy · A.2.7 RoleAlgebra · A.13 Agential Role · IP-1 Role≠Executor
**VSM mapping (systems):** System 3 (control/audit) — taxonomy = org control structure

**Что есть:**
- 12 role-type declarations в CLAUDE.md (Phase 1: 4 active; Phase 2-4: 8 planned) [F5 · R-high]
- Part 4 LOCKED F8 (FPF A.2 derivative) [F5 · R-high]
- 6 department groupings (MGMT/OPS/Sales/Brain/Life/Meta) = RoleAlgebra topology [F4 · R-medium]
- **Phase 3-4 roles = declared без confirmed operational executor bindings** [F4 · R-high]

**Что задумано:**
- Phase 3-4 roles operationalised (executor bindings + mailboxes active) [F2 · R-low]
- Method-signature enforcement per A.15 для всех 12 [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «12 role-types declared в roster» | F5 (verifiable from CLAUDE.md) | Refuted if row count changes without AWAITING-APPROVAL |
| «Phase 1: 4 active» | F5 (Phase column explicit) | Refuted if Phase 2-4 dispatched без Phase promotion |
| «12 U.Role declarations satisfy A.2» | **F3** (A.2 requires method-signature, not just name+model+department; enforcement = STUB) | Refuted if any role missing A.2.7 RoleAlgebra position OR A.13 autonomy budget |

**Anti-scope:**
- NOT executor instances (→ O-06b; IP-1 split)
- NOT running processes
- NOT ROY swarm (= separate executor binding set distinct from legacy 12 roster)
- NOT evidence of operational capability (type-declarations без bindings = no operational evidence)

**Conflation traps (phil):** (1) **CE-2 IP-1 core conflation persists.** ROY swarm = 6 dispatching roles; legacy 12 stale. Neither = 12 running processes. (2) Type-completeness: 12 declared ≠ covers all needed functions; «completeness» asserted без coverage criterion. (3) Phase-implies-active: Phase 1 roles в roster ≠ continuous running (manager mailbox stale since 2026-04-15).

**Hidden assumptions (phil):** CLAUDE.md §Agent Roster = authoritative (vs ROY swarm в .claude/agents/; canonical roster ambiguous). «4 Phase-1 active» = meaningful operational claim (if mailboxes stale, «active» = «declared», not «receiving dispatches»).

**Leverage point (systems, Meadows L7 Rules):** IP-1 rule (Role≠Executor) уже применено = leverage реализован. Без IP-1 все 12 conflated; с IP-1 = role-types autonomous from executor instances.

**Feedback loops (systems):**
- B: Declarations → executor binding attempts → capability gaps discovered → revision OR deferral. Reality constrains aspiration.
- R: Phase-1 operational → trust в approach → more activations.

**Cross-refs:**
- → O-06b (instantiated-by): tokens instantiate types
- → O-07 (governed-by): Part 4 + Pillar C
- → O-01 (part-of): roles constitute holonic structure

**Boundary disputes (phil):**
- vs O-06b: IP-1 boundary declared but not consistently applied в prose. Working file §4 mermaid shows «12 Specialized Agents × 6 Departments» as unified block, not split.
- vs O-07: Part 4 method-signature enforcement = STUB → governance declared but not enforced. O-07 → O-06a edge asymmetric: architectural F5, operational F2.

---

## §7 — O-06b — Jetix-as-executor-bindings (token-level, IP-1 split B)

**FPF primitive (eng):** U.RoleAssignment (A.2.1)
**Phil:** U.RoleAssignment tokens (Holder#Role:Context per A.2.1) — contextual enactments, NOT permanent
**FPF Part hosting:** Part A Cluster A.I; RUSLAN-LAYER executor-binding.yaml
**Applicable FPF mechanisms:** A.2.1 RoleAssignment · A.13 Agential Role · A.2.5 RoleStateGraph · RUSLAN-LAYER executor-binding.yaml.template
**VSM mapping (systems):** System 1 (operations) — ROY swarm = currently active System 1

**Что есть:**
- ROY swarm (brigadier + 5 ROY experts): 15 Phase-B dispatches [F4 · R-medium]
- RUSLAN-LAYER executor-binding.yaml.template present (maps role → model) [F4 · R-medium]
- **Legacy 12 mailboxes stale: last 2026-04-15** [F4 · R-high]
- 23 `.claude/agents/` files (ROY + legacy hybrid) [F4 · R-medium]

**Что задумано:**
- Legacy roster deprecated OR reactivated + boundaries documented (OQ-9) [F2 · R-low]
- All 12 role-type bindings active + documented [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «ROY swarm actively dispatching» | F4 (15 dispatches; «actively» implies cadence) | Refuted if no new ROY dispatch in next 2 work sessions |
| «Legacy 12 mailboxes = stale» | **F3** (necessary не sufficient; direct dispatch without trace possible per D-mgmt-2) | Refuted if session transcript shows legacy invoked via direct dispatch без mailbox record |
| «RUSLAN-LAYER template governs bindings» | F4 (template LOCKED; application to all current bindings unverified) | Refuted if any .claude/agents/*.md binds executor без template fields |

**Anti-scope:**
- NOT role-type declarations (→ O-06a)
- NOT chat history / session memory (those = scratchpad in 5-layer arch)
- NOT persistence across sessions (each binding context-scoped)
- NOT «12 legacy agents» as actively operational (stale + D-mgmt-2 dissent)

**Conflation traps (phil):** (1) **Persistence assumption:** executor bindings described as if persistent actors. A.2.1 Holder#Role:Context = session-scoped enactment. (2) ROY swarm = «the agents»: implicit migration — «agents of Jetix» now = ROY swarm, not declared 12. **Migration NOT explicitly documented в CLAUDE.md.**

**Hidden assumptions (phil):** ROY swarm covers functional responsibilities of legacy 12 (NOT verified: knowledge-synth, life-coach, meta-agent no ROY equivalent). Stale mailbox = inactive (D-mgmt-2 dissent: direct dispatch без trace possible).

**Leverage point (systems, Meadows L7 Rules):** Dispatching rules (brigadier's decomposition logic) = leverage point. ROY swarm vs legacy 12 = already applied leverage.

**Feedback loops (systems):**
- R: ROY dispatches → quality artefacts → confidence → more dispatches → swarm «experience» via strategies.md
- B: Legacy mailboxes stale → if dispatched directly → stale context → degraded output → fewer dispatches → mailboxes remain stale
- R: RUSLAN-LAYER bindings → better alignment → fewer constitutional violations → larger dispatch budget

**Cross-refs:**
- → O-06a (instantiates types)
- → O-01 (operates-on substrate)
- → O-04 (produces working product artefacts)

**Boundary disputes (phil):**
- vs O-06a: IP-1 boundary not consistently applied; working file §4 mermaid shows unified block.
- vs O-01: ROY covers only partial O-06a roster → O-01's «12 role-types» overstates operational coverage.

---

## §8 — O-07 — Foundation Architecture v1.0 (organisational substrate F8-LOCKED)

**FPF primitive (eng):** U.System (A.1) + U.Mechanism (A.6.1) **[D-2 DISPUTED]**
**Phil counter:** U.Episteme (LOCKED documents) describing intended U.System; NOT proof of operational instantiation per A.4 Temporal Duality
**Phil resolution (extended):** **BOTH faces simultaneously — U.Episteme for spec-only Parts; U.Work-evidenced for 4 FPF-derivative Parts. NOT binary.**
**FPF Part hosting:** Part A + Part E Constitution
**Applicable FPF mechanisms:** A.1 Holon · A.6.1 Mechanism · A.6.B Boundary Norm Square · E.5 Guard-Rails · B.3 F-G-R · A.16 Language-State (LOCKED = artefact state)
**VSM mapping (systems):** System 3 (audit/control) + System 2 (coordination)

**Что есть:**
- 11 Parts + Pillar A + Pillar C LOCKED 2026-04-28: git-tag + 8 RUSLAN-ACK [F8 (artefact) · R-high]
- 4 of 11 Parts FPF-derivative operational: Part 4 + 6a + 6b + Pillar C [F4 · R-high]
- 7 of 11 Parts = memory+automation dominant (substrate); abductive loop NOT operational [F4 · R-high]
- **Halt-Log-Alert mechanism described в Part 6b; runtime enforcement = STUB Phase-B** [F4 · R-high]

**Что задумано:**
- Runtime enforcement operational (≤1s / ≤5s / ≤60s per F8/F4/F2) [F2 · R-low]
- All 11 Parts FPF-derivative; abductive loop per B.5.2 [F2 · R-low]
- Claim Register operational beyond LOCKED artefacts [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «Foundation v1.0 LOCKED = F8 grade» | F8 only for **document-formality** («locked via 8 RUSLAN-ACK») — NOT FPF B.3 standard F8 («independently tested 8 times») | Refuted as artefact-lock if Part modified without AWAITING-APPROVAL |
| «11 Parts + Pillars constitute the organisational substrate» | **F3 for «constitute» (operational claim)** — 7 Parts memory/automation; only 4 FPF-derivative operational | Refuted if operational audit shows zero enforcement evidence for Parts 1/3/5/9/11 beyond static storage |
| «Halt-Log-Alert F8 ≤1s» | **F2 for operational claim (STUB Phase-B)**; spec = F5 | Refuted as operational if any F8 violation committed and no halt fires within 1s |

**Anti-scope:**
- NOT proof all 11 Parts operational (Parts 1/3/5/9/11 memory-dominant)
- NOT FPF-compliance certification («tactical FPF adoption, not full FPF-grade» per working file §6.1)
- NOT Halt-Log-Alert as operational enforcement (STUB)
- NOT the operational substrate itself (→ O-01; Foundation specifies O-01, не is O-01)
- NOT Pillar C alone (→ O-08; treated separately due to constitutional weight)

**Conflation traps (phil):** (1) **Artefact-F8 vs claim-F8:** Jetix F8 = approval-grade (single-reviewer Ruslan), not B.3 proof-grade. Calling Foundation «F8» без disambiguation misleads external audiences. (2) D-2 unresolved typing dispute propagates downstream. (3) **All-Parts-equal:** «11 Parts LOCKED» implies equal status. Parts differ radically — Part 6b enforcement F5 operational vs Part 9 owner interaction (no daily-log/ dir exists).

**Hidden assumptions (phil):** 8 RUSLAN-ACK = «extensive review» but all from ONE reviewer reviewing own system. **No external reviewer.** Foundation v1.0 = current authoritative spec (Phase B outputs may implicitly extend без formal Part update).

**Leverage point (systems, Meadows L4 Self-organisation):** Enable Foundation to self-describe operational state (currently F8 artefact; F2-F4 operational). Live operational health signal = L4/L5 leverage; Foundation self-monitors.

**Feedback loops (systems):**
- B: LOCKED → AWAITING-APPROVAL gates → violations flagged → Halt-Log-Alert (spec) → corrected. **STUB enforcement → loop exists в spec, не fully operational.**
- R: Quality → discipline → artefact quality → trust → more investment
- B: Complexity → harder maintenance → violations → erodes trust → revisions

**Cross-refs:**
- → O-01 (constitutes specification)
- → O-08 (contains Pillar C sub-system)
- → O-04 (governs working product)
- → O-06a (governs roles)

**Boundary disputes (phil):**
- vs O-08: Pillar C is part of Foundation v1.0 LOCKED; «Foundation → Pillar C constrains» = circular reference (Pillar C is part of Foundation that Pillar C governs). Unproblematic в practice; muddies ontology.
- vs O-04: Foundation LOCKED AFTER O-04 operations running. **Temporal order inverted** relative to «Foundation constitutes product» narrative.

---

## §9 — O-08 — Pillar C конституциональная система (12 Tier-2 rules)

**FPF primitive (eng):** U.Commitment (A.2.8) + Guard-Rails analog (E.5)
**Phil:** **THREE distinct sub-objects:** (a) rule text U.Episteme; (b) U.Commitment in applied form; (c) machine-enforcement subset — enforceability NOT uniform
**FPF Part hosting:** Part E — Constitution analog
**Applicable FPF mechanisms:** A.2.8 Commitment · E.5 Guard-Rails · A.6.B Boundary Norm Square · B.3 F-G-R
**VSM mapping (systems):** System 5 (identity/policy) — highest normative layer

**Que есть:**
- 12 Tier-2 rules text LOCKED в CLAUDE.md §4.1 + principles/tier-2-system/foundation-generic/ [F8 (text) · R-high]
- Default-Deny table (11 entries) PRESENT: Rule 11 machine-enforced [F5 · R-high]
- R12 additive 2026-05-12: text LOCKED; AWAITING-APPROVAL packet written [F5 · R-high]
- Halt-Log-Alert per Part 6b §I.2 specified; runtime = STUB [F4 · R-medium]

**Что задумано:**
- Machine-enforcement для Rules 1/3/8/9/12 (currently human-review only) [F2 · R-low]
- R12 promoted from AWAITING-APPROVAL to full Tier-2 LOCKED + mechanism [F2 · R-low]
- Fork-and-leave infrastructure evidenced [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «12 hard rules = Tier 2 Constitutional» | F8 для text-lock; **F2 для «constitutional» = uniformly enforced** | Refuted as «12 uniformly enforced» if any Rule 1/3/8/9/12 violation commits without halt fires |
| «Default-Deny (11 entries) = machine-enforced» | F5 | Refuted if novel action class NOT in table proceeds без deny-and-escalate. Test: unlisted action class. |
| «R12 = constitutional Tier 2» | F3 для full constitutional status (text LOCKED but AWAITING-APPROVAL packet not yet ack'd; mechanism = none) | Refuted as «ack'd» if AWAITING-APPROVAL remains beyond current cycle |

**Anti-scope:**
- NOT Tier 1 owner principles
- NOT machine-enforcement для Rules 1/3/8/9/12
- NOT formal U.Commitment objects (A.2.8) для всех 12 (only Rule 11)
- NOT R12 ack'd (AWAITING-APPROVAL pending)

**Conflation traps (phil):** (1) **CE-4 text=enforcement:** 3 sub-categories (machine / human-review / no-mechanism) identified но not visibly separated в CLAUDE.md §4.1. Uniform «constitutional» heading masks stratification. (2) Rule-count as capability signal: «12 constitutional rules» = count of MENTIONED obligations, not EFFECTIVE constraints. Levenchuk's C3 critique applies. (3) **R12 4-source trail = ack'd:** 4-source trail ≠ ack'd. Citing R12 «LOCKED» alongside Rules 1-11 conflates pending-ack with ack'd.

**Hidden assumptions (phil):** Ruslan's human review of Rules 1/3/8/9 reliably performed every session (no audit trail; single-point-of-failure). Default-Deny 11 entries exhaustive для current novel-action classes (no table-maintenance process specified).

**Leverage point (systems, Meadows L2 Goals — paradigm constraints):** Pillar C = paradigm-level constraints on what system can pursue. Каждое rule = goal constraint. R12 = paradigm-level leverage — меняет WHO benefits.

**Feedback loops (systems):**
- B: Rules → constrain agent actions → prevent violations → system integrity. **Enforcement asymmetry: Rule 11 machine; Rules 1/3/8/9/12 human-review.**
- R: RUSLAN-ACK strengthens legitimacy → constitutional vs guideline → better compliance

**Cross-refs:**
- → O-07 (constrains all Foundation writes)
- → O-11 (R12 = additive extension)
- → O-01 (applies-to all substrate actions)

**Boundary disputes (phil):**
- vs O-11: R12 declared part of O-08 AND given separate entry. EP-4 pattern: «R12 as rule-in-O-08» vs «R12 as separate-architectural-meta-property-O-11».
- vs O-07: «Pillar C constrains Foundation» needs per-rule qualification (partial constraint due to enforcement asymmetry).

---

## §10 — O-09 — Strategic Insights Hexagon (synthesis cadence 6+1)

**FPF primitive (eng):** U.Work (A.15.1) + Abductive Loop output (B.5.2)
**Phil:** U.Episteme cluster (6+1 LOCKED insights) + Abductive Loop-adjacent process (NOT full NQD-CAL)
**FPF Part hosting:** Part B (Reasoning); Part 11 (Strategic Direction)
**Applicable FPF mechanisms:** B.5.2 Abductive Loop · E.9 DRR · B.3 F-G-R · E.17 MVPK partial (1A + 1B) · A.10 Evidence Graph
**VSM mapping (systems):** System 4 (intelligence/futures) — strongest intelligence loop в Jetix

**Что есть:**
- 6 LOCKED strategic insights (H1-H7 range; 2026-05-10..12); F-G-R tagged [F5 · R-high]
- **Closest к FPF intelligence amplification per audit §7** [F4 · R-high]
- H7 People-NS LOCKED с 4-source attribution trail (R12 origin) [F5 · R-high]
- 29 D-Lock entries в Decisions DB (Part 11 host) [F5 · R-high]

**Что задумано:**
- Formal B.5.2 NQD-CAL enforcement (alternatives portfolio per insight) [F2 · R-low]
- Systematized weekly cadence (Part 9 daily-log materialization) [F2 · R-low]
- F-G-R level advancement через operational evidence [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «Hexagon = closest к FPF intelligence amplification в Jetix» | F4 (comparative within Jetix; не against FPF bar) | Refuted if independent FPF reviewer classifies другой Jetix component as closer to B.5.2 |
| «6 INSIGHT files = Hexagon synthesis output» | F5 (files exist, LOCKED, F-G-R tagged) BUT «Hexagon» implies structured 6-cell process не documented | Refuted if 6 insights were NOT produced by structured abductive process (no alternatives-portfolio evidence) |
| «B.5.2 Abductive Loop partial implementation» | **F3 («partial» honest but imprecise — abductive requires explicit alternatives-portfolio, not first-answer)** | Refuted if Hexagon logs show alternatives explicitly generated and discarded |

**Anti-scope:**
- NOT formal NQD-CAL alternatives portfolio
- NOT full E.17 MVPK bundle (1A + 1B = informal; no ViewpointBundle definition)
- NOT systematized weekly cadence (3-day generation window for 6 ≠ sustained weekly)
- NOT B.5.2 full Abductive Loop implementation

**Conflation traps (phil):** (1) **Output=process:** 6 LOCKED outputs ≠ formal Abductive Loop process. Output quality ≠ process quality. (2) Proximity-implies-equivalence: «Closest to FPF» ≠ «equivalent to FPF». Comparison relative within Jetix. (3) **Hexagon-as-system:** «Cadence» implies ongoing repetition; one 3-day generation event ≠ cadence.

**Hidden assumptions (phil):** 6 insights в 2026-05-10..12 represent **reproducible** synthesis pattern (ONE data point insufficient для «cadence» claim). F-G-R tagging = intelligence amplification (tagging is provenance discipline, not abductive intelligence work).

**Leverage point (systems, Meadows L5 Information flows):** Добавить structured feedback channel from operational results → Hexagon cadence. Без этого: Hexagon cycles on own outputs (echo chamber risk). With: genuinely adaptive intelligence layer.

**Feedback loops (systems):**
- R: Insights → dispatches → operational results → new insight material → more synthesis. **Strongest intelligence loop в Jetix.**
- B: Insights без operational test → unvalidated → F-G-R stays F4-F5 → can't advance
- R: F-G-R tagging → honest state → accurate adjustment → stronger epistemic culture

**Cross-refs:**
- → O-03 (refines)
- → O-11 (H7 originated R12)
- → O-01 (draws from wiki/knowledge stores)

**Boundary disputes (phil):**
- vs O-03: H1-H7 (2026-05-10..12) AFTER FUNDAMENTAL (2026-04-27). «Refinement» valid only if insights incorporated via AWAITING-APPROVAL. If not, parallel claims без formal reconciliation.
- vs O-11: «R12 originated from H7» = F4 claim (4-source trail documents provenance, не formally proves origination).

---

## §11 — O-10 — Бизнес-модель Phase 1 (TRM / quick-money consulting)

**FPF primitive (eng):** U.PromiseContent (A.2.3) + U.RoleAssignment (A.2.1)
**Phil:** U.WorkPlan + U.PromiseContent; A.2.8 Commitment не unpacked (informal)
**FPF Part hosting:** Part A Cluster A.I
**Applicable FPF mechanisms:** A.2.3 PromiseContent · A.2.8 Commitment · A.6.C Contract Unpacking · B.1.6 Γ_work
**VSM mapping (systems):** System 1 (operations) — external-facing operational loop

**Что есть:**
- TRM model LOCKED v1.0: 6 resource classes + L0-L5 ladder (€3K→€40-60K/мес) [F5 · R-high]
- ICP переопределён в ACTION-PLAN: «Mittelstand DACH ABANDONED → Online-first» [F4 · R-high]
- **Doc 1B §7 НЕ обновлён** (Mittelstand DACH остаётся) [F5 · R-high — LIVE INCONSISTENCY]
- **Revenue = 0** [F5 · R-high]
- Critical path Tseren/Levenchuk = «24-48h critical» 7 дней назад [F4 · R-high]

**Что задумано:**
- First paying client; L0-L5 ladder activation [F2 · R-low]
- A.6.C Contract Unpacking applied [F2 · R-low]
- €100M ARR в 3 года [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «TRM 6-resource model = business model» | **F3** (TRM = U.PromiseContent face only; business model requires also revenue logic + acquisition path + delivery mechanism) | Refuted if TRM replaced by different taxonomy в revised locked doc |
| «ICP = Online-first» | **F2 (LIVE INCONSISTENCY: Doc 1B = Mittelstand; ACTION-PLAN = Online-first)** | Refuted as «consistent ICP» — Doc 1B §7 vs ACTION-PLAN §0 contradiction observable today |
| «L0-L5 = activation path» | **F2** (L0 = first client at any fee; revenue = 0; ladder = U.WorkPlan not U.Work record) | Refuted as activation path if L0 not achieved within N months (no falsifier deadline) |

**Anti-scope:**
- NOT active contracts (revenue = 0; no closed_won)
- NOT consistent ICP (live flag)
- NOT TRM at scale (L0 not achieved)
- NOT 6 resource tracking operational (only 2 of 6 mechanized: attention ≤20 tasks + capital €10/day)

**Conflation traps (phil):** (1) Model=implementation: TRM LOCKED ≠ TRM being implemented. A.4 model ≠ enacted method. (2) **ICP inconsistency invisible cross-document:** Each doc internally consistent; inconsistency only visible cross-document. **Will surface when pitching to prospects.**

**Hidden assumptions (phil):** TRM LOCKED v1.0 = still current ICP (contradicted by ACTION-PLAN). Mgmt + performance fee acceptable to ICP segment без testing.

**Leverage point (systems, Meadows L6 Information flows):** **Немедленный рычаг — fix ICP inconsistency** (Doc 1B §7 update to align с ACTION-PLAN). Не structural change — information correction в ONE document.

**Feedback loops (systems):**
- R: TRM engagement → value delivery → client pays → reinvest → more engagements. **NOT closed: revenue = 0.**
- B: ICP inconsistency → confused positioning → missed outreach → no clients. Balancing through positioning confusion.
- R: Tseren/Levenchuk partnership → warm intro → credibility → first conversation. **Only near-term path to closing Loop 1.**

**Cross-refs:**
- → O-02 (requires): formal contracts → legal entity
- → O-04 (commercialises)
- → O-12 (positioned-by brand)

**Boundary disputes (phil):**
- vs O-02: TRM is commercial implementation of corp concept; dependency direction unstated.
- vs O-12: brand positioning + business model overlap unclear.

---

## §12 — O-11 — R12 Anti-extraction (конституциональный принцип)

**FPF primitive (eng):** U.Commitment (A.2.8) + U.SpeechAct (A.2.9)
**Phil:** **THREE distinct objects:** (a) Pillar C rule text U.Episteme; (b) U.Commitment in specific relationship; (c) architectural meta-property (ClaimScope = all substrate-member relationships) — different F-G-R per face
**FPF Part hosting:** Part E — Constitution (additive Pillar C)
**Applicable FPF mechanisms:** A.2.8 Commitment · A.2.9 SpeechAct · E.5 Guard-Rails · B.3 F-G-R · E.9 DRR (4-source trail = DRR shape)
**VSM mapping (systems):** System 5 (identity/policy) — defines relationship system ↔ members

**Что есть:**
- Tier 2 rule 12 additive 2026-05-12 [F5 (text) · R-high]
- 4-source attribution trail: H7 People-NS + Game Theory M-C + Q2 ack + AWAITING-APPROVAL packet [F5 · R-high]
- Symmetric application declared (Jetix↔members + members↔members + Jetix↔FPF/IWE) [F4 · R-medium]
- **«Meadows Level 2 leverage» (paradigm-level system goal change)** [F4 · R-medium]

**Что задумано:**
- R12 packet Ruslan ack [F2 · R-low]
- Fork-and-leave technical infrastructure sketch [F2 · R-low]
- R12 surface к FPF community (OQ-12 strategic) [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «R12 = constitutional Tier 2 rule» | F5 для text; F2 для enforcement | Refuted as constitutional if AWAITING-APPROVAL not ack'd within cycle |
| «4-source attribution trail» | F5 (sources verifiable) | Refuted if any source link broken or contested |
| «Symmetric application across all substrate relationships» | **F2** (no enforcement mechanism described; «applies symmetrically» = declaration не proof) | Refuted if R12 violation occurs in any substrate-member relationship без halt |

**Anti-scope:**
- NOT bilateral written agreement (Tier 3 prerequisite missing)
- NOT technical fork-and-leave infrastructure evidenced
- NOT formal Game Theory mechanism proof
- NOT IWE/FPF community agreement
- NOT R12 enforcement mechanism (vapor)

**Conflation traps (phil):** (1) **THREE-faces conflation** — Pillar C rule text / applied U.Commitment / architectural meta-property collapsed. Each needs own F-G-R triple. (2) Text-LOCKED ≠ enforcement evidence. (3) «Unique vs IWE» = negative comparison, not proof of operational superiority.

**Hidden assumptions (phil):** Symmetric application possible с current infrastructure (zero evidence of enforcement). Game Theory M-C mechanism applicable to Jetix (referenced not proved).

**Leverage point (systems, Meadows L2 — paradigm constraint):** Highest achievable leverage через principle declaration. **System goal constraint: cannot extract beyond agreed share.**

**Feedback loops (systems):**
- B: R12 commitment → constrains extraction → maintains member trust → members stay engaged
- R: R12 declared → Clan/partner trust → ecosystem members → value created → R12 viable (value shared)

**Cross-refs:**
- → O-08 (extends Pillar C)
- → O-13 (governs Clan members)
- → O-09 (originates from H7)

**Boundary disputes (phil):**
- vs O-08: R12 as rule-in-O-08 vs R12 as separate architectural-meta-property-O-11. **EP-4 pattern here.**

---

## §13 — O-12 — Бренд / публичный слой (Jetix public-facing)

**FPF primitive (eng):** U.PromiseContent (A.2.3) + MVPK face (E.17 partial)
**Phil:** E.17 MVPK candidate (1A/1B two-view); **Workshop = frame не structural anchor без A.1.1 (D-PHIL-SCOPE-2 dissent)**
**FPF Part hosting:** Part E + Part A
**Applicable FPF mechanisms:** E.17 MVPK · A.6.3 EpistemicViewing · A.2.3 PromiseContent · A.7 Strict Distinction (use-mention)
**VSM mapping (systems):** System 4 (env modeling) partial + System 1 (outreach)

**Что есть:**
- Doc 1A (Base Mgmt System charter) + Doc 1B (Corp narrative) LOCKED [F5 · R-high]
- Workshop metaphor LOCKED v1.0 [F5 · R-high]
- 6 outreach files written (2026-05-12..17) [F4 · R-medium]

**Что задумано:**
- Public website [F2 · R-low]
- Enterprise pitch deck [F2 · R-low]
- Full multi-audience MVPK bundles (Phase B) [F2 · R-low]
- A.1.1 BoundedContext formalisation для Workshop (if Ruslan decides OQ-4) [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «Doc 1A + 1B = E.17 MVPK two-view publication» | F4 (two-view structure present) | Refuted if no formal ViewpointBundle declaration |
| «Workshop metaphor = architectural anchor» | **F4 (D-PHIL-SCOPE-2 — needs A.1.1 formalisation)** | Refuted if doc lacks explicit A.1.1 fields (glossary + invariants + scope) |
| «Brand = public-facing layer of Jetix» | F4 | Refuted if no external audience interaction evidenced |

**Anti-scope:**
- NOT public website
- NOT enterprise pitch deck
- NOT full MVPK bundles (Phase B)
- NOT Workshop as formal U.BoundedContext (D-PHIL-SCOPE-2)

**Conflation traps (phil):** (1) **UM-1 use-mention drift:** Workshop одновременно USE (architectural anchor) + MENTION (named conceptual frame). «Owner = мастер; agents = instrumental specialists» — promotion metaphor → use без declaration. (2) Brand monologue: 6 outreach files written, **send confirmations absent**.

**Hidden assumptions (phil):** «Мастерская» metaphor resonates с L1 audience (not tested). External audience exists для Workshop framing.

**Leverage point (systems, Meadows L6 Information flows):** Создать structured feedback capture от внешних разговоров → brand revision. **Сейчас brand monologue; с capture loop = brand dialogue.** Part 10 External Touchpoints designed для этого.

**Feedback loops (systems):**
- R: Brand articulation → external conversations → feedback → Doc 1A/1B revision. **Loop в design; operational status uncertain.**
- B: Workshop без A.1.1 → audiences interpret differently → confused positioning → reduced conversion → pressure to formalize.

**Cross-refs:**
- → O-03 (publication-of)
- → O-10 (positions TRM)
- → O-19 (implemented-by 6 outreach files)

**Boundary disputes (phil):**
- vs O-05: brand ≠ methodology layer (conflation trap available)

---

## §14 — O-13 — People-Network-State / Clan vision (сетевой паттерн)

**FPF primitive (eng):** U.System (A.1 meta-holon) + Meta-Holon Transition (B.2)
**Phil:** Vapor as realised system (0 signatories); U.Episteme of charter; U.WorkPlan для activation
**FPF Part hosting:** Part B — Reasoning (B.2 MHT)
**Applicable FPF mechanisms:** B.2 Meta-Holon Transition · B.2.1 BOSC Triggers · A.1 Holon · A.2.7 RoleAlgebra (6 archetypes ⊗) · R12 constitutional guarantee
**VSM mapping (systems):** System 5 (identity/policy) — vapor instantiation

**Что есть:**
- H7 People-Network-State LOCKED (2026-05-12) [F5 · R-high]
- Clan Charter v0 LOCKED 2026-05-12 [F5 (text) · R-high]
- 6 archetypes declared (Hunter / Guardian / Scholar / Creator / Architect / Merchant) [F5 · R-high]
- Stealth launch declared [F4 · R-medium]
- **0 signatories confirmed** [F5 · R-high]

**Что задумано:**
- First signatory acquisition (probably из Levenchuk/Tseren network) [F2 · R-low]
- 5+ signatories; cooperative formation [F2 · R-low]
- Public launch (post 5 signatories) [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «Clan v0 LOCKED 100-200y» | F5 для text-lock; F2 для timeline ambition | Refuted if signatory acquisition fails OR Ruslan revokes charter |
| «6 archetypes = role bundle set (A.2.7 ⊗)» | F4 (archetypes declared; ⊗ operator structural claim) | Refuted if archetype names changed OR ⊗ relationship not documented |
| «Stealth launch» | F4 | Refuted if visible public launch attempts predate first signatory |

**Anti-scope:**
- NOT 5+ signatories today
- NOT public phase
- NOT cooperative formation
- NOT legal entity for Clan

**Conflation traps (phil):** (1) Charter-existence = community-existence (text LOCKED ≠ social entity). (2) «Network state» term collapses Balaji NS pattern (technical) с Clan (informal community) — different patterns.

**Hidden assumptions (phil):** Charter будет acceptable to first signatories (not tested). R12 anti-extraction = sufficient trust foundation для membership.

**Leverage point (systems, Meadows L10 Paradigm):** Clan vision = paradigm-level commitment («professional network grounded in mutual non-extraction»). До первой подписи = paradigm stated; после = paradigm enacted.

**Feedback loops (systems):**
- R: Charter LOCKED → first signatory → engagement → validates → attracts more. **NOT closed: 0 signatories.**
- B: R12 protection → reduces lock-in fear → more willing to join
- R: More members → cross-pollination → richer patterns → more attractive. **Network effect; requires critical mass.**

**Cross-refs:**
- → O-11 (governed-by R12)
- → O-14 (hosted-by meta-workshop)
- → O-05 (members can-fork methodology)

**Boundary disputes (phil):**
- Clan vs Network State (Balaji): different patterns conflated potentially

---

## §15 — O-14 — Meta-workshop для профессиональных мастеров (Phase B target)

**FPF primitive (eng):** U.System (A.1 supersystem) + U.Method (A.3.1 hosting)
**Phil:** Vapor; A.1 supersystem holon hosting partner-methods; B.2 MHT (system emergence event)
**FPF Part hosting:** Part A Cluster A.II + B.2 MHT
**Applicable FPF mechanisms:** A.1 Holon (meta-level) · A.3.1 Method · A.5 Kernel Modularity · B.2.2 MST
**VSM mapping (systems):** System 5 + supersystem; partner-instances = System 1 within meta-workshop supersystem

**Что есть:**
- Doc 1B framing: «мета-мастерская для профессиональных мастеров со своими мастерскими» [F4 · R-medium]

**Что задумано:**
- Partner-instances [F2 · R-low]
- Interop protocol [F2 · R-low]
- Full Phase C IWE cooperation [F2 · R-low]

**Top claims (phil):**

| Claim | F-G-R | Falsifier |
|---|---|---|
| «Meta-workshop = Jetix Phase B+ target» | F4 (concept stated в Doc 1B) | Refuted if Doc 1B framing dropped OR replaced |
| «A.1 supersystem holon hosting partners» | F2 (vapor; nothing instantiated) | Refuted only when first partner-instance attempted |

**Anti-scope:**
- NOT partner-instances today
- NOT interop protocol
- NOT Phase C IWE cooperation realised

**Conflation traps (phil):** (1) Meta-workshop confused с current Jetix Corp (O-02) — different horizons.

**Hidden assumptions (phil):** Meta-workshop pattern works с >1 partner instance (zero validation). Partners want their own Jetix-instance (zero demand evidence).

**Leverage point (systems, Meadows L1 — transcend paradigm):** Meta-workshop = system that creates systems. Highest leverage point available in Jetix roadmap. **Still vapor.**

**Feedback loops (systems):**
- R: Meta-workshop clarity → partners see value → instances → feedback → design improves. **Not closed: zero instances.**
- B: Complexity → higher bar → fewer partners → less feedback → complexity accumulates.

**Cross-refs:**
- → O-05 (requires methodology distributable)
- → O-13 (supersystem-for Clan)
- → O-02 (requires legal entity for partner contracts)

**Boundary disputes (phil):**
- vs O-02: O-02 «current Jetix Corp» vs O-14 «platform-for-others» — different horizons. Sometimes cited interchangeably.

---

## §16 — Aggregate Epistemic Patterns (phil + systems)

### EP-1..EP-5 (phil per-object)

**EP-1 (Artefact-system gap, ubiquitous).** 10 of 14 objects: LOCKED artefact (A.16) ≠ operational U.Work. Need split per object: Claim-as-document vs Claim-as-operational-system.

**EP-2 (Use-mention drift).** Workshop / Clan / Meta-workshop names mentioned-as-frame → used-as-structural-claim без declaration.

**EP-3 (Role/executor conflation, cross-object).** CE-2 IP-1 split declared но not consistently applied — propagates через O-01 / O-04 / O-07 / O-12.

**EP-4 (Promise без commitment machinery).** O-02 / O-10 / O-11 / O-13: promise-shaped language без A.2.8 U.Commitment objects (no adjudication / holder / receipt).

**EP-5 (F-G-R applied to wrong subject).** F8/F5 labels apply to document LOCK status, не claim truth-grade. Foundation «F8» ≠ standard B.3 F8.

### Patterns 1-5 (systems cross-object)

**Pattern 1 (Spec-to-Operations Gap Loop, reinforcing).** Spec begetting spec без balancing operations feedback. Senge Law 3.

**Pattern 2 (VSM Inversion).** System 5/3 richer than System 1. Risk pre-operations; advantage post-operations.

**Pattern 3 (Adjacent-Possible Concentration).** 5 of 14 objects = «edge of chaos» — один шаг до emergence: O-01 (auto-KB), O-04 (first client), O-09 (NQD-CAL), O-10 (ICP fix), O-11 (R12 ack).

**Pattern 4 (Dual Loop on revenue).** Loop A (spec→credibility→revenue) vs Loop B (no revenue→complexity grows). Loop B dominates pre-first-client.

**Pattern 5 (Meadows clustering).** L1-L2 developed; L9-L12 vapor. Confirms Pattern 2 from different angle.

---

## §17 — Aggregate Dissents Preserved (per AP-6, NOT averaged)

**D-1 (carried from Phase B Step 2).** IWE = paid AI guide vs public template. F4. All comparative statements scoped to public template.

**D-2 (carried + extended).** Foundation typing dispute. Phil resolution: BOTH faces — U.Episteme for spec-only Parts; U.Work-evidenced for 4 FPF-derivative Parts. Not binary. Ruslan decides via OQ-3.

**D-3 (carried).** Hexagon status partial vs full. F3. Resolution depends on whether we measure against full FPF NQD-CAL bar или within Jetix scope.

**D-PHIL-SCOPE-1 (carried).** Functional vs ontological ordering of inventory.

**D-PHIL-SCOPE-2 (carried + reconfirmed).** Workshop = LOCKED frame vs U.BoundedContext без A.1.1. **Per Task 2 deep dive: A.1.1 fields not directly verified in JETIX-WORKSHOP-CONCEPT-2026-04-30.md; dissent remains.**

**D-mgmt-2 (carried).** Legacy 12-agent roster stale-mailbox vs possibly-active-via-direct-dispatch.

**D-mgmt-3 (carried).** Stale state JSON vs more current indicators (git, drafts).

---

## §18 — Aggregate Open Questions (Task 2 surfaced)

**OQ-T2-1 (Doc 1B §7 ICP inconsistency).** Mittelstand DACH (Doc 1B) vs Online-first (ACTION-PLAN). Live inconsistency, observable today. Two LOCKED documents contradict on basic commercial variable. **Will surface при pitching prospects.** Ruslan: which is canonical?

**OQ-T2-2 (R12 three faces — Task 1 OQ-5 confirmed).** Per phil per-object deep: text U.Episteme / applied U.Commitment / architectural meta-property — each needs own F-G-R + evidence. Ruslan decides scoping.

**OQ-T2-3 (Foundation per-Part status disaggregation).** «F8 LOCKED» blanket label hides per-Part variation (Part 6b enforcement F5 vs Part 9 owner-interaction no daily-log/). Add per-Part F-G-R triple instead of monolithic Foundation label?

**OQ-T2-4 (IP-1 propagation to prose).** CE-2 cross-object pattern — apply IP-1 split к CLAUDE.md prose / mermaid / one-liners (currently «12 agents» persists)?

**OQ-T2-5 (Hexagon as «cadence»).** One 3-day generation window for 6 insights ≠ cadence. Either remove «cadence» word OR establish weekly Part 9 cadence to validate.

**OQ-T2-6 (External reviewer for Foundation).** F8 «via 8 RUSLAN-ACK» = single-author approval. Independent external reviewer for Foundation = strategic decision.

**OQ-T2-7 (Meta-workshop activation conditions).** O-14 vapor → когда становится F4 (working concept) vs F2 (forever-aspirational)? Activation conditions undefined.

### Systems-lens-specific (preserved from systems cell)

**SYS-OQ-1 (Cross-loop priority).** 5 adjacent-possible: O-10 first client closes revenue loop (most variety impact); O-01 closes info; O-09 closes intelligence; O-11 closes constitutional; O-04 external feedback. Activate which first? **Activating O-10 generates external signal feeding ALL other loops.**

**SYS-OQ-2 (Requisite variety gap).** High internal variety (governance / intelligence) but low external variety (clients / market / revenue). Compensation = hiring / partnerships (O-02 + O-14). Timing of variety expansion = strategic.

**SYS-OQ-3 (VSM Inversion timing).** System 5 richer than System 1 = correct IF operations imminent. If delay > 12 months, governance complexity becomes liability (Senge Law 1).

**SYS-OQ-4 (Clan vs Business model ordering).** O-13 needs R12 + legal entity + methodology. O-10 needs Doc 1B alignment + first client. **O-10 path = fewer dependencies; O-13 path = deeper leverage.**

---

*Brigadier integration of 3 cells (eng × integrator FPF-deep + systems × integrator feedback loops + phil × critic epistemic). §5.5.5 gate: provenance ✓ inline citations ✓ dissents preserved per AP-6 ✓ NOT averaged. Output: `reports/phase-0-fpf-scope/02-objects-per-fpf-deep.md`. ≤1 page per object × 14 = ~80-line sections. Full cell drafts available для deeper read.*
