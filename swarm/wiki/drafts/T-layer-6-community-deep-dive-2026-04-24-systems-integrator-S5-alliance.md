---
title: "§5 Alliance Architecture — 3 Legal-Structure Options for Mittelstand AI Alliance"
type: systems-integrator
produced_by: systems-expert
mode: integrator
cycle_id: cyc-layer-6-community-deep-dive-2026-04-24
task_id: T-layer-6-community-deep-dive-2026-04-24
cell: C-05
section: "§5 Alliance Architecture"
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: proposed
confidence: high
confidence_method: F-G-R-coherence
provenance_inline: true
sources:
  - {path: "swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md", range: "§6.3 Alliance 3 options binding"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§§3-9 Mittelstand AI Alliance / EISA moment / 7 advantages"}
  - {path: "decisions/JETIX-VISION.md", range: "D20 USB-C + D21 Roy-replication + §5 Long-term Phase 3+"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D27 Fork-and-merge governance + USB-C reinforcement"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md", range: "§2.7 + §8 governance open questions"}
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", range: "§6 USB-C/McKinsey-platform resolution"}
locks_cited: [D13, D15, D20, D21, D27]
investor_peer_input: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S5-alliance-roi.md (referenced, not duplicated — unit-econ ROI per option lives there)"
acceptance_predicate: "count(options) == 3 AND each_option covers {governance, IP, revenue, membership_tiers, phase_fit, risks} AND brigadier_recommendation names ONE option with D13+D20+D21+D27 rationale AND risks_section covers {antitrust, capture, fork-tension, timing} AND count(F-G-R-tagged_claims) >= 4"
---

# §5 Alliance Architecture — 3 Legal-Structure Options for Mittelstand AI Alliance

## Preface — context and positioning frame

The Mittelstand AI Alliance is the vehicle through which Jetix executes the EISA-moment thesis articulated in STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT §3-§4: *«Mittelstand AI Alliance = EISA moment — positioning as sovereign European AI consortium»* [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§4]. The core observation from that document is that the AI market in 2026 structurally mirrors the PC market in 1982: a latent demand for a standard that business can stake a 10-year commitment on, blocked by three buying frictions the Mittelstand feels acutely — data-privacy fear (GDPR / EU AI Act), vendor lock-in risk, and cross-contamination of client knowledge.

The Alliance does not exist yet. As of 2026-04-24 it is concept-only, with no legal entity, no formalized members, and no governance documents [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md#§5]. What does exist is the strategic intent (D20 USB-C universal connector + D21 Roy-replication) and the architectural principle that will govern whatever legal form is chosen (D27 Fork-and-merge governance + D13 Closed core / Open surface).

The systems lens applied in this section models each legal-structure option as a distinct socio-technical system with its own boundary, feedback loops, leverage points, and VSM (Beer, Stafford — «Brain of the Firm» book-as-frame) level-structure. Each option places Jetix in a different position within that VSM. The choice of legal structure is not merely administrative — it determines which feedback loops amplify, which dampen, and whether Jetix retains enough System-5 identity-and-policy authority (VSM Level 5 per Beer) to steer the Alliance without losing the revenue-extraction capability that funds Phase-3+ trajectory.

The investor-expert peer cell (`swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S5-alliance-roi.md`) carries unit-economic ROI projections per option. This document references that cell's conclusions where relevant but does not duplicate the arithmetic.

The window STRATEGIC-INSIGHT §8 names is 6-12 months from 2026-04-24. Delay beyond that risks a competitor staking the EISA position first [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§8 recommendation #5: *«Speed: window NOW — 6-12 месяцев максимум чтобы захватить position»*]. The legal-structure choice therefore has a timing dimension: the wrong option chosen fast is still better than the right option chosen two years late.

---

## §5.1 Option A — Non-profit consortium (Linux Foundation analog)

### Governing inspiration

Option A models Jetix's Alliance on the Linux Foundation (501(c)(6) US non-profit) and the Eclipse Foundation (AISBL Belgian non-profit). These structures are purpose-built for vendor-neutral technical standards bodies: multiple competing commercial players co-invest in shared infrastructure they individually could not justify funding alone. The EISA analog from STRATEGIC-INSIGHT §1 is structurally equivalent: EISA (Extended Industry Standard Architecture, 1988) was the non-IBM consortium that broke IBM's MCA monopoly by publishing an open bus standard. Nine companies pooled resources; none could have done it alone; the standard spread precisely because no single vendor controlled it.

### Governance

Under Option A, the Alliance is governed by a board elected by paying member organizations. Technical decisions are delegated to working groups organized around specific domains (e.g., a «Local-First AI Compliance» working group, a «Mittelstand Onboarding Protocol» working group, a «Fork-and-Merge Methodology» working group). Board composition follows a tiered voting model:

- **Founding members** (committed at Alliance formation, likely €50K–€200K annual dues): 2 seats each, weighted vote.
- **Strategic members** (major Mittelstand enterprises or institutional funders, €20K–€50K/year): 1 seat each, full vote.
- **Regular members** (Mittelstand SMBs, €5K–€20K/year): aggregate representation — every N regular members elect 1 board representative, non-weighted.
- **Observer members** (researchers, non-profits, individual practitioners, €500–€2K/year): no vote; right to attend working group sessions; access to methodology drafts before publication.

Jetix, as the founding methodology steward, would hold a permanent **technical-steward seat** on the board (non-voting on governance matters, voting on technical adoption decisions) plus a **BDFL-style veto on methodology core changes** during Phase-2 (€200K–€1M): the veto right expires or transitions to a super-majority requirement in Phase-3+ as the methodology matures and trust accumulates.

VSM view: under Option A, Jetix occupies System-5 (identity/policy) and System-4 (intelligence/futures) only during a defined founding period. As the board grows, System-5 authority diffuses to the board as a collective. Jetix's effective control gravitates toward System-3 (audit) — it can audit whether the methodology is implemented correctly, but cannot unilaterally decide the methodology's future direction once a sufficient board quorum exists. This is a deliberate design in the Linux Foundation model and is exactly the concern Senge's «the cure can be worse than the disease» (Fifth Discipline, law 7) flags: the cure for Mittelstand's vendor-lock-in fear (radical vendor-neutrality) becomes the disease for Jetix's ability to steer strategic direction.

### IP model

Vendor-neutral, permissive open source. The methodology specification, templates, and compliance checklists published under Apache 2.0 or an equivalent permissive license. No royalties. Contributions from members governed by a Contributor License Agreement (CLA) that grants the Alliance perpetual, irrevocable license to incorporate and redistribute.

The closed core (D13) can still be preserved — Jetix's internal operational configs, specific prompt architectures, and proprietary calibration methods are not required to be contributed to the Alliance. What is contributed is the *surface*: the methodology documentation, the compliance framework, the fork-and-merge protocol specification. This is precisely the D13 grammar: open surface (documentation, templates, patterns), closed core (Jetix's specific implementations).

However, the risk under Apache 2.0 is that any competitor can fork the methodology specification, implement it better, and offer it without membership dues or attribution obligation. The Apache 2.0 license permits this. The Linux Foundation's historical experience shows this is not catastrophic — the network effects of the Alliance membership itself (human relationships, first-mover brand, working group access) create stickiness that license terms alone cannot. But Jetix must accept that the methodology documents, once published under permissive terms, are effectively public goods.

### Revenue model

No revenue at the Alliance entity level beyond operational expenses. Member dues fund:
- Working group coordination (staff, tooling, event hosting).
- Methodology publication and maintenance.
- Compliance certification audits (see below).
- Annual summit (European Mittelstand AI Summit — a brand asset in itself).

Certification fees can be structured as cost-recovery, not profit-generating: Mittelstand firms pay a certification fee to receive an «Alliance-Certified Mittelstand AI Implementation» designation, with fees funding the certification apparatus. Jetix-Corp (a separate for-profit entity that would need to exist alongside the non-profit) earns consulting revenue by helping firms achieve certification — this is the Red Hat model nested inside a Linux Foundation structure.

**What Jetix does NOT receive from Option A:** dividends, licensing royalties, or equity upside from the Alliance entity itself. Jetix's revenue must flow entirely through Jetix-Corp's consulting and services business, which is adjacent to but legally separate from the Alliance.

### Membership tiers and pricing

| Tier | Annual dues | Rights | Target |
|---|---|---|---|
| Founding | €100K–€200K | 2 board seats; methodology co-authorship; name on founding charter | 3–5 large Mittelstand enterprises or institutional sponsors (DACH chambers, industry associations) |
| Strategic | €20K–€50K | 1 board seat; working-group leadership eligibility; certification priority | 10–20 mid-size Mittelstand firms or consulting partners |
| Regular | €5K–€20K | Working group participation; methodology access; certification path | 50–200 Mittelstand SMBs Phase-2+ |
| Observer | €500–€2K | Read-only access; annual summit attendance; newsletter | Researchers, individual practitioners, startups |

At Phase-2 entry (€200K Jetix validation gate, per D15), realistic founding cohort: 3 founding members + 5 strategic + 20 regular + 50 observer = total dues revenue approximately €600K–€1.2M/year — enough to fund a small Alliance staff and working groups. Jetix-Corp consulting on top of this is the actual revenue engine.

### Phase-1 vs Phase-2+ fit

**Phase-1 (€0–€50K, current):** formal Option A legal structure is premature and capital-destroying. A 501(c)(6) US filing or Belgian AISBL costs €15K–€30K in legal fees alone, requires board formation, and creates governance obligations that distract from Phase-1's only job: generating the first €50K in consulting revenue. What IS viable in Phase-1: an informal **«Mittelstand AI Alliance Working Group»** — a Telegram or Slack group of 5–15 Mittelstand contacts who receive early access to methodology drafts, provide feedback, and implicitly become the founding cohort. No legal entity. No dues. A wait-list and an informal charter document (1 page). This seeds the network without incurring formation costs.

**Phase-2 trigger (€200K validation, D15):** formal non-profit formation becomes viable. Legal budget available; first paying clients provide proof-of-concept for methodology claims; first external parties credibly want Alliance membership because Jetix has demonstrated value. This is the earliest Option A makes structural sense.

**Phase-2+ fit:** Option A is the correct structure if Jetix's primary goal is broad adoption of the Mittelstand AI standard with Jetix-Corp as the dominant consulting/services beneficiary. It sacrifices direct methodology revenue in exchange for network-scale adoption. The bet is that standards-level adoption is worth more than proprietary licensing — the Intel/Microsoft lesson from STRATEGIC-INSIGHT §1: they did not own the BIOS, but they owned the layers above, and those layers produced trillions.

**What Option A requires from Jetix:**
- A for-profit Jetix-Corp entity running in parallel (German GmbH or equivalent) to capture consulting revenue.
- Legal budget: €20K–€50K for non-profit formation (Phase-2 unlock).
- Board recruitment: at least 3 founding members willing to pay €100K+ dues before Jetix has full market proof — the hardest Phase-2 constraint.
- Methodology documentation mature enough to publish under permissive license: at minimum, the methodology surface (templates, compliance framework) must be publication-ready.

### Risks specific to Option A

**R1 — Board capture.** Once the Alliance board has sufficient paying members, a coalition of large corporate members can outvote Jetix's technical-steward position and redirect the methodology. Historical Linux Foundation analog: major cloud vendors have repeatedly shaped Linux Foundation working group priorities toward their own infrastructure needs. Mitigation: BDFL veto right locked in founding charter for Phase-2 duration; sunset clause negotiated explicitly.

**R2 — Revenue disconnection.** Jetix's revenue flows only through Jetix-Corp consulting, not through the Alliance. If a large consulting firm (Deloitte, McKinsey) joins as a Strategic member and leverages the Alliance methodology to displace Jetix-Corp on client engagements, Jetix loses the very revenue the Alliance was meant to enable. The Alliance structure has no mechanism to prevent this — it is structurally vendor-neutral. Mitigation: keep proprietary-calibration-layer in the closed core (D13); ensure Jetix-Corp's consulting advantage is non-replicable by methodology documentation alone.

**R3 — Slow formation.** Recruiting founding members willing to pay €100K+ dues requires proof of value Jetix does not yet have in Phase-1. The chicken-and-egg loop: Mittelstand joins when Alliance has credibility; Alliance gains credibility when Mittelstand joins. Mitigation: Phase-1 informal working group seeds the founding cohort without financial commitment; Phase-2 formation follows demonstrated consulting ROI.

**R4 — German cartel office scrutiny.** A non-profit consortium of Mittelstand AI players, setting methodology standards, has structural similarity to a cartel (price coordination through standardized implementation costs). The Bundeskartellamt (German Federal Cartel Office) monitors such structures closely. Mitigation: Alliance methodology must be clearly framed as interoperability standard (like USB-C), not as barrier to entry or price-fixing mechanism. Legal counsel (Germany-based, competition law specialty) required before first formal member recruitment.

**VSM failure mode under Option A:** as board grows, System-5 authority diffuses. Jetix risks becoming a System-1 (operations) contributor within an Alliance it no longer steers. The VSM diagnostic: when does Jetix go from Level-5 to Level-1? When the board's strategic decisions consistently override Jetix's technical-steward position. Senge law 7 in direct application: the cure (vendor-neutral governance) for Mittelstand's disease (vendor lock-in fear) creates Jetix's disease (loss of strategic control).

---

## §5.2 Option B — For-profit standards body (ARM Holdings analog)

### Governing inspiration

Option B takes the ARM Holdings / Qualcomm IP licensing model as its structural analog. ARM does not manufacture chips; it designs the architecture and licenses the instruction set under per-instance royalty or one-time license fees. Every device using an ARM chip pays ARM. The licensee builds on top of the architecture; ARM owns the standard. From STRATEGIC-INSIGHT §8: the recommendation to pursue *«Patents on AI×Mittelstand method combinations — licensable assets»* with a D15 trigger at €200K is the direct seed of this option.

Under Option B, Jetix-Corp (or a Jetix Holding entity, per D19) retains full majority control of the Alliance. External «license partners» receive the right to implement the methodology under defined licensing terms in exchange for per-instance fees, royalties, or certification fees payable to Jetix. External partners get observer seats on a technical advisory board — they can influence but not control the methodology's direction.

### Governance

**Jetix retains System-5 authority in perpetuity.** This is the defining structural difference from Option A. There is no member-elected board with power over Jetix. Instead:

- **Jetix Holding** (legal entity, GmbH or UG initially; AG if Phase-3+ capital markets are considered) owns the methodology IP, the trademark «Mittelstand AI Alliance», and the certification process.
- **Technical Advisory Board (TAB)** composed of license partners (one representative per Strategic licensee), Jetix technical staff, and 1-2 independent domain experts (AI / compliance / Mittelstand industry). TAB advises; Jetix decides.
- **BDFL model:** Ruslan retains effective veto authority over methodology changes, as explicitly named in the founder-orbit principle from JETIX-VISION §3 (*«Архитектор-орбита (non-delegatable): стратегия, вкус, ответственность, утверждение, эскалация, отношения»*).

VSM view: Jetix occupies System-5 (identity), System-4 (intelligence/futures — ARM's core competency is roadmapping the next architecture generation), and System-3 (audit — certification process). License partners operate at System-1 (operations) and System-2 (coordination among themselves). Jetix does not manufacture; it designs and licenses. This is structurally more defensible than Option A from a control standpoint, but generates significantly more friction in the Mittelstand market, where the core buying objection is exactly vendor lock-in.

### IP model

Proprietary. The methodology specification, templates, compliance checklists, and the «Mittelstand AI Alliance» trademark are Jetix IP, registered in Germany and/or EU. Licensing terms per partner tier:

- **Tier-1 (OEM/System Integrator licensees):** one-time license fee + annual renewal. Right to embed the methodology into their own service delivery and use the Alliance trademark in marketing. Example: a German SAP implementation partner pays a one-time €50K license + €15K/year renewal to deliver «Mittelstand AI Alliance-certified implementations» to their clients.
- **Tier-2 (Per-instance royalty):** applicable to software tooling implementations. Per-client deployment of a methodology-based tool generates a royalty stream to Jetix. Relevant if any licensee builds software on top of the methodology (vs. pure consulting services).
- **Certification fees:** Mittelstand firms pay Jetix (or authorized certification bodies) to receive the Alliance-Certified designation. €5K–€20K per certification audit, depending on firm size.

Under Option B, D13 (Closed core / Open surface) has a different implementation than under Option A: the surface that is published is documentation of the interface (what the methodology does, what the certification criteria are), NOT the methodology itself (how it works internally). This is closer to the BIOS-as-published-documentation-but-legally-protected model that STRATEGIC-INSIGHT §3 explicitly names.

### Revenue model

Revenue flows directly to Jetix (via Jetix Holding or Jetix-Corp depending on entity structure). Three streams:

1. **License fees:** one-time + annual renewal per licensee. Forecasted by investor-expert peer cell.
2. **Certification fees:** per-firm certification audit revenue.
3. **Premium services:** Jetix-led engagements for licensees who need methodology deep-dives, custom adaptation of the methodology to their client vertical, or audit-remediation support.

Profit is distributed to Jetix shareholders (Ruslan, and in Phase-3+ potentially a small cap table including early alliance partners who receive equity in lieu of membership dues — an ARM-style model where founding chip vendors received equity stakes in early ARM Ltd.).

**What Jetix receives from Option B:** direct licensing revenue from every firm that implements the methodology at scale. If 100 Mittelstand firms implement the methodology through 10 licensee consulting partners, Jetix earns on each implementation either through OEM license fees or per-instance royalties. This is the most capital-efficient revenue model from Jetix's perspective — methodology revenue is not dependent on Jetix-Corp winning each individual consulting engagement.

### Membership tiers and pricing

Under Option B, «membership» is reframed as «licensing»:

| Tier | Fee structure | Rights | Target |
|---|---|---|---|
| OEM/Integrator License | €50K one-time + €15K/year | Implement methodology for clients; use Alliance trademark; TAB observer seat | German SAP/IT integrators, boutique AI consultancies serving Mittelstand |
| Platform License | €20K one-time + €8K/year + €500/deployment royalty | Embed methodology in software product; certification mark on product | HR-tech, ERP, workflow-automation SaaS vendors targeting Mittelstand |
| Direct Certification | €5K–€20K per audit | «Alliance-Certified» designation for one Mittelstand firm (renewable annually) | End-client Mittelstand firms who want the certification mark for their own clients |
| Observer / Research | €2K/year | Read-only access to methodology drafts; TAB meeting notes; no usage rights | Researchers, industry analysts, policy bodies |

### Phase-1 vs Phase-2+ fit

**Phase-1 (€0–€50K):** Option B legal structure is not viable in Phase-1 — patents are not yet filed (D15 trigger at €200K), the methodology is not yet proven at market scale, and the ARM Holdings model requires a degree of IP moat (patents + trademark + trade secrets) that does not exist at Phase-1. Attempting Option B in Phase-1 would be legally hollow: licenses sold without backed IP are contractually weak and commercially unpersuasive.

**Minimum entry gate:** D15 patent budget trigger (€200K Phase-2 unlock). This is explicit: STRATEGIC-INSIGHT §8 recommendation #4: *«Patents on AI×Mittelstand method combinations — licensable assets (locks in D15 revenue-gated: patent budget €200K+)»*. Before €200K, Option B exists only informally — early «intent-to-license» conversations with potential integrator partners can begin in Phase-2-early, but no formal licensing contracts should be signed until IP protection is in place.

**Phase-3+ fit:** Option B scales best once the methodology is patent-protected and the certification mark has market recognition. At €1M+ revenue, Jetix can fund a dedicated licensing operations function. At $100M+, the model resembles ARM's structure: a relatively small Jetix IP team licensing to hundreds of implementation partners, each generating royalty streams.

**What Option B requires from Jetix:**
- Patent filing budget: €50K–€150K (Germany + EU patents, AI-method combinations). Phase-2 unlock D15.
- Trademark registration: «Mittelstand AI Alliance» in Germany and EU (~€5K, faster than patents).
- Legal infrastructure for licensing contracts (German IP law counsel).
- Market credibility sufficient for partners to pay license fees: minimum 3-5 signed consulting clients demonstrating methodology ROI before first OEM licensee is realistic.

### Risks specific to Option B

**R1 — Mittelstand vendor-lock-in rejection.** STRATEGIC-INSIGHT §3 explicitly names vendor lock-in fear as the core buying friction for the Mittelstand: *«Бизнес боится AI из-за: Утечка данных / Compliance / Vendor lock-in»*. Option B IS a proprietary standard. Mittelstand buyers who have been burned by SAP lock-in, Microsoft lock-in, and Oracle lock-in are structurally predisposed to avoid proprietary methodology lock-in. The marketing challenge under Option B is massive: Jetix must position a proprietary standard as preferable to a vendor-neutral one. Historical evidence suggests this is very hard in B2B markets where procurement departments have learned to include «avoid single-vendor dependency» as a requirement. The ARM model works because there is no open hardware ISA with equivalent market adoption — in AI methodology, open alternatives will exist.

**R2 — Patent validity risk.** AI-method patents are under intense legal scrutiny in the EU. The European Patent Office has narrow patentability criteria for software and business methods — «AI methods» per se are not patentable; only specific technical implementations may qualify. If Jetix's patent applications are rejected or invalidated, the entire IP moat of Option B collapses, leaving the proprietary licensing structure without legal backing. Mitigation: work with specialized AI/software IP counsel; design patent strategy around specific technical innovations (the local-first KB architecture, the fork-and-merge synchronization protocol) rather than abstract methodology claims.

**R3 — Competitor open-source preemption.** If a well-resourced competitor (another AI consultancy, or an open-source project backed by a major cloud vendor) publishes an equivalent AI methodology for Mittelstand under Apache 2.0 before Jetix's patents are filed, Option B is neutralized. The open-source alternative would have zero licensing friction, and Jetix's proprietary approach would lose adoption. STRATEGIC-INSIGHT §8 names the 6-12 month window precisely because this risk is real and time-bounded.

**R4 — Senge Law 7 — the push-back.** «The harder you push, the harder the system pushes back» (Senge, «The Fifth Discipline», law 2). Aggressive proprietary licensing in a market where the core buying objection is proprietary lock-in will generate systematic market resistance — not individual buyer refusals, but a coordinated market-level response (e.g., German Mittelstand associations explicitly recommending against «Jetix-locked» implementations). The feedback loop: proprietary license → Mittelstand resistance → reduced adoption → reduced license revenue → Jetix doubles down on proprietary enforcement → greater resistance. This is a reinforcing negative spiral under conditions where the market already has strong anti-proprietary priors.

**R5 — Antitrust (German cartel law).** A for-profit standards body that controls certification in a specific market segment can attract Bundeskartellamt attention for different reasons than Option A: not cartel (price-fixing), but abuse of market-dominant position (foreclosure of competition through licensing terms). If Jetix sets certification criteria that only Jetix-affiliated implementations can meet, the cartel office may intervene. Mitigation: ensure certification criteria are technically objective and independently auditable; do not set criteria that specifically disadvantage non-Jetix implementations.

**VSM failure mode under Option B:** without adequate market adoption (which Option B's proprietary framing makes harder to achieve), Jetix's licensing revenue stream never materializes. Jetix ends up holding expensive IP that nobody wants to license because the market chose the open alternative. The System-5 authority Jetix preserves under Option B becomes authority over an empty system — a federation of zero.

---

## §5.3 Option C — Hybrid (non-profit methodology upstream + for-profit services downstream)

### Governing inspiration

Option C takes the Mozilla Foundation + Mozilla Corporation dual-entity model and the Red Hat + Fedora community model as its structural analogs. Mozilla Foundation (non-profit) owns the Firefox brand and governs browser development; Mozilla Corporation (wholly-owned for-profit subsidiary) generates revenue from search partnerships and Firefox services. Red Hat (for-profit) is the primary commercial contributor to Fedora (open community project), extracting revenue through enterprise support, certification, and managed services while the open community provides the methodology innovation substrate.

Applied to Jetix: the **Mittelstand AI Alliance Foundation** (non-profit entity, ideally German gemeinnützige GmbH or Belgian AISBL) governs the upstream methodology — the specification, templates, compliance framework, and fork-and-merge protocol. **Jetix-Corp** (German GmbH, Ruslan's existing or soon-to-exist legal entity) delivers for-profit consulting, tooling, certification services, and premium methodology implementations. The Foundation publishes the methodology openly (under a permissive or weak-copyleft license); Jetix-Corp earns revenue by being the most credible implementer of that methodology.

### Governance

**Two-tier governance structure:**

**Foundation tier (upstream):**
- Governed by a Foundation Board composed of founding member representatives + 1-2 independent experts + Jetix's permanent technical-steward seat (non-profit board role, not paid director position).
- Foundation Board governs: methodology specification updates, fork-and-merge protocol rules (per D27), certification criteria (technical), and the Alliance brand license terms.
- Technical Steering Committee (TSC) under the Foundation Board: working groups per methodology domain. TSC decisions require simple majority; Foundation Board ratification for major version changes.
- **Jetix's leverage point in the Foundation:** technical-steward seat with veto right on methodology-core changes (written into founding charter, time-limited to Phase-2 duration then transitioning to super-majority requirement). Ruslan's BDFL principle applies here — he is the permanent upstream-methodology architect, a role with explicit authority but no day-to-day operational control of Foundation staff.

**Jetix-Corp tier (downstream):**
- Jetix-Corp is Ruslan's for-profit operating entity. Fully independent of the Foundation legally, but the primary commercial contributor to Foundation working groups.
- Jetix-Corp earns revenue through:
  - Consulting engagements using the methodology.
  - Certification-as-a-service (auditing Mittelstand firms for Alliance certification — the Foundation sets the criteria, Jetix-Corp runs the audits under a service agreement).
  - Premium tooling (Jetix-proprietary tooling that implements the methodology faster than the open alternative — this is the closed core per D13).
  - Training and onboarding programs for other consultancies who want to implement the methodology.
  - Roy-replication licensing (Phase-3+): other consulting firms pay Jetix-Corp to license the roy-replication operating model and the swarm-agent architecture — these are NOT contributed to the Foundation; they live in Jetix's closed core.

VSM view: the Foundation operates at System-4 (intelligence — tracking methodology evolution, Mittelstand market signals) and System-3 (audit — certification standards). Jetix-Corp operates at System-1 (operations — client delivery) and System-2 (coordination — matchmaker, partner network). Jetix-Ruslan retains System-5 (identity/policy) through the Foundation technical-steward role and the absolute non-delegation of strategy/taste/responsibility from JETIX-VISION §3. The key VSM insight: Option C is the only structure where System-5 (Ruslan + Jetix identity) can remain coherent while System-1 (consulting delivery) scales through the Foundation's ecosystem rather than only through Jetix-Corp's headcount.

D27 Fork-and-merge governance maps directly onto the Foundation: the canonical upstream is the Foundation methodology repository; forks are Alliance member implementations; merge-back is the contribution process [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]. This is not metaphorical — the Foundation's governance IS the fork-and-merge governance Ruslan articulated in audio_519.

### IP model

**Foundation layer:** methodology specification, templates, compliance checklists, and fork-and-merge protocol published under a **weak-copyleft license** (Apache 2.0 permissive for documentation; LGPL-equivalent for any software components). The weak-copyleft choice (vs. strong copyleft like GPL) allows commercial implementations without requiring them to open-source their entire stack — Mittelstand clients can implement the methodology in their proprietary processes without the Foundation claiming rights to their internal systems. This is the right balance for enterprise adoption.

**Jetix-Corp layer:** tooling, agent configurations, swarm architectures, proprietary calibration methods, and the roy-replication operating model remain fully proprietary to Jetix-Corp. These are the D13 Closed core assets — they are never contributed to the Foundation and are licensed commercially only. A competitor can read the Foundation's methodology documentation and implement the methodology; they cannot replicate Jetix's specific tooling or swarm architecture without starting from scratch.

**Trademark layer:** «Mittelstand AI Alliance» trademark owned by the Foundation (non-profit hold). Jetix-Corp licensed by the Foundation to use the trademark in commercial engagements as the primary certified implementer. This prevents Jetix-Corp from being the trademark gatekeeper (which would expose it to the ARM-style proprietary-standard antitrust risk) while ensuring the brand is not fragmented across hundreds of low-quality implementations.

### Revenue model

Option C generates revenue for Jetix-Corp through five streams that the investor-expert peer cell carries in full detail:

1. **Consulting revenue:** direct Mittelstand AI implementation consulting at €150/hour baseline (D3 Phase-1 pricing), scaling to productized packages (D18) as methodology matures.
2. **Certification-as-a-service:** Jetix-Corp runs certification audits under a service agreement with the Foundation. Per-audit fees (€5K–€20K) flow to Jetix-Corp (minus a Foundation contribution percentage, e.g., 20%). Volume scales with Alliance membership growth.
3. **Premium tooling subscription:** proprietary tooling implementing the methodology faster/better than the open-source equivalent. Monthly SaaS-style subscription per deployment. This is the «Mittelstand OS» as described in STRATEGIC-INSIGHT §3, delivered as a managed service.
4. **Training + train-the-trainer:** Jetix-Corp trains other consultancies to deliver Alliance-certified implementations. Per-cohort fee. This is the roy-replication vector at methodology scale — every trained consultancy becomes a distribution channel for Alliance methodology adoption, expanding the Foundation's footprint while generating Jetix-Corp revenue.
5. **Roy-replication licensing (Phase-3+):** consulting firms wanting to license the full Jetix operating model (swarm agents + wiki architecture + protocols) pay Jetix-Corp a license fee. This is separate from the Foundation and operates entirely in the commercial tier.

The Foundation itself is funded by:
- Corporate membership dues (€5K–€100K/year depending on tier — structured identically to Option A's founding/strategic/regular/observer tiers but at lower amounts because commercial value is extracted through Jetix-Corp, not the Foundation).
- Corporate donations from Mittelstand industry bodies (German chambers of commerce, Mittelstand industry associations, EU digital-transformation funds).
- Grant funding: EU Horizon Europe «trustworthy AI» grants, German government digital-Mittelstand programs.
- Sponsorship of the annual European Mittelstand AI Summit.

### Membership tiers and pricing

The Foundation membership tiers govern access to upstream methodology and community:

| Tier | Annual dues | Rights | Target |
|---|---|---|---|
| Founding | €50K–€100K | 2 Foundation Board seats; working-group leadership; early-access to methodology drafts; named on founding charter | 3–5 Mittelstand enterprises or industry associations willing to co-found the Alliance |
| Strategic | €10K–€50K | 1 Foundation Board seat; TSC voting membership; methodology draft access 30-day early | 15–30 Mittelstand enterprises Phase-2+ |
| Regular | €2K–€10K | Working-group participation; published methodology access; certification-path support | 100+ Mittelstand SMBs Phase-3+ |
| Observer | €300–€1K | Newsletter; annual summit attendance; public methodology access only | Researchers, individual practitioners, policy bodies |

Note: pricing is lower than Option A's equivalent tiers because the commercial value to Mittelstand firms comes from Jetix-Corp services (consulting, tooling, certification), not from Foundation membership benefits alone. The Foundation membership is the community and legitimacy vehicle; Jetix-Corp is the revenue vehicle. This bifurcation prevents the «membership-as-product» trap where the Foundation has to deliver enormous membership ROI or face churn.

### Phase-1 vs Phase-2+ fit

**Phase-1 (€0–€50K, current):** the Foundation does not exist yet. This is identical to Option A in Phase-1: an informal «Mittelstand AI Alliance Working Group» operates without legal structure. Jetix-Corp IS Jetix-the-consulting-business (Ruslan solo + Cloud Cowork). The «closed core / open surface» split exists conceptually but is not institutionalized. The Phase-1 action is: (a) operate the informal working group, (b) document the methodology surface in publishable form (templates, compliance checklist drafts, fork-and-merge protocol specification), and (c) begin identifying 3 potential founding members willing to co-fund the Foundation at Phase-2.

**Phase-2 trigger (€200K validation, D15):** Foundation formation. Legal budget available (€20K–€30K for German gemeinnützige GmbH). First 3 founding members recruited from the Phase-1 informal working group — they have already seen the methodology in action through early consulting engagements and have proof of ROI. Foundation publishes first version of methodology under Apache 2.0. Jetix-Corp begins certification-as-a-service. This is the critical Phase-2 gate event for Option C.

**Phase-3+ (€1M+):** Foundation has 50–200 member organizations; Jetix-Corp has 10–20 roy-replication licensees; certification is a meaningful revenue stream; the methodology has been forked and adapted by 5–10 external implementations, with the best merge-back contributions improving the canonical upstream. This is the Red Hat + Fedora flywheel: open community drives adoption, commercial entity captures revenue from the organizations that need support, certification, and premium tooling.

**What Option C requires from Jetix:**
- Dual-entity legal structure (non-profit Foundation + for-profit Corp): €30K–€50K legal fees at Phase-2.
- Clear IP contribution agreement: what Jetix contributes to the Foundation and what it retains as proprietary must be specified in writing at formation — this is the critical governance document.
- Board recruitment (same constraint as Option A: 3 founding members willing to pay €50K+ before market proof).
- Methodology surface publication-ready by Phase-2.
- Ruslan's ongoing technical-steward role in the Foundation (non-trivial time commitment — estimated 4–6 hours/week in Phase-2, declining as Foundation governance matures).

### Risks specific to Option C

**R1 — Structural complexity.** Two legal entities, one governance structure, two sets of stakeholder obligations. Phase-2 operational burden is higher than Option A (one entity) or Option B (one entity). The risk is that Ruslan spends Phase-2 time on Foundation governance rather than on Jetix-Corp revenue generation. Mitigation: minimize Foundation operational complexity — hire a part-time Foundation coordinator at Phase-2 (funded by member dues); keep Foundation scope narrow (methodology publication + certification criteria only); all commercial operations remain at Jetix-Corp.

**R2 — Fork-community tension when upstream and downstream conflict.** When the Foundation's TSC wants to evolve the methodology in a direction that reduces Jetix-Corp's differentiation (e.g., standardizing a component that Jetix-Corp sells as a premium service), internal conflict arises. The Ruslan BDFL veto right is the structural resolution — but using the veto visibly, in a community setting, creates political friction. Mitigation: D13 (Closed core) is the resolution grammar. Things in the Foundation are by definition open surface; Jetix-Corp's competitive advantage must live exclusively in the closed core. If Jetix-Corp's premium service is replicable from the methodology specification, Jetix-Corp's product strategy needs revision, not the Foundation's veto.

**R3 — «Mozilla problem» — foundation capture + corp under-funding.** Mozilla's dual-entity structure has suffered from corporate under-investment in the Foundation mission when commercial revenue fell. The Foundation became seen as a brand custodian, not a methodology innovator. Mitigation: Jetix-Corp commits a defined percentage of revenue (e.g., 10–15%) to Foundation operations via a service/contribution agreement written into the founding charter. This creates a structural revenue flow from commercial to upstream, preventing the under-funding spiral.

**R4 — Antitrust (Option C-specific):** a non-profit foundation that is effectively controlled by a for-profit company (through the technical-steward BDFL veto) is a well-known antitrust trigger in EU competition law. The Bundeskartellamt has investigated similar structures. Mitigation: the BDFL veto must be time-limited in the founding charter (Phase-2 duration only; transitions to super-majority requirement at Phase-3+ or at a defined Foundation membership milestone); the TSC must have genuine independent decision authority on non-core matters; external Foundation board members must be independently credible (not Jetix affiliates).

**R5 — Timing risk.** Option C requires more formation time than Option B (two entities, more complex governance) and more founding-member recruitment than a simple consulting firm. If the 6-12 month window STRATEGIC-INSIGHT §8 names closes before the Foundation is formed and publicly announced, a competitor can claim the EISA position with a simpler structure. Mitigation: the informal working group (Phase-1 action) creates the market positioning effect — the Alliance brand can exist informally before the legal entity does. A public «Mittelstand AI Alliance Working Group» announcement in Phase-1 is a legitimate signal without legal overhead.

---

## §5.X Brigadier recommendation

**Recommended option: Option C (Hybrid — non-profit methodology upstream + for-profit services downstream).**

The recommendation rests on four locked decisions that are all internally consistent with Option C and inconsistent with the alternatives at Phase-1-through-Phase-3 trajectory.

D13 (Closed core / Open surface) is the foundational grammar [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md referenced via D13 in STRATEGIC-INSIGHT §4]. Option C is the legal-structure instantiation of D13: the Foundation holds the open surface (methodology documentation, templates, compliance framework), Jetix-Corp holds the closed core (swarm architecture, proprietary tooling, roy-replication operating model, calibration methods). Option A forces too much into the open surface (the non-profit board can redirect what is published). Option B forces the open surface to be controlled proprietary access, which contradicts D13's intent and generates the Mittelstand vendor-lock-in rejection.

D20 (USB-C universal connector positioning) requires the standard to be genuinely open — Ruslan's verbatim: *«стандарт в мире AI-агентов как USB-C в электронике — будет присутствовать везде»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#USB-C]. USB-C is an open standard; it achieved ubiquity precisely because it is vendor-neutral. Option B (proprietary standard) is structurally incompatible with USB-C positioning — a proprietary standard cannot become ubiquitous in a market where the primary buyer objection is vendor lock-in. Option A achieves the USB-C positioning but at the cost of Jetix's commercial advantage. Option C achieves USB-C positioning at the Foundation level while preserving Jetix-Corp's commercial advantage through the closed-core layer.

D21 (Matchmaker + Roy-replication) maps cleanly onto Option C: every roy in another niche is a Foundation fork + Jetix-Corp commercial implementation. The Foundation governs the fork-and-merge protocol (per D27); Jetix-Corp earns from licensing the roy-replication operating model to each fork [src:decisions/JETIX-VISION.md#D21]. Under Option A, the non-profit board could redirect the fork-and-merge governance in ways that reduce Jetix-Corp's roy-replication revenue. Under Option B, potential roys would resist paying proprietary licensing fees for a standard they could reimplement from open alternatives.

D27 (Fork-and-merge evolution architecture) is architecturally synonymous with Option C's Foundation + Corp structure [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]: *«Jetix = canonical upstream (stable, curated) / Каждый client / partner / ecosystem participant может fork / Лучшие мутации возвращаются upstream»*. The Foundation IS the canonical upstream governance entity. This is not an analogy — D27 describes the governance model that Option C formalizes into legal structure.

The recommendation is easily reversible: Ruslan can ack Option C at the AWAITING-APPROVAL gate, proceed with Phase-1 informal working group (no legal entity required), and revisit the legal-entity decision at Phase-2 trigger (€200K). Choosing Option C now does not commit capital — it commits a strategic direction that can be refined as the market responds. Choosing Option A now would be equivalent but with a slightly different Phase-2 legal form; choosing Option B now requires patent-filing commitment that D15 explicitly gates to €200K, making it structurally unavailable in Phase-1.

**F-G-R tag for brigadier recommendation:**
- F: F4 (operational convention; rests on D13/D20/D21/D27 four-lock convergence — cross-lock coherence is the strongest available evidence at Phase-1 without market validation data)
- ClaimScope: holds for Phase-1 → Phase-3 trajectory; at Phase-4+ ($100M+), the Foundation governance may need a substantial redesign as the Alliance matures into a standard-setting body with regulatory involvement (D20's USB-C final form)
- R: refuted if Ruslan or first founding-member recruitment explicitly rejects non-profit Foundation structure AND market feedback shows Mittelstand buyers prefer proprietary certification marks over open standards — in that case, revisit Option B; accepted when Phase-2 Foundation is formed with ≥3 founding members and first certification revenue flows to Jetix-Corp

---

## §5.Y Risks across all options

### Antitrust risk (German cartel office — Bundeskartellamt)

All three options carry antitrust exposure, but the form differs. Option A (non-profit consortium of Mittelstand AI players) resembles a cartel in the Bundeskartellamt's pattern-matching: horizontal coordination among competitors under a shared methodology standard can be constructed as price coordination if the standard creates a barrier to entry or a uniform cost structure. The Bundeskartellamt is aggressive by EU standards — it was the first EU regulator to investigate Facebook's cross-platform data collection as an abuse of dominant position (2019). A Mittelstand AI methodology consortium will attract scrutiny as AI becomes economically significant. Mitigation across all options: methodology standards must be framed as interoperability infrastructure (enabling, not restricting competition); certification criteria must be independently auditable; no membership tier that excludes competitors from the certification process; antitrust counsel (German, competition law specialty) engaged before first founding-member recruitment regardless of option chosen.

Option B carries a distinct antitrust risk: a for-profit entity controlling a standards body and using certification as a revenue gate is a classic abuse-of-dominant-position pattern if the standard achieves market adoption. ARM Holdings has faced periodic scrutiny on exactly this point. Mitigation for Option B: certification criteria technically objective; licensing terms non-discriminatory; no exclusivity provisions.

Option C (hybrid) is the most complex antitrust structure and requires the most careful legal drafting — the Foundation's non-profit status does not immunize it from competition law if it is effectively controlled by a for-profit entity (Jetix-Corp). The Bundeskartellamt has pierced similar structures.

### Foundation capture by corporate sponsors

Options A and C share this risk: as the Foundation's member base grows, well-resourced corporate members (large German industrial conglomerates, international cloud vendors who want the Alliance methodology standardized in their preferred direction) can outspend the smaller Mittelstand SMBs in membership dues, accumulating board seats and redirecting Foundation priorities toward their commercial interests. Linux Foundation history provides abundant precedent: Amazon, Google, and Microsoft now effectively control the board priorities of multiple Linux Foundation projects through founding-tier membership. The Mittelstand AI Alliance Foundation faces the same structural vulnerability. Mitigation: cap the number of founding/strategic seats that any single organization class can hold; require that founding/strategic members commit to the Alliance's Mittelstand-sovereignty mission explicitly in the membership agreement (not just commercially motivated participation); Ruslan's BDFL veto right (in Option C) provides a structural backstop during Phase-2.

### Fork-community tension — when upstream contribution conflicts with Jetix-Corp interests

Under Option C, Jetix-Corp is the primary commercial implementer of the Foundation methodology. As the Foundation's working groups evolve the methodology, they will occasionally propose changes that make the open-source implementation of the methodology better — which can reduce the differentiation of Jetix-Corp's premium tooling. This is the Red Hat tension: Red Hat (Jetix-Corp equivalent) wants some components to remain complex enough that customers need Red Hat's support; the Fedora community (Foundation equivalent) wants to make those same components simpler and more self-serviceable. The tension is structurally unresolvable — it can only be managed. Management approach: D13 discipline must be explicitly maintained as a Foundation charter principle. The Foundation publishes the methodology specification; Jetix-Corp builds proprietary implementation tools on top. Whenever a Foundation proposal would codify into the specification something that currently lives in Jetix-Corp's closed core, the BDFL veto is the mechanism — but using it creates community friction. The structural solution: Jetix-Corp must continuously invest in closed-core innovation that runs ahead of what the Foundation can standardize, maintaining the differentiation gap. This is the Meadows leverage-point application: the leverage is not in defending existing differentiation but in continuously generating new differentiation faster than the Foundation can standardize it.

### Timing risk — Alliance formalization too early or too late

STRATEGIC-INSIGHT §8 names a 6-12 month window [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§8 recommendation #5]. Two failure modes:

**Too early:** formalizing the Alliance legal entity (Foundation or proprietary body) before Jetix has consulting proof-of-concept burns capital and credibility. A non-profit Foundation formed before the methodology has been validated in market produces a governance structure without content — the working groups have nothing real to work on, and founding members who paid €50K+ dues feel defrauded when the methodology turns out to be aspirational rather than operational. The reinforcing loop: credibility loss → founding member withdrawal → Alliance dissolution before it achieves critical mass. Mitigation: Phase-1 informal working group is the correct timing — test methodology validity through consulting engagements before formal Alliance launch.

**Too late:** waiting for full Phase-2 validation (€200K) to begin Alliance positioning means 2+ years of delay from 2026. A competitor who is watching the same EISA-moment dynamic can announce an informal «Mittelstand AI Consortium» in Q3 2026 and claim the brand position before Jetix formalizes. The brand position matters as much as the legal entity — announcing the «Mittelstand AI Alliance Working Group» publicly in Phase-1 costs nothing legally and costs almost nothing operationally, but stakes the brand claim in the market. This is the Option C Phase-1 action: public working-group announcement + informal methodology publication + first certification framework draft, all before the legal entity exists. The legal entity follows the brand and community; the brand and community do not follow the legal entity.

**F-G-R tag for timing risk claim:**
- F: F3 (multi-case pattern: Linux Foundation, Eclipse Foundation, EISA Consortium all show that informal community precedes legal entity; the pattern is consistent across cases)
- ClaimScope: holds for AI methodology standards in B2B markets; less applicable in hardware standards markets where IP protection is the primary driver (closer to Option B timing requirements)
- R: refuted if a competitor formalizes a Mittelstand AI consortium before Jetix's working-group announcement — in that case, Option B's proprietary certification becomes more strategically viable as a defensive play; accepted when working-group announcement generates ≥5 substantive interest responses from Mittelstand organizations within 60 days of publication

**F-G-R tag for Option A dissent (see dissents section):**
- F: F4 (operational convention; Linux Foundation model has 25+ years of evidence in software standards)
- ClaimScope: holds if the primary success criterion is breadth of adoption; does NOT hold if Jetix-Corp revenue capture is the primary criterion (Linux Foundation does not generate revenue for the Linux creator, Linus Torvalds — he earns through employment, not royalties)
- R: refuted if Option C's dual-entity complexity proves unmanageable at Phase-2 and causes operational failure; accepted when Option C Foundation is formed and first certification revenues flow to Jetix-Corp within 6 months of formation

---

## §13 Preserved dissents

### Dissent-1: Argument for Option A (Non-profit purity achieves faster adoption)

**Source:** systems-expert self-dissent (integrator obligation per shared-protocols §5.3).

**Claim:** Option A (pure non-profit consortium) achieves faster Mittelstand adoption than Option C because it eliminates the structural conflict-of-interest between the Foundation and Jetix-Corp that Mittelstand procurement departments will detect and penalize. Option C's dual-entity structure, visible in founding documents, signals that the «open» Foundation is effectively controlled by a for-profit entity — sophisticated Mittelstand procurement teams will identify this and treat the Alliance certification as a Jetix-branded service, not a genuinely vendor-neutral standard. Option A, by contrast, places Jetix in the same structural position as any other founding member — Jetix-Corp earns consulting revenue through demonstrated excellence, not through structural governance advantage.
- F: F4 (operational convention; supported by EU public sector procurement pattern preference for genuinely vendor-neutral standards bodies over hybrid structures)
- ClaimScope: holds for procurement-driven Mittelstand segments (manufacturing, logistics, finance — sectors with formal procurement processes); less applicable in founder-led SMBs where informal trust networks dominate
- R: refuted if Option C Foundation achieves ≥20 member organizations within 24 months of formation and Jetix-Corp certifications account for ≥30% of total certifications issued — this would prove the structural conflict-of-interest is not materially harming adoption; accepted if procurement-driven Mittelstand buyers explicitly cite «Jetix-controlled foundation» as a concern in sales conversations

### Dissent-2: Argument for Option B (Patent moat is the only defensible position)

**Source:** systems-expert self-dissent drawing from STRATEGIC-INSIGHT §8 recommendation #4.

**Claim:** Option C's open-surface Foundation is a long-run competitive liability because the methodology, once published under permissive license, is irrevocably in the public domain for commercial exploitation. A better-resourced competitor (McKinsey, Deloitte, BCG — all of whom have Mittelstand practices) can read the Foundation's methodology documentation, implement it with their existing client relationships and brand credibility, and displace Jetix-Corp in every market where Jetix-Corp lacks established relationships. Option B's patent moat, despite its short-term Mittelstand-adoption friction, creates the only structural barrier that cannot be replicated by a resource-advantaged competitor. The ARM Holdings model demonstrates that a proprietary AI-adjacent methodology can achieve market-dominant licensing revenue once the critical mass of IP protection is in place — STRATEGIC-INSIGHT §8 explicitly names patents as one of Jetix's 7 competitive recommendations.
- F: F3 (multi-case pattern: ARM Holdings, Qualcomm, Dolby — proprietary standards with patent moat achieve sustained licensing revenue; but all operated in hardware markets with higher patentability rates than AI-method software)
- ClaimScope: holds IF Jetix's methodology contains patentable technical innovations (local-first KB synchronization protocol, fork-and-merge agent coordination mechanism — both potentially patentable as technical implementations); does NOT hold if the methodology is primarily a process-level framework (non-patentable in EU)
- R: refuted if EU patent filings for AI method combinations are rejected by EPO within 18 months of filing — in that case, Option B's IP moat collapses and Option C becomes the default; accepted if ≥2 patent applications receive positive EPO examination reports within 24 months of filing AND at least 1 Mittelstand firm signs an OEM license agreement demonstrating willingness to pay proprietary licensing fees

---

*End of §5 Alliance Architecture. Brigadier recommendation: Option C. Ruslan selects in AWAITING-APPROVAL ack.*
