---
title: "10 — Risks + mitigations (crypto-tribe perception / gas / KYC / regulatory / etc.)"
date: 2026-05-18
type: risks-mitigations-matrix
F: F3
G: jetix-ethereum-risks-mitigations
R: refuted_if_risk_categories_incomplete_OR_mitigations_inadequate
constitutional_posture: R1 + R6 + EP-5
parent: 00-MASTER-ARCHITECTURE.md
---

# 10 — Risks + mitigations

## §FPF primitives

| Decision | FPF primitive | F-G-R |
|---|---|---|
| Risk-mitigation discipline | `E.5 Guard-Rails` + `B.3 F-G-R` | F4 · risk-mitigation-discipline |
| Pre-mortem awareness | `B.5.2 Abductive Loop` (counter-position discipline) | F4 · pre-mortem |

## §1 Risk matrix overview

| # | Risk | Severity | Likelihood | Mitigation | Section |
|---|---|---|---|---|---|
| **R-01** | Crypto-tribe perception alienates methodology community (ШСМ + SEMAT + INCOSE) | HIGH | MEDIUM | Substrate-utilization framing; Phase 1 off-chain establishment | §2 |
| **R-02** | Russian-jurisdiction crypto regulatory barriers | HIGH | MEDIUM | Phase 1 off-chain accessible all jurisdictions; Russian-resident opt-in Phase 2+; VPN if needed | §3 |
| **R-03** | R12 lock-in paradox via Ethereum substrate | MEDIUM | LOW | Multi-substrate stack; fork-and-leave preserved; substrate-agnostic Foundation principle intact | §4 |
| **R-04** | Friend.tech-style financialization attractor | MEDIUM | LOW | No native fungible token Phase 2+; SBT-only attestation; QF distribution mechanism | §5 |
| **R-05** | Gas cost burden on Workshop participants | LOW | LOW | L2 selection (Base $0.01-0.05); gas sponsorship optional Phase 2+ via ERC-4337 | §6 |
| **R-06** | Smart contract bugs / exploits | HIGH | MEDIUM | OpenZeppelin libraries; external audits; bug bounty; incremental rollout | §7 |
| **R-07** | KYC / privacy / regulatory friction | MEDIUM | MEDIUM | ZK-SBT for sensitive attestations; jurisdiction-specific compliance | §8 |
| **R-08** | Cross-chain considerations + L2 deprecation risk | LOW | LOW | OP Stack «boring» choice; cross-L2 bridges; multi-L2 fallback | §9 |
| **R-09** | Buterin outreach goodwill burn (if attempt fails badly) | MEDIUM | MEDIUM | Substantive material (Phase 3 architecture doc); humility; no over-promising | §10 |
| **R-10** | Pillar C + IP-1 violations during implementation | HIGH | LOW | AWAITING-APPROVAL packets; RUSLAN-LAYER overlay discipline; constitutional preservation tests | §11 |
| **R-11** | DAO voter apathy / governance dysfunction | MEDIUM | MEDIUM | Small-Clan scale (10-100); SBT-gated participation; QV anti-concentration | §12 |
| **R-12** | Crypto-bear market timing risk | LOW | MEDIUM | Phase 2+ timing flexible; can defer without committing | §13 |

---

## §2 R-01 Crypto-tribe perception risk (DETAILED)

**Risk description.** Adopting Ethereum substrate signals «crypto-tribe» identity. Target methodology community (ШСМ + Levenchuk lineage + INCOSE + SEMAT + Cynefin) is largely **NOT crypto-aligned**; some explicitly skeptical (per direction 10 §4.3 con 1).

**Concrete adverse outcomes:**
- L1 (Anatoly Levenchuk + Tseren Tserenov) distance from Jetix collaboration
- Methodology community marks Jetix as «just another crypto project»
- Substance overshadowed by tribal positioning (per Six Sigma loss-of-soul analog direction 07 §3)

**Mitigation stack:**

1. **«Substrate-utilization» framing.** Position Ethereum as **execution substrate selection** (per H8 substrate-agnostic principle preserved); not identity adoption. Communicate: «Foundation = FPF + Pillar C; Ethereum = one substrate option Phase 2+».

2. **Phase 1 establishment off-chain first.** Build methodology community + Charter signatories + Workshop platform **before** Ethereum substrate introduction. By Phase 2+ Ethereum overlay, community substance = clear.

3. **No native token Phase 2+.** SBT-only attestation + QF distribution; no fungible token = no speculation magnetism = no «crypto-tribe» financialization.

4. **m/acc framing deferred.** Per direction 10 §4.4 — m/acc opt-in if Workshop demo strong; Phase 1-2 avoid m/acc tribal positioning.

5. **Methodology community communications.** Explicit messaging к L1 + ШСМ: «Ethereum = substrate option; FPF + Pillar C = identity».

6. **Workshop substance carries.** Pattern Language artefact + Workshop methodology = substance; Ethereum = «under-the-hood plumbing».

**Severity:** **HIGH** — if methodology community distances, Jetix L1 collaboration roadmap (vision/08) breaks.

**Likelihood:** **MEDIUM** — risk real but mitigatable through messaging discipline + Phase 1 off-chain establishment.

---

## §3 R-02 Russian-jurisdiction crypto barriers (DETAILED)

**Risk description.** Russian Federation crypto regulations are restrictive (2024+ central bank stance; partial framework; sanctions risk for cross-border crypto). Russian-resident Workshop participants may face:
- Bank account closure for crypto-fiat conversion
- Tax / regulatory complications
- Coinbase/Base sanctions enforcement (US jurisdiction L2)
- VPN requirements

**Mitigation stack:**

1. **Phase 1 off-chain accessible all jurisdictions.** PGP / Karpathy-wiki-sig substrate = jurisdiction-neutral.

2. **Phase 2+ Ethereum overlay = opt-in.** Russian-resident members can stay on Phase 1 substrate; Ethereum participation = optional.

3. **L2 selection mitigates US-jurisdiction risk.** Optimism (less Coinbase-centralized than Base) as Russian-resident-preferred L2; or Polygon zkEVM (European).

4. **Privacy-preserving via ZK-SBT.** Sensitive attestations ZK-private; mitigates KYC surface.

5. **Off-ramp diversity.** Multiple fiat-on-ramp options; member-self-managed wallet (non-custodial).

**Severity:** **HIGH** — Russian-resident Workshop participants forced offline = Phase 2+ benefit reduced.

**Likelihood:** **MEDIUM** — risk varies by member jurisdiction + sanctions evolution.

---

## §4 R-03 R12 lock-in paradox (DETAILED)

**Risk description.** Adopting Ethereum substrate = potential R12 violation if substrate **becomes default** (substrate-agnostic principle violated). «Cooperative-trap» — members locked into Ethereum-specific tooling, fork-and-leave impossible.

**Mitigation stack:**

1. **Substrate-agnostic Foundation principle preserved.** Foundation Parts MUST NOT mandate Ethereum; Ethereum = RUSLAN-LAYER overlay per IP-1.

2. **Multi-substrate stack maintained.** Phase 1 PGP + wiki-sig **continues** Phase 2+; Ethereum **adds**, not replaces.

3. **Fork-and-leave testing (DRA-T4).** Phase 2+ stress-test: member exits Clan, exports SBT + PGP attestations, joins different Clan or fork. Test substrate portability.

4. **Cross-L2 bridges + non-custodial wallets.** Member holds own wallet; cross-L2 portability mature.

5. **Foundation evolution clause.** Pillar C R12 retains text «members can fork-and-leave without penalty» — operational test continuous.

**Severity:** **MEDIUM** — paradox real but mitigatable; not catastrophic.

**Likelihood:** **LOW** — Foundation principle architecture + multi-substrate stack make hard lock-in unlikely.

---

## §5 R-04 Friend.tech-style financialization attractor (DETAILED)

**Risk description.** Per direction 03 pre-mortem — Friend.tech 2024 collapse showed how friend-network tokenization → speculation → bubble → collapse + community damage. Risk Jetix could attract speculation if tokenization wrong.

**Mitigation stack:**

1. **No native fungible token Phase 2+.** SBT-only attestation + QF distribution; no ERC-20 native Jetix token.

2. **SBT non-transferable by design.** Cannot be bought/sold = no secondary market = no speculation surface.

3. **QF distribution mechanism.** Anti-concentration (sqrt formula) discourages financial concentration; encourages broad participation.

4. **Substance-first messaging.** Workshop graduate value comes from **demonstrated methodology mastery**, not «owning Jetix tokens». No «invest in Jetix» framing.

**Severity:** **MEDIUM** — financialization could harm reputation + community.

**Likelihood:** **LOW** — architectural choices (no native token + SBT-only) substantially reduce surface.

---

## §6 R-05 Gas cost burden (DETAILED)

**Risk description.** Workshop participants paying gas could exclude low-income participants from full DAO participation.

**Mitigation per `07-cost-economy-l2-selection.md` §5:**

- L2 (Base) reduces gas to $0.01-0.05/tx
- Annual active-member cost ~$1.30-3.80 (Base) — negligible vs Workshop revenue ($1K-10K)
- ERC-4337 account abstraction = DAO gas sponsorship for onboarding (Phase 2+ pilot)
- ZK-rollup migration Phase 3+ for further reduction

**Severity:** **LOW** — L2 selection resolves at scale.

**Likelihood:** **LOW** — modern L2 ecosystem mature.

---

## §7 R-06 Smart contract bugs / exploits (DETAILED)

**Risk description.** Smart contract code = financial substrate. Bugs (reentrancy, overflow, access-control issues) = exploit + treasury extraction + community harm. History: numerous DAO/DeFi exploits 2016-2026.

**Mitigation stack:**

1. **OpenZeppelin standard libraries.** Use battle-tested patterns; avoid custom-implementing critical primitives (ERC-20, Access Control, Pausable, Multi-sig).

2. **External audits.** ConsenSys Diligence / Trail of Bits / OpenZeppelin Audits for production contracts (~$50-200K). Phase 2+ budget includes audit.

3. **Incremental rollout.** Pilot deployment with limited treasury exposure (Phase 2+ first months); scale gradually.

4. **Bug bounty program.** Immunefi / similar — pay white-hats to find issues pre-exploit.

5. **Time-locked upgrades.** Critical functions = 7-day delay; allows community response to malicious upgrades.

6. **Multi-sig governance.** Treasury operations require ≥3-of-5 signatures (different parties).

7. **Immutable critical contracts.** Revenue distribution + R12 enforcement = immutable post-audit; reduces upgrade attack surface.

**Severity:** **HIGH** — exploit could drain treasury + reputation damage.

**Likelihood:** **MEDIUM** — even audited contracts have bugs; mitigations reduce but don't eliminate.

---

## §8 R-07 KYC / privacy / regulatory friction (DETAILED)

**Risk description.** Mixing fiat banking (legal entity) + on-chain DAO triggers KYC/AML requirements + GDPR + sanctions compliance + tax reporting per jurisdiction.

**Mitigation stack:**

1. **Legal advisor consult Phase 1.** German GmbH-licensed advisor — MiCA + BAFIN guidance.

2. **ZK-SBT for sensitive attestations.** Privacy-preserving role-attestation = GDPR-aligned («right to be forgotten» harder on-chain but ZK-proof + non-public commitment reduces exposure).

3. **KYC-gated for legal-entity-facing interactions.** Workshop client payment → Corp → DAO. KYC at Corp boundary; DAO members not KYC-required (only Corp clients).

4. **Member self-custody.** Members hold own non-custodial wallets; no KYC at DAO membership level.

5. **Jurisdiction-specific compliance.** Tax reporting at member jurisdiction; Corp handles its share.

**Severity:** **MEDIUM** — regulatory friction real but manageable with discipline.

**Likelihood:** **MEDIUM** — regulatory evolution unpredictable.

---

## §9 R-08 Cross-chain considerations + L2 deprecation risk (DETAILED)

**Risk description.** L2 ecosystem still consolidating Q2 2026. Risk chosen L2 deprecated / governance crisis / sequencer failure.

**Mitigation per `07-cost-economy-l2-selection.md` §3-§4:**

- OP Stack choice (Base / Optimism share tech) — easy migration
- Multi-L2 deployment Phase 2+ optional
- Cross-L2 bridges (Across / Hop / Stargate) mature
- Aragon OSx deployable cross-L2

**Severity:** **LOW** — migration cost real but possible.

**Likelihood:** **LOW** — major L2s (Optimism, Arbitrum, Base) ecosystem-supported.

---

## §10 R-09 Buterin outreach goodwill burn (DETAILED)

**Risk description.** Cold outreach к Buterin (text_007 acceleration) inherently low success rate (per direction 10 §6 Counter 1). Failed outreach + over-promising substance = goodwill burn + reputation damage.

**Mitigation:**

1. **Substantive material carries.** Phase 3 architecture doc + Phase 2 Workshop demo + Foundation v1.0 LOCKED = real artefacts (not vapor).

2. **No over-promising.** Outreach framing: «we're building on Ethereum substrate aligned with d/acc; interested in your reaction»; not «join Jetix team».

3. **Humility posture.** Buterin extremely busy + high inbound; failure = expected baseline.

4. **Alternative engagement paths.** Plurality book community contribution; OP Foundation RetroPGF application; d/aDDy Phase 2+ attendance — multiple engagement paths if direct outreach fails.

5. **Public-channel-only baseline.** Twitter follow + blog comments + Devcon visit = zero-risk engagement; cold-DM = optional escalation.

**Severity:** **MEDIUM** — bad outreach attempt could close door indefinitely.

**Likelihood:** **MEDIUM** — outreach success rate inherently low.

---

## §11 R-10 Pillar C + IP-1 violations during implementation (DETAILED)

**Risk description.** Implementation pressure could lead to expedient shortcuts violating Pillar C / IP-1. Examples:
- Naming specific Ethereum addresses in Foundation Parts (IP-1 violation)
- Skipping AWAITING-APPROVAL for «small» substrate changes (R2 violation)
- DAO autonomous resolution of contradictions (R7 violation)
- AI agent voting in DAO (R9 self-modification surface)

**Mitigation stack:**

1. **AWAITING-APPROVAL discipline enforced.** Any Pillar C / Foundation touch = packet required; brigadier scribe surface; Ruslan acks.

2. **RUSLAN-LAYER overlay discipline.** Ethereum addresses live in `shared/state/ethereum-bindings.yaml` Phase 2+; Foundation Parts unchanged.

3. **Constitutional preservation tests.** Continuous lint per `/lint --check-claude-md-sync`; Pillar C ↔ Default-Deny table sync invariant.

4. **AI-agent advisory only.** DAO delegates = human Souls only; AI = scribe / advisor with B.3 F-G-R provenance.

5. **Multi-sig + time-locked upgrades.** Reduce single-actor mutation surface.

**Severity:** **HIGH** — constitutional violations = Foundation integrity damage.

**Likelihood:** **LOW** — discipline patterns established (8 RUSLAN-ACK records; 4 AWAITING-APPROVAL packets historic).

---

## §12 R-11 DAO voter apathy / governance dysfunction (DETAILED)

**Risk description.** DAO governance well-documented voter apathy (Uniswap, Compound, others 2021+). Phase 2+ DAOs may face same.

**Mitigation:**

1. **Small-Clan scale.** First-Clan 10-100 = high participation rate (cf. Mondragón cooperative engagement rates).

2. **SBT-gated voting.** Only Clan-SBT holders vote — selection pressure for engaged members.

3. **QV mechanism.** Anti-«whale apathy» (large holders not dominant; small contributors weighted).

4. **Federation-level optional.** Cross-Clan votes only when needed; not «every Tuesday at 2pm».

5. **Off-chain deliberation + on-chain vote.** Pol.is or similar for deliberation; on-chain vote = final action.

**Severity:** **MEDIUM** — dysfunction reduces DAO value.

**Likelihood:** **MEDIUM** — depends on community engagement quality.

---

## §13 R-12 Crypto-bear market timing risk (DETAILED)

**Risk description.** Q3-Q4 2026 crypto market state unpredictable. Phase 2+ deployment in bear market = negative perception / community withdrawal / gas spikes.

**Mitigation:**

1. **Phase 2+ timing flexible.** Decision checkpoint P2-D5 gates deployment; can defer.

2. **No native token.** No token-price exposure; Jetix value = Workshop substance.

3. **Stablecoin treasury.** USDC / DAI Phase 2+; reduces ETH-price exposure.

4. **Off-chain Phase 1 + 2 substrate.** Bear market doesn't break methodology distribution.

**Severity:** **LOW** — manageable.

**Likelihood:** **MEDIUM** — crypto cycles inevitable.

---

## §14 Plain English

**12 рисков; критические 4:**

1. **Crypto-tribe perception** (R-01) — методология community может distance. **Mitigation:** «substrate-utilization» framing + Phase 1 off-chain establishment + no native token.

2. **Russian-jurisdiction** (R-02) — Russian-resident members могут испытывать access barriers. **Mitigation:** Phase 1 off-chain accessible всем; Phase 2+ Ethereum opt-in.

3. **Smart contract bugs** (R-06) — code = financial substrate; exploits draining treasury. **Mitigation:** OpenZeppelin + audits + bug bounty + incremental rollout.

4. **Pillar C / IP-1 violations** (R-10) — implementation pressure → constitutional shortcuts. **Mitigation:** AWAITING-APPROVAL discipline; RUSLAN-LAYER overlay; constitutional tests.

**Остальные 8 рисков** — managable через mitigation stacks выше.

**Key principle:** все risks **identified** + **mitigated** + **monitored continuously**. Risk =/= блокер; risk = thing to be aware of + плановать против.

## §15 Open questions

| OQ | Question |
|---|---|
| **OQ-10-1** | Crypto-tribe perception study — Phase 2 design? |
| **OQ-10-2** | Audit budget Phase 2+ — €50K min / €200K target? |
| **OQ-10-3** | Russian-resident-specific tooling — VPN / privacy-L2 / hybrid? |
| **OQ-10-4** | Bug bounty Phase 2+ pricing — Immunefi rates / DAO-funded? |
| **OQ-10-5** | KYC posture for clients vs members — TIER differentiation |

## §16 Counter-positions

- **Counter 1 (eng critic):** «Risk matrix incomplete; missing AI-safety risks» — Mitigation: prompt §6.2 covered AI-substrate R12 + Corrigibility risks; add «AI agent governance» risk Phase 3+ if AI agents participate.
- **Counter 2 (phil critic):** «Risks all mitigatable on paper; reality often different» — Mitigation: F3 grade preserves humility; continuous monitoring; Phase gates allow recalibration.
- **Counter 3 (sys integrator):** «12 risks may be incomplete; emergent risks during deployment» — Mitigation: pre-mortem ongoing; new risks logged + mitigations added; Foundation evolution loop incorporates feedback.

## §17 Sources

- Direction 03 pre-mortem (Stack Overflow + Friend.tech): `research/deepening-2026-05-18/03-failure-stackoverflow-friendtech-pre-mortem.md`
- Direction 10 §4.3-§6 Buterin Counter-positions
- Direction 07 §2.2 SBT discrimination risk + §5 Counter-positions
- MiCA Regulation (EU 2024)
- Russian crypto regulation: Central Bank guidance 2024+
- OpenZeppelin security guides: docs.openzeppelin.com/contracts/4.x/security
- Smart contract exploit history: rekt.news (curated incidents)

**Word count:** ~2580.
