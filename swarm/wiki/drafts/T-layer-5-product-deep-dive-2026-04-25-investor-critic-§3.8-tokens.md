---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: §3.8
direction: Tokens / ICO (D23 Option B)
type: layer-deep-dive-section
mode: critic
author: investor-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - {path: "decisions/JETIX-VISION.md", range: "§5 D23 token economy + §8 Investor angle + §13 Phase timeline + Note 5 engineering-faith + 200-year vision"}
  - {path: "decisions/JETIX-PLAN.md", range: "§1 revenue-gated unlocks + §3.1 Phase 1 objectives"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§5 Alliance Option C Hybrid + §5.X brigadier recommendation + §11 Evolution per gate"}
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", range: "§3 D23 lock table + §L5 Product & Services Tokens row"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md", range: "§2 Tokens row + §6 Gates table"}
  - {path: "reports/review_2026-04-24.md", range: "audio_511 rows 681-682 (tokens/ICO) + audio_527 row 693 (reverse-engineering on max)"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§3 structural advantages + §5 Path A/B/C"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md", range: "§3 direction 8 tokens + §7 cell distribution"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/decomposition.md", range: "C-10 acceptance predicate"}
word_count_estimate: ~2050
confidence: medium
confidence_method: judgment + base-rate + regulatory-survey
escalations: []
dissents:
  - claim: "Token should never launch — consulting + educational + licensing + strategic-equity fund growth sufficiently without it"
    F: F4
    ClaimScope: applies if Jetix reaches $100M+ through consulting/product/alliance without needing alternative liquidity mechanism
    R:
      refuted_if: specialist-compensation friction becomes operational blocker above $10M ARR (cross-border payments + delayed comp remain unsolved)
      accepted_if: Phase-3+ review at $100M ARR confirms consulting revenue alone sustains all specialist compensation needs without token infrastructure
---

# §3.8 Tokens / ICO — D23 Option B

> **Critic-mode framing.** This draft is produced under `mode: critic`. Arithmetic and risk analysis precede any promotional narrative. The acceptance predicate from C-10 cell is applied throughout. Explicit dissents are preserved. The goal of this section is not to sell the token concept — it is to produce a rigorous design basis that Ruslan can either approve or reject with full information. Per D23: «design safe + adequate + thoughtful; explicitly NOT crypto-pump style». [src:decisions/JETIX-VISION.md §5 Decision 23]

---

## 1. Mission

The Token / ICO direction (Decision 23, Option B) is **Jetix's optionality layer for ecosystem-coordination economics** at Phase-3+ scale: an internal utility token for specialist compensation and складчина tool-pooling, plus a limited-public security-token layer as an alternative to traditional IPO. Design constraint from the founding lock is absolute and non-negotiable: *«Это все должно быть не какая-то там ебаная пирамида или еще что-то, блядь. Нет. А реально адекватные инструменты, наработки, блядь, технологий»* [src:decisions/JETIX-VISION.md §14 Note 5]. The token is infrastructure for Jetix's growing ecosystem of specialists, Alliance members, and strategic partners — it is not a speculative vehicle and will not be positioned as one.

---

## 2. Phase Activation

**This direction is NOT active in Phase 1 or Phase 2 (G0→G2).** It exists in Phase 1 and 2 as a named concept only. No design effort, no legal consultation, zero engineering hours. The revenue-gated discipline of D15 [src:decisions/JETIX-PLAN.md §1 revenue-gated unlocks] is explicit: the token economy is downstream of operational revenue, not a shortcut around it.

**Activation triggers — two distinct layers:**

| Layer | Trigger | Gate | Status 2026-04-25 |
|---|---|---|---|
| Design exploration begins | $100K self-earned revenue threshold met | G2 internal | Not triggered; €0 revenue today |
| Internal utility token launch | Phase-3 (G3→G4, $1M→$100M) + Alliance Foundation incorporated (L6 Option C acked) + legal counsel retained | G3→G4 | Requires ~€200K+ gate passage first |
| Public token layer | Phase-3+ (G4→G5, $100M→$1T) + regulatory clarity + board-equivalent approval | G4→G5 | Requires full Phase-3+ maturity |

The $100K self-earned trigger is confirmed across sources [src:decisions/JETIX-VISION.md §13 Phase timeline: «Mid-Phase-1 trigger ($100K ≈ €95K self-earned, Decision 23) — token economy exploration начинается (design + architecture)»] and [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §2 Tokens row: «trigger: $100K self-earned internal utility»].

**Disqualifier for any launch (hard stop).** Any token structure that produces speculative-instrument characteristics — retail ICO mechanics, pump-oriented community outreach, unregistered public offering — is disqualified per D23 verbatim. This is not a preference; it is a founding-document constraint binding every future design decision.

---

## 3. Target ICP Mapping — L6 Trinity

Per the L6 Trinity framework [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §2 ICP Trinity]:

**Internal utility token (Phase-3, G3→G4):**
- **Primary recipients:** Jetix specialists (roy-replication partners, matchmaker-aligned specialist pool per D21) who provide complex services to Jetix clients but do not fit traditional employment structures. The core problem the token solves for this group: cross-border payment friction, delayed compensation, and the abstraction of equity vesting that does not match specialist-contractor relationships.
- **Secondary recipients:** Alliance Foundation members (post L6 Option C incorporation per [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5.X brigadier recommendation]) contributing methodology improvements and open-surface publications.
- **Складчина use-case:** Secure Network members pooling tool-access costs (Perplexity Max, Claude subscriptions, research tools) denominated in token units rather than cash transfers. This is the lowest-friction internal utility use-case and the best argument for launching the token before the public layer.

**Public security-token tier (Phase-3+, G4→G5):**
- **Accredited investors and strategic corporate partners only.** Per JETIX-VISION §8 Investor angle: *«Phase 2+ token economy (Decision 23) как alternative-to-IPO liquidity path — design safe, adequate, thoughtful; internal utility Phase 2, limited public Phase 3+»* [src:decisions/JETIX-VISION.md §8]. No general retail access at Phase-3+.
- **Corporation partnerships** per audio_515 references signal the strategic-partner profile: complex enterprise clients who might convert transactional consulting relationships into equity-adjacent participation.

**Explicit anti-ICP (non-negotiable per D23):**
- Crypto-pump believers and retail day-traders seeking 10x in 30 days.
- MLM-adjacent or pyramid-scheme operators.
- Any participant whose primary motivation is token price appreciation rather than ecosystem participation.

---

## 4. Value Proposition

### Internal utility token — the specialist-compensation problem

**Problem stated from specialist perspective:** A specialist contributing high-quality work to Jetix ecosystem projects (engineering, research, sales, philosophy) faces three friction points: (1) cross-border wire transfers involve 2-5% fees and 3-7 day delays; (2) consulting invoices create tax complexity in multiple jurisdictions; (3) traditional equity vesting (4-year cliff structures) does not fit specialists who participate episodically across multiple roys, not as full-time employees.

**Token as solution:** The token denominates specialist contribution and provides four redemption paths: (a) hold for ecosystem appreciation as Jetix revenue scales; (b) apply toward складчина tool-pooling costs within the Secure Network; (c) redeem for Jetix consulting or educational services at a preferred rate; (d) trade peer-to-peer within the Alliance membership (NOT on public exchange at Phase-3). The key investor-critic observation: option (a) is the most speculative and should be structured last, not first. Options (b) and (c) are the strongest utility cases because they are backed by real economic activity.

**What makes this different from crypto-pump approaches:** Value is usage-backed, not speculation-backed. A Jetix token is worth something because it buys access to Jetix services and tool-pools that exist and have value independent of the token. Contrast with ICO-era tokens where the only use-case was «future platform access» before any platform existed.

### Public security-token — the IPO-alternative problem

**Problem from strategic investor perspective:** A strategic partner (corporate, family office, accredited individual) who wants exposure to Jetix's trajectory faces an unpleasant set of options: traditional equity rounds (high valuation lock, dilution, control concession); waiting for a traditional IPO (slow, SEC/exchange burden, post-IPO liquidity constraints); or doing nothing (misses the exposure window). A structured security-token offering at Phase-3+ (with 3+ years of operational revenue, a formal Foundation, and accredited-only access) provides a flexible participation mechanism.

**Jetix differentiation from prior ICOs:** By Phase-3+ when a public token layer is even considered, Jetix has: $100M+ operational revenue (not a pre-revenue promise), Alliance Foundation incorporated per L6 Option C (governance legitimacy), DACH/Mittelstand-specific methodology with track record, and a regulatory-first design posture (MiCA compliance, accredited-only access). The distance between Jetix's proposed approach and the 2017-era ICO model is not marginal — it is categorical. [src:decisions/JETIX-VISION.md §14 «engineering faith»]

---

## 5. Offer Structure (Conceptual — Phase-3+ Legal Work Owns the Details)

**Investor-critic hard note:** the following is a conceptual framework, NOT legal advice and NOT a final offer structure. L7 Business Deep-Dive owns operational pricing and structure. A Phase-3+ corporate lawyer (EU crypto/securities specialty) must be engaged before any of this is implemented. Every number and structure below is a placeholder.

**Internal utility token (Phase-3, design-phase placeholder):**

- **Token unit working name:** Jetix Contribution Unit (JCU). Not locked; placeholder only. Actual name requires branding review.
- **Issuance:** Jetix-Corp issues initial supply. Alliance Foundation (L6 Option C entity) holds a reserve tranche for ecosystem growth and governance. Reserve percentage: TBD by Phase-3 lawyer + Foundation governance board.
- **Valuation mechanism:** Usage-backed. Each JCU is denominated relative to Jetix-service value (e.g., 1 JCU = €X of Jetix consulting services OR складчина tool-pool access for N months). The pricing formula is NOT a free-market exchange rate in Phase-3 — it is an internally-set rate reviewed quarterly by Foundation governance.
- **Redemption paths:** складчина tool-pool access / Jetix services / peer trade within Alliance members / optional conversion to traditional compensation with friction (friction = anti-churn mechanism).
- **Distribution mechanic for specialists:** contribution-hours × quality-multiplier = JCU award. Quality-multiplier set by Ruslan + Foundation governance to prevent gaming.

**Public security-token (Phase-3+, highly provisional):**

- **Structure preferred:** security-token under accredited-investor exemption (EU: Reg D equivalent; DACH: likely requires MiCA compliance + BaFin-registered offering or private placement under EU Prospectus Regulation exemption for < €8M). Not a pure utility token — the security-token framing provides stronger regulatory clarity.
- **Access:** accredited investors only (Phase-3+). No retail access until regulatory maturity is confirmed by Phase-3+ legal counsel.
- **Lockup:** 2-4 year standard for strategic partners. Prevents short-term speculative entry.
- **Governance rights:** observer / advisory / voting per token tier (TBD by Phase-3+ governance design).

---

## 6. Delivery Mechanism

**Phase-1 and Phase-2 (G0→G2): zero delivery effort.** No infrastructure built, no engineering assigned, no legal work done. Token is a named concept only.

**Phase-3 design phase ($100K earned → G3 launch):**
- Legal: EU crypto/securities lawyer engaged (expected cost: €30K-€100K for full MiCA compliance assessment + structure opinions + Foundation IP contribution agreement).
- Governance: Alliance Foundation (L6 Option C) incorporated as the issuer or co-issuer of Foundation-layer tokens; Jetix-Corp issues Jetix-service-backed JCUs.
- Engineering: smart-contract implementation on a regulated chain (Ethereum mainnet / regulated ERC-20 variant; or Solana for lower transaction costs; or private Hyperledger chain for maximum regulatory control). Chain choice is a Phase-3 engineering project — NOT a Phase-1/2 decision.
- Custody: institutional custody solution (Fireblocks, Anchorage, or equivalent) for any token amount above de minimis thresholds. KYC/AML gate mandatory.
- **Human time estimated:** Phase-3 design = 3-6 months heavy lawyer + engineering involvement (200-400 billable hours lawyer + 3-6 months engineering sprint). Phase-3+ operations = ongoing governance + investor-relations role (0.25 FTE minimum).

**Phase-3+ (public layer):**
- Public chain integration (if needed for accredited-venue exchange listings).
- KYC/AML gate at public layer: Jumio or equivalent identity verification.
- Exchange listings: accredited-only venues initially (Securitize, tZERO, or regulated EU tokenized securities platforms).
- Investor relations infrastructure: quarterly reports, token-holder communications, Foundation publications.

---

## 7. Competitive Positioning — Honest Assessment (Critic Mode)

**What Jetix is explicitly NOT doing:**

- 2017-2018 style utility ICOs (Telegram TON, Filecoin, EOS): retail-facing, unregistered, pump-driven, regulatory backlash. Virtually all failed or faced enforcement.
- Pure venture-capital equity rounds: equity dilution + control concession. Token is a complement, not a replacement for equity if Jetix pursues a round.
- Traditional IPO: slow timeline (Phase-3+ minimum), exchange regulatory burden, post-IPO quarterly earnings pressure incompatible with Jetix's long-horizon engineering-faith posture.
- Crypto-pump community-building: token communities organized around price speculation. Anti-pattern per D23.

**Why the Jetix approach could work — honest accounting:**
- By Phase-3+, Jetix has 3+ years of operational revenue, which fundamentally distinguishes it from pre-revenue ICOs.
- Alliance Foundation (L6 Option C) provides governance legitimacy analogous to Mozilla Foundation + Red Hat Corp structure [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5.X]. This is not cosmetic — Foundation provides structural separation of open-surface from commercial operations.
- Accredited-only public access prevents the retail-exposure regulatory risk.
- D23 «safe + adequate + thoughtful» constraint is founding-document-level, not a preference that can be overridden by a future team member.

**Risks — this is where critic mode must be rigorous:**

**R1: Legal risk is high.** EU MiCA (Markets in Crypto-Assets Regulation, fully operational 2024+) classifies tokens into Asset-Referenced Tokens (ARTs), E-Money Tokens (EMTs), and other crypto-assets. A Jetix JCU likely qualifies as «other crypto-asset» or possibly a security token depending on the specific design. US Howey test: if a Jetix token involves investment of money in a common enterprise with expectation of profits primarily from others' efforts — it is a security, requiring SEC registration or a Reg D exemption. The accredited-only design is specifically structured to exploit Reg D 506(c) for US accredited investors. EU private placement exemptions (Prospectus Regulation Article 1(4)) are available for < €8M offerings. A Phase-3 lawyer must confirm these before any token issuance — this is not optional.

**R2: Reputational risk is structurally non-trivial.** Any crypto-adjacent product launch invites «crypto-pump» framing regardless of Jetix's actual design. The DACH/Mittelstand primary market is particularly sensitive to this risk: German and Austrian enterprises are culturally skeptical of speculative finance. Mittelstand procurement officers who have already approved Jetix for AI consulting work may need to reconsider vendor relationships if a token is perceived as speculative. Ruslan's anti-pump quote must be architecturally embedded in the offering, not just asserted in marketing copy.

**R3: Capital opportunity cost.** Phase-3 legal + engineering for token infrastructure costs €100K-€500K before any token is issued. This competes directly with other Phase-3 capital priorities: USB-C services productization, Secure Network scaling, YouTube-analyzer SaaS development, educational methodology repo, matchmaker platform. The expected return calculation for the token investment must clear the same hurdle rate as every other Phase-3 capital allocation — it is not exempt from the investment-fund mentality (D11) [src:decisions/JETIX-VISION.md §3 D11].

**R4: Dilution of strategic focus.** The token is optionality, not core. It is entirely plausible that Jetix reaches $100M ARR through consulting + educational + Alliance membership fees without any token infrastructure whatsoever. The preserved dissent at the top of this document is the investor-critic's primary dissent: the token should never launch if operational revenue solves the specialist-compensation and investor-liquidity problems without it. This is not a weak position — it reflects pattern P5 (Taleb via-negativa): the discipline is to name which optionality items to RETIRE if they are not needed, before they consume Phase-3 capital.

**R5: Timing risk.** Crypto market cycles are real. A token structure launched during a crypto-market bust faces low secondary-market adoption from accredited investors even if the utility is genuine. A token launched during a boom attracts wrong investor profiles despite the accredited-only gate. Timing the market is inconsistent with Jetix's engineering-faith posture; the token must be designed to be utility-backed regardless of crypto-market cycle.

**R6: Regulatory moving target.** EU MiCA is relatively stable but US SEC enforcement posture under successive administrations has been volatile. Jetix is EU-based (DE GmbH per D15 revenue-gated unlock [src:decisions/JETIX-PLAN.md §1]) which helps but does not eliminate US exposure if any accredited US investors participate in the Phase-3+ public layer.

---

## 8. Evolution Per Gate

The gate-by-gate trajectory is explicit and non-compressible. Any acceleration of this timeline is a risk-of-ruin trigger (analyst receiving a solo founder's runway cannot afford premature legal/engineering spend on speculative infrastructure).

**G0→G1 (€0 → €50K Q2 2026): NOT designed.**
Per JETIX-VISION D23 verbatim and JETIX-PLAN revenue-gated discipline: zero hours, zero budget, zero planning effort. The token exists as a named concept in the Vision document and nothing more. Any Phase-1 effort toward token design is a misallocation of founder bandwidth. Ruslan's anti-pump quote from Note 5 functions as the permanent Phase-1 anchor: *«не какая-то там ебаная пирамида»* [src:decisions/JETIX-VISION.md §14 Note 5]. This is the founding filter that every future design decision passes through.

**G1→G2 (€50K → €200K validation): still NOT designed.**
Phase-2 priorities are Secure Network architecture, matchmaker formalization, first USB-C productized client engagement, and Alliance Option C legal structure (Foundation). Token is not in any of these. The Foundation legal work done at Phase-2 (Option C incorporation, ~€30K-€50K per [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5 Phase-2 trigger]) IS a precondition for any future token structure — the Foundation needs to exist before it can act as token issuer or governance entity. But Foundation formation is done for Alliance reasons, not token reasons. Token design remains deferred.

**G2→G3 (€200K → €1M, with $100K self-earned milestone as design trigger):**
The $100K self-earned trigger [src:decisions/JETIX-VISION.md §13 «Mid-Phase-1 trigger»] initiates design exploration only. This phase involves: (a) first lawyer consultation on token structure options (MiCA classification, Howey test analysis, jurisdiction comparison); (b) evaluation of whether internal utility case is sufficiently strong to justify Phase-3 infrastructure costs; (c) Foundation governance decision on whether Foundation or Jetix-Corp should be the token issuer. **No token is issued at this gate.** The output is a go/no-go recommendation from lawyer + investor-expert to Ruslan for HITL ack.

**G3→G4 ($1M → $100M): Internal utility token launch (accredited members + specialists only).**
If Phase-2 go/no-go returns «go», this is when the internal utility layer goes live. Specialists receive JCUs for contributions. Складчина tool-pooling denominated in JCUs. Alliance Foundation members participate in internal token governance. Strategic-investor accredited offering is optional and conditional on MiCA compliance confirmation. This gate requires Alliance Foundation incorporation (L6 Option C), active specialist pool from D21 Roy-replication [src:decisions/JETIX-VISION.md §5], and internal KYC/AML gate. The token at this phase is NOT publicly tradeable. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §6 Evolution G3→G4]

**G4→G5 ($100M → $1T): Public layer potential.**
Per D23 Option B: limited-public token as alternative to IPO [src:decisions/JETIX-VISION.md §5]. Accredited investors and regulated-venue exchange listings. Foundation publishes Apache 2.0 methodology + token-economics documentation. Governance rights for long-term token holders. «Alternative to IPO» positioning: this is structurally correct because a traditional IPO at $100M ARR would require a 3-5 year preparation window, exchange listing fees, quarterly earnings pressure, and loss of founder control. A structured security-token offering to accredited partners avoids most of these friction points while providing the liquidity mechanism strategic investors want.

---

## 9. Cross-Direction Dependencies

The token direction sits in a dense dependency web. It cannot be designed or launched without other directions reaching operational maturity first.

**Depends on:**
- **L6 Alliance Foundation Option C** (incorporated entity; legal substrate for token issuance and governance) [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5.X]. If Option C is not acked by Ruslan, the token structure must be redesigned from scratch — Jetix-Corp alone as issuer has worse regulatory optics than Foundation + Corp dual structure.
- **§3.1 AI Consulting revenue** (funds Phase-3 legal/engineering capex; no consulting ARR = no capital for €100K-€500K token infrastructure spend).
- **§3.3 USB-C Integration Services** (deployments at Phase-3+ compound the economic activity that makes JCU redemption meaningful — if clients use Jetix services regularly, specialist contributions have clear redemption value).
- **§3.5 Secure Network** (members = primary internal utility consumers for складчина tool-pooling; Secure Network must exist before складчина token-accounting makes sense).
- **§3.7 Educational + Investor Programs** (investor-relations infrastructure for Phase-3+ public token layer; investor program participants are the natural accredited-investor audience for the public token).

**Depended on by:**
- **§3.4 Matchmaker** at Phase-3+: specialist compensation via token is one of the friction-reduction mechanisms that makes matchmaking at scale economically clean. Without token, all specialist payments route through traditional wire/banking/invoicing.
- **§3.5 Secure Network** складчина mechanic: tool-pooling becomes more elegant with token accounting than with per-transaction cash transfers among members.
- Jetix-Corp strategic-investor round (Phase-3+): the token layer can run in parallel with a traditional equity round or serve as an alternative, depending on Phase-3+ capital structure decisions.

**Cross-cutting observation.** Token is the **coordination-economic-glue** of the Phase-3+ ecosystem, not a product sold to end-users. This framing matters for the design: the token is infrastructure for Jetix's participants, not an offering pitched to the public. Per D21 Roy-replication [src:decisions/JETIX-VISION.md §5]: as roys emerge in other verticals and niches, the token becomes the coordination layer for inter-roy value exchange. This is the most powerful long-term use-case and the one that most strongly justifies Phase-3+ investment — but it only emerges if Roy-replication methodology succeeds first.

---

## 10. Open Questions — Critic Mode Demands Rigor

Three questions are mandatory per the acceptance predicate (legal_structure, jurisdiction, distribution_mechanism). Two additional are filed as high-priority for Ruslan ack before Phase-3 design work begins.

**Q1 (legal_structure): Security-token vs utility-token vs hybrid?**
The design choice has cascading implications. Pure utility token: lighter regulatory burden in some jurisdictions, but weaker investor protections and higher risk of Howey-test failure in the US. Pure security token: stronger regulatory clarity, fits accredited-investor exemption structures, but heavier issuance burden (prospectus or exemption documentation required). Hybrid (utility-in-EU / security-in-US depending on holder jurisdiction): operationally complex, requires multi-jurisdiction legal opinions. Preferred direction per investor-critic lens: **security-token under accredited-investor exemption** — clearest regulatory pathway for Jetix's actual use-case (specialist compensation + strategic investor participation) and most defensible against enforcement risk. However, Phase-3 lawyer must confirm. This question cannot be answered without EU MiCA classification analysis + US Howey test opinion specific to the Jetix JCU design.
F: F2 (preliminary assessment; not yet legal opinion).

**Q2 (jurisdiction): Where does the Foundation issue, and where does Jetix-Corp issue?**
Foundation (L6 Option C): Switzerland (Ethereum Foundation precedent, crypto-friendly, FINMA has clear crypto guidance), Liechtenstein (Blockchain Act 2020, most purpose-built EU-adjacent crypto framework), Germany (home market but BaFin is conservative on crypto), Malta (historically crypto-friendly but EU credibility concerns). Jetix-Corp (DE GmbH per D15): German-domiciled, which makes DE the default jurisdiction for Jetix-Corp token issuance. The Foundation jurisdiction is an independent decision from the Corp jurisdiction. Tradeoff for Foundation: Switzerland or Liechtenstein offers strongest legal clarity + credibility for crypto; Germany offers stronger Mittelstand-credibility but BaFin scrutiny. This decision should be made by Phase-3 lawyer with input from Alliance founding members.
F: F2 (preliminary framing; jurisdiction selection requires legal + tax advice).

**Q3 (distribution_mechanism at Phase-3+): How does the public layer reach accredited investors?**
Three options: (a) direct private placement to strategic partners only (lowest risk, lowest reach, most controlled); (b) limited offering on regulated tokenized-securities platforms (Securitize, tZERO, or EU equivalents like Tokeny / Caiz) available to accredited investors only; (c) Alliance-member exclusive distribution (members from Secure Network + Alliance Foundation only, bypassing public exchanges entirely in Phase-3+). Option (a) is the most consistent with D23 «safe + adequate + thoughtful» and the least likely to attract unwanted speculation. Option (c) is also conservative but may limit Phase-3+ liquidity for strategic partners. Per investor-critic lens: default to option (a) at G4→G5 launch, with option (b) activated only when regulatory clarity is confirmed and advisor/lawyer recommends.
F: F3 (reasoned judgment; actual mechanism depends on legal structure + market conditions at Phase-3+ time).

**Q4 (token-equity coordination): If Jetix raises an equity round at Phase-3+, how do token-holders interact with equity-holders?**
This is a governance risk. Token-holders with governance rights (voting, advisory) may conflict with equity shareholders on capital allocation decisions. Dilution events (new equity issuance) can impair token value if token rights are senior to or junior to equity in ways that are not specified upfront. A priority governance document is required before any combined equity + token structure exists. This question does not block Phase-1/2 operations but must be resolved before any Phase-3+ investor receives either equity or tokens.
F: F2 (known structural risk; not yet an active design constraint given timeline).

**Q5 (sunset scenario): Does D23 Option B have an expiration trigger?**
Per investor-critic via-negativa discipline (Taleb pattern P5): every optionality item must also have a retirement condition. If Jetix reaches $100M ARR through consulting + Alliance fees + educational products without specialist-compensation friction becoming an operational blocker, the token infrastructure spend (€100K-€500K) may not be justified. The retirement condition for D23 Option B: **if Phase-3 go/no-go lawyer consultation returns a legal-risk-to-benefit ratio that exceeds the opportunity cost of deploying that capital into other Phase-3 priorities, the token does not launch, and D23 Option B is permanently archived.** This is not failure — it is the via-negativa discipline operating correctly. Ruslan should ack this retirement condition explicitly so it is on record.
F: F4 (operational convention; designed to hold the option open without committing capital prematurely).

---

## Critic-Mode Summary Assessment

**Status: DRAFTED — requires Phase-3 gate conditions before any design work begins.**

The token direction is correctly positioned as Phase-3+ optionality, not Phase-1/2 work. D23 design constraints are rigorous and binding. The anti-pump anchor is the most important single constraint in the entire direction design — if it is ever relaxed by a future team member, the reputational risk to Jetix's Mittelstand consulting and Alliance operations would be severe and potentially irreversible.

**Investor-critic verdict on the concept:**
The internal utility token (JCU at G3→G4) has a genuinely strong use-case in specialist compensation and складчина tool-pooling, provided it is backed by real economic activity (Jetix services and tool pools with independently verifiable value). This is categorically different from ICO-era tokens where the only use-case was future platform access before any platform existed.

The public security-token layer (G4→G5) is reasonable as an IPO-alternative mechanism provided: regulatory clarity is confirmed by Phase-3+ legal counsel, Jetix has $100M+ ARR, Alliance Foundation is incorporated and operational, and accredited-only access is structurally enforced. None of these conditions exist today.

**Primary preserved dissent (filed formally):** The token should never launch if consulting + educational + licensing + strategic-equity fund growth sufficiently. This is not a minority view — it is the correct default position until Phase-3 go/no-go confirms otherwise. Capital that would be spent on token infrastructure has a high opportunity cost against other Phase-3 priorities with more immediate revenue impact. The token is option value; option value is maximized by not exercising it prematurely. [src:investor-expert §6.4 via-negativa antifragility — retire fragile positions before they fail]

---

*Drafted by investor-expert (mode: critic), cell C-10, cycle cyc-layer-5-product-deep-dive-2026-04-25. Draft status only. Awaiting brigadier §5.5.5 provenance gate + Ruslan HITL review before promotion to canonical layer in decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md.*
