---
title: Metrics frameworks research — literature distill + Jetix adaptation (Distribution Plan Step 4)
date: 2026-05-20
phase: 7
parent_prompt: prompts/step-4-distribution-plan-2026-05-20.md
F: F4 (literature corroboration solid)
G: step-4-dp-metrics-frameworks
R: refuted_if_metrics_chosen_disconnected_from_cascade_150_15_1M_KEYSTONE
constitutional_posture: R1 + R6 + R11 + R12 + EP-5 + append-only
prose_authored_by: brigadier-scribe (literature distill + Jetix-specific adaptation)
---

# Metrics frameworks research

> Literature distill (CRM funnel benchmarks 2026 / NPS Reichheld amplification / community-led growth measurement / DARPA cohort tracking) + Jetix-specific adaptations. ~1300w.

---

## §1 Literature foundations (2026 benchmarks)

### §1.1 B2B funnel conversion rates

- **Visitor-to-close:** 1.0-1.8% average across B2B SaaS; top-decile 6%+ [src: prospeo.io/s/b2b-conversion-funnel]
- **Visitor-to-lead:** 1.5-2.5% average; top 8-15%
- **MQL-to-SQL conversion:** 15-21% sales-pipeline definitions / 39-42% marketing-funnel; B2B SaaS healthy = 25-40%; top performers 39-40%
- **Win rates B2B:** 17-20%

### §1.2 Cold outreach reply rates

(Per `02-channel-tactics-research.md` §1.1 — literature also referenced here):
- Cold email avg 1-5%; elite >10%; average 3.43%
- Warm intro 34% vs cold 5% (4-7× multiplier)
- Sequences с 3-5 follow-ups: 8.3% reply rate vs 4.1% without
- Telegram >80% open rate (4× email)
- Podcast guest acceptance well-matched ~70%; blended 16-24%

### §1.3 Pipeline velocity (Salesforce / HubSpot definitional)

**Formula:** Pipeline Velocity = (Opportunities × Avg Deal Value × Win Rate) / Sales Cycle Length

- Median SaaS sales cycle: 84 days; optimal range 46-75 days
- Teams tracking velocity weekly: 34% revenue growth / 87% forecast accuracy [src: growthtoday.co/blog/b2b-sales-funnel-metrics]

### §1.4 Response speed

- Responding to inbound lead within 5 min = 21× more likely to qualify vs 30 min wait
- Only 7% of companies hit that window
- Implication: Jetix должен monitor inbound channel (Twitter DM / email reply / Telegram) с low-latency response

### §1.5 NPS (Reichheld)

- 0-10 scale «recommend?» — Promoters (9-10) / Passives (7-8) / Detractors (0-6)
- NPS = % Promoters − % Detractors
- Application к community-led growth: % L2/L3 contacts who publicly promote Jetix = «public NPS proxy»

### §1.6 Community-led growth measurement

- Amplification factor = # of L2/L3 contacts publicly mentioning / referring (organic)
- Cohort retention rate (% of Workshop founding cohort still engaged month-N)
- Net cohort growth rate (Wave 2 recruitment per Wave 1 member)

### §1.7 DARPA-style cohort metrics

- Program managers track: cohort size / cross-discipline diversity / publication output / external citation rate
- Jetix analog: cohort size (5-15 Wave 1) + cross-domain diversity (engineering / philosophy / business / governance) + substrate publication output (concept docs / wikis / methodology) + external mention rate (Karpathy lineage references / podcast mentions)

---

## §2 Core metrics framework для Jetix Distribution Plan

### §2.1 Layer 1 — Touch-level metrics (daily / weekly)

| Metric | Definition | Target benchmark (sourced) | Measurement |
|---|---|---|---|
| **Daily touches volume** | Total outreach touches per day | 10-20 (audio_686 + Pillar C) | CRM /crm-touch log count |
| **Per-tier distribution** | % L2 / % L1 / % Tier-1 | 60-80% / 15-25% / 5-15% | CRM tier aggregation |
| **Per-channel distribution** | % per channel | Channel-dependent | CRM channel field |
| **Touch quality flag** | % touches с paired-frame R12 PASS pre-send checklist | 100% | Pre-send checklist enforcement |

### §2.2 Layer 2 — Response metrics (weekly)

| Metric | Definition | Target benchmark (literature) | Measurement |
|---|---|---|---|
| **Cold response rate** | % cold outreach получивших ответ | 5-15% (elite >10%) | CRM status: cold → warm transition count / cold sent count |
| **Warm intro response rate** | % warm intro responses | 30-50% | CRM status transitions from intro-warm subset |
| **Channel-specific response rate** | Cold email vs Telegram vs Twitter DM | Email 1-5% / Telegram 5-15% / Twitter DM variable | Per-channel split CRM |
| **Time-to-first-response** | Hours from send to response | <72h optimal | timestamp delta CRM logs |
| **Response speed Jetix-side** | Hours from inbound to Jetix reply | <5 min ideal (literature); <24h acceptable | timestamp delta inbound→reply |

### §2.3 Layer 3 — Conversion metrics (weekly / monthly)

| Metric | Definition | Target benchmark | Measurement |
|---|---|---|---|
| **Cold → warm conversion** | % cold contacts becoming warm | 5-15% | CRM status transitions |
| **Warm → contacted conversion** | % warm becoming contacted | 50-80% | CRM status transitions |
| **Contacted → discovery_call conversion** | % contacted reaching discovery call | 30-50% | CRM status transitions |
| **Discovery → proposal conversion** | % discovery_call → proposal | 30-50% | CRM status transitions |
| **Proposal → closed_won** | Final win rate | 17-20% B2B benchmark; Jetix substrate-aligned target 25%+ | CRM status closed_won count |
| **Pipeline velocity** | Opps × Avg Value × Win Rate / Cycle Length | Track monthly; aim ≤75 days cycle | Derived from CRM |

### §2.4 Layer 4 — Amplification metrics (monthly / quarterly)

| Metric | Definition | Target | Measurement |
|---|---|---|---|
| **Amplification factor** | # of L2/L3 contacts publicly mentioning Jetix per month | ≥3 в Q1 launch; ≥10 в Q3 2026 | grep public mentions + CRM amplifier flag |
| **Public NPS proxy** | Promoters minus Detractors among warmed contacts | ≥20 launch; ≥40 EOY | survey or implicit (mentions vs reservations) |
| **Cohort retention** | % Wave 1 cohort still engaged month-N | ≥80% month-3 | Workshop attendance / contribution |
| **Cross-domain diversity** | # of domains в cohort (engineering / philosophy / business / governance / arts) | ≥4 domains | Wave 1 audit |
| **Substrate publication output** | New concept docs / wikis / methodology per month | 2-5 / month | git log count |
| **External citation rate** | # of external references к Jetix substrate per month | ≥1 в Q1 launch; ≥5 в Q3 2026 | Mentions tracking |

### §2.5 Layer 5 — KEYSTONE EOY 2026 cascade metrics

| Metric | EOY 2026 KEYSTONE target | Forward indicator | Current status |
|---|---|---|---|
| **Users** | 1M | Workshop cohort size + amplifier reach × cohort recruitment rate | <100 (early) |
| **$ raised** | $1B | Seed bridge $1M-$5M Q3 2026 → Series A trajectory | $0 (pre-launch) |
| **User-hours** | 100M | Workshop hours + cohort engagement × cohort size | <500 hours (early) |
| **150 → 15 → 1M cascade** | Achieved | Tier-1 partners count + L1 amplifier count + L2 reach | Pre-Phase-1 |

---

## §3 Measurement protocol

### §3.1 Daily

- Log every touch via `/crm-touch` (channel + status pre-touch + status post-touch + outcome flag)
- End-of-day reflection: any burnout signal flags?

### §3.2 Weekly (Friday reflection ritual per Phase 6)

- `/crm-weekly` skill output review
- Per-channel response rate calculation
- Pipeline movement counts (cold → warm → contacted)
- Burnout signals audit (per Phase 6 §5)
- Pivot decisions if needed (template revision / cadence adjustment / frame shift)

### §3.3 Monthly

- Cohort analysis (response rates per audience tier / per template)
- Amplification factor count
- Public NPS proxy estimation
- Substrate publication output count

### §3.4 Quarterly

- Cascade health check (150 → 15 → 1M trajectory)
- Workshop cohort retention assessment
- External citation rate review
- KEYSTONE EOY 2026 trajectory adjustment

---

## §4 Measurement tooling

### §4.1 Existing CRM skills

| Skill | Metric coverage |
|---|---|
| `/crm-touch` | Daily touches volume + per-channel distribution + pre/post status |
| `/crm-update` | Status transitions (conversion metrics) |
| `/crm-weekly` | Weekly aggregation report |
| `/crm-dash` | Real-time pipeline state dashboard |
| `/crm-stuck` | Stalled active entries detection |

### §4.2 Augmentation needed (future ops)

- Per-channel response rate calculator (derivable from /crm-touch logs)
- Amplification factor tracker (grep mentions; manual add к CRM amplifier flag)
- Pipeline velocity formula automation (HubSpot-style calc)
- KEYSTONE cascade tracker (Users / $ raised / user-hours; manual maintenance)

---

## §5 Anti-vanity-metric discipline

**Vanity metrics avoided:**
- Total followers/subscribers (without engagement quality)
- Total posts / threads / videos (without conversion impact)
- «Reached» counts от broadcast channels (without inbound DM signal)

**Quality-anchored metrics preferred:**
- Response RATE (not absolute count)
- Conversion percentages stage-by-stage
- Amplification factor (organic mentions; harder to game)
- Cohort retention (long-tail truth signal)

**R12 alignment:** metrics measure value delivered + relationships built; не extraction maximization.

---

## §6 Sources

- [Sales Funnel Conversion Rate Benchmarks 2026 (Glue Up)](https://www.glueup.com/blog/sales-funnel-conversion-rate-benchmarks)
- [B2B Conversion Funnel Playbook 2026 (Prospeo)](https://prospeo.io/s/b2b-conversion-funnel)
- [22 Essential B2B Sales Funnel Metrics 2026 (Growth Today)](https://www.growthtoday.co/blog/b2b-sales-funnel-metrics)
- [B2B SaaS Conversion Benchmarks 2026 (Pixels Within)](https://pixelswithin.com/b2b-saas-conversion-benchmarks-2026/)
- [2026 B2B SaaS Funnel Conversion Benchmarks (Causal Funnel)](https://www.causalfunnel.com/blog/b2b-saas-funnel-conversion-benchmarks-2026-data-insights/)
- Reichheld «The Ultimate Question 2.0»
- audio_686 (KEYSTONE 1M / $1B / 100M EOY 2026)
- `crm/_schema/statuses.yaml` (Jetix pipeline canonical)
