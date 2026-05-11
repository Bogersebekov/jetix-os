---
title: "Gamification Mining — Realm Entity Spec Derivation"
type: summary
niche: business
scope: cluster
covers: ["E1", "E2", "E3", "E4", "E5", "E6"]
sources: []
related: ["decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md"]
tags: [#type/summary, #status/draft, #topic/gamification, #topic/realm, #topic/synthesis]
created: 2026-05-11
updated: 2026-05-11
confidence: high
pipeline: ingested
state: draft
audit:
  confidence: high
  primary_source_cited: true
  hallucination_risk: low
  fallback_to_bm25: false
---

# Realm Entity Spec Derivation

## TL;DR
Mining identifies specific mechanic+theory+psychology support per Realm entity E1-E6. **Each E now has 4-domain anchored substrate** — Ruslan может describe Realm своими словами, wiki cross-verifies / fills gaps.

## E1 — Persona (Специалист)
- **GAMES**: WoW achievement system, ranked ladder, Civ great-people, Dota MMR, Roblox creator DevEx
- **THEORY**: visible progression Nash-equilibrium-stable
- **PSYCHOLOGY**: SDT competence (Ryan-Deci), flow visibility (Csikszentmihalyi)
- **EXPERTS**: Castronova virtual GDP per-player measurability
- **Spec implications:**
  - 6 stats visible (TRM resources)
  - Achievement portfolio per category
  - Ranked tier visible + hidden MMR refinement
  - Player «legend» status (Great People system)
  - Daily streak DISABLED (Cialdini commitment OK; loss aversion manipulation NOT)

## E2 — Class (Специализация)
- **GAMES**: WoW 13 classes × 3 specs talent tree, Diablo skill trees, Civ tech tree, Dota 130 heroes deep specialization
- **THEORY**: Nash equilibrium asymmetric (different class strategies viable)
- **PSYCHOLOGY**: SDT competence + autonomy в choosing class path
- **EXPERTS**: economic specialization (industry chains EVE, Castronova labor markets)
- **Spec implications:**
  - 6 classes (Hunter / Guardian / Scholar / Creator / Architect / Merchant)
  - Sub-class trees (Talent-tree pattern, 30-50 trade-off choices)
  - Multi-year mastery curve (Dota skill ceiling)
  - Multi-path viable (Civ multi-victory)
  - Respec available (gold/token cost)

## E3 — Clan (Команда)
- **GAMES**: Torn Faction (primary), WoW Guild, EVE Corporation/Alliance, Pokemon Go raids
- **THEORY**: Axelrod iterated PD cooperation, Schelling focal points
- **PSYCHOLOGY**: SDT relatedness, Cialdini social proof + commitment
- **EXPERTS**: Castronova guild economies, Williams Ninja-Metrics social networks
- **Spec implications:**
  - 3-10 members (matches Torn band)
  - Faction Respect = Clan Reputation (cumulative, visible)
  - Faction Armoury = Shared resource pool (AI tools, templates, contacts)
  - Organized Crimes 80-95% split = Organized Projects revenue share
  - Faction Wars = Соревновательные тендеры
  - Faction Tree = Clan progression tree
  - Guild perks unlock at clan tier

## E4 — Quest (Реальная бизнес-задача)
- **GAMES**: WoW quest design loop, Civ multi-path victories, EVE industry chains, Pokemon Go location-based
- **THEORY**: mechanism design (Hurwicz/Maskin), matching markets (Roth), Vickrey auctions
- **PSYCHOLOGY**: SDT autonomy в quest selection, flow challenge-skill balance
- **EXPERTS**: Machinations diagramming, Daniel James indie precedent
- **Spec implications:**
  - 5 parameters: class / level / time / reward / difficulty
  - Reward triple: € + Reputation + Knowledge (intrinsic + extrinsic balance)
  - Difficulty calibrated to player level (flow band)
  - Optional bonus objectives (autonomy)
  - Auto-decomposition multi-stage (EVE industry chain pattern)
  - Quest chains (long-term arc)
  - Mechanism design ensures incentive-compatibility (truthful preferences)

## E5 — Resources (Энергия, фокус, AI credits, audience reach)
- **GAMES**: Torn Energy soft-constraint, EVE ISK + Plex bridge, WoW Token, Roblox Robux/DevEx
- **THEORY**: Vickrey auctions, market mechanisms
- **PSYCHOLOGY**: scarcity (Cialdini) bounded use
- **EXPERTS**: Castronova sinks/faucets + virtual currency design, Lehdonvirta MIT textbook, Guðmundsson MER transparency, Machinations Monte Carlo
- **Spec implications:**
  - 4 resources: Energy (deep work cap), Focus tokens, Audience reach, AI credits
  - Soft caps with predictable regen (Torn Energy pattern)
  - Dual currency: Knowledge tokens (earned) + Premium credits (paid)
  - PLEX-equivalent bridge ($ → Knowledge tokens) to legalize RMT
  - Quarterly Realm MER transparency (EVE precedent)
  - Marketplace player-driven (EVE / Torn precedent)
  - NO whaling design (Shokrizade anti-pattern)

## E6 — Seasons (3-month cycles)
- **GAMES**: Fortnite battle pass (anchor), WoW expansion + Mythic+ rotation, EVE seasons, Civ era progression, LoL global esports circuit
- **THEORY**: Schelling focal points (predictable rhythm)
- **PSYCHOLOGY**: scarcity (Cialdini), variable rewards (cautious), flow refresh
- **EXPERTS**: temporal cohort dynamics
- **Spec implications:**
  - 3-month cycles (Fortnite predictable cadence)
  - Strategic theme per season (Pharma / Berlin GTM / etc.)
  - Battle pass tier progression (Free + Premium)
  - Mid-season live event (Demo Day)
  - Pre-season teaser (Town Hall)
  - Season-end leaderboard + rewards
  - Crossover collaborations (guest mentors aligned to theme)
  - Mythic+ rotation pattern (recurring quest pool с seasonal twist)

## Что ещё открыто
- Specific stat formulas per E1 ресурс
- Specific class skill trees per E2 (deferred к pilot)
- Specific quest difficulty calibration formulas
- Specific Realm MER methodology
- Specific Theme list для seasons 1-4

## Входные страницы
Все 158 mined entries + 4 domain summaries + cross-domain synthesis.
