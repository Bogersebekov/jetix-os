# Dmitry Humanities Letter + Video Outline — CC Autonomous Assembly Prompt

> **Создано:** 2026-05-11 evening.
> **Назначение:** CC автономно собирает draft letter + video outline для Дмитрия (host YouTube «Гуманитарщина»).
> **Notion parent:** `35c2496333bf81c3b329f1d5ce54c3a9` (для context) + new subpage `35d24963-...` (Dmitry plan).
> **Output:** 2 файла в `outreach/`.

---

## Команды запуска

```bash
# В Claude Code:
# (paste prompt ниже)
```

---

===PROMPT===

Задача: автономно собрать **draft letter Дмитрию** (host YouTube «Гуманитарщина») + **video outline** на основе existing canonical docs + Anton report.

## Sources (mandatory read first)

1. `reports/anton-call-report-2026-05-11.md` — recent narrative 2 months
2. `decisions/JETIX-CORPORATION-2026-05-05.md` — Document 1B (Jetix как корпорация)
3. `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` — Workshop концепция
4. `decisions/JETIX-TRM-MODEL-2026-04-30.md` — TRM 6 ресурсов × L0-L5
5. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` — Vision
6. All 6 `decisions/STRATEGIC-INSIGHT-*-2026-05-1*.md` — Hexagon insights
7. `wiki/concepts/jetix-realm/` — 6 Realm stubs (E1-E6)
8. `reports/gamification-mining-analysis-2026-05-11.md` — Шаг C key findings
9. `reports/gamification-question-mining-run-2026-05-11.md` — Шаг D variants
10. `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md` — visual canon

## Шаг 1 — Draft Letter

Output: `outreach/dmitry-humanities-letter-2026-05-11.md`

### Структура (per Notion plan §2)

**§1 Intro (1 параграф)**
- Кто Ruslan: founder Jetix OS, Берлин, AI + management intersection
- Зачем письмо: обсудить Jetix концепцию с humanities lens, потенциально podcast/discussion

**§2 Путь за 2 месяца (compressed narrative, ~200 слов)**
- Где был: Life OS v0 + видение жизни (~март 2026)
- Что построил: Foundation v1.0 LOCKED (28.04), 6 Hexagon insights, Wiki 722 entries, AutoResearch MVP, Jetix Realm 6-entity design
- Reference Anton report path для deeper detail

**§3 Jetix Corporation концепция (core sell, ~400 слов)**
- Workshop метафора: мастерская с adaptive станками (5 owner roles, info I/O)
- TRM model: 6 ресурсов × L0-L5 лестница (Capital / Time-leverage / Audience / Knowledge / Compute / Network)
- Document 1B: 8 faces, Партнёр/Клиент/Работник tiers
- Realm gamification: 6 entities (Persona TRM stats / Class / Clan 3-10 / Quest / Resources / Seasons 3-month) как MMO operational layer над substrate

**§4 6 Hexagon Strategic Insights (LOCKED, ~200 слов)**
- Foundation Model — WHAT
- Partnership Model — HOW grow (Manifest-style)
- R&D Flywheel — HOW compound (90% reinvest)
- Network State (Balaji) — WHERE fits
- Tyson Pattern — HOW founder masters
- Gamified Platform — WHY users engage

**§5 «Мировой порядок» angle (для humanities discussion, ~250 слов)**
- AI эпоха: info-workers становятся создателями корпораций
- Новые social structures: clan / federation / progressive networks vs legacy hierarchies
- Methodology как moat в эпоху equal-access AI
- Anti-extraction principle (Varoufakis technofeudalism critique counterpoint)
- Network State evolution (Balaji — как изменит nation-state model)
- Tyson-mentorship как counter к «scale fast, learn nothing»

**§6 Где сейчас — Точка А (~100 слов)**
- Foundation v1.0 LOCKED
- 722 wiki entries / ~880 edges (после bulk-ack)
- 6 Realm stubs готовы к elaboration
- Active outreach: Цэрэн (МИМ) + Левенчук (ШСМ) + Антон (mentor)
- Первые 10 человек клана — в формировании

**§7 Ключевые вопросы Дмитрию (5 блоков compressed)**
- Block 1: Philosophy of work in AI era
- Block 2: Network State critique (humanities lens)
- Block 3: Anti-extraction principle deep-dive
- Block 4: Gamification of life/work cultural critique
- Block 5: Concrete ask — podcast/discussion/collaboration

**§8 Outro + ask (~50 слов)**
- Готов к podcast / videozvonku
- Открыт к feedback / critique от humanities-lens
- 2 short CTA options (low-barrier: «прочитай — что думаешь?» + higher: «давай созвонимся 30 min»)

### Embed mermaid (4 diagrams)

1. Workshop concept (5 owner roles + info I/O)
2. Hexagon 6 insights map
3. Jetix Realm 6 entities → Workshop/TRM/Doc 1B edges
4. Timeline 2 месяца gantt (briefly — Anton report has detailed)

Palette: cool blues Variant A per `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md`.

### Tone

- Respectful, intellectual, NOT salesy
- Russian primary (Dmitry's audience is Russian-speaking)
- No corporate buzzwords
- Direct, без воды (per Ruslan style preference)
- Humanities-friendly: cite philosophy / culture references where relevant (Varoufakis Technofeudalism / Balaji Network State / Castronova Synthetic Worlds)
- 800-1500 слов total

### Frontmatter

```yaml
---
title: Letter to Dmitry (Гуманитарщина YT host) — Jetix concept + humanities discussion
date: 2026-05-11
type: outreach-letter-draft
status: DRAFT — awaits Ruslan personalization + send
target: Дмитрий, host «Гуманитарщина» YouTube channel
authored_by: ai-scribe (assembly only; Ruslan finalizes voice)
prose_authored_by: hybrid-with-ack-trail (AI structure + Ruslan personal voice in revision)
F: F2
G: outreach-letter-applied-now
R: refuted_if_Ruslan_rejects_structure_OR_no_response_30days
parent_notion: 35d24963-... (Dmitry plan subpage)
sources_used:
  - reports/anton-call-report-2026-05-11.md
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md
  - decisions/JETIX-TRM-MODEL-2026-04-30.md
  - decisions/STRATEGIC-INSIGHT-* (all 6 Hexagon)
  - wiki/concepts/jetix-realm/ (6 stubs)
  - reports/gamification-mining-analysis-2026-05-11.md
---
```

## Шаг 2 — Video Outline

Output: `outreach/dmitry-humanities-video-outline-2026-05-11.md`

### Структура (per Notion plan §4, 5-10 min recording)

**0:00-1:00 Intro**
- Кто Ruslan
- Зачем видео (parallel к письму, voice + face добавляет credibility)

**1:00-3:00 Jetix concept overview**
- Workshop visualised (на экране — diagram)
- Realm overview (gamification как operational layer)
- 1-2 concrete examples (Torn-Faction → Realm-Clan / EVE-MER → Realm-economic-reporting)

**3:00-5:00 «Мировой порядок» angle**
- Why этим заниматься: AI эпоха transforms info-work
- Anti-extraction principle (Varoufakis critique applied)
- Network State evolution thinking
- Progressive networks vs legacy hierarchies

**5:00-7:00 Ключевые вопросы к humanities (5 blocks verbatim per letter §7)**
- Pause для possibility of Dmitry to think
- Reference philosophical traditions humanities relevant

**7:00-9:00 Что сейчас работает**
- Foundation LOCKED state
- 722 wiki entries / Hexagon insights / Realm 6-entity
- Active mentors / progress

**9:00-10:00 Outro + ask**
- Готов к podcast / collaboration
- Прошу feedback от humanities-lens
- TG/email contact info

### Talking points per minute (specific scripts/notes для recording)

Per minute — 3-5 bullet points что сказать (NOT verbatim script, just talking points для Ruslan recording).

### Visuals slate (что на экране)

| Time | Visual |
|---|---|
| 0:00-1:00 | Talking head (intro) |
| 1:00-3:00 | Workshop diagram (mermaid) + Realm 6 entities |
| 3:00-5:00 | Hexagon insights map |
| 5:00-7:00 | Questions list slate |
| 7:00-9:00 | Wiki state dashboard / Foundation parts |
| 9:00-10:00 | Contact slate |

### Frontmatter

```yaml
---
title: Video outline для Dmitry (Гуманитарщина) — 5-10 min recording
date: 2026-05-11
type: video-outline-draft
status: DRAFT — awaits Ruslan refinement + recording
target: Дмитрий, host «Гуманитарщина»
authored_by: ai-scribe
prose_authored_by: hybrid-with-ack-trail
F: F2
G: video-outline-applied-now
R: refuted_if_recording_diverges_significantly_from_outline
parent_notion: 35d24963-... (Dmitry plan)
parent_letter: outreach/dmitry-humanities-letter-2026-05-11.md
---
```

## Шаг 3 — Surface в чат для Ruslan

После создания обоих файлов — surface:

- Letter path + word count + section breakdown
- Video outline path + duration check
- Embedded mermaid count (should be 4 в letter)
- Open items для Ruslan personalization:
  - Dmitry's фамилия / TG / email / channel URL — fill in
  - Prior contact history (если есть) — adjust intro
  - Channel specifics — adjust humanities references
  - Tone preference (formal/informal)
  - Specific ask (podcast / videozvonok / просто feedback)

«Letter + video outline готовы. Открывай в Antigravity / Obsidian / GitHub. Жду твой ack по open items + personalization edits. После твоих edits — recording.»

## Hard constraints

- **Constitutional posture:** F2 blast-radius (outreach files в `outreach/`), NO writes к Foundation / principles / .claude/config / shared/schemas / CLAUDE.md / decisions/ / wiki/
- **AI = scribe (Tier 2 R1):** structure + assembly only; Ruslan adds personal voice + specific Dmitry context
- **Tier 2 R6 provenance:** cite sources в frontmatter
- **Append-only** к `outreach/` (create dir if not exists)
- **Russian primary** для prose (Dmitry russian audience)
- **NO API keys** в commits
- **Truthful claims only:** что в wiki/decisions есть — that's it; NO embellishment

## Wall-clock target

- Letter draft: 15-25 min
- Video outline: 10-15 min
- Total: ~30-40 min

## Commit + push

```bash
mkdir -p outreach
git add outreach/dmitry-humanities-letter-2026-05-11.md outreach/dmitry-humanities-video-outline-2026-05-11.md
git commit -m "[outreach] Dmitry humanities letter + video outline draft — Jetix concept + world order angle + 5 humanities discussion blocks + 4 mermaid"
git push origin main
```

## Final report

Surface to Ruslan:
- SHA финального commit
- GitHub URLs (letter + outline)
- Word count letter / outline duration
- Mermaid count embedded
- Open items list (personalization needed)
- Recommended next: Ruslan reviews → edits → records → sends

Constitutional preserved. AI = scribe. Ruslan = sole strategist + personal voice authority.

GO. Жгу до конца.

===END PROMPT===
