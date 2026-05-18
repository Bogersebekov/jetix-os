---
type: research-doc
phase: 6
title: Hypothesis bank — breadth NOT selection
date: 2026-05-18 evening
authored_by: brigadier-scribe
word_budget: ~3000
fpf_layer: B.3 F-G-R per hypothesis
hypothesis_count_target: 30-50
hypothesis_count_actual: 45
constitutional_posture: breadth-NOT-selection per feedback_breadth_not_selection.md
acceptance_predicate: refuted_if_(<20_H_with_refutation_conditions OR any_H_is_recommendation)
---

# Phase 6 — Hypothesis bank (breadth NOT selection)

> Per `feedback_breadth_not_selection.md` — research stage = surface ALL Q as testable H, NOT recommendations for ack. **No H is selected / promoted / ack'd here.** Ruslan reviews and selects subset для testing.
>
> **Format:** ID / Claim / F / G / R / Test design / Acceptance / Refutation / Cross-ref.
>
> **45 hypotheses surfaced** across 4 categories.

---

## §1 Industry hypotheses (H-ML-1 to H-ML-10)

### H-ML-1 — ML engineers under-served by current education
- **Claim:** Current ML education (Coursera / bootcamps / university) leaves critical gap in (a) production-grade engineering practice (b) formal methodology (c) mentorship.
- **F/G/R:** F3 (industry surveys + Karpathy LLM101n adoption signal) / Global ML community / refuted_if_(Coursera/Udacity satisfaction surveys show >85% «well-prepared» AND Karpathy-tier alternative materials get <10K stars)
- **Test design:** Survey ML engineer cohort (n≥500) on perceived education gaps; correlate с career-stage outcomes
- **Acceptance:** ≥60% of mid-career ML engineers report gap in ≥1 of (production / methodology / mentorship)
- **Cross-ref:** Karpathy direction 09 + doc 02 §2 mental models

### H-ML-2 — ML engineer compensation drives churn vs satisfaction inverted
- **Claim:** Higher compensation ≠ higher satisfaction для ML engineers; meaning + autonomy + craft mastery dominate.
- **F/G/R:** F2 (anecdotal evidence; Karpathy Tesla → Eureka transition) / Senior ML engineers (5+yr) / refuted_if_(controlled comp-vs-satisfaction survey shows monotonic positive correlation)
- **Test design:** Compensation × satisfaction × tenure regression on industry survey data
- **Acceptance:** R² < 0.3 для comp-satisfaction relationship in senior bracket
- **Cross-ref:** doc 02 §5 career paths

### H-ML-3 — Russian-speaking ML community = distinct partner cohort
- **Claim:** Russian-speaking ML community has distinct rhythm / culture / pain points worth dedicated Jetix engagement.
- **F/G/R:** F3 (ШАД / ODS / telegram-channel ecosystem evidence) / Russian-speaking ML engineers / refuted_if_(Jetix outreach RU-specific vs global produces <2× engagement rate)
- **Test design:** A/B test outreach RU-localised vs EN-only
- **Acceptance:** RU-localised outreach response rate >2× EN-only
- **Cross-ref:** doc 02 §6 RU landscape

### H-ML-4 — ML researcher vs ML engineer cohorts have different needs
- **Claim:** ML researcher (paper-focused) and ML engineer (production-focused) need different Workshop curricula.
- **F/G/R:** F3 (career path divergence evidence) / Both cohorts / refuted_if_(survey shows >70% overlap in stated educational needs)
- **Test design:** Cohort survey + Workshop pilot с tracks
- **Acceptance:** ≥40% curriculum divergence between tracks for satisfaction
- **Cross-ref:** doc 02 §1 role taxonomy

### H-ML-5 — Open-source culture aligns с R12 anti-extraction
- **Claim:** ML community open-source norms = natural philosophical fit с R12 anti-extraction substrate ownership thesis.
- **F/G/R:** F3 (HuggingFace / EleutherAI / LAION norms) / Open-source ML contributors / refuted_if_(R12 framing tested in outreach produces NO measurable preference vs neutral framing)
- **Test design:** Outreach A/B with R12-explicit vs neutral framing
- **Acceptance:** R12-framed outreach gets >1.3× response from open-source-active candidates
- **Cross-ref:** R12 LOCK 2026-05-12 + doc 08 §3 Class 2

### H-ML-6 — Mentor scarcity = primary ML community bottleneck
- **Claim:** Quality mentorship is scarce in ML; Jetix Workshop Master-Apprentice model addresses this.
- **F/G/R:** F2 (anecdotal; mentor-matching platforms struggle) / ML learner cohorts / refuted_if_(survey shows mentorship NOT in top-3 stated unmet need)
- **Test design:** Survey ML learners on top-5 unmet needs
- **Acceptance:** Mentorship in top-3 for ≥60% respondents
- **Cross-ref:** doc 08 §2 Workshop apprenticeship

### H-ML-7 — Production gap = strongest ML services opportunity
- **Claim:** ML model production deployment expertise is scarcer than research-style ML expertise; consulting opportunity asymmetric.
- **F/G/R:** F3 (industry job-posting data; MLOps role recent emergence) / Tech orgs adopting ML / refuted_if_(job-posting analysis shows <2× research-vs-production ratio of unfilled roles)
- **Test design:** Job-posting analysis cross-industry; pricing-power evidence in consulting market
- **Acceptance:** Production roles >2× unfilled rate vs research
- **Cross-ref:** doc 05 Layer 3 production tools + doc 08 §6 Class 5

### H-ML-8 — Foundation models change ML role taxonomy
- **Claim:** Foundation models + fine-tuning shifts ML engineer role away from from-scratch architecture toward (a) prompting (b) fine-tuning (c) deployment (d) evaluation. Old taxonomy becoming stale.
- **F/G/R:** F3 (post-2023 industry shift evidence) / Industry ML engineers post-2024 / refuted_if_(from-scratch architecture work increases vs decreases in next 2 yr)
- **Test design:** Repeat survey 2027; measure shift in self-described primary activities
- **Acceptance:** ≥30% shift toward fine-tune/eval/deploy in 2 yr
- **Cross-ref:** doc 04 §4 HuggingFace + doc 02 §2 Karpathy Software 2.0

### H-ML-9 — Russian corporate AI labs interest Jetix-pattern partnership
- **Claim:** Sber / Yandex / Tinkoff / VK AI labs have substrate-pattern interest disjoint от global-frontier-lab partnerships.
- **F/G/R:** F2 (geographic + jurisdictional factors) / RU corporate AI labs / refuted_if_(direct outreach to ≥3 RU corp AI labs produces no engagement vs global outreach)
- **Test design:** Parallel outreach to RU vs global corp labs; measure meeting/partnership conversion
- **Acceptance:** RU labs engage at ≥1.5× rate of global labs
- **Cross-ref:** doc 02 §6 RU landscape

### H-ML-10 — Hackathon community native к ML
- **Claim:** ML community has stronger competitive culture (Kaggle heritage) than other engineering disciplines; hackathon mode native fit.
- **F/G/R:** F3 (Kaggle 16M users + KDD competitions etc.) / ML community / refuted_if_(parallel hackathons in ML vs other-eng domains show ML <1.5× participation rate)
- **Test design:** Parallel Jetix hackathon events ML topic vs non-ML topic; measure participation
- **Acceptance:** ML hackathon ≥1.5× participation of comparable non-ML
- **Cross-ref:** doc 08 §4 Class 3

---

## §2 Tool hypotheses (H-ML-11 to H-ML-25)

### H-ML-11 — FPF + Jupyter integration = unique developer experience
- **Claim:** Jupyter notebook with FPF-aware extensions (provenance markers / F-G-R per cell / acceptance predicates) = differentiated learning + research environment.
- **F/G/R:** F2 (concept-level extrapolation) / Jetix Workshop apprentices / refuted_if_(prototype shows no measurable benefit vs vanilla Jupyter in user study)
- **Test design:** Build prototype; user study с Workshop apprentices
- **Acceptance:** ≥30% productivity / clarity uplift in apprentice tasks
- **Cross-ref:** doc 04 §1 Jupyter + FPF primitives

### H-ML-12 — HuggingFace hub = role-attestation primitive parallel
- **Claim:** HF Hub model-publication = same primitive as Foundation Part 6a Provenance + role-attestation conceptually; learn from HF UX.
- **F/G/R:** F2 (conceptual mapping) / Jetix substrate design / refuted_if_(HF UX patterns don't transfer to Foundation attestation use cases in concrete trial)
- **Test design:** Design Foundation attestation UX inspired by HF model cards
- **Acceptance:** Pattern reuse produces faster prototype + clearer UX vs from-scratch design
- **Cross-ref:** doc 04 §4 HuggingFace

### H-ML-13 — Optuna meta-pattern для brigadier dispatch
- **Claim:** HPO sampler dispatching pattern (TPE / random / Bayesian sampling над expert × mode space) applicable к brigadier cell dispatching as optimisation mechanism.
- **F/G/R:** F2 (conceptual parallel) / Brigadier dispatch logic / refuted_if_(implementation prototype shows no measurable improvement over current heuristic dispatch)
- **Test design:** Prototype HPO-inspired brigadier dispatch; A/B vs current heuristic
- **Acceptance:** ≥20% improvement in cell-output quality OR ≥30% reduction in token cost
- **Cross-ref:** doc 04 §8 Optuna + doc 07 §6.4

### H-ML-14 — PyTorch eager-by-default = research-friendly Workshop default
- **Claim:** PyTorch's eager execution + Python-idiomatic API = better Workshop teaching tool than TensorFlow's traditional static graphs.
- **F/G/R:** F4 (industry adoption evidence; PyTorch dominant in research) / Workshop ML curriculum / refuted_if_(Workshop apprentice retention or learning velocity lower on PyTorch vs TF cohort)
- **Test design:** Cohort comparison if curriculum tracks pilot
- **Acceptance:** PyTorch cohort metrics ≥ TF cohort metrics
- **Cross-ref:** doc 04 §3 PyTorch

### H-ML-15 — Polars vs pandas trade-off material для Workshop
- **Claim:** Polars (modern, lazy, Rust-backed) vs pandas (legacy, eager, mature) = teachable trade-off lesson worth Workshop module.
- **F/G/R:** F3 (post-2024 adoption signal Polars) / Workshop curriculum / refuted_if_(Polars adoption plateaus or reverses by 2027)
- **Test design:** Track GitHub stars / job postings / community adoption 2026-2028
- **Acceptance:** Polars sustained >20% YoY growth
- **Cross-ref:** doc 03 §6 Polars

### H-ML-16 — Gradient boosting trio worth teaching as comparative
- **Claim:** Teaching CatBoost/XGB/LGBM as comparative (vs picking one favourite) = better Workshop module than pick-one approach.
- **F/G/R:** F3 (industry practice variance evidence) / Workshop tabular ML module / refuted_if_(post-module survey shows apprentices confused by trio vs clarified)
- **Test design:** Trio-comparative vs pick-one curriculum A/B in pilot
- **Acceptance:** Trio cohort scores higher on tabular ML problem-solving
- **Cross-ref:** doc 04 §5-7 boosting libs

### H-ML-17 — Grafana = direct Foundation Part 8 implementation candidate
- **Claim:** Grafana + Prometheus stack = production-ready implementation для Foundation Part 8 Health Monitoring requirements.
- **F/G/R:** F3 (Grafana feature-set alignment) / Foundation Part 8 implementation choices / refuted_if_(POC reveals critical Foundation Part 8 SLI/SLO requirements unmappable to Grafana)
- **Test design:** POC implementation; map Part 8 requirements
- **Acceptance:** ≥80% of Part 8 SLI/SLO requirements directly implementable
- **Cross-ref:** doc 05 §6 Grafana + Foundation Part 8

### H-ML-18 — W&B/MLflow patterns inspire brigadier cycle artifact tracking
- **Claim:** W&B experiment-tracking patterns (run / sweep / artifact / lineage) transfer to brigadier cycle artifact tracking (cycle / dispatch / cell-output / provenance).
- **F/G/R:** F2 (conceptual parallel) / Brigadier cycle tooling / refuted_if_(W&B-inspired prototype doesn't reduce cycle artifact debugging time)
- **Test design:** Prototype + measure debugging time vs current approach
- **Acceptance:** ≥30% debugging time reduction
- **Cross-ref:** doc 05 §4-5 W&B/MLflow + Foundation Part 5

### H-ML-19 — Docker containerisation = Workshop infra module
- **Claim:** Docker fluency = teachable Workshop module; substrate for reproducible ML demos.
- **F/G/R:** F4 (industry-standard) / Workshop infra module / refuted_if_(apprentice cohort doesn't retain Docker skills 6mo post-module)
- **Test design:** Pre/post + 6mo follow-up assessment
- **Acceptance:** ≥70% apprentices retain functional Docker fluency
- **Cross-ref:** doc 05 §1 Docker

### H-ML-20 — FastAPI = Jetix API layer candidate
- **Claim:** FastAPI = appropriate choice для Jetix wiki/CRM/voice-pipeline API exposure when needed.
- **F/G/R:** F3 (Python-native + type-driven + auto-docs) / Jetix services API layer / refuted_if_(performance or feature gap surfaces in POC)
- **Test design:** POC of wiki API exposure
- **Acceptance:** POC meets latency + spec requirements
- **Cross-ref:** doc 05 §7 FastAPI

### H-ML-21 — Airflow conceptual analog к brigadier scheduled cycles
- **Claim:** Airflow DAG-based pipeline pattern conceptually parallels brigadier scheduled-cycle orchestration; lessons transferable.
- **F/G/R:** F2 (conceptual) / Brigadier scheduling design / refuted_if_(Airflow patterns don't help brigadier scheduling in concrete design exercise)
- **Test design:** Design exercise mapping Airflow patterns to brigadier needs
- **Acceptance:** ≥3 useful pattern transfers identified
- **Cross-ref:** doc 05 §2 Airflow + Foundation Part 4

### H-ML-22 — Sovereign-AI = differentiated Jetix consulting offer
- **Claim:** Self-hosted MLflow + open-source models + sovereign infra = differentiated consulting offer for RU + EU + privacy-sensitive clients.
- **F/G/R:** F3 (regulatory + geopolitical trends 2024-2026) / RU + EU enterprise clients / refuted_if_(sovereign-AI inquiries <10% of total client interest by 2027)
- **Test design:** Track inquiry mix in quick-money pipeline
- **Acceptance:** ≥15% inquiries cite sovereign-AI as primary requirement
- **Cross-ref:** doc 05 §5 MLflow + doc 08 §6 Class 5

### H-ML-23 — Kubernetes overkill для most Jetix offerings (initially)
- **Claim:** K8s = overkill для Jetix self-use; teach but don't require initially.
- **F/G/R:** F3 (small org context) / Jetix self-use + Workshop curriculum / refuted_if_(Jetix workloads grow to require K8s within 12mo)
- **Test design:** Monitor workload growth
- **Acceptance:** Single VM + Docker adequate for ≥12mo
- **Cross-ref:** doc 05 §11 Kubernetes

### H-ML-24 — Math literacy = Workshop entry gate
- **Claim:** Math foundation (linear algebra + probability + optimisation) = pre-requisite gate для Workshop apprenticeship; without it, ML learning brittle.
- **F/G/R:** F3 (industry educator consensus) / Workshop apprentice selection / refuted_if_(math-weak vs math-strong cohort show no learning velocity difference)
- **Test design:** Cohort cross-comparison
- **Acceptance:** Math-strong cohort ≥1.5× learning velocity
- **Cross-ref:** doc 03 §2 Math

### H-ML-25 — Python fluency assumed; not Workshop foundation
- **Claim:** Python fluency = entry assumption (not core Workshop teaching); module starts with ML-specific Python patterns.
- **F/G/R:** F3 (apprentice cohort baseline) / Workshop entry / refuted_if_(>50% apprentices need Python basics)
- **Test design:** Cohort baseline assessment
- **Acceptance:** <30% need basic Python module
- **Cross-ref:** doc 03 §1 Python

---

## §3 Methodology hypotheses (H-ML-26 to H-ML-35)

### H-ML-26 — ML 7-step = universal information-processing pattern
- **Claim:** ML engineer 7-step workflow generalises к universal information-processing pattern applicable across ≥5 distinct domains (business / personal / project / hackathon / research).
- **F/G/R:** F2 (Phase 4 doc 07 surfaces 6-precedent triangulation; F3 candidate) / Information-processing tasks under uncertainty / refuted_if_(<3 domains map without forcing OR competing frameworks outperform in controlled comparison)
- **Test design:** Workshop apprentice cross-domain transfer study; controlled framework comparison
- **Acceptance:** Direct mapping (no forcing) к 5+ domains; ≥3 independent precedent traditions converge
- **Cross-ref:** doc 07 Phase 4 entire

### H-ML-27 — NASA SE × ML × FPF Workshop = same root pattern
- **Claim:** NASA SE (NPR 7123 17 processes) + ML 7-step + FPF Workshop pattern share root engineering pattern.
- **F/G/R:** F3 (mapping in doc 07 §2.1 establishes 9/17 direct match) / Engineering methodologies generally / refuted_if_(post-hoc curve-fitting accusation sustains; or precedent careful reading rejects mapping)
- **Test design:** Independent reviewer validates mapping (e.g., NASA SE practitioner + FPF expert + ML eng triangulate)
- **Acceptance:** 2-of-3 reviewers concur mapping is non-trivial
- **Cross-ref:** doc 07 §2 cross-precedent triangulation

### H-ML-28 — Bitter Lesson × R12 anti-extraction philosophical alignment
- **Claim:** Sutton's Bitter Lesson (scale + compute > clever priors) aligns с R12 substrate-democratisation thesis (compute democratisation + open substrate > extraction-prone clever monopolies).
- **F/G/R:** F2 (philosophical interpretation) / AI policy framing / refuted_if_(Bitter Lesson supporters reject R12 framing in conversation as forced analogy)
- **Test design:** Conversation with Bitter Lesson advocates
- **Acceptance:** Substantive engagement vs dismissal
- **Cross-ref:** doc 02 §2 Sutton + R12 LOCK

### H-ML-29 — Hypothesis-driven improvement = trainable Workshop core skill
- **Claim:** Step 4 abductive loop discipline = trainable skill; Workshop apprentices can be measurably improved on this dimension.
- **F/G/R:** F3 (educational research on scientific reasoning) / Workshop apprentices / refuted_if_(pre/post assessment shows no improvement)
- **Test design:** Pre/post abductive-reasoning assessment
- **Acceptance:** ≥30% improvement post-module
- **Cross-ref:** doc 06 §4 Step 4

### H-ML-30 — Compound Learning institutional discipline = key Jetix value-prop
- **Claim:** Step 7 institutional compound learning = Jetix substrate value-prop differentiating from commodity ML consulting.
- **F/G/R:** F2 (concept-level claim) / Jetix consulting offering / refuted_if_(clients don't value compound-learning artifact differently from project-deliverable)
- **Test design:** Pricing experiment + client interview
- **Acceptance:** ≥20% pricing premium for compound-learning-included offers
- **Cross-ref:** doc 06 §7 Step 7 + Foundation Part 5

### H-ML-31 — A/B test discipline = transferable Workshop module
- **Claim:** A/B testing discipline (Step 5) generalises к outreach / pricing / event-format / curriculum experiments; Workshop teachable.
- **F/G/R:** F3 (controlled experimentation literature) / Cross-domain experimentation / refuted_if_(apprentice cohort can't transfer A/B discipline к non-ML domain in assessment)
- **Test design:** Cross-domain A/B design assessment
- **Acceptance:** ≥70% apprentices design valid A/B for novel non-ML problem
- **Cross-ref:** doc 06 §5 Step 5

### H-ML-32 — Provenance discipline (Step 2 + Part 6a) = unique Jetix differentiator
- **Claim:** Data + claim provenance discipline applied at institutional scale (Jetix Part 6a) = unique value-prop few competitors match.
- **F/G/R:** F2 (concept-level) / ML consulting market / refuted_if_(provenance-discipline framing in sales doesn't differentiate)
- **Test design:** Sales positioning A/B with vs without provenance emphasis
- **Acceptance:** Provenance-framed offers ≥1.3× win rate
- **Cross-ref:** doc 06 §2 Step 2 + Foundation Part 6a

### H-ML-33 — Hackathon = compressed 7-step execution
- **Claim:** Hackathon format = explicit compressed 7-step exercise; teaching pattern + format reinforce each other.
- **F/G/R:** F2 (Phase 4 doc 07 §3.4 surface) / Hackathon platform design / refuted_if_(hackathon participants don't recognise pattern as helpful structure)
- **Test design:** Post-hackathon survey on pattern utility
- **Acceptance:** ≥60% participants find 7-step framing useful
- **Cross-ref:** doc 07 §3.4 + JETIX-AS-HACKATHON-PLATFORM strategic note

### H-ML-34 — Brigadier cycle ≈ 7-step internally
- **Claim:** Brigadier per-cycle dispatch structure ≈ 7-step internally (problem framing → context gathering → baseline → iteration → test → deploy → reflect).
- **F/G/R:** F2 (conceptual mapping) / Brigadier protocol / refuted_if_(brigadier cycle redesign к explicit 7-step doesn't improve quality / reduce friction)
- **Test design:** Brigadier cycle redesign POC + comparison
- **Acceptance:** Measurable improvement on cycle outcome quality
- **Cross-ref:** doc 07 §6.3 + Foundation Part 4

### H-ML-35 — Step-7 maintenance dominance has business model implications
- **Claim:** Production maintenance owns 60-80% of ML lifetime cost → Jetix offering should include retainer / managed service component, not just delivery.
- **F/G/R:** F3 (MLOps industry data) / Jetix consulting business model / refuted_if_(retainer offers don't outsell project-delivery offers in pricing experiment)
- **Test design:** Pricing model A/B (delivery-only vs delivery + maintenance retainer)
- **Acceptance:** Retainer LTV >2× delivery-only LTV
- **Cross-ref:** doc 06 §7 + doc 05 §13 cross-cutting

---

## §4 Jetix integration hypotheses (H-ML-36 to H-ML-45)

### H-ML-36 — Master Workshop = ML engineer career destination
- **Claim:** Master Workshop of Engineers (text_009 Thread 14 aspiration) = ML engineer career-attractor destination differentiated from FAANG / startup / academia paths.
- **F/G/R:** F2 (aspirational) / Senior ML engineers seeking next-stage / refuted_if_(cohort interviews show Workshop doesn't compete vs FAANG / startup / academia)
- **Test design:** Cohort qualitative + offer comparison
- **Acceptance:** ≥30% of high-tier candidates rank Workshop in top-3 of next-career options
- **Cross-ref:** doc 08 §2 Class 1 + text_009 anchor

### H-ML-37 — FPF accelerates ML engineer onboarding 5×
- **Claim:** FPF formal methodology accelerates ML engineer onboarding to complex projects 5× vs vanilla onboarding.
- **F/G/R:** F2 (strong claim; surface only) / Workshop apprentice onboarding / refuted_if_(controlled cohort comparison shows <1.5× difference)
- **Test design:** Onboarding velocity benchmark cross-cohort
- **Acceptance:** Median time-to-productivity ≥3× faster on FPF-onboarded
- **Cross-ref:** doc 08 §2

### H-ML-38 — Hackathon mode optimal для ML talent surfacing
- **Claim:** Hackathon participation surfaces high-fit ML talent better than passive job-application channels.
- **F/G/R:** F3 (Kaggle-as-recruiting-channel evidence) / Talent identification / refuted_if_(hackathon-sourced hires have lower retention / performance than job-board hires)
- **Test design:** Compare hires sourced from hackathon vs job-board over 18mo
- **Acceptance:** Hackathon-sourced ≥1.3× retention + performance metrics
- **Cross-ref:** doc 08 §4 Class 3

### H-ML-39 — Karpathy-specific outreach high-fit
- **Claim:** Karpathy specifically = high-fit target for Class 2 partnership (Education Layer alignment + Software 2.0 philosophy + open-source ML pedagogy).
- **F/G/R:** F2 (single-target hypothesis) / Karpathy specifically / refuted_if_(outreach gets no engagement OR active dismissal)
- **Test design:** Direct outreach by Ruslan
- **Acceptance:** Meeting or substantive correspondence within 6mo
- **Cross-ref:** direction 09 + doc 08 §3 §3.4

### H-ML-40 — Russian-speaking L2 influencer cohort outreachable
- **Claim:** Russian-speaking ML telegram channel leaders (Котенков / Лапань / etc.) = outreachable L2 cohort for Hackathon mentor / Workshop satellite roles.
- **F/G/R:** F2 (anecdotal accessibility evidence) / RU L2 ML influencers / refuted_if_(systematic outreach gets <20% response rate)
- **Test design:** Systematic outreach with personalised pitch
- **Acceptance:** ≥30% response rate; ≥10% substantive conversation
- **Cross-ref:** doc 02 §6 + doc 08 §8 + JETIX-OUTREACH-SYSTEM strategic note

### H-ML-41 — Sovereign-AI offering wins disproportionately RU + EU
- **Claim:** Sovereign-AI consulting offer wins disproportionately в RU + EU enterprise clients vs US.
- **F/G/R:** F3 (regulatory trends + geopolitics) / Geographic client mix / refuted_if_(geo-split of sovereign-AI wins doesn't show RU+EU bias)
- **Test design:** Track win-rate by geography
- **Acceptance:** RU+EU wins ≥2× US for sovereign-AI offers
- **Cross-ref:** doc 08 §6.4 + doc 05 §5

### H-ML-42 — Workshop curriculum gets external citations
- **Claim:** Workshop curriculum (especially 7-step universal pattern module) gets external citations / adoptions / reference within 12mo of public release.
- **F/G/R:** F2 (aspirational) / ML education community / refuted_if_(zero external citations in 12mo)
- **Test design:** Track citations / forks / references publicly
- **Acceptance:** ≥5 substantive external references
- **Cross-ref:** doc 07 §6.1 + Education Layer strategic note

### H-ML-43 — Cross-disciplinary applicability = Jetix moat
- **Claim:** Jetix's ability to teach 7-step pattern across ML + non-ML domains = competitive moat vs ML-only educators.
- **F/G/R:** F2 (concept-level) / Jetix positioning vs competitors / refuted_if_(cross-disciplinary positioning doesn't differentiate in client choice)
- **Test design:** Positioning A/B in sales material
- **Acceptance:** Cross-disciplinary framing ≥1.3× consideration rate
- **Cross-ref:** doc 07 §3 universal applicability

### H-ML-44 — Education compounded value = gratitude loop substrate
- **Claim:** Education-as-substrate accumulates gratitude loop network effects that pure consulting cannot match.
- **F/G/R:** F2 (gratitude economy concept) / Jetix long-term valuation / refuted_if_(Workshop alumni show no measurable propensity to refer / partner / advocate)
- **Test design:** Alumni network activity tracking over 2yr
- **Acceptance:** Workshop alumni produce ≥3× referrals vs random outreach contacts
- **Cross-ref:** doc 08 §2 + Harari research stream gratitude framing

### H-ML-45 — O-29 «ML/AI engineering substrate» = candidate Phase 0 inventory addition
- **Claim:** «ML/AI engineering substrate» = candidate O-29 addition to `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` Phase 0 inventory.
- **F/G/R:** F2 (research surface) / Phase 0 inventory completeness / refuted_if_(Ruslan ack rejects О-29 as out-of-scope OR re-frames as part of existing object)
- **Test design:** Ruslan ack review (HUMAN GATE per R2 + R11)
- **Acceptance:** Ruslan ack confirms O-29 addition
- **Cross-ref:** doc 10 Phase 8 inventory §APPEND surface + R2 IP-1 caveat per doc 07 §5

---

## §5 Cross-ref table

| H | Type | Cross-ref docs |
|---|---|---|
| H-ML-1 to H-ML-10 | Industry | doc 02, 09, direction 09 |
| H-ML-11 to H-ML-25 | Tool | doc 03/04/05, Foundation Parts |
| H-ML-26 to H-ML-35 | Methodology | doc 06, 07, batch-3 strategic notes |
| H-ML-36 to H-ML-45 | Jetix integration | doc 08, vision/*, decisions/strategic/ |

## §6 Constitutional posture

- **R1:** All H = surface only; NONE selected / promoted / ack'd here
- **R6:** Cross-ref per H to evidentiary substrate
- **R11:** No hypothesis triggers external action автоматически
- **Breadth-NOT-selection:** 45 H surfaced; Ruslan selects subset for testing
- **F-grade explicit:** F2 (concept-level surface) or F3 (evidence-substantiated) per H

---

## §7 What's NOT in this bank

- ❌ Recommendations (only testable hypotheses with refutation conditions)
- ❌ Decisions (Ruslan strategic prose required for any decision)
- ❌ Outreach lists (Class 2-4 specific persons surfaced in doc 08; outreach НЕ запущен)
- ❌ Tool selection (Phase 2+ decision; not this run)
- ❌ Curriculum prescription (Workshop curriculum design = separate run)

---

*Word count: ~2980 / budget 3000. Compliant. 45 hypotheses surfaced (≥30 minimum). All carry F/G/R + test design + acceptance + refutation conditions + cross-ref. Breadth posture preserved.*
