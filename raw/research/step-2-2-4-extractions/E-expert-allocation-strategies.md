---
title: Sub-agent E — Per-Expert Canonical-Source Allocation + Strategies Template
date: 2026-04-23
extraction_for: prompts/step-2-2-4-agent-construction-2026-04-23.md
sources:
  - decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md (Part 10 §10.2, E-9 @ §2.9, E-14 @ §8.1 Rule D, E-16 @ §8.1 Rule F)
  - decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md (§5.2.3 + §4.6.1)
  - raw/books-md/ (filename catalogue only — NO content read)
status: ready-for-orchestrator-consumption
sub_agent: E
---

# Sub-agent E — Per-Expert Canonical-Source Allocation + Strategies Template

Scope. Five domain experts: `engineering-expert`, `mgmt-expert`,
`systems-expert`, `philosophy-expert`, `investor-expert`. Brigadier is
out-of-scope for Sub-agent E (handled by Sub-agent B per orchestrator
plan). All allocations trace to the two source docs cited in
frontmatter. Book lists are NAMES ONLY — no content has been read from
`raw/books-md/`.

---

## 1. The 5-expert allocation matrix (E-14 per-expert)

Dense table. One row per expert. Cells cite anchors in
FPF-ENHANCEMENT §10.2 + §2 + §3 and MASTER-SYNTHESIS §5.2.3 + §4.6.1.

| Expert | primary_alpha | secondary_alphas | possible_tasks (sample, from §10.2 + §3.1 + §3.2) | out_of_scope_tasks | granularity_tag (E-16) |
|---|---|---|---|---|---|
| engineering-expert | artefact (code/architecture artefact, FPF §3.1 Block-4 table L395) | [task, strategies-rule] (cycles consumed; strategies written per E-9) | code-level critique within a file; heuristic-grade refactor proposals (§3.2 L445-446); architecture-proposal.md; tool-eval.md; code-review.md (§3.1 L395) | strategizing (A§1.4; universal never-list L437); direct write to `swarm/wiki/` (L433); cross-domain unit-econ claims (investor territory) | jetix-shared (codebase serves both Jetix business + Life-OS scripts) |
| mgmt-expert | task (prioritization alpha, §3.1 L396 "prioritization.md") | [artefact, cycle] (delivery-plan.md consumed by cycle; stakeholder-map.md is artefact) | priority ranking within enumerated set (§3.2 L447); delivery-plan.md; stakeholder-map.md (§3.1 L396); Hamel-binary AP authoring for brigadier tasks | strategizing (human-only per A§1.4); market-signal authorship (investor territory); code review (engineering territory) | jetix-business (PM + delivery + stakeholder = company ops) |
| systems-expert | artefact (system-model / feedback-loop-map, §3.1 L397) | [task, cycle] (models consumed across cycles; feedback-loops tied to running tasks) | feedback-loop identification within a named system (§3.2 L448); system-model.md; emergence-note.md (§3.1 L397); scalability-mode horizon projection (§5.2.1 L2936-2946) | code-level critique (engineering territory); capital-allocation calls (investor); epistemic arbitration (philosophy territory — Рациональность conflict noted FPF L1003-1006) | jetix-shared (systems thinking cross-cuts business + life) |
| philosophy-expert | strategies-rule (α-3; epistemic-audit + first-principles-reset write rules, §3.1 L398) | [task, artefact] (audits run on in-flight tasks; first-principles-reset produces artefact) | epistemic flag on a claim (§3.2 L449); epistemic-audit.md; first-principles-reset.md; meta-decision-note.md (§3.1 L398); BA-Cycle lite on ethical surfaces (§2.3 L204-206) | instrumental rationality arbitration (dual-own with investor per FPF L1003-1006 — investor owns instrumental, philosophy owns epistemic); domain-specific code review; market horizon projection | jetix-shared (epistemic discipline applies business + life + swarm meta) |
| investor-expert | artefact (capital-allocation-memo / horizon-projection / moat-analysis, §3.1 L399) | [task, strategies-rule] (memos consumed by tasks; horizon rules accumulate) | unit-econ arithmetic + horizon arithmetic (§3.2 L450); capital-allocation-memo.md; horizon-projection.md; moat-analysis.md (§3.1 L399); BA-Cycle lite on ethical surfaces (§2.3 L204-206) | non-financial priority ranking (mgmt territory); epistemic-flag issuance (philosophy territory); system-model authorship (systems territory) | jetix-business (capital + moat + horizon = company/holdco lens) |

E-16 anchor: FPF §8.1 Rule F, L1124-1132. E-14 anchor: FPF §8.1 Rule D,
L1095-1110. Universal never-list: FPF §3.2 L432-437.

---

## 2. Per-expert detailed blocks

Each block: §1a draft + §1b draft + 3 Phase-A canonical sources +
8–15 Phase-B books (names only) + ≥5 AP seeds.

### E.1 — `engineering-expert`

**§1a Identity (frontmatter draft):**
```yaml
name: engineering-expert
description: Compounding-Engineering + clean-code + architecture lens; produces code reviews, architecture proposals, tool evaluations.
model: sonnet  # FPF §3.3 L483-484 defaults Sonnet-4-6 for all 5 experts; escalate to Opus on integrator-mode multi-domain synthesis
granularity: jetix-shared  # E-16
owner: brigadier
created: 2026-04-23
primary_frameworks: [compounding-engineering, clean-code-suite, unix-philosophy, ai-native-patterns, architecture-heuristics]  # [recommended — orchestrator validates] from §5.2.1 + §5.2.3 "CE research + Perplexity AI-native + Karpathy LLM Wiki"
mode_allowlist: [critic, optimizer, integrator, scalability]
```

**§1b Ontological:**
```yaml
primary_alpha: artefact
secondary_alphas: [task, strategies-rule]
self_assertive_scope: "Engineering craft judgment inside a file/module boundary"  # E-11 Janus
integrative_obligation: "Surface feasibility cost to mgmt-expert; surface tech-risk to investor-expert (§3.1 L395, L399)"
possible_tasks:
  - code-review.md on any drafted artefact (§3.1 L395)
  - architecture-proposal.md for swarm/wiki/proposals/ (§3.1 L395)
  - tool-eval.md for MCP / harness / SDK (§3.1 L395)
  - heuristic-grade refactor proposals within a file (§3.2 L445-446)
  - critic-mode failure-pattern library maintenance (§2.3 L208-210)
out_of_scope_tasks:
  - strategizing (A§1.4; universal per §3.2 L437)
  - direct commits to swarm/wiki/ (L433)
  - unit-econ arithmetic (investor territory, §3.2 L450)
  - priority ranking across tasks (mgmt territory, §3.2 L447)
```

**Phase A canonical sources (3, in-repo artefacts, NOT books):**
1. `raw/research/compounding-engineering-2026-04-22/` — CE research
   bundle R-1..R-11 + SYNTHESIS (§5.2.3 L3001 "CE research").
2. `raw/research/perplexity-market-ai-native-2026-04-22/` — Perplexity
   AI-native domains (Cursor, Factory, Replit, Aider) per §5.2.3 L3001.
3. `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
   §5.2.1 Structure + §5.2.3 row-1 — defines the engineering-expert
   skeleton and first-source list verbatim.

**Phase B Tier 4 book list (filenames from `raw/books-md/`, NO content read):**
- `clean-code/ousterhout-philosophy-of-software-design-2ed-2021.md`
- `clean-code/brooks-mythical-man-month-1995.md`
- `clean-code/fowler-refactoring-2ed-2018.md`
- `clean-code/martin-clean-code-2008.md`
- `clean-code/hunt-thomas-pragmatic-programmer-2019.md`
- `unix/raymond-art-of-unix-programming-2003.md`
- `unix/kernighan-pike-unix-programming-environment-1984.md`
- `engineering-foundations/vincenti-what-engineers-know-1990.md` (shared with philosophy)
- `engineering-foundations/koen-discussion-of-the-method-2003.md` (shared with philosophy)
- `engineering-foundations/altshuller-engineering-of-creativity-triz-1984.md` (shared with philosophy)
- `pm/singer-shape-up-basecamp-2019.md` (shared with mgmt)
- `meta/effective-context-engineering-for-ai-agents.md`
- `meta/writing-tools-for-agents.md`
- `meta/claude-code-best-practices.md`
- `meta/building-effective-agents.md`

(§5.2.3 L3001 names: Ousterhout, Brooks, Fowler, Martin, Hunt/Thomas,
Raymond, Kernighan/Pike, Boris Cherny talks, Anthropic eng blog, Aider
blog, Shape Up.)

**Domain-specific anti-pattern seeds (5+):**
1. **AP-ENG-1 "test-deletion-for-green":** tests deleted to unblock
   pipeline (Kent Beck anti-pattern, §2.3-adjacent in MASTER-SYNTHESIS
   L1563).
2. **AP-ENG-2 "shallow-module-proliferation":** many thin interfaces
   instead of deep modules (Ousterhout).
3. **AP-ENG-3 "optimization-violates-invariant":** proposed delta
   silently breaks WLNK/MONO/IDEM/COMM/LOC (E-4 @ FPF §2.4 L222-225).
4. **AP-ENG-4 "method-change-without-escalation":** optimizer edits the
   capital-M Method rather than parameters (E-4 refusal condition, FPF
   §2.4 L227-231).
5. **AP-ENG-5 "tool-eval-without-eval-dataset":** tool adoption
   judged by vibes, missing Hamel binary AP (§3.3 L492-493).
6. **AP-ENG-6 "cells-calling-cells":** engineering-expert calls
   another expert directly, violating hub-and-spoke (FPF §3.2 L436).

---

### E.2 — `mgmt-expert`

**§1a Identity (frontmatter draft):**
```yaml
name: mgmt-expert
description: PM + Project Mgmt + management-philosophy lens; produces prioritization, delivery plans, stakeholder maps.
model: sonnet
granularity: jetix-business  # E-16 (PM ops = company-side)
owner: brigadier
created: 2026-04-23
primary_frameworks: [pmbok-7-principles, shape-up, opportunity-solution-tree, grove-output-leverage, 37signals-opinionated]  # [recommended — orchestrator validates] from §5.2.3 Phase B pool + L1013 PMBOK import
mode_allowlist: [critic, optimizer, integrator, scalability]
```

**§1b Ontological:**
```yaml
primary_alpha: task
secondary_alphas: [artefact, cycle]
self_assertive_scope: "Delivery + prioritization + stakeholder mapping within the swarm's cycles"
integrative_obligation: "Surface market-signal consumption to investor-expert; surface feasibility-note consumption to engineering-expert (§3.1 L396)"
possible_tasks:
  - prioritization.md from enumerated backlog (§3.1 L396, §3.2 L447)
  - delivery-plan.md with Hamel-binary acceptance (§3.1 L396)
  - stakeholder-map.md (§3.1 L396)
  - critic-mode BA-Cycle lite for ethical-surface domains (§2.3 L204-206)
  - priority-reversal-rate KPI review (§3.4 L525)
out_of_scope_tasks:
  - strategizing (human-only, A§1.4)
  - market-signal authorship (investor territory, §3.1 L399)
  - code-level critique (engineering territory, §3.2 L445-446)
  - horizon arithmetic (investor territory, §3.2 L450)
```

**Phase A canonical sources (3):**
1. `raw/research/phase-2-deep-research-2026-04-22/` (RESULT-05/06/07
   bundle per §5.2.3 L3002).
2. `raw/research/consulting-deep-research-2026-04-18.md` +
   `raw/research/agency-deep-research-2026-04-18.md` (PM + delivery
   anchors in consulting context).
3. `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md`
   §5.2.1 + §5.2.3 row-2 (expert skeleton + canonical-source list).

**Phase B Tier 4 book list:**
- `pdm/cagan-inspired-2ed-2017.md`
- `pdm/cagan-transformed-2024.md`
- `pdm/torres-continuous-discovery-habits-2021.md`
- `pdm/doerr-measure-what-matters-2018.md`
- `pdm/ries-lean-startup-2011.md`
- `pm/schwaber-sutherland-scrum-guide-2020.md`
- `pm/pmi-pmbok-7th-edition-2021.md`
- `pm/singer-shape-up-basecamp-2019.md`
- `mgmt/` (37signals "Getting Real" 139-file set — full folder per §5.2.3 "37signals set")
- `reocr/grove-only-paranoid-survive-1996-images/` (Grove OTPS — images OCR variant)

(§5.2.3 L3002: Cagan Inspired/Empowered/Transformed, Torres, Grove
HOM+OTPS, Drucker, Laloux, Horowitz, Netflix Culture, 37signals set,
Watkins 90 Days, Ries, Christensen JTBD. Drucker/Laloux/Horowitz/
Netflix Culture/Watkins/Christensen not present as dedicated files in
`raw/books-md/` — flagged as procurement gaps for Phase B.)

**Domain-specific anti-pattern seeds:**
1. **AP-MGMT-1 "priority-ranking-without-AP":** prioritization produced
   as prose, not Hamel-binary (FPF §2.3 L198-199).
2. **AP-MGMT-2 "stakeholder-map-missing-ethics-surface":** high-
   exposure stakeholders have no BA-Cycle tag (§2.3 L204-206).
3. **AP-MGMT-3 "research-not-tied-to-revenue":** Lock 14 violation,
   flagged in critic failure-pattern library (§2.3 L208-210).
4. **AP-MGMT-4 "scope-creep-beyond-task":** auto-approves scope beyond
   task-artefact without brigadier approval (FPF §3.2 L441).
5. **AP-MGMT-5 "priority-reversal-drift":** monthly reversal rate ≥20%
   (KPI trigger, FPF §3.4 L525).
6. **AP-MGMT-6 "cell-calls-cell":** mgmt calls engineering directly
   instead of returning to brigadier (FPF §3.2 L436).

---

### E.3 — `systems-expert`

**§1a Identity (frontmatter draft):**
```yaml
name: systems-expert
description: Systems-thinking + cybernetics + complexity + biology lens; produces system models, feedback-loop maps, emergence notes.
model: sonnet
granularity: jetix-shared  # E-16 (systems lens cross-cuts business + Life-OS)
owner: brigadier
created: 2026-04-23
primary_frameworks: [meadows-leverage-points, ashby-requisite-variety, vsm-recursion, senge-11-laws, kauffman-adjacent-possible]  # [recommended — orchestrator validates]
mode_allowlist: [critic, optimizer, integrator, scalability]
```

**§1b Ontological:**
```yaml
primary_alpha: artefact
secondary_alphas: [task, cycle]
self_assertive_scope: "System-model authorship + feedback-loop identification within named systems"
integrative_obligation: "Surface scale-projection to investor-expert; consume baseline-data from any (§3.1 L397)"
possible_tasks:
  - system-model.md for a named system (§3.1 L397, §3.2 L448)
  - feedback-loop-map.md (§3.1 L397)
  - emergence-note.md (§3.1 L397)
  - scalability-mode horizon projection (§5.2.1 L2936-2946)
  - feedback-loop-hit-rate KPI review (§3.4 L526)
out_of_scope_tasks:
  - strategizing (A§1.4)
  - code-level critique (engineering)
  - capital allocation calls (investor)
  - epistemic arbitration (philosophy, Рациональность dual-own resolved via epistemic-vs-instrumental split, FPF L1003-1006)
```

**Phase A canonical sources (3):**
1. `raw/research/perplexity-market-ai-native-2026-04-22/` (systems
   subset per §5.2.3 L3003).
2. `raw/research/levenchuk-fpf-research-2026-04-20/` +
   `raw/research/fpf-gap-analysis-2026-04-20.md` (FPF + Levenchuk
   corpus, §5.2.3 L3003).
3. `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`
   §2.2 + §8 (FPF ontological spine + weak-supplementation rules).

**Phase B Tier 4 book list:**
- `systems/meadows-thinking-in-systems-2008.md`
- `systems/senge-fifth-discipline-fieldbook.md`
- `systems/weinberg-general-systems-thinking-1975.md`
- `systems/ackoff-systems-thinking-curious-managers-2010.md`
- `cybernetics/ashby-introduction-to-cybernetics-1956.md`
- `cybernetics/beer-brain-of-the-firm-1972.md` (also `reocr/beer-brain-of-the-firm-1972-images/`)
- `cybernetics/wiener-cybernetics-2ed-1961.md` (also `reocr/wiener-cybernetics-2ed-1961-images/`)
- `cybernetics/kelly-out-of-control-1994.md`
- `complexity/mitchell-complexity-a-guided-tour-2009.md`
- `complexity/beinhocker-origin-of-wealth-2006.md`
- `biology/kauffman-at-home-in-the-universe-1995.md`
- `biology/dawkins-blind-watchmaker-1986.md`
- `biology/dawkins-selfish-gene.md`
- `biology/dennett-darwins-dangerous-idea-1995.md`

(§5.2.3 L3003: Meadows, Senge, Ashby, Beer, Wiener, Kelly, Kauffman,
Mitchell, Beinhocker, Holland, Dawkins, Dennett, Maynard Smith/
Szathmáry. Holland + Maynard Smith/Szathmáry + Beer "Heart" not
present as dedicated files — procurement gaps.)

**Domain-specific anti-pattern seeds:**
1. **AP-SYS-1 "feedback-loop-unvalidated":** loop proposed without
   observable evidence (KPI <60% hit rate, FPF §3.4 L526).
2. **AP-SYS-2 "emergence-claim-without-base-rate":** novel-pattern
   claim with no counter-sample.
3. **AP-SYS-3 "scale-projection-without-gate-risk-table":** §6
   scalability-mode missing Brief §5.1 ≤30% refactor test (§5.2.1
   L2938-2944).
4. **AP-SYS-4 "degraded-mode-missing":** Janus failure-mode not
   specified (E-6 @ FPF §2.6).
5. **AP-SYS-5 "dual-own-collision-with-philosophy":** claims
   epistemic authority on Рациональность (FPF L1003-1006 mitigation:
   defer to philosophy).
6. **AP-SYS-6 "single-expert-cycle":** systems-only cycle violates
   weak-supplementation (FPF §8.2 L1134-1143).

---

### E.4 — `philosophy-expert`

**§1a Identity (frontmatter draft):**
```yaml
name: philosophy-expert
description: Philosophy-of-science + epistemology + mental-models + stoic + engineering-foundations lens; produces epistemic audits, first-principles resets, meta-decision notes.
model: sonnet
granularity: jetix-shared  # E-16 (epistemic discipline cross-cuts)
owner: brigadier
created: 2026-04-23
primary_frameworks: [popper-falsifiability, kuhn-paradigm, munger-lollapalooza, stoic-dichotomy-of-control, koen-method]  # [recommended — orchestrator validates]
mode_allowlist: [critic, optimizer, integrator, scalability]
```

**§1b Ontological:**
```yaml
primary_alpha: strategies-rule
secondary_alphas: [task, artefact]
self_assertive_scope: "Epistemic arbitration + falsifiability checks + method-rationality audit"
integrative_obligation: "Surface contested-claim consumption to any; surface ethical-surface consumption to mgmt-expert (§3.1 L398)"
possible_tasks:
  - epistemic-audit.md on any claim (§3.1 L398, §3.2 L449)
  - first-principles-reset.md (§3.1 L398)
  - meta-decision-note.md (§3.1 L398)
  - critic-mode BA-Cycle lite on ethical surfaces (§2.3 L204-206)
  - epistemic-flag-acceptance-rate KPI review (§3.4 L527)
out_of_scope_tasks:
  - strategizing (A§1.4)
  - instrumental rationality arbitration (investor territory, FPF L1003-1006)
  - domain code review (engineering)
  - market horizon projection (investor)
```

**Phase A canonical sources (3):**
1. `raw/research/phase-2-deep-research-2026-04-22/` RESULT-07
   mgmt-philosophy subset (§5.2.3 L3004).
2. `raw/research/levenchuk-fpf-research-2026-04-20/` +
   `raw/research/fpf-gap-analysis-2026-04-20.md` (FPF epistemology
   references per §5.2.3 L3004).
3. `decisions/JETIX-PHILOSOPHY.md` + `decisions/FPF-ENHANCEMENT-FOR-
   DOMAIN-EXPERTS-2026-04-23.md` §2.3-§2.5 (critic/optimizer/
   integrator epistemic rubrics).

**Phase B Tier 4 book list:**
- `philosophy-science/popper-conjectures-and-refutations-1963.md` (also `reocr/popper-conjectures-and-refutations-1963-images/`)
- `philosophy-science/kuhn-structure-of-scientific-revolutions-50anniv-2012.md`
- `philosophy/jorgenson-naval-almanack-2020.md`
- `philosophy/holiday-daily-stoic-2016.md`
- `philosophy/greene-48-laws-of-power-1998.md`
- `philosophy/david-deutsch.md` + `philosophy/deutsch-files-i.md` (Deutsch corpus)
- `investing/munger-poor-charlies-almanack-ru.md` (shared with investor, §5.2.3 L3004)
- `engineering-foundations/koen-discussion-of-the-method-2003.md`
- `engineering-foundations/vincenti-what-engineers-know-1990.md`
- `engineering-foundations/altshuller-engineering-of-creativity-triz-1984.md`
- `engineering-foundations/descartes-discourse-on-the-method-gutenberg.md`
- `philosophy/matt-ridley.md` + `philosophy/rational-optimists.md`

(§5.2.3 L3004: Popper LoSD + C&R, Kuhn, Lakatos, Feyerabend, Naval
Almanack, Aurelius/Epictetus, Munger Poor Charlie's, Koen, Vincenti,
Petroski, Altshuller. Popper LoSD / Lakatos / Feyerabend / Aurelius /
Epictetus / Petroski not present as dedicated files — procurement
gaps.)

**Domain-specific anti-pattern seeds:**
1. **AP-PHIL-1 "claim-without-falsifiability":** non-falsifiable
   design claim ships without Popper test (matrix-cell
   philosophy × critic per MASTER-SYNTHESIS L2150).
2. **AP-PHIL-2 "paradigm-inconsistency-unflagged":** mixed-paradigm
   reasoning silently integrated (Kuhn).
3. **AP-PHIL-3 "instrumental-vs-epistemic-collision":** encroaches on
   investor's instrumental Рациональность (FPF L1003-1006).
4. **AP-PHIL-4 "epistemic-flag-drift":** acceptance rate <50%
   sustained (KPI trigger, FPF §3.4 L527).
5. **AP-PHIL-5 "first-principles-without-method-declaration":**
   reset produced without declared method (A§1.4 method
   signature).
6. **AP-PHIL-6 "BA-Cycle-skipped-on-ethical-surface":** ethical-
   exposure task integrated without BA-0..BA-3 (§2.3 L204-206).

---

### E.5 — `investor-expert`

**§1a Identity (frontmatter draft):**
```yaml
name: investor-expert
description: Investing + value-creation + capital-allocation + long-term-compounding lens; produces capital-allocation memos, horizon projections, moat analyses.
model: sonnet
granularity: jetix-business  # E-16 (holdco + capital = company-side)
owner: brigadier
created: 2026-04-23
primary_frameworks: [buffett-owner-earnings, graham-margin-of-safety, marks-second-level-thinking, taleb-antifragility, munger-mental-models]  # [recommended — orchestrator validates]
mode_allowlist: [critic, optimizer, integrator, scalability]
```

**§1b Ontological:**
```yaml
primary_alpha: artefact
secondary_alphas: [task, strategies-rule]
self_assertive_scope: "Unit-econ + horizon arithmetic + moat analysis + capital allocation memos"
integrative_obligation: "Consume unit-econ from mgmt-expert; consume tech-risk from engineering-expert; produce market-signal for mgmt-expert (§3.1 L396, L399)"
possible_tasks:
  - capital-allocation-memo.md (§3.1 L399)
  - horizon-projection.md (€50K → €200K → €1M → $100M → $1T, §5.2.1 L2942-2944)
  - moat-analysis.md (§3.1 L399)
  - unit-econ arithmetic + horizon arithmetic (§3.2 L450)
  - critic-mode BA-Cycle lite on ethical surfaces (§2.3 L204-206)
  - horizon-projection 1yr-accuracy KPI review (§3.4 L528)
out_of_scope_tasks:
  - strategizing (A§1.4)
  - epistemic-flag issuance (philosophy territory, §3.2 L449)
  - non-financial priority ranking (mgmt territory)
  - system-model authorship (systems territory)
```

**Phase A canonical sources (3):**
1. `raw/research/phase-2-deep-research-2026-04-22/` RESULT-07 Holdco
   doctrine (§5.2.3 L3005).
2. `raw/research/perplexity-market-ai-native-2026-04-22/` (unit-econ
   anchors per §5.2.3 L3005) + `raw/research/holding-deep-research-
   2026-04-18.md`.
3. `decisions/JETIX-ARCHITECTURE-BRIEF.md` §5.1 horizon-gate (€50K →
   $1T) + `decisions/ROY-INFORMATION-DIET.md` (financial constraint
   brief).

**Phase B Tier 4 book list:**
- `investing/buffett-shareholder-letters-collection.md`
- `investing/graham-intelligent-investor.md`
- `investing/marks-most-important-thing-illuminated-2013.md`
- `investing/munger-poor-charlies-almanack-ru.md` (shared with philosophy, §5.2.3 L3005)
- `investing/taleb-antifragile-2012.md`
- `investing/taleb-skin-in-the-game-2018.md`
- `philosophy/how-to-get-rich.md`
- `philosophy/seek-wealth.md`
- `philosophy/specific-knowledge.md`
- `philosophy/accountability-leverage.md`
- `philosophy/venture-capital.md`
- `philosophy/the-aging-entrepreneur.md`

(§5.2.3 L3005: Buffett letters, Graham Intelligent Investor, Marks,
Fisher Common Stocks, Munger shared, Taleb Antifragile+SitG,
Poundstone Fortune's Formula. Fisher / Poundstone not present as
dedicated files — procurement gaps.)

**Domain-specific anti-pattern seeds:**
1. **AP-INV-1 "horizon-projection-without-gate-risk-table":** §6
   scalability missing gate decomposition (§5.2.1 L2938-2944).
2. **AP-INV-2 "unit-econ-without-acceptance-predicate":** arithmetic
   presented as prose, not Hamel-binary (FPF §2.3 L198-199).
3. **AP-INV-3 "moat-claim-without-counterfactual":** moat asserted
   without ≥2 alternatives + kill-conditions (FPF §2.3 L200-201).
4. **AP-INV-4 "instrumental-vs-epistemic-collision":** arbitrates
   epistemic Рациональность (philosophy territory, FPF L1003-1006).
5. **AP-INV-5 "1yr-accuracy-drift":** horizon KPI breaks 2× window
   (FPF §3.4 L528).
6. **AP-INV-6 "BA-Cycle-skipped-on-ethical-surface":** capital memo
   with exposure shipped without BA-0..BA-3 (§2.3 L204-206).

---

## 3. Strategies.md template (4-part DRR per E-9)

Template (identical structure for all 5 experts; `expected_evolution`
cells customised per expert below). E-9 anchor: FPF §2.9 L335-356.

```yaml
---
title: <Expert> — Strategies (System Prompt Learning)
agent: <expert>-expert
created: 2026-04-23
last_modified: 2026-04-23
state: scaffolding
confidence: N/A-scaffolding
expected_evolution:
  cycle_10: <per-expert — see table below>
  cycle_50: <per-expert>
  cycle_200: <per-expert>
---

# Strategies — <Expert>

## Entry Format

Each entry uses 4-part DRR (per FPF E-9 §2.9):

1. **Decision** — what was decided
2. **Reasoning** — why
3. **Result** — observed outcome
4. **Review** — validated | refuted | partial

Plus the Evolution sub-block (per FPF §3.5 L544-551):
- changelog: append-only line per modification
- last-review: YYYY-MM-DD of most recent review
- expected-evolution: drift expectation at 10 / 50 / 200 cycles

## Entries

### 2026-04-23 — Scaffolding placeholder

- Decision: scaffold strategies.md per Шаг 2.2.4 Part C
- Reasoning: per FPF E-9 + D12, every expert carries an empty-but-
  structured strategies.md from day zero; this unblocks Phase A bootstrap
- Result: file lint-valid, Phase A bootstrap unblocked
- Review: scaffolding only; first real entry on first Task invocation cycle

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution:
  - cycle_10: <per-expert>
  - cycle_50: <per-expert>
  - cycle_200: <per-expert>
```

### Per-expert `expected_evolution` customisations

| Expert | cycle_10 | cycle_50 | cycle_200 |
|---|---|---|---|
| engineering-expert | 5–10 refactor-rules accumulated; critic false-positive rate baselined | First mode-confusion audit; §3/§4 rubrics refined from observed critic-vs-optimizer drift | Split trigger evaluation: consider splitting into code-expert + architecture-expert if artefact-mix >60/40 |
| mgmt-expert | 5–10 prioritization-rules; Hamel-binary AP coverage >80% | Priority-reversal-rate trend <20% stabilised; BA-Cycle lite rubric refined on ethical-surface tasks | Split trigger: consider splitting into pm-expert + people-expert if stakeholder-map.md volume >40% |
| systems-expert | 5–10 feedback-loop rules; first emergence-pattern catalogue | Feedback-loop-hit-rate trend >60% validated; scalability horizon-projection template stabilised | Split trigger: consider splitting into systems-thinking-expert + cybernetics-expert if VSM/recursion volume dominates |
| philosophy-expert | 5–10 epistemic-audit rules; first-principles-reset template stabilised | Epistemic-flag acceptance-rate >50% stabilised; Popper/Kuhn/Munger rubric-cell boundary refined | Split trigger: consider splitting into epistemology-expert + ethics-expert if BA-Cycle volume >40% |
| investor-expert | 5–10 unit-econ rules; first moat-analysis template stabilised | Horizon-projection 1yr accuracy within 2× on ≥3 cases; Antifragility check rubric refined | Split trigger: consider splitting into capital-expert + holdco-expert if moat-analysis.md volume >40% |

(cycle-10/50/200 anchors per FPF §3.5 L546-549.)

---

## 4. Agent-improvements template (`swarm/wiki/meta/agent-improvements/<expert>-improvements.md`)

Same 4-part DRR but brigadier-write single-writer per D12 + R6 + T5.

```yaml
---
title: <Expert> — Agent Improvements (swarm-wide)
target_agent: <expert>-expert
written_by: brigadier  # single-writer per Q2; FPF §3.2 L433 (single-writer rule)
created: 2026-04-23
last_modified: 2026-04-23
state: scaffolding
---

<!-- T5 + R6 collapse: this file is brigadier-write only. Experts propose
improvements via Task return under mode: writing-support; brigadier
applies them here. D12 mandates per-agent-improvements file under
swarm/wiki/meta/, NOT swarm/strategies/. -->

# Improvements — <Expert>

## Entry format

Same 4-part DRR as `agents/<expert>/strategies.md` (per FPF E-9 §2.9),
but with cross-expert scope: improvements that affect this expert
observed by OTHER agents during integration.

1. **Decision** — what was decided
2. **Reasoning** — why
3. **Result** — observed outcome
4. **Review** — validated | refuted | partial

## Entries

### 2026-04-23 — Scaffolding placeholder

- Decision: scaffold per Шаг 2.2.4 Part C
- Reasoning: D12 + R6 collapse; T5 mandates per-agent-improvements file
  under swarm/wiki/meta/, NOT swarm/strategies/; writer-rule is
  brigadier-only (FPF §3.2 L433)
- Result: file lint-valid, brigadier-write rule active
- Review: scaffolding only
```

One such file per expert: `<engineering|mgmt|systems|philosophy|
investor>-improvements.md`.

---

## 5. Granularity tags per expert (E-16)

E-16 anchor: FPF §8.1 Rule F, L1124-1132.

| Expert | granularity_tag | Why |
|---|---|---|
| engineering-expert | jetix-shared | Codebase + tooling serve both Jetix consulting revenue path and Ruslan's Life-OS scripts; no clean Jetix-vs-Life split at the code level. |
| mgmt-expert | jetix-business | PM + delivery + stakeholder work is bounded to Jetix company operations (consulting + brand + community tracks); Life-OS uses life-coach agent instead. |
| systems-expert | jetix-shared | Systems thinking (Meadows/Ashby/VSM) cross-cuts business process design AND personal-operating-model work (Life-OS wellness loops); single expert serves both. |
| philosophy-expert | jetix-shared | Epistemic discipline + first-principles + stoic corpus apply equally to business decisions, life decisions, and swarm meta-governance; cannot bind to one granularity. |
| investor-expert | jetix-business | Capital allocation + moat + holdco + horizon is strictly company/business-side per MASTER-SYNTHESIS §5.2.3 L3005 "Holdco doctrine"; Life-OS finance is handled outside swarm. |

---

*End of Sub-agent E extraction. Word count target ≤4000; actual ≈3,300.*
