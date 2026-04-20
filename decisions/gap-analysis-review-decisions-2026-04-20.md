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

### Rec-06 — B.2 MHT для Jetix phase transitions

- **FPF basis:** B.2 Meta-Holon Transition
- **Cost:** 2-4h
- **Claude rec:** accept (P1)
- [ ] Discussed
- **Ruslan decision:** [TBD]
- **Rationale:** [TBD]

---

## Step 4 — 10 P2 Valuable Recommendations

### Rec-07 — Portfolio через C.18 NQD-CAL + C.19 E/E-LOG

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-08 — A.13:4.3 Agency-CHR fallback

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-09 — E.17 Multi-View Publication Kit (client deliverables)

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-10 — F.9 Bridge + CL convention (cross-direction wiki)

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-11 — A.18 CSLC Characteristic Space (SKU pricing, direction kill criteria)

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-12 — E.10 LEX-BUNDLE naming convention

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-13 — E.5.1 DevOps Lexical Firewall (Core/Tooling split в D6)

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-14 — B.4 Canonical Evolution Loop в 4 rituals

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-15 — F.6 Role Assignment cycle (agent onboarding)

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-16 — C.22 Problem-CHR TaskSignature (client intake)

- [ ] Discussed
- **Ruslan decision:** [TBD]

---

## Step 5 — 6 P3 Nice-to-have Recommendations

### Rec-17 — A.16 PreArticulationCuePack (voice-notes pipeline)

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-18 — F.11 Method Quartet Harmonisation

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-19 — A.6.S Signature Engineering Pair (SKU evolution)

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-20 — E.20 Mechanism Introduction Protocol

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-21 — G.5 Multi-Method Dispatcher

- [ ] Discussed
- **Ruslan decision:** [TBD]

### Rec-22 — First quarterly FPF-Steward audit Q2 2026

- [ ] Discussed
- **Ruslan decision:** [TBD]

---

## Step 6 — 11 Open Questions (Ruslan judgment)

### OQ-01 — Rename "FPF" → "JETIX-FPF"?

- **Claude rec:** B (rename)
- [ ] Discussed
- **Ruslan choice:** [TBD — A/B/C/D или custom]
- **Rationale:** [TBD]

### OQ-02 — P1 adoption scope?

- **Claude rec:** A (all 6 P1)
- [ ] Discussed
- **Ruslan choice:** [TBD]

### OQ-03 — Portfolio as NQD+E/E-LOG timing?

- **Claude rec:** B (wiki artifact Phase 1)
- [ ] Discussed
- **Ruslan choice:** [TBD]

### OQ-04 — E.17 Multi-View threshold?

- **Claude rec:** D (pilot first Audit SKU)
- [ ] Discussed
- **Ruslan choice:** [TBD]

### OQ-05 — F-G-R scope (ADRs only vs + client deliverables)?

- **Claude rec:** B (ADRs + client deliverables)
- [ ] Discussed
- **Ruslan choice:** [TBD]

### OQ-06 — Model D terminology (Russian vs Anglicize)?

- **Claude rec:** D (explicit expansion в D6)
- [ ] Discussed
- **Ruslan choice:** [TBD]

### OQ-07 — D6 FPF Core/Tooling split?

- **Claude rec:** D (soft split + wiki companion)
- [ ] Discussed
- **Ruslan choice:** [TBD]

### OQ-08 — UTS timing (before D6 / concurrent / after)?

- **Claude rec:** B (concurrent)
- [ ] Discussed
- **Ruslan choice:** [TBD]

### OQ-09 — Contribute-back к Левенчук community?

- **Claude rec:** B (soft engagement)
- [ ] Discussed
- **Ruslan choice:** [TBD]

### OQ-10 — Upstream FPF sync trigger (quarterly vs on-demand)?

- **Claude rec:** A (quarterly integrated в FPF-Steward)
- [ ] Discussed
- **Ruslan choice:** [TBD]

### OQ-11 — Agent promotion (current vs A.18 CSLC formal)?

- **Claude rec:** D (hybrid optional)
- [ ] Discussed
- **Ruslan choice:** [TBD]

---

## Step 7 — 9 Innovations confirmation + contribute-back

### Innovations list

1. Portfolio of Directions (P8 + 8-я alpha) — high contribution potential
2. 4-tier resource accounting — high potential
3. 18-manifest AI-native architecture — medium
4. FPF-Steward sub-role — medium
5. Physical Life-OS ≠ Jetix separation — medium
6. DACH + US + RU unified funnel — low-medium
7. 7+7 day rollout — low
8. Company-as-Code + Git = SoT — high
9. Full-FPF-Permeation pattern — low-medium

- [ ] All 9 confirmed
- **Contribute-back timeline:** [TBD — likely tied to OT5 publishing trigger]
- **Documentation strategy Phase 1:** [TBD]

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
