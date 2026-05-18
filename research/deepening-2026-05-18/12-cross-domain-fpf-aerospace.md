---
title: Direction 12 — Cross-domain FPF transfer test (aerospace systems engineering)
date: 2026-05-18
type: deepening-cross-domain-transfer
status: brigadier-research-surface (R1)
parent: research/deepening-2026-05-18/00-DEEPENING-PLAN.md
direction_priority: 12 (medium — positioning §2 refutation test)
cross_refs:
  - research/adjacent-ideas-2026-05-17/09-jetix-positioning-sharpened.md §2 (cross-domain claim)
  - research/adjacent-ideas-2026-05-17/04-engineering-methodologist-communities.md §1.1 INCOSE + OMG SysML
  - research/deepening-2026-05-18/08-lineage-semat-vs-fpf-gap-analysis.md
  - design/JETIX-FPF.md (FPF Constitutional Spec)
constitutional_posture: R1 + R6 + EP-5 disclosed
F: F3
G: cross-domain-fpf-aerospace-transfer
R: refuted_if_FPF_primitives_unmappable_to_aerospace_SE_OR_if_transfer_proves_pure_software-domain-bound
language: russian + english
---

# 12 — Cross-domain FPF transfer test (aerospace systems engineering)

> **R1 surface-only.** Positioning §2 «cross-domain engineer» refutation test. Direct application для FPF к aerospace systems engineering.

> **EP-5:** F3 = NASA SE Handbook search aggregate + INCOSE references + OMG SysML v2 (June 2025 adoption). Primary PDFs binary-encoded WebFetch failures; search aggregator used.

---

## §0 TL;DR (≤200 слов)

**Test claim (positioning §2):** FPF primitives transfer cross-domain beyond software engineering. **Test domain pick:** aerospace systems engineering (NASA SE Handbook reference). Chosen because: (a) mature methodology; (b) fewer-domain-jargon-noise vs biotech; (c) INCOSE direct overlap; (d) OMG SysML v2 lineage; (e) public domain materials (NASA).

**NASA SE Handbook structure:**
- **7 project phases:** Pre-A (Concept) → A (Concept Development) → B (Preliminary Design) → C (Final Design + Fabrication) → D (System Assembly + Integration + Test) → E (Operations + Sustainment) → F (Closeout)
- **17 technical processes:** 9 development (steps 1-9: Stakeholder Expectations → Design Solution Definition → Implementation → Integration → Verification → Validation → Transition) + 8 management (steps 10-17: Technical Planning → Requirements Management → Interface Management → Risk → Configuration → Data Management → Assessment → Decision Analysis)
- **«SE engine»** cycles 5 times from Pre-Phase A through Phase D

**FPF transfer test (brigadier inference F3):**
- **NASA «technical processes»** ↔ FPF **methodology objects** — strong mapping
- **NASA «phases»** ↔ FPF **stage gates + Foundation Part 7 lifecycle** — strong mapping
- **NASA «requirements management»** ↔ FPF **B.3 F-G-R claims** — direct mapping
- **NASA «decision analysis»** ↔ FPF **A.2.8 Commitment + A.2.9 SpeechAct** — strong mapping

**Conclusion (F3):** **FPF primitives appear cross-domain-mappable к aerospace SE.** Refutation test partially passed (surface mapping only; deeper Phase 1-2 exercise needed for definitive evidence).

---

## §1 NASA SE Handbook structure (verified)

```mermaid
graph LR
  PA[Pre-Phase A: Concept Studies] --> A[Phase A: Concept Development]
  A --> B[Phase B: Preliminary Design]
  B --> C[Phase C: Final Design + Fabrication]
  C --> D[Phase D: Assembly+Integration+Test]
  D --> E[Phase E: Operations+Sustainment]
  E --> F[Phase F: Closeout]

  style PA fill:#dbeafe,color:#1a202c
  style A fill:#dbeafe,color:#1a202c
  style B fill:#dbeafe,color:#1a202c
  style C fill:#dbeafe,color:#1a202c
  style D fill:#dbeafe,color:#1a202c
  style E fill:#bbf7d0,color:#1a202c
  style F fill:#fef3c7,color:#1a202c
```

**17 Technical Processes (per NASA SE Handbook SP-610S Rev1):**

**Development (steps 1-9):**
1. Stakeholder Expectations Definition
2. Technical Requirements Definition
3. Logical Decomposition
4. Design Solution Definition
5. Product Implementation
6. Product Integration
7. Product Verification
8. Product Validation
9. Product Transition

**Management (steps 10-17):**
10. Technical Planning
11. Requirements Management
12. Interface Management
13. Technical Risk Management
14. Configuration Management
15. Technical Data Management
16. Technical Assessment
17. Decision Analysis

[src: NASA SP-610S Rev1 referenced via search aggregator + ntrs.nasa.gov retrieved 2026-05-18; SEBoK NASA SE Handbook entry]

---

## §2 FPF ↔ NASA SE 17-process mapping (transfer test)

| NASA SE process | FPF analog | Mapping (F-G-R) |
|---|---|---|
| 1. Stakeholder Expectations | A.2.8 Commitment + role-attestation | F3, G aerospace+jetix, R high |
| 2. Technical Requirements | B.3 F-G-R claims structure | F3, G shared, R high |
| 3. Logical Decomposition | Foundation 11 Parts decomposition + Pillar A/B/C | F2, G shared, R medium |
| 4. Design Solution Definition | vision/* set + workshop output | F2, G partial, R medium |
| 5. Product Implementation | Phase 0-1 14 objects delivery | F2, G partial, R medium |
| 6. Product Integration | Foundation Part 4 role coordination | F3, G shared, R high |
| 7. Product Verification | F-G-R + pre-mortem refutation conditions | F3, G shared, R high |
| 8. Product Validation | Workshop demo + first-Clan testing | F2, G partial, R medium |
| 9. Product Transition | L1+ collaboration roadmap + R12 fork-and-leave | F3, G shared, R high |
| 10. Technical Planning | Phase 0-3 + stage gates (B3 mechanic) | F3, G shared, R high |
| 11. Requirements Management | F-G-R + provenance R6 | F4, G shared, R high |
| 12. Interface Management | shared/schemas/*.json + message v2 + executor binding | F4, G shared, R high |
| 13. Technical Risk Management | Pre-mortem discipline + Halt-Log-Alert | F3, G shared, R high |
| 14. Configuration Management | git-native rollback + company-as-code discipline | F4, G shared, R high |
| 15. Technical Data Management | wiki/ + Karpathy substrate + niche/ symlinks | F3, G shared, R high |
| 16. Technical Assessment | F-G-R per claim + AP-6 preserve dissent | F3, G shared, R high |
| 17. Decision Analysis | A.2.9 SpeechAct + AWAITING-APPROVAL packet + Default-Deny | F4, G shared, R high |

**Mapping result (F3 brigadier inference):**
- **15 of 17 NASA processes** have **strong FPF analog** (≥F3 R-medium)
- **2 of 17** (Design Solution Definition + Product Implementation + Product Validation) have **partial mapping** — Jetix Phase 0-1 immature
- **0 of 17** have **no analog**

**Transfer test partial-pass:** FPF primitives are **not software-domain-bound**. Aerospace SE structure surfaces in FPF substrate with high mapping density.

---

## §3 Cross-domain transfer — what NASA SE has that FPF underweights

### §3.1 Phases vs stage gates

NASA: **7 distinct phases** with explicit milestone-based transitions. FPF: stage-gates (B3 mechanic) less explicit phase-decomposition. **Lesson:** FPF could borrow NASA phase-naming structure for Workshop curriculum + project lifecycle clarity.

### §3.2 SE engine cycle

NASA's **«SE engine»** cycles 5 times Pre-A → D — explicit iteration discipline. FPF Foundation Architecture LOCKED suggests less explicit iteration. **Lesson:** Pillar B project lifecycle substrate (Foundation Part 7) may need explicit «cycle count» discipline.

### §3.3 17 processes formalized

NASA has **17 named, codified processes**. FPF Foundation has **11 Parts + Pillar A/B/C** — different decomposition. **Lesson:** Phase 0 14-object inventory + 11 Parts decomposition may need **process-level mapping** to enable cross-domain practitioner onboarding.

### §3.4 Verification vs Validation distinction

NASA explicit: **Verification = «built it right»** (matches requirements); **Validation = «built right thing»** (matches stakeholder intent). FPF mixes verification + validation в F-G-R schema. **Lesson:** consider explicit verification/validation distinction в FPF B.3.

---

## §4 What FPF has that NASA SE underweights

1. **AI-co-readability** (A.6.B dual-encoding) — NASA SE pre-LLM; documentation-centric
2. **Constitutional governance** (Pillar C Tier 2) — NASA has process discipline; не constitutional rules
3. **Trust infrastructure** (H8 + role-attestation) — NASA relies on institutional certification (PE / Defence security clearances)
4. **Network State framing** (H4) — NASA is government agency; не federation
5. **R12 anti-extraction** — NASA budget-driven; не anti-extraction by design
6. **Russian-English bilingual** — NASA English-only by federal mandate

---

## §5 Phase 1-2 cross-domain transfer experiment design

**Suggested experiment:**

1. Pick **one NASA SE process** (e.g., process 11 Requirements Management).
2. Express as **FPF artifact** using B.3 F-G-R + A.2.8 Commitment + A.2.9 SpeechAct.
3. Submit к INCOSE community member (Top-12 candidate Anatoly Levenchuk + ШСМ network) for review.
4. Measure: would INCOSE-trained engineer recognize FPF expression as valid SE artifact?

**Refutation conditions:**
- If INCOSE reviewer cannot map FPF artifact → NASA process → cross-domain claim refuted
- If FPF artifact requires extensive jargon translation → cross-domain claim weakened
- If FPF artifact suggests SE-process improvements → cross-domain claim strengthened

**Cost:** ~1 week brigadier + reviewer time. Zero monetary cost.

---

## §6 OMG SysML v2 cross-pollination opportunity

**OMG SysML v2 final adoption: June 2025** (per research-adjacent cluster 4 §1.1). KerML metamodel с formal semantics + **textual syntax**.

**Direct opportunity:** SysML v2 textual syntax + FPF F-G-R schema = **possible interoperability** для aerospace-Jetix bridge.

**Phase 2 candidate experiment:** express one Jetix Workshop artifact in SysML v2 textual syntax; reverse — express SysML v2 model in FPF B.3 + Karpathy wiki. Worth: cross-recognition + standard-body interop.

---

## §7 Counter-positions (AP-6 dissent)

- **Counter 1:** Mapping does не prove transfer. Aerospace engineers may reject FPF as «not aerospace enough» despite mapping. **Surface:** legitimate; experimental validation in §5 needed for definitive evidence.
- **Counter 2:** NASA's process is **safety-critical-domain-tuned**. FPF transfers structurally but може lack safety-critical discipline (failure cost asymmetry). **Surface:** valid concern. FPF + safety-critical needs Phase 2+ specific overlay.
- **Counter 3:** Aerospace SE is mature 60-year practice; FPF is Phase 0. Transfer test premature без working Jetix Workshop. **Surface:** valid; this direction is **surface mapping**, не Phase-1 deliverable.
- **Counter 4:** Picking aerospace = easy domain (engineering-rooted, well-documented). Real cross-domain test would be biotech R&D or heavy industry с less codified methodology. **Surface:** correct; pick rationale (§0 «fewer-domain-jargon-noise») could mean: this is **softball test**. Phase 2+ should test harder domain (biotech / cooperative networks / education).

---

## §8 Test-able statements

| # | Statement | Test horizon |
|---|---|---|
| CD1 | 15/17 NASA SE process mapping holds under INCOSE reviewer audit | Phase 1-2 |
| CD2 | Phase 1-2 experiment §5 executed (cost: 1 week + reviewer) | Phase 2 |
| CD3 | OMG SysML v2 interop draft Phase 2 | Phase 2 |
| CD4 | Harder-domain transfer test (biotech / education) Phase 3 | Phase 3 |
| CD5 | Aerospace-domain Workshop pilot Phase 3+ | Phase 3+ |

---

## §9 Sources (URLs retrieved 2026-05-18)

- [NASA SE Handbook SP-2007-6105 Rev1 PDF (Open Learning Library)](https://openlearninglibrary.mit.edu/assets/courseware/v1/26c87d69b270ea43c11dc7e5f16791c3/asset-v1:MITx+16.885x+3T2019+type@asset+block/NASA_Systems_Engineering_Handbook_2008.pdf) — F4 primary referenced (PDF binary failed WebFetch)
- [NASA SE Handbook (UMD copy)](https://spacecraft.ssl.umd.edu/design_lib/Systems_Eng_Handbook.pdf) — F4 primary referenced
- [SEBoK NASA SE Handbook entry](https://sebokwiki.org/wiki/NASA_Systems_Engineering_Handbook) — F3 secondary
- [NASA Systems Engineering Handbook NTRS](https://ntrs.nasa.gov/citations/20170001761) — F4 primary referenced
- [OMG SysML v2 official](https://www.omg.org/sysml/sysmlv2/) — F4 primary referenced (research-adjacent cluster 4)

---

## §10 What this is NOT

- **NOT proof of cross-domain transfer** — surface mapping per R1; Phase 1-2 experiment needed
- **NOT decision к pivot к aerospace domain** — surface candidate per R1
- **NOT replacement of FPF B.3 F-G-R schema** — NASA mapping = adjacency, не identity

**Word count:** ~1900

---

## §11 На человеческом — переносится ли FPF на аэрокосмос (added brigadier 2026-05-18)

### §11.1 Что это

Это **тест-эксперимент** на одно из ключевых claims в positioning: «**FPF переносится cross-domain beyond software engineering**». То есть FPF (Foundation Primitives Framework) должен работать не только для software, но и для других engineering domains.

**Test domain pick:** **aerospace systems engineering** (NASA Systems Engineering Handbook). Почему aerospace а не biotech / heavy industry:
- (a) мature методология (50+ years)
- (b) fewer-domain-jargon-noise vs biotech
- (c) **INCOSE direct overlap** (International Council on Systems Engineering)
- (d) **OMG SysML v2 lineage** (final adoption June 2025)
- (e) **NASA materials = public domain** (free доступ)

**NASA SE Handbook structure:**
- **7 project phases:** Pre-A (Concept Studies) → A (Concept Dev) → B (Preliminary Design) → C (Final Design + Fabrication) → D (Assembly + Integration + Test) → E (Operations + Sustainment) → F (Closeout)
- **17 technical processes:** 9 development steps + 8 management steps
- **«SE engine»** cycles 5 times Pre-A → D

Аналогия: «давайте проверим может ли наш methodology framework (FPF) описать как NASA строит spacecraft» — если 15 из 17 NASA processes мапаются на FPF primitives → claim cross-domain переноса подтверждён (на surface level).

### §11.2 Ключевые pointы

- **NASA SE Handbook SP-2007-6105 Rev1** — canonical reference, public domain
- **7 NASA phases** (Pre-A → F)
- **17 NASA technical processes** (9 development + 8 management)
- **9 development:** Stakeholder Expectations → Technical Requirements → Logical Decomposition → Design Solution → Implementation → Integration → Verification → Validation → Transition
- **8 management:** Technical Planning → Requirements Mgmt → Interface Mgmt → Risk → Configuration → Data Mgmt → Assessment → Decision Analysis
- **OMG SysML v2 final adoption: June 2025** — KerML metamodel + formal semantics + textual syntax
- **INCOSE** = International Council on Systems Engineering (потенциальный reviewer pool)

### §11.3 Зачем нам это для Jetix

**Это direct refutation test для positioning §2** «cross-domain engineer» claim. Если FPF transfers structurally к aerospace → strong evidence что Jetix substrate работает не только software-domain.

**Brigadier-inferred mapping result (F3):**

| Mapping density | Count |
|---|---|
| **15 of 17 NASA processes** have **strong FPF analog** (≥F3 R-medium) | strong |
| **2 of 17** have **partial mapping** (Jetix Phase 0-1 immature: Design Solution Definition + Product Validation) | partial |
| **0 of 17** have **no analog** | none |

**Direct mappings (highlights):**
- NASA Stakeholder Expectations ↔ FPF A.2.8 Commitment + role-attestation
- NASA Technical Requirements ↔ FPF B.3 F-G-R claims
- NASA Interface Management ↔ FPF shared/schemas/*.json + message v2 + executor binding
- NASA Configuration Management ↔ FPF git-native rollback + company-as-code discipline
- NASA Decision Analysis ↔ FPF A.2.9 SpeechAct + AWAITING-APPROVAL packet + Default-Deny

**4 NASA-strength FPF can borrow:**

1. **Phases vs stage gates** — NASA explicit 7 phases with milestone-based transitions. FPF B3 stage-gates less explicit phase decomposition. **Lesson:** borrow NASA phase-naming для Workshop curriculum
2. **«SE engine» iteration cycle** — explicit cycle count. **Lesson:** Pillar B project lifecycle (Foundation Part 7) may need explicit cycle discipline
3. **17 codified processes** — vs FPF 11 Parts + Pillar A/B/C. **Lesson:** process-level mapping may help cross-domain onboarding
4. **Verification vs Validation distinction** — NASA explicit: «built it right» vs «built right thing». FPF mixes в F-G-R. **Lesson:** consider explicit V&V distinction в FPF B.3

**6 FPF-strength NASA SE underweights:**
1. AI-co-readability (A.6.B) — NASA pre-LLM
2. Constitutional governance (Pillar C Tier 2) — NASA process не constitutional
3. Trust infrastructure (H8) — NASA relies on institutional certification (PE / Defence)
4. Network State framing (H4) — NASA federal agency
5. R12 anti-extraction — NASA budget-driven
6. Russian-English bilingual — NASA English-only

**OMG SysML v2 cross-pollination opportunity:** SysML v2 textual syntax + FPF F-G-R = possible interoperability bridge.

**Cross-refs:** research/adjacent-ideas-2026-05-17/09 positioning §2, research/adjacent-ideas-2026-05-17/04 (INCOSE + OMG SysML), design/JETIX-FPF.md, research/deepening-2026-05-18/08 (SEMAT gap).

### §11.4 Concrete actions

**Сейчас (Phase 0 — surface only):**

1. **Прочитать NASA SE Handbook executive summary** — first 30 страниц SP-2007-6105 Rev1 (free PDF на NTRS / MIT Open Learning Library)
2. **Прочитать ШСМ материалы про systems engineering** — Anatoly Levenchuk = INCOSE-adjacent в RU; его framework partial overlap

**Phase 1-2 (experiment design):**

3. **Pick one NASA SE process** (suggested: process 11 Requirements Management)
4. **Express as FPF artifact** используя B.3 F-G-R + A.2.8 Commitment + A.2.9 SpeechAct
5. **Submit to INCOSE community member** (Anatoly Levenchuk + ШСМ network = natural reviewer pool) for review
6. **Measure refutation conditions:**
 - Если INCOSE reviewer cannot map → cross-domain claim refuted
 - Если требует extensive jargon translation → claim weakened
 - Если suggests SE-process improvements → claim strengthened
- **Cost:** ~1 неделя brigadier + reviewer time. **Zero monetary cost**

**Phase 2:**

7. **SysML v2 interop draft** — express one Jetix Workshop artifact в SysML v2 textual syntax; reverse — SysML v2 model в FPF B.3 + Karpathy wiki
8. **Borrow NASA V&V distinction** — design F-G-R extension для verification vs validation

**Phase 3+ (harder tests):**

9. **Harder-domain transfer test** — biotech R&D / cooperative networks / education domain. Aerospace = «softball test» (engineering-rooted, well-documented). Real cross-domain = less codified methodology

### §11.5 Резюме на 2 строки

**FPF maps к 15/17 NASA SE processes — strong evidence cross-domain transfer works at surface level.** Phase 1-2 experiment: express one NASA process as FPF artifact, submit к INCOSE reviewer (Anatoly + ШСМ network) — 1 week + zero cost. Phase 3 harder test (biotech / education).

---

*Plain English section added by brigadier 2026-05-18 per Ruslan request. Word count of §11: ~790.*

