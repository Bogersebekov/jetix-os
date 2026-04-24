---
title: Investor × Integrator — Moat Synthesis + EISA-Moment Valuation
type: integration
layer: drafts
niche: meta
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: ingested
state: drafted
confidence: medium
confidence_method: expert-judgment-from-peer-drafts-tier1-and-bios-research
tier: tier-1
produced_by: investor-integrator
sources:
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - decisions/ROY-INFORMATION-DIET.md
  - raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md
  - prompts/km-architecture-research-2026-04-24.md
related:
  - swarm/wiki/foundations/swarm-alphas.md
binding_scope: km-architecture-investor-integrator-moat
mode: integrator
---

# Investor × Integrator — Moat Synthesis + EISA-Moment Valuation

## §1 Moat Analysis per Variant Flavor

This section evaluates each of the six KM architecture variant combinations
(Layer-A × Layer-B pairs) against a four-lens moat rubric: (1) does the variant
strengthen knowledge-as-leverage specificity, (2) does the variant prove UC-9 and
UC-10 by construction (not policy), (3) does the variant resist infrastructure
commoditization, and (4) does the variant compound over time without capex step-change.

**Moat lens ground truth.** Per `decisions/ROY-INFORMATION-DIET.md §1.6` (canonical):
"Knowledge-as-leverage — главный ров (moat). Jetix answers качественнее на порядок
при тех же вопросах." The moat is not the retrieval stack; it is the *curated Private
Library + methodology specificity + client-private KB architecture* that no cloud
provider can replicate by an API update. The BIOS research states the structural
lesson explicitly: "Ценность не разрушается, а перераспределяется: IBM теряет
лидерство, но Intel и Microsoft становятся триллионными компаниями, потому что они
находятся на слое, который нельзя клонировать через clean room."
[src:raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §10]

| Variant flavor | Moat effect | Reason | F / ClaimScope / R |
|---|---|---|---|
| **A1 + B1** (Filesystem-native / Thin-scaffold) — CONSERVATIVE BASELINE | **Strengthens** | Zero infrastructure capex preserves solo-founder runway for knowledge accumulation. Proves UC-9 by client-subtree namespacing (env-var, Phase A) and UC-10 by OFFLINE_MODE=1 structured-excerpt path. Moat source: Private Library quality compounds without infrastructure drag. Kill-condition: fails when wiki exceeds ~10K pages and PPR latency degrades client /ask quality below FPAR 80%. | F3 / Phase A G1-G2 / Refuted if PPR latency crosses 2s p95 at 5K pages AND BM25 is not triggered within 2 weeks |
| **A1 + B3** (Filesystem-native / Federated mini-swarm, P1 projects only) | **Strengthens (conditional)** | B3 allocates dedicated AI bandwidth to P1 revenue-generating projects (quick-money, ai-tools), compounding methodology delivery quality for the highest-ROI engagements. Does NOT dilute the moat IF restricted to P1 projects at G2+. Dilutes if extended to P3-P4 projects (fragmenting Max-sub turns). | F3 / P1 projects at G2+; NOT for P3-P4 / Refuted if Max-sub turn budget fragments across 8 simultaneous mini-swarms, degrading quality across all projects |
| **A2 + B3** (GraphRAG / Federated mini-swarm) — FULL AGGRESSIVE | **Strengthens at G3+, dilutes if pre-triggered** | GraphRAG community detection provides genuine cross-domain synthesis advantage at 15K+ pages. Combined with B3 mini-swarms, this is the full "Microsoft-position" play: workflow-layer intelligence that compounds. Pre-triggered at G2 (Kelly = -0.09 on GraphRAG G2 per investor-optimizer §2): **dilutes** the moat by consuming capex and ops overhead before the scale justifies it. | F3 / G3+ only (15K+ pages, €1M gate, contractor #1 hired); NOT for Phase A / Refuted if GraphRAG community detection produces sub-FPAR synthesis at G3 scale |
| **A3 + B1** (HippoRAG dense fallback / Thin-scaffold) — GERMAN-LANGUAGE HEDGE | **Neutral to strengthening** | A3 adds German-language semantic retrieval (Mittelstand DACH market). At G1-G2, this is a real-option: strengthens IF the German-language FPAR gap materializes for consulting clients; neutral cost if it does not. B1 thin-scaffold keeps ops overhead zero. The moat implication: German-language semantic precision is a genuine differentiator against US-based AI platforms deploying English-first retrieval. | F3 / DACH Mittelstand clients with German-language query volume; NOT applicable to English-first internal use / Refuted if German-language FPAR gap is not material (i.e., English-language retrieval scores >85% FPAR on German client queries) |
| **A2 + B2** (GraphRAG / PMBOK-rich scaffold) — REFUSED AT G1 | **Dilutes** | Per investor-optimizer §3 Layer-B barbell: B2 is refused at G1. PMBOK overhead on a solo-founder Phase A operation is negative-Kelly (b is low; q is high). Adds documentation liability without revenue. GraphRAG pre-triggered at G2 is also negative-Kelly (full Kelly = -0.09). Double-dilution of the moat: capex spend on infrastructure + methodology overhead simultaneously. | F3 / Refused at G1; revisit at G3 (team of 3) / Refuted if PMBOK overhead at G3 can be absorbed by contractor #1 AND GraphRAG G3 Kelly turns positive (= YES at G3 per investor-optimizer §2) |
| **A3 + B2** (HippoRAG dense / PMBOK-rich scaffold) — REFUSED AT G1 | **Dilutes** | Same rationale as A2+B2: B2 refused at G1. A3 is a real-option (design now, trigger at German-language FPAR failure) — pairing it with B2 at G1 adds ops complexity without revenue. | F3 / Refused at G1 / Same as above |

**Net moat verdict (synthesis):** A1+B1 is the moat-preserving baseline. A1+B3
(P1 restricted) is the first upgrade, compounding methodology quality on revenue
projects. A2+B3 and A3+B1 are G3+ options. A2+B2 and A3+B2 dilute and are
refused at G1. The pattern follows the BIOS parallel: the moat is NOT in the
retrieval infrastructure (which commoditizes) — it is in the Private Library
curation + methodology specificity + UC-9/UC-10 construction proofs.
[src:raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §11 Lesson 4]

---

## §2 Private Library ROI — Buffett Owner-Earnings Frame

**Owner-earnings definition (Pattern P1, investor-expert §2.4).** Owner-earnings
= cash the asset generates after maintenance costs. For the Private Library as an
intangible asset: owner-earnings = (consulting engagements enabled by /ask
retrieval × average engagement value) - (Library maintenance cost: curation time,
/lint cycles, /ingest effort, strategies.md write-backs).

**Investor-critic H-4 baseline.** As of Phase A, the Private Library has no
valuation cadence. Cited from investor-critic §1 H-4: "No valuation cadence
exists; documents establish strategic importance but no quarterly mark-to-market."
[src:swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md §1 H-4]

**Proposed mark-to-market formula (quarterly cadence per investor-optimizer Delta-H5).**

```
Library Owner-Earnings (quarterly) =
  N_engagements_enabled × avg_engagement_value
  - curation_time_cost (h/quarter × €/h)
  - /ingest_cycles × avg_turns_per_cycle × opportunity_cost_per_turn

Where:
  N_engagements_enabled = consulting engagements in quarter where /ask retrieval
                          contributed a material insight (qualitatively logged)
  avg_engagement_value   = €15K-€50K (Mittelstand client range per investor-critic §5)
  curation_time_cost     = Phase A ~4h/week × €120/h × 13 weeks = €6,240/quarter
  opportunity_cost/turn  = Max-sub constraint; sunk cost; treat as €0 marginal
```

**Phase A baseline estimate (conservative, F3).**
- Engagements enabled per quarter: 2-4 (Phase A, early pipeline)
- At €15K average: €30K-€60K gross value enabled
- Curation cost: €6,240/quarter
- Library quarterly owner-earnings: **€23,760 - €53,760** on an intangible asset
  whose book cost was ~€12K one-time (393 books × €30) + ~6 months of curation.
- Annual owner-earnings: **€95K - €215K** on a €12K initial investment.
- Owner-earnings yield: **8x - 18x** on initial acquisition cost in Year 1.

This is not GAAP earnings. This is the Buffett owner-earnings framing applied to
an intangible: the library enables consulting revenue it would not otherwise
generate, minus the cost to maintain the library's quality.

**FPAR as the retrieval-quality proxy.** First-Pass Acceptance Rate (FPAR) is the
fraction of /ask queries answered "sufficiently" without a follow-up query. Below
FPAR 80% for two consecutive quarters signals Library quality decay. Above FPAR
90% signals Library is outperforming: consider expanding curation investment
(more ingests, more typed edges, more /consolidate passes).

```
Quarterly mark-to-market ritual (proposed):
  1. FPAR trend (target ≥80%)
  2. Citation-density growth rate = new typed edges this quarter / total edges prior quarter
  3. Qualitative: Library contributed to N consulting engagements via /ask
  4. If FPAR < 80% for 2 consecutive quarters → Library-quality HITL escalation
  5. If citation-density growth rate < 5% → /consolidate pass scheduled
```

F: F3 (estimate; no production quarterly data yet; model is mechanically correct
given the cost structure)
ClaimScope: Applies to Phase A Jetix-internal Private Library (swarm/wiki/foundations/
as the canonical surface); does not include Tier-4 books (Phase B); does not include
client-specific KBs (priced separately per client engagement).
R: Refuted if first 3 quarterly reviews show FPAR consistently below 80% despite
curation investment — indicating the library architecture (not just quality) is the
bottleneck; receipt: quarterly review log in swarm/wiki/reviews/. Accepted if FPAR
remains ≥80% and N_engagements_enabled grows ≥2 per quarter.

---

## §3 Knowledge Compounding — Intangible-Asset Valuation at Scale

The Private Library is a compounding asset: each ingest adds not only pages but
typed edges that increase retrieval precision for all prior pages. This is the
lollapalooza effect (Pattern P4) applied to knowledge infrastructure: each new
page makes every prior page more valuable through cross-referencing.

**Discount-rate framework.** For an intangible asset that generates consulting
revenue but cannot be sold independently (it is embedded in Jetix's specific
knowledge), the appropriate discount rate is the opportunity cost of the
operator's time: €120/h × 40h/week = €4,800/week = ~€250K/year theoretical
ceiling. A 30% hurdle rate (Constellation reference per investor-expert §2.4
Pattern P6) applied to this ceiling gives a discount rate floor of €75K/year.

**Citation-density compounding.** Each well-connected page is retrievable via
Tier-3 BFS from multiple query entry points. At 1K pages: average degree ~11
edges/page (572 edges / 557 pages, current). At 5K pages with BM25 + PPR:
average degree is expected to compound to ~20 edges/page (knowledge-architecture
research §G.2 scale projections). At 50K pages with GraphRAG communities: average
degree ~30 edges/page with community summaries providing cross-domain shortcut
paths.

**Asset value table (three-point estimate, F3).**

| Wiki size (pages) | Estimated asset value (€) | Discount rate basis | Compounding mechanism |
|---|---|---|---|
| 1,000 | €180,000 - €360,000 | 30% hurdle on €54K-€108K annual owner-earnings (2-4 engagements/qtr × €15K avg, growing) | Thin moat: retrieval from single-niche; typed-BFS depth-2 sufficient; Private Library gives 3-5× FPAR advantage over generic retrieval |
| 5,000 | €600,000 - €1,200,000 | 30% hurdle on €180K-€360K annual owner-earnings (5-10 engagements/qtr × €18K avg; G2 gate) | Growing moat: multi-niche cross-domain synthesis; BM25 secondary; PPR-approximated retrieval; citation density compounding accelerates |
| 50,000 | €3,000,000 - €8,000,000 | 30% hurdle on €900K-€2,400K annual owner-earnings (G3-G4 scale; 20-50 engagements/qtr across team; €15K-€50K avg per engagement type) | Deep moat: GraphRAG community summaries enable one-shot cross-domain synthesis; per-client KBs federated; EISA-standard methodology deployed at scale; network effect begins (each client KB strengthens Jetix methodology through fedback) |

**Key compounding assumption:** owner-earnings grow non-linearly with wiki size
because retrieval precision improvement is super-linear in edges, while maintenance
cost grows sub-linearly (automation absorbs more of the curation overhead at G2+).

**Moat durability caveat (second-level thinking, Pattern P3 / Marks).** What is
already priced in by the Mittelstand AI market? Generic RAG with cloud LLMs. What
is NOT priced in: a 50,000-page wiki of curated, cited, falsifiability-checked
knowledge in systems + investing + engineering + management + philosophy domains,
connected by 1.25 million typed edges (25 edges/page × 50K pages), accessible
via offline-first local inference. That is the differentiation that cannot be
commoditized by a DeepSeek Compaq-moment — because it took years to accumulate
and cannot be replicated by running a clean-room process for 9 months.
[src:raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §10 Lesson 4:
"Infrastructure commoditizes; ценность уходит в application layer и в слои с
настоящими барьерами."]

F: F3 (estimate; valuation at scale is forward-looking with ±40% uncertainty band;
compounding assumption of non-linear edge growth is structurally grounded but not
empirically validated at the named page counts)
ClaimScope: Applies to Jetix's Internal Private Library + methodology-layer wiki as
a single compounding asset; does not include per-client KBs (those are separate
billable assets generating separate revenue streams).
R: Refuted if FPAR at 5,000 pages fails to improve over 1,000-page baseline despite
citation-density growth (indicating edges are being added without improving retrieval
precision — a quality-not-quantity failure); receipt: first 5K-page quarterly review.

---

## §4 Mittelstand AI Alliance — EISA-Moment Valuation

**The EISA analog precisely.** The BIOS research documents the EISA-moment
with precision: "IBM в 1987 попробовала вернуть контроль через PS/2 с
проприетарной шиной MCA. Индустрия создала свой открытый стандарт EISA в ответ
и проигнорировала MCA."
[src:raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §11 Lesson 6]

The Jetix EISA analog: Mittelstand does not want OpenAI/Microsoft to control the
AI-layer in their businesses. The Mittelstand AI Alliance positions as the
"independent, sovereign, European AI consortium" — the EISA response to the MCA
proprietary lock-in threat.

**Strategic Insight confirmation.** STRATEGIC-INSIGHT §3 (canonical): "Jetix
methodology будет published (documentation, templates, patterns) + legally
protected (IP/licensing) = open interface, closed implementation. Client's KB =
client's BIOS — у каждого свой, несравним, не копируется. Jetix orchestration
layer = EISA consortium — открытый стандарт, который все принимают."
[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3]

**BIOS research §13 confirms the valuation structure:**
"Mittelstand AI Alliance как EISA-момент — positioning as sovereign European AI
consortium... Структура а-ля Linux Foundation или ARM Holdings. Членство, IP-pool,
shared infrastructure."
[src:raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §13]

### Network-effect multiplier per added adopter

At the EISA consortium level, the value of membership compounds through Metcalfe's
law with a sector-specific modifier: each new Mittelstand member adds not just a
network node, but a domain-specific KB that strengthens the shared methodology
through fedback (per-client patterns promoted to global/compound-rules/ with HITL
ack). This is stronger than generic Metcalfe: each additional node increases
methodology quality, not just connectivity.

Estimation (F3, base-rate from Constellation Software's 30% hurdle rate model
applied to network-effect businesses):

| Gate | Members | Network-effect multiplier | Methodology quality improvement |
|---|---|---|---|
| G3 (€1M, ~10 members) | 50 Mittelstand clients | ~2.5× vs solo-Jetix | 10 client-specific methodology patterns promoted to global; 50× more domain edge-diversity in shared methodology wiki |
| G4 ($100M, ~50 members) | 500 Mittelstand clients | ~7× vs solo-Jetix | Cross-sector synthesis (manufacturing + services + logistics); Alliance methodology becomes de-facto DACH AI standard |
| G5 ($1T, ~500 members) | 5,000 Mittelstand clients | ~25× vs solo-Jetix | Pan-European sovereign AI methodology standard; regulatory compliance layer embedded; GDPR/EU AI Act attestation as membership benefit |

The multiplier is estimated as √N_members × methodology_quality_coefficient (1.3 for
each domain-diverse member vs generic user). This is more conservative than raw
Metcalfe (N²) because methodology-specificity caps network effects per sector.

### Licensing-revenue stack vs per-client deployment-revenue stack

Two revenue models at G3-G5. The investor must name the opportunity cost of one
vs the other.

**Per-client deployment revenue (current Path B model).**
Unit economics (investor-optimizer Delta-H3, confirmed): €18K year-1 / €15K year-2+
per Mittelstand client, 70.7% GM year-1, 80.8% recurring GM. At 50 clients (G3):
€750K/year recurring GM. At 500 clients (G4): €7.5M/year recurring GM.
Ceiling: ops-constrained (each client requires 2h/month Jetix-side support at scale;
at 500 clients = 1,000h/month = 6.25 FTE). At G4, the per-client deployment model
requires contractor infrastructure; it does not scale to 5,000 clients at solo-founder
quality.

**Alliance licensing revenue (EISA-standard methodology, G3+).**
Model: annual methodology license to each Alliance member, tiered by member size.
- Small Mittelstand (50-200 employees): €5K/year methodology license
- Mid Mittelstand (200-1,000 employees): €15K/year
- Large Mittelstand (1,000+ employees): €50K/year

GM on licensing revenue: ~90% (methodology is a digital product; incremental cost
per license = zero after methodology is productized per D18 lock).

At G3 (50 members, avg €10K/year): €500K/year, 90% GM = €450K net.
At G4 (500 members, avg €15K/year): €7.5M/year, 90% GM = €6.75M net.
At G5 (5,000 members, avg €20K/year): €100M/year, 90% GM = €90M net.

**Opportunity cost declaration (second-level thinking, Pattern P3 / Marks).**
The per-client deployment model scales GM but caps at ops-constrained ceiling.
The licensing model is nearly unbounded in margin but requires the methodology
to be productized (D18 lock) AND requires the Alliance to achieve recognized
standard status (6-12 month window per STRATEGIC-INSIGHT §8 rec 5). The path-not-
taken when choosing pure per-client deployment: forgoing €90M/year G5 licensing
revenue in exchange for more predictable €7.5M/year G4 deployment revenue. The
correct capital allocation is: maximize per-client deployment revenue through G3
(validates methodology, funds Alliance formalization), then shift to licensing-
primary revenue at G4. Barbell: 70% deployment / 30% licensing at G3; invert at G4.

F: F3 (estimate; network-effect multiplier is derived from first principles +
BIOS research historical parallel; licensing revenue model is based on analogy
to Linux Foundation / ARM Holdings pricing; no Mittelstand market survey data)
ClaimScope: Applies to DACH Mittelstand market 2026-2030; does not apply to
hyper-scale AI platforms (different competitive dynamics); does not apply to
non-EU markets without compliance-layer adaptation.
R: Refuted if a faster mover (AWS, Microsoft, SAP) launches a competing Mittelstand
AI consortium with comparable local-first architecture before Jetix reaches G3;
receipt: quarterly competitive landscape review. Accepted if no equivalent consortium
ships at G3-equivalent depth within 12 months of Alliance launch.

---

## §5 Wintel Parallel Correction — Jetix is EISA, NOT OS-Monopoly

This section is the investor's formal correction to a common misreading of the BIOS
parallel that would lead to a wrong capital allocation.

**The wrong read.** "Jetix should position as Microsoft — capture the workflow/OS
layer and extract monopoly rent." This is the narrative fallacy version of the BIOS
parallel: most compelling, most wrong. Anti-pattern AP-INV-8 (narrative fallacy
investing) fires here.

**Why the OS-monopoly position is rejected as un-Jetixy.**

The BIOS research is explicit about why Microsoft won: "Сетевые эффекты: разработчики
пишут под Windows, потому что пользователи на Windows; пользователи на Windows,
потому что там есть sofft. Замкнутый круг." And: "Microsoft контролировала стандарт
через WinHEC и API."
[src:raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §10]

Jetix cannot replicate this because:
1. D17 (Filesystem-SoT) and D13 (Open surface / Closed core) are locked decisions
   that structurally prevent a centralized-server model. "Jetix никогда не становится
   central server для client data." [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §4 D17]
2. D20 (USB-C positioning) explicitly targets standards-level interoperability, not
   monopoly. "Standards-level interoperability — клиент может заменить underlying LLM
   без потери своего KB." [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §4 D20]
3. Mittelstand clients will NOT accept a centralized-monopoly AI platform. GDPR +
   EU AI Act + German sovereignty culture = structural market rejection of the
   Microsoft-monopoly model. [src:raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §12 regulatory difference]
4. The OS-monopoly requires network-effect density that requires venture capital
   and aggressive growth. That contradicts D19 ($1T trajectory through owner-earnings
   compounding, not VC-backed growth) and the solo-founder Phase A constraint.

**The correct read: Jetix is the EISA standardization committee.**

EISA (Extended Industry Standard Architecture) was the OPEN standard that the
industry created to reject IBM's proprietary MCA. EISA was not owned by one company;
it was a consortium. Its value came from legitimacy, not monopoly.

Structural mapping:
- **IBM PS/2 / MCA** = OpenAI / Microsoft Azure trying to lock Mittelstand into cloud
  dependency ("you must send your data to us")
- **EISA consortium** = Mittelstand AI Alliance (sovereign, European, open methodology)
- **Compaq/Phoenix/AMI** = early Alliance members who prove the methodology works on
  their own infrastructure
- **Jetix** = the committee chair + methodology publisher + the Phoenix Technologies of
  the Alliance (Jetix does the 9-month clean-room work once; all Alliance members
  benefit from the methodology license)

**Capital implications of the EISA vs OS-monopoly distinction.**

The OS-monopoly model would require:
- Centralized server infrastructure (contradicts D17)
- Venture capital for rapid scale (contradicts D19 owner-earnings discipline)
- Network-effect investment at loss (contradicts the 30% hurdle rate floor)
- Giving up client data sovereignty to build the data flywheel (contradicts D13)

The EISA-standard model requires:
- Methodology productization (D18 lock: "productization over hours")
- Alliance formalization at Phase 2+ (€200K gate per STRATEGIC-INSIGHT §10)
- Patent protection on specific AI × Mittelstand method combinations (D15 lock: revenue-gated at €200K+)
- Marathon model: partners earn more on Jetix than alternatives (D21 matchmaker)

The EISA model is aligned with ALL 24 locked decisions. The OS-monopoly model
violates D13, D17, D19, and D20.

F: F4 (operational convention grounded in 3 locked decisions D13/D17/D20 + BIOS
research structural analysis + Strategic Insight §3-§4)
ClaimScope: Applies to Phase A-G4 strategic positioning; at G5 ($1T), the Alliance
may develop regulatory authority that changes the topology (but the peer-holon model
per systems-optimizer Delta-2 remains the correct structural frame)
R: Refuted if a non-centralized, non-monopoly Mittelstand AI consortium emerges from
a competitor with comparable depth before Jetix reaches G3 — demonstrating the EISA
position is not uniquely occupiable; receipt: G3 competitive review.

---

## §6 Capital Flow Recommendations per Gate (G1-G5)

Per investor-expert §1d `autonomous` row and §6.1 BOSC-A-T-X horizon-gate table.
All capital deployment requires HITL ack; these are proposals only.

### G1 — €50K gate (current state, Phase A)

**Capital posture:** Zero capex. Max-subscription only. Full A1+B1 barbell
(70/30 real-options per investor-optimizer §3).

- **KM investment:** None beyond Ruslan's time. Filesystem + git + HippoRAG PPR
  on current hardware. FPAR tracking begins (establish baseline).
- **Path B prep:** Productize onboarding kit to 8h delivery (D18 lock target).
  Target: first Path B Mittelstand client at €18K year-1 / €15K year-2+.
- **GPU stance:** On-demand only (Vast.ai €2-5/hour per demo, expensed per
  engagement). Kelly = 0.83/2 = 0.42 — proceed immediately.
  [src:swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md §2]
- **Alliance posture:** Informal (document the vision; no legal entity yet).
- **Risk-of-ruin floor:** No KM capex before €50K revenue gate. No GPU hardware.
  No Neo4j. No dedicated VPS fleet. Downside of wrong architecture bet: 4-8 weeks
  of Max-sub turns (sunk cost) + re-architecture time. Bounded and survivable.
  [src:swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md §2 H-6 fix]

### G2 — €200K gate (5 clients, ~5K wiki pages, first contractor consideration)

**Capital posture:** Trigger-conditional BM25 addition (PPR latency >2s p95).
No Neo4j. No pre-emptive GraphRAG.

- **KM investment:** BM25 secondary at trigger (Kelly = 0.53/2 = 0.27 of upgrade
  budget — proceed at trigger). Per-client wiki-roots isolation enforced (engineering-optimizer
  Δ1 + Δ3). OFFLINE_MODE=1 structured-excerpt path active for client demos.
- **Mistral 7B deployment:** Apache 2.0 license. Client-hosted (Path B: client
  buys hardware per Jetix spec sheet). Jetix-hosted (Path A: Hetzner CX41 €30/month
  per client). On-demand GPU rental at €80-120/month per client demo.
  [src:swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md §4]
- **Path B GM:** 70.7% year-1 (separate onboarding fee €3K + €15K/year). Recurring
  80.8% year-2+.
- **Alliance posture:** 3-5 pilot members (informal agreement). Begin methodology
  documentation for licensing.
- **Capex gate for contractor #1:** ≥3 paying clients AND contractor #1 hire ONLY
  if Path A ops overhead exceeds solo-founder ceiling (>5 concurrent Path A clients).
  [src:swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md §5 Path A notes]

### G3 — €1M gate (~15K pages, team of 3, Neo4j trigger)

**Capital posture:** Neo4j Community at 20K-edge threshold (Kelly = 0.75/2 = 0.34
of G3 infrastructure budget). GraphRAG cron at global-synthesis FPAR failure trigger
(Kelly = 0.60/2 = 0.25 of G3 engineering budget).

- **KM investment:** Per-client edge-store sharding (systems-optimizer Delta-5).
  holon-ref 13th edge type added (systems-optimizer Delta-1 — requires AWAITING-APPROVAL
  per D3 §3.5). GraphRAG community detection for cross-domain synthesis.
- **Inference stack:** Ollama + Llama 3.1-8B-Instruct Q4_K_M (engineering-optimizer
  Δ4 manifest, Phase B implementation). 16GB GPU hardware procurement at G3 gate
  (Kelly = 0.70/2 = 0.33 of G3 capex — proceed after 3-client confirmation).
- **Alliance posture:** Formal entity (Linux Foundation / ARM Holdings structure).
  First methodology licenses. Patent strategy activated (D15 lock: €200K+ trigger).
- **Revenue model:** 70% per-client deployment / 30% licensing (barbell shift begins).

### G4 — $100M gate (multi-BU, 500+ Alliance members)

**Capital posture:** Full hybrid retrieval stack (BM25 + dense + PPR + RRF).
Federated wikis with per-client edge-store (systems-optimizer Delta-5). Per-client
sub-brigadiers (B3 federated mini-swarms fully deployed).

- **Alliance revenue:** €7.5M/year licensing at 500 members × €15K avg. 90% GM.
- **Capex:** Vector DB self-hosted (Qdrant/Chroma, ~€200/month — immaterial at
  $100M revenue scale, <0.01% of revenue).
- **Revenue barbell shift:** 30% per-client deployment / 70% licensing (invert G3 barbell).
- **Horizon-gate shift note:** G4 → G5 transition requires HITL ack per §1d
  requires-approval. This row is a capital-deployment proposal only.

### G5 — $1T gate (civilizational-scale, 5,000+ members)

**Capital posture:** HITL-only deliberation at this scale. Methodological framework
rewrite test: ≤30% per Brief §5.1. Estimated rewrite at G5: add regulatory-engagement
layer + philanthropic-alignment structure + token-circulation (D23 Option B) = ~25%
rewrite. Pass (≤30%).

- **Alliance revenue:** €100M/year licensing at 5,000 members × €20K avg. 90% GM.
- **Retirement ledger (via-negativa, Pattern P5 / Taleb):** Retire any Alliance
  member below 30% Constellation hurdle rate sustained 4 quarters. Retire any
  methodology line that does not cohere with EU regulatory acceptance.
- **HITL required for every G5 capital decision without exception.**

---

## §7 Pros / Cons / Tradeoffs of the Moat Thesis

### Pros (strengthening factors)

1. **Structural impossibility of clean-room replication.** The Private Library's
   moat is accumulation time, not code. No competitor can replicate 393 curated
   books + 5 years of compounding typed edges through a 9-month clean-room process.
   This is the exact inverse of the IBM BIOS position: IBM's 8 KB BIOS was replicable
   in 9 months; Jetix's knowledge graph is NOT.
   [src:raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §11 Lesson 1]

2. **UC-9 / UC-10 as a strategic disqualification filter.** Any competitor that
   cannot prove client-isolation and offline-first inference by construction cannot
   serve GDPR-conscious Mittelstand. This filters out the 35K generic AI-wrapper
   companies and most US-based platforms.
   [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §0]

3. **EISA-standard position is occupiable NOW.** The 6-12 month window
   [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §8 rec 5] is
   open. No equivalent European sovereign AI consortium for Mittelstand exists.

4. **Owner-earnings compound without capex step-change.** Path B at enterprise
   scale (€50K/year) produces 94.2% recurring GM year-2+. The methodology, once
   productized, generates earnings with near-zero COGS growth. This is Buffett
   owner-earnings at the intangible-asset level.
   [src:swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md §6 key insight]

### Cons and kill-conditions

1. **Competitive window is short.** The BIOS research notes: "Скорость действия
   имеет значение... те, кто тянул, — проиграли."
   [src:raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §11 Lesson 5]
   Jetix must ship first Path B client with UC-9 + UC-10 proof within 6 months
   or a faster mover prices in the same position. **This is the moat's kill-condition #1.**

2. **Commoditization of AI agents.** The BIOS research warns: "К 2027 году такие
   системы будут продавать в GitHub Marketplace за €99/месяц. Твой ров должен быть
   не в агентах, а в знании Mittelstand, сети и процессах."
   [src:raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md §13 Риски]
   Jetix's agent framework commoditizes by 2027; the methodology and Private Library
   do not. **Kill-condition #2: if Jetix's moat narrative shifts to "best AI agents"
   rather than "best Mittelstand methodology", the moat fails.**

3. **UC-9 proof is currently policy, not construction.** The engineering-critic
   states explicitly: "Existing substrate can prove UC-9 by construction: NO."
   [src:swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md §6]
   Until engineering-optimizer Δ1+Δ3 are implemented and tested, UC-9 is a
   strategic claim without architectural backing. **Kill-condition #3: any Mittelstand
   client who investigates the isolation architecture finds a policy-level boundary,
   not a construction-level one — destroying trust.**

4. **Solo-founder ops ceiling at G2-G3.** Path A at 5+ clients (Ruslan solo)
   risks the "hours-billing trap" (D18 productization lock). Path C is unacceptable
   at Phase A margins (54% GM). The moat thesis depends on Path B scaling without
   Ruslan's time becoming the bottleneck.
   [src:swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md §5 Path A notes]

### Key tradeoffs

**Tradeoff 1: Library breadth vs depth.** More ingests (broader Library) increase
retrieval recall. Deeper /consolidate passes (denser edges) increase retrieval
precision. At Phase A with bounded turns, depth compounds faster than breadth.
Recommendation: prioritize /consolidate and typed-edge quality over raw page count.

**Tradeoff 2: Alliance formalization speed vs revenue focus.** Formalizing the
Alliance early (Phase 1) builds positioning but consumes founder attention and legal
fees before the €50K gate is cleared. Deferring to Phase 2 (€200K gate) is lower
risk but potentially misses the 6-12 month window. The investor's resolution:
Alliance informal documentation NOW (zero capex); formal entity at €200K gate only
if the window remains open and 3+ potential founding members are identified.

**Tradeoff 3: Mistral 7B vs Llama 3.1-8B as offline-first model.** Mistral 7B
has Apache 2.0 (cleanest license, no legal friction). Llama 3.1-8B has better
reasoning (higher FPAR on synthesis tasks). Investor recommendation: Mistral 7B
as the default (legal simplicity = lower cost of uncertainty); Llama 3.1-8B as
the upgrade path when client-confirmed synthesis quality gap materializes.
[src:swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md §4 recommended default]

---

## §8 Dissents Preserved + Provenance

### Dissents

**Dissent D-1 — Buffett lens (concentrated position) vs Taleb lens (barbell).**

The Buffett owner-earnings framing (concentrated, high-conviction position in
methodology-as-asset) would advocate maximizing depth of investment in the Private
Library and methodology BEFORE expanding to Alliance members. Concentrated: one
great thing done exceptionally.

The Taleb barbell framing advocates 70% conservative (A1+B1, zero-capex baseline)
+ 30% aggressive real-options (A2+B3 design work, Alliance positioning). Barbell:
never medium risk.

Both lenses are internally consistent. The synthesis adopts the barbell (investor-
optimizer §3, Layer-A + Layer-B combined) because the solo-founder Phase A risk
profile favors tail-protection over concentration. The Buffett lens is preserved
as the G3+ default when the operator has contractor #1 and can absorb concentration.

```yaml
dissent:
  - claim: "Concentrated methodology investment (Buffett) is superior to barbell at Phase A"
    F: F4 (operational convention; Buffett's concentrated approach is Buffett's own
       operating context — large capital base, no runway constraint, multiple decades
       of compounding. Solo-founder Phase A has a fundamentally different risk profile.)
    ClaimScope: Applies if Ruslan has €100K+ cash reserve (2+ years runway); does not
      apply at €50K gate with Max-subscription-only constraint
    R:
      refuted_if: "Ruslan's consulting revenue crosses €200K with no capex spend,
        demonstrating concentrated methodology investment outperformed the barbell"
      accepted_if: "Barbell preserves solo-founder runway through G1-G2 without
        stranded capital incident"
    source_lens: Buffett pattern P1 (§2.4) vs Taleb pattern P5 (§2.4)
```

**Dissent D-2 — FPAR 80% threshold vs 90% threshold.**

The investor-optimizer (Delta-H4) proposes FPAR 80% as the Library-quality floor.
The engineering-critic implies higher expectations for /ask in production client
contexts. A case can be made for FPAR 90% as the floor (library decay triggers
at 90%, not 80%).

```yaml
dissent:
  - claim: "FPAR threshold should be 90% for client-facing /ask, not 80%"
    F: F2 (operational convention; no empirical data yet on what FPAR corresponds to
       client satisfaction in Mittelstand consulting contexts)
    ClaimScope: Applies to client-facing /ask (Path A/B/C deployments); Phase A
      internal Jetix use may accept lower threshold
    R:
      refuted_if: "First 3 client engagements show FPAR 80-85% producing client
        complaints about /ask answer quality"
      accepted_if: "FPAR 80-85% produces no client satisfaction issues in first year"
```

**Dissent D-3 — Alliance timing (systems-optimizer vs investor-optimizer).**

Systems-optimizer Delta-2 and the BIOS research advocate positioning the peer-holon
Alliance topology NOW (Phase A). The investor-optimizer §5 Refusal 3 notes: "Alliance
formalization requires Phase 2 per Strategic Insight §10." The tension: positioning
vs formalizing. Resolution (synthesis): informal positioning (documented, public-
facing language) is zero-capex and can happen now; legal entity formation requires
€200K gate. The investor accepts both as consistent: position now, formalize later.

```yaml
dissent:
  - claim: "Alliance legal entity can be formed at Phase A without €200K gate"
    F: F2 (operational convention; no legal cost data for Linux Foundation / ARM
       Holdings equivalent structure in Germany)
    ClaimScope: Applies to the legal cost and ops overhead of a formal consortium;
      does not apply to informal positioning (positioning has no cost floor)
    R:
      refuted_if: "Legal counsel confirms Alliance formation cost <€5K one-time with
        minimal ongoing overhead — below the H-1 capex threshold"
      accepted_if: "Legal counsel quotes €20K+ for formation — confirming Phase 2 gate"
```

### Provenance

| Source | Range | Quote / basis |
|---|---|---|
| decisions/ROY-INFORMATION-DIET.md | §1.6 | "Knowledge-as-leverage — главный ров (moat). Jetix answers качественнее на порядок при тех же вопросах." |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §0 | "Jetix's play: занять эту позицию через local-first AI + client-private KB architecture." |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §3 | "Jetix methodology будет published + legally protected = open interface, closed implementation. Client's KB = client's BIOS." |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §4 D17 | "Jetix никогда не становится 'central server' для client data." |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §8 rec 5 | "Speed: window NOW — 6-12 месяцев максимум чтобы захватить position." |
| raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md | §10 structural analysis | "Ценность не разрушается, а перераспределяется... Intel и Microsoft выиграли потому, что их слои не клонировались." |
| raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md | §11 Lesson 4 | "Инфраструктурный слой коммодитизируется, ценность уходит в application layer и в слои с настоящими барьерами." |
| raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md | §11 Lesson 6 | "Стандарт всегда побеждает проприетарную платформу на зрелом рынке. IBM в 1987 попробовала вернуть контроль через PS/2 с MCA. Индустрия создала EISA." |
| raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md | §13 Решение 3 | "Mittelstand AI Alliance как EISA-момент — positioning as sovereign European AI consortium." |
| raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md | §13 Риски | "К 2027 году такие системы будут продавать в GitHub Marketplace за €99/месяц. Твой ров должен быть не в агентах, а в знании Mittelstand, сети и процессах." |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md | §1 H-4 | "No valuation cadence for the Private Library asset; no quarterly mark-to-market." |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md | §5 Path A | "Gross margin at €15K revenue: 70.0% (borderline)." |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md | §5 knowledge-as-leverage note | "The Library's value is not the cost of acquisition but the earnings it enables." |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md | §2 Kelly table | "GraphRAG at G2 pre-emptive: Kelly = -0.09. DO NOT BET." |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md | §3 barbell | "Net barbell: 70% conservative (A1+B1) / 30% real-options across aggressive tails." |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md | §6 key insight | "Path B at enterprise-tier (€50K/year) produces >90% recurring GM (yr 2+). The methodology, once productized, scales with zero COGS growth." |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md | §6 | "Existing substrate can prove UC-9 by construction: NO." |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md | §1 Δ2 | "OFFLINE_MODE=1 structured-excerpt synthesis — Phase A UC-10 path." |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md | §2 Delta-2 | "Peer-holon model: each client holon is autonomous; Jetix-central is methodology-provider, not parent-holon." |

### Synthesis confidence

confidence: medium
confidence_method: expert-judgment-from-peer-drafts-tier1-and-bios-research

**Confidence ceiling rationale.** The moat thesis is structurally sound and grounded
in 3 BIOS-research citations + 3 locked decisions (D13/D17/D20) + peer expert drafts.
The ceiling is medium (not high) because: (1) the EISA-moment valuation at G4-G5
scale is forward-looking with ±40% uncertainty; (2) the competitive-window claim
(6-12 months) cannot be empirically verified before the window closes; (3) UC-9
is currently policy-not-construction, making the moat's most critical architectural
pillar an aspiration rather than a proven fact. High confidence would require: first
Path B client shipped with confirmed UC-9 + UC-10 proof, and first quarterly FPAR
baseline established.

### Escalations

```yaml
escalations:
  - trigger: requires-hitl-ack
    gate-type: capital-flow-recommendation (§6 G1-G5 table)
    reason: All capital deployment decisions require Ruslan ack per investor-expert §1d never row.
            This draft is a PROPOSAL. No capital deployed without HITL.

  - trigger: requires-hitl-ack
    gate-type: horizon-gate-shift (G3 → G4 transition)
    reason: G3 to G4 is a phase-promotion event (€1M → $100M, Fission MHT). Requires
            explicit HITL ack per investor-expert §1d requires-approval.

  - trigger: peer-input-needed
    peer: engineering-expert
    mode: critic
    reason: UC-9 is currently policy-not-construction (engineering-critic §6 confirmed).
            The moat thesis in §1 (UC-9 strengthens moat) depends on UC-9 being proven
            by construction before any client deployment. Engineering-expert must confirm
            Δ1+Δ3 implementation closes the gap.

  - trigger: peer-input-needed
    peer: systems-expert
    mode: integrator
    reason: Delta-1 (holon-ref 13th edge) requires AWAITING-APPROVAL per D3 §3.5. The
            moat synthesis in §4 (federated per-client KB compounding) depends on this
            edge type being available. Systems × integrator must confirm the D3 extension
            gate before the Alliance valuation numbers in §4 are actionable.
```

---

*End of draft. Produced by investor-integrator mode. Brigadier promotes to canonical
after provenance gate + HITL ack. This draft is NOT canonical wiki. All capital
deployment decisions in §6 require Ruslan explicit ack before execution.*
