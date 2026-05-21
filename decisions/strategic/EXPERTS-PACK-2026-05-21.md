---
title: Experts Pack — Jetix через 5 ROY swarm lenses
date: 2026-05-21
type: experts-pack-substrate
parent_prompt: prompts/expanded-docs-substrate-2026-05-21.md
parent_phase_0: reports/expanded-docs-2026-05-21/phase-0-fpf-lens-scope.md
parent_plan: daily-logs/_EXPANDED-DOCS-PLAN-2026-05-21.md
prose_authored_by: brigadier-scribe (Server CC autonomous — substrate only, no strategic prose authoring)
target_audience: Ruslan + future audiences receiving Jetix pitch
F: F2
G: experts-pack-2026-05-21
R: refuted_if_5_lenses_absent_OR_cross_synthesis_missing_OR_R1_strategic_prose_authored_OR_LOCK_modified
constitutional_posture: R1 surface + R6 provenance + IP-1 STRICT + EP-5 F-grade + AP-6 dissent preserved + research-pool-pattern + SKIP-list-integrity
word_count_target: ~4500-5000w
status: ACTIVE
---

# Experts Pack — Jetix через 5 ROY swarm lenses

> **Объект:** Описание Jetix-системы через 5 ROY swarm expert lenses (engineering / investor / mgmt / philosophy / systems) с пересборкой corpus substrate. **Brigadier substrate only** — R1 strategic prose stays с Ruslan. Каждая lens читает свой top-5-7 высокосигнальных substrate-доков per Phase 0 матрицы 5×15 [src: reports/expanded-docs-2026-05-21/phase-0-fpf-lens-scope.md §4].

---

## §0 Intro — что такое Experts Pack и почему FIRST

**Что:** Описание Jetix через 5 native expert lenses + corpus pass через каждую призму.

**Почему FIRST в expanded docs scope:** ROY swarm = native Jetix substrate (5 experts × 4 modes = 20 routing cells per Foundation v1.0 Bundle 5 LOCKED 2026-04-28 [src: CLAUDE.md `## Active ROY Swarm`]). Jetix описан через 5 expert frames = **self-coherent** + signals depth. Если делать Questions / Tasks / Dev Plan / One-pager без expert pass, downstream documents становятся «slop» без expert depth.

**Что НЕ делает (constitutional posture):**
- ❌ Strategic prose authoring (R1 / Pillar C Tier 2 rule 1 — owner sole strategist; agents draft only)
- ❌ Locks для 20-25% take rate (R-batch-9-N1; DR-26 gates math validation pending [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §6])
- ❌ SKIP-list breach (O-62 Fund-of-Humanity / O-66/67/68 NOT surfaced [src: FINAL v2 §5])
- ❌ Tier B autonomous promotion (research-pool pattern strict)
- ❌ AP-6 dissent averaging — verbatim preservation

**Как Experts Pack informs остальные 4 docs:**
- **Questions Pack:** каждая lens surface own questions → unified Questions Pack
- **Tasks Pack:** prioritize 48 KAs через 5 lenses — какие KAs best-leverage каждую expert competency
- **Dev Plan:** 5 horizons reviewed через 5 lenses — какой horizon что каждый expert prioritizes
- **One-pager:** какие 1-2 lens primary per audience (L1 engineer → eng+inv; L2 amplifier → mgmt+sys; L3 institutional → phil+sys; humanitarian → phil+mgmt)

---

## §1 Engineering-expert lens — clean code / architecture / Compounding Engineering

**Self-lens summary (`.claude/agents/engineering-expert.md` re-read):** Compounding-Engineering + clean-code suite (Ousterhout / Brooks / Fowler / Martin / Hunt-Thomas) + Unix philosophy + AI-native patterns (Karpathy LLM-Wiki, Cursor / Aider / Factory / Replit) + architecture heuristics (Anthropic Orchestrator-Workers, Shape Up). Primary alpha: artefact (α-2). Produces code-review.md / architecture-proposal.md / tool-eval.md / refactor-proposal.md.

### §1.1 Что engineering-expert видит в Jetix

Jetix = **AI-native multi-agent system as code-and-config product**. The system itself = engineering artefact (filesystem source-of-truth per Global Rule 4 [src: CLAUDE.md L141]; Notion = view-only). Three layers visible to engineering lens:

1. **Substrate layer** — Foundation v1.0 (11 Parts + Pillar C) as architectural skeleton; YAML schemas (`shared/schemas/`); shared protocols (`swarm/lib/shared-protocols.md`); routing table (`swarm/lib/routing-table.yaml`).
2. **Agent layer** — 5 ROY swarm experts + brigadier + 3 mini-swarms (project-brigadier template, quick-money-brigadier, levenchuk-deep-dive-brigadier stub).
3. **Wiki+Hypothesis+CRM layer** — `swarm/wiki/` v3 (typed-edge KB), `hypotheses/` 7-layer architecture (overnight 20.05 evening; 9 skills CLI), `crm/` 169 contacts (KA-03 overnight; 14 sections per person/org).

### §1.2 Strongest Jetix components от engineering lens

| Component | Why strong (engineering view) |
|---|---|
| ROY swarm scaffolding | 5 expert agent files = hub-and-spoke per Part 4 §H IP-1; mode-allowlist + write-scope-glob + decision-rights ritual in each file = explicit contracts [src: `.claude/agents/engineering-expert.md` §1d] |
| Foundation 11 Parts + Pillar C | F8 schemas (F-G-R / Default-Deny / Halt-Log-Alert / Corrigibility / WORD COUNT 10K-20K) under `shared/schemas/` = formal contracts not vibes [src: CLAUDE.md `### F8 Constitutional schemas`] |
| Wiki v2 (Karpathy LLM Wiki + OmegaWiki structure) | 9 entity types + 9 typed edges (`wiki/graph/edges.jsonl`) + 6 niches + skills `/ingest` `/ask` `/lint` `/consolidate` `/build-graph` = grep-friendly до 10K records [src: CLAUDE.md `## Wiki Architecture v2`] |
| Hypothesis Architecture 7-layer | Overnight build 20.05 evening; first-class `hypotheses/` dir + 9 CLI skills + 5 samples H-001..H-005 + alpha-machinery (OMG Essence 2.0 inspired) + Friday ritual scaffold [src: hypotheses/docs/architecture-overview.md + daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §1 row 2] |
| KA-03 CRM | 169 contacts segmented (7 L1 / 35 L2 / 51 L3) с 13 pipeline statuses + voice-pipeline DRAFT-only integration + 24 roles in 6 groups + idempotent `/crm-rebuild-index` [src: CLAUDE.md `## CRM System`] |

### §1.3 Weakest Jetix components от engineering lens

| Component | Why weak (engineering view) |
|---|---|
| Technical brief (C.3) | NOT STARTED 20.05 [src: decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md §1]; L1 engineer cohort recruiting (Karpathy lineage / OSS maintainers / ML researchers) requires engineering-depth doc that doesn't yet exist |
| Deployment story | Ruslan operates solo; no CI/CD for agent system itself; no eval-driven testing per Boris Cherny pattern; agent strategies.md updates manual rather than gated cycle outputs (Pillar C rule 9 violation surface — preserved via gates но enforcement layer thin) |
| ROI clarity для L1 engineers | «Что engineer получит за 6 weeks Workshop?» — substrate sparse beyond «free учебник + Claude Code access + community + hypothesis arch» [src: decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md §6]; concrete portfolio outcome / skill ladder unclear |
| LLM provider lock-in risk | Claude Max sub + Anthropic Sonnet 4.6 / Opus 4.7 heavy dependency; no abstraction layer if Anthropic pricing/availability shifts; ROY-INFORMATION-DIET locks no API billing but doesn't address provider diversification |
| Wiki v2 scale beyond 10K records | Current spec optimised до 10K (grep-friendly); 1M users EOY 2026 KEYSTONE [src: audio_686] implies scale beyond grep-bounds; sharding / community-Louvain migration plan partial |

### §1.4 5+ open questions / risks from engineering lens

1. **Q-ENG-1** В каком point Wiki v2 grep-friendly modell breaks down? (10K limit per CLAUDE.md; 1M user trajectory implies migration required by ~ Q3 2026.)
2. **Q-ENG-2** Какая верификационная архитектура для агентского self-modification? (Pillar C rule 9 «no self-modification at runtime» — но Layer 2 strategies.md self-write exception. Где enforcement layer?)
3. **Q-ENG-3** Cursor / Aider / Factory / Replit integration story — Jetix как «AI-native» but какой DX (developer experience) для contributor outside Anthropic Max?
4. **Q-ENG-4** Eval-driven tooling для hypothesis architecture — 5 samples + 9 skills built overnight, но eval suite ещё нет; how to falsify each hypothesis по schedule?
5. **Q-ENG-5** Multi-agent orchestration cost — Phase A = 6 agents (brigadier + 5 experts); Phase B split-triggers могут multiply количество. Token economics at scale?
6. **R-ENG-1** Engineering-expert sole-writer of canonical wiki forbidden (Q2 brigadier-only) — но Layer 2 self-write exception. Drift risk при Phase B split.

### §1.5 Cross-cite — Левенчук engineering connection

Левенчук distillation Гл. Инженерия личности 2023 + Метод как объект 1-го класса (Методология 2025 Гл. 4) = direct engineering substrate [src: research/levenchuk-books-distillation-2026-05-20/06-cross-link-к-jetix-substrate.md §3 findings 1+5]. Engineering-expert primary frame: «Метод как объект 1-го класса» ≈ Compounding Engineering Plan-Work-Review-Compound loop — каждая cycle делает следующую дешевле через `strategies.md` accumulation. Цитата: «mthd creates next mthd», compounding visible в `agents/<expert>/strategies.md` Layer-2 self-writes [src: CLAUDE.md L82].

K-research K-2 Engineer Workshop applicable [src: K-2 pattern — Engineer Workshop BL-1 retained per Updated Plan §3.4]: 5-15 founding engineer cohort = first-class engineering audience for Jetix Phase 1.

---

## §2 Investor-expert lens — capital allocation / unit-econ / moats / long-term compounding

**Self-lens summary (`.claude/agents/investor-expert.md` re-read):** Buffett owner-earnings + Graham margin-of-safety + Marks second-level thinking + Taleb antifragility + Munger inversion / lollapalooza. Phase-A canonical sources: RESULT-07 Holdco doctrine + AI-native unit-econ + JETIX-ARCHITECTURE-BRIEF §5.1 horizon-gate (€50K → €200K → €1M → $100M → $1T). Primary alpha: artefact (α-2; capital-allocation-memo / horizon-projection / moat-analysis / unit-econ).

### §2.1 Что investor-expert видит в Jetix

Jetix = **solo-founder consulting motion scaling toward holdco** через 5-tier horizon-gate (€50K Q2-shippable → €200K → €1M → $100M → $1T). Investor lens primary anchor: voice anchor audio_686 «1M users / $1B raised / 100M user-hours EOY 2026» KEYSTONE F2-3 [src: decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md §0.2 + voice anchor citation]. Современное состояние: $0 MRR; Max-subscription discipline (€300-800/month Phase-1 run rate); 18-month runway baseline.

### §2.2 Strongest Jetix components от investor lens

| Component | Why strong (investor view) |
|---|---|
| Mondragón ratio R12 anti-extraction | Distribution Plan §6 R12 paired-frame discipline + Pillar C Tier 2 candidate rule 12 (FUNDAMENTAL §6.1) + Ethereum substrate Option D Hybrid (Phase 2+ overlay; founder/avg wage cap + QF revenue distribution + fork-and-leave exit tokens) [src: CLAUDE.md §4.2 R12 programmable enforcement] — moat differentiation vs extractive Silicon Valley default |
| 20-25% take rate substrate | Voice batch-9 audio_710 explicit; «20-25% to platform with responsibility-pact reinvestment loop» — paired с responsibility-pact (R12 anti-extraction primitive) [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §2 row 7 + §6 R-batch-9-N1]; **provisional pre DR-26 unit-econ deep-dive validation** |
| 1M users → $1B raise trajectory | audio_686 KEYSTONE F2-3 = explicit horizon anchor; cascade 150 → 15 → 1M architecture [src: decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md §0.3] |
| Holdco doctrine fit | Buffett-Berkshire pattern (capital allocator centre + autonomous BUs below + 30% hurdle rate) maps directly to Jetix-as-platform supporting cohort outcomes [src: investor-expert.md §2.4 Pattern P6] |
| Specific-knowledge moat (Naval) | Левенчук + ШСМ + 16 транс-дисциплин distillation + 12-Component Audit + Master Map 726-line systems view = uncopyable substrate (not commodity) [src: research/levenchuk-books-distillation-2026-05-20/00-SUMMARY §5 top-10 bridges; 6 ⭐⭐⭐ chapters identified] |

### §2.3 Weakest Jetix components от investor lens

| Component | Why weak (investor view) |
|---|---|
| Monetization unproven (current MRR $0) | No first revenue; «$100K baseline summer 2026» voice anchor audio_681 but conversion mechanism unspecified |
| Margin-of-safety arithmetic absent | No unit-econ-arithmetic.md ever drafted; DR-26 launch pending — until result, 20-25% take rate provisional, NOT publicly lockable [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §6 R-batch-9-N1] |
| Owner-earnings unstated | Buffett owner-earnings (= GAAP + depreciation - maintenance capex - working capital change) never computed for Jetix as business; pattern P1 critic Conformance check C1 fail by default |
| Risk-of-ruin floor unstated | What burn rate ends Ruslan runway? ROY-INFORMATION-DIET locks €300-800/month но не stated explicit «cycle ends at X months» |
| Cohort intake mechanism unclear | First-cohort quantity / selection / equity-like stake distribution unspecified; Hackathon Platform concept doc + Workshop BL-1 partial substrate but cohort onboarding economics absent |

### §2.4 5+ open questions / risks from investor lens

1. **Q-INV-1** Final % take rate after DR-26 unit-econ validation — 20% / 25% / piecewise / Mondragón-style?
2. **Q-INV-2** Mondragón ratio cap (founder/avg max ratio) — 6:1 (классический Mondragón) / 9:1 / другое? [src: CLAUDE.md §4.2 R12 programmable enforcement]
3. **Q-INV-3** QF (Quadratic Funding) matching pool size + mechanic — какой источник matching capital?
4. **Q-INV-4** First-cohort partnership equity-like stake distribution — founding partner gets % platform / per-cohort residuals / what?
5. **Q-INV-5** Fork-and-leave exit token mechanic — Ethereum substrate Option D Hybrid (Phase 2+ deferred) но concrete deploy timing?
6. **Q-INV-6** Revenue split per L1 / L2 / L3 partnership tier — Distribution Plan §3 cascade architecture not yet monetized per-tier
7. **R-INV-1** Unit-econ slippage [src: R-batch-9-N1 daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §6.3]; DR-26 launch pending; pre-result public lock = AP-6 violation candidate
8. **R-INV-2** Moat defensibility — specific-knowledge (Naval) substrate, но первый external corroboration (Левенчук response Week 2) pending [src: A-5 Левенчук pitch drafting Week 2]

### §2.5 Cross-cite — Distribution Plan + Mondragón + QF research

Distribution Plan §5 monetization + §6 R12 paired-frame [src: decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md §5-§6]. Mondragón cooperative substrate maps directly: 80,000-employee federation; founder/worker wage ratio enforced 6:1 max; profits to community 30%, operations 45%, capital reserve 25% — структура pattern для R12 programmable enforcement (FUNDAMENTAL §6.1 candidate rule 12 acked 2026-05-12 [src: CLAUDE.md §4.1 rule 12]). QF research (Buterin / Weyl Quadratic Funding) substrate referenced в Ethereum substrate ack [src: CLAUDE.md §4.2 R12 programmable enforcement Phase 2+ Ethereum acked 2026-05-18].

---

## §3 Mgmt-expert lens — PM / delivery / ethics-surface

**Self-lens summary (`.claude/agents/mgmt-expert.md` re-read):** PMBOK 7 principles + Shape Up + Opportunity-Solution-Tree (Cagan/Torres) + Grove Output/Leverage + 37signals opinionated. Primary alpha: task (α-1). Produces prioritization.md / delivery-plan.md / stakeholder-map.md / BA-Cycle-lite ethics-surface.

### §3.1 Что mgmt-expert видит в Jetix

Jetix = **multi-stream delivery operation** across 8 active projects + 11 A-actions Week 1 + 48 KAs + 22 Tier B candidates + 25 DR research candidates + 169 CRM contacts. Mgmt lens primary concern: **delivery cadence sustainability** при solo-operator constraint (Ruslan) + Manager attention budget max 20 active tasks (Pillar C §4.2 — RUSLAN-LAYER cap [src: CLAUDE.md §4.2]).

### §3.2 Strongest Jetix components от mgmt lens

| Component | Why strong (mgmt view) |
|---|---|
| 48 KAs + 11 A-actions consolidated | batch-7 (16 KAs) + batch-8 (14 KAs) + batch-9 (18 KAs) = 48 raw [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §0]; 7 A-actions FINAL v2 + 11 A-actions Updated Plan 21.05 = Kanban-ready backlog |
| Daily Log discipline | Append-only chronology + day-goal-of-day pattern + voice-pipeline integration (run_pipeline.sh 4 steps + manual review) [src: CLAUDE.md `## Voice-Notes Pipeline`] |
| Weekly Friday reflection ritual | A-7 from FINAL v2; Hypothesis Architecture 7-layer overnight build operationalised Friday cadence scaffolding [src: hypotheses/docs/architecture-overview.md §5 short-term plan] |
| Stage-gated B3 mechanic | `/project-de-morph` rollback skill + `/project-promote` для bets→consulting/research/product при SG-4 [src: CLAUDE.md `## KM MVP quick ops`]; реверс возможен через git revert |
| CRM 169 contacts с pipeline statuses | 13 pipeline statuses + draft_from_voice → cold → warm → contacted → discovery_call → proposal → negotiation → closed_won/closed_lost; stuck detection >14d no touch surfaces [src: CLAUDE.md `## CRM System`] |

### §3.3 Weakest Jetix components от mgmt lens

| Component | Why weak (mgmt view) |
|---|---|
| Manager attention budget vs 48 KAs surfaced | Max 20 active tasks per Pillar C §4.2 [src: CLAUDE.md §4.2]; currently 48 KAs raw inventory — **needs prioritization pass** (Tasks Pack Phase 3 mandate) |
| Burnout signals | audio_708 «не выебываемся, яички в кулачок» self-coaching + «срочность колоссальна» tension preserved AP-6 [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §6 R-2]; Ruslan IA-8 reflection scheduled; mitigation cadence weak |
| Weekend тишина boundary | KA-07 R12 weekend review — what protects Sunday from intrusion? Mitigation: A-6 weekend KA-07 reviews scheduled but boundary enforcement substrate sparse |
| Priority-reversal rate KPI absent | mgmt-expert §3.4 L525 KPI «monthly reversal rate <20%» — never measured in Jetix; rolling-window discipline not yet built |
| Stakeholder map (169 CRM) → delivery-plan link | KA-03 done; но 169 contacts → which 14 Tier-1 active queue → which weekly cadence target — link not yet fully traced (A-NEW-8 ack queue review pending) |

### §3.4 Ethics-surface — R12 + KA-07

R12 Charter LOCKED 2026-05-12 (FUNDAMENTAL §6.1 candidate rule 12 [src: CLAUDE.md §4.1]); R12 programmable Ethereum substrate Option D Hybrid acked 2026-05-18 [src: CLAUDE.md §4.2]. **KA-07 R12 review weekend** [src: A-6 from FINAL v2] = active ethics-surface mgmt task. BA-Cycle lite applicable: BA-0 surface detection (capital with stakeholder impact + public commitment) → BA-3 audit trigger (when re-evaluate?).

### §3.5 5+ open questions / risks from mgmt lens

1. **Q-MGMT-1** Daily cadence sustainable scaling — 15-20/day (current Distribution Plan §0.4) → 50/day → 100/day → 1000/day? Where does Ruslan/agent boundary become hard?
2. **Q-MGMT-2** Manager attention budget enforcement — где hard cap 20 active tasks lands в скрипты / hooks / agent decisions? (Pillar C §4.2 has cap; enforcement layer surface sparse)
3. **Q-MGMT-3** Burnout signals + recovery cadence — какой leading indicator (sleep / mood / energy) trips circuit breaker?
4. **Q-MGMT-4** Weekly Friday ritual first execution (A-7) — какой output format / acceptance criteria / consequences of skipped?
5. **Q-MGMT-5** Cohort intake delivery contract — onboarding doc C.5 missing; «day 1-30 actions / mastery milestones / mentor pairing» substrate sparse [src: decisions/strategic/DISTRIBUTION-PLAN-2026-05-20.md §1 C.5]
6. **R-MGMT-1** Scope creep 48 KAs raw — без dedup + prioritization = method exhaustion candidate (AP-MGMT-5 priority-reversal-rate ≥20% sustained 1 month trigger candidate)
7. **R-MGMT-2** Tier-1 ack queue 14 names KA-03 — 30 min each × 14 = 7h batched; в один week realistic?

---

## §4 Philosophy-expert lens — epistemology / mental models / stoic / engineering foundations

**Self-lens summary (`.claude/agents/philosophy-expert.md` re-read):** Popper falsifiability + Kuhn paradigm shifts + Lakatos research programmes + Munger lollapalooza + 100+ mental models + Stoic dichotomy of control + Koen heuristic-as-method + Vincenti engineering knowledge taxonomy + Altshuller TRIZ + Descartes systematic doubt + Naval clear-thinking. Primary alpha: strategies-rule (α-3). Produces epistemic-audit.md / first-principles-reset.md / meta-decision-note.md / BA-Cycle-lite. Owns **epistemic** Рациональность (FPF L1003-1006 dual-own boundary — instrumental Рациональность is investor's).

### §4.1 Что philosophy-expert видит в Jetix

Jetix = **epistemically-disciplined system attempting humanity-scale claims with embedded falsifiability + dissent preservation**. Philosophy lens primary concern: claim status discipline (which claims F2 vs F5 vs F8) + paradigm coherence (when Jetix integrates Cagan + Левенчук + Buffett + Munger lenses, какой paradigm-shift acknowledged?) + Popper falsifiability for forecasts (audio_686 1M / $1B / 100M EOY 2026 — what observation refutes?).

### §4.2 Strongest Jetix components от philosophy lens

| Component | Why strong (philosophy view) |
|---|---|
| FPF spec rigour | 3758-line constitutional spec; IP-1/IP-2/IP-3/IP-7 + A.6.B + A.14 + B.3 + Janus duality + Constructor-Theory cut + Rule B graph-of-creation recursion closure [src: CLAUDE.md `### Constitutional documents`] — formal contracts not vibes |
| 8-Octagon LOCK structure | F8 schemas (F-G-R / Default-Deny / blast-radius / AWAITING-APPROVAL packet / Halt-Log-Alert / Corrigibility / WORD COUNT 10K-20K / canonical health-signal / message v2.0.0) [src: CLAUDE.md `### F8 Constitutional schemas`] |
| R1 Ruslan sole strategist discipline | Pillar C Tier 2 rule 1 «AI does NOT make strategic decisions» enforced via `prose_authored_by:` frontmatter [src: CLAUDE.md §4.1 rule 1] |
| AP-6 dissent preservation | 6 batch-9 dissent atoms preserved verbatim (dual-hypothesis 707 / тягучка 709 / господствующим 712 / фундамент 708 / etc.) [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §10 row «AP-6 dissent preserved»] |
| 6 ⭐⭐⭐ Левенчук chapters identified | СМ Т2 Гл. 5+6 (систем + системное мышление) + Методология 2025 Гл. 4 (метод объект 1-го класса) + Гл. 6 (5 регионов стратегирования) + Интеллект-стек Гл. 1 (16 транс-дисциплин) + Инженерия личности Гл. 8 (LXP) — deep FPF phase candidates [src: research/levenchuk-books-distillation-2026-05-20/00-SUMMARY-FOR-RUSLAN.md] |

### §4.3 Weakest Jetix components от philosophy lens

| Component | Why weak (philosophy view) |
|---|---|
| AP-6 batch-9 atoms unresolved | 6 dissent atoms preserved verbatim, но resolution path для contradictions sparse (dual-hypothesis 707 = self-vs-method-vs-system framing tension; «фундамент» 708 = bedrock claim status unclear) [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §6.3 R-batch-9-N1..N4] |
| Self-validation abductive caveat (R-batch-9-N2) | audio_712-713 «I built it responsibly → it must be good» = abductive reasoning [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §6.3 R-batch-9-N2]; bootstrap proof structure не sufficient alone; external corroboration needed |
| Timing-argument hubris (R-batch-9-N3) | audio_709 «сейчас уже должны заниматься такие системы» implies Jetix = the-system → singular framing fragile; «one of the systems / contributing to convergence» softer framing per HR-4 paraphrase [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §6.3 R-batch-9-N3] |
| Civilization-threshold framing | «humanity-scale exokortex / 1M users EOY 2026 / 100M user-hours» — claim status F2-F3 (anecdote / single-case observation) per philosophy-expert §5.1; F5+ requires explicit measurement KPI |
| 5 GAPS Левенчук distillation | OMG Essence 2.0 alpha-machinery / Праксиология (Mises) / 5 регионов стратегирования / Системные ритмы / 16 транс-дисциплин full integration — substrate gaps [src: research/levenchuk-books-distillation-2026-05-20/00-SUMMARY-FOR-RUSLAN.md §4] |

### §4.4 5+ open questions from philosophy lens

1. **Q-PHIL-1** Epistemic humility frame для one-pager — каким language pitch material conveys «возможно мы ошибаемся / fork-and-leave fine» без undermining conviction?
2. **Q-PHIL-2** Proof structure for «методы по объединению методов» (O-107 canonical one-liner) — что falsifies? Popper-style bold conjecture vs Lakatos research programme framing?
3. **Q-PHIL-3** Civilization threshold framing — claim is descriptive (we observe X) или prescriptive (we should do Y)? Hume's is/ought wall.
4. **Q-PHIL-4** Левенчук responsiveness gate — если Левенчук не отвечает Week 2, какой epistemic status «specific-knowledge moat» (Naval) тезиса?
5. **Q-PHIL-5** R-batch-9-N4 governance R12 boundary — «Jetix управляет смыслами ценностями» (audio_711) = meaning-frame imposition risk vs voluntary opt-in paired-frame [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §6.3 R-batch-9-N4]; философский audit deferred to DR-31
6. **Q-PHIL-6** Hypothesis architecture 7-layer epistemic status — Layer 6 (OMG Essence alpha-machinery) imported from Левенчук substrate но Jetix-substrate proof-of-fit ещё нет

### §4.5 Cross-cite — Левенчук эпистемология + Stoic philosophy

Левенчук СМ Т2 Гл. 5+6 (системы / системное мышление) + Методология 2025 Гл. 5 (рациональность как навык) [src: research/levenchuk-books-distillation-2026-05-20/02-sistemnoe-myishlenie-2024-tom-2-toc-highlights.md + 03-metodologiya-2025-toc-highlights.md]. Stoic dichotomy of control applicable to A-actions: какие variables в-нашем-контроле (drafting / outreach send / hypothesis-add) vs не-в-нашем-контроле (Дмитрий response / Левенчук response / market reception). Premeditatio malorum applicable to one-pager risks: какие failure modes Ruslan уже учитывает?

---

## §5 Systems-expert lens — systems thinking / cybernetics / VSM / complexity

**Self-lens summary (`.claude/agents/systems-expert.md` re-read):** Meadows 12 leverage points + Ashby requisite variety + Beer VSM 5-layer recursion + Senge 11 laws of systems + Kauffman adjacent-possible + Wiener cybernetics + Kelly out-of-control + Mitchell complexity + Beinhocker. Primary alpha: artefact (α-2; system-model.md / feedback-loop-map.md / emergence-note.md / scalability-projection.md).

### §5.1 Что systems-expert видит в Jetix

Jetix = **5-tier nested system traversing solo-operator → Phase 1 cohort → L1/L2/L3 cascade → humanity-scale exokortex**. Systems lens primary concern: boundary definition + feedback loop polarities + leverage points (Meadows L1-L12 ranking) + requisite variety budget (Ashby).

**Native VSM-fit:** Beer VSM 5 levels mapping:
- Level 1 (operations) — Ruslan + agents executing daily work
- Level 2 (coordination) — brigadier hub-and-spoke per Part 4 §H
- Level 3 (audit/optimisation) — Compounding Engineering Plan-Work-Review-Compound 40/10/40/10
- Level 4 (intelligence/futures) — Hypothesis Architecture 7-layer + strategic horizon-gate substrate
- Level 5 (identity/policy) — Pillar C Tier 2 constitutional rules + FPF spec

### §5.2 Strongest Jetix components от systems lens

| Component | Why strong (systems view) |
|---|---|
| Jetix-as-exokortex frame | Левенчук Инженерия личности Гл. 8 verbatim metaphor «интеллект студента как выносная часть LXP» [src: research/levenchuk-books-distillation-2026-05-20/05-injeneriya-lichnosti-toc-highlights.md + §3 finding 5]; Jetix substrate-as-cognitive-extension primary frame |
| 5 acked concept docs F2 | JETIX-HACKATHON-PLATFORM / RECURSIVE-SELF-DEVELOPMENT-ENGINE / SYSTEM-MERGER-PROTOCOL-FPF / OUTREACH-SYSTEM-SCALABLE / EDUCATION-LAYER-SYSTEM-THINKING — 5 system-models acked 18.05 [src: ls decisions/JETIX-*-2026-05-18.md] |
| Master Map 726-line systems view | `swarm/wiki/...master-map.md` — 6 mermaid diagrams + 726-line systems substrate [src: prompt §0 substrate inventory line item «Master Map»] |
| Closed-loop O-111 | Jetix↔society closed-loop development — system-level reinforcing loop substrate (development feeds society feeds development) [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §3 row «O-111»] |
| OMG Essence alpha-machinery | Hypothesis Architecture Layer 6 — alpha-machinery from Левенчук substrate (GAP-1 closed overnight 20.05 evening) [src: hypotheses/docs/architecture-overview.md + Левенчук distillation 06-cross-link §3 finding 1] |
| Foundation 11 Parts holarchy | Each Part = sub-holon (System State Persistence / Signal Ingestion / Knowledge Base / Role Taxonomy / Compound Learning / Provenance / Human Gate / Project Lifecycle / Health Monitoring / Owner Interaction / External Touchpoints) + Pillar A/B/C overlay [src: CLAUDE.md `### 10 LOCKED Foundation parts`] |

### §5.3 Weakest Jetix components от systems lens

| Component | Why weak (systems view) |
|---|---|
| Jetix↔society closed-loop substrate sparse | O-111 single-batch surface (batch-9); no system-model.md authored для closed-loop diagram with polarity + substrate per loop |
| System boundary HR-3 batch-9 | audio_711 «Jetix управляет смыслами ценностями» — boundary between Jetix-as-tool vs Jetix-as-governance-layer ambiguous; voluntary opt-in paired-frame mitigates но system boundary still soft [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §6.3 R-batch-9-N4] |
| Requisite variety budget unstated | Ashby check predicate (controller must have ≥ variety than controlled system): Jetix controlling «meaning + values» layer requires immense variety — budget never explicitly stated |
| Adjacent-possible (Kauffman) forecast absent | From current state — какие states adjacent (1 hop reachable)? Kauffman lens to scalability projection currently sparse |
| Senge 11 laws audit absent | «Today's problems come from yesterday's solutions» / «the harder you push, the harder the system pushes back» — critic checklist not yet applied to Jetix interventions |

### §5.4 5+ open questions from systems lens

1. **Q-SYS-1** Jetix↔society closed-loop polarity — reinforcing loop (society funds Jetix → Jetix multiplies society) или balancing loop (extraction limits cap growth)? R12 paired-frame design intends reinforcing с anti-extraction floor.
2. **Q-SYS-2** System boundary — что вне Jetix scope? Pillar C rule 11 Default-Deny novel actions + Part 6b human gate define inside; outside boundary requires explicit anti-scope list ≥3 items (systems-expert §3.1 check 4)
3. **Q-SYS-3** Requisite variety budget at scale — 1M users + governance layer + meaning frame = which variety captured by Foundation + Pillar C + agents vs actual variety in 1M-user heterogeneity?
4. **Q-SYS-4** Feedback loops in cohort intake mechanism — 150 → 15 → 1M cascade architecture has which amplifying loops + which balancing? Distribution Plan §0.3 substrate cascade но polarity per loop not stated
5. **Q-SYS-5** Emergence claim — «методы по объединению методов» (O-107) emergence at system level? Counter-sample considered? Per systems-expert §3.1 check 3 «every emergent claim ≥1 counter-sample» — substrate sparse
6. **Q-SYS-6** Adjacent-possible audit — from current $0 MRR + 18-month runway + 5-15 founding cohort target Q3 2026, which states reachable in 1 cycle (1 month)? Which states require structural change?

### §5.5 Cross-cite — Beer VSM + Левенчук системное мышление

Beer VSM 5-layer recursion = native fit для Jetix nested-system structure (см. §5.1 mapping). Левенчук СМ Т1 + Т2 systems thinking distillation [src: research/levenchuk-books-distillation-2026-05-20/01+02-tom-toc-highlights.md] + intellect-stack 12-component audit [src: K-4 12-Component Audit per Updated Plan §1] + Method-Systems-Thinking deep [src: research/method-systems-thinking-deep-2026-05-19/]. Левенчук distillation finding 4: «СМ 2024 Т2 Гл. 8 (графы создания) ↔ Recursive Engine concept doc» — Левенчук direct structural source для graph-of-creation в Jetix Recursive Engine.

---

## §6 Cross-expert synthesis

Top 5 themes that emerge from ALL 5 lenses cumulative + top 5 gaps + recommended next research areas.

### §6.1 Top 5 themes (multi-lens convergence)

1. **R12 anti-extraction = primary moat differentiation** — investor lens (specific-knowledge moat) + philosophy lens (epistemic discipline + skin-in-the-game) + mgmt lens (ethics-surface BA-Cycle) + systems lens (closed-loop without extraction floor) converge. Engineering lens secondary (R12 programmable Ethereum substrate Phase 2+ deferred implementation).
2. **5 acked concept docs F2 + Master Map = system-level substrate proof** — systems + engineering + investor lenses converge: 5 concept docs (Hackathon Platform / Recursive Engine / System Merger / Outreach Scalable / Education Layer) [src: ls decisions/JETIX-*-2026-05-18.md] + Master Map 726-line = «specific-knowledge moat» (Naval) operationalised; not vibes.
3. **Hypothesis Architecture 7-layer = falsifiability discipline operationalised** — philosophy + systems + engineering lenses converge. OMG Essence alpha-machinery integration (GAP-1 closed); 9 CLI skills + 5 samples = epistemic discipline as code, not just claim.
4. **Левенчук substrate = primary external corroboration** — philosophy + systems + engineering lenses converge. 6 ⭐⭐⭐ chapters + cross-link matrix 5 books × 8 sources + DE-RU glossary 40 entries = «not made up» external proof structure.
5. **48 KAs + 11 A-actions = mgmt-primary delivery substrate** — mgmt lens primary; systems + engineering secondary (delivery as feedback loop in Compounding Engineering Plan-Work-Review-Compound).

### §6.2 Top 5 gaps (multi-lens convergence)

1. **Unit-econ unproven** — investor + mgmt + philosophy lenses converge. 20-25% take rate voiced batch-9 but margin-of-safety arithmetic absent (investor); priority-reversal-rate KPI absent (mgmt); F-grade explicit needed (philosophy). DR-26 launch gates.
2. **Technical brief (C.3) absent** — engineering + mgmt + investor lenses converge. L1 engineer cohort recruiting blocker; «ROI for engineer» story sparse.
3. **System boundary HR-3** — systems + philosophy + mgmt lenses converge. «Jetix управляет смыслами ценностями» boundary ambiguity; voluntary opt-in mitigates but requires explicit out-of-scope ≥3 items.
4. **Cohort intake mechanism unclear** — investor + mgmt + systems lenses converge. First-cohort quantity / selection / equity / onboarding (C.5) substrate sparse; «day 1-30 actions / mastery milestones» missing.
5. **5 GAPS Левенчук distillation** — philosophy + systems lenses converge. OMG Essence alpha-machinery / Праксиология / 5 регионов стратегирования / Системные ритмы / 16 транс-дисциплин — substrate-gaps known but unfilled.

### §6.3 Recommended next research areas (informs DR-33 «как доносить» scope refinement)

- **DR-26 unit-econ deep-dive ⭐⭐** — primary gate; Mondragón / QF / cooperative DAOs unit-econ baselines [src: A-NEW-7 from daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §2]
- **DR-31 governance R12 boundary audit** [src: daily-logs/_UPDATED-EXECUTION-PLAN-2026-05-21.md §6.3 R-batch-9-N4; P3 deferred] — long-term ethical-surface
- **DR-33 communication best practices** — Heath SUCCES + Pixar + TED + Feynman + Kahneman + audience-specific styling [src: daily-logs/_EXPANDED-DOCS-PLAN-2026-05-21.md §2 row 6 + §4 row Prompt 3]; informs all 5 docs styling iteration
- **Левенчук 6 ⭐⭐⭐ chapters deep FPF phase** — 50-100h budget; OMG Essence + 5 регионов + 16 транс-дисциплин full integration [src: research/levenchuk-books-distillation-2026-05-20/00-SUMMARY-FOR-RUSLAN.md §3 + §4]
- **System-model.md authoring для Jetix↔society closed-loop** — systems-expert primary task; substrate sparse

---

## §7 How Experts Pack feeds other 4 docs

| Doc | Primary lens informing | Secondary lens | Source feeding |
|---|---|---|---|
| **Questions Pack** | All 5 (each surfaces own Qs) | — | Q-ENG-1..5 + Q-INV-1..6 + Q-MGMT-1..5 + Q-PHIL-1..6 + Q-SYS-1..6 = ~28 questions из Experts Pack base + Questions Pack ~22 more from other substrate = ~50 target |
| **Tasks Pack** | Mgmt (primary; 48 KAs + 11 A-actions = task domain) | Engineering (KAs subset technical); Systems (cascade architecture as task structure) | §3.5 + §3.2 row 1 — Tasks Pack prioritization through 5 lenses |
| **Dev Plan** | Investor (horizon-gate primary) + Systems (5-tier nested) | Mgmt (delivery per horizon); Philosophy (R-batch-9 risks per horizon) | §2.1 horizon-gate + §5.1 nested-system mapping |
| **One-pager** | L1 engineer audience → engineering + investor lens | L2 amplifier → mgmt + systems; L3 institutional → philosophy + systems; Humanitarian → philosophy + mgmt | §1-§5 each lens informs which audience |

### §7.1 One-pager audience-specific lens primary

- **L1 engineer audience** (Karpathy lineage / OSS maintainers / ML researchers): primary lens = engineering + investor; emphasis на architecture (ROY swarm + Foundation 11 Parts + Hypothesis arch + Wiki v2) + unit-econ + moat (specific-knowledge Naval)
- **L2 amplifier audience** (R-comm influencers / Telegram channels / RU systems community): primary lens = mgmt + systems; emphasis на operational (48 KAs + Daily Log discipline + CRM 169 + cascade architecture)
- **L3 institutional audience** (LP/VC/Anthropic principals/MIM): primary lens = philosophy + systems; emphasis на epistemic (FPF + 8-Octagon LOCK + AP-6 dissent preservation) + civilization framing (humanity-scale exokortex + closed-loop O-111)
- **Humanitarian audience** (Open Philanthropy / AI safety / global welfare): primary lens = philosophy + mgmt; emphasis на ethics (R12 anti-extraction + Mondragón ratio + fork-and-leave + BA-Cycle) + impact (1M users + 100M user-hours)

---

## §8 Acceptance (Experts Pack Phase 1 closure)

- ✅ 5 ROY expert lenses applied (sections §1-§5 each ~600-800w)
- ✅ Strongest / weakest Jetix components per lens enumerated
- ✅ 5+ open questions / risks per lens surfaced (target ≥25 cumulative; achieved ~28)
- ✅ Cross-cite Левенчук applied per lens где applicable
- ✅ Cross-synthesis (§6): 5 themes + 5 gaps + recommended research areas
- ✅ How Experts Pack feeds 4 other docs (§7)
- ✅ Constitutional posture preserved (R1 + R6 + IP-1 STRICT + EP-5 + AP-6 + SKIP-list integrity)
- ✅ 20-25% take rate provisional only (DR-26 gates)
- ✅ Brigadier substrate ONLY — Ruslan R1 strategic prose authoring deferred to one-pager Phase 5 slots

---

*Experts Pack closure 2026-05-21. Phase 1 ⭐ deliverable. ~4500w. Per memory feedback_research_pool_pattern.md + feedback_constitutional.md + feedback_fpf_lens_first.md. Next: Phase 2 Questions Pack.*
