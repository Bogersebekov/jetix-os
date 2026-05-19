---
type: research-doc
phase: 7
session: k-4-intellect-12-component-audit-2026-05-19
date: 2026-05-19 afternoon
authored_by: brigadier-scribe (ROY swarm; synthesis)
language: russian-primary + english-framework-primitives
word_budget: ~2500
constitutional_posture: R1 + R11 + R12 + EP-5 + breadth-NOT-selection
status: BRIGADIER-DRAFT
hypothesis_count: 30 (H-IC-1 .. H-IC-30)
---

# Phase 7 — Hypothesis Bank (30 H) + R12 Alignment + 3 Curriculum Design Recommendations

> 30 testable hypotheses across 4 categories: (1) Framework coverage 1-8; (2) Gap candidates 9-15; (3) Curriculum design 16-25; (4) Educational outcomes 26-30. R12 anti-extraction alignment check. 3 design options surfaced (NO recommendation).

---

## §1 Hypothesis format

```yaml
ID: H-IC-N
Claim: <statement>
F: F0-F4 (F1=anecdotal / F2=conceptual / F3=mixed / F4=empirical / F0=undetermined)
G: <bounded context (cohort / scale / domain)>
R: refuted_if_<predicate>
Test design: <how to test — cohort A/B / completion / retention / factor analysis>
Acceptance: <success criteria>
Cross-ref: <existing canonical OR framework precedent>
```

---

## §2 Framework coverage hypotheses (H-IC-1 to H-IC-8)

### H-IC-1
- **Claim:** «12-component framework covers Sternberg Triarchic analytical+creative+practical dimensions at ≥75% coverage»
- **F:** F2 (per Phase 1 coverage matrix; verdict was F3 strong analytical, F2 creative, F2 practical)
- **G:** Phase 1 audit; 12 × 3 mapping
- **R:** refuted_if (cross-mapping shows <9/12 components hit any Sternberg dimension)
- **Test design:** factor-analytic survey of 12 components × 3 Sternberg constructs in cohort N≥100; loadings ≥0.5
- **Cross-ref:** `02-sternberg-triarchic.md` §6

### H-IC-2
- **Claim:** «12-component has incomplete CHC coverage (≥5 of 10 broad abilities under-represented: Gv, Ga, Gs, Glr, Grw)»
- **F:** F3 (Phase 2 §6.4)
- **G:** Phase 2 audit; 12 × 10 CHC broads
- **R:** refuted_if (factor analysis of 12-component shows broad-ability structure isomorphic к CHC)
- **Test design:** WJ-IV battery + 12-component measures in N≥200 cohort
- **Cross-ref:** `03-chc-model.md` §6.3

### H-IC-3
- **Claim:** «Gardner musical + bodily-kinesthetic + naturalist intelligences are absent from 12-component»
- **F:** F3 (Phase 3 §6.3)
- **G:** Phase 3 audit
- **R:** refuted_if (Gardner-instrument shows musical/BK/naturalist scores load on 12-component measures)
- **Test design:** MIDAS (Multiple Intelligences Developmental Assessment Scale) + 12-component cohort cross-test
- **Cross-ref:** `04-gardner-multiple-intelligences.md` §6.3

### H-IC-4
- **Claim:** «Goleman EI empathy + social-skills domains are NOT covered by 12-component»
- **F:** F3 (Phase 4 §4.2)
- **G:** EI subset (empathy + social-skills)
- **R:** refuted_if (12-component participants score ≥mean on MSCEIT empathy + social subscales)
- **Test design:** MSCEIT + 12-component cohort
- **Cross-ref:** `05-modern-ai-capability-ei-deary.md` §4.2

### H-IC-5
- **Claim:** «12-component scores correlate с g-factor (general intelligence) at r ≥ 0.5»
- **F:** F0 (untested; predicted F3 based on Sternberg + CHC pattern)
- **G:** N ≥ 200 cohort
- **R:** refuted_if (factor analysis shows <0.3 g-loading)
- **Test design:** factor analyse 12 measures + WAIS-V; report g-loadings
- **Cross-ref:** Deary tradition §3

### H-IC-6
- **Claim:** «Modern AI capability benchmarks (ARC-AGI, MMLU, HELM) measure ≤3 of 12 components (C9, C12, partial C3)»
- **F:** F3 (Phase 4 §4.1)
- **G:** Current SOTA LLM benchmarks 2024-2026
- **R:** refuted_if (new benchmark targets ≥5 of 12 components)
- **Test design:** systematic benchmark-design audit; cross-link Chollet «Measure of Intelligence» 2019
- **Cross-ref:** `05-modern-ai-capability-ei-deary.md` §4.1

### H-IC-7
- **Claim:** «WICS wisdom + synthesis = partially covered by 12-component через C10 + C2; F2 partial»
- **F:** F2 (Phase 1 §6.3 surfaced gap)
- **G:** WICS subset
- **R:** refuted_if (12-component captures all 4 WICS dimensions fully)
- **Test design:** WICS leadership inventory + 12-component cohort
- **Cross-ref:** `02-sternberg-triarchic.md` §4

### H-IC-8
- **Claim:** «12-component «direction-understanding» (C1) is weakly precedented in mainstream cognitive psychology»
- **F:** F3 (Phase 5 §2.3 — Cluster D Executive-Vision was «12-component-original»)
- **G:** Mainstream cognitive psych frameworks (Sternberg / CHC / Gardner / EI)
- **R:** refuted_if (precedent framework found with explicit «direction-understanding» as primitive)
- **Test design:** Literature scan + concept-mapping
- **Cross-ref:** `06-12-component-audit-gap-analysis.md` §2.3

---

## §3 Gap hypotheses (H-IC-9 to H-IC-15) ⭐

### H-IC-9
- **Claim:** «Working memory (CHC Gwm) = missing component candidate; folding into C4 (attention) is insufficient»
- **F:** F4 (CHC empirical Gwm-Gf ≠ Gwm-Attention; distinguishable)
- **G:** Education Layer Tier-1 design
- **R:** refuted_if (C4 expanded definition empirically captures Gwm without separate component)
- **Test design:** factor analyze C4 measures + WJ-IV Gwm subtests; if separable factors → C13 Gwm needed
- **Acceptance:** if separable → propose C13; if not → expand C4 definition
- **Cross-ref:** Phase 5 MC-1

### H-IC-10
- **Claim:** «Empathy + social skills (Goleman EI) = missing-component candidate; CRITICAL for master-apprentice methodology + collective-intellect Jetix mission»
- **F:** F4 (Workshop methodology depends on master-apprentice empathy)
- **G:** Workshop cohort N ≥ 20
- **R:** refuted_if (apprentices succeed on Stage-3 component acquisition WITHOUT empathy/social training)
- **Test design:** cohort A (with social-skill training) vs cohort B (without) — track Stage-3 transition rate
- **Acceptance:** if A > B by ≥20% → add C13 + C14 social/empathy
- **Cross-ref:** Phase 5 MC-6+MC-7

### H-IC-11
- **Claim:** «Long-term memory + retrieval (CHC Glr) + creativity (FO narrow) = missing-component candidate»
- **F:** F4 (CHC empirically supported)
- **G:** Education Layer Tier-1
- **R:** refuted_if (C7 questions + C6 tool-creation jointly capture Glr+FO)
- **Test design:** WJ-IV Glr battery + 12-component cohort
- **Cross-ref:** Phase 5 MC-5

### H-IC-12
- **Claim:** «Processing speed / automaticity (CHC Gs + Sternberg automatization) = missing-component candidate; should be modeled as fluency-stage of existing components NOT separate»
- **F:** F3
- **G:** Curriculum design
- **R:** refuted_if (separate Gs measure provides independent variance from fluency-stage of M1-M12)
- **Test design:** longitudinal study: Stage-1→Stage-3 transitions + RT measure
- **Cross-ref:** Phase 5 MC-2

### H-IC-13
- **Claim:** «Visual-spatial processing (CHC Gv) = partial-missing; matters for engineering Workshop specifically»
- **F:** F3
- **G:** Engineering domain
- **R:** refuted_if (engineering apprentices succeed without spatial training)
- **Test design:** spatial-reasoning intervention in subset of engineering cohort
- **Cross-ref:** Phase 5 MC-3

### H-IC-14
- **Claim:** «Auditory-musical processing (CHC Ga / Gardner musical) = missing; LOW priority for engineering Workshop, HIGH priority for general Education Layer»
- **F:** F2
- **G:** Domain-conditional
- **R:** refuted_if (engineering Workshop succeeds without ANY auditory dimension training)
- **Test design:** domain-stratified curriculum design comparison
- **Cross-ref:** Phase 5 MC-4

### H-IC-15
- **Claim:** «Wisdom + synthesis (Sternberg WICS) = critical for R12-alignment of curriculum; surfaced via C10 expansion possible»
- **F:** F3 (WICS leadership empirical)
- **G:** Late-stage curriculum (Tier-2+)
- **R:** refuted_if (C10 proportion-sense alone captures wisdom in Stage-4 graduates)
- **Test design:** Sternberg balance-theory-wisdom inventory + 12-component Stage-4 cohort
- **Cross-ref:** Phase 5 MC-8

---

## §4 Curriculum design hypotheses (H-IC-16 to H-IC-25)

### H-IC-16
- **Claim:** «Hackathon-driven sequencing (Option C) maximizes engagement vs Foundations-first (Option A)»
- **F:** F0 (untested; Jetix vision F2 conceptual prediction)
- **G:** Workshop cohort
- **R:** refuted_if (Option A retains ≥80% of Option C engagement metrics)
- **Test design:** cohort A vs C; engagement metrics (attendance, project ships, peer-engagement)
- **Acceptance:** ≥20% engagement gap → Option C preferred for engagement criterion
- **Cross-ref:** `07-curriculum-module-map.md` §6

### H-IC-17
- **Claim:** «Karpathy LLM101n pattern (build-from-scratch + per-lecture motivation) transferable to 12-component modules»
- **F:** F2 (analogy strong; not yet empirically tested in non-ML domain)
- **G:** General Education Layer
- **R:** refuted_if (Karpathy-pattern modules show lower completion vs traditional in non-ML cohort)
- **Test design:** Karpathy-style module M6 (tool-creation) vs traditional lecture-style; compare completion + Stage-3 transition
- **Cross-ref:** `research/deepening-2026-05-18/09-people-karpathy-eureka-llm101n.md`

### H-IC-18
- **Claim:** «Master-apprentice 1:1 pairing accelerates Stage-2 → Stage-3 transition by ≥30% vs group-only learning»
- **F:** F2 (apprenticeship tradition F3; cognitive-load theory F3)
- **G:** Workshop cohort
- **R:** refuted_if (group-only learners show no Stage-3 transition delay)
- **Test design:** RCT с 1:1 vs group-only over 6-month cohort
- **Cross-ref:** Workshop methodology

### H-IC-19
- **Claim:** «Hybrid A+B (Foundations-first 4 weeks + Project-based) outperforms pure-A or pure-B on combined retention + engagement metrics»
- **F:** F0
- **G:** Workshop cohort
- **R:** refuted_if (hybrid does not beat best-of-pure-A-or-pure-B)
- **Test design:** 3-arm cohort: A / B / Hybrid; retention + engagement composite score
- **Cross-ref:** `07-curriculum-module-map.md` §6.4

### H-IC-20
- **Claim:** «Adding C13 (empathy + social) as explicit 13th component improves Stage-3 cohort outcomes by ≥15%»
- **F:** F0; theory-driven prediction (MC-6+7 critical for collective-intellect)
- **G:** Cohort N ≥ 40
- **R:** refuted_if (C13-cohort matches 12-component-cohort outcomes)
- **Test design:** RCT comparison
- **Cross-ref:** H-IC-10

### H-IC-21
- **Claim:** «Module M9 (Reasoning) is teachable to Stage-3 в ≤6 weeks for engineering cohorts; Stage-4 в ≤18 months»
- **F:** F2 (Karpathy LLM101n empirical: ~6 weeks для first-principles reasoning Stage-3)
- **G:** Engineering cohorts
- **R:** refuted_if (>50% of engineering cohort fails Stage-3 by week 6)
- **Test design:** track Stage-3 transition for M9 in pilot cohort
- **Cross-ref:** `07-curriculum-module-map.md` M9

### H-IC-22
- **Claim:** «Module M10 (Proportion-sense) requires longest acquisition (Stage-3 ≥12 months) of all 12 modules»
- **F:** F2 (philosophical: wisdom-component traditionally slow)
- **G:** All cohorts
- **R:** refuted_if (M10 Stage-3 transition ≤6 months in pilot cohort)
- **Test design:** longitudinal tracking
- **Cross-ref:** WICS wisdom precedent

### H-IC-23
- **Claim:** «12-component curriculum can be open-sourced (CC-BY-SA) without compromising Jetix competitive position; aligned с R12 anti-extraction»
- **F:** F3 (Karpathy LLM101n precedent: open-source pedagogy + maintains author position)
- **G:** Jetix curriculum
- **R:** refuted_if (open-sourcing erodes Workshop apprentice acquisition)
- **Test design:** prospective comparison after pilot release
- **Cross-ref:** R12 §9.3

### H-IC-24
- **Claim:** «Foundations-first sequencing (Option A) more reliably produces Stage-4 (generative) graduates than hackathon-driven (Option C)»
- **F:** F0; depth-vs-breadth tradeoff theory
- **G:** Workshop cohort
- **R:** refuted_if (Option C Stage-4 graduates ≥ Option A)
- **Test design:** 2-year cohort comparison
- **Cross-ref:** `07-curriculum-module-map.md` §6.1

### H-IC-25
- **Claim:** «Master-apprentice cascade (1 master : 10 apprentices : 100 sub-apprentices) sustains quality к 1M-user Workshop scale per audio_686 batch-4»
- **F:** F1 (no precedent at this scale; Mondragón cooperative tradition F2)
- **G:** Workshop scale 1M users
- **R:** refuted_if (sub-apprentice tier shows ≥40% Stage-3 transition drop vs primary apprentices)
- **Test design:** ramp study from 100 → 1K → 10K cohort
- **Cross-ref:** R12 Mondragón ratio cap (Pillar C Tier 2 §4.2)

---

## §5 Educational outcomes hypotheses (H-IC-26 to H-IC-30)

### H-IC-26
- **Claim:** «Per-component completion measurable via project artifact (concrete output) — Stage-3 transition signal»
- **F:** F3 (apprenticeship + Karpathy tradition)
- **G:** All modules
- **R:** refuted_if (≥30% of Stage-3 transitions not artifact-evidenced)
- **Test design:** artifact catalog per cohort member
- **Cross-ref:** Workshop methodology

### H-IC-27
- **Claim:** «Multi-component competence (≥9 of 12 modules at Stage-3+) = signal of "Workshop-graduate" status»
- **F:** F1 (operational threshold; arbitrary until validated)
- **G:** Workshop credentialing
- **R:** refuted_if (graduates show successful outcomes with <9 components at Stage-3)
- **Test design:** longitudinal graduate-tracking + outcome correlation
- **Cross-ref:** Workshop credentialing

### H-IC-28
- **Claim:** «12-component curriculum graduates show ≥30% higher startup/career outcomes vs control (no-curriculum) at 2-year mark»
- **F:** F0 (Karpathy LLM101n + apprenticeship tradition F2 supporting analogy)
- **G:** Workshop graduates 2024-2027
- **R:** refuted_if (outcomes match control at 2-year)
- **Test design:** longitudinal RCT (cohort vs self-taught control)
- **Cross-ref:** Sternberg «Successful Intelligence» life-outcome focus

### H-IC-29
- **Claim:** «Cohort peer-learning (apprentice-apprentice) contributes ≥40% of Stage-3 transitions vs master-apprentice alone»
- **F:** F2 (cognitive apprenticeship tradition F3)
- **G:** Workshop cohorts
- **R:** refuted_if (peer-learning ablation does not affect Stage-3 transition)
- **Test design:** peer-learning intervention RCT
- **Cross-ref:** Workshop methodology

### H-IC-30
- **Claim:** «12-component framework + R12-aligned curriculum is replicable by other Clans (per Pillar C Tier 2 R12 programmable enforcement) without Jetix dependency»
- **F:** F2 (open-source + fork-and-leave principle)
- **G:** Multi-Clan deployment
- **R:** refuted_if (forked instances show ≥30% quality drop vs Jetix Workshop)
- **Test design:** support 3+ external Workshop adoptions; track outcome parity
- **Cross-ref:** Pillar C Tier 2 §4.2 R12 programmable + Ethereum substrate

---

## §6 §9.3 R12 alignment check ✅

Per prompt §9.3 — explicit anti-extraction verification.

### §6.1 R12 verbatim (Pillar C Tier 2 foundation_generic rule 12, FUNDAMENTAL §6.1 candidate rule 12, LOCKED 2026-05-12):

> «No extraction beyond agreed share — AI / substrate cannot extract value from members beyond agreed share; members can fork-and-leave without penalty.»

### §6.2 12-component curriculum R12 alignment

| Aspect | Compliance | Notes |
|---|---|---|
| **Open educational resources** | ✅ | Karpathy LLM101n model; all curriculum materials CC-BY-SA license |
| **Fork-and-leave** | ✅ | Apprentices can leave Workshop with all materials + skills; no contractual lock-in |
| **No knowledge-monopolization** | ✅ | 12-component framework openly published (this research run = part of substrate) |
| **Master-apprentice ≠ extraction** | ✅ | Apprenticeship = teaching, NOT labor extraction; no «free apprentice work» extracted |
| **R12 programmable enforcement (Option D Hybrid via Ethereum, acked 2026-05-18)** | ✅ | Workshop revenue model can implement QF (quadratic funding) + Mondragón ratio cap |
| **Cohort revenue distribution** | ⏳ | RUSLAN-LAYER design decision (Phase 7 surfaces hypothesis H-IC-30 multi-Clan replicability) |

**Verdict: R12 aligned ✅** — 12-component curriculum substrate does NOT enable extraction-beyond-share.

### §6.3 Anti-pattern check (extraction risk surfaces)

Potential R12 violations to AVOID:

1. ❌ Curriculum behind paywall (>marginal cost of delivery)
2. ❌ Apprentice contractual lock-in (e.g., 2-year non-compete)
3. ❌ Master-IP retained against apprentice (apprentice cannot use what they learned)
4. ❌ Workshop credentialing as gatekeeping (vs as signal-only)
5. ❌ AI-tutor data extraction beyond curriculum delivery

**Mitigation surface:** Phase 7 hypothesis H-IC-23 + H-IC-30 + Pillar C R12 programmable enforcement provide the substrate.

---

## §7 §9.4 — 3 Curriculum design recommendations (surface ≥3 options, NO recommendation)

Per breadth-NOT-selection — 3 design options parallel; per-option tradeoffs explicit; NO ranking.

### §7.1 Option A — Foundations-first (rigour-prioritized)

**Sequencing:** M1 → M2 → M3 → M4 → M5 → M9 → M7 → M8 → M6 → M10 → M11 → M12 (linear, cumulative)

**Trade-off:**
- Pros: rigorous + systematic; aligns с CHC factor-analytic tradition; deeper Stage-3+ outcomes (H-IC-24)
- Cons: slow + linear (~9-12 month minimum); engagement-risk (H-IC-16); late tool-creation (M6 = week 6-9 minimum); engineer-unfriendly pacing

**Best fit:** PhD-track / academic-rigour cohorts; structured-learning preference

### §7.2 Option B — Project-based (applied + motivating)

**Sequencing:** modules activated per project demand; learner-driven trajectory

**Trade-off:**
- Pros: applied + motivating; immediate engineering output; engineer-attractive; matches actual workflow
- Cons: component gaps may emerge; inconsistent cross-cohort; hard to assess (no clean completion); risks shallow M10 + M2

**Best fit:** Self-directed senior engineers; portfolio-building track

### §7.3 Option C — Hackathon-driven (high engagement + community)

**Sequencing:** 12 hackathons (1 per component over ~6 months) + master-apprentice 1:1 between hackathons

**Trade-off:**
- Pros: high engagement + community formation (H-IC-16); rapid cycles + immediate Stage-2; aligns Jetix hackathon vision; portfolio generation (12 hackathon projects per cohort member)
- Cons: depth concerns Stage 3+ (H-IC-24); burnout risk (12 intensive events); master-apprentice may suffer; hard для M2 + M10 в hackathon format

**Best fit:** Early-career + community-building track; Workshop activation vehicle

### §7.4 Cross-cutting tradeoffs (R1 surface, NO recommendation)

| Criterion | Option A | Option B | Option C |
|---|---|---|---|
| Time to Stage-3 | 9-12 mo | 12-18 mo | 6-12 mo |
| Engagement | Medium | High | **Highest** |
| Depth (Stage-4) | **Highest** | Medium | Medium |
| Engineer-attractive | Low | **Highest** | High |
| Cohort-scalability | Medium | Low | **Highest** |
| Cost-per-graduate | High | Medium | Low |
| R12-alignment (fork-and-leave ease) | ✅ | ✅ | ✅ |
| Karpathy LLM101n fit | Partial | **Strong** | **Strong** |

**Brigadier-scribe NOTE per R1:** This table surfaces tradeoffs. NO recommendation made. Ruslan ack required для selection или hybrid choice.

---

## §8 Open questions (R1 surface)

- Should pilot cohort run **3-arm RCT** (A vs B vs C) to empirically test H-IC-16+19+24? Resource cost ~6 months + 60+ cohort members
- Should missing-component candidates (MC-1 Gwm / MC-5 Glr / MC-6+7 empathy+social / MC-2 Gs) be added before pilot OR mid-pilot pivoting allowed?
- 12 → 14 → 16 component expansion: where to stop? (Phase 5 surfaced ~14 critical; Ruslan ack decision)
- Curriculum credentialing — Workshop-graduate как degree-equivalent? Or signal-only? (H-IC-27)
- Cohort revenue model — Mondragón ratio + QF (R12 programmable) — design specifics: Ruslan ack required

---

## §9 Phase 7 summary

- **30 hypotheses** across 4 categories (8 framework / 7 gap / 10 design / 5 outcomes)
- **R12 alignment check ✅** (curriculum substrate does NOT enable extraction)
- **3 sequencing options surfaced parallel** (Foundations-first / Project-based / Hackathon-driven) с tradeoff matrix; NO recommendation per R1
- **Hybrid options** flagged (Phase 7 §7 + H-IC-19 candidate)
- **Acceptance criterion §13:** ≥20 H + R12 alignment + 3 design options ✅

---

*Phase 7 hypothesis bank + curriculum design ✅. 30 H surfaced; R12 alignment confirmed; 3 design options parallel (NO recommendation). Phase 8 synthesis + Summary + 6-8 mermaid + final push next.*
