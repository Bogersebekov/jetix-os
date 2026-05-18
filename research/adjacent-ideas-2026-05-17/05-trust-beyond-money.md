---
title: Cluster 5 — Trust mechanisms beyond money
date: 2026-05-17
type: research-cluster
status: brigadier-research-surface (R1)
parent: research/adjacent-ideas-2026-05-17/00-MASTER-RESEARCH-INDEX.md
cluster: §1.5
constitutional_posture: R1 surface-only + R6 provenance + EP-5 disclosed
F: F2
G: research-cluster-trust-beyond-money
R: refuted_if_alternative_trust_mechanisms_disconnected_from_FPF_H8_OR_if_SBT_VC_design_unrelated_to_role_attestation
language: russian + english
---

# Cluster 5 — Trust mechanisms beyond money (H8 adjacency)

> **R1 surface-only.** Surfaces working precedents для H8 Trust Infrastructure (text_001 «деньги ↔ trust beyond money» core insight).

---

## §0 TL;DR (≤200 слов)

H8 Trust Infrastructure (Octagon LOCKED 2026-05-17) postulates trust mechanisms beyond money. Adjacent precedents — 5 категорий:

**(1) Time-based currencies:** TimeBanks.org (Edgar Cahn 1980+); Time Dollars tax-exempt; **Cahn died Jan 2022 age 86**; principles: We Are All Assets, Redefining Work, Reciprocity, Social Networks.

**(2) Reputation systems:** PGP Web of Trust (Zimmermann 1992) — strong set grew 18K (2003)→62K (2018)→57.5K (2019); Stack Overflow karma (10pt upvote, downvote costs 2pt to downvoter — asymmetric); GitHub stars / Linux maintainership / Apache committer.

**(3) Cryptographic credentials:** **W3C Verifiable Credentials v2.0 — W3C Recommendation May 2025** (производственное использование: TruAge, CA DMV, SpruceID, Danube Tech, ETRI); **Soulbound Tokens (SBTs)** — Buterin+Weyl+Ohlhaver «Decentralized Society: Finding Web3's Soul» May 2022 paper; non-transferable, publicly verifiable.

**(4) Mechanism design:** **RadicalxChange + Plurality (Weyl 2018+)**; Quadratic Voting voice credits → square-root counted; Microsoft Research Plural Technology Collaboratory; «Plurality: The Future of Collaborative Technology and Democracy» (2024 collab с Audrey Tang).

**(5) Cooperative + gift economies:** **Mondragón** (Basque Spain 1956+) — 70,085 employees (2024), wage ratio 3:1-9:1 (avg 5:1), one-worker-one-vote; **Graeber «Debt: First 5000 Years» (2011)** — human economies as ongoing obligations; **Marcel Mauss gift economy** ancestry.

**Adjacency к H8:** **SBT + W3C VC = direct cryptographic substrate** для role-attestation; **TimeBanks core principles = exact frame** для anti-extraction R12 positive face; **Mondragón = working 70-year non-money-primary trust at scale**. PGP web-of-trust = working «transitive trust network» = direct ancestor for FPF role-attestation graph.

---

## §1 Key works / movements / people

### §1.1 Time-based currencies

**TimeBanks.org / Edgar Cahn (1980+)** — Time Dollar = 1 hour labor regardless of skill. Tax-exempt complementary currency. **Founded 1980 in response to Reagan social program cuts.** **4 core principles:** We Are All Assets / Redefining Work (rewards unpaid + care work) / Reciprocity / Social Networks. **Time Dollar Institute** (1995, Cahn). **Edgar Cahn died January 23, 2022, age 86.** [src: https://www.timebanks.org/dr-cahn; https://nonprofitquarterly.org/edgar-cahns-second-act-time-banking-and-the-return-of-mutual-aid/, retrieved 2026-05-17]

> Verbatim (Cahn 4 principles): «We Are All Assets — everyone has something to contribute.»

**Ithaca HOURS (1991+)** — Paul Glover, Ithaca NY. Local complementary currency. ~$100K+ circulated at peak. Faded by 2010s. Lesson: depends heavily on champion.

**LETS schemes (Local Exchange Trading Systems)** — Michael Linton 1983+ Canada → UK + global. ~3000+ schemes globally peak. Mutual credit ledger. Mostly volunteer-run.

**SEL France (Systèmes d'Échange Local)** — French LETS variant. Active 1990s-2020s.

### §1.2 Reputation systems

**PGP Web of Trust (Phil Zimmermann, 1992)** — PGP v2.0 manual. **Decentralized fault-tolerant web of confidence**, alternative to centralized PKI. Grass-roots activists initial target. OpenPGP certificate signing → directed graph. **Strong set** (most connected portion): 18K (2003) → 62K (2018) → 57.5K (May 2019). **Key Signing Parties:** in-person ID verification rituals. **GnuPG** = open-source implementation. [src: https://en.wikipedia.org/wiki/Web_of_trust, retrieved 2026-05-17]

**Stack Overflow reputation (Spolsky + Atwood, 2008+)** — Karma points = community-trust measure. Asymmetric incentive: upvote +10, downvote -1 (recipient) but **-2 to downvoter** (downvote = serious commitment). Privilege gating: comment / upvote / downvote / edit / moderator. **«How Stack Overflow's reputation system led to its own downfall» (Slashdot, June 2025)** — recent debate that gamification damaged ecology. [src: https://stackoverflow.blog/2022/10/09/how-to-earn-a-million-reputation-on-stack-overflow-be-of-service-to-others/; https://developers.slashdot.org/story/25/06/02/0922250/, retrieved 2026-05-17]

**GitHub stars** — proxy for project trust. Not validated; gameable. But: persistent signal.

**Linux kernel maintainership** — Linus Torvalds + lieutenants. Path-based trust transitivity. ~30 years compounded reputation.

**Apache committer status** — Apache Software Foundation. Earned through sustained contribution. Strong signaling.

### §1.3 Cryptographic credentials

**W3C Verifiable Credentials v2.0 (Recommendation, May 2025)** — VC Working Group; 7 W3C Recommendations published. Production deployments: **TruAge, CA DMV, SpruceID, Danube Tech, ETRI (Korea)**. **VC API** in production (HTTP API for issuance + verification). Cryptographically secure + privacy respecting + machine-verifiable. [src: https://www.w3.org/news/2024/w3c-invites-implementations-of-verifiable-credentials-data-model-v2-0/; https://www.w3.org/TR/vc-data-model-2.0/, retrieved 2026-05-17]

**Soulbound Tokens (SBT) — Buterin + Weyl + Ohlhaver (May 2022)** — paper «Decentralized Society: Finding Web3's Soul» (SSRN 4105763). **Non-transferable, publicly verifiable digital tokens.** Use cases: university alumni credentials, professional certifications, community memberships. **DeSoc (Decentralized Society)** = co-determined sociality through Souls + community SBT graph. Concerns: privacy / discrimination of identifiable SBT holders. [src: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763; https://decrypt.co/resources/what-are-soulbound-tokens-building-blocks-for-a-web3-decentralized-society, retrieved 2026-05-17]

> Verbatim (Buterin/Weyl/Ohlhaver 2022): «Decentralized Society (DeSoc) is a co-determined sociality, where Souls and communities come together bottom-up, as emergent properties of each other.»

**Decentralized Identifiers (DID) — W3C standard 2022** — companion to VC. Self-sovereign identity.

**Formal verification trust (Coq / Lean):** Proof as trust artifact — different domain but same idea: «proof verifiable = trust transferred».

### §1.4 Mechanism design (RadicalxChange + Plural)

**Glen Weyl — RadicalxChange (2018+), Plural Technology Collaboratory (Microsoft Research)** — 501(c)(3) nonprofit. **Quadratic Voting (QV):** voice credits → square-root counted votes. Mitigates tyranny of majority + factional control. **Quadratic Funding** (similar mechanism for public-goods funding) — used by Gitcoin (Cluster 3 cross-ref). **Microsoft Research Plural Technology Collaboratory** = Weyl's research lab. **«Plurality: The Future of Collaborative Technology and Democracy»** — 2024 collaborative project with Audrey Tang. Plurality Institute founded by Weyl. [src: https://www.radicalxchange.org/wiki/quadratic-voting/; https://glenweyl.com/radicalxchange/, retrieved 2026-05-17]

**E. Glen Weyl** — economist, Microsoft Research, founder of Plurality Institute + RadicalxChange. Co-author с Buterin of SBT paper. Living center of «mechanism design + identity + cooperation» research.

**Audrey Tang** — former Taiwan Digital Minister. Practical implementer of plural technology in government. Mastodon / vTaiwan / Polis.

### §1.5 Cooperative + gift economies

**Mondragón Corporation (Basque Spain, 1956+)** — founded by Father José María Arizmendiarrieta. **70,085 employees (2024), 4 areas: finance / industry / retail / knowledge.** 30,660 in Basque Country + 29,340 elsewhere Spain + ~10K abroad. **Largest worker cooperative federation globally.** Wage ratios: 3:1 to 9:1, avg 5:1. **One worker one vote.** Corporate values: Co-operation / Participation / Social Responsibility / Innovation. Mondragon Cooperative Congress (1984) = umbrella governance. **68 years sustained value-aligned coordination.** [src: https://en.wikipedia.org/wiki/Mondragon_Corporation; https://www.mondragon-corporation.com/en/about-us/, retrieved 2026-05-17]

**David Graeber — «Debt: The First 5,000 Years» (2011)** — anthropological history of debt от Sumer 3500 BCE. **«Human economies»** = ongoing obligations through gifts + marriages + sociability; vs **debt** = impersonal calculation that ends relationship when paid. **Marcel Mauss gift economy theory** (1925 «The Gift») = direct intellectual ancestor. [src: https://en.wikipedia.org/wiki/Debt:_The_First_5,000_Years, retrieved 2026-05-17]

> Verbatim (Graeber 2011, paraphrase): "Human economies are built on (ongoing) obligations rather than debt; debt is an impersonal calculation which, once paid, ends the relationship."

**Lewis Hyde — «The Gift» (1983)** — gift economy in creative arts.

**Marcel Mauss — «The Gift / Essai sur le don» (1925)** — foundational anthropology.

### §1.6 Other adjacencies

**eBay feedback (1995+)** — pioneer commerce reputation; bilateral feedback.
**Couchsurfing / Airbnb reviews** — trust-for-physical-access.
**Yelp / TripAdvisor** — review-based trust for service.
All face Goodhart's-law gaming over time.

---

## §2 Verbatim quotes

**Edgar Cahn (TimeBanks 4 principles):**
> «We Are All Assets — everyone has something to contribute.»

**Buterin/Weyl/Ohlhaver (DeSoc paper, May 2022):**
> «Decentralized Society (DeSoc) is a co-determined sociality, where Souls and communities come together bottom-up, as emergent properties of each other, to co-create plural network goods and intelligences, at a range of scales.»

**Graeber «Debt» (paraphrase):**
> «Human economies are built on (ongoing) obligations rather than debt; debt is an impersonal calculation which, once paid, ends the relationship.»

**Mondragón mission (corporate values):**
> «Co-operation, Participation, Social Responsibility, Innovation» + «intercooperation, grassroots management, corporate social responsibility, innovation, democratic organisation, education and social transformation.»

**Phil Zimmermann (PGP web of trust intent, 1992):**
> [PGP users would accumulate keys from designated trusted introducers, creating an emergent decentralized fault-tolerant web of confidence.]

---

## §3 Adjacency assessment

### Overlap (direct H8 substrate)

| H8 / Jetix claim | Adjacent precedent | Overlap depth |
|---|---|---|
| Role-attestation as trust mechanism (text_001) | **W3C VC v2.0 + SBT** | **DIRECT — production-ready substrate** |
| Trust through demonstrated results (text_001) | Stack Overflow karma + GitHub stars + Linux maintainership | **STRONG** — proven patterns |
| Transitive trust graph via FPF | PGP Web of Trust graph | **EXACT structural parallel** |
| H8 = non-money trust at substrate | Mondragón 68-year scale | **DIRECT — proof of concept at industrial scale** |
| R12 anti-extraction positive face | TimeBanks principles 1-4 | **EXACT philosophical parallel** |
| FPF as substrate for cooperation | Graeber «human economies» | **STRONG philosophical alignment** |
| Quadratic mechanisms for collective decisions | RxC QV + Plural | **STRONG** — directly applicable design |
| Network of clans with cross-clan trust | Mondragón Cooperative Congress umbrella governance | **DIRECT — 1984 reorganization precedent** |

### Divergent

| Jetix unique | Adjacent missing |
|---|---|
| Methodology + AI substrate underlying trust | TimeBanks / Mondragón = pre-AI |
| Role-attestation tied to **engineering capability** | SBT / VC = generic credentials |
| FPF F-G-R as **machine-verifiable** trust grade | PGP signed assertion only |
| Constitutional Default-Deny + Corrigibility | DAOs / DeSoc weak on governance guarantees |
| Multilingual methodology (Russian + English) | Western lineage default |
| Workshop as physical-digital hybrid trust venue | TimeBanks digital-only; Mondragón physical-rooted |

---

## §4 Failure cases / lessons learned

**Stack Overflow reputation system damage (Slashdot 2025).** Gamification over time eroded ecology — newcomers face «no easy questions answered» culture, downvote-shy answerers. **Lesson:** reputation systems mutate community culture over decades. **Direct lesson for H8:** R-discipline в design choices; consider periodic reset mechanisms or anti-gaming bounds.

**PGP Web of Trust limited scale despite 30 years.** Strong set ~50-60K nodes is small. **Failure mode:** UX friction (key signing parties don't scale); benefits unclear to non-activists; replaced by centralized PKI + corporate identity providers. **Lesson:** decentralized trust at consumer scale requires UX that doesn't ask users to reason about trust math. FPF role-attestation must hide complexity.

**Ithaca HOURS faded.** Lesson: champion-dependency. Without Paul Glover, community currency stopped. **Direct Jetix lesson:** Ruslan-dependency mitigation in Foundation.

**TimeBanks scale limit.** Despite 40 years, TimeBanks remain niche. **Hypothesis:** time-unit doesn't carry skill-differentiation signal; high-skill labor undervalued. **Lesson for Jetix:** FPF role-attestation **must carry skill-differentiation** (engineering mastery levels), not flat-time-credit pattern.

**SBT privacy concerns.** Buterin/Weyl/Ohlhaver paper itself acknowledges: discrimination risk; SBT holders identifiable by attribute. **Lesson:** privacy-preserving design (selective disclosure VC) before scale.

**Mondragón critiques** — wage ratio still grew over decades; outside-Spain workers don't have full membership; criticized as «cooperative capitalism». **Lesson:** sustaining cooperative principles at scale requires constitutional discipline (matches Jetix Pillar C).

**DeSoc «Web3 soul» mostly aspirational.** Despite May 2022 paper, SBT mainstream adoption limited. **Lesson:** crypto-native framing can repel non-crypto audiences. **Direct Jetix lesson:** keep H8 role-attestation **substrate-agnostic** — could be VC, could be Git commits, could be Karpathy-wiki signatures — don't lock to crypto rails.

**Quadratic Voting limited adoption.** Despite Weyl pedigree + government engagements, QV remains niche. **Lesson:** mechanism design needs viral pull, not just intellectual elegance.

---

## §5 Contact / read / follow list

| Name | Role / Handle | Why interesting | Ask? |
|---|---|---|---|
| Edgar Cahn (deceased Jan 2022) | TimeBanks founder | Historical reference; read «No More Throw-Away People» | Read book |
| TimeBanks.org current leadership | timebanks.org | Active community successor | Distant-follow |
| Vitalik Buterin | Ethereum founder; @VitalikButerin | DeSoc paper author; living center of crypto + governance design | Follow Twitter + blog |
| Glen Weyl | Microsoft Research Plural Tech; @glenweyl | Plurality + RxC founder; SBT co-author | Read «Plurality» 2024 book; possible cold outreach if Jetix mature |
| Puja Ohlhaver | SBT paper co-author; lawyer | Legal+tech interface | Follow |
| Audrey Tang | former Taiwan Digital Minister | Practical implementer of Plural tech | Watch Tang talks; vTaiwan study |
| W3C VC Working Group | w3c/vc-data-model | Standards substrate | Watch VC API roadmap |
| SpruceID team | spruceid.com | Production VC implementation | Read engineering blog |
| Mondragón Cooperative Congress | mondragon-corporation.com | Living 68-year cooperative governance | Visit Basque Country one day? Read case studies |
| Father Arizmendiarrieta (historical) | Mondragón founder | Founder principles | Read biography |
| David Graeber (deceased 2020) | anthropologist | «Debt» reading | Read book |
| Marcel Mauss (historical) | anthropologist | «The Gift» essential | Read essay |
| Lewis Hyde | «The Gift» author | Creative gift economy | Follow recent essays |
| Phil Zimmermann | PGP founder; living elder | Web of trust originator | Read recent interviews |

---

## §6 Connections к Jetix Phase 0 + H1-H8 + vision/*

| Jetix artefact | Adjacent connection |
|---|---|
| **H8 Trust Infrastructure (LOCKED 2026-05-17)** | **DIRECT — entire cluster is H8 substrate research** |
| **R12 anti-extraction (constitutional candidate rule)** | TimeBanks 4 principles = exact philosophical parallel |
| **FPF role attestation primitive (A.2.8 Commitment + A.2.9 SpeechAct)** | W3C VC v2.0 = production substrate; SBT = adjacency |
| **F-G-R schema (FPF B.3)** | F (formality) = analogous to VC issuer-reputation; R (reliability) = analogous to VC freshness/revocation status |
| **vision/04 first 10-person Clan** | Mondragón initial group (Arizmendiarrieta + students) = exact precedent |
| **H7 People-NS «mastery as currency»** | TimeBanks failure mode (flat-time-credit) shows skill-differentiation needed; SBT can carry it |
| **Workshop revenue distribution (vision/03)** | Mondragón wage ratio model (3:1-9:1) + Gitcoin quadratic funding |
| **Pillar C Corrigibility** | DAO governance failures show importance of constitutional safeguards |
| **Audit trail / decisions/* substrate** | PGP signing pattern = adjacent for «who attested when» |

---

## §7 Open questions

1. **VC adoption test:** Could first-Clan Jetix members carry W3C VC «engineering capability» credentials? 1-week pilot with SpruceID stack.
2. **SBT vs VC trade-off:** SBT = on-chain (transparency + immutability + cost) vs VC = off-chain (privacy + flexibility + free). For H8 — which substrate fits better? Strategic study needed.
3. **Mondragón visit:** Worth Phase 2+ field-research trip to Basque Country? Direct learnings.
4. **PGP web-of-trust experiment:** Could 10-person first Clan pilot key-signing party as proof-of-concept? Surface FPF artifacts as PGP-signed claims.
5. **TimeBanks failure mode parity:** Where does Jetix risk «flat-currency-no-skill-signal»? FPF schema must differentiate.
6. **Quadratic Funding for first Clan revenue:** Could H8 incorporate QF mechanism for revenue distribution? Test with hypothetical 10-person Workshop.
7. **Graeber + Mauss reading group:** Worth Phase 0-1 internal study? Frame H8 anthropologically.
8. **Stack Overflow downfall parallel:** Where does Jetix risk SO trajectory (gamification eats ecology)? Pre-mortem.
9. **«Plurality» book deep read:** Tang/Weyl 2024 book — direct overlap with H4+H7+H8?

---

## Sources (URLs retrieved 2026-05-17)

- [TimeBanks Edgar Cahn](https://www.timebanks.org/dr-cahn)
- [Cahn second act — NPQ](https://nonprofitquarterly.org/edgar-cahns-second-act-time-banking-and-the-return-of-mutual-aid/)
- [Web of trust — Wikipedia](https://en.wikipedia.org/wiki/Web_of_trust)
- [Stack Overflow rep blog](https://stackoverflow.blog/2022/10/09/how-to-earn-a-million-reputation-on-stack-overflow-be-of-service-to-others/)
- [W3C VC Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [W3C VC 2024 invitation](https://www.w3.org/news/2024/w3c-invites-implementations-of-verifiable-credentials-data-model-v2-0/)
- [DeSoc / SBT paper — SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763)
- [Decrypt on SBT](https://decrypt.co/resources/what-are-soulbound-tokens-building-blocks-for-a-web3-decentralized-society)
- [RadicalxChange QV](https://www.radicalxchange.org/wiki/quadratic-voting/)
- [Glen Weyl RxC](https://glenweyl.com/radicalxchange/)
- [Mondragón Corporation — Wikipedia](https://en.wikipedia.org/wiki/Mondragon_Corporation)
- [Mondragón about](https://www.mondragon-corporation.com/en/about-us/)
- [Graeber Debt — Wikipedia](https://en.wikipedia.org/wiki/Debt:_The_First_5,000_Years)
- [Slashdot — SO reputation downfall 2025](https://developers.slashdot.org/story/25/06/02/0922250/)

---

## §8 На человеческом — какие precedents trust beyond money (added brigadier 2026-05-18)

### §8.1 Что это

Это **обзор существующих trust mechanisms, которые работают без денег** — direct adjacency для **H8 Octagon Trust Infrastructure LOCKED 2026-05-17**. Audio_672 core insight = «деньги ↔ trust beyond money»: для Jetix substrate trust между members должен работать не только через payments.

**5 categories adjacent precedents:**

1. **Time-based currencies** — TimeBanks (Edgar Cahn 1980+); Ithaca HOURS; LETS schemes
2. **Reputation systems** — PGP Web of Trust (Zimmermann 1992); Stack Overflow karma; GitHub stars; Linux maintainership; Apache committer
3. **Cryptographic credentials** — W3C Verifiable Credentials v2.0 (Rec May 2025); Soulbound Tokens (SBT, Buterin/Weyl/Ohlhaver 2022)
4. **Mechanism design** — RadicalxChange Quadratic Voting + Quadratic Funding (Weyl); Plurality book (Tang/Weyl 2024)
5. **Cooperative + gift economies** — Mondragón (70K employees, 1956+); Graeber «Debt» (2011); Marcel Mauss «The Gift» (1925)

Аналогии:
- **TimeBank** = «1 час работы любого = 1 час работы любого другого» (Cahn philosophy)
- **PGP Web of Trust** = «cryptographic подпись на friend's key, transitively trust строится через цепочки» (с 1992 = 34 года)
- **VC v2.0** = «digital passport с selective disclosure, W3C standard Recommendation 2025»
- **SBT** = «non-transferable badge на blockchain, виден all»
- **Quadratic Voting** = «voice credits → square-root counted, не 1-token-1-vote» (anti-tyranny majority)
- **Mondragón** = «70-year cooperative с wage cap 5:1 average и one-worker-one-vote» (см. research/deepening/06)

### §8.2 Ключевые pointы

- **TimeBanks** — Edgar Cahn 1980+; **died Jan 23, 2022, age 86**; 4 principles: We Are All Assets / Redefining Work / Reciprocity / Social Networks
- **PGP Web of Trust** — Zimmermann 1992; strong set: **18K (2003) → 62K (2018) → 57.5K (2019)**
- **Stack Overflow** — asymmetric karma (+10 upvote, -1 to recipient downvote, **-2 to downvoter**); 2025 «How SO reputation system led to downfall» Slashdot (см. research/deepening/03)
- **W3C VC v2.0** — **Recommendation 15 May 2025**; production: TruAge, CA DMV, SpruceID, Danube Tech, ETRI Korea
- **SBT paper «Decentralized Society: Finding Web3's Soul»** — SSRN 4105763, May 2022; Buterin + Weyl + Ohlhaver
- **Quadratic Funding** — used by Gitcoin ($45M+ distributed); square-root counting amplifies small donors
- **Mondragón** — 70,085 employees (2024), 5:1 average wage ratio, **68 years sustained value-aligned coordination**
- **Graeber «Debt: First 5,000 Years» (2011)** — «human economies» = ongoing obligations vs debt = impersonal calculation

### §8.3 Зачем нам это для Jetix

**Direct adjacencies for H8:**

| H8 design surface | Adjacent precedent | Lesson |
|---|---|---|
| Role-attestation substrate | **W3C VC v2.0 + SBT** | Cryptographic, machine-verifiable; VC selective disclosure preferred (см. research/deepening/07) |
| Trust transitivity | **PGP Web of Trust** | 34-year working transitive trust network; directed graph; key-signing parties |
| Non-money cooperative trust at scale | **Mondragón 70 years** | Working 70-year non-money-primary trust at industrial scale (см. research/deepening/06) |
| Anti-extraction (R12) positive face | **TimeBanks 4 principles** | «Everyone has something to contribute» = positive R12 framing |
| Reputation gamification anti-pattern | **Stack Overflow 2025 downfall** | Single-signal asymmetric karma decays ecology (см. research/deepening/03) |
| Anti-tyranny majority | **Quadratic Voting** | Voice credits + square-root counting; relevant для H8 governance |
| Anthropological framing | **Graeber + Mauss** | Trust = ongoing obligations, не debt; FPF role-attestation = «human economy» pattern |

**Direct H8 design implications (cross-ref research/deepening/07 substrate matrix):**

- **Layer 1 (immediate, free):** PGP-signed Foundation Part changes + Karpathy-wiki-sig convention formalized
- **Layer 2 (production):** add W3C VC v2.0 over Phase 1
- **Layer 2+ (pattern adopt):** Coordinape epoch-peer-reward для Workshop revenue (БЕЗ Ethereum)
- **Layer 3+ (optional):** SBT только для crypto-native partner Clans

**Cross-refs:** decisions/STRATEGIC-INSIGHT-H8-* (H8 LOCKED 2026-05-17), R12 anti-extraction, vision/03 Workshop, vision/08 L1+, research/deepening-2026-05-18/03 (SO + Friend.tech), research/deepening-2026-05-18/06 (Mondragón), research/deepening-2026-05-18/07 (substrate matrix), research/deepening-2026-05-18/11 (Tang + Weyl Plurality).

### §8.4 Concrete actions

**Сейчас (Phase 0):**

1. **W3C VC v2.0 spec preamble** прочитать (first 20 страниц) — production-ready substrate primary candidate
2. **TimeBanks 4 principles** в Pillar C Tier 1 / Workshop curriculum incorporate как positive R12 framing
3. **Read Graeber «Debt» chapter 1-3** (если ещё не) — anthropological frame для H8

**Phase 1:**

4. **PGP web-of-trust pilot** — 10-person first Clan key-signing party as proof-of-concept; FPF artifacts as PGP-signed claims
5. **Stack Overflow downfall pre-mortem** — где Jetix рискует SO trajectory (gamification eats ecology)?
6. **TimeBanks failure mode parity** — где Jetix рискует «flat-currency-no-skill-signal»? FPF schema must differentiate

**Phase 2:**

7. **W3C VC v2.0 implementation pilot** — first Workshop graduate gets VC-formatted attestation; SpruceID / TruAge как reference
8. **Quadratic Funding для first Clan revenue distribution** — Gitcoin pattern applied к hypothetical 10-person Workshop
9. **«Plurality» book deep read** (Tang/Weyl 2024) — H4+H7+H8 cross-cluster overlap (см. research/deepening-2026-05-18/11)

**Phase 3+:**

10. **Mondragón study visit possible** (Спания, Country Basques) — 68-летний working cooperative; intelligence gathering

### §8.5 Резюме на 2 строки

**5 categories trust-beyond-money: TimeBanks (Cahn) / PGP WoT (1992, 34yrs) / W3C VC v2.0 (Rec May 2025) / Quadratic Voting (Weyl) / Mondragón (70 years cooperative).** Для H8 layered approach: PGP + VC v2.0 + Mondragón cooperative logic; avoid Stack Overflow gamification + Friend.tech financialization attractors.

---

*Plain English section added by brigadier 2026-05-18 per Ruslan request. Word count of §8: ~750.*

