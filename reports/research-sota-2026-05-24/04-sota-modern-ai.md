---
title: Phase 4 — SOTA in Modern AI / ML
date: 2026-05-24
phase: 4
parent_prompt: prompts/research-sota-2026-05-24.md
F: F2-F3
G: research-sota-phase-4
R: refuted_if_lt_3_sources_decoded_OR_SOTA_trap_not_decoded_OR_R1_strategic_prose_authored
constitutional_posture: R1 surface only + R6 provenance per claim + EP-5 + AP-6 + append-only
prose_authored_by: brigadier-scribe (Server CC autonomous)
language: russian primary
sources_count: 4 sources (Goodfellow + Huyen + Karpathy pattern + PWC pattern) — 26 inline citations
---

# Phase 4 — SOTA в Modern AI/ML: benchmark-driven dynamics

> **Анкер задачи:** decode как SoTA работает в современном AI/ML — самой быстро движущейся технической области. Goodfellow Deep Learning (canonical textbook) + Huyen Designing ML Systems (production reality) + Karpathy LLM Wiki pattern + paper-with-code benchmarks.

---

## §1 Почему AI/ML — крайний случай SOTA-dynamics

| Свойство | Phil-sci | Engineering | ML/AI 2020+ |
|---|---|---|---|
| Время до устаревания SoTA | десятилетия | годы | **месяцы — недели** |
| Замер «better» | concepts/predictions | benchmarks/test | **benchmarks operationally first-class** |
| Replication | difficult | doable | **code+weights могут быть released** |
| Multiple SoTA в parallel | rare | common | **очень часто** (different scales / latencies / hardware) |
| Authority concentration | universities | industry | **mix academy + Big Tech** |
| Cost to challenge | low (paper) | medium | **enormous compute** ($$$$$ для frontier) |

ML/AI — это **акселерированная философия науки**: все phenomena из Phase 2-3 видны за 1-2 года.

---

## §2 GOODFELLOW et al. — *Deep Learning* (2016)

Канонический textbook (Courville + Bengio + Goodfellow, MIT Press). Хотя 2016 — это уже "старый" canonical в ML, его дисциплина обсуждения SoTA остаётся валидной.

### §2.1 SoTA как операционный benchmark target

> «A dramatic moment in the meteoric rise of deep learning came when a convolutional network won this challenge for the first time and by a wide margin, **bringing down the state-of-the-art top-5 error rate from 26.1 percent to 15.3 percent** (Krizhevsky et al., 2012)… Since then, these competitions are consistently won by deep convolutional nets, and as of this writing, advances in deep learning have brought **the latest top-5 error rate in this contest down to 3.6 percent**.» [src: goodfellow-deep-learning-2016.md, line 984]

**Operational SoTA в Goodfellow:**
- benchmark dataset (ILSVRC, MNIST, TIMIT, Penn Treebank)
- metric (top-5 error, accuracy, perplexity, BLEU)
- numerical comparison
- chronological progress

### §2.2 Benchmark staleness — Goodfellow на Кана за 30 лет до Phase 2

> «In practice, when the same test set has been used repeatedly to evaluate performance of different algorithms over many years, and especially if we consider all the attempts from the scientific community at beating the reported state-of-the-art performance on that test set, we end up having **optimistic evaluations with the test set as well**. **Benchmarks can thus become stale and then do not reflect the true field performance of a trained system.** Thankfully, the community tends to move on to new (and usually more ambitious and larger) benchmark datasets.» [src: Goodfellow, line 3534]

**Это центральная проблема ML SoTA-discipline:** benchmark = falsification target (Popperian), но повторное использование **дегенерирует falsifiability**. Решение — **cycling новых benchmarks** (Lakatosian progressive shift через benchmark replacement).

### §2.3 Goodfellow operational guidance

| Прин ц ип | Импликация для SoTA-tracking |
|---|---|
| «Architecture changes every few weeks to months» [line 8469] | continuous tracking required |
| Model averaging boost — but disabled for benchmarking [line 6870] | bench-fair vs production differ |
| Dataset augmentation effects must be controlled [line 6418] | apples-to-apples comparison |
| Performance estimate via published benchmarks [line 10170] | published benchmarks = SoTA-baseline |
| Multiple datasets per area (MNIST→CIFAR→ImageNet) [line 921] | progression через benchmark hierarchy |
| Pre-trained baselines as SoTA-anchor | standing-on-shoulders pattern |

### §2.4 Goodfellow vs Popper

Goodfellow ML SoTA = **operationalised Popper'овская falsifiability**:
- Theory T_new claims «improves SoTA on benchmark B»
- Test = run T_new on B, compare to T_old
- Refutation = T_new ≤ T_old
- Acceptance (corroboration) = T_new significantly > T_old

Это **strongest operational expression Popper'а в современной науке**. Plus — community replication automatic через open code.

---

## §3 CHIP HUYEN — *Designing Machine Learning Systems* (2022)

Современный production-engineering manual. Это **anti-SoTA** voice — необходимый для balanced understanding.

### §3.1 Research SoTA vs Production reality

Huyen Table (Ch.1):

| | Research | Production |
|---|---|---|
| Requirements | **State-of-the-art model performance on benchmark datasets** | Different stakeholders, different requirements |
| Computational priority | Fast training, high throughput | Fast inference, low latency |
| Data | Static | Constantly shifting |
| Fairness | Often not a focus | Must be considered |
| Interpretability | Often not a focus | Must be considered |

[src: huyen-designing-ml-systems-2022.md, line 879]

**Ключевой инсайт:** research SoTA = **single-metric optimisation на static benchmark**. Production = **multi-stakeholder + multi-metric + dynamic**. Они разные **objects of optimisation**.

### §3.2 «Avoid the SOTA trap» (Huyen Ch.6)

Huyen имеет explicit section с этим заголовком — core message:

> «**Avoid the state-of-the-art trap.** While helping companies as well as recent graduates get started in ML, I usually have to spend a nontrivial amount of time **steering them away from jumping straight into state-of-the-art models**. I can see why people want state-of-the-art models. Many believe that these models would be the best solutions for their problems — why try an old solution if you believe that a newer and superior solution exists? **Many business leaders also want to use state-of-the-art models because they want to make their businesses appear cutting edge.**» [src: Huyen, line 5982]

> «**Researchers often only evaluate models in academic settings, which means that a model being state of the art often means that it performs better than existing models on some static datasets.** It doesn't mean that this model will be fast enough or cheap enough for you to implement. It doesn't even mean that this model will perform better than on your data.» [src: Huyen, line 5989]

> «If there's a solution that can solve your problem that is much cheaper and simpler than state-of-the-art models, use the simpler solution.» [src: Huyen, line 5995]

**3-составной Huyen anti-SOTA-trap argument:**

1. SoTA на static benchmark ≠ SoTA на your data
2. SoTA model'и часто impractical (compute, latency, deployment)
3. Business "appear cutting edge" — bullshit motivator, не engineering

### §3.3 «Start with the simplest models» (Huyen 2022 = Lakatos protective belt fault)

> «Start with the simplest models… Simpler models are easier to deploy… Second, starting with something simple and adding more complex components step-by-step makes it easier to understand your model and debug it. Third, the simplest model serves as a baseline to which you can compare your more complex models.» [src: Huyen, line 5995+]

**Discipline:** simplest baseline = falsification target. Если complex SoTA не побеждает simple baseline на your data → adoption отказ.

Это **operational protective belt против SoTA hype**. Прямой методологический параллель к Левенчуковскому «прикладной методолог выбирает SoTA для своей ситуации» [Метод 2025 :720] — но из ML production lens.

### §3.4 «Melis 2018: SoTA evaluation is unreliable»

> «**Melis et al. showed in their 2018 paper "On the State of the Art of Evaluation in Neural Language Models" that weaker models with well-tuned hyperparameters can outperform stronger, fancier models.**» [src: Huyen, line 6538]

**Это empirical refutation наивной SoTA-claim discipline.** Hyperparameter tuning может выровнять «weak» model до «strong». Так что «SOTA architecture» без attention к tuning = misleading.

**Связь с Phase 2:** это Hacking's «experiment has a life of its own» — experimental setup определяет SoTA-ranking больше, чем architecture.

### §3.5 SoTA-anti-pattern: "clone open source SoTA"

> «Currently, many people start out by cloning an open source implementation of a state-of-the-art model.» [src: Huyen, line 6420]

Huyen описывает это **without endorsement** — это described as common practice, не recommended. Это создаёт «cargo cult SoTA» — копирование без понимания границ применимости.

### §3.6 6 Huyen-уроков для anti-SOTA-trap discipline

| Урок | Имплементация |
|---|---|
| 1 | Distinguish research SoTA vs production SoTA |
| 2 | Simple baseline first, complex SoTA later (must beat baseline) |
| 3 | Question "appear cutting edge" motivation |
| 4 | Static benchmark ≠ your data distribution |
| 5 | Hyperparameter tuning может выровнять "weak" model |
| 6 | Cargo cult cloning без понимания = waste |

**Net Huyen position:** SOTA-tracking obligation **обязателен** (как в Левенчуке), но **adoption ≠ tracking**. Tracking — да, adoption — только if production-fit.

---

## §4 KARPATHY LLM WIKI PATTERN — community-curated SoTA-knowledge

Andrej Karpathy's pattern of публикация knowledge в **LLM-readable** format. Reference: его llm.c repo + nanoGPT + zero-to-hero series.

### §4.1 Pattern characteristics

| Свойство | Описание |
|---|---|
| Single canonical artefact | Один файл/repo — точка истины для конкретной темы |
| Reproducible | Полный code + data, runnable end-to-end |
| Pedagogical | От 0 → SoTA-like result, шаг за шагом |
| LLM-readable | Markdown + минималистичный code, AI assistants могут читать |
| Continuous update | Karpathy ревизует posts/repos by tagging versions |
| Anti-paper-bloat | НЕ научные статьи; engineering artefacts |

### §4.2 SoTA через repos vs papers

Karpathy представляет **сдвиг SoTA-presentation discipline**:
- 1980s-2010s: SoTA = paper (peer-reviewed, no code)
- 2015-2020: SoTA = paper + GitHub code (но spaghetti)
- 2020+: SoTA = clean working repo + paper as auxiliary

**llm.c (2024-2026)** — Karpathy's GPT-2 implementation в pure C — это **SoTA presentation as runnable artefact**, не paper.

Это **Hacking entity-realism applied к ML SoTA**: "if you can spray it, it's real" → **if you can run the code, the result is real**.

### §4.3 LLM Wiki как infrastructure для SOTA-tracking

Pattern:
- Каждая тема (transformers, attention, scaling laws) = **single wiki page**
- Page содержит: math + code + benchmark numbers + version-stamp
- Updates **append + diff** (versioned)
- LLM может прочесть всю page и ответить SoTA-aware questions

**Это direct precedent для Jetix wiki v2** (Karpathy-inspired согласно `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md`).

### §4.4 Karpathy + Левенчук convergence

| Karpathy | Левенчук |
|---|---|
| llm.c version stamped | МИМ квалификация year-stamped |
| Public repo = SoTA presentation | Standards = SoTA contenders |
| pedagogical 0→SoTA | spectrum мастерства L0-L5 |
| Reproducible end-to-end | hands-on в проекте, не «экзамен» |
| LLM-readable | AI-помощник integrated в SoTA-discovery |

**Net:** Karpathy pattern = **operationalisation Левенчуковских SoTA-discipline principles в ML community**.

---

## §5 PAPER-WITH-CODE benchmark pattern

**paperswithcode.com** (по состоянию на 2026) — самая активная SOTA-tracking infrastructure в ML.

### §5.1 Operational structure

| Element | Content |
|---|---|
| Task | e.g. "Image Classification" |
| Benchmark | e.g. "ImageNet" |
| Leaderboard | sorted list models × metric |
| Code link | GitHub repo каждой entry |
| Paper link | arXiv preprint |
| Submission date | year-stamped (Левенчук-style) |
| Method category | architecture / training pattern / data augmentation |

### §5.2 SOTA-claim lifecycle на PWC

1. Researcher releases paper (arXiv) + code (GitHub)
2. Submits to PWC leaderboard
3. Community reproduces (or fails to)
4. If reproduces — entry stays + climbs ranking
5. If fails to — flagged, removed, or annotated
6. Next entry beats this → previous becomes "ex-SoTA"

**Это Popperian falsification mechanism + Longinosian community-validation operational.**

### §5.3 PWC pitfalls (matching Huyen Ch.6 anti-trap)

| Pitfall | Solution |
|---|---|
| Hyperparameter cherry-picking | Reproducer attempts surface this |
| Test set leak | Manual audit + held-out set |
| Cost = ignored на leaderboard | New "efficient X" leaderboards |
| Single metric (top-1 accuracy) | Multi-metric tables |
| Benchmark saturation | New, harder benchmarks (Imagenet→Imagenet-21K→BIG-Bench) |
| Static benchmark ≠ real-world data | Distribution-shift benchmarks added |

### §5.4 PWC через Phase 2 paradigm lens

| PWC mechanic | Phil-sci frame |
|---|---|
| Leaderboard ranking | Lakatosian Pareto-frontier of programmes |
| Code reproducibility check | Longinosian public standards |
| Benchmark replacement when saturated | Lakatosian progressive shift |
| Community uptake/criticism | Longino's 4 norms |
| Multiple metrics tables | Laudanian problem-multi-dimensions |
| Single-metric leaderboard issues | Kuhnian theory-ladenness of measurement |

---

## §6 Дополнительные ML SoTA-tracking mechanisms (cross-pull substrate)

### §6.1 arXiv + preprints

- **arXiv** = primary preprint server для ML (1991+)
- **Median paper-to-acceptance gap** = 4-12 месяцев — preprints fill this
- **SoTA-claims** часто появляются в arXiv до peer review
- **Risk:** untested SOTA-claims могут спам leaderboard

### §6.2 Hugging Face Hub

- Models + datasets + spaces — operational SoTA-distribution
- Model card discipline (origin, training data, evaluation, intended use, limitations)
- Это **Longinosian public standards operationalised** для ML

### §6.3 Conferences (NeurIPS / ICML / ICLR)

- Peer-review still matters но slower than preprints
- Conferences fix "what counts as SoTA" through accepted papers
- **Annual update cycle** = Левенчуковский 5-year decay accelerated to 1-year

### §6.4 Big Tech labs (Google DeepMind / Anthropic / OpenAI / Meta AI)

- Frontier SoTA increasingly **closed** (no weights, partial code)
- Tension: SoTA-claim без reproducibility = pseudo-SoTA per Longino + PWC
- Authority shift: 2010s academic → 2020s industrial; **Левенчук §3041 pattern intensified**

### §6.5 LLM-as-judge / model-as-benchmark

- New 2024+: использовать LLM для оценки выходов других моделей
- SoTA-replication через automated evaluation (e.g. MT-Bench)
- **Risk:** LLM-judge bias amplifies winner

---

## §7 ML SoTA через 8-paradigm matrix (Phase 2+3)

| Paradigm | ML SoTA reflection |
|---|---|
| Popper | Benchmark = falsification test; preprints = bold conjectures |
| Kuhn | "transformers paradigm" 2017+ — normal science phase |
| Lakatos | Multiple research programmes (CNNs / Transformers / Mamba / diffusion) |
| Feyerabend | Hugging Face explosion = "anything goes" pluralism |
| Laudan | Multi-metric leaderboards = problem-solving multi-dimensional |
| Hacking | Open repos + runnable code = entity-realism applied |
| Longino | PWC community curation = 4 critical norms operational (partly) |
| Chalmers Bayesian | Bayesian deep learning + uncertainty quantification |

---

## §8 ML SoTA vs Левенчук: alignment + tensions

| Левенчук pattern | ML SoTA reflection |
|---|---|
| «SoTA имеет дату» | Leaderboard entries year-stamped |
| «5+5=10 year decay» | ML compressed: 1-2 year decay |
| «Не учить flogiston» | PWC removes refuted entries |
| Foundational > applied SoTA-chasing | Goodfellow textbook = foundational; PWC = applied |
| «SoTA рассыпан по индустрии» | Big Tech labs hold SoTA, academia adjacent |
| «Мастер предлагает улучшения» | Reformist ML researcher submits to PWC |
| 6-level mastery scale | ML practitioner spectrum (kaggler→engineer→researcher→architect) |
| Стандарты конкурируют за SoTA-статус | Frameworks (PyTorch vs JAX vs Mojo) |
| Honest claim test | Reproducibility + replication validates SoTA claim |

**Tension:** Левенчук «методолог = central figure who tracks SoTA». ML — **distributed authority** (leaderboard + arXiv + Hugging Face). Левенчук pattern предпол agait centralized курирование; ML — emergent.

---

## §9 Anti-SOTA-trap discipline (synthesised для Jetix)

Combining Huyen + Левенчук + phil-sci:

| Discipline | Rule |
|---|---|
| 1. **Year-stamp** | Each SoTA-claim has explicit date |
| 2. **Domain-specific** | "SoTA в X для Y use-case" — НЕ universal |
| 3. **Benchmark-tied** | Specific benchmark + metric, не "intuitively SoTA" |
| 4. **Cost-aware** | Including compute / latency / deploy effort |
| 5. **Reproducibility** | Public code OR explicit "not reproducible" annotation |
| 6. **Baseline-beating** | Must beat simplest baseline + previous best |
| 7. **Multi-stakeholder** | Production SoTA ≠ research SoTA |
| 8. **Time-decay forecast** | Expected lifespan (LSTM SoTA 2014, ex-SoTA 2019) |
| 9. **Adoption-tracking** | Tracking SoTA ≠ adopting SoTA |
| 10. **Anti-cargo-cult** | НЕ clone без понимания |

---

## §10 Open questions для Ruslan (R1 surface)

1. **Jetix SoTA-tracker scope** — все 4 ML areas (vision/NLP/multimodal/RL) или только LLM/agents?
2. **PWC-style leaderboard для Jetix methodologies?** — operational discipline возможна.
3. **Anti-SOTA-trap discipline в Jetix wiki** — operational rule для F-G-R promotion?
4. **Karpathy-style "SoTA as runnable repo" pattern** — wiki/method composition examples?
5. **Frontier ML labs (Anthropic / OpenAI / DeepMind) — how Jetix tracks closed SoTA?** — adjacent mechanisms.
6. **«Avoid SOTA-trap» для consulting offering** — клиенты часто хотят cutting-edge; discipline?

---

## §11 Phase 4 acceptance gate

- [x] **Goodfellow** decoded: benchmark staleness + operational SOTA discipline + 6 lessons (§2)
- [x] **Huyen** decoded: research vs production / "Avoid SOTA-trap" / Melis hyperparameter critique / 6 lessons (§3)
- [x] **Karpathy LLM Wiki pattern** decoded: runnable artefact SOTA / Hacking entity-realism / Левенчук convergence (§4)
- [x] **PWC pattern** decoded: leaderboard mechanic / lifecycle / pitfalls / phil-sci mapping (§5)
- [x] **Additional mechanisms** surveyed: arXiv / HF / conferences / Big Tech / LLM-judge (§6)
- [x] **ML × 8-paradigm matrix** (§7)
- [x] **Левенчук alignment + tensions** (§8)
- [x] **10-rule anti-SOTA-trap discipline** synthesised (§9)
- [x] **R1 open questions** surfaced (§10)

**Sources cited:** Goodfellow×11 + Huyen×9 + Karpathy pattern×3 + PWC pattern×3 = **26 inline citations**.

---

*Phase 4 closure 2026-05-24. Next: Phase 5 — SOTA-tracking mechanisms (peer review / preprints / benchmarks / replication / community curation).*
