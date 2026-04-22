---
id: extraction-e-constraints-24-locks
title: Extraction E — Tier-2 constraint compliance matrix + 24 Locks + quality rubric
date: 2026-04-22
type: reference-extraction
role: compliance-check reference for master synthesis Parts 4-6
sources:
  - decisions/ROY-ALIGNMENT-2026-04-22.md
  - decisions/ROY-INFORMATION-DIET.md
  - raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md
  - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md
  - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md
  - decisions/JETIX-ARCHITECTURE-BRIEF.md
---

# Extraction E — Tier-2 Constraints Reference

Source shortcuts: PRE = `TENSIONS-PRE-RESOLVED.md`; ST2 = `TENSIONS-RESOLVED.md`; ST2B = `TENSIONS-RESOLVED-STAGE-2B.md`; Brief = `JETIX-ARCHITECTURE-BRIEF.md`; ALIGN = `ROY-ALIGNMENT-2026-04-22.md`; DIET = `ROY-INFORMATION-DIET.md`.

## A. 24 Locked Decisions — Canonical Table

| # | Title | Statement (verbatim or paraphrase-marked) | Source | Why locked | Swarm-design implication |
|---|---|---|---|---|---|
| 1 | Gentleman/Predator | "Gentleman inside / Predator outside." | PRE §D1 | Brand-identity formula Ruslan approved | Every swarm surface bifurcates tone/policy/access by observer-class |
| 2 | Solo-now-team-ready | "Solo-now-with-team-ready-scaffolding." | PRE §D2 | Must absorb 2nd/3rd pilot without refactor | Mailboxes/state/role-manifests multi-pilot Day 1; no `/home/ruslan/*` hard-codes |
| 3 | Closed/Open | "Closed outside / Open inside (team)." | PRE §D3 | Transparency inside, opacity outside | Outputs tiered (public/member/partner/core) |
| 4 | Name = Jetix | "Jetix (не Jackson) — name не меняется." | PRE §D4 | "Jackson/Джек" = speech-recognition artefact | Ingest canonicalises `Jackson\|Джек` → `Jetix` pre-persistence |
| 5 | Consulting-first | "Consulting-first Phase 1. Community попутно. Secure Network = Phase 2+ evolution." | PRE §D5 | Reconciles Note 1 + Note 2 as phased | Phase A prioritises consulting-pipeline; Secure Network = extensibility only |
| 6 | No advisors | "Anton/Vladislav/Rodion не ключевые. Убрать." | PRE §D6 | "Нет, они не ключевые" | No advisor/mentor slot in roster; no legacy-mentor dependency |
| 7 | Union archetypes | "Union — объединить оба списка, максимальное разнообразие." — 10 base; Brief §2 normalises to 11 (adds bloggers Stage 3) | PRE §D7; Brief §2 | Broad cast for Secure Network | Taxonomy supports 11-way metadata; ICP filter layers on top |
| 8 | Layered identity | "Jetix = layered identity — different faces per observer/phase." | PRE §D8 | Grammar of context-adaptive identity | Configurable face per observer+phase; outputs tag frame |
| 9 | Pain primary | "Pain-based primary + Opportunity-based secondary. Акцент на боль." | ST2 §D9/T1 | Layered outbound, not either/or | Content artefacts tag frame; TOF pain-default, mid/deep opportunity |
| 10 | EN+US first | "Phase 1 market = English + US. Germany Phase 2+." | ST2 §D10/T2 | US gives revenue scale; DE = legal home | Multi-jurisdiction (US CA AI regs + EU AI Act) supported |
| 11 | Consulting+Producer+Fund | "Продюсерский центр = Phase 1 core parallel consulting. Investment-fund = operating philosophy Day 1." | ST2 §D11/T3 | Resource distribution = investment | Resource-Allocation Engine first-class; decisions carry `expected_return`+`horizon`+`kill_criteria` |
| 12 | Smart+site+social-TOF | "Умные audience. Основа = сайт+шаблоны+видео+PDF. Соцсети на МАКСИМУМ как TOF." | ST2 §D12/T4 | Correction of "не создавать соцсеть" misread | Pipeline tags TOF/mid/deep; no Jetix-native social platform Phase 1 |
| 13 | Open surface / Closed core | "Open surface (results/frame/demos/templates) / Closed core (prompts/wiki/workflows/config)." | ST2 §D13/T5 | Refines D3 for methodology | Pipeline splits surface (auto-gen) vs core (access-gated); expert prompts = core |
| 14 | Revenue-instrumental research | "Phase 1 research только revenue-serving. Philosophy/bet/curiosity → park." | ST2 §D14/T6 | Servant, not master | Phase A scope-filtered; philosophy/scalability agents constrained Phase 1 |
| 15 | Revenue-gated spend | "Heavy-spend gated by revenue. Gates: $20-30K → €50K → €200K → €1M." | ST2 §D15/T7 | "Gated, not banned" | Cost enforcement at billing level; gate-state flag in governance |
| 16 | Phase 1 simple chat | "Phase 1 простой chat, invite-based, no formal anti-free-riding. Formal Phase 2+/3+." | ST2 §D16/T8 | Subscription = baseline-commitment filter | Minimal Phase 1 community adapter; extensions pre-wired dormant |
| 17 | Filesystem = SoT | "Filesystem = единственный authoritative source. Notion = collaboration/UI tool only." | ST2 §D17/T9 | Overrides CLAUDE.md prior "Notion external truth" | Swarm writes to git; any Notion sync one-way; commit after every stage |
| 18 | Productization | "Consulting risks mitigated через productization, не hours. Scale via products+templates+community." | ST2 §D18/T10 | "Ruslan ест свой food" | Pipeline outputs packaged artefacts; multi-tier pricing primitive |
| 19 | $1T Holding-Scale | "Jetix — мировой рекорд скорости $1T market cap. $100M → $100B → $1T." | ST2B §D19 | Engineering-faith, not hype | Schemas 10^3–10^6 entity Day 1; no boutique-scale shortcuts |
| 20 | USB-C + Enterprise-Fast | "USB-C level в AI+business-cooperation; structure = enterprise-fast." | ST2B §D20 | Neither slow-corporate nor chaotic-startup | Enterprise-grade ops; protocol/connector surfaces first-class |
| 21 | Matchmaker + Roy-Replication | "Jetix = partnership matchmaker + facilitator. Roy-out-of-10 replicable template." | ST2B §D21 | Network effects via roy coordination | Methodology-as-system exporter; matchmaker primitives; inter-roy protocol Phase 3+ |
| 22 | ICP 5-criteria + direction | "Startupper + azart + stable + adequate + upward-direction. Direction-of-life axis first-class." | ST2B §D22 | Quality filter on archetypes (vertical axis) | Membership engine: 5-criteria + direction; outreach agents apply filter |
| 23 | Token Option B | "Phase 2 internal non-transferable; Phase 3+ public — economic-claim only. Option B approved default." | ST2B §D23 | Preserves D3 membrane + enables liquidity | No governance/community-access rights bundled in Phase 3+ public token |
| 24 | Open-source research | "Phase 2+ activates OSS research direction. Core methodology остаётся closed per D13." | ST2B §D24 | Surface-layer research, not operational | Research splits open-publishable vs closed-operational; Phase A does NOT do OSS research |

## B. Operating Mode Specification

Both files compatible but differ on detail; contradictions flagged.

**Mode A — Full Auto.** Triggers (ALIGN §4): smoke tests / simple well-defined scope / validated patterns post-successful-Stage-Gated runs. DIET §1.5 adds: routine / low-stakes. Brigadier delegates → experts execute → brigadier synthesises → commit. Ruslan reviews final only.

**Mode B — Stage-Gated Interactive.** Triggers (ALIGN §4): architecture synthesis / strategy decisions / anything long-term. DIET §1.5 broadens to "strategic pivots / new patterns / anything touching 24 Locks." Key architectural-decision triggers (ALIGN §8): >1-month impact / trade-off between projects or resources / new framework proposal / agent or skill add-remove / cost escalation / conflict with 24 Locks. Non-triggers (ALIGN §8, continue without gate): research inventory / draft synthesis / cleanup-refactor / wiki-entry creation / routine reviews.

**Gate file pattern.** ALIGN §4: `decisions/AWAITING-APPROVAL-<topic>-<date>.md`. DIET §1.5: `stage-<N>-<name>-AWAITING-APPROVAL.md` + `stage-<N>-<name>-DECISION.md`. Contradiction flagged; synthesis must pick canonical.

**Gate content (ALIGN §4 mandatory):** context + options considered + recommendation + rationale + risk register.

**Approval + resume.** ALIGN §4: commit → push → pause (can continue non-blocking work) → Ruslan review → approves / redirects / drills-down → рой continues on approval signal. DIET §1.5 formalises four responses: **Approve** / **Redirect** (change direction or constraints) / **Drill-down** (deeper investigation of aspect) / **Abort** (halt and save current state).

**Mode selection = per-task.** Default for large architecture synthesis / first roy launch = Stage-Gated (ALIGN §4); default for Phase-A architecture work = Mode B (DIET §1.5).

## C. Matrix 5×4 Baseline

Source: ALIGN §§1–3.

**Team size (§1):** 5 domain experts + brigadier = 6 agents total. Not 9, not 10 separate.

**5 experts with canonical first-sources (§2 verbatim):**

| Agent | Domain | Canonical first-sources |
|---|---|---|
| engineering-expert | CE + clean code + unix + AI-native + architecture | Ousterhout, Brooks, Fowler, Martin, Hunt/Thomas, Karpathy, Boris Cherny, Anthropic engineering blogs, Aider, Cognition, 37signals, Shape Up, `compounding-engineering-2026-04-22/` R-1..R-11 + SYNTHESIS |
| mgmt-expert | Product + Project + mgmt philosophy | Cagan (Inspired, Transformed), Torres, Grove, Laloux, Horowitz, Drucker, 37signals, PMBOK, Shape Up, Netflix Culture, `phase-2-deep-research/RESULT-05/06/07` |
| systems-expert | Systems thinking + cybernetics + complexity + biology/evolution | Meadows, Senge, Ashby, Beer, Wiener, Kelly, Dawkins, Dennett, Kauffman, Mitchell, Beinhocker, Левенчук (3 files) |
| philosophy-expert | Philosophy of science + mental models + stoic + epistemology + eng foundations | Popper, Kuhn, Naval, Aurelius/Epictetus, Munger, Farnam Street, SEP, Descartes, Koen, Vincenti, Altshuller |
| investor-expert | Investing + value + capital allocation + compounding | Buffett letters, Graham, Marks, Munger, Taleb (Antifragile, Skin in the Game) |

**Brigadier (§2):** separate role, NOT matrix cell. Coordinator / task delegator / synthesis manager. Reads own `brigadier.md` prompt.

**4 role-modes (§3, orthogonal):** Critic (holes/adversarial) / Optimizer (cost/elegance/removal) / Integrator (coherent whole) / Scalability-architect (Phase 3 / $1T defense / anti-fragility).

**Matrix = 5 × 4 = 20 invocations (§3).** Same deep domain knowledge per mode → no dilution. Role-mode = framing lens, not separate KB.

**Invocation pseudocode (§3 verbatim):**
```
Task(
  agent: "systems-expert",
  mode: "critic" | "optimizer" | "integrator" | "scalability",
  context: {...}
)
```

**Prompt granularity (§5):** 1500–3000 lines per agent. Each prompt = research distillation + primary sources + role definition + mode-switching sections + integration protocols + per-mode few-shots.

**Cost model (§6):** Max subscription, NOT API. Ops: `unset ANTHROPIC_API_KEY` before each Claude Code launch; Max plan 20× active; `--dangerously-skip-permissions` OK in tmux; per-turn budget via Max limits; no $47K-incident risk.

**Compute target (§7):** Primary — server Claude Code (`ssh ruslan@100.99.156.28` → tmux), Opus 4.7 1M + extended thinking max, branch `claude/jolly-margulis-915d34`. Secondary (Cloud Cowork) — coordination / prompt-gen / review assist only.

## D. Phase A / B / C Recursive Pattern

Source: ALIGN §9.

**Phase A — Baseline Swarm Creation.** Claude Code reads Tier 1 deep + Tier 2 required + Tier 3 skim. **Tier 4 books NOT touched** (explicit — reserved as recursive self-improvement fuel). Output: `MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM` (20–30K words) + 5 expert prompts + brigadier prompt (1500–3000 lines each). Depth-within-scope, scope = Tier 1+2+3.

**Phase B — Recursive Self-Improvement.** First real task for baseline swarm. Swarm reads Tier 4 books (Ousterhout / Brooks / Fowler / Ashby / Beer / Kelly / Meadows / Cagan / Grove / Laloux / Shape Up / Karpathy wiki). Each expert deep-reads its domain through own lens. Swarm refines system prompts + coordination protocols. Output: `decisions/JETIX-SWARM-V2-SELF-IMPROVED-2026-04-XX.md` + updated agents.

**Phase C — Real Work.** After Phase B — real problem. Likely recursive synthesis Layer 1 meta-system + Layer 2 Jetix overlay per DIET. Exact scope TBD.

**Rationale (§9):** avoids overload (no 393-book drowning); leverages swarm's own capability (domain-lens deep reads > generic CC read); compound (Phase B reflects matrix synergy); measurable git delta.

**TBD in Шаг 2.1 (§10, verbatim):** communication channels (wiki stigmergic vs mailbox JSONL hybrid) / termination stack concrete (maxTurns, budget, verifier, HITL trigger) / recursive iteration pattern (convergence, max passes) / exact smoke-test design / skill roadmap finalisation / hooks+monitoring / memory+wiki write protocol (single-writer Phase 1 vs CRDT).

## E. Quality Criteria & Architect Questions

### E.1 10-axis scoring rubric (Brief §8.1 + §8.2)

| # | Axis | Measurement | Weight |
|---|---|---|---|
| 1 | Phase-1 readiness | % of §3.1 Phase-1 caps with concrete design + effort estimate < phase budget | 20% |
| 2 | Scale trajectory | 10× at each gate ≤30% rework (LoC + schema-migration per §5.1) | 15% |
| 3 | Foundation quality | All 8 §4 subsections with concrete schema/API/protocol | 15% |
| 4 | Locks compliance | Each lock → ≥1 component with citation. Uncited = axis ≤3 | 18% |
| 5 | Universality | B-test config/code ≥90%; C-test ≥3 use-cases; D-test grep 0 on `base/` | 10% |
| 6 | Operational simplicity | Founder-understandable + new-pilot onboardable ≤5 days | 10% |
| 7 | Cost efficiency | Per-agent-turn $; Phase-1 run-rate; >€800/mo = disqualifier | 0% (gate) |
| 8 | Resilience | Degraded-mode spec per critical subsystem; MTTR ≤60min | 5% |
| 9 | Security posture | Tier enumeration (surface/member/partner/core) + auto-gen + GDPR Art.22 gate | 5% |
| 10 | Innovation | Novel protocol/schema beyond OME/FPF/ADR inheritance | 2% |

**Hard floor:** any axis <3 = disqualified. **Disqualifiers (§8.3):** §6 hard-constraint violation / §7 anti-pattern present / §10 question unaddressed / lock uncited / >€800/mo without justification.

### E.2 Architect Questions (Brief §10)

**Count note:** Brief §10 lists **15** questions (Q1–Q15). The briefing's "16" claim is inaccurate vs source.

- Q1 Repository structure — base/overlay (`jetix-os/` + `jetix-company/`, hooks, MHT-1 path)
- Q2 Agent roster reconciliation (12→11, renames, 5 Ruslan sub-roles, `message.schema.json` enum)
- Q3 Integration points inventory (~12 systems R/W × auth × fallback × gate; DPA per integration)
- Q4 Scaling mechanism Phase-1→$1T without rewrite (per-subsystem scale-path table, sharding)
- Q5 Data architecture — wiki + atoms + provenance (3-layer, 9 types, 25K HARD, ingest v2)
- Q6 Privacy/security — membrane + GDPR + EU AI Act (tier ACL, auto-gen surface, Art.22(3) flow)
- Q7 API architecture — multi-provider + cost control (router, compute-contract, ≤€800/mo)
- Q8 Token economy Option B membrane preservation (state-machine, rights-separation schema)
- Q9 Matchmaker algorithm — 4 modules (graph / algorithm / contract-fixation / metrics)
- Q10 Roy-replication formalisation (kit contents, lifecycle, inter-roy protocol, kill criteria)
- Q11 Content pipeline TOF/mid/deep (pipeline graph, archetype rendering, deep-ACL)
- Q12 Dashboard — OME-style metrics (schema v1/v2/v3, render, alerts)
- Q13 Escalation routing — founder vs AI layer (class taxonomy, SLA, Art.22(3))
- Q14 Onboarding architecture — pilot ramp ≤7 days (checklist, permissions, migration audit)
- Q15 USB-C protocol layer (taxonomy, message-schema set, verification)

### E.3 16 Anti-Patterns (Brief §7 verbatim titles)

AP-1 Notion-as-primary-store · AP-2 Hour-billing-only · AP-3 Mass-market/attention-economy · AP-4 Public OSS Phase 1/2 of core · AP-5 Hard-coded Jetix-specific in base · AP-6 One-person-company assumptions · AP-7 Slow-corporate governance · AP-8 Chaotic-startup governance · AP-9 Motivational-circle community · AP-10 Attention-extraction mechanics · AP-11 Single-provider AI architecture · AP-12 Pure-research institution Phase 1 · AP-13 Public token with governance/community-access rights (any phase) · AP-14 Equal-weight distribution across channels · AP-15 Monolithic brand identity · AP-16 Boutique-scale shortcuts.

### E.4 Binding ship criteria (Brief §1, §5, §6, §8)

- **Phase-1 ship:** €50K Q2-shippable (Brief §1). DIET §1.2 normalises as "7–14 день launch."
- **Phase-3 scalability:** 10× per gate ≤30% subsystem LoC refactor; schema migrations ≤3 per subsystem per gate (target), <10 hard-fail (Brief §5.1).
- **Cost ceiling:** €300–800/month Phase 1 run-rate (Brief §1, §5.6, §8.3).
- **21 hard constraints C1–C21** (Brief §6) — each disqualifier; operationalise 24 Locks at architecture-gate level.
- **Precedence (Brief §1):** D1+D2+D3+24 Locks > Brief > OME/FPF/ADR > atoms.

## F. Two-Layer Distillation Spec

Source: DIET opening two-layer section + §1.1.

### Layer α — Philosophical Layer
**What:** how system MUST BE — first principles, quality/cleanliness/integrity/epistemic discipline, strategic navigation lens.
**Feeds from:** §3.1 CE (50/50, $100 rule) + §3.7 Mgmt Philosophy (Drucker, 37signals, Laloux) + §3.8 Systems Thinking (Meadows/Senge/Левенчук/FPF) + §3.9 Cybernetics (Ashby, Beer VSM) + §3.11 Investing (Munger, Taleb) + §3.12 Mental Models (Kahneman, Deutsch, Ahrens) + §3.13 Biology/Evolution (Dennett universal algorithm) + §3.14 Philosophical Strategic (Naval, Stoic, Tao, Finite/Infinite Games) + §3.15 Philosophy of Science (Popper, Kuhn, Lakatos).
**Deliverable:** `decisions/PHILOSOPHICAL-LAYER-DISTILLATION.md` — 20–40 first principles.
**Rule:** when architecture/tactics conflict — philosophical layer breaks tie.

### Layer β — System + Code Layer
**What:** how system IS BUILT — architecture, engineering practices, code quality, concrete patterns.
**Feeds from:** §3.1 CE (agents/skills/Plan-Work-Review-Compound) + §3.2 AI-native OS + §3.3 Linux/Unix (Raymond, Kernighan) + §3.4 Clean Code (Ousterhout, Pragmatic, Refactoring) + §3.5 PM (Shape Up) + §3.6 Product Mgmt (Discovery → Delivery) + §3.9 Cybernetics (VSM impl) + §3.10 Complexity (scale laws) + §3.16 Eng Foundations (Koen, Vincenti, Petroski, TRIZ) + §3.17 Agent primary sources.
**Deliverable:** `decisions/SYSTEM-CODE-LAYER-DISTILLATION.md` — engineering patterns + architectural primitives.
**Rule:** implementation decisions — which patterns/tools/structures to use.

### Overlap clause
§3.8 Systems Thinking + §3.9 Cybernetics feed BOTH layers. Swarm itself decides aspect assignment.

### Ortho check — meta-system-first-then-Jetix-overlay (DIET §1.1)
- **Layer 1 / Layer 2 = WHAT we build** (meta-system base / Jetix overlay). Swarm MUST first build universal meta-system (Jetix-agnostic OS for solo-founder/systems-thinker), THEN apply Jetix overlay (philosophy + 24 Locks + archetypes + trajectory). Base/overlay pattern; D1 Vision §4 + V1 Conservative §3 hint already.
- **§α/β = HOW we think about it** (philosophical / system-code).
- **Independent axes.** Swarm result explicitly addresses both.

**Deliverables (§1.4):** `META-SYSTEM-UNIVERSAL-BASE.md` + `JETIX-OVERLAY-ON-META-SYSTEM.md` + `JETIX-FINAL-SYSTEM-SYNTHESIS-iteration-N.md` (3–5 variants) + scoring table (10 axes × N variants) + migration plan + risk register + `prompts/next-iteration/`.

## G. Compliance-Check Template

Audit instrument for Parts 4-6. Status cells empty by design.

| Lock # | Lock title | Where addressed (Part/Section) | Status (✅/⚠️/❌) | Rationale / tension flagged |
|---|---|---|---|---|
| 1 | Gentleman/Predator |  |  |  |
| 2 | Solo-now-team-ready |  |  |  |
| 3 | Closed/Open |  |  |  |
| 4 | Name = Jetix |  |  |  |
| 5 | Consulting-first |  |  |  |
| 6 | No advisors |  |  |  |
| 7 | Union archetypes (11) |  |  |  |
| 8 | Layered identity |  |  |  |
| 9 | Pain primary |  |  |  |
| 10 | EN+US first |  |  |  |
| 11 | Consulting+Producer+Fund |  |  |  |
| 12 | Smart+site+social-TOF |  |  |  |
| 13 | Open surface / Closed core |  |  |  |
| 14 | Revenue-instrumental research |  |  |  |
| 15 | Revenue-gated spend |  |  |  |
| 16 | Phase 1 simple chat |  |  |  |
| 17 | Filesystem = SoT |  |  |  |
| 18 | Productization |  |  |  |
| 19 | $1T Holding-Scale |  |  |  |
| 20 | USB-C + Enterprise-Fast |  |  |  |
| 21 | Matchmaker + Roy-Replication |  |  |  |
| 22 | ICP 5-criteria + direction |  |  |  |
| 23 | Token Option B |  |  |  |
| 24 | OSS research (Phase 2+) |  |  |  |

## H. Tensions / Open Questions the Synthesis Must Resolve

### H.1 TBD items flagged in Tier-2 sources

1. **ALIGN §10** — all seven must be resolved in master synthesis: comms channels (wiki stigmergic vs mailbox JSONL hybrid) / termination stack (maxTurns, budget, verifier, HITL trigger) / iteration pattern (convergence, max passes, compound) / smoke-test design / skill roadmap / hooks+monitoring / memory-write protocol (single-writer Phase 1 vs CRDT).
2. **DIET Q1–Q3** — Q1 Scope priority (trim ~60h diet to P0+P1 ~35–40h?); Q2 Add Economics (Hayek/Coase/Ostrom) / Design+UX (Norman/Rams)?; Q3 Mode A vs B default next iteration.
3. **Brief §3.1.9 / §4.1** — Phase-2/3+ agent roster "TBD per Q2 architect proposal"; note as architect-variant responsibility, not Phase A baseline.

### H.2 Contradictions between Tier-2 files

1. **Gate file naming.** ALIGN §4: `decisions/AWAITING-APPROVAL-<topic>-<date>.md` (context+options+recommendation+rationale+risk). DIET §1.5: `stage-<N>-<name>-AWAITING-APPROVAL.md` + `stage-<N>-<name>-DECISION.md`. Different path prefix and structure. Synthesis must pick canonical — suggested two-tier (not binding): `decisions/AWAITING-APPROVAL-*.md` for swarm-wide architectural decisions; `stage-<N>-*.md` for brigadier-internal stage splits.

2. **Archetype count.** PRE §D7 locks "10 archetypes." Brief §2 normative note re-counts as 11 (10 base + bloggers Stage 3). ALIGN does not mention bloggers. Synthesis must adopt 11-way schema per Brief normative rule.

3. **Mode B trigger scope.** ALIGN §4 scopes Stage-Gated to "key architectural decisions only" with explicit non-triggers (research inventory / draft synthesis / cleanup / wiki-entry / routine review). DIET §1.5 broadens to "architecture / strategic pivots / new patterns / anything touching 24 Locks." Reconcile: ALIGN non-trigger list authoritative carve-outs; DIET expansion = illustrative trigger examples.

4. **Tier-4 in Phase A.** ALIGN §9 bans Tier 4 books in Phase A. DIET Category 3 lists Tier 4 books (Ousterhout / Ashby / Meadows / Cagan / Grove / Laloux / Shape Up / Karpathy full / Dawkins / Kauffman / Naval / Popper / Koen / Vincenti / Altshuller) as MUST/SHOULD reading. Not a contradiction of intent — DIET lists full diet (Phase A + B); ALIGN §9 restricts Phase-A subset. Synthesis must explicitly split: Phase-A = Tier 1+2+3 only (already-in-repo CE / Perplexity / Левенчук + free-online Ashby/Raymond/Naval); Phase-B = physical books Ruslan acquires.

5. **Architect-question count.** Briefing claims 16; Brief §10 has 15 (Q1–Q15). Answer the actual 15.

6. **Anti-pattern count.** Brief §7 has exactly 16 anti-patterns (AP-1…AP-16). Matches briefing claim. Confirmed.

7. **Agent-count collision.** Brief §6 C14: "11-agent canonical roster" (life-coach → Life-OS). ALIGN §1: "5 experts + brigadier = 6 agents total." Not a contradiction — two rosters: (a) 6-agent Phase-A baseline swarm that **builds** the system; (b) 11-agent operational roster (D6) that **runs** Jetix-company post-build. Synthesis must distinguish explicitly.

### H.3 Design-space items: synthesis delivers options, does not collapse

- **DIET §1.7 Jetix ↔ Partners co-evolution loop.** Ruslan explicitly requests 3–5 design options (mechanism × phase × pros/cons × dependencies × analogs: Berkshire / Y Combinator / Andreessen / Stripe ecosystem / Tiny Capital / Constellation). Preserve option set in Parts 4-6, do not collapse.
- **Decision 23 Options A/B/C/D.** Option B (internal Phase 2, limited public Phase 3+) = Ruslan-approved default per ST2B §D23 header. A/C/D noted but deprecated.

---

**End of Extraction E.** Reference instrument for Parts 4-6 compliance-checking; no new decisions, no commentary on the 24 Locks.
