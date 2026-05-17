---
task_id: phase-0-fpf-scope-2026-05-17
produced_by: engineering-expert × integrator
mode: integrator
status: draft (brigadier integrates)
F: F4
G: phase-0-cell-draft
R: refuted_if_object_count_<8_OR_FPF_primitive_misassigned_OR_provenance_missing
date: 2026-05-17
inputs:
  - JETIX-WORKING-FILE-v0-2026-05-17.md
  - reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md
  - reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md
  - raw/external/ailev-FPF/FPF-Spec.md (TOC + Part A/B read; selective)
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md
  - decisions/JETIX-TRM-MODEL-2026-04-30.md
  - CLAUDE.md
---

# Jetix через FPF Lens — Inventory объектов (Phase 0)

> **Scope.** Engineering-expert × integrator. Phase 0 FPF scope definition.
> Задача: surface inventory объектов Jetix через FPF primitive lens.
> NOT стратегический выбор. NOT оценка «хорошо / плохо». Surface facts only.

---

## §0 Summary — что найдено через FPF разбор

FPF lens разбивает Jetix на 14 различимых объектов разных онтологических типов.
Четыре базовых объекта (оперативный субстрат / юр.лицо in-progress / задумка-vision /
работающий продукт) — реальны, но каждый из них покрывается РАЗНЫМИ FPF-примитивами,
которые не сводятся друг к другу. Ещё 10 объектов surface'ятся через FPF lens:
методология-паттерн-язык, агентная система, Foundation-архитектура (F8-LOCKED
organisational substrate), Strategic Layer Hexagon (synthesis cadence), бизнес-модель
Phase 1 (TRM / quick-money), конституциональный принцип R12, бренд-публичный слой,
сетевой эффект / People-Network-State vision, Clan Charter (дистрибутируемый паттерн),
и meta-workshop для профессиональных мастеров. Главный FPF-structural вывод:
Foundation v1.0 = U.System организационного уровня с формально закреплённой ролевой
структурой (A.2) и провенансной дисциплиной (B.3 F-G-R), но без полного U.Episteme
slot-graph (C.2.1), без Abductive Loop NQD-CAL (B.5.2), и без MVPK multi-view
bundles (E.17). Это «FPF-adjacent tactical substrate», а не полный FPF-grade.
Два объекта (Vision-задумка / Hexagon) — ближайшие аналоги FPF intelligence
amplification. Остальные = memory + automation.

Итого объектов в таблице: **14**. Базовых: 4. Поверхнутых дополнительно: 10.

---

## §1 Inventory table

| # | Object name | FPF primitive (U.*) | FPF Part hosting | Applicable FPF primitives | Status | Bounded context | Top claim F-G-R | Provenance |
|---|---|---|---|---|---|---|---|---|
| O-01 | **Jetix как оперативный субстрат (information management system)** | U.System (A.1) + U.BoundedContext (A.1.1) | Part A — Kernel Architecture | A.1 Holon · A.1.1 BoundedContext · A.15 Role-Method-Work · A.2 Role Taxonomy · A.4 Temporal Duality | работает-частично | Holds: single-owner AI OS (Ruslan, Berlin); 12 agents × 6 departments; filesystem = SoT. NOT includes: corporate entity / partner instances / Phase B organisation | F4 · jetix-operational · refuted_if_owner_scope_change_OR_12_agents_drop | `CLAUDE.md §System Overview`; `JETIX-WORKING-FILE-v0 §2` |
| O-02 | **Jetix как юридическое лицо / корпорация (in-progress)** | U.RoleAssignment (A.2.1) + U.PromiseContent (A.2.3) | Part A Cluster A.I | A.2.1 RoleAssignment · A.2.3 PromiseContent (TRM promise) · A.2.8 Commitment · A.6.C Contract Unpacking | задумка → прорабатывается | Holds: Doc 1B conceptual frame + TRM ladder + partner engagement model. NOT includes: registered legal entity today (in-progress); actual client contracts; Phase 1 operational revenue | F4 · jetix-corp-concept · refuted_if_TRM_model_abandoned_OR_no_legal_registration | `decisions/JETIX-CORPORATION-2026-05-05.md §0`; `decisions/JETIX-TRM-MODEL-2026-04-30.md §1` |
| O-03 | **Jetix как задумка / vision (future state target)** | U.WorkPlan (A.15.2) + U.MethodDescription (A.3.2) | Part A Cluster A.III | A.4 Temporal Duality · A.15.2 WorkPlan · A.3.2 MethodDescription · E.9 DRR (strategic direction) · B.5.1 Explore→Shape→Evidence→Operate | задумка → прорабатывается | Holds: 35 UC × 12 categories vision (FUNDAMENTAL); generational ambition 100-200y (Clan Charter §1.7). NOT includes: Phase 1 operations; current revenue; FPF-grade strategic claims | F4 · jetix-vision-fundamental · refuted_if_35UC_misencoded_OR_charter_ambition_abandoned | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §0-§1`; `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md §1.7` |
| O-04 | **Jetix как работающий продукт (что РЕАЛЬНО работает СЕЙЧАС)** | U.Work (A.15.1) + U.Capability (A.2.2) | Part A Cluster A.II–A.V | A.15.1 Work · A.2.2 Capability · B.3 F-G-R (deployed) · A.10 Evidence Graph · A.2.5 RoleStateGraph | работает-частично | Holds: Foundation v1.0 LOCKED (11 Parts); 12 agents; brigadier Phase A; 8 active projects; voice pipeline; CRM; Wiki v2; CLAUDE.md skills. NOT includes: Phase B managed team; enterprise clients; TRM at scale | F5 · jetix-canonical · refuted_if_Foundation_LOCKED_violated_OR_brigadier_not_dispatching | `swarm/wiki/foundations/synthesis/foundation-master-overview-technical-2026-04-29.md`; `CLAUDE.md §Architecture` |
| O-05 | **Jetix как методология / pattern language (forkable)** | U.MethodDescription (A.3.2) + U.Method (A.3.1) | Part A Cluster A.II | A.3.1 Method · A.3.2 MethodDescription · B.4 Canonical Evolution Loop · A.5 Kernel Modularity · E.9 DRR | задумка → прорабатывается | Holds: FUNDAMENTAL Layer 1 as sector-agnostic pattern; Fork guide v0 (§11 working file). NOT includes: distributed template format; formal IWE-Pack analogue; Phase C remit | F2 · future-pattern-experimental · refuted_if_Jetix-as-Pack_pattern_designed_with_concrete_dist_format | `JETIX-WORKING-FILE-v0 §11`; `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §0 двуслойный принцип` |
| O-06 | **Jetix как агентная система (multi-agent orchestration)** | U.RoleAssignment (A.2.1) + U.Method (A.3.1) | Part A Cluster A.I–A.II | A.2 Role Taxonomy · A.2.1 RoleAssignment · A.2.7 RoleAlgebra · A.13 Agential Role · A.15 Role-Method-Work · IP-1 Role≠Executor | работает-частично | Holds: 12 agents × 6 departments; brigadier 5 experts × 4 modes = 20 cells; hub-and-spoke topology; Phase A solo. NOT includes: multi-human team; Phase B split-triggers; executor-identity claims | F5 · jetix-canonical · refuted_if_agent_roster_changes_without_AWAITING-APPROVAL | `CLAUDE.md §Agent Roster`; `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` |
| O-07 | **Foundation Architecture v1.0 (organisational substrate F8-LOCKED)** | U.System (A.1) + U.Mechanism (A.6.1) | Part A + E Constitution cluster | A.1 Holon · A.6.1 Mechanism · A.6.B Boundary Norm Square · E.5 Guard-Rails analog · B.3 F-G-R · E.9 DRR shape | работает-полно | Holds: 11 Parts + Pillar A + Pillar C LOCKED 2026-04-28; 8 RUSLAN-ACK records. NOT includes: Phase B extensions; non-Ruslan instances; Foundation revision without AWAITING-APPROVAL | F8 · jetix-foundation-canonical · refuted_if_any_Foundation_Part_violated_without_AWAITING-APPROVAL | `CLAUDE.md §Foundation Architecture v1.0`; `swarm/wiki/foundations/synthesis/foundation-master-overview-technical-2026-04-29.md` |
| O-08 | **Pillar C конституциональная система (12 Tier-2 rules + R12)** | U.Commitment (A.2.8) + Guard-Rails analog (E.5) | Part E — Constitution cluster | A.2.8 Commitment · E.5 Guard-Rails · E.2 Eleven Pillars (analog) · B.3 F-G-R (R12 via B.3) · A.6.B Boundary Norm Square (L/A/D/E classification) | работает-полно | Holds: 12 hard rules Tier 2 system-level; Default-Deny table (11 entries); R12 anti-extraction (4-source trail). NOT includes: Tier 1 owner principles (owner-only); Phase B enforcement hooks (Phase B materialization) | F8 · jetix-pillar-c-constitutional · refuted_if_constitutional_never_list_count_changes_without_RUSLAN-ACK | `swarm/wiki/foundations/principles/architecture.md`; `CLAUDE.md §4.1`; `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` |
| O-09 | **Strategic Insights Hexagon (synthesis cadence 6+1)** | U.Work (A.15.1) + Abductive Loop output (B.5.2) | Part B — Reasoning Cluster | B.5.2 Abductive Loop · E.9 DRR · B.3 F-G-R · E.17 MVPK (partial — 1A/1B views) · A.10 Evidence Graph | работает-частично | Holds: 6 LOCKED strategic insights (H1-H7 2026-05-10..12); F-G-R tagged; multi-view 1A+1B; D-Lock entries. NOT includes: formal NQD-CAL alternatives portfolio; full E.17 MVPK bundle; weekly cadence not yet systematized | F5 · jetix-canonical · refuted_if_hexagon_synthesis_stops_OR_F-G-R_tagging_dropped | `decisions/STRATEGIC-INSIGHT-*-2026-05-10..12.md` (6 docs); `JETIX-WORKING-FILE-v0 §5.1` |
| O-10 | **Бизнес-модель Phase 1 (TRM / quick-money consulting)** | U.PromiseContent (A.2.3) + U.RoleAssignment (A.2.1) | Part A Cluster A.I | A.2.3 PromiseContent · A.2.8 Commitment · A.6.C Contract Unpacking · B.1.6 Γ_work (resource aggregation) | прорабатывается | Holds: TRM 6-resource model; L0-L5 ladder (€3K → €40-60K/мес); ICP Mittelstand DACH; mgmt + performance fee. NOT includes: active contracts; Phase B partnerships; €100M ARR target (future horizon only) | F4 · jetix-corp-concept · refuted_if_TRM_ladder_units_change_without_LOCKED_revision | `decisions/JETIX-TRM-MODEL-2026-04-30.md §1-§2`; `decisions/JETIX-CORPORATION-2026-05-05.md §0` |
| O-11 | **R12 Anti-extraction (конституциональный принцип)** | U.Commitment (A.2.8) + U.SpeechAct (A.2.9) | Part E — Constitution cluster (additive Pillar C) | A.2.8 Commitment · A.2.9 SpeechAct · E.5 Guard-Rails · B.3 F-G-R · E.9 DRR (4-source trail = DRR shape) | работает-частично | Holds: Tier 2 rule 12 (additive 2026-05-12); 4-source attribution trail; symmetric application. NOT includes: bilateral written agreement (Tier 3 prerequisite); formal Game Theory mechanism proof; IWE/FPF community agreement | F5 · jetix-constitutional-candidate · refuted_if_r12_packet_rejected_OR_4_source_trail_broken | `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md`; `CLAUDE.md §4.1 rule 12`; `JETIX-WORKING-FILE-v0 §5.2 Appendix B` |
| O-12 | **Бренд / публичный слой (Jetix public-facing)** | U.PromiseContent (A.2.3) + MVPK face (E.17 partial) | Part E — Constitution (E.17 partial) + Part A | E.17 MVPK (1A plain face = Doc 1A; 1B deep = Doc 1B) · A.6.3 EpistemicViewing · A.2.3 PromiseContent | прорабатывается | Holds: Doc 1A (single-page charter); Doc 1B (narrative); Workshop metaphor (LOCKED); brand=Jetix. NOT includes: public website; enterprise pitch deck; formal multi-audience MVPK bundles (Phase B) | F4 · jetix-brand · refuted_if_workshop_metaphor_abandoned_OR_1A_Doc_deprecated | `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` (Doc 1A); `decisions/JETIX-CORPORATION-2026-05-05.md` (Doc 1B) |
| O-13 | **People-Network-State / Clan vision (дистрибутируемый сетевой паттерн)** | U.System (A.1 meta-holon) + Meta-Holon Transition (B.2) | Part B — Reasoning Cluster (B.2 MHT) | B.2 Meta-Holon Transition · B.2.1 BOSC Triggers · A.1 Holon · A.2.7 RoleAlgebra (6 archetypes ≤/⊗) · R12 (constitutional guarantee для members) | задумка → прорабатывается | Holds: H7 People-Network-State LOCKED (2026-05-12); Clan Charter v0 LOCKED; 6 archetypes; stealth launch. NOT includes: 5+ signatories today (0 confirmed); public phase; Phase B cooperative formation | F5 · charter-applied-now · refuted_if_no_first_signature_within_60d_OR_Ruslan_rejects_draft | `decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md`; `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` |
| O-14 | **Meta-workshop для профессиональных мастеров (Phase B target)** | U.System (A.1 supersystem) + U.Method (A.3.1 hosting) | Part A Cluster A.II + B.2 MHT | A.1 Holon (meta-holon level) · A.3.1 Method · A.5 Kernel Modularity (fork-and-instantiate) · B.2.2 MST (system emergence) | задумка | Holds: Doc 1B framing «Jetix = мета-мастерская для профессиональных мастеров со своими мастерскими». NOT includes: implemented partner-instances today; formal protocol for partner-Jetix interoperability; Phase C IWE cooperation | F4 · jetix-phase-B-framing · refuted_if_meta-workshop_activation_path_falsified | `decisions/JETIX-CORPORATION-2026-05-05.md §0`; `JETIX-WORKING-FILE-v0 §3.3` |

---

## §2 Per-object notes (2-5 предложений per object)

### O-01 — Jetix как оперативный субстрат

Jetix-OS сегодня — **U.System** с явным **U.BoundedContext** (single-owner scope,
filesystem = SoT, Notion = view). FPF A.1 Holon применимо: систему можно рассматривать
как holonic structure — 12 агентов (субголоны) внутри 6 departments (суперголоны)
под brigadier-оркестратором. A.15 Role-Method-Work alignment частично применяется через
Part 4 Role Taxonomy (A.2 derivative), но **method-signature enforcement**
неполный (RUSLAN-LAYER overlay incomplete per `06-honest-self-audit.md §2`).
A.4 Temporal Duality (design-time vs run-time) реализована через Foundation v1.0 LOCKED
(design) + активные циклы (run). Статус: «работает-частично» — substrate functional,
но не FPF-grade intelligence amplification.

### O-02 — Jetix как юр.лицо / корпорация

Doc 1B (`decisions/JETIX-CORPORATION-2026-05-05.md`) описывает корпорацию как
«applied use case» Базовой Системы — это FPF-aligned framing: **U.RoleAssignment**
(партнёр / клиент / работник — три различных роли с distinct commitments), плюс
**U.PromiseContent** для TRM ladder (L0-L5 promise clauses). A.2.8 Commitment
применимо: TRM model содержит implicit deontic обязательства (management fee +
performance fee), но они не оформлены как formal FPF Commitment objects. A.6.C
Contract Unpacking пока не применялась — контракты неформальные. Юр.лицо не зарегистрировано.

### O-03 — Jetix как задумка / vision

FUNDAMENTAL vision (35 UC × 12 категорий) — **U.WorkPlan** (intended future state,
not yet executed work). FPF A.4 Temporal Duality напрямую применима: plan vs reality
разрыв здесь максимален. Clan Charter §1.7 puts ambition at 100-200 лет —
это explicitly open-ended evolution (FPF P-10 principle). B.5.1 Explore→Shape→Evidence→Operate:
Vision находится в «Explore» state, не в «Operate». E.9 DRR shape применима для
стратегических решений (Lock entries) — 29 D-Lock entries зафиксированы в
`decisions/strategic/`.

### O-04 — Jetix как работающий продукт

U.Work (A.15.1) — «Record of Occurrence» — описывает то, что уже произошло:
Foundation LOCKED (8 RUSLAN-ACK records), brigadier dispatches, 5 активных циклов
Phase B. U.Capability (A.2.2): 12 agents × tools × skills = deployed capabilities.
**Честная оценка (из `06-honest-self-audit.md §12`):** ~27 компонентов = memory+automation,
~12 = intelligence/FPF-derivative. Итого: «память + автоматизация + ~25%
structural-intelligence + ~10% FPF-derivative» — НЕ full FPF-grade intelligence
amplification. Работает реально, но Левенчуковский bar не достигнут.

### O-05 — Jetix как методология / pattern language

U.MethodDescription (A.3.2) — «Recipe for Action» — эта роль для Jetix пока F2
(experimental). FUNDAMENTAL Layer 1 написан как sector-agnostic, что соответствует
FPF A.8 Universal Core (domain-agnostic generalization). Fork guide v0 (`JETIX-WORKING-FILE-v0
§11`) описывает минимальный viable instance (6 шагов). Формального IWE-Pack-like
distribution format нет. Это кандидат Phase C ремита (если cooperation plan Tier 3
активируется).

### O-06 — Jetix как агентная система

IP-1 Role≠Executor — **прямая FPF-derivative** (A.2 Role + A.13 Agential Role +
RUSLAN-LAYER executor-binding.yaml.template). A.2.7 RoleAlgebra применима для
department topology: `RoleS ≤ RoleG` (sales-lead ≤ MGMT Lead); `RoleAlgebra ⊥`
между peer departments (sales ⊥ brain — нет прямой подчинённости). A.13 Agential
Role: агенты — это roles-with-autonomy-budget, а не U.Agent type (FPF deliberately
не мнит U.Agent type). Hub-and-spoke topology = A.2.1 RoleAssignment pattern
(Holder#Role:Context format используется через acting_as: в message schema).

### O-07 — Foundation Architecture v1.0

Foundation = **U.System** с explicit **U.Mechanism** (A.6.1) инстансами: Part 6a =
F-G-R mechanism (B.3 derivative); Part 6b = Guard-Rails mechanism (E.5 analog);
Pillar C = deontic constraint set (A.2.8 Commitment pattern applied at system level).
A.6.B Boundary Norm Square применима — Foundation boundary explicitly declared
через LOCKED tag + git_tag + AWAITING-APPROVAL enforcement. F8 grade = highest
assurance level в Jetix F-G-R scale. Это наиболее FPF-aligned объект в системе.

### O-08 — Pillar C конституциональная система

A.2.8 Commitment — это именно то, что такое Pillar C Tier 2 rules: deontic
obligations (MUST NOT / SHALL) applied system-wide. E.5 Guard-Rails analog: Default-Deny
table (11 entries) = closest Jetix analog к FPF Guard-Rails, но без формального
Norm-CAL vocabulary. R12 rule 12 — **additive**, не из FPF Spec (собственный contribution).
Halt-Log-Alert response (F8 ≤1s / F4 ≤5s / F2 ≤60s) — operational extension к
FPF B.3 assurance grades, специфичная для Jetix (per `JETIX-WORKING-FILE-v0 §5.5`).

### O-09 — Strategic Insights Hexagon

Это **ближайший к FPF intelligence amplification** объект в Jetix (per `06-honest-self-audit.md
§7`). B.5.2 Abductive Loop: Hexagon генерирует explicit abductive output (alternatives
portfolio visible в H1-H7 docs). E.9 DRR shape: каждый LOCKED insight = strategic
decision record с провенанс-цепочкой. B.3 F-G-R: каждый insight тегируется F/G/R.
E.17 MVPK partial: 1A (plain Doc) + 1B (deep Doc) = two-view publication.
Gap vs FPF: нет formal NQD-CAL alternatives discipline; нет full MVPK bundle с
typed publication surfaces. Работает частично — процесс не систематизирован как
weekly cadence.

### O-10 — Бизнес-модель Phase 1 (TRM)

TRM = U.PromiseContent: «мы управляем 6 ресурсами клиента одновременно» — это
consumer-facing promise clause (A.2.3 semantics). B.1.6 Γ_work (Work as Spent Resource):
TRM tracks 6 resource classes (capital / founder-time / audience / knowledge / compute /
talent) — это directly aligned с FPF resource aggregation pattern. A.2.8 Commitment:
performance fee clause = contingent deontic commitment (if performance → fee).
A.6.C Contract Unpacking: TRM promise не unpacked в FPF-formal sense (informal договорённость).
ICP = Mittelstand DACH (50-500 emp manufacturing) — конкретный bounded context.

### O-11 — R12 Anti-extraction

R12 — **own contribution, NOT in FPF Spec** (per Phase B audit `JETIX-WORKING-FILE-v0
§5.2` + `06-honest-self-audit.md §13`). A.2.8 Commitment: rule 12 = prohibition-modality
deontic (agents / substrate MUST NOT extract value beyond agreed share). A.2.9 SpeechAct:
R12 activation = instituting speech act (Q2 Ruslan ack 2026-05-12). 4-source attribution
trail = E.9 DRR shape (not labeled as such, but functionally a decision record).
Meadows Level 2 leverage point (system goals). Применяется симметрично: Jetix не
экстрактирует у партнёров; партнёры не экстрактируют у Jetix; substrate не у owner.

### O-12 — Бренд / публичный слой

Doc 1A (Base Management System) + Doc 1B (Jetix Corporation) = two-view publication
(E.17 MVPK shape). A.6.3 EpistemicViewing: каждый из этих docs = view of the same
described entity (Jetix-as-system) для разных audiences (partner / client / investor).
A.2.3 PromiseContent: «мета-мастерская для профессиональных мастеров» = public-facing
promise. Gap: нет formal ViewpointBundle definition (MVPK full implementation
требует typed ViewpointBundleLibrary — A.6.3 E.17.1/E.17.2).

### O-13 — People-Network-State / Clan vision

H7 insight + Clan Charter = кандидат B.2 Meta-Holon Transition: индивидуальные
мастера (субголоны) → Clan (суперголон) = MHT event. B.2.1 BOSC Triggers применим:
добавление новых signatories = Boundary + Scale trigger. A.2.7 RoleAlgebra:
6 archetypes (Hunter / Guardian / Scholar / Creator / Architect / Merchant) = role
bundle set (⊗ operator). R12 применяется как конституциональная гарантия для
members (fork-and-leave without penalty). FPF не содержит Network-State как
паттерн — это Jetix-originated concept (per `JETIX-WORKING-FILE-v0 §5.6 J-U2`).

### O-14 — Meta-workshop для профессиональных мастеров

A.1 Holon на уровне supersystem: Jetix-instance-for-Ruslan + partner-Jetix-instances =
potential meta-holon. A.5 Kernel Modularity (open-ended kernel + extension layering):
каждый partner-instance = fork + specialise FUNDAMENTAL, не duplicate. B.2.2 MST:
meta-workshop activation = system emergence event (new capabilities не available в
single instance). A.3.1 Method hosting: Jetix-as-meta-workshop hosts partner methods
(их мастерские) — это FPF A.3.1 Method as the abstract way of doing within a bounded
context. Пока F4 — задумка, не реализована.

---

## §3 Cross-refs между объектами

| Связь | Type | Direction | Notes |
|---|---|---|---|
| O-07 Foundation → O-01 Субстрат | hosts | О-07 constitutes O-01 | Foundation = organizational substrate; O-01 = runtime instantiation |
| O-08 Pillar C → O-07 Foundation | constrains | O-08 constrains all Foundation writes | Constitutional layer above Foundation |
| O-11 R12 → O-08 Pillar C | extends | R12 is additive rule в Pillar C Tier 2 | Additive 2026-05-12; не изменяет предыдущие 11 правил |
| O-09 Hexagon → O-03 Vision | refines | Hexagon outputs refine Vision-задумка | H1-H7 distill from Vision + operational observation |
| O-13 Clan → O-11 R12 | governed-by | Clan members governed by R12 | R12 as constitutional guarantee for Clan |
| O-02 Корпорация → O-10 TRM | implements | TRM = commercial implementation of Corp concept | TRM ladder = promise content of Corp |
| O-04 Продукт → O-07 Foundation | built-on | Product capabilities hosted by Foundation | Foundation v1.0 = organisational substrate for all product |
| O-05 Методология → O-14 Meta-workshop | enables | Methodology (FUNDAMENTAL layer) enables partner instantiation | Fork guide v0 → Phase C potential |
| O-06 Агентная система → O-07 Foundation | governed-by | Agents governed by Foundation Part 4 + Pillar C | IP-1 Role≠Executor applied to agent roster |
| O-12 Бренд → O-03 Vision | publication-of | Brand = MVPK view of Vision | Doc 1A/1B = audience-specific views of same entity |
| O-14 Meta-workshop → O-13 Clan | supersystem-for | Meta-workshop hosts Clan members' workshops | Phase B+ activation path |
| O-09 Hexagon → O-11 R12 | originates | H7 People-NS = origin of R12 candidate | R12 first surfaced в H7 insight |

---

## §4 Dissents preserved

### D-1 (from Phase B Step 2 — CARRIED)

- **Claim:** «IWE in public template = paid aisystant AI guide» dissent.
  All comparative statements O-01/O-04 vs IWE scoped to `FMT-exocortex-template v0.31.0`
  (public). Paid AI guide may reveal mechanisms that change the comparison.
- F: F3 · G: phase-b-dissent · R: refuted_if_Aisystant_B2_access_shows_equivalent_F-G-R_AND_R12-analog

### D-2 (this cell — integrator self-dissent)

- **Claim (this cell):** O-07 Foundation maps to U.System + U.Mechanism (A.6.1).
- **Counter-claim surfaced:** Foundation could alternatively be typed as
  U.MethodDescription (A.3.2) — «the recipe for how the org runs» — rather than
  U.System (the running system itself). The ambiguity is genuine: Foundation is both
  the specification AND the instantiated system.
- **Resolution status:** Not resolved here per integrator scope. Brigadier may dispatch
  philosophy × critic for epistemic arbitration on this typing question.
- F: F3 · G: fpf-typing-dispute · R: refuted_if_FPF_Part_A_authors_clarify_U.System_vs_U.MethodDescription_boundary_for_org_architecture

### D-3 (this cell — on Hexagon status)

- **Claim (this cell):** O-09 Hexagon is «работает-частично» (closest to FPF intelligence
  amplification in Jetix).
- **Counter-claim:** Hexagon may be better classified as «работает-полно» within its
  own scope (generates locked STRATEGIC insights with F-G-R + multi-view). The «partial»
  label reflects comparison against full FPF B.5.2 NQD-CAL, which Jetix has not adopted.
  Within Jetix's own discipline, Hexagon process IS complete.
- F: F3 · G: jetix-hexagon-status · R: refuted_if_Hexagon_cadence_is_documented_as_systematic_weekly_ritual

---

## §5 Open questions для Ruslan

> Per integrator scope: surface что не могу решить в рамках этого cell.

**OQ-1 (FPF primitive typing ambiguity).** Foundation v1.0 типизируется как U.System
(O-07) или U.MethodDescription (O-05 overlap)? Это не тривиальный вопрос: если
Foundation = U.MethodDescription, то Foundation revisions — это updates к «recipe»,
и применяется FPF A.16 Language-State Transduction Coordinator. Если U.System —
то это architectural change с другими constraints. Engineering не может решить эту
типологическую границу без философской экспертизы.

**OQ-2 (O-02 Корпорация: когда FPF A.6.C Contract Unpacking применять).** TRM contracts
пока неформальны. При переходе к реальным клиентам: когда TRM promise clause должна
быть unpacked в formal FPF Commitment objects (A.2.8)? Это вопрос R2 gate-timing
(архитектурное изменение — AWAITING-APPROVAL).

**OQ-3 (O-13 Clan: BOSC Trigger threshold).** Сколько signatories = Meta-Holon
Transition (B.2.1 BOSC Trigger) для Clan? 5 (base target) или 10 (target)? FPF B.2.1
не даёт числовой порог — только quality-based triggers (Boundary / Objective /
Supervisor / Complexity change). Ruslan решает threshold per R1.

**OQ-4 (O-05 vs O-14: когда Methodology → Meta-workshop activation).** Fork guide v0
(§11) — Phase C remit. Когда этот activation path становится F4 (прорабатывается) vs
остаётся F2 (задумка)? Связано с Cooperation Plan Tier 3 activation (FPF/IWE dialogue).

**OQ-5 (O-11 R12: surface к FPF community?).** Per `JETIX-WORKING-FILE-v0 §12 OQ-5`:
«Surface R12 как contribution candidate to FPF Part E? Or keep as Jetix-internal?»
Engineering не может решить — это стратегическое решение (R1 Ruslan sole strategist).

**OQ-6 (C4 benchmark и epistemic calibration).** O-04 «работает реально» и O-07 F8
LOCKED — но C4 comparison (Arm A vs D 7-criteria) не запущен. Пока C4 не done, claim
«Jetix умнее vanilla AI» остаётся F2. Timing C4 — Ruslan решает (B2 blocker + Aisystant).

**OQ-7 (объект «Life OS как personal substrate» в инвентаре?).** Проект `life-os`
(CLAUDE.md projects P3 Active) surface'ится в инвентаре как отдельный объект? Он
является sub-scope O-01 (операционный субстрат) или отдельным U.BoundedContext
(личная жизнь ≠ бизнес)? Engineering surface'ит этот вопрос; brigadier/Ruslan решают
нужен ли O-15 в следующей итерации.

---

*Engineering-expert × integrator. Objects surface'нуты: 14 (4 базовых + 10 поверхнутых).
All provenance refs present. Dissents preserved: 3. Open questions: 7.*
