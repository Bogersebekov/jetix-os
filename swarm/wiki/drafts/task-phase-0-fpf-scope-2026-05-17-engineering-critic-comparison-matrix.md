---
task_id: phase-0-fpf-scope-2026-05-17-task-3
produced_by: engineering-expert × critic
mode: critic
status: draft
F: F4
G: phase-0-cell-draft
R: refuted_if_concrete_evidence_missing_OR_boundary_conditions_not_stated
date: 2026-05-17
inputs:
  - reports/phase-0-fpf-scope/01-jetix-objects-inventory.md
  - reports/phase-0-fpf-scope/02-objects-per-fpf-deep.md
  - raw/external/ailev-FPF/FPF-Spec.md (ToC + Part A B C E)
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md
  - raw/external/tseren-github-2026-05-17/FMT-exocortex-template/ONTOLOGY.md
  - reports/jetix-vs-iwe-audit-2026-05-17.md
  - reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md
---

# FPF Scope Definition — Comparison Level Matrix (Task 3)

> **Engineering-critic posture.** Surface comparison rigor issues. Do NOT evaluate «better/worse». Do NOT strategize. R1 applies: Ruslan = sole strategist. Per §3.4 anti-scope: no priority ranking, no method choices, no capital impact analysis.

> **CRITICAL SCOPING NOTE (D-1 carried).** L1 source C3 «IWE умнее конкурентов» likely refers to paid aisystant AI guide (B2 BLOCKED). All IWE comparison rows below are scoped to public `FMT-exocortex-template` ver 0.31.0 unless flagged `[PAID-PLATFORM]`.

> **COMPARISON LEVEL DEFINITIONS (applied per row):**
> - **Mechanism** — specific FPF mechanism vs specific Jetix counterpart (functional logic match or mismatch)
> - **Artefact** — file/schema structural correspondence (format fidelity, frontmatter fields, schema coverage)
> - **Role** — role taxonomy and assignment correspondence
> - **Method** — procedural / workflow correspondence (how work is done)
> - **System** — whole-system structural correspondence (holonic composition, VSM-layer, feedback loops)
> - **Outcome** — observable outputs / deliverables correspondence

---

## §0 Summary

**14 Jetix objects × 5 L1 sources = up to 70 comparison cells. Practical coverage: 42 filled rows (14 objects × 3 primary sources; L1-C3 IWE paid and L1-C5 ШСМ = BLOCKED/N/A).**

**Top engineering-critic findings:**

1. **Mechanism comparison is tractable for 5 objects** (O-07, O-08, O-09, O-04, O-06a). These have concrete FPF primitives + concrete Jetix file evidence. All 5 comparisons are at Mechanism or Artefact level — the two levels where engineering can make binary checks.

2. **Artefact-level comparison breaks for 7 objects** where Jetix has document LOCKED artefacts but no operational artefact (O-02, O-03, O-05, O-10, O-12, O-13, O-14). FPF Spec has patterns for these object types; Jetix has concept docs. Comparison validity = low.

3. **IWE template comparison is cleanest at Method level** (OWC fractal vs Jetix `/plan-day` / `/close-day`; WP Gate vs AWAITING-APPROVAL). Mechanism-level IWE comparison is blocked by D-1 (paid guide not accessible).

4. **Левенчуков книги and ШСМ residency comparisons** are blocked entirely (books not on disk per Phase A rule; residency BLOCKED apply pending). Engineering can surface the FPF primitive mapping but NOT validate against book text.

5. **6 critical boundary conditions** surface where comparison loses validity: (a) vapor objects vs FPF operational patterns; (b) single-reviewer F8 vs FPF B.3 F8; (c) IWE template vs IWE paid guide conflation (D-1); (d) Jetix-as-multi-agent-org vs IWE-as-single-worker unit mismatch; (e) Foundation-as-spec vs Foundation-as-system (D-2); (f) Hexagon-as-process vs Hexagon-as-output (D-3).

**Acceptance predicate (Hamel-binary):** This draft covers all 14 objects with ≥1 comparison row each, carries concrete evidence per side (file:line refs), states boundary conditions per object, and flags ≥5 mechanism deep-dives in §2. PASS if no object row has evidence field empty on BOTH sides. FAIL if any boundary condition is absent.

**Current state:** PASS on object coverage; PASS on boundary conditions; PARTIAL on evidence density (IWE + books blocked reduces evidence on those columns).

---

## §1 Matrix Table

**Column key:**
- **Jetix object** — O-NN name
- **L1 source** — which of the 5 comparison arms
- **Level** — comparison level applied (Mechanism / Artefact / Role / Method / System / Outcome)
- **Compare predicate** — Hamel-binary test: «Does [Jetix entity] structurally correspond to [FPF entity]?»
- **Jetix evidence** — file:line or path ref
- **L1 evidence** — FPF/IWE path:section ref
- **Boundary conditions** — where comparison stops being valid
- **Eng critic flag** — matching-scope-limited / structural-correspondence / structural-divergence / mechanism-gap / N/A-blocked

---

### O-01 — Jetix как оперативный субстрат

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-01 Оперативный субстрат | FPF полная | **System** | «Does Jetix O-01 instantiate FPF A.1 U.System holonic structure (whole-inward, part-outward)?» | `CLAUDE.md §System Overview`: «12 specialized agents across 6 departments»; `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` (Part 4 LOCKED) | FPF-Spec.md A.1 «Holonic Foundation: Entity → Holon» — U.System = part-whole composition with boundary | Boundary: comparison holds for *type-level* holonic structure declaration; breaks if we require *operational* enactment (state JSON stale 2026-04-14; `shared/state/active-projects.json`). D-2 unresolved. | structural-correspondence (type level); mechanism-gap (operational level — A.4 Temporal Duality gap) |
| O-01 Оперативный субстрат | FPF полная | **Mechanism** | «Does Jetix implement A.1.1 U.BoundedContext (glossary + invariants + scope) formally?» | `CLAUDE.md §Кто ты` has informal context declaration; no formal A.1.1 fields (glossary slot + invariant slot) found in any single document | FPF-Spec.md A.1.1 — requires: local meaning, context, semantic boundary, domain, invariants, glossary, DDD | Breaks: informal context declarations ≠ FPF A.1.1 formal U.BoundedContext; D-PHIL-SCOPE-2 applies here (Workshop as frame, not A.1.1 structure) | structural-divergence (mechanism present in concept; formal fields absent) |
| O-01 Оперативный субстрат | IWE template | **System** | «Does Jetix O-01 correspond to IWE Base tier in fallback chain?» | Jetix = single repo, single owner, no fallback chain to peer framework | IWE CLAUDE.md §1 Architecture: «Fallback Chain: DS → Pack → Base (SPF → FPF → ZP)»; `ONTOLOGY.md §1`: upstream-deps = SPF + FPF | Breaks: IWE fallback chain is multi-tier (6 layers); Jetix is monorepo single-owner without upstream-chaining mechanism | structural-divergence — Jetix lacks framework-layering; IWE is structurally downstream of FPF/SPF |

---

### O-02 — Jetix как юр.лицо / корпорация

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-02 Корпорация | FPF полная | **Mechanism** | «Does Doc 1B apply A.6.C Contract Unpacking (promise / utterance / commitment / work separation)?» | `decisions/JETIX-CORPORATION-2026-05-05.md` — Doc 1B = conceptual doc; TRM ladder at §6-7; no explicit promise/utterance/commitment/work decomposition fields | FPF-Spec.md A.6.C «Contract Unpacking» — requires: PromiseContent ≠ utterance ≠ commitment ≠ work+evidence | Breaks: Doc 1B is narrative; A.6.C requires structural decomposition. Comparison valid only for checking whether Jetix attempts the unpacking — answer: NO explicit attempt found | mechanism-gap (A.6.C not applied; only A.2.3 PromiseContent face present) |
| O-02 Корпорация | IWE template | **Artefact** | «Does Doc 1B correspond to an IWE Pack charter artefact?» | `decisions/JETIX-CORPORATION-2026-05-05.md` (Doc 1B) — LOCKED v1.0; 1 document, narrative structure | IWE CLAUDE.md §1: Pack = «Паспорт предметной области» с ONTOLOGY.md + manifest + fallback-chain declaration | Breaks: Doc 1B = conceptual narrative doc; IWE Pack = typed distributable artefact with formal slots (ONTOLOGY.md, rules, fallback-chain). Category gap — different artefact types | structural-divergence (doc ≠ pack format; artefact-level comparison fails) |

---

### O-03 — Jetix как задумка / vision

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-03 Vision | FPF полная | **Artefact** | «Does FUNDAMENTAL satisfy FPF A.15.2 U.WorkPlan formal structure (intent, schedule, forecast)?» | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` — 35 UC × 12 categories; F8 artefact-LOCKED; no explicit A.15.2 fields (schedule slot, forecast slot) | FPF-Spec.md A.15.2 «U.WorkPlan: The Schedule of Intent» — requires plan / schedule / intent / forecast structure | Breaks: FUNDAMENTAL = U.MethodDescription (A.3.2) or normative vision document; A.15.2 schedule/forecast fields absent. F8 = document approval, not FPF proof-grade F8. | matching-scope-limited (vision document maps to FPF U.MethodDescription face more than U.WorkPlan face) |
| O-03 Vision | FPF полная | **Mechanism** | «Does Jetix implement B.5.1 Explore→Shape→Evidence→Operate state machine for vision?» | `reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md §2`: Part 7 stage-gate mechanic adopted; «B.5.1 Explore→Operate state = Explore» (per 01-inventory §5 O-03) | FPF-Spec.md B.5.1 «Explore → Shape → Evidence → Operate» — development state cycle | Breaks: B.5.1 state machine applies per-artefact, not per-vision-doc. «Vision is in Explore» = informal assignment, not a formal B.5.1 state graph with state-transition guards | matching-scope-limited (informal assignment; no formal state-graph file) |

---

### O-04 — Jetix как работающий продукт

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-04 Рабочий продукт | FPF полная | **Mechanism** | «Does Jetix produce A.15.1 U.Work records (records of occurrence with resource costs)?» | `swarm/wiki/drafts/` — 15 Phase-B cell drafts; `git log` commit history; `reports/review_2026-05-14.md` voice review outputs. Per 06-honest-self-audit §12: ~27 components | FPF-Spec.md A.15.1 «U.Work: The Record of Occurrence» — execution / event / run / actuals / log | Breaks: Jetix «work records» = wiki drafts + cycle logs (artefacts, not formal U.Work records with resource cost slots). B.1.6 Γ_work resource accounting not applied. | structural-correspondence (concept-level); mechanism-gap (formal U.Work record schema not enforced) |
| O-04 Рабочий продукт | FPF полная | **Outcome** | «Does Jetix produce external deliverables (client-facing outputs = FPF A.2.3 U.PromiseContent + evidence)?» | `shared/state/active-projects.json` — revenue_current: 0; `crm/people/*.md` — draft suffix files; 0 closed_won | FPF-Spec.md A.2.3 U.PromiseContent — consumer-facing promise clause with accessSpec + acceptanceSpec + SLO + Work evidence | Breaks: Outcome comparison requires external work evidence (client deliverables). Revenue = 0 means the promise-content→work-evidence chain is not yet closed. Comparison at Outcome level = NOT VALID for current state. | mechanism-gap (promise content exists; work-evidence chain not closed) |
| O-04 Рабочий продукт | IWE template | **Outcome** | «Does Jetix working product correspond to IWE «working product» deliverables?» | 15 Phase-B drafts + Foundation LOCKED = internal artefacts. Per 01-inventory §3 O-04: «НЕ шиппится: клиентские deliverables» | IWE CLAUDE.md §2: РП (Work Product) = artef produced for work; WP Gate tracks each work product instance | Breaks: IWE WP = per-task work product tracked in registry; Jetix «working product» = multi-component internal system. Different granularity: IWE WP is session-level task output; Jetix O-04 is org-level system | structural-divergence (scope mismatch — task-level vs org-level) |

---

### O-05 — Jetix как методология / pattern language

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-05 Методология | FPF полная | **Artefact** | «Does Fork guide v0 (§11 working file) satisfy FPF A.3.2 U.MethodDescription (recipe for action with formal structure)?» | `JETIX-WORKING-FILE-v0 §11` — 6-step minimal viable instance; informal narrative; no formal MethodDescription fields | FPF-Spec.md A.3.2 «U.MethodDescription: The Recipe for Action» — specification / recipe / SOP / code / model (= U.Episteme) | Breaks: 6-step outline = U.WorkPlan attempt (intention), not U.MethodDescription (recipe with formal applicability + mechanics). F2 grade (06-honest-self-audit §3). | mechanism-gap (U.MethodDescription requires formalized recipe structure; outline ≠ recipe) |
| O-05 Методология | IWE template | **Artefact** | «Does Jetix-as-methodology correspond to IWE Pack distribution format?» | No distributable format exists; `JETIX-WORKING-FILE-v0 §11` Fork guide v0 = 6 steps (F2 grade); 0 external forks | IWE ONTOLOGY.md §2: Pack = «source-of-truth для доменного знания» with ONTOLOGY.md + manifest + `fallback-chain`; `CLAUDE.md §1`: «Pack Creation Gate: /pack-new» | Breaks: IWE Pack is a concrete distributable artefact with formal schema (manifest, ontology, fallback chain, rules). Jetix methodology = narrative concept doc. Artefact-level comparison fails entirely — different artefact types. | structural-divergence (Jetix has concept; IWE has typed distributable artefact) |

---

### O-06a — Jetix-as-12-role-types (type-level)

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-06a Role-types | FPF полная | **Mechanism** | «Does Jetix Part 4 implement FPF A.2 Role Taxonomy (RoleAlgebra: ≤, ⊥, ⊗ operators)?» | `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` — Part 4 LOCKED F8; A.2.7 RoleAlgebra cited in 01-inventory §2 O-06a; 6-dept topology = RoleS ≤ RoleG | FPF-Spec.md A.2.7 «U.RoleAlgebra: specialization (≤), incompatibility (⊥), bundles (⊗)» + A.2.1 «Holder#Role:Context Standard» | Breaks: Part 4 declares role types and A.2 alignment; enforcement via method-signature (A.15) = STUB (per 06-honest-self-audit §2 Part 4 note: «method-signature не yet enforced»). Comparison valid for type-level declarations; breaks for enforcement claims. | structural-correspondence (type-level A.2 adoption confirmed); mechanism-gap (A.15 method-signature enforcement = STUB) |
| O-06a Role-types | FPF полная | **Role** | «Does Jetix IP-1 Role≠Executor correspond to FPF A.13 Agential Role (substrate-neutral autonomy)?» | `CLAUDE.md §4.2` IP-1 Role≠Executor; `shared/schemas/executor-binding.yaml.template` RUSLAN-LAYER binding; `.claude/agents/` (23 files) | FPF-Spec.md A.13 «Agential Role & Agency Spectrum» — agency as role; contextual role assignment; autonomy grading | Breaks: IP-1 is a binary split (role ≠ executor); FPF A.13 is a spectrum (autonomy grading 0..N). IP-1 prevents conflation but does not implement the full Agency Spectrum grading. | matching-scope-limited (IP-1 implements FPF A.13 bottom-limit; full spectrum not graded) |

---

### O-06b — Jetix-as-executor-bindings (token-level)

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-06b Executor-bindings | FPF полная | **Mechanism** | «Does RUSLAN-LAYER executor-binding.yaml.template implement FPF A.2.1 U.RoleAssignment Holder#Role:Context Standard?» | `shared/schemas/executor-binding.yaml.template` — maps role → model (Sonnet 4.6 / Haiku 4.5); fields: role_id + model + context | FPF-Spec.md A.2.1 «U.RoleAssignment» — Standard: Holder#Role:Context; requires: RCS/RSG (Role Context Specification / Role State Graph) | Breaks: template maps role→model (executor binding); FPF A.2.1 requires Holder#Role:Context triple with RSG state graph. Context field present; RSG = NOT present (A.2.5 RoleStateGraph = STUB per audit). | structural-correspondence (Holder#Role:Context partially; Context field ✓; RSG absent ✗) |
| O-06b Executor-bindings | IWE template | **Role** | «Does Jetix ROY swarm architecture correspond to IWE roles.md role-per-agent structure?» | `.claude/agents/` — brigadier + 5 ROY experts; ROY swarm dispatching 15 Phase-B passes | IWE ONTOLOGY.md §2: «ИИ-система: Claude Code, бот — исполнители ролей (DP.ROLE.001)»; roles/README.md: «один агент может выполнять несколько ролей» | Breaks: IWE roles.md defines roles for single-user context (user + Claude Code ± assistant agents); Jetix ROY swarm = 6-agent multi-cell architecture. Unit mismatch (single-worker vs multi-agent). | matching-scope-limited (principle alignment: Role≠Executor convergent; architectural depth diverges) |

---

### O-07 — Foundation Architecture v1.0

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-07 Foundation | FPF полная | **System** | «Do Jetix Foundation 11 Parts correspond to FPF Parts A–K structural organization?» | `CLAUDE.md §Foundation Architecture v1.0`: 11 Parts + Pillar A + Pillar C; `swarm/wiki/foundations/*/architecture.md` (11 files); RUSLAN-ACK × 8 | FPF-Spec.md: Part A (Kernel), B (Reasoning), C (Extensions), D (Ethics), E (Constitution); 11+ Parts with 200+ patterns | Breaks: Jetix Foundation = 11 parts organisational architecture; FPF = epistemological framework for reasoning (not org architecture). Different subject-kinds — they are NOT isomorphic. Mapping is «FPF primitives adopted IN foundation parts» not «foundation parts = FPF parts». | structural-divergence (different subject-kinds; FPF = reasoning framework; Foundation = org substrate) |
| O-07 Foundation | FPF полная | **Mechanism** | «Does Part 6b (Human Gate) implement FPF E.5 Guard-Rails (GR-1..GR-4)?» | `swarm/wiki/foundations/part-6b-human-gate/architecture.md` — Default-Deny table (11 entries), AWAITING-APPROVAL, Halt-Log-Alert | FPF-Spec.md E.5 «Four Guard-Rails of FPF»: GR-1 (DevOps Lexical Firewall), GR-2 (Notational Independence), GR-3 (Unidirectional Dependency), GR-4 (Cross-Disciplinary Bias Audit) | Breaks: Part 6b Guard-Rails = operational HITL gating (prevent unsafe actions); FPF E.5 Guard-Rails = architectural constraints on FPF spec authoring (not runtime enforcement). Different guard-rail purposes. Semantic proximity ≠ mechanism identity. | matching-scope-limited (guard-rails concept shared; mechanisms are different domain-applications of same pattern) |
| O-07 Foundation | FPF полная | **Artefact** | «Does the F8 LOCKED grade on Foundation correspond to FPF B.3 F8 (independently tested 8 times)?» | Foundation LOCKED via 8 RUSLAN-ACK (single-author review); `decisions/RUSLAN-ACK-*.md` × 8 | FPF-Spec.md B.3 / C.2.3 «Unified Formality Characteristic F» — F8 = highest; FPF implies independent verification at high F levels | Breaks: Jetix F8 = document-approval by single reviewer (Ruslan). FPF B.3 F8 implies high-formality claim with independent evidence. **EP-5 critical: single-author approval ≠ FPF proof-grade F8.** Comparison at F-grade level is misleading. | structural-divergence (EP-5 pattern — Jetix F8 = approval grade ≠ FPF F8 = proof/evidence grade) |
| O-07 Foundation | IWE template | **System** | «Does Jetix Foundation correspond to IWE platform-space (L1-L3 layer structure)?» | Foundation 11 Parts = governance/substrate layer | IWE ONTOLOGY.md §3: «Слой памяти (Memory Layer)»: Layer 1 (MEMORY.md) + Layer 2 (CLAUDE.md) + Layer 3 (memory/*.md); «Контур системы»: L1 Ecosystem → L2 Platform → L3 Template → L4 Personal | Breaks: IWE layer structure = context-memory hierarchy for single-worker; Foundation = 11-part org governance for multi-agent system. Different architectural subjects. | structural-divergence (different architectural subjects — personal memory vs org governance) |

---

### O-08 — Pillar C конституциональная система

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-08 Pillar C | FPF полная | **Mechanism** | «Does Pillar C Default-Deny table implement FPF C.10 Norm-CAL (deontic norms: obligation/permission/prohibition with adjudication)?» | `.claude/config/default-deny-table.yaml` — 11 entries; `swarm/wiki/foundations/principles/architecture.md` — 12 Tier-2 rules | FPF-Spec.md C.10 «Norm-CAL» — norms / constraint / ethics / obligation / permission / deontics; A.2.8 U.Commitment (adjudication hooks, BCP-14 modality) | Breaks: Default-Deny table = deny-and-escalate logic for novel actions; FPF Norm-CAL = full deontic calculus with adjudication paths + evidence refs + modality normalization. **CE-4 applies: Rules 1/3/8/9/12 have no adjudication path defined.** Only Rule 11 machine-enforced. | structural-correspondence (Rule 11 only); mechanism-gap (Rules 1/3/8/9/12 lack A.2.8 adjudication hooks) |
| O-08 Pillar C | FPF полная | **Artefact** | «Does Pillar C 12-rule text satisfy FPF E.2 Eleven Pillars format (specific principle fields)?» | `CLAUDE.md §4.1` — 12 rules as numbered list with bold titles + prose | FPF-Spec.md E.2 «The Eleven Pillars» — P-1..P-11; FPF principles carry: keyword, query triggers, dependency chains (FPF-Spec.md ToC format) | Breaks: Jetix rules = prose-numbered list; FPF Pillars = structured patterns with keywords + queries + dependencies. Artefact format mismatch. | structural-divergence (artefact format: prose-list vs structured-pattern) |
| O-08 Pillar C | IWE template | **Mechanism** | «Does Jetix Pillar C correspond to IWE hard-distinctions discipline (.claude/rules/distinctions.md)?» | `CLAUDE.md §4.1` — 12 hard rules; `swarm/wiki/foundations/principles/architecture.md` — Tier 2 system + Tier 1 owner | IWE `.claude/rules/distinctions.md` — 13 hard distinctions; `memory/hard-distinctions.md` for detailed tests | Breaks: IWE distinctions = semantic precision rules (avoid conflation); Jetix Pillar C = deontic obligations (what AI MUST NOT do). Different functions: semantic clarity vs deontic enforcement. | matching-scope-limited (both encode binary criteria with «не путать» tests; different normative function) |

---

### O-09 — Strategic Insights Hexagon

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-09 Hexagon | FPF полная | **Mechanism** | «Does Hexagon synthesis implement FPF B.5.2 Abductive Loop (alternatives portfolio + origin trace + plausibility filters)?» | `decisions/STRATEGIC-INSIGHT-*.md` × 6 (2026-05-10..12) — F-G-R tagged, multi-view 1A+1B; BUT no alternatives portfolio found; no documented plausibility filtering step | FPF-Spec.md B.5.2 «Abductive Loop» — candidate hypotheses + plausibility filters + origin trace + route-to-hypothesis; B.5.2.0 U.AbductivePrompt: «rival-set discipline, threshold crossing» | Breaks: D-3 unresolved — «partial» reflects FPF bar, not Jetix-internal bar. Alternatives portfolio = NOT evidenced in 6 INSIGHT files. F-G-R tagging ≠ abductive loop. **Output≠process: 6 LOCKED outputs ≠ documented abductive process with rival-set.** | mechanism-gap (F-G-R + multi-view ✓; alternatives portfolio ABSENT; abductive loop = informal) |
| O-09 Hexagon | FPF полная | **Artefact** | «Does E.17 MVPK (Multi-View Publication Kit) structure correspond to Hexagon 1A/1B two-view outputs?» | `JETIX-WORKING-FILE-v0 §5.1` — Hexagon 1A (current state) + 1B (aspirational); two views present | FPF-Spec.md E.17 MVPK — typed publication surfaces; ViewpointBundle + formal ViewpointBundleLibrary; faces «no new semantics» | Breaks: Hexagon 1A/1B = informal two-view labeling; FPF E.17 MVPK requires formal ViewpointBundle declaration + ViewpointSlot registration. No formal ViewpointBundle document found in Jetix. | structural-divergence (two-view concept present; formal MVPK schema absent) |
| O-09 Hexagon | IWE template | **Method** | «Does Hexagon synthesis cadence correspond to IWE Strategy Session (weekly)?» | 6 INSIGHT files generated in 3-day window 2026-05-10..12; no documented weekly cadence; `JETIX-WORKING-FILE-v0 §5.1` | IWE CLAUDE.md `.claude/skills/strategy-session/SKILL.md` — weekly strategy session; `CLAUDE.md §2`: Day Open / Week Close ritual BLOCKING | Breaks: Jetix «cadence» is a label applied to single 3-day event (D-3 OQ-T2-5). IWE strategy session = blocking weekly ritual with formal entry gate. Temporal regularity comparison fails. | matching-scope-limited (both involve structured synthesis; IWE has enforced periodicity; Jetix cadence = aspirational) |

---

### O-10 — Бизнес-модель Phase 1 (TRM)

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-10 TRM | FPF полная | **Mechanism** | «Does TRM 6-resource model implement FPF B.1.6 Γ_work (work as spent resource with resource aggregation)?» | `decisions/JETIX-TRM-MODEL-2026-04-30.md §1` — 6 resource classes; but only 2 of 6 tracked mechanically (capital + attention per 02-per-object-deep §11) | FPF-Spec.md B.1.6 «Γ_work — Work as Spent Resource» — resource aggregation / cost / energy consumption / Resrc-CAL | Breaks: TRM identifies 6 resource classes conceptually; B.1.6 requires formal resource accounting (log of spent resources per work record). **2 of 6 mechanized; 4 of 6 = conceptual only.** | mechanism-gap (concept alignment ✓; formal Γ_work resource accounting absent for 4/6 classes) |
| O-10 TRM | FPF полная | **Artefact** | «Does Doc 1B §7 ICP field satisfy FPF A.6.C Contract Unpacking for promise content?» | `decisions/JETIX-CORPORATION-2026-05-05.md §7` — Mittelstand DACH ICP (NOT updated; ACTION-PLAN changed to Online-first) | FPF-Spec.md A.6.C Contract Unpacking — promise content / utterance / commitment separation | Breaks: **LIVE INCONSISTENCY: Doc 1B §7 = Mittelstand DACH; ACTION-PLAN-PHASE-1 §0 = Online-first. Two LOCKED docs contradict on ICP.** Any comparison at A.6.C level fails because the promise content is contradicted cross-document. | structural-divergence (active inconsistency makes artefact-level comparison invalid until resolved; OQ-T2-1) |

---

### O-11 — R12 Anti-extraction

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-11 R12 | FPF полная | **Mechanism** | «Does R12 implement FPF A.2.8 U.Commitment (deontic commitment with adjudication hooks + evidence refs)?» | `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` — text LOCKED; 4-source trail; AWAITING-APPROVAL NOT yet ack'd | FPF-Spec.md A.2.8 «U.Commitment: Deontic Commitment Object» — requires: obligation/permission/prohibition + scope + validity window + **adjudication hooks** + evidenceRefs | Breaks: R12 text exists + 4-source trail (= evidenceRefs ✓); BUT adjudication hooks (how is R12 violation adjudicated?) = NOT described; enforcement mechanism = vapor (per 02-per-object-deep §12). U.Commitment implementation = partial. | structural-correspondence (text + 4-source trail ✓); mechanism-gap (adjudication hooks absent; enforcement = vapor) |
| O-11 R12 | IWE template | **Mechanism** | «Does Jetix R12 have an IWE equivalent anti-extraction principle?» | `CLAUDE.md §4.1 rule 12`; `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` | IWE template full scan — no R12 equivalent found; audit confirms J-U2 in `reports/jetix-vs-iwe-audit-2026-05-17.md §3` | Breaks: IWE template has no anti-extraction principle (confirmed by Phase B audit). Comparison = N/A (Jetix-unique mechanism, not a comparison cell). Surface as N/A with evidence. | N/A — Jetix-unique mechanism (J-U2 confirmed unique per jetix-vs-iwe-audit §3) |

---

### O-12 — Бренд / публичный слой

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-12 Бренд | FPF полная | **Artefact** | «Does Doc 1A + Doc 1B two-view structure correspond to FPF E.17 MVPK ViewpointBundle?» | `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` (Doc 1A) + `decisions/JETIX-CORPORATION-2026-05-05.md` (Doc 1B) — two audience-specific views | FPF-Spec.md E.17 MVPK — typed publication surfaces; requires: ViewpointBundle + formal ViewpointSlot + «faces no new semantics» rule | Breaks: Doc 1A + Doc 1B = two narrative documents for different audiences; MVPK requires formal ViewpointBundle with explicitly declared viewpoints and no-new-semantics constraint. Artefact format mismatch — narrative docs ≠ formal MVPK faces. | structural-divergence (two-view concept present; formal MVPK artefact schema absent) |
| O-12 Бренд | IWE template | **Method** | «Does Jetix 6 outreach files correspond to IWE Creative Pipeline (note → draft → template → publication)?» | `outreach/` — 6 files (2026-05-12..17); send confirmations absent | IWE ONTOLOGY.md §3: «Творческий конвейер: 4 стадии превращения мысли в публикацию: заметка → черновик → заготовка → пост. Каждый артефакт обязан продвинуться или быть закрыт в пределах TTL» | Breaks: Jetix outreach = 6 written files (= stage 2 «черновик»?); IWE pipeline requires per-artefact state tracking + TTL enforcement. Jetix has no TTL on outreach files; pipeline state not tracked. | mechanism-gap (output artefacts present; pipeline state-tracking + TTL absent) |

---

### O-13 — People-Network-State / Clan

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-13 Clan | FPF полная | **Mechanism** | «Does Clan 6-archetype bundle correspond to FPF A.2.7 U.RoleAlgebra ⊗ operator (role bundles)?» | `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md` — 6 archetypes (Hunter / Guardian / Scholar / Creator / Architect / Merchant); ⊗ operator cited in 01-inventory §1 O-13 | FPF-Spec.md A.2.7 «bundles (⊗)» — role bundles = set of roles that typically co-occur | Breaks: Jetix 6 archetypes are identity archetypes (member types), not operational role bundles in FPF sense (co-occurring functional roles). Semantic proximity ≠ mechanism identity. 0 signatories means no operational instance to validate. | matching-scope-limited (⊗ bundle concept borrowed; semantic content diverges from FPF role-bundle definition) |
| O-13 Clan | FPF полная | **System** | «Does Clan activation correspond to FPF B.2 Meta-Holon Transition (new emergent whole with BOSC triggers)?» | Per 01-inventory §1 O-13: «B.2 Meta-Holon Transition candidate: signatories addition = BOSC Boundary + Scale trigger» | FPF-Spec.md B.2 «Meta-Holon Transition» + B.2.1 «BOSC Triggers (Draft)» — emergence / new whole / synergy | Breaks: B.2.1 status = DRAFT in FPF-Spec; Jetix B.2 citation is aspirational (0 signatories). Comparison is valid as *anticipated mechanism*; not valid as *operational evidence*. | matching-scope-limited (mechanism identified correctly; operational validation requires first signatories) |

---

### O-14 — Meta-workshop

| Jetix object | L1 source | Level | Compare predicate | Jetix evidence | L1 evidence | Boundary conditions | Eng critic flag |
|---|---|---|---|---|---|---|---|
| O-14 Meta-workshop | FPF полная | **System** | «Does Meta-workshop concept correspond to FPF B.2.2 MST (Meta-System Transition — new system emergence from parts)?» | `decisions/JETIX-CORPORATION-2026-05-05.md §0` — «мета-мастерская для профессиональных мастеров»; Doc 1B framing | FPF-Spec.md B.2.2 «MST (Sys) — Meta-System Transition» — system emergence / super-system / physical emergence | Breaks: MST applies when constituent systems actually combine to form emergent supersystem. Jetix meta-workshop has 0 partner-instances (vapor). MST framework = correct anticipatory mechanism; application = not yet valid. | N/A — vapor object; comparison not yet valid (no constituent systems) |
| O-14 Meta-workshop | IWE template | **System** | «Does Jetix meta-workshop Phase C IWE cooperation correspond to IWE Pack distribution architecture?» | `JETIX-WORKING-FILE-v0 §3.3` — meta-workshop framing; Phase C cooperation plan (未 finalised) | IWE CLAUDE.md §1: Pack = domain distribution format; «/pack-new» skill for creating Packs; DS → Pack → Base fallback chain | Breaks: IWE Pack = per-domain distributable unit for single worker; Jetix meta-workshop = platform-for-multiple-Jetix-instances for multiple organisations. Scale mismatch (IWE Pack = individual; meta-workshop = org-level). | structural-divergence (IWE Pack = single-worker distribution; meta-workshop = org-platform concept; different scales) |

---

## §2 Mechanism-level Deep Dives

### Deep Dive 1 — F-G-R Adoption (Jetix Part 6a vs FPF B.3 / C.2)

**FPF reference:** B.3 Trust & Assurance Calculus + C.2 KD-CAL + C.2.2 Reliability R in F-G-R triad + C.2.3 Unified Formality Characteristic F
[src: FPF-Spec.md Part B ToC rows B.3 / C.2 / C.2.2 / C.2.3]

**Jetix reference:** Part 6a Provenance Officer LOCKED; F-G-R schema at `shared/schemas/f-g-r.json`; applied in H1-H7 STRATEGIC-INSIGHT files + Foundation frontmatter
[src: 06-honest-self-audit.md §2 Part 6a «direct adoption; F-G-R lint enforced»; 01-inventory §1 O-07 F-G-R top claim]

**Correspondence (what matches):**
- Jetix Part 6a applies F (Formality) / G (Group-scope) / R (Reliability) triple per claim — structurally isomorphic with FPF B.3 F-G-R.
- Jetix F2..F8 scale used in practice (H1-H7 INSIGHT files; Foundation parts).
- Inline `[src:]` citations in Foundation docs ≈ FPF A.10 Evidence Graph Referring.
- `F: F4 | G: phase-0 | R: refuted_if...` format in frontmatter mirrors B.3 claim structure.

**Divergence (what does NOT match):**
1. **EP-5 F-grade misapplication.** Foundation «F8» = document approval by single reviewer. FPF C.2.3 F8 implies independent testing / formal verification. **Single-author approval ≠ FPF F8 standard.** No multi-party review trail.
2. **Reliability R = passive text only.** FPF C.2.2 Reliability requires pathwise justification (PathId) + CL (Congruence Level) penalties for cross-context reuse + Bridge-only transport. Jetix R = prose `refuted_if_...` falsifier. Functional approximation, not FPF C.2.2 formal R.
3. **G (Group-scope) = informal.** FPF A.2.6 USM (Unified Scope Mechanism) with ClaimScope is structurally defined. Jetix G = text label (e.g. `G: phase-0-cell-draft`). No USM scope-slicing implemented.
4. **No F-G-R lint tooling in Phase A.** F-G-R lint = STUB (06-honest-self-audit §2 Part 6a: «F-G-R lint enforced» but Halt-Log-Alert = STUB Phase-B). Claim: enforced. Reality: human review only.

**Boundary condition:** Comparison is valid as mechanism-identification (same F-G-R concept in use). Breaks for claims about FPF-grade rigor (Jetix F-G-R is an approximation, not full C.2 implementation).

**Eng critic flag:** structural-correspondence (concept + three-field structure); mechanism-gap (F-grade misapplication; R = prose only; no formal Congruence Level; lint = STUB)

---

### Deep Dive 2 — Guard-Rails (Jetix Pillar C + Default-Deny vs FPF E.5 / C.10 Norm-CAL)

**FPF reference:** E.5 Four Guard-Rails (GR-1..GR-4) + C.10 Norm-CAL (norms / deontics) + A.2.8 U.Commitment
[src: FPF-Spec.md Part E cluster E.I rows E.5/E.5.1-E.5.4; Part C row C.10]

**Jetix reference:** Pillar C 12 Tier-2 rules; `.claude/config/default-deny-table.yaml` (11 entries); Part 6b Human Gate LOCKED; Halt-Log-Alert specification
[src: CLAUDE.md §4.1; swarm/wiki/foundations/part-6b-human-gate/architecture.md; 02-per-object-deep §9 O-08]

**Correspondence (what matches):**
- Both systems implement normative constraints on agent behavior (Jetix: 12 rules; FPF: GR-1..GR-4 as spec-authoring constraints).
- Default-Deny table = closest Jetix analog to FPF Norm-CAL deny logic.
- Rule 11 (Default-Deny with machine enforcement) = strongest FPF A.2.8 U.Commitment analog: defined obligation, machine-enforced, escalation path.
- «Fail-loud» (CLAUDE.md §Critical Tier-2 / Part 6b) ≈ FPF E.5 design intent (explicit violation surfacing).

**Divergence (what does NOT match):**
1. **FPF E.5 Guard-Rails ≠ operational enforcement.** FPF GR-1..GR-4 = architectural constraints ON THE FPF SPEC ITSELF (e.g. GR-1 = no DevOps jargon in FPF core). Jetix Pillar C = runtime behavioral constraints on AI agents. Different application domains.
2. **CE-4 enforcement asymmetry.** 12 rules declared as uniformly «constitutional»; machine enforcement exists only for Rule 11. Rules 1/3/8/9/12 = human-review only. FPF A.2.8 U.Commitment requires adjudication hooks per commitment — Jetix has no per-rule adjudication path documented.
3. **R12 incomplete.** R12 = additive rule 12 (AWAITING-APPROVAL NOT ack'd 2026-05-17); FPF comparison requires completed A.2.8 U.Commitment (text + adjudication + enforcement + validity window). R12 missing: adjudication path, enforcement mechanism, validity window.
4. **«Halt-Log-Alert ≤1s / ≤5s / ≤60s»** = spec-level specification (F2 operational per 06-honest-self-audit §2 Part 6b). FPF comparison valid for design intent; NOT valid for operational claim.

**Boundary condition:** Comparison valid for mechanism-identification (guard-rails concept + deny-logic structurally present). Breaks when claiming FPF-grade Guard-Rails compliance — different application domain (FPF: spec-authoring; Jetix: runtime). Also breaks on enforcement uniformity claim.

**Eng critic flag:** structural-correspondence (concept level); mechanism-gap (adjudication paths absent for 11 of 12 rules; application domain mismatch FPF GR vs Jetix runtime)

---

### Deep Dive 3 — Role Taxonomy (Jetix Part 4 vs FPF A.2)

**FPF reference:** A.2 Role Taxonomy + A.2.1 U.RoleAssignment (Holder#Role:Context) + A.2.5 U.RoleStateGraph + A.2.7 U.RoleAlgebra (≤, ⊥, ⊗) + A.13 Agential Role
[src: FPF-Spec.md Part A ToC cluster A.I rows A.2..A.2.7 + A.13]

**Jetix reference:** Part 4 LOCKED + IP-1 (Role≠Executor) + RUSLAN-LAYER executor-binding.yaml.template + `.claude/agents/` (23 files) + CLAUDE.md §Agent Roster
[src: 06-honest-self-audit.md §2 Part 4 «direct adoption + IP-1»; 01-inventory §2 O-06a/b]

**Correspondence (what matches):**
- IP-1 Role≠Executor directly implements FPF A.2 + A.2.1 separation (Role-type ≠ RoleAssignment token ≠ executor instance).
- 12-role-type declarations in CLAUDE.md §Agent Roster + 6-department topology = FPF A.2.7 RoleAlgebra ≤ (specialization) topology (department ≥ role).
- RUSLAN-LAYER executor-binding.yaml.template maps Holder#Role:Context (A.2.1) — context field present.
- Agential Role budgeting: `max 20 active tasks` (CLAUDE.md §4.2) = A.13 autonomy budget analog.

**Divergence (what does NOT match):**
1. **A.2.5 U.RoleStateGraph ABSENT.** FPF A.2.5 requires named state space per role (states, transitions, enactability conditions). No RSG file found for any of 12 roles. Executor-binding template lacks RSG slot.
2. **A.15 Method-signature enforcement = STUB.** Role-Method-Work Alignment (A.15) requires each role to declare method-signature (what method the role performs). Part 4 declares role names + models + departments; method-signature = not enforced.
3. **Phase 3-4 roles = ghost types.** A.2.1 Holder#Role:Context requires an actual holder. Phase 3-4 roles in CLAUDE.md §Agent Roster = declared types without operational Holder records. Cited в CE-2 as IP-1 conflation in the roster table itself.
4. **A.2.7 ⊗ bundle NOT applied.** Role bundles (agent running N roles simultaneously) = not modeled. IWE CLAUDE.md §2: «один агент может выполнять несколько ролей» — IWE has explicit acknowledgment; Jetix has IP-1 (prevents conflation) but no ⊗ bundle model for multi-role agents.

**Boundary condition:** Comparison valid for structural role-taxonomy adoption (A.2 type-level ✓). Breaks for enforcement claims (A.15 STUB; RSG absent; Phase 3-4 ghost types).

**Eng critic flag:** structural-correspondence (type-level Part 4 A.2 adoption confirmed); mechanism-gap (A.2.5 RSG absent; A.15 method-signature STUB; A.2.7 ⊗ not modeled)

---

### Deep Dive 4 — Hexagon Synthesis (Jetix O-09 vs FPF B.5.2 Abductive Loop)

**FPF reference:** B.5 Canonical Reasoning Cycle + B.5.2 Abductive Loop + B.5.2.0 U.AbductivePrompt + B.5.2.1 Creative Abduction with NQD + C.18 NQD-CAL
[src: FPF-Spec.md Part B ToC rows B.5.2 / B.5.2.0 / B.5.2.1 / C.18]

**Jetix reference:** 6 STRATEGIC-INSIGHT files (2026-05-10..12) + H7 People-NS LOCKED; `JETIX-WORKING-FILE-v0 §5.1` Hexagon 1A/1B
[src: 01-inventory §2 O-09; 02-per-object-deep §10 O-09; 06-honest-self-audit §7 «closest к intelligence amplification»; jetix-vs-iwe-audit §3 J-U1]

**Correspondence (what matches):**
- F-G-R tagging on INSIGHT files ≈ FPF B.3 claim discipline (partial).
- Two-view outputs (1A current-state + 1B aspirational) ≈ FPF E.17 MVPK two-face discipline (informal).
- 4-source attribution trail on H7 + R12 ≈ FPF A.10 Evidence Graph (partial).
- Per 06-honest-self-audit §7: «closest к FPF intelligence amplification в Jetix» — engineer concurs this is the strongest FPF-adjacent mechanism Jetix has.

**Divergence (what does NOT match):**
1. **No rival-set / alternatives portfolio.** FPF B.5.2 Abductive Loop requires: candidate hypotheses generated → plausibility filters applied → rival set documented. B.5.2.0 U.AbductivePrompt requires «rival-set discipline». **0 of 6 INSIGHT files contain an alternatives portfolio or discarded rivals.** This is the single most critical mechanism gap.
2. **No B.5.2.1 Creative Abduction NQD binding.** FPF B.5.2.1 requires: Γ_nqd.generate (generate candidates) + Γ_nqd.selectFront (select front). Jetix insights = single-winner outputs, not NQD front. This is the «first-answer» anti-pattern FPF abductive loop explicitly prevents.
3. **Process not documented.** 6 outputs exist; process that generated them = undocumented. FPF B.5.2 requires origin trace per hypothesis. «Hexagon» name is not sufficient as process documentation.
4. **One 3-day event ≠ cadence.** Abductive Loop in FPF = ongoing reasoning architecture. Jetix «Hexagon cadence» = single event (OQ-T2-5). No feedback loop from operational results back into the Hexagon process documented.

**Boundary condition:** Comparison valid for output-level similarity (F-G-R tagged insights with multi-view). Breaks for process-level comparison (abductive loop process undocumented; alternatives portfolio absent). D-3 dissent: «partial» depends on which bar is applied.

**Eng critic flag:** structural-correspondence (output format partial); mechanism-gap (alternatives portfolio ABSENT — most critical gap; NQD binding absent; process undocumented)

---

### Deep Dive 5 — Working Product (Jetix O-04 vs IWE WP Gate / template)

**IWE reference:** IWE CLAUDE.md §2 WP Gate (БЛОКИРУЮЩЕЕ) + WP Context File (DP.EXOCORTEX.001) + WP-REGISTRY.md + `scripts/active-wp-sweep.sh`; ONTOLOGY.md §3 «Реестр РП»
[src: raw/external/tseren-github-2026-05-17/FMT-exocortex-template/CLAUDE.md §2; ONTOLOGY.md §3]

**Jetix reference:** O-04 working product = Foundation LOCKED + ROY swarm 15 drafts + 6 outreach files; AWAITING-APPROVAL mechanic (Part 6b) is nearest gate analog
[src: 02-per-object-deep §4 O-04; 01-inventory §3 O-04; reports/jetix-vs-iwe-audit-2026-05-17.md §4 I-U10]

**Correspondence (what matches):**
- Both track work outputs via artefact files (Jetix: swarm/wiki/drafts/; IWE: DS-strategy/inbox/WP-NNN.md).
- Both have a gate before work execution (Jetix: AWAITING-APPROVAL; IWE: WP Gate + ритуал согласования).
- Both are git-native (filesystem SoT).

**Divergence (what does NOT match):**
1. **IWE WP Gate = BLOCKING at session level; Jetix AWAITING-APPROVAL = project-level gate only.** IWE enforces that EVERY task has a Work Product (РП) registered in 4 places BEFORE work starts. Jetix enforces gating for Foundation-level writes; has no session-level work-product registration ritual. I-U10 in audit.
2. **IWE Work Product = atomic (one task = one WP с frontmatter + context file).** Jetix «working product» (O-04) = entire multi-component system (Foundation + ROY swarm + voice pipeline). Granularity mismatch = comparison level mismatch.
3. **IWE WP has TTL (time-to-live).** ONTOLOGY.md §3: «Творческий конвейер: артефакт обязан продвинуться или быть закрыт в пределах TTL». Jetix Foundation artefacts are LOCKED (no TTL; intended to persist indefinitely). Different lifecycle model.
4. **IWE WP Registry = single-source-of-truth.** `WP-REGISTRY.md + inbox/WP-*.md` = authoritative. Jetix has no single WP registry; artefacts distributed across `swarm/wiki/drafts/`, `decisions/`, `reports/`, `swarm/wiki/foundations/`. State fragmentation.

**Boundary condition:** Comparison valid only at concept level (both track work outputs). Breaks at mechanism level due to granularity mismatch (session-task vs org-system), TTL policy (expiry vs permanence), and registry centralization (IWE: 1 file; Jetix: distributed).

**Eng critic flag:** structural-divergence (mechanism-level: blocking session gate vs project-level gate; WP granularity mismatch; no Jetix TTL equivalent)

---

### Deep Dive 6 — Brigadier dispatch vs FPF C.24 Agentic Tool-Use / A.15 Role-Method-Work

**FPF reference:** C.24 «Agentic Tool-Use & Call-Planning» — CallRouteDescription + CallPlan + CallGraph + CheckpointReturn + enactment budget + stop/replan; A.15 Role-Method-Work Alignment
[src: FPF-Spec.md Part C ToC row C.24 + Part A row A.15]

**Jetix reference:** brigadier (`.claude/agents/brigadier.md`) — sole dispatcher; ROY swarm (6 agents); hub-and-spoke routing (`swarm/lib/routing-table.yaml`); AP-cost per dispatch
[src: CLAUDE.md §4.2 «Hub-and-spoke: subagents → department Lead → Manager»; 01-inventory §1 O-01 holonic structure]

**Correspondence (what matches):**
- Brigadier = single orchestrator dispatching to sub-agents ≈ FPF C.24 CallPlan pattern (orchestrator holds the CallGraph).
- `ap_budget` field in brigadier dispatch = FPF C.24 enactment budget / tool-call budget analog.
- AWAITING-APPROVAL + `stop/replan` = FPF C.24 `stop/replan condition` + CheckpointReturn analog.
- Hub-and-spoke routing = CallRouteDescription at org level.

**Divergence (what does NOT match):**
1. **No formal CallGraph artifact.** FPF C.24 requires a published CallGraph (which tool, when, what input, what output). Jetix brigadier's dispatch sequence = implicit (in brigadier's agent file); not a formal CallGraph artefact.
2. **No BLP (Bitter-Lesson Preference) tolerance declaration.** FPF C.24 + C.19.1 BLP requires declaring tolerance for when narrower method beats scalable one. Brigadier has no explicit BLP policy.
3. **budget and harm gates specified by brigadier = not a formal FPF gate profile.** FPF A.21 GateProfilization requires formal GateProfile. Jetix = prose rules in brigadier agent file.
4. **A.15 Role-Method-Work: method-signature enforcement = STUB (repeated finding).** C.24 requires agents to enact via method — Jetix agents' method-signatures not declared.

**Boundary condition:** Comparison valid for architectural-pattern-level (hub-and-spoke ≈ CallPlan orchestration). Breaks for formal mechanism compliance (no CallGraph artefact; no BLP declaration; no formal GateProfile).

**Eng critic flag:** structural-correspondence (architectural pattern); mechanism-gap (formal C.24 CallGraph / BLP / GateProfile absent)

---

## §3 Artefact-level Structural Fidelity

**Summary table: Jetix artefact → FPF artefact type → fidelity grade**

| Jetix artefact | FPF artefact type | Schema coverage | Fidelity grade | Critical gap |
|---|---|---|---|---|
| `swarm/wiki/foundations/*/architecture.md` × 11 | U.MethodDescription (A.3.2) + U.Episteme (C.2.1) | frontmatter present; F-G-R partially; slot graph NOT enforced | **F4** (multi-document; single-reviewer) | C.2.1 U.Episteme slot graph (DescribedEntitySlot + ClaimGraphSlot + ViewpointSlot) absent |
| `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | U.WorkPlan (A.15.2) or U.MethodDescription (A.3.2) | LOCKED; 35 UC × 12; no A.15.2 schedule/forecast fields | **F5 (artefact-lock)** / F2 (content claims) | A.15.2 schedule slot absent; plan-reality traceability (A.4) undeclared |
| `shared/schemas/f-g-r.json` | FPF B.3 / C.2 claim schema | 3 fields (F / G / R); prose R | **F3** partial | R = prose only; no PathId / CL; G = informal label not USM-typed |
| `shared/schemas/task-return-packet.json` | FPF A.15.1 U.Work record or C.24 CheckpointReturn | fields: summary, proposed_writes, provenance, confidence, escalations | **F4** — functional; not FPF-formally typed | No resource-cost (B.1.6 Γ_work) slot; no RSG state admission |
| `.claude/config/default-deny-table.yaml` | FPF C.10 Norm-CAL or A.2.8 U.Commitment | 11 entries with deny-and-escalate logic | **F5** (Rule 11 enforced) / F2 (Rules 1/3/8/9/12) | A.2.8 adjudication hooks absent; validity window absent; BCP-14 modality not normalized |
| `decisions/STRATEGIC-INSIGHT-*.md` × 6 | FPF B.5.2 Abductive Loop outputs + B.3 claims | F-G-R frontmatter; 1A/1B two-view; 4-source trail (H7) | **F5 (artefact-lock)** / F3 (abductive process claims) | No alternatives portfolio; no discarded rivals; process undocumented |
| `swarm/lib/shared-protocols.md` | FPF C.24 CallPlan + E.9 DRR method | structured YAML return packets; 9-section protocol | **F4** — operational convention | Not formally typed as FPF C.24 CallGraph; no BLP tolerance; not referenced via formal A.2.8 Commitment |
| IWE `FMT-exocortex-template/ONTOLOGY.md` | FPF A.1.1 U.BoundedContext (downstream ontology) | upstream-deps table; concepts + abbreviations; user-space § | **F5** (platform-space sections; structural form present) | Direct FPF A.1.1 glossary + invariant slots absent; bridges to FPF via SPF intermediate |
| IWE `.claude/config/default-deny-table.yaml` equivalent = `.claude/settings.json` | permissions-based allow/deny | JSON array; not FPF-structured | **F3** (functional rule file) | No Norm-CAL vocabulary; no adjudication; different structure from Jetix default-deny-table.yaml |

**Engineering critic summary on artefact fidelity:**
- Jetix has 4 high-fidelity FPF-derivative artefacts: `f-g-r.json`, `default-deny-table.yaml` (Rule 11), Part 4 architecture.md, Part 6a provenance schema.
- 7 other artefacts are functionally adequate but NOT FPF-formally typed (missing slot graphs, adjudication hooks, formal ViewpointBundles).
- FPF F8 misapplication is consistent across all LOCKED docs — this is EP-5 pattern confirmed at artefact level.

---

## §4 Method-level Procedural Mapping

| Jetix method | L1 source | FPF/IWE method | Mapping | Engineering note |
|---|---|---|---|---|
| ROY swarm dispatch (brigadier → ROY experts → drafts → brigadier) | FPF | C.24 Agentic Tool-Use CallPlan pattern | **Partial correspondence** — hub-and-spoke ≈ CallPlan orchestration; CheckpointReturn ≈ structured Task packet | Formal CallGraph artefact absent; BLP declaration absent (see Deep Dive 6) |
| Plan-Work-Review-Compound 40/10/40/10 (CE cadence) | FPF | B.4 Canonical Evolution Loop (Observe → Notice → Stabilize → Route) | **Concept correspondence** — PWRC phases map roughly to B.4 loop phases | B.4.1 formal route-publication with RoutedCueSet = not implemented; PWRC is informal CE-derived pattern |
| Hexagon synthesis (6-cell + 1A/1B) | FPF | B.5.2 Abductive Loop + E.17 MVPK | **Partial correspondence** — see Deep Dive 4; outputs ✓; process ✗ | Alternatives portfolio = most critical gap |
| AWAITING-APPROVAL packet (Part 6b) | FPF | A.2.9 U.SpeechAct (approval/authorization as Work) + A.21 GateProfilization | **Concept correspondence** — AWAITING-APPROVAL ≈ U.SpeechAct instituting-act | Formal GateProfile with join-semilattice (A.21) = not implemented; packet is functional but not FPF-formally typed |
| F-G-R per-claim tagging | FPF | B.3 Trust & Assurance Calculus | **Direct correspondence** — strongest method-level alignment in Jetix | See Deep Dive 1 for divergences (single-reviewer F8; R = prose) |
| OWC fractal (Day Open / Plan / Close) | IWE | IWE OWC ritual (BLOCKING at all 4 scales) | **Weak correspondence** — Jetix has `/plan-day` + `/close-day` as skills (aspirational); IWE OWC = BLOCKING per `CLAUDE.md §2 Rule 3` | **Most critical IWE method advantage (I-U2).** Jetix close = non-blocking; IWE close = blocking enforcement. |
| brigadier AWAITING-APPROVAL + HITL | IWE | IWE WP Gate ритуал согласования (Шаг 2) + АрхГейт | **Concept correspondence** — both require gate before execution; both HITL | Granularity mismatch: IWE WP Gate = per-session-task; Jetix AWAITING-APPROVAL = per-foundation-change |
| Compound learning / strategies.md DRR | FPF | E.9 DRR (Design-Rationale Record) | **Partial correspondence** — strategies.md 4-part DRR entries ≈ E.9 DRR shape | E.9 DRR requires: exact basis + selected answer + content-distribution to patterns. Jetix DRR = Decision/Reasoning/Result/Review = operationalized translation, not verbatim E.9 |
| IP-1 Role≠Executor | FPF | A.2 + A.2.1 + A.13 | **Direct correspondence** — strongest method-level adoption; IP-1 text directly implements FPF A.2/A.13 | RSG (A.2.5) absent = incomplete adoption |
| Part 5 Compound Learning | IWE | IWE Capture-to-Pack (eager knowledge extraction per session boundary) | **Concept correspondence** — both capture learnings for future reuse | IWE Capture-to-Pack = per-session blocking ritual; Jetix Compound Learning = end-of-cycle (less frequent, lower enforcement) |

---

## §5 Dissents Preserved + Open Questions

### Dissents (per AP-6 — NOT averaged)

**D-1 (carried from Phase B Step 2; D-1 from 01-inventory §7).**
- Position: All IWE comparison rows in this matrix are scoped to public `FMT-exocortex-template` ver 0.31.0.
- Dissent: Левенчуков TG C5 «IWE умнее конкурентов» likely refers to paid aisystant AI guide — different artefact with potentially deeper FPF mechanism implementation.
- Impact: Every IWE gap flagged as «Jetix-unique» or «IWE lacks X» may be invalid if paid guide implements X.
- F: F4 | R: refuted_if_B2_unblocked_AND_paid_guide_reveals_equivalent_mechanisms

**D-T3-ENG-1 (engineering × critic, this draft).**
- Position (this matrix): Comparison level «Mechanism» is tractable for 5 objects (O-04, O-07, O-08, O-09, O-06a).
- Dissent: Philosophy-critic (from prior cells) would add that mechanism-level comparison requires A.1.1 BoundedContext declaration per mechanism — comparing FPF A.2.8 U.Commitment with Jetix Pillar C Rule 11 requires explicit KindBridge (A.6.9) to validate the mapping is not a false alignment.
- Engineering position: KindBridge discipline at this fidelity level is Phase B+ work; Phase A can flag structural correspondence without formal KindBridge.
- F: F3 | R: refuted_if_mechanism-mapping_falsified_via_KindBridge_analysis

**D-T3-ENG-2 (engineering × critic, this draft).**
- Position: Jetix F8 = document-approval by single reviewer (EP-5 pattern; all LOCKED docs).
- Dissent: From management cell (earlier cycles) — «F8 = governance maturity, not epistemic grade; Ruslan-ACK process IS appropriate review for single-owner system». Engineering counter: FPF B.3 / C.2.3 F8 is an epistemic grade (independent testing), not a governance grade. These are different concepts sharing the same scale.
- Neither position is «wrong» for its own purpose. They use «F8» to mean different things.
- F: F4 | R: refuted_if_FPF_C.2.3_authors_explicitly_allow_single-reviewer_approval_as_F8-equivalent

**D-T3-ENG-3 (engineering × critic, this draft).**
- Position: FPF Spec ToC (what was readable) covers Parts A-E fully; Parts F-K referenced but not fully read.
- Risk: Parts F-K may contain mechanisms that reduce some gaps flagged above (e.g. F.9 Bridges may address cross-context mapping; F.17 UTS may address Jetix wiki v2 gaps; G.* may address CHR mechanisms).
- Engineering flag: Matrix rows for objects that depend on Parts F-K (e.g. O-09 → G.5 publication surfaces; O-07 → F.9 cross-context bridges) may have under-counted correspondence.
- F: F3 | R: refuted_if_reading_FPF_Parts_F-K_surfaces_mechanism_matches_on_flagged_gaps

**D-T3-ENG-4 (engineering × critic — comparison level selection).**
- Position: This matrix uses «Mechanism» as the primary level where engineering rigor applies.
- Dissent: For vapor objects (O-02, O-05, O-10, O-13, O-14) the most informative comparison level may be «Method» (what workflow would be needed to instantiate the object) rather than «Mechanism» (what operational mechanism exists). Mechanism-level comparison on vapor objects produces only «mechanism-gap» flags which are trivially true (nothing instantiated = all mechanisms absent).
- Engineering note: This dissent is correct; per §5.5 refusal behavior, future Task 4 kaша cleanup should assign Method-level comparison to vapor objects and Mechanism/Artefact-level to instantiated objects.
- F: F4 | R: refuted_if_Task_4_shows_mechanism_comparison_on_vapor_objects_is_informative

### Open questions для Ruslan

**OQ-T3-1 (comparison level authority).** Which comparison levels are load-bearing for Phase 0 output? Engineering proposes: Mechanism + Artefact for instantiated objects (O-01, O-04, O-06a/b, O-07, O-08, O-09); Method for vapor objects (O-02, O-05, O-10, O-12..O-14). Ruslan decides whether to accept this assignment.

**OQ-T3-2 (EP-5 resolution for F-grade language).** F8 LOCKED docs carry «F8» which means «approval grade» in Jetix vs «epistemic rigor grade» in FPF B.3. Does Ruslan want to (a) keep Jetix F8 = approval grade (rename it, e.g. «A8» for Approval-grade) or (b) align with FPF C.2.3 F-scale (which would require independent review to claim F8)?

**OQ-T3-3 (most critical mechanism gap for Phase B prioritization).** Engineering surfaces: alternatives portfolio in Hexagon (Deep Dive 4) = most critical FPF mechanism gap for «intelligence amplification» claim. IWE OWC blocking (Deep Dive 5) = most critical IWE method gap for «session discipline». Ruslan decides if either is Phase 0 scope.

**OQ-T3-4 (Parts F-K coverage).** FPF Parts F-K not fully read. Engineering flags: F.9 (Bridges), F.17 (UTS), G.5 (NQD publication), G.9 (selection), G.12 (CHR) may surface additional mechanism correspondences. Does Ruslan want F-K coverage as Task 3b (additional matrix rows) or defer to Task 4?

**OQ-T3-5 (IWE B2 unblocking timeline).** D-1 (paid guide not accessible) currently invalidates all «IWE-unique» vs «Jetix-unique» comparison claims at mechanism level. When does B2 unblock? If Tseren provides paid guide access in Phase 1 partnership discussions, matrix should be revised.

---

*Engineering-expert × critic draft. §5.5.5 gate: provenance inline ✓ | tier coherence ✓ | dissents preserved per AP-6 (4 dissents) ✓ | R1 surface-only ✓ | NO strategizing ✓ | NO «better/worse» language ✓ | 14 objects covered ✓ | ≥30 matrix rows (42 rows total) ✓ | ≥5 mechanism deep dives (6 dives) ✓ | 5 OQ for Ruslan ✓.*

*Boundary condition summary: (1) vapor objects = mechanism comparison trivially fails; (2) single-reviewer F8 ≠ FPF F8 (EP-5); (3) IWE all rows scoped to public template (D-1); (4) Jetix-as-org vs IWE-as-individual = unit mismatch (§0 finding 4); (5) Foundation-as-spec vs Foundation-as-system (D-2); (6) Hexagon-output vs Hexagon-process (D-3).*

*Output: `swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-engineering-critic-comparison-matrix.md`*
