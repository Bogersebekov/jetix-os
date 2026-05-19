---
title: "Taleb Via Negativa — remove fragility before optimisation"
type: concept
niche: meta
sources:
  - research/safety-develop-validation-2026-05-19/06-taleb-antifragile-black-swan.md (Phase 5 deep mining)
  - Taleb N.N. «Antifragile: Things That Gain from Disorder» (Random House 2012) — primary
  - Taleb N.N. «The Black Swan» (Random House 2007)
  - Taleb N.N. «Skin in the Game» (Random House 2018)
related:
  - concepts/safety-develop-cross-disciplinary-corroboration.md (parent — risk-philosophy parallel)
  - concepts/sre-error-budget.md (sibling — engineering parallel)
tags: [#type/concept, #topic/risk, #topic/antifragility, #topic/taleb, #topic/via-negativa, #priority/p3]
topics: [taleb, antifragility, black-swan, via-negativa, barbell-strategy, fragility, safety-develop]
created: 2026-05-19
updated: 2026-05-19
confidence: F2 (core principles widely-cited) / F3 (politically-loaded extensions marked)
pipeline: ingested
constitutional_posture: R1 surface + R6 verbatim per claim + EP-5 F-grade + anti-cherry-pick (critique surfaced)
prose_authored_by: brigadier-scribe (K-5 Phase 5)
tier_status: Tier C (reference concept; complement к safety-develop-cross-disciplinary-corroboration.md)
batch_id: k-5-safety-develop-validation-2026-05-19
---

# Taleb Via Negativa — remove fragility before optimisation

> **K-5 Tier C reference concept.** Risk-philosophy parallel for Safety→Develop ordering. Mechanism: «remove fragility BEFORE adding reinforcement / optimisation».

## Суть в одной строке

«The first task in dealing with the unknown is to remove the source of fragility, not to add reinforcements» (Taleb 2012 ch. 21) — risk-philosophy operationalisation of Safety→Develop.

## Three-state fragility gradient

| State | Behaviour under volatility | Examples |
|---|---|---|
| **Fragile** | Loses from volatility | Glass; over-optimised systems |
| **Robust** | Neutral to volatility | Rock; well-engineered systems |
| **Antifragile** | Gains from volatility | Immune system; biological evolution; trial-and-error organisations |

## Verbatim core claims

**Via negativa (Taleb 2012 ch. 20):**
> «The idea of via negativa, the application of the way of subtraction — the heuristic that we know what is wrong with more clarity than what is right, and that knowledge grows by subtraction.»

**Tail risk first (Taleb 2007 ch. 1 Black Swan):**
> «What we call here a Black Swan… is an outlier… carries an extreme impact… in spite of its outlier status, human nature makes us concoct explanations for its occurrence after the fact.»

**Barbell strategy (Taleb 2012 ch. 11):**
> «I am barbelled, meaning I take risks on small bets but want to be conservative on the large ones.»

**Skin in the game (Taleb 2018):**
> Decision-makers must bear consequences. Absence of skin in the game = extractive (push fragility onto others).

## Critique surface (anti-cherry-pick — breadth-NOT-selection)

**Aven 2015 academic critique:**
> «The concept of antifragility has been received with considerable interest in the practitioner community, but the academic risk-analysis community has been more cautious. The boundaries between resilience, robustness, and antifragility are not always clear, and Taleb's examples sometimes conflate distinct phenomena.»

**Politically-loaded extensions:** INCERTO vols. 4-5 include political commentary (anti-«IYI» / libertarian skepticism). K-5 marks F3 — core antifragility F2; political extensions F3 (NOT relied on для Safety→Develop pattern extraction).

## Applied antifragility (industrial validation)

**Chaos Engineering** (Netflix Chaos Monkey 2011+; Principles of Chaos 2017):
- Inject controlled disorder to expose fragility BEFORE catastrophic manifestation
- Direct industrial application of via negativa
- Microservices «embrace failure» discipline

## R12 alignment

**STRONG via «Skin in the Game»** (Taleb 2018). Decision-makers must bear safety-failure cost; absence of skin in the game = extractive. Parallel к R12 anti-extraction.

**IP-1 caveat:** Pillar C Tier 2 rule 5 explicit — «AI does NOT claim skin-in-the-game / ownership / consequences». Taleb's framing applies to humans-in-loop, NOT autonomous agents.

## Cross-link к Safety→Develop

См. `concepts/safety-develop-cross-disciplinary-corroboration.md` — Taleb = 5th distinct safety-type (fragility / tail-risk).

---

*Wiki Tier C reference concept. K-5 Phase 5 Taleb deep mining substrate. F2 core / F3 politically-loaded marked (anti-cherry-pick discipline).*
