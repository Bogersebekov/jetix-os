---
title: Phase 11 — Risk surface per variant
date: 2026-05-21
type: risk-register
phase: 11
parent_prompt: prompts/economic-model-tokenomics-2026-05-21.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F3 analytical
G: economic-model-tokenomics-phase-11-risk-surface
R: refuted_if_per_variant_risks_incomplete_OR_mitigations_strawman_OR_probability_impact_misordered
constitutional_posture: R1 surface + R6 + R12 paired-frame + EP-5 + AP-6 dissent preservation
language: russian primary
---

# Phase 11 — Risk Surface Per Variant

> **Тезис.** Per-variant risk register (10 variants × top 5 risks each) + V10-specific extended risk surface + mitigation strategies + Mermaid D20 quadrant chart probability×impact.

---

## §A Risk taxonomy (8 risk classes)

Per per-variant analysis, 8 risk classes considered:

| Class | Description |
|---|---|
| R1.SCB | Smart contract bug (audit miss / unknown exploit) |
| R2.GAT | Governance attack (whale concentration / 51% / vote-buying) |
| R3.REG | Regulatory issue (BaFin / SEC / MiCA enforcement) |
| R4.LIQ | Liquidity problem (treasury insolvency / RageQuit cascade) |
| R5.R12 | R12 edge case (ratio cap breach / extraction perception) |
| R6.UX | UX complexity (wallet support / partner onboarding friction) |
| R7.CDR | Cohort dropout (retention < threshold / churn cascade) |
| R8.SPC | Token speculation (price volatility / external trader influence) |

---

## §B Per-variant top 5 risks

### §B.1 V1 — Vanilla ERC-20

| Risk | Prob | Impact | Mitigation |
|---|---|---|---|
| R2.GAT (whale governance) | High | High | Off-chain Charter only — weak; consider quadratic vote upgrade |
| R5.R12 (no native ratio cap) | High | Medium | Strict Charter discipline + quarterly audit |
| R8.SPC (DEX speculation) | High | Medium | Limit DEX listing Phase 1; controlled liquidity |
| R6.UX | Low | Low | Universal MetaMask UX |
| R3.REG | Medium | Medium | Securities law opinion per jurisdiction |

### §B.2 V2 — ERC-3643 Compliance + Soulbound

| Risk | Prob | Impact | Mitigation |
|---|---|---|---|
| R6.UX (KYC overhead) | High | High | UX optimization (Persona/Sumsub/Onfido one-tap) |
| R3.REG (still possible) | Medium | High | Tokeny Solutions legal opinion + per-jurisdiction setup |
| R1.SCB (newer standard) | Medium | High | $50-100K audit; OpenZeppelin patterns; multi-audit |
| R7.CDR (KYC friction discourages) | Medium | Medium | Phased KYC (workshop tier optional; partner tier mandatory) |
| R4.LIQ (permissioned = locked) | Low | Medium | Burn-and-redeem mechanic |

### §B.3 V3 — ve-Token

| Risk | Prob | Impact | Mitigation |
|---|---|---|---|
| R2.GAT (vote-bribery market) | High | High | Limit ve-boost curve; soulbound vote weight cap |
| R7.CDR (capital lockup deters new partners) | High | High | Shorter min-lock period (1 week not 1 year) |
| R4.LIQ (locked capital) | Medium | High | Partial unlock options для emergencies |
| R8.SPC (transferable base token) | Medium | Medium | Vest before transferable |
| R6.UX (ve-math complexity) | Medium | Low | Educational materials + UX docs |

### §B.4 V4 — Quadratic Funding + RetroPGF

| Risk | Prob | Impact | Mitigation |
|---|---|---|---|
| R4.LIQ (matching pool sustainability) | High | High | Internal funding source instead of external dep (Gitcoin pattern issue) |
| R2.GAT (Sybil без identity) | High | High | Gitcoin Passport / Worldcoin / BrightID integration |
| R6.UX (QF math complexity) | Medium | Low | UX wrapper + educational |
| R7.CDR (round-by-round coordination) | Medium | Medium | Quarterly cadence + governance discipline |
| R5.R12 (round emergent ratio) | Medium | Medium | Per-round audit |

### §B.5 V5 — Mondragón-style 60/40

| Risk | Prob | Impact | Mitigation |
|---|---|---|---|
| R7.CDR (60/40 rigid, may deter flexibility-seeking partners) | Medium | Medium | Option A/B/C choice per Charter |
| R1.SCB (60/40 routing logic) | Low | High | Standard audit |
| R6.UX (Mondragón abstraction unfamiliar to crypto-native) | Low | Low | Educational positioning |
| R8.SPC (transferable ERC-20 base) | Low | Medium | Soulbound member NFT layer |
| R5.R12 (ratio cap edge cases) | Medium | High | Per-class ratio cap design (see Phase 5 §C.3) |

### §B.6 V6 — Triple-role NFT Bundle

| Risk | Prob | Impact | Mitigation |
|---|---|---|---|
| R6.UX (3 token-ids per partner) | High | Medium | UX wrapper + bundled display + educational |
| R1.SCB (ERC-1155 complexity) | Medium | High | OpenZeppelin reference + multi-audit |
| R2.GAT (per-role weight imbalance) | Medium | Medium | Aggregate cap design + governance review |
| R7.CDR | Low | Medium | Charter explicit + retention discipline |
| R5.R12 (per-role caps) | Low | Medium | On-chain check |

### §B.7 V7 — Reputation + Revenue Hybrid

| Risk | Prob | Impact | Mitigation |
|---|---|---|---|
| R2.GAT (reputation scorer centralization) | High | High | Distributed scoring (peer-rated SourceCred); audit cadence |
| R6.UX (2-token + reputation tracking) | Medium | Medium | UX wrapper |
| R5.R12 (REP threshold gaming) | Medium | Medium | Governance audit |
| R1.SCB (custom REP contract) | Medium | High | Custom audit |
| R7.CDR | Low | Medium | Charter discipline |

### §B.8 V8 — Cooperative DAO + RageQuit (Moloch)

| Risk | Prob | Impact | Mitigation |
|---|---|---|---|
| R4.LIQ (RageQuit cascade drain treasury) | Medium | High | 30-day notice + withdrawal lock period |
| R5.R12 (no native ratio cap) | Medium | Medium | Off-chain Charter |
| R2.GAT (Moloch governance) | Low | Medium | Battle-tested 5+ years |
| R6.UX | Low | Low | DAOhaus UX mature |
| R7.CDR | Low | Medium | RageQuit вентиль relieves dissent pressure |

### §B.9 V9 — ENS-style Domain

| Risk | Prob | Impact | Mitigation |
|---|---|---|---|
| R5.R12 (no ratio cap) | High | High | Off-chain Charter (weak) |
| R4.LIQ (renewal fee revenue volatile) | Medium | Medium | Diversify revenue (Workshop + Cohort + Domain) |
| R8.SPC (subdomain trading possible) | Medium | Medium | Soulbound subdomain restrictions |
| R7.CDR (renewal forget) | Medium | Medium | Renewal reminders + grace period |
| R6.UX (ENS abstraction) | Low | Low | Brand alignment |

### §B.10 V10 — ⭐ Hybrid (most complex)

V10-specific risks expanded в §C below.

---

## §C V10 specific risk surface (extended)

V10 hybrid is most complex variant; risks deserve extended attention.

### §C.1 R1.SCB — Smart contract bug

**Prob:** Medium **Impact:** High

**Details:**
- 5 interacting modules (ERC-1155 + SBT + Moloch + QF + Mondragón router)
- New combo (no battle-tested precedent for full stack)
- Audit budget $75-150K warranted
- Multi-audit strategy required (2-3 firms: OpenZeppelin Audit / Trail of Bits / ConsenSys Diligence / Quantstamp)

**Mitigation:**
- Phased deployment (deploy modules separately Y1; integrate Y2)
- Bug bounty program ($50-100K bounty pool)
- Time-lock + multisig admin (3/5 Ruslan + 2 управленцы + 2 advisors)
- Annual re-audit

### §C.2 R2.GAT — Governance attack

**Prob:** Low **Impact:** High

**Details:**
- V10 hybrid: SBT 1-id-1-vote baseline + QF + delegate optional + reputation thresholds
- Hybrid governance lowers single-attack-vector concentration
- Still possible: identity layer Sybil if не integrated Worldcoin / BrightID

**Mitigation:**
- Identity layer integration Worldcoin Phase 2+ (per V10 default)
- Reputation-weighted proposal thresholds
- 90% supermajority required для constitutional changes
- Bicameral structure (Token House + Citizens' House) Phase 3+ per Optimism pattern

### §C.3 R3.REG — Regulatory issue

**Prob:** Medium **Impact:** High

**Details:**
- V10 has tokens (security classification risk per BaFin / SEC / MiCA EU framework)
- ERC-1155 investor token (token 0x02) likely classified as security
- Soulbound promoter (token 0x03) likely not security (non-transferable + identity-bound)
- Worker NFT (token 0x01) ambiguous

**Mitigation:**
- Legal opinion per jurisdiction (EU + US + Russia + Berlin DE)
- ERC-3643 compliance wrapper Phase 2+ option preserved
- Reg D / Reg S structure для security-classified tokens
- KYC layer optional Phase 1; mandatory Phase 2+

### §C.4 R4.LIQ — Liquidity problem

**Prob:** Low **Impact:** High

**Details:**
- RageQuit cascade risk (multiple simultaneous exits drain treasury)
- Treasury reinvestment ROI < 1.0 sustained → operational deficit
- Workshop pricing not scaling → revenue stagnates

**Mitigation:**
- Withdrawal lock period 30-90 day RageQuit notice
- Proportional cap (max 20% of treasury extractable per quarter)
- Bridge funding Y1-4 ~€245K (per DR-26 Scenario B)
- Treasury reserves minimum 6-month operations target

### §C.5 R5.R12 — Edge case

**Prob:** Low **Impact:** Medium

**Details:**
- Cohort small (<6) → 5:1 ratio cap edge case (per Phase 5 §C.3 edge δ; Phase 6 §9.1)
- Aggregate top partner exceeds 5:1 even with per-role caps
- L2 #управленцы scaling threshold (per Phase 4 §3.3 — >8 управленцев + 5:1 cap)
- Voice Reading α/β/γ/δ ambiguities (Phase 1 §B)

**Mitigation:**
- Cohort threshold gate (relaxed cap при cohort <6 with quarterly review)
- Aggregate cap design + governance 90% supermajority override
- Per-class ratio cap (Ruslan in management class; workers internal — separate)
- R1 explicit decisions to disambiguate

### §C.6 R6.UX — Complexity

**Prob:** High **Impact:** Medium

**Details:**
- Triple-role NFT bundle (3 token-ids per partner) + SBT + utility token
- Wallet display challenges (ERC-1155 + ERC-721 mix)
- Onboarding flow complex (3-mint at sign-up + KYC if Phase 2+)
- Governance UX (SBT + QF + delegate)

**Mitigation:**
- ERC-4337 account abstraction (gasless onboarding + paymaster + session keys)
- Workshop tier paymaster sponsorship Y1 (Jetix subsidizes gas for new partners)
- UX wrapper application с educational onboarding
- Tutorial cohort cycles dedicated к token UX education

### §C.7 R7.CDR — Cohort dropout

**Prob:** Medium **Impact:** Medium

**Details:**
- Closed-loop self-sustaining dependent на retention ρ ≥ 70%
- DXdao 2024 sunset example shows what happens при unsustainable
- Workshop tier student → partner conversion rate key

**Mitigation:**
- Mondragón-spirit cohort culture
- RageQuit available (psychological safety knowing exit option)
- Workshop tier scholarships partial (anti-attrition)
- Partner emergency fund Phase 2+

### §C.8 R8.SPC — Speculation

**Prob:** Low **Impact:** Medium

**Details:**
- Soulbound promoter NFT prevents speculation
- Investor NFT (ERC-1155 token 0x02) transferable с restrictions
- Utility token (ERC-20) transferable + DEX-listable

**Mitigation:**
- 12-month investor NFT lock at onboarding
- Limit DEX listing utility token Y1 (controlled supply)
- Governance vote required для major liquidity events
- Anti-speculation Charter discipline

### §C.9 Integration debt (V10-specific)

5 modules to maintain:
1. ERC-1155 triple-role bundle
2. ERC-5114 SBT identity
3. Moloch DAO RageQuit
4. QF matching pool
5. Mondragón 60/40 router

**Mitigation:** Phased deployment Y1 baseline 3 modules → Y2 add QF + RetroPGF → Y3 add RetroPGF rounds.

### §C.10 Audit cost (V10-specific)

$75-150K Phase 1 audit budget. Likely cover:
- $30-50K base contract audit (single firm)
- $20-30K formal verification (audit firm or specialized)
- $20-40K multi-audit second firm
- $5-20K integration testing + bug bounty
- $5-15K ongoing audit cadence (annual re-audit)

**Mitigation:** Phased audit deployment + bug bounty for ongoing security; budget contingency 20%.

---

## §D Mitigation strategies (cross-cutting)

### §D.1 Constitutional safeguards

- R12 LOCK preserved (this audit + Phase 10)
- Halt-Log-Alert framework (per Part 6b §I.2) on R12 violations
- F-G-R DOGFOOD per claim
- Corrigibility (Ruslan ack authority final)

### §D.2 Programmatic safeguards (V10)

- On-chain ratio cap check
- Soulbound promoter (anti-Sybil)
- RageQuit proportional treasury
- QF matching contribution-aligned
- Time-lock + multisig admin

### §D.3 Governance safeguards

- 90% supermajority для constitutional changes
- Quarterly transparent audit (governance review)
- Bicameral structure Phase 3+ option (Optimism pattern)
- Reputation-weighted proposal thresholds

### §D.4 Operational safeguards

- Workshop tier external market signal
- Multi-audit smart contract strategy
- Bug bounty Phase 1 launch
- Annual re-audit
- Bridge funding Y1-4 reserved

---

## §E Risk-adjusted recommendation

V10 hybrid has **highest absolute risk** (most complex + largest audit budget) **AND highest absolute upside** (strongest R12 + triple-role + closed-loop).

**Risk-adjusted ranking:**
1. **V10 hybrid** — Risk-adjusted **best** if audit budget $75-150K secured + Phased deployment
2. **V5 Mondragón** — Risk-adjusted strong fallback (lower complexity, similar R12 strength minus promoter role)
3. **V8 Moloch RageQuit** — Risk-adjusted lowest-complexity R12-strong (simplest but missing triple-role + ratio cap)
4. **V6 Triple-role** — Risk-adjusted balanced (triple-role native; missing full Mondragón framework)

**Avoid for Phase 1 (risk-adjusted):**
- V1 vanilla (weak R12; high governance attack risk)
- V3 ve-token (capital lockup + bribery risk Phase 1)
- V9 ENS (weak ratio + extraction control)

---

## §F Mermaid D20 — Risk surface quadrant per variant (probability × impact)

```mermaid
quadrantChart
    title V10-specific risks — Probability × Impact (cross-variant comparison)
    x-axis Low_impact --> High_impact
    y-axis Low_probability --> High_probability
    quadrant-1 Top risk priority (high prob + high impact)
    quadrant-2 Monitor (low impact + high prob)
    quadrant-3 Accept (low prob + low impact)
    quadrant-4 Design out (high impact + low prob)
    V10 R6 UX complexity: [0.55, 0.80]
    V10 R5 R12 edge case: [0.45, 0.20]
    V10 R1 smart bug: [0.85, 0.40]
    V10 R2 governance attack: [0.85, 0.15]
    V10 R3 regulatory: [0.80, 0.40]
    V10 R4 liquidity: [0.80, 0.15]
    V10 R7 cohort dropout: [0.55, 0.50]
    V10 R8 speculation: [0.45, 0.15]
    V1 R2 whale governance: [0.85, 0.80]
    V3 R2 vote-bribery: [0.80, 0.75]
    V4 R4 matching pool: [0.75, 0.85]
```

---

## §G R1 decisions pending

| # | Decision | Brigadier provisional | Ruslan R1 |
|---|---|---|---|
| 1 | V10 audit budget allocation ($75-150K range) | $100K Phase 1 | ⏳ |
| 2 | Phased V10 deployment timeline | Y1 baseline / Y2 QF / Y3 RetroPGF | ⏳ |
| 3 | Multi-audit firm selection | OZ + Trail of Bits | ⏳ |
| 4 | Identity layer (Worldcoin / BrightID / Gitcoin Passport)? | Worldcoin lean | ⏳ |
| 5 | Bug bounty pool size | $50-100K | ⏳ |
| 6 | Bridge funding source Y1-4 (~€245K Scenario B) | Foundation / Anthropic / personal | ⏳ |
| 7 | RageQuit withdrawal notice period (30/60/90 days)? | 30-day default | ⏳ |
| 8 | Cohort threshold gate value (relaxed ratio cap below cohort N) | 6 | ⏳ |

---

## §H Cross-refs

- Phase 3 TOKENOMICS-VARIANTS sub-doc per-variant detail
- Phase 4 RECURSIVE-PARTNERSHIP §3.3 #управленцы scaling threshold
- Phase 5 §C.3 ratio cap edge cases α/β/γ/δ
- Phase 6 TRIPLE-ROLE §9 failure modes
- Phase 7 closed-loop dynamics §G sensitivity
- Phase 10 R12 conformance per variant

---

*Phase 11 closure 2026-05-21. Brigadier-scribe Cloud Cowork.*
