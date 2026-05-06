---
id: gap-analysis-review-decisions-2026-04-20
title: Gap Analysis Review — Ruslan Decisions Tracker
date-opened: 2026-04-20
status: IN PROGRESS
phase: Stage 3.6 — Post-FPF-Discovery Gap Analysis review
type: decision-tracker
decision-maker: ruslan
scribe: claude-opus-4-7
input: raw/research/fpf-gap-analysis-2026-04-20.md (commit 74cf858)
output-target: ADR Chunk 8 (Post-FPF-Discovery Additions) + D9 draft v0.6
notion: https://www.notion.so/3482496333bf8174a7ffd6f30c02f0bf
status: archived
archived_at: 2026-05-06
archived_reason: Stage-3 chunk tracker — historical decision journal
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via CANONICAL-WALKTHROUGH-2026-05-06.md)
---

# Gap Analysis Review — Decisions Tracker

Живой ADR отслеживающий Ruslan decisions по 22 recommendations + 11 open
questions + 9 innovations из `fpf-gap-analysis-2026-04-20.md`.

В конце этого файл becomes input для Claude Code — он соберёт **ADR Chunk 8**
(Post-FPF-Discovery Additions) + обновит **D9 draft v0.6**.

---

## 🎯 Quality commitment

Максимальная глубина + качество, на 100%. Отталкиваемся от:
- FPF-Spec.md (62K строк первоисточник Левенчука)
- Вся философия 5 primitives + 16 trans-disciplines
- Все patterns, instruments, guard-rails
- Никаких compromises — everything applicable adopted

Previous 11 Ruslan overrides — все в +Левенчук direction. Здесь same course.

---

## 📍 Current position

- **Step:** [TBD — будет updated как идём]
- **Decisions made:** [TBD — count]
- **Pending:** 22 recs + 11 OQ + 9 innovations

---

## Step 1 — Orientation (Executive Summary + Overall alignment) ✅ COMPLETE 2026-04-20

**Ruslan meta-directive (overall stance for Steps 2-7):**
> "Я хочу всё что там ещё не дотягивается улучшить. Максимально глубоко.
> Все критические gaps — качественно разбирать по одному."

### Alignment score: 65/100

- [x] ✅ ACCEPTED — validation checkpoint passed

### Top 5 strongest alignments

1. Role ≠ Executor/Holder split (P2 + 18 role-manifests)
2. Past-participle state machine discipline
3. Holonic 3-level mereological creation graph
4. Constitution pillars alignment (DRR as ADR, 4 Guard-Rails partial)
5. [fifth — check gap analysis]

- [x] ✅ ACCEPTED — top 5 alignments characterization confirmed

### Top 5 critical gaps

1. Boundary Unpacking cluster (A.6.*) — ~15%
2. Trust & Assurance Calculus (B.3 F-G-R) — ~30%
3. Characteristic Space (A.17-A.21) — ~5%
4. Unified Term Sheet (F.17 UTS) — ~25%
5. Multi-View Publication (E.17) — ~20%

- [x] ✅ ACCEPTED — top 5 critical gaps confirmed, **all to be improved maximum depth**

**Ruslan's overall judgment on Executive Summary:**

> ✅ ACCEPTED bottom line framing (core ontology strong, middle-tier gaps,
> adopt all). Stance: **"всё что не дотягивается — улучшить"**. Идём
> качественно по одному через Steps 2-7 и adopt maximum of applicable.

---

## Step 2 — 5 Critical Gaps deep dive

### Gap 1 — Boundary Unpacking (A.6.*) ✅ APPROVED

- [x] Discussed 2026-04-20
- **Decision:** ✅ **ACCEPT full (Option A)** — адоптируем A.6.B Boundary Norm Square L/A/D/E routing во всех 3 templates (contract + DPA + proposal) Phase 1.
- **Plus:** A.6.C Contract Unpacking, A.6.0 U.Signature, A.6.P Relational Precision, A.6.Q Quality Term, A.6.H Wholeness — adopted deeply во всех applicable places.
- **Cost:** 4-6h Phase 1 + ~5 min per new clause ongoing.
- **Rationale:** Ruslan directive — "подтверждаем полностью, внедряем глубоко, качественно". DACH enterprise compliance signal; audit-readiness; reusable L sections между contracts.
- **Ties to:** Rec-01 P1 (это тот же scope).
- **Implementation:** Day 5 (proposal template), Day 6 (contract + DPA template) — full L/A/D/E structure. Plus `decisions/policy/boundary-discipline.md` explaining routing convention.

### Gap 2 — Trust & Assurance Calculus (B.3 F-G-R) ✅ APPROVED

- [x] Discussed 2026-04-20
- **Decision:** ✅ **ACCEPT full + deep adoption (Option A)** — F-G-R tags в ADRs + client deliverables + agent output Phase 1.
- **Plus deep:** Evidence Types catalog, CL (Congruence Level), Bridges, Pathwise Justification, Weakest-link analysis — adopted где applicable.
- **Scope:** ADRs + client deliverables + agent outputs (sales-research, audit-reports, strategic analyses).
- **Cost:** 3-5h Phase 1 (policy doc + retrofit 10-15 existing ADRs + template updates) + ~1 min per new ADR/deliverable ongoing.
- **Rationale:** Ruslan directive — "подтверждаем полностью + deep adoption". Art. 22 GDPR defence strengthened; AI-agent output discipline; audit trail quality.
- **Ties to:** Rec-04 P1 (same scope).
- **Implementation:**
  - `decisions/policy/trust-tagging.md` — policy document для F/G/R conventions
  - F-scale F0-F9 defined + Jetix examples (expected range F0-F3)
  - ClaimScope naming convention (bounded context paths)
  - R-levels: R-low / R-medium / R-high / R-certified / R-formally-proven
  - Retrofit existing ADRs with F-G-R tags
  - Meta-agent prompt update: enforce F-G-R tagging
  - FPF-Steward quarterly audit scope includes F-G-R compliance check

### Gap 3 — Characteristic Space (A.17-A.21) ✅ APPROVED

- [x] Discussed 2026-04-20
- **Decision:** ✅ **ACCEPT full + deep adoption (Option A)** — все 5 patterns (A.17 CHR-NORM, A.18 CSLC, A.19 CharacteristicSpace + mechanisms, A.20 Dynamics, A.21 MM-CHR) adopted Phase 1.
- **Scope: 3 concrete applications Phase 1:**
  1. SKU pricing CHR space — `decisions/policy/sku-pricing-chr.yaml` (3-5h)
  2. Direction kill criteria CHR — template в `directions/_templates/kill-chr-template.yaml` + applied к existing directions (3-5h)
  3. Agent promotion CHR — `decisions/policy/agent-promotion-chr.yaml` (2-5h)
- **Plus:** `decisions/policy/characteristic-space-conventions.md` — общие conventions для Jetix CSLC usage.
- **Plus deep:** NQD-CAL (C.18), E/E-LOG (C.19), MM-CHR (A.21), Pareto dominance — adopted где applicable.
- **Cost:** 8-15h Phase 1 + 30-60 min per new SKU/direction/promotion ongoing.
- **Rationale:** Ruslan directive — "максимально подтверждаю". Измеримые decisions > subjective; defensible pricing; objective agent promotion; consistent comparison framework.
- **Ties to:** Rec-11 P2 (elevated to P1-equivalent per Ruslan stance), OQ-11 (agent promotion CSLC).
- **Elevation note:** Rec-11 was P2 в gap analysis; Ruslan max-depth stance elevates effective priority to P1.

### Gap 4 — Unified Term Sheet (F.17 UTS) ✅ APPROVED

- [x] Discussed 2026-04-20
- **Decision:** ✅ **ACCEPT full + deep adoption (Option A)** — F.17 UTS + E.10 LEX-BUNDLE + SenseCells + Bridges adopted Phase 1.
- **Plus deep:** Layout A (Kernel-first, 30-50 core rows × 6-8 context columns); 4-register LEX-BUNDLE per row (tech/plain/legacy/mnemonic); explicit Bridges between contexts; Rationale per row.
- **Cost:** 6-10h Phase 1 setup + ~2h per quarter FPF-Steward audit.
- **Rationale:** Ruslan directive — "полное и глубокое внедрение". Critical для 18 agents + future hires + clients; prevents ontological drift; onboarding hire-friendly.
- **Ties to:** Rec-02 P1, OQ-08 (timing).
- **Implementation:**
  - `wiki/foundations/jetix-uts.md` — central UTS table
  - Layout A (Kernel-first), 30-50 core rows
  - Context columns: FPF U.Type / Jetix tech / Jetix plain / ШСМ-Russian / Essence-legacy / DACH-legal / AI-industry / Bridges / Rationale
  - LEX-BUNDLE 4-register naming per row
  - SenseCells per non-trivial cell
  - Bridges explicit equivalence mappings
- **Timing:** **Concurrent с D6 FPF writing** (OQ-08 Variant B) — UTS rows = U.Types = D6 Section 8 ontology. Ensures consistency.
- **Maintenance:** FPF-Steward quarterly audit includes UTS review scope.

### Gap 5 — Multi-View Publication (E.17) ✅ APPROVED

- [x] Discussed 2026-04-20
- **Decision:** ✅ **ACCEPT full + deep adoption (Option A — modified)** — Viewpoint Bundle defined Phase 1 + **mandatory multi-view для all Audit SKU deliveries from first delivery onward** (ne pilot-only).
- **Plus:** E.18 TGA simpler form — A.6.3.CR (Same-Entity Retextualization) для safe cross-view translation.
- **Plus:** ISO/IEC/IEEE 42010 alignment noted (professionalism signal).
- **Jetix Viewpoint Bundle (5 viewpoints Phase 1):**
  - Executive (CEO, Aufsichtsrat; 2-3 pages; plain + finance)
  - Technical (CTO, engineers; 20-40 pages; technical + specs)
  - Governance (board, risk committee; 3-7 pages; governance + legal)
  - Regulatory (BfDI, EU AI Act auditors; 3-5 pages; regulatory + legal)
  - Internal-learning (Jetix team; 5-10 pages; internal + FPF)
- **Cost:** 3-5h setup (Viewpoint Bundle + canonical template + first view templates) + 8-12h first pilot + marginal ongoing after templates mature.
- **Rationale:** Ruslan directive — "подтверждаю все глубоко, максимально фиксируем". Mittelstand deal acceleration; audit-readiness; scale-prep для Phase 2a+.
- **Ties to:** Rec-09 P2 (elevated via max-depth stance), OQ-04 (pilot threshold — override to mandatory).
- **Implementation:**
  - `decisions/templates/jetix-viewpoint-bundle.yaml` — Viewpoint definitions
  - `decisions/templates/audit-canonical-template.md` — underlying artifact structure
  - `decisions/templates/views/` — 5 view templates
  - Correspondences table — canonical section → view section mapping
  - Update protocol: canonical changes → views regenerated
  - First pilot: Müller GmbH audit (or first actual Audit SKU client)

---

## ✅ Step 2 COMPLETE 2026-04-20 — All 5 Critical Gaps APPROVED Full Depth

All 5 critical gaps adopted **maximum depth**, no compromises:
- Gap 1 Boundary Discipline (A.6.*) — full L/A/D/E + A.6.C/0/P/Q/H cluster
- Gap 2 Trust & Assurance (B.3 F-G-R) — ADRs + client deliverables + agent output
- Gap 3 Characteristic Space (A.17-21) — SKU pricing + direction kill + agent promotion CHR
- Gap 4 UTS (F.17) — 30-50 rows table + LEX-BUNDLE + SenseCells + Bridges
- Gap 5 Multi-View (E.17) — Viewpoint Bundle + mandatory multi-view all Audit SKUs

**Total Gap 1-5 work estimate:** ~30-45h Phase 1 + ongoing discipline.

**Promoted to P1-equivalent:** Rec-09 (Multi-View), Rec-11 (CHR Space) — были P2, elevated via max-depth stance.

---

## Step 3 — 6 P1 Critical Recommendations

### Rec-01 — Boundary Norm Square lanes в contract/DPA templates

- **FPF basis:** A.6.B + A.6.C
- **Cost:** 4-6h
- **Claude rec:** accept (P1)
- [ ] Discussed
- **Ruslan decision:** [TBD — accept / modify / defer / reject]
- **Rationale:** [TBD]
- **Modifications (if any):** [TBD]

### Rec-02 — UTS skeleton для Jetix concepts

- **FPF basis:** F.17 Unified Term Sheet
- **Cost:** 6-10h
- **Claude rec:** accept (P1)
- [ ] Discussed
- **Ruslan decision:** [TBD]
- **Rationale:** [TBD]

### Rec-03 — D.5 Bias-Audit Cycle для EU AI Act compliance ✅ APPROVED

- **FPF basis:** D.5 Bias-Audit & Ethical Assurance
- **Cost:** 3-5h setup + 1h per deliverable + 2h quarterly
- [x] Discussed 2026-04-20
- **Ruslan decision:** ✅ **ACCEPT full + deep adoption (Option A)**
- **Rationale:** "подтверждаю полностью, внедряем глубоко". EU AI Act compliance + Art. 22 GDPR defense + enterprise client readiness.
- **Implementation:**
  - `decisions/policy/bias-audit-cycle.md` — policy + 4-stage cycle (BA-0/BA-1/BA-2/BA-3)
  - Templates: BA-0 kickoff / BA-1 scan / BA-3 closure
  - `bias-register.yaml` schema per deliverable
  - Per-deliverable structure: `clients/<client>/audits/<audit>/bias-audit/`
  - Quarterly aggregation: `decisions/bias-audit/YYYY-QN-bias-audit.md`
  - Bias Taxonomy (REP / ALG / VIS / MET / LNG) structured
  - Phase 1 simplified: BA-0 + BA-1 + BA-3 (solo Ruslan, no BA-2 Panel Review until Phase 2a Beirat Ethics advisor)
  - Integration с `decisions/policy/eu-ai-act.md` (OT3 approved) + FPF-Steward quarterly audit scope (R12 approved)

### Rec-04 — F (Formality) + R (Reliability) tags в ADR/deliverable frontmatter

- **FPF basis:** B.3 Trust & Assurance Calculus
- **Cost:** 3-5h
- **Claude rec:** accept (P1)
- [ ] Discussed
- **Ruslan decision:** [TBD]
- **Rationale:** [TBD]

### Rec-05 — A.14 typed mereology edges (ComponentOf / PortionOf / PhaseOf) ✅ APPROVED

- **FPF basis:** A.14 Advanced Mereology + A.6.H Wholeness
- **Cost:** 2-4h Phase 1 + 5 min per new edge ongoing
- [x] Discussed 2026-04-20
- **Ruslan decision:** ✅ **ACCEPT full + deep adoption (Option A)**
- **Rationale:** "полностью подтверждаю, внедряем глубоко". Cheap finishing touch для MC3 full-depth mereological graph. Reasoning accuracy; semantic clarity; FPF-Steward auditability.
- **Implementation:**
  - `wiki/foundations/jetix-creation-graph.md` — retag existing 5 generic edges с A.14 typed edges
  - `decisions/policy/mereology-edge-types.md` — documentation 10 edge types:
    - A.14 core 6: ComponentOf / ConstituentOf / PortionOf / PhaseOf / MemberOf / AspectOf
    - Jetix-introduced 4: creates / operates-in / methodologically-uses / constrained-by / fills
    - When-to-use-which guide + anti-patterns
  - A.6.H Wholeness patterns applied где relevant
  - FPF-Steward quarterly audit scope includes edge type verification
- **Ties to:** MC3 (already accepted full 3-level graph), Gap 3 (CHR foundations relate).

### Rec-06 — B.2 MHT для Jetix phase transitions ✅ APPROVED

- **FPF basis:** B.2 Meta-Holon Transition + B.2.1 Emergence + B.2.2 Re-identification + B.2.5 Supervisor-Subholon Feedback
- **Cost:** 2-4h Phase 1 + 2h per transition when happens
- [x] Discussed 2026-04-20
- **Ruslan decision:** ✅ **ACCEPT full (Option A)** — 4 MHTs documented + template + integrations Phase 1
- **Rationale:** "подтверждаем полностью, внедряем глубоко". Systematic transition management; invariant preservation; audit-readiness; bridge к scale.
- **Implementation:**
  - `decisions/policy/phase-transitions-mht.md` — 4 MHTs documented:
    - Phase 1 → 2a (solo + hire)
    - Phase 2a → 2b (team 5-20)
    - Phase 2b → 2c (€10-50M, multi-entity, first acquisition)
    - Phase 2c → 3 (€50M+, multi-entity federation)
  - Each MHT: from-holon / to-holon / trigger-conditions / emergence-signals / re-identification (invariants + mutables) / transition-process (pre/during/post) / supervisor-subholon-feedback
  - `decisions/templates/mht-template.yaml` — reusable template
  - Integration: D8 rollout + D7 career levels + Area 4 Life-OS separation
- **Ties to:** Area 4 Triple-AND Phase 2a trigger (already approved), D7 phase transitions table, Item 6 folder structure evolution.

---

## ✅ Step 3 COMPLETE 2026-04-20 — All 6 P1 Recommendations APPROVED Full Depth

- Rec-01 Boundary Norm Square → ✅ via Gap 1
- Rec-02 UTS skeleton → ✅ via Gap 4
- Rec-03 D.5 Bias-Audit Cycle → ✅ Full
- Rec-04 F+R tags ADR → ✅ via Gap 2
- Rec-05 A.14 typed mereology edges → ✅ Full
- Rec-06 B.2 MHT phase transitions → ✅ Full

**Plus P2 elevated к P1-equivalent:**
- Rec-09 E.17 Multi-View → ✅ via Gap 5
- Rec-11 A.18 CSLC → ✅ via Gap 3
- Rec-12 E.10 LEX-BUNDLE → ✅ via Gap 4 UTS

---

## Step 4 — 10 P2 Valuable Recommendations ✅ ALL APPROVED 2026-04-20

**Ruslan directive:** "All full + Deep Adoption. Подтверждаю."

### Rec-07 — Portfolio через C.18 NQD-CAL + C.19 E/E-LOG ✅ APPROVED
- **Decision:** ACCEPT full (3-5h). C.18 NQD distinctions + C.19 Exploration/Exploitation log per direction. Strengthens Portfolio model.
- **Implementation:** per-direction `ee-log.yaml` + `nqd-distinctions` sections.

### Rec-08 — A.13:4.3 Agency-CHR fallback ✅ APPROVED
- **Decision:** ACCEPT full (1-2h). Agency-CHR adds formal agency-scale 0.0-1.0 dimension к 3-tier J-Auto/Approve/Strategic.
- **Implementation:** `executor-binding.yaml` gets `agency-profile` section + fallback rule.

### Rec-09 — E.17 Multi-View Publication ✅ APPROVED via Gap 5 (elevated)

### Rec-10 — F.9 Bridge + CL convention ✅ APPROVED
- **Decision:** ACCEPT full (2-3h). Bridges между contexts + Congruence Level measurement для semantic drift.
- **Implementation:** convention applied в cross-direction wiki + UTS bridge section.

### Rec-11 — A.18 CSLC Characteristic Space ✅ APPROVED via Gap 3 (elevated)

### Rec-12 — E.10 LEX-BUNDLE ✅ APPROVED via Gap 4 UTS (via LEX-BUNDLE 4-register naming)

### Rec-13 — E.5.1 DevOps Lexical Firewall (D6 Core/Tooling split) ✅ APPROVED
- **Decision:** ACCEPT full (Option C OQ-07 soft split, 3-5h). D6 JETIX-FPF Core-focused (20-30 pages); `wiki/foundations/fpf-tooling.md` companion (10-20 pages).
- **E.5.3 Unidirectional Dependency** preserved (Core → Tooling, not reverse).

### Rec-14 — B.4 Canonical Evolution Loop в 4 rituals ✅ APPROVED
- **Decision:** ACCEPT full (1-2h). Observe/Reflect/Decide/Act mapped к daily/weekly/monthly/quarterly.
- **Implementation:** D8 4-rituals section updated с explicit evolution loop framing.

### Rec-15 — F.6 Role Assignment cycle (agent onboarding) ✅ APPROVED
- **Decision:** ACCEPT full (1-2h). Extends already-accepted `agent_onboarding` (Левенчук Part 3 #2) с full cycle + retrospective step + template.

### Rec-16 — C.22 Problem-CHR TaskSignature ✅ APPROVED
- **Decision:** ACCEPT full (2-3h). Structured client problem intake: Problem-CHR coordinate + TaskSignature (inputs/outputs/constraints/acceptance-criteria).
- **Implementation:** template в `decisions/templates/client-intake-problem-chr.yaml`; applied per client engagement.

**Total P2 new work: ~13-22h Phase 1.**

---

## Step 5 — 6 P3 Nice-to-have Recommendations ✅ ALL APPROVED 2026-04-20

**Ruslan directive:** "all подтверждаю, deep adoption".

### Rec-17 — A.16 PreArticulationCuePack (voice-notes pipeline) ✅ APPROVED
- **Decision:** ACCEPT full (1-2h). Template `inbox/cues/<slug>.md` с maturity layer pre-articulation → claim → hypothesis → direction progression.

### Rec-18 — F.11 Method Quartet Harmonisation ✅ APPROVED
- **Decision:** ACCEPT full (1-2h). Monthly check per direction: method-design / method-work / method-plan / method-evidence alignment. Ties с Rec-14 B.4 Evolution Loop.

### Rec-19 — A.6.S Signature Engineering Pair (SKU evolution) ✅ APPROVED
- **Decision:** ACCEPT full (1-2h). Versioned SKU signatures (v1 active для old clients + v2 для new).

### Rec-20 — E.20 Mechanism Introduction Protocol ✅ APPROVED
- **Decision:** ACCEPT full (1h). Protocol doc для introducing new mechanisms — trial period, success criteria, rollback plan.

### Rec-21 — G.5 Multi-Method Dispatcher ✅ APPROVED
- **Decision:** ACCEPT full (2-3h). MethodFamily Registry + dispatcher rules для multi-method decisions.

### Rec-22 — First quarterly FPF-Steward audit Q2 2026 ✅ APPROVED
- **Decision:** ACCEPT full (2-4h Q2 close). First `decisions/fpf-stewardship/2026-Q2-ontology-audit.md` validates Phase 1 FPF adoptions.

**Total P3 new work: ~8-14h Phase 1.**

---

## Step 6 — 11 Open Questions (Ruslan judgment)

### OQ-01 — Rename "FPF" → "JETIX-FPF"? ✅ RESOLVED

- **Claude rec:** B (rename)
- [x] Discussed 2026-04-20
- **Ruslan choice:** ✅ **B — JETIX-FPF** ("переименуем в Jetix FPF, чтобы ничего не запуталось")
- **Implementation:**
  - D6 rename: `design/JETIX-FPF-LITE.md` → `design/JETIX-FPF.md` (already planned; now finalized naming)
  - Cross-references везде updated
  - Attribution explicit: "JETIX-FPF — Jetix-specific adaptation of First Principles Framework (FPF) by Anatoly Levenchuk"

### OQ-02 — P1 adoption scope? ✅ RESOLVED via Steps 2-3

- **Ruslan choice:** All 6 P1 accepted + 3 P2 elevated (Gap 3/5 → Rec-09/11/12) — effectively MORE than Claude rec A.

### OQ-03 — Portfolio as NQD+E/E-LOG timing? ✅ RESOLVED via Rec-07

- **Ruslan choice:** Phase 1 adoption (wiki artifact) — consistent с Step 4.

### OQ-04 — E.17 Multi-View threshold? ✅ RESOLVED via Gap 5

- **Ruslan choice:** Modified Option A — **Mandatory от first delivery onward** (stronger than Claude pilot rec).

### OQ-05 — F-G-R scope (ADRs only vs + client deliverables)? ✅ RESOLVED via Gap 2

- **Ruslan choice:** ADRs + client deliverables + agent outputs — full scope (more than Claude rec B).

### OQ-06 — Model D terminology (Russian vs Anglicize)? ✅ RESOLVED

- **Claude rec:** D (explicit expansion в D6)
- [x] Discussed 2026-04-20
- **Ruslan choice:** ✅ **B — Anglicize полностью, use FPF canonical terminology** ("похуй на историю, делай по FPF как правильно")
- **Implementation:**
  - "Model D Nested Hierarchy" → retire as primary term; replaced by **"Nested Holonic Structure"** (FPF A.1 + A.14 canonical)
  - Всё документы updated: ADR, D6 JETIX-FPF, D1, D2, D4, D5 refer к "Nested Holonic Structure" primary
  - "Model D" может appear как legacy alias only (footnote where historically referenced)
  - D6 introduces concept using FPF canonical: "Jetix uses Nested Holonic Structure (A.1 Holonic Foundation + A.14 Advanced Mereology)"

### OQ-07 — D6 FPF Core/Tooling split? ✅ RESOLVED via Rec-13

- **Ruslan choice:** Option C soft split — `design/JETIX-FPF.md` (Core, 20-30 pages) + `wiki/foundations/fpf-tooling.md` companion (10-20 pages).

### OQ-08 — UTS timing? ✅ RESOLVED via Gap 4

- **Ruslan choice:** Concurrent с D6 writing (Option B).

### OQ-09 — Contribute-back к Левенчук community? ✅ RESOLVED

- **Claude rec:** B (soft engagement)
- [x] Discussed 2026-04-20
- **Ruslan choice:** ✅ **A — No contribution (hard stance)** ("всё держим, ничего никуда не отправляем, нигде не публикуем")
- **Implementation:**
  - All 9 Jetix innovations remain **internal-only**
  - **No formal pull-requests, proposals, или public sharing** с Левенчук community
  - Ruslan может attend курсы Левенчука sam для own learning — no obligation to share
  - Full secret sauce preservation
  - Review trigger: **none Phase 1-2** (consistent с OT5 internal-only). Phase 3+ — только если publishing decision explicit revisited
- **Consistency с OT5:** strengthens internal-only stance (no soft engagement even)

### OQ-10 — Upstream FPF sync trigger (quarterly vs on-demand)? ✅ RESOLVED

- **Claude rec:** A (quarterly auto)
- [x] Discussed 2026-04-20
- **Ruslan choice:** ✅ **Modified Option C — Semi-annual reminder, Ruslan triggers decision manually** ("не автоматом, будут напоминания, semi-annual, держим под контролем")
- **Implementation:**
  - Every 6 months (Q2 close + Q4 close) — FPF-Steward audit **flags** "upstream FPF sync review due"
  - Reminder only — **не автоматический** fetch/apply
  - Ruslan decides когда actually sync (может быть same quarter, может be defer)
  - Sync involves: check github.com/ailev/FPF main branch для delta since last vendor; if substantive update → re-vendor FPF-Spec.md + Readme.md; update ATTRIBUTION.md version; propagate changes в Jetix adaptation as needed
  - Not every reminder becomes actual sync (trigger-based selective)

### OQ-11 — Agent promotion (current vs A.18 CSLC formal)? ✅ RESOLVED via Gap 3

- **Ruslan choice:** A.18 CSLC adopted full (Gap 3) — formalism мandatory для agent promotion (stronger than Claude hybrid rec).

---

## ✅ Step 6 COMPLETE 2026-04-20 — All 11 Open Questions RESOLVED

| OQ | Topic | Decision |
|----|-------|----------|
| OQ-01 | FPF rename | ✅ B — JETIX-FPF |
| OQ-02 | P1 adoption scope | ✅ All 6 P1 + 3 P2 elevated |
| OQ-03 | Portfolio NQD+E/E-LOG timing | ✅ Phase 1 (wiki artifact) |
| OQ-04 | E.17 Multi-View threshold | ✅ Mandatory от first delivery |
| OQ-05 | F-G-R scope | ✅ ADRs + client deliverables + agent outputs |
| OQ-06 | Model D terminology | ✅ B — Anglicize (Nested Holonic Structure) |
| OQ-07 | D6 Core/Tooling split | ✅ Soft split + wiki companion |
| OQ-08 | UTS timing | ✅ Concurrent с D6 |
| OQ-09 | Contribute-back | ✅ A — No contribution (hard stance) |
| OQ-10 | Upstream FPF sync | ✅ Semi-annual reminder (Ruslan manual trigger) |
| OQ-11 | Agent promotion CSLC | ✅ A.18 CSLC full (mandatory) |

---

## Step 7 — 9 Innovations confirmation ✅ COMPLETE 2026-04-20

### All 9 confirmed internal-only (per OQ-09 A)

1. ✅ **Portfolio of Directions** (P8 + 8-я alpha) — Strategic, Phase 1 implemented
2. ✅ **4-tier Resource Accounting** (Capital+Compute+Deep Hours+Attention+Ecosystem) — Operational
3. ✅ **18-manifest AI-native architecture** — Organizational, Day 9 implementation
4. ✅ **FPF-Steward sub-role** (meta-agent) — Methodological, via R12
5. ✅ **Physical Life-OS ≠ Jetix separation** — Architectural, Day 8
6. ✅ **DACH + US + RU unified funnel** — Market, P6 adopted
7. ✅ **7+7 day rollout** (sales-first) — Operational
8. ✅ **Company-as-Code + Git = SoT** — Foundational, P1 core
9. ✅ **Full-FPF-Permeation pattern** — Methodological, OT5 adopted

### Contribute-back: NO (per OQ-09 A)

- **Никакого sharing, publishing, proposals к ailev/FPF community**
- All innovations remain Jetix internal secret sauce
- No review trigger Phase 1-2
- Phase 3+ — только если OT5 publishing decision **explicitly revisited** (unlikely per current stance)

### Documentation strategy Phase 1

- **Single internal reference:** `wiki/foundations/jetix-innovations.md` — живой document listing all 9 + rationale + current implementation status
- **Preservation, not publishing** — innovations retained с context для own methodology evolution
- Reference-only (не active sharing)

---

## Step 8 — Consolidation summary

**To be filled когда Steps 1-7 complete.**

### Total P1 accepted: [TBD]
### Total P2 accepted: [TBD]
### Total P3 accepted: [TBD]
### Total extra Phase 1 work: [TBD hours]
### Changes к timeline: [TBD]
### Changes к Jetix architecture: [TBD list]

---

## Step 9 — Claude Code task

**After Steps 1-8 complete — write task-prompt для Claude Code:**

- Input: этот tracking file (all decisions) + existing ADR + D9 draft + gap analysis
- Output: ADR Chunk 8 written + D9 draft v0.6 regenerated
- После завершения — D6 FPF writing unblocked

**Task-prompt path:** `prompts/adr-chunk-8-writing-2026-04-20.md`

---

## Ruslan directives (overall)

> Максимальная глубина + качество, на 100%. Никаких compromises. Всё что
> применимо из FPF — внедряем. Стратегический курс как с 11 overrides —
> +Левенчук direction.

(Добавляется в ADR Chunk 8 как опорный принцип.)
