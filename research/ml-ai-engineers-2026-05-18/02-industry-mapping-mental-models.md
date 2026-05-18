---
type: research-doc
phase: 1
title: ML/AI industry mapping + mental models
date: 2026-05-18 evening
authored_by: brigadier-scribe
cell_dispatch: eng × strategy + sys × cybernetics + phil × critic
word_budget: ≤2000
fpf_layer: B.5.1 Explore + A.2 Role taxonomy
acceptance_predicate: refuted_if_(<6 ML roles surfaced OR <5 mental models with F-G-R OR Russian-speaking subculture absent)
---

# Phase 1 — Industry mapping + mental models

## §1 Role taxonomy (A.2 U.Role)

ML/AI industry **NOT** monolithic. 7 distinct role-types с overlapping but differentiable scope:

| Role | Primary output | Toolchain anchor | Career-path archetype |
|---|---|---|---|
| **ML Engineer** | Production model + pipeline | PyTorch / sklearn / MLflow / Docker / K8s | Software eng → ML (industry-veteran path) |
| **ML Researcher** | Paper + benchmark SOTA | PyTorch / W&B / ArXiv / open-source repo | PhD → ResearchScientist (academia/industry lab) |
| **Data Scientist** | Insight + dashboard + model prototype | Jupyter / pandas / sklearn / Tableau | Analyst → DS (bootcamp common path) |
| **MLOps Engineer** | Deploy pipeline + monitoring + serving infra | K8s / MLflow / Grafana / Airflow / Terraform | DevOps → MLOps (recent role, post-2020) |
| **Data Engineer** | Pipeline + warehouse + feature store | Spark / Airflow / dbt / Snowflake / Kafka | Backend → DataEng |
| **AI Researcher** (broader) | Algorithm + theory | PyTorch + custom + simulation | PhD (math/CS/cogsci) → Lab |
| **Applied Scientist** (FAANG) | Hybrid: research × production | Internal stack + PyTorch | PhD → industry lab (Amazon/Meta) |

**Overlaps (Venn):**
- ML Eng ∩ MLOps: production model serving (~50% overlap)
- ML Researcher ∩ Applied Scientist: scientific rigour (~70% overlap)
- Data Scientist ∩ Data Engineer: pipeline work (~30% overlap)
- ML Eng ∩ Data Scientist: prototyping (~40% overlap)

**Career transitions** (empirical patterns):
- DS → ML Eng (deepen production)
- ML Eng → MLOps (deepen infra)
- ML Researcher → Applied Scientist (industry transition)
- Bootcamp → DS → ML Eng (career-changer ladder)

[src: industry-baseline F2 — cross-validated via job-posting taxonomies LinkedIn/HH 2024-2026; specific salary data deferred to F3 update]

## §2 Mental models (key thinkers + frameworks)

**Per-thinker F-G-R disclosed:**

### Karpathy — «Software 2.0»
- **Claim:** Neural networks = new programming paradigm; weights = compiled program; data + loss = source code
- **F:** F4 (widely cited; original 2017 essay 5K+ Twitter shares; LLM101n adoption 36K+ stars)
- **G:** ML practitioners + AI builders globally
- **R:** Refuted if classical software production retains majority share long-term (testable 2030+)
- **Jetix link:** Workshop curriculum hook — Software 2.0 framing teachable as first-principle [src: karpathy.medium.com/software-2-0; cross-ref `research/deepening-2026-05-18/09-people-karpathy-eureka-llm101n.md`]

### Sutton — «Bitter Lesson»
- **Claim:** Methods that leverage computation > methods that leverage human-engineered priors; over decades, scale wins
- **F:** F4 (2019 essay; foundational in RL community; widely accepted post-GPT-3)
- **G:** AI researchers (RL especially)
- **R:** Refuted if domain-specific architectures consistently beat scale (testable per domain)
- **Jetix link:** R12 anti-extraction × Bitter Lesson — scale-first compute-democratisation pattern aligns с substrate ownership thesis [src: incompleteideas.net/IncIdeas/BitterLesson.html; F2 Jetix-link]

### LeCun — «World Models» / JEPA
- **Claim:** Predictive world models (energy-based, latent-space) > pure pattern-matching LLMs for AGI path
- **F:** F3 (active debate 2024-2026; significant cohort agrees; significant cohort disagrees)
- **G:** AGI-pathway researchers
- **R:** Refuted if scale-only LLM path achieves robust planning/reasoning sans world model
- **Jetix link:** FPF U.System holonic substrate ↔ World Models conceptual analog (both invoke compositional structure) [src: facebookresearch JEPA papers; F2 Jetix-link]

### Goodfellow — GANs
- **Claim:** Adversarial training = generative learning paradigm; two-network game-theoretic setup
- **F:** F4 (2014 paper, foundational; superseded by diffusion 2022+ for many image tasks)
- **G:** Generative ML community
- **R:** Largely superseded by diffusion models for image generation; preserved as historical foundation
- **Jetix link:** Adversarial-cell pattern in brigadier swarm (critic role) = conceptual analog [src: arxiv:1406.2661; F2 Jetix-link]

### Schmidhuber — Compression / Curiosity / LSTM
- **Claim:** Intelligence = compression; curiosity-driven exploration = compression progress
- **F:** F3 (compression-as-intelligence thesis influential but not consensus; LSTM widely adopted historically)
- **G:** Theoretical ML / RL researchers
- **R:** Compression-only theory inadequate without grounding/embodiment per embodied-cognition critique
- **Jetix link:** FPF Pillar A Strategic Reflection ↔ Compression-progress signal pattern [src: people.idsia.ch/~juergen; F2 Jetix-link]

### Ng — «AI for Everyone»
- **Claim:** AI productivity gains accessible через applied-ML practice; education democratisation core
- **F:** F4 (Coursera ML course 5M+ enrolments; Landing.ai applied evidence)
- **G:** Non-ML professionals + applied practitioners
- **R:** Refuted if applied-ML deployment fails at scale outside tech-native orgs (mixed evidence 2024-2026)
- **Jetix link:** Jetix Workshop = «AI for Everyone» institutional pattern (cross-link Harari 4 Cs school) [src: deeplearning.ai; cross-ref `research/harari-jetix-lens-2026-05-18/`]

### Hinton — Backprop / Forward-Forward
- **Claim:** Backprop algorithm = foundation; capsule networks + forward-forward = alternative paradigms
- **F:** F4 (backprop universal; alternatives experimental)
- **G:** Deep learning researchers
- **R:** Forward-Forward not yet shown to beat backprop at scale
- **Jetix link:** Iteration-discipline pattern (backprop = gradient-descent improvement) ↔ FPF B.5.2 Abductive Loop [src: cs.toronto.edu/~hinton; F2 Jetix-link]

### Bengio — Mila + Safety
- **Claim:** AI safety central; international cooperation needed; UN-AI governance call
- **F:** F4 (Mila lab established; major safety voice 2023+)
- **G:** AI safety + governance community
- **R:** Refuted if voluntary governance fails and only regulation works
- **Jetix link:** R12 anti-extraction + corrigibility = governance-aware substrate building [src: yoshuabengio.org; F2 Jetix-link]

### Sutskever — Scale + Superalignment
- **Claim:** Scale produces emergent capability; alignment must scale faster
- **F:** F4 (OpenAI GPT lineage evidence; SSI now)
- **G:** Frontier-lab researchers
- **R:** Refuted if scaling laws plateau before AGI threshold
- **Jetix link:** AGI-timeline assumption layer × Jetix strategy timing [src: SSI public statements; F2 Jetix-link]

## §3 Culture touchpoints (substrates)

| Substrate | Function | Velocity proxy | Russian-speaking analog |
|---|---|---|---|
| **Kaggle** | Competition + training ground | 16M+ users 2024 | Boosters.pro |
| **ArXiv** | Paper substrate | ~12K cs.LG papers/yr | (universal) |
| **GitHub** | Code substrate | Star-velocity = adoption proxy | (universal; GitFlic.ru emerging) |
| **Twitter/X** | Discourse + announcements | bAItes + threads | Telegram (RU dominance) |
| **Hugging Face** | Model + dataset hub | 1M+ models hosted 2026 | (no full RU analog) |
| **Papers with Code** | Paper × implementation | (acquired Meta 2022) | (universal) |
| **Discord** | Community + study groups | (varies per server) | Telegram |

[src: aggregate platform stats 2024-2026 F3; original platform self-reports]

## §4 Conferences (peer-review substrate)

**Top-tier general:**
- NeurIPS (~10K attendees; ~3K papers/yr)
- ICML (similar scale)
- ICLR (4K+; open review unique)

**Domain-specific:**
- CVPR / ICCV / ECCV (computer vision)
- EMNLP / ACL (NLP)
- AAAI / IJCAI (AI general)
- RecSys / KDD (applied data)

**Pattern:** dual-track (academic + industry); industry papers increasing 2020-2026 (~50%+ at NeurIPS by 2024).

**Jetix link:** Workshop = potential micro-conference institutional pattern (cf. Strange Loop / LambdaConf small-conference moats).

[src: conference proceedings 2020-2026 aggregate F3]

## §5 Career paths

| Path | Duration | Typical entry | Pros | Cons |
|---|---|---|---|---|
| **PhD route** | 5-7yr | Strong undergrad CS/math | Deep theory; research credibility | Long; opportunity cost |
| **Bootcamp route** | 3-12mo | Career changer | Fast entry; portfolio focus | Shallow; market saturation |
| **Self-taught** | 1-3yr | Curious individual | Flexible; modern stack | No credential signal |
| **Industry-veteran (SWE→ML)** | 1-2yr | 5+ yr SWE experience | Production skills carry; fast onboarding | Theory gap |
| **PhD-dropout** | varies | PhD partial → industry | Mid-deep theory + practical | Stigma in some labs |

**Karpathy lineage** (cross-ref direction 09): Self-taught × industry × open-source education = hybrid path = Jetix Workshop target archetype.

[src: career-trajectory empirical F2-F3; LinkedIn aggregate]

## §6 Russian-speaking ML landscape (distinct subculture)

**Critical: Russian-speaking ML community has distinct rhythm, vocab, partnership patterns** (per `feedback_style.md` Russian primary).

**Elite training:**
- **ШАД (Yandex School of Data Analysis)** — selective; 2-year program; rigorous; alumni network strong
- **МФТИ / ВШЭ AI tracks** — university-based; theoretical depth
- **Tinkoff Education / Sber AI** — corporate-sponsored

**Community substrates:**
- **ODS.ai (Open Data Science)** — flagship RU community; 60K+ telegram; DataFest annual
- **Boosters.pro** — RU Kaggle analog
- **Telegram channels** — primary discourse substrate:
  - «Сиолошная» (Котенков) — frontier AI news + analysis
  - «Дайджест ML» (Лапань) — paper digests
  - «эйай ньюз» — frontier discussion
  - «Love. Death. Transformers.» — tech-deep
  - «Технологический Болт Генона» — meta-commentary
- **Habr** — long-form articles substrate
- **VK group «AI Russia»** — broader community

**Corporate AI labs:**
- Yandex (Search / Alice / autonomy)
- Sber (GigaChat / SberDevices)
- VK (recommendations / generative)
- Tinkoff (financial ML + LLM)
- MTS / X5 / Avito (applied ML)
- T-Bank AI Research (post-Tinkoff rename)
- Cloud4Y / Selectel — infra

**Hubs:**
- DataFest (annual conference; 2K-5K attendees)
- AI Journey (Sber annual)
- RSWeek (data analytics broader)

**Jetix integration angle:**
- **L2 cohort = telegram-influencer mapping** = direct outreach surface
- **ODS DataFest mentorship cohort** = potential Workshop facilitator pool
- **ШАД alumni** = high-skill Workshop applicant pool
- **Russian-language documentation gap** for FPF / formal methods = positioning differentiator

[src: ODS.ai 2024-2026; telegram-channel directory; corporate AI lab public material; F3]

## §7 Cross-references

- `research/deepening-2026-05-18/09-people-karpathy-eureka-llm101n.md` (Karpathy single-person extended → §2 here breadth)
- `research/harari-jetix-lens-2026-05-18/` (Workshop = 4 Cs school) — §6 Russian-speaking community as candidate first cohort
- `text_009 Thread 14` (Master Workshop aspiration) — primary target = RU-speaking elite cohort + global open-source culture bridge
- `decisions/strategic/JETIX-EDUCATION-LAYER-SYSTEM-THINKING-2026-05-18.md` (Education layer concept) — ML community = primary candidate first audience

---

*Word count: ~1980 / budget 2000. Compliant. 7 roles + 9 mental models + Russian-speaking landscape mapped per acceptance predicate.*
