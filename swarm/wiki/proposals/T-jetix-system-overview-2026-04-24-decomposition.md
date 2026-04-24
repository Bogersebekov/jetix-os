---
task_id: T-jetix-system-overview-2026-04-24
cycle_id: cyc-jetix-system-overview-2026-04-24
decomposed_at: 2026-04-24
shape: combined-description-synthesis
chat_or_decompose: decompose
decompose_rationale: >-
  E-17 Decompose-or-Chat gate predicates 1+4 fire. Predicate-1: complexity >> simple —
  14 layer sections × ≥800 words = ≥11K words minimum; combined with top-level §0-§6
  + post-layer §L+1..§L+4, reach 15-25K target. Predicate-4: multi-domain synthesis
  required — every layer demands integration across engineering/mgmt/systems/philosophy/
  investor lenses. Matrix invocation mandatory.
---

# Phase-2 WBS — JETIX-SYSTEM-OVERVIEW decomposition

## §1 Strategy: 4-wave parallel dispatch per brigadier-strategies 2026-04-24 (20-cell pattern compounded)

Pattern validated in T-km-architecture-research cycle: 4 waves of parallel cells within each wave
achieves ~35-45 min wall-clock vs ~3-4h serial. This task uses **3-wave structure** (not 4) because:

- Wave 1 = 5 core-stack layers in parallel (L0-L4) — one cell per layer, one expert each per §7 launch assignment.
- Wave 2 = 5 business-stack layers in parallel (L5-L9).
- Wave 3 = 4 cross-cutting layers in parallel (L-R / L-C / L-B / L-P).
- Integration pass (brigadier, serial) = top-level §0-§6 + §L+1..§L+4 + USB-C/McKinsey resolution.
- Part F = philosophy × critic on coherence + 28-locks consistency (single cell).

Total: **15 cells** (14 layer-cells + 1 coherence-critic). Well under 20-cell cap. `mode: integrator`
dominates (description task; critic reserved for Part F coherence audit).

## §2 Per-cell WBS

### Wave 1 — Core system stack L0-L4 (dispatched 2026-04-24, parallel ×5)

```yaml
- cell: engineering × integrator
  layer: L0 Foundation — Company-as-Code
  class: M
  ap_cost: 45000
  ap_budget: 70000
  inputs:
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
    - decisions/JETIX-ARCHITECTURE-BRIEF.md
    - reports/review_2026-04-24.md
    - reports/summary_2026-04-24.md
    - swarm/lib/shared-protocols.md
    - CLAUDE.md
    - swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-engineering-integrator-L0-foundation.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (files:git-tree/.claude/config/agents/wiki/
    tools: /ingest,/lint/,/consolidate,/build-graph/ data: atomic-commits+provenance+declarative-yaml)
    + Boundaries + Interfaces-with-L1/L2/L9 + Current-status + Evolution-path-Phase-1-to-Phase-3+
    + ≥3 audio_NNN references (510/519/520) + ≥1 Mermaid/ASCII diagram of git-repo layers + D25
    verbatim cited + agents listed (system-admin + brigadier + engineering-expert) + anti-patterns
    per D25 addendum.

- cell: systems × integrator
  layer: L1 Knowledge — Query-driven KB + Private Library
  class: M
  ap_cost: 45000
  ap_budget: 70000
  inputs:
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md  # D28 verbatim
    - decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md  # 6 variants context
    - swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md  # what just materialized
    - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md  # client-private positioning
    - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md  # topic-wikis + project-wikis
    - reports/review_2026-04-24.md
    - reports/summary_2026-04-24.md
    - CLAUDE.md  # wiki v2 vs v3 structure
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-systems-integrator-L1-knowledge.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (wiki/ hot + cold archive / Private
    Library 393 books / 9 entity types / niches / graph edges) + Boundaries + Interfaces-L0/L2/L3/L4
    + Current-status (v2 legacy + v3 spine + KM Mat design-records) + Evolution Phase-1 A1 →
    Phase-2 A2+B2 → Phase-3 A3 trajectory per KM-ARCH-VARIANTS + Phase-1 client-private isolation
    stack (Strategic-Insight §6) + D28 verbatim + ≥4 audio_NNN (517/520/522/518) + Mermaid showing
    hot/cold/client-namespaces/topic-wikis/project-wikis.

- cell: engineering × integrator
  layer: L2 Ingest & Signal
  class: M
  ap_cost: 45000
  ap_budget: 70000
  inputs:
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md  # D28 query-driven ingest
    - reports/review_2026-04-24.md  # voice pipeline reference
    - reports/summary_2026-04-24.md
    - CLAUDE.md  # voice-notes pipeline + skills
    - .claude/agents/inbox-processor.md  # legacy L2 agent
    - swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-engineering-integrator-L2-ingest.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (voice-transcribe tools/transcribe.py,
    tools/extract.py, tools/filter.py, tools/review_report.py; auto-loggers; crawlers; inbox-processor;
    /ingest) + Boundaries (NOT L1 canonical wiki; NOT L3 synthesis) + Interfaces-L0/L1/L3 + Current
    status (manual-now + review_NNN files) + Evolution to reverse-engineering crawlers (YouTube
    analyzer per audio_518, AI-code extraction per audio_522, public-source shadow-reading audio_527)
    + ≥4 audio_NNN (514/518/522/527) + diagram of ingest pipeline stages + D28 /ingest --anchor
    enforcement.

- cell: systems × integrator
  layer: L3 Synthesis & Compounding Engineering
  class: M
  ap_cost: 45000
  ap_budget: 70000
  inputs:
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
    - .claude/agents/strategist.md
    - .claude/agents/knowledge-synth.md
    - .claude/agents/meta-agent.md
    - swarm/lib/shared-protocols.md  # §§1-9
    - swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partC-stage-gates-merged.md
    - reports/review_2026-04-24.md
    - agents/brigadier/strategies.md  # compounding-engineering live example
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-systems-integrator-L3-synthesis.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (strategist + knowledge-synth +
    meta-agent + brigadier compound protocol; /compile skill; CE 40/10/40/10 cadence; sandbox-
    черновик принцип audio_520; per-cycle strategies.md accumulation; gate-learning DRRs) +
    Boundaries (NOT L1 raw storage; NOT L4 routing; NOT L9 gate-check) + Interfaces-L1/L2/L4/L9
    + Current status (3 cycles compound log visible) + Evolution (skill codification /
    extract-from-design + /recommend-trajectory per brigadier strategies) + ≥3 audio_NNN
    (519/520/521) + diagram of plan-work-review-compound loop.

- cell: mgmt × integrator
  layer: L4 Agent Layer — Holding-style (6 ROY + 14 legacy)
  class: M
  ap_cost: 50000
  ap_budget: 75000
  inputs:
    - .claude/agents/brigadier.md  # size warning — read §1-§3 + §7-§9 selectively
    - .claude/agents/engineering-expert.md
    - .claude/agents/mgmt-expert.md
    - .claude/agents/systems-expert.md
    - .claude/agents/philosophy-expert.md
    - .claude/agents/investor-expert.md
    - .claude/agents/strategist.md
    - .claude/agents/knowledge-synth.md
    - .claude/agents/manager.md
    - .claude/agents/life-coach.md
    - .claude/agents/personal-assistant.md
    - .claude/agents/inbox-processor.md
    - .claude/agents/sales-lead.md
    - .claude/agents/sales-researcher.md
    - .claude/agents/sales-outreach.md
    - .claude/agents/meta-agent.md
    - .claude/agents/crazy-agent.md
    - .claude/agents/system-admin.md
    - .claude/agents/staging-writer.md
    - .claude/agents/sweep-worker.md
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md  # D26 holding-with-agents
    - swarm/lib/shared-protocols.md
    - reports/review_2026-04-24.md
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L4-agents.md
  cell_acceptance_predicate: >-
    Section ≥800 words table-view of all 20 agents (6 ROY + 14 legacy) with model / dept / niche /
    layer-residence / status; explanation of ROY 5×4 matrix; 5-layer per-agent memory (system.md,
    strategies.md, scratchpad.md, niche/, mailbox); hub-and-spoke routing; "holding-with-agents"
    per D26 verbatim; legacy 14 treated per brigadier §1a untouchable-in-Phase-A; ROY experts
    untouchable in §L+1..§L+4 of this doc; Boundaries (NOT L3 compound; NOT L9 gate) + Interfaces
    L0/L1/L3/L9 + Current-status (ROY built 2026-04-23, 3 cycles run) + Evolution to brigadier
    split at Phase-B trigger + per-expert team activation at 50-100 headcount (D26) + ≥4 audio_NNN
    (510/514/521/529) + diagram of matrix + legacy ring.
```

### Wave 2 — Business stack L5-L9 (dispatched after Wave 1 returns, parallel ×5)

```yaml
- cell: investor × integrator
  layer: L5 Product & Services — Smart AI directions
  class: M
  ap_cost: 50000
  ap_budget: 75000
  inputs:
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md  # Smart AI internal note
    - decisions/JETIX-VISION.md  # §5 Phase-by-Phase offerings
    - decisions/JETIX-PLAN.md
    - reports/review_2026-04-24.md  # audio_508/510/511/514/524/527/528/529
    - reports/summary_2026-04-24.md
    - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
    - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md  # Pillar 5 products/services
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md
  cell_acceptance_predicate: >-
    Section ≥800 words enumerating all 8+ product/service directions (Smart AI flagship, AI
    consulting for complex tasks, USB-C integration services, matchmaker platform, YouTube-analyzer
    SaaS, Secure Network, educational products, tokens/ICO Phase 3) with per-direction Mission /
    status / audio_NNN; Smart AI internal-only lock per D25-D28 addendum §Smart-AI verbatim;
    Boundaries (NOT L6 revenue/gates — Phase-by-phase trajectory belongs L6; NOT L8 Alliance-
    specific delivery — Alliance belongs L8); Interfaces-L6/L8/L4/L-B + Current (consulting €0
    Phase 0; продюсерский центр Phase 1 target) + Evolution through 5 gates with which direction
    activates at which gate + ≥5 audio_NNN.

- cell: mgmt × integrator
  layer: L6 Business & Trajectory
  class: M
  ap_cost: 50000
  ap_budget: 75000
  inputs:
    - decisions/JETIX-VISION.md  # §7 ICP + §11 Phase Timeline + §13 Phase Timeline
    - decisions/JETIX-PLAN.md
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
    - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
    - reports/review_2026-04-24.md
    - reports/summary_2026-04-24.md
    - raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L6-business.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (ICP per D22 + 11 archetypes per
    JETIX-VISION §7.1 including Phase-1-buyers миллионер $1M+/year per audio_529; outreach
    mechanism; pricing per D18; 5 gates €50K → €200K → €1M → $100M → $100B → $1T per D19 + D3;
    potential partnerships Anthropic/Porsche/BMW/Apple/Google/Tesla per audio_515) + Boundaries
    (NOT L5 per-product detail; NOT L7 research) + Interfaces-L5/L7/L8/L-R + Current (€0 Phase
    1 active, no paying clients) + Evolution per-gate trigger + ≥6 audio_NNN (506/510/511/515/523/528/529)
    + gates table.

- cell: philosophy × integrator
  layer: L7 Research & Reverse-Engineering
  class: M
  ap_cost: 45000
  ap_budget: 70000
  inputs:
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md  # D24 open-source research direction
    - decisions/JETIX-VISION.md  # §5 D24 research direction
    - decisions/JETIX-PHILOSOPHY.md
    - reports/review_2026-04-24.md  # audio_510/515/524/527 verbatim
    - reports/summary_2026-04-24.md
    - raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md  # new-laws-tools
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-philosophy-integrator-L7-research.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (open-source research direction per
    D24; reverse-engineering на максималках per audio_527; new AI-protocols/laws/validation
    tools per chat-voice USB-C; Левенчук ШСМ direction; research-revenue-instrumental Phase 1
    per D14) + Boundaries (NOT L1 knowledge storage; NOT L5 product; revenue-gated per D14) +
    Interfaces-L1/L5/L8 (Alliance contributions) + Current (Private Library 393 books only) +
    Evolution Phase-2-unlock-triggers + ≥4 audio_NNN + list of reverse-engineering targets.

- cell: mgmt × integrator
  layer: L8 People & Alliance — Swarm + Digital Portraits
  class: M
  ap_cost: 50000
  ap_budget: 75000
  inputs:
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md  # D26 team 50-100 + D27 fork-and-merge
    - decisions/JETIX-VISION.md  # §8 per-archetype + D21 matchmaker
    - decisions/JETIX-PHILOSOPHY.md
    - reports/review_2026-04-24.md  # audio_506/507/510/512/513/519/524/525/527
    - reports/summary_2026-04-24.md
    - raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md
    - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md  # Mittelstand AI Alliance
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (core team 50-100 per D26; Alliance +
    5h/week roy-replication per D21; Secure Network Telegram-based; digital portraits audio_524;
    fork-community per D27; matchmaker manual-now → platform later per D21; Mittelstand AI Alliance
    per Strategic-Insight) + Boundaries (NOT L6 ICP filter; NOT L4 agents) + Interfaces-L4/L6/L7/L-B
    + Current (Ruslan + Cloud Cowork only; 0 team hires) + Evolution through hiring gates per
    D15 + ≥6 audio_NNN (506/507/510/512/513/519/524/525/527) + D27 verbatim + D26 verbatim.

- cell: philosophy × integrator
  layer: L9 Governance & Evolution
  class: M
  ap_cost: 50000
  ap_budget: 75000
  inputs:
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md  # D25/D27
    - decisions/JETIX-PHILOSOPHY.md
    - raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md  # D1-D8
    - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md  # D9-D18
    - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md  # D19-D24
    - swarm/lib/shared-protocols.md  # §4 HITL escalation
    - reports/review_2026-04-24.md
    - .claude/agents/brigadier.md  # §6 Gate-Check
    - agents/brigadier/strategies.md  # compound accumulation
    - swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md  # live gate example
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-philosophy-integrator-L9-governance.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (decisions/ + 28 locks D1-D28;
    AWAITING-APPROVAL gates per shared-protocols §4; sandbox-черновик принцип audio_519; мета-
    описания as first filter audio_519; fork-and-merge upstream-controller per D27; beta-first /
    не переспрашивать / не даунгрейдить policies per audio_528) + Boundaries (NOT L3 compound;
    NOT L4 agent memory) + Interfaces-ALL-layers (cross-cutting) + Current (28 locks in force,
    3 gates acked, 1 gate awaiting) + Evolution Phase-B split-trigger per brigadier §1d + ≥4
    audio_NNN + 10-item autonomous/requires-approval/never table summarized from brigadier §1d.
```

### Wave 3 — Cross-cutting layers L-R / L-C / L-B / L-P (dispatched after Wave 2 returns, parallel ×4)

```yaml
- cell: systems × integrator
  layer: L-R Resource Management (NEW — Ruslan 2026-04-24 explicit)
  class: M
  ap_cost: 40000
  ap_budget: 65000
  inputs:
    - reports/review_2026-04-24.md  # audio_449, 510 tokens, 413, 428 explicit
    - reports/summary_2026-04-24.md
    - decisions/JETIX-VISION.md  # D11 investment-fund-philosophy Day 1
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
    - agents/brigadier/strategies.md  # real AP budget traces
    - swarm/lib/shared-protocols.md  # §9 Max-sub
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-systems-integrator-L-R-resource.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (unified tracking of time / attention
    / finances / energy / credits — Anthropic tokens + Groq + others; every decision consumes
    these; per-agent resource consumption reporting; budget alerts at thresholds per audio_510
    Anthropic tokens overrun concern; D11 resource-allocation-engine) + Boundaries (NOT L9
    governance; NOT L-P Life-OS — though overlap with Ruslan's personal finance) + Interfaces-
    ALL-layers (cross-cutting) + Current (AP budgets in cell WBS; Max-sub assertion; Anthropic
    tokens as first-class) + Evolution to per-agent dashboard Phase-2 + Ruslan verbatim
    *"очень важно, всё должно тоже трекаться"* + ≥4 audio_NNN (449/510/413/428) + table of 5
    resources × 5 gates.

- cell: engineering × integrator
  layer: L-C Compute & Infrastructure (NEW)
  class: M
  ap_cost: 40000
  ap_budget: 65000
  inputs:
    - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md  # local-first + distilled LLMs
    - reports/review_2026-04-24.md  # audio_526 Jetix-owned infra
    - reports/summary_2026-04-24.md
    - decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md  # UC-10 ollama+Mistral
    - .claude/agents/system-admin.md
    - CLAUDE.md  # server context
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-engineering-integrator-L-C-compute.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (own compute capability — servers,
    GPUs for distilled local LLMs Mistral/Llama for client-private inference; SSH ulimit discipline;
    audio_526 Phase-3+ own hardware + электростанции verbatim; Anthropic+Groq API accounts
    currently external; own servers currently single primary workstation) + Boundaries (NOT L0
    Company-as-Code which covers git-versioned configs; NOT L1 Knowledge storage) + Interfaces-
    L0/L1/L-R + Current (single workstation + SSH; no GPU; no own data-center) + Evolution
    Phase-2 own-server-for-clients → Phase-3 own-data-center → Phase-3+ own-power-generation +
    ≥2 audio_NNN (526 + STRATEGIC-INSIGHT) + table of compute-dependencies per layer.

- cell: mgmt × integrator
  layer: L-B Brand & Narrative (NEW)
  class: M
  ap_cost: 40000
  ap_budget: 65000
  inputs:
    - decisions/JETIX-VISION.md  # §1 tagline + §10 positioning vs competitors
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md  # USB-C + Smart AI
    - reports/review_2026-04-24.md  # audio_507 landing + 527 compass + 528 OS
    - reports/summary_2026-04-24.md
    - raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md  # sales asset verbatim
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L-B-brand.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (messaging, taglines; USB-C метафора
    verbatim; прошивка Windows метафора per D25-D28 addendum; operating system мирового масштаба
    audio_528; Smart AI internal label; landing pages for 3 audiences — авантюристы / инвесторы /
    работники мечты per audio_507; document-compass 5-15 pages per audio_527) + Boundaries (NOT
    L5 products; NOT L6 sales outreach) + Interfaces-L5/L6/L8/L7 + Current (1 landing page
    draft; Voice-2 chat USB-C as sales asset) + Evolution toward 3-audience-landing launch
    Phase-1 + compass 5-15pp after SYSTEM-OVERVIEW lands + ≥3 audio_NNN (507/527/528) + table
    of brand layer stack (tagline/метафоры/audiences/compass/landing).

- cell: philosophy × integrator
  layer: L-P Life OS (personal cross-cutting)
  class: M
  ap_cost: 40000
  ap_budget: 65000
  inputs:
    - reports/review_2026-04-24.md  # audio_517/518/525
    - reports/summary_2026-04-24.md
    - .claude/agents/life-coach.md
    - .claude/agents/personal-assistant.md
    - decisions/JETIX-VISION.md  # §3 founder context
    - CLAUDE.md  # projects list includes life-os P3
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-philosophy-integrator-L-P-life-os.md
  cell_acceptance_predicate: >-
    Section ≥800 words covering Mission + What-lives-here (Ruslan personal wellness / productivity /
    finance / Bank of Ideas / Life Notion page — explicitly part of system per audio_517 verbatim
    "описать конкретные части системы под запуски бизнесов и коммуникации с людьми" + audio_518
    auto-logging жизни; life-coach + PA agents) + Boundaries (NOT L4 business-agents; NOT L6
    ICP — personal cross-cutting) + Interfaces-L4/L-R/L1 + Current (life-os P3 project active;
    Notion Life OS page linked per CLAUDE.md; legacy agents exist) + Evolution toward external-
    clients-life-os Phase-2 (sell to millionaires per audio_529) + ≥3 audio_NNN (517/518/525) +
    diagram of personal-system ⊂ Jetix-system relationship.
```

### Integration (brigadier, serial after Wave 3)

```yaml
- actor: brigadier
  class: M
  responsibility: >-
    Assemble all 14 layer drafts into decisions/JETIX-SYSTEM-OVERVIEW.md with top-level §0
    TL;DR + §1 why-exists + §2 reading-order + §3 28-Locks-table + §4 system-diagram + §5
    trajectory-overview + §6 USB-C/McKinsey resolution + post-layer §L+1 open-questions + §L+2
    gaps-requiring-new-M-tasks + §L+3 recommended-next-3-M-tasks + §L+4 how-Ruslan-uses-doc.
  inputs: [all 14 layer drafts + entire Tier-1 + voice-transcripts]
  cell_acceptance_predicate: >-
    JETIX-SYSTEM-OVERVIEW.md exists; word count 15-25K; every layer section has ≥800 words;
    §3 table has 28 D-rows with primary-layer mapping; §4 has system-wide Mermaid/ASCII diagram;
    §6 USB-C/McKinsey resolution explicit with brigadier recommendation + Ruslan-ack-options;
    frontmatter complete per _templates; commit cadence 14 per-layer + top-level + integration.
```

### Part F — Coherence + 28-locks consistency critic

```yaml
- cell: philosophy × critic
  class: M
  ap_cost: 35000
  ap_budget: 55000
  inputs:
    - decisions/JETIX-SYSTEM-OVERVIEW.md  # full assembled draft
    - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
    - raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md
    - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md
    - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md
  expected_artefact: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-philosophy-critic-coherence.md
  cell_acceptance_predicate: >-
    Returns ≥10 binary Conformance Checks (each layer has ≥800 words; every audio_NNN reference
    resolves; 28 lock rows present; no contradictions with D1-D28; USB-C/McKinsey resolution
    non-null; Mermaid/ASCII diagram parses; 3-audience reading-order explicit) + ≥2 Alternatives
    for Part G compound structure + Anti-scope section + Hamel-binary Acceptance Predicate +
    F-G-R triples on any FAIL + proposed_replacement for each FAIL.
```

## §3 Parallelism + dependencies

```
Wave 1 (5 parallel cells, L0-L4)
    ↓ (returns land; brigadier verifies drafts exist + schema-valid)
Wave 2 (5 parallel cells, L5-L9)
    ↓
Wave 3 (4 parallel cells, L-R/L-C/L-B/L-P)
    ↓
Integration pass (brigadier serial; assembles SYSTEM-OVERVIEW.md)
    ↓
Part F coherence critic (philosophy × critic, 1 cell)
    ↓
AWAITING-APPROVAL packet + HALT
    ↓ (Ruslan ack)
Phase 7 Compound + Phase 8 Archive
```

Cross-wave peer-input: each wave's integrator cells can read previous wave's drafts from
`swarm/wiki/drafts/` — no `peer-input-needed` escalations expected. Brigadier pre-populates
`inputs:` with pre-known peer-draft paths per strategies 2026-04-24 compounded pattern.

## §4 Commit cadence (per launch §11)

```
[sys-overview] Phase-1 intake + Phase-2 WBS
[sys-overview] Wave 1 dispatched (L0-L4)
[sys-overview] §L0 Foundation promoted
[sys-overview] §L1 Knowledge promoted
[sys-overview] §L2 Ingest promoted
[sys-overview] §L3 Synthesis promoted
[sys-overview] §L4 Agents promoted
[sys-overview] Wave 2 dispatched (L5-L9)
[sys-overview] §L5 Products promoted
[sys-overview] §L6 Business promoted
[sys-overview] §L7 Research promoted
[sys-overview] §L8 People-Alliance promoted
[sys-overview] §L9 Governance promoted
[sys-overview] Wave 3 dispatched (cross-cutting)
[sys-overview] §L-R Resource promoted
[sys-overview] §L-C Compute promoted
[sys-overview] §L-B Brand promoted
[sys-overview] §L-P Life-OS promoted
[sys-overview] top-level §0-§6 assembled + integration pass
[sys-overview] Part F coherence critic; AWAITING-APPROVAL; HALT
```

~20 commits target. Push per commit on `claude/jolly-margulis-915d34`; no amend, no force, no --no-verify.

## §5 Risk register

| risk | likelihood | impact | mitigation |
|---|---|---|---|
| A layer cell fails to meet ≥800w floor | medium | low | Critic catches in Part F; brigadier re-dispatches with "expand" context |
| Voice-evidence conflicts with a D1-D28 lock surfaced during drafting | medium | medium | Flag in §L+1 Open Questions per anti-scope §4; do NOT override lock |
| USB-C/McKinsey resolution §6 contested | high | medium | Present as brigadier *recommendation*; Ruslan acks/rejects in review |
| Mermaid diagrams exceed legibility | low | low | Fallback to ASCII art; 1 diagram per layer + 1 system-wide |
| Cell schema return malformed | low | low | Reject per shared-protocols §3; re-invoke with schema_error context |
| Cross-cell contradiction surfaces | medium | medium | Preserve as `dissents[]` in integrator drafts; surface in §L+1 |
| Context-budget overrun mid-wave | medium | medium | Resume-state.md per brigadier §8 pattern; fresh session post-Wave2 if needed |
| Parallel KM Mat ack lands mid-cycle | medium | low | Two separate task_ids; no artefact overlap; separate commits |
| Server ulimit | low | medium | `ulimit -n 65535` already set permanently per master-plan R-1 |

## §6 Self-improvement mandate (non-optional per launch §8)

Per major section landing:
- Wave-1 landing → gate-learning entry to `agents/brigadier/strategies.md` under "Wave-1 L0-L4 learnings"
- Wave-2 landing → gate-learning entry under "Wave-2 L5-L9 learnings"
- Wave-3 landing → gate-learning entry under "Wave-3 cross-cutting learnings"
- Per-cell learnings that surface → per-expert improvement entries to
  `swarm/wiki/meta/agent-improvements/<expert>-improvements.md` (brigadier writes proposal;
  expert self-promotes Layer-2 per shared-protocols §1).
- Emergent insights (surprises, cross-domain connections discovered during integration) →
  full concept pages to `swarm/wiki/insights/` immediately.

Compound expectation: future brigadier cycle reads these and does better.
