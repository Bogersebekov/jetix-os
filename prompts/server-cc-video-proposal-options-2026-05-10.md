---
title: Server CC Brigadier — Video Proposal Options для Цэрэн + Левенчук + ШСМ (comprehensive brainstorm)
type: brigadier-prompt
created: 2026-05-10
author: cloud-cowork (Ruslan ack)
target_executor: server-cc on existing window (action-plan window now free) или new window
mode: Ultrathink + comprehensive brainstorm
push_policy: draft commit на ветку, await Ruslan ack
F: F4
G: video-proposal-options-brainstorm
R: refuted_if_authoritative_recommendations_or_no_constitutional_check_or_premature_video_script
constitutional_anchor:
  - Tier 2 Rule 1 (AI = brainstorm + structure options; Ruslan = sole decider what to use)
  - Tier 2 Rule 6 (provenance per option — source memo/insight/canonical)
  - Append-only (existing canonical / action plan untouched)
  - Default-Deny (draft → ack → only then video script generation as separate task)
estimated_effort: 1.5-2.5 hours autonomous
---

# Video Proposal Options — Comprehensive Brainstorm

> **Контекст.** Action Plan acked (`decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` = baseline, не отходим).
> Ruslan focus: **immediate critical path A1.1 — видео Цэрэну** (после которого все decisions решаются).
>
> **Goal.** Single comprehensive document — **brainstorm всех возможных angles** для proposal Цэрэн + Анатолий Левенчук + ШСМ (мастерская инженеров-менеджеров). НЕ video script (это separate task). НЕ recommended single path. **Options paper** — все возможные:
> - что мы (Jetix / Ruslan) можем дать (comprehensive list)
> - что хотим получить (от них)
> - возможные форматы collaboration (5+ типов)
> - что хотим донести (key messages)
> - что хотим узнать (questions to ask)
> - anti-patterns (что НЕ говорить)
> - order of disclosure (что когда раскрыть)
> - materials to show
> - key tensions during call
>
> **Workflow.** CC накидывает comprehensive options. Ruslan reviews → picks paths → CC does separate video script generation.

---

## §1 Inputs to study (read context)

### A.1 Audience profile sources

- `crm/people/tseren-tserenov.md` (CRM record Цэрэна)
- `prompts/tseren-tg-analysis-2026-04-28.md` + `prompts/tseren-youtube-analysis-2026-04-28.md` (analysis)
- Notion pages про Цэрэн analysis — see `📅 2026-05-08 → 🎬 Tseren Video Recording 2026-05-08` subpage's references к outreach hub
- Voice memos с упоминанием Цэрэна / Левенчука (через voice-pipeline-2026-05-10 deliverables)
- Strategic Insight Partnership Model §6.1 «Цэрэн validates pattern»

### A.2 Action plan baseline (acked)

- `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` — Action Plan acked baseline
- Especially §2.2 Cluster 2 (Levenchuk-Tseren synergy critical path)
- §3 Strategic Insights applied
- §4.1 Tier 1 immediate actions

### A.3 Strategic Insights дня (what informs proposal)

- `decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md` (НЕ упоминать Цэрэну per §5; но informs internal positioning)
- `decisions/STRATEGIC-INSIGHT-JETIX-PARTNERSHIP-MODEL-2026-05-10.md` (Manifest pattern + RES.1-3 + §6.1 Цэрэн validates + §6.2 optional video line + §13 R&D Flywheel)

### A.4 Canonical foundation (что показывать as evidence)

- `decisions/JETIX-CORPORATION-2026-05-05.md` (Document 1B — applied use case, especially §3 TRM / §9 partnership variants A-E / §10 Roadmap)
- `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` (Document 1A — universal foundation)
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` (Workshop metaphor)
- `decisions/JETIX-TRM-MODEL-2026-04-30.md` (TRM 6 ресурсов + L0-L5 ladder)
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (constitutional anchor)
- `swarm/wiki/synthesis/diagrams-2026-05-07/workshop-deep/v4-system-boundary.md` (Workshop v4 diagram — visual evidence)
- `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` (Foundation overview)

### A.5 Top-20 voice items relevant к Цэрэн / Levenchuk

- `reports/voice-pipeline-2026-05-10/03-current-lens-actionables.md` items #6, #8, #12, #13, #14, #15, #16 (Levenchuk-Tseren cluster)
- audio_602 «фрейм партнёра, а не соискателя»
- audio_604 «совместное создание fundamental docs»
- audio_616 «видео-презентация Jetix с диаграммами»
- audio_633 «мировые рекорды»

### A.6 Existing Tseren outreach work (29.04 hub)

- Notion `🎯 29-04-2026 Outreach Tseren + Strategic Documents` ([3512496333bf81029b5ec89628fcdcc8](https://www.notion.so/3512496333bf81029b5ec89628fcdcc8))
- Frame LOCKED (открытый честный outreach)
- 10 Q&A LOCKED (Q1-Q10)
- 3 блока структуры видео (Hook / Main / CTA)
- Первое видео отправлено 04.05 (response unknown)

---

## §2 Document structure required

File: `decisions/VIDEO-PROPOSAL-OPTIONS-TSEREN-LEVENCHUK-2026-05-10.md`

### §2.1 Required sections

```markdown
---
title: Video Proposal Options — Цэрэн + Левенчук + ШСМ
date: 2026-05-10
type: proposal-options-brainstorm
status: draft (awaiting Ruslan picks)
audience: Цэрэн Цэрэнов / Анатолий Левенчук / ШСМ
parent_action_plan: decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md (acked baseline)
parent_strategic_insights:
  - decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md
  - decisions/STRATEGIC-INSIGHT-JETIX-PARTNERSHIP-MODEL-2026-05-10.md
parent_canonical:
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
F: F4
G: video-proposal-options
R: refuted_if_premature_authoritative_recommendation_or_video_script_generated
---

# Video Proposal Options — Цэрэн + Левенчук + ШСМ

## §0 Что это (purpose)
Brainstorm всех возможных angles для proposal. Options paper — Ruslan picks, не AI decides.

## §1 Audience profile (3 entities)

### §1.1 Цэрэн Цэрэнов
- Кто: креатор + system school + Anatoly Levenchuk's circle / protégé
- Channels: Telegram + YouTube (linktr.ee/tseren)
- Что value (на основе analysis): системное мышление, Левенчук методологии, ИТ-управление, профессионал-инженер
- Текущее состояние: previous video sent 04.05; response status (unknown — assume не открыт ещё или open)
- Personality signal (от voice + analysis): прогрессивный, открытый, высокая планка

### §1.2 Анатолий Левенчук
- Кто: системный мыслитель, ШСМ founder, "мастерская инженеров-менеджеров"
- Канон: системное мышление, инженерия знаний, методологии управления
- Что value: глубокая методологическая основа, теоретическая строгость
- Audience: thousands students / followers
- Personality signal: серьёзный, строгий, готов работать долго

### §1.3 ШСМ как organisation / community
- Что: сообщество инженеров-менеджеров вокруг Левенчука
- Что value: methodology + community + endorsement signal

## §2 Что мы можем им дать (comprehensive list)

5-15 things, each:
- Item description
- Source (canonical / insight / artefact)
- Который из 3 audience members это resonates (Цэрэн / Левенчук / ШСМ)
- Why valuable to them specifically

Examples (server CC должен expand):
- D1 Workshop substrate (architecture v4 diagram + 1A foundation)
- D2 12-agent AI infrastructure (Manager + agents)
- D3 Compound learning discipline (12 months trekking, 8158 hours)
- D4 Foundation v1.0 LOCKED — 11 Parts (governance, provenance, etc.)
- D5 Visualization tooling (Mermaid pipeline + canonical operations)
- D6 Voice pipeline (47 memos × 8 deliverables capability)
- D7 Document 1A/1B (universal base + applied use case)
- D8 TRM model (6 resources × L0-L5 ladder × 3 phases)
- D9 First-mover position в Founder-OS category (Foundation Model insight implicit, NOT communicated)
- D10 R&D Flywheel commitment (RES.2 90% reinvest)
- D11 ... (more)

## §3 Что хотим получить (от них)

5-15 things, each:
- Item description
- Source (voice / canonical / insight)
- От кого получаем (Цэрэн / Левенчук / ШСМ)
- Why valuable to us

Examples:
- R1 ШСМ methodologies integration в Jetix (Document 1B §10 Step 2)
- R2 Audience access (Tseren TG + YouTube; Левенчук student base)
- R3 Co-creation fundamental docs (audio_604)
- R4 Strategic guidance / mentorship
- R5 Network multiplier (intro к 7-8 strategic council кандидатов)
- R6 Endorsement signal (community mark of approval)
- R7 First instantiation Manifest-pattern partnership
- R8 Possible equity / financial backing
- R9 Joint product development
- R10 ... (more)

## §4 Возможные форматы collaboration (5+ типов)

For each format:
- Format name
- Who участвует (Tseren / Levenchuk / ШСМ / какие comb)
- Pros for Jetix / Pros for them
- Cons / risks
- Document 1B §9 partnership tier mapping (Founding / Strategic / Operating Partner)
- Suggested terms (financial / equity / time / etc.)
- Proposed first step

Tiers:
- F1 Strategic Partner (Founding Partner per Document 1B §9.1) — full equity-leaning long-term
- F2 Operating Partner — joint product development
- F3 Mentor / Advisor — lighter touch, periodic guidance
- F4 Co-creation на specific project (e.g. Workshop integration)
- F5 Investment partnership — financial backing
- F6 Endorsement / community partnership — distribution support
- F7 Affiliate-style revenue share
- F8 Combined — multiple tiers parallel
- + sub-variants per relationship

## §5 Что хотим донести (key messages)

5-10 messages, each:
- Message statement (1-2 sentences)
- Source (insight / canonical)
- Why this audience needs to hear it
- Strength of evidence (artefact to show)

Examples:
- M1 «Сегодня уже есть substrate, не идея в голове» — show 1A/1B/Foundation v1.0/Workshop diagram
- M2 «Мы партнёрим, не продаём» (Manifest pattern)
- M3 «Reinvest 90% в R&D — long-term play, не short-term cash»
- M4 «Synergy unlock = critical path для $100K к концу лета»
- M5 «Ruslan = серьёзный operator (12 months disciplined tracking)»
- M6 «Готовы serious commitments сразу»
- M7 ... (more)

## §6 Что хотим узнать (questions to ask)

5-10 questions, each:
- Question
- Why ask (what hypothesis we test)
- Expected answer ranges + interpretation

Examples:
- Q1 «Какой главный resource gap в их системе сейчас?»
- Q2 «Что они уже пробовали для scaling и почему не зашло?»
- Q3 «Какая скорость движения комфортна?»
- Q4 «Кто в их network может быть relevant для Strategic Council?»
- Q5 «Готовы ли они к long-term partnership (vs short engagement)?»
- Q6 ... (more)

## §7 Anti-patterns — что НЕ говорить

Explicit list of 5-10 things to AVOID:
- AP1 НЕ упоминать Foundation Model insight (per Insight §5)
- AP2 НЕ транслировать desperation (per voice item «фрейм партнёра, не соискателя»)
- AP3 НЕ predetermined offer (gives them choice)
- AP4 НЕ продавать «ещё один tool»
- AP5 НЕ наивный pitch без foundation evidence
- AP6 НЕ упоминать Mittelstand DACH (RES.1 abandoned)
- AP7 НЕ извиняться за scale ambition ($1T trajectory baseline preserved)
- AP8 ... (more)

## §8 Order of disclosure (что когда раскрыть)

Stage-gated revelation across multiple touch points:

### Stage 1: First video (this recording)
- What to reveal: hook + основное предложение + show Workshop v4 diagram + ask for first call
- What NOT to reveal: detailed financial terms, R&D 90% specifics, $1T trajectory

### Stage 2: First call
- What to reveal: Document 1B excerpts, TRM model, partnership variants menu
- What NOT to reveal: Strategic Council shortlist names, internal Strategic Insights drafts

### Stage 3: 2-я call / письмо
- What to reveal: chosen partnership tier proposal, financial terms, equity structure
- What NOT to reveal: anti-patterns / weak signals

### Stage 4: After first commitment
- What to reveal: full canonical access, joint planning, governance model
- What NOT to reveal: yet untested hypotheses (deferred Phase 2+)

### Stage 5: Phase 1→2 transition
- What to reveal: full strategic insights, R&D allocation matrix, future direction backlog

## §9 Materials to show / share

For each material:
- Material item
- Format (link / screen share / verbal description)
- When (Stage 1-5)
- Source (path в repo)

Examples:
- MAT1 Workshop v4 diagram — screen share Stage 1
- MAT2 Document 1B excerpts (§3 TRM, §9 Partnership) — link Stage 2
- MAT3 Foundation Workshop overview — link Stage 2
- MAT4 12-month retrospective — share Stage 2 if relevant
- MAT5 Action Plan tiers (without internal decisions) — share Stage 3
- MAT6 ... (more)

## §10 Key tensions / decisions during call

Specific scenarios + suggested moves:

### T1 — Если они скептичны
- Sub-tactic: ask их critique vs defend; let it inform Phase 1 decisions

### T2 — Если они нет времени
- Sub-tactic: fallback simpler offer (F3 Mentor lighter touch; or Stage 1 only — observe response)

### T3 — Если они want $$ commitments upfront
- Sub-tactic: navigate RES.2 90% reinvest; offer equity-leaning vs cash terms

### T4 — Если они хотят ducked / non-committal
- Sub-tactic: do NOT push; observe → re-engage in 30-60 days

### T5 — Если они подключают других людей
- Sub-tactic: welcome (Strategic Council expansion vector); ask кто these people

### T6 — ... (more)

## §11 Mermaid diagram — collaboration possibilities flow

Visualize:
- Center: Цэрэн / Левенчук / ШСМ
- Forks: 5+ collaboration formats (F1-F5+)
- Each fork → outcomes / dependencies
- Variant A cool blues palette per `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md`

## §12 Cross-references

- Action Plan: which actions реализуются через which option
- Strategic Insights: which insight informs which message / format
- Canonical: which doc supports which message / option
- Voice items: provenance per option (memo:line)

## §13 Open questions для Ruslan ack перед video recording

5-10 questions, each:
- Question for Ruslan
- Default if not explicitly answered
- Why this matters

Examples:
- Q.A1 Который из F1-F8 collaboration formats — default proposal в video?
- Q.A2 Tseren ⊃ Levenchuk approach (через Tseren) или separate parallel approach?
- Q.A3 Pricing reveal — at Stage 1 or Stage 2?
- Q.A4 Show full Workshop diagram or only top-3 elements?
- Q.A5 Length target — 5 min / 7 min / 10 min?
- Q.A6 ... (more)

## §14 What this document does NOT do

- ❌ NOT video script (separate task after Ruslan picks options)
- ❌ NOT authoritative recommendation
- ❌ NOT canonical update
- ❌ NOT communication channel selection (TG / email / etc.)
- ❌ NOT Phase 2 planning

## §15 Related artefacts

- Action Plan (acked) — `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md`
- Strategic Insights дня (2)
- Canonical (5 docs)
- Voice pipeline 8 deliverables
- Notion `🎬 Tseren Video Recording 2026-05-08` subpage (existing structure 3 blocks)
- Notion `🎯 29-04-2026 Outreach Tseren hub` (frame + 10 Q&A locked)
```

### §2.2 Quality criteria

- Each option / item must have provenance (source path / voice memo / insight ref)
- Each Stage 1-5 disclosure has explicit «include» / «exclude» list (no ambiguity)
- Mermaid diagram included с Variant A palette
- Document size target: 800-1500 lines (cap 2000)
- No authoritative recommendations — pure options
- Constitutional posture explicit (§14)

---

## §3 PHASE B — Push draft + signal (5 min)

```bash
git add decisions/VIDEO-PROPOSAL-OPTIONS-TSEREN-LEVENCHUK-2026-05-10.md
git commit -m "[video-proposal] Comprehensive options brainstorm для Цэрэн + Левенчук + ШСМ — что давать / получать / форматы / messages / questions / anti-patterns / disclosure stages (draft awaiting Ruslan picks)"
git push origin HEAD
```

**НЕ push to main.** **НЕ tag.** Wait Ruslan ack.

---

## §4 What NOT to do

- ❌ НЕ writes video script (separate task after Ruslan picks)
- ❌ НЕ recommends single path / authoritative
- ❌ НЕ touches canonical / wiki / action plan / strategic insights
- ❌ НЕ updates Document 1B §9 partnership variants
- ❌ НЕ commits to channel (TG / email / etc.)
- ❌ НЕ push to main, НЕ tag

---

## §5 Constitutional cross-check

| Rule | Application | Compliance |
|---|---|---|
| Tier 2 R1 | Brainstorm options. Ruslan picks. | ✅ |
| Tier 2 R2 | Draft only. Existing untouched. | ✅ |
| Tier 2 R6 | Provenance per option. | ✅ |
| Append-only | New doc only. | ✅ |
| Default-Deny | Draft → ack → only then video script. | ✅ |

---

## §6 Time / size budget

- Read context: 20-30 min
- Brainstorm + structure: 45-90 min
- Document writing: 30-60 min (incl. Mermaid)
- Push: 5 min

**Total: 1.5-2.5 hours autonomous.**

Target output: 800-1500 lines.

---

## §7 Final signal к Ruslan

After push:
- Branch + commit SHA
- Doc path
- Sections completed (15 sections)
- Options counts:
  - D# (что давать) count
  - R# (что получать) count
  - F# (collaboration formats) count
  - M# (key messages) count
  - Q# (questions) count
  - AP# (anti-patterns) count
  - MAT# (materials) count
  - T# (tensions) count
- Stage 1-5 disclosure breakdown
- Mermaid included? yes/no
- Open questions count для Ruslan
- Constitutional posture verified

---

**Brigadier signature.** Acting_as `proposal-options-brainstorm-orchestration-role`. Comprehensive list mode. Ruslan = sole picker. NEXT phase (after picks) = video script generation as separate task.
