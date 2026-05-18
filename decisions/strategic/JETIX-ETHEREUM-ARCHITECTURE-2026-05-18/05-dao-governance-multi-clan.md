---
title: "05 — DAO governance для multi-Clan coordination"
date: 2026-05-18
type: dao-governance-architecture
F: F2
G: jetix-dao-multi-clan-governance
R: refuted_if_DAO_governance_pattern_incompatible_with_Pillar_C_Tier_2_OR_concentration_risk_unmitigated
constitutional_posture: R1 + R6 + EP-5
parent: 00-MASTER-ARCHITECTURE.md
---

# 05 — DAO governance для multi-Clan coordination

## §FPF primitives

| Decision | FPF primitive | F-G-R |
|---|---|---|
| Single-Clan DAO governance | `U.System` (A.1) holon + `A.2.7 RoleAlgebra` Clan-level | F3 · single-clan-dao |
| Multi-Clan composition | `B.2 MHT` (Meta-Holon Transition: Clan holons → multi-Clan supersystem) | F3 · multi-clan-mht |
| DAO governance evolution | `B.4 Canonical Evolution Loop` per DAO + Foundation Pillar C consent | F3 · governance-evolution |
| Anti-concentration mechanism | `E.5 Guard-Rails` (Pillar C R12) + `B.3 F-G-R` | F4 · anti-concentration |

## §1 DAO framework options

### §1.1 Aragon OSx (recommended Phase 2+ default — F2 surface)

**Production maturity:** Aragon = 2017+ original; OSx = 2024+ modular re-architecture.

**Architecture:**
- DAO contracts modular (Solidity facets pattern)
- Plugin system for governance modules (token voting / multi-sig / custom)
- Permissions framework granular
- Used in production: 1000+ DAOs deployed

**Jetix fit:**
- ✅ Plugin system allows custom Jetix governance modules (e.g., F-G-R-attested votes; R12-enforcement plugin)
- ✅ Mature audit history
- ✅ Not locked-in (DAOs are owned by their members; Aragon can stop without breaking DAOs)
- ✅ Cross-L2 deployable

**Concerns:**
- Solidity complexity (Diamond-like pattern; learning curve)
- Aragon company sustainability long-term

[src: aragon.org docs retrieved 2026-05-18]

### §1.2 Moloch v3 (Coalition-friendly alternative)

**Production maturity:** 2019+ (v1); v3 2023+.

**Architecture:**
- Member-share voting (ERC-20 share token)
- «RageQuit» mechanism = built-in fork-and-leave (members can exit with proportional treasury share)
- Simple Solidity contracts (less complex than Aragon)
- Used by: MetaCartel, MetaGov, others

**Jetix fit:**
- ✅ **RageQuit = direct R12 fork-and-leave alignment** — built-in protocol-level mechanism
- ✅ Simpler contracts = easier audit
- ✅ Member-share aligned to contribution

**Concerns:**
- Less modular than Aragon (fewer plugin options)
- Member-share model may not fit Jetix Workshop revenue distribution (QF model)

### §1.3 Coordinape Circles (peer-reward pattern, not full governance)

**Production maturity:** 2021+; production-grade.

**Architecture per direction 07 §2.5:**
- Epoch-based GIVE/GET token allocation
- Circle = NFT-gated membership
- Peer allocations → reward distribution

**Jetix fit:**
- ⚠️ Not full governance — peer-reward mechanism only
- ✅ Useful as **pattern reference** для Workshop revenue distribution (per direction 07 §2.5 recommendation: «borrow Coordinape epoch-peer-reward pattern without locking к Coordinape substrate»)
- ⚠️ Ethereum lock-in if used as substrate

### §1.4 Custom Solidity (long-tail option)

**Concerns:**
- Audit cost ($50-200K)
- Maintenance burden
- Less battle-tested

**Recommendation:** Use only if Aragon + Moloch insufficient for Jetix-specific needs. Phase 3+ consideration.

### §1.5 Brigadier comparison summary (F2 surface)

| Framework | Modularity | Maturity | R12 fork-and-leave | Audit cost | Recommendation |
|---|---|---|---|---|---|
| **Aragon OSx** | HIGH | 2024+ (OSx) | Configurable (plugin) | Free (audited stack) | **Default Phase 2+** |
| **Moloch v3** | MEDIUM | 2023+ (v3) | **Native RageQuit** | Free (audited) | Alternative if RageQuit prioritized |
| **Coordinape** | LOW (peer-reward only) | 2021+ production | Not applicable | Free | **Pattern reference**, not substrate |
| **Custom Solidity** | HIGH | New | Custom-implement | $50-200K audit | Defer to Phase 3+ |

---

## §2 Multi-Clan DAO architecture

### §2.1 Single-Clan DAO

**Pattern:**
- 1 Aragon DAO per Clan (10-100 members)
- SBT-gated membership (only Clan-SBT holders can vote)
- Plugin: Quadratic Voting (Tang+Weyl) — small contributions weighted more heavily
- Plugin: R12 enforcement (revenue distribution + RageQuit-style fork-and-leave)
- Treasury holds Workshop revenue

### §2.2 Multi-Clan «Federation»

**Pattern (per CONCEPT-MAN-AS-ARMY §7.1 Stage 2-3):**
- Each Clan = 1 Aragon DAO (independent treasury + governance)
- Federation = «meta-DAO» where each Clan delegates 1 representative
- Federation governs:
  - Cross-Clan disputes (R12 violations between Clans)
  - Shared infrastructure costs (Foundation maintenance + Workshop platform)
  - Inter-Clan SBT recognition (Clan A graduate SBT recognized by Clan B?)
- Federation does NOT govern:
  - Individual Clan internal decisions (preserves R12 + autonomy)
  - Workshop curriculum per Clan
  - Revenue distribution within Clan

### §2.3 Federation voting mechanism

**Surface options (Ruslan picks):**

| Mechanism | Description | Pros | Cons |
|---|---|---|---|
| **One Clan, one vote** | Each Clan = 1 vote in Federation | Simple; equality | Doesn't reflect Clan-size or contribution |
| **Quadratic Voting (delegate-weighted)** | Each delegate gets vote weight ∝ sqrt(Clan-size) | Anti-concentration; small Clans not drowned | Sybil-resistance via SBT-gated Clans |
| **F-G-R reliability weighted** | Vote weight ∝ Clan's R-grade reliability score | Quality-weighted; incentivizes high-reliability | Complex; F-G-R aggregation challenge |
| **Hybrid (QV + reliability)** | (QV) × (R-grade factor) | Best of both | Most complex |

**Brigadier inference (F2):** **Quadratic Voting** as Phase 2+ default; **Hybrid** as Phase 3+ refinement.

### §2.4 Mermaid: Multi-Clan DAO governance

**Full diagram:** `diagrams/04-dao-clan-governance.md`.

---

## §3 Constitutional preservation

### §3.1 Pillar C Tier 2 R7 (no negotiate contradictions autonomously without human gate)

**Risk:** DAO autonomous governance could autonomously resolve cross-Clan contradictions, violating R7.

**Mitigation:**
- Federation governance scope limited to **defined contract** functions (not arbitrary discussions)
- Cross-Clan disputes escalate to human-review (Ruslan ack OR multi-Clan delegate consensus)
- Foundation Pillar C preserved as **out-of-DAO-scope** (DAO cannot amend Pillar C)

### §3.2 IP-1 Role≠Executor preservation

**Risk:** DAO addresses could become «executor instances» named in Foundation Parts → IP-1 violation.

**Mitigation:**
- Foundation Parts MUST NOT name DAO contract addresses
- DAO addresses live in RUSLAN-LAYER overlay (`shared/state/ethereum-bindings.yaml` Phase 2+)
- Foundation references abstract `U.Role` types only

### §3.3 R12 anti-extraction preservation

**Risk:** DAO governance majority could extract value from minority (51% attack).

**Mitigation:**
- Quadratic Voting weakens 51% attack (anti-concentration)
- RageQuit (Moloch-style fork-and-leave) preserves exit option
- Revenue distribution contract enforces Mondragón 5:1 cap (per `03-r12-programmable-enforcement.md`)
- Federation governance scope explicitly excludes Clan internal R12 enforcement

### §3.4 Corrigibility (Pillar C Tier 2 rule 9 — AI does NOT self-modify at runtime)

**Risk:** DAO upgradeable contracts = potential «AI self-modification» surface if DAO governance includes AI-agent delegates.

**Mitigation:**
- DAO delegates = human Souls only (not AI agents)
- AI-agent participation = advisory/scribe role (FPF B.3 F-G-R provenance attested)
- Critical contract upgrades = multi-sig + time-locked (7-day delay)

---

## §4 Plain English

**Что такое DAO в Jetix?**

DAO = **Decentralized Autonomous Organization** — это организация управляемая через smart contracts на blockchain. Вместо CEO + Board решают **держатели токенов** (или членских SBT) через голосования.

**Структура Jetix DAO:**
- **Per-Clan DAO** — каждый Clan = собственный DAO. Голосует по: revenue distribution / curriculum / new member admissions / Workshop scheduling
- **Federation meta-DAO** — все Clan-DAOs делегируют представителей. Голосует по: cross-Clan disputes / shared infrastructure / cross-Clan SBT recognition

**Какой framework использовать?**

**Aragon OSx** (recommended Phase 2+ default):
- Production-ready (1000+ DAOs)
- Modular (plugins для custom governance)
- Не lock-in (DAO принадлежит участникам)

**Альтернативы:**
- **Moloch v3** — proще; built-in RageQuit (fork-and-leave) — direct R12 alignment
- **Coordinape** — только peer-reward (не full governance); полезен **как pattern** для Workshop revenue

**Сохраняется ли Pillar C?**

**ДА.** DAO scope ограничен **defined contract functions**. Cross-Clan disputes / Pillar C amendments / strategic decisions — **escalate к human review** (Ruslan ack или multi-Clan delegate consensus). DAO **не** заменяет Foundation governance; **дополняет** на execution layer.

**Privacy:**
- DAO votes могут быть **public** (default) — для transparency
- ZK-voting опционально для sensitive votes (Buterin/d/acc-aligned)

## §5 Open questions

| OQ | Question |
|---|---|
| **OQ-05-1** | Aragon OSx vs Moloch v3 — Phase 2+ default? |
| **OQ-05-2** | Federation voting mechanism — QV / one-Clan-one-vote / hybrid? |
| **OQ-05-3** | Federation scope — what decisions are Federation vs Clan? |
| **OQ-05-4** | DAO delegate selection — direct election / rotation / appointment by Clan? |
| **OQ-05-5** | AI agent participation in DAO — advisory only / voting / forbidden? |
| **OQ-05-6** | Treasury currency — ETH / stablecoin / multi-currency? |
| **OQ-05-7** | Cross-Clan SBT recognition — automatic / per-Federation-vote / per-Clan opt-in? |

## §6 Counter-positions

- **Counter 1 (phil critic):** «DAO governance = formalization of cooperation → may freeze evolution». Mitigation: Pillar C preserved out-of-DAO-scope; B.4 evolution loop continues via Foundation review.
- **Counter 2 (sys integrator):** «Multi-Clan Federation = supersystem risk; emergence of central authority». Mitigation: Federation scope explicitly limited; rotation of delegates; QV anti-concentration.
- **Counter 3 (investor scalability):** «DAO audit + tooling cost not justified pre-Workshop revenue». Mitigation: Phase 2+ timing assumes Workshop revenue established; use open-source Aragon (no custom audit needed initially).
- **Counter 4 (eng critic):** «DAO voter apathy is well-documented» (Compound, Uniswap, others). Mitigation: small-Clan scale (10-100 members) = participation rate higher; QV reduces «whale apathy»; SBT-gated voting requires active membership.

## §7 Sources

- Aragon OSx docs: aragon.org/aragon-osx
- Moloch v3: github.com/HausDAO/Molochv3-contracts
- Coordinape docs: docs.coordinape.com
- Quadratic Voting (Posner+Weyl 2017): radicalxchange.org/concepts/quadratic-voting/
- Multi-DAO governance patterns: various (gitcoin.co, optimism.io governance)

**Word count:** ~1450.
