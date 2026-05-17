---
title: Comparison Level Matrix — Phase 0 Task 3 (Jetix object × L1 source × FPF level)
date: 2026-05-17
phase: Phase 0 Task 3
type: integrated-comparison-matrix
status: brigadier-integrated (3 cells: phil × critic + eng × critic + systems × scalability)
parent: reports/phase-0-fpf-scope/01-jetix-objects-inventory.md + reports/phase-0-fpf-scope/02-objects-per-fpf-deep.md
F: F4
G: phase-0-comparison-matrix
R: refuted_if_comparison_predicate_unstated_OR_categorical_mismatch_not_flagged_OR_BLOCKED_sources_not_flagged_OR_scalability_boundary_missing
language: russian + english (FPF primitives)
audience: Ruslan + L1 (Levenchuk / Tseren)
cell_drafts:
  - swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-philosophy-critic-comparison-matrix.md
  - swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-engineering-critic-comparison-matrix.md
  - swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-systems-scalability-comparison-matrix.md
l1_sources:
  C1_FPF_full: raw/external/ailev-FPF/FPF-Spec.md (72,800 lines, vendored 2026-05-16)
  C2_IWE_template: raw/external/tseren-github-2026-05-17/FMT-exocortex-template/ v0.31.0
  C3_IWE_paid_AI_guide: BLOCKED (Aisystant subscription pending — B2)
  C4_Levenchuk_books: B-blocker (not in repo; referenced via FPF/IWE)
  C5_ШСМ_residency: BLOCKED (apply pending)
constitutional_posture: R1 surface-only + R2 Foundation read-only + R6 provenance + append-only
---

# Comparison Level Matrix — Phase 0 Task 3

> **Scope.** Brigadier integration of 3 cells (phil × critic boundaries + eng × critic mechanism rigor + systems × scalability boundaries). Per Jetix object × L1 source × FPF level (Mechanism / Artefact / Role / Method / System / Outcome). All dissents preserved per AP-6. **NOT recommending priority** (R1 — Ruslan decides).

> **Critical scoping (D-1 carried).** L1 source C3 «IWE» в Левенчуковском TG = paid aisystant AI guide (B2 BLOCKED). All IWE comparisons here scoped to **public template v0.31.0**. C4 Левенчуковские books не в repo — referenced via FPF/IWE distillation only. C5 ШСМ residency BLOCKED.

---

## §0 Brigadier integration summary

**3-cell convergence на key findings:**

**Finding F-1 (phil + eng + systems all flag):** **EP-1 artefact-system gap dominant — 10 of 14 objects carry LOCKED artefact status while operational status F2-vapor.** Каждое comparison MUST declare which face is being compared. Без declaration — predicate underdetermined. Most affected: O-03 vision, O-07 Foundation, O-08 Pillar C, O-11 R12.

**Finding F-2 (eng):** **Mechanism-level comparison tractable for 5 objects** — O-07 (Foundation × FPF Parts A-K), O-08 (Pillar C × E.5/A.2.8), O-09 (Hexagon × B.5.2), O-04 (Working product × A.15.1/B.3), O-06a (Role-types × A.2). These have concrete FPF primitives + concrete Jetix file evidence. **Comparison rigor highest here.**

**Finding F-3 (eng):** **Artefact-level comparison breaks для 7 objects** где Jetix имеет LOCKED concept docs но no operational artefact: O-02, O-03, O-05, O-10, O-12, O-13, O-14. FPF Spec has patterns; Jetix has concepts. Comparison validity = low.

**Finding F-4 (phil):** **12 categorical mismatches (CM-01..CM-12)** где comparison cannot be made meaningfully (apples vs oranges). Examples: O-02 (vapor) vs IWE template (no corp entity model); O-10 TRM vs Levenchuk books (business model design не subject of Levenchuk FPF books); O-06b token-level vs Levenchuk books (operate at type-level).

**Finding F-5 (phil):** **11 scope qualifications (SQ-01..SQ-11)** где comparison valid BUT must be qualified (scope-limited). Examples: «vs IWE» = must say «public template only, paid AI guide B2 BLOCKED»; «vs Levenchuk» = must say «via FPF distillation, not direct book reading»; «Foundation F8» = approval-grade not B.3 proof-grade.

**Finding F-6 (systems):** **VSM Inversion master pattern.** S5/S3 richer than S1. Jetix advantages в S5 (R12, FUNDAMENTAL, Pillar C) + partial S3 (F-G-R, Foundation governance). IWE advantages в S1/S2 (OWC fractal, WP Gate, Day Close blocking). FPF Spec advantages в S3/S4 (full abductive loop, MVPK, Guard-Rails formalism).

**Finding F-7 (systems):** **Antifragility check FAILS at 10× scale.** Static read: ~40-50% structural change required. Jetix needs OWC discipline (I-U2 gap), TTL memory (I-U4 gap), Pack distribution format (I-U1 gap), VSM Level-3 emergence. >30% structural change = FRAGILE.

**Finding F-8 (systems):** **5 adjacent-possible activations** — O-01 (auto-KB), O-04 (first client via Tseren), O-09 (NQD-CAL add), O-10 (ICP fix), O-11 (R12 ack). Each один шаг до emergence. Activating O-10 generates external signal feeding ALL other loops.

---

## §1 — Reading Key

**Comparison levels (FPF lens):**
- **Mechanism** — specific FPF mechanism vs specific Jetix counterpart (functional logic match)
- **Artefact** — file/schema structural correspondence (format fidelity)
- **Role** — role taxonomy and assignment correspondence
- **Method** — procedural / workflow correspondence (how work is done)
- **System** — whole-system architecture (holonic composition, VSM-layer, feedback loops)
- **Outcome** — observable outputs / deliverables correspondence

**Flag codes (phil + eng):**
- **CM** = categorical mismatch (different subject-kinds; comparison N/A)
- **SQ** = scope qualification needed (valid but must scope)
- **FU** = falsifier unclear (predicate needs sharpening)
- **PC** = predicate collision (two different claims bundled)
- **MG** = mechanism-gap (concept present; implementation absent)
- **SD** = structural-divergence (different architectures)
- **SC** = structural-correspondence (architectural alignment)
- **MSL** = matching-scope-limited (partial match within scope)
- **BL** = BLOCKED (B2 IWE paid OR C5 ШСМ)

**L1 sources:** C1 = FPF Spec / C2 = IWE template public / C3 = IWE paid AI guide (BLOCKED) / C4 = Левенчук books (B-blocker) / C5 = ШСМ residency (BLOCKED).

---

## §2 — Integrated Matrix Table

### O-01 — Jetix как оперативный субстрат

| L1 source | Level | Compare predicate | Evidence (Jetix / L1) | Boundary / Scope | Flags |
|---|---|---|---|---|---|
| C1 FPF | **System** | Jetix O-01 = holonic U.System matching A.1 + A.1.1 BoundedContext? | `CLAUDE.md §System Overview` / FPF A.1, A.1.1 | Type-level structure ✓; A.1.1 formal fields (glossary + invariants) ABSENT. Operational face: state JSON stale 2026-04-14 | SC type-level / MG operational / SQ artefact-vs-operational |
| C1 FPF | **Mechanism** | A.1.1 formal U.BoundedContext fields satisfied? | informal context в CLAUDE.md / FPF A.1.1 | Informal ≠ formal; D-PHIL-SCOPE-2 applies | SD / MG |
| C2 IWE | **System** | Both = AI-OS for intellectual work; share holonic containment? | ROY swarm + filesystem-SoT / IWE L1-L4 contour | Structurally analogous; OWC vs voice-pipeline different operational discipline. IWE has fallback chain (DS→Pack→SPF→FPF→ZP); Jetix flat-canonical | SC / SD chain-architecture |
| C2 IWE | **Mechanism** | 5-layer Jetix memory vs IWE 4-layer? | agents/*/[core/strategies/scratchpad/niche/mailbox] / IWE MEMORY.md + CLAUDE.md + memory/* + roles/ | Different direction: IWE = human-centered; Jetix = inter-agent. Predicate must state which sub-mechanism | MSL / SC concept |
| C4 Levenchuk | **Method** | Jetix substrate methodology vs FPF practitioner discipline? | ROY dispatch + brigadier + cycle / Интеллект-стек, Системный фитнес-практика | Unit-of-analysis difference (individual practitioner vs AI OS substrate). Books not in repo | SQ unit / FU falsifier |
| C3 IWE-paid / C5 ШСМ | — | Hypothetical | — | — | **BL** |

### O-02 — Jetix как юр.лицо / корпорация (vapor)

| L1 source | Level | Compare predicate | Evidence | Boundary / Scope | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Mechanism** | Doc 1B applies A.6.C Contract Unpacking (promise/utterance/commitment/work)? | `decisions/JETIX-CORPORATION-2026-05-05.md` Doc 1B / FPF A.6.C | Doc 1B = narrative; A.6.C requires structural decomposition. **No explicit attempt found.** Mechanism comparison fails (vapor). | MG / CM operational |
| C1 FPF | **Artefact** | Doc 1B carries A.2.8 U.Commitment fields? | Doc 1B / FPF A.2.8 | TRM = U.PromiseContent at best; A.2.8 obligation-holder + adjudication path absent | MG / EP-4 |
| C2 IWE | **System** | IWE template has corp entity model analogue? | — / IWE = single-person intellectual OS | **N/A:** IWE not corp template. No system-level analog | **CM** |
| C2 IWE | **Artefact** | Doc 1B = Pack charter? | Doc 1B narrative / IWE Pack (ONTOLOGY.md + manifest) | Doc 1B = narrative; Pack = typed distributable. Category gap | SD |
| C2 IWE | **System** | IWE has Role Contract pattern Jetix lacks для corp? | informal Role expectations / IWE roles/ Role Contract | YES — Role Contract increases controller variety; pattern Jetix can adopt. **At €200K (first hire) Jetix's informal expectations can't scale** | SC pattern-borrowable |
| C4 Levenchuk Менеджмент | **Role** | Levenchuk team-roles vs O-02 Partners/Clients/Workers? | Doc 1B 3 levels / Levenchuk books (referenced) | Levenchuk role taxonomy = FPF A.2 derived; Jetix roles = informal. Valid at Role level WITH scope qualifier | SQ formality |
| C3 / C5 | — | — | — | — | **BL** |

### O-03 — Jetix как задумка / vision

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Artefact** | FUNDAMENTAL = A.15.2 U.WorkPlan formal structure? | FUNDAMENTAL 35 UC × 12 cat / FPF A.15.2 | No A.15.2 schedule/forecast fields. FUNDAMENTAL = U.MethodDescription (A.3.2) more than U.WorkPlan | MSL / mechanism-domain mismatch |
| C1 FPF | **Artefact** | FUNDAMENTAL satisfies E.9 DRR + E.17 MVPK (multi-audience)? | FUNDAMENTAL / FPF E.9 + E.17 | DRR fields partial; MVPK = 1A+1B partial. Currently unclear how many ViewpointBundles | FU |
| C1 FPF | **Mechanism** | B.5.1 Explore→Operate state assignment formal? | «Explore» informal label / FPF B.5.1 | Informal assignment; no formal state-graph file | MSL |
| C2 IWE | **Artefact** | FUNDAMENTAL = IWE Pack-equivalent (domain SoT)? | FUNDAMENTAL Layer 1 sector-agnostic / IWE Pack | **Purpose mismatch:** IWE Pack = knowledge domain spec; FUNDAMENTAL = vision declaration. Structural similarity; semantic divergence | SQ semantic / SC structural |
| C4 Levenchuk Методология | **Method** | FUNDAMENTAL's vision-encoding method = Levenchuk's prescribed method? | 35 UC framework / Levenchuk books (referenced) | FUNDAMENTAL predates current Phase B Levenchuk engagement. **Retrospective: does it conform?** | SQ direction |
| C3 / C5 | — | — | — | — | **BL** |

### O-04 — Jetix как работающий продукт

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Mechanism** | Из ~27 components, how many implement B.5.2 Abductive Loop + B.3 F-G-R? | ~12 FPF-derivative / FPF B.5.2 + B.3 | **PC: «~27» bundles 3 categories.** Abductive loop NOT operational. F-G-R partial (per artefact, не per claim full). | PC / MG |
| C1 FPF | **Mechanism** | Jetix produces A.15.1 U.Work records с resource costs? | swarm/wiki/drafts/15 + git log / FPF A.15.1 | «Work records» = artefacts, не formal U.Work с resource cost slots. B.1.6 Γ_work не applied | MG / SC concept |
| C1 FPF | **Outcome** | Jetix produces external deliverables (A.2.3 + work-evidence)? | revenue_current:0; no closed_won / FPF A.2.3 | **Outcome comparison NOT VALID** — promise content→work evidence chain not closed | MG / **FAILS-OUTCOME-VALIDATION** |
| C2 IWE | **Mechanism** | Jetix operational gates (brigadier + AWAITING-APPROVAL + F-G-R lint) = IWE ORZ + WP Gate + ArchGate? | brigadier dispatch + AWAITING-APPROVAL / IWE WP Gate + ORZ + ArchGate | Different gate scope: IWE = session-level blocking; Jetix = architectural-level. **Comparison valid с qualification** | SQ scope / MSL |
| C2 IWE | **Outcome** | Jetix wiki/KB vs IWE Capture-to-Pack? | wiki 551 records (informal) / IWE Pack SPF-structured | Different output structure; informal entity types vs SPF Pack discipline | SD |
| C2 IWE | **System** | OWC fractal adoption gap | aspirational /plan-day, /close-day / IWE OWC blocking 4-scales | **At 10× sessions: Jetix non-blocking close = knowledge loss; IWE blocks each scale** | MG / I-U2 gap |
| C4 Levenchuk Интеллект-стек | **Outcome** | Levenchuk C3 critique: Jetix produces intelligence amplification > vanilla AI? | ~12 FPF-derivative / Интеллект-стек bar | **Falsifier needed concrete:** «what does Jetix produce that same input to Claude without Jetix cannot?» Per audit: partial. F2 currently. | FU / C4 benchmark needed |
| C3 / C5 | — | — | — | — | **BL** |

### O-05 — Jetix как методология / pattern language

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Artefact** | Fork guide v0 satisfies A.3.2 U.MethodDescription? | working-file §11 6-step outline / FPF A.3.2 | 6-step = U.WorkPlan attempt; не U.MethodDescription recipe. F2 grade | MG |
| C1 FPF | **Method** | FUNDAMENTAL Layer 1 satisfies A.8 Universal Core? | Layer 1 sector-agnostic / FPF A.8 | Valid at Artefact level (structure); NOT at Method level (no enacted method). **0 instantiations.** | SQ / FU |
| C1 FPF | **System** | FUNDAMENTAL + Fork guide = A.5 Kernel Modularity + A.8 Universal Core forkable architecture? | two-layer architecture / FPF A.5 + A.8 | **At €1M+ (Phase C activation): Fork guide v0 insufficient — first forker needs structural instantiation guide.** Adjacent-possible if formalised | MSL / Phase C remit |
| C2 IWE | **Artefact** | Fork guide vs IWE Pack distribution format? | Fork guide v0 = narrative / IWE Pack = manifest + ONTOLOGY.md + fallback chain | **Maturity mismatch:** IWE operational forkable; Jetix narrative concept. Artefact comparison fails entirely. | SD / CM artefact-type |
| C2 IWE | **System** | Both claim forkability — IWE operational vs Jetix aspirational? | Fork guide v0 (F2, 0 forkers) / IWE setup.sh + update.sh + releases | Comparison valid only as «aspirational analogy, NOT current parity». **Falsifier: «Jetix Fork guide successfully used by ≥1 external party» = refuted (0)** | CM-maturity / FU |
| C4 Levenchuk Методология | **Method** | Jetix methodology derives from / conforms to Levenchuk's? | FUNDAMENTAL + Pillar C / Levenchuk Методология | Genealogy ≠ conformance. Phase B engagement IS CURRENT, не Phase A design input | SQ genealogy-vs-conformance |
| C3 / C5 | — | — | — | — | **BL** |

### O-06a — Jetix-as-12-role-types (IP-1 type-level)

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Role** | 12 declarations satisfy A.2 + A.2.7 RoleAlgebra + A.13 Agential Role? | CLAUDE.md §Agent Roster + Part 4 LOCKED / FPF A.2 | Type-level ✓; **method-signature (A.15) enforcement = STUB.** A.2.7 declared but не lintable | SC type / MG enforcement |
| C1 FPF | **Mechanism** | IP-1 Role≠Executor = full A.13 Agency Spectrum? | IP-1 binary split / FPF A.13 spectrum 0..N | IP-1 = bottom-limit only; full A.13 grading not implemented | MSL |
| C2 IWE | **Role** | Jetix role declarations vs IWE roles/ Role Contracts (DP.ROLE.001)? | CLAUDE.md + .claude/agents/*.md / IWE Pack DP.ROLE.001 | Different structural homes; both require method-signature before executor assignment. **IWE: blocking via IntegrationGate; Jetix: STUB enforcement.** | SC / MG enforcement |
| C2 IWE | **System** | Jetix 12 broad vs IWE 5 deep roles? | 12 × 6 depts / IWE 5 roles (Strategist/Extractor/Auditor/Planner/WP-Sync) + Role Contracts | Jetix coverage breadth; IWE depth per role. **At 10× complexity: Role Contract pattern needed.** | SC complementary / SQ |
| C4 Levenchuk books | **Role** | 6-dept topology = Levenchuk practitioner role taxonomy? | 12 × 6 / Levenchuk books referenced | Levenchuk = practitioner-level (разработчик/менеджер); Jetix = AI agent roles. **Different role granularity.** Books predate AI-OS deployment | SQ granularity / FU |
| C3 / C5 | — | — | — | — | **BL** |

### O-06b — Jetix-as-executor-bindings (IP-1 token-level)

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Mechanism** | RUSLAN-LAYER executor-binding.yaml = A.2.1 Holder#Role:Context? | template + .claude/agents/ / FPF A.2.1 | Holder#Role:Context partial: Context ✓; **RSG (A.2.5 RoleStateGraph) absent (STUB).** | SC partial / MG RSG |
| C1 FPF | **System** | ROY swarm = A.2.1 + A.13 operational agential system? | brigadier + 5 experts × 4 modes / FPF A.2.1 + A.13 | A.13 autonomy budgets **NOT explicitly declared.** **At 10× dispatch: brigadier cannot distinguish self-escalate vs human gate** | MSL / scalability-gap |
| C2 IWE | **Mechanism** | Brigadier dispatch (LLM-driven) = IWE rule-engine.sh (rule-based deterministic)? | brigadier + routing-table.yaml (hint) / IWE rules-registry.yaml + rule-engine.sh | **Architecture mismatch:** IWE deterministic, Jetix LLM-driven. WP Gate blocks work without plan; AWAITING-APPROVAL blocks Foundation writes — different domains | SQ architecture / MSL |
| C2 IWE | **Role** | ROY swarm = IWE roles.md? | brigadier + 5 ROY / IWE roles.md (5 roles) | Unit mismatch: IWE single-user; Jetix 6-agent multi-cell. Role≠Executor convergent principle | MSL principle / SD depth |
| C4 Levenchuk | **Role** | Token-level vs type-level Levenchuk operates at | tokens / books = types only | **N/A at token level — Levenchuk role taxonomy is type-level (A.2), не A.2.1 RoleAssignment** | **CM** |
| C3 / C5 | — | — | — | — | **BL** |

### O-07 — Foundation Architecture v1.0 (F8-LOCKED)

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **System** | Foundation 11 Parts = FPF 11 Pillars (A-K)? | 11 Parts + Pillar A/C / FPF Parts A-K | **PC: Foundation = org substrate; FPF Parts = epistemological framework.** Different subject-kinds. Mapping = «FPF primitives adopted IN Foundation Parts» NOT «Foundation Parts = FPF Parts». | SD different subject-kinds |
| C1 FPF | **Mechanism** | Part 6b (Human Gate) implements FPF E.5 Guard-Rails (GR-1..GR-4)? | Default-Deny + AWAITING-APPROVAL / FPF E.5 (DevOps Lexical Firewall / Notational Indep / Unidirectional Dep / Cross-Disciplinary Bias Audit) | **Semantic proximity ≠ mechanism identity.** Part 6b = operational HITL gating (runtime); FPF E.5 = architectural constraints on FPF spec authoring. Different guard-rail purposes. | MSL / SD purpose |
| C1 FPF | **Artefact** | F8 LOCKED grade = FPF B.3 F8 standard? | 8 RUSLAN-ACK (single-author) / FPF B.3 F8 (independently verified) | **EP-5 CRITICAL:** Jetix F8 = approval-grade by single reviewer (Ruslan). FPF B.3 F8 = independent evidence + verification. **Comparison at F-grade misleading.** | **SD EP-5 / mandatory disclosure** |
| C1 FPF | **System** | Foundation Parts have formal dependency declarations? | Foundation 11 Parts flat / FPF Parts dependency graph («Builds on / Prerequisite for») | **Scalability gap:** FPF dependency graph scales (independent Part upgrades); Jetix monolithic Foundation cycle revision. **At 10 partner instances: 10× revision-propagation cost** | SD scalability |
| C2 IWE | **Artefact** | Foundation 11 Parts = IWE CLAUDE.md + memory/ + .claude/hooks/ + skills/? | 11 architecture.md files + CLAUDE.md / IWE template structure | Different scale and purpose scope: IWE single-owner intellectual OS; Jetix multi-role AI OS governance. **Artefact comparison valid at structural shape level only** | SQ scope / SC structural |
| C2 IWE | **System** | Foundation lacks IWE's S-35 memory lifecycle / OS scheduling / ArchGate? | Foundation 11 Parts substrate / IWE S-35 + launchd + ArchGate | **At €1M: Jetix Foundation has no OS-level scheduling (I-U5 gap); no memory TTL (I-U4 gap)** | MG / scalability-gap |
| C4 Levenchuk Менеджмент / Системная инженерия | **System** | Foundation governance arch follows Levenchuk's FPF-applied management? | 11 Parts + Pillar A/C / Levenchuk Менеджмент (FPF-applied) | **Scale + actor mismatch:** Levenchuk targets human orgs; Foundation = AI OS with one human. Valid if qualified «structural principles regardless of human/AI actor» | SQ scale / FU |
| C3 / C5 | — | — | — | — | **BL** |

### O-08 — Pillar C (12 Tier-2 rules)

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Mechanism** | Default-Deny table implements FPF C.10 Norm-CAL (deontic + adjudication)? | .claude/config/default-deny-table.yaml (11 entries) + 12 rules / FPF C.10 + A.2.8 | **CE-4 from Task 1 confirmed:** Rule 11 only machine-enforced. Rules 1/3/8/9/12 = no adjudication path (A.2.8 hooks absent). Comparison: 1 of 12 mechanism-grade, 11 of 12 artefact-grade. | MG (11/12) / SC (1/12) |
| C1 FPF | **Artefact** | 12 rule text = FPF E.2 Eleven Pillars format? | prose-numbered list / FPF E.2 (keywords + query triggers + dep chains) | Format mismatch: prose-list vs structured-pattern | SD format |
| C1 FPF | **System** | Pillar C two-tier (Tier 1 + Tier 2) = FPF E.2 Eleven Pillars? | Tier 1 (manager) + Tier 2 (system) / FPF E.2 Eleven Pillars | A.6.B Boundary Norm Square NOT formally applied. **At 10× agent operations: 11/12 human-enforced = single-point-of-failure** | MG / scalability-fragility |
| C2 IWE | **Mechanism** | Default-Deny + Halt-Log-Alert = IWE rule-engine.sh + hooks? | STUB Halt-Log-Alert / IWE rule-engine.sh operational | **Maturity asymmetry:** IWE operational; Jetix STUB Phase-B. Falsifier «Halt-Log-Alert fires within SLA» NOT verified | MG / SQ maturity |
| C2 IWE | **Mechanism** | Pillar C = IWE 13 hard distinctions (distinctions.md)? | Pillar C 12 rules / IWE 13 distinctions | **Function mismatch:** IWE = semantic precision (avoid conflation); Jetix = deontic obligations (what AI MUST NOT). Both encode binary criteria. | MSL different-function / SC encoding |
| C2 IWE | **System** | IWE blocking rules vs Jetix advisory for 11/12 rules | STUB enforcement / IWE blocking (WP Gate, ArchGate, OWC Close) | **At 10× sessions: IWE blocking prevents violations; Jetix advisory cannot scale Ruslan's attention** | MG / scalability-gap |
| C4 Levenchuk books | **Artefact** | Pillar C two-tier = Eleven Pillars in FPF books? | Tier 1 + Tier 2 / FPF E.2 referenced | Levenchuk Eleven Pillars = formal FPF E.2; Jetix Pillar C inspired but not formally E.2 | SQ formality |
| C3 / C5 | — | — | — | — | **BL** |

### O-09 — Strategic Insights Hexagon

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Method** | Hexagon process conforms to B.5.2 Abductive Loop (alternatives-portfolio + NQD-CAL)? | 6 LOCKED insights + F-G-R + multi-view / FPF B.5.2 «rival-set discipline + threshold crossing» | **CRITICAL: «output=process» conflation.** 6 LOCKED outputs ≠ documented abductive process. **Alternatives portfolio NOT evidenced.** F-G-R tagging ≠ abductive loop. | MG / D-3 process-evidence |
| C1 FPF | **Artefact** | E.17 MVPK (multi-view publication) = Hexagon 1A/1B two-view? | 1A current + 1B aspirational / FPF E.17 MVPK formal ViewpointBundle | Two-view concept present; formal MVPK schema (ViewpointBundle + ViewpointSlot) absent | SD partial / MG |
| C1 FPF | **System** | Hexagon = B.5.2 Abductive Loop intelligence system? | 6 insights at F5 / FPF B.5.2 NQD-CAL | **PARTIAL: outputs ✓; alternatives NOT explicit (one-data-point generation, не systematic abduction).** At 10× decisions: echo chamber risk (no falsification mechanism per B.3 R) | MG / scalability-risk |
| C2 IWE | **Method** | Hexagon weekly cadence = IWE Strategy Session? | 3-day generation window for 6 insights / IWE weekly strategy session BLOCKING | **«Cadence» applied to single 3-day event ≠ sustained weekly process.** OQ-T2-5. IWE has enforced periodicity | MSL / FU |
| C2 IWE | **Outcome** | Hexagon outputs vs IWE strategy session WeekPlan? | LOCKED strategic insights (multi-week synthesis) / IWE WeekPlan (operational planning daily) | **Different temporal granularity:** operational planning (IWE) vs strategic synthesis (Jetix). Complementary, not equivalent. **Both needed at €200K** | SC complementary / SQ |
| C4 Levenchuk Методология | **Method** | Hexagon applies Levenchuk's abductive discipline? | H1-H7 production / Levenchuk Методология abductive | NQD step (null hypothesis before conclusion) NOT documented publicly | FU / SQ |
| C3 / C5 | — | — | — | — | **BL** |

### O-10 — Бизнес-модель Phase 1 (TRM)

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Mechanism** | TRM 6-resource = FPF A.2.3 PromiseContent + A.2.8 Commitment + A.6.C Contract Unpacking? | TRM LOCKED 6-resource ladder / FPF A.2.3 + A.2.8 + A.6.C | A.2.3 PromiseContent ✓; **A.2.8 fields absent (obligation-holder + adjudication + receipt).** A.6.C not applied (informal). | MG / EP-4 |
| C1 FPF | **Mechanism** | TRM = B.1.6 Γ_work (work as spent resource)? | only 2 of 6 tracked (attention + capital) / FPF B.1.6 | **2 of 6 mechanized; 4 of 6 = conceptual only.** Falsifier observable. | MG (4/6) |
| C1 FPF | **Artefact** | Doc 1B §7 ICP satisfies A.6.C Contract Unpacking? | Doc 1B §7 Mittelstand / ACTION-PLAN §0 Online-first / FPF A.6.C | **LIVE INCONSISTENCY (OQ-T2-1):** Doc 1B §7 = Mittelstand DACH; ACTION-PLAN-PHASE-1 §0 = Online-first. Two LOCKED docs contradict. **Comparison at A.6.C level FAILS until resolved.** | **SD / live-flag / MUST-RESOLVE** |
| C2 IWE | **Mechanism** | TRM = IWE service clause format (DP.SC.NNN: trigger + inputs + outputs + SLA + failure)? | TRM 6-resource + L0-L5 / IWE DP.SC.NNN | Different abstraction: TRM business-level; IWE = tool/skill level. Comparison valid с scope qualifier | SQ abstraction |
| C2 IWE | **System** | At Phase C: TRM = commercial layer + IWE OWC = operational layer? | TRM model / IWE OWC | **Complementary:** TRM = promise; OWC = execution. Designed TRM без evolved session discipline = fragile (Kelly out-of-control) | SC complementary |
| C4 Levenchuk | **Method** | Business model design = Levenchuk's subject? | TRM / Levenchuk books | **N/A:** business model design NOT subject of Levenchuk FPF books | **CM** |
| C3 / C5 | — | — | — | — | **BL** |

### O-11 — R12 Anti-extraction

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Mechanism** | R12 text = A.2.8 U.Commitment с adjudication hooks? | r12-anti-extraction-2026-05-12.md AWAITING-APPROVAL + 4-source trail / FPF A.2.8 | **PC: THREE faces.** Text face: 4-source trail = evidenceRefs ✓. **Adjudication hooks ABSENT.** Enforcement mechanism = vapor. | SC text / MG enforcement |
| C1 FPF | **System** | R12 = unique vs FPF E.5 Guard-Rails (no equivalent в FPF Spec)? | text LOCKED / FPF E.5 + Phase B verification | **NO direct FPF analogue (verified Phase B).** R12 = Jetix-unique. **Meadows L2 leverage** (system goal). FPF E.5 closest container но не addresses member-value-extraction. | unique (J-U2) / SC concept-new |
| C2 IWE | **System** | IWE template has R12-equivalent? | — / IWE template scan (no R12 found per audit §3 J-U2) | **N/A — Jetix-unique mechanism confirmed** | **CM / unique** |
| C2 IWE | **System** | R12 surface к IWE community? | — / Cooperation Plan options | Surfacing R12 to IWE ecosystem → potential adoption creates mutual protection norm | strategic-OQ-12 |
| C4 Levenchuk books | **Artefact** | R12 = principle Levenchuk describes? | R12 / Levenchuk books referenced | OQ-12 strategic (Ruslan). Falsifier: «Levenchuk books contain equivalent под different name» — to verify | FU strategic |
| C3 / C5 | — | — | — | — | **BL** |

### O-12 — Бренд / публичный слой

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Artefact** | Doc 1A + 1B = E.17 MVPK ViewpointBundle? | Doc 1A + Doc 1B / FPF E.17 | Two-view structure ✓; **formal ViewpointBundle declaration absent**, no MVPK bundles for all audiences | SC partial / MG |
| C1 FPF | **Outcome** | Doc 1A + 1B = complete publication system? | 1A + 1B / FPF E.17 4-6 ViewpointBundles per audience | **At €200K: 2-view MVPK insufficient — each audience needs dedicated ViewpointBundle** | MG / scalability-gap |
| C1 FPF | **Mechanism** | Workshop metaphor satisfies A.1.1 U.BoundedContext (glossary + invariants + scope + anti-scope)? | JETIX-WORKSHOP-CONCEPT-2026-04-30.md / FPF A.1.1 | **D-PHIL-SCOPE-2 dissent:** A.1.1 fields NOT directly verified в Workshop doc. **Likely lacks formal A.1.1 structure** (per phil deep dive) | FU / EP-2 use-mention |
| C2 IWE | **Artefact** | Jetix brand vs IWE README.md + ONTOLOGY.md + Pack-concept public face? | Doc 1A/1B internal LOCKED / IWE GitHub repo с releases | **Maturity mismatch:** IWE deployed public artefacts с version badge; Jetix internal LOCKED docs (no website) | SQ deployment-maturity / SD |
| C2 IWE | **Method** | 6 outreach files vs IWE Creative Pipeline (note→draft→template→post)? | 6 outreach files (send confirmed:0) / IWE 4-stage pipeline + TTL | **Jetix lacks pipeline state tracking + TTL.** OWC fractal Close not enforced | MG / I-U6 gap |
| C2 IWE | **Outcome** | Jetix brand monologue vs IWE structured community feedback (CONTRIBUTING.md)? | 6 outreach files (no replies) / IWE CONTRIBUTING.md + iwe-bug-report + iwe-rules-review | **IWE structured intake; Jetix has output без structured intake.** **At community scale (O-13): pattern needed** | MG / I-U-feedback gap |
| C4 Levenchuk | **Method** | Brand presentation methodology? | Doc 1A/1B / Levenchuk books referenced | OQ marketing methodology gap | FU / SQ |
| C3 / C5 | — | — | — | — | **BL** |

### O-13 — People-Network-State / Clan

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **Method** | Clan Charter encodes B.2 Meta-Holon Transition с BOSC triggers? | 6 archetypes + stealth launch / FPF B.2 + B.2.1 BOSC | **BOSC explicit trigger fields not verified** (Boundary/Operation/Scale/Composition/Agency/Time/eXternal). Charter has archetypes; full B.2.1 fields unclear | FU / MSL |
| C1 FPF | **Mechanism** | 6 archetypes = A.2.7 ⊗ role-bundle operator? | 6 archetypes / FPF A.2.7 ⊗ | **Semantic proximity ≠ identity:** Jetix archetypes = identity types; A.2.7 = co-occurring functional roles. Different semantics | MSL / SQ |
| C1 FPF | **System** | Clan activation = B.2.2 MST protocol? | 0 signatories / FPF B.2.2 MST | **B.2.2 MST protocol = undeclared.** At 5+ signatories: transition unmanaged | MG / scalability-fragility |
| C2 IWE | **System** | IWE template has community-system analogue? | 0 signatories Jetix / IWE = individual-scale; agent-inbox extension is AI-only | **N/A at current scale.** Community features in IWE = paid aisystant (B2). Neither FPF nor IWE template provides ready Clan model | **CM** |
| C4 Levenchuk | **System** | Multi-actor community governance principles? | Clan / Levenchuk Менеджмент referenced | Books discuss multi-actor governance; surface Clan principles vs Levenchuk principles | FU |
| C3 / C5 | — | — | — | — | **BL** |

### O-14 — Meta-workshop (Phase B+ vapor)

| L1 source | Level | Compare predicate | Evidence | Boundary | Flags |
|---|---|---|---|---|---|
| C1 FPF | **System** | Meta-workshop = A.5 Kernel Modularity + A.3.1 Method hosting composable method-ecosystem? | vapor concept (Doc 1B framing) / FPF A.5 + A.3.1 | **VAPOR:** concept stated; A.5 + A.3.1 = right mechanisms; no instance to evaluate | vapor / SQ Phase-C |
| C1 FPF | **System** | Phase C activation requires 3 simultaneous unlocks (O-05 + O-02 + O-13)? | — / dependencies | **All three currently vapor.** Meta-workshop = maximum adjacent-possible expansion requires 3 unlocks | scalability-dependent |
| C2 IWE | **System** | IWE Pack format provides structural pattern for partner instances? | Doc 1B framing / IWE Pack-as-domain-unit (ONTOLOGY.md + manifest + fallback chain) | **YES — IWE architecture demonstrates pattern.** «Jetix holds SPF/FPF base; each partner creates Pack». **Pattern Jetix can adopt** | SC pattern-borrowable / strategic |
| C4 Levenchuk | **System** | Meta-system formation? | — / Levenchuk books referenced | OQ-T2-7 activation conditions | FU |
| C3 / C5 | — | — | — | — | **BL** |

---

## §3 — Mechanism Deep Dives (6 priority comparisons)

Per eng × critic — comparisons где **rigor highest** (concrete FPF primitives + concrete Jetix evidence):

### DD-1. F-G-R Adoption: Jetix Part 6a vs FPF B.3

- **FPF source:** FPF Spec B.3 «Trust & Assurance Calculus» (F-G-R per claim)
- **Jetix counterpart:** `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` (F-G-R schema enforcement)
- **Verdict:** Concept aligned (B.3 directly adopted); enforcement = single-author by Ruslan (EP-5 concern). At claim level (full B.3) = partial; at artefact level = adopted.
- **Falsifier:** Each promoted Foundation artefact carries explicit F-level + G-scope + R-falsifier per claim. Currently: artefact-level F-G-R; per-claim = inconsistent.
- **Scalability:** B.3 scales per-claim; current Jetix adoption scales per-artefact. **At 10× claims gap amplifies.**

### DD-2. Guard-Rails: Jetix Pillar C + Default-Deny vs FPF E.5

- **FPF source:** FPF E.5 «Four Guard-Rails of FPF» (GR-1..GR-4 architectural constraints on spec authoring)
- **Jetix counterpart:** Pillar C 12 rules + `.claude/config/default-deny-table.yaml` (11 entries) + Halt-Log-Alert spec
- **Verdict:** **Different domain-applications of same pattern.** FPF E.5 = architectural constraints на FPF spec evolution. Pillar C = operational HITL gating runtime. Semantic proximity, не mechanism identity.
- **Falsifier:** Both prevent unsafe additions. FPF E.5: prevents FPF Spec drift. Jetix Pillar C: prevents unsafe actions. Different domains, similar shape.
- **Scalability:** Pillar C 11/12 advisory at scale = single-point-of-failure (Ruslan). IWE blocking pattern scales better.

### DD-3. Role Taxonomy: Jetix Part 4 vs FPF A.2

- **FPF source:** A.2 Role Taxonomy + A.2.1 RoleAssignment + A.2.5 RoleStateGraph + A.2.7 RoleAlgebra + A.13 Agential Role
- **Jetix counterpart:** `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` + IP-1 Role≠Executor
- **Verdict:** **Most FPF-aligned object в Jetix.** A.2.1 partially (Context ✓, RSG absent); A.2.7 declared but не lintable; method-signature enforcement = STUB.
- **Falsifier:** Per-role check that method-signature + RoleAlgebra position + autonomy-budget present.
- **Scalability:** Without A.2.5 RoleStateGraph operational, brigadier sees 2 states per role (active/inactive). At 10× tasks = coordination bottleneck.

### DD-4. Hexagon vs FPF B.5.2 Abductive Loop

- **FPF source:** B.5.2 Abductive Loop (rival-set discipline + threshold crossing + NQD-CAL)
- **Jetix counterpart:** `decisions/STRATEGIC-INSIGHT-*.md` × 6 (H1-H7 LOCKED 2026-05-10..12); F-G-R tagged; multi-view 1A+1B
- **Verdict:** **«Closest to FPF intelligence amplification» per audit §7 BUT alternatives portfolio NOT evidenced.** «Output=process» conflation. 6 LOCKED outputs ≠ documented abductive process.
- **Falsifier:** Hexagon generation logs show ≥2 alternatives explicitly stated and discarded with kill-conditions before each LOCKED insight.
- **Scalability:** Without NQD-CAL = echo chamber at 10× decisions. Confirmation bias amplifies.

### DD-5. Working product outputs: Jetix vs FPF intelligence amplification bar

- **FPF source:** A.15.1 U.Work + B.1.6 Γ_work + B.5.2 Abductive Loop
- **Jetix counterpart:** Cycle outputs (15 Phase-B drafts + Foundation LOCKED + outreach files + voice reviews)
- **Verdict:** Internal artefacts produced; external work-evidence chain NOT closed (revenue = 0). Per 06-honest-self-audit §12: ~27 components / ~12 intelligence-bearing. **Not FPF-grade.**
- **Falsifier (Levenchuk C3):** «Jetix produces что vanilla Claude cannot» — falsifiable by controlled comparison. **C4 benchmark not yet run (B2 dependency).**
- **Scalability:** Without external loop closure, internal output scaling = internal complexity scaling. Loop B dominates.

### DD-6. Foundation 11 Parts vs FPF Parts A-K architectural mapping

- **FPF source:** FPF Spec Parts A-K (Kernel / Reasoning / Extensions / Ethics / Constitution / etc.) с dependency graph
- **Jetix counterpart:** Foundation 11 Parts + Pillar A + Pillar C
- **Verdict:** **Different subject-kinds.** Jetix = org substrate (memory + governance + coordination). FPF = epistemological framework. **NOT isomorphic.** Mapping = «FPF primitives adopted IN Foundation Parts». Per audit §2.1: 4 of 11 FPF-derivative; 7 of 11 memory/automation.
- **Falsifier:** Per-Part audit: which FPF primitive each Part implements vs which is memory-only.
- **Scalability:** FPF dependency graph scales; Jetix monolithic Foundation cycle revision. **At 10 partner instances = 10× revision-propagation cost.**

---

## §4 — Categorical Mismatches (12 explicit N/A flags)

Per phil × critic — где comparison **cannot be made meaningfully** (apples vs oranges):

| # | Mismatch | Reason |
|---|---|---|
| CM-01 | O-02 corp × IWE template at System | IWE = single-person intellectual OS; не corp entity template |
| CM-02 | O-05 methodology distribution × IWE Pack | Maturity mismatch: Jetix = narrative concept; IWE = operational distributable artefact |
| CM-03 | O-06b executor-bindings × Levenchuk books | Books operate at type-level (A.2); executor bindings = token-level (A.2.1) |
| CM-04 | O-10 TRM business model × Levenchuk books at Method | Business model design не subject of Levenchuk FPF books |
| CM-05 | O-13 Clan × IWE template at System | IWE individual-scale; community features = paid aisystant (B2 BLOCKED) |
| CM-06 | O-07 Foundation Parts × FPF Parts A-K at System | Different subject-kinds: org substrate vs epistemological framework |
| CM-07 | O-04 working product outcome validation | **Outcome comparison NOT VALID** — promise→work-evidence chain not closed (revenue = 0) |
| CM-08 | O-11 R12 × FPF Spec at System | **NO direct FPF analogue** (verified Phase B); R12 = Jetix-unique |
| CM-09 | O-11 R12 × IWE template | **NO IWE equivalent** (confirmed J-U2 Phase B audit) |
| CM-10 | O-10 ICP comparison | **LIVE INCONSISTENCY** Doc 1B vs ACTION-PLAN — comparison FAILS until resolved |
| CM-11 | Workshop metaphor × A.1.1 BoundedContext | D-PHIL-SCOPE-2: Workshop lacks A.1.1 fields; comparison reveals gap |
| CM-12 | F8 Jetix vs F8 FPF B.3 | **EP-5 CRITICAL:** Jetix F8 = single-author approval; FPF B.3 F8 = independent verification. Misleading comparison |

---

## §5 — Scope Qualifications Needed (11 SQ)

Per phil × critic — где comparison valid BUT must be qualified:

| # | Qualification | Applies to |
|---|---|---|
| SQ-01 | «vs IWE» = «public template v0.31.0 only; paid AI guide B2 BLOCKED» | ALL IWE comparison rows |
| SQ-02 | «vs Levenchuk books» = «via FPF/IWE distillation, не direct book reading» | ALL C4 comparison rows |
| SQ-03 | «Jetix F8» = «approval-grade by Ruslan (8 RUSLAN-ACK), не FPF B.3 proof-grade» | O-07, O-08, O-09 |
| SQ-04 | Comparison face declaration: artefact vs operational | EP-1 affects 10 of 14 objects |
| SQ-05 | IP-1 face declaration: type-level vs token-level | O-06a / O-06b separation |
| SQ-06 | Workshop = U.BoundedContext only IF A.1.1 fields present | O-12 D-PHIL-SCOPE-2 |
| SQ-07 | «Phase C remit» = no defined start condition | O-05, O-14 |
| SQ-08 | Unit-of-analysis: individual practitioner vs AI-OS substrate | O-01, O-04, O-06a vs Levenchuk |
| SQ-09 | Temporal granularity: weekly (IWE) vs multi-month (Jetix Hexagon) | O-09 vs IWE |
| SQ-10 | Maturity asymmetry: IWE deployed operational vs Jetix STUB | O-04, O-05, O-08 vs IWE |
| SQ-11 | «100-200y ambition» = unfalsifiable over horizon (normative not predictive) | O-03 |

---

## §6 — VSM Mapping (systems × scalability)

Cross-system architectural comparison:

| VSM Level | FPF Spec | IWE Template | Jetix current | Comparison |
|---|---|---|---|---|
| **S5 (identity/policy)** | Part E Constitution (E.5 Guard-Rails + Eleven Pillars) | CLAUDE.md §2 blocking + Fallback Chain | **Pillar C (12 rules) + FUNDAMENTAL + R12 — RICHEST в Jetix** | Jetix S5 advantage |
| **S4 (intelligence/futures)** | Part B Reasoning (B.5.2 + E.17 + E.9) | Strategy Session + WeekPlan + Digital Twin | O-09 Hexagon (partial B.5.2) + Part 11 + Vision | FPF S4 advantage; IWE S4 operational |
| **S3 (audit/control)** | Part A Kernel (A.2.8 + A.6.B + B.3) | R24 Auditor + ArchGate + Week/Month Close | **Foundation v1.0 + F-G-R + AWAITING-APPROVAL — SECOND-RICHEST** | Jetix S3 advantage (artefact); IWE blocking-rule advantage |
| **S2 (coordination)** | A.2 + A.2.1 + A.13 | OWC fractal + WP Gate + WP Registry | ROY swarm + shared-protocols.md | IWE S2 mature; Jetix operational но under-specified |
| **S1 (operations)** | A.15 + A.3 + A.10 | Day Open/Close + Capture-to-Pack + WP delivery | Voice pipeline + wiki + CRM — **WEAKEST в Jetix; zero external closure** | IWE S1 advantage |

**VSM Inversion verdict (Finding F-6).** Jetix S5/S3 rich; S1 weak. **Pre-operations: hazard.** **Post-operations: advantage.**

---

## §7 — Scalability Projections (systems × scalability)

5 gates with antifragility check (Finding F-7):

| Gate | Threshold | Jetix readiness | Restructure required | Verdict |
|---|---|---|---|---|
| G-1 | €50K (current) | tactical FPF adoption | ~10% | OK для current |
| G-2 | €200K (first hire) | Doc 1B inconsistency + no Role Contracts + no OS scheduling | ~25% | warning |
| G-3 | €1M (managed team / first distribution) | no Pack format + no OWC + no TTL | ~40% | **FRAGILE** (antifragility FAIL) |
| G-4 | $100M ARR | meta-workshop + community + VSM Level-3 emergence | ~50% | **FRAGILE** (major restructure) |
| G-5 | $1T (Clan Charter 100-200y ambition) | unfalsifiable over horizon | N/A | normative not predictive |

**Antifragility check.** Static read: ~40-50% restructure at 10×. Exceeds 30% threshold → **FRAGILE.** De-morph reversibility (B2 mechanic) partially offsets (~10%). Edge of FRAGILE threshold (D-SYS-3 dissent preserved).

**Adjacent-possible activations (5 of 14 objects, один шаг каждое):** O-01 auto-KB / O-04 first client / O-09 NQD-CAL / O-10 ICP fix / O-11 R12 ack. Activating O-10 first client generates external signal feeding ALL other loops.

---

## §8 — Network Effects + Supersystem Comparison

**FPF Spec = community-scale system.** Each FPF contribution refines shared pattern library. Network effects.
**IWE template = individual-scale system.** Per-practitioner instance + Pack inheritance. Network effects via Pack ecosystem.
**Jetix = single-instance org-scale system.** No community contribution path; no instance distribution. **Captures none of network effects.**

**Scalability implication.** At Phase C (meta-workshop activation), Jetix needs to either:
1. **Adopt FPF community contribution path** — R12 to FPF Part E (OQ-12)
2. **Adopt IWE Pack distribution format** — Jetix-as-Pack для partners
3. **Build own network mechanism** — Clan Charter signatory path

Strategic decision (R1 — Ruslan).

---

## §9 — Falsifiable Comparison Predicates (15 FP)

Per phil × critic — concrete falsifiers for top comparison claims:

| # | Comparison | Falsifier |
|---|---|---|
| FP-01 | Foundation operational | Operational audit shows Parts 1/3/5/9/11 zero execution evidence beyond static storage |
| FP-02 | Jetix F8 = FPF B.3 F8 | Refuted by EP-5: single-author approval ≠ independent verification |
| FP-03 | Hexagon B.5.2 conformance | Refuted if generation logs show no explicit alternatives discarded |
| FP-04 | Jetix > vanilla Claude (Levenchuk C3) | Falsifiable by C4 benchmark Arm A vs D. Pending B2. |
| FP-05 | TRM tracks 6 resources | Refuted if resource logs show <6 mechanically tracked |
| FP-06 | Halt-Log-Alert operational | Refuted if F8 violation committed без halt within 1s |
| FP-07 | Workshop = A.1.1 BoundedContext | Refuted if doc lacks explicit glossary + invariants + scope |
| FP-08 | R12 unique vs IWE | Confirmed Phase B audit; falsifier = «IWE paid AI guide reveals R12-equivalent» (B2 blocker) |
| FP-09 | 12 rules = constitutional uniformly enforced | Refuted by enforcement asymmetry (Rule 11 only machine) |
| FP-10 | ICP = consistent | **Refuted today** by Doc 1B vs ACTION-PLAN inconsistency |
| FP-11 | Method-signature per role enforced | Refuted by STUB status |
| FP-12 | Hexagon weekly cadence | Refuted: 3-day window for 6 insights ≠ weekly |
| FP-13 | Fork guide v0 = enables forking | Refuted: 0 external forkers |
| FP-14 | Clan stealth launch | Refuted if visible public attempts pre-first-signatory |
| FP-15 | R12 ack'd | Refuted if AWAITING-APPROVAL remains unacked beyond cycle |

---

## §10 — Dissents Preserved (per AP-6, NOT averaged)

**D-1 (carried).** IWE = paid AI guide vs public template. SQ-01.

**D-2 (carried + extended).** Foundation typing dispute. Phil resolution: BOTH faces per-Part.

**D-3 (carried).** Hexagon partial vs full — depends on bar (FPF NQD-CAL vs Jetix scope).

**D-PHIL-SCOPE-2 (carried + reconfirmed Task 2).** Workshop A.1.1 status — fields likely absent.

**D-mgmt-2 (carried).** Legacy 12 agents stale vs possibly-active.

**D-T3-1 (phil new).** O-09 Hexagon: Output vs Process. Output level ≠ process level. Process unverified.

**D-T3-2 (phil new).** O-07 F8 в comparisons. EP-5: approval-grade misleads externally.

**D-T3-3 (phil new).** O-01 vs IWE scale asymmetry. Structurally comparable; deployment maturity не comparable.

**D-T3-ENG-1 (eng).** EP-5 F-grade misapplication cross-cutting.

**D-T3-ENG-2 (eng).** Foundation-as-spec vs Foundation-as-system (D-2) affects artefact fidelity grades.

**D-T3-ENG-3 (eng).** FPF Parts F-K coverage gap — mechanism count may be under-counted.

**D-T3-ENG-4 (eng).** Vapor objects should use Method-level comparison (не Mechanism-level).

**D-SYS-3 (systems carried).** Antifragility ~40-50% restructure; de-morph absorbs ~10%; edge of FRAGILE.

**D-SYS-4 (systems).** IWE public template lacks S3; paid platform may reveal S3 (B2 blocker).

**D-SYS-NEW-1 (systems).** VSM Inversion = current hazard OR future advantage (depends on revenue closure timing).

**D-SYS-NEW-2 (systems).** Tactical FPF adoption sufficient (Phase A) vs structural gap compounds (Phase B+ debt).

---

## §11 — Open Questions для Ruslan (R1 surface only)

**OQ-T3-1.** Из 6 priority mechanism deep dives (§3), какие включать в Phase 0 master document (§5)? Все 6 = comprehensive; subset = focused.

**OQ-T3-2 (C4 benchmark timing).** Falsifier FP-04 «Jetix > vanilla Claude» = C4 benchmark. Pending B2. Когда run Arm A vs D experiment?

**OQ-T3-3 (B2 unblock priority).** Aisystant subscription resolves C3 (IWE paid guide). High-priority blocker for: SQ-01 + CM-09 + FP-08.

**OQ-T3-4 (FPF Parts F-K reading).** D-T3-ENG-3: full FPF Spec reading would surface more comparison rows. Worth dispatching deep-read cell?

**OQ-T3-5 (ICP inconsistency resolution path).** Doc 1B §7 vs ACTION-PLAN. Which canonical? Update direction?

**OQ-T3-6 (R12 to FPF community surface).** OQ-12 carried + reinforced: R12 = J-U2 verified unique. Surface as contribution candidate?

**OQ-T3-7 (Pack format adoption).** IWE Pack pattern для Phase C activation (O-14 meta-workshop). Strategic.

**OQ-T3-8 (External reviewer pattern).** FP-02 EP-5 concern: single-author approval misleads externally. Add external reviewer для key Foundation Parts?

**SYS-OQ-1 (from Task 2 carried).** Cross-loop priority — 5 adjacent-possible activations. **O-10 first client = highest variety impact (closes ALL loops).**

**SYS-OQ-2.** Requisite variety expansion timing — hiring / partnerships когда?

**SYS-OQ-3.** VSM Inversion resolution timing — operations imminent (advantage) vs delayed >12 months (liability).

**SYS-OQ-4.** Clan (O-13) vs Business model (O-10) ordering — O-10 fewer dependencies; O-13 deeper leverage.

**SYS-OQ-5.** Antifragility posture — accept FRAGILE at 10× (Phase A tactical) vs invest in structural alignment (Phase B+ effort)?

**SYS-OQ-6.** OWC fractal adoption — adopt IWE I-U2 (session-level blocking) когда?

---

## §12 — Most Viable Comparisons (summary view per L1 source)

**For Ruslan quick scan: which comparisons имеют smysl now (with current source access).**

| L1 source | Status | Viable comparisons | NOT viable |
|---|---|---|---|
| **C1 FPF Spec** | ✓ Vendored | All 14 objects × Mechanism / Artefact / System levels possible. **Highest rigor:** O-04 / O-06a / O-07 / O-08 / O-09 / O-11 mechanism level. | EP-5 single-author F-grade conflation. CM-12 mandatory disclosure. |
| **C2 IWE public template** | ✓ Vendored | 10 of 14 objects × System / Mechanism levels. **Highest rigor:** O-01 / O-04 / O-06a / O-06b / O-07 / O-08 / O-12. | CM-01, CM-05, CM-09 + SQ-01 (paid-vs-public). |
| **C3 IWE paid AI guide** | **BLOCKED** | None (hypothetical only) | All comparisons hypothetical |
| **C4 Левенчук books** | B-blocker | Surface-only via FPF/IWE distillation. References valid; direct book quotes not | Direct book-based mechanism comparison |
| **C5 ШСМ residency** | **BLOCKED** | None (hypothetical) | All comparisons hypothetical |

**Phase 0 acceptance.** This matrix surfaces **comparison structure**, not comparison conclusions. Ruslan decides what to pursue (R1).

---

*Brigadier integration of 3 cells (phil × critic comparison boundaries + eng × critic mechanism rigor + systems × scalability VSM/scale). §5.5.5 gate: provenance per row ✓ falsifiable predicates ✓ CM/SQ/MG/SD flags consistent ✓ dissents preserved per AP-6 ✓ BLOCKED sources explicit. Output: `reports/phase-0-fpf-scope/03-comparison-matrix.md`. Full cell drafts available для deeper read.*
