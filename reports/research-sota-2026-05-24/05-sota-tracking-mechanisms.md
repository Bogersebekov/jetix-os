---
title: Phase 5 — SOTA-Tracking Mechanisms
date: 2026-05-24
phase: 5
parent_prompt: prompts/research-sota-2026-05-24.md
F: F2-F3
G: research-sota-phase-5
R: refuted_if_lt_8_mechanisms_decoded_OR_R1_strategic_prose_authored
constitutional_posture: R1 surface only + R6 provenance per claim + EP-5 + AP-6 + append-only
prose_authored_by: brigadier-scribe (Server CC autonomous)
language: russian primary
sources_count: substrate cross-pull (5 traditions × 9 mechanisms) — 20 inline citations + cross-references
---

# Phase 5 — SOTA-Tracking Mechanisms: как сообщества знают что SoTA

> **Анкер задачи:** decode operational mechanisms через которые сообщества identify, validate, replace SoTA — peer review, preprints, benchmarks, replication, community curation. **Это «как именно работает» дополнение к «что такое» (phases 1-4).**

---

## §1 Зачем mechanisms separately?

Phases 1-4 decoded **what SoTA is** (philosophically + Левенчуковски + ML-style). Phase 5 — **как community operationally knows**:

- Не один человек объявляет SoTA → весь field признаёт
- Существует **процесс validation + selection + retirement**
- Этот процесс ≠ единая структура — это **assemblage of mechanisms**
- Каждый mechanism имеет свои biases + failure modes

8 mechanisms (одна — meta) decoded ниже. Каждое — через lens (1) operational, (2) bias/failure, (3) применимо к Jetix.

---

## §2 Mechanism 1 — PEER REVIEW

### §2.1 Operational

| Step | Action |
|---|---|
| 1 | Researcher submits manuscript to journal/conference |
| 2 | Editor finds 2-3 anonymous reviewers (domain experts) |
| 3 | Reviewers provide written critique + recommendation |
| 4 | Author revises + resubmits |
| 5 | Editor decides accept/reject/major revision |
| 6 | Published — formal "in record" |

### §2.2 Connection to SoTA

- Peer review = **institutional validation of SoTA-claim**
- Published paper = "this passes minimum bar для consideration as SoTA"
- Citation rate (post-publication) = community uptake = additional SoTA-validation

### §2.3 Biases / failures

| Bias | Description |
|---|---|
| Slow | Median 6-18 months to publication; SoTA-claims age while in review |
| Conservative | Novel claims often rejected by paradigm-bound reviewers (Kuhnian — Phase 2 §3) |
| Network effect | Established names get easier reviews |
| Reproducibility crisis | Pass peer review ≠ result replicable (Longino's "uptake" norm fails) |
| Replication papers undervalued | "New result" preferred over "confirms previous" |

### §2.4 Phil-sci frame

- Popperian: peer review = institutional check against unfalsifiable claims
- Kuhnian: peer review enforces paradigm boundaries
- Longinosian: implements **norm 1 (venues for criticism)** + **norm 2 (uptake)**

### §2.5 Jetix-application

- Wiki page promotion: F2 → F3 requires "reviewer = ROY expert + Provenance Officer"
- Cycle pre-commit hook checks F-G-R discipline
- Не классическое peer review — это **institutional Longino + Hacking instrumental check**

---

## §3 Mechanism 2 — PREPRINTS (arXiv, bioRxiv, SSRN)

### §3.1 Operational

| Step | Action |
|---|---|
| 1 | Researcher uploads manuscript to arXiv (no peer review) |
| 2 | DOI + version stamping assigned |
| 3 | Community can read immediately |
| 4 | Comments + critique через external channels (Twitter, blogs) |
| 5 | Author may revise (v1, v2, v3 versioned) |
| 6 | Often submitted to journal/conference separately later |

### §3.2 Connection to SoTA

- **Speed:** SoTA-claim available days после writing, не months
- **Versioning:** Левенчуковский year-stamp natively expressed (`arxiv.org/abs/2401.12345v3`)
- **Community-first validation** (vs editor-first in peer review)
- **Hugging Face / GitHub** часто linked → reproducibility check at preprint time

### §3.3 Biases / failures

| Bias | Description |
|---|---|
| No filter | Bad/wrong claims pollute feed |
| Hype-amplification | Twitter-virality > scientific quality |
| Pre-print "SoTA" claims часто не reproduce |
| ML community: SOTA-leapfrogging arms race |
| Status-seeking → benchmark-cherry-picking |

### §3.4 Phil-sci frame

- Feyerabendian: arXiv = "anything goes" — pluralism enabled
- Longinosian: norm 1 (venue) operational; norm 2 (uptake) varied
- Lakatosian: progressive vs degenerating programmes visible faster

### §3.5 Jetix-application

- Wiki `pipeline: ingested` ≈ preprint status (unreviewed, available)
- `pipeline: linted` ≈ reviewer-checked
- `pipeline: ready` ≈ peer-review accepted
- F-G-R discipline → preprint stage = F2-F3

---

## §4 Mechanism 3 — BENCHMARKS (leaderboards)

### §4.1 Operational

| Step | Action |
|---|---|
| 1 | Community curates canonical task + dataset |
| 2 | Held-out test set (with answers hidden) |
| 3 | Researchers submit predictions + code |
| 4 | Automated evaluation produces score |
| 5 | Public leaderboard ranks entries |
| 6 | "SoTA" = top entry on leaderboard (per metric) |

### §4.2 Connection to SoTA

- **Most operational SoTA-mechanism** в ML — leaderboard literally calls top "SOTA"
- **Quantitative comparison** unique to benchmarks (vs qualitative peer review)
- **Time-stamped progression** visible
- Phase 4 §5 PWC detailed

### §4.3 Biases / failures (already partly covered Phase 4)

| Bias | Description |
|---|---|
| Benchmark saturation | After many attempts, scores converge near ceiling |
| Test set leakage | Direct/indirect leakage into training |
| Single-metric tunnel | Optimisation toward metric, away from real-world utility |
| Cost-blind | Compute / inference cost not in leaderboard |
| Benchmark-rot | Old benchmarks irrelevant for new problems |

### §4.4 Phil-sci frame

- Popperian: benchmark = falsification test (most explicit operational form)
- Hacking: experimental instrument стабильный across paradigms
- Goodhart's law (cited Левенчуком 1794653:159): metric becomes target → distortion

### §4.5 Jetix-application

- Wiki `comparisons/` cluster может функционировать как Jetix-internal benchmark
- E.g. "5 methodology composition variants × 6 evaluation criteria" matrix
- Method V2 §J meta-method comparison evaluations = benchmark-like

---

## §5 Mechanism 4 — REPLICATION (independent verification)

### §5.1 Operational

| Step | Action |
|---|---|
| 1 | Original SoTA-claim published |
| 2 | Independent team attempts to reproduce |
| 3 | If reproduces → confirmation |
| 4 | If fails to reproduce → published replication-failure |
| 5 | Original claim downgraded или retracted |

### §5.2 Connection to SoTA

- **Strongest validation of SoTA-status** — survives independent test
- Longino norm 2 (uptake) operationalised
- Hacking experimental-realism: "if can reproduce, real"

### §5.3 Biases / failures

| Bias | Description |
|---|---|
| Replication-crisis | Many published results don't replicate (psychology, medicine, sometimes ML) |
| Publication bias | Successful replications boring → unpublished |
| Cost of replication | Often expensive (compute, materials) → underdone |
| File-drawer effect | Failed replications never see light |

### §5.4 Phil-sci frame

- Popperian: replication = falsification test repeated
- Longinosian: norm 4 (tempered equality) — replication needs access to original
- Laudanian: replication = problem-solving expansion (more confirmed problems)

### §5.5 Jetix-application

- Methodology compositions applied к real partner-clan → replication?
- Wiki `experiments/` cluster — could log "we replicated X tactic with Y partner, result Z"
- Currently weak — Jetix substrate has limited replication discipline (Phase 7 gap)

---

## §6 Mechanism 5 — COMMUNITY CURATION (wikis, awesome-lists, blogposts)

### §6.1 Operational

| Step | Action |
|---|---|
| 1 | Curator (sometimes pseudonymous) maintains list/wiki |
| 2 | Community submits additions (PRs to awesome-lists, wiki edits) |
| 3 | Curator filters + organises |
| 4 | Updated continuously vs annual publication |
| 5 | Reputation of curator → trust of list |

### §6.2 Connection to SoTA

- **Survey-level SoTA** — "what's the current best for X" answered by curated list
- Wikipedia's "State of the art in X" sections sometimes
- Awesome-* GitHub lists (awesome-deep-learning, awesome-machine-learning)
- LessWrong sequences / Astral Codex Ten / Karpathy posts → SoTA pedagogical curation

### §6.3 Biases / failures

| Bias | Description |
|---|---|
| Curator bias | Single perspective shapes list |
| Update lag | Even continuous curation can fall behind |
| Centralisation risk | If curator stops, list fossilises |
| Quality opaque | "Curator says SoTA" — no formal validation |
| Status-amplification | Inclusion in popular list → reputation feedback loop |

### §6.4 Phil-sci frame

- Longinosian: norm 3 (public standards) — IF curator transparent about criteria
- Feyerabendian: pluralism if multiple competing lists
- Kuhnian: paradigm-bound — list embodies curator's paradigm

### §6.5 Jetix-application

- `swarm/wiki/topics/` indices = community-curated SoTA-style lists per topic
- `crm/_schema/strategy-hooks.yaml` = curated SoTA-tactics list
- 6 niche slices (personal/business/sales/life/tech/meta) — niche-specific SoTA-curation
- Karpathy LLM Wiki pattern (Phase 4 §4) = canonical Jetix wiki precedent

---

## §7 Mechanism 6 — CONFERENCES + WORKSHOPS

### §7.1 Operational

| Step | Action |
|---|---|
| 1 | Annual conference (NeurIPS, ICML, KDD) |
| 2 | Paper acceptance → presentation slot |
| 3 | Best Paper Awards highlight SoTA-claimants |
| 4 | Workshops focus narrow areas |
| 5 | Hallway conversations + posters propagate consensus |
| 6 | Community "feels" what's SoTA через atmosphere |

### §7.2 Connection to SoTA

- **Synchronisation point** для field (Kuhnian "what is normal science")
- **Hallway test:** if everyone at NeurIPS talks about X, X = SoTA candidate
- **Award signals** authoritative SoTA-validation

### §7.3 Biases / failures

| Bias | Description |
|---|---|
| Annual cadence | Slower than preprints |
| Geography bias | In-person attendance correlates with status |
| Industry sponsorship → topic-bias |
| Best Paper awards politicised |
| Workshop community can echo-chamber |

### §7.4 Phil-sci frame

- Kuhnian: conferences = paradigm-maintenance ritual
- Longinosian: norms 1 + 2 (venues + uptake) |
- Tempered equality fails: travel cost gates participation

### §7.5 Jetix-application

- Jetix internal "cycles" (cyc-foundation-build, cyc-km-materialization) функционируют как conferences
- Cycle output = "Best Paper" equivalent (canonical promotion)
- HITL Stage Gate = peer review ритуал

---

## §8 Mechanism 7 — CITATION ANALYSIS + BIBLIOMETRICS

### §8.1 Operational

| Step | Action |
|---|---|
| 1 | Paper cited by others (Google Scholar, Semantic Scholar) |
| 2 | High citation count → influential |
| 3 | h-index, impact factor, altmetrics |
| 4 | Top-cited papers in area = SoTA-canon retroactively |

### §8.2 Connection to SoTA

- **Lagging indicator** — citations accumulate over years
- **Robust к benchmark-gaming** — citations harder to fake
- **Community consensus marker** — many independent reads + uses

### §8.3 Biases / failures

| Bias | Description |
|---|---|
| Citation lag | Top SoTA today won't have citations yet |
| Citation cartels | Mutual citation rings inflate |
| English-bias | Non-English work undercited |
| Old work over-cited (Matthew effect) |
| Negative citation counted same as positive |

### §8.4 Phil-sci frame

- Laudanian: citations = community problem-solving uptake
- Longinosian: norm 2 (uptake) measured |
- Feyerabendian critique: bibliometrics measure conformity not truth |

### §8.5 Jetix-application

- Internal wiki cross-refs (`[[concept-name]]`) = Jetix citation pattern
- `wiki/graph/edges.jsonl` typed edges = citation network
- Top-referenced wiki concepts = Jetix internal SoTA

---

## §9 Mechanism 8 — STANDARDS BODIES (ISO, ANSI, IEEE, W3C)

### §9.1 Operational

| Step | Action |
|---|---|
| 1 | Stakeholders form working group |
| 2 | Draft standard developed iteratively |
| 3 | Public comment periods |
| 4 | Final approval voting |
| 5 | Published standard — "what compliant systems do" |
| 6 | Periodically updated |

### §9.2 Connection to SoTA

- **Officially endorsed SoTA** per industry/community
- Левенчук §14 phase 1: "Стандарты конкурируют за то, чтобы быть SoTA"
- BUT: Левенчук §7 phase 1: standards often LAG SoTA by years

### §9.3 Biases / failures

| Bias | Description |
|---|---|
| Slow process | 5-10 year cycles |
| Politicised — large players dominate |
| Lowest-common-denominator (compromise) |
| Lag behind cutting-edge |
| Replaced standards still in industry use |

### §9.4 Phil-sci frame

- Kuhnian: standards = explicit paradigm definition
- Lakatosian: compete as research-programme protective belts
- Lagging-SoTA Левенчуковский pattern

### §9.5 Jetix-application

- `decisions/` LOCKED docs = Jetix internal "standards"
- Foundation Architecture v1.0 LOCKED 2026-04-28 = constitutional standard
- F-G-R / Default-Deny / Halt-Log-Alert = schema standards
- Mirror standards-process: HITL Stage Gate = approval voting analog

---

## §10 Mechanism 9 (meta) — INSTITUTIONAL MEMORY / META-RESEARCH

### §10.1 Operational

| Step | Action |
|---|---|
| 1 | Periodic survey-of-surveys papers (Annual Reviews) |
| 2 | Living documents (Wikipedia, awesome-lists) |
| 3 | History-of-X books (e.g. Goodfellow Ch.1) |
| 4 | Retrospective conferences (10-year revisit of paradigm-shifting paper) |
| 5 | Replication-of-classics initiatives |

### §10.2 Connection to SoTA

- **Meta-SoTA**: what is current consensus about how SoTA evolved
- Connect новые SoTA-claim к historical trajectory (Lakatos progressive)
- Surface "forgotten SoTA" (Левенчук §16: SoTA рассыпан по индустрии)

### §10.3 Biases / failures

| Bias | Description |
|---|---|
| Survey papers bias toward authors' perspective |
| Wikipedia edit wars in active areas |
| History-textbook simplification |
| Forgotten work stays forgotten |

### §10.4 Phil-sci frame

- Laudanian: history reveals problem-solving trajectory
- Longinosian: collective historical narrative-formation
- Chalmers (Phase 3 §4) = textbook = exactly this mechanism

### §10.5 Jetix-application

- `archive/INDEX.md` + `swarm/wiki/cycles/_index.md` = Jetix institutional memory
- `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` = retrospective survey
- canonical/INDEX.md = current consensus state

---

## §11 9-Mechanism Comparison Matrix

| Mech | Speed | Cost | Authority | Bias-risk | Jetix-applicability |
|---|---|---|---|---|---|
| 1 Peer review | Slow | Medium | High | Conservative | partly (HITL) |
| 2 Preprints | Fast | Low | Low | Hype | strong (wiki `ingested`) |
| 3 Benchmarks | Fast | High (compute) | High | Goodhart | medium (comparisons cluster) |
| 4 Replication | Slow | High | Highest | Crisis | weak (gap — Phase 7) |
| 5 Community curation | Medium | Low | Medium | Curator | strong (topics/) |
| 6 Conferences | Slow | High | High | Geography | medium (cycles) |
| 7 Citations | Slow (lag) | Low | High (eventually) | Lag | strong (wiki edges) |
| 8 Standards | Very slow | High | Highest (compliance) | Lag | strong (LOCKED) |
| 9 Meta-research | Slow | Medium | Medium | Author-bias | medium (archive) |

---

## §12 Connection to substrate cross-pull

### §12.1 Cybernetic SoTA-tracking (DR-40 line)

Cybernetic external-system pattern: **feedback-from-outside = SoTA-tracking mechanism**. Ashby requisite variety: external observers с different variety detect failure modes invisible internally.

| Cybernetic concept | SoTA-tracking imp |
|---|---|
| Variety amplification | Multiple observer perspectives → richer SoTA-judgement |
| Negative feedback | Failed predictions force update |
| Variety mismatch | Internal SoTA-claim ≠ external SoTA → revision |
| Black-box probing | Benchmark = probing experiment |
| Beer VSM System 4 | "Outside + future" observation = SoTA tracking |

### §12.2 Complexity science (Mitchell + Beinhocker)

- Complex adaptive systems: SoTA emerges, not designed top-down
- Beinhocker: economic SoTA = best business strategies extracted from competition
- Selection pressure → SoTA filtering
- **Связь с Lakatos progressive programmes:** market selection = institutional progressive shift test

### §12.3 Karpathy LLM Wiki precedent

(Phase 4 §4 already covered) — Karpathy pattern combines mechanisms 5 + 2 + 3 = curation + preprint-speed + benchmark-rigor in single artefact.

---

## §13 Substrate cross-pull summary table

| Mechanism | Cybernetics | Complexity | Phil-sci | Левенчук | ML/AI |
|---|---|---|---|---|---|
| Peer review | external observer | selection pressure | Longino | методолог review | journals |
| Preprints | variety distribution | mutation source | Feyerabend | gugл/lit search | arXiv |
| Benchmarks | probing protocol | fitness landscape | Popper | стандарт competition | PWC |
| Replication | feedback loop | replicator dynamics | Hacking | hands-on проект | reproducibility crisis |
| Curation | filter / amplifier | niche construction | Longino | методолог гармонизация | awesome-lists |
| Conferences | synchronisation pulse | swarm coordination | Kuhn | МИМ резидентура | NeurIPS |
| Citations | trace / log | preferential attachment | Laudan | provenance | bibliometrics |
| Standards | controller | locked-in convention | Lakatos hard core | BoK | ISO/IEEE |
| Meta-research | introspection | meta-evolution | Chalmers | retrospective | Annual Reviews |

---

## §14 Что НЕТ ни в одном individual mechanism

| Что необходимо | Где отсутствует |
|---|---|
| Cross-domain SoTA-translation | individual mechanisms domain-bound |
| Adversarial preservation (AP-6) | most mechanisms favour winner — Feyerabend missing |
| Year-stamp on quality of SoTA-claim | partial (preprints arXiv versioning); incomplete |
| Honest cost-benefit на SoTA-claim | benchmarks ignore deployment cost |
| Multi-stakeholder SoTA (Huyen Ch.1) | none formally support |
| Forgotten work retrieval | meta-research partial |

**Это все candidates для Jetix extension proposals (Phase 7 §extensions).**

---

## §15 Open questions для Ruslan (R1 surface)

1. **Replication mechanism в Jetix** — currently weakest; how to operationalise?
2. **Benchmark cluster в comparisons/** — formal или ad hoc?
3. **Periodic survey-of-Jetix** — meta-research cadence?
4. **External observers** (cybernetic SoTA-tracking) — formalised role или ad-hoc?
5. **Cross-clan SoTA-translation** — partner-clan merger pattern?
6. **Standards body equivalent в Jetix** — FPF Steward partly, broader?

---

## §16 Phase 5 acceptance gate

- [x] **9 mechanisms decoded** (§§2-10): peer review / preprints / benchmarks / replication / curation / conferences / citations / standards / meta-research
- [x] **Each mechanism**: operational + biases + phil-sci frame + Jetix-application
- [x] **9-mechanism comparison matrix** (§11)
- [x] **Substrate cross-pull**: cybernetics + complexity + Karpathy (§12-13)
- [x] **Missing pieces** identified (§14)
- [x] **R1 open questions** (§15)

**Sources cited:** 20 inline + 15 cross-references to Phases 1-4 + substrate.

---

*Phase 5 closure 2026-05-24. Next: Phase 6 — SOTA как operational concept в МИМ (Master Qualification cross-cite deep).*
