---
title: "MLOps Lifecycle (Huyen 2022)"
type: concept
niche: tech
agents: [ml-ai-foundations-expert]
sources:
  - raw/external/research-corpus-2026-05-23/sota/huyen-designing-ml-systems-2022.md
related:
  - concepts/dl-curriculum-3-parts.md
  - concepts/mast-failure-taxonomy.md
tags: [#type/concept, #topic/ml, #topic/mlops]
topics: [mlops, production-ml]
created: 2026-05-24
updated: 2026-05-24
confidence: high
pipeline: ingested
F: F2
G: jetix-shared
---

# MLOps Lifecycle (Huyen 2022)

## Суть в одной строке

Chip Huyen Designing ML Systems (2022) — production ML lifecycle: data → feature → model → deployment → monitoring → iteration.

## Определение

Designing Machine Learning Systems (Huyen 2022) — каноническая reference для production ML engineering:

1. **Data engineering** — sources / formats / processing / storage / sampling
2. **Feature engineering** — handling missing values / scaling / discretization / crossing
3. **Model development** — training / evaluation / experiment tracking / debugging
4. **Deployment** — batch vs online prediction / model serving / edge vs cloud
5. **Monitoring** — distribution shift / model degradation / data quality
6. **Iteration / continual learning** — feedback loops + retraining triggers

## Применимость

- **Production ML SE methodology canonical reference**
- **Cross-ref engineering-expert** для production engineering questions (engineering-expert authoritative)
- **Pair с MAST failure taxonomy** для MAS-specific failure modes

## Связи

- Pair с: [[concepts/dl-curriculum-3-parts]] (textbook layer)
- Pair с: [[concepts/mast-failure-taxonomy]] (failure mode layer)

## Источники

- [src: raw/external/research-corpus-2026-05-23/sota/huyen-designing-ml-systems-2022.md]
- [src: reports/book-driven-agents-2026-05-24/05-wiki-auto-creation-proposals.md §5.3.A21]
