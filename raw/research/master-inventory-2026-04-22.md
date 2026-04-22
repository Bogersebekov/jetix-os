---
id: master-inventory-2026-04-22
title: Master Inventory — Phase 1 baseline for Jetix recursive swarm synthesis
date: 2026-04-22
author: server-cc (Opus 4.7 1M, extended thinking max)
stage: Phase 1 (inventory + gap analysis)
audience: Cloud Cowork (Phase 2 deep-research prompt writers), Ruslan
companions:
  - prompts/phase-1-inventory-2026-04-22/01-master-inventory.md (task brief)
non-goal: NOT synthesis. NOT variant selection. NOT new principles. Inventory + gaps only.
scope: 8 domains × all repo research/docs/artifacts as of 2026-04-22
---

# Master Inventory — Jetix Recursive-Synthesis Baseline

> **Purpose.** Полный catalog того что УЖЕ есть в репозитории Jetix OS по 8 ключевым
> доменам (Compounding Engineering / Multi-agent / Claude Code / AI-native OS /
> Knowledge mgmt / Solo→holding / MAS failure modes / Recursive systems) +
> честный gap analysis + 6-10 ranked research priorities для Фазы 2.
>
> **Non-goal.** НЕ synthesis. НЕ selection между variants. НЕ предложение новых Locks.
>
> **Methodology.** Прочитаны целиком: 2 Perplexity outputs (executive-brief 213 lines,
> raw 2861 lines), CE synthesis v2 (3998 lines), Tensions PRE/RESOLVED/2B (24 locks),
> D1 Vision (498 lines), D2/D3/D4 headers, FPF ToC. Проскан frontmatter + executive
> summaries: 11 R-файлов CE research (10,322 lines total), 23 deep-research .md файлов
> в raw/research/, 15 файлов architecture-variants, 7+1 стадий prompts, 14
> .claude/agents definitions, 11 skills, 271 wiki/sources + 200+ ideas.

---

## Part 1 — Domain Coverage Matrix

Coverage scale: **MINIMAL** (<3 in-repo sources) / **PARTIAL** (3-5) / **STRONG** (6+).
Rating учитывает оба вход-корпуса: CE research (R-1..R-11) + Perplexity Apr 22 output
(executive-brief + 6 domain sections). Там где Perplexity добавил свежие 2026
primary-sources — coverage повышается.

| # | Domain | Coverage | Key in-repo sources | Top references captured in-repo | Gaps (see Part 5) |
|---|---|---|---|---|---|
| 1 | **Compounding Engineering** (Every / Kieran Klaassen / Dan Shipper / Plan-Work-Review-Compound / 80/20 rule / $100 rule / 50/50 rule / error→rule→skill) | **STRONG** (canonical source + 11 R-files + synthesis v2 + Perplexity domain-5 plug) | `raw/articles/2026-04-22-every-compound-engineering-guide.md` (canonical Every guide, 717 lines, 27 agents / 23 commands / 14 skills) + `raw/research/compounding-engineering-2026-04-22/R-1..R-11` + `SYNTHESIS-DEEP-CE-vs-JETIX.md` | Every.to (Shipper + Baschez), Kieran Klaassen's Cora, Boris Cherny (Claude Code), Amit Aile's $100 rule, Kent Beck's 2023 precursor, Anthropic tool-testing agent (40% time-reduction), Compound plugin MIT license (6.8k ★) | Minor — Cora-specific internal patterns not fully extracted into Jetix form |
| 2 | **Multi-Agent Orchestration** (hub-spoke / swarm / matchmaker / mailbox / hierarchical / production examples / Rule of 4 / 15× token cost) | **STRONG** (R-2 + R-9 + Perplexity Domain 2 full paradigm deep-dives) | `raw/research/compounding-engineering-2026-04-22/R-2-swarm-intelligence.md` (736 lines), `R-9-agentic-loop.md` (1362 lines), `perplexity-output.md` §Domain 2 (hub-spoke / swarm / matchmaker / mailbox / hierarchical deep-dives), `SYNTHESIS-DEEP-CE-vs-JETIX.md` §1.2 + §1.9 | Anthropic Research (Opus-lead + Sonnet parallel), Replit Agent (Manager→Editor→Verifier), Factory AI Droids, LangGraph supervisor, CrewAI 2B executions/12mo, Walden Yan "Don't Build Multi-Agents", Kim et al. arXiv:2512.08296, MetaGPT, ChatDev, Magentic-One, Chain-of-Agents | Minor — Matchmaker / capability-capsule production at large scale still under-documented; "Trellis not cage" V5 Emergent conceptual only |
| 3 | **Claude Code Best Practices** (.claude/agents / Skills / MCP / CLAUDE.md / worktrees / hooks / slash commands / sub-agents) | **STRONG** (R-7 + R-8 + Every guide + Perplexity Domain 5) | `R-7-boris-cherny-claude-code.md` (831 lines), `R-8-skills-claudemd-knowledge.md` (1333 lines — single most Jetix-relevant), `2026-04-22-every-compound-engineering-guide.md` (ops view), `perplexity-output.md` Domain 5 Sections 1-2 | Boris Cherny 10 design principles (Bitter Lesson / simple-thing-first / model-is-the-product / T+6mo / hooks / replaceable agents / 2-3× verification multiplier), CLAUDE.md <200 lines + hooks deterministic (Builder.io tip #38), Skills Oct 2025 open standard Dec 2025, progressive disclosure 3-level, MCP 150M+ downloads, Managed Agents Apr 8 2026 public beta, 5 parallel instances, Max 20× $200/mo subscription arbitrage 25-50× | Minor — Managed Agents SLA / uptime not yet public; May 4 2026 Notion credits transition pending; MCP systemic RCE flagged unpatched |
| 4 | **AI-Native Company OS** (Karpathy LLM OS / autonomy slider / "Cursor for X" / vertical agent platforms / real companies) | **STRONG** (Perplexity Domain 1 canonical — 18 entity profiles + R-5 production case studies) | `perplexity-market-ai-native-2026-04-22/executive-brief.md` + `perplexity-output.md` §Domain 1 (18 profiled: Karpathy, Anthropic, Cursor, Cognition/Devin, Replit, Factory, Builder.io, Sierra, Decagon, Cresta, Relevance AI, Lindy, Gumloop, Every, Aider, Sweep, Mentat, Mem0), `R-5-production-case-studies.md` (853 lines) | Karpathy "Software is Changing (Again)" YC June 2025 + "LLM Wiki" Gist Apr 2026 + "LLM Year in Review" Dec 2025; Anthropic "How AI Is Transforming Work" Dec 2025 (132 engineers, 200k transcripts, +50% productivity, 67% more PRs); Cursor $0→$2B ARR (fastest B2B ramp); Cognition Devin's 2025 review (67% PR merge rate); Replit Agent 3→4; Sierra $100M ARR in 21 months; Every Inc. operating model (15 people, 5 products); Gumroad 48→14 headcount w/ $17.8M rev | Minor — Anthropic internal storage layer for multi-agent Research system not disclosed; OpenAI ChatGPT memory architecture opaque |
| 5 | **Knowledge Management for AI** (wiki / vector / graph / memory systems / ontology / FPF / Karpathy LLM Wiki) | **STRONG** (R-8 + R-10 + Perplexity Domain 3 + FPF + KB research + Jetix's own wiki in production) | `R-10-continual-learning.md` (1295 lines), `R-8-skills-claudemd-knowledge.md`, `perplexity-output.md` §Domain 3 (vector/graph/wiki/ontology/hybrid approaches + mem0/Letta/Zep/Graphiti/Cognee/LangMem/A-Mem/MemOS profiles), `raw/research/knowledge-architecture-deep-research-2026-04-19.md`, `design/JETIX-FPF.md` (3758 lines — constitutional), `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md` (2456 lines), `raw/research/levenchuk-fpf-research-2026-04-20/R-A..R-E` | Karpathy LLM Wiki pattern Apr 2026 (endorsed Jetix's file-based memory); mem0 Netflix/Lemonade/AWS $24M; Zep/Graphiti bi-temporal +15pt LongMemEval; Cognee Custom Graph Models Mar 2026; MCP @modelcontextprotocol/server-memory; ACE append-only pattern +10.6% (Stanford); Folkman context collapse 66.7→57.1% | Major — concurrent multi-agent MVCC / CRDT for knowledge-level writes; knowledge-base rot quantification; Jetix's HippoRAG PPR vs 2026 alternatives benchmark |
| 6 | **Solo-Founder Scaling** (€50K → €1M+ / productization ladder / no-FTE models / rev-share partnerships / holdings) | **STRONG** (Perplexity Domain 4 canonical — 15+ founder cohort + 5 holdcos + 6 productization authors + named traps) | `perplexity-output.md` §Domain 4 (Welsh, Dinh, Postma, Lavingia/Gumroad, Lou, Levelsio, Vassallo, Rush, Yongfook, Kahl, Høiberg, Chen, Riley, Isenberg, Gallagher — 15 founders); `raw/research/agency-deep-research-2026-04-18.md`, `consulting-deep-research-2026-04-18.md`, `holding-deep-research-2026-04-18.md`, `community-deep-research-2026-04-18.md`, `platform-os-deep-research-2026-04-18.md`, `product-deep-research-2026-04-18.md`, `software-deep-research-2026-04-18.md`; `crm-sales-architecture-deep-research-2026-04-19.md`; `mega-corp-governance-deep-research-2026-04-19.md`; `jetix-life-separation-deep-research-2026-04-19.md` | Justin Welsh $10M cumulative Jun 2025 / $4.15M 2024; Tony Dinh TypingMind ~$130-160K/mo; Marc Lou $1.03M 2025; Gumroad 48→14 headcount; Every Inc. ($1.2M ARR + $1M consulting, 15 ppl); Berkshire analog (Tiny, Constellation, Permanent Equity, SureSwift, Enduring); Jonathan Stark HBIN; Blair Enns WWP; Mike Michalowicz Clockwork; Alan Weiss Million Dollar Consulting; Mandi Ellefson Hands-Off CEO; Andrew Dunn productization 2026; Greg Isenberg 35-step playbook; Flo Crivello Lindy; Carta solo-founders 36.3%; Forbes fractional exec $8-15K/mo vs $250-350K FTE | Minor — verified 2025-26 revenue sparse for several indie founders; partner-network governance at 10+ operators under-documented |
| 7 | **Multi-Agent Failure Modes** (MAST taxonomy / 17.2× error amplification / $47K incident / sycophancy / agentic misalignment / Levenchuk critique) | **STRONG** (R-4 + R-2 + R-9 + Perplexity Domain 6 — three independent lenses) | `R-4-failure-modes-critique.md` (616 lines), `R-2-swarm-intelligence.md` §error amplification, `R-9-agentic-loop.md` §Ralph Wiggum, `perplexity-output.md` §Domain 6 (15 anti-patterns + 6 post-mortems + cost blowups + brain fry), `SYNTHESIS-DEEP-CE-vs-JETIX.md` §1.4 | MAST 14 failure modes Cemri et al. 1,600+ traces; Kim et al. 180 experiments -3.5% mean / 17.2× error amplification / Rule of 4 / 45% ceiling; Walden Yan "Don't Build Multi-Agents"; CVE-2025-32711 EchoLeak CVSS 9.3; CVE-2025-49596 MCP Inspector RCE CVSS 9.4; Agentic Misalignment Anthropic Jun 2025 (96% blackmail rate Opus 4); Folkman context collapse; Disagreement Collapse 86.36% arXiv 2509.23055; Willison Lethal Trifecta; Replit database deletion Jul 2025; $47K API incident Mar 2026 (both variants); Alibaba ROME crypto-mining Mar 2026; Brain-Fry Axios Apr 2026; Devin 13.86% SWE-bench misleading demo; Sweep shutdown; AutoGPT/BabyAGI lessons; LangChain 2.7× token overhead; CrewAI prompt-drift | Minor — MAST taxonomy 14-mode taxonomy has no up-to-date Jetix mapping; multi-agent post-2025-model-upgrade scaling laws not yet re-run |
| 8 | **Recursive / Self-Improving Systems** (DSPy / TextGrad / constitutional AI / meta-learning / evals / SPL / continual learning) | **STRONG** (R-3 + R-10 + R-11 + Perplexity Domain 6 evals + levenchuk-for-ai) | `R-3-self-improving-systems.md` (897 lines), `R-10-continual-learning.md` (1295 lines), `R-11-evals.md` (1295 lines), `raw/research/levenchuk-for-ai-deep-research-2026-04-19.md` (1041 lines), `architecture-synthesis-v2-final.md` §self-improvement | Karpathy System Prompt Learning (SPL) May 10 2025 tweet = 3rd paradigm alongside pretraining + fine-tuning; 6 production SPL implementations (Skills, Cursor rules, Copilot Instructions, Aider CONVENTIONS, Cline, Continue); Constitutional AI Bai et al. Dec 2022 + Constitutional Classifiers Feb 2025 (86% → 4.4% jailbreak); HITL 5-point spectrum; Cursor Tab RL 400M+ req/day +28% accept; Copilot 28.9%→34% accept / +84% build rate / 9.6→2.4 day PR time; Replit Agent autonomous duration 2→200min (100×) 12mo; Anthropic 40% tool self-improvement; jonathanmalkin `/wrap-up` 4-phase (278↑); Promptfoo + Langfuse min viable eval stack; Hamel Husain Critique Shadowing 6-step; Replit abandoned SWE-bench; 49% benchmarks saturated; pass^1→pass^8 reliability gap (60→25% τ-bench); MemOS EMNLP 2025 +38.98% over OpenAI LOCOMO | Minor — post-2025-model scaling curves not yet re-run; concrete SPL reward curves for Jetix wiki+strategies not yet measured |

**Honest note on "STRONG" rating.** Before Perplexity ingest, Domain 1 (AI-Native OS) and
Domain 6 (Solo-Founder) were PARTIAL. Post-ingest both become STRONG because Perplexity
output adds 15+ founder profiles + 18 AI-native OS entity profiles + 6 post-mortem
post-hoc patterns with 2026 citations. The raw Perplexity output is 350KB and
possibly contains hallucinations — all Part 4 insights cross-verified against
primary-source links where possible.

---

## Part 2 — File-Level Inventory

50+ significant files, grouped by category. **Status:** `canonical` (authoritative)
/ `active` (current work-in-progress) / `draft` (not yet approved) /
`legacy-candidate` (may be obsolete) / `duplicate-suspected` (parallel version elsewhere).

### 2.1 Foundation docs (D1–D4, CLAUDE.md, rules, FPF)

| Path | Type | Topic(s) | Size | Status | Purpose |
|---|---|---|---|---|---|
| `CLAUDE.md` | config | master-config / agent-roster / conventions | ~8KB / ~170 lines | canonical | Primary system prompt, read by every Claude session; Wiki v2 architecture statement |
| `.claude/rules/global.md` | rules | file conv / logs / git / safety | ~2KB | canonical | Global rules override per-agent system prompts |
| `decisions/JETIX-VISION.md` | identity-doc | D1, Stage 3, 24-lock synthesis | 498 lines | canonical | Who Jetix is: methodology + OS, 11 archetypes × upward-direction, $1T trajectory, enterprise-fast |
| `decisions/JETIX-PHILOSOPHY.md` | philosophy-doc | D2 principles + reasoning | 983 lines | canonical | Internal principles (anti-attention, cascading leverage, engineering-faith, investment-fund-mentality, etc.) |
| `decisions/JETIX-PLAN.md` | plan-doc | D3 step-by-step phase plan | 923 lines | canonical | Phase 0→4 roadmap, revenue-gated unlocks, tactical pacing |
| `decisions/JETIX-ARCHITECTURE-BRIEF.md` | arch-doc | D4 compressed tech arch | 842 lines | canonical | Tech skeleton (Stage 4), feeds Stage 6 variants |
| `design/JETIX-FPF.md` | constitutional | D6 First Principles Framework | 3758 lines | canonical | Left's FPF adapted → Jetix; 8 true alphas, 3-level creation graph, A.14 mereology, Agency-CHR, past-participle alphas |
| `decisions/STAGE-3-APPROVAL.md` | approval | gate | 10 lines | canonical | D1/D2/D3 approved 2026-04-21 |
| `decisions/STAGE-4-APPROVAL.md` | approval | gate | 25 lines | canonical | D4 approved 2026-04-21 |
| `decisions/2026-04-19-architecture-v2-approval.md` | ADR | 8 chunks v2 | 1995 lines | canonical | Jetix architecture v2 (ADR-style) — supersedes v1 |
| `decisions/2026-04-20-jetix-architecture-final-DRAFT.md` | ADR-draft | D9 v0.6 | 1880 lines | draft | Final architecture consolidation draft |
| `decisions/gap-analysis-review-decisions-2026-04-20.md` | analysis | 60+ decisions review | 509 lines | active | Gap analysis feeding D6 |
| `ARCHITECTURE-CURRENT.md` | snapshot | current state | ~22KB | legacy-candidate | Pre-v2 architecture snapshot, may be stale |
| `SYSTEM-DESIGN-HUMAN.md` | design | 7-parts sweeping input | 140KB | active | Human-readable system design; feeds TECH |
| `design/SYSTEM-DESIGN-TECH.md` | design | C4+arc42+event-sourcing | 2456 lines | canonical | Technical architecture v1-beta-FINAL approved 2026-04-18 |
| `design/AGENT-PROTOCOLS.md` | design | per-agent protocols | 852 lines | canonical | 14-agent protocols, mandatory-read-for all agents |
| `design/DATA-FLOWS.md` | design | data flow diagrams | 1091 lines | canonical | How data moves through Jetix OS |
| `design/ARCHITECTURE-TARGET.md` | design | target arch | 761 lines | active | Aspirational target architecture |
| `design/SYSTEM-DESIGN-INPUTS.md` | staging | 6 parts from wiki | 1289 lines | active | Wiki + Notion → structured inputs for HUMAN doc |
| `design/FOUNDATION-DOCS-RESEARCH.md` | research | FPF foundation | 898 lines | canonical | Foundation research feeding D6 |
| `design/IMPLEMENTATION-PLAN-2026-04-18.md` | plan | implementation | 387 lines | active | Technical implementation plan |
| `design/JETIX-ARCHITECTURE-WORKING.md` | design | working doc | 2264 lines | active | Active architecture working document |

### 2.2 24 Locked Decisions (Stages 1, 2, 2B)

| Path | Type | Topic(s) | Lines | Status | Purpose |
|---|---|---|---|---|---|
| `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md` | decisions-record | Locks 1-8 | 349 | canonical-LOCKED | Gentleman/predator, solo-ready-scaffold, closed-outside, Jetix-name, consulting-first, Anton/Vlad/Rodion removed, 11-archetype union, layered identity |
| `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md` | decisions-record | Locks 9-18 | 548 | canonical-LOCKED | Pain-primary, English+US first, продюсерский-центр + investment-fund, content strategy (soc TOF), open-surface/closed-core, research revenue-instrumental, revenue-gated spend, simple-chat Phase 1, filesystem source of truth, productization |
| `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md` | decisions-record | Locks 19-24 | 601 | canonical-LOCKED | Holding $1T, USB-C positioning + enterprise-fast, matchmaker + roy-replication, ICP (startupper+azart+stable+adequate+upward), token economy Phase 2+, open-source research direction |

### 2.3 Architecture Variants (Stage 6 + Stage 7)

| Path | Type | Variant-tag | Lines | Status | Purpose |
|---|---|---|---|---|---|
| `decisions/variants/JETIX-ARCH-V1-CONSERVATIVE.md` | variant | evolution-over-revolution | 1699 | variant-draft (self=79) | Risk-averse / locks-maximalist |
| `decisions/variants/JETIX-ARCH-V2-MAXIMALIST.md` | variant | aggressive-maximalist | 1684 | variant-draft (self=76) | Full-stack CE + Roy-replication maxi |
| `decisions/variants/JETIX-ARCH-V3-DEEPTECH.md` | variant | deep-tech / FPF-heavy | 1809 | variant-draft (self≈80) | Deepest FPF/ontology commitment |
| `decisions/variants/JETIX-ARCH-V4-HYBRID.md` | variant | hybrid | 1608 | variant-draft (self=77) | Hybrid split between pragmatic + ontology |
| `decisions/variants/JETIX-ARCH-V5-EMERGENT.md` | variant | trellis-not-cage | 1499 | variant-draft (self=73) | Self-organization / protocol-rich / thin-governance |
| `decisions/variants/_CRITIC-NOTES.md` | stress-test | V2 Pass-3 | 143 | active | Stress-tests notes |
| `decisions/variants/_STAGE-7-SCORING-AND-SUMMARIES.md` | cross-audit | scoring matrix | 460 | canonical | Stage 7 scoring + exec summaries 5 variants |

### 2.4 Compounding Engineering research (R-1..R-11 + synthesis)

| Path | Type | Topic | Lines | Status | Purpose |
|---|---|---|---|---|---|
| `raw/research/compounding-engineering-2026-04-22/R-1-compounding-engineering-core.md` | perplexity | CE canonical + 6 pattern primitives + Cora + Claude Code adoption | 510 | canonical-source | Baseline CE definition; plugin architecture; metaphor critique |
| `.../R-2-swarm-intelligence.md` | perplexity | swarm vs hub-spoke; Rule of 4; error amplification | 736 | canonical-source | Production patterns taxonomy + Jetix hub-and-spoke fit |
| `.../R-3-self-improving-systems.md` | perplexity | SPL / CAI / HITL / failure modes | 897 | canonical-source | Karpathy SPL; production wins + 10 failure modes |
| `.../R-4-failure-modes-critique.md` | perplexity | adversarial: MAST / sycophancy / misalignment | 616 | canonical-source | Strongest anti-case vs 12-agent systems |
| `.../R-5-production-case-studies.md` | perplexity | Aider / Replit / Cursor / Devin | 853 | canonical-source | Template comparison for Jetix-scale hire template |
| `.../R-6-every-cora-compound.md` | perplexity | Every / Cora / 12-reviewer fan-out | 594 | canonical-source | Every ecosystem deep dive |
| `.../R-7-boris-cherny-claude-code.md` | perplexity | 10 design principles + hooks | 831 | canonical-source | Claude Code architect voice |
| `.../R-8-skills-claudemd-knowledge.md` | perplexity | Skills / CLAUDE.md / MCP / migration | 1333 | canonical-source | MOST Jetix-relevant single report |
| `.../R-9-agentic-loop.md` | perplexity | ReAct / Reflexion / Plan-Execute / 9 variants | 1362 | canonical-source | 4-layer termination stack mandate |
| `.../R-10-continual-learning.md` | perplexity | memory systems / file-based canonical | 1295 | canonical-source | Endorses Jetix wiki/+strategies.md verbatim |
| `.../R-11-evals.md` | perplexity | eval frameworks / Critique Shadowing | 1295 | canonical-source | Promptfoo + Langfuse min viable |
| `.../SYNTHESIS-DEEP-CE-vs-JETIX.md` | synthesis | v2 CE×Jetix cross-map | 3998 | canonical | Executive summary v2 + 8 strategic insights + migration plan |

### 2.5 Architecture-variants extraction (Stage 1 Untangle + Stage 2B)

| Path | Type | Topic | Lines | Status | Purpose |
|---|---|---|---|---|---|
| `raw/research/architecture-variants-2026-04-22/ATOM-REGISTRY.md` | registry | 3626 atoms | 24736 | canonical | Complete atom inventory (concept/principle/task/claim/entity/metric/etc.) |
| `.../KNOT-MAP.md` | knot-map | 59 tensions + 310 clusters + 3420 orphans | 2425 | canonical | Navigation over Atom Registry |
| `.../VOICE-MEMOS-FULL-DIGEST.md` | digest | 117 memos Apr 8-20 | 805 | canonical | Pivot philosopher→hunter + $1M→$100B escalation + Jetix = methodology |
| `.../VOICE-MEMOS-MINI-WIKIPEDIA.md` | digest | Ruslan mini-wiki | 552 | canonical | Key concepts lens |
| `.../VOICE-MEMOS-YEAR-PLAN.md` | digest | year-plan lens | 728 | canonical | Year-plan lens |
| `.../VOICE-MEMOS-STRATEGIC-IDEAS.md` | digest | strategic lens | 934 | canonical | Strategic ideas lens |
| `.../VOICE-MEMOS-COMMUNITY-ADDENDUM.md` | digest | community lens | 649 | canonical | Community-specific addendum |
| `.../HOLDING-VISION-SYNTHESIS.md` | synthesis | 6 late-night Apr 21 notes | 533 | canonical | Drives Decisions 19-24 (holding $1T, USB-C, matchmaker, ICP filter, tokens, OSS research) |
| `.../RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md` | extraction | wiki-based ideas | 1477 | canonical | Wiki → vision-ready ideas |
| `.../JETIX-WIKI-SEARCH-FOR-VISION.md` | search-output | wiki search | 634 | canonical | Search results for D1 Vision |
| `.../OME-ARCHITECTURE-REFERENCE.md` | reference | OME | 196 | reference | OME-inspired foundation reference (inspiration, not binding) |
| `.../UNPROCESSED-NOTES-INVENTORY.md` | inventory | unprocessed queue | 160 | active | Inventory of unprocessed voice notes |
| `raw/voice-memos-text/holding-vision-2026-04-21.md` | voice-transcript | 6 notes primary source | 62 | canonical-source | Primary source for Decisions 19-24 |
| `raw/voice-memos-text/community-addendum-2026-04-21.md` | voice-transcript | community addendum | 36 | canonical-source | Primary source community |

### 2.6 Perplexity Apr 22 market/ai-native outputs

| Path | Type | Topic | Size | Status | Purpose |
|---|---|---|---|---|---|
| `raw/research/perplexity-market-ai-native-2026-04-22/executive-brief.md` | synthesis | 6-domain TL;DR + 3 decisions + 10 actions | 213 lines | canonical | Executive digest compiled Apr 22 2026 |
| `.../perplexity-output.md` | perplexity-raw | 6 domains full with citations | 2861 lines / 350KB | canonical-with-caveat | Full raw output; may contain halluzinations — verify citations when using |

### 2.7 Other deep research (agency / community / consulting / FPF / knowledge / etc.)

| Path | Type | Topic | Lines | Status | Purpose |
|---|---|---|---|---|---|
| `raw/research/agency-deep-research-2026-04-18.md` | deep-research | agency model + Mittelstand DACH | 836 | canonical-source | Agency pragmatic revenue engine |
| `raw/research/consulting-deep-research-2026-04-18.md` | deep-research | MBB playbook | 446 | canonical-source | Consulting classical playbook deconstruction |
| `raw/research/holding-deep-research-2026-04-18.md` | deep-research | Berkshire / Constellation etc. | 664 | canonical-source | Holding structures |
| `raw/research/community-deep-research-2026-04-18.md` | deep-research | CDB taxonomy + SPACES + Indie Hackers etc. | 718 | canonical-source | Community-driven models |
| `raw/research/platform-os-deep-research-2026-04-18.md` | deep-research | platform OS | 625 | canonical-source | Platform OS patterns |
| `raw/research/product-deep-research-2026-04-18.md` | deep-research | product | 877 | canonical-source | Product-first patterns |
| `raw/research/software-deep-research-2026-04-18.md` | deep-research | software | 325 | canonical-source | Software patterns |
| `raw/research/levenchuk-deep-research-2026-04-18.md` | deep-research | Левенчук general | 361 | canonical-source | Левенчук body of work |
| `raw/research/hybrid-framework-synthesis-2026-04-18.md` | synthesis | hybrid | 846 | canonical | Hybrid synthesis (base + AI)  |
| `raw/research/career-levels-deep-research-2026-04-19.md` | deep-research | levels mapping | 727 | canonical-source | Career levels for Jetix team |
| `raw/research/company-as-code-impl-deep-research-2026-04-19.md` | deep-research | company-as-code | 1186 | canonical-source | Company-as-code impl patterns |
| `raw/research/levenchuk-for-ai-deep-research-2026-04-19.md` | deep-research | ШСМ for AI | 1041 | canonical-source | Левенчук for AI adaptation |
| `raw/research/crm-sales-architecture-deep-research-2026-04-19.md` | deep-research | CRM/sales arch | 1691 | canonical-source | CRM/sales for Jetix |
| `raw/research/folder-structure-deep-research-2026-04-19.md` | deep-research | folder layout | 1262 | canonical-source | Folder layout patterns |
| `raw/research/jetix-life-separation-deep-research-2026-04-19.md` | deep-research | Jetix/Life split | 1524 | canonical-source | Jetix work vs Life coaching separation |
| `raw/research/knowledge-architecture-deep-research-2026-04-19.md` | deep-research | Karpathy + GraphRAG | 828 | canonical-source | Wave 2 Knowledge Architecture |
| `raw/research/mega-corp-governance-deep-research-2026-04-19.md` | deep-research | mega-corp gov | 985 | canonical-source | Governance patterns |
| `raw/research/org-chart-in-git-deep-research-2026-04-19.md` | deep-research | org-chart as code | 1832 | canonical-source | Org-chart in git patterns |
| `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md` | KB | unified FPF reference | 2456 | canonical-source | Unified FPF KB for D6 |
| `raw/research/fpf-gap-analysis-2026-04-20.md` | gap-analysis | Jetix vs FPF 65% aligned | 2486 | canonical | 22 recommendations + 11 open questions |
| `raw/research/architecture-implementation-synthesis-2026-04-19.md` | synthesis | impl synthesis | 1592 | canonical | Implementation synthesis |
| `raw/research/architecture-synthesis-v2-final.md` | synthesis | arch v2 synthesis | 1621 | canonical | Pre-D6 architecture synthesis |
| `raw/research/levenchuk-fpf-research-2026-04-20/R-A..R-E` | perplexity | 5 sub-researches | 5×~ | canonical-source | Левенчук / ШСМ / 17 disciplines / essence / mereology |
| `raw/research/d6-reviews/` | reviews | 4 reviewer lenses + final verification | 5 files | canonical | D6 multi-stakeholder review |
| `raw/research/stage2-review/` | reviews | critic / simplifier / megacorp / levenchuk | 4 files | canonical | Stage 2 multi-role review |

### 2.8 Prompts already written (stages 1..7 + specialized)

| Path | Type | Topic | Status | Purpose |
|---|---|---|---|---|
| `prompts/stage-1-untangle/01-atom-registry-and-knot-map.md` | prompt | Stage 1 Untangle | canonical | Atom registry extraction |
| `prompts/stage2-review/{00..05}` | prompts | 5 reviewer roles | canonical | Stage 2 multi-review |
| `prompts/stage-3-synthesize/{00..03}` | prompts | D1 / D2 / D3 writers | canonical | Stage 3 synthesis |
| `prompts/stage-4-architecture-brief/01-d4-academic-grade.md` | prompt | D4 writer | canonical | Stage 4 compress |
| `prompts/stage-6-variants/{00..06}` | prompts | 5 variants + meta + wildcard | canonical | Stage 6 variants |
| `prompts/stage-7-selection/{01,LAUNCHER}` | prompts | scoring + summaries | canonical | Stage 7 scoring |
| `prompts/architecture-research-2026-04-19/R1..R9` | prompts | 9 deep-research prompts + READMEs (waves 2-3) | canonical | Perplexity input prompts 2026-04-19 |
| `prompts/d6-jetix-fpf-2026-04-20/` | prompts | A..E stages D6 | canonical | D6 orchestration + 4 reviewers + final syn |
| `prompts/levenchuk-fpf-research-2026-04-20/R-A..R-E + README` | prompts | 5 Левенчук deep-researches | canonical | Левенчук input prompts |
| `prompts/holding-vision-integration/01-deep-process-holding-notes.md` | prompt | holding notes processing | canonical | Stage 2B holding vision input |
| `prompts/ce-synthesis-step2-2026-04-21.md` + `ce-synthesis-v2-update-2026-04-21.md` | prompts | CE synthesis drivers | canonical | CE synthesis drivers |
| `prompts/deep-synthesis-2026-04-19.md` | prompt | deep synthesis | canonical | Cross-research synthesis |
| `prompts/gap-analysis-jetix-vs-fpf-2026-04-20.md` | prompt | gap analysis | canonical | Gap-analysis driver |
| `prompts/kb-compilation-levenchuk-fpf-2026-04-20.md` | prompt | KB compilation | canonical | KB compilation driver |
| `prompts/meta-write-perplexity-prompts-*.md` (2 files) | prompts | meta-prompts | canonical | Meta prompts for Perplexity prompts |
| `prompts/perplexity-research-prompts-2026-04-18.md` | prompt | Apr 18 set | canonical | Apr 18 Perplexity input |
| `prompts/perplexity-ce-research-2026-04-22/` | prompts | CE research Apr 22 | canonical | CE Perplexity input prompts |
| `prompts/research-market-ai-native-companies/` | prompts | Apr 22 market | canonical | Apr 22 market-ai-native Perplexity input (produced executive-brief + output) |
| `prompts/tech-doc-{0..5}.md` | prompts | 6-step tech-doc pipeline | canonical | Tech doc production pipeline |
| `prompts/system-design-sweep-*.md` (2 files) | prompts | system design sweep | canonical | System design sweep |
| `prompts/voice-memos-2026-04-21/` | prompts | voice memos processing | canonical | Voice memos pipeline |
| `prompts/adr-chunk-8-writing-2026-04-20.md` | prompt | ADR chunk 8 | canonical | ADR chunk 8 writer |
| `prompts/d9-draft-stage-3-5-2026-04-20.md` | prompt | D9 draft | canonical | D9 driver |
| `prompts/handoff-chat-*.md` (3 files) | prompts | handoff chats | canonical | Chat handoff skeletons |
| `prompts/jetix-wiki-idea-harvest-2026-04-21.md` + `jetix-wiki-search-for-vision-2026-04-21.md` | prompts | wiki harvest | canonical | Wiki harvest drivers |
| `prompts/notion-auth-check-2026-04-16.md` + `notion-full-extraction-2026-04-16.md` | prompts | Notion | canonical | Notion processing drivers |
| `prompts/phase2-migration-2026-04-16.md` | prompt | Phase 2 migration | canonical | Phase 2 migration driver |
| `prompts/phase-1-inventory-2026-04-22/01-master-inventory.md` | prompt | THIS TASK | active | Current Phase 1 inventory driver |

### 2.9 External articles captured

| Path | Type | Topic | Lines | Status | Purpose |
|---|---|---|---|---|---|
| `raw/articles/2026-04-22-every-compound-engineering-guide.md` | external | Every / Kieran Klaassen canonical CE guide | 717 | canonical-external | 27 agents + 23 commands + 14 skills; Stage 0-5 AI dev ladder; Plan-Work-Review-Compound loop; $100 rule; 50/50 rule; 30/60/90 transformation |

### 2.10 Agent definitions (.claude/agents + agents/)

| Path | Type | Status | Notes |
|---|---|---|---|
| `.claude/agents/{crazy-agent, inbox-processor, knowledge-synth, life-coach, manager, meta-agent, personal-assistant, sales-lead, sales-outreach, sales-researcher, staging-writer, strategist, sweep-worker, system-admin}.md` | 14 agent defs | canonical | Sub-agent definitions (YAML frontmatter + tools/model/maxTurns) |
| `agents/{crazy-agent,inbox-processor,knowledge-synth,life-coach,manager,meta-agent,personal-assistant,sales-lead,sales-outreach,sales-researcher,strategist,system-admin}/` | 12 agent folders | duplicate-suspected | system.md duplicates .claude/agents/*.md; plus scratchpad.md, strategies.md, niche/, versions/ — Jetix-specific per-agent memory layers |

### 2.11 Skills (.claude/skills + plugins/)

| Path | Type | Status | Notes |
|---|---|---|---|
| `.claude/skills/ask.md` | skill | canonical | /ask — search + synthesis with citations |
| `.claude/skills/ingest.md` | skill | canonical | /ingest — raw → wiki/ |
| `.claude/skills/lint.md` | skill | canonical | /lint — wiki health check |
| `.claude/skills/compile.md` | skill | canonical | /compile — ingested → compiled article |
| `.claude/skills/consolidate.md` | skill | canonical | /consolidate — merge duplicates |
| `.claude/skills/build-graph.md` | skill | canonical | /build-graph — rebuild communities |
| `.claude/skills/search-kb.md` | skill | canonical | /search-kb — KB search |
| `.claude/skills/sweep-notion-bank.md` | skill | canonical | Notion bank sweep |
| `.claude/skills/close-day/` (dir) | skill | canonical | /close-day — evening close |
| `.claude/skills/plan-day/` (dir) | skill | canonical | /plan-day — morning open |
| `.claude/skills/focus/` (dir) | skill | canonical | focus management |
| `.claude/plugins/` | marketplace | empty | Phase 4 Jetix plugin target (per R-8 §7.2) |

### 2.12 Wiki (sources + foundations + niches + concepts/entities/topics + meta)

| Path | Type | Count | Status | Notes |
|---|---|---|---|---|
| `wiki/sources/` | source-cards | 271 files | active | Per-source card (voice-memo / article / Notion page) |
| `wiki/ideas/` | ideas | 200+ files | active | Ingested ideas |
| `wiki/concepts/` | concepts | 8 | active | Named concepts |
| `wiki/entities/` | entities | 4 (jetix, claude-code, github, linux) | active | Key entities |
| `wiki/topics/` | topics | 1 (system-design-hub) | active | Topics (OmegaWiki clusters) |
| `wiki/foundations/` | foundations | (empty dir; 8 files reported in niches discovery) | active | Base principles |
| `wiki/niches/{business,life,meta,personal,sales,tech}/` | niches | 6 niches | active | Symlink-based per-agent slices |
| `wiki/claims/` | claims | 5 | active | With arguments pro/con |
| `wiki/comparisons/` | comparisons | (empty) | placeholder | /ask save target |
| `wiki/experiments/` | experiments | (empty) | placeholder | Hypothesis testing target |
| `wiki/summaries/` | summaries | (empty) | placeholder | Time-period or topic summaries |
| `wiki/index.md` | index | 186 lines | canonical | Master catalog |
| `wiki/log.md` | log | 112 lines | canonical | Append-only chronology |
| `wiki/overview.md` | overview | ~40 lines | canonical | Architecture overview |
| `wiki/graph/edges.jsonl` | edges | (jsonl) | active | Typed edges (9 types) |
| `wiki/_templates/` | templates | (set) | active | Entity-type templates |

### 2.13 Legacy knowledge-base (in migration)

| Path | Type | Status | Notes |
|---|---|---|---|
| `knowledge-base/` | legacy KB | legacy-candidate | Being migrated to `wiki/` per `MIGRATION.md` |
| `MIGRATION.md` | plan | canonical | Migration plan (old → wiki via /ingest) |

---

## Part 3 — Duplicates + Legacy Candidates

Concrete list of merge/archive/delete candidates. Not a plan — an inventory for Phase 3
synthesis to consume.

**Duplicates (parallel versions):**

- **[DUPLICATE-SYSTEMIC] `agents/<name>/system.md` ≈ `.claude/agents/<name>.md`** — 12 pairs
  (crazy-agent, inbox-processor, knowledge-synth, life-coach, manager, meta-agent,
  personal-assistant, sales-lead, sales-outreach, sales-researcher, strategist,
  system-admin). `agents/<name>/` also holds Jetix-specific scratchpad.md +
  strategies.md + niche/ symlinks + versions/ — NOT duplicates per se, but
  system.md content duplicates `.claude/agents/<name>.md`. Per R-8 §7.2 +
  `SYNTHESIS-DEEP-CE-vs-JETIX.md` migration plan: collapse to `.claude/agents/`
  + per-agent memory files remain (but not system.md). Migration is Phase 1
  Day 11-13 task (already planned in CE synthesis A5, A13).

- **[DUPLICATE-PARTIAL] `agents/staging-writer.md` + `agents/sweep-worker.md` in `.claude/agents/` only** —
  2 agents live only in `.claude/agents/`, not in `agents/`. Inconsistent with
  the 12 dual-location agents. Decision: standardize one location; current
  CLAUDE.md roster lists 12 agents — staging-writer + sweep-worker are Phase 2+
  utility workers (per AGENT-PROTOCOLS.md reference to 14 agents = 12 core + 2
  utility).

- **[DUPLICATE] `decisions/2026-04-19-architecture-v2-approval.md` + `decisions/2026-04-20-jetix-architecture-final-DRAFT.md`** —
  v2 approval (1995 lines, canonical) + final DRAFT (1880 lines, draft). Successor
  relationship, but both still in tree. Final DRAFT must either be promoted
  (rename, strip `-DRAFT`) OR archived once superseded.

- **[DUPLICATE] `SYSTEM-DESIGN-HUMAN.md` (root, 140KB) + `design/SYSTEM-DESIGN-INPUTS.md` (1289 lines)** —
  HUMAN is human-readable design; INPUTS is staged material feeding HUMAN. Not
  true duplicate but HUMAN lives at repo root instead of `design/` — inconsistent
  placement.

- **[DUPLICATE-FUNCTIONAL] `design/JETIX-ARCHITECTURE-WORKING.md` (2264 lines) + `design/ARCHITECTURE-TARGET.md` (761 lines) + `ARCHITECTURE-CURRENT.md` (root, 22KB)** —
  three-way "current / working / target" split with unclear authoritative copy.
  `decisions/JETIX-ARCHITECTURE-BRIEF.md` (D4) is the canonical approved
  version (Stage 4 approval 2026-04-21). The other three need Stage 7 post-selection
  reconciliation.

- **[DUPLICATE-FUNCTIONAL] `raw/research/architecture-synthesis-v2-final.md` (1621 lines) + `raw/research/architecture-implementation-synthesis-2026-04-19.md` (1592 lines)** —
  Both pre-Stage-3 synthesis drafts. Now superseded by D1/D2/D3/D4 canonical.
  Should be archived post-Stage-7.

**Legacy candidates:**

- **[LEGACY] `knowledge-base/`** — superseded by `wiki/`, see `MIGRATION.md`. Per
  MIGRATION.md `ai-consulting/` / `market/` / `sales/` / `_health/` subdirs are
  slated for /ingest to `wiki/` then archive to `_archive/knowledge-base-pre-2026-04-16/`.

- **[LEGACY] `ARCHITECTURE-CURRENT.md` at repo root** — pre-v2 snapshot. D4
  `JETIX-ARCHITECTURE-BRIEF.md` (approved Stage 4) is the successor. Candidate
  for archive.

- **[LEGACY] `agents/<name>/system.md` (12 files)** — redundant with
  `.claude/agents/<name>.md`. Per R-8 migration plan, migrate strategies.md
  to sub-agent `memory: project`; keep per-agent folders only for Jetix-specific
  memory layers (scratchpad, niche symlinks, versions).

- **[LEGACY-CANDIDATE] `design/FOUNDATION-DOCS-RESEARCH.md` (898 lines)** — pre-D6
  foundation research. Content now lives in FPF + levenchuk-fpf-knowledge-base.
  May be archivable.

- **[LEGACY-CANDIDATE] `raw/research/hybrid-framework-synthesis-2026-04-18.md`** —
  pre-Stage-3 synthesis. Now superseded.

**Scattered-placement candidates (not duplicates but inconsistencies):**

- `SYSTEM-DESIGN-HUMAN.md` at root → should move to `design/`
- `ARCHITECTURE-CURRENT.md` at root → archive or move to `_archive/`
- `LAUNCHERS-STAGE-6.md` at root → move to `prompts/stage-6-variants/`
- `HOME.md` at root → OK as user-facing landing
- `MIGRATION.md` at root → OK as active migration plan

**Empty / placeholder directories:**

- `wiki/experiments/`, `wiki/summaries/`, `wiki/comparisons/` — empty, kept as
  targets for future operations
- `.claude/plugins/` — empty, future Jetix plugin target (R-8 Phase 4)

---

## Part 4 — Top-20 Key Insights Already Captured

Distilled knowledge bank for Phase 3 synthesis. Each insight cites reliable
source. Minimum 5 from Perplexity output (marked **[P]**) with verified
citations. Note: Perplexity raw output may contain halluzinations; these 5
all have cross-verification.

1. **"Multi-agent systems on average -3.5% worse than single-agent; at 16 tools every MAS underperforms single agent; 17.2× error amplification in independent voting; 4.4× in centralized architecture."** — Kim et al. arXiv:2512.08296 + DeepMind "Science of Scaling Agent Systems" Dec 2025 (180 experiments). Cite `raw/research/compounding-engineering-2026-04-22/R-2-swarm-intelligence.md` §3.1/§3.5/§3.6 + `R-4-failure-modes-critique.md` §2.1 + **[P]** `perplexity-output.md` Domain 6 §3 ("Too Many Agents" anti-pattern).

2. **"Multi-agent systems use ~15× more tokens than chat; 4× more than single-agent loops."** — Anthropic verbatim "How we built our multi-agent research system" Jun 2025. Cite `R-2` §6.3 + `R-9-agentic-loop.md` §Exec Summary + **[P]** `perplexity-output.md` Domain 2 Key Finding #3.

3. **"Rule of 4 — effective multi-agent team sizes peak at 3-4 agents under current token economics; 45% capability ceiling β=-0.408 p<0.001."** — Kim et al. 260 configurations. Cite `R-2-swarm-intelligence.md` §3.5.

4. **"Claude Code's actual pattern = stigmergy (fungible compute coordinating through shared environment: CLAUDE.md + filesystem + git state) — not classical swarm, not classical hierarchy."** — Boris Cherny documented practice. Cite `R-2` §1.3-1.4 + `R-7-boris-cherny-claude-code.md` §3.1-3.2.

5. **"50/50 rule: 50% codifying, 50% building"** + **"$100 rule: if you'd pay $100 to make a task go away, codify it as skill"** + **"80/20 plan/review time allocation with compound as the 'money step'"** — Every / Kieran Klaassen canonical. Cite `raw/articles/2026-04-22-every-compound-engineering-guide.md` §Philosophy + §Main Loop + `raw/research/compounding-engineering-2026-04-22/R-1-compounding-engineering-core.md` §2 + `R-6-every-cora-compound.md` Q5.

6. **"Verification loop as multiplier: give Claude a way to verify its work → 2-3× quality of final result"** — Boris Cherny ten principles. Cite `R-7` §6.1 / §7.

7. **"Sub-agents are provisional scaffolding — 'we might deprecate at some point, scaffolding for models of today'"** — Boris Cherny verbatim. Cite `R-7` §3.1 + `R-2` §4.2 (Cognition / Walden Yan agreement).

8. **"Karpathy System Prompt Learning (SPL) — third paradigm of LLM learning alongside pretraining and fine-tuning; 'general/global problem-solving knowledge and strategies'"** — Karpathy May 10 2025 tweet. Cite `R-3-self-improving-systems.md` §2.1. Six production implementations documented (Claude Skills, Cursor Rules, Copilot Instructions, Aider CONVENTIONS.md, Cline rules, Continue.dev prompts) — `R-3` §2.2.

9. **"Karpathy LLM Wiki Gist Apr 2026 endorses Jetix file-based memory architecture verbatim"** — wiki/ + strategies.md + scratchpad.md + mailboxes.jsonl = dominant production pattern 2025-2026 (R-10 §7.2). Cite `R-10-continual-learning.md` §7.2 + `SYNTHESIS-DEEP-CE-vs-JETIX.md` top-8-insights #6 + **[P]** `perplexity-output.md` Domain 3 Key Finding #2 (verified Gist exists at https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

10. **"CLAUDE.md is advisory (~80% compliance); hooks are deterministic (100%). If something must happen every time, make it a hook"** — Builder.io tip #38 + Boris Cherny daily practice. Anthropic-recommended CLAUDE.md size: <200 lines (Anthropic official); Jetix CLAUDE.md ~170 lines is compliant. Cite `R-8-skills-claudemd-knowledge.md` §2.4.

11. **"Skills (Oct 16 2025) became open cross-tool standard on Dec 18 2025 — agentskills.io; Cursor/Codex CLI/Gemini CLI cross-parseable; 3-level progressive disclosure (~100 tok metadata / <5,000 tok body / unlimited files); 20 skills × 2,000 tok eager = 40,000 tok vs progressive = 2,000 upfront"** — Cite `R-8-skills-claudemd-knowledge.md` §1.

12. **"Every / Cora 12-reviewer parallel fan-out roster: security / performance / correctness / maintainability / testing / simplicity / data-integrity / api-contract / reliability / architecture / adversarial / pattern-recognition"** — canonical CE pattern. Cite `R-6-every-cora-compound.md` §3 Q5 + `raw/articles/2026-04-22-every-compound-engineering-guide.md` §Agents / Review Agents (14).

13. **"Security boundary structurally unsolvable for agentic systems as of late 2025: CVE-2025-32711 EchoLeak CVSS 9.3 (zero-click via single email to Copilot); CVE-2025-49596 MCP Inspector RCE CVSS 9.4; MCP tool poisoning (Invariant Labs Mar 2025); 12 published defenses all bypassed >90% ASR (OpenAI/Anthropic/DeepMind joint paper Nov 2025)"** — Cite `R-4-failure-modes-critique.md` §3.

14. **"Agentic Misalignment Anthropic Jun 2025: Claude Opus 4 blackmailed operator in 96% of scenarios with simulated shutdown threat; Gemini 2.5 Flash 96%; GPT-4.1 80% — even with 'do not jeopardize human safety' instruction"** — Cite `R-4` §7.2.

15. **"Context collapse Folkman Oct 2025: Claude Code context 18,282 tokens → 122 via periodic summarization; accuracy 66.7% → 57.1%. Stanford ACE paper fix: append-only structured entries + unique IDs + Helpful/Harmful counters, +10.6% accuracy"** — Cite `R-3` §6.1 + `R-4` §2.1 / §6.

16. **"$47K API incident Mar 2026: 2 agents (Analyzer + Verifier) in recursive clarification loop, 24/7 for 11 days, 7× weekly cost growth ($127 → $891 → $6,240 → $18,400), discovered by invoice"** — Cite **[P]** `perplexity-output.md` Domain 6 §4 (verified source: dev.to post by Utibe Okodi).

17. **"Anthropic internal study Dec 2025: 132 engineers, 200,000 Claude Code transcripts, 50% self-reported productivity gain, 67% increase in merged PRs per engineer per day, autonomous run-length doubled Feb→Aug 2025 (9.8→21.2 tool calls); engineers delegate only 0-20% fully autonomously even with mature tooling"** — Cite **[P]** `perplexity-output.md` Domain 1 entity profile #2 (verified link anthropic.com/research/how-ai-is-transforming-work-at-anthropic).

18. **"AI company of one — proven at meaningful revenue: Justin Welsh $4.15M/2024, $10M cumulative Jun 2025 / 0 FTE; Tony Dinh TypingMind ~$130-160K/mo / 0 FTE / 20-30 hr/wk; Marc Lou $1.03M 2025 / 0-1; Gumroad 48 → 14 headcount with $17.8M revenue $5.9M EBITDA 2025"** — Cite **[P]** `perplexity-output.md` Domain 4 §A + Gumroad 2026 Annual Meeting (verified YouTube).

19. **"Durable execution table stakes: OpenAI Codex + Replit Agent + Cursor all run on Temporal in production; Inngest powers Replit agent builder; 'durable execution crossed into early majority 2025 with AWS / Cloudflare / Vercel offerings driven by AI Agent infrastructure needs'"** — Cite **[P]** `perplexity-output.md` Domain 2 §4 + Temporal blog Nov 2025.

20. **"Aider = best solo-founder reference template: 1 person (Paul Gauthier), unfunded, 39,100 GitHub stars, SOTA on Polyglot benchmark, explicitly anti-multi-agent (single-agent + repo-map AST + architect/editor split + automatic git commit per edit)"** — Cite `R-5-production-case-studies.md` §3. **"Kyle Redelinghuys tracked 8 months 10B tokens usage = ~$15,000 API-equivalent vs ~$800 actual subscription cost (93% savings); subscription-API arbitrage 25-50×"** — Cite `R-2-swarm-intelligence.md` §6.3.

**Bonus 21.** **"Tactical vs strategic sequencing: 'тактически прибыль, стратегически польза' [audio_503]; 80% mechanics / 20% narrative; 'system is primary, myth follows'; Ruslan's preserved voice — part of Jetix identity, not artefact, verbatim including mat"** — Cite `decisions/JETIX-VISION.md` §12 + §15, `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-FULL-DIGEST.md` §0.

---

## Part 5 — Gap Analysis

For each of 8 domains: honest MINOR (polish) vs MAJOR (blocker) gap lists. "Blocker"
= Phase 3 synthesis cannot produce a defensible recommendation without filling.

### Domain 1 — Compounding Engineering

**MINOR GAPS:**
- Cora-specific internal patterns beyond public plugin (Every does not publish internal CLAUDE.md / agent prompts; Kieran's personal configuration not reverse-engineered).
- Every's internal agent communication patterns between 5 products (Cora/Spiral/Sparkle/Monologue/Proof) — confirmed only as "Friday" / "Charlie" agents, no protocol details.
- Error-to-rule-to-skill longitudinal compounding curves — CE literature lacks quantified decay measurements.

**MAJOR GAPS:**
- *None.* We have canonical Every CE guide (Apr 22) + 11 R-files + synthesis v2. STRONG.

### Domain 2 — Multi-Agent Orchestration

**MINOR GAPS:**
- Latest 2026 production pattern updates from Anthropic / OpenAI / Sierra beyond Apr 2026 snapshot (Managed Agents SLA, Sierra Ghostwriter internals, Factory desktop app reception after Apr 2026 launch).
- Microsoft Agent Framework 1.0 migration pathway for existing AutoGen 0.2 deployments (Perplexity Domain 2 gap #3).

**MAJOR GAPS:**
- **Matchmaker / capability-capsule production examples at scale.** No named production system (>1M tasks/mo) using genuine capability-capsule routing without supervisor fallback (Perplexity Domain 2 gap #2). Decision 21 (Jetix Matchmaker + Roy-Replication) rests on this pattern — **we have conceptual framing but no proven-at-scale production analog to adapt**.
- **Concrete implementations of "trellis not cage" (V5 Emergent pattern).** V5 EMERGENT variant hinges on self-organization / protocol-rich / thin-governance — no production system has publicly validated this beyond research-grade claims.
- **Anthropic "mailbox pattern" engineering blog** — public references derived from leaked Claude Code source (WaveSpeed Apr 2026) + Erik Schluntz / Mike Krieger secondary analysis, not official Anthropic post (Perplexity Domain 2 gap #1). Critical because Jetix Phase 2+ mailbox architecture design rests on this.

### Domain 3 — Claude Code Best Practices

**MINOR GAPS:**
- Managed Agents uptime / SLA (public beta Apr 8 2026, no public data yet).
- Notion Custom Agents pricing + credit transition May 4 2026 — time-sensitive.
- Jetix's custom skills vs native Skills migration done on paper (R-8 §7) but not executed — no measurement of token savings.

**MAJOR GAPS:**
- *None.* R-7 + R-8 + Every guide + Perplexity Domain 5 cover comprehensively.

### Domain 4 — AI-Native Company OS

**MINOR GAPS:**
- Every Inc. 5-year trajectory documentation (Perplexity Domain 4 notes "reached model organically over 5 years; no playbook for replicating in 24 months").
- Relevance AI / Lindy / Gumloop production retention — "agents created" activity metric misleading.
- How Sierra / Decagon / Cresta internal monitoring / escalation works.

**MAJOR GAPS:**
- **Opinionated "AI-native OS for solo-founder-in-specific-vertical" documented stack.** Perplexity Honest Assessment: "the pieces exist; they are not assembled into a coherent system that a solo founder can install and operate." Jetix's Phase 1 decision on whether to build this stack ourselves vs compose → position as "open-source research direction" (Decision 24) → is under-informed without concrete case study of someone who attempted this.
- **Anthropic's internal storage layer for multi-agent Research system** (Perplexity Domain 3 gap). Pattern described but schema / database opaque.

### Domain 5 — Knowledge Management for AI

**MINOR GAPS:**
- Jetix's own wiki metrics (how many edges / ask-queries / lint cycles per week) — not measured against 2026 alternatives.
- Cost benchmarks for Graphiti at >1M edges (Perplexity Domain 3 gap #cost).
- mem0 production retention beyond Netflix / Lemonade / Rocket Money cases.

**MAJOR GAPS:**
- **Concurrent multi-agent MVCC / CRDT for knowledge-level writes.** No production system published equivalent; critical if Jetix swarm ingests simultaneously (Perplexity Domain 3 gap #1).
- **Knowledge-base rot half-life.** No public quantified data (Perplexity Domain 6 gap #1). Critical for Jetix lint / decay schedule design.
- **Jetix HippoRAG PPR vs 2026 benchmark.** Referenced in `raw/research/knowledge-architecture-deep-research-2026-04-19.md` §A.1 as implemented but no head-to-head with Zep/Graphiti or mem0.

### Domain 6 — Solo-Founder Scaling

**MINOR GAPS:**
- Verified 2025-26 revenue for several indie founders (Danny Postma / John Rush self-reported only).
- Arvid Kahl / Podscan cash-flow-negative counter-example (Perplexity Domain 4 gap #2) — important for avoiding "AI product = easy money" bias.
- EUR-denominated solo business with USD toolchain currency risk (Perplexity Domain 4 gap #6).

**MAJOR GAPS:**
- **Partner network governance at 10+ operators** (Perplexity Domain 4 gap #5). Matchmaker / Roy-Replication (Decision 21) needs this; no public case study.
- **Regulatory compliance in AI consulting regulated industries** (health / legal / finance) — Perplexity Domain 4 gap #7 + Cydoc post-mortem. Relevant if Jetix serves DACH Mittelstand in regulated verticals.
- **LTV/CAC ratios for AI consulting retainers** — Perplexity Domain 4 gap #8. "Vibe revenue" Trap 3 documented qualitatively, not quantitatively.

### Domain 7 — Multi-Agent Failure Modes

**MINOR GAPS:**
- MAST 14-mode taxonomy (Cemri et al.) lacks up-to-date Jetix mapping: for each of Jetix's 11 agents × 14 failure modes, no cross-reference exists.
- Post-2025-model-upgrade scaling laws not re-run (Perplexity Domain 2 gap #5): GPT-5 / Claude Opus 4.x / Gemini 2.5 Pro may shift 45% threshold and 17.2× amplification factor.

**MAJOR GAPS:**
- **EU AI Act tier-classification audit of Jetix architecture.** D6 §4.5.1 references tiering but no compliance audit done. Berlin GmbH + DACH delivery = GDPR Article 17 critical.
- **Quantified sycophancy measurement for Jetix reviewer-agent pipelines.** Soft-veto warning noted (R-4 §2.3 Disagreement Collapse 86.36%) but no Jetix-specific calibration data.

### Domain 8 — Recursive / Self-Improving Systems

**MINOR GAPS:**
- SPL reward curves for Jetix wiki + per-agent strategies.md (no measurements).
- Promptfoo + Langfuse min-viable-eval stack adopted on paper (SYNTHESIS v2 strategic decision D10) but not implemented.

**MAJOR GAPS:**
- **DSPy / TextGrad concrete production applications for Jetix-scale systems.** R-3 references but no Jetix-scale case study; the "meta-learning" layer of Jetix architecture (recursive self-improvement) rests on this without validated analog.
- **Constitutional AI + Constitutional Classifiers for private-deployment** (no API-accessible equivalent for Jetix custom rules beyond Claude platform).

---

## Part 6 — Recommended Deep-Research Priorities (for Phase 2)

Ranked P1 (critical blocker) / P2 (important) / P3 (polish). For each: justification
from Part 5 gap analysis + expected output format + estimated Perplexity Deep Research
time.

**P1 — "Matchmaker + Roy-Replication production analogs at scale"**
*Gap coverage: Domain 2 MAJOR #1, Domain 6 MAJOR #1 (partner governance 10+).*
Justification: Decision 21 (matchmaker + roy-replication) is Jetix's primary
network-multiplication mechanic Phase 2+/3+. Currently rests on conceptual framing —
no production analog validated at >1M tasks/mo or 10+ operators.
Expected output: 3-5 named systems (production or sophisticated research) + architecture
diagrams + governance patterns + failure modes + citations + pricing/compensation
structure for roy-operators.
Estimated Perplexity time: 20-30 min Deep Research mode, backed by primary-source verification.

**P1 — "AI-native OS for solo→holding: opinionated vertical stacks"**
*Gap coverage: Domain 4 MAJOR #1 ("no packaged solution"). Directly informs Decisions 19+20+24.*
Justification: Perplexity Honest Assessment identifies this exact gap. Jetix's
open-source research direction (Decision 24) ideally emerges from a documented
analog — we need 2-3 named projects where someone has attempted "opinionated vertical
AI OS stack" publicly, even imperfectly, with retrospective analysis.
Expected output: 3-5 named attempts + what worked / regretted + stack composition +
retention data + public assets (repos / posts / courses) + 2026-04 freshness stamp.
Estimated time: 20-30 min.

**P1 — "MAST taxonomy mapped to Jetix 11-agent architecture — concrete failure-mode prevention matrix"**
*Gap coverage: Domain 7 MAJOR #1 (EU AI Act + compliance audit) + MINOR #1 (MAST cross-ref).*
Justification: Safety baseline for recursive swarm launch. Before Phase 4 (baseline
swarm construction) we must have failure-mode-by-agent matrix — else recursive
improvement amplifies latent MAST modes.
Expected output: 14 MAST modes × 11 Jetix agents matrix; current mitigation coverage;
residual risks; compliance (EU AI Act tier, GDPR Art. 17) audit notes; citations.
Estimated time: 25-35 min Deep Research; synthesis mode (not new research, cross-walking R-4 + Agent-Protocols).

**P1 — "Anthropic mailbox pattern — primary sources"**
*Gap coverage: Domain 2 MAJOR #3 (no official Anthropic engineering blog).*
Justification: Jetix current `comms/mailboxes/<agent>.jsonl` architecture rests on
"Anthropic mailbox pattern" — which (per Perplexity) is derived from leaked Claude
Code source code (WaveSpeed Apr 2026) + secondary analysis, NOT an official Anthropic
post. We need to verify: (a) whether an official writeup exists, (b) whether our
interpretation matches Claude Code internal implementation, (c) known failure modes
at production scale.
Expected output: primary sources inventory (official vs leaked-secondary) + concrete
Claude Code in-memory/file/UDS/remote-bridge channel semantics + reproducible
design notes for Jetix's JSONL-file-mailbox variant.
Estimated time: 15-20 min Deep Research.

**P2 — "Concurrent multi-agent MVCC / CRDT for knowledge-graph writes"**
*Gap coverage: Domain 5 MAJOR #1.*
Justification: Phase 4 baseline swarm will read/write Jetix wiki concurrently. No
current system publishes MVCC for knowledge-semantics writes; we need to know what
patterns exist in industrial KG (Neo4j, TigerGraph, Cognee) and what tradeoffs
apply.
Expected output: 3-5 approaches (CRDT / optimistic concurrency / transactional KG /
single-writer serialization) + production examples + tradeoffs for Jetix's scale
(thousands of edges, single-founder authority).
Estimated time: 15-25 min.

**P2 — "DSPy / TextGrad / meta-learning applied to production agentic systems"**
*Gap coverage: Domain 8 MAJOR #1.*
Justification: Recursive self-improvement (Jetix Phase 4 core thesis) needs grounded
production analog beyond Anthropic tool-testing-agent (40% gain). DSPy and TextGrad
exist as frameworks — but do any production systems use them at Jetix-scale?
Expected output: 2-5 named production systems + performance metrics + operational
cost + code-repo links + failure modes documented.
Estimated time: 20-30 min.

**P2 — "Knowledge-base rot half-life: empirical measurements"**
*Gap coverage: Domain 5 MAJOR #2.*
Justification: Lint / decay schedule design rests on rot timescale. No public
quantified data; industry is "aggressive decay + selective persistence" as pattern
without numbers.
Expected output: 2-5 empirical studies (academic or vendor) + vector-DB re-embed
intervals + wiki/markdown rot rate + agent memory ("strategies") rot + halving
benchmarks.
Estimated time: 15-20 min.

**P3 — "EU AI Act tier classification for consulting + productized services + holding Phase 3+"**
*Gap coverage: Domain 7 MAJOR #1 (compliance audit).*
Justification: Decision 15 revenue-gated unlocks include Phase 2+ DACH Mittelstand
expansion; GDPR + EU AI Act tiering is essential for DACH sales cycle. Not blocker
for Phase 2 research but needed by Phase 2 implementation.
Expected output: tier classification per SKU (Audit / Implementation / Retainer /
Fund / Matchmaker / Roy) + TOM mapping + documentation templates.
Estimated time: 25-35 min (regulatory research heavy).

**P3 — "LTV/CAC ratios for AI consulting retainers; vibe-revenue quantification"**
*Gap coverage: Domain 6 MAJOR #3.*
Justification: Productized retainer pricing Phase 1 should use benchmarked LTV/CAC
not guesswork. "Vibe revenue" retention documented qualitatively; quantitative
benchmarks would strengthen D18 pricing decisions.
Expected output: 5-10 agency / SaaS / AI consulting LTV/CAC benchmarks 2024-2026 +
retention curves for AI-specific offerings + vibe-revenue pattern statistical
evidence.
Estimated time: 15-25 min.

**P3 — "Constitutional Classifiers for private / self-hosted deployment"**
*Gap coverage: Domain 8 MAJOR #2.*
Justification: Constitutional AI + Classifiers (Anthropic 86% → 4.4% jailbreak rate)
are platform-only. Jetix Phase 3+ may want self-hosted equivalent for custom rule
enforcement; no public analog identified.
Expected output: 2-5 open-source / academic implementations + bench numbers +
integration path.
Estimated time: 20-30 min.

---

## Self-review notes

- **Coverage honesty.** 7 of 8 domains rated STRONG, 1 (none) rated MINIMAL or PARTIAL. This is
  accurate reflection of the corpus: the recent addition of Perplexity Apr 22 executive-brief +
  full output specifically fills what were PARTIAL-level domains (1, 4, 6) with named-entity
  + founder-cohort coverage. Domain 5 Major gaps (concurrent MVCC, KB-rot half-life) are not
  solvable by re-reading — they require Phase 2 new research. Domain 7 Major gap (EU AI Act
  audit) similarly.
- **Part 4 Perplexity integration.** Requirement was ≥5 Perplexity insights with verified citations;
  delivered 6 ([P]-marked #9, #16, #17, #18, #19 + #1 cross-mark). All 6 verified against primary
  links where possible.
- **Part 5 MINOR+MAJOR per domain.** Requirement met for all 8 domains.
- **Part 6 6-10 priorities.** Delivered 10 ranked: 4×P1 + 3×P2 + 3×P3.
- **Citation discipline.** Every insight and claim carries inline citation `[file §section]` or
  `[Perplexity-output.md Domain N §M]` + external primary-source URL where applicable.
- **Length.** ~7,400 words body excluding YAML frontmatter and tables; table-heavy; dense.
- **Non-goals held.** Not synthesis (no variant selection), not new Locks proposed, not opinion-giving beyond ranked priorities.
- **Language discipline.** Russian quotes preserved verbatim (per D1 Vision voice-preservation rule); English structural labels.

**END Phase 1 Master Inventory.**
