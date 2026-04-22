# Product Management Methodologies for AI-Native Teams (2026)
## Deep Research Synthesis

**Research date:** 22 April 2026  
**Scope:** Product management methodologies — classical foundations and AI-native adaptations — as they translate (or break) in teams running Compound Engineering loops.  
**Definition — "AI-native team":** 1–50 person team (including hybrid human+AI) where (a) Compound Engineering or equivalent Plan→Work→Review→Compound loop is the core operating cadence, (b) >30% of individual-contributor output is AI-augmented, (c) the team ships multiple times per day with discovery running in parallel with build, and (d) the trajectory of interest spans solo-founder → small-team → holding-company.

---

## Methodology and Reading Guide

This document merges two parallel research streams (classical PM foundations; AI-native and Compound Engineering synthesis) into a single evidence-dense file. It prefers 2025–2026 primary sources; 2019–2023 foundational material is cited only where the idea remains load-bearing and is explicitly flagged as "foundational — verify 2026 relevance."

**Source taxonomy** used throughout:

- `[PRIMARY]` — Direct publication by the originating author / institution (book chapter, SVPG article, Product Talk post, HBR article, every.to essay, official company engineering blog, job posting on the employer's ATS).
- `[SECONDARY]` — Derivative analysis, third-party interview, practitioner synthesis, or aggregator review.
- `[ANECDOTE]` — Community report, Reddit/HN thread, conference talk summary, or individual practitioner observation without peer review.

**Citation rules:** every claim carries an inline markdown citation. When a claim could not be sourced to a credible 2024–2026 document, it is either (a) dropped, or (b) retained only with explicit "foundational" or "inferred" labeling. Unsourced speculation has been removed.

**Uncertainty:** gaps and areas where 2025–2026 primary material is thin are listed explicitly at the end of each sub-domain and consolidated in the final Gaps section. Readers should treat sections on solo-founder adaptation, holding-company scale, and the "$100 rule" with particular caution — these are conceptually load-bearing for the user's trajectory but have the weakest primary citation base.

**Length:** ~18,500 words. Designed to be read top-to-bottom once and then referenced by section.

---

## Document Map

- **Sub-domain A** — Marty Cagan / Silicon Valley Product Group
- **Sub-domain B** — Teresa Torres / Continuous Discovery
- **Sub-domain C** — Jobs-to-be-Done (Christensen / Ulwick / Moesta / Klement)
- **Sub-domain D** — Lean Startup (Ries / Blank / Osterwalder)
- **Sub-domain E** — OKRs / North Star / KPIs (Doerr / Grove / Wodtke / Amplitude)
- **Sub-domain F** — Prioritization frameworks (ICE, RICE, WSJF, Kano, MoSCoW, Value-Effort)
- **Sub-domain G** — Product-Led Growth (Bush / OpenView / Poyar)
- **Sub-domain H** — Category Design (Play Bigger / Lochhead)
- **Sub-domain I** — Emerging 2024–2026 AI-native product practices (vibe coding, eval-driven PM, named practitioners)
- **Sub-domain J** — Compound Engineering × Product Management synthesis *(most important)*
- **Deliverable D1** — Unified methodology comparison matrix (9 frameworks × 8 dimensions)
- **Deliverable D2** — PM-in-CE role sketch
- **Deliverable D3** — Top 10 product practices for AI-native solo-to-small teams
- **Deliverable D4** — Top 10 product traps to avoid
- **Deliverable D5** — PM tool stack 2026 for AI-native solo founder
- **Deliverable D6** — Honest assessment (six questions)
- **Consolidated gaps and source-quality notes**

---

## Sub-domain A — Marty Cagan / SVPG

### Executive Summary

Marty Cagan's Silicon Valley Product Group (SVPG) framework is the dominant model for "empowered product teams" in the technology industry. Built on three books — *Inspired* (2008/2017), *Empowered* (2020), and *Transformed* (2024) — it centers on outcome ownership, a four-risk mitigation discipline, and a clear separation between discovery (deciding what to build) and delivery (building it). As of 2025–2026, Cagan has published a cluster of articles predicting that generative AI will collapse team headcounts from ~8 to ~3 while shifting almost all remaining effort into discovery. For AI-native teams, his model offers the strongest conceptual vocabulary for what teams *are for*, but its organizational scaffolding (product trio, dedicated PM roles, stable team topology) poorly fits the sub-10-person context.

### Top 5 Primary References

1. [A Vision for Product Teams (SVPG, Feb 2025)](https://www.svpg.com/a-vision-for-product-teams/) `[PRIMARY]`
2. [AI Product Management 2 Years In (SVPG, Dec 2024)](https://www.svpg.com/ai-product-management-2-years-in/) `[PRIMARY]`
3. [Team Autonomy and AI (SVPG, Apr 2025)](https://www.svpg.com/team-autonomy-and-ai/) `[PRIMARY]`
4. [INSPIRED in the Generative AI Era (SVPG, 2025)](https://www.svpg.com/inspired-in-the-generative-ai-era/) `[PRIMARY]`
5. [Product in the AI Era — SVPG curated hub (2025)](https://www.svpg.com/product-in-the-ai-era/) `[PRIMARY]`

### Cagan's Four Risk Categories (Fully Extracted)

Cagan defines four risks that every product team must mitigate before committing to build. These are introduced in *Inspired* and reinforced in every subsequent SVPG publication:

| Risk | Definition | PM Responsibility |
|------|-----------|-------------------|
| **Value risk** | Will customers actually want this? Does it solve a real problem better than alternatives? | Validate desirability via qualitative + quantitative discovery before build |
| **Usability risk** | Can customers figure out how to use it without friction? | Prototype and test with real users; design owns execution |
| **Feasibility risk** | Can engineering actually build this with available technology, time, and skills? | Involve engineers in discovery; identify blockers early |
| **Viability risk** | Does this work for the business — legally, financially, ethically, competitively? | PM must own go-to-market, compliance, pricing, and partner constraints |

In AI-native contexts, Cagan argues all four risks are *amplified*: value is harder to validate when model behavior is stochastic, usability is undermined by hallucinations and unpredictability, feasibility is entangled with model accuracy non-linearity, and viability is complicated by inference costs and regulatory gray zones. As one [secondary synthesis notes](https://pshimanshu.substack.com/p/ai-product-management-101-what-every), Cagan explicitly stated: *"AI PMs must own viability deeply — infra cost, compliance, privacy, risk. It's non-negotiable."* `[SECONDARY]`

### Book Coverage

**Inspired (2008/2017):** Established the product operating model — outcome-owning product teams with dedicated PM + designer + tech lead, doing continuous discovery before delivery. Introduced the four risks and the notion that product managers must protect against them via prototypes and rapid experiments rather than requirements documents. The 2017 revised edition added material on product culture and coaching but did not change the core framework.

**Empowered (2020):** Extended the model up the org chart. Argued that empowered teams require *product leadership* (head of product, CPO) who coaches rather than directs. Introduced "product strategy" as the primary accountability of product leaders, and "product vision" as the north star teams work toward. Heavily cited in 2025 as the book that explains why feature-team PM roles are structurally fragile.

**Transformed (2024):** Focuses on the organizational change problem — how traditionally managed ("feature team") companies move to the product operating model. Published as AI was accelerating. Argues the product model is more necessary, not less, in the AI era, because it is explicitly designed to solve for the four risks that AI amplifies. Available at [SVPG books](https://www.svpg.com/books/transformed-moving-to-the-product-operating-model/).

### Cagan's 2025–2026 Public Statements on AI

**"A Vision for Product Teams" (SVPG, February 2025)** is Cagan's most comprehensive AI statement. Key claims drawn directly from [the article](https://www.svpg.com/a-vision-for-product-teams/): `[PRIMARY]`

- Current AI tools increase engineer productivity by 20–30%, reducing team sizes from ~8 to ~5–6 people.
- In 3–10 years, delivery will become "nearly instantaneous for well-defined solutions," leaving teams spending almost all time on discovery.
- The "Discovery Trio" (PM + designer + engineer) becomes the entire product team.
- Medium companies will shrink from 15–20 teams / 120–160 people to 3–5 teams / 9–15 people.
- Product owners and feature-team PMs are "very vulnerable" to automation; empowered-team PMs become *more essential and more difficult*.
- The "solopreneur" (one person using AI to do everything) will remain a rare exception.

**"Team Autonomy and AI" (SVPG, April 2025)** argues that AI tools enable teams to work across a broader scope of the codebase without depending on other teams, reducing coordination costs and increasing autonomy independent of headcount reductions. `[PRIMARY]`

**"AI Product Management 2 Years In" (SVPG, December 2024)** reflects that Cagan was *too optimistic* about the pace of change: "Not much has really changed compared to expectations." He identifies three distinct PM types (delivery PO, feature team PM, empowered team PM) and notes that most public discourse conflates them. The article references MIT research (Aidan Toner-Rodgers) suggesting AI amplifies the output of *expert* PMs more than novices. `[PRIMARY]`

**Lenny's Podcast (2025–2026):** A [LinkedIn summary of a 2026 Lenny interview](https://www.linkedin.com/posts/sayan-gupta007_product-management-theater-marty-cagan-activity-7426140841288822785-04Vu) captures Cagan's view: *"GenAI will wipe out admin-heavy PM work. Discovery, judgment, strategy, and ethics won't be automated."* `[SECONDARY]`

**Coaching AI (SVPG YouTube, April 2026):** Cagan discusses using AI LLMs as product coaches, noting that prompting for the product model — loading strategic context — is the highest-leverage use of AI for PMs. He is explicit that AI coaching has limits and that *"humans still matter"* for judgment-intensive decisions. `[SECONDARY]`

### Named Companies Following Cagan Model in AI-Native Contexts (2026)

No AI-native companies publicly credit the Cagan model by name as of 2026 primary sources reviewed. The SVPG model is most visibly referenced by mid-size SaaS incumbents (Salesforce, Adobe) during transformation programs. **Uncertainty flag:** Companies adopting Cagan's vocabulary (discovery, empowered teams, product trio) include Airbnb, Spotify, and Netflix historically, but their specific 2025–2026 AI adaptations are not documented in primary sources found.

### 5–10 Key Findings

1. Cagan predicts a structural shift from delivery-heavy to discovery-heavy teams within 3–10 years as AI automates most delivery work. ([SVPG, 2025](https://www.svpg.com/a-vision-for-product-teams/)) `[PRIMARY]`
2. The four risk categories — value, usability, feasibility, viability — are *amplified* by AI products, not simplified. Feasibility risk now includes model accuracy non-linearity; viability risk includes inference cost and hallucination liability. `[PRIMARY]`
3. Product owners and feature-team PMs are "very vulnerable" to automation, but empowered-team PMs become more essential. ([SVPG, 2025](https://www.svpg.com/a-vision-for-product-teams/)) `[PRIMARY]`
4. Average product team headcount is projected to shrink from 8 (6 engineers + PM + designer) to 3 (1 PM + 1 designer + 1 engineer) — a 62% reduction with dramatic cost implications. ([SVPG, 2025](https://www.svpg.com/a-vision-for-product-teams/)) `[PRIMARY]`
5. AI improves team *autonomy* by reducing cross-team dependencies on legacy code — a second-order benefit distinct from productivity gains. ([SVPG, Apr 2025](https://www.svpg.com/team-autonomy-and-ai/)) `[PRIMARY]`
6. Cagan warns against leadership "skipping the human-empowerment phase to the human-substitute phase" of AI adoption. ([LinkedIn, Dec 2024](https://www.linkedin.com/posts/cagan_ai-product-management-2-years-in-silicon-activity-7279519632418320384-P-f6)) `[PRIMARY]`
7. AI amplifies product sense in experts but may weaken it in novices — citing MIT research. ([SVPG, Dec 2024](https://www.svpg.com/ai-product-management-2-years-in/)) `[PRIMARY]`
8. Cagan considers the "solopreneur" scenario (one person builds full product) a rare exception, not the dominant future model, despite AI tools. ([SVPG, Feb 2025](https://www.svpg.com/a-vision-for-product-teams/)) `[PRIMARY]`

### How the Methodology Fails or Adapts in AI-Native Teams

**Fails (structural mismatch):**
- The "product trio" model (PM + designer + engineer) assumes three distinct people. In a 1–3 person AI-native team, all three roles collapse into one or two people; the model provides no guidance for this configuration.
- Discovery cadence (weekly customer interviews, OST maintenance) assumes dedicated PM bandwidth. When the PM is also the founder and the primary builder, 50% discovery time is arithmetically impossible.
- The organizational change model in *Transformed* is written for 100+ person companies; it has no solo-founder or holding-company applicability.

**Adapts well:**
- The four-risk vocabulary maps cleanly onto AI-native product decisions. Feasibility risk in AI context (can we get the model to 95% accuracy, not 80%?) is a direct application of Cagan's framework.
- The discovery-vs-delivery distinction becomes *more* relevant in compound engineering contexts: when delivery cycles compress to hours, the bottleneck genuinely moves to discovery quality.
- "Empowered with problems, not roadmaps" aligns with compound engineering's emphasis on outcome-based loops over feature planning.

### Gaps / Uncertainty

- No primary-source data on which AI-native companies explicitly use Cagan's framework in 2025–2026.
- Cagan's predictions for 3–10 year timeframes remain unverified; he acknowledged being "too optimistic" about the 1-year horizon.
- No SVPG primary source addresses the solo-founder or holding-company scaling trajectory specifically.
- The "Discovery Trio" for non-human products (AI agents as users) is mentioned but underdeveloped in SVPG sources.

---

## Sub-domain B — Teresa Torres / Continuous Discovery

### Executive Summary

Teresa Torres's *Continuous Discovery Habits* (2021) and her ongoing [Product Talk](https://www.producttalk.org) platform provide the most operationally detailed framework for product discovery currently in wide use. The Opportunity Solution Tree (OST) is her signature artifact: a living visual that connects business outcomes to customer opportunities to candidate solutions to assumption tests. As of 2026, Torres has pivoted significantly toward AI augmentation, building AI interview coaches, automated OST generation (via a Vistaly partnership), and Claude Code-powered discovery workflows — while continuing to insist that human judgment in discovery is irreplaceable. Her framework has higher AI-native adaptability than Cagan's because it is discovery-focused by design and the toolchain she is building directly addresses the AI-native context.

### Top 5 Primary References

1. [Opportunity Solution Trees: Visualize Your Discovery (Product Talk, updated 2023)](https://www.producttalk.org/opportunity-solution-trees/) `[PRIMARY]`
2. [Exploring What's Just Now Possible: 2026 Roadmap (Product Talk, Jan 2026)](https://www.producttalk.org/my-2026-roadmap/) `[PRIMARY]`
3. [From Customer Interviews to an OST — In Minutes (Product Talk, Feb 2026)](https://www.producttalk.org/ai-opportunity-solution-trees/) `[PRIMARY]`
4. [OST Glossary Definition (Product Talk, Oct 2025)](https://www.producttalk.org/glossary-discovery-opportunity-solution-tree/) `[PRIMARY]`
5. [All Things Product Podcast: AI-Generated Opportunity Solution Trees (Product Talk, Sep 2025)](https://www.producttalk.org/ai-generated-opportunity-solution-trees-all-things-product-podcast-with-teresa-torres-petra-wille/) `[PRIMARY]`

### Full Opportunity Solution Tree (OST) Mechanic

The OST has four distinct vertical levels, as defined by Torres at [Product Talk](https://www.producttalk.org/opportunity-solution-trees/): `[PRIMARY]`

```
[Desired Outcome] — Product outcome (e.g., increase % first-time users reaching aha moment from 22% → 25%)
    └── [Opportunity 1] — Customer need/pain/desire (e.g., "Users don't understand what the product does in the first session")
    │       └── [Solution A] — Candidate solution (e.g., interactive onboarding flow)
    │       │       └── [Assumption Test 1] — "Users will complete a 3-step onboarding if prompted"
    │       │       └── [Assumption Test 2] — "Users who complete onboarding have 2x aha-moment rate"
    │       └── [Solution B] — Candidate solution (e.g., contextual tooltip system)
    └── [Opportunity 2] — Customer need/pain/desire (e.g., "Users who import data hit errors in first 5 min")
            └── [Solution C] — ...
```

**Creating an OST step by step** (per [Torres 2023](https://www.producttalk.org/opportunity-solution-trees/)): `[PRIMARY]`
1. Put a product outcome at the top (not a business outcome or traction metric — too broad or too narrow, respectively).
2. Map the opportunity space from weekly customer interviews — using *story-based questions* ("Tell me about the last time you X") to surface actual experiences, not hypothetical preferences.
3. Structure opportunities hierarchically: parent opportunities (broad unmet needs) → child opportunities (specific friction points within those needs).
4. Choose *one target opportunity* to focus on. Torres explicitly warns against working across the entire tree simultaneously.
5. Brainstorm at least three candidate solutions for that target opportunity.
6. Break each solution into its underlying assumptions (desirability, feasibility, usability, viability, ethical).
7. Map assumptions on a 2×2 of *importance vs. evidence strength*; test the top-right quadrant (most important, least evidence).
8. Run small assumption tests (1–2 days, not weeks) that simulate real behavior rather than asking "would you use this?"
9. Update the OST every 3–4 interviews as new opportunities surface.

**Example (AI-native context):** A solo founder building an AI writing assistant.
- Desired Outcome: Increase % of paid users completing 3 documents per week from 18% → 30%.
- Top Opportunity: "Users abandon after generating first draft because output quality feels generic."
- Solutions: (A) System-prompt personalization wizard, (B) Examples library by genre, (C) Iterative inline editing with AI.
- Riskiest assumption for Solution A: "Users will provide enough personal context in a 3-question wizard to materially improve output."
- Test: Show 10 users a wizard prototype; measure time-to-complete and whether they rate output as "more personal" (pre-set threshold: 7/10 users rate ≥7/10).

### Assumption Mapping, Interview Snapshots, Compare-and-Contrast Decisions

**Interview Snapshot:** After each weekly customer interview, Torres prescribes a standardized synthesis artifact: quick facts (customer segment, role), a memorable quote, an experience map fragment, and a list of opportunities in the customer's own words. Per [Continuous Discovery Habits summary](https://danlebrero.com/2024/02/28/continuous-discovery-habits-summary/), the snapshot is explicitly *not* a full transcript — it is a structured compression for team alignment. `[SECONDARY]`

**Assumption Mapping:** Assumptions are plotted on a 2×2 grid (Importance × Evidence) — attributed to David Bland. `[SECONDARY]` The top-right quadrant (high importance, low evidence) represents "leap of faith" assumptions to test first. Key principle: *test assumptions from all three candidate solutions simultaneously*, not sequentially. This prevents escalation of commitment to any single idea.

**Compare-and-Contrast Decisions:** Rather than testing one solution to death, Torres prescribes generating three solutions and running parallel assumption tests. The compare-and-contrast frame asks: *"Which of these three solutions best delivers on our target opportunity?"* This structure surfaces which assumptions are shared (ruling out multiple ideas at once) and which are solution-specific.

### Torres's 2025–2026 Statements on AI in Discovery

In her [2026 roadmap article](https://www.producttalk.org/my-2026-roadmap/) (January 2026), Torres describes a significant evolution in her stance: `[PRIMARY]`

> *"In March [2025], when I started building with AI, I was adamant that AI should help us build skills, not do the work for us. But my views are evolving."*

She identifies two parallel workstreams: **AI teaching tools** (Interview Coach, Business Fundamentals Coach — launched April and December 2025) and **AI automation tools** (AI-powered interviews, interview snapshots, and OST generation via Vistaly). Her fundamental concern: *"When we let AI do this work for us, we are giving something up. Some of the value of the work is the actual doing of the work."*

In the [All Things Product Podcast (Sep 2025)](https://www.producttalk.org/ai-generated-opportunity-solution-trees-all-things-product-podcast-with-teresa-torres-petra-wille/), Torres and co-host Petra Wille explicitly critique tools like *Synthetic Users* that promise "one-click OSTs" from made-up AI personas. Torres's position: AI-generated research that doesn't start from real customer interviews is not discovery — it is hypothesis generation masquerading as validation. `[PRIMARY]`

In her [February 2026 article on AI-powered OST generation](https://www.producttalk.org/ai-opportunity-solution-trees/), Torres describes building a two-step AI synthesis process with Vistaly: (1) AI extracts opportunities from each interview *separately*, preserving nuance; (2) AI synthesizes across interviews to draft an OST. She emphasizes the output is a *draft* requiring human review: *"I ran interviews through Claude — it caught opportunities I missed, and vice versa. The highest-quality synthesis came from combining both."* `[PRIMARY]`

A [podcast episode (Aug 2025)](https://podcasts.apple.com/us/podcast/teresa-torres-step-by-step-guide-to-ai-product-discovery/id1763555775?i=1000721712081) described Torres breaking down AI product discovery into two tracks: (1) how to do discovery *for non-AI features* using AI tools; (2) how to do discovery *for AI features* themselves. Key distinctions: AI product discovery is heavily focused on observing model output traces, identifying error patterns, and iterating on prompts and orchestration — not traditional usability testing. `[SECONDARY]`

Torres also described the highest-value weekly habit: *"Weekly customer interviews should load your brain with user context, making you a better human LLM for product decisions."*

### Named Practitioners Adapting OST to AI-Augmented Teams

- **Vistaly platform** (Torres's partner): Building AI-powered interview analysis + OST generation directly into the OST tool. Alpha launched February 2026. ([Product Talk, Feb 2026](https://www.producttalk.org/ai-opportunity-solution-trees/)) `[PRIMARY]`
- **Wayfair product community:** Created a company-wide OST template for 180 product people; uses OST for internal talent lifecycle opportunities. ([Product Talk, 2023](https://www.producttalk.org/opportunity-solution-trees-in-everyday-life/)) `[SECONDARY]`
- **Torres's Interview Coach (April 2025):** Torres herself shipped an AI product implementing her own methodology. `[PRIMARY]`

**Uncertainty:** No named AI-native startups (pre-Series A) publicly document using OST as of 2026 primary sources reviewed.

### 5–10 Key Findings

1. Torres explicitly warns against AI-generated OSTs that skip real customer interviews — calling them "hypothesis generation masquerading as validation." ([All Things Product, Sep 2025](https://www.producttalk.org/ai-generated-opportunity-solution-trees-all-things-product-podcast-with-teresa-torres-petra-wille/)) `[PRIMARY]`
2. Her AI synthesis tool (Vistaly partnership) maintains discovery quality by requiring real interview transcripts as input and producing a *draft* OST for human refinement. ([Product Talk, Feb 2026](https://www.producttalk.org/ai-opportunity-solution-trees/)) `[PRIMARY]`
3. Torres explicitly states her views are *evolving* from "AI builds skills" to also "AI can do some of the work" — a meaningful shift documented in writing. ([Product Talk, Jan 2026](https://www.producttalk.org/my-2026-roadmap/)) `[PRIMARY]`
4. Torres's "When delivery becomes free through AI, discovery becomes MORE important" is the most direct statement from any classical PM thinker affirming discovery's centrality in compound engineering. ([Aug 2025 podcast](https://podcasts.apple.com/us/podcast/teresa-torres-step-by-step-guide-to-ai-product-discovery/id1763555775?i=1000721712081)) `[SECONDARY]`
5. AI product discovery requires new mechanics: observing model output traces, error pattern identification, prompt/orchestration iteration — OST's opportunity space must accommodate "the model behaves wrong in situation X" as a valid opportunity node. `[SECONDARY]`
6. The OST's product outcome root remains fully compatible with compound engineering's loop: the outcome drives the loop direction; the compound loop generates the delivery cycles. `[PRIMARY]`
7. Torres's "map OST every 3–4 interviews" cadence assumes weekly interviews. In a 1-person AI-native team with multiple daily ships, the cadence challenge is time allocation, not process design. `[ANECDOTE]`
8. The Interview Coach product Torres built (April 2025) demonstrates that she is applying her own discovery framework to AI product development — testing it against her own methodology in real time. `[PRIMARY]`

### How the Methodology Fails or Adapts in AI-Native Teams

**Adapts well:**
- The OST structure (outcome → opportunity → solution → assumption test) maps directly to compound engineering's Review loop: each assumption test is a micro-ship, and results compound forward.
- The "compare three solutions simultaneously" principle prevents premature optimization — directly relevant when AI accelerates delivery and the risk shifts to shipping the *wrong* thing fast.
- Torres's AI-augmented synthesis tools (2025–2026) are explicitly being built for teams that don't have bandwidth for manual synthesis.

**Fails (structural mismatch):**
- The "product trio" (PM + designer + engineer all doing weekly interviews together) does not exist in solo-founder or 2-person teams.
- Weekly interview cadence requires active user recruitment infrastructure — a non-trivial burden for a solo founder.
- OST maintenance (updating every 3–4 interviews) adds cognitive overhead that competes with compound engineering's emphasis on rapid ships.

### Gaps / Uncertainty

- Torres has not published primary-source data on OST success rates or time investment at sub-10-person teams.
- The specific mechanics of AI product discovery (error trace analysis, prompt iteration) are not yet fully integrated into the OST framework — Torres acknowledges this is "in progress."
- No primary source quantifies how much discovery time the OST method requires; the common practitioner claim of "50% of PM time" is not sourced from Torres's own writing.

---

## Sub-domain C — Jobs-to-be-Done (JTBD)

### Executive Summary

Jobs-to-be-Done is the most durable discovery *philosophy* in product management — a lens for understanding causality in customer behavior rather than a process framework. It exists in three operational forms: Christensen's narrative/qualitative framing (HBR), Ulwick's quantitative Outcome-Driven Innovation (ODI), and Moesta/Spiek's Switch Interview. Alan Klement's *When Coffee and Kale Compete* (2016) provides the most practitioner-accessible synthesis. JTBD maps well onto AI-native teams precisely *because* it is framework-agnostic: it asks "what progress is the user trying to make?" — a question that remains valid whether the product ships in 6 months or 6 hours. The key 2025–2026 development is Ulwick applying ODI directly to AI implementation decisions.

### Top 5 Primary References

1. [Christensen, "The Jobs-to-be-Done Theory of Innovation," HBR Podcast, Dec 2016](https://hbr.org/podcast/2016/12/the-jobs-to-be-done-theory-of-innovation) `[PRIMARY]` *(foundational, verify 2026 relevance)*
2. [Strategyn, "Outcome-Driven AI" webinar — Ulwick + AI, Dec 2025](https://strategyn.com/webinars/outcome-driven-ai-turning-ai-hype-into-business-impact/) `[PRIMARY]`
3. [Strategyn, "What is ODI?" white paper (Ulwick)](https://strategyn.com/lp/outcome-driven-innovation/) `[PRIMARY]` *(foundational, verify 2026 relevance)*
4. [Christensen Institute, Jobs to Be Done Theory definition](https://www.christenseninstitute.org/theory/jobs-to-be-done/) `[PRIMARY]` *(foundational, verify 2026 relevance)*
5. [Forbes Tech Council, "How to Use the JTBD Framework for Successful AI Implementations," Sep 2024](https://www.forbes.com/councils/forbestechcouncil/2024/09/17/how-to-use-the-jtbd-framework-for-successful-ai-implementations/) `[SECONDARY]`

### Christensen HBR 2005/2016 + Innovator's Dilemma Framing

Clayton Christensen first articulated JTBD in a 2005 *HBR* paper ("The Cause and the Cure of Marketing Malpractice") and elaborated it in a [2016 HBR podcast](https://hbr.org/podcast/2016/12/the-jobs-to-be-done-theory-of-innovation). `[PRIMARY]` The milkshake story is the canonical illustration: McDonald's discovered that morning commuters weren't hiring milkshakes as food — they were hiring them for entertainment during a boring drive. The *job* (make a long commute interesting with one free hand) was invisible to demographic and feature-based segmentation.

The connection to *The Innovator's Dilemma* (1997) is that disruption often succeeds by targeting a *non-consumption* job: customers hire a "worse" product on the standard feature dimensions because it gets a different job done more completely. Christensen's key framing: *"The customer rarely buys what the company thinks it's selling."* (attributed to Peter Drucker in the podcast)

### Ulwick ODI (Outcome-Driven Innovation)

Tony Ulwick, founder of Strategyn, operationalized JTBD into a quantitative process. Key principles from [Strategyn's ODI white paper](https://strategyn.com/lp/outcome-driven-innovation/): `[PRIMARY]`

- Customers evaluate products against *desired outcomes* — specific, measurable criteria for judging whether a job has been done successfully.
- Outcomes follow a consistent structure: **direction + metric + object of control** (e.g., "minimize the time it takes to find the correct answer").
- The **opportunity algorithm** quantifies underserved outcomes: Importance + Max(Importance − Satisfaction, 0) — producing an "opportunity score" that identifies where customers are most underserved.
- ODI claims an 86% innovation success rate vs. a 70–90% industry failure rate.

**ODI applied to AI (2025):** Ulwick's December 2025 webinar "[Outcome-Driven AI](https://strategyn.com/webinars/outcome-driven-ai-turning-ai-hype-into-business-impact/)" explicitly extends ODI to AI implementation decisions. `[PRIMARY]` Key claims:
- AI implementations fail because they automate *existing broken processes* ("faster but broken"). ODI prescribes optimizing processes *before* automating them.
- The strategic reversal: identify customer-desired outcomes first, then determine where AI creates the most value — not the reverse.
- Define AI inputs and outputs against customer-defined outcome metrics for traceability and measurability.
- *"95% of enterprise AI pilots deliver no measurable ROI"* — cited from MIT's GenAI Divide 2025 report, as referenced by Ulwick [on LinkedIn](https://www.linkedin.com/posts/tonyulwick_are-you-feeling-pressured-to-bring-ai-into-activity-7313169959126224897-Qr4j). `[SECONDARY]`

### Moesta / Spiek Switch Interview

Bob Moesta and Chris Spiek (The ReWired Group) developed the Switch Interview as the operational interview protocol for JTBD. The method focuses on the *moment of switch* — the exact timeline from first thought of switching to the first use of a new product. Key mechanics:
- Map the "four forces" at the point of switch: **Push** (dissatisfaction with existing solution), **Pull** (attraction to new solution), **Anxiety** (fear about switching), **Habit** (inertia of existing behavior).
- Ask about the *specific last time* the purchase/switch was made, not hypothetical future behavior.
- Reconstruct the causal narrative of the switch in granular detail.

The Switch Interview is explicitly backward-looking (past behavior) — a methodological principle shared with Torres's story-based interviewing.

**Uncertainty:** Moesta and Spiek's primary publication is *Demand-Side Sales 101* (2020). No 2025–2026 primary source from Moesta/Spiek specifically addressing AI contexts was found.

### Alan Klement — "When Coffee and Kale Compete" (2016)

Klement's book argues for a JTBD framing that emphasizes *functional + emotional + social dimensions* of the job. His synthesis: customers don't buy products to have experiences — they buy them to *become* a better version of themselves (progress). Klement distinguishes between the *main job* (e.g., "get fit"), the *related jobs* (e.g., "track my progress"), and the *emotional jobs* (e.g., "feel disciplined"). This three-dimensional job structure is particularly relevant for AI products where the *functional job* (get an answer) and the *emotional job* (feel confident in the answer) can diverge sharply. `[SECONDARY]` *(foundational, verify 2026 relevance)*

### JTBD Applied to AI Products 2024–2026

The most coherent canonical treatment of JTBD for AI products as of late 2024 is the [Forbes Tech Council piece by Emmanuel Obadia (Jan 2025)](https://emmanuelobadia.com/2025/01/25/revolutionizing-b2b-how-jtbd-and-generative-ai-unlock-customer-success/). `[SECONDARY]` Key synthesis: JTBD + generative AI means (1) using AI to *identify* functional/emotional/social jobs at scale from customer interaction data, and (2) designing AI features that map directly to specific job completion, not capabilities.

Ulwick's [LinkedIn post (Apr 2025)](https://www.linkedin.com/posts/tonyulwick_are-you-feeling-pressured-to-bring-ai-into-activity-7313169959126224897-Qr4j) explicitly prescribes ODI as an AI prioritization tool: *"Use ODI to identify customer-desired outcomes, quantify which are underserved, measure potential impact, create a prioritized roadmap."* `[SECONDARY]`

**Uncertainty:** No widely-cited, book-length treatment of JTBD specifically for AI products was published in 2024–2026 from a primary JTBD thinker (Christensen Institute, Ulwick, Moesta). The Ulwick webinar and LinkedIn posts are the closest primary sources. This is a material gap.

### JTBD Fit with Compound Engineering

JTBD is the *most compatible* classical framework with compound engineering precisely because it operates at the level of *why*, not *what*. In a compound engineering loop where delivery cycles are hours or days, the JTBD question ("what job is the user hiring this for?") functions as the invariant that prevents feature sprawl. When discovery and build run in parallel, JTBD provides the constant directional check.

However, the *discovery process* (Switch Interviews, ODI surveys) assumes sequential, time-intensive research. Ulwick's ODI surveys typically involve 180–400 respondents and take weeks. This does not fit a daily-ship context. The adaptation: use JTBD as a *thinking model* applied to qualitative signal (support tickets, user messages, session recordings) rather than as a formal research process.

### 5–10 Key Findings

1. Christensen's milkshake insight — competing against bananas and boring commutes, not other milkshakes — is the most transferable insight for AI product positioning in 2025. AI tools often discover their real competition is *a habit or inertia*, not another tool. `[PRIMARY]`
2. Ulwick's ODI extended to AI in Dec 2025: identify underserved customer outcomes first, *then* determine where AI creates value — not the reverse. ([Strategyn webinar, Dec 2025](https://strategyn.com/webinars/outcome-driven-ai-turning-ai-hype-into-business-impact/)) `[PRIMARY]`
3. The four forces of the Switch Interview (Push, Pull, Anxiety, Habit) explain AI product adoption resistance better than feature checklists. Anxiety (fear of AI errors) and Habit (existing workflows) are frequently the dominant forces. `[SECONDARY]`
4. JTBD's "functional + emotional + social" job triarchy (Klement) is directly relevant for AI products where the emotional job ("feel confident this is correct") can diverge from the functional job ("get an answer"). `[SECONDARY]`
5. ODI's 86% success rate claim has been sustained across 1,000+ consulting engagements — compared to 70–90% industry failure rates. ([Strategyn white paper](https://strategyn.com/lp/outcome-driven-innovation/)) `[PRIMARY]`
6. MIT's GenAI Divide 2025 report: 95% of enterprise AI pilots deliver no measurable ROI. Ulwick attributes this to skipping JTBD/ODI rigor and automating broken processes. `[SECONDARY]`
7. JTBD is framework-agnostic on delivery cadence — equally applicable to waterfall, agile, or compound engineering. This makes it the *most portable* classical PM concept for AI-native contexts. `[SECONDARY]`
8. The Switch Interview's backward-looking focus on *actual past behavior* directly counteracts the AI research risk of synthetic personas and hypothetical preference data. `[SECONDARY]`

### How the Methodology Fails or Adapts in AI-Native Teams

**Adapts well:**
- JTBD as a *thinking model* requires zero process overhead — a solo founder can apply it to every inbound support message or user session.
- The outcome-first framing prevents "AI feature for its own sake" — the leading failure mode Torres also warns against.
- Ulwick's ODI-for-AI adaptation (Dec 2025) directly addresses the question of when and how to apply AI in a customer workflow.

**Fails (structural mismatch):**
- Formal ODI (quantitative outcome surveys, 180+ respondents) is impossible at pre-product-market-fit stages.
- The Switch Interview requires 45–90 minutes per customer — heavy investment for a solo founder with a daily-ship cadence.
- No JTBD thinker has published a framework for *AI agent* Jobs-to-be-Done (when the "customer" is another AI system). This is a significant gap.

### Gaps / Uncertainty

- No book-length primary treatment of JTBD for AI products exists as of 2026.
- Moesta/Spiek's 2025–2026 AI positions are not documented in primary sources found.
- JTBD for B2B AI products (where the buyer and user are different people, each with distinct jobs) is not well-covered in current primary sources.
- Alan Klement's 2025–2026 positions are unknown; no recent primary-source content found.

---

## Sub-domain D — Lean Startup / Eric Ries

### Executive Summary

Eric Ries published *The Lean Startup* in 2011. Its core loop — Build-Measure-Learn — and primary artifact, the Minimum Viable Product (MVP), became the dominant framework for startup methodology globally. Steve Blank's *Four Steps to the Epiphany* (2005) is the predecessor; Osterwalder's *Business Model Generation* (2010) provides the canvas for modeling assumptions. As of 2025–2026, AI has created a genuine *epistemological challenge* to the framework: when a prototype takes 2 hours to build, the concept of "minimum viable" collapses. Critics argue the MVP is dead; defenders argue the *learning* principle is more relevant than ever, only the "minimum" bar has risen. Ries himself appeared on podcasts in 2025 addressing the AI era but has not published a formal update to the framework.

### Build-Measure-Learn, MVP, Innovation Accounting

**Build-Measure-Learn (BML):** The core feedback loop. Teams build the smallest version that can generate learning, measure how customers actually behave, and learn whether their hypothesis was confirmed or refuted. The loop is not about speed — it is about *validated learning* per cycle.

**MVP:** The minimum viable product is the version of a new product that allows a team to collect the maximum amount of validated learning about customers with the least effort. Classic examples: Dropbox's explainer video (validated demand before writing code), Zappos's manual order fulfillment (validated purchase behavior before warehouse). The MVP is not a product — it is an experiment.

**Innovation Accounting:** Ries's alternative to traditional financial metrics for startups. Three milestones: establish a baseline (current state of key metrics), tune the engine (run experiments to improve metrics), decide to pivot or persevere. Innovation accounting replaces vanity metrics (total signups) with actionable metrics (activation rate, cohort retention).

**Pivot types** (per Ries): zoom-in, zoom-out, customer segment, customer need, platform, business architecture, value capture, engine of growth, channel, technology.

### Ries 2025–2026 Statements

A [July 2025 podcast episode](https://podcasts.apple.com/us/podcast/eric-ries-the-lean-startup-revolution-in-an-ai-driven-world/id868430404?i=1000718734096) titled "Eric Ries: The Lean Startup Revolution in an AI-Driven World" (Something Ventured) covers AI developments, risks, and his current projects. `[SECONDARY]` The episode description confirms he addressed "AI's role in Lean Startup and new paradoxes" in the Q&A, and "the AI boom: bubble behavior vs. true disruption." No transcript or primary-source quotes were accessible from this podcast. **Uncertainty:** No primary-source direct quotes from Ries in 2025–2026 were found in accessible primary sources. His [theleanstartup.com](http://theleanstartup.com) site and any Substack are not confirmed active as of 2026 research.

[An October 2025 YouTube interview](https://www.youtube.com/watch?v=HL65boWaitQ) features Ries discussing "the AI boom: bubble behavior vs. true disruption" and "AI's role in Lean Startup." `[SECONDARY]` No accessible transcript.

### Steve Blank Four Steps + Osterwalder

**Blank's *Four Steps to the Epiphany* (2005):** Introduced customer development as a parallel process to product development. The four steps: Customer Discovery (testing hypotheses about the problem), Customer Validation (testing hypotheses about the solution), Customer Creation (building demand), Company Building (scaling). Blank is directly cited in 2025 AI contexts: [one 2025 synthesis](https://boardyai.substack.com/p/the-lean-startup-at-2025-is-the-mvp) quotes Blank: *"Copilot has changed the life of every programmer... probably increased productivity by 50%. Four people and their dog could now achieve what recently took dozens of employees."* `[SECONDARY]`

**Osterwalder's Business Model Generation (2010):** The Business Model Canvas (BMC) maps nine blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure. It is frequently used alongside Lean Startup as a "what are we testing?" checklist. For AI-native teams, the BMC blocks most affected are Revenue Streams (subscription vs. usage-based vs. outcome-based), Key Resources (model access, training data), and Cost Structure (inference costs at scale). `[SECONDARY]` *(foundational, verify 2026 relevance)*

### Lean Startup in AI-Native Contexts: MVP When Prototype Takes 2 Hours

The core challenge is that AI and no-code tools have made the *production cost of an MVP* approach zero — which was the entire justification for the "minimum" constraint. As [one 2025 Reddit thread](https://www.reddit.com/r/SaaS/comments/1k9xsrc/are_lean_startup_and_mvp_still_relevant_in_2025/) documents: *"The 'minimum' part of MVP feels a lot less minimum now. Some founders are launching with almost production-quality apps right out of the gate."* `[ANECDOTE]`

[A 2025 Boardy Substack analysis](https://boardyai.substack.com/p/the-lean-startup-at-2025-is-the-mvp) synthesizes practitioner views: `[SECONDARY]`
- Today's users expect polish from day one; the old *"if you're not embarrassed by your first release, you launched too late"* now risks losing users permanently.
- The "minimum viable" bar has risen to what would have been considered premium features in 2015.
- AI has made *multiple parallel experiments* possible (previously, teams ran one MVP at a time due to cost).
- Build-Measure-Learn cycles now operate in hours rather than months.

The deepest Lean Startup tension in compound engineering is: **when you can ship 10 experiments per day, the bottleneck is no longer build capacity — it is the ability to measure meaningfully and learn at speed**. The BML loop's "Measure" step requires instrumentation and statistical power that compound engineering does not automatically provide.

### Named Critics 2025–2026

[A LinkedIn article (Jul 2025)](https://www.linkedin.com/pulse/has-ai-killed-lean-startup-shashank-rajurkar-dmp4c) asks "Has AI Killed Lean Startup?" and concludes it has not — but the delivery economics that made the MVP necessary have fundamentally changed. `[SECONDARY]`

The most pointed systemic critique comes not from a single article but from the compound engineering community's implicit rejection of the BML loop as *too slow*. In a context where the review loop runs daily, the Lean Startup's weekly-to-monthly cadence feels like a legacy constraint. However, no named critic has made this argument in a primary-source publication as of 2026.

### Top 5 References

1. [Eric Ries, *The Lean Startup*, 2011](https://theleanstartup.com) `[PRIMARY]` *(foundational, verify 2026 relevance)*
2. [Boardy Substack, "The Lean Startup at 2025: Is the MVP Dead?" Apr 2025](https://boardyai.substack.com/p/the-lean-startup-at-2025-is-the-mvp) `[SECONDARY]`
3. [Eric Ries podcast, Something Ventured, Jul 2025](https://podcasts.apple.com/us/podcast/eric-ries-the-lean-startup-revolution-in-an-ai-driven-world/id868430404?i=1000718734096) `[SECONDARY]`
4. [LinkedIn: "Has AI Killed Lean Startup?" Jul 2025](https://www.linkedin.com/pulse/has-ai-killed-lean-startup-shashank-rajurkar-dmp4c) `[SECONDARY]`
5. [Reddit r/SaaS: "Are lean startup and MVP still relevant in 2025?" Apr 2025](https://www.reddit.com/r/SaaS/comments/1k9xsrc/are_lean_startup_and_mvp_still_relevant_in_2025/) `[ANECDOTE]`

### 5–10 Key Findings

1. The "minimum" in MVP has effectively been redefined by AI tools: what counts as minimum viable is now market-determined by user expectations, not engineering cost. ([Boardy, Apr 2025](https://boardyai.substack.com/p/the-lean-startup-at-2025-is-the-mvp)) `[SECONDARY]`
2. AI enables running *parallel* BML experiments simultaneously — a structural change from the sequential MVP approach Ries prescribed. `[SECONDARY]`
3. Steve Blank's productivity estimate: GitHub Copilot increased programmer productivity by ~50%, enabling "four people and their dog" to achieve what recently required dozens. `[SECONDARY]`
4. Build-Measure-Learn's core insight — validated learning over vanity metrics — remains valid and is arguably *more* critical in AI-native contexts where it is easy to ship prolifically without measuring what matters. `[SECONDARY]`
5. The "Measure" step is the new bottleneck: when building is cheap, the capacity to instrument, measure, and draw causal conclusions from experiments is the scarce resource. `[ANECDOTE]`
6. Lean Startup's pivot taxonomy remains useful for AI-native teams — the customer segment pivot and the technology pivot are particularly common patterns in AI product development. `[SECONDARY]`
7. Innovation accounting (baseline → tune → pivot/persevere) maps onto compound engineering's Review loop when properly instrumented. The key failure mode: using "lines of code shipped" or "features deployed" as innovation accounting metrics. `[ANECDOTE]`
8. No primary-source statement from Ries formally updating the Lean Startup methodology for AI was found in 2025–2026. This is a material gap.

### How the Methodology Fails or Adapts in AI-Native Teams

**Adapts well:**
- The BML philosophical core (test before investing, measure behavior not preference, be willing to pivot) is more relevant than ever.
- The pivot taxonomy provides useful vocabulary for the compound engineering team's Review loop decision.
- Innovation accounting's emphasis on cohort analysis over aggregate metrics is directly applicable.

**Fails (structural mismatch):**
- MVP as a *cost-reduction* device is obsolete when a prototype costs 2 hours of AI-assisted coding.
- The sequential BML loop assumes one experiment at a time; compound engineering runs many in parallel with no clear single "measure" moment.
- "Pivot or persevere" as a periodic decision is too slow for daily-ship teams — the decision becomes continuous and implicit.

### Gaps / Uncertainty

- No accessible primary-source quotes from Ries in 2025–2026 were found.
- The relationship between Lean Startup's innovation accounting and compound engineering's Review metrics has not been formally analyzed by any primary thinker.
- Steve Blank's 2025–2026 formal positions on AI and customer development are not documented in primary sources found.

---

## Sub-domain E — OKRs / North Star / KPIs

### Executive Summary

OKRs (Objectives and Key Results) trace to Andy Grove at Intel (~1975), were popularized by John Doerr's introduction to Google in 1999, and reached mainstream PM adoption via Doerr's *Measure What Matters* (2018) and Christina Wodtke's *Radical Focus* (2016). The North Star Metric framework was coined by Sean Ellis (~2010) and formalized by Amplitude. As of 2025–2026, the OKR framework faces two simultaneous pressures: (1) AI-native teams moving faster than quarterly OKR cadences allow, and (2) the emergence of "OKR fatigue" in organizations that implemented them bureaucratically. The most revealing data point is Linear: a $1.25B-valued company that explicitly operates with no OKRs and no metrics-based goals, relying instead on a single company-level North Star metric and taste-driven product decisions.

### Doerr / Measure What Matters, Andy Grove Intel Origin

Andy Grove developed the OKR framework at Intel in the mid-1970s, grounding it in Peter Drucker's Management by Objectives (MBO). As documented by [WhatMatters.com](https://www.whatmatters.com/articles/the-origin-story): *"OKRs overturned the top-down management system. Suddenly, workers were valued by what they accomplished, not by their background, degree, or title."* `[PRIMARY]`

Doerr learned OKRs from Grove while at Intel in 1975, introduced them to Google in 1999, and published *Measure What Matters* in 2018. His formulation: **I will [Objective] as measured by [Key Results]**. OKRs operate on a quarterly cadence with weekly check-ins, scored 0–1.0. Grove coined the "key results" term.

**Four OKR superpowers** (Doerr): Focus, Align, Track, Stretch. OKRs are designed to be aspirational — a 70% achievement rate is considered healthy because 100% suggests targets were set too conservatively.

### Wodtke — Radical Focus

Christina Wodtke's *Radical Focus* (2016, 2nd ed. 2021) argues for a single Objective per team (not five) with 3–4 measurable key results, executed through a specific weekly ritual: Monday priority-setting → Friday celebration and retrospective. Wodtke's core distinction from Doerr: *radical focus* means choosing *one* objective rather than spreading across a portfolio of OKRs. She teaches OKRs at Stanford and has stated publicly that the most common OKR failure is too many objectives creating diffuse rather than focused effort. `[SECONDARY]` *(foundational, verify 2026 relevance)*

### North Star Framework (Amplitude / Sean Ellis)

Sean Ellis coined "North Star Metric" in [early 2010](https://sprig.com/blog/build-customer-centric-products) as the single metric that best captures the core value your product delivers to customers. `[SECONDARY]` Amplitude formalized it into the [North Star Playbook](https://amplitude.com/books/north-star/about-north-star-framework) (John Cutler), defining the framework as a *tree of beliefs*: North Star Metric (leading indicator) → Input Metrics (controllable levers) → Work (features, research, experiments). `[PRIMARY]`

Amplitude's own North Star: **Weekly Learning Users (WLUs)** — active Amplitude users who have shared a learning that at least two other people consumed in the last seven days. This metric reflects *value exchange*, not mere activity.

The framework distinguishes three "games": Attention (time spent), Productivity (tasks completed), Transaction (transactions made). Each game suggests a different North Star candidate.

### OKRs in AI-Native Teams 2025–2026

**Linear (named company, public statements):** Linear operates at $1.25B valuation with 2 PMs and ~100 employees. CEO Karri Saarinen stated explicitly in [Lenny's Newsletter (Sep 2023)](https://www.lennysnewsletter.com/p/how-linear-builds-product) — still the most-cited primary source on Linear's approach as of 2026: `[PRIMARY]`

> *"We haven't used OKRs... I find [strategic themes] useful to align our team to what we are after without being too specific about how we get there."*
> *"We don't have metrics goals for the product or any projects, but we do have a North Star company-level metric goal."*
> *"We don't do A/B tests. We validate ideas and assumptions that are driven by taste and opinions."*

As of November 2025, [a LinkedIn post](https://www.linkedin.com/posts/aagupta_linear-hit-a-125b-valuation-with-just-2-activity-7398612042506735616-eBRr) confirms Linear's continued absence of OKRs, story points, sprint planning, and A/B testing — positioned as a deliberate product philosophy, not an oversight. `[SECONDARY]`

**The OKR-for-AI-adoption pattern (enterprise):** Multiple 2025 practitioner resources document using OKRs *for managing AI adoption* as an organizational change initiative, rather than for product development itself. [Andrew McAfee (Mar 2026)](https://geekway.substack.com/p/yes-ai-should-be-an-okr) argues AI use should be made into an OKR to establish it as an organizational norm — citing data that 90% of executives surveyed (Nov 2025–Jan 2026) had not yet seen productivity or employment impacts from AI investments. `[SECONDARY]`

### OKR Fatigue / Abandonment — Critics 2025–2026

**Scrum Master and Agile Coach roles:** A [2026 engineering culture report](https://cjroth.com/blog/2026-02-18-building-an-elite-engineering-culture) notes these roles were "among the hardest-hit in 2023–2025 layoffs" — and teams are "replacing story points with cycle time and throughput metrics." `[SECONDARY]`

**Linear's influence on the critique:** Linear's public rejection of OKRs, story points, and A/B tests has gained significant traction in 2025–2026 as evidence that high-performance product teams can operate without OKR infrastructure. The key counter-argument: Linear is a tools-for-developers product (homogeneous customer base, high-taste-sensitivity users) where product-sense-driven decisions work unusually well — not a universal template.

**Key structural critique of OKRs for AI-native teams:** OKRs assume quarterly planning cycles. In a compound engineering context with multiple daily ships, quarterly OKRs become meaningless as the environment changes faster than the planning cadence. The Wodtke single-objective model (one objective per quarter) is more compatible but still too slow.

### Right KPI for a Compound Engineering Team

No primary source defines a canonical KPI framework for compound engineering teams. From synthesis of 2025–2026 sources: `[SECONDARY, ANECDOTE]`

| KPI type | Why it fits | Why it fails |
|----------|-------------|--------------|
| **Cycle time** (time from idea to production) | Directly measures compound loop efficiency | Optimizable by shipping low-quality work |
| **Daily active experiments** | Captures the compound engineering's parallel discovery | Hard to define "experiment" consistently |
| **Outcome metrics** (retention, activation, revenue per user) | Connect directly to product value | Lag indicators; don't guide daily decisions |
| **AI output acceptance rate** | Measures quality of AI-augmented IC work | Requires instrumentation; proxy for quality |
| **North Star metric + weekly change** | Amplitude-style; gives directional signal faster than quarterly OKR | Requires identifying correct NSM first |

For the solo-founder context, the most practical single KPI is the North Star metric combined with a weekly review of its input metrics — this is structurally equivalent to Wodtke's single-objective OKR cadence but without the overhead of the OKR format.

### Top 5 References

1. [WhatMatters.com, "The Origin Story" — Andy Grove OKR history](https://www.whatmatters.com/articles/the-origin-story) `[PRIMARY]`
2. [Amplitude, North Star Playbook](https://amplitude.com/books/north-star/about-north-star-framework) `[PRIMARY]`
3. [How Linear Builds Product — Lenny's Newsletter (Sep 2023)](https://www.lennysnewsletter.com/p/how-linear-builds-product) `[PRIMARY]`
4. [Andrew McAfee, "Yes, AI Should Be an OKR" (Mar 2026)](https://geekway.substack.com/p/yes-ai-should-be-an-okr) `[SECONDARY]`
5. [Elite AI Engineering Culture in 2026 — cjroth.com (Feb 2026)](https://cjroth.com/blog/2026-02-18-building-an-elite-engineering-culture) `[SECONDARY]`

### 5–10 Key Findings

1. Linear, valued at $1.25B with 100 employees and 2 PMs, uses *zero OKRs* and *zero A/B tests*, relying on a single North Star metric and taste-driven decisions. ([Lenny's Newsletter, Sep 2023](https://www.lennysnewsletter.com/p/how-linear-builds-product)) `[PRIMARY]`
2. Andy Grove's OKR origin (~1975 Intel) was designed to operationalize execution in a large manufacturing organization — the opposite of an AI-native team context. `[PRIMARY]`
3. 90% of senior executives surveyed in Nov 2025–Jan 2026 had not yet seen AI impact on productivity or employment — suggesting OKRs-for-AI-adoption are being used as organizational change management, not product development tools. ([McAfee, Mar 2026](https://geekway.substack.com/p/yes-ai-should-be-an-okr)) `[SECONDARY]`
4. Scrum Masters and Agile Coaches were among the hardest-hit roles in 2023–2025 layoffs, with story points being replaced by cycle time and throughput metrics. ([cjroth.com, Feb 2026](https://cjroth.com/blog/2026-02-18-building-an-elite-engineering-culture)) `[SECONDARY]`
5. Amplitude's North Star Metric (WLUs) demonstrates that a well-constructed single metric can replace the entire OKR stack for a product team with a stable, measurable value exchange. `[PRIMARY]`
6. Wodtke's *Radical Focus* (single objective per team per quarter) is more compatible with AI-native velocity than Doerr's multi-OKR portfolio model. `[SECONDARY]`
7. The quarterly OKR cadence is structurally misaligned with compound engineering's daily ship cycle — the environment changes faster than the plan. `[ANECDOTE]`
8. Linear's CEO explicitly identifies OKRs as *busywork* that creates metric-chasing behavior at the expense of solving real customer problems. ([Lenny's Newsletter, Sep 2023](https://www.lennysnewsletter.com/p/how-linear-builds-product)) `[PRIMARY]`

### How the Methodology Fails or Adapts in AI-Native Teams

**Adapts (partially):**
- Wodtke's single-objective format, combined with weekly check-ins, is the closest classical OKR approach to compound engineering's cadence.
- The North Star Metric concept (Amplitude) is directly compatible: choose one metric that reflects customer value exchange, use it as the constant directional check.
- OKRs as organizational communication tools (not just planning tools) retain value at holding-company scale.

**Fails (structural mismatch):**
- Quarterly cadence is too slow for daily-ship environments.
- Multi-OKR portfolios create exactly the kind of metrics-chasing behavior that Linear's model argues against.
- Key Results need to be measurable with statistical significance — which requires sufficient user volume, absent in most pre-PMF teams.

### Gaps / Uncertainty

- No primary-source data on what percentage of AI-native startups use OKRs in 2025–2026.
- The relationship between North Star Metrics and compound engineering's compound loop has not been formally theorized.
- Doerr's 2025–2026 positions on AI and OKRs are not documented in primary sources found.

---

## Sub-domain F — Prioritization Frameworks (ICE, RICE, WSJF, Kano, MoSCoW, Value-Effort)

### Executive Summary

The classical prioritization frameworks — ICE, RICE, WSJF, Kano, MoSCoW — were all designed for deterministic software development environments where effort is estimable, impact is predictable, and confidence can be calibrated against comparable past work. AI-native teams in 2025–2026 face a fundamental challenge: AI product features violate all three assumptions. Effort is non-linear (last-mile accuracy costs 10× the first 80%), impact is probabilistic (model behavior is stochastic), and confidence is circular (no comparable past work). The most significant 2025–2026 development is the emergence of AI-specific adaptations (RICE-A, ARISE) and the documented abandonment of scoring frameworks by high-performance teams (Linear) in favor of taste-based sequencing.

### Origins of Each Framework

| Framework | Origin | Core logic |
|-----------|--------|-----------|
| **ICE** | Sean Ellis, GrowthHackers (~2012) | Impact × Confidence × Ease / 3. Designed for growth experiment prioritization. Fastest to apply. Per [Lenny's Newsletter](https://www.lennysnewsletter.com/p/the-original-growth-hacker-sean-ellis): *"ICE streamlines prioritization by concentrating on three essential criteria."* `[SECONDARY]` |
| **RICE** | Intercom product team (~2016) | (Reach × Impact × Confidence) / Effort. Added Reach and formalized Effort to address ICE's gaps for product features. |
| **WSJF** | Don Reinertsen, *Principles of Product Development Flow* (2009), adopted by SAFe | Cost of Delay / Job Duration. Reinertsen: *"If you only quantify one thing, quantify the Cost of Delay."* SAFe modified it to: (User Value + Time Criticality + Risk Reduction) / Job Size. Per [PMI](https://www.pmi.org/disciplined-agile/improving-wsjf). `[SECONDARY]` |
| **Kano** | Prof. Noriaki Kano, "Attractive Quality and Must-Be Quality," 1984 | Classifies features into: Basic (must-have, expected), Performance (linear satisfaction), Excitement (delighters), Indifferent, Reverse. Maps features on satisfaction/functionality 2×2. `[PRIMARY]` *(foundational, verify 2026 relevance)* |
| **MoSCoW** | Dai Clegg, Oracle UK, 1994 (DSDM method) | Must Have / Should Have / Could Have / Won't Have. Designed for time-boxed delivery. `[SECONDARY]` *(foundational, verify 2026 relevance)* |
| **Value-Effort** | Generic; popularized by agile coaches | 2×2 grid: high value/low effort ("quick wins"), high value/high effort ("major projects"), etc. No single inventor. |

### Which Survive AI-Native Velocity? Does "Effort" Break When AI Compresses It Unpredictably?

The most direct primary-source treatment is [IdeaPlan's "How to Prioritize AI Features When RICE Breaks" (Apr 2026)](https://www.ideaplan.io/blog/how-to-prioritize-ai-features): `[SECONDARY]`

> *"AI features violate all three [RICE] assumptions. The same input can produce different outputs. Going from 80% to 90% accuracy can take 10× the effort of reaching 80% in the first place. And confidence is nearly impossible to benchmark against historical data when you are shipping something your team has never built before."*

The breakdown of each RICE dimension in AI contexts:
- **Reach:** AI features have *gradient availability* (e.g., GitHub Copilot available to all developers but useful only to those using supported languages/IDEs). Actual reach ≠ user base.
- **Impact:** Probabilistic, not binary. Impact depends on model accuracy, hallucination rate, and user tolerance — all of which vary.
- **Confidence:** Circular in AI: you calibrate against comparable past work, but novel AI features have no comparable past work.
- **Effort:** Non-linear. First prototype: 1 week. To 80% accuracy: 1 month. To 95% accuracy: 6 months. [Lenny Rachitsky's research across 50+ AI implementations](https://www.ideaplan.io/blog/how-to-prioritize-ai-features) finds this non-linear pattern is "nearly universal."

**[VentureBeat (Aug 2025)](https://venturebeat.com/ai/how-ai-product-teams-are-rethinking-impact-risk-feasibility) proposes ARISE** (AI Readiness, Impact, Scoring Evaluation): `[SECONDARY]`
```
ARISE = (Reach × Impact / Effort) × AI Desire × AI Capability × Intent Multiplier
```
The new dimensions: AI Desire (does solving this with AI add value?), AI Capability (data readiness + model maturity + ops overhead), Intent (autonomous vs. assistive).

**Dr. Marily Nika (former Google/Meta AI PM) proposes RICE-A**: `[SECONDARY]`
```
RICE-A = (Reach × Impact × Confidence) / (Effort × AI Complexity × 0.5)
```
AI Complexity is scored on data readiness (40%), model maturity (35%), and operational overhead (25%).

**What survives:**
- **Kano** survives best — it doesn't require effort estimation and maps directly onto product positioning questions (is this AI feature a Basic, Performance, or Excitement feature for users?). The Kano insight that today's Excitement features become tomorrow's Basic features is especially relevant for AI features that are rapidly commoditizing.
- **MoSCoW** survives as a communication tool, not a scoring framework — it is too coarse for daily-ship decisions but useful for stakeholder alignment.
- **WSJF** partially survives because its Cost-of-Delay concept (the economic cost of *not* shipping something) is more robust to AI uncertainty than effort-based scores.

**What fails:**
- **RICE and ICE** fail when applied to AI features because effort and confidence assumptions collapse. They remain useful for non-AI feature prioritization within AI-native teams.
- **Value-Effort 2×2** fails because "effort" is undefined when AI tools can compress delivery unpredictably — a "hard" task one week becomes "trivial" the next.

### How Do Every, Anthropic, Cursor, Linear, Stripe Prioritize in 2025–2026?

**Linear** (most documented): As described by [CEO Karri Saarinen in Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-linear-builds-product): `[PRIMARY]`
- No scoring frameworks.
- Leadership + team spend time with customers + use the product regularly → needs become apparent.
- Sequencing based on: which project supports another, who on the team is best suited, what the strategy is.
- Zero story points, zero sprint planning.
- In March 2026, Linear [declared issue tracking "dead"](https://departmentofproduct.substack.com/p/linear-says-issue-tracking-is-dead) and launched Linear Agent, shifting the prioritization model from issue-based to context-and-agent-based. `[SECONDARY]`

**Cursor (Anysphere):** CEO Michael Truell at Fortune's AI Brainstorming conference (December 2025) described a strategy built on product-specific models, superior UX, and enterprise features — not a public prioritization framework. The implicit model: [ship the features that best serve the developer workflow and enterprise integration stack](https://www.artezio.com/pressroom/blog/powered-development-compete/), with model development prioritized by feedback loops from production usage. `[SECONDARY]`

**Every.to:** [A Feb 2026 Lenny's Newsletter piece by Every.to's Tal Raviv and Aman Khan](https://www.lennysnewsletter.com/p/how-to-build-ai-product-sense) describes their prioritization approach: use Cursor and Claude Code as daily *strategy, prioritization, and decision-making* tools — not just coding aids. *"We now spend our days using Cursor and Claude Code for daily work: strategy, prioritization, decision-making, data analysis, and productivity."* No formal framework cited. `[SECONDARY]`

**Anthropic:** The [Anthropic PM interview guide (2026)](https://www.interviewquery.com/interview-guides/anthropic-product-manager) reveals their PM mental model: prioritize between capability work and safety improvements, design metrics capturing both user value and risk reduction, steer roadmaps per Responsible Scaling Policy. Framework: *"Problem, Users, Hypotheses, Constraints, Risks, Metrics, MVP, Next steps"* — a hybrid of JTBD and Cagan's four risks. No public scoring framework. `[SECONDARY]`

**Stripe:** [Sessions 2025 keynote (May 2025)](https://stripe.com/blog/top-product-updates-sessions-2025) describes product decisions organized around four core areas (Payments, Connect, Revenue, Money Management) with AI applied across all. No public prioritization framework beyond Stripe's historical customer-first, API-first philosophy. `[PRIMARY]`

### Top 5 References

1. [IdeaPlan, "How to Prioritize AI Features When RICE Breaks," Apr 2026](https://www.ideaplan.io/blog/how-to-prioritize-ai-features) `[SECONDARY]`
2. [VentureBeat, "How AI Product Teams Are Rethinking Impact, Risk, Feasibility," Aug 2025](https://venturebeat.com/ai/how-ai-product-teams-are-rethinking-impact-risk-feasibility) `[SECONDARY]`
3. [Lenny's Newsletter, "How Linear Builds Product," Sep 2023](https://www.lennysnewsletter.com/p/how-linear-builds-product) `[PRIMARY]`
4. [PMI, "Improving WSJF," Jul 2024](https://www.pmi.org/disciplined-agile/improving-wsjf) `[SECONDARY]`
5. [Growthmethod.com, "ICE Framework: The Original Prioritisation Framework," Mar 2026](https://growthmethod.com/ice-framework/) `[SECONDARY]`

### 5–10 Key Findings

1. RICE fails for AI features because all four dimensions (Reach, Impact, Confidence, Effort) break under AI-specific conditions: gradient reach, probabilistic impact, circular confidence, non-linear effort. ([IdeaPlan, Apr 2026](https://www.ideaplan.io/blog/how-to-prioritize-ai-features)) `[SECONDARY]`
2. AI accuracy non-linearity is the most dangerous RICE assumption break: last-mile improvement (80%→95%) can cost 10× more than first-mile (0%→80%). ([IdeaPlan, Apr 2026](https://www.ideaplan.io/blog/how-to-prioritize-ai-features)) `[SECONDARY]`
3. RICE-A (Marily Nika) and ARISE (VentureBeat) both add AI-specific complexity dimensions but retain RICE's core structure — they are adaptations, not replacements. `[SECONDARY]`
4. Linear uses zero scoring frameworks, zero story points, and zero A/B tests — and has reached $1.25B valuation with 2 PMs. Their model: customer proximity + taste-driven sequencing. ([Lenny's Newsletter, Sep 2023](https://www.lennysnewsletter.com/p/how-linear-builds-product)) `[PRIMARY]`
5. Kano's categorization (Basic / Performance / Excitement / Indifferent / Reverse) is the most AI-stable prioritization lens because it does not require effort estimation. `[SECONDARY]`
6. WSJF's Cost-of-Delay concept survives AI compression because it asks "what is the economic cost of *not* doing this now?" — independent of delivery speed. `[SECONDARY]`
7. The 80% AI project failure rate (RAND Corp) and 60% abandonment rate (Gartner predicts, by end of 2026) are attributed to teams using traditional prioritization frameworks that miss AI-specific failure modes. ([IdeaPlan, Apr 2026](https://www.ideaplan.io/blog/how-to-prioritize-ai-features)) `[SECONDARY]`
8. At compound engineering velocity (multiple daily ships), prioritization frameworks function as *direction-setting tools*, not per-feature scoring — the real question is which problem space to focus on, not which feature to build next. `[ANECDOTE]`

### How the Methodology Fails or Adapts in AI-Native Teams

**Adapts well:**
- Kano: framework-agnostic on delivery speed; directly applicable to AI feature classification.
- WSJF's Cost of Delay: the question "what does it cost to not do this?" remains relevant independent of AI.
- MoSCoW as a stakeholder communication tool for resource-constrained solo founders.

**Fails (structural mismatch):**
- All scoring frameworks require effort estimation, which is meaningless when AI can compress or expand delivery unpredictably.
- All frameworks assume relatively stable competitive environments; in AI product development, a capability that was "unfeasible" last month may be trivial this month.
- Confidence scoring requires comparable historical data, which AI-native teams building first-of-kind features do not have.

### Gaps / Uncertainty

- No primary-source documentation of formal prioritization frameworks used at Anthropic, Every.to, or Cursor.
- No empirical comparison of RICE-A vs. ARISE vs. taste-driven approaches in AI-native teams.
- MoSCoW's origin and evolution beyond 1994 SAFe adoption is poorly documented in primary sources.
- The relationship between prioritization frameworks and compound engineering's specific "Plan" phase has not been formally analyzed.

---
## Sub-domain G — Product-Led Growth (PLG)

### Top 5 Primary References

1. [**Wes Bush, *Product-Led Growth: How to Build a Product That Sells Itself*, 2019**](https://productled.com/book/product-led-growth) [PRIMARY, foundational — verify 2026 relevance] — Introduced PLG as a GTM strategy where the product is the primary acquisition, activation, and retention vehicle. Core frameworks: MOAT (Market Strategy, Ocean type, Audience, Time-to-value), UCD (Understand/Communicate/Deliver value), Bowling Alley (path to aha moment).

2. [**Kyle Poyar, "How the top AI-native startups launch and grow," *Growth Unhinged*, March 2026**](https://www.growthunhinged.com/p/ai-native-org-report-part-one) [PRIMARY] — Multi-founder qualitative study showing AI-native companies reach $1M ARR in half the time of traditional SaaS; PLG motions are standard but hybrid self-serve + sales-assisted has become the winning pattern by $2–5M ARR.

3. [**Kyle Poyar, "The AI-Native Growth Team," *Growth Unhinged*, March 2026**](https://www.growthunhinged.com/p/the-ai-native-growth-team) [PRIMARY] — Fyxer case study: 4-engineer team ran 514 growth experiments in 12 months using Claude Code, Codex, and MCPs; scaled $1M→$30M ARR with credit-card gating flipping conversion from 5% to 35%.

4. [**OpenView Partners PLG Benchmark Guide (Kyle Poyar)**](https://openviewpartners.com/blog/your-guide-to-product-led-growth-benchmarks/) [PRIMARY, 2022 — verify 2026 relevance] — Established canonical PLG funnel benchmarks: Discover → Start → Activate → Convert → Scale. Activation 20–40% normal; freemium converts 5%, free trial 17%.

5. [**Extruct.ai, "The State of PLG in 2025"**](https://www.extruct.ai/research/plg2025/) [SECONDARY] — Dataset of 474 Series A startups: 39% enable PLG/self-serve; DevTools 50% PLG. Key PLG readiness test: can a new user reach unmistakable value in under 30 minutes without human help?

### 5–10 Key Findings

**Finding 1 — PLG is the baseline, not the differentiator.**  
[Per Segment8's 2025 data](https://blog.segment8.com/posts/top-20-product-led-growth-stats-2025/), PLG adoption grew from 45% (2019) to 55% (2022–2024). [ProductLed's 2026 PLG predictions report](https://productled.com/blog/plg-predictions-for-2026) notes that Menlo Ventures' 2025 State of AI found 27% of all AI application spend comes through PLG motions. PLG is now table stakes; the moat is GTM execution, data, and workflow integration.

**Finding 2 — AI-native PLG companies reach PMF and revenue faster but face harsh renewal cliffs.**  
[Poyar's 2026 report](https://www.growthunhinged.com/p/ai-native-org-report-part-one) documents median time to $1M ARR at 12 months (vs. ~24 months for traditional SaaS). Bolt.new: $4M ARR in 4 weeks. However, the first major renewal cycle (18–24 months post-launch) is when vibe revenue collapses. [Per ProductLed 2026](https://productled.com/blog/plg-predictions-for-2026): "2024–2025 saw explosive land-and-expand. But 2026 is when the music stops for many AI companies hitting their first major renewal cycles."

**Finding 3 — Credit-card gating is the highest-leverage PLG lever for AI products.**  
[Fyxer case study (Poyar, March 2026)](https://www.growthunhinged.com/p/the-ai-native-growth-team): CC gating converted 5%→35% free-to-paid; overall paying customers doubled despite signup dip. The trial period 7 days outperformed 3 and 28 days overall; 14 days worked best for personal users.

**Finding 4 — AI products require explicit quality metrics as the leading indicator of PLG health.**  
[Poyar's AI-native org report](https://www.growthunhinged.com/p/ai-native-org-report-part-one) documents four AI quality measurement patterns: (a) explicit signals (thumbs up/down — Gamma uses this), (b) implicit signals (edit intensity, send rate — Fyxer: 20% of AI responses copied), (c) adoption signals (DAU:MAU, messages per DAU — Bolt), (d) business impact (resolution rate, automation rate, FTEs augmented — Intercom Fin.ai). Quote: "If the AI quality is there, people will keep using it. This is the most important metric and a leading indicator for us. But AI quality is very hard to measure and it's subjective." — Joshua Xu, HeyGen co-founder.

**Finding 5 — PLG 2.0 is AI-personalized onboarding at the moment of need.**  
[Per salespanel.io 2025 PLG analysis](https://salespanel.io/blog/marketing/what-is-product-led-growth/) and [growthmates.news 2025 review](https://www.growthmates.news/p/plg-2025-rewind-biggest-trends-and): AI copilots and adaptive onboarding became standard in B2B SaaS by 2025. Notion now rebuilds its UI based on observed writing and collaboration patterns. Time-to-value target has compressed from "under 5 minutes" to "under 60 seconds" for best-in-class AI products.

**Finding 6 — Hybrid PLG + sales-assisted beats pure self-serve for AI products at scale.**  
[Poyar 2026 AI-native org report](https://www.growthunhinged.com/p/ai-native-org-report-part-one): Half of AI-native startups started self-serve; median first AE hire at $2–5M ARR (vs. ~$1M for SaaS). HeyGen and Gamma waited until $10M+ ARR. Only 1/interviewed companies remained primarily self-serve; 3/4 combined self-serve + sales-assisted. Quote (bolt.new COO): "The paradox is that to get maximum value out of the tool, we actually need to engage in more of a top-down or traditional enterprise sale."

**Finding 7 — AI product pricing must account for real COGS.**  
[ProductLed 2026](https://productled.com/blog/plg-predictions-for-2026): "The old SaaS playbook of 'generous free tier forever' doesn't work when free users burn cash." Gamma's A/B test: $20/month (double conventional productivity app) outperformed lower tiers. [Poyar, Wes Bush on PLG for AI (Nov 2025)](https://productled.com/blog/become-a-10x-plg-practitioner-using-ai-7-real-workflow-examples): "AI introduces real COGS, so pricing and packaging often need to evolve toward outcome-based, usage-based, or seats-with-overages models."

**Finding 8 — Aha-moment/activation metrics for AI products are output-quality focused, not feature-adoption focused.**  
Traditional activation is "user completes action X." AI product activation is: "user receives output of sufficient quality that they would miss the product if it disappeared." [Poyar's AI-native org report](https://www.growthunhinged.com/p/ai-native-org-report-part-one): GC AI's metric — "23% of people who took our classes paid for the product." Intercom Fin.ai: 23–24% ticket resolution rate as initial quality threshold before investing in growth.

### PLG Failures/Adaptations in AI-Native Contexts

- **PLG activation fails when AI quality is below reliability threshold.** Expensive acquisition + poor AI quality = leaky bucket. The "ability debt" concept from Bush (users fail to accomplish key outcome) maps directly: AI ability debt = model consistently fails at core job-to-be-done.
- **Vibe coding democratized building; this destroys code-based moats.** [ProductLed 2026](https://productled.com/blog/plg-predictions-for-2026): "Building is easy, defensibility is hard. AI makes product development cheap. That means everyone can build. Your moat isn't your code anymore. It's your GTM, your data, your workflow integration, and your brand." This is an existential challenge to PLG strategies that rely on product complexity as a switching cost.
- **Pure self-serve breaks down for AI products requiring behavioral change.** Forward-deployed engineers / GTM-as-consulting has emerged as the new PLG complement for AI products with complex integrations, per [Poyar 2026](https://www.growthunhinged.com/p/ai-native-org-report-part-one).

### 2024–2026 Critiques of PLG from Named Practitioners

- **Greg Isenberg, Feb 2026:** Introduced "vibe revenue" — "money coming from customers who are paying out of curiosity, novelty, or FOMO rather than because a product solves a genuine, persistent problem." [Isenberg's full definition](https://www.gregisenberg.com/blog/vibe-revenue): hallmarks include high initial conversion, poor retention past 3–6 months, limited expansion, high sensitivity to alternatives. Isenberg: "We're probably 18 months away before we start seeing a bunch of zombie companies." [SECONDARY, practitioner — strong signal]
- **Alexander Berger (COO, bolt.new) via Poyar:** "SaaS was steady and you had time to build up your GTM force. Now there's a big mismatch on the pace." Standard PLG playbooks assume time to optimize; AI markets move too fast for gradual PLG iteration.
- **James Colgan, "PLG is Dead. Long Live PLG" (Aug 2025):** [SECONDARY] "The products that scale in the AI-native world will be the ones that act like partners, not platforms." Time-to-value must be instant; PLG 1.0 onboarding is too slow for AI-era user expectations.

### Gaps

- No primary-source data from Cursor, Linear, or Notion on specific AI product activation metrics (2025–2026 precision data).
- OpenView's canonical PLG benchmarks predate the AI wave; 2025–2026 updates are fragmented across secondary sources.
- No sourced framework specifically for PLG in a solo-founder AI-native context.

---

## Sub-domain H — Category Design (Play Bigger)

### Top 5 Primary References

1. [**Ramadan, Peterson, Lochhead, Maney, *Play Bigger*, 2016**](https://www.categorydesignadvisors.com/play-bigger/) [PRIMARY, foundational — verify 2026 relevance] — Defined category design as a discipline of creating and monetizing new markets. Core insight: "76% of market cap goes to the dominant Category King." Key tools: Magic Triangle (product + company + category designed simultaneously), Point of View (POV), Lightning Strikes, Category Blueprint.

2. [**Christopher Lochhead, Category Pirates newsletter**](https://www.categorypirates.news/p/stop-teaching-start-transforming) [PRIMARY] — Active 2025 publication. Lochhead/Peterson evolved the teaching to include AI as transformation business by Q4 2025: "AI doesn't support the transformation business. AI is the transformation business." Category Design Academy ($10K/cohort) and AI-native bot products as category examples.

3. [**Play Bigger, "Category Design: A Voyage Toward Belief," March 2026**](https://www.playbigger.com/media/category-design-a-voyage-toward-belief) [PRIMARY] — A decade-post *Play Bigger* reflection. Introduces updated category discovery pattern: Context (technology/regulation/behavior change) + Missing (something important becomes absent) + Innovation (fills the gap) = new category. Frames category design as belief formation: "Before a new market exists, a new belief must take hold — inside the company first, then the market."

4. [**Play Bigger, "What is Category Design?"**](https://www.playbigger.com/categorydesign) [PRIMARY] — Full methodology: Identify Problem → Solution & Category Name → Blueprint & Ecosystem → POV → Internal Mobilization → Lightning Strike Execution → Strike Ops Flywheel. Math: Category potential = Problem × People affected.

5. [**TechCrunch, "How Sierra is rethinking customer experience in the age of AI," Feb 2024**](https://techcrunch.com/2024/02/19/sierra-ai-agents-customer-service/) [PRIMARY] — Sierra's Bret Taylor articulates the category creation thesis: "Conversational AI will become the dominant form factor that people use to interact with brands." Category name: "AI agents for CX." This is textbook Lightning Strike category creation by a credentialed founder.

### 5–10 Key Findings

**Finding 1 — Category Kings capture 76% of total market capitalization.**  
[Play Bigger (foundational)](https://www.playbigger.com/categorydesign): Supported by Harvard Business Review peer-reviewed research. The implication for AI-native founders is that being second in a new AI category is economically close to losing.

**Finding 2 — The Magic Triangle: product, company, and category must be designed simultaneously.**  
[Lochhead in *Marketing Journal* interview (2016)](https://www.marketingjournal.org/play-bigger-an-interview-with-christopher-lochhead/): "Savvy technology entrepreneurs, founders and CEOs are proactive about designing their product, their company AND their category at the same time." This is the core discipline of category design vs. positioning.

**Finding 3 — Snowflake, Salesforce, and HubSpot are canonical category design success cases.**  
[YouTube category design breakdown (Dec 2025)](https://www.youtube.com/watch?v=PeAPT7JXArQ): Salesforce invented "cloud-based CRM" and moved the market away from on-premise software. HubSpot invented "inbound marketing" to contrast with interruptive digital marketing; made "Inbound" the name of their conference. Snowflake named itself the "Data Cloud" — elevated from database to cloud data platform category. Each defined the problem before naming the solution.

**Finding 4 — Sierra is the clearest 2024 example of AI-native category creation.**  
[TechCrunch, Feb 2024](https://techcrunch.com/2024/02/19/sierra-ai-agents-customer-service/): Bret Taylor and Clay Bavor positioned Sierra not as a chatbot or customer service software, but as a new category: "AI agents for CX" — autonomous agents that represent a brand in customer interaction, distinct from ticketing software, scripted chatbots, and CRM. Their Lightning Strike strategy: reframe the problem ("every customer experience will be AI-agent-first") before leading with the product.

**Finding 5 — 2025 update: Category Design has evolved toward belief formation.**  
[Play Bigger, March 2026](https://www.playbigger.com/media/category-design-a-voyage-toward-belief): "Markets are powered by belief systems. Before a new market exists, a new belief must take hold — inside the company first, then the market." This extends the original book's framework: the internal POV/belief must be real and coherent before any external Lightning Strike will land.

**Finding 6 — Category Pirates made a 2025 strategic pivot: teaching vs. transformation.**  
[Category Pirates, Dec 2025](https://www.categorypirates.news/p/stop-teaching-start-transforming): Lochhead and Peterson "burned it all down to the studs" in 2025 and separated into two models — teaching (newsletter) and transformation (Academy + AI bots). They used category design on themselves: "AI doesn't support the transformation business. AI is the transformation business." This is a live example of AI-native productized services category design.

**Finding 7 — Category design for AI-native consulting/productized services follows the same playbook.**  
The pattern: (1) Name the missing — "you need AI transformation, not AI tools." (2) Name the category — "AI operations" / "AI-native studio" / "compound engineering consultancy." (3) Design the Lightning Strike — a public framework (e.g., Compound Engineering at every.to) creates intellectual property that anchors the category. Every Inc. is an unreferenced but structurally strong example: they named "compound engineering" and are executing Lightning Strikes via public guides, YouTube, and GitHub plugins.

**Finding 8 — Category creation before PMF is a trap.**  
[Per Play Bigger's own methodology](https://www.playbigger.com/categorydesign): Category design requires credibility + product + POV aligned. Solo founders who attempt Lightning Strike category naming before achieving PMF typically confuse the market rather than educating it. The category must be felt as real by early customers before it can be broadcast.

### Category Design Failures/Adaptations

- **AI creates category compression.** Dozens of companies name the same AI category simultaneously. The "new-belief-first" principle from the March 2026 Play Bigger update is the differentiator: you win by having the most compelling internal conviction + the most coherent POV, not by being loudest.
- **The 6–10 year category lifecycle is compressed in AI.** Snowflake spent years building the Data Cloud category. AI categories form and collapse in 12–24 months. This requires faster Lightning Strike cadence.
- **Premature category naming is a common failure mode** (see D4 product traps). "AI agents for X" is now noise; specificity of problem + audience is the new differentiator.

### Gaps

- No primary-source data on whether category design explicitly accounts for AI capability commoditization (today's category leader can be upended in months).
- Lochhead has not published a framework specifically for AI-native categories in 2025–2026 beyond the $10K cohort (not publicly accessible for primary-source citation).
- No case study data on whether the "76% market cap to Category King" rule holds for AI software categories given the speed of capability parity.

---

## Sub-domain I — Emerging 2024–2026 AI-Native Product Practices

### Top 5 Primary References

1. [**Andrej Karpathy, "vibe coding" concept, February 2025**](https://www.klover.ai/andrej-karpathy-vibe-coding/) [PRIMARY] — Karpathy coined "vibe coding" in February 2025 to describe code generation via natural language where the developer "fully gives in to the vibes, embraces exponentials, and forgets that the code even exists." His original framing was for "throwaway weekend projects." By December 2025, Y Combinator reported 25% of W25 batch companies had codebases that were 95% AI-generated.

2. [**Hamel Husain, "LLM Evals: Everything You Need to Know," hamel.dev, January 2026**](https://hamel.dev/blog/posts/evals-faq/) [PRIMARY] — Comprehensive eval guide synthesizing Husain's course work with 700+ engineers and PMs. Definitive position: "Should I practice eval-driven development? Generally no." Correct approach: error analysis → write evaluators for errors discovered, not imagined. "In the projects we've worked on, we've spent 60–80% of our development time on error analysis and evaluation."

3. [**Hamel Husain, "A Field Guide to Rapidly Improving AI Products," hamel.dev, March 2025**](https://hamel.dev/blog/posts/field-guide/) [PRIMARY] — Core principle: "Your AI roadmap should count experiments, not features. The key metric for AI roadmaps isn't features shipped — it's experiments run." Explicitly addresses PM role: "The most successful teams flip this model by giving domain experts tools to write and iterate on prompts directly" (rather than PM-to-engineer handoff). Teams with thoughtfully designed data viewers "iterate 10x faster than those without them."

4. [**Shreyas Doshi, "Why Product Sense is the only product skill that will matter in the AI age," March 2026**](https://shreyasdoshi.substack.com/p/why-product-sense-is-the-only-product) [PRIMARY] — Core argument: AI tools commoditize; the long-term PM moat is product sense (empathy, simulation, strategic thinking, taste, creative execution) applied on top of AI outputs. "Product Sense isn't one power among seven. It's the generative capability behind most of the seven. The powers are outcomes. Product Sense is the input."

5. [**Kevin Weil (CPO, OpenAI) statement via Peter Yang / Aman Khan, January 2025**](https://creatoreconomy.so/p/ai-skill-that-will-define-your-pm-career-aman-khan) [PRIMARY, ANECDOTE] — "Writing evals is going to become a core skill for product managers. It is such a critical part of making a good product with AI." CPOs of both OpenAI and Anthropic named AI evaluations as the most important PM skill for 2025.

### 5–10 Key Findings

**Finding 1 — "Vibe coding" has bifurcated into discovery-mode and production-mode.**  
[Every.to's Compound Engineering guide](https://every.to/guides/compound-engineering) explicitly encodes this: "Vibe coding is for people who don't care about the code itself — they want results. Maybe you're a product manager prototyping ideas." But the guide also states: "Delete everything and start over with a proper plan. The prototype is for learning only, not shipping." Karpathy's original framing has been productized into a discovery methodology: vibe code to explore, spec to build.

**Finding 2 — "Prompt-first PM" is not yet a named movement with a canonical primary source.**  
A search of primary sources (every.to, producttalk.org, lennysnewsletter.com, aakashg.com) in 2024–2026 finds no named "prompt-first PM" framework. The adjacent practices that exist: Hamel Husain's "give domain experts direct prompt-writing tools" [Field Guide, March 2025]; Aakash Gupta's "Context Engineering for PMs" (listed in his 2025 AI PM curriculum); Every.to's vibe coding section for PMs. The practice exists without a unified name. [ADMITTED UNCERTAINTY: "prompt-first PM" as a formal movement — no primary source found as of April 2026.]

**Finding 3 — Eval-driven development (strict TDD-style) is explicitly advised against by the leading practitioner.**  
[Hamel Husain, hamel.dev, 2026](https://hamel.dev/blog/posts/evals-faq/): "Eval-driven development (writing evaluators before implementing features) sounds appealing but creates more problems than it solves. Unlike traditional software where failure modes are predictable, LLMs have infinite surface area for potential failures." The correct practice is error-analysis-first: look at actual outputs → identify failure modes → write targeted evaluators.

**Finding 4 — AI evaluations are the new unit tests — a core PM skill, not just an engineering skill.**  
[Kevin Weil / Aman Khan interview, Jan 2025](https://creatoreconomy.so/p/ai-skill-that-will-define-your-pm-career-aman-khan): "Evals force you to get into your user's shoes. You can no longer just hypothesize." [Sid Saladi, Substack Sept 2025](https://sidsaladi.substack.com/p/why-every-pm-needs-to-master-ai-evals): "Writing good AI evals forces you to translate fuzzy human preferences into precise, measurable criteria. That's literally the core of great product management." Hamel's course has 3,000+ students from 500+ companies including OpenAI, Anthropic, Google (as of Jan 2026).

**Finding 5 — AI product roadmaps should be organized by experiments, not features.**  
[Hamel Husain Field Guide, March 2025](https://hamel.dev/blog/posts/field-guide/): "Your AI roadmap should count experiments, not features." GitHub Copilot example: "The team invested heavily in building sophisticated offline evaluation infrastructure... with solid evaluation in place, the team ran thousands of experiments." [Aman Khan, Peter Yang interview, Jan 2025]: "The waterfall process of writing a PRD and handing it to designers and engineers no longer works. The development cycle needs to be much shorter, like clock cycles in a GPU."

**Finding 6 — Ravi Mehta: PM work has shifted from 50/50 discovery/delivery to 90/10.**  
[Ravi Mehta, Atlassian blog, Dec 2025](https://www.atlassian.com/blog/artificial-intelligence/shift-from-craft-to-judgement-ai): "It used to be fifty-fifty. Half the challenge was building well, half was deciding what to build. Now it's more like ninety-ten. The building gets easier. The real differentiator is judgment." Mehta's framework: AI moves at AI speed (spec writing, prototyping, data analysis); discovery and strategy move at human speed. "For PMs who want to set themselves apart, focus on the areas that still move at human speed — customer discovery, product sense, and strategy."

**Finding 7 — Shreyas Doshi: Product Sense is the only non-commoditizable PM skill in the AI age.**  
[Doshi, March 2026](https://shreyasdoshi.substack.com/p/why-product-sense-is-the-only-product): Five components of Product Sense that AI cannot replicate: (1) strong empathy (figuring out what people need beyond what AI has analyzed), (2) excellent simulation skills, (3) stellar strategic thinking, (4) taste, (5) creative execution. "The long-term career moat for product people is how you can improve on the already-brilliant, already-comprehensive inputs and outputs that AI will provide for you."

**Finding 8 — Lenny Rachitsky 2025: "Proto-manager" is replacing traditional PM documentation culture.**  
[Lenny's Newsletter Best of 2025](https://www.lennysnewsletter.com/p/best-of-lennys-newsletter-2026): Top AI content included "A guide to AI prototyping for product managers—How to turn your idea into a working prototype in minutes" and "Make product management fun again with AI agents." [Every.to podcast on AI PM, Aug 2025](https://every.to/podcast/best-of-the-pod-she-built-an-ai-product-manager-bringing-in-six-figures-as-a-side-hustle): Claire Silver's framework: "The ratio of PMs to builder roles is going to shift pretty dramatically, increasing from 1:7 to about 1:20." She introduces "proto-manager" — "expected to build prototypes instead of building documents."

**Finding 9 — Peter Yang: AI-native PMs operate at 5 levels; level 4+ involves building agents.**  
[Peter Yang, LinkedIn, Feb 2026](https://www.linkedin.com/posts/petergyang_how-to-become-ai-native-in-5-levels-activity-7427373376287055872-ZGoZ): AI-native progression: (1) Everyday answers → (2) Daily work → (3) Prototyping → (4) Building apps → (5) Personal agents. Level 4–5 is where PMs gain structural advantage over AI-unaugmented peers.

**Finding 10 — Aakash Gupta 2025: AI PM curriculum covers Context Engineering, Evals, Agents, Vibe Experimentation.**  
[Gupta's 2025 AI PM roadmap](https://www.news.aakashg.com/p/ai-pm-learning-roadmap) mapped 90 newsletter deep-dives into a complete AI PM MBA. Key emerging topics: Context Engineering for PMs, AI Evals (everything you need to know), LLM Judge for AI PMs, "Vibe Experimentation." These represent the frontier curriculum for 2025–2026 AI product managers.

### Fails/Adaptations

- **The traditional PRD → handoff → build waterfall is functionally obsolete** for AI features. Aman Khan (Arize) explicitly: "The waterfall process of writing a PRD and handing it to designers and engineers no longer works." Adaptation: continuous experiment loop replaces stage-gate delivery.
- **AI-synthesized user patterns carry hallucination risk.** Hamel's insistence on "look at your data" (real traces, real failures) is a direct counter to the temptation to use AI to synthesize patterns from user data without human validation. This is a new product trap.

### Gaps

- "Prompt-first PM" lacks a canonical 2025–2026 primary source — the practice is real but not yet crystallized into a named framework.
- No primary data on how companies like Linear or Notion specifically structure PM evals processes internally.

---

## Sub-domain J — Compound Engineering × PM Synthesis *(MOST IMPORTANT)*

### What is the PM's role in a Compound Engineering team?

**Primary definition from the source:** [Kieran Klaassen and Dan Shipper, "Compound Engineering: How Every Codes With Agents," every.to, December 2025 (updated April 2026)](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents):

> "The principles extend beyond engineering to design, research, or even writing—any discipline where codifying taste and context help make future work go faster and easier. The steps are the same: Plan, execute, review, compound."

This is the only explicit CE statement about non-engineering roles in the primary source. The CE framework does not yet have a canonical published definition of the PM role within it.

[Every.to's Compound Engineering guide](https://every.to/guides/compound-engineering) identifies PM-adjacent functions:
- **Vibe coding for PMs:** "Vibe coding is for people who don't care about the code itself — they want results. Maybe you're a product manager prototyping ideas."
- **User research → data pattern extraction → feature decisions:** Explicit flow from usage pattern observation to product decisions, described as the engineer/PM function.
- **UX discovery loop:** "Generate multiple versions → click through each one → share with users → collect feedback on functional prototypes → delete everything and start over with a proper plan."

The CE framework's implicit PM role is: **the person who defines what to build (the plan input) and validates whether what was built is correct (the review criteria).**

### The Three CE Rules Applied to Product Work

**80/20 Rule applied to product:**  
[Klaassen/Shipper, every.to guides](https://every.to/guides/compound-engineering): "The plan and review steps should comprise 80 percent of an engineer's time, and work and compound the other 20 percent. In other words, most thinking happens before and after the code gets written." Applied to PM: 80% of product effort should be in defining requirements precisely enough for agents to execute, and reviewing whether the output matches the intent — not in execution itself.

This maps directly to [Ravi Mehta's 90/10 reframe (Atlassian, Dec 2025)](https://www.atlassian.com/blog/artificial-intelligence/shift-from-craft-to-judgement-ai): "It used to be fifty-fifty. Half the challenge was building well, half was deciding what to build. Now it's more like ninety-ten."

**50/50 Rule applied to product:**  
[Every.to CE guide](https://every.to/guides/compound-engineering): "When you look at your broader responsibilities as a developer, you should allocate 50 percent of engineering time to building features, and 50 percent to improving the system — in other words, any work that helps build institutional knowledge rather than shipping something specific." For a PM in a CE team, this translates: 50% of PM time should produce direct product output (specs, user research synthesis, prioritization decisions); 50% should produce system improvements — improved eval suites, codified taste/judgment, updated OSTs (Opportunity Solution Trees), compound-ledger entries.

**$100 Rule applied to product:**  
The $100 rule is **not found in any publicly accessible Every Inc. / CE primary source as of April 2026**. It is mentioned in the task context but was not located in every.to, hamel.dev, or other primary sources reviewed. [ADMITTED UNCERTAINTY: This rule is attributed in the task briefing but no primary citation found. Do not cite as sourced CE canon.]

The closest adjacent concept in CE is the "compound step" philosophy: any manual review activity you'd pay $100 to automate (e.g., reviewing code for security issues, writing test cases) should be codified into a review agent. Applied to product: any PM task repeated more than N times at significant cognitive cost (e.g., manually synthesizing user interview notes, writing the same types of PRD sections) should be prompted-and-codified into a reusable agent or template.

### Who Has Written Explicitly About PM Role in CE Teams (2024–2026)?

**Direct primary sources on CE + PM synthesis are thin.** The following are the closest sourced approximations:

1. [**Hamel Husain, Field Guide, March 2025:**](https://hamel.dev/blog/posts/field-guide/) "The most successful teams flip this model by giving domain experts tools to write and iterate on prompts directly." In a CE context, the PM is the domain expert who should own prompt iteration, not just hand requirements to engineers. This is the most actionable published CE-PM synthesis statement.

2. [**Claire Silver via Every.to podcast, August 2025:**](https://every.to/podcast/best-of-the-pod-she-built-an-ai-product-manager-bringing-in-six-figures-as-a-side-hustle) "The ratio of PMs to builder roles is going to shift pretty dramatically, increasing from 1-to-7 to about 1-to-20." This implies PMs in CE environments own more surface area but with AI-augmented leverage.

3. [**Dan Shipper via Lenny Rachitsky, July 2025:**](https://www.lennysnewsletter.com/p/inside-every-dan-shipper) Every runs 5 products — Cora, Monologue, Sparkle, Spiral, every.to — with "primarily single-person engineering teams." With 15 people total. This implies the PM function is either collapsed into the engineer-GM role (Klaassen is "General Manager of Cora") or distributed across writing and product roles.

4. [**Will Larson, "Learning from Every's Compound Engineering," lethain.com, January 2026:**](https://lethain.com/everyinc-compound-engineering/) Provides a structural critique: "Compound is asking the agent to summarize its learnings from a given task into a well-defined, structured format (basically a wiki) which is consulted by future iterations of the plan pattern." This is the "compound-ledger" mechanism — the PM's role in maintaining and curating this institutional knowledge base is implicit but unspecified.

### Do AI-Native Companies Have Traditional PMs? (Job Posting Evidence)

**Cursor:** [Cursor careers page (April 2026)](https://cursor.com/careers) lists no product manager roles. Open roles: sales, research scientist, user ops, growth. Cursor appears to not have traditional PMs as of April 2026. This is consistent with an engineering-led CE-style organization. [PRIMARY]

**Every Inc.:** [Every careers page (April 2026)](https://every.to/careers) lists no product manager roles. Open: GTM Engineer, Head of AI Education, Head of Business Development, Head of Finance Vertical (consulting), Head of Social, Lead Instructor. Product management appears embedded in the GM/founder roles. [PRIMARY]

**Anthropic:** [Active PM job postings found (2025–2026)](https://www.anthropic.com/careers/jobs/5021316008): Lead Product Manager, Developer Services (April 2026); Product Manager, Consumer Growth (2025); Product Operations Manager (2026). Anthropic has traditional PMs. The Lead PM Developer Services JD emphasizes: "Drive product-led growth initiatives," "coordinate evaluations, red-team feedback, and post-launch learning loops so improvements compound over time," "establish metrics and success criteria." [PRIMARY] Salary: $275K–$305K USD for growth PM.

**Sierra:** [Sierra PM roles (2025–2026)](https://jobs.ashbyhq.com/Sierra/0c66e8ed-1c18-4b64-ad27-a522a866b6e1): "Product Manager, Voice" (April 2026) — requires 3+ years PM experience, voice/real-time systems, "Make voice measurable and improvable: Define how we evaluate voice agents: latency, interruption handling, resolution rate, and conversation quality. Build feedback loops that improve performance over time." Agent Data Platform PM: "Become trusted advisor to our customers, in partnership with forward-deployed teams." Sierra PMs are forward-deployed, eval-designing, and customer-facing. [PRIMARY]

**Linear:** [Linear careers (April 2026)](https://linear.app/careers) lists one "Product Manager" role (Europe/North America) — no details available. Also lists "Senior/Staff Product Engineer, AI." [PRIMARY]

### Is "PM as Prompt Engineer + Eval Designer" an Emergent 2025–2026 Role?

**Yes, with significant evidence.** This is not fully crystallized in a single named role but is the convergent practice across multiple sources:

- [Kevin Weil (CPO, OpenAI) via Peter Yang/Aman Khan, Jan 2025](https://creatoreconomy.so/p/ai-skill-that-will-define-your-pm-career-aman-khan): "Writing evals is going to become a core skill for product managers."
- [Sierra PM JD, April 2026](https://jobs.ashbyhq.com/Sierra/0c66e8ed-1c18-4b64-ad27-a522a866b6e1): PM required to define evaluation frameworks and build feedback loops.
- [Anthropic PM JD, 2026](https://www.anthropic.com/careers/jobs/5021316008): PM coordinates evaluations and red-team feedback.
- [Hamel Husain's course](https://maven.com/parlance-labs/evals): "Who this course is for — Engineers and PMs who ship prompt changes and hope nothing breaks."
- [Diego Granados, LinkedIn Dec 2025](https://www.linkedin.com/posts/diegogranadosh_in-2025-product-managers-went-from-can-activity-7401682905384833024-JZi9): "In 2025, Product Managers went from 'can GenAI do that?' to '…but is it ready to be shipped?'"

### Gaps

- No CE-specific PM role definition published by Klaassen or Shipper as of April 2026. The CE framework remains primarily engineering-framed.
- The $100 rule is not sourced in any CE primary publication found.
- No public case study of a CE-native PM workflow at any company.

---
---

## Deliverable D1 — Unified Methodology Comparison Matrix

Each row is sourced from the sub-domain above and synthesized from the partial matrices produced in both research streams. "AI-native adaptation" is a qualitative judgment drawn from the cited authors' own 2024–2026 positions where available; where authors have not published a 2024–2026 position, it is flagged `unknown` or inferred with a caveat.

| # | Framework | Origin year / author | Core unit of product thinking | Discovery mechanism | Delivery mechanism | AI-native adaptation | Solo-founder fit | Holding-scale fit | Primary-source quality |
|---|-----------|---------------------|-------------------------------|--------------------|--------------------|---------------------|-----------------|-------------------|----------------------|
| 1 | **Cagan / SVPG** | 2008 *Inspired* / Marty Cagan | Outcome-owning empowered product team | Discovery Trio (PM + Designer + Eng) running prototypes, interviews, experiments | Continuous delivery by the trio | **Medium** — four-risks vocabulary adapts directly; trio structure doesn't fit sub-10-person AI-native teams | **Low** — minimum team of three assumed; no solo playbook | **Medium** — workable 5–50; holding co needs added org layer | **High** — svpg.com primary, 2024–2026 articles |
| 2 | **Torres / Continuous Discovery** | 2021 *Continuous Discovery Habits* / Teresa Torres | Customer opportunity (need, pain, desire) | Weekly customer interviews + Opportunity Solution Tree + assumption testing | Framework-agnostic; builds begin after assumption validation | **High** — Torres is actively experimenting with AI for OST assistance 2025–2026; framework is discovery-native | **Medium** — OST works for one person; parallel build/discovery needs adaptation | **Medium** — scales to 50; holding-company guidance absent | **High** — producttalk.org primary, 2025–2026 |
| 3 | **JTBD** | Christensen 1997 / 2006 HBR; Ulwick ODI 2002; Moesta Switch Interview | Job — functional, emotional, social progress sought | Switch interviews (Moesta), outcome surveys (Ulwick ODI), progress stories (Klement) | Framework-agnostic | **High** — Ulwick's "Outcome-Driven AI" webinar (Dec 2025) extends ODI to AI implementation; JTBD adds ~zero process overhead | **High** — thinking model, runs with one person | **High** — ODI used by Fortune 500; scales across portfolio | **Medium** — Christensen HBR/Institute primary; Ulwick primary; Moesta/Klement no 2025–2026 primary found |
| 4 | **Lean Startup** | 2011 / Eric Ries (Blank 2005 predecessor) | Hypothesis — an assumption about customer behaviour or business model | Build-Measure-Learn, MVP as learning experiment | Continuous deployment; ship minimum, measure, iterate | **Medium** — BML survives; "minimum" in MVP collapses when a usable prototype takes 2 hours; no 2025–2026 Ries primary | **High** — informal operating model of most early-stage founders | **Low** — innovation accounting designed for single venture | **Low-Medium** — theleanstartup.com not confirmed active 2026; synthesizers dominate |
| 5 | **OKRs / North Star** | OKR: 1975 Intel (Grove) / popularised Doerr 1999; North Star: Ellis ~2010 / codified Amplitude | Objective + Key Results; or single North Star metric | Implicit — OKR retros + strategy; no defined discovery method | Implicit — teams own delivery against KRs | **Low-Medium** — quarterly OKR cadence misaligns with daily-ship; North Star Metric and Linear-style single-metric models adapt better | **Medium** (Wodtke single-OKR) / **High** (North Star alone) | **High** — scales to holding alignment; portfolio North Star per company is an established pattern | **Medium** — Doerr WhatMatters primary; Amplitude primary; Linear via Lenny primary |
| 6 | **RICE / ICE / WSJF / Kano / MoSCoW** | RICE ~2016 Intercom; ICE Sean Ellis; WSJF SAFe; Kano 1984; MoSCoW DSDM 1990s | Prioritised feature opportunity scored on N dimensions | None — assumes opportunities are already known | None — assumes agile sprint delivery | **Low** — all scoring dimensions destabilise under AI (non-linear effort, probabilistic impact, circular confidence); RICE-A/ARISE are retrofits | **Low** — scoring overhead too heavy for solo | **Medium** — useful at 20+ where coordination cost demands shared scoring | **Low-Medium** — no inventor has published an AI-native update; 2025–2026 critique is mostly secondary |
| 7 | **Product-Led Growth** | 2019 *Product-Led Growth* / Wes Bush, OpenView Partners | The free-user experience — time-to-value and aha moment | Usage analytics, funnel diagnostics, onboarding A/B | Self-serve freemium or trial → convert → expand | **High (with caveat)** — AI onboarding personalization, eval-based activation quality, and usage-based pricing are native; COGS discipline is new | **High** — low CAC + high leverage suits solo founders | **High** — portfolio-wide motion if each product has its own PLG loop | **Good** — Bush book 2019, OpenView benchmarks, Poyar Growth Unhinged 2024–2026 |
| 8 | **Category Design (Play Bigger)** | 2016 *Play Bigger* / Ramadan, Peterson, Lochhead, Maney | Problem–Category–POV triangle | Market-belief formation, Lightning Strikes, customer conditioning | Category-playbook execution over 6–10 year horizon | **Medium** — AI as proof-of-belief engine; category lifecycles are compressing to 12–24 months | **Medium** — requires sustained POV discipline; time-intensive | **High** — each portfolio company can own a sub-category | **Good** — Play Bigger book + Category Pirates newsletter active 2025–2026 |
| 9 | **Compound Engineering × PM** | 2024–2026 / Klaassen, Shipper (Every Inc.) + Husain (eval-driven dev) | The compound-loop cycle (Plan → Work → Review → Compound) | Vibe-coded prototype → real-user feedback loop; eval suite as spec | Agent-orchestrated CI/CD; parallel sub-agent review; compound-ledger updates | **Native** — framework is AI-native by construction; ~80% plan+review, ~20% execute | **High** — explicitly designed for 1-person engineering; GM/PM hybrid is the archetype | **Medium-High** — each product in a portfolio can run CE independently; cross-portfolio synthesis is unsolved | **Partial primary** — every.to 2025–2026; Husain hamel.dev primary; no PM-specific sub-framework yet published |

**How to read this matrix.** The right-most four columns are the most decision-relevant and the most disputable. "AI-native adaptation" answers the question *does this framework survive translation?* "Solo-founder fit" and "Holding-scale fit" answer *does it survive scale translation?* The only framework native to both AI and the 1-person unit is row 9 (CE × PM) — and it is also the one with the thinnest primary-source base for the PM-specific sub-framework. That is not a coincidence; it is the central tension of this document.

---

## Deliverable D2 — PM-in-CE Role Sketch

### Core Responsibilities (3–5, sourced)

1. **Define build-ready requirements (Plan input).** In CE, agents need precise, detailed plans to produce good output. The PM is the person most responsible for the quality of the plan input — translating user research, strategic priorities, and success criteria into agent-usable specifications. [Source: CE guide, every.to — "Good planning is not pure delegation — it requires the developer to think hard and be creative in order to push the agent down the right paths."]

2. **Own evaluation criteria and review standards (Review co-owner).** The PM defines "what good looks like" — the success criteria against which agent output is judged. This is the eval discipline: from acceptance criteria in traditional PM to formal eval suites in AI-native PM. [Source: Kevin Weil/Aman Khan, Jan 2025; Sierra PM JD, April 2026; Anthropic PM JD, 2026]

3. **Maintain compound-ledger of product learnings.** In CE, the "compound" step stores lessons from each cycle. The PM role includes curating the product-layer compound ledger: codified user research insights, validated spec patterns, known failure modes. [Source: CE guide — "We take what we learned in any of the previous steps and record them so that the agent can use them next time."; Hamel Husain Field Guide — "Teams invest weeks building complex AI systems, but can't tell me if their changes are helping or hurting."]

4. **Customer discovery (human-speed, non-delegatable).** Discovery remains the PM's highest-value, least-automatable function. [Source: Ravi Mehta, Atlassian Dec 2025 — "Customer discovery, product sense, and strategy: Those are only getting more important."; Shreyas Doshi, March 2026 — "Strong empathy (can you figure out what people need beyond what AI has already analyzed?)"]

5. **Prototype-validate-spec loop.** In CE environments, PMs are expected to build functional prototypes (via vibe coding), test them with real users, then delete and spec properly. [Source: CE guide every.to — "Vibe code to discover what you want, then spec to build it properly. The spec always wins for final implementation, but vibe coding accelerates discovery."]

### Artifacts They Build

| Artifact | Description | Source |
|----------|-------------|--------|
| **Agent-ready plan documents** | Detailed specification fed into the CE Plan step: objective, proposed architecture, success criteria, constraints, prior patterns to reference | [CE guide, every.to](https://every.to/guides/compound-engineering) |
| **Eval suite / acceptance criteria** | Formal or lightweight evaluators for each AI feature: what constitutes pass/fail, what sample traces confirm quality | [Hamel Husain evals guide](https://hamel.dev/blog/posts/evals-faq/); [Sierra PM JD](https://jobs.ashbyhq.com/Sierra/0c66e8ed-1c18-4b64-ad27-a522a866b6e1) |
| **Opportunity Solution Tree (OST)** | Living doc mapping desired outcomes → opportunities → solutions; updated as user research compounds | [Teresa Torres, producttalk.org — foundational; verify 2026 relevance] |
| **Compound-ledger entries** | Codified product learnings: user patterns discovered, spec patterns that worked, known failure modes for AI features | [CE guide — the compound step; Hamel Field Guide — "build simple tools that remove friction"] |
| **Vibe-coded prototypes** | Functional (not shipped) UI explorations for discovery, deleted after user feedback | [CE guide — vibe coding section] |
| **Error analysis reports** | Structured review of LLM output failures from production traces; drives eval refinement | [Hamel Field Guide: "Error analysis is the most important activity in evals"] |

### Time Allocation % (sourced reasoning)

| Activity | Allocation | Reasoning |
|----------|-----------|-----------|
| **Customer discovery + user research** | 35% | Ravi Mehta (Atlassian, Dec 2025): "90/10 — deciding what to build is 90% of success now." This is the highest-leverage, least-AI-substitutable PM activity |
| **Spec writing + plan creation** | 25% | CE 80/20 rule applied to PM: most effort in pre-build clarity; agent-ready specs require precision |
| **Eval design + error analysis + quality review** | 20% | Hamel Husain: "We've spent 60–80% of our development time on error analysis." For a PM, this is 20% in a collaborative CE team |
| **Compound-ledger + institutional codification** | 15% | CE 50/50 rule: half system investment; for PM this is maintaining living product docs, OSTs, and learnings repos |
| **Stakeholder + async communication** | 5% | Dan Shipper's Every operates as "demo culture not memo culture"; stakeholder work is compressed in small teams |

### Obsolete Traditional PM Activities in CE (sourced)

- **Writing PRDs for engineers to hand off.** [Aman Khan/Peter Yang, Jan 2025]: "The waterfall process of writing a PRD and handing it to designers and engineers no longer works." In CE, the plan document feeds agents directly.
- **Manual test case definition.** CE: "Manually writing tests... is now unnecessary." [Shipper/Klaassen, every.to, Dec 2025]
- **Scheduling sprint ceremonies.** CE teams run Plan→Work→Review→Compound continuously; sprint/standup cadences are replaced by async compound loops.
- **Asking engineering candidates to code without AI assistance.** [Shipper/Klaassen, every.to]: "So is asking an engineering candidate to code without access to the internet."
- **Lengthy written discovery synthesis decks.** [Hamel Field Guide, March 2025]: "Having a learning expert communicate teaching principles through PowerPoint, only for engineers to translate that back into English prompts, created unnecessary friction."

### New Activities (agent prompt curation, eval design, compound-ledger maintenance — cited)

- **Agent prompt curation:** PM owns and iterates on system prompts for product-facing AI features. [Hamel Field Guide, March 2025]: "The most successful teams flip this model by giving domain experts tools to write and iterate on prompts directly."
- **Eval design:** Writing acceptance criteria as evaluators. [Kevin Weil via Aman Khan, Jan 2025]; [Hamel evals guide, Jan 2026]
- **Compound-ledger maintenance:** Curating the institutional knowledge base that makes future build cycles faster. [CE guide compound step]
- **Vibe-coded prototype creation:** Building and testing functional prototypes without formal engineering. [CE guide vibe coding section; Lenny's Newsletter Best of 2025 — "A guide to AI prototyping for product managers"]
- **Error analysis on production AI traces:** Looking at real LLM outputs and categorizing failures before writing evaluators. [Hamel Field Guide, March 2025]

### Named 2025–2026 Job Postings That Reflect This Role

| Company | Role | Date | Key Signals |
|---------|------|------|-------------|
| [**Anthropic**](https://www.anthropic.com/careers/jobs/5021316008) | Lead PM, Developer Services | 2026 | "Coordinate evaluations, red-team feedback, and post-launch learning loops so improvements compound over time"; PLG mandate |
| [**Anthropic**](https://jobs.menlovc.com/companies/anthropic/jobs/49543903-product-manager-consumer-growth) | PM, Consumer Growth | 2025 | "A/B testing and user funnel optimization"; "balance rapid iteration with commitment to AI safety" |
| [**Sierra**](https://jobs.ashbyhq.com/Sierra/0c66e8ed-1c18-4b64-ad27-a522a866b6e1) | PM, Voice | 2026 | "Make voice measurable and improvable: define how we evaluate voice agents"; "build feedback loops that improve performance" |
| [**Sierra**](https://jobs.westboundequity.com/companies/sierra-2-90e5d64d-40bb-415e-bbca-4108552c8ee9/jobs/47173384-product-manager-agent-data-platform) | PM, Agent Data Platform | 2025 | "Innovate: Discovering new tools and processes for building agents"; forward-deployed + 0–1 product bets |
| [**Linear**](https://linear.app/careers) | Product Manager | 2026 | One open role; no details available; adjacent "Senior/Staff Product Engineer, AI" suggests engineering-heavy product team |
| **Cursor** | No PM roles open | April 2026 | Cursor has no traditional PM roles listed — model appears to be engineer-led product with no dedicated PM function [PRIMARY] |
| **Every Inc.** | No PM roles open | April 2026 | No PM roles; product embedded in GM and founder roles [PRIMARY] |

---

## Deliverable D3 — Top 10 Product Practices for AI-Native Solo-to-Small Teams

Ranked by estimated adoption value for 1–50 person AI-native teams.

| Rank | Practice | Origin Framework | Why It Works (mechanism) | Adoption Evidence | Cost to Adopt | When to Skip |
|------|----------|-----------------|--------------------------|-----------------|---------------|--------------|
| 1 | **Eval suite as product spec** | Hamel Husain, [hamel.dev, 2025–2026](https://hamel.dev) | Forces precise articulation of "good" before building; creates regression protection; becomes compound-ledger | 3,000+ engineers+PMs trained; Kevin Weil (OpenAI CPO), Anthropic CPO both named as most important PM skill 2025 | Medium: 1–2 days per feature to write initial evals; tooling cost minimal (Promptfoo is free) | Skip when feature is pure UI with deterministic behavior; don't write evals for errors you haven't yet seen |
| 2 | **Vibe-coded prototype → user feedback in one day** | Karpathy + CE guide, [every.to](https://every.to/guides/compound-engineering) | Compresses discovery cycle from weeks to hours; functional prototypes elicit better feedback than mockups | CE guide explicitly recommends; Ravi Mehta (Atlassian, Dec 2025): "Product teams use vibe-coding tools to build small tests, put them in front of real users" | Low: hours to build, free-to-trial tools (Lovable, v0, Replit) | Skip for infra/backend features; skip when you already have high-confidence spec from prior research |
| 3 | **Weekly customer interviews (continuous discovery)** | Teresa Torres, Continuous Discovery Habits, [producttalk.org](https://www.producttalk.org) [foundational, verify 2026 relevance] | Maintains fresh signal on evolving user needs; prevents building on stale assumptions; compounding research effect | Standard recommendation across Lenny, Ravi Mehta, Shreyas Doshi; Doshi: "Strong empathy — figuring out what people need beyond what AI has analyzed" | Low: 1 hour/week; requires systematic recruitment | Skip in pre-PMF stage when pivoting rapidly and customer definition is unstable |
| 4 | **OST (Opportunity Solution Tree) as living doc** | Teresa Torres, Continuous Discovery Habits [foundational] | Maps desired outcomes → opportunities → solutions; prevents solutions in search of problems; keeps team aligned | Standard practice in strong PLG teams; no 2025–2026 primary update found — foundational cite only | Low: template-based; effort is in keeping it current | Skip for single-feature solo tools where there's one obvious outcome to optimize |
| 5 | **Compound-ledger of learned specs** | Klaassen/Shipper, CE guide, [every.to, Dec 2025–Apr 2026](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) | Makes each build cycle faster by codifying what works; institutional memory survives context loss; agents read it in future plan steps | Every Inc. uses this internally across 5 products with 15 people | Low: CLAUDE.md / AGENTS.md file + CI enforcement; free | Skip for one-time projects; skip if you lack discipline to update after each cycle |
| 6 | **Experiment-first roadmap (count experiments, not features)** | Hamel Husain, [Field Guide, March 2025](https://hamel.dev/blog/posts/field-guide/) | Aligns team to what AI products actually require — rapid iteration and measurement; prevents feature theater | Fyxer: 514 experiments in 12 months; GitHub Copilot: thousands of experiments after eval infrastructure in place | Medium: requires eval infrastructure and experiment tracking | Skip when in pure exploration/pre-PMF and you need to ship something tangible to get user signal |
| 7 | **JTBD switch interview** | Bob Moesta / Chris Spiek [foundational]; Wes Bush MOAT framework | Reveals actual switching trigger (what "job" user was doing before, what forced them to seek new solution); stronger signal than survey | Standard recommendation; Bush's UCD framework centers on this | Low: 30–60 min per interview; requires synthesis discipline | Skip when you have strong behavioral data and interviews would be redundant |
| 8 | **Quarterly bets with appetite (Shape Up flavored)** | Basecamp/Ryan Singer, *Shape Up* [foundational, verify 2026 relevance] | Fixed time + appetite (not scope) prevents scope creep; forces upfront shaping discipline; maps well to CE plan step | Adopted by Linear, various small teams; no 2025–2026 primary citation found | Low: process change only | Skip for very small teams (<3 people) where informal coordination works |
| 9 | **Kill-list discipline** | Basecamp/Stripe philosophy [ANECDOTE — no primary 2025–2026 citation] | Prevents feature accumulation that increases maintenance burden; forces continuous ROI judgment | Referenced in Basecamp writing; no sourced 2025–2026 primary citation | Low: requires PM conviction to propose kills | Skip when users have deep feature attachment that would cause churn |
| 10 | **Outcome > output OKRs** | John Doerr, OKRs [foundational]; PLG extension | Aligns team to user outcomes not delivery metrics; prevents "shipped = done" culture; maps to PLG expansion metrics | Standard recommendation; Lenny/Shreyas content repeatedly emphasizes outcomes | Medium: culture change + stakeholder alignment required | Skip in very early stage (<6 months post-launch) where you're still discovering what outcomes matter |

---

## Deliverable D4 — Top 10 Product Traps to Avoid

| Trap | Why It's a Trap | Evidence / Citation |
|------|----------------|---------------------|
| 1. **"AI-as-faster-developer" (not discovery partner)** | Using AI to ship faster without using it to discover better is pure velocity theater. The compounding returns are in eval loops, user signal acceleration, and learned patterns — not raw ship speed. | [Hamel Husain Field Guide, March 2025](https://hamel.dev/blog/posts/field-guide/): "The teams who succeed barely talk about tools at all. Instead, they obsess over measurement and iteration." |
| 2. **Vibe revenue mistaken for PMF** | Early AI product signups driven by curiosity/FOMO look identical to PMF for 3–6 months. Retention curves reveal the truth. Raising money or scaling GTM on vibe revenue destroys unit economics. | [Greg Isenberg, gregisenberg.com, Feb 2026](https://www.gregisenberg.com/blog/vibe-revenue): "Vibe revenue is money coming from customers who are paying out of curiosity, novelty, or FOMO rather than because a product solves a genuine, persistent problem." |
| 3. **Over-reliance on AI-synthesized user patterns (hallucination risk)** | AI-synthesized research can fabricate plausible-sounding user patterns that don't reflect actual behavior. Without grounding in real traces and real user quotes, AI-generated insight is confabulation. | [Hamel Husain Field Guide, March 2025](https://hamel.dev/blog/posts/field-guide/): "Look at your data. Nothing replaces the insight gained from examining real examples." Error analysis must be done on real outputs, not synthetic summaries. |
| 4. **Eval suites diverging from real user value** | Eval infrastructure becomes a local optimization trap: optimizing for eval pass rates instead of user outcomes. Teams pass 100% of evals while users churn. | [Hamel Husain evals FAQ, Jan 2026](https://hamel.dev/blog/posts/evals-faq/): "Be wary of optimizing for high eval pass rates. If you're passing 100% of your evals, you're likely not challenging your system enough." |
| 5. **MVP fetishism** | In AI products, an under-quality AI feature destroys trust more durably than not shipping at all. The "ship fast and iterate" SaaS mantra fails when the AI output quality is below reliability threshold on day one. | [Poyar AI-native org report, March 2026](https://www.growthunhinged.com/p/ai-native-org-report-part-one): HeyGen quote: "If the AI quality is there, people will keep using it. This is the most important metric and a leading indicator for us." |
| 6. **Category creation before PMF** | Attempting Lightning Strike category naming before achieving PMF confuses the market. Category design requires credibility, working product, and a POV that customers feel as true. | [Play Bigger methodology](https://www.playbigger.com/categorydesign): The category must be designed simultaneously with product and company — not as an early branding exercise. [Extruct.ai PLG 2025](https://www.extruct.ai/research/plg2025/): "If you must 'teach' before value, start sales-led and productize learnings." |
| 7. **OKR cargo cult** | Using OKR format (Objective + Key Results) without grounding in actual user outcome measurement. OKRs filled with output metrics (features shipped, documents written) dressed as outcomes. | [Widespread practitioner observation; no single primary 2025–2026 citation.] The CE 50/50 rule implicitly counters this: system improvements are measured differently from feature outputs. [ANECDOTE] |
| 8. **RICE theater (inflated confidence scoring)** | RICE (Reach, Impact, Confidence, Effort) scores are often reverse-engineered to justify predetermined decisions. Confidence scores are typically invented. | [Widespread PM community critique; no single named 2025–2026 primary source.] Ravi Mehta (Atlassian, Dec 2025): "Determining what to build becomes 90% of success, up from roughly 50% before" — implying shallow prioritization frameworks are insufficient. [ANECDOTE] |
| 9. **Premature productization of a service** | Building software infrastructure before validating that the workflow is stable and repeatable. Common in AI-native consulting: automating a process before understanding it. | [Hamel Field Guide, March 2025](https://hamel.dev/blog/posts/field-guide/): "It's very consultative in that you really have to partner with the customer to understand their existing workflows and reimagine the work for the future. You can't just blindly automate what's been done in the past." |
| 10. **Solo founder building PM function when not the binding constraint** | Investing in PM infrastructure (OSTs, OKRs, eval pipelines) before the bottleneck is product clarity. Pre-PMF, the binding constraint is signal — not process. | [Extruct.ai PLG 2025](https://www.extruct.ai/research/plg2025/): "If both [self-serve readiness tests] are 'yes', design self-serve now. If not, run a human-led motion to learn quickly." PM process overhead before PMF is a distraction. |

---

## Deliverable D5 — PM Tool Stack 2026 for AI-Native Solo Founder

### Discovery (AI-Augmented User Research)

| Tool | Role | AI-Native Features | Why / When |
|------|------|-------------------|------------|
| [**Dovetail**](https://dovetailapp.com) | Centralized research library; interview synthesis | Automated transcription, insight tagging, video highlight reels, "Ask Dovetail" (NL query over all research) | Best when you have recurring user interviews; [Figma resource library, 2024](https://www.figma.com/resource-library/ai-tools-for-product-discovery/) reports 236% ROI documented |
| [**Sprig**](https://sprig.com) | In-product micro-surveys and analytics | AI Study Creator, in-product targeting, product health dashboards | Best for activation/aha-moment instrumentation; [Figma AI tools guide](https://www.figma.com/resource-library/ai-tools-for-product-discovery/) |
| [**Kraftful**](https://kraftful.com) | Feedback → spec generation | Auto-drafts PRDs from user feedback, AI-led user interviews, daily digests | Solo-founder specific: collapses research → spec in one tool |
| [**Looppanel**](https://looppanel.com) | Rapid interview analysis | Discussion guide mapping, AI tagging, sentiment analysis | Best when interview volume is high (>5/week) |

### Eval (LLM Evaluation)

| Tool | Best For | Pricing | Why |
|------|----------|---------|-----|
| [**Promptfoo**](https://promptfoo.dev) | CLI testing, red teaming, local-first, CI/CD integration | Free (OSS, 10K probes) | Best for solo founders: zero cost, privacy-preserving, security testing; [Braintrust comparison, Nov 2025](https://www.braintrust.dev/articles/best-prompt-evaluation-tools-2025) |
| [**Braintrust**](https://braintrust.dev) | All-in-one: eval + tracing + experiments; collaborative | Free (5 users, 1M spans); paid above | Best when team grows or you need production observability; [Techsy.io ranking 2026](https://techsy.io/blog/best-llm-evaluation-tools) |
| [**Langfuse**](https://langfuse.com) | Open-source tracing, self-hosting | Free (self-hosted); cloud paid | Best for privacy-sensitive use cases; [ranked #3 overall by Techsy 2026](https://techsy.io/blog/best-llm-evaluation-tools) |
| [**DeepEval**](https://deepeval.io) | Most metrics (50+), pytest-native, agent eval | Open source | Best for teams already using pytest; [ranked #1 overall by Techsy 2026](https://techsy.io/blog/best-llm-evaluation-tools) |
| **Patronus AI** | Enterprise-grade safety + compliance evals | Enterprise pricing | Skip for solo founders; overkill until enterprise compliance is required |

### Prioritization

| Tool | Notes |
|------|-------|
| [**Linear**](https://linear.app) | Cycle management + project tracking; used by Cursor, many AI-native teams; MCPs available for AI integration (Fyxer case study); no AI-native prioritization features per se |
| [**ChatPRD**](https://chatprd.ai) | AI PRD generation + logic stress-testing; Lenny included in Product Pass 2025 |
| **Custom AI prioritization** | Use Claude/GPT with your OST context; no dedicated AI-native prioritization tool found that outperforms well-prompted LLM as of April 2026 |

### OKR

| Tool | AI-Native Features |
|------|-------------------|
| [**Perdoo**](https://perdoo.com) | OKR + roadmap; no notable AI-native features found |
| [**Weekdone**](https://weekdone.com) | Weekly check-ins, OKR tracking; no notable AI-native features found |
| **Productboard** | [Ravi Mehta blog, July 2025](https://blog.ravi-mehta.com/p/ai-supercharging-every-phase): AI will embed in product management platforms like Productboard; "AI integrated into your core product systems will have deep knowledge of your product, customers, market, and strategy" |

### Feature Flagging

| Tool | Best For | Notes |
|------|----------|-------|
| [**Statsig**](https://statsig.com) | All-in-one: flags + A/B testing + analytics + session replay | Powers OpenAI, Notion, Figma; 1 trillion events/day; AI copilot features for product workflows; CUPED reduces experiment runtime 30–50% |
| [**GrowthBook**](https://growthbook.io) | Open-source; maximum control; cost-effective at scale | Best for privacy-sensitive or budget-constrained teams; requires more DIY |
| [**LaunchDarkly**](https://launchdarkly.com) | Enterprise feature management | Overkill for solo founder; standard for larger teams |

### Customer Feedback

| Tool | AI-Native Features | Notes |
|------|-------------------|-------|
| [**Canny**](https://canny.io) | AI-powered feedback clustering | Standard for public roadmap + voting |
| [**Dovetail**](https://dovetailapp.com) | Full research platform; "Ask Dovetail" NL query | Best for deep research synthesis |
| [**Productboard**](https://productboard.com) | AI links customer feedback to features and strategic goals | [PM Society, July 2025](https://blog.productmanagementsociety.com/7-essential-ai-tools-for-product-managers-in-2025-3/) |

### "PM-as-Agent" Tools 2025–2026

**No credible dedicated "PM-as-agent" product found as of April 2026.** The YC Spring 2026 Request for Startups explicitly lists ["Cursor for Product Managers"](https://modelence.com/yc-rfs-spring-2026/cursor-for-product-managers) as an open problem: "Build a production-ready AI-native SaaS for product teams that helps them decide what to build — not just how to build it." This confirms the category does not yet have a dominant player. Closest approximations in use: ChatPRD (spec generation), Kraftful (feedback → spec), custom agent workflows via n8n/Lindy, Dovetail's "Ask Dovetail."

---

## Deliverable D6 — Honest Assessment

### 1. Is there a credible 2025–2026 published PM framework designed for AI-native teams?

**Partial.** No single integrated framework exists as of April 2026. The closest components:
- [Hamel Husain's eval-driven AI product development practice (hamel.dev, 2025–2026)](https://hamel.dev) covers the build/measure loop but does not address discovery or strategy.
- [Every Inc.'s Compound Engineering guide (every.to, 2025–2026)](https://every.to/guides/compound-engineering) covers the engineering-side workflow and implicitly defines a PM-shaped role but does not formalize it as a PM framework.
- [Aakash Gupta's AI PM MBA (aakashg.com, 2025)](https://www.news.aakashg.com/p/ai-pm-learning-roadmap) is the most comprehensive curriculum but is a synthesis of existing frameworks rather than a new integrated methodology.

No named "Compound PM" or "CE-PM" framework exists with a primary author and canonical URL as of April 2026.

### 2. What's the new job of a PM in a compound-engineering team? (Operational definition)

A PM in a compound-engineering team is the **plan-quality owner and institutional-knowledge steward**. Their primary outputs are: (a) agent-ready requirement documents precise enough to be executed by AI coding agents without human clarification; (b) eval suites that define what "good output" means for each AI feature; (c) a compound-ledger of validated product learnings that makes future build cycles faster. Their primary inputs are: continuous customer discovery (human-speed, non-delegatable) and usage pattern analysis (AI-augmented). They build functional prototypes for discovery (not for shipping), conduct error analysis on production AI traces, and update the institutional knowledge base after each cycle. Traditional PM activities — writing PRDs for engineer handoff, running sprint ceremonies, creating status update decks — are either automated, deprecated, or compressed into the Plan step of the CE loop.

### 3. Will traditional PM roles shrink, grow, or transform? (Evidence both directions)

**Transform, with pockets of contraction.**

*Evidence for transformation (role evolves, not eliminated):*
- [Ravi Mehta, Atlassian Dec 2025](https://www.atlassian.com/blog/artificial-intelligence/shift-from-craft-to-judgement-ai): "AI isn't replacing the craft of product management — it's reshaping it. AI will handle more of the doing. But strategy, empathy, and taste are going to matter even more."
- [Shreyas Doshi, March 2026](https://shreyasdoshi.substack.com/p/why-product-sense-is-the-only-product): Product Sense (empathy, simulation, strategic thinking) is non-automatable.
- [Anthropic, Sierra actively hiring PMs](https://www.anthropic.com/careers/jobs/5021316008) with eval and AI quality mandates.
- [Claire Silver via Every.to, Aug 2025](https://every.to/podcast/best-of-the-pod-she-built-an-ai-product-manager-bringing-in-six-figures-as-a-side-hustle): PM:engineer ratio shifts from 1:7 to 1:20 — fewer PMs per engineer but higher impact per PM.

*Evidence for contraction:*
- [Cursor careers page, April 2026](https://cursor.com/careers): No PM roles. Engineering-led product.
- [Every Inc. careers page, April 2026](https://every.to/careers): No PM roles. Product embedded in GM/founder.
- The "proto-manager" concept (build prototypes, not documents) suggests the traditional non-technical PM with no build ability faces structural obsolescence.
- [Lenny's Newsletter Best of 2025](https://www.lennysnewsletter.com/p/best-of-lennys-newsletter-2026): "Product manager is an unfair role. So work unfairly." — framing of the role as defensible only by those who adapt.

### 4. Most Overrated Classical PM Practice in AI-Native Contexts?

**The PRD-to-handoff waterfall.** Writing a detailed requirements document that engineers then translate into implementation plans is the most thoroughly deprecated classical PM practice in AI-native teams. [Aman Khan, Jan 2025](https://creatoreconomy.so/p/ai-skill-that-will-define-your-pm-career-aman-khan): "The waterfall process of writing a PRD and handing it to designers and engineers no longer works. The development cycle needs to be much shorter, like clock cycles in a GPU." [Hamel Field Guide, March 2025](https://hamel.dev/blog/posts/field-guide/): The PM-to-engineer prompt-translation handoff "created unnecessary friction." In CE, the plan document feeds agents directly; the PM writes for agents, not humans. Classic PRD format — problem statement, user stories, acceptance criteria, open questions — maps onto the CE Plan step but requires a fidelity upgrade and a shift from narrative to evaluable criteria.

### 5. 90-Minute PM Curriculum for a New AI-Native Team (10 Concepts)

| # | Concept | Source | Time |
|---|---------|--------|------|
| 1 | **CE loop fundamentals** (Plan→Work→Review→Compound; 80/20 + 50/50 rules) | [CE guide, every.to](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) | 10 min |
| 2 | **Product Sense as the only non-commoditizable PM skill** (empathy, simulation, strategic thinking, taste, creative execution) | [Shreyas Doshi, March 2026](https://shreyasdoshi.substack.com/p/why-product-sense-is-the-only-product) | 10 min |
| 3 | **Evals as the new unit test: error analysis first, eval writing second** | [Hamel Husain evals FAQ, Jan 2026](https://hamel.dev/blog/posts/evals-faq/) | 10 min |
| 4 | **Vibe-coded prototype → user feedback in one day (discovery mode)** | [CE guide vibe coding section](https://every.to/guides/compound-engineering); Ravi Mehta, Dec 2025 | 10 min |
| 5 | **PLG fundamentals: MOAT, time-to-value, activation → aha → expand** | [Wes Bush, 2019](https://productled.com/book/product-led-growth); [OpenView PLG benchmarks](https://openviewpartners.com/blog/your-guide-to-product-led-growth-benchmarks/) | 10 min |
| 6 | **Vibe revenue vs. real PMF: retention is the only truth** | [Greg Isenberg, Feb 2026](https://www.gregisenberg.com/blog/vibe-revenue); [Poyar AI-native org report, March 2026](https://www.growthunhinged.com/p/ai-native-org-report-part-one) | 10 min |
| 7 | **Experiment-first roadmap: count experiments, not features** | [Hamel Field Guide, March 2025](https://hamel.dev/blog/posts/field-guide/) | 10 min |
| 8 | **Category design basics: Magic Triangle, POV, Lightning Strike** | [Play Bigger (2016)](https://www.categorydesignadvisors.com/play-bigger/); [Category Pirates (2025)](https://www.categorypirates.news) | 10 min |
| 9 | **Compound-ledger: codify every learned spec pattern** | [CE guide compound step, every.to](https://every.to/guides/compound-engineering) | 5 min |
| 10 | **The proto-manager: build prototypes not documents, own evals not status updates** | [Claire Silver / Every.to, Aug 2025](https://every.to/podcast/best-of-the-pod-she-built-an-ai-product-manager-bringing-in-six-figures-as-a-side-hustle); [Lenny's Newsletter 2025](https://www.lennysnewsletter.com/p/best-of-lennys-newsletter-2026) | 5 min |

---
---

## Consolidated Gaps, Uncertainty, and Source-Quality Notes

This section merges the unsourced-claim registers and thin-area notes from both research streams into a single register. It is designed to be read before acting on any deliverable in this document.

### Unsourced or Under-Sourced Claims

1. **The "$100 rule"** — referenced in the original research brief as a Compound Engineering codification heuristic ("codify if you'd pay $100 to never do it again"). Extensive search of every.to did not surface a primary Klaassen/Shipper publication of this specific phrasing as of April 2026. Treat as practitioner heuristic, not sourced CE canon. The underlying idea — codify recurring tasks — is compatible with CE's compound-ledger principle but the specific dollar threshold is unsourced.

2. **"Prompt-first PM" as a named movement** — no primary source found. The underlying practices (context engineering, prompt iteration, eval design as product spec) exist under other names but no canonical 2025–2026 framework or named proponent has published under this label.

3. **Cursor's internal PM practice** — Cursor had no PM roles open as of April 2026 and has published no account of how product decisions are structured internally. All claims about Cursor's PM approach are inference, not primary source.

4. **Every Inc.'s internal PM workflow** — Dan Shipper's Lenny interview (July 2025) is paywalled; the CE framework describes engineering practice, but how product discovery operates at Every beyond the CE loop is unconfirmed.

5. **Linear's PM practices** — Linear has a PM role open but no JD detail was captured, and there are no 2025–2026 blog posts or interviews from Linear PMs on internal process. "How Linear Grows" (Gupta) is a growth case study, not a PM-process case study.

6. **Moesta / Spiek 2025–2026 AI-context positions** — no primary content from Bob Moesta or Chris Spiek specifically addressing AI products in 2025–2026 was located. Switch Interview AI application is extrapolated from the mechanic, not cited.

7. **Eric Ries 2025–2026 primary statements** — no direct Ries quotes from accessible primary sources for 2025–2026 found. Podcast descriptions confirm AI was discussed but transcripts were inaccessible; `theleanstartup.com` was not confirmed active.

8. **Alan Klement 2025–2026 positions** — no recent primary-source content from Klement was found.

9. **Named AI-native companies explicitly crediting Cagan's model** — SVPG's framework is widely cited but no sub-50-person AI-native startup publicly credits it by name in 2025–2026 primary sources.

10. **John Doerr 2025–2026 positions on OKRs and AI** — no primary Doerr content specifically on AI-native team OKR adaptation was found.

11. **Stripe, Anthropic, Cursor formal prioritisation frameworks** — public product leaders at these companies have not published formal accounts of their internal prioritisation process; the Anthropic PM interview guide hints but is not a primary source on actual practice.

12. **MoSCoW 2025–2026 relevance** — no primary-source treatment of MoSCoW in AI-native contexts found; the framework appears to have faded from active 2025–2026 practitioner discussion.

13. **OKR tools with genuine AI-native features** — Perdoo, Weekdone, Lattice and similar were reviewed, but no 2025–2026 primary evidence of AI-native features that materially change the PM workflow was found. Weakest tool category in D5.

14. **Solo-founder PLG data specific to AI products** — Poyar's AI-native org report covers Series A+; benchmark data for truly solo-founder AI products is absent from primary sources.

15. **Patronus AI comparative review** — found in passing but no primary comparative review of Patronus vs. alternatives for the solo-founder use case was located.

16. **CE × PLG intersection** — no primary source explicitly addresses how Compound Engineering and PLG interact. The inference that CE enables higher experiment velocity (which enables better PLG iteration) is logical but unsourced.

### Topics Where 2025–2026 Primary Material Is Thin

- **JTBD for AI-agent products** where the "customer" is another AI agent, not a human — no canonical primary treatment exists.
- **Discovery time allocation in Compound Engineering** — the "~50% discovery" claim is widely repeated but no primary source from any framework author defines it in AI-native contexts.
- **Holding-company PM methodology** — none of the nine frameworks explicitly addresses multi-product holding structures; this is a genuine white space in both classical and AI-native PM literature.
- **Formal innovation accounting for AI products** — Lean Startup's innovation accounting was designed for human-behaviour metrics; no primary adaptation for AI product metrics (model accuracy, hallucination rate, token cost per outcome) exists from Ries or a primary thinker.
- **Solo-founder PM methodology** — all nine frameworks assume a team; no classical PM thinker has published a solo-founder adaptation as a primary work, and the CE-PM synthesis is still emergent.
- **Compound Engineering loop integration with classical PM** — the specific Plan→Work→Review→Compound framework is not mentioned in any classical PM primary sources reviewed; translation between CE and classical PM requires inference, not direct citation.

### Source-Quality Notes by Author / Institution

- **SVPG (Cagan, Jones):** highest primary source quality. svpg.com articles directly attributed, dated, and primary; multiple 2024–2026 pieces on AI.
- **Product Talk (Torres):** high primary source quality. producttalk.org articles primary with confirmed 2025–2026 dates; newsletter active.
- **Strategyn (Ulwick):** high for ODI foundations; the December 2025 "Outcome-Driven AI" webinar is primary but no full transcript was accessible for direct quotes.
- **HBR / Christensen Institute:** primary for Christensen foundational work; the Institute publishes periodic updates but no major 2025–2026 JTBD treatise was found.
- **Lean Startup sources (Ries):** low for 2025–2026. Ries's primary voice is absent from accessible 2025–2026 sources; synthesizers dominate.
- **OKR sources (Doerr / WhatMatters, Wodtke, Amplitude):** mixed. WhatMatters.com is primary-organizational; Amplitude's North Star Playbook is primary; Wodtke content is primary but dated 2021; Linear's single-metric pattern is captured via Lenny's Newsletter primary interview.
- **Prioritisation frameworks:** mostly secondary for 2025–2026 adaptations. No original inventor has published an AI-native update in accessible primary sources.
- **Every Inc. (Klaassen, Shipper):** primary for Compound Engineering itself (every.to); gaps on PM-specific application; paywall on some interviews.
- **OpenView / Growth Unhinged (Bush, Poyar):** good primary coverage for PLG and AI-native PLG benchmarks 2024–2026.
- **Category Pirates (Lochhead):** active primary newsletter 2025–2026; Play Bigger book (2016) remains the anchor.
- **Hamel Husain (hamel.dev):** primary for eval-driven development; an emerging authority on eval design as a PM discipline.
- **Karpathy, named AI-native practitioners (Yang, Rachitsky, Doshi, Mehta, Gupta):** mixed primary quality — newsletter posts are primary, but few have published a named *framework* for AI-native PM; most commentary is essayistic.

### How to Use This Gaps Register

Treat the weakest areas (solo-founder methodology, holding-scale PM, $100 rule, Cursor/Linear internal practice) as places where the document is reasoning from mechanism rather than citation. Do not quote this document as authoritative on those points; use the cited primary sources for load-bearing decisions and this document as a map. Where the CE × PM synthesis (sub-domain J, deliverables D2–D6) makes specific role or practice claims, the evidence is drawn primarily from every.to and from named 2025–2026 job postings, but the full synthesised PM-in-CE role is a constructed position, not a cited framework — it is the document's contribution, not a summary of an existing canon.

---

*Document compiled 22 April 2026. Streams A and B researched independently then merged. Total word count ≈18,500. All inline citations preserved from source streams. Unsourced claims removed or explicitly labelled. No hype; uncertainty flagged.*
