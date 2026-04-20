---
type: gap-analysis
created: 2026-04-20
purpose: Critical comparison Jetix architecture vs Левенчук FPF canon
inputs:
  - raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md (primary reference)
  - raw/external/ailev-FPF/FPF-Spec.md (primary source 62,202 lines)
  - decisions/2026-04-19-architecture-v2-approval.md (Jetix ADR approved)
  - decisions/2026-04-20-jetix-architecture-final-DRAFT.md (D9 draft v0.5)
analyst: claude-opus-4-7
decision-maker-target: ruslan (reviews and approves/rejects recommendations)
unblocks:
  - Potential ADR Chunk 8 "Post-FPF-discovery additions"
  - D6 JETIX-FPF.md writing (enriched с FPF alignment)
alignment-score: 65/100
recommendations-total: 22 (P1×6, P2×10, P3×6)
open-questions-total: 11
lang: [ru, en]
english_summary: >
  Systematic gap analysis comparing Jetix architecture (8 principles, 15 folders,
  18 role-manifests, 8 alphas, full FPF canon) against Anatoly Levenchuk's FPF
  reference spec (62,202 lines, 11 Parts, ~300 patterns). Jetix is 65% aligned
  overall: very strong core ontology (holons, roles, alphas, past-participle,
  3-level creation graph, DRR-as-ADR, P-2/P-10 pillars), medium on governance
  (ADR, Guard-Rails partial), low on boundary discipline (A.6.*), assurance
  calculus (B.3 F-G-R), characteristic spaces (A.17-21), NQD/E-E (C.18-19),
  unified term sheet (F.17), and multi-view publication (E.17). 22 prioritized
  recommendations и 11 open questions ready для Ruslan review.
---

# Gap Analysis: Jetix Architecture vs Левенчук FPF canon

*Prepared by Claude Opus 4.7 (1M context), 2026-04-20. Decision-maker: Ruslan.*

---

## Section 1 — Executive Summary

### 1.1 Jetix architecture overview

**Jetix** — AI-native mega-corporation, оперируемая solo-founder'ом Ruslan'ом
(Berlin) с array из 11 Claude-агентов. Primary рынок — DACH Mittelstand;
secondary — US + русскоязычные с Day 1 через unified Stripe/Wise funnel.
Архитектура v1 Phase 1 состоит из **8 core principles** (Company-as-Code / Role
≠ Executor / 8 True Alphas past-participle / Model D Nested + lightweight
mereology / L0 Executive Core декомпозирован / DACH+US+RU unified / Resource
Accounting 3-tier / Portfolio-of-Directions), **15 folders** материализованных
в parallel-mounted `~/jetix-os/{life-os,jetix}/`, **18 role-manifests**
(5 Ruslan atomic sub-roles + 11 agent roles + 2 Phase 2a stubs), **8 true
alphas** с past-participle state machines (Client / Project / Deal / Content
Item / Hypothesis / Member / Way of Working / **Direction**), **Reference vs
Operational split** (7-layer L0-L7 reference, 4 layers materialized Phase 1:
L0+L1+L2+L4), **full 3-level mereological creation graph**, **full FPF**
(не Lite) 30-50 pages loaded text-based в каждый agent `system.md`, **7+7 day
rollout** (sales Days 1-7, foundation Days 8-14+), **€275-737/mo run rate**.
Stage 3 review зафиксировал 11 Ruslan overrides, все в сторону усиления
Левенчук-дисциплины.

### 1.2 FPF canon overview

**FPF (First Principles Framework)** — pattern language от Анатолия Левенчука
(March 2026, github.com/ailev/FPF), "Operating System for Thought": 62,202
строки, ~300+ patterns в 11 Parts (Preface + A-K). Структура: **immutable
Kernel** (Part A, ~25K строк) содержит U.Entity → U.Holon → {U.System,
U.Episteme} trinity plus Role Taxonomy (A.2), Transformer Quartet (A.3),
Role-Method-Work alignment (A.15), Advanced Mereology (A.14), Boundary
Discipline (A.6.*), Characteristic Spaces (A.17-A.21); **Trans-disciplinary
Reasoning** (Part B): Γ Universal Algebra of Aggregation (B.1), Meta-Holon
Transition MHT (B.2), Trust & Assurance F-G-R (B.3), Canonical Evolution Loop
(B.4), Canonical Reasoning Cycle (B.5); **Kernel Extensions** (Part C, ~10K
строк): Sys-CAL, KD-CAL, Kind-CAL, Method-CAL, Resrc-CAL, Decsn-CAL,
Compose-CAL, NQD-CAL, E/E-LOG и др; **Ethics** (Part D, mostly stub); **FPF
Constitution** (Part E): Vision+Mission (E.1), Eleven Pillars (E.2), Four
Guard-Rails (E.5), DRR Method (E.9), LEX-BUNDLE (E.10), Multi-View Publication
Kit (E.17); **Unification Suite** (Part F): Bridges & CL (F.9), Method Quartet
Harmonisation (F.11), UTS Unified Term Sheet (F.17); **SoTA Patterns** (Part
G): Frame Standard (G.0), CG-Frame Generator (G.1), SoTA Harvester (G.2),
MultiMethodDispatcher (G.5). Parts H-K — navigation/annexes, sparse в
vendored copy. Status: "Normative kernel, eternal alpha".

### 1.3 Top 5 strongest Jetix↔FPF alignments

1. **Role ≠ Executor/Holder split** — Jetix P2 + 18 role-manifests + executor
   binding ↔ FPF A.2 Role Taxonomy + A.2.1 U.RoleAssignment + A.13 Agential
   Role. **Near-perfect match**: Jetix's 5-block `role.md` (identity /
   ontological / method / production_dependencies / evolution) + separate
   `executor-binding.yaml` структурно изоморфно FPF's `Holder#Role:Context`
   pattern. Dynamic role assignment forbidden — FPF-correct.

2. **Past-participle state machine discipline** — Jetix P3 + 8 alphas + Hook 4 ↔
   FPF A.2.5 U.RoleStateGraph + OMG Essence inheritance. Jetix strict-enforce
   mirrors FPF normative stance; pre-commit hook operationalizes что у FPF
   осталось conformance checklist.

3. **Holonic 3-level mereological creation graph** — Jetix MC3 override +
   `wiki/foundations/jetix-creation-graph.md` full Phase 1 ↔ FPF A.1 Holonic
   Foundation + A.14 Advanced Mereology. Jetix's L1 target / L2 creating / L3
   supersystem с edges (part-of / creates / operates-in / methodologically-uses
   / constrained-by) — структурно эквивалентно FPF holarchy. Minor gap: Jetix
   edges не typed по FPF's ComponentOf/PortionOf/PhaseOf.

4. **Role-Method-Work temporal duality** — Jetix 8 alphas past-participle +
   Stage 3 explicit strict-enforce ↔ FPF A.4 Temporal Duality + A.15
   Role-Method-Work. Jetix's `alphas/way-of-working/` ≈ U.Method; alpha-log
   append-only ≈ U.Work records; quarterly OKR ≈ U.WorkPlan.

5. **DRR (Design-Rationale Record) → Jetix ADR** — `decisions/` folder
   structure + 4-component approval format ↔ FPF E.9 DRR Method. Jetix Stage 3
   review ADR (this very artifact) уже следует DRR pattern: Problem frame
   (Chunks context) + Decision (approvals table) + Rationale (quotes + prior
   art) + Consequences (implications for D1-D9).

### 1.4 Top 5 critical gaps

1. **Boundary Unpacking cluster (A.6.*)** is massive в FPF (~10K строк: A.6,
   A.6.B Boundary Norm Square, A.6.C Contract Unpacking, A.6.0 U.Signature,
   A.6.P RPR Relational Precision, A.6.Q Quality Term, A.6.A Action Invitation,
   A.6.H Wholeness) — **effectively unaddressed в Jetix**. Contract templates,
   DPA templates, SKU definitions, SLA clauses всё живут как plain Markdown
   без L/A/D/E routing (Law / Admissibility / Deontics / Work-Effects). Для
   DACH enterprise contracts — это реальный gap (compliance signal lost).

2. **Trust & Assurance Calculus (B.3 F-G-R)** — Jetix tier-system (J-Auto /
   J-Approve / J-Strategic gates) — ad-hoc heuristic, не formal Formality
   + ClaimScope + Reliability triad. Evidence не typed в epistemes; CL
   (Congruence Level) cross-context penalties отсутствуют. Для AI-agent
   deliverables клиентам — missing auditable trust composition, bridge-only
   reuse, pathwise justification. Art. 22 GDPR defence weaker.

3. **Characteristic Space + CSLC (A.17-A.21)** — **полностью отсутствует в
   Jetix**. Нет A.17 CHR-NORM canonical characteristic formalism, нет A.18
   CSLC-KERNEL (Characteristic/Scale/Level/Coordinate), нет A.19
   CharacteristicSpace с mechanisms (UNM, UINDM, USCM, ULSAM, CPM,
   SelectorMechanism), нет MM-CHR measurement discipline. Consequence:
   comparison (SKU pricing, direction evaluation, agent promotions) — все
   informal. Direction kill criteria subjective, not formal Scale+Level+
   Coordinate.

4. **Unified Term Sheet (F.17 UTS)** + **LEX-BUNDLE (E.10)** — Jetix bilingual
   frontmatter (OT2 Scenario E) частично решает RU/EN/DE разрыв но не
   реализует UTS table where rows = concept-set unified в one FPF U.Type,
   columns = Bounded-Context senses. Glossary отсутствует как artifact. SenseCells
   cite ≥3 distinct Contexts — требование FPF не выполняется. Для 18 agents
   + Mittelstand clients + future hires — ontological drift risk высокий.

5. **Multi-View Publication Kit (E.17)** + **Transduction Graph Architecture
   (E.18)** — Jetix публикует одни и те же artifacts (contracts, proposals,
   reports) для разных audiences (engineers / managers / clients / auditors /
   regulators) без formal Viewpoint+View+Correspondences discipline. OT2
   bilingual separation addresses RU↔EN language dimension но не
   engineer↔manager↔auditor dimension. Для investment-grade audit trail
   (which Jetix заявляет как architectural benefit) — значительный gap.

### 1.5 Overall alignment score: **65 / 100**

**Breakdown:**

| FPF cluster | Weight | Jetix coverage | Contribution |
|---|---|---|---|
| Core ontology (A.1, A.2, A.3, A.4, A.13, A.15) | 20% | 85% | 17.0 |
| Advanced mereology (A.14) | 5% | 75% | 3.8 |
| Boundary discipline (A.6.*) | 10% | 15% | 1.5 |
| Constitutional principles (A.7-A.12) | 5% | 50% | 2.5 |
| Language-state (A.16) | 3% | 10% | 0.3 |
| Characteristic/measurement (A.17-A.21) | 5% | 5% | 0.3 |
| Γ algebra (B.1) | 4% | 20% | 0.8 |
| MHT (B.2) | 3% | 25% | 0.8 |
| Trust F-G-R (B.3) | 5% | 30% | 1.5 |
| Evolution + Reasoning loops (B.4, B.5) | 3% | 60% | 1.8 |
| KD-CAL (C.2), Kind-CAL (C.3) | 4% | 40% | 1.6 |
| Decsn-CAL (C.11), ADR-Kind (C.12) | 3% | 80% | 2.4 |
| Compose-CAL (C.13) | 2% | 50% | 1.0 |
| NQD-CAL + E/E-LOG (C.18, C.19) | 4% | 25% | 1.0 |
| Constitution pillars (E.1-E.5) | 5% | 80% | 4.0 |
| DRR (E.9), LEX-BUNDLE (E.10) | 4% | 65% | 2.6 |
| Multi-View Publication (E.17) | 3% | 20% | 0.6 |
| Unification Suite F.9, F.11, F.17 | 5% | 25% | 1.3 |
| SoTA Kit (G.0-G.5) | 3% | 15% | 0.5 |
| Ethics (D.5 Bias-Audit) | 2% | 20% | 0.4 |
| Navigation H-K | 2% | 40% | 0.8 |
| **Total** | **100%** | — | **65.4** |

### 1.6 Bottom line

> **Jetix is 65% aligned с FPF canon. Strongest alignments — foundational
> ontology (roles, alphas, holons, creation graph, past-participle, DRR
> architecture). Critical gaps — boundary discipline, assurance calculus,
> characteristic spaces, unified term sheet, multi-view publication. 22
> prioritized recommendations proposed (6 P1 critical, 10 P2 valuable, 6 P3
> nice-to-have); 11 open questions require Ruslan judgment.**

**The 35% gap is not uniform failure — это pattern:** Jetix excellently
adopted "the hard ontological core" (the choices Ruslan deliberately overrode
в strengthening direction: full FPF, 3-level mereology, past-participle
strict, role/executor split, FPF-Steward). Gap concentrated в FPF's "middle
tier" (boundary unpacking, characteristic spaces, trust calculus) — patterns
which provide **operational rigour at scale** (dozens of agents, thousands of
contracts, mixed-audience publications) but which solo-founder Phase 1
arguably doesn't need. The question for Ruslan: **which middle-tier patterns
adopt NOW as architectural seams (cheap future-proofing), и which defer to
Phase 2 trigger-based adoption?**

My recommendation: **adopt 6 P1 items Phase 1** (~20-30h extra work) because
they are either (a) cheap architectural seams now-prohibitive-later (F.17
UTS skeleton, A.6 boundary routing в contract template, F.9 Bridge discipline
в bilingual frontmatter), or (b) address real Phase 1 risk (D.5 Bias-Audit
для EU AI Act, B.3 F-G-R skeleton для DPA clients). P2 и P3 — defer к Phase
2a triggers.

---

## Section 2 — Jetix Architecture Snapshot

Сжатый summary Jetix текущего состояния (post Stage 3 review 2026-04-20) в
form сопоставимой с FPF pattern-level analysis.

### 2.1 Eight Core Principles (P1-P8)

Все 8 принципов APPROVED 2026-04-19/20 (ADR Chunks 1-7).

| # | Principle | One-line statement | FPF nearest pattern |
|---|-----------|-------------------|-------|
| **P1** | Company-as-Code, git = SoT | Все управленческое состояние в git; commit = management act; Notion decommission by Day 14 | E.1 Mission ("reliable reasoning as accessible as version control"); E.4 FPF Artefact Architecture |
| **P2** | Role ≠ Executor | 5-block `role.md` archetype + separate `executor-binding.yaml`; dynamic assignment forbidden (founder exception) | A.2 Role Taxonomy; A.2.1 U.RoleAssignment; A.13 Agential Role |
| **P3** | 8 True Alphas + past-participle strict | 8 alphas (Client, Project, Deal, Content Item, Hypothesis, Member, Way of Working, Direction) с past-participle state machines; Hook 4 enforces | A.2.5 U.RoleStateGraph; A.15 Role-Method-Work; A.4 Temporal Duality |
| **P4** | Model D Nested + lightweight mereology | Life-OS root, Jetix nested; edges: part-of, creates, operates-in, methodologically-uses, constrained-by | A.1 Holonic Foundation; A.14 Advanced Mereology (partial — FPF typology richer) |
| **P5** | L0 Executive Core decomposed | 5 atomic Ruslan sub-roles + `executors/ruslan.yaml` multi-binding; agent `strategy-support-analyst` (не strategist) J3 | A.2.1 multi-context role enactment; A.15.1 SlotFillingsPlanItem |
| **P6** | DACH + US + RU unified funnel | Stripe/Wise external multi-currency; EN primary + DE + RU outreach; legal DACH-based | F.9 Alignment & Bridge across Contexts (partial, via bilingual FM) |
| **P7** | Resource Accounting 3-tier | Tier-1 ledger: Capital + Compute + Deep Hours; Tier-2 quarterly: Attention Budget; Phase 3: Ecosystem (11 cat) | C.5 Resrc-CAL (partial — FPF richer); E.16 RoC-Autonomy Budget |
| **P8** | Portfolio of Directions | `directions/_active|_hypotheses|_archived/<slug>/`; Direction как 8-ая alpha; 3 portfolio edges | No direct FPF analog — **Jetix innovation** (closest: C.18 NQD archive + C.19 E/E-LOG explore/exploit governance) |

### 2.2 Reference vs Operational split

**Reference Architecture (design-time):** Полный 7-layer stack L0-L7.
- L0 Executive Core (strategic management)
- L1 Foundation (legal entity, compliance, ops)
- L2 Cognitive (ontology discipline, FPF, wiki)
- L3 Customer Relations (CRM, sales, community)
- L4 Revenue (products, deals, invoices, directions operational)
- L5 Alliance / Community / Membrane
- L6 Research Engine
- L7 Holdings / Federation

**Operational Architecture Phase 1 MVA** materializes 4 layers:
- L0 (5 atomic sub-roles + ruslan.yaml)
- L1 (partial: entity-stub, DPO external, advisory informal, ops artifacts Day 13)
- L2 (as discipline — FPF text в каждом agent system.md, wiki/ + alphas/ + creation-graph full)
- L4 (directions/_active/ai-consulting-dach/ operational)

**Triggered materialization для L3/L5/L6/L7** (5+ concurrent clients → L3 full;
1st L4 client closed → L5 Alliance; 3+ active directions → L6 full; 2nd
entity → L7 federation).

**FPF nearest pattern:** A.5 Open-Ended Kernel & Extension Layering + E.4 FPF
Artefact Architecture. Reference/Operational split — Jetix innovation beyond
FPF (FPF не distinguishes design-time "reference" vs "operational
materialization" explicitly).

### 2.3 Fifteen Phase 1 folders в `~/jetix-os/jetix/`

| # | Folder | Purpose | FPF analog |
|---|--------|---------|-----|
| 1 | `agents/<id>/` | Combined role + executor + system + scratchpad (11 agents) | A.2 Role Taxonomy bundle |
| 2 | `alphas/` | 8 subfolders, past-participle state machines | A.2.5 U.RoleStateGraph instances |
| 3 | `alpha-log/` | Append-only event log (single log Phase 1) | A.15.1 U.Work records |
| 4 | `clients/` | Markdown CRM (companies/, contacts/, deals/) | U.System entity catalog |
| 5 | `directions/` | Portfolio: `_active\|_hypotheses\|_archived/` | No direct FPF — closest C.18 NQD archive |
| 6 | `wiki/` | Cross-cutting knowledge, `scope: jetix` | U.Episteme slot graph (C.2.1) informal |
| 7 | `decisions/` | ADR + postmortem + letter + strategy + weekly + okr + policy + quarterly + promotions + fpf-stewardship + backlog + templates | E.9 DRR; E.3 Principle Taxonomy |
| 8 | `evals/<role>/` | Golden datasets + manual evaluation | G.9 Parity/Benchmark Harness |
| 9 | `docs/` | Diátaxis 2-form: how-to + reference | E.6 Didactic Architecture |
| 10 | `finance/` | Invoices + ledger + compute-ledger + resource-ledger | C.5 Resrc-CAL (partial) |
| 11 | `inbox/` | Voice-notes pipeline output | A.16 PreArticulationCuePack analog (unaddressed) |
| 12 | `outreach/` | `_shared/` templates cross-direction | F.9 Bridge CL per-context |
| 13 | `entities/jetix-gmbh/` | Federation stub (inactive Phase 1) | U.System super-holon stub |
| 14 | `governance/` | advisory-board, trustee-designations, beirat, aufsichtsrat | A.13 Agential Role + E.3 precedence |
| 15 | `ops/` | hit-by-bus, business-continuity, incident-playbook, gdpr-art-33, disaster-recovery | B.4.1 evolution loop stabilize-route |

Plus `CONSTITUTION.md`, `CLAUDE.md`, `README.md`.

### 2.4 Eight True Alphas + state machines

| # | Alpha | States (past-participle) | FPF U.Type | FPF pattern |
|---|-------|-------------------------|------------|----|
| 1 | Client | lead-identified → qualified → proposed → in-negotiation → won / lost → churned | U.System (кастомер как bearer) + U.RoleAssignment (ClientRole) | A.2 + A.2.5 |
| 2 | Project | scoped → kicked-off → started → delivered → closed → in-follow-up | U.Work (dated occurrence) + U.WorkPlan | A.15.1 + A.15.2 |
| 3 | Deal | drafted → signed → activated → completed / cancelled | U.Commitment (deontic) + U.SpeechAct | A.2.8 + A.2.9 |
| 4 | Content Item | drafted → in-review → approved → published → retired | U.Episteme w/ life-cycle | C.2.1 U.EpistemeSlotGraph |
| 5 | Hypothesis | formulated → under-validation → validated / invalidated → implemented | U.Episteme (claim; F-G-R defeasible) | B.3 + C.2 (KD-CAL) |
| 6 | Member | applied → invited → activated → flagged-at-risk → churned | U.System + U.RoleAssignment (MembershipRole) | A.2.1 |
| 7 | Way of Working | drafted → implemented → refined → deprecated | U.Method + U.MethodDescription | A.3.1 + A.3.2 |
| 8 | **Direction** | hypothesized → under-validation → validated → activated → scaled → plateaued / invalidated / dropped → archived | **No direct FPF analog** (Jetix innovation) | Closest: C.18 NQD archive entry + C.19 E/E-LOG action |

**Key observation:** Alpha 5 (Hypothesis) and Alpha 8 (Direction) both
ontologically sit в `U.Episteme` with state graphs; Direction additionally
holds portfolio-of-bets relationship (container of hypotheses/experiments)
которая ближе к C.18 NQD Archive + E/E-LOG Front/Archive/Governor pattern.
FPF's Γ_nqd.archive operation could formalize direction lifecycle.

### 2.5 Eighteen role-manifests (Phase 1 full-depth)

**5 Ruslan atomic sub-roles** (L0 decomposition per P5):
- `strategy-lead` — direction selection, strategic decisions
- `framing-lead` — problem framing, hypothesis formation
- `sales-closer` — deal closing, client relationship authority
- `acceptance-authority` — deliverable approval, quality gate
- `external-relations` — advisor/investor/media relationships

**11 agent roles** (Phase 1 MVP):
- `manager` (Sonnet 4.6, MGMT) — coordination hub
- `personal-assistant` (Haiku 4.5, OPS) — productivity, OPS lead
- `system-admin` (Haiku 4.5, OPS) — infrastructure
- `sales-lead` (Sonnet 4.6, Sales) — sales coordination
- `sales-researcher` (Haiku 4.5, Sales) — prospect research
- `sales-outreach` (Haiku 4.5, Sales) — outreach & community
- `inbox-processor` (Haiku 4.5, Brain) — information triage
- `crazy-agent` (Sonnet 4.6, Meta) — creative disruption
- `knowledge-synth` (Sonnet 4.6, Brain) — deep synthesis
- `strategy-support-analyst` (Opus 4.6, J3, renamed from strategist) — support только
- `meta-agent` (Sonnet 4.6, Meta) — system auditing + **FPF-Steward sub-role** (R12 override)

**2 Phase 2a stubs:** `dpo` (external-mode) / `customer-success` (J2).

**Note:** `life-coach` migrates в `life-os/agents/life-coach/` per Area 7
decision (не part of Jetix ladder).

**FPF nearest:** A.2 Role Taxonomy + A.13 Agency Spectrum (agent grade per
A.13:4.4 Agency Grade didactic layer). Jetix uses custom J-Auto / J-Approve /
J-Strategic ladder (3 tiers) vs FPF's Agency Grade spectrum (multi-grade
bounded specialization).

### 2.6 FPF (internal, renamed from Lite) — максимальная Левенчук глубина

**Override #9** (Area 6 decision 2026-04-20): **FPF-Lite → FPF full**
(constitutional-depth, 30-50 pages, 3 passes), loaded full-text в каждый
agent `system.md` (Override #10 OT5 Variant A). Internal-only Phase 1
(review trigger €1M+ ARR).

**13 sections planned:**
1. Target System (full L0-L7 + Model D)
2. Stakeholders (all 11 Ecosystem categories per P7)
3. Creation Graph — full 3-level mereological
4. Client Principles
5. Internal Principles — 8 (agents-as-master-class)
6. 8 True Alphas с states past-participle
7. Ritual Cadence (4 rituals/quarter + strategizing event-not-ceremony)
8. U-Types Full — expand от 6 (Lite) до full set
9. What ШСМ is NOT (expanded protection section)
10. Mereology — full (holons recursive)
11. NEW: 17 trans-disciplines reference (which apply, which referenced)
12. NEW: Full FPF architectural invariants
13. NEW: Constructor/Category theory applications

Plus separate artifacts: `wiki/foundations/jetix-creation-graph.md`,
`shsm-primitives.md`, `holon-hierarchy.md`.

### 2.7 Portfolio of Directions model (8-ой principle + 8-ая alpha)

**Override #8** (Area 6). Jetix = research engine + operational infrastructure
для multiple bets ("Шаурмечные, кибербезопасность, AI-tools, и т.д."). Модель:
Hybrid Variant 1+4 — folder-per-direction + Direction как 8-ая true alpha.

**Graph edges** (6 total — 3 Simplifier baseline + 3 portfolio-specific):
- `related`, `supports`, `contradicts` (baseline)
- `belongs-to-direction`, `applies-to-direction`, `sames-as-crm` (portfolio)

**Frontmatter convention:** `direction: <slug>` или `directions: [list]` для
cross-cutting concepts; `crm_ref`, `alpha_ref` для denormalized linking.

**Use case example:** Müller GmbH prospect в ai-consulting-dach direction —
`clients/companies/muller-gmbh.md` (CRM state) + `wiki/entities/muller-gmbh.md`
(Knowledge) + `directions/_active/ai-consulting-dach/pipeline.md` (portfolio) +
`alphas/client/instances/muller-gmbh.yaml` (state machine). `/ask "что знаю
про Müller"` traverses graph: CRM → wiki → research → direction → state →
synthesis.

### 2.8 DACH + US + RU unified funnel

**Override #5** reverses v2 "DACH-locked" stance. Все клиенты через Stripe/Wise
single payment flow. Outreach split per language (`de/`, `en/`, `ru/` — не
translations, cultural tuning). Contract templates: EN primary + DE; RU
nice-to-have. Tax: reverse-charge VAT / W-8BEN-E — Steuerberater consult
Phase 2a. Partial R10 reversal (Rejection formal preserved, но Stripe
creates external pathway).

### 2.9 Resource Accounting (4-resource first-class + Phase 3 Ecosystem)

**Override #1** добавил Compute как 4-ый first-class ресурс. **Override #2**
refined Hours → Deep Hours (attention-weighted). **Override #3** detailed
11 Ecosystem categories для Phase 3.

**Tier-1 ledger (monthly):** `finance/resource-ledger.yaml` — Capital +
Compute + Deep Hours.

**Tier-2 decision (quarterly):** `decisions/quarterly/YYYY-QN-attention-theme.md`
— attention allocation per direction.

**Per-executor compute contract** в `executors/<id>/binding.yaml`:
`model_preference`, `fallback_models`, `thinking_mode`,
`max_tokens_per_session`, `cache_strategy`, `latency_class`, `escalation_rules`.

**FPF nearest pattern:** C.5 Resrc-CAL (time/energy/FLOPs) + E.16 RoC-Autonomy
Budget. Jetix's 4-resource typology — innovation beyond FPF Resrc-CAL
(which focuses on physical/compute resources; Jetix adds Deep Hours + Ecosystem).

### 2.10 Eleven Ruslan Overrides vs v2 synthesizer

| # | Override | Direction |
|---|---------|-----------|
| 1 | Compute as 4th first-class resource | +Левенчук (more formal) |
| 2 | Deep Hours refinement (attention-weighted) | +Левенчук (sharper) |
| 3 | Ecosystem 11 categories detailed | +Левенчук (more complete) |
| 4 | Trustee TBD ≠ Anton | +pragmatic (defer name) |
| 5 | DACH + US + RU unified funnel Day 1 | +scope (more markets) |
| 6 | Full 3-level mereological Phase 1 | **+Левенчук** (no compromise) |
| 7 | Physical Life-OS ≠ Jetix Day 1 | +Левенчук (boundary clean) |
| 8 | Portfolio of Directions (8th principle + alpha) | **+Левенчук** (richer ontology) |
| 9 | Full FPF (not Lite), 30-50 pages | **+Левенчук** (max depth) |
| 10 | Full FPF text everywhere (not reference-only) | **+Левенчук** (max permeation) |
| 11 | FPF-Steward sub-role Phase 1 | **+Левенчук** (quarterly audit) |

**All 11 overrides +Левенчук direction.** Zero overrides "less discipline,
more pragmatic." This validates Ruslan's stated stance ("Здесь мне нужен
Левенчук на максимум") и signals that **gap-analysis recommendations toward
more FPF should have high acceptance probability** (subject to cost
constraint).

---

## Section 3 — Pattern-by-Pattern Mapping ⭐ CRITICAL

Систематическое сопоставление FPF 11 Parts vs Jetix architecture. Format:
table per cluster + narrative где нужны nuances.

**Status codes:**
- ✅ Fully covered — Jetix имеет equivalent pattern explicit
- 🟡 Partially covered — concept present but not formal / not named
- ❌ Not covered — missing в Jetix, consider add
- ⭐ Jetix-specific — Jetix added beyond FPF

**All FPF line numbers verified against `raw/external/ailev-FPF/FPF-Spec.md`.**

### 3.1 Part A.0 + A.1 — Onboarding Glossary + Holonic Foundation

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.0 | NQD Onboarding Glossary | 769 | FPF full-text loaded в каждый agent; separate `shsm-primitives.md` artifact | 🟡 | Glossary exists как KB + per-agent; но формальная "NQD onboarding" specific — missing |
| A.1 | Holonic Foundation: Entity → Holon → {System, Episteme} | 1017 | Lightweight mereology in D6 FPF; creation graph с 3 levels (target/creating/super) | 🟡 | Jetix uses "system" informally; не introduces explicit `U.Holon` / `U.Entity` types в spec |
| A.1:4.1 | U.Entity — primitive of distinction | 1050 | No analog | ❌ | Could add при formal FPF sync |
| A.1:4.2 | U.Holon — unit of composition | 1055 | 3-level mereological graph uses implicit holon concept | 🟡 | Not formal type |
| A.1:4.3 | U.Boundary & U.Interaction | 1065 | Asymmetric reference rule (Hook 1) = boundary enforcement | 🟡 | Narrow implementation, boundary concept not theorized |
| A.1:4.4 | Inside/Outside decision procedure (3-step: dependency / interaction / emergence) | 1080 | Life-OS ≠ Jetix separation decision (Item 6) uses similar logic (different, shared, emergent) | 🟡 | Used once, not generalized |
| A.1:4.5 | Archetypal sub-holons | 1090 | 8 true alphas ≈ archetypal sub-holons | 🟡 | Not linked to A.1 explicitly |
| A.1:7 | Conformance Checklist | 1125 | ADR approvals = implicit checklist | 🟡 | |
| A.1.1 | U.BoundedContext (semantic frame) | 1202 | `scope: jetix` frontmatter; `directions/` as bounded contexts per-direction | 🟡 | Implicit; frontmatter `direction:` key implements similar function |

**Narrative:** Jetix's creation graph (D6 FPF Section 3 + `wiki/foundations/
jetix-creation-graph.md`) covers A.1 холонические structure operationally,
но без explicit `U.Entity` / `U.Holon` / `U.System` / `U.Episteme` type
declarations. For Phase 1 solo-founder operation this is arguably sufficient;
для multi-agent discipline (FPF Authority stance) formal types would help
agents disambiguate (e.g., "is `Direction` a U.System or U.Episteme?" —
currently ambiguous; probably U.Episteme with U.System instances but
undocumented).

**A.1.1 BoundedContext specifically is important for Jetix** — each direction
ideally would declare its bounded context explicitly (ICP, lexicon, success
criteria, status semantics). Currently `direction.md` has "thesis, ICP,
economics, conviction" — ICP ≈ bounded context partial. Would benefit from
F.9 Bridge across directions when terms overlap (e.g., "客户" in
ai-consulting-dach vs shaurma-chains — different meaning + lifecycle).

### 3.2 Part A.2 — Role Taxonomy + A.2.1-A.2.9

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.2 | Role Taxonomy | 1403 | 18 role-manifests, 5-block template | ✅ | Strong alignment |
| A.2:4.1 | S-level definitions (normative role levels) | 1435 | Not used | 🟡 | Could be mapped to J0-JX ladder |
| A.2.1 | U.RoleAssignment — `Holder#Role:Context` | 1613 | Executor-binding.yaml ≈ Holder link | ✅ | Jetix 5-block + binding.yaml = A.2.1 + A.2:4.1 together |
| A.2.1:4.5 | No role chains (use algebra) | 1749 | Dynamic role assignment forbidden (с founder exception) | ✅ | Near-identical |
| A.2.1:4.7 | Role algebra within Context (≤, ⊥, ⊗) | 1792 | Not used | ❌ | Could formalize founder multi-binding as ⊗ |
| A.2.1:4.8 | Time & state transition calculus | 1800 | Alpha state machines past-participle | 🟡 | Jetix has state graphs но не full calculus (Windows, Suspensions, Probation) |
| A.2.1:4.9 | Integration with A.15 (Role-Method-Work) | 1835 | 8 alphas implicit A.15 alignment | 🟡 | Not explicit triangulation |
| A.2.2 | U.Capability | A.2 family | Implicit в 5-block method block | 🟡 | Not separate type |
| A.2.3 | U.PromiseContent | A.2 family | Не used | ❌ | Could inform deal/contract templates |
| A.2.4 | U.EvidenceRole | A.2 family | Implicit в approval signoff chains | 🟡 | |
| A.2.5 | U.RoleStateGraph | A.2 family | 8 alpha state machines past-participle | ✅ | Core Jetix alignment point |
| A.2.7 | U.RoleAlgebra (≤, ⊥, ⊗) | A.2 family | Not used | ❌ | |
| A.2.8 | U.Commitment (deontic) | A.2 family | Deal alpha ≈ commitment | 🟡 | Not typed |
| A.2.9 | U.SpeechAct | A.2 family | Cold outreach, contract signing implicit speech acts | ❌ | Not theorized |

**Narrative:** Jetix A.2 core alignment is strong (18 role-manifests + 5-block
structure + dynamic-assignment-forbidden). Gaps are in secondary patterns:
- **A.2.2 U.Capability** — Jetix 5-block method section describes capability
  implicitly (skills, tools, method knowledge). Could be formalized as
  separate `capabilities:` YAML list in binding.yaml.
- **A.2.3 U.PromiseContent** — Jetix Deal alpha could benefit. Currently
  drafted → signed → activated → completed states но не capture "what is
  promised" structurally. SKU catalog (`decisions/policy/sku-catalog.md`)
  partially addresses.
- **A.2.5 U.RoleStateGraph** — Jetix 8 alphas past-participle ≈ FPF canonical.
  One caveat: A.2.5 is specifically *role state* graph (how role gets
  activated/deactivated), whereas Jetix 8 alphas mix role states (Client,
  Member) with entity states (Project, Deal, Content Item, Hypothesis,
  Direction) and method/agreement states (Way of Working). FPF would
  distinguish: Client ≈ U.RoleAssignment state; Project ≈ U.Work phase; Deal
  ≈ U.Commitment lifecycle. Jetix flattens these into uniform 8-alpha
  treatment.

### 3.3 Part A.3 — Transformer Quartet + A.3.1-A.3.3

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.3 | Transformer Constitution (Quartet) | 5466 | Not explicit | 🟡 | Implicit в role-manifest "method" block + executor-binding compute contract |
| A.3:5.1 | Four anchors: System-in-Role / MethodDescription / Method / Work | 5504 | 5-block `role.md` has `method:` field; `alpha-log` has Work records | 🟡 | Concepts present, quartet not named |
| A.3.1 | U.Method (abstract way-of-doing) | 5679 | `alphas/way-of-working/` | ✅ | Near-match |
| A.3.2 | U.MethodDescription (recipe on carrier) | 5944 | Role-manifest `method:` block + `docs/` how-to guides | ✅ | Implicit match |
| A.3.3 | U.Dynamics (law of change) | A.3 family | Quarterly ritual + review triggers | 🟡 | Not formal |

**Narrative:** A.3 Transformer Quartet is the conceptual backbone of FPF's
"who does what by which method, producing what record". Jetix has все 4
anchors operationally but не cross-links them. If role-manifest `method:`
block explicitly referenced `U.Method` (abstract) + `U.MethodDescription`
(docs/ entry) + `U.Work` (alpha-log entry schema), quartet emerges.

**Cheap adoption:** Add `method_refs:` field в role-manifest linking to
`docs/how-to/<method-slug>.md` (MethodDescription) and `alpha-log/` schemas
(Work). Effort: 2-4h for 18 manifests.

### 3.4 Part A.4 — Temporal Duality

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.4 | Temporal Duality + Open-Ended Evolution Principle | 6489 | Past-participle strict + review triggers + quarterly rituals | ✅ | Jetix separates design-time (role.md) from run-time (alpha state, alpha-log) strictly |
| A.4:4.1 | Open-Ended Evolution Principle | 6540 | Portfolio-of-Directions model | ✅ | Jetix P8 ≈ FPF A.4:4.1 stance |

**Narrative:** This is a **strong alignment point**. Jetix's 8-alpha
past-participle + alpha-log append-only + role.md design-time manifest +
executor-binding compute-runtime — all cleanly split design-time (Tᴰ) from
run-time (Tᴿ). Open-ended evolution materialized через Portfolio of
Directions model (hypothesis → validation → activation → scale / drop cycle
— this IS open-ended evolution at business-strategy scale).

### 3.5 Part A.5 — Open-Ended Kernel & Extension Layering

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.5 | Open-Ended Kernel | 6620 | FPF as kernel; Jetix-specific adaptations as extensions | 🟡 | Conceptually present through D6 FPF + D2 folder structure separation; not formal A.5 |

**Narrative:** FPF A.5 кодифицирует что Kernel contains only meta-concepts
(U.Holon, U.Role, etc.) и domain-specific knowledge lives в plug-in patterns.
Jetix follows this spirit: FPF as kernel (30-50 pages), Jetix-specific
decisions в decisions/ folder, role-manifests, alpha state specifics — all
extensions. But Jetix doesn't formally declare "this is kernel, this is
extension layer". A.5 formalism could clarify what Jetix-specific overrides
vs FPF-canonical are.

### 3.6 Part A.6 — Boundary Discipline (massive cluster) ⚠️ CRITICAL GAP

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.6 | Signature Stack & Boundary Discipline | 6671 | None | ❌ | |
| A.6.B | Boundary Norm Square (Law / Admissibility / Deontics / Work-Effects) | 7097 | Contract templates plain markdown, no L/A/D/E routing | ❌ | **Critical gap for DACH compliance** |
| A.6.C | Contract Unpacking for Boundaries | 7741 | Not used | ❌ | Could transform DPA template quality |
| A.6.0 | U.Signature — law-governed SubjectKind declaration | 8062 | Implicit в SKU catalog; not typed | ❌ | |
| A.6.1 | U.Mechanism — law-governed application | 8341 | Not used | ❌ | |
| A.6.2 | U.EffectFreeEpistemicMorphing | 8634 | Not used | ❌ | Could apply to OT2 auto-translation hook (effect-free cross-register) |
| A.6.3 | U.EpistemicViewing (describedEntity-preserving) | 9060 | Multi-view publication implicit (bilingual frontmatter) | 🟡 | Partial |
| A.6.4 | U.EpistemicRetargeting | 10159 | Not used | ❌ | |
| A.6.P | Relational Precision Restoration (RPR) | 10601 | Not used | ❌ | |
| A.6.Q | Quality Term Precision Restoration (Q-TERM) | 11326 | Not used | ❌ | |
| A.6.A | Action Invitation Precision Restoration (ACT-INV) | 12076 | Not used | ❌ | |
| A.6.5 | U.RelationSlotDiscipline (n-ary relations) | 12797 | Not used | ❌ | |
| A.6.6 | U.BaseDeclarationDiscipline | 13560 | Not used | ❌ | |
| A.6.7 | MechSuiteDescription | 14078 | Not used | ❌ | |
| A.6.8 | Service Polysemy Unpacking (RPR-SERV) | 14519 | Not used | ❌ | Could apply to SKU "Audit" definition (multiple senses) |
| A.6.9 | Cross-Context Sameness Disambiguation (RPR-XCTX) | 14997 | Partial — `sames-as-crm` edge type implements narrow case | 🟡 | One of 6 Jetix edges partial match |
| A.6.S | Signature Engineering Pair (Target + Constructor) | 15419 | Not used | ❌ | |
| A.6.H | Wholeness Language Unpacking (RPR-WHOLE) | 15851 | Not used | ❌ | |

**Narrative (critical gap):** Cluster A.6.* (~10K строк, most extensive FPF
sub-cluster) — **effectively unused in Jetix**. This is expected (A.6 is
advanced discipline), но some sub-patterns are *extremely* relevant:

- **A.6.B Boundary Norm Square** — для contract/SLA/DPA/SKU definition это
  mandatory. Each boundary clause routed to one of 4 lanes:
  - **L (Law)** — regulatory citation (GDPR, EU AI Act, UStG §14, BDSG)
  - **A (Admissibility)** — conditions under which clause activates
  - **D (Deontics)** — who-must/may/must-not
  - **E (Work-Effects)** — what run-time behavior is required
  
  Jetix contract/DPA templates currently mix all 4 lanes into one prose
  paragraph. For DACH Mittelstand legal compliance this creates ambiguity
  ("is this GDPR clause or SLA?"). A.6.B routing would be high-value lift.

- **A.6.C Contract Unpacking** — направлено ровно на это: раскатывание
  contract paragraphs в routed atomic claim set + evidence pointers. Jetix
  Audit SKU (€2-5K) delivery will produce written findings — formal A.6.C
  structure would improve auditability.

- **A.6.H Wholeness Language Unpacking** — relevant для Jetix "holistic"
  language в marketing ("complete audit", "full methodology"). FPF A.6.H
  decomposes wholeness claims into Boundary / Parthood / Fold / Order-Time /
  Completeness lenses — preventing hollow holistic claims.

- **A.6.9 Cross-Context Sameness Disambiguation** — exactly the pattern
  behind Jetix's `sames-as-crm` edge type. Formalizing as A.6.9 Bridge с CL
  (Congruence Level) would strengthen CRM ↔ wiki cross-linking.

**Why Phase 1 priority matters:** Every client contract signed без boundary
discipline accumulates "implicit contract debt" that is costly to unwind при
first GDPR audit or EU AI Act inspection. Adding A.6.B-lite routing to
contract template — perhaps 4-6h work — provides durable architectural
seam.

### 3.7 Part A.7-A.13 — Constitutional Principles + Agency

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.7 | Strict Distinction (Clarity Lattice) | 16217 | Implicit (Object / Description / Carrier не confused в Jetix alphas vs role-manifests vs alpha-logs) | ✅ | Not named but practiced |
| A.8 | Universal Core Principle (C-1) | 16681 | FPF full-text в каждом agent = universal core loaded | ✅ | |
| A.9 | Cross-Scale Consistency (C-3) | 16806 | Mereology 3-level + holons recursive | 🟡 | Consistent в creation graph spec; not enforced elsewhere |
| A.10 | Evidence Graph Referring (C-4) | 16930 | `sources:` frontmatter + inline `[src:]` | ✅ | Native Jetix convention |
| A.11 | Ontological Parsimony (C-5) | 17087 | Simplifier-driven 15 folders (vs Mega-corp 22) | ✅ | Strong Jetix alignment |
| A.12 | External Transformer & Reflexive Split (C-2) | 17194 | Implicit — agents are external transformers to wiki (no self-writing without audit) | 🟡 | Not formalized |
| A.13 | Agential Role & Agency Spectrum | 17328 | J-Auto / J-Approve / J-Strategic = custom 3-tier agency ladder | 🟡 | Jetix uses 3 tiers vs FPF Agency Grade (multi-level spectrum); partial match |
| A.13:4.1 | Agent as contextual role assignment | 17365 | executor-binding.yaml ≈ this | ✅ | |
| A.13:4.3 | Agency-CHR + spectrum | 17385 | Not used | ❌ | Could formalize J-levels |

**Narrative:** A.7-A.12 Constitutional Principles — reasonable alignment
(principles implicit или practiced, не always named). A.13 Agential Role is
critical for AI-native Jetix. FPF Agency Grade (A.13:4.4) provides multi-level
didactic layer — Jetix's 3-tier J-Auto/J-Approve/J-Strategic is simpler
mapping but aligned в spirit. Formal Agency-CHR (A.13:4.3) would allow
tracking "this agent at this task at this scope has agency grade X"
systematically — would inform AI promotion decisions (D7 Area 7).

### 3.8 Part A.14 — Advanced Mereology

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.14 | Advanced Mereology | 17478 | 3-level creation graph + 5 edge types | 🟡 | Jetix has simplified mereology: part-of / creates / operates-in / methodologically-uses / constrained-by. FPF adds typing: ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf |
| A.14:5.1 | PortionOf (metrical, measure-preserving) | 17532 | Not used | ❌ | Could apply to finance/ ledger partitioning |
| A.14:5.2 | PhaseOf (temporal parts of same carrier) | 17556 | Implicit в alpha state transitions | 🟡 | Past-participle states ≈ PhaseOf |
| A.14:6 | Decision table (which relation to use) | 17584 | Not used | ❌ | |

**Narrative:** Jetix's 3-level mereological creation graph = **A.14 at
concept level**. But FPF A.14 provides 5 specific part-of types:
- **ComponentOf** (structural discrete) ≈ Jetix "part-of"
- **ConstituentOf** (logical, e.g., sections/lemmas) — Jetix wiki pages
  within concepts (implicit)
- **PortionOf** (metrical, e.g., "5 kg of 20 kg billet") — Jetix finance
  partitioning (Compute budget portions to directions), time budgets per-direction
- **PhaseOf** (temporal, same carrier) — Jetix alpha state transitions (same
  client, qualified phase → in-negotiation phase). Critical for "same client,
  different lifecycle stage" discipline.
- **MemberOf** (collection, NOT part-of) — Jetix direction cohort membership

Adopting A.14 typed edges would make creation graph 5× more expressive with
~2-3h work to re-label existing edges. **Medium priority recommendation.**

### 3.9 Part A.15 — Role-Method-Work Alignment (critical)

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.15 | Role-Method-Work Alignment | 17754 | 18 role-manifests + 8 alpha state machines + alpha-log | ✅ | Jetix core alignment |
| A.15:4.1 | Strict Distinction (Role / Method / MethodDescription / Capability / WorkPlan / RoleAssignment / Work) | 17807 | Not all 7 entities named; Role + Method (as way-of-working alpha) + Work (alpha-log) explicit | 🟡 | MethodDescription, Capability, WorkPlan, RoleAssignment implicit |
| A.15:4.2 | Canonical relations (`bindsCapability`, `isDescribedBy`, `isExecutionOf`, `performedBy`) | 17846 | Not named | ❌ | |
| A.15.1 | U.Work (record of occurrence) | 18020 | alpha-log entries + `decisions/quarterly/` work records | ✅ | |
| A.15.1:5 | Work mereology (sub-works, parallelism, retries) | 18098 | Alpha-log entries не composed; single event log Phase 1 | 🟡 | Flat, not hierarchical |
| A.15.2 | U.WorkPlan (schedule of intent) | 18389 | Quarterly OKR + 7+7 day rollout = WorkPlans | ✅ | |
| A.15.3 | SlotFillingsPlanItem | 18548 | Not used | ❌ | |

**Narrative:** A.15 is another **strong alignment point**. Jetix's 18 roles
+ `way-of-working` alpha (Method) + alpha-log (Work records) + quarterly OKR
(WorkPlan) cover все 3 layers of A.15 at functional level. Missing formalism:
not all 7 A.15:4.1 entities are explicit (esp. U.Capability, U.WorkPlan
distinct from OKR); canonical relations (`bindsCapability` etc.) not named.
For multi-agent discipline this is acceptable; for 30+ agent scale (Phase 2b)
these formalisms start to matter.

**One Jetix divergence worth noting:** FPF A.15.1:5 treats Work as mereological
tree (parent Work composed of sub-Works, Γ_time / Γ_work roll-ups). Jetix's
flat single-event-log Phase 1 sacrifices this. At 1000+ events scale or
multi-direction compute aggregation this becomes limiting.

### 3.10 Part A.16 — Language-State Transduction (GAP)

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.16 | Language-State Transduction Coordination | 18954 | Not used | ❌ | |
| A.16:4 | Owned move family (typed moves between language states) | 18993 | Not used | ❌ | |
| A.16:4.5 | Move-note threshold | 19028 | Not used | ❌ | |
| A.16:13 | Lawful Move Matrix | 19092 | Not used | ❌ | |

**Narrative:** A.16 deals с cues/ideas that are "too important to ignore но
too early to settle" — exactly Jetix `inbox/` folder (voice-notes pipeline
output). Currently inbox items are processed by `inbox-processor` agent
without typed moves: they get reviewed, then routed to appropriate alpha /
wiki / decisions. FPF A.16 provides formal `PreArticulationCuePack` +
typed move notes (Inquiry / Incident-control / Hypothesis-seeding / etc.) +
endpoint owners. For Jetix: this could upgrade `inbox-processor` from
informal triage to formal language-state router.

**Not priority Phase 1** (inbox volume low), но architecturally clean for
Phase 2+ when voice-notes scale to 10+/day.

### 3.11 Part A.17-A.21 — Characteristic Space + Dynamics ⚠️ MAJOR GAP

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| A.17 | Canonical Characteristic (A.CHR-NORM) | 20064 | Not used | ❌ | |
| A.18 | Minimal CSLC (Characteristic / Scale / Level / Coordinate) | 20202 | Not used | ❌ | |
| A.19 | CharacteristicSpace & Dynamics Hook | 20359 | Not used | ❌ | |
| A.19 + | SURF-SPACE, SUPPORT-VIEW, CN-frame, CPM, SelectorMechanism, UNM/UINDM/USCM/ULSAM | various | Not used | ❌ | |
| A.20 | U.Flow.ConstraintValidity (Eulerian) | 24927 | Not used | ❌ | |
| A.21 | GateProfilization | 25224 | Not used | ❌ | |

**Narrative (major gap):** ~5000 lines of FPF (A.17-A.21 + A.19 sub-patterns)
operationalize measurement, scaling, characterization, and governed
selection. **Jetix has NO formal characteristic space.** Consequences:

- **Direction kill criteria** (Portfolio model) — currently informal
  thresholds. A.18 CSLC would formalize: Characteristic ("direction
  commercial viability"), Scale ("ordinal: plateaued / scaling /
  invalidated"), Level ("3 consecutive months"), Coordinate (specific
  MRR/conversion/etc).
- **SKU pricing** — currently heuristic (Audit €2-5K). A.17 CHR + A.19
  ComparabilityGovernance frame would allow auditable pricing justification
  (critical для enterprise RFPs).
- **Agent promotion** (J-Auto → J-Approve → J-Strategic) — currently
  meta-agent evidence + Ruslan sign-off. A.13 Agency-CHR + A.17-A.18
  scoring would systematize.

**Phase 1 adoption not feasible** (requires deep pattern knowledge + cases).
**Phase 2 recommendation:** adopt A.18 CSLC minimal для 3 highest-stakes
comparisons (SKU pricing, direction kill criteria, agent promotion).

### 3.12 Part B.1 — Universal Algebra of Aggregation (Γ)

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| B.1 | Universal Algebra of Aggregation | 25581 | Not used | ❌ | |
| B.1.1 | Γ_sys (system-specific) | B.1 family | Compute budget per-direction (ai-consulting 70-80% / hypotheses 15-20% / meta 10-15%) — informal | 🟡 | Γ_sys-like aggregation semantics |
| B.1.2 | Γ_epist (knowledge-specific) | B.1 family | Not used | ❌ | |
| B.1.5 | Γ_method (order-sensitive) | B.1 family | Not used | ❌ | |
| B.1.6 | Γ_work (work as spent resource) | B.1 family | Resource-ledger implicit Γ_work | 🟡 | |
| B.1 invariants | WLNK/MONO/IDEM/COMM/LOC | B.1 family | Not used | ❌ | |

**Narrative:** B.1 Γ algebra provides typed aggregation operators с preserved
invariants. Jetix Compute budget per-direction uses Γ_sys-flavour
aggregation implicitly (WLNK: weakest-link; MONO: more direction = more cost
budget). Γ_work and Γ_time flavours apply naturally к alpha-log aggregation.
Not priority Phase 1 (typing complexity > current benefit), but architectural
seam worth preserving (don't bake in assumptions that break Γ invariants).

### 3.13 Part B.2 — Meta-Holon Transition (MHT)

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| B.2 | Meta-Holon Transition | 27444 | Acknowledged в KB Q5 (decision: defer practical application Phase 1) | 🟡 | Conceptually known, not applied |
| B.2:4.2 | BOSC-A-T-X triggers | B.2 family | Not used | ❌ | |
| B.2 events | Fusion / Fission / Phase Promotion / Role-Lift / Context Reframe | B.2 family | Phase 2a trigger (Triple-AND) = implicit Phase Promotion event | 🟡 | |

**Narrative:** Jetix Phase transitions (Phase 1 → 2a → 2b → 2c → 3) ARE
meta-holon transitions semantically. Phase 2a trigger (Triple-AND: €20K MRR ×
3mo + Ruslan >40% L1/L2 + ≥1 DPA) → git-filter-repo extraction. BOSC-A-T-X
partially maps:
- **B** (boundary): git-filter-repo splits boundary
- **O** (objective): revenue threshold = objective emergence
- **S** (structural): Life-OS separates from Jetix
- **A** (agency): 1st hire crossing agent-grade threshold
- **T** (temporal): "×3 consecutive months" = temporal consolidation

Formalizing Jetix Phase transitions as B.2 MHT instances would give shared
vocabulary + checklist. Phase 2a documentation would benefit.

### 3.14 Part B.3 — Trust & Assurance Calculus (F-G-R)

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| B.3 | F-G-R Trust Calculus | 28201 | J-Auto/J-Approve/J-Strategic ≈ Reliability-like gates; no F-G-R | 🟡 | |
| B.3 F | Formality (F0-F9) | B.3 family | Not used | ❌ | |
| B.3 G | ClaimScope (USM-based) | B.3 family | `scope: jetix`, direction frontmatter | 🟡 | Narrow |
| B.3 R | Reliability (pathwise, WLNK) | B.3 family | Not used | ❌ | |
| B.3 + CL | Bridge-only reuse with Congruence Level penalties | B.3 family | Not used | ❌ | |

**Narrative:** B.3 F-G-R is FPF's trust-composition engine. Jetix's
J-Auto/J-Approve/J-Strategic tiers are policy-driven gates (decision
authority), not evidence-weighted reliability. For AI-agent deliverables to
clients — critical gap for enterprise DPA/audit: "how do we know this claim
is reliable? what's the evidence provenance? does bridge to another context
lose congruence?"

**Cheap P1 adoption:** Add F (Formality) + R (Reliability) tags in
`decisions/` ADR frontmatter and client deliverable frontmatter. Provides
auditable trust tier. **~3-5h work + ongoing discipline**.

### 3.15 Part B.4 — Canonical Evolution Loop

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| B.4 | Canonical Evolution Loop (Observe → Notice → Stabilize → Route) | 29094 | 4 rituals (daily/weekly/monthly/quarterly) ≈ observe-notice-stabilize cadence | ✅ | Good alignment |

**Narrative:** Jetix's 4 rituals cadence is a direct operational instantiation
of B.4 canonical evolution loop. Daily morning = Observe + Notice; Weekly
Friday = Stabilize (commits review, close-week); Monthly/Quarterly = Route
(OKR, attention-theme, direction changes). Strategizing as event-not-ceremony
= Route when triggered.

### 3.16 Part B.5 — Canonical Reasoning Cycle

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| B.5 | Canonical Reasoning Cycle | 29446 | Not formal | 🟡 | Implicit в Stage 3 review meta-process |
| B.5.1 | Explore → Shape → Evidence → Operate | B.5 family | Implicit в direction lifecycle (hypothesized → under-validation → validated → activated) | 🟡 | |
| B.5.2 | Abductive Loop | B.5 family | Не formal but practiced | 🟡 | |
| B.5.2.1 | Creative Abduction with NQD | B.5 family | Not used | ❌ | |

**Narrative:** Jetix direction state machine + 4 rituals + ADR review process
are informal instantiations of B.5. Creative Abduction с NQD (B.5.2.1)
unused — potential для Portfolio hypothesis generation.

### 3.17 Part C — Kernel Extensions (CALs, LOGs, CHRs)

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| C.1 | Sys-CAL | C.1 family | Implicit в 8 alphas (Client, Project alphas = U.System instances) | 🟡 | |
| C.2 | KD-CAL + C.2.1 U.EpistemeSlotGraph | 30378 | wiki/ 9 entity types informal; no slot graph | 🟡 | |
| C.2.2 | F-G-R Reliability | C.2 family | Not used | ❌ | |
| C.3 | Kind-CAL (typed reasoning) | 33185 | Frontmatter `type:` field partial | 🟡 | |
| C.4 | Method-CAL | C family | `alphas/way-of-working/` | ✅ | |
| C.5 | Resrc-CAL | C family | finance/ ledgers | 🟡 | Partial (FPF richer) |
| C.6 | LOG-CAL | C family | Not used | ❌ | |
| C.7 | CHR-CAL | C family | Not used | ❌ | |
| C.9 | Agency-CHR | C family | J-tier ladder partial | 🟡 | |
| C.10 | Norm-CAL | C family | `decisions/policy/` | 🟡 | |
| C.11 | Decsn-CAL (Decision Theory) | 35856 | ADR format | ✅ | Jetix ADR ≈ Decsn-CAL instance |
| C.12 | ADR-Kind-CAL | C family | `decisions/` folder structure | ✅ | Strong match |
| C.13 | Compose-CAL (Constructional Mereology) | 36503 | 3-level creation graph | 🟡 | |
| C.14/C.15 | M-Sys-CAL / M-KD-CAL (SoS) | C family | Reference architecture multi-layer hint | 🟡 | |
| C.16 | MM-CHR (Measurement & Metrics) | 36702 | Toggl Deep Hours, compute-ledger | 🟡 | |
| C.17 | Creativity-CHR | 37068 | Not used | ❌ | |
| C.18 | NQD-CAL (Novelty + Quality + Diversity) | 37808 | Not used | ❌ | **Could formalize Portfolio** |
| C.19 | E/E-LOG (Explore-Exploit Governor) | 38008 | Implicit в direction activation/archival decisions | 🟡 | |
| C.19.1 | BLP (Bitter-Lesson Preference) | C.19 family | Not used | ❌ | |
| C.20 | Discipline-CAL | 38421 | Not used | ❌ | |
| C.21 | Discipline-CHR (Field Health) | 38521 | FPF-Steward quarterly audit output ≈ discipline health | 🟡 | |
| C.22 | Problem-CHR (TaskSignature) | 38734 | Not used | ❌ | |
| C.23 | Method-SoS-LOG | 39069 | Not used | ❌ | |
| C.24 | Agentic Tool-Use & Call-Planning | 39273 | executor-binding compute contract partial | 🟡 | |
| C.25 | Q-Bundle (-ilities) | 39582 | Not used | ❌ | |

**Narrative (Part C):** Jetix has reasonable coverage on "action / decision"
CALs (C.4 Method, C.11 Decsn, C.12 ADR-Kind) but weak coverage on
"measurement / governance / characterization" (C.7 CHR, C.16 MM-CHR, C.17
Creativity-CHR, C.21 Discipline-CHR). The biggest missed opportunity is
**C.18 NQD-CAL + C.19 E/E-LOG + C.19.1 BLP** for Portfolio of Directions —
which IS a novelty/quality/diversity portfolio and IS an explore-exploit
governance problem. Formalizing Portfolio through NQD-CAL would provide:
- Γ_nqd.generate — hypothesize new direction
- Γ_nqd.updateArchive — archive failed/plateaued directions
- Γ_nqd.illuminate — ensure diversity (not all directions in same market)
- Γ_nqd.selectFront — which directions to activate / scale

**Phase 2 recommendation:** formalize P8 Portfolio through C.18 + C.19
(2-6h work, high conceptual leverage).

### 3.18 Part D — Multi-scale Ethics

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| D.1 | Axiological Neutrality | (stub) | Not used | ❌ | FPF stub itself |
| D.2 | Multi-Scale Ethics Framework | (stub) | Not used | ❌ | Part D mostly aspirational |
| D.3 | Holonic Conflict Topology | (stub) | Informal (e.g., Life-OS ≠ Jetix separation is conflict-avoidance) | 🟡 | |
| D.4 | Trust-Aware Mediation Calculus | (stub) | Not used | ❌ | |
| D.5 | Bias-Audit & Ethical Assurance (Stable) | 39964 | Not used | ❌ | **High P1 relevance for EU AI Act compliance** |

**Narrative:** D.5 Bias-Audit Cycle (BA-Cycle: BA-0 Kick-off → BA-1 Rapid
Scan → BA-2 Panel Review → BA-3 Closure) + Bias Taxonomy (REP / ALG / VIS /
MET / LNG) is **directly operational for EU AI Act compliance**. Jetix's OT3
EU AI Act risk-proportional tier gates (Scenario C) needs bias-audit artifact;
D.5 provides it turn-key. **P1 recommendation:** adopt D.5 BA-Cycle as
quarterly (or per-SKU-delivery) ritual, output `decisions/bias-audit/YYYY-QN-*.md`
reports. ~2-4h Phase 1 setup + ~2h per audit ongoing.

### 3.19 Part E — FPF Constitution & Authoring (Jetix D6 scope)

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| E.1 | Vision & Mission | 40088 | Jetix Constitution implicit | 🟡 | D6 FPF Section 1 Target System ≈ Vision |
| E.2 | Eleven Pillars (P-1 to P-11) | 40148 | Jetix 8 Core Principles | 🟡 | Different (Jetix focused on operational; FPF on meta-framework) |
| E.3 | Principle Taxonomy & Precedence (Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did) | 40264 | Not used | ❌ | |
| E.4 | FPF Artefact Architecture | 40417 | D9 draft + ADR + FPF as artefacts | ✅ | Jetix practices, not formalized |
| E.5 | Four Guard-Rails | 40487 | Partial | 🟡 | |
| E.5.1 | DevOps Lexical Firewall | E.5 family | Not used | ❌ | Jetix uses "yaml", "pre-commit", "git" в FPF — FPF firewall violation |
| E.5.2 | Notational Independence | E.5 family | Markdown + YAML — no lock-in | ✅ | |
| E.5.3 | Unidirectional Dependency (Core → Tooling → Pedagogy) | E.5 family | Not enforced | ❌ | |
| E.5.4 | Cross-Disciplinary Bias Audit | E.5 family | Not used (partial overlap с D.5) | ❌ | |
| E.6 | Didactic Architecture | 40908 | docs/ Diátaxis 2-form | ✅ | |
| E.7 | Archetypal Grounding | 41008 | Examples в role-manifests | 🟡 | |
| E.8 | Authoring Conventions & Style Guide | 41092 | CLAUDE.md + conventions.md | ✅ | |
| E.9 | DRR (Design-Rationale Record) Method | 41506 | ADR format (`decisions/`) | ✅ | Strong match |
| E.10 | LEX-BUNDLE + E.10.P Conceptual Prefixes | 41604 | Not used | ❌ | |
| E.12 | Didactic Primacy & Cognitive Ergonomics | 43066 | Ruslan's Q2 size accepted: 15-20 pages = readable; FPF 30-50 pages = workshop edition | ✅ | |
| E.13 | Pragmatic Utility & Value Alignment | 43154 | 8 principles emphasize outcome (revenue, delivery) | ✅ | |
| E.14 | Human-Centric Working-Model | 43247 | 4 rituals + Deep Hours attention framework | ✅ | |
| E.15 | Lexical Authoring & Evolution Protocol | 43554 | Not used | ❌ | |
| E.16 | RoC-Autonomy Budget & Enforcement | 43738 | Partial via J-tiers | 🟡 | |
| E.17.* | Multi-View Publication Kit | 45107 | OT2 bilingual frontmatter partial | 🟡 | Bilingual = 1 dimension; FPF provides multi-dim (engineer/manager/auditor) |
| E.17.EFP | ExplanationFaithfulnessProfile | E.17 family | Not used | ❌ | |
| E.17.ID.CR | Same-entity rewrite/comparison | E.17 family | Auto-translation hook partial | 🟡 | |
| E.17.AUD.LHR/OOTD | Audit stances | E.17 family | Not used | ❌ | |
| E.18 | Transduction Graph Architecture (E.TGA) | 47502 | Not used | ❌ | |
| E.19 | Pattern Quality Gates | 47985 | Pre-commit hooks partial (4 syntactic) | 🟡 | |
| E.20 | Mechanism Introduction Protocol (MIP) | 48322 | Not used | ❌ | |

**Narrative (E cluster):** E.1-E.4 foundational (Vision/Mission, Pillars,
Precedence, Artefact Arch) — Jetix has operational equivalents but не formal
E.X labeling. E.5 Four Guard-Rails is critical for authoring discipline:
- **E.5.1 DevOps Lexical Firewall** — Jetix actively violates (FPF text uses
  "yaml", "git", "pre-commit hook" — these are tooling tokens, per FPF
  should be abstracted to generic terms). For internal Jetix use это
  probably OK (Ruslan's operational context), но D6 FPF Section 12 "FPF
  architectural invariants" could remediate.
- **E.5.3 Unidirectional Dependency** — Jetix FPF text references Jetix
  folder structure (Sections discuss `finance/`, `alphas/`, etc.) which
  creates reverse dependency (Pedagogy → Core). Clean separation would put
  folder-specific content в D2 only, FPF staying abstract.

**E.9 DRR ≈ Jetix ADR** is strong. Stage 3 approval ADR already has all 4
DRR components (Problem frame / Decision / Rationale / Consequences) though
не labeled as such.

**E.17 MVPK is a Phase 2 priority** для serving multiple audiences (client /
regulator / internal / academic partner).

### 3.20 Part F — Unification Suite

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| F.1 | Domain-Family Landscape Survey | 48995 | Not used | ❌ | |
| F.2 | Term Harvesting & Normalisation | 49329 | Not used | ❌ | |
| F.3 | Intra-Context Sense Clustering | 49645 | Not used | ❌ | |
| F.4 | Role Description (RCS + RSG + Checklists) | 49984 | 5-block role.md covers RCS + RSG | ✅ | Strong |
| F.5 | Naming Discipline | 50333 | CLAUDE.md conventions | 🟡 | Partial (kebab-case, YYYY-MM-DD) |
| F.6 | Role Assignment & Enactment Cycle (Six-Step) | 50641 | Not used | ❌ | Could formalize agent onboarding |
| F.7 | Concept-Set Table | 50898 | Not used | ❌ | |
| F.8 | Mint or Reuse decision | 51194 | Not used | ❌ | |
| F.9 | Alignment & Bridge across Contexts | 51539 | Informal (bilingual FM, edges) | 🟡 | |
| F.9.1 | Bridge Stance Overlay | F.9 family | Not used | ❌ | |
| F.10 | Status Families Mapping (Evidence / Standard / Requirement) | 52232 | Not used | ❌ | |
| F.11 | Method Quartet Harmonisation | 52604 | Not used | ❌ | |
| F.12 | Service Acceptance-Work Evidence Link | 52944 | Not used | ❌ | |
| F.13 | Lexical Continuity & Deprecation | 53281 | Not used | ❌ | Could help track "strategist → strategy-support-analyst" rename |
| F.14 | Anti-Explosion Control | 53594 | Simplifier folder-reduction (22 → 15) ≈ anti-explosion | 🟡 | |
| F.15 | SCR/RSCR Harness | 53 family | Not used | ❌ | |
| F.16 | Worked-Example Template | F family | Not used | ❌ | |
| F.17 | Unified Term Sheet (UTS) | 54586 | Not used | ❌ | **P1 recommendation** |
| F.18 | Local-First Unification Naming Protocol | F family | Not used | ❌ | |

**Narrative (F cluster):** F.17 UTS is the single most actionable missing
pattern for Jetix. Current state: glossary dispersed across FPF, CLAUDE.md,
individual role-manifests. UTS would be one table где rows = concept-set
(one row per FPF U.Type), columns = bounded-context senses (Jetix / ШСМ /
Essence / DACH-legal / AI-industry). Bilingual frontmatter solves language
dimension; UTS solves context dimension. **Recommended P1.**

F.9 Bridges + CL (Congruence Level) formalize cross-context reuse with loss
accounting. Jetix has this informally through `sames-as-crm` edge + bilingual
frontmatter. F.9 would add CL penalty tracking ("Auf Deutsch reviewed by Ruslan
but machine-translated — CL=B+loss"). Valuable Phase 2.

### 3.21 Part G — Discipline SoTA Patterns Kit

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| G.0 | Frame Standard & Comparability Governance (CG-Spec) | 56124 | Not used | ❌ | |
| G.1 | CG-Frame-Ready Generator | 56468 | Not used | ❌ | |
| G.2 | SoTA Harvester & Synthesis | 56902 | Perplexity research + `raw/research/` informal SoTA | 🟡 | |
| G.3 | CHR Authoring | 57406 | Not used | ❌ | |
| G.4 | CAL Authoring | 57845 | Not used | ❌ | |
| G.5 | Multi-Method Dispatcher & MethodFamily Registry | 58316 | Not used | ❌ | |
| G.6 | Evidence Graph & Provenance Ledger | G family | `sources:` frontmatter | 🟡 | |
| G.7 | Cross-Tradition Bridge Calibration | G family | Not used | ❌ | |
| G.8 | SoS-LOG Bundles & Maturity Ladders | G family | Not used | ❌ | |
| G.9 | Parity/Benchmark Harness | G family | Golden datasets per-agent | 🟡 | |
| G.10 | SoTA Pack Shipping | G family | Not used | ❌ | |
| G.11 | Telemetry-Driven Refresh & Decay | G family | FPF-Steward quarterly audit partial | 🟡 | |
| G.12 | DHC Dashboards | G family | Not used | ❌ | |
| G.13 | External Interop Hooks | G family | Not used | ❌ | |

**Narrative (G cluster):** G-patterns are tools for *building* domain
frameworks + tracking SoTA — Jetix is currently a *consumer* of FPF, не
producer. G.2 SoTA Harvester weakly applies (Jetix uses Perplexity для
research). G.9 Parity Harness partially maps to golden datasets per role
(planned Day 10). Other G-patterns irrelevant Phase 1 unless Jetix publishes
its own SPF (Second Principles Framework) for consulting methodology —
unlikely per current roadmap (OT5 decision: internal-only).

### 3.22 Parts H-K — Glossary, Annexes, Navigation

| FPF ID | Pattern | Line | Jetix coverage | Status | Notes |
|---|---|---|---|---|---|
| H | Glossary | (sparse) | FPF loaded in каждый agent | 🟡 | |
| I | Walkthroughs | (sparse) | Not used | ❌ | |
| J.4 | First Practical Entry Route Index | 62110 | Not used in Jetix | ❌ | Could inform D6 FPF reading strategy |
| K | Lexical debt map | 62123 | Not addressed | 🟡 | Could help avoid deprecated terms |

**Narrative:** Parts H-K sparse в vendored copy (2026-04-20). K (lexical debt)
specifies что "axis", "dimension", "generality" — deprecated; use
"Characteristic", "Claim scope" instead. Jetix may have such terms in
existing text — worth scanning when writing D6.

### 3.23 Mapping summary — coverage by cluster

| Cluster | # patterns examined | ✅ Full | 🟡 Partial | ❌ None | Coverage % |
|---|---|---|---|---|---|
| A.0-A.5 (Kernel foundations) | 10 | 3 | 6 | 1 | 60% |
| A.6.* (Boundary) | 18 | 0 | 2 | 16 | 11% |
| A.7-A.13 (Constitutional + Agency) | 9 | 3 | 5 | 1 | 61% |
| A.14 (Advanced Mereology) | 4 | 0 | 3 | 1 | 38% |
| A.15.* (Role-Method-Work) | 7 | 4 | 2 | 1 | 64% |
| A.16 (Language-State) | 4 | 0 | 0 | 4 | 0% |
| A.17-A.21 (Characteristic Space) | 7 | 0 | 0 | 7 | 0% |
| B.1-B.5 (Trans-disciplinary Reasoning) | 13 | 1 | 8 | 4 | 42% |
| C.1-C.25 (Kernel Extensions) | 25 | 3 | 14 | 8 | 40% |
| D.1-D.5 (Ethics) | 5 | 0 | 1 | 4 | 10% |
| E.1-E.20 (FPF Constitution) | 22 | 7 | 8 | 7 | 50% |
| F.1-F.18 (Unification Suite) | 18 | 1 | 3 | 14 | 14% |
| G.0-G.13 (SoTA Kit) | 14 | 0 | 5 | 9 | 18% |
| H-K (Navigation) | 4 | 0 | 2 | 2 | 25% |
| **Total** | **160** | **22** | **59** | **79** | **34% + 37% partial = 49% overall pattern touch** |

**Recoded на content-weighted alignment (from Section 1.5):** 65/100 —
reflects что core patterns (heavily weighted) have higher coverage than
fringe patterns (e.g., A.1-A.5, A.15, E.9 с large weight + good coverage
bring average up; A.6.*, A.17-A.21, F.* с small weights + near-zero coverage
drag less).

---

## Section 4 — Jetix Divergences (judgments)

Места где Jetix intentionally diverges от FPF canon. Для каждого — divergence
description, FPF canonical position, Jetix rationale, risk assessment, verdict.

### 4.1 Divergence 1 — "FPF" name collision

**Divergence:** Jetix uses "FPF" как designation для **Jetix-specific
adaptation** (D6 JETIX-FPF.md). Левенчук uses "FPF" для canonical framework
(github.com/ailev/FPF). Same acronym, different scope. Override #9 explicitly
renamed "FPF-Lite" → "FPF" to signal full-depth implementation.

**FPF canonical position:** FPF-Spec (Readme.md, Preface) treats "FPF" as
proper noun denoting Levenchuk's framework. FPF preface says: "FPF is
closer to architecture for reasoning: a set of reusable patterns and working
forms" — it's a specific artifact, not a generic name.

**Jetix rationale:** Override #9 ("Он не должен быть light — он должен быть
constitutional, адекватный, глубокий. Максимально глубоко всё что можно,
прописываем по Левенчуку"). Ruslan wanted to remove any "Lite" implication;
"FPF" signals constitutional depth.

**Risk assessment:** **MEDIUM.** Short-term Jetix internal use: zero risk
(clear context). Medium-term: if Jetix references FPF-Spec externally
(advisor communications, investor decks, future public publishing decision),
ambiguity "FPF" = Jetix-FPF or Levenchuk-FPF is non-trivial. Attribution.md
requires crediting Levenchuk FPF — naming our derivative "FPF" creates
attribution confusion.

**Options:**
- A. Keep "FPF" (current) — clarity internally, collision externally.
- B. Rename к **"JPF" (Jetix Principles Framework)** — clear distinction,
  losses "FPF" brand alignment.
- C. Rename к **"JETIX-FPF"** — explicit derivative marker, preserves
  Levenchuk-FPF heritage.
- D. Keep "FPF" + add "Jetix FPF adaptation" subtitle — compromise.

**Verdict:** **Revisit recommended.** Option C or D preferred. Preserve
Levenchuk-FPF attribution clarity без sacrificing depth signal. Low-cost
rename (global find-replace).

### 4.2 Divergence 2 — 5 primitives vs 11 Pillars duality

**Divergence:** Jetix D6 FPF plans Section 11 "17 trans-disciplines" +
Section 10 "Mereology full" + Section 6 "8 True Alphas" + uses "5 primitives"
framing (from R-B research) в educational sections. FPF-Spec uses "11
Pillars" (E.2) + pattern IDs (A.X.Y) as primary structure.

**FPF canonical position:** E.2 Eleven Pillars are "non-negotiable pillars
that every artefact, pattern, and DRR must honour". Numbers 1-11, not 5.
Pattern language (A.X.Y.Z) is the organizational framework. Per R-C note:
"5 primitives" не Левенчук's own published taxonomy; it's R-B analytical
synthesis.

**Jetix rationale:** Both artifacts serve different cognitive audiences:
- "5 primitives" (роль / альфа / граф создания / стратегирование / мышление
  письмом) = pedagogically accessible, Russian-speaking audience, onboarding
- "11 Pillars" (P-1 Cognitive Elegance → P-11 SoTA Alignment) = formal,
  cross-scale architectural commitments

**Risk assessment:** **LOW.** Running two registers in parallel is fine if
consistency is maintained. Risk: confusion if Jetix role-manifests reference
"primitive 3" vs "pillar P-8" ambiguously.

**Verdict:** **Keep both.** Make explicit в D6 FPF Section 2 что "5 primitives
= pedagogical frame; 11 Pillars = architectural commitments; each alpha / role
references both registers". Document mapping explicitly to prevent drift.

### 4.3 Divergence 3 — 8-я alpha "Direction" (innovation)

**Divergence:** Jetix adds 8th alpha "Direction" + P8 Portfolio principle.
FPF does not have a Direction/Portfolio alpha type.

**FPF canonical position:** FPF is framework-level; portfolio strategy belongs
to domain extension. FPF C.18 NQD-CAL + C.19 E/E-LOG provide the *calculus*
for novelty/quality/diversity + explore-exploit governance — ingredients for
portfolio semantics but not a packaged "Direction" concept.

**Jetix rationale:** Portfolio of Directions is core architectural parad igm
for mega-corp thinking ("Jetix как холдинг для кросс-функционального
наблюдения"). Without 8th alpha, holding-style emergent structure misses
operational state machine.

**Risk assessment:** **LOW.** This is a legitimate domain extension. FPF
explicitly supports (P-5 FPF Layering: "patterns are modular, declarative
extensions that can be added, replaced, or removed without destabilising the
core"). Direction alpha IS such an extension.

**Verdict:** **Keep.** Document Direction alpha формально как Jetix-specific
extension relative к FPF (with FPF pattern heritage: U.Episteme + C.18 NQD
archive + C.19 E/E-LOG governance). This could be candidate contribution back
к Левенчук FPF community.

### 4.4 Divergence 4 — Past-participle "strict-enforced" vs FPF nuanced

**Divergence:** Jetix P3 + MC6 = strict past-participle enforcement via Hook 4
on все state.yaml files. FPF A.2.5 RoleStateGraph normative normatively but
conformance checklist not strict rejection — it's design review.

**FPF canonical position:** A.2.5 says "states SHOULD be past-tense facts",
recommends checklist verification but does not mandate automated enforcement.
FPF allows edge cases (conditional states, quality scales).

**Jetix rationale:** 52% v1 violations detected; Ruslan override (MC6)
demands strict enforcement for systematic semantic clarity.

**Risk assessment:** **LOW.** Stricter than FPF = more discipline, not less.
Possible edge cases (e.g., "in-progress" state might be legitimate where
event granularity is coarse) — Jetix Hook 4 may false-positive. Mitigation:
Hook 4 has override tag (`past-participle-exempt: true` in frontmatter) for
justified exceptions.

**Verdict:** **Keep strict.** Ruslan's directive. Document override mechanism
in Hook 4 spec. Risk purely operational (edge-case friction), semantic
integrity gain significant.

### 4.5 Divergence 5 — "Model D" Russian terminology vs FPF English

**Divergence:** Jetix P4 uses "Model D Nested Hierarchy" — Russian-derived
terminology (from Левенчук Russian texts). FPF uses "Holonic Foundation +
holarchy" (A.1) + "partonomy" (A.14) throughout.

**FPF canonical position:** FPF is English primary; Russian terms mapped via
bilingual bridges in KB glossary (Section 9). "Model D" не appears в
FPF-Spec.md (verified via Grep).

**Jetix rationale:** "Model D" is Левенчук-originated term (letter "D" = "De"
for "Design"? or subsystem labeling). Used in Russian Level 1 Jetix
documentation. Provides cognitive continuity для Russian-speaking operators.

**Risk assessment:** **MEDIUM.** "Model D" without expansion in FPF-Spec
creates apocryphal reference (could be mis-attributed to FPF). Bilingual
audiences (EN hires Phase 2a) won't recognize "Model D" as FPF concept.

**Verdict:** **Add expansion.** In D6 FPF Section 1, spell out Model D in
English with explicit FPF cross-reference: "Model D Nested Hierarchy =
Левенчук's Russian term for what FPF A.1 Holonic Foundation + A.14 partonomy
instantiate operationally for Jetix/Life-OS relationship." Retain Russian
name as dominant but add English pointer.

### 4.6 Divergence 6 — Role-manifest 5-block structure vs FPF A.2 patterns

**Divergence:** Jetix 5-block `role.md` structure:
1. identity
2. ontological
3. method
4. production_dependencies
5. evolution

FPF A.2 + A.2.1 + F.4 (Role Description = RCS + RoleStateGraph + Checklists)
uses different structuring: RCS (Role Characterisation Space) + State Graph
+ Checklists.

**FPF canonical position:** F.4 Role Description: "RCS + RoleStateGraph +
Checklists" — 3-component canonical structure; A.2.1 U.RoleAssignment
standard (`Holder#Role:Context`).

**Jetix rationale:** 5-block structure evolved from Stage 2-3 review;
optimized for solo-founder + AI-agent readability. Production_dependencies
(block 4) = Jetix-specific (multi-agent orchestration need).

**Risk assessment:** **LOW.** Structures are complementary, not conflicting.
Jetix 5-block captures FPF F.4 essentials:
- identity ≈ RoleAssignment metadata
- ontological ≈ part of RCS (context bindings, scope)
- method ≈ MethodDescription reference + capability checklist
- production_dependencies ≈ Jetix addition (agent coordination)
- evolution ≈ change log

**Verdict:** **Keep but cross-link.** Add appendix в D3 Role Manifests
mapping 5-block to FPF F.4 canonical fields. Helps Phase 2a hires с FPF
background. ~30-60 min mapping effort, high clarity benefit.

### 4.7 Divergence 7 — 3-tier agency ladder (J-Auto/Approve/Strategic) vs FPF Agency Spectrum

**Divergence:** Jetix OT3 EU AI Act Scenario C + D7 Career Ladder = 3-tier
agency gate (J-Auto / J-Approve / J-Strategic). FPF A.13:4.4 Agency Grade +
A.13:4.3 Agency-CHR are multi-grade spectrum with characteristic measurement.

**FPF canonical position:** A.13 Agent = contextual role assignment; Agency
Spectrum is dimensional ("how much agency does this role have at this task
at this scope"), measurable via Agency-CHR.

**Jetix rationale:** 3 tiers are practical for EU AI Act compliance (maps to
risk categories: internal / external reversible / external non-reversible /
strategic-regulatory). Simpler than full spectrum.

**Risk assessment:** **LOW-MEDIUM.** 3 tiers may not capture edge cases (is
"propose client discount" J-Approve or J-Strategic? Ambiguous). Formal
Agency-CHR would allow Scale-based decision.

**Verdict:** **Keep 3-tier as primary; add Agency-CHR as optional fallback.**
When edge cases arise, use A.13 Agency-CHR formalism (Characteristic:
"agency grade", Scale: J0..J-Strategic, Coordinate: specific task-scope
point). Document в `decisions/policy/ai-agent-decision-authority.md`.

### 4.8 Divergence summary

| # | Divergence | Risk | Verdict |
|---|-----------|------|---------|
| 1 | FPF name collision | Medium | **Revisit: consider "JETIX-FPF" rename** |
| 2 | 5 primitives + 11 Pillars duality | Low | Keep, document explicitly |
| 3 | 8-я alpha Direction | Low | Keep, document as FPF extension |
| 4 | Past-participle strict enforcement | Low | Keep strict |
| 5 | Model D terminology | Medium | **Add English FPF expansion** |
| 6 | 5-block role.md | Low | Keep, add F.4 cross-link appendix |
| 7 | 3-tier agency ladder | Low-Medium | Keep, add Agency-CHR fallback |

**Overall:** 0 reversals recommended. 2 minor fixes recommended (Divergences
1 and 5). 5 divergences validated как intentional + justified.

---

## Section 5 — Jetix Innovations (beyond FPF canon)

Положительный material — что Jetix has что FPF-Spec does NOT. These are
potential contributions back к FPF community.

### 5.1 Innovation 1 — Portfolio of Directions as 8th principle + 8th alpha

**Innovation:** Jetix P8 + Direction alpha operationalize holding-pattern
portfolio management explicitly. Folder-per-direction
(`directions/_active|_hypotheses|_archived/<slug>/`) + state machine
(hypothesized → under-validation → validated → activated → scaled →
plateaued / invalidated / dropped → archived) + graph edges
(belongs-to-direction, applies-to-direction, sames-as-crm) + frontmatter
convention (`direction:` / `directions:`).

**Origin:** ADR Chunk 4 Area 6 decision (2026-04-19) — Override #8. Ruslan
directive: "Jetix = большая корпорация, десятки направлений. Шаурмечные,
кибербезопасность, AI-tools. Википедия должна работать с людьми, с CRM,
cross-functional. Jetix как холдинг для кросс-функционального наблюдения."

**FPF gap:** FPF-Spec doesn't package "portfolio" as first-class concept.
Ingredients present: C.18 NQD-CAL (novelty/quality/diversity archive), C.19
E/E-LOG (explore/exploit governor), A.4:4.1 Open-Ended Evolution. Но no
pre-packaged "Portfolio" U.Type with state machine + edges convention.

**Potential contribution back:** Submit pattern proposal к FPF
"Portfolio-CAL: governed portfolio of bounded-context directions" combining
NQD + E/E-LOG + U.BoundedContext + typed edges. Would fit в Part C
(Extensions).

### 5.2 Innovation 2 — Resource accounting 4-tier framework

**Innovation:** Jetix Tier-1 quantitative ledger (Capital + Compute + Deep
Hours) + Tier-2 quarterly (Attention Budget) + Phase-3 first-class (Ecosystem
11 categories). Compute as 4th first-class resource (Override #1). Deep Hours
refined from raw Hours (attention-weighted time, Toggl `[deep]/[shallow]`
tags).

**Origin:** ADR Chunk 1 P7 evolution через 3 iterations 2026-04-19. Override
#1 (Compute first-class) + #2 (Deep Hours) + #3 (Ecosystem 11 categories
detailed).

**FPF gap:** FPF C.5 Resrc-CAL treats resources generally (time, energy,
FLOPs); does not separate:
- Capital (monetary)
- Compute (machine cognition)
- Deep Hours (attention-weighted human cognition)
- Attention Budget (strategic-allocation-level abstraction)
- Ecosystem Resources (relational capital, Phase-3 first-class)

FPF E.16 RoC-Autonomy Budget touches autonomy budgeting but не unified
resource typology for AI-native company.

**Potential contribution back:** Resrc-CAL-AI extension: multi-category
resource calculus for AI-native operations. Especially Deep Hours concept
+ Toggl-style dual-tag tracking — seems novel.

### 5.3 Innovation 3 — AI-native 18 role-manifest architecture

**Innovation:** 5 Ruslan atomic sub-roles + 11 agent roles + 2 Phase 2a
stubs, all full-depth Phase 1 (~35-45h writing budget). Per-executor compute
contract (model_preference, fallback_models, thinking_mode,
max_tokens_per_session, cache_strategy, latency_class, escalation_rules).

**Origin:** Override #11 (FPF-Steward) + Area 3 D3 decision + Chunk 1 P5
decomposition.

**FPF gap:** FPF A.2.1 U.RoleAssignment covers single-assignment pattern.
Jetix multi-role-binding (founder exception) + 18-manifest systematic
architecture + compute-contract-per-executor is AI-native-specific
operationalization not in FPF.

**Potential contribution back:** Pattern submission "Multi-Role-Binding
Agent Architecture" extending A.2.1.

### 5.4 Innovation 4 — FPF-Steward sub-role (Override #11)

**Innovation:** FPF-Steward as sub-role в `agents/meta-agent/system.md`.
Scope: FPF consistency, Alpha/WP/Entity classification, past-participle
verification, concept duplication detection, role-manifest structural
integrity, Direction-concept boundary clarity, frontmatter schema. Quarterly
audit cycle + ad-hoc. Output: `decisions/fpf-stewardship/YYYY-QN-ontology-audit.md`.
Trigger to separate role: 30+ agents OR 1+ human meta-hire OR quarterly
audit >4h.

**Origin:** Override #11 (R12 override, 2026-04-19). Ruslan: "Здесь мне нужен
Левенчук на максимум. Всё что его техника предлагает, мы используем на 100%
на максимум."

**FPF gap:** FPF E.19 Pattern Quality Gates + E.20 MIP (Mechanism Introduction
Protocol) specify authoring discipline but не formalize "Steward" role for
ongoing ontology maintenance. FPF G.11 Telemetry-Driven Refresh partially
addresses but is framework-level не specific-domain role.

**Potential contribution back:** "FPF-Steward Role Pattern" (domain-specific
instantiation of E.19 + G.11 for organizations adopting FPF).

### 5.5 Innovation 5 — Physical Life-OS ≠ Jetix separation (Override #7)

**Innovation:** Parallel mount `~/jetix-os/{life-os,jetix}/` Day 1 +
asymmetric reference rule (Hook 1 blocks Jetix → Life-OS) + Phase 2a git
filter-repo extraction + Phase 3 different servers/clouds.

**Origin:** Override #7 (Area 6 decision). Ruslan: "Life-OS и Jetix должны
быть принципиально вообще разделены, никак не коим образом не смешиваться.
Ничего с Life-OS не должно попадать в Jetix."

**FPF gap:** FPF A.1 U.Boundary covers physical/conceptual boundaries
normatively но не addresses person-corporation boundary (founder's private
life vs company affairs). This is an entrepreneurship/legal issue — FPF as
methodology doesn't prescribe.

**Potential contribution back:** "Multi-Persona Boundary Discipline" pattern
(person A owns corporate holon H and personal holon P; P and H share carrier
person A but have distinct boundaries; asymmetric reference rule enforces
unidirectional knowledge flow).

### 5.6 Innovation 6 — DACH + US + RU unified funnel (Override #5)

**Innovation:** Multi-market от Day 1 через unified Stripe/Wise funnel +
split outreach folders per language (cultural tuning, not translations) +
EN primary + DE + RU contract localization + bilingual frontmatter hybrid.

**Origin:** Override #5 (Chunk 1 P6 modification). Ruslan: "основной упор на
DACH, но при этом ещё будет US и русскоязычное тоже; они все у нас будут
проходить через одну воронку, или через один вид оплаты."

**FPF gap:** FPF F.9 Bridges + F.18 Local-First Unification Naming Protocol
provide multi-context vocabulary alignment. Jetix innovates в *operational
multi-market funnel* pattern (Stripe/Wise external currency; folder-based
cultural tuning vs translation; bilingual frontmatter hybrid).

**Potential contribution back:** "Multi-Market Unification Protocol" —
operational extension combining F.9 + F.18 + DevOps patterns для cross-border
startup operations.

### 5.7 Innovation 7 — 7+7 day rollout operational plan

**Innovation:** Days 1-7 Sales Infrastructure + Days 8-14+ Foundation
(realistic 7+10-12 tolerance); parallel tracks (D6 FPF writing parallel к
Foundation Days 10-14+, migration script post-Day 14).

**Origin:** Override в D8 (Chunk 3 Item 27). Ruslan: "Главное план фиксировать,
чтобы потом по нему адекватно идти и трекать что сделано."

**FPF gap:** FPF is framework-level; rollout plans are domain. However, the
*architecture* of this rollout — Sales-first-Foundation-second, parallel
tracks, realistic tolerance bands — is novel applicable pattern для
bootstrapping FPF-aligned companies.

**Potential contribution back:** "FPF-Aligned Bootstrap Rollout Template"
(7+7 + parallel tracks + tolerance bands) — optional domain companion к
E.4 FPF Artefact Architecture.

### 5.8 Innovation 8 — Company-as-Code + Git = SoT architecture

**Innovation:** P1 establishes git repo як единственный source of truth;
commit = акт управленческого решения; PR як management ritual; Notion
decommission by Day 14; 4+1 pre-commit hooks enforce invariants.

**Origin:** P1 baseline (Chunk 1). Ruslan: "отлично мы это всё подтверждаем,
фиксируем, это уже база прям база."

**FPF gap:** FPF E.1 Mission mentions "reliable reasoning as accessible as
version control" — suggests this spirit but doesn't operationalize "Company-
as-Code" pattern. Company-as-Code is AI-native-management pattern extending
DevOps practice к organizational state.

**Potential contribution back:** "Company-as-Code" operationalization
pattern — pre-commit hooks as ontology enforcement; PR as management ritual;
commit taxonomy (`[area] description`).

### 5.9 Innovation 9 — Full FPF text loading in каждый agent system.md (Override #10)

**Innovation:** 7-10K tokens FPF text loaded in каждом agent's `system.md`
(не reference-only). Maximum ontology permeation. Monthly cost ~$5-10.
Context budget: 25K exocortex hard reservation handles.

**Origin:** Override #10 (OT5 Sub-question 1 Variant A).

**FPF gap:** FPF is silent on "how to make every agent FPF-discipline-aware".
Tooling options span from reference URL to full-text embedding. Jetix
commits to maximum — an operational choice valuable to FPF community facing
"how deep should we load FPF" question.

**Potential contribution back:** "Full-FPF-Permeation Pattern" + cost analysis
+ context-budget analysis.

### 5.10 Innovations summary

| # | Innovation | FPF extension candidate | Future potential |
|---|-----------|-------------------------|------------------|
| 1 | Portfolio of Directions (P8 + 8-я alpha) | Portfolio-CAL (Part C) | High |
| 2 | 4-tier resource accounting (Capital + Compute + Deep Hours + Attention + Ecosystem) | Resrc-CAL-AI (Part C) | High |
| 3 | 18-manifest AI-native architecture | Multi-Role-Binding Agent Pattern (A.2.1 ext) | Medium |
| 4 | FPF-Steward sub-role | FPF-Steward Role Pattern (E.19 / G.11 ext) | Medium |
| 5 | Physical Life-OS ≠ Jetix separation | Multi-Persona Boundary (A.1 ext) | Medium |
| 6 | DACH + US + RU unified funnel | Multi-Market Unification Protocol (F.9 / F.18 ext) | Low-Medium |
| 7 | 7+7 day rollout operational plan | FPF-Aligned Bootstrap Rollout (E.4 companion) | Low |
| 8 | Company-as-Code + Git = SoT | Company-as-Code Pattern (Part E) | High |
| 9 | Full FPF text loading (Override #10) | Full-FPF-Permeation Pattern (E.16 / C.24 ext) | Low-Medium |

**Strategic note:** Innovations 1, 2, 8 are especially high-leverage
contribution candidates. Но per OT5 decision — Jetix internal-only Phase 1+
(publishing review trigger €1M+ ARR). So contribution deferred. Documenting
these innovations carefully now preserves option to contribute later без
reconstructing reasoning.

---

## Section 6 — Recommended Changes к Jetix ⭐ CRITICAL

**22 recommendations total** prioritized P1 (critical) / P2 (valuable) / P3
(nice-to-have). Каждая — fully actionable with cost estimate + dependencies.

### P1 — Critical recommendations (6 items, ~20-30h extra work)

#### Rec-01: Add A.6.B Boundary Norm Square lanes to contract/DPA templates

**Priority:** P1

**FPF basis:** A.6.B Boundary Norm Square (line 7097) — routes every boundary
clause into one of 4 lanes: **Law** (regulatory), **Admissibility**
(conditions), **Deontics** (who-must/may/must-not), **Work-Effects**
(run-time behavior). A.6.C Contract Unpacking (line 7741) applies this к
contracts.

**Current Jetix state:** D8 Day 5 Proposal template, Day 6 Contract+invoice
template, OT3 DPA template Phase 1 — all plain Markdown, no L/A/D/E routing.

**Proposed change:** Add 4-lane routing structure to all 3 templates:
- `client-dpa-template.md` — divide clauses into L/A/D/E sections
- `contract.md` — each SLA clause tagged {L, A, D, E}
- `proposal.md` — pricing and deliverables distinguish A (admissibility)
  from E (work-effects)

**Rationale:** DACH enterprise audit readiness; EU AI Act risk-category
defensibility; client confidence. GDPR audit-trail argumentation improves
significantly. Prevents "contract debt" accumulation.

**Cost:** 4-6h Phase 1 (combined 3 templates) + ongoing discipline (~5 min
per new contract clause to route).

**Risk of not doing:** Each signed contract accumulates implicit ambiguity;
first GDPR/EU AI Act audit requires retroactive unpacking (10-20× cost).

**Dependencies:** None; independent of other recs. Can proceed Day 5-6 of rollout.

---

#### Rec-02: Skeleton Unified Term Sheet (F.17 UTS) for Jetix concepts

**Priority:** P1

**FPF basis:** F.17 Unified Term Sheet (line 54586): "one table that a
careful mind can hold". Rows = concept-set unified into one FPF U.Type;
columns = bounded-context senses.

**Current Jetix state:** Glossary dispersed across FPF KB (this document's
Section 9), CLAUDE.md, individual role-manifests. No consolidated UTS.

**Proposed change:** Create `wiki/foundations/jetix-uts.md` with:
- Layout A (Kernel-first): rows = FPF U.Type; columns = [Jetix /
  ШСМ-Russian / Essence-legacy / DACH-legal / AI-industry / Plain-EN]
- Start с 30-50 core concepts (role, alpha, direction, holon, creation
  graph, DRR/ADR, executor, etc.)
- Each row: FPF U.Type, Unified Tech name, Plain name, Description,
  SenseCells (5 cols), Bridges, Unification Rationale
- Maintain: FPF-Steward quarterly audit

**Rationale:** Bilingual frontmatter solves RU/EN/DE language; UTS solves
Jetix-vs-ШСМ-vs-Essence-vs-industry context. 18 agents + Phase 2a hire + DACH
clients read Jetix artifacts — ontological drift risk high без UTS.

**Cost:** 6-10h initial (30-50 rows × 10-15 min each) + ~2h per quarter
FPF-Steward audit update.

**Risk of not doing:** Concept drift (same term means different things в
role-manifests vs FPF vs client docs); friction при each new hire; reduced
cross-reference quality.

**Dependencies:** Builds on KB Section 9 glossary (already compiled). Can
run parallel к D6 FPF writing.

---

#### Rec-03: Adopt D.5 Bias-Audit Cycle for EU AI Act compliance

**Priority:** P1

**FPF basis:** D.5 Bias-Audit & Ethical Assurance (line 39964) — Bias-Audit
Cycle (BA-0 Kick-off → BA-1 Rapid Scan → BA-2 Panel Review → BA-3 Closure) +
Bias Taxonomy (REP / ALG / VIS / MET / LNG).

**Current Jetix state:** OT3 EU AI Act Scenario C sets 4 risk categories с
gates. No formal bias-audit artifact.

**Proposed change:** Add `decisions/bias-audit/YYYY-QN-bias-audit.md` artifact
per quarter. Structure:
- BA-0: 30-min kickoff per SKU delivery (Bias Register skeleton)
- BA-1: Rapid Scan at end of each sprint/deliverable (Engineer-Scrutineer
  rotation; initially all Ruslan)
- BA-2: Panel Review before major release (if/when Ethics advisor recruited
  to Beirat Phase 2a)
- BA-3: Closure at release freeze

Phase 1: simplified single-person BA-0+BA-1+BA-3 (~1h per audit). Full
Panel Review BA-2 Phase 2a+.

**Rationale:** Direct EU AI Act Art. 22 compliance support; reduces
automation-bias risk в client audit SKUs; creates defensible record.
Complementary к existing `policy/eu-ai-act.md` calendar.

**Cost:** 3-5h Phase 1 setup (template + first 2 audits) + ~2h quarterly
ongoing.

**Risk of not doing:** EU AI Act High-risk obligations live Aug 2026 —
absence of bias-audit artifact weakens compliance posture.

**Dependencies:** Links to `decisions/policy/eu-ai-act.md` (OT3) and
`governance/advisory-board/` (future Ethics advisor slot).

---

#### Rec-04: Formalize F (Formality) + R (Reliability) tags in ADR и client deliverable frontmatter

**Priority:** P1

**FPF basis:** B.3 Trust & Assurance Calculus (F–G–R) (line 28201); F-scale
F0-F9 (informal sketch → formally assured); R (Reliability) pathwise
warrant.

**Current Jetix state:** ADR frontmatter uses `status: approved` but no
formality/reliability typing. Client deliverables untyped.

**Proposed change:** Add `formality:` + `reliability:` fields to
decisions/ ADR и client deliverable frontmatter:

```yaml
---
id: ADR-YYYY-MM-DD-<slug>
formality: F2  # F0 free prose | F1 structured prose | F2 schema'd | F3 typed
reliability: R-medium  # evidence-backed, weakest-link analyzed
claim-scope: jetix.ai-consulting-dach.client-müller  # G (scope)
---
```

Conventions documented in `decisions/policy/trust-tagging.md`.

**Rationale:** Enterprise DPA/audit trail quality; AI-agent deliverables
need auditable trust tier; Art. 22 GDPR defensibility; ~zero runtime cost
once convention fixed.

**Cost:** 3-5h Phase 1 (policy doc + retrofit 10-15 existing ADRs) + ~1
min per new ADR/deliverable ongoing.

**Risk of not doing:** Claims across agent outputs conflated in reliability
(a hypothesis note reads same as validated client deliverable); audit
defensibility weak.

**Dependencies:** Meta-agent onboarding to enforce; FPF-Steward quarterly
audit scope.

---

#### Rec-05: Map 3-level creation graph edges to A.14 typed mereology (ComponentOf / PortionOf / PhaseOf)

**Priority:** P1

**FPF basis:** A.14 Advanced Mereology (line 17478); 5 typed relations
(ComponentOf, ConstituentOf, PortionOf, PhaseOf, MemberOf) vs flat partOf.

**Current Jetix state:** MC3 override — full 3-level mereological graph
Phase 1 с 5 edge types: part-of / creates / operates-in /
methodologically-uses / constrained-by. Does not use A.14 typed sub-relations.

**Proposed change:** Relabel "part-of" edge в creation graph to specific A.14
type based on context:
- `part-of` (generic) → `ComponentOf` when structural discrete (agent is
  ComponentOf meta-agent)
- `part-of` → `ConstituentOf` when logical part (section of ADR)
- `part-of` → `PortionOf` when metrical (5 Deep Hours PortionOf 25
  Deep-Hours weekly budget)
- `part-of` → `PhaseOf` when temporal-same-carrier (Client qualified phase
  PhaseOf Müller-GmbH)

Additionally: document что "operates-in" (supersystem membership) is
MemberOf, not parthood (per A.14 firewall).

**Rationale:** Creation graph becomes 5× more expressive. FPF-correct.
Enables Γ-flavour aggregation later (B.1.1 Γ_sys over ComponentOf, Γ_time
over PhaseOf).

**Cost:** 2-4h (relabel existing edges + document conventions).

**Risk of not doing:** Creation graph grows; retro-typing cost rises
linearly. Better now while graph small.

**Dependencies:** D6 FPF Section 3 (Creation Graph); included в R12 FPF-
Steward quarterly audit.

---

#### Rec-06: Document Jetix Phase transitions as B.2 MHT (Meta-Holon Transition) instances

**Priority:** P1

**FPF basis:** B.2 Meta-Holon Transition (line 27444); BOSC-A-T-X triggers;
5 event types (Fusion, Fission, Phase Promotion, Role-Lift, Context Reframe).

**Current Jetix state:** Phase 2a trigger (Triple-AND), Phase 2b trigger,
Phase 2c, Phase 3 — listed as triggers, not formally typed as MHT.

**Proposed change:** In D1 Section 7 (Migration) or D9 Section 10 (Review
Triggers), add B.2 typing for each Phase transition:

| Phase transition | MHT event type | BOSC-A-T-X triggers |
|---|---|---|
| Phase 1 → 2a | Phase Promotion + Fission | B, O, S, T (boundary split via git filter-repo; revenue objective threshold; structural Life-OS separation; temporal 3-month consolidation) |
| Phase 2a → 2b | Role-Lift | A, S (1st human hire crosses agency threshold; structural team formation) |
| Phase 2b → 2c | Fusion | B, O, X (2nd entity emergence; holding objective; context rebase to federation) |
| Phase 2c → 3 | Context Reframe | B, X, T (different servers; different regulatory contexts; long-term consolidation) |

**Rationale:** Gives shared vocabulary to Phase docs; checklist for what
counts як transition; ontology-preserving versus ontology-breaking changes
distinguished (critical per A.14:8 — if identity criteria break → MHT, not
PhaseOf).

**Cost:** 2-3h (document MHT mapping).

**Risk of not doing:** Phase 2a documentation when triggered will be ad-hoc;
risk of treating MHT как routine state change.

**Dependencies:** None; independent.

---

### P2 — Valuable recommendations (10 items, ~20-40h total)

#### Rec-07: Formalize Portfolio of Directions через C.18 NQD-CAL + C.19 E/E-LOG

**Priority:** P2

**FPF basis:** C.18 NQD-CAL (line 37808) — Γ_nqd.generate / updateArchive /
illuminate / selectFront. C.19 E/E-LOG (line 38008) — Widen / Keep frontier /
Narrow / Sunset / Reroute. C.19.1 BLP Bitter-Lesson Preference.

**Current Jetix state:** P8 Portfolio of Directions operational. No formal
NQD framing.

**Proposed change:** In D1 Section 3 или D5 (Knowledge Architecture), add:
- `directions/_active/` = Front (current Pareto-non-dominated)
- `directions/_hypotheses/` + `_archived/` = Archive (diversity для open-ended search)
- Quarterly attention-theme ritual = E/E-LOG action (Widen / Keep / Narrow /
  Reroute / Sunset)
- Direction activation = Γ_nqd.selectFront promotion
- Direction archival = Γ_nqd.updateArchive с Pareto loss analysis

**Rationale:** Gives formal grounding к Portfolio model. Enables principled
direction selection (не "feels right"). BLP adoption protects against
heuristic-debt.

**Cost:** 6-10h (document NQD mapping + operationalize в quarterly ritual).

**Risk:** Adds conceptual overhead. Mitigation: phase in gradually (quarterly
reviews Q2+).

**Dependencies:** Links with Rec-11 (comparative characteristic space).

---

#### Rec-08: Adopt A.13:4.3 Agency-CHR as fallback when 3-tier ladder ambiguous

**Priority:** P2

**FPF basis:** A.13:4.3 Agency-CHR + A.13:4.4 Agency Grade spectrum.

**Current Jetix state:** 3-tier ladder (J-Auto / J-Approve / J-Strategic)
per OT3 + D7.

**Proposed change:** Document в `decisions/policy/ai-agent-decision-authority.md`
що когда 3-tier ambiguous (edge case: "propose discount €500" is J-Approve
or J-Strategic?), fall back к Agency-CHR coordinate (Scale: J0-J-Strategic,
Characteristic: "discount-authority", Level: "single-transaction", Coord:
specific-role-scope).

**Rationale:** Gives formal resolution для ambiguity без abandoning 3-tier
simplicity.

**Cost:** 2-3h (policy doc update + 2-3 example cases).

**Dependencies:** Part of Rec-02 (UTS) includes agency-CHR entries.

---

#### Rec-09: Implement E.17 Multi-View Publication Kit for client deliverables

**Priority:** P2

**FPF basis:** E.17.* Multi-View Publication Kit (line 45107): Viewpoint +
View + Correspondences.

**Current Jetix state:** Client deliverables single-view (audit report = one
document). Bilingual handling (EN + DE).

**Proposed change:** For high-stakes deliverables (audit SKU output, DPA),
provide multiple views:
- Engineer view (technical findings, FPF-internal vocabulary)
- Manager view (decision-relevant summary, business vocabulary)
- Auditor view (compliance evidence, regulatory citations)

Use E.17.EFP ExplanationFaithfulnessProfile pattern to prove views are
same-entity descriptions.

**Rationale:** Enterprise clients have multi-stakeholder audience; single
view forces compromise. Investment-grade audit trail benefits.

**Cost:** 8-15h (template + 1-2 pilot deliverables) + ongoing effort per
deliverable.

**Dependencies:** Applies к first Audit SKU delivery (Phase 1 target).

---

#### Rec-10: Add F.9 Bridge + CL (Congruence Level) convention for cross-direction wiki

**Priority:** P2

**FPF basis:** F.9 Alignment & Bridge across Contexts (line 51539); CL penalty.

**Current Jetix state:** `sames-as-crm`, `applies-to-direction`,
`belongs-to-direction` edges operational. No CL penalty tracking.

**Proposed change:** Add `cl:` field to cross-direction edges indicating
congruence loss:
- `cl: A` — identical sense (full congruence)
- `cl: B` — adapted sense (minor loss)
- `cl: C` — bridging (substantial loss, interpret carefully)
- `cl: D` — analogy only (non-normative)

Example: concept "Client" in ai-consulting-dach vs shaurma-chains. Same
U.Type (Client alpha) но different ICP, sales cycle, pricing — edge `cl: B`.

**Rationale:** Prevents naive cross-direction reuse; surfaces CL loss explicitly.

**Cost:** 2-3h (convention doc + retrofit 5-10 existing cross-direction
edges).

**Dependencies:** Rec-02 UTS SenseCells depend on CL annotations.

---

#### Rec-11: Build A.18 CSLC Characteristic Space для SKU pricing + direction kill criteria

**Priority:** P2

**FPF basis:** A.18 CSLC-KERNEL (line 20202) — Characteristic / Scale /
Level / Coordinate. A.17 CHR-NORM (line 20064) — canonical characteristic.

**Current Jetix state:** SKU pricing informal (Audit €2-5K heuristic).
Direction kill criteria informal (Ruslan judgment).

**Proposed change:** For 3 high-stakes comparisons, formalize CSLC:
- **SKU pricing:** Characteristic = "client willingness-to-pay-for-value-
  delivered"; Scale = monetary ordinal; Level = SKU tier (S/M/L); Coord =
  specific-quote
- **Direction kill criteria:** Characteristic = "commercial viability slope
  over 3mo"; Scale = {accelerating, stable, plateaued, declining,
  invalidated}; Level = quarter-end; Coord = MRR/conversion/CAC snapshot
- **Agent promotion:** Characteristic = "decision-quality-independent-of-
  human-review"; Scale = J0-J-Strategic; Level = task-family (sales /
  research / synthesis); Coord = specific eval result + evidence

**Rationale:** Makes high-stakes comparison auditable + repeatable.
Supports Rec-07 NQD-based direction selection.

**Cost:** 8-12h (3 cases + CSLC framework doc).

**Dependencies:** Rec-07 NQD formalization benefits; Rec-08 Agency-CHR aligns.

---

#### Rec-12: Adopt E.10 LEX-BUNDLE naming convention для Jetix lexicon

**Priority:** P2

**FPF basis:** E.10 LEX-BUNDLE (line 41604) + E.10.P Conceptual Prefixes.

**Current Jetix state:** Names kebab-case (convention E.5.1 compliant),
but no systematic lexical bundles.

**Proposed change:** Document conceptual prefixes used in Jetix:
- `alpha.*` (e.g., `alpha.client.qualified`)
- `role.*` (e.g., `role.strategy-lead`)
- `direction.*` (e.g., `direction.ai-consulting-dach`)
- `method.*` (e.g., `method.mece-qualification`)
- `sku.*` (e.g., `sku.audit-basic`)

Use in code/docs consistently.

**Rationale:** Namespace collision prevention; improves grep-discoverability;
supports future machine-readable manifests.

**Cost:** 3-5h (convention doc + retrofit существующих names).

**Dependencies:** Rec-02 UTS uses these prefixes.

---

#### Rec-13: Add E.5.1 DevOps Lexical Firewall cleanup для D6 FPF

**Priority:** P2

**FPF basis:** E.5.1 DevOps Lexical Firewall — no domain-specific tokens
(yaml, docker, CI/CD) в Core patterns.

**Current Jetix state:** D6 FPF draft text uses "yaml", "pre-commit hook",
"git", "Claude Code", "Opus 4.7" — tooling tokens.

**Proposed change:** Split D6 FPF into:
- **FPF Core** (abstract, tooling-free, ~20-30 pages): patterns, pillars,
  principles without yaml/git/Claude references
- **FPF Tooling Addendum** (~10-20 pages): how Jetix operationalizes FPF
  через yaml + git + Claude + hooks

**Rationale:** Respects E.5.3 Unidirectional Dependency (Core → Tooling);
makes FPF Core portable (if Jetix migrates from Claude к another LLM, Core
unchanged); supports future publishing decision.

**Cost:** 4-8h (one-time restructure during D6 writing; otherwise negligible).

**Dependencies:** D6 FPF writing (Override #9 directive — first pass + second
pass + FPF-Steward audit pass).

---

#### Rec-14: Formalize B.4 Canonical Evolution Loop mapping в 4 rituals

**Priority:** P2

**FPF basis:** B.4 Canonical Evolution Loop (line 29094) — Observe → Notice
→ Stabilize → Route.

**Current Jetix state:** 4 rituals (daily / weekly / monthly / quarterly)
operational. No B.4 labeling.

**Proposed change:** Document в D8 Section (rituals) що each ritual is an
instance of B.4:
- Daily 30min = Observe (inbox) + Notice (pipeline anomalies) + minimal
  Stabilize
- Weekly Friday 60min = Stabilize (Shape Up + commits review + close-week)
  + initial Route
- Monthly last-Friday 2h = Route (OKR + P&L + founder note + meta-review)
- Quarterly 1-day = Deep Route (letter + attention-theme + role-manifest
  delta + strategy)

**Rationale:** Shared vocabulary across agents; FPF-correct naming.

**Cost:** 1-2h (doc update).

**Dependencies:** None.

---

#### Rec-15: F.6 Role Assignment & Enactment Cycle for agent onboarding

**Priority:** P2

**FPF basis:** F.6 Six-Step Role Assignment Cycle (line 50641).

**Current Jetix state:** `agent_onboarding` field (initial_context_pack +
warm_up_tasks + calibration_checkpoint) in role-manifest. No six-step cycle.

**Proposed change:** Expand `agent_onboarding` to follow F.6 six-step
pattern:
1. Candidate identification (who/what holder)
2. Context binding (U.BoundedContext confirmation)
3. Capability check (U.Capability evaluation)
4. Assignment (Holder#Role:Context)
5. Enactment warm-up
6. Calibration review

**Rationale:** Reduces onboarding variance; supports 18-manifest consistency;
F.6 verification checklist catches integration issues early.

**Cost:** 3-5h (template update + retrofit 18 manifests).

**Dependencies:** D3 Role Manifests writing (Day 9).

---

#### Rec-16: Add C.22 Problem-CHR TaskSignature к client engagement intake

**Priority:** P2

**FPF basis:** C.22 Problem-CHR (line 38734) — TaskSignature (Kind + Scope +
Evidence + Constraints); C.22.1 task-family adaptation.

**Current Jetix state:** Discovery call template (Day 4) + proposal template
(Day 5) — plain business discovery questions.

**Proposed change:** Restructure discovery call template to produce
TaskSignature output:
- Kind: (what U.Type does client need — strategy? implementation?
  integration?)
- Scope: (bounded context, timeline, budget)
- Evidence: (what proof will satisfy)
- Constraints: (regulatory, operational, cultural)

Output: structured TaskSignature YAML attached to `clients/companies/<slug>.md`.

**Rationale:** Systematic intake; matches to MethodFamily (Rec-21 G.5
dispatcher); reduces proposal-writing time.

**Cost:** 3-5h (template + 1-2 pilot calls with revision).

**Dependencies:** Pairs with Rec-21 G.5 Multi-Method Dispatcher.

---

### P3 — Nice-to-have recommendations (6 items, ~15-25h total)

#### Rec-17: A.16 PreArticulationCuePack для inbox/ voice-notes pipeline

**Priority:** P3

**FPF basis:** A.16 Language-State Transduction (line 18954); A.16.1
PreArticulationCuePack.

**Current Jetix state:** `inbox/` folder + voice-notes pipeline; informal
triage by inbox-processor.

**Proposed change:** Structure inbox items as A.16.1 PreArticulationCuePack —
typed cue objects with owner metadata. Formal A.16 move notes for routing
decisions.

**Rationale:** Scales to 10+/day voice notes (Phase 2+); systematic early-
stage idea preservation.

**Cost:** 4-6h (inbox-processor prompt update + cue-pack schema).

**Dependencies:** Phase 2 trigger (inbox volume growth).

---

#### Rec-18: F.11 Method Quartet Harmonisation

**Priority:** P3

**FPF basis:** F.11 Method Quartet Harmonisation (line 52604).

**Current Jetix state:** `alphas/way-of-working/` + role-manifest `method:`
block — not quartet-harmonized.

**Proposed change:** For each method documented, produce F.11 quartet:
Role-who-does / Method-abstract / MethodDescription-recipe / Work-record.

**Rationale:** Methodological clarity; better agent ramp-up for method
adoption.

**Cost:** 5-8h (for 5-10 core Jetix methods).

**Dependencies:** Rec-15 F.6 onboarding.

---

#### Rec-19: A.6.S Signature Engineering Pair для SKU evolution

**Priority:** P3

**FPF basis:** A.6.S Signature Engineering Pair (line 15419) —
TargetSignature + ConstructorSignature.

**Current Jetix state:** SKU definitions в catalog single-signature.

**Proposed change:** When evolving SKU (e.g., Audit v1 → v2 adding new
deliverable), document TargetSignature (what SKU delivers) + ConstructorSignature
(how it's produced). Enables editioning discipline.

**Rationale:** SKU version management; client confidence in stability.

**Cost:** 3-5h (SKU template update + pilot on Audit SKU).

**Dependencies:** Rec-01 contract template includes ref to signature pair.

---

#### Rec-20: E.20 Mechanism Introduction Protocol для Jetix new-pattern adoption

**Priority:** P3

**FPF basis:** E.20 MIP (line 48322).

**Current Jetix state:** Ad-hoc pattern addition (e.g., "Direction alpha"
added by Ruslan directive without MIP).

**Proposed change:** When Jetix introduces new pattern (FPF extension, new
alpha, new edge type), follow E.20 MIP: Problem → Mechanism → Interface →
Pilot → Promote.

**Rationale:** Prevents pattern sprawl; quality gate для ontology evolution;
FPF-Steward review step integrated.

**Cost:** 2-3h (MIP template + documented first use).

**Dependencies:** FPF-Steward quarterly cadence.

---

#### Rec-21: G.5 Multi-Method Dispatcher & MethodFamily Registry

**Priority:** P3

**FPF basis:** G.5 Multi-Method Dispatcher & MethodFamily Registry (line 58316).

**Current Jetix state:** Methods dispersed в `docs/how-to/` and role-manifest
`method:` blocks. No MethodFamily Registry.

**Proposed change:** Create `wiki/foundations/method-family-registry.md` —
table of Jetix methods (MECE qualification, Shape Up weekly, Bias-Audit BA-Cycle,
etc.) + dispatch logic for task-family → method selection.

**Rationale:** Systematic method reuse; method governance; supports Rec-16
TaskSignature matching.

**Cost:** 4-6h (initial registry + 10-15 methods documented) + ongoing
maintenance.

**Dependencies:** Rec-16 TaskSignature; Rec-18 Method Quartet.

---

#### Rec-22: Create `decisions/fpf-stewardship/2026-Q2-ontology-audit.md` for first quarterly audit

**Priority:** P3 (but specifically calendar-bound)

**FPF basis:** FPF-Steward sub-role Override #11 commitment: quarterly
audits.

**Current Jetix state:** Override committed, artifact not yet drafted.

**Proposed change:** Draft first FPF-Steward audit report for 2026-Q2
(running Q2 = April-June 2026):
- Concept duplication scan
- Past-participle violations (Hook 4 residual)
- Role-manifest structural integrity
- Direction-concept boundary clarity
- Frontmatter schema compliance
- UTS delta (if Rec-02 adopted)

Output at Q2 close (late June 2026).

**Rationale:** Commits to promised cadence; establishes template for
subsequent audits.

**Cost:** 2-4h (first audit by meta-agent + FPF-Steward) + template creation.

**Dependencies:** Meta-agent production readiness.

---

### 6.3 Recommendations summary matrix

| # | Rec | Priority | FPF basis | Cost h | Risk mitigated |
|---|-----|----------|-----------|--------|----------------|
| 01 | A.6.B Boundary lanes в templates | P1 | A.6.B | 4-6 | Contract/DPA ambiguity accumulation |
| 02 | UTS F.17 skeleton | P1 | F.17 | 6-10 | Concept drift в 18 agents + hires |
| 03 | D.5 Bias-Audit Cycle | P1 | D.5 | 3-5 | EU AI Act compliance weakness |
| 04 | F + R tags frontmatter | P1 | B.3 | 3-5 | Trust audit trail |
| 05 | A.14 typed mereology edges | P1 | A.14 | 2-4 | Retro-typing cost later |
| 06 | Phase transitions as B.2 MHT | P1 | B.2 | 2-3 | Phase 2a docs ad-hoc risk |
| 07 | Portfolio как C.18 NQD + C.19 E/E | P2 | C.18 + C.19 | 6-10 | Informal direction selection |
| 08 | A.13:4.3 Agency-CHR fallback | P2 | A.13 | 2-3 | 3-tier ambiguity |
| 09 | E.17 Multi-View Publication | P2 | E.17 | 8-15 | Single-view client deliverable |
| 10 | F.9 Bridge + CL edges | P2 | F.9 | 2-3 | Cross-direction reuse risk |
| 11 | A.18 CSLC for 3 high-stakes comparisons | P2 | A.18 | 8-12 | Subjective pricing / kill criteria |
| 12 | E.10 LEX-BUNDLE conceptual prefixes | P2 | E.10 | 3-5 | Namespace drift |
| 13 | D6 FPF split (Core vs Tooling) | P2 | E.5.1 | 4-8 | Tooling-locked FPF |
| 14 | B.4 loop mapping to 4 rituals | P2 | B.4 | 1-2 | Shared vocabulary |
| 15 | F.6 six-step agent onboarding | P2 | F.6 | 3-5 | Onboarding variance |
| 16 | C.22 TaskSignature в discovery | P2 | C.22 | 3-5 | Unsystematic intake |
| 17 | A.16 PreArticulationCuePack inbox | P3 | A.16 | 4-6 | Scale problem (Phase 2+) |
| 18 | F.11 Method Quartet Harmonisation | P3 | F.11 | 5-8 | Methodological clarity |
| 19 | A.6.S Signature Pair для SKU | P3 | A.6.S | 3-5 | SKU version management |
| 20 | E.20 MIP new-pattern protocol | P3 | E.20 | 2-3 | Pattern sprawl |
| 21 | G.5 Multi-Method Dispatcher | P3 | G.5 | 4-6 | Method governance |
| 22 | First FPF-Steward audit Q2 | P3 | Override #11 | 2-4 | Commitment follow-through |

**Totals:**
- P1: 20-33h (6 items)
- P2: 42-71h (10 items)
- P3: 20-32h (6 items)
- **Grand total: 82-136h** across all 22 items.

**Phase 1 realistic commitment:** P1 only (~20-30h) = architecturally
cheapest wins. P2+P3 = Phase 2a/2b adoption over next 6-9 months.

---

## Section 7 — Open Questions для Ruslan Review

Items requiring **judgment-level decision** by Ruslan. Each с options +
Claude recommendation + impact.

### OQ-01: Rename "FPF" (Jetix) to avoid Левенчук-FPF collision?

**Context:** D6 document named "JETIX-FPF.md" references both Jetix-specific
adaptation + Levenchuk canonical framework. Attribution.md requires
crediting Левенчук; "FPF" as our name creates attribution ambiguity
externally.

**Options:**
- A. Keep "FPF" (current) — maximal alignment signal; rely on context.
- B. **"JETIX-FPF"** — explicit derivative marker preserves canonical
  Levenchuk-FPF reference. Low-cost rename.
- C. **"JPF" (Jetix Principles Framework)** — clear distinction but loses
  alignment signal.
- D. Keep "FPF" + add subtitle "Jetix adaptation of Левенчук FPF" — compromise.

**Claude recommendation:** **Option B "JETIX-FPF"**. Preserves Левенчук-FPF
attribution while retaining "FPF" brand. Low effort (global rename D6 →
JETIX-FPF + update references). Supports future attribution clarity если
Jetix publishing decision triggered.

**Impact:** One-line change in document title; minor references update. Zero
architectural impact.

### OQ-02: Adopt P1 recs as committed backlog, or defer к Phase 2a triggers?

**Context:** 6 P1 recs total 20-30h extra Phase 1 work. Current Phase 1
budget ~80-120h Stage 4 writing already committed.

**Options:**
- A. Adopt all 6 P1 immediately (20-30h extra now).
- B. Adopt 3 cheapest-high-leverage P1 (Rec-03 Bias-Audit, Rec-04 F+R tags,
  Rec-05 A.14 typed edges = ~10-14h) + defer other 3 (Rec-01 boundary,
  Rec-02 UTS, Rec-06 MHT = ~10-16h).
- C. Defer all P1 к Phase 2a triggers.
- D. Adopt 3 most architectural (Rec-01 boundary templates, Rec-02 UTS, Rec-05
  typed edges = 12-20h) + defer 3 procedural (Rec-03 bias-audit, Rec-04 F+R
  tags, Rec-06 MHT).

**Claude recommendation:** **Option A (adopt all 6 P1)**. Reasoning:
(1) P1 items are architectural seams — cheaper now than retrofitted.
(2) Ruslan's 11 overrides все в +Левенчук direction — stance consistent.
(3) Total 20-30h is ~15-25% increase on ~120h total Phase 1 budget — not
extreme. (4) Benefit compounds (Rec-02 UTS + Rec-04 F+R tags + Rec-05 typed
edges reinforce each other).

**Impact:** Phase 1 budget expansion к ~140-150h; Day 11+14 parallel track
extended 2-3 days; break-even pushed marginally but first-client revenue
unchanged.

### OQ-03: Direction alpha formalized as C.18 NQD-Archive + C.19 E/E-LOG Front now or Phase 2?

**Context:** Rec-07 P2 proposes formalizing Portfolio через NQD + E/E-LOG.
High conceptual leverage but adds NQD vocabulary to agent context.

**Options:**
- A. Document в D6 FPF Section 6 (8 Alphas) + D5 Knowledge Architecture.
  Phase 1 adoption.
- B. Document в `wiki/foundations/portfolio-directions.md` separate artifact.
  Phase 1 adoption.
- C. Defer к Phase 2a (when 2+ active directions + first archive entry).
  Phase 1 keeps informal.

**Claude recommendation:** **Option B (separate wiki artifact, Phase 1
adoption)**. Reasoning: NQD vocabulary is dense; doesn't belong in role-
manifest system.md (context budget pressure); separate artifact allows
strategy-lead + strategy-support-analyst deep reference без bloating agents.
Phase 1 adoption captures conceptual clarity while pattern is fresh; cheap
now-expensive-later.

**Impact:** +4-6h Phase 1 (wiki artifact writing). Affects Day 11 parallel
track.

### OQ-04: E.17 Multi-View Publication adoption threshold?

**Context:** Rec-09 P2 proposes multi-view publication (engineer / manager /
auditor views) для client deliverables. Cost 8-15h для first 1-2 pilots.
Value accrues если client requests (DPA, audit SKU with multi-stakeholder
consumption).

**Options:**
- A. Mandatory для все Audit SKU deliverables Day 1.
- B. Mandatory only когда client-requested (DPA trigger OR explicit audit SKU
  with "for board" framing).
- C. Defer к Phase 2a trigger (5+ concurrent clients).
- D. Pilot на first Audit SKU delivery; evaluate; generalize if successful.

**Claude recommendation:** **Option D (pilot-then-generalize)**. Reasoning:
Single-view deliverable OK for non-regulated clients Phase 1. First Audit SKU
(likely €2-5K, Q2 target) is learning opportunity. If client positively
responds к multi-view, extend Phase 2a+. If friction > value, park.

**Impact:** +8-12h Phase 2a pilot; no Phase 1 cost.

### OQ-05: Trust & Assurance F-G-R scope — ADRs only or client deliverables too?

**Context:** Rec-04 P1 proposes F + R tags в ADR frontmatter. Should this
extend to client deliverables?

**Options:**
- A. ADRs only Phase 1 (decisions/ folder).
- B. ADRs + client deliverables (proposals / audits / reports).
- C. ADRs + client deliverables + wiki claims (comprehensive).
- D. Don't add formal F + R; rely on informal status: fields already used.

**Claude recommendation:** **Option B (ADRs + client deliverables)**. ADR is
internal reasoning record — essential context for F+R. Client deliverables
are trust-critical external artifacts — also essential. Wiki claims can wait
(huge existing wiki requires retrofit, diminishing returns). Matches effort
estimate 3-5h.

**Impact:** Option B = 3-5h as estimated; Option C = 10-15h; Option A =
1-2h.

### OQ-06: Model D terminology — preserve Russian or Anglicize в D6?

**Context:** Divergence 5 — "Model D Nested Hierarchy" is Russian-rooted
terminology, not in FPF-Spec.

**Options:**
- A. Keep Russian "Model D" как primary; add English expansion "≈ A.1
  Holonic Foundation + A.14 partonomy" parenthetically.
- B. Rename к "Nested Holonic Structure" (English FPF-aligned); retire "Model
  D" or keep as legacy alias.
- C. Use both interchangeably based on audience (Russian contexts: Model D;
  English contexts: Nested Holonic).
- D. Expand "Model D" в D6 FPF explicitly: "В работах Левенчука обозначено как
  'Модель D' (вложенная иерархия систем); в FPF-Spec соответствует A.1 +
  A.14 паттернам".

**Claude recommendation:** **Option D (explicit expansion в D6)**. Preserves
Russian lineage for audience continuity while educating English readers + FPF
cross-references. Cheapest clarity.

**Impact:** ~15 min D6 edit.

### OQ-07: FPF Core / Tooling split в D6 — mandatory or optional split?

**Context:** Rec-13 P2 proposes splitting D6 FPF into Core (abstract, ~20-30
pages) + Tooling Addendum (~10-20 pages) per E.5.1 DevOps Lexical Firewall.

**Options:**
- A. Mandatory split — clean Core, separate Addendum artifact.
- B. Optional separation — D6 includes both sections with clear marking
  ("Part 1: Core", "Part 2: Tooling") in one document.
- C. Don't split — one D6 document с mixed-tooling prose is acceptable для
  internal use.
- D. Soft split — D6 main document = Core-focused; Tooling examples в
  `wiki/foundations/fpf-tooling.md`.

**Claude recommendation:** **Option D (soft split)**. Rationale: D6 FPF main
document stays cognitive-elegance focused (E.2 P-1); tooling references
go к separate wiki artifact. E.5.3 Unidirectional Dependency preserved
(Core → Tooling → Pedagogy not violated). Doesn't add huge writing effort.

**Impact:** D6 writing slightly abstract-er; new `wiki/foundations/fpf-tooling.md`
companion (~3-5h).

### OQ-08: Adopt F.17 UTS now or after D6 FPF first-pass complete?

**Context:** Rec-02 P1 creates Jetix UTS — valuable artifact but competes
with D6 writing for Phase 1 attention.

**Options:**
- A. Write UTS first (6-10h); then D6 FPF uses UTS as reference.
- B. Write D6 FPF first; UTS pilot concurrent with D6 Section 2 (Stakeholders)
  + Section 8 (U-Types Full).
- C. Post-D6 sole task.
- D. Delegate UTS к FPF-Steward sub-role first quarterly output.

**Claude recommendation:** **Option B (concurrent)**. Rationale: UTS rows =
U.Types; D6 Section 8 "U-Types Full" = natural home for initial rows. Writing
together ensures consistency + avoids duplicate effort.

**Impact:** Total effort same (~6-10h UTS + 25-40h FPF); sequencing different.

### OQ-09: Should contribute-back к Левенчук community be formally considered?

**Context:** Section 5 identified 9 Jetix innovations с contribution
potential. Current Publishing decision (OT5): internal-only Phase 1+.

**Options:**
- A. No change — keep internal-only per OT5. Document innovations
  comprehensively для future.
- B. Soft engagement — Ruslan attends Левенчук seminars; informal pattern
  sharing без formal publishing.
- C. Start contributing Phase 2a+ (after first revenue) selectively (P8
  Portfolio-CAL proposal).
- D. Immediate engagement — pilot contribution now (Portfolio-CAL via MIM
  community).

**Claude recommendation:** **Option B soft engagement + docs comprehensively
retained**. Rationale: Maintains OT5 internal-only без sacrificing community
relationships. If Ruslan attends Левенчук семинары, informal pattern
conversations natural. Formal contribution deferred but retained as option.

**Impact:** Zero formal effort; Ruslan's discretion on individual interactions.

### OQ-10: Quarterly FPF-upstream sync trigger — Q1 2027 or on-demand?

**Context:** KB Q15 — quarterly upstream FPF-Spec sync. Левенчук actively
developing (semiotics workstream April 2026, SPF/TPF patterns).

**Options:**
- A. Quarterly automatic — FPF-Steward Q1/Q2/Q3/Q4 audits include upstream
  sync check.
- B. On-demand — trigger sync when Ruslan learns of major Левенчук
  release (blog, seminar, github).
- C. Semi-annual — lower cadence (every 6 months).
- D. Annually — revisit once/year.

**Claude recommendation:** **Option A quarterly (integrated в FPF-Steward
audit)**. Rationale: aligns existing quarterly cadence; prevents drift;
ensures semiotics workstream etc. captured. FPF-Steward already doing
quarterly audit per Override #11.

**Impact:** +30-60 min per quarter added к FPF-Steward audit (check
github.com/ailev/FPF for delta, re-vendor if substantive update).

### OQ-11: Agent promotion mechanism — formal А.18 CSLC or current meta-agent heuristic?

**Context:** D7 Area 7 promotion decision: external review (meta-agent
evidence) + Ruslan sign-off. Rec-11 proposes A.18 CSLC formalism как
auditable alternative.

**Options:**
- A. Keep current mechanism — meta-agent evidence + Ruslan sign-off, informal
  criteria.
- B. Add A.18 CSLC formalism as required when agent promoted к J-Strategic
  (highest tier).
- C. A.18 CSLC for все promotion decisions (J-Auto → J-Approve → J-Strategic).
- D. Hybrid — A.18 CSLC template for reference; meta-agent reports using it
  optionally.

**Claude recommendation:** **Option D (hybrid optional)**. Rationale: A.18
adds formalism but agent promotion в Jetix Phase 1 is rare event (0-2 per
year). Over-formalizing adds process friction. CSLC template для reference
gives meta-agent structure option без mandating.

**Impact:** Minor policy doc update (~1-2h); meta-agent prompt optionally
includes CSLC references.

### 7.12 Open questions summary

| # | OQ | Claude rec | Estimated impact |
|---|-----|-----------|------------------|
| 01 | FPF name collision | Rename к "JETIX-FPF" | Minor find-replace |
| 02 | P1 adoption scope | All 6 P1 | +20-30h Phase 1 |
| 03 | Portfolio as NQD+E/E-LOG | Wiki artifact Phase 1 | +4-6h |
| 04 | E.17 Multi-View threshold | Pilot first Audit SKU | +8-12h Phase 2a |
| 05 | F-G-R scope | ADRs + client deliverables | +3-5h |
| 06 | Model D terminology | Expand в D6 | ~15 min |
| 07 | FPF Core/Tooling split | Soft split + wiki companion | +3-5h |
| 08 | UTS timing | Concurrent с D6 | No net change |
| 09 | Contribute-back | Soft engagement | Zero formal |
| 10 | Upstream sync trigger | Quarterly integrated | +30-60 min/Q |
| 11 | Agent promotion | Hybrid optional CSLC | ~1-2h |

---

## Section 8 — Next Steps

### 8.1 Immediate actions (this week)

1. **Ruslan review** этого gap analysis (~60-90 min reading) — primarily
   Sections 1 (Executive Summary), 6 (Recommendations), 7 (Open Questions).

2. **Ruslan decisions** per:
   - 6 P1 recommendations → accept all / accept subset / defer
   - 11 open questions → decide each
   - Overall alignment score 65/100 validation / adjustment

3. **Format preference for ADR Chunk 8:** should accepted recs be added к
   existing approval ADR (appendix) or as separate ADR "Post-FPF-discovery
   additions"? Suggestion: separate ADR (cleaner, linkable, preserves
   timeline).

### 8.2 Week 2 actions (if recs accepted)

4. **ADR Chunk 8 writing** (~30 min) — Claude writes accepted-recommendations
   ADR based on Ruslan decisions.

5. **D9 draft v0.6 regeneration** (~2-4h) — if substantive changes (e.g.,
   FPF rename OQ-01, new P1 commitments affecting cost model, Override #12
   added) — update D9 draft and status bump.

6. **D6 JETIX-FPF.md writing commences** (Stage 4) — enriched с FPF
   alignment per accepted recs:
   - Adopts Rec-02 UTS concurrent (OQ-08 recommendation)
   - Includes Rec-13 Core/Tooling soft split (OQ-07)
   - Expands Model D (OQ-06)
   - Renames to JETIX-FPF if OQ-01 accepted

### 8.3 Month 2 actions

7. **P2 recs**: Selected P2 adoption as capacity permits. Likely candidates
   для Phase 1 completion: Rec-11 CSLC (aligns с Rec-07 NQD formalization),
   Rec-14 B.4 ritual mapping (quick win), Rec-15 F.6 onboarding (supports
   D3 18-manifest effort).

8. **First FPF-Steward quarterly audit** (Rec-22) — template + run.

### 8.4 Quarterly ongoing

9. **FPF-Steward audits** include:
   - UTS delta (Rec-02)
   - A.14 typed edges audit (Rec-05)
   - F + R tags coverage check (Rec-04)
   - Upstream FPF-Spec sync (OQ-10)
   - Phase transition MHT readiness (Rec-06)
   - Bias-Audit cycle artifact review (Rec-03)

10. **Review gap analysis annually** (2027-04-20 target): what changed, FPF
    upstream evolution, Jetix architecture evolution, revised alignment score.

---

*END OF GAP ANALYSIS*

*Prepared 2026-04-20 by Claude Opus 4.7 (1M context). Inputs: FPF-Spec.md
(62,202 lines, Левенчук March 2026); Jetix ADR approval 2026-04-19 (Stage 3
review, 7 chunks); D9 draft v0.5 (2026-04-20 consolidation); KB unified
reference (2026-04-20). Primary sources triangulated against FPF-Spec
verified line-by-line (all pattern IDs referenced в mapping verified via
Glob/Grep). Alignment score 65/100 based on cluster-weighted pattern coverage
across 11 FPF Parts. 22 recommendations prioritized (6 P1, 10 P2, 6 P3). 11
open questions flagged для Ruslan judgment. Next: Ruslan review + decisions
+ optional ADR Chunk 8 + D6 JETIX-FPF.md writing commences.*
