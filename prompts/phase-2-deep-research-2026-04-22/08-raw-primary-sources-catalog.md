---
id: phase-2-08-raw-primary-sources-catalog
title: Raw Primary Sources Catalog (Bibliography Spec for Ruslan)
author: cloud-cowork
date: 2026-04-22
tool: NOT-Perplexity — this is a manual acquisition spec
priority: P1 (parallel to Perplexity runs; do while waiting)
audience: Ruslan — source-material to acquire into repo
status: ready-to-execute
---

# Primary Sources Catalog — Acquisition Spec

> **This is not a Perplexity prompt.** This is a bibliography Ruslan executes manually (or delegates to a cheap Haiku agent) to stockpile primary-source material in `raw/books-pm/` + `raw/articles/` so Phase 3 synthesis has cite-able material on hand.

## Execution model

For each item:

1. **Fetch the source** (download PDF / save HTML / capture full article + date + author)
2. **Convert to markdown** with YAML frontmatter matching the Jetix wiki schema (`id`, `title`, `author`, `date`, `source-url`, `type`, `topics`, `status: raw`)
3. **Save to the target path** listed per-item
4. **Optional /ingest later** — not required for Phase 2 (Phase 3 synthesizer will /ingest)

Priority tiers (do P1 first; P2 if time; P3 nice-to-have):

- **P1** = must-have primary source; cited directly in Files 05/06/07 Perplexity prompts; synthesis document will rely on it
- **P2** = important context; enriches synthesis
- **P3** = bonus; for long-horizon learning

Format for each entry below:

```
### N. Title — Author, Year
- Type / Format / Length
- URL or acquisition method
- Target save path
- Priority: P1/P2/P3
- Why it matters: 1-2 sentences
```

---

## Category 1 — Project Management

### 1. Shape Up — Ryan Singer (Basecamp), 2019
- Book / free online HTML / ~200 pages
- https://basecamp.com/shapeup (read free; also HTML/ePub/PDF downloads)
- Save to: `raw/books-pm/shape-up-basecamp-2019.md` (capture full text via HTML→MD conversion)
- Priority: **P1**
- Why: The defining non-sprint PM methodology for small teams; directly referenced in File 05 Perplexity prompt + Shape-Up-↔-CE synthesis question.

### 2. The Goal — Eliyahu M. Goldratt, 1984 (rev 1992, 2004)
- Business novel / Kindle + paperback / ~400 pages
- ISBN 978-0884271956 · Goodreads: https://www.goodreads.com/book/show/113934
- Save to: `raw/books-pm/the-goal-goldratt-1984.md` (personal summary + top 20 quotes — full text is copyrighted)
- Priority: **P2**
- Why: Theory of Constraints origin; bottleneck thinking applies directly to AI-native workflows where the bottleneck shifted.

### 3. Project to Product — Mik Kersten, 2018
- Book / ~250 pages
- ISBN 978-1942788393 · https://projecttoproduct.org
- Save to: `raw/books-pm/project-to-product-kersten-2018.md` (summary + Flow Framework extraction)
- Priority: **P2**
- Why: Flow Framework bridges enterprise PM and product-mode; relevant for Phase 2+ holding-shape.

### 4. Lean Software Development — Mary & Tom Poppendieck, 2003
- Book / ~200 pages · ISBN 978-0321150783
- Save to: `raw/books-pm/lean-software-development-poppendieck-2003.md` (summary + 7 principles verbatim)
- Priority: **P2**
- Why: The 7 Lean principles directly underpin later Kanban / Continuous Delivery / DevOps practice.

### 5. The Phoenix Project — Gene Kim et al., 2013
- Novel / ~350 pages · ISBN 978-0988262591
- Save to: `raw/books-pm/phoenix-project-kim-2013.md` (summary + Three Ways extraction)
- Priority: **P3**
- Why: DORA / DevOps origin-fiction; useful operational analog but more engineering than PM.

### 6. DORA Accelerate State of DevOps reports 2024, 2025, 2026
- Annual PDF reports from Google Cloud / DORA
- https://cloud.google.com/devops/state-of-devops/
- Save to: `raw/articles/dora-state-of-devops-2024.md`, `-2025.md`, `-2026.md`
- Priority: **P1**
- Why: Canonical measurement baseline; 2024-2026 reports increasingly covered AI-augmented delivery.

### 7. Linear Method — Linear team, 2020 onwards (living doc)
- Web / continuously updated
- https://linear.app/method
- Save to: `raw/articles/linear-method-complete-2026.md` (capture all pages as of April 2026)
- Priority: **P1**
- Why: The only PM methodology authored by a 2020s company explicitly for their own small-team AI-adjacent operating model.

---

## Category 2 — Product Management

### 8. Inspired: How to Create Tech Products Customers Love — Marty Cagan, 2008 (rev 2017)
- Book / ~350 pages · ISBN 978-1119387503
- Save to: `raw/books-pm/inspired-cagan-2017.md` (summary + top-15 chapters verbatim)
- Priority: **P1**
- Why: Canonical Silicon Valley Product Group doctrine; foundation for File 06.

### 9. Empowered: Ordinary People, Extraordinary Products — Cagan + Chris Jones, 2020
- Book / ~400 pages · ISBN 978-1119691297
- Save to: `raw/books-pm/empowered-cagan-jones-2020.md`
- Priority: **P1**
- Why: Empowered-product-team doctrine; required reading for Phase 2+ partnership-operator model.

### 10. Transformed: Moving to the Product Operating Model — Marty Cagan, 2024
- Book / ~400 pages · ISBN 978-1119697336
- Save to: `raw/books-pm/transformed-cagan-2024.md`
- Priority: **P1**
- Why: Cagan's 2024 update explicitly addressing modern (incl. AI-hint) transformations.

### 11. Continuous Discovery Habits — Teresa Torres, 2021
- Book / ~240 pages · ISBN 978-1736633304 · https://producttalk.org/continuous-discovery-habits/
- Save to: `raw/books-pm/continuous-discovery-habits-torres-2021.md`
- Priority: **P1**
- Why: OST (Opportunity Solution Tree) method + weekly-customer-contact discipline; directly cited File 06.

### 12. The Lean Startup — Eric Ries, 2011
- Book / ~320 pages · ISBN 978-0307887894
- Save to: `raw/books-pm/lean-startup-ries-2011.md`
- Priority: **P2**
- Why: MVP / Build-Measure-Learn — still referenced but showing age in AI-native contexts.

### 13. The Four Steps to the Epiphany — Steve Blank, 2005
- Book / ~400 pages · ISBN 978-0976470700
- Save to: `raw/books-pm/four-steps-epiphany-blank-2005.md`
- Priority: **P2**
- Why: Customer development origin; precursor to Lean Startup and product-market-fit thinking.

### 14. When Coffee and Kale Compete — Alan Klement, 2018
- Book / ~200 pages · Free PDF at https://www.whencoffeeandkalecompete.com
- Save to: `raw/books-pm/when-coffee-and-kale-klement-2018.md`
- Priority: **P2**
- Why: The most practitioner-actionable JTBD treatment; free online.

### 15. Measure What Matters — John Doerr, 2018
- Book / ~320 pages · ISBN 978-0525536222 · Companion site: https://www.whatmatters.com
- Save to: `raw/books-pm/measure-what-matters-doerr-2018.md`
- Priority: **P1**
- Why: OKR canonical treatment; covers Grove→Google lineage relevant to File 07.

### 16. Radical Focus — Christina Wodtke, 2016 (rev 2021)
- Book / ~200 pages · ISBN 978-0996006033
- Save to: `raw/books-pm/radical-focus-wodtke-2021.md`
- Priority: **P2**
- Why: OKR-as-operating-system in small teams; more actionable than Doerr for solo-to-small.

### 17. Play Bigger — Al Ramadan, Dave Peterson, Christopher Lochhead, Kevin Maney, 2016
- Book / ~250 pages · ISBN 978-0062407610
- Save to: `raw/books-pm/play-bigger-lochhead-2016.md`
- Priority: **P2**
- Why: Category Design — relevant for Jetix's "USB-C positioning" (Decision 20).

### 18. Product-Led Growth — Wes Bush (ProductLed / OpenView), 2019
- Book / ~240 pages · Free PDF at https://productled.com/book
- Save to: `raw/books-pm/product-led-growth-bush-2019.md`
- Priority: **P2**
- Why: PLG canonical treatment; relevant for Phase 3+ productized-SaaS arm.

### 19. The Innovator's Dilemma — Clayton Christensen, 1997
- Book / ~280 pages · ISBN 978-1422197585
- Save to: `raw/books-pm/innovators-dilemma-christensen-1997.md`
- Priority: **P3**
- Why: Foundational; JTBD origin via Christensen; aged but referenced by every PM writer since.

---

## Category 3 — Management Philosophy

### 20. High Output Management — Andy Grove, 1983 (rev 1995)
- Book / ~260 pages · ISBN 978-0679762881
- Save to: `raw/books-pm/high-output-management-grove-1995.md` (full summary + Horowitz's annotations)
- Also capture: https://a16z.com/content/andy-groves-high-output-management/
- Priority: **P1**
- Why: Canonical management text; OKR origin; 1-on-1 + task-relevant-maturity taxonomy.

### 21. Only the Paranoid Survive — Andy Grove, 1996
- Book / ~210 pages · ISBN 978-0385483827
- Save to: `raw/books-pm/only-paranoid-survive-grove-1996.md`
- Priority: **P2**
- Why: Strategic inflection points — directly applicable to AI-era 2026 transitions.

### 22. The Effective Executive — Peter Drucker, 1967
- Book / ~180 pages · ISBN 978-0060833459
- Save to: `raw/books-pm/effective-executive-drucker-1967.md`
- Priority: **P1**
- Why: Drucker's most-referenced; knowledge-worker doctrine; 5 effective habits.

### 23. Managing Oneself — Peter Drucker (HBR article, 1999; republished as book 2008)
- Article / ~40 pages · Free HBR archive: https://hbr.org/2005/01/managing-oneself
- Save to: `raw/articles/managing-oneself-drucker-1999.md`
- Priority: **P1**
- Why: The single most relevant Drucker piece for solo-founder self-management.

### 24. The Practice of Management — Peter Drucker, 1954
- Book / ~400 pages · ISBN 978-0060878979
- Save to: `raw/books-pm/practice-of-management-drucker-1954.md` (summary only)
- Priority: **P3**
- Why: Historical canonical; MBO (Management by Objectives) origin.

### 25. Getting Real — Jason Fried + DHH (37signals), 2006
- Book / Free online HTML / ~200 pages
- https://basecamp.com/gettingreal
- Save to: `raw/books-pm/getting-real-37signals-2006.md` (capture full text)
- Priority: **P1**
- Why: Founding 37signals manifesto; direct precursor to Rework, Remote, Shape Up.

### 26. Rework — Jason Fried + DHH, 2010
- Book / ~280 pages · ISBN 978-0307463746
- Save to: `raw/books-pm/rework-37signals-2010.md`
- Priority: **P1**
- Why: Condensed 37signals operating philosophy.

### 27. Remote: Office Not Required — Jason Fried + DHH, 2013
- Book / ~256 pages · ISBN 978-0804137508
- Save to: `raw/books-pm/remote-37signals-2013.md`
- Priority: **P2**
- Why: Canonical remote-work treatment; Jetix is solo-remote by default.

### 28. It Doesn't Have to Be Crazy at Work — Jason Fried + DHH, 2018
- Book / ~240 pages · ISBN 978-0062874788
- Save to: `raw/books-pm/it-doesnt-have-to-be-crazy-37signals-2018.md`
- Priority: **P1**
- Why: Most recent 37signals operational doctrine; "calm company" framing — directly resonant with Jetix "anti-attention" principle (D2).

### 29. Powerful: Building a Culture of Freedom and Responsibility — Patty McCord, 2017
- Book / ~210 pages · ISBN 978-1939714091
- Save to: `raw/books-pm/powerful-mccord-2017.md`
- Priority: **P1**
- Why: Netflix HR / culture doctrine from the author.

### 30. No Rules Rules: Netflix and the Culture of Reinvention — Reed Hastings + Erin Meyer, 2020
- Book / ~320 pages · ISBN 978-1984877864
- Save to: `raw/books-pm/no-rules-rules-hastings-meyer-2020.md`
- Priority: **P1**
- Why: Talent density + informed captain + freedom-and-responsibility full treatment.

### 31. The Hard Thing About Hard Things — Ben Horowitz, 2014
- Book / ~300 pages · ISBN 978-0062273208
- Save to: `raw/books-pm/hard-thing-about-hard-things-horowitz-2014.md`
- Priority: **P1**
- Why: Wartime vs peacetime CEO; hard-truth management tactical advice.

### 32. What You Do Is Who You Are — Ben Horowitz, 2019
- Book / ~272 pages · ISBN 978-0062871336
- Save to: `raw/books-pm/what-you-do-horowitz-2019.md`
- Priority: **P2**
- Why: Culture-as-actions — directly applicable to building a methodology-as-company (Jetix D1).

### 33. Reinventing Organizations — Frederic Laloux, 2014
- Book / ~380 pages · https://www.reinventingorganizations.com (PDF available)
- Save to: `raw/books-pm/reinventing-organizations-laloux-2014.md`
- Priority: **P2**
- Why: Teal / self-management canonical; Jetix partnership-network shape is teal-adjacent.

### 34. The First 90 Days — Michael D. Watkins, 2003 (rev 2013)
- Book / ~290 pages · ISBN 978-1422188613
- Save to: `raw/books-pm/first-90-days-watkins-2013.md`
- Priority: **P2**
- Why: Onboarding / role-transitions — applicable to solo-founder wearing 10 hats + new roy onboarding.

### 35. The Almanack of Naval Ravikant — Eric Jorgenson (compiler), 2020
- Book / Free PDF at https://www.navalmanack.com
- Save to: `raw/books-pm/almanack-naval-jorgenson-2020.md`
- Priority: **P2**
- Why: Solopreneur philosophy distilled; leverage + specific knowledge + code/media leverage.

### 36. Anything You Want — Derek Sivers, 2011
- Book / ~80 pages · https://sive.rs/a
- Save to: `raw/books-pm/anything-you-want-sivers-2011.md`
- Priority: **P3**
- Why: Solo-operator lean business philosophy, short and dense.

### 37. Useful Not True — Derek Sivers, 2024
- Book / ~100 pages · https://sive.rs/ut
- Save to: `raw/books-pm/useful-not-true-sivers-2024.md`
- Priority: **P3**
- Why: 2024 epistemic philosophy applicable to AI-era "truth with citations" pattern.

### 38. Zero to Sold — Arvid Kahl, 2020
- Book / ~370 pages · https://thebootstrappedfounder.com/zero-to-sold/
- Save to: `raw/books-pm/zero-to-sold-kahl-2020.md`
- Priority: **P2**
- Why: Bootstrapped-founder primary source; directly addresses Jetix-shape solo journey.

---

## Category 4 — Holding Company Doctrine

### 39. Berkshire Hathaway Annual Letters — Warren Buffett, 1977-2024
- Annual PDFs · https://www.berkshirehathaway.com/letters/letters.html
- Save to: `raw/books-pm/berkshire-letters-2020-2024.md` (5 most recent condensed; earlier letters summarized in a single meta-file)
- Priority: **P2**
- Why: Canonical holding-company operator doctrine; capital allocation + ownership-without-operation.

### 40. Constellation Software Annual Letters — Mark Leonard, 2008-2020
- Annual PDFs · https://www.csisoftware.com/investor-relations
- Save to: `raw/books-pm/constellation-letters-2008-2020-compilation.md` (single compilation)
- Priority: **P2**
- Why: Acquire-and-hold doctrine for software businesses; Mark Leonard stopped writing after 2020 but letters remain the canonical small-cap-holdco playbook.

### 41. The Outsiders — William Thorndike, 2012
- Book / ~280 pages · ISBN 978-1422162675
- Save to: `raw/books-pm/outsiders-thorndike-2012.md`
- Priority: **P1**
- Why: 8 unconventional CEO case studies (Singleton, Buffett, Malone, Henry Singleton) — the definitive capital-allocator canon.

### 42. Poor Charlie's Almanack — Charlie Munger, 2005 (rev eds)
- Book / ~500 pages · Stripe Press edition: https://stripepress.com/book/poor-charlies-almanack
- Save to: `raw/books-pm/poor-charlies-almanack-munger-2005.md` (mental-models extraction)
- Priority: **P2**
- Why: Multi-disciplinary mental-models — applicable directly to Jetix FPF practice.

### 43. Andrew Wilkinson — Tiny operating-model content, 2020-2026
- Podcast interviews (Invest Like the Best, Twenty Minute VC, Founders) + Tiny.com content
- Save to: `raw/articles/tiny-wilkinson-compilation-2026.md`
- Priority: **P2**
- Why: Modern micro-holdco operating-model; directly analog to Jetix Phase 3+ shape.

---

## Category 5 — CE-Adjacent Additional Reading

### 44. The Pragmatic Programmer — Andrew Hunt + David Thomas, 1999 (20th Anniversary Ed 2019)
- Book / ~350 pages · ISBN 978-0135957059
- Save to: `raw/books-pm/pragmatic-programmer-hunt-thomas-2019.md`
- Priority: **P2**
- Why: Engineering-craft canonical; many CE principles trace here (DRY, don't-live-with-broken-windows, tracer bullets).

### 45. A Philosophy of Software Design — John Ousterhout, 2018 (rev 2021)
- Book / ~190 pages · ISBN 978-1732102217
- Save to: `raw/books-pm/philosophy-software-design-ousterhout-2021.md`
- Priority: **P2**
- Why: Complexity minimization doctrine; "deep modules" = capability-capsule design intuition.

### 46. Test-Driven Development By Example — Kent Beck, 2002
- Book / ~240 pages · ISBN 978-0321146533
- Save to: `raw/books-pm/test-driven-development-beck-2002.md`
- Priority: **P2**
- Why: TDD founding text; verification-loop → CE $100 rule lineage.

### 47. Extreme Programming Explained — Kent Beck, 1999 (2nd Ed 2004)
- Book / ~190 pages · ISBN 978-0321278654
- Save to: `raw/books-pm/extreme-programming-explained-beck-2004.md`
- Priority: **P2**
- Why: Pair programming / small releases / customer collaboration — all survive AI-native translation.

### 48. Refactoring — Martin Fowler, 1999 (2nd Ed 2018)
- Book / ~440 pages · ISBN 978-0134757599
- Save to: `raw/books-pm/refactoring-fowler-2018.md`
- Priority: **P3**
- Why: Refactoring catalog; AI-augmented refactoring is a 2025-2026 trend.

---

## Category 6 — Multi-Agent Theory + Agentic Systems

### 49. Multiagent Systems: Algorithmic, Game-Theoretic, Logical Foundations — Shoham + Leyton-Brown, 2008
- Book / ~530 pages · Free PDF http://www.masfoundations.org
- Save to: `raw/books-pm/multiagent-systems-shoham-leyton-brown-2008.md` (key chapters summary)
- Priority: **P2**
- Why: Canonical academic treatment; contract-net, auction, coordination formally defined.

### 50. An Introduction to Multiagent Systems — Michael Wooldridge, 2009 (2nd Ed)
- Book / ~480 pages · ISBN 978-0470519462
- Save to: `raw/books-pm/intro-multiagent-systems-wooldridge-2009.md` (summary only; text copyright)
- Priority: **P3**
- Why: Pre-LLM-era agent theory; still the best conceptual foundation.

### 51. Karpathy LLM Wiki — Andrej Karpathy, April 2026 (living Gist)
- Gist / ~2,000 lines (as of 2026-04)
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Save to: `raw/articles/karpathy-llm-wiki-gist-2026-04.md`
- Priority: **P1**
- Why: The single most important 2026 conceptual piece on knowledge management for LLM agents.

### 52. Karpathy — Software Is Changing (Again) — YC AI Startup School, June 2025
- Video transcript + slides · https://www.youtube.com/watch?v=LCEmiRjPEtQ
- Save to: `raw/articles/karpathy-software-changing-again-yc-2025-06.md`
- Priority: **P1**
- Why: The LLM OS intellectual framework canonical reference.

### 53. Karpathy — Year in Review 2025 — https://karpathy.bearblog.dev/year-in-review-2025/
- Blog post / capture full text
- Save to: `raw/articles/karpathy-year-review-2025-12.md`
- Priority: **P2**
- Why: 2025 retrospective; context for 2026 direction.

### 54. Anthropic — Building Effective Agents, December 2024
- https://www.anthropic.com/engineering/building-effective-agents
- Save to: `raw/articles/anthropic-building-effective-agents-2024-12.md`
- Priority: **P1**
- Why: Foundational agent-pattern reference; still the best official framework.

### 55. Anthropic — How we built our multi-agent research system, June 2025
- https://www.anthropic.com/engineering/built-multi-agent-research-system
- Save to: `raw/articles/anthropic-multi-agent-research-system-2025-06.md`
- Priority: **P1**
- Why: Primary source for multi-agent production architecture lessons.

### 56. Anthropic — How AI Is Transforming Work at Anthropic, December 2025
- https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- Save to: `raw/articles/anthropic-how-ai-transforming-work-2025-12.md`
- Priority: **P1**
- Why: 132 engineers × 200K transcripts; the most rigorous AI-native engineering-org dataset.

### 57. Anthropic — Agentic Misalignment, June 2025
- https://www.anthropic.com/research/agentic-misalignment
- Save to: `raw/articles/anthropic-agentic-misalignment-2025-06.md`
- Priority: **P1**
- Why: Empirical misalignment data; Claude Opus 4 blackmail scenarios 96%.

### 58. Walden Yan — Don't Build Multi-Agents (Cognition Labs)
- https://cognition.ai/blog/dont-build-multi-agents (verify URL current)
- Save to: `raw/articles/cognition-dont-build-multi-agents.md`
- Priority: **P1**
- Why: The strongest argument against multi-agent — must be in corpus for balanced view.

### 59. Cemri et al. — Why Do Multi-Agent LLM Systems Fail? (MAST) — arXiv:2503.13657, March 2025
- Paper / ~30 pages
- https://arxiv.org/abs/2503.13657
- Save to: `raw/articles/mast-cemri-2025-03.md`
- Priority: **P1**
- Why: THE 14 failure-mode taxonomy; required for File 03 synthesis.

### 60. Kim et al. — Science of Scaling Agent Systems — arXiv:2512.08296 (Dec 2025)
- Paper / ~40 pages
- https://arxiv.org/abs/2512.08296
- Save to: `raw/articles/kim-science-scaling-agents-2025-12.md`
- Priority: **P1**
- Why: 180-experiment evidence base for 17.2× error amplification, Rule of 4.

### 61. Hamel Husain — Your AI Product Needs Evals, March 2024
- https://hamel.dev/blog/posts/evals/
- Save to: `raw/articles/hamel-husain-evals-2024-03.md`
- Priority: **P1**
- Why: Definitive eval practitioner guide.

### 62. Every Inc. — Master Plan Part II — Dan Shipper, September 2025
- https://every.to/on-every/every-s-master-plan-part-ii
- Save to: `raw/articles/every-master-plan-part-ii-2025-09.md`
- Priority: **P1**
- Why: Every Inc. operating model as published by Dan Shipper.

### 63. Boris Cherny — Claude Code Engineering Talks + Blog 2024-2026
- YouTube (AI Engineer Summit) + anthropic.com posts
- Save to: `raw/articles/boris-cherny-claude-code-compilation-2026.md` (curated compilation)
- Priority: **P1**
- Why: Claude Code principal architect voice; 10 design principles.

### 64. Temporal — Of Course You Can Build Dynamic AI Agents with Temporal, November 2025
- https://temporal.io/blog/of-course-you-can-build-dynamic-ai-agents-with-temporal
- Save to: `raw/articles/temporal-dynamic-ai-agents-2025-11.md`
- Priority: **P2**
- Why: Durability-layer canonical; explains OpenAI Codex / Replit / Cursor runtime.

### 65. CrewAI — Lessons from 2 Billion Agentic Workflows, January 2026
- https://blog.crewai.com/lessons-from-2-billion-agentic-workflows/
- Save to: `raw/articles/crewai-2billion-workflows-2026-01.md`
- Priority: **P1**
- Why: Largest published production dataset on multi-agent systems.

### 66. Vectorize.io — mem0 vs Zep Comparison, March 2026
- https://vectorize.io/articles/mem0-vs-zep
- Save to: `raw/articles/vectorize-mem0-vs-zep-2026-03.md`
- Priority: **P2**
- Why: Best direct comparison of the two leading memory systems.

### 67. OX Security — MCP Supply Chain Audit, April 2026
- https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/
- Save to: `raw/articles/ox-security-mcp-audit-2026-04.md`
- Priority: **P1** (time-sensitive)
- Why: Before deploying any MCP server; flags systemic RCE.

### 68. Dev.to — The AI Agent That Cost $47,000 — Utibe Okodi, March 2026
- https://dev.to/utibe_okodi_339fb47a13ef5/the-ai-agent-that-cost-47000-while-everyone-thought-it-was-working-1lg6
- Save to: `raw/articles/47k-agent-incident-okodi-2026-03.md`
- Priority: **P1**
- Why: Cost-blowup post-mortem canonical citation.

### 69. Justin Welsh — My Complete $10M Journey, June 2025
- https://www.justinwelsh.me/newsletter/my-10m-journey
- Save to: `raw/articles/justin-welsh-10m-journey-2025-06.md`
- Priority: **P1**
- Why: Primary source for solo-founder milestone pacing and revenue mix.

### 70. Andrew Dunn — How to Productize Your AI Consulting Offer in 2026, January 2026
- https://newsletter.andrewdunn.co/p/how-to-productize-your-ai-consulting-offer-in-2026
- Save to: `raw/articles/andrew-dunn-productize-ai-consulting-2026-01.md`
- Priority: **P1**
- Why: Most actionable productization blueprint for current stage.

---

## Category 7 — Canonical Essays and Short Pieces

### 71. Paul Graham — Do Things That Don't Scale, July 2013
- http://paulgraham.com/ds.html
- Save to: `raw/articles/pg-do-things-that-dont-scale.md`
- Priority: **P1**
- Why: Solo-founder manual-first doctrine; Jetix Phase 1 operating mode.

### 72. Paul Graham — How to Do Great Work, July 2023
- http://paulgraham.com/greatwork.html
- Save to: `raw/articles/pg-great-work-2023-07.md`
- Priority: **P2**
- Why: Condensed craft-and-career doctrine.

### 73. Paul Graham — Writes and Write-Nots, October 2024
- http://paulgraham.com/writes.html
- Save to: `raw/articles/pg-writes-write-nots-2024-10.md`
- Priority: **P2**
- Why: AI-era writing + thinking framing.

### 74. Karpathy — System Prompt Learning tweet thread, May 10 2025
- https://twitter.com/karpathy (archive the full thread)
- Save to: `raw/articles/karpathy-spl-2025-05.md`
- Priority: **P1**
- Why: The "3rd paradigm of LLM learning" framing; foundational for Jetix wiki+strategies pattern.

### 75. Jeff Bezos — 2004 Shareholder Letter (PowerPoint ban / 6-pager memo origin)
- https://www.sec.gov/Archives/edgar/data/1018724/000119312505070440/dex991.htm
- Save to: `raw/articles/bezos-2004-shareholder-letter-6pager.md`
- Priority: **P2**
- Why: Writing-culture origin; Stripe + Amazon both trace to this.

### 76. Bezos — Type 1 / Type 2 Decisions, 2015 Shareholder Letter
- https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm
- Save to: `raw/articles/bezos-type1-type2-decisions-2015.md`
- Priority: **P2**
- Why: Decision-reversibility framing relevant to AI-agent delegation taxonomy.

### 77. Steve Yegge — Platforms Rant (originally accidentally-public Google+, 2011)
- https://gist.github.com/chitchcock/1281611
- Save to: `raw/articles/yegge-platforms-rant-2011.md`
- Priority: **P3**
- Why: Bezos-API-mandate doctrine; useful analog for Jetix USB-C positioning.

### 78. Dan Luu — Various posts on engineering decisions, career, organizations
- https://danluu.com (compile top 10 posts)
- Save to: `raw/articles/dan-luu-compilation-top-10.md`
- Priority: **P2**
- Why: Counter-hype data-driven engineering-org commentary; high-signal.

### 79. Simon Willison — Various AI/agent posts 2024-2026
- https://simonwillison.net (compile top 20 AI posts)
- Save to: `raw/articles/simon-willison-ai-compilation-2024-2026.md`
- Priority: **P1**
- Why: The single most reliable independent commentator on LLM/agent systems; Lethal Trifecta coined.

### 80. Kieran Klaassen — Cora + Every CE public posts, 2024-2026
- https://every.to/@kieran (or wherever hosted)
- Save to: `raw/articles/kieran-klaassen-ce-compilation-2024-2026.md`
- Priority: **P1**
- Why: Kieran is the CE practitioner-author; direct primary source.

---

## Summary table — priority counts

| Category | P1 | P2 | P3 | Total |
|---|---|---|---|---|
| 1. Project Management | 2 | 3 | 1 | 6 (+ 1 multi-year DORA = 7) |
| 2. Product Management | 5 | 5 | 2 | 12 |
| 3. Management Philosophy | 7 | 6 | 2 | 15 (includes 20-38) |
| 4. Holding Company | 1 | 3 | 0 | 4 |
| 5. CE-Adjacent | 0 | 3 | 1 | 4 |
| 6. Multi-Agent + Agentic | 11 | 2 | 0 | 13 |
| 7. Canonical Essays | 4 | 4 | 2 | 10 |
| **Totals** | **30** | **26** | **8** | **65 items** |

(Meta count: 18 books + 15 books + 5 books for 6-Mutil = approx 30 books + 30 essays/posts = 60+, exceeds 15 books + 10 essays requirement — deliver in prioritized tiers.)

## Execution plan (parallel to Perplexity runs)

1. **Day 1** — Execute all P1 items (30 items). Budget: ~4-6 hours for a Haiku agent with web fetch capability, or 1 full work day of manual capture.
2. **Day 2-3** — Execute P2 items (26 items) as time permits while Perplexity runs.
3. **Backlog** — P3 items captured opportunistically; not blocker for Phase 3 synthesis.

Each captured file should have YAML frontmatter:

```yaml
---
id: <slug-based-on-filename>
title: <exact title>
author: <first-last>
date: <YYYY-MM-DD or YYYY for books>
source-url: <canonical URL>
type: book-summary | article | blog-post | paper | video-transcript
topics: [pm, product-mgmt, management-philosophy, ce, multi-agent, holding]
priority: P1|P2|P3
status: raw
captured-date: 2026-04-22+
---
```

## After acquisition

1. No /ingest yet — that's Phase 3 synthesis work
2. Flag Cloud Cowork when P1 tier is complete; synthesis can proceed
3. Track progress in `raw/books-pm/_inventory.md` (create on first capture)

---

*END SPEC 08 — Primary Sources Catalog*
