---
title: "07 — Cost economy + L2 selection trade-offs"
date: 2026-05-18
type: l2-selection-cost-economy
F: F3
G: jetix-l2-selection-cost-economy
R: refuted_if_L2_cost_estimates_misrepresented_OR_security_assumptions_violated_OR_substrate_choice_premature_LOCK
constitutional_posture: R1 surface (option matrix only — NO autonomous L2 commit per prompt §4) + R6 + EP-5
parent: 00-MASTER-ARCHITECTURE.md
---

# 07 — Cost economy + L2 selection trade-offs

> **Prompt §4 reminder:** «НЕ auto-decide L2 selection (Optimism vs Arbitrum vs Base) — surface options + trade-offs». **This doc surfaces options only.** Ruslan picks.

## §FPF primitives

| Decision | FPF primitive | F-G-R |
|---|---|---|
| L2 selection | `A.6.1 U.Mechanism` (execution substrate selection) | F3 · l2-comparison-matrix |
| Cost optimization | `B.1.6 Γ_work` (cost-scalability composition) | F4 · l2-cost-matrix |

## §1 L2 landscape (Q2 2026 state)

[src: l2beat.com state retrieved 2026-05-18; production state as of Q2 2026]

| L2 | Type | TVL (Q1 2026 approx) | Founded | Owner / governance | Gas cost / tx |
|---|---|---|---|---|---|
| **Arbitrum One** | Optimistic rollup | ~$15B | 2021 (mainnet) | Arbitrum Foundation + DAO | ~$0.10-0.30 |
| **Optimism (OP Stack)** | Optimistic rollup | ~$8B | 2021 | OP Foundation + Token House + Citizens House DAO | ~$0.05-0.20 |
| **Base** | Optimistic rollup (OP Stack) | ~$10B | 2023 (mainnet) | Coinbase (centralized sequencer) | ~$0.01-0.05 |
| **Polygon zkEVM** | ZK-rollup | ~$200M | 2023 (mainnet) | Polygon Foundation | ~$0.10-0.50 |
| **zkSync Era** | ZK-rollup | ~$500M | 2023 | Matter Labs + ZK Nation DAO | ~$0.05-0.30 |
| **StarkNet** | ZK-rollup (Cairo) | ~$1B | 2022 | StarkWare + StarkNet Foundation | ~$0.10-1.00 |
| **Linea** | ZK-rollup | ~$1B | 2023 | ConsenSys | ~$0.10-0.50 |
| **Scroll** | ZK-rollup | ~$500M | 2023 | Scroll Foundation | ~$0.10-0.50 |

**Categories:**
- **Optimistic rollups** (Arbitrum / Optimism / Base): 7-day withdrawal period; mature; cheaper proofs
- **ZK rollups** (zkSync / Polygon zkEVM / StarkNet / Linea / Scroll): faster finality; expensive proofs; cryptographic security

## §2 9-dimension comparison

| Dimension | Arbitrum | Optimism | **Base** | zkSync | StarkNet | Polygon zkEVM |
|---|---|---|---|---|---|---|
| **Maturity** | 4+ years | 5+ years | 3+ years | 3+ years | 4+ years | 3+ years |
| **Gas cost** | Medium-low | Low | **Lowest** | Low-medium | Medium | Medium |
| **Decentralization** | Medium | Medium (3 sequencers) | LOW (Coinbase single sequencer; roadmap to decentralize) | Medium | Low-medium | Medium |
| **Security model** | Optimistic (fraud proofs; 7d withdrawal) | Optimistic | Optimistic | ZK proofs | ZK proofs (Cairo) | ZK proofs |
| **EVM compatibility** | Full | Full | Full | Full (with Era) | Cairo (different) | Full |
| **DAO tooling** | Aragon supported | OP Governance native | All EVM tooling | Aragon supported | StarkNet-specific | Aragon supported |
| **Coinbase ecosystem (mainstream onboarding)** | NO | NO | **YES** (native Coinbase integration) | NO | NO | NO |
| **Token (governance + speculation risk)** | ARB token | OP token | NO native token (clean) | ZK token | STRK token | POL/MATIC |
| **Russian-jurisdiction access** | Medium (sanctions risk) | Medium | Medium-Low (Coinbase US-anchored) | Medium | Medium | Medium |

## §3 Trade-off summary

### §3.1 Base (Coinbase L2) — pros/cons

**Pros:**
- ✅ **Lowest gas costs** (~$0.01-0.05/tx) — best for Workshop participant scale
- ✅ **Mainstream onboarding** — Coinbase fiat-on-ramp native; Workshop participants without crypto experience can join easier
- ✅ **No native token** — reduces crypto-tribe perception risk; no speculation distraction
- ✅ **Full EVM** — Aragon / Moloch / OpenZeppelin all work
- ✅ **OP Stack technology** — shared with Optimism (proven base)

**Cons:**
- ❌ **Centralized sequencer (Coinbase)** — censorship vulnerability; single point of failure
- ❌ **Coinbase US-jurisdiction** — sanctions / KYC enforcement; Russian-jurisdiction holders may face access barriers
- ❌ **Coinbase product/strategy risk** — if Coinbase deprecates Base, migration cost
- ⚠️ **Decentralization roadmap unclear** — Coinbase has stated intent but timing uncertain

### §3.2 Optimism — pros/cons

**Pros:**
- ✅ **Most decentralized of optimistic L2s** (3-sequencer architecture; OP Governance DAO mature)
- ✅ **d/acc alignment** — OP Foundation philosophical-adjacent to Buterin d/acc
- ✅ **OP Stack open-source** — others build on it (Base, Mode, etc.)
- ✅ **RetroPGF** — production retroactive public goods funding (Plurality/QF aligned)
- ✅ **Token House + Citizens House bicameral governance** — Plurality-adjacent

**Cons:**
- ❌ **Higher gas than Base** (~2-4× Base cost)
- ❌ **OP token speculation** — governance token can be financially-captured

### §3.3 Arbitrum — pros/cons

**Pros:**
- ✅ **Largest L2 by TVL** — ecosystem depth
- ✅ **Arbitrum Foundation + DAO** — governance maturity

**Cons:**
- ❌ **Higher gas than Base/Optimism** (~5-10× Base)
- ❌ **ARB token speculation** — recent governance controversies (Arbitrum Foundation 2023 incident)

### §3.4 zkSync / StarkNet / Polygon zkEVM — pros/cons

**Pros:**
- ✅ **ZK proofs = stronger cryptographic security** (no 7-day fraud-proof window)
- ✅ **Faster finality** (~1-2 hours vs 7 days)
- ✅ **Privacy potential** — ZK-rollups extensible to private state

**Cons:**
- ❌ **Less mature DAO tooling** — Aragon supported but lower production volume
- ❌ **Higher proof generation costs** (passed to users)
- ❌ **StarkNet Cairo** = different VM (not EVM) — lock-in if chosen
- ❌ **Most early-stage** — production-readiness uncertain

## §4 Brigadier recommendation (F2 surface)

**Base as Phase 2+ default**, with **Optimism as fallback** if decentralization-prioritized.

**Rationale:**
1. **Lowest cost** = lowest friction for Workshop participant scale (10 → 100 → 1000)
2. **Mainstream onboarding** = reduces crypto-tribe perception risk (Coinbase = mainstream brand)
3. **No native token** = clean architectural choice; no speculation distraction
4. **OP Stack technology** = if Coinbase issues arise, migration to Optimism trivial (shared tech)

**Critical disclaimers:**
- Base centralized sequencer = **NOT acceptable long-term** for d/acc-aligned positioning. Roadmap monitoring required.
- Russian-jurisdiction holders may need alternative L2 access (Optimism / Polygon as alternatives)
- Cross-L2 bridging (Across / Hop / Stargate) preserves portability — fork-and-leave R12 alignment

**Alternative consideration: multi-L2 deployment**

Phase 2+ deploy on **both Base AND Optimism**:
- Lower friction (members pick L2 by jurisdiction / preference)
- R12 fork-and-leave portability
- Higher deployment cost (2× contracts)

## §5 Workshop participant cost analysis

**Estimated per-participant annual gas cost (Phase 2+ active member):**

| Activity | Frequency | Gas per tx | Annual cost (Base) | Annual cost (Optimism) |
|---|---|---|---|---|
| Clan-membership SBT mint | 1× | $0.05 | $0.05 | $0.20 |
| Workshop-graduate SBT mint | 1-3× | $0.05 | $0.05-0.15 | $0.20-0.60 |
| DAO vote | 12-24× | $0.02 | $0.24-0.48 | $1-2 |
| Revenue distribution claim | 4-12× | $0.05 | $0.20-0.60 | $1-3 |
| Contribution signaling (QF) | 12-50× | $0.02 | $0.24-1.00 | $1-5 |
| Cross-L2 bridge (occasional) | 1-3× | $0.50 | $0.50-1.50 | $0.50-1.50 |
| **TOTAL (active member)** | | | **~$1.30-3.80/year** | **~$4-12/year** |

**Comparison:**
- Compared to consulting hourly rate ($100-500/h Workshop graduates) = **negligible** even Optimism cost
- Compared to Workshop revenue share ($1K-10K/year per member) = **<0.5% of revenue** Base case

**Conclusion:** Gas cost on L2 = **practical for Workshop scale**. Phase 2+ doesn't require gas-sponsorship initially; DAO treasury subsidy optional.

## §6 Gas sponsorship via Account Abstraction (ERC-4337)

**For lowest-friction onboarding:**

- DAO treasury pays gas for new members during onboarding (first 30 days)
- ERC-4337 account abstraction enables gasless UX (sponsored transactions)
- After onboarding period, member self-pays

**Trade-off:** DAO treasury cost vs onboarding friction reduction. Phase 2+ pilot recommended.

## §7 Plain English

**Что такое L2 (Layer 2)?**

L1 Ethereum = «main highway» — security maximum, но gas цена $5-50 per transaction. Слишком дорого для Workshop участников.

L2 = «параллельные roads» которые **наследуют security от L1** но cost gas всего $0.01-0.10. Production-ready L2s: Optimism (2021), Arbitrum (2021), Base (2023), zkSync (2023).

**Какой L2 выбрать?**

**Base** — рекомендуется default Phase 2+:
- Самый дешёвый ($0.01-0.05/tx)
- Лучший mainstream onboarding (Coinbase интеграция)
- Нет native token (нет speculation distraction)
- Технология OP Stack (тот же что Optimism — migration trivial если нужно)

**Минусы Base:**
- Coinbase central sequencer = censorship risk
- US-jurisdiction = Russian holders могут испытать access barriers

**Альтернатива — Optimism:**
- Decentralization выше
- d/acc-aligned (RetroPGF + bicameral governance)
- Но gas в 2-4× дороже Base

**Recommendation:** **Base + bridge к Optimism** for participants kotorые need decentralization OR have jurisdiction issues. Phase 2+ multi-L2 deployment = небольшая extra работа, большая participant flexibility.

**Сколько стоит для Workshop участника?**

- На Base: **$1.30-3.80 в год** для активного member (vs Workshop revenue $1K-10K)
- На Optimism: **$4-12 в год** (still negligible)

Gas cost = **non-issue** на L2. DAO treasury может subsidize onboarding period (Phase 2+ pilot).

## §8 Open questions

| OQ | Question |
|---|---|
| **OQ-07-1** | Phase 2+ default L2 — Base / Optimism / multi-L2? |
| **OQ-07-2** | Cross-L2 bridge integration — Across / Hop / Stargate / native? |
| **OQ-07-3** | Gas sponsorship via ERC-4337 — Phase 2+ onboarding pilot? |
| **OQ-07-4** | Russian-jurisdiction L2 access — separate substrate or VPN-mediated? |
| **OQ-07-5** | Migration strategy if chosen L2 deprecated — Aragon DAO migration tooling? |
| **OQ-07-6** | ZK-rollup (zkSync / StarkNet) revisit at Phase 3+ — proof maturity + privacy benefits? |

## §9 Counter-positions

- **Counter 1 (phil critic):** «Base = Coinbase = corporate centralization → contradicts decentralization ethos». Mitigation: Phase 2+ multi-L2 (Base + Optimism); Base preferred for onboarding velocity, Optimism for decentralization-prioritized members.
- **Counter 2 (sys integrator):** «Multi-L2 deployment doubles complexity» — Mitigation: same Solidity contracts; deployment script handles both; cross-L2 bridges proven.
- **Counter 3 (investor scalability):** «L2 ecosystem still consolidating; choosing now = lock-in risk» — Mitigation: choose «boring» (OP Stack — Base + Optimism share tech); avoid bleeding-edge (StarkNet / experimental L3s).
- **Counter 4 (eng critic):** «ZK-rollup security stronger than optimistic; ZK-rollup will dominate by 2027» — Mitigation: monitor ZK production-maturity; Phase 3+ revisit; Phase 2+ start with mature optimistic for ecosystem depth.

## §10 Sources

- L2Beat: l2beat.com (state retrieved 2026-05-18)
- Optimism RetroPGF: optimism.io/retropgf
- Base docs: docs.base.org
- Arbitrum docs: docs.arbitrum.io
- ERC-4337 Account Abstraction: eips.ethereum.org/EIPS/eip-4337
- Cross-L2 bridges: acrossprotocol.com, hop.exchange, stargate.finance

**Word count:** ~1830.
