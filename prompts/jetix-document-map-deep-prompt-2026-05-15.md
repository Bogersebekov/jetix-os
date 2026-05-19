---
title: Deep prompt — карта местности всех основных документов Jetix OS + инструкция по изучению
date: 2026-05-15
type: server-cc-trigger-prompt
status: ready-to-fire
target_executor: server CC (Plan Mode, autonomous 1.5-3h)
target_output: decisions/JETIX-DOCUMENT-MAP-2026-05-15.md (или canonical/, server CC решит)
language: russian
purpose: создать единый authoritative «карта местности» документ — карту всех актуальных документов + инструкцию по изучению + 3 mermaid с цветовой кодировкой, для использования (a) как trekking в видео-знакомстве, (b) как onboarding для L1 / mentors / future partners, (c) как карта местности для самого Руслана
F: F2
G: document-map-applied-now
R: refuted_if_docs_list_diverges_more_than_10pct_from_canonical_within_30d
companion_files:
  - canonical/INDEX.md (existing index, дополнить указанием на новый MAP)
  - CANONICAL-WALKTHROUGH-2026-05-06.md (от 06.05, частично устарел — surface diff)
  - outreach/jetix-document-pool-2026-05-12.md (outreach-focused, не general)
---

# 🎯 Deep prompt: Карта местности всех основных документов Jetix OS + инструкция по изучению

> **Как использовать.** Открой `tmux new -s cc-doc-map`, запусти `claude`, paste этот файл как первый prompt. Server CC войдёт в Plan Mode и автономно выполнит всю работу за 1.5-3 часа.

---

## §0 Кто я / контекст (для server CC если новый)

**Руслан**, founder **Jetix OS** — multi-agent система для управления AI consulting business + личной жизнью. Berlin.

**Sole strategist** (Tier 2 R1). AI = scribe / structurer / analyst.

**Foundation v1.0 LOCKED 28.04.2026.** Tag `foundation-architecture-locked-2026-04-28`. 11 Parts + Pillar C.

**Charter v0 LOCKED 12.05.2026.** Heptagon (7 strategic insights) LOCKED 10-12.05.2026.

Sегодня — **2026-05-15**.

---

## §1 ЗАДАЧА

Создать **ОДИН авторитетный документ** — «карта местности» всех актуальных рабочих документов Jetix OS + инструкция по их изучению.

Этот документ нужен в трёх ролях:

1. **Trekking-карта в видео** — Руслан в видео-знакомстве (для Цэрэна / Левенчука / других L1 кандидатов) будет показывать этот документ в Antigravity вместо открытия 6 отдельных файлов. Mermaid'ы должны быть screen-share-friendly (читаемые при 1080p, не overcrowded).
2. **Onboarding-инструкция** — если человек после видео хочет изучить систему, ему даётся ссылка на этот документ → он видит карту + рекомендуемый track чтения для своего профиля → читает по track'у.
3. **Карта местности для самого Руслана** — quick orientation куда смотреть.

**Это НЕ:**
- Не заменяет `canonical/INDEX.md` (он остаётся как plain list)
- Не заменяет outreach doc pool (он остаётся как outreach-focused per-L1 sequence)
- Не Foundation write (это applied-now F2 deliverable, не Foundation-level)

---

## §2 ИСХОДНЫЕ ДОКУМЕНТЫ ДЛЯ КАРТЫ (минимум, server CC дополнит)

Server CC должен прочитать минимум следующие documents и surface ВСЕ актуальные (LOCKED + ACTIVE). Это **стартовый список** — НЕ полный.

### §2.1 Constitutional / Foundation
- [JETIX VISION FUNDAMENTAL](decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md) — 35 UC × 12 categories, Layer 1 of 2
- [JETIX FPF Constitutional Spec](design/JETIX-FPF.md) — 3758 строк, FPF-Steward governed
- [Foundation Build Master Plan Brief](decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md)
- 11 Parts: `swarm/wiki/foundations/part-1-*` … `part-11-*` + `principles/`
- 12 Tier-2 Constitutional rules (R1-R12) — `principles/tier-2-system/foundation-generic/`

### §2.2 Heptagon (7 Strategic Insights)
- H1 [Foundation Model](decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md)
- H2 [Partnership Model](decisions/STRATEGIC-INSIGHT-JETIX-PARTNERSHIP-MODEL-2026-05-10.md)
- H3 R&D Flywheel (§13 within Partnership)
- H4 [Network State Balaji](decisions/STRATEGIC-INSIGHT-BALAJI-NETWORK-STATE-2026-05-10.md)
- H5 [Tyson Mentorship Pattern](decisions/STRATEGIC-INSIGHT-TYSON-MENTORSHIP-PATTERN-2026-05-10.md)
- H6 [Gamified Platform](decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md)
- H7 [People-Network-State](decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md) ← LOCKED 12.05

### §2.3 Конституция клана
- [Charter v0 LOCKED](decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md) — 14 секций
- R12 Anti-Extraction packet — `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md`

### §2.4 Базовые методологические
- Документ 1A — [Базовая Система Управления](decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md) LOCKED 05.05
- Документ 1B — [Jetix Corporation](decisions/JETIX-CORPORATION-2026-05-05.md) LOCKED 06.05 (~30K слов)
- Workshop concept — [JETIX-WORKSHOP-CONCEPT-2026-04-30.md](decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md)
- TRM Model — [JETIX-TRM-MODEL-2026-04-30.md](decisions/JETIX-TRM-MODEL-2026-04-30.md)
- Foundation overview technical — [foundation-master-overview-technical-2026-04-29.md](swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md)
- Foundation overview human/workshop — [foundation-master-overview-human-workshop-2026-05-06.md](swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md)

### §2.5 Monetization research (Phase 2+ hypothesis bank)
- v0 — [JETIX-MONETIZATION-AUDIENCE-COOPERATION-METHODOLOGY-v0-2026-05-14.md](decisions/JETIX-MONETIZATION-AUDIENCE-COOPERATION-METHODOLOGY-v0-2026-05-14.md) — 75 H + 5 баckets
- Wave 2 — [reports/monetization-research-2026-05-14/wave2/](reports/monetization-research-2026-05-14/wave2/) — +18 H + 75 test designs + 15 книг + 25 industry + 73 Q sub-H = **166 H total**
- Status: `ruslan-acked-as-hypothesis-bank-2026-05-14` — bank для Phase 2+, не selection ladder

### §2.6 Outreach
- Pitch Doc — [outreach/jetix-mentor-partner-pitch-2026-05-12.md](outreach/jetix-mentor-partner-pitch-2026-05-12.md)
- Document pool — [outreach/jetix-document-pool-2026-05-12.md](outreach/jetix-document-pool-2026-05-12.md)
- Video scenario v2 — [_archive/calls/_VIDEO-RECORDING-tseren-2026-05-15.md](_archive/calls/_VIDEO-RECORDING-tseren-2026-05-15.md)
- Antigravity checklist — [_archive/calls/_VIDEO-ANTIGRAVITY-CHECKLIST-2026-05-15.md](_archive/calls/_VIDEO-ANTIGRAVITY-CHECKLIST-2026-05-15.md)
- L1 First Clan profiles — `profiles/l1-first-clan/` (9 имён)
- Anton call report — [reports/anton-call-report-2026-05-11.md](reports/anton-call-report-2026-05-11.md)

### §2.7 Operations / Methodology
- Voice pipeline canon — [swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md](swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md)
- AutoResearch — `tools/jetix-autoresearch/` + Karpathy integration plan
- Mermaid style guide — [swarm/wiki/operations/mermaid-style-guide-2026-05-07.md](swarm/wiki/operations/mermaid-style-guide-2026-05-07.md)
- Wiki Architecture v2 — `wiki/` + skills `/ingest` `/ask` `/lint` `/consolidate`
- CRM system — `crm/README.md` + `crm/PLAN.md`

### §2.8 Research deep
- People-NS research — [reports/jetix-people-network-state-research-2026-05-11.md](reports/jetix-people-network-state-research-2026-05-11.md)
- Game Theory research — [reports/jetix-game-theory-cheating-research-2026-05-12.md](reports/jetix-game-theory-cheating-research-2026-05-12.md)
- Phase 4 wiki digest — [reports/phase-4-wiki-digest-2026-05-11.md](reports/phase-4-wiki-digest-2026-05-11.md)
- Gamification question mining — [reports/gamification-question-mining-run-2026-05-11.md](reports/gamification-question-mining-run-2026-05-11.md)

### §2.9 Action Plan / strategic decisions
- [ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md](decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md) — 4-tier ladder
- Strategic decisions log — [decisions/strategic-decisions-2026-05-12.md](reports/strategic-decisions-2026-05-12.md) (если есть)
- Видения / визуализации `decisions/strategic/` — 29 D-Lock entries

### §2.10 Handoff / orientation
- canonical/INDEX.md (existing)
- CANONICAL-WALKTHROUGH-2026-05-06.md (110 docs со статусом, частично устарел)
- _HANDOFF_to_next_cowork_session_2026-05-11.md (latest cowork handoff)
- HOME.md, README.md, MIGRATION.md (root level)

**Server CC: surface ВСЕ дополнительные documents через `git log --oneline` за последние 30 дней + `find canonical/ decisions/ outreach/ reports/ swarm/wiki/synthesis/ -name "*.md"`. Подтянуть ВСЁ актуальное.**

---

## §3 PER-DOCUMENT FIELDS (обязательная схема в карте)

Для каждого документа карта должна содержать:

| Field | Что |
|---|---|
| Title | Имя документа |
| Path | Relative path в репо |
| Status | LOCKED / ACTIVE / DRAFT / SUPERSEDED |
| Type | constitutional / strategic-insight / charter / methodology / outreach / research / operations / handoff |
| Date created | YYYY-MM-DD |
| Last updated | YYYY-MM-DD (если правлено после создания) |
| LOCK tag | git tag if LOCKED |
| Reading time | @ 200 wpm Russian |
| Что внутри | 1-2 строки |
| Зачем нужен | 1 строка |
| Target audience | researcher / L1 candidate / mentor / operator / Ruslan-only |
| Cites | список documents этот документ ссылается |
| Cited by | список documents которые ссылаются на этот |
| Supersedes | если заменяет более ранний |
| F-G-R | Formality / Group-scope / Reliability per FPF B.3 |
| prose_authored_by | ruslan / hybrid-with-ack-trail / ai-draft |

**Provenance per item (Tier 2 R6):** для каждого LOCKED документа — commit SHA где случился LOCK.

---

## §4 ТРИ MERMAID СХЕМЫ (обязательно)

Все mermaids — per [mermaid-style-guide-2026-05-07.md](swarm/wiki/operations/mermaid-style-guide-2026-05-07.md) (Variant A cool blues palette). Использовать **разные accent цвета per category** для визуальной группировки.

### Mermaid 1 — Категориальная карта (overview map)

Назначение: одним взглядом видеть **все** документы, сгруппированные по категориям, с цветовой кодировкой.

Структура:
- `flowchart TB` или `graph TB`
- Subgraph per категория (Constitutional / Heptagon / Charter / Базовые / Monetization / Outreach / Operations / Research / Action Plan)
- Цвет subgraph fill = категория:
  - Constitutional / Foundation = тёмно-синий (#1a3a5c)
  - Heptagon = оранжевый (#e07b00)
  - Charter = пурпурный (#6b3fa0)
  - Базовые методологические = teal (#2a7a7a)
  - Monetization = зелёный (#3a8a3a)
  - Outreach = жёлто-зелёный (#a0a020)
  - Operations / Methodology = серый (#5a5a5a)
  - Research deep = голубой (#3a7aa0) — Variant A core
  - Action Plan / Strategic decisions = красно-розовый (#a04a4a)
- Status через node shape:
  - LOCKED = `[[Title]]` (double bracket)
  - ACTIVE = `[Title]` (single rect)
  - DRAFT = `(Title)` (rounded)
  - SUPERSEDED = `((Title))` (circle) + strikethrough в label
- Под каждым node — короткая подпись «что внутри» (3-5 слов)

Должно помещаться на одном экране 1080p (screen-share quality). Если получается переполнено — разделить на 2 sub-mermaid'а.

### Mermaid 2 — Reading Order Ladder (4 tracks for different audiences)

Назначение: дать рекомендованный порядок чтения для 4 типов аудитории. Чтобы человек сразу видел «вот мой track».

4 tracks:

**Track A — «Быстрый обзор» (~50 мин)** — для человека после видео:
- Pitch Doc (18 мин) → Charter §1 Preamble (5 мин) → H7 People-NS (12 мин) → Anton report (29 мин, опционально)

**Track B — «L1 candidate serious» (~3-4 ч)** — для серьёзного кандидата:
- Pitch → Charter v0 (full) → H6 Gamified + H7 People-NS → Workshop concept → Anton report → 2-3 relevant Hexagon insights per profession

**Track C — «Researcher / academic» (~8-12 ч)** — для глубокого читателя:
- Foundation overview technical → all H1-H7 → People-NS research → Game Theory research → Phase 4 wiki digest → Vision FUNDAMENTAL

**Track D — «Mentor / partner / investor» (~5-7 ч)** — для potential investor / advisor:
- Doc 1A → Doc 1B → Vision FUNDAMENTAL → Charter → TRM Model → Action Plan Phase 1 → Hexagon (selective)

Mermaid: `flowchart LR` с ветвлениями. Каждый track — отдельная subgraph. Документы — nodes. Числа = минуты чтения. Total reading time per track видно visually.

### Mermaid 3 — Граф зависимостей (cites / extends / supersedes / locked-by)

Назначение: показать **как документы строятся друг на друге**.

Edges типизированы (different style per type):
- `depends-on` (solid arrow)
- `extends` (dashed arrow)
- `supersedes` (red strikethrough arrow)
- `cites` (thin gray arrow)
- `locked-by` (double arrow с timestamp)

Примеры зависимостей которые должны быть visible:
- Charter v0 ← H7 People-NS ← Heptagon ← Foundation ← Vision FUNDAMENTAL
- R12 ← H7 People-NS + Game Theory research
- Doc 1B ← Doc 1A ← Foundation
- Monetization Wave 2 ← Wave 1 ← v0 prompt
- Video scenario v2 ← Pitch ← Charter ← H7
- Action Plan ← Hexagon ← Foundation

Это **граф знаний**, не tree. Edges могут пересекаться.

---

## §5 ИНСТРУКЦИЯ ПО ИЗУЧЕНИЮ (текстовая, помимо mermaid)

После mermaids — раздел с текстовыми инструкциями:

### «Если ты впервые здесь»
- Какой track тебе подходит (вопрос «кто ты»)
- Минимальный путь к пониманию
- Где остановиться если хочешь только overview

### «Если ты L1 candidate»
- Per-name customization (ссылка на `outreach/jetix-document-pool-2026-05-12.md` §«Per-L1-Candidate»)

### «Если ты mentor / investor»
- Что прочитать чтобы оценить
- Что НЕ нужно (Foundation технические детали)

### «Если ты researcher»
- С чего начать
- Самые плотные deep-research отчёты

### «Если ты сам Ruslan и нужна orientation»
- Quick reference по path'ам
- Где что искать

---

## §6 FORMAT / STYLE

- Markdown с YAML frontmatter (см. ниже шаблон)
- Russian primary, English ok для tech terms
- Все file paths — clickable markdown links `[label](path)` для Antigravity
- Все 3 mermaid embedded inline (не separate files)
- Append-only updates discipline (§«Changelog» в конце)
- Cross-references как relative paths

### YAML frontmatter шаблон

```yaml
---
title: Карта местности Jetix OS — все основные документы + инструкция по изучению
date: 2026-05-15
type: document-map / orientation-guide
status: ACTIVE
purpose: |
  Карта-инструкция для (a) trekking в видео-знакомстве, (b) onboarding L1/mentors,
  (c) self-orientation Ruslan'а.
audience:
  - L1 First Clan candidates (9 имён)
  - Future mentors / investors / partners
  - Researchers
  - Ruslan (self-orientation)
F: F2
G: document-map-applied-now
R: refuted_if_docs_list_diverges_more_than_10pct_from_canonical_within_30d
prose_authored_by: ai-draft
provenance:
  cites:
    - canonical/INDEX.md
    - CANONICAL-WALKTHROUGH-2026-05-06.md
    - outreach/jetix-document-pool-2026-05-12.md
  trigger_prompt: prompts/jetix-document-map-deep-prompt-2026-05-15.md
language: russian
---
```

---

## §7 ГДЕ РАЗМЕСТИТЬ

**Suggest:** `decisions/JETIX-DOCUMENT-MAP-2026-05-15.md`

Причина: это applied F2 deliverable (используется в видео + outreach), не constitutional. Decisions/ — корректный namespace.

**Alternative:** `canonical/JETIX-DOCUMENT-MAP-2026-05-15.md` (но canonical/ обычно содержит только INDEX).

**Server CC: выбери location, обоснуй в commit message.**

---

## §8 ПОБОЧНЫЕ ОБНОВЛЕНИЯ (мелкие, в одном commit'е)

1. **canonical/INDEX.md** — добавить указатель на новый MAP в самом верху как «See first: JETIX-DOCUMENT-MAP-2026-05-15.md»
2. **outreach/jetix-document-pool-2026-05-12.md** — добавить ссылку «Companion: новая карта местности → ...» в frontmatter / §0
3. **_archive/calls/_VIDEO-RECORDING-tseren-2026-05-15.md** Блок 5 — обновить чтобы упомянуть MAP как primary visual вместо отдельных файлов
4. **_archive/calls/_VIDEO-ANTIGRAVITY-CHECKLIST-2026-05-15.md** — добавить Tab 0 «JETIX-DOCUMENT-MAP» в самом начале как primary file для screen-share

---

## §9 CONSTITUTIONAL DISCIPLINE

- **prose_authored_by:** ai-draft (это descriptive index, не strategic prose)
- **Tier 2 R1** preserved — не strategize, только catalog
- **Tier 2 R2** preserved — не trogат Foundation paths (Parts 1-11 / principles/ / shared/schemas/ / .claude/config/)
- **Tier 2 R6** preserved — provenance per item (commit SHA + path + date для каждого LOCKED документа)
- **Tier 2 R11** preserved — Default-Deny на uncategorized actions
- НЕ promote / decide / recommend
- НЕ §РЕКОМЕНДАЦИИ / §МОИ ВЫВОДЫ (это покрыто feedback_breadth_not_selection EXTENSION 2026-05-14)
- Reading order = **objective reading sequence**, не моя «лучше начать с X»

---

## §10 VERIFICATION ПЕРЕД COMMIT

Server CC выполняет перед commit:

1. **Все cross-references resolve** — каждый `[label](path)` указывает на actual existing file
2. **YAML frontmatter valid** — `yaml.safe_load` parse
3. **Mermaid validation** — `/validate-mermaid` skill на все 3 схемы (если skill экземпляр доступен; иначе manual visual review)
4. **Mermaid screen-share-friendly** — render at 1920×1080, читаемо без zoom
5. **Reading times accurate** — `wc -w` per file / 200 wpm
6. **No API keys / secrets** в content
7. **API keys grep** — `grep -rE 'ANTHROPIC_API_KEY|sk-[A-Za-z0-9]{32,}' decisions/JETIX-DOCUMENT-MAP-*.md` → 0 hits
8. **Tier 2 R6 provenance check** — для каждого LOCKED документа есть commit SHA

---

## §11 COMMIT + PUSH

```bash
git add decisions/JETIX-DOCUMENT-MAP-2026-05-15.md \
        canonical/INDEX.md \
        outreach/jetix-document-pool-2026-05-12.md \
        _archive/calls/_VIDEO-RECORDING-tseren-2026-05-15.md \
        _archive/calls/_VIDEO-ANTIGRAVITY-CHECKLIST-2026-05-15.md
```

Commit message convention:

```
[document-map] карта местности всех основных документов + 3 mermaid (категориальная / reading order ladder / граф зависимостей) + side-updates canonical-INDEX + doc-pool + video-scenario Tab 0

Что нового:
- decisions/JETIX-DOCUMENT-MAP-2026-05-15.md (NEW) — главная карта
- 3 mermaid схемы с цветовой кодировкой per категория
- 4 reading tracks (быстрый обзор / L1 / researcher / mentor)
- Per-document metadata schema (status / type / reading time / cites / cited-by / F-G-R)
- Provenance per LOCKED документу
- Текстовая инструкция «если ты X — начни с Y»

Side updates:
- canonical/INDEX.md — pointer to new MAP at top
- outreach/jetix-document-pool-2026-05-12.md — companion link to MAP
- _archive/calls/_VIDEO-RECORDING-tseren-2026-05-15.md Блок 5 — MAP как primary visual
- _archive/calls/_VIDEO-ANTIGRAVITY-CHECKLIST-2026-05-15.md — Tab 0 MAP
```

Затем `git push origin main`.

---

## §12 ВРЕМЯ + SCOPE

- **Ожидаемое время:** 1.5-3 ч autonomous Plan Mode
- **Plan Mode подходит** (multiple files / deep reading / careful mermaid composition)
- **Парallel reading допустим** — server CC может open file batches
- **Если упирается в context** — split на phases (Phase A categorization → Phase B mermaids → Phase C reading tracks → Phase D verify + commit)

---

## §13 ЕСЛИ ВОЗНИКАЮТ ВОПРОСЫ

Server CC: если по ходу работы возникает фундаментальный strategic вопрос — **НЕ решать самостоятельно**. Записать в раздел «§Open Questions for Ruslan» в конце документа и продолжать остальную работу. Открытые вопросы = hypotheses-to-test (per `feedback_breadth_not_selection.md`), не gates.

Tactical / formatting вопросы — решай сам.

---

## §14 ПОСЛЕ COMPLETION

После git push:

1. Создать `_HANDOFF_to_next_cowork_session_2026-05-15.md` с указателем на новый MAP
2. (опционально) Mermaid PNG export для использования в видео — `mermaid.live` или skill `/mermaid-export`
3. Сообщить Ruslan'у через CRM update / append к scratchpad: «MAP готов, commit SHA, render screen-share OK / нужны правки»

---

## §15 НАПОМИНАНИЕ КОНСТИТУЦИОННЫМ ПРАВИЛАМ

- НЕ commitить secrets / API keys
- НЕ skip hooks (`--no-verify`)
- НЕ force-push в main
- НЕ trogат `~/.ssh/` / `private/` / `.env`
- Commit message: `[area] description` (этот раз: `[document-map] ...`)
- Russian for content, English ok for tech / commit headers

---

## §16 ОЖИДАЕМЫЙ РЕЗУЛЬТАТ

После `git pull origin main` в Antigravity:
- Новый файл `decisions/JETIX-DOCUMENT-MAP-2026-05-15.md` (~600-1200 строк + 3 mermaid)
- Обновлённый `canonical/INDEX.md` с pointer на MAP
- Обновлённый Video scenario / Antigravity checklist с Tab 0 = MAP

Руслан открывает MAP в Antigravity → видит:
1. **Mermaid 1 (категориальная карта)** — overview сразу
2. **Mermaid 2 (reading ladder)** — какой track читать
3. **Mermaid 3 (граф зависимостей)** — как документы связаны
4. **Per-document detail table** — drill-down per файл
5. **Instructions per audience** — кому что читать

Эта карта затем используется:
- В видео Блок 5 как primary visual (вместо открытия 6 отдельных файлов)
- В TG-выдаче L1 кандидатам как первая ссылка после видео
- Для onboarding mentors / partners
- Для self-orientation Ruslan'a

---

*Создано 2026-05-15 (Cloud Cowork session). Trigger для server CC autonomous Plan Mode execution. Constitutional anchor: AI = scribe / structurer / analyst, Ruslan = sole strategist. Tier 2 R1/R2/R6/R11 + append-only + Default-Deny.*
