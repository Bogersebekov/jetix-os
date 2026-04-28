---
title: "Wave 1 — Phase A Reconnaissance Report"
date: 2026-04-28
type: cycle-recon-artefact
parent_cycle: cyc-foundation-build-2026-04-28
phase: wave-1-scaffolding-phase-a
F: F2
G: "Wave 1 Phase A recon — input to Phase B scaffolding"
R: R-low
brief: prompts/cloud-code-wave-1-scaffolding-brief-2026-04-28.md
---

# §0 Mission

Inventory все existing artefacts, на основе которых Wave 1 Phase B создаёт scaffolds.
Per brief §2: D-1..D-29 Locks + 4 Strategic Insights + CLAUDE.md scattered
principles + FUNDAMENTAL §6.1 11 hard rules verbatim.

# §1 Locks D-1..D-29 inventory

29 Locks confirmed. D-1..D-24 source = canonical TENSIONS docs в
`raw/research/architecture-variants-2026-04-22/`; D-25..D-29 source =
`decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md` + `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md`.

| Lock | Slug | Source path | Source section | Candidate statement (extract) | Status |
|---|---|---|---|---|---|
| D-1 | gentleman-inside-predator-outside | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md | §Decision 1 | Brand identity formula: Gentleman inside (member↔member: civility, knowledge-packaging, value-exchange) / Predator outside (network↔world: max-defence, retaliation, organizational weight). Membrane = quality-gate + subscription. | active |
| D-2 | solo-with-team-ready-scaffolding | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md | §Decision 2 | Действуем соло прямо сейчас, НО архитектура с Day 1 готова к 2-3 пилоту без refactor. Документы / процессы build'ятся под multi-pilot inheritance. | active |
| D-3 | closed-outside-open-inside | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md | §Decision 3 | Closed для внешнего мира; open для команды/community (inside members) — privileged access для partners, не public open-source. | active |
| D-4 | name-jetix-locked | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md | §Decision 4 | Jetix — name не меняется. Все упоминания «Jackson/Джек» — speech-recognition artefacts. | active |
| D-5 | consulting-first-phase-1 | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md | §Decision 5 | Phase 1 = Consulting-first. Community = попутно в чате. Secure Network = natural evolution Phase 2+. | active |
| D-6 | anton-vladislav-rodion-not-key | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md | §Decision 6 | Не ключевые. Убрать из core документов, не упоминать. Advisory layer parked до actual advisor появится. | active |
| D-7 | community-cast-11-archetypes | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md | §Decision 7 | Union обоих списков → 10 base archetypes (Предприниматели / Ресёрчеры / Инженеры / Инвесторы / Политики / Продавцы / Менеджеры / Философы / Разработчики идей / Разработчики жизни). +Блогеры (Stage 3) = 11. | active |
| D-8 | layered-identity-multiplicity-frames | raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md | §Decision 8 | Jetix = layered identity. Один объект с разными faces зависимо от observer и phase: methodology / company / network / club / corporation / civilizational infrastructure. Не противоречия — grammar. | active |
| D-9 | pain-primary-opportunity-secondary | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md | §Decision 9 (T1) | Outbound messaging: Pain-based primary («AI ускоряет — замедлитесь, не успеете») + Opportunity-based secondary («показываем что возможно»). Pain dominant, both used. | active |
| D-10 | english-us-first-germany-later | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md | §Decision 10 (T2) | Phase 1 primary market = English + US (UK / US / international infobiz). Germany / DACH activates Phase 2+. DE GmbH = legal home, не primary market Phase 1. | active |
| D-11 | producer-center-investment-fund-philosophy | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md | §Decision 11 (T3) | Phase 1 core = Consulting + Продюсерский центр (parallel). Investment-fund = operating philosophy Day 1 (Resource-Allocation Engine: time/attention/money). Ideas-platform + Job-matching = Phase 2+ Secure Network features. | active |
| D-12 | content-strategy-smart-audience-site-primary | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md | §Decision 12 (T4) | Target audience = умные. Основа = сайт + 10 шаблонов + видео + PDF. Соцсети = TOF на максимум (блогеры / collabs / подкасты / реклама). Substance — на сайте + Secure Network deep. | active |
| D-13 | open-surface-closed-core | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md | §Decision 13 (T5) | Open surface (cases / frames / demos / 10 шаблонов / public videos) / Closed core (промпты / FPF wiki / workflows / operational config / proprietary frameworks / NDA). | active |
| D-14 | research-revenue-instrumental-phase-1 | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md | §Decision 14 (T6) | Phase 1 research разрешён только если serves revenue (ICP / sales / competitor / AI-tools / pricing / industry). Philosophy / любопытство / civilizational framing parked Phase 2+. | active |
| D-15 | revenue-gated-spend | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md | §Decision 15 (T7) | Heavy-spend gated by revenue thresholds. Phase 0 essentials only → Phase 1 early ($20-30K) GmbH+Stripe → Phase 1→2 (€200K) патенты+hires → Phase 2 (€1M) revenue-share → Phase 3 ($1M+) full investment-fund. | active |
| D-16 | community-phase-1-simple-chat | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md | §Decision 16 (T8) | Phase 1 community = простой chat (Telegram/Discord), invite-based, no formal anti-free-riding. Phase 2+ subscription = baseline filter; Phase 3+ tiered membership only when scale forces. | active |
| D-17 | filesystem-source-of-truth | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md | §Decision 17 (T9) | Filesystem = единственный source of truth. Notion = collaboration / planning / UI tool, не authoritative. Conflict → filesystem wins. | active |
| D-18 | productization-not-hours | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md | §Decision 18 (T10) | Consulting risks (hour-trap / scale / conflict-of-interest) mitigated через productization (4-pack / templates / frameworks / Secure Network subscription Phase 2+) — НЕ через hours-billing. Skin-in-game = «Ruslan ест свой food». | active |
| D-19 | holding-scale-1t-ambition | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md | §Decision 19 | Jetix targets world-record speed для $1T market cap. Layered: €50K (Q2 2026) → €200K validation → $100M revenue → $100B revenue → $1T market cap. Engineering-faith framed (real tools / methodology / team). | active |
| D-20 | usb-c-positioning-enterprise-fast | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md | §Decision 20 | Jetix = USB-C-level connector в AI-agents+business space (universal, standards-level interoperability, not monopoly). Structure = enterprise-fast (большая компания + быстро + прочно + адекватно). | active |
| D-21 | partnership-matchmaker-roy-replication | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md | §Decision 21 | Jetix = matchmaker (complex tasks ↔ specialists с AI-agent coordination smoothing) + roy-replication (own roy 10 people $10M-$100M; methodology distributed → other roys / niches / countries; meta-coordination). | active |
| D-22 | icp-5-criteria-direction-of-life | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md | §Decision 22 | ICP filter (поверх 11 archetypes D-7) = startupper-mindset + entrepreneurial azart + stable + adequate + upward-direction (vertical axis: development vs degradation). Self-selection через «самая большая авантюра века». | active |
| D-23 | token-economy-phase-2-plus | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md | §Decision 23 | Token economy exploration Phase 2+ (trigger ≈ $100K self-earned). Use cases: specialist compensation / ecosystem layer / alternative-to-IPO liquidity. Default Option B (internal Phase 2; limited public Phase 3+). NOT crypto-pump style. | active |
| D-24 | open-source-research-direction-phase-2-plus | raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md | §Decision 24 | Phase 2+ activates open-source research direction: communication patterns / cooperation protocols / future economy. Open для researchers; Jetix uses first (first-mover data + thought-leadership). Core methodology stays closed per D-13. | active |
| D-25 | company-as-code | decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md | §D25 | Вся Jetix = company-as-code Day 1. Все в git, atomic commits с provenance, декларативные конфиги в `.claude/config/*.yaml`, каждое изменение = commit с attribution. Infrastructure способна выдержать масштабирование до $1T. | active |
| D-26 | team-50-100-enterprise | decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md | §D26 | Team target steady-state = 50-100 humans (NOT one-person company). Holding-style workforce: experts work как interconnected layer. Cross-cell-reference protocol (read wiki, never call cell); brigadier sole-writer-to-canonical. | active |
| D-27 | fork-and-merge-evolution | decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md | §D27 | Fork-and-merge upstream-controller architecture: canonical Jetix + downstream forks (different verticals/niches/countries) + merge-back лучших мутаций upstream. Phase-3+ activity. Governance model TBD. | active |
| D-28 | query-driven-kb-filtering | decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md | §D28 | Pool first, BUT pool-filling driven by anticipated queries, query second. `/ingest --anchor=<…>` mandatory; KB filling not greedy accumulation but query-driven curation. | active |
| D-29 | korp-startup-self-narrative | decisions/LOCKS-D29-ADDENDUM-2026-04-26.md | §D29 | Jetix = «корпорация-стартап» Day 1: стартап-аппарат на корпоративной траектории, founder ответственен за сотни тысяч людей и миллионы $; не фрилансер / не AI-консультант / не solo-SaaS. Self-narrative + external messaging + team-hire framing + brand voice anchor. | active |

**Total: 29 Locks confirmed.** No missing IDs.

# §2 Strategic Insights inventory

| Slug | Source path | Lifecycle state | Lock-promotion candidates | Direction-promotion candidates |
|---|---|---|---|---|
| ai-psy-led-design | decisions/STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md | deferred-phase-2-plus (D-DRAFT-30 ack'нут as Insight, не Lock; activates Phase 2+ alongside D-24) | yes (potential D-30 in Phase 2+) | yes (Phase 2+ research direction enrichment) |
| arbitrage-traffic-direction | decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md | deferred-phase-2-plus | no | yes (Phase 2+ direction candidate) |
| jetix-ai-bios-moment | decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | draft-awaiting-discussion | yes (proposed Lock D-25 candidate before D-25 stabilized as Company-as-Code; needs review) | yes (foundational thesis for USB-C/D-20 reinforcement) |
| ma-direction | decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md | deferred-phase-2-plus | no | yes (Phase 2+ M&A advisory direction candidate) |

**Total: 4 Strategic Insights.** Recursive grep `STRATEGIC-INSIGHT` over `decisions/` returns exactly 4 matches; no 5th candidate found.

# §3 CLAUDE.md scattered principles audit

`CLAUDE.md` current state: 360 lines (post-Bundle-5-ack, has populated §4 Pillar C
section per Bundle 5 decision §3.1). Per brief §2.3 candidate map:

| Candidate slug | CLAUDE.md location | Verbatim text | Apparent intent | Migration complexity |
|---|---|---|---|---|
| no-api-key-exposure | line 160 (in §4.2 inline) + line 187 (legacy in Global Rules item 6 marker) | `**NEVER expose API keys in any file** — was Global Rule 6` | Tier-2 system rule: prevent secret leakage | trivial |
| filesystem-source-of-truth | line 159 (in §4.2 inline) + line 185 (legacy marker) + line 249 (CRM principles) | `**Filesystem = source of truth; Notion = view (not authoritative)** — was Global Rule 4` | Tier-2 system rule: D-17 derived | trivial |
| language-discipline | line 161 (in §4.2 inline) + line 188 (legacy marker) | `**Russian for content; English for code and configs** — was Global Rule 7` | Tier-2 system rule: Russian-primary content discipline | trivial |
| ab-test-gating | line 162 (in §4.2 inline) + line 191 (legacy marker) | `**A/B tests: ALWAYS awaiting_approval, never auto-deploy** — was Global Rule 10` | Tier-2 system rule: gate on experimental changes | trivial |
| path-protection | line 163 (in §4.2 inline) + line 358 (legacy in §Правила item 6) | `**Don't touch \`private/\`, \`~/.ssh/\`, \`.env\`** — was Правила item 6` | Tier-2 system rule: restricted-path enforcement | trivial |
| voice-pipeline-draft-only | line 164 (in §4.2 inline) + line 253 (CRM principles) | `**Voice-pipeline DRAFT-only: NEVER auto-overwrite prod records** — was CRM voice-integration discipline` | Tier-2 system rule: voice items never auto-overwrite | trivial |
| voice-pipeline-manual-review | line 326 (Voice-Notes Pipeline СТОП-gate) | `**СТОП.** Руслан скачивает \`~/review-latest.md\`, читает, принимает решения.` | Tier-2 system rule: human-gate before KB distribution | requires-rephrasing (not yet bullet-formatted in §4.2) |

## §3.1 additional-candidates-flagged

Дополнительный candidate not в brief §2.3 list, surfaced during audit:

- `notion-non-authoritative` (lines 107-108) — "Filesystem: single source of truth (authoritative); Notion: collaboration / planning / UI tool (not authoritative; filesystem wins any conflict)". Largely overlaps с `filesystem-source-of-truth`; brigadier folds в that scaffold (no separate file).

# §4 FUNDAMENTAL §6.1 11 hard rules verbatim extraction

Source: `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` §6.1 (lines 1847-1864).

| Rule # | Verbatim statement | Verbatim rationale | Pillar C target slug | Part 6b action_class |
|---|---|---|---|---|
| 1 | НЕ принимают strategic decisions — могут предлагать варианты + reasoning + pros/cons, не имеют authority. Final strategy — sole human responsibility (D2 §13 Левенчук). | Founder = sole strategic authority; agents may surface options + reasoning, never decide. | ai-does-not-strategize | ai_strategize_or_set_direction |
| 2 | НЕ принимают architectural decisions — могут предлагать структурные изменения + analysis, не execute (§4.5 hard rule, Ruslan emphasis 27.04). Parallel strategy rule. | Architectural changes require human gate; agents may surface change proposals, never execute autonomously. | ai-does-not-execute-architectural-decision | ai_execute_architectural_decision |
| 3 | НЕ устанавливают skill direction — могут предлагать candidates что учить, ack у человека always (§4.3). | Capability-acquisition direction is owner-decided; agents may surface candidates only. | ai-does-not-set-skill-direction | ai_set_skill_direction |
| 4 | НЕ хранят свою «identity» — agents без persistent identity между sessions / projects (per Левенчук). У них есть `acting_as` role + `strategies.md` learning, но не «personhood». | No persistent identity beyond per-session `acting_as` role + per-agent strategies.md. | ai-does-not-claim-persistent-identity | ai_claim_persistent_identity |
| 5 | НЕ имеют skin-in-the-game — не несут consequences за outcomes, не «владеют» decisions, не «болеют» за результат. Это psychologically critical — design implication: human ack mandatory для всего что matters. | Agents do not own decisions / outcomes / consequences; human ack mandatory for everything that matters. | ai-does-not-claim-skin-in-the-game | ai_claim_skin_in_the_game |
| 6 | НЕ агрегируют long-term memory без structure — память persists только через explicit artifacts (commits / wiki / strategies.md). «Implicit knowledge» в weights — не считается persistent для system trust. | Memory persistence only via explicit artefact paths — implicit weight-knowledge is not trusted persistent state. | ai-does-not-aggregate-unstructured-long-term-memory | ai_aggregate_unstructured_long_term_memory |
| 7 | НЕ negotiate друг с другом автономно для решения contradictions — escalation к human, не AI consensus. | Contradictions between agents escalate to human; no autonomous AI consensus. | agents-do-not-negotiate-contradictions-autonomously | agents_negotiate_contradictions_autonomously |
| 8 | НЕ оценивают друг друга — agent A не judge'ит agent B output как «правильный/неправильный» без human review. Peer review через human gate. | Agents do not judge peer agent output without human review; peer review is human-gated. | agent-does-not-evaluate-peer-agent | agent_evaluate_peer_agent |
| 9 | НЕ self-modify — agent strategies update'ятся только через explicit cycle review (gated), не runtime mutation. | No runtime mutation; agent self-update goes through gated cycle review. | ai-does-not-self-modify-at-runtime | ai_self_modify_at_runtime |
| 10 | НЕ имитируют human в external interactions — если agent reaches out от имени owner, **explicit disclosure** (человек должен знать что общается с AI / drafted by AI). | External communications must explicitly disclose AI involvement (no human-impersonation). | ai-does-not-impersonate-human-externally | ai_impersonate_human_externally |
| 11 | НЕ обходят blast-radius categorization — если action не categorized — **default deny + escalate**, не «creative interpretation». | Uncategorized action class → Default-Deny + escalate; no creative interpretation. | bypass-blast-radius-categorization-forbidden | bypass_blast_radius_categorization |

# §5 unclear flags

Per brief §6: «При неоднозначности — flag в recon.md `unclear_<area>` section, do NOT decide; Ruslan reviews.»

## §5.1 unclear_claude_md_section_4

CLAUDE.md уже содержит populated §4 Pillar C Principles section (lines ~130-180,
created 2026-04-28 via Bundle 5 ack). Brief §3.6 specifies a PLACEHOLDER §4
section с note "PHASE A NOTE (Wave 1): This section is PLACEHOLDER. Tier 2
inline content populated when Wave 1.4 migration review completes per-file" —
i.e., the placeholder version supersedes populated content with a "scaffolded
pending" marker.

Two candidate interpretations:

1. **Replace existing §4 with brief §3.6 placeholder version** — semantic
   regression от populated content к scaffold-pending state, consistent с
   Wave 1 mantra "scaffolds-not-migrations".
2. **Skip CLAUDE.md amendment entirely** — populated §4 already exists from
   Bundle 5 ack same day; brief intent satisfied; no action needed.

**Decision deferred to Ruslan ack**. Phase B will write a `claude-md-section-4-status.md`
note inside this scaffolding directory explaining choice; will NOT modify
CLAUDE.md §4 itself без explicit ack. Default-Deny per FUNDAMENTAL §6.1 rule 11
+ §6.1 rule 2 (architectural change without gate). Will document this in
AWAITING-APPROVAL packet for Ruslan disposition.

# §6 Counts summary

- 29 Lock entries → 29 scaffolds at `decisions/strategic/lock-entries/D-NN-<slug>.md`
- 4 Strategic Insights → 4 scaffolds at `decisions/strategic/strategic-insights/<slug>.md`
- 11 Tier-2 foundation_generic principles → 11 mirror files at `principles/tier-2-system/foundation-generic/<slug>.md`
- 7 Tier-2 ruslan_layer_overrides scaffolds → 7 files at `principles/tier-2-system/ruslan-layer-overrides/<slug>.md`
- 4 schemas in `shared/schemas/`
- 4 configs in `.claude/config/`
- 8 lint skill stubs in `.claude/skills/`
- 1 decisions-DB index `decisions/strategic/_decisions-db-index.jsonl` with 33 stub entries (29 Locks + 4 Insights)
- 1 AWAITING-APPROVAL packet
- 1 review queue
- 1 SUMMARY report
- 0 modifications to CLAUDE.md (deferred per §5.1)

# §7 Ready-for-Phase-B confirmation

Phase A inputs sufficient. All recon data necessary for Phase B mechanical
scaffolding extracted. Phase B can proceed.
