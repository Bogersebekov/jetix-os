---
title: Phase 9 — Mondragón + Cooperative DAOs Comparable
date: 2026-05-21
type: comparable-analysis-record
phase: 9
parent_prompt: prompts/economic-model-tokenomics-2026-05-21.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F4 derivative (Mondragón data + cooperative DAO public docs cited inline)
G: economic-model-tokenomics-phase-9-mondragon-coops-comparable
R: refuted_if_Mondragón_data_misattributed_OR_DAO_data_misstated_OR_comparable_strawman
constitutional_posture: R1 surface + R6 + R12 paired-frame
language: russian primary
---

# Phase 9 — Mondragón + Cooperative DAOs Comparable

> **Тезис.** Comparable analysis: Mondragón (68-year track record) + 6 cooperative DAOs (Gitcoin / RaidGuild / DXdao / Optimism RetroPGF / Aragon / Colony). Lessons mapped к Jetix V10 hybrid + structure innovation gap. 2 mermaid D17-D18.

---

## §A Mondragón Cooperative Corporation (MCC)

[src: Whyte & Whyte «Making Mondragon» Cornell 1991 + MCC Annual Reports 2020-2023 + Hansmann «Ownership of Enterprise» Harvard 2000 + Carroll & Buchholtz «Business & Society» 12th ed ch.6]

### §A.1 Core data points

| Metric | Value (2023) | Comment |
|---|---|---|
| Years operational | 68 (founded 1956) | One of longest-running cooperative federations globally |
| Workers | ~80,000 | Active cooperative members |
| Cooperatives | 95 | Industrial / retail / financial / educational |
| Revenue annual | ~€11B | Top-50 Spanish enterprise |
| Institutional retention | ~60% of surplus | Reserves + collective fund + cross-coop |
| Member direct | ~40% of surplus | Member capital accounts (paid at retirement) |
| Wage ratio cap | 5:1 (relaxed from 3:1 Eroski 1990s) | Highest-paid ≤ 5× lowest-paid |
| Inter-coop social fund | 10% | Funds Caja Laboral / new coop incubation |
| Member retention rate | ~85-90% | Cooperative discipline |
| Mondragón University | 4000+ students | Workforce training |
| Caja Laboral assets | €25B+ | Cooperative bank funding |

### §A.2 Structural features mapped к Jetix

| Mondragón feature | Description | Jetix V10 translation |
|---|---|---|
| **Worker-ownership** | Every worker = owner; 1-member-1-vote governance | ERC-1155 worker NFT (token 0x01) + ERC-5114 SBT identity = 1-member-1-vote |
| **60/40 split** | 60% к coop reserves + collective fund; 40% к individual member accounts | V10 hybrid auto-routes locked worker NFT: 60% treasury reserves / 40% member account (per Phase 5 §B.2) |
| **5:1 wage ratio cap** | Highest-paid ≤ 5× lowest-paid | On-chain Mondragón ratio cap check (revert if violation); 90% supermajority governance for override |
| **10% inter-coop social fund** | Mondragón Foundation funds new coop incubation | V10 QF matching pool funded by 5-10% L1 institutional skim quarterly |
| **Caja Laboral (coop bank)** | Member savings + new coop funding | V10 DAO treasury + future Jetix-internal lending pool (Phase 3+) |
| **Mondragón University** | Workforce training + cooperative pedagogy | Workshop tier L4-L7 already operational |
| **Cross-coop social services** | Healthcare / pension / education shared across coops | Jetix-internal partner support — partial Phase 2+; Foundation grants Phase 1 |
| **Exit (fork-and-leave)** | Member capital account returned at retirement / exit (с 5-15% holdback typical) | V10 RageQuit smart contract — immediate proportional treasury claim |
| **Cooperative law structure** | Basque cooperative legal entity (sociedad cooperativa) | Tokenomic / DAO structure (no traditional legal entity Phase 1; LLC wrapper considered Phase 2+) |

### §A.3 Mondragón innovation gap (что Jetix дополняет)

Mondragón limitations и Jetix beyond-Mondragón innovations:

| Mondragón limitation | Cause | Jetix innovation |
|---|---|---|
| **Geographically bound (Basque)** | Cooperative legal entity tied к regional jurisdiction | Tokenomic substrate global digital (Ethereum L2) |
| **2-role (worker + owner only)** | Industrial-era manufacturing focus | 3-role triple-role partner (worker + investor + promoter) |
| **Concentration tendency** | Eroski + Fagor dominance (Fagor sub-coop collapse 2013) | Promoter NFT explicit reward for new-partner-bringing → anti-concentration |
| **Slow innovation cycle** | Cooperative governance consensus slow | Sub-brigadier mini-swarm parallel decision-making + tighter feedback loops |
| **External market discipline weak** | Coops insulated from competition long periods | Workshop tier external students = market signal; partnership pipeline external benchmarking |
| **Charter discipline only (no programmatic)** | Pre-blockchain era | On-chain Mondragón ratio cap + QF matching + RageQuit (Option D Hybrid acked 2026-05-18) |

[src: Whyte & Whyte ch.7 critique + Mondragón Fagor post-mortem reports 2013 + Cooperative Cyril Errasti 2018]

### §A.4 Mondragón risk inheritance Jetix should anticipate

1. **Concentration tendency** — without active anti-concentration mechanism, Mondragón sub-coops grew unequally; Eroski 50K+ workers vs смaller coops 100-1000 workers. Jetix mitigation: promoter NFT explicit cascading reward.
2. **Innovation slow** — Mondragón missed dotcom + crypto waves; remained traditional industrial focus. Jetix mitigation: AI-native + crypto-native baseline.
3. **External market discipline** — Mondragón cooperatives insulated; Fagor over-extension led к collapse. Jetix mitigation: external Workshop demand signal + partner pipeline.
4. **Concentration of voice via management track** — Mondragón управленческая структура over time more hierarchical; some critics note diminished worker voice. Jetix mitigation: SBT 1-identity-1-vote + QF quadratic + 90% supermajority governance.

---

## §B Cooperative DAOs comparable (6+ analyzed)

### §B.1 Gitcoin

[src: Gitcoin governance forum + QF rounds 14-20 data 2022-2024 + a16z crypto-startup playbook]

| Metric | Value | Comment |
|---|---|---|
| Founded | 2017 | One of first DAO-style public-goods coops |
| Members | ~10K active QF round participants | Plus broader passive token holders |
| Revenue model | 5-10% operating take on QF matching | Funded externally via Coinbase / Polychain Capital |
| Distribution | QF matching pool: total = (Σ √c_i)² | Quadratic Funding native Buterin foundational |
| Treasury | ~$50M+ (2024) | Diverse holdings |
| Governance | GTC token + Gitcoin DAO | Proposals + voting |
| R12 compliance | Strong (contribution-rewarding; fork-and-leave possible) | But matching pool dependency external |
| Lessons для Jetix | QF matching pool = adopt V10; quarterly rounds; Sybil resistance via Gitcoin Passport | Internal funding (closed-loop) instead of external Coinbase dependency |

### §B.2 RaidGuild (Moloch DAO v2)

[src: RaidGuild Handbook + Moloch DAO v2 docs + DAOhaus framework]

| Metric | Value | Comment |
|---|---|---|
| Founded | 2019 | Web3 services cooperative |
| Members | ~150 raiders (2024) | Active members across 4 cohorts |
| Revenue model | 10% Treasury take on project revenue | Members keep 90% direct |
| Distribution | Member-pledged Loot + Shares; proportional treasury claim | RageQuit immediate |
| Treasury | ~$3-5M | Member-managed |
| Governance | Moloch v2 (1 share = 1 vote); proposals + vote period + grace + RageQuit | R12-exemplar (per Game Theory M-C mechanism §11) |
| R12 compliance | ✅✅ Exemplar — RageQuit fork-and-leave native | Cited Q2 ack 2026-05-12 R12 LOCK packet |
| Lessons для Jetix | Moloch RageQuit = adopt V10; 10% take low; member-pledge governance | Higher take rate (25%) for Jetix vs RaidGuild 10% (more institutional capacity needed) |

### §B.3 DXdao (sunset 2024)

[src: DXdao governance + sunset post-mortem 2024 + Friendly Forking proposal]

| Metric | Value | Comment |
|---|---|---|
| Founded | 2019 | Decentralized investment DAO |
| Status | **Sunset 2024** (treasury distributed к members) | Sustainability failure |
| Revenue model | 30-50% protocol fees on DXswap / DXmesa | Higher take than Jetix proposal |
| Distribution | DXD token + Treasury | Treasury growth via fees |
| Treasury | ~$20M+ at peak | Distributed at sunset |
| Governance | Reputation + DXD token (dual) | Complex |
| R12 compliance | △ Mixed — high take + ops overhead led к sustainability failure | NOT R12-exemplar |
| **Lessons для Jetix** | **Avoid overcomplex governance**; keep ops lean; sustainable ops > complex features; Friendly Forking spirit at sunset preserved R12 | Jetix risk: V10 hybrid complexity Phase 1 → simplification if needed |

### §B.4 Optimism RetroPGF

[src: Optimism RetroPGF rounds 1-5 reports 2022-2024 + Buterin blog «Why retroactive PGF»]

| Metric | Value | Comment |
|---|---|---|
| Founded | 2021 (Optimism Foundation) | L2 rollup chain |
| Members | RetroPGF rounds: 1500+ projects funded | Quarterly rounds |
| Revenue model | Sequencer revenue + OP token treasury allocation | $200M+ disbursed |
| Distribution | Retroactive PGF rounds — voters distribute fixed pool based on demonstrated impact | Anti-promise; reward outcomes |
| Treasury | OP token reserves multi-billion | Token-funded |
| Governance | Optimism Citizens' House (RetroPGF voters) + Token House (OP holders) | Bicameral |
| R12 compliance | ✅✅ Strong — public-good aligned; retroactive; recipients не extracted-from | Aspirational pattern |
| Lessons для Jetix | RetroPGF rounds — adopt в V10 Phase 2+ when contribution diversity ≥30 partners; sequencer-funded model maps to Jetix workshop-funded matching pool | Bicameral governance considered Phase 3+ |

### §B.5 Aragon

[src: Aragon governance docs + ANT token + Aragon DAO 2022 sunset/restructure]

| Metric | Value | Comment |
|---|---|---|
| Founded | 2017 | DAO infrastructure protocol |
| Members | ANT holders + sub-DAOs | Aragon DAO governance |
| Revenue model | Protocol fees + framework licensing | Modest |
| Distribution | ANT token + Aragon Court (dispute resolution) | Complex |
| Treasury | $200M+ at peak; significantly drawdown | Volatility |
| Governance | ANT voting + Aragon Court arbitration | Disputes resolved on-chain |
| R12 compliance | △ Mixed — framework R12-aligned but ANT governance whale risk | |
| Lessons для Jetix | Aragon governance framework usable as plumbing layer; avoid dependency on ANT token health | Use Aragon contracts but не Aragon token |

### §B.6 Colony

[src: Colony.io docs + native token CLNY]

| Metric | Value | Comment |
|---|---|---|
| Founded | 2016 | Reputation-based DAO platform |
| Members | Per-colony scale variable; SourceCred-inspired reputation | Smaller community |
| Revenue model | Protocol fees on colony actions | Modest |
| Distribution | Reputation-weighted (non-transferable) + CLNY governance | Hybrid |
| Treasury | Colony-internal | Per-colony |
| Governance | Reputation-weighted voting | Non-transferable rep |
| R12 compliance | ✅ Strong — reputation non-transferable = anti-speculation | |
| Lessons для Jetix | Reputation-based governance = adopt в V10 hybrid; SourceCred contribution scoring pattern | |

### §B.7 Comparison summary

| DAO | R12 native | Self-sustaining proven | Years | Treasury size | Adopt-to-V10 lesson |
|---|---|---|---|---|---|
| Mondragón | ✅ Charter | ✅ 68y | 68 | €11B revenue | 60/40 + 5:1 + 10% social fund |
| Gitcoin | ✅ QF | △ external funded | 7 | $50M+ | QF matching pool |
| RaidGuild | ✅✅ RageQuit | ✅ 5y | 5 | $3-5M | Moloch RageQuit pattern |
| DXdao | △ | ❌ Sunset 2024 | 5 | Distributed | AVOID overcomplex |
| Optimism RetroPGF | ✅✅ | ✅ sequencer-funded | 3 | $200M+ disbursed | RetroPGF rounds Phase 2+ |
| Aragon | △ | △ | 7 | $200M peak; drawdown | Framework plumbing only |
| Colony | ✅ Reputation | △ | 8 | per-colony | Reputation governance pattern |

---

## §C Lessons applied к Jetix V10 hybrid (consolidation)

V10 hybrid integrates lessons:

| Component | Source | V10 mechanism |
|---|---|---|
| 60/40 institutional/member split | Mondragón 68y | Smart contract routes locked worker NFT |
| 5:1 wage ratio cap | Mondragón | On-chain check + 90% supermajority override |
| QF matching pool | Gitcoin (Buterin 2018 paper) | 5-10% L1 institutional skim quarterly |
| RageQuit fork-and-leave | RaidGuild Moloch v2 | Smart contract proportional treasury claim |
| RetroPGF rounds (Phase 2+) | Optimism | Future quarterly distribution к worker contributors |
| Reputation governance | Colony / SourceCred | Reputation-weighted proposal thresholds |
| Inter-coop social fund (translated) | Mondragón 10% | QF matching pool |
| Anti-concentration (promoter dimension) | Beyond-Mondragón innovation | Soulbound promoter NFT |
| Sub-brigadier mini-swarm | Beyond-Mondragón (AI-native) | Parallel decision-making per project |
| External market discipline | Mondragón gap | Workshop tier external students |

**Outcome:** V10 hybrid = Mondragón + cooperative DAO best-of-breed synthesis + AI-native + tokenomic-native enhancements.

---

## §D Mermaid D17 — Mondragón structure mapping к Jetix V10

```mermaid
classDiagram
    class MondragónFeature {
        +60/40_split: institutional/member
        +5_to_1_ratio_cap
        +10_percent_social_fund
        +Caja_Laboral_bank
        +Mondragón_University
        +Worker_ownership
        +Fork_and_leave
    }
    class JetixV10Hybrid {
        +ERC1155_triple_role_NFT
        +Mondragón_60_40_routing
        +OnChain_5_to_1_ratio_check
        +QF_matching_pool_quarterly
        +DAO_treasury
        +Workshop_tier_L4_L7
        +SBT_identity
        +RageQuit_proportional
    }
    class CooperativeDAOLessons {
        +Gitcoin_QF
        +RaidGuild_RageQuit
        +Optimism_RetroPGF
        +Colony_Reputation
        +DXdao_avoid_overcomplexity
    }

    MondragónFeature --|> JetixV10Hybrid : 60/40 + 5:1 + social_fund + university adopted
    CooperativeDAOLessons --|> JetixV10Hybrid : QF + RageQuit + RetroPGF + Reputation adopted

    note for JetixV10Hybrid "Beyond-Mondragón: + Promoter NFT (3rd role)<br/>+ AI-native sub-brigadier<br/>+ tokenomic programmable enforcement"
```

---

## §E Mermaid D18 — Cooperative DAOs decentralization vs R12 (quadrantChart)

```mermaid
quadrantChart
    title Cooperative DAOs — Decentralization vs R12 conformance
    x-axis Low_decentralization --> High_decentralization
    y-axis Weak_R12 --> Strong_R12
    quadrant-1 Strong R12 + High decentralization (V10 target)
    quadrant-2 Strong R12 + Low decentralization
    quadrant-3 Weak R12 + Low decentralization
    quadrant-4 Strong decentralization + Weak R12
    Mondragón: [0.50, 0.85]
    Gitcoin: [0.70, 0.75]
    RaidGuild: [0.55, 0.92]
    DXdao_sunset: [0.65, 0.45]
    Optimism_RetroPGF: [0.75, 0.85]
    Aragon: [0.60, 0.55]
    Colony: [0.50, 0.75]
    Jetix_V10_target: [0.80, 0.95]
```

---

## §F Open R1 questions surfaced

| # | Question | Pending Ruslan |
|---|---|---|
| 1 | Adopt Mondragón Caja Laboral-equivalent lending pool Phase 3+? | ⏳ |
| 2 | Workshop tier == Mondragón University parallel? Brand alignment? | ⏳ |
| 3 | Cross-coop social fund 10% maps к QF — exact % L1 skim (5/7.5/10%)? | ⏳ |
| 4 | Sub-brigadier mini-swarm = beyond-Mondragón innovation; how to brand? | ⏳ |
| 5 | Optimism RetroPGF Phase 2+ adoption timing (cohort threshold)? | ⏳ |

---

## §G Cross-refs

- TOKENOMICS-VARIANTS sub-doc V10 hybrid spec
- Phase 8 self-sustaining growth thesis §C cooperative DAO comparison
- Phase 7 closed-loop dynamics §D comparison к Mondragón
- Phase 11 risk surface concentration tendency mitigation

---

*Phase 9 closure 2026-05-21. Brigadier-scribe Cloud Cowork.*
