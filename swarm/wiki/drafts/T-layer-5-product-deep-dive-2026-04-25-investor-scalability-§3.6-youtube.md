---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: §3.6
direction: YouTube-analyzer SaaS
type: layer-deep-dive-section
mode: scalability
author: investor-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - {path: "reports/review_2026-04-24.md", range: "rows 684-689 (YouTube-analyzer rows 198-199), row 801 (audio_527 reverse-engineering)"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md", range: "YouTube-analyzer row + §6 gate evolution + §7 audio_514 + audio_527 verbatim"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D20 USB-C reinforcement, D27 Fork-and-Merge"}
  - {path: "decisions/JETIX-VISION.md", range: "§7 archetypes (Блогер + Teacher) + §5 D24 open-source research"}
  - {path: "decisions/JETIX-PLAN.md", range: "§5 Phase 2 + §6 Phase 3 gates + revenue-gated unlock table"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§2.1 ICP Trinity + §3 Archetypes + §2 Блогер archetype"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§8 7 recommendations (moat = Mittelstand + compliance; scale windows)"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md", range: "§3 direction table + §6 anti-scope"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/decomposition.md", range: "C-08 cell acceptance predicate"}
word_count_estimate: 2000
confidence: medium
confidence_method: analogy + judgment (SaaS unit-econ ranges from comparable tools; gate timing from JETIX-PLAN gates; methodology from audio verbatim)
escalations: []
dissents:
  - claim: "YouTube-analyzer should activate in Phase 2 (G2, €200K) not Phase 3 (G3→G4, $100M) given audio_514 urgency framing"
    F: F4
    ClaimScope: applies only if Phase-1 consulting clients include YouTube operators who create pull demand for the tool before G3
    R:
      refuted_if: "no Phase-1/2 consulting client ever requests YouTube-channel intelligence as a deliverable"
      accepted_if: "≥1 Phase-1 consulting client explicitly requests YouTube analysis AND is willing to pay ≥$2K for a manual report; receipt: first signed engagement for YouTube-analysis consulting"
  - claim: "Build-vs-license: white-label existing tool + Jetix methodology layer is capital-superior to greenfield SaaS build for Phase-2 manual-delivery stage"
    F: F4
    ClaimScope: applies at G2 (€200K) only; may not hold at G3+ where moat differentiation matters
    R:
      refuted_if: "no credible white-label YouTube-analytics platform with API access + acceptable ToS exists at acceptable cost at Phase-2 activation"
      accepted_if: "a white-label option is identified with LTV/CAC >3x and ToS compliance at the Phase-2 manual-service stage"
---

# §3.6 YouTube-analyzer SaaS

> Cell C-08 | investor-expert × scalability | Wave B
> Cycle: cyc-layer-5-product-deep-dive-2026-04-25
> Source: audio_514 "золотая жила" + audio_527 reverse-engineering methodology + review_2026-04-24 rows 684-689

---

## 1. Mission

YouTube-analyzer SaaS is a tool that analyzes YouTube channels at scale across any niche: advertising sponsor data, inferred team structures, cooperation graph, content-gap detection, and ICP-match scoring. The core asymmetric advantage is **bulk analysis** — not per-channel manual lookup, but sweeping an entire niche (all 200 channels in "German B2B SaaS founders" or "English-speaking productivity educators") simultaneously to surface patterns invisible to competitors doing one-channel research. Per Ruslan's verbatim from audio_514: *«YouTube может стать золотой жилой для Jetix через автоматический анализ всех каналов по любой теме, сбор данных о рекламе, командах, возможностях кооперации в реальном времени»* [src:reports/review_2026-04-24.md#row 684]. The rigor underpinning the analyzer is the reverse-engineering methodology: *«Jetix будет заниматься реверс-инжинирингом на максималках для своего развития и развития общества — извлекать знания из AI, кодов, бизнесов конкурентов»* [src:reports/review_2026-04-24.md#row 801, audio_527]. YouTube is the first named niche for this methodology; the underlying framework is applicable to TikTok, podcasts, Instagram, and LinkedIn at Phase 3+.

The "золотая жила" framing is not a marketing phrase — it is a capital-allocation signal. Ruslan identified this direction specifically because the data-advantage is asymmetric: anyone with a YouTube account can view individual channels; nobody at SaaS scale is currently aggregating niche-wide intelligence and selling it as a self-serve product targeted at the content creator and agency segment. That gap is the margin-of-safety in the moat claim.

---

## 2. Phase Activation

**Current state (Phase 1, G0→G1, €0→€50K Q2 2026):** concept only. No code written, no product, no revenue. The direction is latent. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md#§5]. Phase 1 must not be diluted by YouTube-analyzer build activity; the sole Phase-1 mandate is €50K consulting + Продюсерский центр pilot. Audio_514 urgency framing ("золотая жила") creates pressure to act earlier — this tension is a preserved dissent (see frontmatter and §10).

**Phase 2 (G1→G2, €50K→€200K; "done-for-you analyst service"):** the first monetization step is NOT building SaaS. It is delivering YouTube-channel analysis as a consulting engagement or analyst-report product. If a Phase-1 consulting client is a content creator, agency, or marketing director who asks "who else is in my niche? who are the sponsors? who should I partner with?" — the investor-expert's trigger fires: deliver a manual niche-intelligence report ($2K-$10K one-shot depending on scope) using the voice pipeline, `/ingest`, `/ask`, and agent tools. This establishes willingness-to-pay before committing engineering capital. Activation trigger: **first paying client who requests YouTube-channel intelligence as a deliverable**. [src:decisions/JETIX-PLAN.md#§4 Phase 1→2 transition tools trigger]

**Phase 3 MVP SaaS (G2→G3, €200K→€1M):** self-serve SaaS beta. YouTube Data API integration, analytics engine, three-tier offering, payment layer. First 50-500 paying users. Unit-economics measurement begins: churn rate, CAC, LTV, COGS per query/channel.

**Phase 3+ scale (G3→G4, €1M→$100M):** SaaS scale to 500-5000 paying users; first enterprise-tier contracts with Fortune-500-adjacent clients; international expansion (DE/EN primary, then ES/FR/PT/BR); integration with §3.4 Matchmaker (the collab graph produced by YouTube-analyzer feeds the Matchmaker specialist-pool directly).

**Phase 4+ ($100M→$1T):** the YouTube-analyzer becomes the seed of a Reverse-Engineering-as-a-Service platform. YouTube, TikTok, Instagram, podcast, LinkedIn covered. If Alliance Option C (Foundation non-profit upstream + Jetix-Corp downstream) is acked per L6 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§5 Option C], the reverse-engineering methodology is published as Apache 2.0 via the Foundation; the proprietary data-pipeline and insight-generation layer remains Jetix-Corp property. This is the D13 "Closed core / Open surface" pattern applied to data-intelligence products. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§4 D13 column]

**Sunset trigger:** none. The direction scales to international Phase 3+. What retires per gate is described in §6 Evolution and §9 Antifragility check.

---

## 3. Target ICP Mapping (L6 Trinity)

The ICP mapping for YouTube-analyzer must consume the L6 ack'd Trinity framework [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§2.1] and the archetype-level detail from §3 Archetypes.

**Primary ICP — Блогер archetype (L6 primary archetype 4):**

Ruslan's verbatim from audio_514 is explicit: *«YouTube-создатели — идеальная целевая аудитория: дисциплинированные, ответственные, хотят развиваться»* [src:reports/review_2026-04-24.md#row 685]. The behavioral match is high: a creator who wants to understand their niche, find collaboration partners, audit who their competitors work with commercially, and identify what content is missing. They act fast, self-serve well, and have a direct financial stake in the intelligence. The payment-ability filter from L6 §2.1 applies: specialist-bloggers with 5K+ audience who can allocate $49-$149/mo to a SaaS tool or $2K-$10K for a one-off report satisfy the OR-gate ($5K/mo retainer OR $10K one-shot). Smaller creators below that threshold are community-tier, not Phase-1 paying ICP.

**Secondary ICP — infobiz operators and content agencies:**

Content agencies producing for bloggers and educators (Phase 2+ SaaS); marketing teams at Mittelstand companies using YouTube for thought-leadership (Phase 3+ enterprise tier); English-speaking infobiz operators who produce courses, memberships, or coaching at scale and need YouTube-niche intelligence as a competitive-research input. This segment intersects with the Продюсерский центр ICP (§3.2) — operators who use Jetix's producer services AND need niche analysis are double-ICP clients with higher LTV. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§2.1 Specialist-blogger + Startupper digital row]

**Tertiary ICP — Phase 3+ enterprise competitive-intelligence teams:**

Big-company strategy departments that currently pay $50K+/year for Forrester/Nielsen brand-intelligence subscriptions. YouTube-at-niche-scale is a data source they do not have systematic access to. This tier requires custom API access, dedicated support, private instances, and GDPR-compliant data pipelines. Payment-ability trivially passes. Activation gate: Phase 3+ ($100M trajectory). [src:decisions/JETIX-PLAN.md#§6 Phase 3 Fortune 500 conversations]

**ICP exclusions (anti-ICP):** casual individual creators with <5K audience (cannot pay); crypto-YouTube channels (not Jetix's moat niche); AI-hype-passive users expecting free competitive intelligence. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#Anti-ICP]

---

## 4. Value Proposition

**The problem, in client language:**

"I'm a content creator, agency strategist, or marketing director. I need to know — fast — who is in my niche on YouTube, what sponsors they have, roughly how large their teams are, who they collaborate with, and what content gaps exist. Right now this takes 40+ hours of manual research per niche and I still miss 80% of signals because I cannot process 200 channels in parallel. By the time I finish my manual research, the landscape has already shifted."

**The outcome promised:**

Niche-level channel intelligence in minutes rather than weeks: ad sponsors detected via metadata analysis, team-size estimated from channel-metadata signals, collaboration graph surfaced (who has appeared on whose channel), content-gap opportunities flagged (topics heavily viewed in adjacent niches, underrepresented in the target niche), ICP-match scoring against a user-supplied ICP definition. The output is an actionable intelligence report — not raw data, but interpreted insights in the Jetix reverse-engineering rigor tradition.

**How Jetix differs from all alternatives:**

The differentiator is not a feature — it is a combination of three structural advantages unavailable to any competitor today:

First, **bulk-analysis at niche scale**. Competitors like TubeBuddy and vidIQ are per-channel optimization tools. The user opens one channel and audits it. YouTube-analyzer opens all 200 channels in a niche simultaneously and reports patterns, rankings, and anomalies. This is not an incremental feature improvement; it is a different unit of analysis. [src:reports/review_2026-04-24.md#row 684, audio_514]

Second, **AI-produced insights, not scraped metadata**. SocialBlade scrapes and displays public counts. YouTube-analyzer ingests metadata signals, runs Jetix-methodology pattern-recognition (knowledge-synth + crazy-agent as insight-generation microservices at Phase 3+), and returns language-model synthesized intelligence: "Channel X is likely sponsored by B2B SaaS tools in the €10K/month range; their most common collaboration partner type is productivity educators with 50K+ subscribers; the niche has a gap in long-form technical content above 20 minutes." That is not a scraped number — it is a judgment.

Third, **integration with the Jetix ecosystem**. Clients using YouTube-analyzer are at the same time candidates for Продюсерский центр (they need production after they understand the niche), Matchmaker (they need collaboration partners after they identify them), and Educational products (they want to understand the methodology behind the analysis). The cross-direction flywheel means a YouTube-analyzer SaaS user has higher LTV than a standalone tool subscription would suggest. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md#§6 G3→G4 row]

**USB-C framing for this direction:**

YouTube-analyzer is the first concrete product expression of the reverse-engineering-as-a-service concept. The same pattern — bulk ingestion of public signals, AI-pattern synthesis, structured intelligence output — is applicable to any competitive-intelligence domain. YouTube is the USB-C reference implementation. When the methodology is proven on YouTube (Phase 3), it becomes the standard for any niche-intelligence product Jetix builds next. This mirrors the D20 USB-C positioning at the product layer: Jetix builds the standard connector pattern, not a one-off tool. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D20 USB-C reinforcement]

---

## 5. Offer Structure (Placeholder — L7 Owns Final Pricing)

The offer structure has four tiers corresponding to the four activation phases. All pricing is a placeholder range; final pricing arithmetic belongs to L7 Business Deep-Dive.

**Tier 0 — Done-for-you analyst service (Phase 1/2, pre-SaaS):**

Jetix delivers manual YouTube-niche analysis as a consulting engagement. Analyst (knowledge-synth + crazy-agent + sales-researcher agents + Ruslan editorial judgment) produces a structured niche-intelligence report: channels found, sponsor patterns, collaboration graph, content gaps, ICP-match ranked list. Placeholder: €2K-€10K per one-shot report, depending on niche depth (number of channels, intelligence layers requested). This is Phase-1 pull-forward monetization — no engineering build required, uses existing agent tools. The report IS the product; SaaS automates it later.

**Tier 1 — Self-serve SaaS, solo creators and small agencies (Phase 3 MVP):**

Placeholder: €49-€149/month. Usage-based tiers within subscription (queries per month, channels per analysis). Target: solo specialist-bloggers with 5K-100K audience, small content agencies (1-5 people). Self-serve onboarding, pre-built templates for standard niches, no custom support. Unit-econ target: LTV >3× CAC at this tier is the pass criterion before Phase 3+ investment. Placeholder: CAC €50-€200 (content-led acquisition via Продюсерский центр channel + Secure Network referrals); LTV €600-€1800 at 12-month retention.

**Tier 2 — Team SaaS, multi-seat agencies and marketing teams (Phase 3 scale):**

Placeholder: €299-€999/month. Multi-seat accounts, advanced filtering (custom ICP scoring criteria, industry-specific sponsor taxonomy), export to CSV/JSON/API, white-label report templates. Target: content agencies 5-20 people; marketing departments at scale-up companies. Requires CS support for onboarding; higher margin than Tier 1 despite higher support cost.

**Tier 3 — Enterprise, competitive-intelligence retainer (Phase 3+ scale → G4):**

Placeholder: €5K-€20K/month retainer + custom implementation fee. Private instance, GDPR-compliant EU data pipeline, dedicated account management, custom niche taxonomies, integration with client CRM/Slack/Notion, quarterly intelligence briefings. Target: Fortune-500-adjacent strategy teams, large publisher groups, enterprise marketing departments. Sales motion: direct Ruslan relationship + referral through Alliance network; not self-serve.

**Note — L7 owns final pricing.** These are architectural ranges to size the opportunity and determine which tiers justify Phase-3 build investment. Final pricing, CAC/LTV/churn arithmetic, and tier-boundary decisions are L7 Business Deep-Dive work. [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md#§6 anti-scope]

---

## 6. Delivery Mechanism

**Phase 1 (concept, G0→G1):**

No delivery mechanism built. Direction is latent. If a consulting client organically requests niche-intelligence work, the existing agent suite (knowledge-synth for synthesis, crazy-agent for lateral pattern detection, sales-researcher for lookup, inbox-processor for data triage) delivers a manual report. The `/ingest` pipeline processes channel-metadata sources; `/ask` queries for patterns. Voice pipeline extracts audio-content signals from video transcripts if needed. Engineering effort: zero new build. This is the "Tier 0 report as consulting deliverable" from §5.

**Phase 2 (manual reporting productized, G1→G2):**

A standardized analyst-report template is designed and productized. Ruslan + 1 analyst-role contractor (hired per €200K gate per JETIX-PLAN §4) deliver 5-15 reports per quarter. YouTube Data API integration is built as a lightweight internal tool — not customer-facing, but enabling the analyst to pull channel metadata programmatically rather than manually. The methodology is documented in the Jetix methodology repo (§3.7 Educational products dependency). Engineering estimate: 2-4 weeks of engineering-expert time to build internal channel-data pipeline; no frontend, no billing, no auth. This is pre-product infrastructure.

**Phase 3 MVP SaaS (G2→G3):**

Dedicated engineering team (2-3 engineers per D26 Phase-3 team target [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]) builds: YouTube Data API integration, analytics engine, dashboard UI, authentication, billing (Stripe). Jetix agents (knowledge-synth, crazy-agent) power the insight-generation layer as internal microservices. Tech stack at Phase 3 (engineering-expert territory, named for reference only): Python data pipeline, PostgreSQL + TimescaleDB for time-series channel data, React frontend, Stripe billing, Claude API for insight synthesis. The investor-scalability lens names the tech stack for capital-sizing purposes only; implementation is engineering-expert's domain.

**Phase 3+ infrastructure (G3→G4):**

EU data-center deployment (per D17 filesystem-SoT, client data sovereignty [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§3]); GDPR-compliant data-handling pipeline for channel-operator metadata; YouTube ToS compliance monitoring; rate-limit management architecture. At scale, the competitive advantage of bulk analysis requires negotiating API quota increases or establishing a direct Google partnership — that is a Phase-3 gate decision (see §10 Open Questions Q4).

**Automation level by phase:** Phase 1 = manual (zero automation). Phase 2 = semi-automated (internal tools only, analyst-delivered). Phase 3 = high (SaaS self-serve). Phase 3+ = very high (enterprise API + automated intelligence briefings).

---

## 7. Competitive Positioning

The five named alternatives and their limitations form the positioning thesis. The investor-scalability lens supplements the standard competitive-analysis with the moat-durability check (kill-conditions per §10 Open Questions).

**TubeBuddy ($8-$30/month):**

Creator-focused; per-channel keyword and tag optimization; basic analytics; grade scores for video SEO. Target user: individual creator optimizing one channel. What it does NOT do: bulk niche analysis, sponsor detection, collaboration graph, multi-channel pattern synthesis. Kill condition for Jetix's differentiation: TubeBuddy adds bulk-niche analysis at comparable pricing. Assessment: unlikely in Phase 3 time frame — TubeBuddy's product identity and customer base are per-channel optimization; bulk-niche intelligence would cannibalize their core positioning. Moat durability: medium.

**vidIQ ($7-$40/month):**

Similar to TubeBuddy with a slightly stronger machine-learning angle; daily idea generation, trending topic tracking, competitor channel tracking (manual, per-channel). Does not do bulk niche synthesis. Consumer-grade product oriented toward solo creators. Same kill condition as TubeBuddy. Moat durability: medium.

**SocialBlade (free + $4-$25/month):**

Public stats and channel ranking. Scrapes subscriber counts, view counts, estimated earnings from public metadata. No intelligence layer — raw numbers only. Competitive gap is largest here: SocialBlade gives you data; YouTube-analyzer gives you judgments. Kill condition: SocialBlade adds AI-insight layer. Assessment: SocialBlade competes on data breadth; adding deep intelligence would require significant LLM integration investment that is outside their current product direction. Moat durability: medium-high.

**Social Bakers / Sprout Social (enterprise, $200-$2K/month):**

Multi-platform social analytics; YouTube is one channel among Facebook, Instagram, TikTok, LinkedIn in their suite. General-purpose; no methodology layer; no bulk-niche analysis specific to YouTube. Serves enterprise social teams, not content creators or agencies. Pricing tier and sales motion are different from Jetix's SaaS target. Kill condition: Social Bakers adds YouTube-specific niche-intelligence module targeting the creator/agency segment. Assessment: possible but requires product strategy shift away from their multi-platform generalist positioning. Moat durability: medium.

**Custom YouTube Data API scripts (free-to-build, requires engineering):**

Any engineering-capable team can query the YouTube Data API and build their own analysis. This is the most dangerous "competitor" for the moat — because Jetix's raw data inputs are from the same public API. What Jetix has that a DIY script does not: the interpretation methodology (reverse-engineering rigor from audio_527), the Jetix agent ecosystem for synthesis, the UX layer for non-engineering users, and the continuously improving insight taxonomy built from all users' niche queries. The moat is methodology + synthesis quality + product velocity, not data exclusivity. Kill condition: a methodology-first competitor (e.g., a consulting firm-turned-SaaS) replicates the reverse-engineering methodology. This is the most credible long-term threat. Moat durability: medium (methodology is partially codifiable; moat = combination of methodology + integration + specific knowledge, not single-factor).

**Manual human analysts ($50-$200/hour):**

High quality, high cost, slow (40+ hours per niche). YouTube-analyzer's value proposition over human analysts is speed and cost at sufficient quality. The Tier-0 done-for-you service (Jetix as the "analyst") is positioned above manual analysts on quality (AI-enhanced pattern recognition) and comparable on price for a one-shot engagement. Kill condition: improved AI tooling makes manual analysts dramatically cheaper (e.g., a future Claude context window makes full-niche analysis trivially fast for any researcher). This is the long-run risk; short-run Jetix is ahead. Moat durability: low-medium (dependent on Jetix maintaining analytical lead over commoditizing AI tools).

**Why Jetix wins in Phase 3 time frame:**

- Scale via bulk analysis (structural advantage, not a feature)
- AI-produced insights synthesized through Jetix methodology (quality differentiation)
- Integration with Продюсерский центр + Matchmaker ecosystem (ecosystem LTV multiplier)
- DACH-specific niche option: German-language bloggers are systematically underserved by all competitors above (all are English-primary or language-agnostic). [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§2 Moat = Mittelstand knowledge]
- Reverse-engineering methodology rigor (D20 USB-C standard applied to data-intelligence products)

**Primary risk:** YouTube API rate limits and ToS enforcement. YouTube actively monitors and throttles bulk data collection. Any SaaS built on bulk YouTube API calls is subject to quota restrictions, ToS changes, and potential API deprecation. This is a capital-deployment risk that must be named explicitly: the Phase-3 SaaS build decision must be preceded by a ToS/API compliance audit and, at scale, by a Google partnership discussion. [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/decomposition.md#C-08 risks]

---

## 8. Evolution Per Gate

The five-gate evolution follows the concept → manual-delivery → MVP SaaS → SaaS scale → international platform arc. Each gate names what activates, what retires (antifragility via-negativa), and what the investor-scalability trigger is.

**Gate 1: Phase 1 (G0→G1, €0→€50K, "concept + latent")**

Status: concept documented in voice-memo (audio_514, audio_527); no action taken. The direction sits on the bench while Phase-1 consulting + Продюсерский центр execute. If a Phase-1 consulting client who is a YouTube operator organically creates demand for niche analysis, Tier-0 manual delivery is permitted using existing agent tools — but this is opportunistic, not structured investment.

What retires at this gate: none (nothing to retire; direction is latent). What activates: awareness of the opportunity, documentation of the methodology, the template for a one-shot report.

Investor-scalability trigger to proceed to Gate 2: first paying client who requests YouTube-channel analysis as a named deliverable AND is willing to pay ≥$2K for the engagement. Without this empirical signal, Gate 2 capital allocation is not warranted.

**Gate 2: Phase 2 (G1→G2, €50K→€200K, "manual reporting service productized")**

Status: analyst-report template standardized; Ruslan + analyst-role contractor deliver 5-15 reports per quarter; YouTube Data API lightweight internal tool built (engineering-expert work, 2-4 weeks). Revenue: $2K-$10K per report × 5-15 reports/quarter = $10K-$150K/year potential at mid-range. This is NOT the SaaS build. This is manual labor productized enough to deliver reliably and charge for.

What retires at this gate: any attempt to build a self-serve UI or billing layer before unit-economics are proven. Investor principle applied: Graham margin-of-safety. Capital deployed in engineering before LTV/CAC is known is capital deployed without margin-of-safety arithmetic.

Investor-scalability trigger to proceed to Gate 3: ≥10 paid reports delivered at ≥$3K average; repeat customers identified (LTV signal); client qualitative feedback confirms AI-synthesized intelligence is decision-grade (not just interesting). AND revenue from consulting + Продюсерский центр has cleared the €200K gate.

**Gate 3: Phase 3 MVP SaaS (G2→G3, €200K→€1M, "self-serve beta")**

Status: SaaS MVP launched. Three tiers live. 50-500 paying users. Churn and unit-economics measured for the first time. The Phase-3 build requires dedicated engineering (2-3 engineers, 4-6 months of development, estimated €100K-€200K in engineering cost). This is the first capital-heavy investment in this direction. It requires: (a) Gate-2 unit-econ evidence, (b) €200K consulting revenue unlocking the engineering budget, (c) HITL ack from Ruslan before committing engineering capital.

What retires at this gate: the per-report analyst-delivery model for the self-serve ICP. Enterprise reports continue as Tier 3; the analyst-delivered product becomes the enterprise tier only. Solo creators and small agencies migrate to Tier 1/2 self-serve.

Investor-scalability trigger to proceed to Gate 4: SaaS MRR ≥€30K sustained 3 months; churn <5%/month at Tier 1; LTV:CAC ratio ≥3:1 empirically measured. Below these thresholds, scaling spend is not warranted — the SaaS economics are not yet proven.

**Gate 4: SaaS Scale (G3→G4, €1M→$100M, "scale + international")**

Status: 500-5000 paying users; first 3-10 enterprise contracts; international expansion (DE/EN primary, then ES/FR/PT/BR). Integration with §3.4 Matchmaker (collaboration graph from YouTube-analyzer feeds Matchmaker specialist-pool). DACH-German-niche product line launched alongside English-primary offering.

What retires at this gate: any allocation that has not produced owner-earnings within 4 quarters (Buffett owner-earnings criterion, Constellation 30% hurdle rate reference). Low-margin self-serve tiers that are below hurdle may be restructured or eliminated in favor of mid-tier and enterprise. Via-negativa: remove weak tiers before adding features to them.

Investor-scalability trigger to proceed to Gate 5: $100M ARR milestone; multi-BU P&L structure required per D26 (team 50-100); international revenue ≥30% of total.

**Gate 5: Reverse-engineering platform ($100M→$1T, "civilizational scale")**

Status: YouTube-analyzer is the seed; the platform covers YouTube + TikTok + Instagram + podcast + LinkedIn + any other niche-intelligence domain. Alliance Foundation (Option C per L6 ack) publishes the reverse-engineering methodology as Apache 2.0; Jetix-Corp operates the proprietary data-pipeline and insight-generation layer. 10K+ users across all platforms. Multi-roy federation operates — each roy in a different geographic/language market has its own analyzer instance.

What retires at this gate: any platform coverage that fails to reach 30% Constellation hurdle rate in its market segment within 4 quarters of launch.

---

## 9. Cross-Direction Dependencies

**Depends on (inputs YouTube-analyzer needs from other directions):**

- **§3.1 AI Consulting (early revenue):** Phase-1 consulting revenue funds Phase-2 analyst-service build and Phase-3 SaaS engineering capital. Without the €200K consulting gate clearing, no SaaS build capital exists. Hard dependency.
- **§3.2 Продюсерский центр (early adopter ICP):** The Продюсерский центр serves Блогеры and infobiz operators — exactly YouTube-analyzer's primary ICP. Producer center clients are the most natural early adopters for the analyzer: they need to understand the niche before they can produce into it. Cross-sell motion: consulting → producer center → YouTube-analyzer in sequence. This is a high-probability ICP overlap.
- **§3.7 Educational products (methodology shareable):** The reverse-engineering methodology behind the analyzer is documented in the Educational products direction (D27 fork-and-merge, §3.7). When the methodology is published, it is the credibility signal that makes YouTube-analyzer's insights trustworthy. Without the methodology being articulable (published or documented), clients have no reason to trust that AI-synthesized intelligence is more rigorous than a human Google search.

**Depended on by (outputs YouTube-analyzer feeds to other directions):**

- **§3.2 Продюсерский центр (channel strategy data):** YouTube-analyzer produces the competitive-intelligence that informs a blogger's content strategy. The producer center uses this data as input to the research → script pipeline. At Phase 3+, the integration becomes native: a Продюсерский центр client's YouTube-analyzer subscription automatically feeds the production pipeline.
- **§3.4 Matchmaker (collaboration graph):** The cooperation-opportunity data from YouTube-analyzer (who has collaborated with whom, which channels are looking for collaboration partners based on metadata signals) directly enriches the Matchmaker specialist-pool. A blogger who is identified as an ideal collaboration partner by YouTube-analyzer is a candidate for Matchmaker introduction. At Phase 3+, this integration may be the Matchmaker platform's primary data source for the content creator segment.
- **§3.5 Secure Network (member perk):** At Phase 3, Secure Network members in the content-creator segment receive YouTube-analyzer access as part of their membership perk (складчина model). This reduces standalone CAC (community-based acquisition) and increases Secure Network retention (tangible tool value beyond networking).
- **§3.9 Smart AI (flagship label):** YouTube-analyzer is a concrete demonstration of Smart AI capabilities: it learns patterns, retains niche context, synthesizes intelligence from structured data. Per audio_529's "Smart AI saves context and helps people manage projects more effectively", the analyzer is a Phase-3 product showcase for what Smart AI means in practice. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md#§7 audio_529]

**Cross-cutting dependencies:**

- **§3.7 Educational (methodology shared via educational program):** The reverse-engineering methodology (audio_527 "на максималках") documented in §3.7 is co-owned conceptually with YouTube-analyzer. The methodology publication (D27 fork-and-merge, Apache 2.0 via Foundation if Option C acked) is the credibility moat for the analyzer product. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]
- **D28 Query-driven KB:** The analyzer's insight-generation relies on query-driven knowledge-base patterns — ingesting channel data only against declared relevance anchors (niche, ICP criteria, sponsor taxonomy) rather than ingesting all available YouTube metadata indiscriminately. This is D28 operationalized at the product level. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28]

---

## 10. Open Questions (Investor-Scalability Lens)

Five open questions requiring Ruslan decision or empirical signal before capital allocation decisions escalate. These questions are the gate conditions that determine whether each subsequent Phase investment is warranted.

**Q1 — Phase-activation: should YouTube-analyzer pull forward to Phase 2 (G2, €200K) as a structured initiative rather than an opportunistic consulting add-on?**

Audio_514 urgency framing ("золотая жила") suggests early action. Gate-sequencing discipline says Phase 1 must not be diluted. Preserved dissent (see frontmatter): the activation trigger should be empirical — if Phase-1 consulting clients include YouTube operators who create organic pull demand, the direction accelerates naturally. If Phase-1 clients are all Mittelstand and do not request YouTube analysis, the direction stays latent until Phase 3. This is an empirical question that resolves itself as Phase-1 clients are acquired; no pre-commitment of capital required. Investor principle: second-level thinking (Marks) — what is already priced in here is "YouTube is important"; the question is whether the Блогер ICP pull demand materializes in Phase 1 or only in Phase 2+.

**Q2 — Build vs license: is white-labeling an existing platform + Jetix methodology layer capital-superior to greenfield SaaS build?**

Preserved dissent (see frontmatter, dissent 2). A white-label TubeBuddy or vidIQ API + Jetix's insight-generation layer (knowledge-synth agent) may produce a Phase-2 MVP faster and cheaper than a greenfield build. The cost is: (a) ToS compliance of the underlying platform, (b) moat erosion (white-labeled platform = competitor can access same data), (c) integration dependency risk. The capital-superior option may change between Phase 2 (manual delivery; white-label is fine) and Phase 3 (SaaS scale; greenfield is required for moat). Decision needed before Phase 3 engineering capital is committed. This is in the `requires-approval` decision-rights category; brigadier escalation at Phase 3 gate.

**Q3 — Unit economics placeholder: what is realistic CAC for the YouTube-creator ICP?**

SaaS CAC for the $49-$149/month self-serve tier typically runs $50-$300 depending on acquisition channel (content-led < $100; paid ads $200-$500; community referral $30-$80). LTV at 12-month retention × $99/month average = $1,188. LTV:CAC ratio target: ≥3×, meaning CAC must be ≤$396. Content-led and community-referral acquisition channels make this feasible; paid-ads channels do not. Implication: Phase-3 CAC strategy must be content-led + community-referral first. Paid-ads for this tier are a risk-of-ruin scenario (CAC exceeds LTV, leads to negative-unit-economics scaling). Final arithmetic: L7 owns; these are holding ranges for Phase-3 build-decision gate.

**Q4 — YouTube ToS and API quotas at scale: when does Jetix need a direct Google partnership?**

The YouTube Data API quota for free accounts is 10,000 units/day. At SaaS scale with multiple concurrent users running bulk-niche queries (100+ channels per query), this quota exhausts immediately. Paid API quota expansion is available but expensive and subject to ToS review. The long-term SaaS build requires either: (a) YouTube partnership (direct quota negotiation), (b) legitimate non-API data collection methods (e.g., publicly viewable metadata via structured scraping within ToS limits), or (c) a channel-metadata sharing agreement with content creators who authorize Jetix to act as their analytics agent. This is a legal and partnership surface that must be scoped before Phase-3 engineering capital is committed. HITL decision: Ruslan must review ToS compliance path before SaaS build authorization.

**Q5 — DACH-niche launch vs English-primary launch: which market first at Phase-3 SaaS?**

D10 (English-primary) applies [src:decisions/JETIX-PLAN.md#§3.7], which suggests English-language market as the Phase-3 launch target. The counter-argument: German-speaking YouTube bloggers are systematically underserved by all existing competitors (TubeBuddy, vidIQ are English-centric); a DACH-specific product launch may face less competition, lower CAC, and faster community word-of-mouth through Secure Network and Alliance members. Tension with D10 is preserved here; does not override D10, but names the commercial case for a DACH-first variant. This is a marketing and distribution question for L7 to resolve with Ruslan ack. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§8 recommendation 2, Moat = Mittelstand knowledge]

---

## Scalability Mode — BOSC-A-T-X Trigger Summary and Antifragility Check

Per §6 mandate of the investor-expert scalability mode, the YouTube-analyzer direction must satisfy the antifragility predicate at each gate: does the capital allocator gain optionality from disorder rather than lose it?

**€50K → €200K:** The direction is latent (no capital deployed). Zero fragility. Optionality preserved: if a consulting client creates organic demand, the analyst-report Tier 0 can activate with zero pre-investment, turning volatility (unexpected client request) into revenue. Barbell structure: 100% held in T-bills equivalent (no investment) + optionality (activate on demand). Antifragility check: pass.

**€200K → €1M:** First capital deployment (analyst template + internal API tool, €5K-€20K estimated). Capital is small and retrievable (the template has standalone value; the internal tool is reusable across other research). Fragility introduction: the analyst-contractor cost (fixed monthly obligation). Mitigant: analyst-contractor is shared across consulting, Продюсерский центр, and YouTube-analyzer — not YouTube-analyzer-dedicated. Antifragility check: pass (low concentration of fragile spend).

**€1M → $100M (Phase 3 SaaS build):** This is the capital-heavy gate (€100K-€200K engineering build). Fragility introduction: engineering capital is largely sunk once committed; the team build-up creates fixed costs; the YouTube API dependency is a regulatory risk. Mitigant: gate condition (10 paid reports + LTV:CAC ≥3:1 empirically proven) before committing. The margin-of-safety check at this gate is explicit: if Phase-2 manual-service unit-economics are below 3:1 LTV:CAC, the SaaS build decision is deferred, regardless of urgency framing. Graham margin-of-safety principle. Antifragility check: conditional pass (requires Gate-2 evidence; not pre-committed).

**$100M → $1T:** The platform architecture, multi-niche coverage, and Foundation publication of methodology (D27 + Alliance Option C) produces antifragility: if one niche-intelligence product fails (e.g., YouTube changes its ToS severely), other niche-intelligence products (TikTok, podcasts, LinkedIn) continue operating under the same methodology layer. The platform's resilience improves when individual niche instances fail and are retired — the methodology is strengthened by seeing failure modes in practice. Antifragility check: pass (structural gain from disorder at platform scale).

**Via-negativa retirement ledger (what to RETIRE per gate):**

- **€50K → €200K:** Retire any temptation to build a MVP before Tier-0 demand is proven. Retire "experiment" build activity that consumes engineering bandwidth without a paying client validating the intelligence use-case.
- **€200K → €1M:** Retire any analyst-delivery capacity that is not recouping ≥$3K per report average. Retire per-channel (non-bulk) analysis as the primary offer — it is the low-differentiator variant. Retire the direction if ≥10 paid reports cannot be delivered within 6 months of Phase-2 activation.
- **€1M → $100M:** Retire the analyst-delivery model for solo-creator ICP (migrate them to self-serve SaaS or lose them). Retire any SaaS tier with LTV:CAC below 2:1 sustained 2 quarters.
- **$100M → $1T:** Retire any niche-intelligence product below Constellation 30% hurdle rate sustained 4 quarters. Retire any market where Jetix has less than #3 position by methodology quality (second-level thinking: being in a market ≠ winning it; being #5 in 5 markets = worse than being #1 in 2 markets).

---

## Provenance

| Source | Range | Key content used |
|---|---|---|
| `reports/review_2026-04-24.md` | rows 684-689 | audio_514 "золотая жила" verbatim; audio_514 "YouTube-создатели — идеальная целевая аудитория" verbatim; audio_527 reverse-engineering methodology |
| `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md` | §2 YouTube-analyzer row, §6 gate table, §7 audio_514/audio_527 verbatim | Gate timing (G3→G4); concept-only status confirmation; audio quotes grounded |
| `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md` | D20 USB-C reinforcement, D27 Fork-and-Merge | USB-C as standard pattern; fork-and-merge for methodology publication |
| `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md` | §2.1 ICP Trinity, §2.1 Блогер row, Anti-ICP | Payment-ability filter; Блогер archetype; anti-ICP exclusions |
| `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` | §8 recommendations 1-7, §4 D13/D20 lock table | Moat = Mittelstand + methodology; BIOS/standard positioning; speed window |
| `decisions/JETIX-PLAN.md` | §4 Phase 1→2 transition, §5 Phase 2, §6 Phase 3 | Revenue-gated unlock table; engineering capital availability at €200K gate; Phase-3 Fortune 500 gate |
| `decisions/JETIX-VISION.md` | §7 archetypes (Блогер + Teacher), §5 D24 open-source research | Блогер archetype behavioral description; D24 research-open connection |
| `swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/decomposition.md` | C-08 cell acceptance predicate | Cell contract verification |

---

*Drafted by investor-expert (× scalability), Cell C-08, Wave B, task T-layer-5-product-deep-dive-2026-04-25. Awaiting brigadier §5.5.5 provenance gate. HITL ack required before capital-deployment decisions at Gate 3 (SaaS build authorization).*
