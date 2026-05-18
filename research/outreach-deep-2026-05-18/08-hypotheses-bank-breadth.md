---
type: research-phase-7
phase: 7
session: outreach-system-scalable-deep-research-2026-05-18
date: 2026-05-18 evening
parents:
  - prompts/outreach-system-scalable-deep-research-2026-05-18.md §9 (Phase 7 spec)
  - Phases 1-6 (all preceding)
  - ~/.claude/projects/C--Users-49152/memory/feedback_breadth_not_selection.md
cells_dispatched: all cells × surfacing
F: F2
G: outreach-deep-2026-05-18-hypothesis-bank
R: refuted_if_(hypotheses <25 with refutation_conditions OR overlap >30% with concept doc D OS-T1..T5 OR refutation predicates absent / vague)
constitutional_posture: R1 + R6 + R11 + R12 + EP-5 + breadth-NOT-selection
word_budget: 3500
---

# Phase 7 — Hypothesis Bank (37 H, Breadth Coverage, Refutation Explicit)

> **R1 + breadth NOT selection.** All H = testable hypotheses с refutation_conditions. NOT decisions для ack; NOT recommendations. Ruslan reviews bank → picks which (if any) to design test for.

> Per `feedback_breadth_not_selection.md`: surface complete bank; do NOT collapse к single recommendation per category.

---

## §0 Format reference

Per §9.1 prompt:

```
ID: H-OUT-N
Claim: <statement>
F: F2-F3 (per EP-5)
G: <bounded context>
R: refuted_if_<specific predicate>
Test design: <how to test>
Acceptance: <success criteria>
Refutation conditions: <falsification predicates>
Cross-ref: <existing canonical OR research stream OR ML/AI 45-H>
```

---

## §1 Recruitment hypotheses (H-OUT-1 to H-OUT-7)

### H-OUT-1 — 10-person video team assembly within 60 days feasible
- **Claim:** 10-team can be assembled via RU L2 telegram + Workshop apprenticeship referrals + freelancer platforms within 60-day window.
- **F:** F2 (concept doc D OS-T1 baseline)
- **G:** Phase 1 Q3 2026 60-day window
- **R:** refuted_if_(team incomplete >75% capacity by day 60 OR vetting bar relaxed >2 standard deviations)
- **Test design:** Recruitment funnel tracking — sources / interviews / hires per week.
- **Acceptance:** ≥75% capacity (7-8 of 10) hired by day 60 with vetting bar preserved.
- **Cross-ref:** Phase 3 §2 + concept doc D §3.1 + OS-T1

### H-OUT-2 — Workshop apprenticeship referral = highest quality recruit source
- **Claim:** Workshop apprenticeship referrals produce highest 90-day retention + output quality vs other sources.
- **F:** F2 (pre-data)
- **G:** 90-day cohort post-hire
- **R:** refuted_if_(retention rate <T1 source vs T2/T3 OR output quality variance not significant)
- **Test design:** Cohort tracking — retention + KPI per source channel over 90 days.
- **Acceptance:** Workshop-referred ≥1.3× retention rate + ≥1.2× output quality vs T2/T3 sources.
- **Cross-ref:** Phase 3 §2.1 + Workshop concept 2026-04-30

### H-OUT-3 — 5 role-types sufficient; no 6th role needed Phase 1
- **Claim:** Per concept doc D §3.1, 5 role-types (Producer/Copywriter/Talent/Researcher/CRM) sufficient for Phase 1; no 6th specialised role needed.
- **F:** F2
- **G:** 60-day operational window
- **R:** refuted_if_(operational gaps identified that none of 5 roles cover in 60-day retro)
- **Test design:** 60-day retro identifying gaps + role attribution.
- **Acceptance:** Zero unaddressed operational gaps in retro.
- **Cross-ref:** Phase 3 §1 + concept doc D §3.1

### H-OUT-4 — Compensation Model α (fixed + variable + Mondragón cap) optimal
- **Claim:** Model α (fixed €2-4K + ≤30% variable + Mondragón ratio cap + exit-tokens) optimal for 90-day retention vs Model β (part-time stipend) and Model γ (project-rate).
- **F:** F2
- **G:** 10-team comp decision
- **R:** refuted_if_(90-day retention <80% OR explicit comp-related exit reasons surfacing)
- **Test design:** Implementation of one model; 90-day retention + exit interview.
- **Acceptance:** ≥80% retention + zero comp-related exits attributable.
- **Cross-ref:** Phase 3 §2.3 + Pillar C Tier 2 R12 + First Clan Charter LOCK 2026-05-12

### H-OUT-5 — Vetting bar: prior content production experience required
- **Claim:** Prior content production portfolio (≥3 published works) = mandatory vetting bar correlates с output quality.
- **F:** F2
- **G:** Per-role vetting Phase 3 §2.2
- **R:** refuted_if_(output quality variance not significant by prior-experience tier)
- **Test design:** Cohort comparison — high vs low prior experience.
- **Acceptance:** High-experience cohort ≥1.5× output quality (peer-review rubric).
- **Cross-ref:** Phase 3 §2.2

### H-OUT-6 — Geographic distribution Berlin + RU + remote optimal
- **Claim:** Mixed Berlin-Workshop + RU L2 + remote distribution = optimal timezone coverage + cultural coherence (vs Berlin-only or remote-only).
- **F:** F2
- **G:** 10-team geographic policy
- **R:** refuted_if_(timezone-coordination overhead >15% capacity OR cultural drift identified at quarterly retro)
- **Test design:** Quarterly retro + coordination-overhead tracking.
- **Acceptance:** Coordination overhead <15% capacity; zero documented cultural drift incidents.
- **Cross-ref:** Phase 3 §2.1 + sovereign-AI alignment (H-ML-22)

### H-OUT-7 — Diverse hiring improves output quality
- **Claim:** Female / non-binary / cross-cultural hiring quota improves output quality (peer rubric) by capturing wider perspective range.
- **F:** F2 (industry research mixed)
- **G:** Per-cohort comp via peer rubric
- **R:** refuted_if_(diverse vs non-diverse cohort show no peer-rubric quality difference OR diversity tax in coordination >quality lift)
- **Test design:** Cohort comparison with diverse vs less-diverse composition.
- **Acceptance:** Diverse cohort ≥1.1× peer-rubric score with comparable coordination overhead.
- **Cross-ref:** Phase 3 §2.1 + Workshop concept inclusivity

---

## §2 6-resources hypotheses (H-OUT-8 to H-OUT-13)

### H-OUT-8 — Information + Team + Time triad sufficient Phase 1
- **Claim:** 3-resource baseline (per text_009 ¶3 verbatim) sufficient for Phase 1 operation without 4-5-6 specification.
- **F:** F3 (4-6/6 precedent corroboration; voice anchor explicit)
- **G:** Phase 1 60-day operational
- **R:** refuted_if_(6-month operational gap analysis identifies resource bottleneck unaddressed by Info+Team+Time only)
- **Test design:** 6-month operational gap analysis post-Phase 1.
- **Acceptance:** Zero unaddressed bottleneck from missing 4-5-6 resource slot.
- **Cross-ref:** Phase 2 §1 + text_009 ¶3 verbatim

### H-OUT-9 — 6-resources framework matches a16z implicit
- **Claim:** a16z's implicit 6-resources operationalisation (per Andrew Chen content) maps к one of Lists A-D (probably mix of B-Network + C-Compute + D-Methodology).
- **F:** F2
- **G:** Andrew Chen content analysis
- **R:** refuted_if_(systematic content analysis shows no clean mapping to any candidate list)
- **Test design:** Researcher dossier — Chen content + content-analyse for resource taxonomy.
- **Acceptance:** ≥4 of 6 resources в Chen content map cleanly к one candidate list.
- **Cross-ref:** Phase 1 §2 + Phase 2 §3

### H-OUT-10 — Compute > Capital для Phase 1
- **Claim:** Compute (List C #4) bottleneck more material than Capital (List A/B #4) для Phase 1 throughput.
- **F:** F2
- **G:** Phase 1-2 operational
- **R:** refuted_if_(Compute spend rate < Capital spend rate or compute не bottleneck по retro)
- **Test design:** Per-resource bottleneck monitoring + monthly spend rate.
- **Acceptance:** Compute = top-3 bottleneck identified by month 3; Capital not top-3.
- **Cross-ref:** Phase 2 §4 List C

### H-OUT-11 — Mentor-bandwidth = scarcest 5th resource Phase 2
- **Claim:** Mentor-bandwidth (List C #5) = scarcest Phase 2 resource due к 1:5 TPS pairing demand.
- **F:** F2
- **G:** Phase 2 cohort 1 (Wave 1, Q3-Q4 2026)
- **R:** refuted_if_(mentor capacity does not saturate before any other resource)
- **Test design:** Per-cohort mentor capacity utilisation monitoring.
- **Acceptance:** Mentor-bandwidth = top-1 bottleneck Phase 2 cohort 1.
- **Cross-ref:** Phase 2 §4 + Phase 4 §3 TPS pairing

### H-OUT-12 — 6-resources framework portable к other 8 Jetix projects
- **Claim:** 6-resources framework applies к hackathon-platform / system-merger / education / quick-money / brand / community / ai-tools / engineering-thinking projects.
- **F:** F2
- **G:** Cross-project application
- **R:** refuted_if_(≥3 projects do not fit без forcing OR project-specific resource framework outperforms)
- **Test design:** Per-project bootstrap pilot with 6-resources framing.
- **Acceptance:** ≥6 of 8 projects fit cleanly; per-project resource framework can be derived from base 6.
- **Cross-ref:** Phase 2 §8 + `.claude/config/project-types.yaml`

### H-OUT-13 — Naval «specific knowledge» = synthesis-aware 6th resource (List D)
- **Claim:** Naval Ravikant «specific knowledge» concept = 6th resource of List D (synthesised); correlates с outreach quality per-target.
- **F:** F2
- **G:** L1 + Master Workshop outreach
- **R:** refuted_if_(target feedback на specific-knowledge framing does not differentiate vs generic-knowledge framing)
- **Test design:** A/B test specific-knowledge framed vs generic framed outreach к Master Workshop targets.
- **Acceptance:** Specific-knowledge framed ≥1.3× substantive engagement rate.
- **Cross-ref:** Phase 1 §3 Naval + Phase 2 §5 List D

---

## §3 Training cohort hypotheses (H-OUT-14 to H-OUT-19)

### H-OUT-14 — 100-trained cohort assembly within 12 months feasible
- **Claim:** Per concept doc D OS-T2 + Phase 4 §7 12-month Gantt, 100 operators trained within 12 months (Q4 2026 milestone).
- **F:** F2
- **G:** Phase 4 12-month cohort
- **R:** refuted_if_(trained <30 by Q4 2026 OR pairing capacity collapses)
- **Test design:** Monthly cohort milestone tracking.
- **Acceptance:** ≥30 trained by Q4 2026; trajectory к 100 by Q1-Q2 2027.
- **Cross-ref:** Phase 4 §7 + concept doc D OS-T2

### H-OUT-15 — TPS mentor-pairing produces ≤4h/target velocity
- **Claim:** Per concept doc D §3.2 + `research/deepening-2026-05-18/14` TPS pattern, trainee post-Tier-3 produces personalised outreach within ≤4h per target.
- **F:** F2
- **G:** Tier 3 graduate productivity
- **R:** refuted_if_(median time-per-target >6h after Tier 3 completion)
- **Test design:** Per-trainee throughput tracking post-Tier-3.
- **Acceptance:** Median time/target ≤4h; 80th percentile ≤6h.
- **Cross-ref:** Phase 4 §3 + concept doc D §3.2

### H-OUT-16 — Tier 1 + Tier 2 sufficient for outreach competence
- **Claim:** Tier 1 (Foundation) + Tier 2 (Methodology) curriculum produces baseline outreach competence; Tier 3 specialisation = depth not baseline.
- **F:** F2
- **G:** Tier 2 graduate output quality
- **R:** refuted_if_(Tier 2 graduates fail baseline peer-review threshold consistently)
- **Test design:** Tier 2 graduate output baseline benchmark.
- **Acceptance:** ≥80% Tier 2 graduates produce baseline-quality outreach (peer review ≥3.5/5).
- **Cross-ref:** Phase 4 §2.1-2.2

### H-OUT-17 — Trainee-mentor pairing 1:5 ratio optimal
- **Claim:** 1 mentor : 5 trainees ratio optimal; 1:3 = waste; 1:8 = quality drift.
- **F:** F2
- **G:** Tier 2-3 pairing
- **R:** refuted_if_(1:5 quality variance > 1:3 OR 1:8 quality acceptable)
- **Test design:** Pilot cohort с varied ratios.
- **Acceptance:** 1:5 quality ≥1:3 within ±5% with mentor-capacity efficiency.
- **Cross-ref:** Phase 4 §3.2 + TPS deepening doc

### H-OUT-18 — Fork-and-leave preserved → recruitment improves
- **Claim:** Per First Clan Charter R12 LOCK, fork-and-leave preservation → higher referral rate post-exit (positive-fork pattern), vs lock-in patterns.
- **F:** F2
- **G:** Post-exit referral rate
- **R:** refuted_if_(post-fork referral rate not >0 OR fork rate >30% indicating systematic dissatisfaction)
- **Test design:** Post-exit interview + referral tracking 12 months post-fork.
- **Acceptance:** ≥10% of fork-and-leave alumni refer ≥1 future recruit within 12 months.
- **Cross-ref:** Phase 4 §4.3 + First Clan Charter R12 LOCK 2026-05-12

### H-OUT-19 — Career trajectory к Master Workshop pulls highest-quality recruits
- **Claim:** Tier 4 → Workshop apprentice → Master Workshop track attracts higher-quality recruits than Tier-3-terminal trajectory.
- **F:** F2 (aspirational)
- **G:** Tier 1 applicant pool quality
- **R:** refuted_if_(Master-Workshop-track applicants no quality differential vs other-track)
- **Test design:** Applicant cohort cross-comparison by track preference.
- **Acceptance:** Master-Workshop-track applicants ≥1.5× peer-rubric pre-cohort score.
- **Cross-ref:** Phase 4 §2.4 + text_009 Thread 14

---

## §4 Personalisation hypotheses (H-OUT-20 to H-OUT-25)

### H-OUT-20 — LLM-assist + human craft hybrid saves 70% time без authenticity loss
- **Claim:** Hybrid (Phase 5 §1) saves 70% time vs full-human while maintaining authenticity (no LLM-signature detection >5%).
- **F:** F2
- **G:** Phase 5 personalisation
- **R:** refuted_if_(LLM-signature detection >20% OR time-saving <50%)
- **Test design:** A/B blind test — full-LLM vs hybrid vs full-human; target detection rate + time-per-engagement.
- **Acceptance:** Hybrid 60-80% time saving + LLM-signature detection <10%.
- **Cross-ref:** Phase 5 §1.3 + H-ML cross-link

### H-OUT-21 — Per-target research depth correlates с response rate quadratically
- **Claim:** Response rate scales super-linearly with per-target research depth (≥quadratic correlation up to threshold).
- **F:** F2
- **G:** Per-class outreach
- **R:** refuted_if_(per-target effort vs response rate correlation linear or flat)
- **Test design:** Per-engagement research-depth tracking + response correlation analysis.
- **Acceptance:** Quadratic-or-better correlation Spearman ≥0.7 up к 4h-per-target threshold.
- **Cross-ref:** Phase 5 §3.2 + Naval specific-knowledge pattern

### H-OUT-22 — 3 A/B variants per target class sufficient; 5+ overkill
- **Claim:** 3 A/B variants per target class (per Phase 5 §2.2) sufficient; 5+ shows diminishing returns.
- **F:** F2
- **G:** Per-class A/B testing
- **R:** refuted_if_(5+ variants show variance >25% over 3-variant baseline)
- **Test design:** A/B/C/D/E test with 5 variants per class; variance analysis.
- **Acceptance:** Variance reduction plateau at 3 variants (≤10% additional reduction with 5+).
- **Cross-ref:** Phase 5 §2.2

### H-OUT-23 — R12 data minimisation не reduces response rate
- **Claim:** R12 data-minimisation (Phase 5 §4.1) preserves response rate vs full-extraction baseline.
- **F:** F2
- **G:** Per-engagement response rate
- **R:** refuted_if_(data-minimised cohort response rate <80% of full-extraction baseline)
- **Test design:** A/B test — data-minimised vs full-public-data outreach (no scraped-private data either way).
- **Acceptance:** Data-minimised response rate ≥95% of full-public baseline; statistical parity.
- **Cross-ref:** Phase 5 §4.1 + R12

### H-OUT-24 — Synthetic LLM-signature reduces trust 20%+
- **Claim:** Per Phase 5 §1.3 phil critic dissent — detected LLM-signature reduces target trust 20%+ vs human-craft equivalent.
- **F:** F2
- **G:** Per-target trust feedback
- **R:** refuted_if_(blind-test detection <5% OR detected-LLM response rate within ±5% of human-craft)
- **Test design:** Blind-test response analysis; target post-engagement feedback (consent-based).
- **Acceptance:** Detection-rate <10% with hybrid mode; full-LLM = ≥30% detection rate.
- **Cross-ref:** Phase 5 §1.3 + phil critic AP-6 dissent

### H-OUT-25 — Permanent suppression + opt-out reduces complaint rate 5×
- **Claim:** Hard-coded suppression list + opt-out respect (Phase 5 §4.2) reduces complaint rate 5× vs no-suppression baseline.
- **F:** F3 (CAN-SPAM / GDPR norm baseline)
- **G:** Per-engagement complaint rate
- **R:** refuted_if_(suppression-enabled complaint rate not statistically lower than no-suppression baseline)
- **Test design:** Per-engagement complaint tracking pre/post suppression discipline.
- **Acceptance:** Complaint rate ≤1/10K engagements with suppression vs ≥5/10K baseline.
- **Cross-ref:** Phase 5 §4.2 + R12 + GDPR norm

---

## §5 Target audience hypotheses (H-OUT-26 to H-OUT-32)

### H-OUT-26 — L1 5%+ response rate achievable via warm-intro chain
- **Claim:** Per concept doc D OS-T4 + Phase 6 §3.1, L1 inner ring (Karpathy etc.) 5%+ response rate achievable when warm-intro chain in place.
- **F:** F2 (aspirational)
- **G:** Phase 1 L1 funnel
- **R:** refuted_if_(L1 response rate <1% within 12mo)
- **Test design:** Per-L1-target tracking; warm-intro chain status; response rate.
- **Acceptance:** ≥5% response rate (≥1 of 20 L1 targets respond meaningfully within 12mo).
- **Cross-ref:** Phase 6 §3.1 + concept doc D OS-T4

### H-OUT-27 — Master Workshop 15%+ interest rate via deep research substrate
- **Claim:** Per Phase 6 §3.1 + concept doc D, deep-research-backed outreach к Master Workshop next-tier achieves ≥15% interest rate.
- **F:** F2
- **G:** Master Workshop Q3-Q4 2026 cohort
- **R:** refuted_if_(interest rate <5% OR substance gap detected by ML scholar feedback)
- **Test design:** Per-target outreach with deep research substrate; interest-rate tracking.
- **Acceptance:** ≥15% Master Workshop next-tier interest rate.
- **Cross-ref:** Phase 6 §3.1 + text_009 Thread 14

### H-OUT-28 — Миллиардеры 1-3% response rate floor
- **Claim:** Per Phase 6 §3.2, миллиардеры 1-3% response rate floor achievable via «×100 multiplier» framing (with R12 reframe to target-retains-primary-value).
- **F:** F2
- **G:** 3K-target funnel
- **R:** refuted_if_(response rate <0.5% OR R12 caveat triggers reputation cost)
- **Test design:** 3K-target outreach с response tracking + reputation monitoring.
- **Acceptance:** 1-3% response rate; zero documented R12 reputation incidents.
- **Cross-ref:** Phase 6 §3.2 + text_008 «×100 multiplier» framing

### H-OUT-29 — Sovereign-AI RU L2 = highest-quality cohort entry
- **Claim:** Per H-ML-22 + H-ML-40, RU L2 telegram community с Sovereign-AI offer = highest-quality cohort entry rate (vs other language / community combinations).
- **F:** F2
- **G:** RU L2 cohort entry rate
- **R:** refuted_if_(RU L2 response rate not differentially higher than baseline other-language outreach)
- **Test design:** A/B vs other-language / other-community baseline.
- **Acceptance:** RU L2 response rate ≥2× baseline other-language.
- **Cross-ref:** ML/AI 45-H H-ML-22 + H-ML-40 + Phase 6 §1.5

### H-OUT-30 — Платформы B2B cycle quarter-length acceptable Phase 2
- **Claim:** Per Phase 6 §1.6, Платформы B2B quarter-length cycle acceptable to Jetix cashflow Phase 2.
- **F:** F2
- **G:** Phase 2 Platform pipeline
- **R:** refuted_if_(cycle-length >2 quarters median OR cashflow gap created by long cycle)
- **Test design:** Per-Platform-deal cycle tracking; cashflow integration.
- **Acceptance:** ≥75% Platform deals close within 1 quarter; cashflow plan absorbs longer cycles.
- **Cross-ref:** Phase 6 §1.6 + System Merger Protocol Concept doc C

### H-OUT-31 — Tier prioritisation matrix portable beyond outreach
- **Claim:** Per Phase 6 §8, T1-T3 matrix portable к other Jetix programs (Workshop / Clan / hackathon / investor / partner).
- **F:** F2
- **G:** Cross-program application
- **R:** refuted_if_(≥3 programs do not fit matrix без forcing)
- **Test design:** Per-program pilot of T1-T3 framing.
- **Acceptance:** ≥4 of 5 programs fit cleanly.
- **Cross-ref:** Phase 6 §8

### H-OUT-32 — Conversion funnel L1 → cohort entry rate >20%
- **Claim:** Per Phase 5 §3.4, L1 positive responses convert к cohort entry ≥20%.
- **F:** F2
- **G:** L1 funnel conversion
- **R:** refuted_if_(L1 response → cohort entry conversion <10%)
- **Test design:** Per-L1-response cohort-entry tracking.
- **Acceptance:** ≥20% L1 responses become substantive cohort engagement (meeting / Workshop / Clan exploration).
- **Cross-ref:** Phase 5 §3.4

---

## §6 Cross-precedent hypotheses (H-OUT-33 to H-OUT-37)

### H-OUT-33 — Sahil solo content pattern viable as 10-team Phase 1 backbone
- **Claim:** Per Phase 1 §1.7, Sahil's content-as-outreach pattern adopted by 10-team copywriter + researcher = viable Phase 1 outreach backbone.
- **F:** F2
- **G:** Phase 1 content velocity
- **R:** refuted_if_(content velocity from 10-team <Sahil-solo baseline within 60 days)
- **Test design:** Content velocity tracking 10-team vs Sahil documented output.
- **Acceptance:** ≥3× Sahil-solo velocity (10-team multiplier minus coordination overhead).
- **Cross-ref:** Phase 1 §1 + Phase 3 §3.2 Copywriter

### H-OUT-34 — Chen warm-intro chain + 10-team = exponential L1 reach
- **Claim:** Per Phase 1 §2.7 + Phase 6 §1.1, warm-intro chain + 10-team-supported deep research = exponential L1 reach (per Thread 12 «снежный ком»).
- **F:** F2
- **G:** L1 funnel velocity Phase 1
- **R:** refuted_if_(L1 funnel velocity не exponential — linear or sub-linear)
- **Test design:** L1 reach tracking over 6 months; growth-curve analysis.
- **Acceptance:** L1 reach grows ≥1.5× quarter-over-quarter (exponential signal).
- **Cross-ref:** Phase 1 §2 + Phase 6 §1.1 + Thread 12

### H-OUT-35 — Naval asymmetric leverage applicable к ALL 6 classes
- **Claim:** Per Phase 1 §3.7, Naval's asymmetric leverage framing (specific knowledge + content multiplier) applies к all 6 target classes.
- **F:** F2
- **G:** Per-class asymmetric leverage application
- **R:** refuted_if_(≥2 classes show leverage framing forced or counterproductive)
- **Test design:** Per-class A/B asymmetric-leverage framing vs baseline.
- **Acceptance:** ≥5 of 6 classes show leverage framing ≥1.2× engagement vs baseline.
- **Cross-ref:** Phase 1 §3.7

### H-OUT-36 — Levels build-in-public integrated с Workshop apprenticeship
- **Claim:** Per Phase 1 §4.7, Pieter Levels build-in-public pattern adopted by Workshop apprenticeship = transparency-substrate amplifier.
- **F:** F2
- **G:** Workshop docs visibility
- **R:** refuted_if_(Workshop docs не attract apprenticeship applications within 6mo)
- **Test design:** Workshop docs public release + apprenticeship application tracking.
- **Acceptance:** ≥30 apprenticeship applications within 6 months of public release.
- **Cross-ref:** Phase 1 §4 + Workshop concept 2026-04-30

### H-OUT-37 — GitHub DevRel cohort pattern adapts к Master Workshop
- **Claim:** Per Phase 1 §5.7, GitHub DevRel cohort engagement pattern (Universe + meetup + advocate) adapts к Master Workshop tiered cohort engagement.
- **F:** F2
- **G:** Q3-Q4 2026 Master Workshop substrate
- **R:** refuted_if_(DevRel-style adaptation не attracts Master Workshop next-tier within 6mo)
- **Test design:** Implement DevRel-style cohort engagement (annual event + regional meetup + advocate); track Master Workshop next-tier attraction.
- **Acceptance:** ≥5 Master Workshop next-tier engaged via DevRel-style mechanism within 6mo of launch.
- **Cross-ref:** Phase 1 §5 + Phase 6 §1.2

---

## §7 Cross-ref table

| H-ID range | Category | Cross-ref domain |
|---|---|---|
| H-OUT-1 to H-OUT-7 | Recruitment | Phase 3 + concept doc D §3.1 + R12 compensation |
| H-OUT-8 to H-OUT-13 | 6-resources | Phase 2 + text_009 ¶3+4 + cross-precedent |
| H-OUT-14 to H-OUT-19 | Training cohort | Phase 4 + TPS deepening + Workshop concept |
| H-OUT-20 to H-OUT-25 | Personalisation | Phase 5 + AP-6 dissent + R12 |
| H-OUT-26 to H-OUT-32 | Target audience | Phase 6 + concept doc D §5 + ML/AI 45-H |
| H-OUT-33 to H-OUT-37 | Cross-precedent | Phase 1 + concept doc D §6 |

---

## §8 Cross-link к ML/AI 45-H

| H-OUT | H-ML cross-link |
|---|---|
| H-OUT-13 (Naval specific knowledge) | H-ML-22 Sovereign-AI offer |
| H-OUT-19 (Master Workshop trajectory) | H-ML-36 Master Workshop ML engineer destination |
| H-OUT-26 (L1 5%+ response) | H-ML-39 Karpathy-specific outreach |
| H-OUT-29 (RU L2 cohort) | H-ML-40 RU L2 telegram community + H-ML-22 |
| H-OUT-30 (Платформы B2B) | (Concept doc C cross-ref) |
| H-OUT-19 (career trajectory) | H-ML-44 Education compounded gratitude loop |

---

## §9 Constitutional preservation

- **R1:** All 37 H = surface only; NONE selected / promoted / ack'd here.
- **R6:** Cross-ref per H к evidentiary substrate.
- **R11:** No hypothesis triggers external action автоматически.
- **R12:** Per H, R12 risk surfaced where applicable (esp. recruitment + personalisation).
- **EP-5:** F-grade per H; F2 predominant; F3 для H-OUT-8 (3-resource baseline) + H-OUT-25 (suppression vs CAN-SPAM/GDPR norm).
- **Breadth NOT selection:** all 37 surfaced; Ruslan picks which to operationalise.

---

*Phase 7 hypothesis bank. 37 H с refutation conditions across 6 categories (Recruitment / 6-resources / Training / Personalisation / Target audience / Cross-precedent). R1 + R6 + R11 + R12 + EP-5 + breadth-NOT-selection preserved. [src: Phases 1-6 + concept doc D + voice anchor text_009 + ML/AI 45-H + cross-precedent]*
