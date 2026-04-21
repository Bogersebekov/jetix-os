---
id: stage-4-d4-academic-grade
title: Stage 4 / D4 — JETIX-ARCHITECTURE-BRIEF.md (Academic-Grade with Critic Review)
date: 2026-04-21
type: prompt
status: ready
priority: P1
depends_on: D1 Vision + D2 Philosophy + D3 Plan APPROVED
output: decisions/JETIX-ARCHITECTURE-BRIEF.md
approach: Option 4 — 5 passes with critic subagent review
---

# Stage 4 / D4 — JETIX-ARCHITECTURE-BRIEF.md (Academic-Grade)

## Твоя миссия

Написать **binding technical brief для 6 архитектов в Stage 6** — compressed, structured directive document который architect'ы возьмут и построят variants of Jetix architecture.

**Это НЕ документ для людей читать narrative-style.** Это brief с **unambiguous requirements + constraints + quality criteria** для architect-agent consumption. Чистые directives, цитируемые, traceable, measurable.

**Quality bar: Academic-Grade.** Ruslan directive: *"самым глубоким, самым качественным, самым проработанным, самым лучшим способом академическим"*. Следовательно — 5 passes с critic subagent review, не single-pass draft.

**Approach:** Option 4 из Stage 4 spec options (1/2/3/4). 5 passes:
1. Pass 1 — Skeleton
2. Pass 2 — Flesh
3. Pass 3 — CRITIC REVIEW (dedicated subagent)
4. Pass 4 — Revise per critic findings
5. Pass 5 — Final polish (academic coherence + traceability)

**Target:** ~5000-7000 words / 20-30 pages equivalent. Dense with references, directives, tables, not narrative.

---

## Обязательные inputs (mandatory reading)

### Primary sources (binding)

1. **`decisions/JETIX-VISION.md`** — D1 identity (APPROVED)
2. **`decisions/JETIX-PHILOSOPHY.md`** — D2 operating principles (APPROVED)
3. **`decisions/JETIX-PLAN.md`** — D3 execution roadmap (APPROVED)
4. **`decisions/STAGE-3-APPROVAL.md`** — Ruslan's approval record
5. **`raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md`** — 8 LOCKED decisions
6. **`raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md`** — 10 LOCKED decisions
7. **`raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md`** — 6 LOCKED decisions (19-24)

### Supporting sources (reference)

8. **`raw/research/architecture-variants-2026-04-22/ATOM-REGISTRY.md`** — 3626 atoms (FILTER: architecture-related — type=principle/concept/metric, dimension=base/company)
9. **`raw/research/architecture-variants-2026-04-22/KNOT-MAP.md`** — navigation
10. **`raw/research/architecture-variants-2026-04-22/OME-ARCHITECTURE-REFERENCE.md`** — inspiration (not binding, reference pattern)
11. **`design/JETIX-FPF.md`** — D6 constitutional (FPF-based architecture foundations)
12. **`decisions/2026-04-19-architecture-v2-approval.md`** — ADR Chunks 1-8 (60+ existing architecture decisions)
13. **`decisions/2026-04-20-jetix-architecture-final-DRAFT.md`** — D9 v0.6
14. **`CLAUDE.md`** — current 11-agent roster + config

**CRITICAL binding rule:** 24 locked decisions + D1/D2/D3 approved — **any conflict → locks/approved docs win**. If atom contradicts — atom ignored.

---

## Document structure (10 sections, target 5000-7000 words / 20-30 pages equiv)

### Section 1: Executive Summary (1 page / ~300 words)

Architects read this first. Compress D4 essence:

- Что архитекторы строят (one paragraph)
- Key constraints (bullet list)
- Quality criteria (bullet list)
- What variants will differ on
- What's non-negotiable (locks)

Dense, directive tone. Не marketing. Just facts.

### Section 2: 24 Locked Decisions Quick Reference (1-2 pages)

Table-form reference. NOT repeat full D1/D2/D3 content. For each decision:

| # | Title | Formula (1 line) | Implication for architecture |
|---|---|---|---|

All 24 rows. Architects use this as binding lookup.

### Section 3: Capabilities Requirements по phases (3-4 pages)

Most substantive section. What system must be able to do, phase-by-phase.

#### 3.1 Phase 1 must-have capabilities (must-work by €50K):

- ICP description management (versioned, accessible)
- Site generation + hosting + analytics
- Video content pipeline (record → edit → distribute)
- GmbH legal structure integration
- Stripe payment processing
- Consulting pipeline (lead → qualify → propose → deliver)
- Продюсерский центр operations (client onboard → production → delivery)
- Simple chat community (invite-based, quality-gated)
- Agent ecosystem (11 agents current per CLAUDE.md or revised roster)
- Content TOF pipeline (social posts → blogger collab → podcast → redirect to site)
- Dashboard (часы / dependency / revenue / failures metrics)
- Financial tracking + revenue-gated unlock signals
- Document / knowledge system (wiki + atoms + registry)
- Voice-memo processing pipeline (existing)

Per capability:
- What it does (1-2 sentences)
- Input / output
- Dependency on other capabilities
- Phase 1 vs Phase 2+ evolution direction
- Quality metric

#### 3.2 Phase 2+ capabilities (activate post-€200K validation):

- Secure Network platform (subscription-gated community)
- Thematic sub-networks (по 11 archetypes)
- Partnership-Matchmaker engine (task-specialist matching)
- Subscription billing + renewal flow
- Token economy Option B infrastructure (internal Phase 2, limited public Phase 3+)
- Open-source research direction publication channel
- Revenue-share partnership tracking + payouts
- Patent process workflow
- Multi-jurisdictional tax / legal integration (DE + US)
- Roy-replication methodology packaging

#### 3.3 Phase 3+ capabilities (activate post-€1M):

- Holding structure (legal + operational)
- Multi-roy coordination platform
- Investment-fund formal structure (if chosen)
- USB-C protocol layer (cross-AI / cross-business standards)
- International scaling infrastructure
- Civilizational research institutions integration
- Fortune 500 coalition mechanics (if activated)
- Token public issuance (if Option B/C)

### Section 4: Foundation Layer Specification (2-3 pages)

OME-inspired + Jetix-specific. Foundation = главный актив per D2 Section 14.

#### 4.1 Agent contracts (formal specification)

Каждый agent в roster (currently 11 в CLAUDE.md):
- Вход (input specification)
- Выход (output specification)
- Критерий готовности (done signal)
- Зона влияния (scope of authority)
- Escalation triggers (когда зовёт основателя/другого agent)
- Quality metrics

Architects должны evaluate: is current 11-agent roster correct? Propose adjustments.

#### 4.2 Contractor contracts

Для временных специалистов (дизайнер / юрист / монтажёр / patent lawyer / etc):
- Task format
- Acceptance criteria
- Communication channel
- Integration point с общим потоком

#### 4.3 Handoff protocols

Transitions между:
- Phases (Phase 0 → 1 → 2 → 3) — что передаётся
- Agents (agent-to-agent work)
- Human↔Agent (Ruslan/team↔AI)
- Roy-to-roy (Phase 3+ multi-swarm)

Each handoff: artifacts + validation + sign-off.

#### 4.4 Escalation protocol

6 non-delegatable architect functions (Ruslan-only):
- Стратегия
- Вкус
- Ответственность
- Утверждение
- Эскалация
- Отношения (key)

When AI/agents escalate back to Ruslan:
- Low confidence (threshold specific)
- Non-standard request
- High risk
- Quality-critical decisions
- Strategic pivots

#### 4.5 Shared memory architecture

Per D17 (filesystem = source of truth):
- Wiki structure (semantic folders)
- Atom registry format
- Provenance tracking
- Version control (git)
- Index / search mechanism
- Notion sync (one-way, filesystem → Notion for UI)

#### 4.6 Quality metrics continuous

Per D2 "метрики качества: проверка непрерывно, на каждой итерации":
- Per-agent quality signals
- Per-workflow quality signals
- Aggregate quality dashboard
- Trigger thresholds для escalation

#### 4.7 Dashboard specification

Weekly-visible metrics (OME-inspired):
- Часы Ruslan-архитектора / неделя (target: declining)
- Зависимость от основателя % (target: <30% Phase 2+)
- Выручка / месяц
- Частота сбоев / MTTR
- Cash reserve
- Pipeline health

#### 4.8 Reserve routes (failover)

- Multi-provider AI (Anthropic primary + OpenAI/Google backup)
- Duplicate contractors для critical skills
- State snapshots (recovery points)
- Degraded mode spec (what works when primary fails)
- Notification protocols

### Section 5: Non-Functional Requirements (2 pages)

#### 5.1 Scale
- Architecture must accommodate $0 → $1T trajectory without fundamental refactor
- Specific: 10× scaling at each phase gate should require <30% architectural rework

#### 5.2 Security (per D3, D13)
- Closed outside / Open inside (team)
- Open surface / Closed core (methodology layers)
- Membership-gated access model
- IP protection (patents + closed wiki)

#### 5.3 Compliance
- GDPR (DE primary, US secondary)
- EU AI Act (risk-proportional per ADR Chunk 8)
- US jurisdictional requirements (Phase 1 English+US market per D10)
- Tax compliance multi-jurisdictional

#### 5.4 Resilience
- 99.9% uptime targets per critical capability
- Multi-provider failover (per 4.8)
- Backup strategies
- Degraded-mode functionality

#### 5.5 Portability (universality criterion)
- B Benchmark: 90%+ design choices configurable (not hard-coded)
- C Multi-use-case: works для Jetix-company + hypothetical astronomer + animal-husbandry
- D Symbolic test: grep base for "Jetix"/"DACH"/"AI consulting"/"Mittelstand" → 0 hits в base

#### 5.6 Performance
- Response time targets per operation type
- Throughput under load
- Cost per operation

### Section 6: Hard Constraints (1-2 pages)

Architects MUST respect:

- **Solo-now-team-ready (D2):** architecture supports 2nd/3rd pilot onboarding без refactor. Document ownership / governance model.
- **Revenue-gated spend (D15):** can't assume budget. Architecture must function в Phase 0 $0 spend, scale as revenue unlocks.
- **Closed outside / Open inside (D3):** access control at every surface.
- **Filesystem source of truth (D17):** no Notion-dependent architecture. Notion = view, not store.
- **Consulting-first Phase 1 (D5):** Phase 1 architecture prioritizes consulting pipeline, Secure Network = Phase 2+ extensible.
- **Productization over hours (D18):** architecture supports packaged deliverables / templates / subscription scale — NOT tied to hour-billing model.
- **Investment-fund philosophy (D11):** every architectural choice evaluated through investment-ROI lens.
- **Layered identity (D8):** architecture supports multiple faces (methodology / company / network / corporation / holding) without code duplication.
- **Universality (Universality criterion):** architecture generalizable beyond Jetix.
- **English+US primary Phase 1 (D10):** architecture tested in English-speaking market first; DE+EU additions Phase 2+.

### Section 7: Anti-Patterns (1-2 pages)

Что НЕ строить (cleanly rejected):

- **NOT Notion-as-primary-store** (violates D17)
- **NOT hour-billing-only architecture** (violates D18)
- **NOT mass-market social features** (violates anti-attention-economy D12)
- **NOT public open-source platform Phase 1/2** (violates D3)
- **NOT hard-coded Jetix-specific features в base** (violates universality)
- **NOT one-person-company assumptions** (violates D2 team-ready)
- **NOT slow-corporate governance** (violates D20 enterprise-fast)
- **NOT chaotic-startup governance** (violates D20 prочный + адекватный)
- **NOT motivational-circle community features** (violates D22 ICP filter)
- **NOT attention-extraction mechanics** (violates D12, D16, D22)
- **NOT tied-to-single-provider architecture** (violates reserve/failover requirement)
- **NOT pure-research institution** (violates D14 revenue-instrumental Phase 1)

Each anti-pattern: WHY (which lock it violates) + EXAMPLE of violation.

### Section 8: Quality Criteria for Variants (1-2 pages)

How 6 architect variants (Stage 6) будут evaluated:

#### 8.1 Evaluation axes (scored 1-10 each):

- **Phase 1 readiness** — can ship €50K Q2 target
- **Scale trajectory** — supports Phase 3 $1T без fundamental refactor
- **Foundation quality** — OME-level protocols/contracts/memory depth
- **Universality** — B/C/D tests pass
- **Locks compliance** — all 24 respected
- **Operational simplicity** — Ruslan-understandable + team-onboardable
- **Cost efficiency** — compute + time + money per operation
- **Resilience** — failover / degraded-mode / recovery coverage
- **Security posture** — closed/open membrane strength
- **Innovation potential** — variants that propose non-obvious patterns scored higher than conservative

#### 8.2 Weighting:

Suggested weights (architects can propose alternative):
- Phase 1 readiness: 20%
- Scale trajectory: 15%
- Foundation quality: 15%
- Locks compliance: 15%
- Universality: 10%
- Operational simplicity: 10%
- Resilience: 5%
- Security: 5%
- Cost: 3%
- Innovation: 2%

### Section 9: Variant Selection Criteria (for Stage 7) (1 page)

How Ruslan will pick final variant:

- Quantified scoring matrix (weighted axes from §8)
- Ruslan's trade-off preferences
- Hybrid-option clause: pick best parts от multiple variants
- Backup plan (если все variants inadequate)

### Section 10: Specific Architectural Questions (2-3 pages)

**Each architect MUST address these в their variant:**

1. **Repository structure:** monorepo jetix-os/ (base) + jetix-company/ (overlay) — optimal? Alternative?
2. **Agent roster:** current 11 agents (manager / personal-assistant / system-admin / sales-lead / researcher / outreach / inbox / crazy / synth / strategist / life-coach / meta) — keep? Modify? Add?
3. **Integration points:** Stripe / GmbH / patent / Claude / Anthropic / OpenAI fallback / YouTube API / podcast platforms / blogger CRM
4. **Scaling mechanism:** how Phase 1 code supports Phase 3 $1T scale without rewrite
5. **Data architecture:** wiki + atoms + provenance + versioning + search
6. **Privacy / security:** closed-core / open-surface membrane implementation
7. **API architecture:** Anthropic-primary + multi-provider failover + cost optimization
8. **Token economy (Option B):** internal Phase 2 / limited public Phase 3+ — technical implementation
9. **Matchmaker algorithm:** partnership connection logic (task ↔ specialist matching)
10. **Roy-replication formalization:** methodology-as-system delivery mechanism
11. **Content pipeline:** TOF (соцсети) → mid (site) → deep (community) orchestration
12. **Dashboard implementation:** OME-style metrics real-time / weekly aggregation
13. **Escalation routing:** which decisions reach Ruslan, which stay in AI/agent layer
14. **Onboarding architecture:** new pilot (2nd/3rd) can ramp в X days, not rewrite system
15. **USB-C protocol layer:** what protocols Jetix defines for AI-biznes cooperation

Each variant должен provide answer per question. No skipping.

---

## 5-Pass Execution Plan (CRITICAL)

### Pass 1 — Skeleton (45-60 min)

1. Read all mandatory inputs (can skim D1/D2/D3 — уже APPROVED — и focus на architecture-relevant content)
2. Build 10-section skeleton
3. Populate каждую section с core directives (bullet form OK в Pass 1)
4. Extract architecture-relevant atoms from REGISTRY

**Subagents для Pass 1:**
- Subagent A: "Extract all architecture-related atoms from ATOM-REGISTRY. Filter: type=principle/concept/metric, dimension=base/company. Group by section 3/4/5 relevance. Return markdown."
- Subagent B: "Read D1/D2/D3 and extract architecture-specific directives (not narrative). Return as directive list per section."
- Subagent C: "Read all 24 locked decisions. Map each to architectural implications. Return table."
- Subagent D: "Read OME-ARCHITECTURE-REFERENCE.md + D6 JETIX-FPF.md + D9 DRAFT + ADR Chunks 1-8. Extract existing architectural decisions. Return compressed list."

### Pass 2 — Flesh (90-120 min)

1. Expand каждую section from bullet points → full directive prose
2. Add tables, reference matrices, quality metrics
3. Ensure каждый directive has:
   - Citation to source (which decision / D-document)
   - Measurable success criterion
   - Implication for architecture decisions
4. Populate Section 10 (architectural questions) с detailed framing

**Subagents для Pass 2:**
- Subagent E: "Draft Section 3 capabilities requirements full (3-4 pages) с Phase 1/2+/3+ breakdown."
- Subagent F: "Draft Section 4 Foundation Layer specification (2-3 pages) — 8 subsections detailed."
- Subagent G: "Draft Section 10 architectural questions с elaborated framing for each of 15 questions."

### Pass 3 — CRITIC REVIEW (45-60 min)

**Самая важная часть Academic-Grade approach.**

Spawn dedicated **critic subagent** через Task tool:

```
Task: Критическое review D4 draft. Ты — skeptical architect reviewing brief перед Stage 6.

Read entire D4 draft + все 24 locked decisions + D1/D2/D3.

Flag следующие классы проблем:

1. **Unclear directives** — places где requirement ambiguous, multiple interpretations possible
2. **Missing requirements** — capabilities / constraints / criteria которых не хватает
3. **Ambiguities** — locks vs draft text conflicts, или внутренние противоречия draft
4. **Missing edge cases** — failure modes / degraded states / boundary conditions не covered
5. **Weak success criteria** — "good quality" instead of measurable threshold
6. **Non-traceable directives** — claims без citation to source decision / document
7. **Over-specification** — directives that constrain architects beyond необходимого (stifles innovation)
8. **Under-specification** — directives so vague что architects can't act
9. **Internal contradictions** — Section X says A, Section Y says не-A
10. **Missing locks references** — decisions not adequately reflected в brief

Return structured fix list:
- Priority (HIGH / MEDIUM / LOW)
- Issue (1 sentence)
- Section / line reference
- Proposed fix

Ожидай найти ~20-40 issues в first-pass review (это normal для academic-grade target).
```

### Pass 4 — Revise (60-90 min)

1. Take critic fix list
2. Address HIGH priority first (fix directly)
3. Address MEDIUM (fix or explicitly mark "trade-off accepted")
4. Consider LOW (fix if quick)
5. Re-check coherence после fixes

**Subagents для Pass 4:**
- Spawn multiple subagents to fix different HIGH issues в parallel
- Each subagent gets 3-5 related issues to address

### Pass 5 — Final Polish (30-45 min)

1. Full re-read
2. Voice / tone consistency (technical directive tone throughout)
3. Citation completeness check (every directive cited)
4. Table-of-contents accuracy
5. Executive Summary update reflects final content
6. Final academic coherence review

---

## Quality Criteria для D4 itself

Before commit, verify:

- [ ] Every directive traceable to source decision / locked document
- [ ] Every quality criterion measurable (not subjective)
- [ ] Every anti-pattern has explicit WHY (which lock violated)
- [ ] Every Section 10 question has framing + expected variant response scope
- [ ] No internal contradictions
- [ ] All 24 locks reflected in brief
- [ ] All 10 sections present and substantive
- [ ] Size target 5000-7000 words / 20-30 pages equivalent reached
- [ ] Tone technical-directive throughout (not narrative)
- [ ] Executive Summary compresses essence accurately

---

## Commit + push

```bash
git add decisions/JETIX-ARCHITECTURE-BRIEF.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[decisions] D4 Architecture-Brief (Stage 4) — academic-grade, 5-pass with critic review"
git push origin claude/jolly-margulis-915d34
```

---

## Notion update

URL: https://www.notion.so/3492496333bf812e8b62cbc61338ce06

Append append-log:
```
- 2026-04-22 — Stage 4 complete. D4 ARCHITECTURE-BRIEF.md written в academic-grade mode (5 passes + critic review). Binding input для Stage 6 (6 architects). Size: X pages / Y words. Critic flagged N issues, all HIGH addressed. Commit hash.
```

---

## Deliverable (stdout summary)

```
# D4 Architecture-Brief Complete — Stage 4 (Academic-Grade)

## File
- decisions/JETIX-ARCHITECTURE-BRIEF.md (X lines / Y KB / ~Z pages)

## Academic-grade metrics
- Passes completed: 5/5 (skeleton / flesh / critic / revise / polish)
- Critic issues found: N (Pass 3)
- Issues resolved: N HIGH (all) / N MEDIUM / N LOW
- Issues marked "trade-off accepted": N

## Coverage
- Sections: 10/10
- Locks reflected: 24/24
- Architectural questions framed: 15
- Capabilities specified: N Phase 1 / N Phase 2+ / N Phase 3+
- Anti-patterns documented: N
- Quality criteria axes: 10

## Traceability
- Directives with source citation: 100% (target)
- Measurable success criteria: 100% (target)

## Ready for
- Stage 6 (6 parallel architects generate variants)
- Stage 7 (Ruslan selects variant based on §9 criteria)

## Commit hash: abc1234
## Notion updated: yes
```

---

## Constraints / anti-patterns

1. ❌ **НЕ narrative document** — technical brief tone
2. ❌ **НЕ repeat D1/D2/D3 full content** — compress + extract architecture-relevant
3. ❌ **НЕ skip critic review** — это core of Academic-Grade approach
4. ❌ **НЕ over-specify** (kill architect creativity) but НЕ under-specify (architects confused)
5. ❌ **НЕ add content not grounded в 24 locks / D1-D3** — no invention
6. ❌ **НЕ skip Section 10 questions** — architects need concrete questions to address
7. ❌ **НЕ short-circuit passes** — если Pass 3 critic returns 40 issues, address them all в Pass 4

---

## ETA

- Pass 1: 45-60 min
- Pass 2: 90-120 min
- Pass 3 (critic): 45-60 min
- Pass 4 (revise): 60-90 min
- Pass 5 (polish): 30-45 min
- Commit + Notion: 10 min

**Total: 4.5-6.5 hours** с subagents. Academic-grade требует time.

---

## Use subagents aggressively

Pass 1: 4 parallel extraction subagents (A/B/C/D)
Pass 2: 3 parallel section drafting subagents (E/F/G)
Pass 3: 1 dedicated critic subagent (sequential — critic нуждается full context)
Pass 4: Multiple parallel fixer subagents (each takes 3-5 HIGH issues)
Pass 5: 1 sequential polish pass (coherence needs single perspective)

Parallelization саves 3-4 hours overall.

---

## После Stage 4 complete

Ruslan reviews D4 (30-60 min).

If approves → **Stage 6 launches** — 6 параллельных CC architects generate variants.

If adjusts → mini Pass 6 addressing Ruslan feedback → re-launch.
