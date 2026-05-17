---
task_id: phase-0-fpf-scope-2026-05-17-task-2
produced_by: engineering-expert × integrator
mode: integrator
status: draft (brigadier integrates)
F: F4
G: phase-0-cell-draft
R: refuted_if_object_missing_OR_anti_scope_missing_OR_F-G-R_per_claim_absent
date: 2026-05-17
inputs:
  - reports/phase-0-fpf-scope/01-jetix-objects-inventory.md (Task 1 integrated)
  - raw/external/ailev-FPF/FPF-Spec.md (selective — A.1/A.1.1/A.2/A.2.1/A.2.3/A.2.8/A.2.9/A.3.1/A.3.2/A.4/A.13/A.15/A.15.1/A.15.2/A.16/B.2/B.3/B.5.2/E.5/E.9/E.17)
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/JETIX-TRM-MODEL-2026-04-30.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md
  - JETIX-WORKING-FILE-v0-2026-05-17.md
  - reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md
  - CLAUDE.md
---

# Per-Object Deep Description — Phase 0 FPF Scope Task 2

> **Constitutional posture.** Surface-only (R1). No strategic judgments. No
> good/bad evaluations. Provenance per claim. F-G-R triples mandatory.
> This file = engineering-expert × integrator draft. Brigadier integrates
> with systems-integrator + philosophy-critic parallel cells.

> **Default-mode note.** Mode prefix omitted in dispatch → treated as
> `mode: integrator` per §5.0 default-mode rule. Applied accordingly.

---

## §0 Summary (≤300 слов)

Deep-dive across 14 objects surface'нул три повторяющихся паттерна:

**1. Дуализм artefact/system.** Каждый объект существует в двух состояниях:
как locked artefact (A.16 language-state) и как operational instantiation
(A.4 run-time / A.15.1 U.Work). Для большинства объектов (O-03, O-07, O-08,
O-11, O-13) artefact-сторона F8/F5; operational-сторона F2-F4 или vapor.
Это не противоречие — это честное отображение реального состояния системы.
FPF A.4 Temporal Duality именно для этого и существует.

**2. FPF primitives четко ложатся на 4 кластера.** Организационный субстрат
(O-01/O-06a/O-06b/O-07) = A.1+A.2 cluster. Трансформационный движок
(O-04/O-09/O-05) = A.3+A.15+B.5 cluster. Конституциональный слой
(O-08/O-11) = A.2.8+E.5 cluster. Концептуально-vapor (O-02/O-03/O-10/O-12/
O-13/O-14) = A.15.2+B.2 cluster. Это FPF-derived структура, не новое
изобретение.

**3. Anti-scope boundaries критически важны.** Большинство conflation traps
(CE-1..CE-5 из Task 1) возникают потому, что один объект используется в двух
ролях одновременно: как описание (U.Episteme) и как операциональная система
(U.System/U.Work). FPF A.7 Strict Distinction = главный инструмент для
разрешения этих трапов.

**Engineering integrator note.** Parallel cells (systems-integrator,
philosophy-critic) surface feedback loops per object и epistemic per-object
analysis соответственно. Dissents из этих двух клеток НЕ усреднены здесь —
они сохранены в §15. Brigadier integrates three-cell outputs.

**Claim count.** 14 objects × avg 5-7 claims = ~84 F-G-R tagged claims total.
All claims have provenance refs. Acceptance predicate: each object has
«что есть» + «что задумано» + anti-scope + cross-refs + ≥3 F-G-R claims.

---

## §1 — O-01 — Jetix как оперативный субстрат (information management system)

**FPF primitive:** U.System (A.1) + U.BoundedContext (A.1.1)
**FPF Part hosting:** Part A Kernel — Cluster A.I (Foundational Ontology)
**Applicable FPF mechanisms:**
- A.1 Holonic Foundation — система + её части как голоны
- A.1.1 U.BoundedContext — semantic frame: single-owner, filesystem=SoT
- A.2 Role Taxonomy — 12 role-types × 6 departments
- A.4 Temporal Duality — design (Foundation LOCKED) vs run (active cycles)
- A.15 Role-Method-Work Alignment — частичное: Part 4 operative, method-signature не enforced

**Что есть (concrete, evidenced):**

- Filesystem-canonical state management + git-native rollback работает.
  [F5 · jetix-operational · R-high] [src: CLAUDE.md §Global Rules «Filesystem = source of truth»; CLAUDE.md §Architecture «Filesystem: single source of truth»]
- Voice pipeline (transcribe → extract → filter → review) активен: 11 voice reviews
  за последний цикл. [F4 · jetix-operational · R-medium] [src: 06-honest-self-audit.md §5 «Voice pipeline (transcribe + extract + filter + review) = automation»; JETIX-WORKING-FILE-v0 §0 snapshot «11 voice reviews active»]
- Wiki v2 substrate: 551 record в wiki/index.md; ROY swarm dispatching активен.
  [F4 · jetix-operational · R-medium] [src: 01-jetix-objects-inventory.md §2 O-01 «wiki 551 records; ROY swarm dispatching»]
- Holonic structure operational: brigadier orchestrates 5 ROY experts (4 modes × 5 = 20 cells).
  [F4 · jetix-operational · R-medium] [src: CLAUDE.md §Agent Roster; JETIX-WORKING-FILE-v0 §4 «brigadier 5 experts × 4 modes = 20 cells»]
- shared/state/ JSON stale: last_updated 2026-04-14. State persistence = partial.
  [F3 · jetix-operational · R-medium] [src: 01-jetix-objects-inventory.md §3 O-01 «shared/state/ JSON stale (last 2026-04-14)»]

**Что задумано (target, aspirational):**

- Full auto-KB distribution (distribute.py.bak архивирован — manual-only сейчас).
  [F2 · jetix-target · R-low] [src: CLAUDE.md §Voice-Notes Pipeline «distribute.py архивирован в distribute.py.bak — автоматически не запускается»]
- Part 3 Methodology Library operational (сейчас memory-dominant substrate).
  [F2 · jetix-target · R-low] [src: 06-honest-self-audit.md §2 «Part 3 = memory»]
- Method-signature enforcement via A.15 — RUSLAN-LAYER overlay incomplete.
  [F2 · jetix-target · R-low] [src: 06-honest-self-audit.md §2.1 «method-signature не yet enforced (RUSLAN-LAYER overlay incomplete)»]

**Anti-scope (что НЕ относится):**

- NOT Notion (= view, не SoT; conflation trap CE-3 adjacent — treating Notion state as canonical)
- NOT filesystem-repo artefacts themselves (= carrier per A.10 Evidence; O-01 = operating U.System, не carrier)
- NOT юрлицо / корпорация (→ O-02; conflation trap: treating operational substrate как corporate entity)
- NOT vision/aspirational state (→ O-03; A.4 Temporal Duality: run-time ≠ design-time)
- NOT Phase B managed team or enterprise clients (→ O-14; out of current bounded context)

**Cross-refs:**
- → O-04 (hosts: working product capabilities run on this substrate)
- → O-06b (executor-bindings: ROY swarm dispatched within this substrate)
- → O-07 (constituted-by: Foundation v1.0 specifies this substrate's governance)
- → O-08 (constrained-by: Pillar C Tier-2 rules apply to all substrate actions)

---

## §2 — O-02 — Jetix как юр.лицо / корпорация (in-progress)

**FPF primitive:** U.RoleAssignment (A.2.1) + U.PromiseContent (A.2.3)
**FPF Part hosting:** Part A Cluster A.I; future Part A Cluster A.II
**Applicable FPF mechanisms:**
- A.2.1 U.RoleAssignment — Holder#Role:Context Standard для партнёр/клиент/работник
- A.2.3 U.PromiseContent — TRM ladder = consumer-facing promise clause
- A.2.8 U.Commitment — обязательства формально не оформлены
- A.6.C Contract Unpacking — не применялась к Doc 1B contract language

**Что есть (concrete, evidenced):**

- Doc 1B LOCKED v1.0 = conceptual document describing Jetix Corp structure (партнёры / клиенты / работники).
  [F5 · jetix-corp-concept · R-high] [src: JETIX-CORPORATION-2026-05-05.md frontmatter «status: LOCKED v1.0; purpose: концептуальный документ для партнёров/инвесторов»]
- TRM model LOCKED v1.0 = companion canonical to Workshop: 6-resource model + L0-L5 ladder.
  [F5 · jetix-corp-concept · R-high] [src: JETIX-TRM-MODEL-2026-04-30.md frontmatter «status: LOCKED v1.0»]
- Ruslan = физлицо Berlin; no GmbH/UG registered; no entity-incorporation.md in repo.
  [F4 · jetix-operational-honest · R-high] [src: 01-jetix-objects-inventory.md §2 O-02 «Ruslan = физлицо Берлин. Doc 1B purpose = концептуальный документ»]

**Что задумано (target, aspirational):**

- GmbH/UG/Ltd инкорпорация + формальные partner commitments по A.2.8.
  [F2 · jetix-corp-target · R-low] [src: JETIX-CORPORATION-2026-05-05.md §0 «Trajectory: €5K (now) → $100K к концу лета 2026 → €100M+ ARR через 3 года»]
- A.6.C Contract Unpacking applied to partner engagement (promise/utterance/commitment/work separation).
  [F2 · jetix-corp-target · R-low] [src: 01-jetix-objects-inventory.md §2 O-02 «A.6.C Contract Unpacking не применялась»]
- 3 engagement levels operational: Partners (top tier) + Clients (TRM) + Workers (salary).
  [F2 · jetix-corp-target · R-low] [src: JETIX-CORPORATION-2026-05-05.md §0 TL;DR «3 уровня вовлечения»]

**Anti-scope (что НЕ относится):**

- NOT current operational entity (vapor as instantiated; CE-3 trap: treating concept-doc as operational)
- NOT active client contracts today (revenue = 0; cross-ref O-10)
- NOT the operational substrate (→ O-01; conflation trap CE-3)
- NOT Jetix-as-pattern (→ O-05; фorkable methodology ≠ specific corp entity)

**Cross-refs:**
- → O-10 (implements: TRM = commercial implementation of Corp concept)
- → O-03 (refines: Corp concept is vision-derived)
- → O-14 (targets: meta-workshop = Phase B+ corporate form)

---

## §3 — O-03 — Jetix как задумка / vision (future state target)

**FPF primitive:** U.WorkPlan (A.15.2) + U.MethodDescription (A.3.2)
**FPF Part hosting:** Part A Cluster A.III (Time & Evolution); Part 11 (Strategic Direction)
**Applicable FPF mechanisms:**
- A.4 Temporal Duality — design-time intent vs run-time reality; gap здесь максимален
- A.15.2 U.WorkPlan — FUNDAMENTAL = schedule of intent for future system
- A.3.2 U.MethodDescription — sector-agnostic «recipe» layer (Layer 1 of 2)
- E.9 DRR — 29 D-Lock entries в Decisions DB = DRR-shaped records
- B.5.1 Explore→Operate — system is in «Explore» state

**Что есть (concrete, evidenced):**

- FUNDAMENTAL LOCKED v1.0 (2026-04-27): 35 UC × 12 categories vision document.
  [F8 · jetix-vision-artefact · R-high] [src: JETIX-VISION-FUNDAMENTAL-2026-04-27.md frontmatter «status: LOCKED v1.0; locked_date: 2026-04-27»]
- Two-layer architecture declared: Layer 1 (FUNDAMENTAL — sector-agnostic) + Layer 2 (RUSLAN-LAYER — Ruslan-specific).
  [F5 · jetix-vision-canonical · R-high] [src: JETIX-VISION-FUNDAMENTAL-2026-04-27.md §0 «Layer 1 of 2 — fundamental base. Layer 2 = JETIX-VISION-OF-SYSTEM-2026-04-27.md (Ruslan-specific overlay)»]
- Part 11 Strategic Direction Substrate hosts vision artefacts (6 strategic doc types + Decisions DB).
  [F5 · jetix-canonical · R-high] [src: CLAUDE.md §Foundation Architecture v1.0 «Part 11 — Strategic Direction Substrate (Pillar A)»; JETIX-WORKING-FILE-v0 §7]
- 8 RUSLAN-ACK records confirm vision alignment; git-tagged «foundation-architecture-locked-2026-04-28».
  [F5 · jetix-canonical · R-high] [src: CLAUDE.md §Foundation Architecture v1.0 §8 RUSLAN-ACK records]

**Что задумано (target, aspirational):**

- Vision realised in client-facing product (revenue = 0 today; B.5.1 = «Explore» state).
  [F2 · jetix-vision-target · R-low] [src: 06-honest-self-audit.md §2.2 «project management, monetization, community — все три substrate concerns»]
- 100-200 year marathon timeline (Clan Charter §1.7).
  [F4 · charter-applied-now · R-medium] [src: JETIX-FIRST-CLAN-CHARTER-2026-05-12.md revision_history «§1.7 marathon timeline updated 10-15→100-200 лет»]
- FPF-grade intelligence amplification level for the vision system itself.
  [F2 · jetix-vision-target · R-low] [src: 06-honest-self-audit.md §2.2 «Phase A is memory + automation substrate; not yet FPF-grade»]

**Anti-scope (что НЕ относится):**

- NOT current operational reality (A.4: design-time vision ≠ run-time capability)
- NOT proof of revenue or clients (→ O-10 for business model)
- NOT FPF-grade strategic claims (F2 positioning until C4 benchmark runs per JETIX-WORKING-FILE-v0 §6.3)
- NOT Ruslan-specific LAYER (that's Layer 2, separate document)

**Cross-refs:**
- → O-04 (targeted-by: working product is partial realisation of vision)
- → O-09 (refined-by: Hexagon insights refine vision claims)
- → O-12 (publication-of: brand = MVPK view of vision)

---

## §4 — O-04 — Jetix как работающий продукт (что РЕАЛЬНО работает СЕЙЧАС)

**FPF primitive:** U.Work (A.15.1) + U.Capability (A.2.2)
**FPF Part hosting:** Part A Cluster A.II–A.V; multiple Parts operational
**Applicable FPF mechanisms:**
- A.15.1 U.Work — Record of Occurrence (git commits, cycle logs, voice pipeline outputs)
- A.2.2 U.Capability — evidenced system abilities (Foundation LOCKED, ROY swarm dispatching)
- B.3 F-G-R — operational adoption: all promoted artefacts carry F-G-R tags
- A.10 Evidence Graph Referring — provenance chain via sources[] + inline [src:] citations
- A.2.5 U.RoleStateGraph — past-participle states в CRM (13 pipeline statuses) + wiki

**Что есть (concrete, evidenced):**

- Foundation v1.0 LOCKED (F8): 11 Parts + Pillar A + Pillar C; 8 RUSLAN-ACK records; git-tagged.
  [F8 · jetix-foundation-canonical · R-high] [src: CLAUDE.md §Foundation Architecture v1.0; JETIX-WORKING-FILE-v0 §7]
- ROY swarm (brigadier + 5 experts): actively dispatching в Phase B (15 Phase-B cell drafts confirmed).
  [F4 · jetix-operational · R-medium] [src: 01-jetix-objects-inventory.md §3 O-04 «15 Phase-B drafts»; JETIX-WORKING-FILE-v0 §6 Step 1-3 complete]
- Per honest-self-audit §12: ~27 components total; ~12 = intelligence/FPF-derivative; ~15 = memory+automation.
  [F4 · jetix-operational-honest · R-high] [src: 06-honest-self-audit.md §2.1 «memory-dominant (5 Parts) + automation-dominant (3 Parts) + FPF-derivative (4 Parts + Pillar C)»]
- 6 outreach files written (2026-05-12..17); Tseren/Levenchuk contacts в CRM.
  [F4 · jetix-operational · R-medium] [src: 01-jetix-objects-inventory.md §3 O-04 «6 outreach files = current external-facing artefacts»]
- Revenue = 0 confirmed. No client deliverables shipped externally.
  [F5 · jetix-operational-honest · R-high] [src: shared/state/active-projects.json «revenue_current: 0» per 01-jetix-objects-inventory.md §1 O-04]

**Что задумано (target, aspirational):**

- Phase B managed team + enterprise clients at TRM scale.
  [F2 · jetix-phase-B-target · R-low] [src: JETIX-WORKING-FILE-v0 §6.3 C4 benchmark «NOT yet run»]
- Full FPF-grade intelligence amplification (not «memory + automation» dominant).
  [F2 · jetix-target · R-low] [src: 06-honest-self-audit.md §7.1 «THIS is the closest to intelligence amplification — still draft-grade»]
- Foundation enforcement fully operational (Halt-Log-Alert не stub).
  [F2 · jetix-target · R-low] [src: JETIX-WORKING-FILE-v0 §5.5 «Halt-Log-Alert response per Part 6b» + «Status: Runtime = STUB per 06-honest-self-audit.md»]

**Anti-scope (что НЕ относится):**

- NOT Phase B extensions or enterprise scale (→ O-14)
- NOT TRM at scale / active client contracts (→ O-10; revenue = 0)
- NOT the vision-artefact (→ O-03; A.4 Temporal Duality: run-time ≠ design-time)
- NOT «Foundation LOCKED = system operational» (CE-3: artefact LOCKED ≠ Parts fully operational)

**Cross-refs:**
- → O-07 (built-on: Foundation v1.0 = organisational substrate)
- → O-01 (runs-on: operational substrate = carrier)
- → O-09 (produces: Hexagon insights are outputs of working product activity)

---

## §5 — O-05 — Jetix как методология / pattern language (forkable)

**FPF primitive:** U.MethodDescription (A.3.2) + U.Method (A.3.1)
**FPF Part hosting:** Part A Cluster A.II (Transformation Engine)
**Applicable FPF mechanisms:**
- A.3.2 U.MethodDescription — FUNDAMENTAL Layer 1 = «recipe for action» (sector-agnostic)
- A.3.1 U.Method — the actual doing; NOT yet instantiated beyond Ruslan's own instance
- A.5 Kernel Modularity — sector-agnostic core → extensible with domain-specific layers
- A.8 Universal Core — FUNDAMENTAL Layer 1 aligned with sector/person/business-agnostic intent
- B.4 Canonical Evolution Loop — methodology must evolve per DRR; no static recipes

**Что есть (concrete, evidenced):**

- FUNDAMENTAL Layer 1 (sector-agnostic) LOCKED v1.0: 35 UC × 12 categories в вакууме.
  [F5 · jetix-methodology-artefact · R-high] [src: JETIX-VISION-FUNDAMENTAL-2026-04-27.md §0 «Generic-only, sector/person/business-agnostic»]
- Fork guide v0 (§11 working file): 6-step minimal viable Jetix instance.
  [F2 · future-pattern-experimental · R-low] [src: JETIX-WORKING-FILE-v0 §11 «F2 — experimental. Scaffold для future Jetix-as-Pack pattern»]
- Two-layer architecture (FUNDAMENTAL + RUSLAN-LAYER overlay) = structural separation of universal from specific.
  [F4 · jetix-methodology-structural · R-medium] [src: JETIX-VISION-FUNDAMENTAL-2026-04-27.md §0 «Если кто-то другой возьмёт Jetix-методологию → берёт FUNDAMENTAL и пишет свой LAYER»]

**Что задумано (target, aspirational):**

- Distributed Jetix-as-Pack format (HTTP manifest fetch analogue) — Phase C remit.
  [F2 · future-pattern-experimental · R-low] [src: JETIX-WORKING-FILE-v0 §11.3 «Formal Jetix-as-IWE-Pack pattern… Phase C remit»]
- First external forker instantiates methodology for their own domain.
  [F2 · future-pattern-target · R-low] [src: JETIX-WORKING-FILE-v0 §11 «§11.2 What does NOT transfer»]
- Cooperation Plan Tier 3 activation (FPF/IWE community cooperation) enables methodology distribution.
  [F2 · future-pattern-target · R-low] [src: 01-jetix-objects-inventory.md §2 O-05 «Phase C remit (если cooperation plan Tier 3 активируется)»]

**Anti-scope (что НЕ относится):**

- NOT distributable format today (vapor; no forkers; CE-5 adjacent: treating concept as distributed product)
- NOT the specific Jetix instance (→ O-01; methodology ≠ instantiated system)
- NOT IWE Pack (different unit: IWE = single intellectual worker; Jetix = multi-agent business OS)
- NOT Phase C activations (no cooperation plan finalised yet)

**Cross-refs:**
- → O-14 (enables: forkable methodology enables partner instantiation)
- → O-03 (derived-from: methodology derived from FUNDAMENTAL vision)
- → O-12 (distinct-from: brand/public layer ≠ methodology layer; conflation trap available)

---

## §6 — O-06a — Jetix-as-12-role-types (type-level, IP-1 split A)

**FPF primitive:** U.Role set (A.2 type-level)
**FPF Part hosting:** Part A Cluster A.I; Part 4 (Role Taxonomy & Coordination Protocol)
**Applicable FPF mechanisms:**
- A.2 Role Taxonomy — 12 abstract functional role-type declarations
- A.2.7 U.RoleAlgebra — department topology: RoleS ≤ RoleG (specialisation); 6 departments
- A.13 Agential Role & Agency Spectrum — agents = roles with autonomy budget, not U.Agent type
- IP-1 Role≠Executor — FPF-derived principle: type-level role ≠ executor token

**Что есть (concrete, evidenced):**

- 12 role-type declarations in CLAUDE.md §Agent Roster: 4 Phase-1 active + 8 Phase 2-4 declared.
  [F5 · jetix-role-taxonomy · R-high] [src: CLAUDE.md §Agent Roster table «Phase 1: manager/personal-assistant/system-admin/sales-lead active»]
- Part 4 (Role Taxonomy & Coordination Protocol) LOCKED F8: FPF A.2 derivative for role taxonomy.
  [F5 · jetix-foundation-canonical · R-high] [src: 06-honest-self-audit.md §2.1 «Part 4 = FPF-derivative + intelligence; Direct adoption; IP-1 Role≠Executor explicit»]
- 6 department groupings (MGMT / OPS / Sales / Brain / Life / Meta) = U.RoleAlgebra topology.
  [F4 · jetix-role-taxonomy · R-medium] [src: CLAUDE.md §Agent Roster; JETIX-WORKING-FILE-v0 §4 mermaid «12 Specialized Agents × 6 Departments»]
- Phase 3-4 roles (knowledge-synth, strategist, life-coach, meta-agent) = declared type-level without confirmed operational executor bindings.
  [F4 · jetix-operational-honest · R-high] [src: 01-jetix-objects-inventory.md §2 O-06a/b «Phase 3-4 agents = declared role-types без confirmed operational executor bindings»]

**Что задумано (target, aspirational):**

- Phase 3-4 roles operationalised: executor bindings confirmed + mailboxes active.
  [F2 · jetix-phase-B-target · R-low] [src: CLAUDE.md §Agent Roster Phase column]
- Method-signature enforcement per A.15 for all 12 roles.
  [F2 · jetix-target · R-low] [src: 06-honest-self-audit.md §2.1 «method-signature не yet enforced»]

**Anti-scope (что НЕ относится):**

- NOT 12 simultaneously running processes (CE-2 categorical error: role-type ≠ executor-token)
- NOT specific executor instances (Sonnet 4.6 / Haiku 4.5 → O-06b)
- NOT conversation threads or running processes (A.13: agents = roles with autonomy budget)
- NOT permanent actors (A.2.1 RoleAssignment = contextual, not permanent identity)

**Cross-refs:**
- → O-06b (instantiated-by: executor tokens instantiate type-level roles per A.2.1)
- → O-07 (governed-by: Part 4 + Pillar C governs role taxonomy)
- → O-01 (part-of: role-types constitute the holonic structure of operational substrate)

---

## §7 — O-06b — Jetix-as-executor-bindings (token-level, IP-1 split B)

**FPF primitive:** U.RoleAssignment (A.2.1)
**FPF Part hosting:** Part A Cluster A.I; RUSLAN-LAYER executor-binding.yaml
**Applicable FPF mechanisms:**
- A.2.1 U.RoleAssignment — Holder#Role:Context Standard (contextual enactments, not permanent)
- A.13 Agential Role — autonomy budget graded per role instance
- A.2.5 U.RoleStateGraph — state of each role assignment (active/inactive/stale)
- RUSLAN-LAYER executor-binding.yaml.template — maps role-types to specific models

**Что есть (concrete, evidenced):**

- ROY swarm (brigadier + 5 ROY experts) actively dispatched in Phase B: 15 confirmed dispatches.
  [F4 · jetix-executor-bindings · R-medium] [src: JETIX-WORKING-FILE-v0 §6 «Steps 1-3 complete; Phase B Шаги 1+2+3 = complete»; 01-jetix-objects-inventory.md §2 O-06b]
- RUSLAN-LAYER executor-binding.yaml.template present: maps role → model (Sonnet 4.6 / Haiku 4.5).
  [F4 · jetix-executor-bindings · R-medium] [src: CLAUDE.md §Foundation Architecture v1.0 «shared/schemas/executor-binding.yaml.template — IP-1 Role≠Executor RUSLAN-LAYER binding»]
- Legacy 12 mailboxes stale: last active 2026-04-15 (comms/mailboxes/manager.jsonl:L1-4).
  [F4 · jetix-operational-honest · R-high] [src: 01-jetix-objects-inventory.md §2 O-06b «Legacy 12-mailbox roster = stale (last 2026-04-15)»]
- 23 .claude/agents/ files present (ROY swarm + legacy hybrid).
  [F4 · jetix-operational · R-medium] [src: 01-jetix-objects-inventory.md §1 O-06b provenance «.claude/agents/ (23 files)»]

**Что задумано (target, aspirational):**

- Legacy roster deprecated OR reactivated + boundaries documented (OQ-9 open).
  [F2 · jetix-target · R-low] [src: 01-jetix-objects-inventory.md §8 «OQ-9 (Phase 1 → Phase B coordination). Migration plan: legacy roster deprecated OR reactivated? When/how CLAUDE.md updated?»]
- All 12 role-type executor bindings active + documented per RUSLAN-LAYER.
  [F2 · jetix-target · R-low] [src: CLAUDE.md §Agent Roster Phase column]

**Anti-scope (что НЕ относится):**

- NOT the abstract role-type taxonomy (→ O-06a; IP-1 split)
- NOT persistent actors across sessions (A.2.1: contextual enactment, not permanent identity)
- NOT 12 simultaneous running processes (CE-2: executors dispatched on-demand, not always-on)
- NOT Foundation architecture specification (→ O-07; executor bindings = runtime tokens within spec)

**Cross-refs:**
- → O-06a (instantiates: tokens instantiate types per A.2.1)
- → O-01 (runs-within: executor bindings operate within operational substrate)
- → O-07 (governed-by: Part 4 + Pillar C governs all executor behavior)

---

## §8 — O-07 — Foundation Architecture v1.0 (organisational substrate F8-LOCKED)

**FPF primitive:** U.System (A.1) + U.Mechanism (A.6.1) [DISPUTED — see dissents]
**FPF Part hosting:** Part A + Part E (Constitution analog)
**Applicable FPF mechanisms:**
- A.1 Holonic Foundation — Foundation = system of systems (11 Parts as holons)
- A.6.1 U.Mechanism — Part 6a F-G-R schema, Part 6b Guard-Rails as mechanism instances
- A.6.B Boundary Norm Square — Pillar C deontic rules as boundary norms (L/A/D/E claims)
- E.5 Guard-Rails analog — Default-Deny table (11 entries) = closest Jetix analog
- B.3 F-G-R — adopted as Part 6a Provenance Officer core mechanism
- A.16 Language-State — «LOCKED» = A.16 language-state of U.Episteme (artefact); NOT U.Work operational record

**Что есть (concrete, evidenced):**

- 11 Parts + Pillar A + Pillar C LOCKED 2026-04-28: git-tag confirmed, 8 RUSLAN-ACK records.
  [F8 · jetix-foundation-canonical · R-high] [src: CLAUDE.md §Foundation Architecture v1.0 «git tag: foundation-architecture-locked-2026-04-28»; JETIX-WORKING-FILE-v0 §7]
- 4 of 11 Parts are FPF-derivative operational: Part 4 (A.2 derivative) + Part 6a (F-G-R) + Part 6b (Guard-Rails) + Pillar C.
  [F4 · jetix-foundation-operational · R-high] [src: 06-honest-self-audit.md §2.1 «Direct FPF-derivative (4 Parts): Part 4 + Part 6a + Part 6b + Pillar C»]
- 7 of 11 Parts = memory+automation dominant (substrate-level); abductive loop NOT operational.
  [F4 · jetix-operational-honest · R-high] [src: 06-honest-self-audit.md §2.1 «Memory-dominant (5 Parts): 1, 3, 5, 9, 11 + Automation-dominant (3 Parts): 2, 7, 8»]
- Halt-Log-Alert mechanism described in Part 6b; runtime enforcement = STUB (Phase B).
  [F4 · jetix-operational-honest · R-high] [src: JETIX-WORKING-FILE-v0 §5.5 «Halt-Log-Alert response per Part 6b §I.2» + runtime note; 01-jetix-objects-inventory.md §2 O-07]

**Что задумано (target, aspirational):**

- Runtime enforcement operational: Halt-Log-Alert ≤1s/≤5s/≤60s per F8/F4/F2 violations.
  [F2 · jetix-target · R-low] [src: CLAUDE.md §Critical Tier-2 Principles «F8 grade violations halted ≤1s; F4 grade ≤5s; F2 grade ≤60s»]
- All 11 Parts FPF-derivative (not just 4); abductive loop operational per B.5.2.
  [F2 · jetix-target · R-low] [src: 06-honest-self-audit.md §10.2 «Shared gaps vs FPF: Full U.Episteme slot graph enforcement — neither enforces»]
- Claim Register (per A.6.B) operational beyond Foundation LOCKED artefacts.
  [F2 · jetix-target · R-low] [src: 06-honest-self-audit.md §2 «Claim Register absent»]

**Anti-scope (что НЕ относится):**

- NOT proof of fully operational system (CE-3: «Foundation LOCKED» = artefact A.16 language-state, NOT U.Work operational evidence)
- NOT Phase B extensions (F8 for artefact; Phase B = when runtime enforcement materialises)
- NOT the organizational substrate itself (→ O-01; Foundation specifies O-01, is not O-01)
- NOT Pillar C text alone (→ O-08; Pillar C = sub-object within Foundation, treated separately due to constitutional weight)

**Dissent D-2 (carried from Task 1 — NOT resolved):**
- Eng view: U.System + U.Mechanism
- Phil counter: U.Episteme (language-state LOCKED documents), NOT U.Work operational system per A.4
- FPF-grounded resolution: BOTH are correct for different «faces» of Foundation (A.4 design-face = U.Episteme LOCKED; run-face = U.System partially instantiated). Brigadier surfaces to Ruslan per OQ-3.

**Cross-refs:**
- → O-01 (constitutes: Foundation specifies the operational substrate)
- → O-08 (contains: Pillar C is sub-system of Foundation)
- → O-04 (hosted-by: working product capabilities built on Foundation)
- → O-06a (governs: Part 4 governs role taxonomy)

---

## §9 — O-08 — Pillar C конституциональная система (12 Tier-2 rules)

**FPF primitive:** U.Commitment (A.2.8) + Guard-Rails analog (E.5)
**FPF Part hosting:** Part E — Constitution (analog)
**Applicable FPF mechanisms:**
- A.2.8 U.Commitment — 12 rules as deontic commitment objects (MUST NOT / SHALL)
- E.5 Guard-Rails — Default-Deny table (11 entries) = machine-enforcement subset
- A.6.B Boundary Norm Square — L/A/D/E claim classification for constitutional rules
- B.3 F-G-R — DOGFOOD principle: every promoted claim carries F/G/R

**CRITICAL NOTE (phil × critic CE-4):** Three distinct sub-categories of rule collapsed under «12 hard rules»:
(a) Machine-enforced: Rule 11 (Default-Deny) — F8 enforcement confirmed
(b) Human-review conventions: Rules 1/3/8/9 — enforced by Ruslan review, not machine
(c) No machine-enforcement path yet: R12 — text LOCKED, mechanism vapor
Different F-G-R per cluster. See §15 dissents.

**Что есть (concrete, evidenced):**

- 12 Tier-2 constitutional rules text LOCKED: inlined in CLAUDE.md §4.1, canonical at principles/tier-2-system/foundation-generic/.
  [F8 · jetix-pillar-c-text · R-high] [src: CLAUDE.md §4.1 Tier 2 Constitutional «12 hard rules»; swarm/wiki/foundations/principles/architecture.md]
- Default-Deny table (11 entries) PRESENT: .claude/config/default-deny-table.yaml — Rule 11 machine-enforced.
  [F5 · jetix-pillar-c-operational · R-high] [src: CLAUDE.md §Foundation Architecture v1.0 «.claude/config/default-deny-table.yaml — Part 6b §I.2 constitutional_never_list (11 entries)»]
- R12 anti-extraction additive 2026-05-12: text LOCKED; AWAITING-APPROVAL packet written.
  [F5 · jetix-constitutional-candidate · R-high] [src: CLAUDE.md §4.1 rule 12 + swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md]
- Halt-Log-Alert response per Part 6b §I.2: specified (F8 ≤1s / F4 ≤5s / F2 ≤60s); runtime = STUB.
  [F4 · jetix-pillar-c-operational · R-medium] [src: JETIX-WORKING-FILE-v0 §5.5; 01-jetix-objects-inventory.md §2 O-08]

**Что задумано (target, aspirational):**

- Machine-enforcement for Rules 1/3/8/9/12 (currently human-review only).
  [F2 · jetix-target · R-low] [src: 01-jetix-objects-inventory.md §8 «OQ-7 (Pillar C enforcement asymmetry)»]
- R12 formally promoted from AWAITING-APPROVAL to full Tier-2 LOCKED rule with enforcement mechanism.
  [F2 · jetix-target · R-low] [src: JETIX-WORKING-FILE-v0 §5.2 «R12 anti-extraction»; swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md]
- Fork-and-leave infrastructure evidenced (not just declared).
  [F2 · jetix-target · R-low] [src: CLAUDE.md §4.1 rule 12 «members can fork-and-leave without penalty»]

**Anti-scope (что НЕ относится):**

- NOT Tier 1 owner principles (→ principles/tier-1-manager/_index.md; agents do NOT enforce Tier 1)
- NOT «12 fully enforced rules» (CE-4: enforcement asymmetry exists; different F-G-R per cluster)
- NOT the Foundation architecture itself (→ O-07; Pillar C is constitutional sub-system hosted BY Foundation)
- NOT R12 enforcement mechanism (→ O-11 for R12 specific analysis)

**Cross-refs:**
- → O-07 (constrains: Pillar C constrains all Foundation writes)
- → O-11 (contains: R12 is additive rule in Pillar C)
- → O-08-self → O-01 (applies-to: all substrate actions governed by Pillar C)

---

## §10 — O-09 — Strategic Insights Hexagon (synthesis cadence 6+1)

**FPF primitive:** U.Work (A.15.1) + Abductive Loop output (B.5.2)
**FPF Part hosting:** Part B (Trans-disciplinary Reasoning); Part 11 (Strategic Direction)
**Applicable FPF mechanisms:**
- B.5.2 Abductive Loop — explicit abductive output (H1-H7 each has alternatives surfaced)
- E.9 DRR — 4-part Decision-Reasoning-Result-Review shape per insight
- B.3 F-G-R — tagged per insight (F4-F5 range; G: jetix-canonical; R: R-high)
- E.17 MVPK partial — 1A (surface view) + 1B (deep view) = two-view publication
- A.10 Evidence Graph — provenance trail per insight (H7 has 4-source trail)

**Что есть (concrete, evidenced):**

- 6 LOCKED strategic insights (H1-H7 range; 2026-05-10..12): each tagged with F-G-R, LOCKED canonical.
  [F5 · jetix-canonical · R-high] [src: JETIX-WORKING-FILE-v0 §5.1 «6 insights LOCKED 10-12 May 2026»; decisions/STRATEGIC-INSIGHT-*-2026-05-10..12.md]
- Hexagon = «closest к FPF intelligence amplification in Jetix» per honest self-audit §7.
  [F4 · jetix-operational-honest · R-high] [src: 06-honest-self-audit.md §7.1 «THIS is the closest to intelligence amplification in Jetix»]
- H7 People-NS LOCKED with 4-source attribution trail (R12 origin).
  [F5 · jetix-canonical · R-high] [src: JETIX-WORKING-FILE-v0 Appendix B; decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md]
- 29 D-Lock entries in Decisions DB (Part 11 host).
  [F5 · jetix-canonical · R-high] [src: CLAUDE.md §Foundation Architecture v1.0 «Strategic Layer F2 promotion queue — decisions/strategic/ (29 D-Lock entries)»]

**Что задумано (target, aspirational):**

- Formal B.5.2 NQD-CAL enforcement: alternatives portfolio declared explicitly, not just summarised.
  [F2 · jetix-target · R-low] [src: 01-jetix-objects-inventory.md §2 O-09 «NQD-CAL informal»]
- Systematized weekly synthesis cadence (currently event-driven, not regular).
  [F2 · jetix-target · R-low] [src: 01-jetix-objects-inventory.md §3 O-09 «Hexagon weekly cadence emerging»]
- Full E.17 MVPK bundle (currently 1A+1B only; bundles for multiple audience types missing).
  [F2 · jetix-target · R-low] [src: JETIX-WORKING-FILE-v0 §10.2 «E.17 MVPK full multi-view bundles — both have viewpoints, neither has full bundles»]

**Anti-scope (что НЕ относится):**

- NOT formal NQD-CAL alternatives portfolio (B.5.2 informal in Jetix; gap acknowledged)
- NOT full E.17 MVPK (2-view partial; not full multi-audience bundle)
- NOT the Vision itself (→ O-03; Hexagon REFINES vision, not IS vision)
- NOT systematized weekly ritual with evidence (cadence not documented as systematic per D-3 dissent)

**Dissent D-3 (carried from Task 1):**
- Eng claim: O-09 = «работает-частично» (partial vs full FPF B.5.2)
- Counter-claim: Within Jetix scope, Hexagon IS complete (generates LOCKED insights with F-G-R + multi-view)
- «Partial» = comparison against FPF bar, not against internal standard
- NOT resolved; preserved per AP-6.

**Cross-refs:**
- → O-03 (refines: Hexagon outputs refine Vision задумка)
- → O-11 (originates: H7 People-NS = R12 origin)
- → O-04 (produced-by: Hexagon insights are outputs of working product activity)

---

## §11 — O-10 — Бизнес-модель Phase 1 (TRM / quick-money consulting)

**FPF primitive:** U.PromiseContent (A.2.3) + U.RoleAssignment (A.2.1)
**FPF Part hosting:** Part A Cluster A.I; Part 10 (External Touchpoints)
**Applicable FPF mechanisms:**
- A.2.3 U.PromiseContent — «управляем 6 ресурсами клиента одновременно» = consumer-facing promise clause
- A.2.8 U.Commitment — mgmt fee + performance fee obligations (не оформлены formally)
- A.6.C Contract Unpacking — not applied to TRM contract language
- B.1.6 Γ_work — TRM tracks 6 resource classes (capital / founder-time / audience / knowledge / compute / talent)

**Что есть (concrete, evidenced):**

- TRM model LOCKED v1.0 (2026-04-30): 6 resource classes + L0-L5 ladder (€3K → €40-60K/мес).
  [F5 · jetix-canonical · R-high] [src: JETIX-TRM-MODEL-2026-04-30.md §1 table «6 resource classes»; JETIX-WORKING-FILE-v0 §3.2]
- ICP INCONSISTENCY detected: Doc 1B = Mittelstand DACH 50-500 emp manufacturing; ACTION-PLAN-PHASE-1 = ABANDONED → Online-first. Doc 1B §7 not updated.
  [F4 · jetix-operational-honest · R-high] [src: 01-jetix-objects-inventory.md §2 O-10 «ICP переопределён в ACTION-PLAN-PHASE-1: Mittelstand → Online-first. Doc 1B §7 не обновлён»]
- Revenue = 0 confirmed; no closed_won CRM records.
  [F5 · jetix-operational-honest · R-high] [src: shared/state/active-projects.json «revenue_current: 0»; 01-jetix-objects-inventory.md §1 O-10]
- Critical path: Tseren/Levenchuk partnership в «24-48h critical» status (7 days elapsed).
  [F4 · jetix-operational · R-medium] [src: 01-jetix-objects-inventory.md §2 O-10 «Critical path: Tseren/Levenchuk partnership — already 7 days в «24-48h critical» status»]

**Что задумано (target, aspirational):**

- First paying client; L0-L5 ladder activation at L1 (€3K hypothesis).
  [F2 · jetix-business-target · R-low] [src: JETIX-TRM-MODEL-2026-04-30.md §1; JETIX-CORPORATION-2026-05-05.md §0 «$100K к концу лета 2026»]
- ICP inconsistency resolved: one canonical ICP documented.
  [F2 · jetix-business-target · R-low] [src: OQ implied by 01-jetix-objects-inventory.md §2 O-10 ICP inconsistency flag]
- TRM at scale: 3 clients L3+ running simultaneously = first network effect.
  [F2 · jetix-business-target · R-low] [src: JETIX-CORPORATION-2026-05-05.md §0 TL;DR «synergy между участниками»]

**Anti-scope (что НЕ относится):**

- NOT current operational revenue (aspiration; revenue = 0 evidenced)
- NOT €100M ARR (→ Layer D future vision; far target)
- NOT the Phase B partnership model (→ O-14; meta-workshop)
- NOT TRM-at-scale without first client (cannot claim «TRM works» without U.Work evidence)

**Cross-refs:**
- → O-02 (implemented-by: TRM = commercial implementation of Corp concept)
- → O-12 (brand-layer-for: business model is part of brand public-facing layer)
- → O-17-candidate (feeds-into: CRM is the operational support for TRM client tracking)

---

## §12 — O-11 — R12 Anti-extraction (конституциональный принцип)

**FPF primitive:** U.Commitment (A.2.8) + U.SpeechAct (A.2.9)
**FPF Part hosting:** Part E — Constitution (additive; NOT in FPF Spec itself)
**Applicable FPF mechanisms:**
- A.2.8 U.Commitment — prohibition-modality deontic: «cannot extract beyond agreed share»
- A.2.9 U.SpeechAct — R12 activation = instituting speech act (Q2 ack 2026-05-12 by Ruslan)
- E.5 Guard-Rails — constitutional addition analogous to Guard-Rails mechanism
- B.3 F-G-R — 4-source attribution trail; F5 text / F2 enforcement per cluster
- E.9 DRR — 4-source trail = DRR-shaped record for R12 origin

**CRITICAL NOTE (phil × critic CE-5):** THREE distinct objects collapsed under «R12»:
(a) Pillar C rule text U.Episteme (F5/R-high; LOCKED)
(b) Applied U.Commitment in specific relationships (F4/R-medium; informal)
(c) Architectural meta-property (F2/R-low; vapor enforcement)
Different F-G-R per face. Do NOT average.

**Что есть (concrete, evidenced):**

- R12 text LOCKED 2026-05-12: CLAUDE.md §4.1 rule 12 + 4-source attribution trail confirmed.
  [F5 · jetix-constitutional-candidate · R-high] [src: CLAUDE.md §4.1 rule 12 «No extraction beyond agreed share»; JETIX-WORKING-FILE-v0 Appendix B]
- AWAITING-APPROVAL packet written: swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md.
  [F5 · jetix-constitutional-candidate · R-high] [src: CLAUDE.md §4.1 rule 12 packet reference; JETIX-WORKING-FILE-v0 §5.2]
- 4-source attribution trail confirmed: H7 People-NS (commit 93b796d) + Game Theory M-C §11 + Q2 ack + AWAITING-APPROVAL packet.
  [F5 · jetix-constitutional-canonical · R-high] [src: JETIX-WORKING-FILE-v0 Appendix B «4-source attribution trail»]
- NOT in FPF Spec (verified per Phase B Step 1); NOT in public IWE template (verified Step 2).
  [F4 · jetix-unique · R-medium] [src: JETIX-WORKING-FILE-v0 §5.2 «NONE in public IWE template»; 06-honest-self-audit.md note]

**Что задумано (target, aspirational):**

- R12 formally promoted from AWAITING-APPROVAL to full Pillar C Tier-2 rule.
  [F2 · jetix-target · R-low] [src: swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md status «Phase B-pending lock»]
- Fork-and-leave infrastructure technically evidenced (not just declared in text).
  [F2 · jetix-target · R-low] [src: CLAUDE.md §4.1 rule 12 «members can fork-and-leave without penalty»]
- R12 surface к FPF community as potential contribution to FPF Part E (OQ-12 open).
  [F2 · jetix-target-strategic · R-low] [src: 01-jetix-objects-inventory.md §8 OQ-12; JETIX-WORKING-FILE-v0 §12 «R12 surfacing к Tseren / Levenchuk»]

**Anti-scope (что НЕ относится):**

- NOT bilateral written agreement (text declaration ≠ signed contract; A.6.C not applied)
- NOT technical fork-and-leave infrastructure (vapor; no evidenced mechanism)
- NOT formal Game Theory mechanism proof (cited informally; not formally proven)
- NOT IWE/FPF community agreement (surface only; Ruslan decides per OQ-12)
- NOT «rule 12 = enforced» (CE-4/CE-5: text LOCKED ≠ enforcement operational)

**Cross-refs:**
- → O-08 (extends: R12 is additive rule in Pillar C)
- → O-13 (governed-by: Clan members governed by R12 per Charter)
- → O-09 (originated-in: H7 People-NS = R12 origin)

---

## §13 — O-12 — Бренд / публичный слой (Jetix public-facing)

**FPF primitive:** U.PromiseContent (A.2.3) + MVPK face (E.17 partial)
**FPF Part hosting:** Part E (E.17 MVPK) + Part A (A.6.3 EpistemicViewing)
**Applicable FPF mechanisms:**
- E.17 MVPK candidate — Doc 1A (Base Mgmt System) + Doc 1B (Corporation) = two-view publication attempt
- A.6.3 EpistemicViewing — audience-specific projections (same described entity → different presentations)
- A.2.3 U.PromiseContent — Jetix = «мастерская для работы с информацией» (consumer-facing promise)
- A.7 Strict Distinction — Workshop as frame ≠ Workshop as formal U.BoundedContext (phil dissent D-PHIL-SCOPE-2)

**Что есть (concrete, evidenced):**

- Doc 1A (Base-Management-System-2026-05-04) + Doc 1B (Jetix-Corporation-2026-05-05) LOCKED: two-audience publication shape.
  [F5 · jetix-brand-canonical · R-high] [src: decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md frontmatter LOCKED; decisions/JETIX-CORPORATION-2026-05-05.md frontmatter «LOCKED v1.0»]
- Workshop metaphor LOCKED v1.0 (decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md): canonical architectural anchor per Ruslan.
  [F5 · jetix-canonical-workshop · R-high] [src: JETIX-WORKING-FILE-v0 §3.1 «LOCKED v1.0; F5 canonical»]
- No formal ViewpointBundle definition per E.17 full MVPK: two views exist (1A/1B), not a complete bundle.
  [F4 · jetix-brand-honest · R-high] [src: 01-jetix-objects-inventory.md §2 O-12 «Gap: нет formal ViewpointBundle definition»]
- Public website does NOT exist; no enterprise pitch deck shipped.
  [F4 · jetix-operational-honest · R-high] [src: 01-jetix-objects-inventory.md §3 O-12 «Public website не существует»]

**Что задумано (target, aspirational):**

- Full E.17 MVPK bundle: multiple audience-specific views (Mittelstand CEO / Partner / Investor / Community member).
  [F2 · jetix-brand-target · R-low] [src: JETIX-WORKING-FILE-v0 §10.2 «E.17 MVPK full multi-view bundles — Jetix has viewpoints, neither has full bundles»]
- Public website + enterprise pitch deck.
  [F2 · jetix-brand-target · R-low] [src: 01-jetix-objects-inventory.md §3 O-12 «Brand = aspirational external-facing layer»]
- Workshop metaphor formalised as A.1.1 U.BoundedContext (если Phil dissent D-PHIL-SCOPE-2 resolved in favour of formalisation).
  [F2 · jetix-brand-target · R-low] [src: D-PHIL-SCOPE-2 dissent «Workshop CONCEPT document = narrative richness без formal A.1.1 structure»]

**Anti-scope (что НЕ относится):**

- NOT the operational substrate (→ O-01; brand = external-facing view of system, not system itself)
- NOT formal U.BoundedContext WITHOUT A.1.1 formalisation (D-PHIL-SCOPE-2 dissent; Ruslan decides OQ-4)
- NOT the Vision document (→ O-03; brand = MVPK view of vision for external audiences)
- NOT full MVPK bundle (E.17 partial only; 2-view, not complete bundle)

**Cross-refs:**
- → O-03 (publication-of: brand = MVPK view of Vision)
- → O-10 (brand-layer-for: brand frames the TRM business model for external audiences)
- → O-19-candidate (implemented-by: 6 outreach files = brand-in-action)

---

## §14 — O-13 — People-Network-State / Clan vision (сетевой паттерн)

**FPF primitive:** U.System (A.1 meta-holon) + Meta-Holon Transition (B.2)
**FPF Part hosting:** Part B (B.2 Meta-Holon Transition) + Part A (A.1 meta-holon)
**Applicable FPF mechanisms:**
- B.2 Meta-Holon Transition — individual masters → Clan = potential MHT event
- B.2.1 BOSC Triggers — signatory addition = Boundary + Scale trigger for system-level shift
- A.1 Holon — 6 archetypes (Hunter/Guardian/Scholar/Creator/Architect/Merchant) as role-holons
- A.2.7 U.RoleAlgebra — 6 archetypes modeled via ⊗ operator (role bundles)
- R12 — constitutional guarantee for Clan members per Charter §1

**Что есть (concrete, evidenced):**

- Clan Charter v0 LOCKED 2026-05-12: constitutional + manifesto; §1 Preamble = Ruslan voice.
  [F5 · charter-applied-now · R-high] [src: JETIX-FIRST-CLAN-CHARTER-2026-05-12.md frontmatter «status: LOCKED; F: F5; G: charter-applied-now»]
- H7 People-Network-State LOCKED (2026-05-12, commit 93b796d): strategic insight parent for Clan concept.
  [F5 · jetix-canonical · R-high] [src: JETIX-WORKING-FILE-v0 §5.1 + §5.2; decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md]
- 0 signatories confirmed: stealth launch declared; 5-base/10-target/10-15-ambition goal.
  [F4 · jetix-operational-honest · R-high] [src: JETIX-FIRST-CLAN-CHARTER-2026-05-12.md frontmatter «signatories_confirmed: 0; signatories_target: 5 base / 10 target»]
- 6 archetypes declared (ach'нуто per Q-D2 2026-05-12): Hunter/Guardian/Scholar/Creator/Architect/Merchant.
  [F5 · charter-applied-now · R-high] [src: JETIX-FIRST-CLAN-CHARTER-2026-05-12.md §1.0a + frontmatter «realm_scope: FULL 6 archetypes»]

**Что задумано (target, aspirational):**

- 5+ signatories within 60d (R-value of charter: refuted_if_no_first_signature_within_60d).
  [F2 · charter-target · R-low] [src: JETIX-FIRST-CLAN-CHARTER-2026-05-12.md frontmatter «R: refuted_if_no_first_signature_within_60d_OR_Ruslan_rejects_draft»]
- L2 federation phase (≥1K members, 12-24 months per Charter §1).
  [F2 · charter-target · R-low] [src: JETIX-FIRST-CLAN-CHARTER-2026-05-12.md frontmatter «launch_mode: stealth; NOT для public publication до L3 milestone»]
- Cooperative formation (формальная структура beyond Charter text).
  [F2 · charter-target · R-low] [src: 01-jetix-objects-inventory.md §3 O-13 «cooperative formation»]

**Anti-scope (что НЕ относится):**

- NOT 5+ signatories today (0 confirmed; vapor as instantiated network)
- NOT public phase (stealth launch; NOT для public до L3 per Charter)
- NOT cooperative legal formation (text only; no legal structure)
- NOT Jetix OS itself (→ O-01; Clan = separate network layer; members ≠ AI agents)
- NOT meta-workshop (→ O-14; Clan = member network; meta-workshop = hosting supersystem)

**Cross-refs:**
- → O-11 (governed-by: R12 = constitutional guarantee for Clan members)
- → O-14 (supersystem-for: meta-workshop hosts partner workshops; Clan = member network within)
- → O-09 (originated-in: H7 People-NS = conceptual parent of Clan)

---

## §15 — O-14 — Meta-workshop для профессиональных мастеров (Phase B target)

**FPF primitive:** U.System (A.1 supersystem) + U.Method (A.3.1 hosting)
**FPF Part hosting:** Part A Cluster A.II + B.2 MHT (Meta-Holon Transition)
**Applicable FPF mechanisms:**
- A.1 Holon (meta-level) — meta-workshop = supersystem holon hosting partner-instances
- A.3.1 U.Method — meta-workshop hosts partner methods (each partner = fork + specialise)
- A.5 Kernel Modularity — partner-instance = fork of Jetix kernel (not duplicate)
- B.2.2 MST — meta-workshop activation = system emergence event (supersystem forming from holons)
- R12 — binding constitutional guarantee when partners join substrate

**Что есть (concrete, evidenced):**

- Doc 1B framing: «Jetix — мета-мастерская для профессиональных мастеров со своими мастерскими».
  [F4 · jetix-phase-B-framing · R-medium] [src: JETIX-CORPORATION-2026-05-05.md §0 TL;DR verbatim; JETIX-WORKING-FILE-v0 §3.3]
- Fork guide v0 (§11 working file) = minimal viable scaffold for instantiation — F2 experimental.
  [F2 · future-pattern-experimental · R-low] [src: JETIX-WORKING-FILE-v0 §11 «F2 — experimental»]
- No partner-instances today; no interop protocol documented.
  [F4 · jetix-operational-honest · R-high] [src: 01-jetix-objects-inventory.md §3 O-14 «Vapor. Phase C IWE cooperation = activation path»]

**Что задумано (target, aspirational):**

- Phase C IWE cooperation plan Tier 3 activation enables first partner-instance.
  [F2 · jetix-phase-C-target · R-low] [src: JETIX-WORKING-FILE-v0 §11.3 «Phase C remit if cooperation plan progresses»]
- Formal Jetix↔partner interoperability protocol (currently no spec).
  [F2 · jetix-phase-C-target · R-low] [src: 01-jetix-objects-inventory.md §2 O-14 «NOT: formal protocol для partner-Jetix interoperability»]
- Multi-Clan federation = B.2.2 MST event: system emergence from individual partner holons.
  [F2 · jetix-phase-C-target · R-low] [src: JETIX-WORKING-FILE-v0 §3.3 «When this activates, R12 anti-extraction becomes the canonical guarantee binding partner-instances»]

**Anti-scope (что НЕ относится):**

- NOT implemented partner-instances today (vapor; concept-only)
- NOT Phase A or Phase B deliverable (Phase C+)
- NOT IWE itself (different unit; IWE = single intellectual worker; meta-workshop = hosting network)
- NOT the Clan network (→ O-13; Clan = member network; meta-workshop = supersystem hosting partner workshops)
- NOT active IWE cooperation plan (in progress; Tier 1/2/3 options in outreach/JETIX-FPF-COOPERATION-PLAN)

**Cross-refs:**
- → O-13 (supersystem-for: meta-workshop hosts Clan member workshops in Phase C+)
- → O-05 (enabled-by: forkable methodology enables partner instantiation)
- → O-02 (corporate-form-for: Corp concept = the formal entity hosting meta-workshop)

---

## §16 Aggregate Dissents Preserved (cross-object, per AP-6)

**D-1 (carried from Phase B Step 2):**
- «IWE» в C5 Левенчука = paid AI guide on aisystant, NOT public FMT-exocortex-template v0.31.0.
- Impact: all Jetix-vs-IWE comparisons scoped to public template (B2 blocker).
- [F4 · R: refuted_if_Aisystant_B2_unblocks_AND_paid_guide_matches_template_architecture]

**D-2 (O-07 FPF typing — NOT resolved):**
- Eng view: O-07 = U.System + U.Mechanism
- Phil counter: O-07 = U.Episteme (LOCKED documents per A.16 language-state; NOT U.Work operational system per A.4)
- Engineering integrator's position: BOTH apply to different «faces» of Foundation per A.4 Temporal Duality. This is not a contradiction — it's an accurate description of a dual-faced artefact.
- Brigadier surfaces to Ruslan via OQ-3.
- [F3 · R: refuted_if_FPF_Part_A_authors_clarify_U.System_vs_U.MethodDescription_boundary]

**D-3 (O-09 Hexagon status — NOT resolved):**
- Eng claim: «работает-частично» (vs full FPF B.5.2 NQD-CAL)
- Counter-claim: Within Jetix scope, Hexagon IS complete. «Partial» = comparison against FPF bar.
- Both positions preserved.
- [F3 · R: refuted_if_Hexagon_cadence_documented_as_systematic_weekly_ritual_with_alternatives_portfolio]

**D-PHIL-SCOPE-2 (O-12 Workshop metaphor — NOT resolved):**
- Position: Workshop = LOCKED canonical architectural anchor (Ruslan-dictated).
- Dissent (phil): Workshop CONCEPT = narrative richness WITHOUT formal A.1.1 BoundedContext (glossary + invariants + scope). «LOCKED canonical» ≠ formal-structure-declaration.
- Engineering integrator note: the dissent is FPF-grounded. A.7 Strict Distinction separates use from mention. Workshop-as-metaphor (mention) ≠ Workshop-as-BoundedContext (use). IF Phase 0 output requires formal FPF anchor, A.1.1 formalisation needed. IF narrative frame suffices, no action.
- [F4 · R: refuted_if_JETIX-WORKSHOP-CONCEPT_2026-04-30_contains_explicit_A.1.1_fields]
- Ruslan decides per OQ-4.

**D-CE-4 (O-08 Pillar C enforcement asymmetry — acknowledged, not resolved):**
- «12 constitutional rules» collapses machine-enforced (Rule 11) + human-review (Rules 1/3) + vapor-enforcement (R12) into single F-level claim.
- Different F-G-R per enforcement cluster:
  - Rule 11 (Default-Deny): F8/R-high
  - Rules 1/3/8/9 (human-review): F5/R-medium (depends on Ruslan attention)
  - R12 (text only): F5-text/F2-enforcement
- Not a defect — reflects real state. Needed for honest FPF scope characterisation.
- [F4 · acknowledged · not-resolved-by-integrator]

---

## §17 Open Questions Surface'нуты через Deep Dive

> **R1 Constitutional posture.** Surface only. Ruslan decides. No recommendations.

**OQ-T2-1 (per-object FPF primitive finality).** For O-07 Foundation: which FPF primitive is PRIMARY for Phase 0 FPF scope work? If U.Episteme (A.16 face) → scope = «designing the operational system». If U.System (A.1 face) → scope = «analysing the operational system». Different Phase 0 outputs.

**OQ-T2-2 (Workshop formalisation trigger).** D-PHIL-SCOPE-2 is load-bearing for O-12 brand/public layer. Trigger: does Phase 0 output REQUIRE formal A.1.1 BoundedContext for Workshop? If yes → formalisation task needed. If narrative frame sufficient → no action.

**OQ-T2-3 (O-10 ICP inconsistency).** Doc 1B §7 (Mittelstand DACH) vs ACTION-PLAN-PHASE-1 (Online-first). Two conflicting ICPs for the same business model. NOT resolvable by this cell (R1). Surface: which canonical ICP is authoritative?

**OQ-T2-4 (O-06a/b boundary for FPF scope).** Phase 0 FPF scope definition needs to declare which level of «agents» is in scope. O-06a (type-level, 12 role-types) = architectural analysis. O-06b (token-level, ROY swarm 6 active) = operational analysis. Different FPF mechanisms apply.

**OQ-T2-5 (O-11 R12 three-face priority).** For FPF scope: is R12 primarily (a) constitutional text to be typed as U.Episteme, (b) an applied U.Commitment to be tracked per relationship, or (c) an architectural meta-property requiring system-wide evidence? Different Phase 0 tasks per answer.

**OQ-T2-6 (O-04 vs O-07 primary anchor).** §6 (reference-frame stability from Task 1) names O-04 as most rigorous anchor. Engineering integrator confirms: O-04 (U.Work evidenced) is more stable than O-07 (artefact LOCKED; operational partial). Surface: does Ruslan agree that O-04 = primary anchor for «what Jetix is now»?

**OQ-T2-7 (FPF primitive coverage completeness).** 14 objects mapped to A.1 / A.2 / A.3 / B.2 / B.3 / B.5.2 / E.5 / E.9 / E.17 primitives. FPF Parts C/D/F/G not yet applicable at Jetix's current maturity. Surface: are there FPF primitives I did NOT map that should be mapped for Phase 0 scope?

---

## §18 Engineering Integrator Packet (structured return)

```yaml
mode: integrator
context:
  task_id: phase-0-fpf-scope-2026-05-17-task-2
  cycle_id: phase-0-fpf-scope-2026-05-17
inputs:
  - {cell: "engineering × integrator (this)", draft_path: "swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-engineering-integrator-per-object-deep.md", summary: "14 objects deep-described; each has что-есть + что-задумано + anti-scope + cross-refs + F-G-R claims"}
  - {cell: "brigadier-input", draft_path: "reports/phase-0-fpf-scope/01-jetix-objects-inventory.md", summary: "Task 1 integrated inventory — primary input for Task 2"}

synthesis:
  - claim: "14 objects mapped to FPF primitives; duality artefact/system present in majority of objects"
    F: F4
    ClaimScope: "holds for Jetix Phase 0 per-object deep description based on Task 1 inventory + canonical sources"
    R: {refuted_if: "object count < 14 in output OR anti-scope missing for any object", accepted_if: "all 14 objects have что-есть + что-задумано + anti-scope + ≥3 F-G-R claims + cross-refs"}
  - claim: "4 FPF primitive clusters identified: organisational-substrate (A.1+A.2 cluster) / transformation-engine (A.3+A.15+B.5 cluster) / constitutional (A.2.8+E.5 cluster) / conceptual-vapor (A.15.2+B.2 cluster)"
    F: F4
    ClaimScope: "holds for Jetix Phase A; clusters may shift with Phase B operational depth"
    R: {refuted_if: "a 5th cluster is identified OR an object does not fit any 4 clusters", accepted_if: "all 14 objects fit one of 4 clusters without residual"}
  - claim: "CE-1..CE-5 categorical errors from Task 1 are confirmed by per-object anti-scope analysis"
    F: F4
    ClaimScope: "holds for Phase 0 deep description; Task 4 каша cleanup is the remediation path"
    R: {refuted_if: "anti-scope boundaries are not violated in canonical documents", accepted_if: "canonical docs still contain conflations (evidenced in per-object sections)"}

dissents:
  - {source_cell: "phil × critic (Task 1, carried)", claim: "O-07 Foundation = U.Episteme (LOCKED A.16) not U.System operational", F: F4, ClaimScope: "holds for A.4 design-face of Foundation", R: {refuted_if: "operational audit shows all 11 Parts executing", accepted_if: "7 of 11 Parts remain memory/automation dominant"}}
  - {source_cell: "phil × critic (Task 1, carried)", claim: "Workshop metaphor lacks A.1.1 BoundedContext discipline (D-PHIL-SCOPE-2)", F: F4, ClaimScope: "FPF formal anchor requires A.1.1; narrative frame may suffice if not claiming formal BoundedContext", R: {refuted_if: "JETIX-WORKSHOP-CONCEPT-2026-04-30 contains explicit A.1.1 fields", accepted_if: "Workshop doc = narrative only, no A.1.1 fields confirmed"}}
  - {source_cell: "engineering × integrator (self-dissent D-3)", claim: "O-09 Hexagon = partial (vs FPF B.5.2 bar) but complete within Jetix internal standard", F: F3, ClaimScope: "comparative claim against FPF bar only", R: {refuted_if: "cadence becomes systematic weekly with formal alternatives portfolio", accepted_if: "cadence remains event-driven without NQD-CAL discipline"}}

residual_open_questions:
  - "OQ-T2-1: O-07 FPF primitive PRIMARY face for Phase 0 (U.Episteme vs U.System)"
  - "OQ-T2-2: Workshop A.1.1 formalisation trigger"
  - "OQ-T2-3: O-10 ICP inconsistency canonical resolution"
  - "OQ-T2-4: O-06a/b scope level for FPF scope definition"
  - "OQ-T2-5: O-11 R12 three-face priority"
  - "OQ-T2-6: O-04 vs O-07 as primary anchor (Ruslan confirmation)"
  - "OQ-T2-7: FPF primitive coverage completeness"

recommended_next_step:
  - {action: "brigadier integrates with systems-integrator cell + philosophy-critic cell (parallel Task 2 outputs)", dispatch_target: "brigadier-promote", rationale: "per task brief 'Twin task perspectives'"}
  - {action: "surface OQ-T2-1..OQ-T2-7 to Ruslan alongside Task 1 OQ-1..OQ-13", dispatch_target: "HITL", rationale: "R1 constitutional — Ruslan sole strategist; surface only"}
  - {action: "Task 4 каша cleanup brief: CE-1..CE-5 confirmed by per-object anti-scope analysis", dispatch_target: "brigadier", rationale: "Task 4 uses this output as input"}

proposed_writes:
  - path: "swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-engineering-integrator-per-object-deep.md"
    frontmatter: "see file header"
    body: "this file"
    edges_to_add:
      - {from: "task-phase-0-fpf-scope-2026-05-17-task-2", to: "reports/phase-0-fpf-scope/01-jetix-objects-inventory.md", type: "input-consumed"}
      - {from: "task-phase-0-fpf-scope-2026-05-17-task-2", to: "raw/external/ailev-FPF/FPF-Spec.md", type: "canonical-source"}

provenance:
  - {path: "reports/phase-0-fpf-scope/01-jetix-objects-inventory.md", range: "§1 integrated table + §2 per-object notes + §3 functioning vs aspirational + §4 cross-refs + §7 dissents + §8 open questions", quote: "primary input; all object characterisations derived from this"}
  - {path: "raw/external/ailev-FPF/FPF-Spec.md", range: "Table of Content Part A (A.1-A.19) + Part B (B.2/B.3/B.5)", quote: "selective read; primitives referenced per object"}
  - {path: "decisions/JETIX-CORPORATION-2026-05-05.md", range: "frontmatter + §0 TL;DR", quote: "O-02/O-14 provenance"}
  - {path: "decisions/JETIX-TRM-MODEL-2026-04-30.md", range: "frontmatter + §1", quote: "O-10 provenance"}
  - {path: "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md", range: "frontmatter + §0", quote: "O-03/O-05 provenance"}
  - {path: "decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md", range: "frontmatter + §1.0-§1.0a", quote: "O-13 provenance"}
  - {path: "JETIX-WORKING-FILE-v0-2026-05-17.md", range: "§0-§6 + §10-§11 + Appendix B", quote: "cross-reference for multiple objects"}
  - {path: "reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md", range: "§1-§7", quote: "O-04/O-07/O-09 honest-state provenance"}
  - {path: "CLAUDE.md", range: "§System Overview + §Agent Roster + §Foundation Architecture v1.0 + §4.1", quote: "O-01/O-06a/O-07/O-08 provenance"}

confidence: medium
confidence_method: schema-coverage
escalations:
  - {trigger: "peer-input-needed", peer: "systems-integrator × integrator", reason: "feedback loops per object not covered by this cell — parallel Task 2 cell"}
  - {trigger: "peer-input-needed", peer: "philosophy-critic × integrator", reason: "epistemic per-object analysis not covered by this cell — parallel Task 2 cell"}
```

---

*Engineering-expert × integrator draft. 14 objects covered. Each object: что есть + что задумано + anti-scope + cross-refs + ≥3 F-G-R tagged claims. 4 dissents preserved per AP-6. 7 open questions surface'нуты. Constitutional posture: R1 (surface only) + R2 (Foundation read-only) + R6 (provenance per claim). Brigadier integrates с parallel cells.*
