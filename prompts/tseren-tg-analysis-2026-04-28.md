---
title: "Tseren Telegram Analysis — Server CC Launch Prompt"
date: 2026-04-28
type: cloud-code-launch-prompt
target: Claude Code session on server (claude/jolly-margulis-915d34)
parent_track: tseren-tserenov-outreach-analysis
step: 1.2.1
estimated_walltime: 15-45min
---

# §0 Mission

Анализ Telegram канала @systemsthinkinglife (Tseren Tserenov, «Системное мышление для жизни») для outreach decision (mentor / investor / partner). Это Шаг 1.2.1 многошагового research pipeline, отдельный track от Foundation v1.0 (Foundation LOCKED 2026-04-28, эта работа параллельная).

# §1 Источник

- **JSON export** Telegram Desktop, формат `result.json`
- **622 messages**, период 2021-03-12 → 2026-04-28 (5 лет архив)
- 533 messages с reactions, 606 с text, 19 forwards
- 5.7 MB
- **Branch:** `claude/clever-ramanujan-bd4845` (Cloud Cowork side)
- **Commit:** `fc055be` (head)
- **Path:** `raw/research/2026-04-28-tseren-tg-export/result.json`

# §2 Sync from CC branch

```bash
cd ~/jetix-os
git fetch origin claude/clever-ramanujan-bd4845
git checkout claude/jolly-margulis-915d34
git pull origin claude/jolly-margulis-915d34
mkdir -p raw/research/2026-04-28-tseren-tg-export
git show origin/claude/clever-ramanujan-bd4845:raw/research/2026-04-28-tseren-tg-export/result.json > raw/research/2026-04-28-tseren-tg-export/result.json
git add raw/research/2026-04-28-tseren-tg-export/result.json
git commit -m "[research] sync Tseren TG export from CC clever-ramanujan-bd4845"
git push origin claude/jolly-margulis-915d34
```

# §3 Контекст для analysis

Tseren Tserenov делает то же что делает Ruslan (Jetix founder) — направление **системного мышления + развития интеллекта**. Это RU-экосистема ШСМ Анатолия Левенчука.

Ruslan рассматривает его как кандидата на роль **mentor / investor / partner** — первый и потенциально лучший в этой категории на текущий момент. Поэтому требуется качественный analysis перед outreach.

Анализ делается **бережно**: не предложения / не суждения / не predictions. Только pattern extraction с цитатами.

# §4 Задача — 12 dimensions analysis

## Категория A — Кто он (identity & expertise)

**1. Identity**
- Имя, биография, локация, языки, фото (если упоминает в постах), professional background

**2. Expertise & focus areas**
- Топ-5 тем по частоте + что он позиционирует как core competency
- Что он делает профессионально (если упоминает)

**3. Core theses**
- Повторяющиеся claims: «системное мышление = X», «развитие интеллекта работает через Y»
- Топ-5 thesis statements которые он повторяет (с цитатами)

**4. Voice & personality**
- Tone (educational / philosophical / personal / business / провокативный)
- Style (структурированный / спонтанный / cited / raw)
- Production quality (длинные структурированные посты vs короткие takes)

## Категория B — Его экосистема (lineage)

**5. Methodology references**
- Цитаты Левенчука / упоминания ШСМ / конкретные frameworks
- Насколько прямо в школе ШСМ (Левенчук-производный) vs развил своё
- Конкретные books / authors которых рекомендует

**6. Influence network**
- Кого цитирует / уважает / с кем спорит
- Persons map: имена которые повторяются в постах
- Кто его mentor'ы / collaborators / противники (если visible)

## Категория C — Аудитория

**7. Audience signals**
- Reactions distribution (если есть в JSON `reactions:` field): top reactions, average per post, peaks
- Engagement rate evolution: последние 30 постов vs all-time
- Виды реакций: 👍 ❤️ 🔥 etc — какие dominant
- Если views в JSON есть — ranges, peaks, top-10 most-viewed posts

**8. Posting cadence + evolution**
- Total posts per year/month — bar chart-style summary
- Active periods vs lulls
- Topics drift over time (что менялось 2021 → 2026)

## Категория D — Fit assessment

**9. Career stage signals**
- Юный / experienced / settled / scaling — какой signal
- Monetization signals: упоминает ли платные курсы / Boosty / донаты / freemium
- Bandwidth: как часто пишет, насколько глубоко (signal загруженности)

**10. Partnership openness**
- Упоминает ли коллабы / сов.проекты / приглашения учеников / соавторов
- Открытые / закрытые сигналы — готов ли к connections
- Есть ли в архиве "ищу X" / "если ты Y, напиши" / "приходите на курс" patterns

## Категория E — Tactical для outreach

**11. Pitch angles**
- Что ему может быть ценного от Jetix (на основе его pain points / open questions / gaps в его стэке)
- Какие темы он проявил интерес но не разобрал глубоко (потенциальная co-creation зона)
- Какие frameworks он использует но видно что ищет lateral input

**12. Avoidance signals**
- Что он критикует / отвергает / о чём резок (anti-pitch — НЕ упоминать в контакте)
- Tone preferences: формально или casually обращаются к нему ученики / собеседники
- Что он считает плохим вкусом в outreach (если упоминает)

# §5 Workflow

## Phase A — Recon JSON (5 мин)

1. Прочитать структуру JSON (top-level keys, message types, available fields)
2. Подтвердить что reactions / forwards / replies есть в structured form
3. Identify any service messages (joins / channel events) для skip'а
4. Output: short note в analysis-report.md §0 «Source recon» — 5-10 строк

## Phase B — Processing script (10-15 мин)

Написать Python script `tools/analyze_tseren_tg.py` который:

- Parse `result.json`
- Filter only message-type entries (skip service)
- Extract per-message: id, date, date_unixtime, text (concatenate text_entities), reactions (count + emojis), forwarded_from, reply_to_message_id, character count
- Aggregate:
  - Posts per year, per month — counts
  - Reaction stats: total reactions per post (mean / median / max), top-emoji distribution, top-10 most-reacted posts
  - Text length distribution: short (<200 chars) / medium (200-1000) / long (>1000)
  - Forward sources frequency
  - Reply chain depth signals
- Word frequency analysis: top-100 значимых слов (с STOPWORDS filtering на русском)
- Topic clusters (simple — ключевые слова frequency-based, не ML)
- Sample posts per dimension (для citation)

Save processed data: `raw/research/2026-04-28-tseren-tg-export/processed-data.json`

## Phase C — Manual analysis with extraction (15-30 мин)

Прочитать processed data + sample posts (top by reactions; representative across years; explicit thesis posts) → manual analysis по 12 dimensions.

Каждая dimension:
- 3-7 findings as structured bullet points
- 3-5 верных дословных цитат как evidence (с date + msg id)
- Confidence (high / medium / low) на каждый major claim

## Phase D — Write report (10-15 мин)

Output: `raw/research/2026-04-28-tseren-tg-export/analysis-report.md`

Структура:

```markdown
# Tseren Tserenov — Telegram Analysis Report

**Source:** @systemsthinkinglife · 622 posts · 2021-03 → 2026-04
**Date analyzed:** 2026-04-28
**Purpose:** outreach decision (mentor / investor / partner)

## §0 Source recon
[Phase A output]

## §1 TL;DR
5-10 lines top-level findings.

## §2 Identity
[Findings + quotes + confidence]

## §3 Expertise & focus areas
...

[... все 12 sections ...]

## §14 Resultative summary
«Что я знаю о Tseren после Telegram analysis» — 1-2 параграфа integrated picture.

## §15 Outreach recommendations
- Pitch angles (top 3): какие подходы вероятно сработают
- Avoidance signals: что не делать в первом сообщении
- Tone calibration: как обращаться (вы / ты, формально / casually)
- First touch suggestion: какой именно low-friction first step предложить

## §16 Gaps for next steps
- Что Telegram НЕ показал
- Что нужно искать в Шагах 1.2.2 (YouTube), 1.2.3 (system-school.ru), 1.2.4 (Левенчук)
```

## Phase E — Commit + push

```bash
git add tools/analyze_tseren_tg.py raw/research/2026-04-28-tseren-tg-export/processed-data.json raw/research/2026-04-28-tseren-tg-export/analysis-report.md
git commit -m "[research] Tseren TG analysis report — 12 dimensions, 622 posts processed"
git push origin claude/jolly-margulis-915d34
```

# §6 Constraints

- **No AI hallucination** — каждый claim в отчёте backed дословной цитатой из export. Если evidence нет — сказать «pattern not visible» / «requires next-step source».
- **Russian primary** в findings text; English только для code / config / technical fields
- **Confidence calibration honest**: не "high" если evidence уровня "medium"
- **AI = scribe, не commentator** (per memory `feedback_ai_is_scribe_not_author_for_strategic_docs`)
  - Extract patterns, не judgements
  - Quote facts, не characterize Tseren'а как личность
  - Recommendations должны быть основаны на extracted signals, не на impression
- **Beta-first** — отчёт достаточно качественный для решения outreach action, не perfect (per memory `feedback_beta_first_not_perfectionism`)
- **Enterprise + $1T baseline** preserved (per memory `feedback_no_solo_founder_downgrade`) — если будет про fit для investor role, evaluate против реальной trajectory Jetix
- **Don't push to main** — только `claude/jolly-margulis-915d34`
- **Push после commit (always)**

# §7 Stop condition

Бригадир (CC server-side) STOP при completion:

1. Phase A done → recon committed
2. Phase B done → script + processed-data committed
3. Phase C done → manual analysis в head
4. Phase D done → analysis-report.md committed
5. Phase E done → push completed
6. **Notify** (через tmux session log или просто финальный output): `"Шаг 1.2.1 ANALYSIS DONE — report at raw/research/2026-04-28-tseren-tg-export/analysis-report.md, commit <SHA>, branch claude/jolly-margulis-915d34"`

Не делать Шаг 1.2.2 (YouTube) — это отдельный шаг для другой session с другими источниками (NotebookLM-based).

# §8 Estimated walltime

**15-45 минут** total:
- Phase A recon: 5 min
- Phase B script: 10-15 min (с быстрым debug если нужно)
- Phase C analysis: 15-30 min (зависит от глубины quote extraction)
- Phase D writing: 10-15 min
- Phase E push: 1 min

Если Phase B script упал — debug, не abandon. JSON структура подтверждена работающей. Если глубокая проблема с парсингом — flag в notes для Ruslan review.

---

*End of brief. Foundation track stays paused; this is Tseren research track. Compound velocity not expected (mechanical analysis, не synthesis). Output = decision-grade report для outreach action.*
