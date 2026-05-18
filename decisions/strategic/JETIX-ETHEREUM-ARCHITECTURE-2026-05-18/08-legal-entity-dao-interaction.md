---
title: "08 — O-02 Corporation + DAO interaction architecture"
date: 2026-05-18
type: legal-entity-dao-interaction
F: F2
G: jetix-legal-entity-dao-interaction
R: refuted_if_legal_entity_dao_interaction_incompatible_with_R12_OR_if_tax_jurisdiction_unmitigated
constitutional_posture: R1 + R6 + EP-5 (legal/tax discipline — surface options; Ruslan + legal advisor pick)
parent: 00-MASTER-ARCHITECTURE.md
---

# 08 — O-02 Corporation + DAO interaction architecture

> **Critical disclaimer:** This doc surfaces architecture options. Jurisdictional / tax / regulatory decisions require **licensed legal advisor** consultation. Brigadier surface only — NOT legal advice.

## §FPF primitives

| Decision | FPF primitive | F-G-R |
|---|---|---|
| Legal entity O-02 (Doc 1B Corporation) | `U.RoleAssignment` (A.2.1) + `U.PromiseContent` (A.2.3) + Doc 1B v0 LOCKED | F4 (concept) / F2 (realization — 0 entity registered) |
| DAO holds treasury | `U.System` (A.1) execution-layer holon | F3 · dao-treasury |
| Legal-DAO bridge | `A.6.B Boundary Norm Square` (boundary between legal entity + DAO) + `A.7 Strict Distinction` | F2 · legal-dao-bridge |

## §1 The architectural question

**Jetix Corporation (O-02 Phase 0 inventory)** = future legal entity (vapor; not yet registered). Per Doc 1B Corporation narrative + JETIX-CORPORATION-2026-05-05.

**Ethereum architecture introduces DAO** (Phase 2+ overlay).

**Question:** How do legal entity + DAO coexist? 4 architectural patterns:

### Pattern A — Legal entity holds everything, no DAO

Traditional: Corp registered (German UG / GmbH / Liechtenstein Stiftung / Cayman foundation). Bank account holds revenue. Operational decisions by Corp directors.

**Pros:** Clear legal substrate; mature tax/compliance; banking access.

**Cons:** No on-chain composability; doesn't realize Ethereum architecture benefits; doesn't natively support fork-and-leave; centralized.

**R12 alignment:** Weak (depends entirely on Corp directors' R12-discipline).

### Pattern B — DAO-only, no legal entity

Pure on-chain. DAO holds treasury; smart contracts execute revenue distribution; members = SBT holders.

**Pros:** Native R12 enforcement; fork-and-leave native; transparent.

**Cons:** Banking access limited (no fiat-on-ramp without intermediary); legal liability unclear (Wyoming DAO LLC + Marshall Islands DAO acts emerging but immature); B2B contracts require legal counterparty.

**R12 alignment:** Strong (programmable).

### Pattern C — Legal entity + DAO **hybrid (RECOMMENDED — F2 surface)**

Pattern: Legal entity (O-02 Corporation registered) holds bank account + signs B2B contracts + handles tax compliance. DAO (Ethereum L2) holds operational treasury + governs revenue distribution + executes R12 enforcement.

**Bridge:**
- Legal entity's bank receives client payments (fiat)
- Legal entity converts fraction to ETH/USDC → transfers to DAO treasury
- DAO governs distribution via QF + R12 enforcement
- Legal entity withholds tax + handles regulatory compliance for its share

**Pros:**
- ✅ Banking access (fiat-on-ramp)
- ✅ B2B contracts viable (Corp = signing party)
- ✅ R12 programmable enforcement (DAO layer)
- ✅ Fork-and-leave preserved (DAO membership independent of Corp)
- ✅ Tax compliance manageable (Corp-level accounting)

**Cons:**
- ⚠️ Complexity (2 entities to maintain)
- ⚠️ Trust assumption (Corp directors must transfer to DAO faithfully)
- ⚠️ Jurisdictional choice critical

**R12 alignment:** Strong (DAO programmable + Corp R12-text-committed).

### Pattern D — Foundation entity + DAO (Plurality-style)

Pattern: Non-profit Foundation (Liechtenstein Stiftung / Swiss Verein / German gGmbH) holds IP + brand. DAO holds operational treasury + governance. Members contribute to both.

**Pros:** Foundation non-extractive structure aligns R12; DAO + non-profit Foundation = «Plurality book» model.

**Cons:** Non-profit may not fit «consulting revenue» Phase 1 plans (commercial vs charitable distinction).

**Brigadier inference:** **Pattern C (Hybrid)** Phase 2+ recommended. Pattern D revisit Phase 3+ if Workshop revenue → primarily methodology distribution (non-commercial).

---

## §2 Jurisdictional options

### §2.1 Germany (UG / GmbH)

**Pros:** Ruslan resident; familiar; Mittelstand DACH market (per Doc 1B); EU regulatory clarity (MiCA framework crypto regulation 2024).

**Cons:** Corporate tax ~30% (high); EU bureaucracy; banking-crypto restrictions some banks.

**MiCA (Markets in Crypto-Assets Regulation, 2024+):** EU crypto regulation. DAO entities not directly covered; SBT non-financial = NOT regulated as crypto-asset; Workshop revenue token ↔ fiat = financial service surface. **Legal advisor consult needed.**

### §2.2 Liechtenstein Stiftung (Foundation)

**Pros:** Stiftung = traditional non-profit holding structure; aligned с Plurality + Ethereum Foundation precedents; political-neutrality; English-language legal.

**Cons:** Establishment cost ~CHF 30K-50K; ongoing CHF 5-10K/year; not commercial-revenue-focused (charitable orientation).

**Use case:** Phase 3+ if Jetix evolves toward methodology-distribution non-profit (Plurality model).

### §2.3 Cayman Islands (Foundation / Limited Liability Company)

**Pros:** Standard crypto-native jurisdiction (Ethereum Foundation, MakerDAO trust, others); 0% corporate tax; LLM/Foundation structures mature for DAO.

**Cons:** «Offshore tax haven» perception risk; counter-d/acc «transparency» principle; political risk if regulatory shift.

**Use case:** Phase 2+ if commercial-DAO-hybrid prioritized + tax-optimization-acceptable.

### §2.4 Marshall Islands DAO LLC (2022 DAO Act)

**Pros:** First jurisdiction with explicit DAO legal recognition; 0% tax; cheap (~$5K setup).

**Cons:** Reputational concerns (small island, less prestige); compliance evolving.

**Use case:** Pure DAO-only (Pattern B) if chosen.

### §2.5 Wyoming DAO LLC (2021 DAO Supplement)

**Pros:** US jurisdiction (Coinbase/Base alignment); explicit DAO LLC structure.

**Cons:** US tax + reporting; sanctions/Russian-holder access barriers.

### §2.6 Brigadier recommendation (F2 surface)

**Phase 1-2:** Germany UG (Ruslan-resident; familiar; cheap ~€500 setup; Mittelstand DACH alignment per Doc 1B).

**Phase 2+:** German GmbH (when revenue >€50K/year — UG conversion mandatory) + Cayman Foundation (for DAO holding structure; political-neutrality).

**Phase 3+:** Revisit Liechtenstein Stiftung if methodology-distribution non-profit emerges.

**Legal advisor consult required.**

---

## §3 Revenue flow (Pattern C hybrid)

```
1. Client pays Workshop ($10K fiat)
   ↓
2. Jetix UG / GmbH receives in bank account
   ↓
3. Jetix UG / GmbH withholds:
   - VAT (19% Germany — €1900)
   - Corporate tax provisioned (~€2500)
   - Operating expenses (rent / tools / etc.)
   → Net ~€5600 to DAO
   ↓
4. Jetix UG / GmbH converts €5600 → USDC (via licensed crypto-fiat ramp)
   ↓
5. USDC transferred to DAO treasury (Ethereum L2 — Base)
   ↓
6. DAO smart contract triggered:
   - QF distribution calculated (per `06-quadratic-funding-workshop-revenue.md`)
   - Mondragón 5:1 ratio cap enforced (per `03-r12-programmable-enforcement.md`)
   - Distribution to member wallets
   ↓
7. Members withdraw USDC → fiat (per-member basis, jurisdiction-specific tax)
```

**Variant (cheaper / less compliant):** Skip step 4 (fiat → USDC conversion at Corp level); members invoice Corp directly for share. **Trade-off:** simpler accounting but loses programmable R12 enforcement.

---

## §4 Constitutional preservation

### §4.1 IP-1 Role≠Executor

**Risk:** Legal entity directors named in Foundation Parts = IP-1 violation.

**Mitigation:** Foundation Parts name abstract `U.Role` types (director-role, treasurer-role); specific persons + Ethereum addresses = RUSLAN-LAYER overlay.

### §4.2 R12 anti-extraction

**Risk:** Corp directors extract value via Corp-level salaries / dividends before DAO transfer.

**Mitigation:**
- Corp directors compensation **bounded by Mondragón ratio** (5:1) at Corp level
- DAO transfer schedule = predictable + auditable (e.g., monthly + public)
- Corp accounting transparency (annual audit + DAO publication)

### §4.3 Corrigibility (Pillar C Tier 2 rule 9)

**Risk:** Corp directors could refuse DAO transfers → effectively control treasury extraction.

**Mitigation:**
- Articles of Association include **DAO-transfer obligation** clauses
- Multi-director structure (≥3) with rotation
- Annual audit + DAO ack on Corp accounting
- Worst-case: DAO can fork-and-leave (start new Corp with different directors)

---

## §5 Plain English

**Зачем нужны legal entity + DAO одновременно?**

Простыми словами — **«юр.лицо для внешнего мира; DAO для внутреннего governance»**.

**Без legal entity (только DAO):**
- ❌ Клиенты не могут заплатить fiat (нет банка)
- ❌ B2B контракты невозможны (DAO не может подписывать legal documents в большинстве jurisdictions)
- ❌ Налоги: серая зона; risk регуляторных проблем

**Без DAO (только legal entity):**
- ❌ R12 enforcement через trust директоров (слабее)
- ❌ Fork-and-leave невозможен (Corp = иерархическая структура)
- ❌ Transparency ограничена annual report

**Hybrid (Pattern C — recommended Phase 2+):**
- ✅ Legal entity = «лицо для внешнего мира» (banking + B2B + compliance)
- ✅ DAO = «internal governance + R12 enforcement» (programmable + transparent + fork-and-leave)

**Аналогия:** Mondragón имеет cooperatives (юр. структура) + Sociedad Cooperativa (membership / governance структура). Два слоя; cooperatives = legal interface к external world; membership structure = internal governance + ratio cap.

**Юрисдикция?**

Phase 1-2: **Germany UG** (cheap ~€500 setup; Ruslan resident; Mittelstand market alignment).

Phase 2+: **GmbH** (mandatory when revenue >€50K) + **Cayman Foundation** (для DAO holding; political-neutrality).

Phase 3+: revisit **Liechtenstein Stiftung** если methodology distribution non-profit.

**Главное:** **Legal advisor consultation REQUIRED.** Этот doc = architecture surface, не legal advice.

---

## §6 Open questions

| OQ | Question |
|---|---|
| **OQ-08-1** | Phase 1-2 entity — UG / GmbH / Stiftung / other? |
| **OQ-08-2** | Pattern A / B / C / D — hybrid recommended; Ruslan confirms? |
| **OQ-08-3** | MiCA implications для Workshop revenue tokenization — legal advisor consult |
| **OQ-08-4** | Russian-tax-residency members — fiat-to-DAO routing? |
| **OQ-08-5** | Foundation IP (FPF + Pattern Language) — Corp-held / Foundation-held / DAO-held? |
| **OQ-08-6** | Director rotation mechanism — Annual / on-vote / fixed-term? |
| **OQ-08-7** | Tax-optimization vs perception risk — onshore vs offshore? |

## §7 Counter-positions

- **Counter 1 (mgmt critic):** «Hybrid complexity may overwhelm Phase 2 small-scale operations» — Mitigation: Phase 1 entity setup simple (UG €500); DAO introduction Phase 2+ after revenue established.
- **Counter 2 (investor scalability):** «Multi-entity tax complexity costs > benefits at first-Clan scale» — Mitigation: Phase 1 UG only; Phase 2+ Foundation only when DAO treasury justifies. Incremental complexity.
- **Counter 3 (phil critic):** «Legal entity = central authority contradicts decentralization principle» — Mitigation: legal entity = «interface к external world» (banking + B2B); internal governance = DAO. Pattern C = best-of-both.
- **Counter 4 (sys integrator):** «Tax compliance risk = central failure mode; can shut down operation» — Mitigation: legal advisor diligence Phase 1; multi-jurisdiction Phase 2+ (fallback if one jurisdiction fails).

## §8 Sources

- Doc 1B Corporation: `decisions/JETIX-CORPORATION-2026-05-05.md`
- MiCA Regulation (EU 2024): eur-lex.europa.eu/eli/reg/2023/1114
- Marshall Islands DAO Act 2022: rmi-attorneys.com (search «DAO Act»)
- Wyoming DAO Supplement 2021: wyoleg.gov
- Mondragón structure: research/deepening-2026-05-18/06-success-mondragon-68yr-mechanism.md
- Ethereum Foundation Liechtenstein Stiftung: ethereum.foundation/about

**Word count:** ~1700.
