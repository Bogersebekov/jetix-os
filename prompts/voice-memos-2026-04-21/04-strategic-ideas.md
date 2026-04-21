---
id: voice-memos-step-5-strategic-ideas
title: Step 5 — Strategic Ideas / Гипотезы из ~117 Voice-Memos
date: 2026-04-21
type: prompt
status: ready
depends_on: Step 1 (transcripts ready)
parallel_with: Step 3 (mini-wiki), Step 4 (year plan)
---

# Step 5 — Strategic Ideas / Гипотезы из ~117 Voice-Memos

## Контекст

Voice-memos Ruslan'а — это его main "thinking channel". Он туда надиктовывает стратегические idеи, гипотезы про бизнес-модели, community, движения, философию. Часто эти идеи **теряются** в потоке операционных TODOs и философских размышлений.

Нужно вытащить именно **strategic layer** — идеи и гипотезы уровня "если X то Y", business models, community / movement visions, philosophical frames, ставки (bets).

**Это главный вход для Genesis Document — особенно Part A (Philosophy), Part B (7 Dimensions), Part C (Capabilities overlays).**

Notion page: https://www.notion.so/3492496333bf813fbbbec5deabcc61a4

## Критическое правило

**Извлечение ПРЯМО ИЗ RAW TRANSCRIPTS**, не из review report / mini-wiki / year-plan. Все три шага (3, 4, 5) должны быть independent — каждый читает raw transcripts самостоятельно.

**НЕ читать VOICE-MEMOS-MINI-WIKIPEDIA.md или VOICE-MEMOS-YEAR-PLAN.md** — иначе категории / находки этого шага заразятся их структурой.

**НЕ игнорировать "странные" идеи** — странное может быть gold. Ruslan часто высказывает радикальные / амбициозные гипотезы которые другие системы отсеяли бы как шум.

## Задача

Извлечь полный strategic layer из всех ~117 transcripts по 5 категориям:

1. **Hypotheses** — формулировки "если X то Y" / "предполагаю что..." / "возможно..."
2. **Business Models** — идеи как зарабатывать, pricing, монетизация
3. **Community / Movement Ideas** — объединение людей, ecosystem thinking, "Jetix объединяет winners", мировой масштаб
4. **Philosophical Frames** — миссия, ценности, long-term vision (200-year thinking), смысл, этика
5. **Bets / Ставки** — куда Ruslan хочет вкладывать ресурсы, в чём уверен, на что ставит

## Input

- `raw/transcripts/*.txt` — ~117 файлов (single primary source)
- `raw/voice-memos/` — для mtime sorting chronologically
- Context reference (для НЕ-дублирования, не primary):
  - `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md` — 367 цитат уже собранных

## Алгоритм

### Фаза 1 — Inventory + chunking

1. Список всех transcripts chronologically
2. Chunks по 10-15 transcripts (меньше чем в Шагах 3-4 потому что strategic layer плотнее и требует внимательнее чтения)

### Фаза 2 — Deep extraction через subagents (parallel batches)

Для каждого chunk — spawn subagent через Task tool с фокусом ТОЛЬКО на strategic layer:

```
Task: Извлечь strategic ideas / hypotheses / business-models / community /
      philosophy / bets из batch transcripts.

Input: [transcript paths для этого chunk]

КРИТИЧНО:
- Preserve direct Ruslan voice (verbatim quotes, Russian)
- НЕ переформулировать / НЕ "улучшать" — только копировать точные слова
- НЕ отсеивать "странные" идеи — они могут быть gold
- Каждый item имеет attribution: [src:transcript_path:approximate_position]

Для каждого transcript субагент находит:

1. HYPOTHESES (паттерны: "если...то", "предполагаю", "возможно", "скорее всего"):
   {
     "hypothesis": "точная формулировка или близкий paraphrase",
     "quote_verbatim": "...",
     "confidence_signal": "высокая/средняя/низкая (из voice)",
     "testable": true/false,
     "domain": "business/technology/social/personal",
     "transcript": "audio_XXX.txt"
   }

2. BUSINESS MODELS:
   {
     "model_name": "e.g., 'Jetix как Resource-Allocation Engine'",
     "description_quote": "...",
     "revenue_mechanism": "как именно зарабатывает",
     "target_segment": "кто клиент / участник",
     "differentiator": "чем отличается",
     "phase": "now / €50K / €200K / post-€200K / long-term",
     "transcript": "audio_XXX.txt"
   }

3. COMMUNITY / MOVEMENT IDEAS:
   {
     "idea": "е.g., 'Jetix объединяет winners', 'AI-native community'",
     "core_quote": "...",
     "who_belongs": "кого Ruslan видит как участников",
     "purpose": "зачем community существует",
     "scale": "local / regional / global / 'мировой масштаб'",
     "mechanism": "как community работает / связывается",
     "transcript": "audio_XXX.txt"
   }

4. PHILOSOPHICAL FRAMES:
   {
     "frame": "e.g., 'жизнь как GTA с сохранениями', '200-year vision'",
     "articulation_quote": "...",
     "implications": "что это значит для design / decisions",
     "category": "mission / values / long-term-vision / ethics / epistemology / meaning",
     "transcript": "audio_XXX.txt"
   }

5. BETS / STAVKI:
   {
     "bet": "во что Ruslan верит / на что ставит",
     "quote": "...",
     "resource_commitment": "время / деньги / фокус / люди",
     "upside": "что получает если prediction correct",
     "downside": "что теряет если wrong",
     "timeframe": "когда станет ясно",
     "transcript": "audio_XXX.txt"
   }

Output: JSONL со структурированными items.
```

### Фаза 3 — Aggregation + thematic clustering

После subagent runs:

1. **Cluster hypotheses** по domain (business / technology / social / personal)
2. **Cluster business models** по:
   - Revenue mechanism (consulting / templates / community membership / platform / marketplace / other)
   - Phase alignment
3. **Map community ideas** на scale axis (local → mировой)
4. **Organize philosophical frames** по category (mission / values / vision / ethics / epistemology / meaning)
5. **Rank bets** по confidence signal + resource commitment
6. **Cross-references:**
   - Где hypothesis подтверждается bet
   - Где business model зависит от community idea
   - Где philosophy drives business model

### Фаза 4 — Output document

Создать `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md`:

```markdown
---
id: voice-memos-strategic-ideas
title: Strategic Ideas / Гипотезы из ~117 Voice-Memos
date: 2026-04-21
type: strategic-extraction
status: ready
sources:
  - raw/transcripts/ (~117 файлов)
purpose: |
  Strategic layer extracted напрямую из voice-memos.
  Primary input для Genesis Document Part A (Philosophy) + Part B (7 Dimensions).
---

# Strategic Ideas / Гипотезы из ~117 Voice-Memos

## 1. Meta-Stats
- Total strategic items: N
  - Hypotheses: N
  - Business models: N
  - Community ideas: N
  - Philosophical frames: N
  - Bets: N
- Transcripts contributing strategic layer: N / 117
- Hottest transcripts (most strategic items): [top 10 list]

## 2. Hypotheses

### 2.1 Business domain
| # | Hypothesis | Quote | Testable | Confidence |
|---|-----------|-------|----------|------------|

### 2.2 Technology domain
...

### 2.3 Social domain
...

### 2.4 Personal domain
...

### 2.5 Cross-domain / Meta hypotheses
(гипотезы на стыке — often most valuable)

## 3. Business Models

### 3.1 Phase 1 (€50K → €200K)
| Model | Revenue mechanism | Target segment | Differentiator | Quote |
|-------|-------------------|----------------|----------------|-------|

### 3.2 Phase 2 (post-€200K)
...

### 3.3 Long-term / experimental
...

### 3.4 Discarded / rejected (если Ruslan явно отказался)
...

## 4. Community / Movement Ideas

### 4.1 Core community concept
Главная идея что такое Jetix community (из самых чётких формулировок)

### 4.2 Community ideas list

| # | Idea | Who belongs | Purpose | Scale | Mechanism | Source |
|---|------|-------------|---------|-------|-----------|--------|

### 4.3 Connection to "winners / объединение"
(специальный раздел — это ключевая тема которую Ruslan flag'нул, нужно собрать все upмentions в один connected narrative)

### 4.4 World-scale ambitions
Где Ruslan говорит про "мировой масштаб" / "экономические прорывы" / движение

## 5. Philosophical Frames

### 5.1 Mission articulations
(как Ruslan формулирует миссию в разные моменты)

### 5.2 Core values
(что Ruslan явно называет важным)

### 5.3 Long-term / 200-year vision
(все upmentions будущего через 50-200 лет)

### 5.4 Ethics / epistemology / meaning
(философские стойки)

### 5.5 Metaphors / аналогии Ruslan использует
("жизнь как GTA", "дирижёр", "корпорация из одного", "Westinghouse / Accenture", "merchants объединили мир", etc.)

## 6. Bets / Ставки

### 6.1 High-confidence bets
| # | Bet | Resource commitment | Upside | Downside | Timeframe | Quote |
|---|-----|---------------------|--------|----------|-----------|-------|

### 6.2 Medium-confidence bets
...

### 6.3 Speculative bets
...

### 6.4 Contrarian bets
(где Ruslan идёт против mainstream view — особенно ценно)

## 7. Cross-references

### 7.1 Hypothesis → Bet
Где гипотеза подтверждается Ruslan'овским bet:
- Hypothesis "X" → Bet "Y"

### 7.2 Philosophy → Business Model
Где философия drives конкретную бизнес-модель

### 7.3 Community → Business Model
Где community ideas требуют specific monetization

### 7.4 Internal tensions
Где strategic ideas конфликтуют между собой:
- "X" vs "Y" (оба от Ruslan)

## 8. 7-Dimensions Map

Как strategic items питают 7 dimensions Genesis Document:

### 8.1 База (universal OS)
- Relevant hypotheses:
- Relevant philosophy:

### 8.2 Jetix-life
...

### 8.3 Jetix-company
...

### 8.4 Community ← ожидается высокая плотность
...

### 8.5 Money path ← business models все сюда
...

### 8.6 Relationships ← community-winners connection
...

### 8.7 Philosophy ← весь Phil раздел
...

## 9. Top 30 Strategic Quotes (Ruslan voice preserved)

(30 самых важных direct quotes которые должны попасть в Genesis Document дословно)

| # | Quote | Type (hyp/bm/comm/phil/bet) | Transcript |
|---|-------|------------------------------|------------|

## 10. Provenance Index

(compact table: strategic item → transcript source)
```

### Фаза 5 — Commit

```bash
git add raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md
git commit -m "[research] Strategic ideas extraction из ~117 voice-memos"
git push origin claude/jolly-margulis-915d34
```

## Ограничения

- **Primary source = .txt transcripts**. Не читать mini-wiki / year-plan output.
- **Preserve voice** — direct quotes verbatim, Russian, никаких "улучшений".
- **НЕ ФИЛЬТРОВАТЬ "странные" идеи** — радикальное / амбициозное может быть core.
- **Attribution обязательна** — каждый strategic item с transcript reference.
- **НЕ добавлять свои интерпретации** — если что-то unclear, flag как `[?unclear intent]` но сохрани quote.
- **НЕ дублировать wiki harvest 367 цитат** — если item уже в harvest, пометь `[also in wiki harvest]` и добавь новый context из voice-memo.
- **Cross-references (Фаза 3 step 6)** — это ТОЛЬКО когда связь явная в тексте, не выдумывать связи.
- **ETA:** 3-5 часов (это самый глубокий из трёх параллельных шагов).

## Deliverable (stdout summary)

```
# Strategic Ideas Extraction Complete

- File: raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md
- Size: X lines / Y KB
- Transcripts analyzed: N
- Strategic items total: N
  - Hypotheses: N (breakdown by domain)
  - Business models: N (breakdown by phase)
  - Community ideas: N (scales breakdown)
  - Philosophical frames: N
  - Bets: N (confidence breakdown)
- Cross-references: N
- 7-dimensions impact: [short summary]
- Top 30 quotes selected: yes
- Commit hash: abc1234
```
