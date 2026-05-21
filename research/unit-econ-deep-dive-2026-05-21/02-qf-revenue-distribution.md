---
title: DR-26 Phase 2 — Quadratic Funding (QF) + Revenue Distribution Mechanics
date: 2026-05-21
type: research-substrate
parent_prompt: prompts/dr-26-unit-econ-deep-dive-2026-05-21.md
phase: 2
F: F4
G: dr-26-phase-2-qf-mechanics
R: refuted_if_QF_formula_misstated_OR_R12_overlay_incompatibility_unflagged_OR_distribution_math_wrong
constitutional_posture: R1 + R6 + R12 + IP-1 STRICT + EP-5 + append-only
prose_authored_by: brigadier-scribe (Cloud Cowork — autonomous Phase 2 substrate compile)
language: russian primary
---

# DR-26 Phase 2 — QF + Revenue Distribution Mechanics для Jetix

> **Цель Phase 2.** Зафиксировать QF math basics + cooperative variant + Jetix-specific revenue distribution mapping + compatibility с R12 programmable Ethereum substrate (ack 2026-05-18 Option D Hybrid).

---

## §1 QF (Quadratic Funding) math basics

### §1.1 Origin + canonical paper

**Authors:** Vitalik Buterin (Ethereum Foundation) + Zoë Hitzig (Harvard) + E. Glen Weyl (Microsoft Research / RadicalXChange).
**Paper:** «Liberal Radicalism: A Flexible Design For Philanthropic Matching Funds» (NBER WP 2018; arXiv:1809.06421) [src: Buterin, Hitzig, Weyl 2018]

**Core principle:** funding should be proportional к **square of sum of square roots of individual contributions**, не proportional к total dollars contributed.

### §1.2 Canonical formula

For project p with contributions {c_1, c_2, ..., c_n} from n distinct contributors:

```
F(p) = (Σ √c_i)² 
```

The «matching» amount allocated from matching pool:

```
M(p) = F(p) − Σc_i = (Σ √c_i)² − Σc_i
```

Total funding для project p:

```
Total(p) = Σc_i + M(p) = (Σ √c_i)²
```

### §1.3 Worked example

**Project A:** 1 contributor gives $100 → F = (√100)² = $100; matching $0; total $100.
**Project B:** 100 contributors give $1 each (total $100) → F = (100 × √1)² = $10,000; matching = $10,000 − $100 = $9,900; total $10,000.

**Same total contribution ($100); 100× difference в matched funding because of contributor count.**

Это формула favores broad-base contribution (community signal), penalizes concentrated wealth.

### §1.4 Matching pool sourcing

QF requires external matching pool funded by:
- Foundation / institutional donor (Optimism Foundation / Ethereum Foundation / Gitcoin matching round sponsors)
- Protocol fees redirected к matching pool (Gitcoin GTC + Optimism sequencer fees)
- Member contribution в shared pool (cooperative variant)

**Without matching pool QF degenerates к Σ c_i (linear funding).** Pool size determines QF's amplification effect.

---

## §2 QF в cooperative context (Gitcoin precedent)

### §2.1 Gitcoin Grants iteration history

- **GR1 (Feb 2019):** $25K matching pool; 38 projects; ~$163K total funded [src: Gitcoin GR1 round report]
- **GR15 (Sep 2022):** $4M+ matching pool; 1,000+ projects [src: Gitcoin GR15 results]
- **Beta rounds 2024:** Optimism / Allo Protocol / specific ecosystem rounds [src: Gitcoin docs 2024]

### §2.2 Modifications for cooperative use

Gitcoin layered modifications over canonical QF:

1. **Pairwise-bonded matching (COCM)** — Connection-Oriented Cluster Matching (Buterin 2022) attenuates collusion: matching reduced for contributors that historically vote together [src: Buterin blog 2022 «Pairwise coordination subsidies»]
2. **Gitcoin Passport** — identity layer reducing Sybil attacks (anti-extraction defence) [src: Gitcoin Passport docs 2022-2024]
3. **Project verification** — KYC / KYB-light verification для recipients [src: Gitcoin Grants Stack docs]
4. **Round-specific eligibility criteria** — per-round constraints (geographic / sector / value-aligned) [src: Gitcoin round configurations]

### §2.3 Lessons for Jetix QF application

| Pattern | Jetix application |
|---|---|
| **Matching pool from take rate** | Jetix institutional take rate → matching pool for Workshop / Hackathon / Clan-level initiatives |
| **COCM cluster attenuation** | Defends against Clan-level collusion в matching distribution |
| **Identity layer (Passport-like)** | Per Pillar C R12 fork-and-leave + member identity attested via Clan Charter signature |
| **Round-specific eligibility** | Jetix per-round criteria (cohort progression / mastery milestones / Clan endorsement) |

---

## §3 Revenue distribution model для Jetix — design space

### §3.1 Revenue source taxonomy

**Possible Jetix revenue sources Phase 1-3:**

1. **Workshop / Hackathon participation fees** — direct cohort subscription
2. **Consulting + advisory** — short-term high-margin work (per `crm/_schema/strategy-hooks.yaml` baseline)
3. **Educational artifact licensing** — content + methodology to institutions
4. **Foundation / grant funding** — external matching pool source
5. **Investment / capital raise** — equity-like (per Distribution Plan §0.2 1M/$1B EOY 2026 KEYSTONE)
6. **Member subscriptions** — recurring Clan membership fees
7. **Open-source / public goods recipient** — Gitcoin / Optimism RetroPGF qualification

### §3.2 Revenue split skeleton (proposed; subject to Phase 5 sensitivity refinement)

Below skeleton parametrises «take rate» as **T** (variable for sensitivity); «retention rate» as **R** (Mondragón pattern ~50% retention); «matching pool» as **M** (cooperative QF analogue); «direct member payout» as **D**.

```
Revenue from any source = 100%

Member-direct distribution: D = (1 - T) %
Institutional take rate: T %
  T = R (retention для reinvestment / R&D / Workshop scaling)
    + M (matching pool для QF-style cohort initiatives)
    + O (Foundation operating budget — Ruslan + brigadier + infrastructure)

T = R + M + O
```

### §3.3 Three sub-skeleton variants

**Variant A — Mondragón-style mostly-retention:**
- T = 25%; R = 15%; M = 5%; O = 5%
- Member-direct D = 75%
- Heavy reinvestment loop; matching pool small; operations lean

**Variant B — Gitcoin-style mostly-matching:**
- T = 15%; R = 3%; M = 7%; O = 5%
- Member-direct D = 85%
- Light reinvestment loop; matching pool larger; operations lean
- Requires external matching pool supplement

**Variant C — Federation-balanced:**
- T = 20%; R = 8%; M = 7%; O = 5%
- Member-direct D = 80%
- Balanced reinvestment + matching + operations

### §3.4 Cooperative ownership stake (per Clan / per member)

Per H7 People-NS L1-L6 ladder + R12 Tier 2:

- Member contribution → reputation token (non-transferable, per DXdao REP precedent)
- Member contribution accumulates over time → ownership weight в Clan governance
- Member exit (R12 fork-and-leave) — preserves contribution history + proportional treasury share (via R12 programmable Option D)
- Cross-Clan recognition — federation-level reputation portable

**Take rate ≠ ownership stake** — take rate is institutional retention при revenue flow; ownership stake = governance / treasury claim. Separate but linked.

---

## §4 Implementation considerations

### §4.1 On-chain vs off-chain

| Aspect | Off-chain (Phase 1 Charter) | On-chain (Phase 2+ Ethereum Option D) |
|---|---|---|
| **Take rate enforcement** | Charter text + member ack; institutional culture (Mondragón-style) | Smart contract enforces split at distribution time |
| **Matching pool QF** | Manual round operation; centralized treasury | Allo Protocol-style automated round + on-chain QF distribution |
| **R12 fork-and-leave** | Charter exit clause; institutional honor | RageQuit-style smart contract |
| **Mondragón ratio cap** | Charter wage-ratio cap; member-democratic enforcement | Smart contract caps max-payout = min-payout × ratio_param |
| **Cost** | $0 + governance overhead | $50-200K audit + L2 gas fees + ongoing maintenance [per R12 programmable ack §6] |
| **Reversibility** | High (Charter amendable) | Lower (smart contract upgrade-gated via multi-sig 3-of-5 + 7-day time-lock per R12 programmable ack §6) |
| **R12 alignment** | Subject to institutional drift (Mondragón Eroski caveat) | Programmable guarantee Phase 2+ |

**Recommendation Phase 1:** Off-chain Charter discipline (Pillar C-aligned). **Phase 2+:** Migrate к Ethereum Option D Hybrid (per R12 programmable ack); Clan-level opt-in.

### §4.2 Distribution cadence

- **Per-Workshop:** distribute revenue at end-of-Workshop (week / month)
- **Per-Quarter:** institutional treasury distribution (R+M+O)
- **Per-Year:** annual Mondragón-style member surplus distribution + Foundation review

### §4.3 Variable take rate gradient

Per Distribution Plan cascade (150 → 15 → 1M) — Jetix scale matters:

- **Phase 1 (5-15 founding cohort):** higher institutional take rate justifiable (Foundation-building cost; reinvestment-heavy)
- **Phase 2-3 (50-150 active members):** moderate take rate (steady-state cohort flow + matching pool building)
- **Phase 4-5 (1500+ federation):** lower take rate viable (federation efficiency + external matching pool achievable + scale economics)

**Piecewise gradient:** 25% Phase 1 → 20% Phase 2-3 → 15% Phase 4-5 → 10% post-EOY-2026 KEYSTONE.

Mondragón ratio cap remains constant (e.g., 5:1 wage spread) regardless of phase.

---

## §5 Compatibility с R12 programmable Ethereum substrate (acked 2026-05-18 Option D Hybrid)

### §5.1 R12 programmable enforcement stack

Per `swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md` Option D Hybrid:

1. **Mondragón ratio cap** — smart contract enforces max-share ≤ min-share × ratio_param (default 5:1; Clan-configurable)
2. **Quadratic Funding (Tang+Weyl)** — QF formula for revenue distribution с anti-concentration property
3. **Fork-and-leave exit tokens** — RageQuit-style member exit с proportional treasury share preserved

### §5.2 Default-Deny table additions (per ack §4)

4 new RUSLAN-LAYER action classes (Phase 2+ overlay):

- `r12_smart_contract_deploy` — F5 blast-radius; ack + Clan opt-in + audit gates
- `r12_dao_revenue_distribute` — F4; quorum + ratio cap check
- `r12_fork_and_leave_execute` — F4; member request + 30-day notice + circuit breaker
- `r12_smart_contract_upgrade` — F5; multi-sig 3-of-5 + 7-day time-lock + DAO quorum

### §5.3 Compatibility matrix Jetix Revenue Distribution vs R12 Option D Hybrid

| Jetix revenue mechanism | R12 Option D component | Compatibility |
|---|---|---|
| Institutional take rate (T) split into R + M + O | Smart contract distribution split; immutable params per round | ✅ Direct |
| Matching pool QF (M component) | Tang+Weyl QF formula; Gitcoin Passport identity layer | ✅ Direct (per ack §2 Option B) |
| Member direct payout (D = 1-T) | Smart contract distribution to member addresses; Mondragón ratio cap | ✅ Direct (per ack §2 Option A) |
| Member exit (R12 fork-and-leave) | RageQuit / treasury share preserved | ✅ Direct (per ack §2 Option C) |
| Variable take rate (Phase 1-5 gradient) | DAO-configurable distribution params per round; multi-sig upgrade | ✅ via upgrade-gated mechanism |
| Per-Clan opt-in | Each Clan deploys own enforcement contract | ✅ per ack §3.2 |

**Conclusion:** Proposed Jetix revenue distribution model fully compatible с R12 programmable Option D Hybrid. No new extraction vectors beyond those already mitigated per ack §6.

### §5.4 Extraction vector check (new — Phase 2 specific)

| New vector | Mitigation |
|---|---|
| Variable take rate gradient (T_phase_1 vs T_phase_4) increases at Foundation discretion | Multi-sig 3-of-5 + 7-day time-lock + DAO quorum для upgrade; Charter-stated gradient locked at Clan creation |
| Matching pool QF concentration via sybil attack | Gitcoin Passport identity layer + COCM cluster attenuation |
| Mondragón ratio param manipulation | Charter-stated cap; immutable params per round; upgrade requires multi-sig + time-lock |
| Off-chain to on-chain migration period | Phased rollout; Clan-level opt-in; Charter discipline Phase 1 → smart contract Phase 2+ |

---

## §6 Open questions for Phase 4 + Phase 5

1. **Ratio cap parameter:** Mondragón historical 4-9:1; what for Jetix? Likely 5:1 Phase 1 conservative; 4:1 если more cooperative-aligned. Phase 5 sensitivity dependent.
2. **Matching pool source Phase 1:** before Ethereum substrate live, matching pool funded from where? Foundation operating treasury? External (Anthropic / VC / Foundation)?
3. **Reputation token mechanic:** how Jetix mints/tracks contribution-tokens off-chain Phase 1?
4. **Per-Workshop vs per-Quarter cadence:** member cash-flow expectations vs institutional planning rhythm.

---

## §7 Closure Phase 2

QF math + cooperative variant + Jetix revenue distribution skeleton (3 variants — Mondragón-style retention-heavy, Gitcoin-style matching-heavy, federation-balanced) compiled. On-chain vs off-chain implementation tradeoffs documented. Compatibility с R12 programmable Ethereum Option D Hybrid (acked 2026-05-18) verified across 6 mechanisms; no new extraction vectors beyond those already mitigated.

**Working hypothesis для Phase 5 sensitivity:** T = 15-25% range; split-skeleton variants C (balanced) или A (Mondragón-retention) most plausible defaults; gradient (Variant C → Variant B post-scale) potentially superior.

**Commit:** `[dr-26] Phase 2 QF + revenue distribution mechanics`

---

*Phase 2 closure 2026-05-21. F4 / G: dr-26-phase-2-qf-mechanics / R: refuted_if_QF_formula_misstated_OR_R12_overlay_incompatibility_unflagged_OR_distribution_math_wrong.*
