---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: §3.9
direction: Smart AI Flagship Narrative
type: layer-deep-dive-section
mode: critic
author: philosophy-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", section: "§Smart AI verbatim"}
  - {path: "reports/review_2026-04-24.md", section: "audio_529 rows 808-811"}
  - {path: "decisions/JETIX-VISION.md", section: "§7 archetypes + §4 D13"}
  - {path: "decisions/JETIX-PHILOSOPHY.md", section: "§2 D2 amplifier-not-replacement"}
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", section: "§0 TL;DR + §L5 Smart AI row"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md", section: "§2 Smart AI row + §1 Mission"}
  - {path: "prompts/swarm-launch-brigadier-l5-product-deep-dive-2026-04-25.md", section: "§3 direction 9 + §4 template"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md", section: "§3 row 9 + §6 anti-scope"}
word_count_estimate: ~2100
confidence: high
confidence_method: synthesis-from-locked-decisions-plus-verbatim-voice-plus-philosophy-critic-rubrics
escalations: []
dissents:
  - position: "Smart AI framing may function as internal narrative while simultaneously drifting toward external product branding in practice — the two usages are not cleanly separable without an enforcement mechanism"
    held_by: philosophy-expert (critic observation)
    F: F3
    ClaimScope:
      holds_when: "no /lint signal exists for external-facing Smart AI usage; human oversight is the only gate"
      not_valid_when: "a /lint rule is implemented per D25 Company-as-Code that flags Smart AI appearing on external materials without Ruslan ack"
    R:
      refuted_if: "a /lint signal is added AND tracked for 2+ cycles with zero false-positives"
      receipt: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/ decision log"
      accepted_if: "the /lint signal is absent AND the internal/external drift is observed in any swarm output"
---

# §3.9 Smart AI Flagship Narrative

## Epistemic Preamble (critic-mode obligation)

This section applies the philosophy-expert critic lens to the Smart AI Flagship Narrative — an internal category descriptor for Jetix's product portfolio. Critic mode here means epistemic rigor first: preserving the "internal label, not external product name" status; not inadvertently promoting; auditing every claim for falsifiability; flagging genuine philosophical tensions. The section covers the full 9-item adapted template. There is no Offer structure because Smart AI is not a sellable product — it is a conceptual category-lens applied across all 8 other directions. This distinction is load-bearing and is preserved throughout. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §Smart AI]

---

## 1. Mission

Smart AI is the **category descriptor** Ruslan uses internally to describe what Jetix builds across all 8 product directions. The category names a generation of AI systems distinguished by specific observable traits: context-preservation, memory-retention, and project-management assistance — not by any single technology or product.

The primary source for this framing is audio_529 [src:reports/review_2026-04-24.md rows 808-811]:

> *«Smart AI сохраняет контекст, обучается, помогает людям самим обучаться и управлять жизнью/проектами более эффективно. Требует глубокую экспертизу для использования.»* [audio_529]

The smartphone analogy, transmitted verbatim from the same session and preserved in the D25-D28 Addendum, establishes the conceptual architecture: *«Jetix делает Smart AI — как раньше были телефоны, потом смартфоны, так же произойдёт с ИИ»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §Smart AI].

The mission of this narrative framing is not to sell Smart AI as a branded product. The mission is epistemic: to give Ruslan and the internal team a coherent conceptual vocabulary for what Jetix is building, so that the 8 operational directions are understood as instantiations of one category-bet rather than 9 unrelated products. This is a portfolio-coherence function, not a marketing function.

**Distinction preserved.** Jetix = Jetix externally. Smart AI = how the category of work is described in internal discussion and early-sales exploratory conversations. These are not interchangeable. [src:decisions/JETIX-SYSTEM-OVERVIEW.md §0 TL;DR]

---

## 2. Phase Activation + Status

**Active in:** All phases as internal narrative label. Cross-phase. Does not have a single activation trigger because it is not a product — it is a category descriptor that applies from Phase 0 (€0) onward.

**External status:** Internal label only. This is mandatory to preserve.

The definitive status anchor is Ruslan's verbatim statement from the D25-D28 Addendum: *«ну типа запиши между прочим но нет это ещё не лок блять забей хуй»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §Smart AI]. Translated into formal policy: Smart AI is a D29-candidate-deferred designation. The narrative exists and may be used in internal + early-sales discussions. It is not authorized for landing pages, pitch decks, product-SKU language, or investor deck front pages. Any external-facing reference requires explicit Ruslan ack that has not yet been given.

**Falsifiability of this status declaration (critic obligation — AP-PHIL-1 prevention).** The claim "Smart AI is internal-only" is falsifiable: it is refuted if Smart AI language appears on any external-facing Jetix material (landing page, pitch deck, public blog post claiming the term as a Jetix product name) without documented Ruslan ack. The falsifier is observable in the repository and on external surfaces. The claim is currently accepted because no such external usage exists in the canonical corpus as of 2026-04-25.

**Sunset condition.** The Smart AI narrative dissolves if: (a) Ruslan explicitly deprecates it; (b) external AI-category language converges on a different term that supersedes it; or (c) at D29 promotion, it either graduates to external product framing or is retired as obsolete. None of these conditions have fired.

---

## 3. Target ICP Mapping (Category-Frame, Not Direct Sale)

Smart AI is not a direct ICP target. It is a category-lens applied when speaking to ICPs about the 8 operational directions. The mapping is therefore about which ICPs receive the framing most effectively, not which ICPs are being sold to.

**Most effective application contexts:**

The **Startupper** archetype [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3] benefits most from the Smart AI category-frame because Startuppers build or evaluate AI systems and can distinguish between a category-level claim ("this is a new generation of AI") and a product-level claim ("this is a specific product called Smart AI"). The phones-to-smartphones analogy lands cleanly with this audience because they have already internalized the concept of category shifts in technology.

The **Operator-Founder-CEO** archetype evaluates portfolios of AI tooling against category shifts. Smart AI framing reframes the conversation from "which AI tool do I buy?" to "am I making a category-level infrastructure bet?" — a more useful question for this archetype's decision horizon.

The **Teacher / Educational archetype** [src:decisions/JETIX-VISION.md §8] appreciates conceptual-category framing because their work involves explaining what something is at a structural level. The Smart AI category is more explainable than any specific product-feature comparison.

**Anti-use cases.** The Smart AI framing is counterproductive with: cold outreach to technical engineers who will read "Smart AI" as marketing-speak and dismiss it immediately; enterprise procurement teams who need specific product-SKU language for budget allocation; and Mittelstand mid-managers whose primary Jetix hook is the GDPR-compliant local-first AI methodology (where "Smart AI" adds no specificity and may introduce confusion).

**Payment-ability filter** (L6 constraint per [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md §2]): Smart AI narrative targets the same Tier-1 filter ($5K/mo recurring OR $10K one-shot) as the operational directions it describes, but this filter does not apply to the narrative itself — it applies to the products the narrative frames.

---

## 4. Value Proposition (Category-Frame, Not Offer)

**Problem the Smart AI framing solves.** There is a cognitive saturation problem in the current AI market: clients face a landscape of ChatGPT wrappers, agent frameworks, AI tools, automation services, AI consultants, and AI platforms — most described in indistinguishable language. The question "is this a ChatGPT wrapper?" is a legitimate client concern that signals category confusion. Smart AI framing addresses this by positioning Jetix at the category level: not another product within the existing category, but a descriptor of a new category of AI system. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §1]

**How the framing works (smartphone analogy).** The phones-to-smartphones shift is one of the most broadly understood technology category transitions of the last two decades. The shift was not about features ("this phone has a touchscreen"); it was about the definition of what a phone is. Smart AI makes an analogous claim: AI systems that preserve context, retain memory, and assist with project management across time are categorically different from AI tools that process individual prompts without persistence. The analogy is intuitive, non-academic, non-triumphalist, and avoids the over-claim of "AGI." [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §Smart AI; reports/review_2026-04-24.md row 808]

**Observable traits that ground the category (anti-vague-claim discipline — AP-PHIL-1).** The Smart AI category is anchored in four observable Jetix properties, not in marketing language. A claim is epistemically valid only if it is grounded in observable features; otherwise it is unfalsifiable brand positioning. The four anchors:

- **D25 Company-as-Code** [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D25]: every Jetix knowledge artifact has provenance in git. This is the "memory-retention" trait instantiated in actual infrastructure — not a claim, a system.
- **D17 Filesystem-SoT**: the canonical knowledge state is reconstructable from git history. This is "context-preservation" in a specific, falsifiable sense.
- **D13 Closed core / Open surface** [src:decisions/JETIX-VISION.md §4]: the methodology has a protected core and an open interface layer — this is "intelligent governance" of the AI system, not just the AI outputs.
- **D28 Query-driven KB Filtering** [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28]: the knowledge base is filtered by relevance to declared active queries, not accumulated indiscriminately. This is "selective intelligence" — the AI system knows what it is for.

These four anchors give Smart AI its falsifiable content. "Jetix builds Smart AI" is not a brand claim when it is shorthand for "Jetix builds context-preserving, memory-retaining, query-filtered, governance-disciplined AI infrastructure per D25/D17/D13/D28." It is a brand claim — and an unfalsifiable one — if it is merely an adjective asserting quality.

**D2 amplifier-not-replacement constraint.** The D2 Philosophy document establishes that Jetix positions as amplifier, not replacement [src:decisions/JETIX-PHILOSOPHY.md §2]. "Smart AI" language must not inadvertently drift toward replacement-framing. "Smart AI that helps you manage your projects" is amplifier language. "Smart AI that replaces your project manager" is replacement language. The distinction is epistemic and operational, not aesthetic. The critic flags this boundary explicitly: every external-facing Smart AI description in future materials must pass the amplifier/replacement check against D2.

---

## 5. Internal vs External Usage Guidance

This section takes the place of Offer Structure because Smart AI is a narrative instrument, not a product.

**Authorized internal usage:**

Internal team discussions about what Jetix is building are the natural home for Smart AI language. "This is a Smart AI system" is precise shorthand for the four-anchor bundle (D25/D17/D13/D28) when speaking to team members who hold the full context. It is efficient, accurate, and epistemically sound in this context. [src:decisions/JETIX-SYSTEM-OVERVIEW.md §0 TL;DR]

Early-sales exploratory conversations — introductory calls, informal presentations, community discussions — may include Smart AI framing as a category descriptor. "Jetix operates in the Smart AI category" is a defensible positioning statement in these contexts because the interlocutor has not yet committed to a specific product evaluation and the framing sets expectations at the right level of abstraction.

Training materials and educational content benefit from the Smart AI category because they explain conceptual structure. Phase 3+ educational products (methodology repo as Apache 2.0, per L6 Alliance Option C) may introduce "Smart AI methodology" as a category-reference concept — but as educational content, not product branding. [src:decisions/JETIX-SYSTEM-OVERVIEW.md §§L5 trajectory table G3]

Philosophical and thought-leadership content (the Philosopher archetype's channel per [src:decisions/JETIX-VISION.md §8]) can carry Smart AI framing as category-level analysis: "AI is undergoing a category shift analogous to phones-to-smartphones, and Jetix is building infrastructure for the Smart AI generation" is a legitimate thought-leadership claim grounded in audio_529 [src:reports/review_2026-04-24.md row 808].

**Prohibited external usage:**

Landing pages and homepage hero copy. The D29 lock has not been granted. Using "Smart AI" as hero-copy language would function as a de facto product-name commitment that Ruslan explicitly has not made. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §Smart AI verbatim]

Pitch decks to investors. Investor decks describe a company's product offering. Smart AI as a product name in an investor deck implies a product-naming decision that would require D29. This usage is prohibited until Ruslan explicitly grants the ack.

Product-SKU language. "Buy our Smart AI service" is a reification of the category into a product, which is the exact risk Ruslan identified and rejected. The category is not for sale; the products the category describes are for sale.

Press releases and public corporate communications. These are HITL-only artifacts anyway (per philosophy-expert §1d "human-owned territory respected"). Smart AI in a press release would require both HITL ack and D29 promotion.

**Policy summary.** Smart AI appears in narrative framing. It never appears in product branding without D29. Jetix = Jetix externally; Smart AI = how internal-and-early-sales discussion describes what Jetix builds. This is a D29-candidate-deferred status: may graduate to external product framing at future Ruslan ack, or dissolve if superseded by industry terminology.

**Critic flag: enforcement gap.** There is currently no automated mechanism that prevents Smart AI from appearing on external materials. The D25 Company-as-Code principle [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D25] and the /lint infrastructure [src:CLAUDE.md] together make an automated enforcement check technically possible: a /lint rule that flags "Smart AI" appearing in any file outside `swarm/`, `agents/`, `decisions/` directories would catch unauthorized external placement. This is an open question per §10 below (Q4 — Reification risk operational check). Until such a signal exists, the only enforcement gate is Ruslan's direct review.

---

## 6. Delivery Mechanism (Narrative-Infrastructure, Not Product Delivery)

Smart AI is delivered as a narrative frame through the agents and artefacts that produce Jetix-facing materials.

**Internal narrative carriers.** The manager agent and philosophy-expert apply the category-frame in synthesis tasks. The crazy-agent [src:CLAUDE.md §Agent Roster] is the appropriate carrier for exploratory Smart AI conceptual work — testing whether the framing holds under edge cases. The knowledge-synth agent applies it when synthesizing cross-direction materials. Brigadier integrates narrative consistency across canonical swarm output: when a section of a canonical document describes the Jetix portfolio, the Smart AI framing should appear consistently or not at all, never inconsistently. [src:swarm/lib/shared-protocols.md §1 wiki write protocol]

**Integration with educational stack.** Phase 3+ educational products (§3.7 Educational direction in this deep-dive) may include a "Smart AI category introduction" module. This is where the phones-to-smartphones analogy gets its first licensed external expression — as educational content, not product branding. The Apache 2.0 licensing model for Foundation educational content (L6 Alliance Option C [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md §2]) means this module would be openly available as a conceptual framework, not as a Jetix product name.

**Human oversight gate.** Ruslan approves any Smart AI external-facing reference per D29-deferred status. This is an architect-orbit function [src:decisions/JETIX-VISION.md §3 architect-orbit non-delegatable]: strategy and taste are Ruslan-only. The philosophy-expert critic function is to flag any inadvertent external-promotion drift in swarm output — this is the epistemic discipline contribution.

---

## 7. Competitive Positioning (Category-Level)

**The alternative category names in market use:**

"AI Agent" has achieved near-total commoditization in 2025-2026. Every vendor calls its product an AI agent. The term no longer carries discriminating information. Smart AI's advantage over "AI Agent" framing is specificity: the observable traits (context-preservation / memory-retention / project-assistance) are more specific than "agentic."

"AGI" is an over-claim that Ruslan explicitly rejects via D2: *«Jetix = amplifier, not replacement»* [src:decisions/JETIX-PHILOSOPHY.md §2]. Smart AI is the correct epistemic alternative to AGI-framing: it names a category that is ambitious without being triumphalist, specific without being falsely precise.

"Copilot" is Microsoft-branded and carries the connotation of human-pilot + AI-copilot, which preserves the amplifier-not-replacement framing but is unavailable as an unowned term. Smart AI is the unowned-category equivalent.

"Cognitive AI" and "Reasoning AI" are model-centric: they describe properties of the underlying AI model, not properties of the AI system (which includes governance, memory, provenance, and query-filtering). Smart AI can name a system that uses current models but is categorically different in its architecture.

**Why the framing works when it works.** The phones-to-smartphones analogy is culturally embedded, non-technical, and maps to a lived experience of category transition that most target ICPs have personally witnessed. It positions the claim at the right level of abstraction: not "we have better technology" (model-level claim), but "we are building for the next generation of AI use" (category-level claim). The four observable anchors (D25/D17/D13/D28) give the category claim verifiable content when challenged. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D25-D28]

**Critic-mode risk register.** The following risks are not marketing concerns; they are epistemic risks to the framing's coherence. Each requires explicit acknowledgment.

*Risk 1: Term commoditization.* "Smart AI" as a phrase is not owned and not uncommon. If multiple vendors adopt "Smart AI" as generic marketing language, the category claim loses its discriminating power. The Popper falsifiability test: this risk is refuted if competitor adoption of "Smart AI" language does not occur by €200K gate; it is confirmed if multiple competitors are using the term without Jetix having established the category anchor first. No measurement protocol for this risk currently exists — this is an open question (Q5 below).

*Risk 2: Reification drift.* The risk Ruslan named explicitly: treating Smart AI as a product over time, through accumulated informal usage, until the internal/external boundary erodes. The mechanism is gradual: team members start using "Smart AI" in client materials because it appears in internal documents; clients start asking about "the Smart AI product"; the term acquires product connotations without any explicit D29 decision. This is the most significant operational risk of the Smart AI narrative, and it is not addressed by the current framing alone. The Kuhnian observation: the paradigm shift from "Smart AI as category descriptor" to "Smart AI as product name" would happen through accumulated usage, not through a single decision event.

*Risk 3: Cross-lingual ambiguity.* "Smart AI" in Russian reads as an Anglicism: "умный ИИ" is the natural Russian translation but lacks the brand resonance. In German, "Smarte KI" is possible but syntactically awkward. If Jetix serves German Mittelstand clients (P1A primary [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md §2]), the English term may create unnecessary friction. This is an unresolved question about cross-lingual consistency (Q2 in §10 below).

*Risk 4: AGI adjacency misread.* Some audiences will hear "Smart AI" and map it to "smarter AI" → "AGI direction." This risks violating D2 amplifier-not-replacement framing by implication even when the explicit framing is correct. The defense is: always pair "Smart AI" with the observable-traits definition (context-preserving / memory-retaining / project-assistive) in any exploratory usage. The bare phrase alone is insufficient.

---

## 8. Evolution Per Gate

**Phase 0 → G1 (€0 → €50K, current):** Smart AI exists as internal vocabulary and this drafted section of the deep-dive document. Not on public materials. Used in internal discussions when team members (swarm agents) need a category frame for the portfolio. The phones-to-smartphones analogy is available as a conceptual shorthand in early-sales conversations where the full four-anchor explanation would be premature. [src:decisions/JETIX-SYSTEM-OVERVIEW.md §5 trajectory table G1]

**G1 → G2 (€50K → €200K):** Smart AI may appear in educational and thought-leadership content as a category framing. If Ruslan publishes thought-leadership blog posts about the AI category shift (consistent with the Philosopher and Teacher archetypes' natural content interest), Smart AI framing is appropriate there as category analysis, not product branding. Still NOT on product pages, service descriptions, or pitch decks. The boundary is: educational/analytical = permitted; commercial/positional = not permitted without D29. [src:decisions/JETIX-SYSTEM-OVERVIEW.md §5 G2]

**G2 → G3 (€200K → €1M):** The L6 Alliance Option C (Foundation non-profit upstream + Jetix-Corp proprietary downstream per [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md §2]) creates a legitimate external surface for Smart AI as a category concept. The Jetix Foundation may publish "Smart AI methodology" as an Apache 2.0 educational reference. This is the category concept's first controlled external appearance — as an educational framework contributed to the commons, not as a Jetix product name. At this gate, D29 re-evaluation is appropriate: does "Smart AI" resonate with Foundation community members? Is it being adopted or ignored?

**G3 → G4 ($1M → $100M):** Ruslan re-evaluates D29 status with empirical data accumulated across G2→G3. The decision criterion should be explicit (see Q1 in §10). If the category language has been adopted in educational contexts and resonates with the expanded ICP base, D29 promotion is justified. If the industry has converged on different terminology, Smart AI dissolves. Either outcome is epistemically sound; both are preferable to an undecided status persisting indefinitely. [src:decisions/JETIX-SYSTEM-OVERVIEW.md §5 G4]

**G4 → G5 ($100M → $100B → $1T):** At this horizon, the category designation becomes operationally irrelevant in one of two ways: either "Smart AI" has been adopted industry-wide and become generic (like "smartphone" became a common noun), in which case it no longer functions as Jetix-specific positioning; or it has been superseded by newer category language. In either case, Jetix's brand at this scale rests on operational track record, not on category-naming. [src:decisions/JETIX-SYSTEM-OVERVIEW.md §5 G5 USB-C framing]

The Kuhnian model (P2 — paradigm shift, §2.4 of this agent's core) applies here: Smart AI is an intra-paradigm category descriptor during the current AI expansion phase. When the next paradigm shift occurs (as it inevitably will, given the speed of AI development), Smart AI language may name the prior paradigm in retrospect, the way "feature phone" names the pre-smartphone generation in retrospect. Jetix's long-run positioning via D20 USB-C [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §USB-C reinforcement] operates at a level of abstraction that survives paradigm shifts; Smart AI does not need to.

---

## 9. Cross-Direction Dependencies — Smart AI as Portfolio Unifier

The Smart AI narrative's most important function is portfolio coherence: it gives all 8 operational directions a common conceptual parent. Without it, the 9 directions read as a diversified portfolio of unrelated bets. With it, they read as 8 instantiations of one category-level infrastructure play.

**§3.1 AI Consulting for Complex Tasks.** Internally: "Jetix provides Smart AI consulting — we deploy the category correctly for your specific business context." This framing elevates the consulting offer from "AI implementation help" to "category-adoption guidance." The distinction matters: a client buying AI implementation help is buying a service; a client adopting the Smart AI category is making an infrastructure bet. The latter conversation justifies premium pricing and long-term retainer relationships. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §2 AI Consulting row]

**§3.2 Продюсерский центр.** Smart AI applied to content production: AI-enhanced content pipelines with context-preservation (each client's content history informs future production) and memory-retention (the system accumulates the client's voice, style, audience data over time). This is "AI-produced content as Smart AI application" — not a generic content tool but a content system that learns the operator.

**§3.3 USB-C Integration Services.** The alignment is the closest: USB-C Integration = Smart AI infrastructure deployed privately on client servers. The client gets a Smart AI system (context-preserving / memory-retaining / project-assistive) that runs on their hardware under their data sovereignty. This direction is the most concrete instantiation of the Smart AI category claim and provides the best demonstration case for the phones-to-smartphones analogy. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §USB-C reinforcement]

**§3.4 Matchmaker Platform.** Smart AI coordination layer: humans and AI specialists are matched at the right level of abstraction. The context-preservation trait is critical here — a matchmaker platform that forgets previous matches and resets with each session is not Smart AI; one that accumulates coordination history and improves match quality over time is. D27 Fork-and-Merge [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D27] gives the matchmaker platform its evolutionary mechanism: successful coordination patterns are merged back to canonical.

**§3.5 Secure Network.** Smart AI community: a quality-gated peer network of Smart AI practitioners and operators. The framing shifts the Secure Network from "another professional community" to "the peer network for people building with and deploying the Smart AI category." This is the community that exists at the intersection of the category shift — the practitioners who are navigating the phones-to-smartphones moment in AI.

**§3.6 YouTube-Analyzer SaaS.** Smart AI applied to competitive intelligence: the YouTube-analyzer is a category extension demonstration. It shows that Smart AI architecture (context-preserving, memory-retaining, query-driven per D28 [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28]) can be applied to intelligence gathering, not just to internal knowledge management. This is important for the category claim: Smart AI is general-purpose infrastructure, not a specific use-case solution.

**§3.7 Educational Products + Investor Programs + Grant Hunting.** This is the direction most directly carrying the Smart AI narrative outward. "Smart AI methodology" as an Apache 2.0 educational framework (G2→G3 per L6 Alliance Option C) is the first authorized external expression of the category. The educational direction is also the natural home for the phones-to-smartphones analogy: in training materials, it explains the category shift; in methodology documentation, it grounds the design decisions.

**§3.8 Tokens / ICO.** Smart AI ecosystem token: governance and specialist compensation at infrastructure scale. The framing positions the token not as crypto speculation but as a coordination instrument for Smart AI infrastructure contributors. This is the weakest Smart AI framing connection of the 8 — tokens can exist for many kinds of infrastructure and the Smart AI category claim adds limited discriminating value here. The critic flags this: if tokens are eventually implemented (Phase 3+, per [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md §3 row 8]), the Smart AI connection should be established through the D27 fork-and-merge governance model, not through the token mechanism itself.

**Unifying thread.** Smart AI narrative allows Jetix to describe 9 directions as ONE category-bet rather than 9 separate products. This has two epistemic benefits: (1) it makes the portfolio more coherent to explain to sophisticated interlocutors who ask "why these 9?"; (2) it creates a falsifiable category claim — if "Smart AI" is a real category, then the 8 directions should all share the four observable traits (D25/D17/D13/D28). If any direction lacks those traits, it either needs to acquire them or it does not belong in the Smart AI category, which would be a genuine discovery about portfolio coherence. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §4 Interfaces]

---

## 10. Open Questions (Philosophy-Critic Lens)

The following questions are open epistemic questions — not rhetorical or decorative. Each has a falsifiable resolution condition. They are preserved as genuine philosophical tensions in the Smart AI narrative, per the dissent-preservation mandate (E-5).

**Q1: Promotion to D29 — under what empirical evidence?** Ruslan's verbatim statement defers the D29 decision [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §Smart AI verbatim]. The open question is not whether to promote (that is Ruslan's decision) but what evidence would be relevant to the decision. Candidate signals: (a) educational content using Smart AI framing receives positive engagement from ICPs who were not primed with the framing; (b) early-sales conversations where Smart AI framing was used show higher conversion to further discussions than conversations where it was absent; (c) Jetix Foundation community members adopt "Smart AI" as self-description without being prompted. Without a declared evidence threshold, the D29 deferral risks persisting indefinitely through inertia.

**Q2: Cross-lingual consistency.** "Smart AI" in Russian-language contexts reads as a deliberate Anglicism. "Умный ИИ" is the literal translation but lacks the category-level resonance. In German-language Mittelstand conversations (P1A primary [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md §2 constraint 2]), neither "Smart AI" nor "Smarte KI" functions cleanly. The question is whether Jetix standardizes on English "Smart AI" across all linguistic contexts as a proper noun (like "iPhone" or "Android" — not translated), or whether the category concept is translated while the Jetix brand stays in English. This is unresolved and will become operationally significant at G1→G2 when early-sales conversations with German-speaking Mittelstand clients begin.

**Q3: Dissolution scenario — when and what ends Smart AI narrative?** The narrative has no sunset condition beyond vague "industry convergence on other terminology." This is epistemically insufficient: a claim with no falsification condition cannot be retired in a principled way. The critic recommends declaring a sunset review point — at G3 ($1M revenue gate), conduct a structured review: has "Smart AI" been adopted in external educational content? Has industry usage converged on a different term? If neither question has a clear yes, the narrative should be formally retired rather than left as an indefinitely-deferred D29 candidate.

**Q4: Reification risk operational check.** Is there a /lint signal for Smart AI appearing on external-facing material without Ruslan ack? The D25 Company-as-Code principle [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D25] makes such a signal technically feasible: a lint rule checking for "Smart AI" appearing in files under directories conventionally used for external materials (any `public/`, `brand/`, `pitches/`, or generated landing page files) would be an automated enforcement gate. Without this, the internal/external boundary relies entirely on human review and informal convention — which is insufficient at scale per D25 discipline.

**Q5: Philosophy-scientific claim test — amplifier boundary.** D2 Philosophy establishes "Jetix = amplifier, not replacement" [src:decisions/JETIX-PHILOSOPHY.md §2]. The question is whether the Smart AI category claim, as it becomes more familiar and casual in usage, inadvertently drifts toward replacement-language. The drift mechanism: "Smart AI helps you manage your projects" (amplifier) → "Smart AI manages your projects" (ambiguous) → "Smart AI replaces your project manager" (replacement). The first formulation is D2-compliant; the third violates it. The critic cannot monitor this drift in real-time, but the philosophy-expert can flag instances of D2-violating Smart AI language in any artefact that passes through critic-mode review. This is an ongoing epistemic obligation, not a one-time check. [src:decisions/JETIX-PHILOSOPHY.md §2; decisions/JETIX-SYSTEM-OVERVIEW.md §0 Smart AI internal label]

---

## Conformance Checklist (§3.1 of philosophy-expert core — critic mode)

| Check | Result | Evidence |
|---|---|---|
| Falsifier-named (Popper / AP-PHIL-1) | pass | Status claim falsified by observable external usage; category traits (D25/D17/D13/D28) each falsifiable independently |
| Paradigm-named on shift (Kuhn / AP-PHIL-2) | pass | Prior paradigm (generic AI tools) named; anomaly (context-less / memory-less AI) named; successor paradigm (Smart AI generation) named with observable traits |
| Mental-model + applicable conditions (Munger / AP-mental-model-out-of-context) | pass | Phones-to-smartphones analogy cited with applicable conditions (intuitive category shift) and inapplicable conditions (AGI-claim territory, D2 boundary) |
| Method declares what it is NOT (via-negativa) | pass | §5 explicit: NOT product branding; NOT D29; NOT landing page language; NOT pitch deck language |
| Dichotomy-of-control identified | pass | In-control: internal usage conventions, swarm output review, /lint implementation; Not-in-control: industry terminology convergence, competitor adoption of "Smart AI" phrase |
| Fallacy-named when named | pass | No unnamed fallacies; category-commoditization risk named without claiming fallacy where none present |
| Meta-claim grounded in object-level | pass | Every meta-claim (Smart AI as category) grounded in concrete object-level instances (D25/D17/D13/D28 observable traits; audio_529 verbatim) |

**Acceptance Predicate (Hamel-binary):** "All claims in this §3.9 draft carry an explicit falsifier per AP-PHIL-1 check AND the D29-not-granted status is preserved verbatim without drift toward product-branding language AND the four observable anchors (D25/D17/D13/D28) ground every category-level claim AND the audio_529 smartphone analogy is cited in its original framing without over-extension."

---

## Structured Return Packet

```yaml
summary: >
  §3.9 Smart AI Flagship Narrative draft complete. 9-item template applied (no Offer structure
  per direction-type = cross-phase internal narrative). Key epistemic preservation:
  D29-not-granted status maintained verbatim; four observable anchors (D25/D17/D13/D28) ground
  the category claim; audio_529 smartphone analogy preserved without over-extension; D2
  amplifier-not-replacement boundary explicitly policed; 5 open questions raised with
  falsification conditions; 1 dissent on enforcement gap preserved.

proposed_writes:
  - path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-philosophy-critic-§3.9-smart-ai.md"
    action: write
    status: completed

provenance:
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", section: "§Smart AI verbatim + D25/D28"}
  - {path: "reports/review_2026-04-24.md", section: "rows 808-811 audio_529"}
  - {path: "decisions/JETIX-VISION.md", section: "§4 D13 + §7 archetypes + §8 per-archetype angles"}
  - {path: "decisions/JETIX-PHILOSOPHY.md", section: "§2 D2 amplifier-not-replacement"}
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", section: "§0 TL;DR + §5 trajectory table"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md", section: "§1 + §2 Smart AI row"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md", section: "§2 + §3 row 9 + §6 anti-scope"}

confidence: high
confidence_method: >
  All source materials read. All claims traced to locked decisions or verbatim voice.
  Critic mode applied: AP-PHIL-1 falsifiability check run on every major claim.
  D2 amplifier boundary explicitly policed. D29 non-promotion preserved throughout.
  No invention beyond what sources support.

escalations: []

dissents:
  - position: "Smart AI framing may function as internal narrative while simultaneously drifting toward external product branding in practice — the internal/external boundary has no automated enforcement mechanism"
    held_by: philosophy-expert (critic observation)
    F: F3
    ClaimScope:
      holds_when: "no /lint signal for external Smart AI usage exists; only human review is the gate"
      not_valid_when: "a /lint rule per D25 is implemented and tracked"
    R:
      refuted_if: "a /lint signal is implemented and confirmed zero-false-positive across 2 cycles"
      receipt: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/ decisions log"
      accepted_if: "no /lint enforcement exists as of G1 gate review"
    reconciliation:
      method: "escalate to Ruslan HITL for D25-compatible enforcement mechanism decision"
      verdict: "preserve dissent; do not average into 'probably fine'"
```
