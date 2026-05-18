---
title: Harari через Jetix lens — research plan + namespace map
date: 2026-05-18
type: research-plan
parent_prompt: prompts/harari-through-jetix-lens-2026-05-18.md
brigadier_phase: meta-plan
status: in_progress
constitutional_posture: R1 surface-only + R6 provenance per claim + R2 namespace-scoped + append-only
F: F3
G: harari-jetix-lens-2026-05-18
language: russian + english (verbatim citations)
---

# Harari через Jetix lens — namespace plan

> **R1.** Surface only. Не promote Harari claims as Jetix strategy.
> **R6.** Provenance per claim (book/chapter where extractable; URL + retrieved_date online).
> **EP-5.** F-G-R по Jetix convention (F2-F4 для secondary-source extracts; NOT FPF B.3 F8).

## §0 Scope

Прогнать Yuval Noah Harari corpus (5 источников) через Jetix lens для extraction insights / patterns которые resonate с vision text_001-007 + H1-H8 Octagon + virtual tribe + trust mechanism + FPF universal language themes.

## §1 Namespace structure

```
research/harari-jetix-lens-2026-05-18/
├── 00-LENS-PLAN.md                          # this file
├── 01-sapiens-jetix-lens.md                 # Cognitive revolution + shared myths
├── 02-homo-deus-jetix-lens.md               # Dataism + useless class
├── 03-21-lessons-jetix-lens.md              # Meaning + community + education
├── 04-nexus-jetix-lens.md                   # ⭐ Info networks (priority #1)
├── 05-sapienship-publications-lens.md       # AI governance / d/acc adjacency
├── 98-CROSS-BOOK-SYNTHESIS.md               # Trajectory + cross-themes + Jetix decision
└── 99-SUMMARY-FOR-RUSLAN.md                 # ≤1500 words; 10-min read; Top-7 + reading order

raw/external/harari-corpus-2026-05-18/
└── 00-corpus-access-log.md                  # provenance trail (R6)
```

## §2 Per-doc structure (uniform across 01-05)

- §0 TL;DR (≤200 слов)
- §1 Verbatim Harari quotes (top 10 most relevant)
- §2 Core Harari claims (numbered)
- §3 Jetix lens application per claim
- §4 What Harari shows что Jetix может learn / borrow
- §5 What Harari is critical of — does Jetix avoid these?
- §6 Direct mappings к specific Jetix artefacts (O-objects + H-insights + vision/ + FPF primitives)
- §7 Open questions (R1 surface, не decide)
- §8 На человеческом (plain Russian summary)

## §3 11 themes tracked (cross-cutting tags)

| Theme tag | Harari source primary | Jetix anchor primary |
|---|---|---|
| `#shared-myths-cooperation` | Sapiens (Cognitive Revolution) | text_002 «новый internet» + Foundation as shared myth |
| `#cognitive-revolution` | Sapiens (Part 1) | text_001 trust shift + text_002 FPF as language upgrade |
| `#dataism-critique` | Homo Deus (Ch 9) | R12 anti-extraction |
| `#useless-class-warning` | Homo Deus | Workshop counter-mechanism |
| `#information-flow-mechanics` | Nexus | FPF protocol design |
| `#truth-vs-order` | Nexus | F-G-R discipline + AP-6 dissent |
| `#story-vs-data` | Nexus + Sapiens | Workshop human-readable + FPF formal dual |
| `#decentralized-vs-centralized` | Nexus + 21 Lessons | d/acc + Ethereum substrate (text_007) |
| `#meaning-crisis` | 21 Lessons (Ch 19-21) | Workshop mastery vs commodified work |
| `#cooperation-at-scale` | Sapiens | text_004 virtual tribe + first clan |
| `#AI-alignment-democracy` | Nexus + Sapienship | governance / Pillar C / R12 |

## §4 Workflow

Phase 1 corpus access ✓ (raw/external/harari-corpus-2026-05-18/00-corpus-access-log.md)
Phase 2a Nexus 04 (priority #1) → commit
Phase 2b Homo Deus 02 → commit
Phase 2c Sapiens 01 → commit
Phase 2d 21 Lessons 03 → commit
Phase 2e Sapienship 05 → commit
Phase 3 cross-synthesis 98 → commit
Phase 4 summary 99 → commit + final push origin main

## §5 Constitutional posture

- R1 surface only — НЕ Harari-as-Jetix-authority, NEUTRAL framing
- R2 — namespace research/harari-jetix-lens-2026-05-18/ ONLY; Foundation read-only
- R6 — provenance per claim (book + chapter where possible; URL + retrieved_date online)
- R11 — Default-Deny
- AP-6 — preserve dissent (Harari has critics: Narayanan + Vishnoi + Hallpike + Economist «glib» + Jacobson «thick promise thin import») surface per doc §5
- EP-5 — disclosed F2-F4 grades per artefact
- Append-only — new dir; no overwrites
- NO paid API per memory feedback_no_api_keys (WebSearch + WebFetch built-in only)
- Parallel run к text-005-007-blockchain-integration — НЕ trog'ает namespace research/blockchain-integration-2026-05-18/
