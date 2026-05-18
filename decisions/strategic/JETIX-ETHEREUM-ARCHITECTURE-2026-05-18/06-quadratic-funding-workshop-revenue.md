---
title: "06 — Quadratic Funding для Workshop revenue distribution (Tang+Weyl/Buterin pattern)"
date: 2026-05-18
type: quadratic-funding-revenue-distribution
F: F2
G: jetix-quadratic-funding-workshop-revenue
R: refuted_if_QF_mechanism_violates_R12_OR_creates_Sybil_attack_surface_unmitigated_OR_scale_unsuitable_for_first-clan
constitutional_posture: R1 + R6 + EP-5
parent: 00-MASTER-ARCHITECTURE.md
---

# 06 — Quadratic Funding (QF) для Workshop revenue distribution

## §FPF primitives

| Decision | FPF primitive | F-G-R |
|---|---|---|
| QF for Workshop revenue | `U.PromiseContent` (A.2.3) + `B.3 F-G-R` (claim provenance) | F3 · qf-workshop-revenue |
| Anti-concentration | `E.5 Guard-Rails` (Pillar C R12) | F4 · anti-concentration |
| Plurality + cooperation | `A.16 U.Episteme` shared + `U.Commitment` (A.2.8) | F3 · plurality-mechanism |

## §1 Quadratic Funding origin (Buterin/Hitzig/Weyl 2018)

[src: arxiv.org/abs/1809.06421 «Liberal Radicalism: A Flexible Design for Philanthropic Matching Funds»]

**Mechanism:** Matched-pool funds distribute weighted by **square of sum of square-roots of contributions**:
```
matching_for_project_i = (Σ_j sqrt(contribution_j_to_i))²
```

**Key property:** **Small contributions weighted disproportionately**:
- 1 person × $100 → 1 × sqrt(100) = 10 → 10² = 100 matching units
- 10 people × $10 each → 10 × sqrt(10) ≈ 31.6 → 31.6² ≈ 1000 matching units (10× the matching)

**Anti-concentration:** Single large contributor cannot dominate matching; distributed small contributors mirror «cooperative behavior» signal.

**Production deployments:** Gitcoin Grants (15+ rounds, ~$50M distributed, 2020+); Optimism RetroPGF; CLR.fund.

## §2 Jetix Workshop revenue distribution patterns

### §2.1 Workshop revenue context

**Per Phase 0 inventory + Workshop Concept v2:**
- Workshop = «мастерская» where information-substrate is processed
- Participants = Clan members + paying clients (Phase 2+)
- Revenue source = client payments for Workshop output + paid mentorship + consulting derivatives
- R12 constraint: «no extraction beyond agreed share»

### §2.2 Distribution mechanism options

| Option | Mechanism | R12 alignment | Complexity |
|---|---|---|---|
| **A — Equal split** | revenue / member count | Strong (equal share) | Lowest |
| **B — Proportional to hours** | revenue × hours / total hours | Medium (hours measurement reliable?) | Medium |
| **C — Mondragón 5:1 ratio cap** | flexible distribution within ratio | Strong | Medium |
| **D — Quadratic Funding** | matched pool + contributor-weighted | Strong + anti-concentration | High |
| **E — Coordinape epoch peer-reward** | members allocate GIVE → GET conversion | Strong + peer-judged | Medium |
| **F — Hybrid (QF + Mondragón ratio cap)** | QF distribution × ratio cap | Strongest | Highest |

**Brigadier inference (F2 surface):** **Hybrid (Option F)** for Phase 2+ — most R12-aligned + anti-concentration + bounded.

### §2.3 Hybrid (QF + Mondragón cap) mechanism

**Step 1 — Workshop revenue event** (e.g., client pays $10K for Workshop session):
- Revenue enters smart contract treasury

**Step 2 — Member contribution signaling** (each Workshop participant signals):
- «I contributed to this project» (with magnitude — hours / quality / role)
- Signaling = peer-weighted (other members confirm)

**Step 3 — QF matching calculation** (smart contract):
- Apply QF formula to contributor signals
- Generate proposed distribution

**Step 4 — Mondragón ratio cap enforcement**:
- Verify max-share / min-share ≤ 5:1
- If violation → re-distribute excess from max to min proportionally

**Step 5 — Distribution execution**:
- Smart contract transfers to member wallets
- Event log emitted (Evidence Graph A.10)

### §2.4 Sybil resistance

QF Sybil attack: fake contributor accounts inflating sqrt(contributions) per project.

**Mitigations:**
1. **SBT-gated participation:** only Clan-membership SBT holders can signal contributions
2. **F-G-R reliability weight:** signals × R-grade factor
3. **Peer attestation:** signals require ≥1 peer co-sign
4. **Stake requirement:** signalers stake small SBT-bond; lost if peer-reviewed as Sybil

### §2.5 Mermaid: Workshop revenue → QF distribution

**Full diagram:** `diagrams/03-quadratic-revenue-flow.md`.

---

## §3 R12 alignment analysis

**R12 Tier 2 rule:** «No extraction beyond agreed share».

| R12 sub-rule | QF satisfies? | Notes |
|---|---|---|
| **No single party dominates value capture** | ✅ YES (sqrt formula anti-concentration) | Strongest property of QF |
| **Members can fork-and-leave** | ✅ YES (per-distribution event, no lock-in to mechanism) | RageQuit-style mechanism alongside |
| **Substrate-agnostic** | ⚠️ PARTIAL — QF can be off-chain (Mondragón hybrid) or on-chain (Gitcoin) | Phase 2 baseline = off-chain; Phase 2+ overlay = on-chain |
| **Transparent + auditable** | ✅ YES (formula deterministic; signals on-chain) | Audit-friendly |
| **Anti-extraction enforcement** | ✅ YES (programmable cap; Mondragón ratio) | Hybrid Option F |

**Net:** QF is **R12-aligned**. Hybrid Option F = strongest fit.

---

## §4 Scale considerations

**First-Clan (10 members, Phase 2):**
- QF formula works but data-thin (10 contributors → less statistical signal than Gitcoin Grants 10K+ contributors)
- **Brigadier recommendation (F2):** start with **Mondragón 5:1 ratio + equal-base + small-bonus** for first-Clan; introduce QF at 100-member scale (Phase 2)

**Phase 2 (100 members):**
- QF more meaningful with statistical depth
- Pilot QF for Workshop revenue distribution

**Phase 3 (1000+ members):**
- Full QF mainstream
- Coordinape-pattern peer-reward as supplementary signal

---

## §5 Plain English

**Что такое Quadratic Funding (QF)?**

Простыми словами — **«механизм где маленькие contributions взвешиваются непропорционально много»**.

Пример:
- Сценарий A: **1 миллиардер дал $100K** → matching pool добавляет ~$10K
- Сценарий B: **100 человек дали по $10 каждый ($1K total)** → matching pool добавляет ~$10K

В обоих сценариях matching = одинаковая, **но**:
- Сценарий A: 1 голос (1 рука)
- Сценарий B: 100 голосов (100 рук)

QF **награждает «100 рук»** больше чем «1 миллионная рука». Это **anti-concentration mechanism**.

**Почему это важно для Jetix?**

Workshop revenue distribution через QF =:
- **R12 anti-extraction aligned** (не один master захватывает весь revenue)
- **Anti-Sybil через SBT** (только real Clan-members могут signal contributions)
- **Auditable** (on-chain formula deterministic)
- **Bounded** (Mondragón 5:1 ratio cap гарантирует max/min не превышает 5:1)

**Использование в Phase 1 / 2:**

- **Phase 1 (10 members):** **Mondragón ratio + equal-base** (QF data-thin для 10 contributors)
- **Phase 2 (100 members):** **QF pilot** для Workshop revenue
- **Phase 3 (1000+):** **Full QF + Coordinape supplement**

**Аналогия Gitcoin Grants:** Gitcoin Grants раздаёт $5M+ каждый round через QF; 15+ rounds; production-grade. Jetix может **borrow pattern** + customize.

## §6 Anti-Sybil discipline

**Sybil attack:** один человек создаёт 100 fake accounts → signals contributions → QF formula gives 100× matching.

**Jetix anti-Sybil stack:**
1. **SBT-gated participation:** только Clan-SBT holders могут signal (1 SBT per real Soul)
2. **F-G-R weight:** signals × R-grade (новые/unverified Souls = lower weight)
3. **Peer attestation:** signal requires ≥1 co-sign from established Soul
4. **Stake requirement:** signaler stakes bond; lost if peer-reviewed as Sybil
5. **Historical pattern analysis:** off-chain ML detects suspicious signal patterns (Phase 3+)

**Net:** multi-layer anti-Sybil makes attack expensive and detectable.

## §7 Open questions

| OQ | Question |
|---|---|
| **OQ-06-1** | Matching pool funding source — % of revenue / external grants / DAO mint? |
| **OQ-06-2** | First-Clan distribution mechanism — Mondragón / QF / hybrid? |
| **OQ-06-3** | Signal granularity — binary (contributed yes/no) / continuous (hours) / qualitative (role-weighted)? |
| **OQ-06-4** | Distribution frequency — per-project / monthly epoch / quarterly? |
| **OQ-06-5** | Cross-Clan QF (multi-Clan revenue events) — Federation-mediated? |
| **OQ-06-6** | Off-chain QF computation + on-chain settlement (cheaper) vs full on-chain? |

## §8 Counter-positions

- **Counter 1 (mgmt critic):** «QF complexity makes participation friction-y» — Mitigation: UX-design priority; off-chain signal UI + on-chain settlement; SBT-gated reduces decision surface.
- **Counter 2 (eng critic):** «QF Sybil attacks at first-Clan scale (10 members) trivially detectable, but mitigations don't scale to 10000» — Mitigation: layered anti-Sybil; future ZK-attestation possible.
- **Counter 3 (sys integrator):** «QF over-rewards small contributors who may be free-riders» — Mitigation: SBT-gated + peer attestation + F-G-R weight together filter free-riders.
- **Counter 4 (phil critic):** «QF imports specific Plurality political philosophy; may not fit all Jetix contexts» — Mitigation: QF = one option; Coordinape / Mondragón alternatives available; hybrid recommended.

## §9 Sources

- Buterin/Hitzig/Weyl 2018: arxiv.org/abs/1809.06421
- Gitcoin Grants production: gitcoin.co/grants
- CLR.fund: clr.fund
- Optimism RetroPGF: optimism.io/retropgf
- Tang+Weyl Plurality (direction 11): `research/deepening-2026-05-18/11-people-tang-weyl-plurality-2024.md`
- Direction 06 Mondragón: `research/deepening-2026-05-18/06-success-mondragon-68yr-mechanism.md`
- Coordinape: docs.coordinape.com

**Word count:** ~1290.
