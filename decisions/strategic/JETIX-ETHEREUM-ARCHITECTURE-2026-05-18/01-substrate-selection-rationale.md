---
title: "01 — Substrate selection rationale: why Ethereum, why L2, why not Bitcoin"
date: 2026-05-18
type: substrate-rationale
F: F3
G: jetix-ethereum-substrate-rationale
R: refuted_if_rationale_misrepresents_Ethereum_capabilities_OR_if_Bitcoin_dismissal_unfair
constitutional_posture: R1 surface + R6 + EP-5
parent: 00-MASTER-ARCHITECTURE.md
---

# 01 — Substrate selection rationale: why Ethereum, why L2, why not Bitcoin

## §FPF primitives

| Decision | FPF primitive | F-G-R |
|---|---|---|
| Ethereum-as-substrate (vs Bitcoin) | `A.6.1 U.Mechanism` selection + `A.6.B Boundary Norm Square` | F3 · ethereum-substrate-rationale |
| L2 rollup selection necessity | `B.1.6 Γ_work` (cost-scalability composition) | F4 · l2-cost-scalability |
| Substrate-binding vs agnostic principle | `A.7 Strict Distinction` (Foundation principle vs RUSLAN-LAYER overlay per IP-1) | F4 · ip-1-substrate-binding |

## §1 Why Ethereum (not Bitcoin)

**text_007 ¶2:** «работали бы с биткойном, в душе не ебем, кто это будем работать с биткойном тоже... как раз вот эфир — гениально — как раз вот Jetix работает с эфиром, конечно. Ну и не уровнем ниже.»

**Decoded technically:**

| Substrate | Capability | Jetix fit |
|---|---|---|
| **Bitcoin L1** | Value-transfer + UTXO; no native Turing-complete smart contracts (Script is restricted); BIPs add functionality slowly (Taproot 2021; OP_CAT debate ongoing) | ❌ Insufficient — Jetix needs programmable governance + role-attestation + QF + R12 enforcement |
| **Bitcoin L2 (Lightning / RSK / Stacks)** | Some programmability (RSK EVM-compatible; Stacks PoX); but ecosystem maturity << Ethereum L2; DAO tooling minimal | ⚠️ Possible Phase 3+ option; not Phase 2+ default |
| **Ethereum L1** | Native EVM; mature smart-contract ecosystem; SBT lineage (Buterin/Weyl/Ohlhaver 2022); DAO standards (ERC-721, ERC-1155, ERC-4337 account abstraction); ZK-rollup native | ✅ Fit |
| **Ethereum L2 (Optimism / Arbitrum / Base / Polygon zkEVM)** | All L1 capabilities + 100-1000× cost reduction + faster finality | ✅ Best fit for Phase 2+ deployment |

**«Не уровнем ниже» (text_007 ¶2)** — Ruslan voiced abstraction-level distinction. Bitcoin = transactional layer (value transfer); Ethereum = programmable governance layer. Jetix operates at governance layer; Bitcoin substrate is at wrong abstraction level for Jetix needs.

## §2 Why L2 (not pure L1)

L1 Ethereum gas costs (~$5-50 per transaction depending on congestion) prohibit Workshop participant onboarding scale. L2 rollups (Optimism / Arbitrum / Base / Polygon zkEVM):
- **Cost:** ~$0.01-0.10 per transaction
- **Security:** inherits L1 security (rollup proofs settle to L1)
- **EVM compatibility:** full (smart contracts portable L1 ↔ L2)
- **Ecosystem maturity:** Optimism (2021+); Arbitrum (2021+); Base (Coinbase 2023+; rapidly growing); Polygon zkEVM (2023+)
- **Cross-L2 bridges:** mature tooling (Across, Hop, Stargate); preserves R12 fork-and-leave portability

**Detail L2 selection:** `07-cost-economy-l2-selection.md`.

## §3 Why programmability matters для Jetix

Jetix architectural needs (per Phase 0 14 objects + H8 Octagon + R12 + Workshop revenue):
1. **Role attestation portability** → SBT (non-transferable tokens encoding role claims) → requires programmable substrate
2. **DAO governance Clan + multi-Clan** → smart-contract voting + treasury → requires programmable substrate
3. **Quadratic Funding for Workshop revenue** → on-chain QF mechanism → requires programmable substrate (Tang+Weyl + Gitcoin pattern)
4. **R12 programmable enforcement option** → revenue distribution smart contract with Mondragón 5:1 ratio enforcement → requires programmable substrate
5. **Fork-and-leave preservation** → portable SBT + cross-L2 bridges → requires substrate flexibility

Bitcoin substrate fails on (1)-(5) without significant L2 development cost. Ethereum L2 = production-ready substrate for all 5.

## §4 Substrate-binding vs Foundation principle (IP-1 preservation)

**Critical distinction:** Foundation v1.0 LOCKED 2026-04-28 specifies `U.Role` taxonomy at abstract role-types (per IP-1 Role≠Executor). Specific substrate bindings = **RUSLAN-LAYER overlay** per `shared/schemas/executor-binding.yaml.template`.

**Implication:** Ethereum substrate = **RUSLAN-LAYER overlay binding** for Phase 2+ execution. Foundation Parts MUST NOT name specific Ethereum contract addresses. This preserves IP-1 + substrate-agnostic Foundation principle.

**Risk:** if Ethereum substrate gets coded into Foundation Parts → IP-1 violation + Foundation principle violation. **Mitigation:** all Ethereum-specific contracts referenced through RUSLAN-LAYER binding files (e.g., `shared/state/ethereum-bindings.yaml` Phase 2+).

## §5 Plain English

**Зачем Ethereum, а не Bitcoin?**

Простыми словами:
- **Bitcoin** = «цифровое золото». Хорош для хранения / перевода стоимости. **Не умеет** сложные смарт-контракты (DAO, голосования, программируемые правила).
- **Ethereum** = «программируемые деньги + governance». Умеет всё что Bitcoin + полноценный язык смарт-контрактов (Solidity). На Ethereum построены большинство DAO + DeFi + SBT (Soulbound Tokens).

Jetix требует programmable governance (DAO для Clan координации) + role attestation (SBT для подтверждения роли) + revenue distribution (Quadratic Funding для Workshop). Всё это **возможно на Ethereum**, **не возможно на Bitcoin без L2 разработки**.

**Зачем L2, а не L1?**

L1 Ethereum транзакции стоят $5-50. Workshop participant с зарплатой $50/час не может платить $20 за каждое голосование в DAO. L2 (Optimism / Arbitrum / Base) — это **scaling layer** который наследует security от L1 но снижает gas до $0.01-0.10.

L2 = production-ready substrate для Workshop scale.

**Бitcoin = поездка на Запорожце 1985 года**: едет, но не умеет навигатор, кондиционер, ABS.

**Ethereum L2 = современная машина с полным набором функций**: едет + умеет все нужные Jetix capabilities.

## §6 Open questions

| OQ | Question |
|---|---|
| **OQ-01-1** | Bitcoin L2 (RSK / Stacks) Phase 3+ revisit? |
| **OQ-01-2** | Multi-chain strategy (Ethereum + Solana + Cosmos)? Or Ethereum-only? |
| **OQ-01-3** | If Ethereum suffers governance crisis (e.g., split chain) — fallback substrate? |

## §7 Counter-positions (preserved)

- **Counter 1 (phil critic):** «Ethereum-only = single point of failure». Mitigation: Foundation principle substrate-agnostic preserved; W3C VC v2.0 off-chain Phase 2 baseline; fork-and-leave portability across substrates.
- **Counter 2 (investor scalability):** «Crypto-bear market timing risk». Mitigation: Phase 2+ introduction = no time-sensitive commitment; can be delayed if market signals adverse.
- **Counter 3 (sys integrator):** «Ethereum governance is not Jetix governance». Mitigation: Ethereum substrate for execution layer; Jetix governance per Foundation Pillar C + Clan Charter (independent layers).

## §8 Sources

- text_007 ¶2 verbatim
- Bitcoin script limitations: en.bitcoin.it/wiki/Script
- Ethereum Yellow Paper (Wood 2014+)
- L2 ecosystem maturity: l2beat.com (state of L2s)
- SBT origin: SSRN 4105763 (Weyl + Buterin + Ohlhaver 2022)

**Word count:** ~950.
