---
title: Phase 2 — Refined taxonomy (beyond P/S/M/N → deeper sub-clusters)
date: 2026-05-24
phase: 2/7
parent_substrate: reports/book-driven-agents-2026-05-24/01-corpus-knowledge-domains.md + reports/research-corpus-pipeline-2026-05-24/phase-6-bucket-cross-mapping.md
constitutional_posture: R1 surface + R6 + IP-1 + append-only
prose_authored_by: brigadier-scribe (server CC autonomous)
density: MAX (§11.0 — taxonomy refinement = technical depth)
F: F2
G: book-driven-agents-phase-2
R: refuted_if_sub_cluster_assignment_orphans_books_OR_visualization_tree_inconsistent
---

# Phase 2 — Refined taxonomy

> Beyond Phase 6 4-bucket P/S/M/N → **17 sub-clusters** organized into 5 mega-clusters. Each sub-cluster = single-purpose knowledge domain mappable to a candidate agent or wiki. Mega-clusters serve cross-cluster coordination at brigadier level.

## §2.1 Method

**Input:** Phase 1 §1.A–§1.K per-book profiles (80 books) + §1.L lineage synthesis (8 candidate lineage clusters).

**Decomposition logic:**
- **Phase 6 4 buckets are HORIZONTAL (book-folder-of-origin oriented).** Useful for downstream research prompts but TOO COARSE for agent role design.
- **Refined sub-clusters are FUNCTIONAL (single-purpose knowledge domain).** Each sub-cluster = "what an agent would consult this for." Mapping is **many-to-many** (one book may seed 1-4 sub-clusters via different concepts).
- **Mega-clusters preserve Phase 6 hierarchy** for cross-bucket synthesis BUT are explicitly NON-EXCLUSIVE: a book can sit in multiple mega-clusters.

## §2.2 17 sub-clusters × 5 mega-clusters (full taxonomy)

### Mega-cluster I: INFLUENCE & RECRUITMENT (was Phase 6 P bucket — refined)

**SC1 — Propaganda Classical (mass-communication 1895-1965 substrate)**
- Books: Le Bon 1895 / Freud Group Psychology 1921 / Lippmann 1922 / Bernays 1923 + 1928 / Ellul 1965 (critical) / Chomsky-Herman 1988
- Defining axis: **mass-communication theory** of how publics are shaped via crowd psychology + media + symbolic substitution
- Key methods: PR campaign protocol; ambient-propaganda diagnostic; 5-filters propaganda model; group-leader cascade
- Provenance density: 6 books (5 P=3 + 1 P=3); ALL OCR-validated (Bernays ×2 + Le Bon + Freud Phase 2 Mistral; Chomsky-Herman + Ellul text-extract clean)
- Agent mapping: → **propaganda-expert** (Phase 3 candidate #1)

**SC2 — Cult & Mass-Movement Recruitment (totalism + true-believer dynamics)**
- Books: Hoffer 1951 / Lifton 1961 (8 criteria) / Hassan 1988 (BITE) / Henrich 2020 (cultural-evolution overlay)
- Defining axis: **recruitment-substrate analysis + diagnostic** for cultic/movement formation
- Key methods: BITE model; 8-criteria-thought-reform diagnostic; mass-movement substrate analysis; cumulative cultural intelligence overlay
- Provenance density: 4 books (3 P=3 + 1 P=2)
- Agent mapping: → **recruitment-dynamics-expert** (Phase 3 candidate #2)

**SC3 — Persuasion Tactics Catalog (Cialdini-Greene-Heath canon)**
- Books: Cialdini 1984 (+ RU duplicate) / Cialdini 2016 / Greene 1998 / Heath 2007 / Berger 2013 / Eyal 2014
- Defining axis: **named-pattern catalogs** for persuasion and influence tactics
- Key methods: 6 principles (Cialdini) + 7th unity / 48 laws (Greene) / SUCCES (Heath) / STEPPS (Berger) / Hook model (Eyal)
- Provenance density: 6 books (5 P=3 + 1 P=3); Cialdini RU = duplicate flag retained
- Agent mapping: → **persuasion-tactics-expert** (sub-specialty; could merge into propaganda OR influence-ethics depending on Ruslan preference Phase 3)

**SC4 — Community & Tribe Formation (movement-design methodology)**
- Books: Godin Permission Marketing 1999 / Godin Tribes 2008 / Raymond Cathedral 1999 / Srinivasan Network State 2022
- Defining axis: **tribe/community formation as methodology** (cohort recruitment ≠ persuasion but adjacent)
- Key methods: permission-ladder; tribe-design protocol (3 things); bazaar development; 7-step network-state recipe
- Provenance density: 4 books (3 P=3 + 1 P=2)
- Agent mapping: → component of **recruitment-dynamics-expert** OR standalone **community-formation-expert** (Phase 3 candidate variant)

**SC5 — Behavioral Foundations Cross-Cluster (System 1/2 + WEIRD overlay)**
- Books: Kahneman 2011 (P+S+M cross) / Henrich 2020 (also in SC2) / Csikszentmihalyi Flow 1990 (also in SC11)
- Defining axis: **cross-cluster cognitive/behavioral substrate** underlying influence + game design + methodology
- Key methods: dual-process model; cognitive bias catalog; cross-cultural comparison; flow-state design
- Provenance density: 3 books spanning multiple mega-clusters
- Agent mapping: → consulted by multiple agents (propaganda-expert / nlp-expert / influence-ethics-expert / gamification); foundational cross-reference; NOT its own agent

### Mega-cluster II: NLP & VERBAL-REFRAMING (was Phase 6 N bucket — refined)

**SC6 — NLP Foundational Canon (Bandler-Grinder origin)**
- Books: Bandler-Grinder Structure of Magic 1975 / Frogs into Princes 1979 / Trance-formations 1981 / Reframing 1982
- Defining axis: **origin canon NLP** + Ericksonian hypnosis substrate
- Key methods: meta-model (12-14 patterns); Milton-model (12+ patterns); 6-step reframing; modeling protocol
- Provenance density: 4 books (all N=3 + P=3 on 3/4)
- Agent mapping: → core of **nlp-expert** (Phase 3 candidate #3)

**SC7 — NLP Encyclopedia + Verbal-Reframing Extensions (Dilts + Andreas extensions)**
- Books: Dilts Encyclopedia 2000 (1724pp) / Dilts Sleight-of-Mouth 1999 / Andreas Heart of the Mind 1989 / Andreas-Faulkner New Tech Achievement 1996 / O'Connor-Seymour 1990
- Defining axis: **systematic extension** of NLP — Logical Levels (Bateson lineage) + 14 sleight patterns + practitioner primers
- Key methods: Logical Levels; SCORE model; 14 sleight-of-mouth patterns; submodalities; well-formed-outcomes
- Provenance density: 5 books (all N=3)
- Agent mapping: → extension of **nlp-expert** (consulted in advanced cases)

**SC8 — NLP Commercialization + Communication-Adjacent (Robbins + Bolton)**
- Books: Robbins Unlimited Power 1986 / Robbins Awaken Giant 1991 / Bolton People Skills 1979
- Defining axis: **mass-market + communication-skills** NLP-adjacent literature
- Key methods: NAC (Robbins) / state-management / 3-part I-message (Bolton) / active listening
- Provenance density: 3 books (all N=2)
- Agent mapping: → consulted by **nlp-expert** but lower-priority (commercialization layer)

### Mega-cluster III: PHILOSOPHY OF SCIENCE & SOTA TRACKING (was Phase 6 S phil-sci subset — refined)

**SC9 — Falsificationism + Paradigm Theory (Popper-Kuhn-Lakatos-Feyerabend quartet)**
- Books: Popper Logik der Forschung 1934 / Conjectures & Refutations 1963 / Kuhn Structure 1962 / Lakatos Programmes 1978 / Feyerabend Against Method 1975 / Laudan Progress 1977 / Chalmers textbook 1976
- Defining axis: **canonical phil-sci debate** — falsifiability / paradigms / research programmes / anarchism / problem-solving
- Key methods: falsification protocol; paradigm-shift analysis; hard-core/protective-belt; counter-induction; problem-solving progress audit
- Provenance density: 7 books (all S=3 + 6 with M=2-3)
- Agent mapping: → **sota-tracker-expert** (Phase 3 candidate #4); philosophy-expert continues to consult on epistemic-audit lens; sota-tracker = method-of-tracking-the-field

**SC10 — Social + Tacit Epistemology (Polanyi-Longino-Hacking pragmatism)**
- Books: Polanyi Personal Knowledge 1958 / Tacit Dimension 1966 / Longino Fate of Knowledge 2002 / Hacking Representing & Intervening 1983 / Menand pragmatism 1997 / Merleau-Ponty 1942
- Defining axis: **social + tacit + experimental** epistemology (NOT the falsifiability quartet)
- Key methods: tacit-explicit dialectic; transformative-criticism criteria; entity-realism; pragmatic inquiry; phenomenological reduction
- Provenance density: 6 books
- Agent mapping: → consulted by **sota-tracker-expert** + **philosophy-expert** (already-existing ROY agent); foundational complement to SC9

### Mega-cluster IV: METHODOLOGY ENGINEERING (was Phase 6 M bucket — refined)

**SC11 — Heuristic Problem-Solving (Polya canon)**
- Books: Polya How to Solve It 1945 / Lakatos Proofs & Refutations adjacency (1976 — not in 80, but Polya direct lineage to Lakatos)
- Defining axis: **named-heuristic-catalog methodology** for problem-solving
- Key methods: Polya 4-step plan; heuristic dictionary (80+ entries); analogy reasoning; working-backward
- Provenance density: 1 book core (Polya) + cross-reference Lakatos hard-core/protective-belt
- Agent mapping: → core component of **methodology-engineer** (Phase 3 candidate #5)

**SC12 — Method-as-Discipline / Method Engineering (Schön-Levenchuk-OMG Essence)**
- Books: Schön Reflective Practitioner 1987 / OMG Essence v1.1 2015 / Levenchuk Метод 2025 / Sistemnoe Myishlenie т.1+т.2 2024 / Intellekt-Stek 2023 / Injeneriya Lichnosti / Senge Fifth Discipline SUMMARY 1990 / Visual Toolbox Climate-KIC 2016
- Defining axis: **method as engineered artefact** — alphas / states / way-of-working / reflective-practicum / facilitation toolkit
- Key methods: OMG Essence kernel (7 alphas); Levenchuk method-engineering protocols; reflective-practicum; system-thinking textbook protocol; visual-facilitation patterns
- Provenance density: 8 books (Levenchuk dominant — 5 books, all M=3)
- Agent mapping: → core of **methodology-engineer** (Phase 3 candidate #5)

**SC13 — Russian СМД + MMK Substrate (Shchedrovitsky lineage)**
- Books: 17.pdf = Shchedrovitsky vol-17 / cross-reference Levenchuk explicit MMK acknowledgement
- Defining axis: **Soviet/Russian methodology school** — мыследеятельность + ОД-игры + рефлексия
- Key methods: ОД-игра (organizational-activity-game); thinking-doing schema; reflexive method
- Provenance density: 1 book core (17.pdf) + Levenchuk 5 books cite explicitly
- Agent mapping: → consulted by **methodology-engineer** + **levenchuk-deep-dive-brigadier** (existing stub) for Russian-language users; cross-cultural complement

**SC14 — Software Engineering Method Canon (Dijkstra-Knuth-google-SRE-Young CQRS)**
- Books: Dijkstra Short Intro 1969 / Knuth TAOCP vol2 1969 / google-sre-book / Young CQRS 2010
- Defining axis: **SE-specific methodology** — structured programming + algorithmics + reliability + event-driven architecture
- Key methods: weakest-precondition calculus; literate programming; SLO/SLI/error-budget; CQRS pattern
- Provenance density: 4 books
- Agent mapping: → consulted by **engineering-expert** (already-existing ROY agent — coverage gap noted but engineering-expert already covers); NOT a new agent (existing coverage adequate)

### Mega-cluster V: ML/AI + GAME THEORY + GAMIFICATION (was Phase 6 S-DL subset + K gamification — refined)

**SC15 — ML/AI Foundations + SOTA**
- Books: Goodfellow Deep Learning 2016 / Huyen Designing ML Systems 2022 / arxiv qian-scaling-laws / cemri-mast-failure-modes / kim-multi-agent-scaling
- Defining axis: **ML/AI canonical knowledge** + multi-agent system scaling research
- Key methods: DL curriculum; MLOps lifecycle; MAS scaling protocols; failure-mode taxonomy
- Provenance density: 5 books (all S=3); 3 arxiv MAS papers are recent (2024-2025)
- Agent mapping: → **ml-ai-foundations-expert** (Phase 3 candidate #6)

**SC16 — AI Safety + Alignment Methodology (Askell-Bai constitutional + Jetix Pillar C kinship)**
- Books: Askell HHH 2021 / Bai Constitutional AI 2022
- Defining axis: **AI alignment methodology** — HHH triad / RLAIF / constitutional principle scaffolding
- Key methods: HHH evaluation protocol; CAI training pipeline (SL + RL with principles); critique-revise loop
- Provenance density: 2 books — but **directly informs** Pillar C Tier 2 architecture (HHH triad explicitly cited в Tier 2 corrigibility per Bundle 1)
- Agent mapping: → **ai-safety-alignment-expert** (Phase 3 candidate variant; could merge with ml-ai-foundations OR standalone given Jetix Pillar C kinship)

**SC17 — Game Theory + Game Design + Virtual Economies**
- Books: Schelling Strategy of Conflict 1960 / Axelrod Evolution of Cooperation 1984 / Csikszentmihalyi Flow 1990 / Koster Theory of Fun 2004 / Salen-Zimmerman Rules of Play 2003 / Rouse 2004 / Rogers Level Up 2010 / Schell Lenses / Castronova Synthetic Worlds 2005 / Lehdonvirta-Castronova Virtual Economies 2014 / Varoufakis Technofeudalism 2023 / Eyal Hooked 2014 (also SC3)
- Defining axis: **game-as-system** — strategic interaction + design discipline + virtual-economy design + platform critique
- Key methods: Schelling-point identification; tit-for-tat; flow-state design; lens-by-lens audit; faucet-sink balance; rentier-economy diagnostic
- Provenance density: 12 books (with 1 cross to SC3 Eyal)
- Agent mapping: → **gamification-engagement-expert** (Phase 3 candidate variant; consider Ruslan strategic decision — could merge with influence-ethics-expert at boundary OR with crypto-economic substrate for Jetix gamification project)

## §2.3 Cross-cluster boundary cases (R12 + IP-1 implications)

| Boundary case | Books touched | Concern | Resolution proposal |
|---|---|---|---|
| **NLP (SC6-8) ↔ Cult-Recruitment (SC2)** | Bandler-Grinder Trance-formations 1981 + Hassan BITE 1988 + Lifton 1961 | NLP "covert hypnosis" patterns explicitly used в cult recruitment per Hassan diagnostic | Phase 3 **nlp-expert** REQUIRES paired-frame check via **influence-ethics-expert** OR shared R12-guardrail (analogous to swarm-protocol §X) |
| **Persuasion-Tactics (SC3) ↔ Recruitment (SC2)** | Cialdini 6 principles + Hoffer recruitment + Greene 48 laws | Greene 48 laws explicitly amoral; Cialdini explicitly distinguishes ethical/unethical use; Hoffer descriptive | Phase 3 **persuasion-tactics-expert** EITHER merges with propaganda-expert OR pairs with influence-ethics-expert for R12 paired-frame discipline |
| **Game-Design (SC17) ↔ Persuasion (SC3)** | Eyal Hooked 2014 + Schell Lenses (engagement design) + Csikszentmihalyi Flow (state mgmt) | Hook model explicitly persuasion engineering for products; Eyal himself authored "manipulation matrix" for ethics; gamification can extract per R12 boundary | Phase 3 **gamification-engagement-expert** carries R12 boundary check; paired-frame with influence-ethics-expert |
| **SOTA-Tracker (SC9) ↔ Existing philosophy-expert** | Popper-Kuhn-Lakatos-Feyerabend quartet (already philosophy-expert lens per CLAUDE.md ROY swarm table) | Philosophy-expert ALREADY covers epistemology + mental models per existing system.md | Phase 3 explicit IP-1 split: philosophy-expert = **epistemic-audit + first-principles reset** (mode focus); sota-tracker = **method discipline for tracking field state** (different cell — instrumental rationality of staying current vs evaluative rationality of audit) |
| **Methodology-Engineer (SC11-14) ↔ Existing systems-expert + mgmt-expert** | OMG Essence + Levenchuk + Senge + Schön → SE method engineering | Systems-expert covers cybernetics; mgmt-expert covers delivery; method-engineering ≠ either | Phase 3 IP-1 split: methodology-engineer = **method-as-engineered-artefact**, complementary to systems-expert + mgmt-expert; new cell |
| **Levenchuk corpus (5 books all M=3)** | sistemnoe-myishlenie ×2 + metodologiya + intellekt-stek + injeneriya-lichnosti | Existing **levenchuk-deep-dive-brigadier** is STUB (P3 deferred per file header) | Phase 3 propose **methodology-engineer = canonical Levenchuk-corpus consumer**; levenchuk-deep-dive-brigadier remains stub until SG-4 promotion (per /project-bootstrap §8) |

## §2.4 Visualization tree (ASCII)

```
80-BOOK CORPUS
├── I. INFLUENCE & RECRUITMENT (mega-cluster I, was P bucket)
│   ├── SC1 — Propaganda Classical (6 books)         → propaganda-expert
│   ├── SC2 — Cult & Mass-Movement Recruitment (4)   → recruitment-dynamics-expert
│   ├── SC3 — Persuasion Tactics Catalog (6)         → persuasion-tactics-expert OR merge
│   ├── SC4 — Community & Tribe Formation (4)        → component of recruitment-dynamics-expert
│   └── SC5 — Behavioral Foundations cross (3)       → consulted-cross (no own agent)
│
├── II. NLP & VERBAL-REFRAMING (mega-cluster II, was N bucket)
│   ├── SC6 — NLP Foundational Canon (4)             → nlp-expert (core)
│   ├── SC7 — NLP Encyclopedia + Extensions (5)      → nlp-expert (advanced)
│   └── SC8 — NLP Commercialization (3)              → nlp-expert (low-priority)
│
├── III. PHILOSOPHY OF SCIENCE & SOTA (mega-cluster III, was S phil-sci subset)
│   ├── SC9 — Falsificationism + Paradigm (7)        → sota-tracker-expert (+ philosophy-expert existing)
│   └── SC10 — Social + Tacit Epistemology (6)       → cross-consulted (philosophy-expert + sota-tracker)
│
├── IV. METHODOLOGY ENGINEERING (mega-cluster IV, was M bucket)
│   ├── SC11 — Heuristic Problem-Solving (Polya)     → methodology-engineer
│   ├── SC12 — Method-as-Discipline (Schön/Levenchuk/OMG Essence/Senge/Climate-KIC) (8) → methodology-engineer (core)
│   ├── SC13 — Russian СМД + MMK (1+Levenchuk cross) → methodology-engineer + levenchuk-deep-dive-brigadier stub
│   └── SC14 — SE Method Canon (Dijkstra/Knuth/SRE/CQRS) (4) → engineering-expert (existing — no new agent)
│
└── V. ML/AI + GAME THEORY + GAMIFICATION (mega-cluster V, was S-DL subset + K gamification)
    ├── SC15 — ML/AI Foundations + SOTA (5)          → ml-ai-foundations-expert
    ├── SC16 — AI Safety + Alignment (Askell+Bai)    → ai-safety-alignment-expert (variant)
    └── SC17 — Game Theory + Game Design + Virtual Econ (12) → gamification-engagement-expert (variant)
```

## §2.5 Aggregate counts verification

| Mega-cluster | Sub-clusters | Books (counted, with multi-cluster overlaps marked) |
|---|---|---|
| I. INFLUENCE & RECRUITMENT | 5 (SC1-SC5) | SC1(6) + SC2(4) + SC3(6, with 1 duplicate) + SC4(4) + SC5(3 cross) = 23 unique books w/ cross-refs |
| II. NLP & VERBAL-REFRAMING | 3 (SC6-SC8) | SC6(4) + SC7(5) + SC8(3) = 12 books (matches Phase 6 N bucket exactly) |
| III. PHIL-SCI & SOTA | 2 (SC9-SC10) | SC9(7) + SC10(6) = 13 books unique |
| IV. METHODOLOGY ENGINEERING | 4 (SC11-SC14) | SC11(1) + SC12(8) + SC13(1+cross) + SC14(4) = 14 books unique |
| V. ML/AI + GAMING + GAMIFICATION | 3 (SC15-SC17) | SC15(5) + SC16(2) + SC17(12, with 1 cross to SC3) = 19 books unique |

**Total unique books mapped across sub-clusters:** ~80 (matches Phase 6) with some books in 2-4 sub-clusters (e.g., Kahneman in SC3 + SC5; Eyal in SC3 + SC17; Henrich in SC2 + SC5)

## §2.6 Constitutional check Phase 2

- **R1:** All taxonomy claims = technical synthesis, не strategic. Strategic choices (which agents to create, names, scopes) DEFERRED to Phase 3 surface + Phase 6 packet + Ruslan ack
- **R6:** Each sub-cluster carries explicit book list with [src:] paths via Phase 1 backreferences
- **R12:** Boundary cases §2.3 explicitly flagged for paired-frame discipline (NLP↔Cult; Persuasion↔Recruitment; Gamification↔Persuasion)
- **IP-1:** Sub-cluster → agent mapping uses role-archetype slugs (kebab-case, abstract role-type), не executor-instance names. Phase 4 will preserve at system.md draft level.

## §2.7 Phase 2 closure

- 17 sub-clusters × 5 mega-clusters identified ✅
- ASCII visualization tree provided ✅
- Cross-cluster boundary cases (R12 + IP-1) flagged ✅
- Aggregate count consistent with Phase 6 ✅
- 6-7 primary agent candidates emergent (Phase 3 will formalize): propaganda-expert + recruitment-dynamics-expert + nlp-expert + sota-tracker-expert + methodology-engineer + ml-ai-foundations-expert + (variants: persuasion-tactics / community-formation / ai-safety-alignment / gamification-engagement / influence-ethics)

**Next:** Phase 3 — agent topology design (5-10 NEW ROY candidates proposed; R1 surface only).

---

*Phase 2 closure 2026-05-24. Refined taxonomy preserves Phase 6 bucket invariant while enabling cleaner agent-domain mapping. R12 paired-frame discipline scaffolded for boundary cases. Phase 3 surfaces options for Ruslan.*
