# Anton Call Report — Prompt для запуска CC

> **Создано:** 2026-05-11 midday.
> **Назначение:** новый CC instance собирает review-отчёт за 2 месяца для созвона Ruslan'а с ментором Антоном.
> **Parent:** Notion subpage `35d2496333bf8179b809f68640f86ed3` (Отчёт для созвона с Антоном — Подготовка).
> **Wall-clock:** ~90-120 min target.

---

## Команды запуска

```bash
# В новом tmux window:
claude --dangerously-skip-permissions

# Затем paste весь текст ниже под линией ===PROMPT===
```

---

===PROMPT===

Задача: собрать детальный review-отчёт за последние 2 месяца для созвона Ruslan'а с ментором Антоном.

Source of truth: Notion подстраница https://www.notion.so/35d2496333bf8179b809f68640f86ed3 (Отчёт для созвона с Антоном — Подготовка, parent Daily Log 11.05). Прочитай ПОЛНОСТЬЮ перед началом.

ACK defaults по §7 open questions:
- Anchor дата = 2026-03-11 (60 дней назад от сегодня)
- Формат output = markdown + Notion mirror (PDF skip)
- Voice insights = сводно (top themes, не построчно)
- Все 5 блоков §4 релевантны
- Дата созвона + Антонов psychology background — Ruslan решит отдельно, не блокирует сборку

Выполни Шаги 1-5 из §6 Notion подстраницы:

### ШАГ 1 — Data collection (30-45 min)

1. **GitHub history:**
   ```
   git log --since="2026-03-11" --pretty=format:"%h %ad %s" --date=short > /tmp/git-log-2mo.txt
   ```
   Категоризируй commits: foundation / wiki / reports / decisions / tools / fixes. Counts per category.

2. **Notion Daily Logs query** (DB 30a24963-33bf-8005-817a-000beb10bcd4):
   - Все dailies с date 2026-03-11 → 2026-05-11
   - Extract: Key Action (Plan) + Actual Main Action + Reflection + Day type
   - Identify recurring themes / turning points / major events

3. **Toggl stats** (используй tools/toggl_sync.py или Toggl API):
   - Breakdown по 8 canonical projects за 60 дней
   - Total hours per project / per category (DW / Сон / Рутина / etc.)
   - DW sub-direction breakdown (RES/OBR/SOZD/UCH/PODG/KOM)
   - Energy distribution (flow / обычный / тяжело / пиздец)

4. **Voice pipeline stats:**
   - 47 voice memos обработано
   - Top themes (cluster summary from reports/voice-pipeline-2026-05-10/06-meta-analysis.md)
   - 1262 candidates → 137 Tier A v3
   - Major recurring concepts (top-20)

5. **Wiki KB current state** (из reports/wiki-state-analysis-2026-05-11.md):
   - 575 entries breakdown by type
   - 6 niches
   - Top edge clusters / hubs

6. **Decisions list:**
   ```
   ls decisions/ | grep -E "RUSLAN-ACK|STRATEGIC-INSIGHT|JETIX" | sort
   ```
   Group by type: Foundation Parts / Hexagon insights / canonical docs / RUSLAN-ACK records.

### ШАГ 2 — Narrative сборка (30-45 min)

Напиши timeline narrative по фазам (по неделям или по событиям, твой call). Для каждой фазы:
- Дата range
- Что делал (top 3-5 activities)
- Что узнал (insights surfaced)
- Turning points / decisions
- Какой sentiment / energy (per Toggl + Daily Log Reflections)

Insights mapping:
- 6 Hexagon insights в хронологическом порядке (Foundation Model → Partnership → R&D → Balaji → Tyson → Gamified)
- Secondary insights (Workshop / TRM / Partner Factory / Network State elements / etc.)
- Cross-connections между insights (как один привёл к другому)

Deliverables timeline:
- Canonical LOCKED docs (когда что было acked)
- Infrastructure milestones (Wiki v2 / Voice Pipeline / AutoResearch / Mermaid stack)
- Operations (Stage 2A v3 / Gamification plan)

Open tensions / blockers:
- 5 open tensions из Action Plan §1.5
- RES.1-3 из Partnership Model
- Что отложено (Phase-2+ deferred)

### ШАГ 3 — Mermaid diagrams (10-15 min)

1. **Timeline gantt** — фазы 2 месяцев + major milestones (LOCKED events / insight births)
2. **Insights map flowchart** — 6 Hexagon + secondary + связи между ними
3. **State diagram** — Точка А (~2 месяца назад: Life OS v0 + видение) → Точка Б (сейчас: Foundation LOCKED + 6 Hexagon + Wiki + AutoResearch)

Palette: cool blues Variant A per swarm/wiki/operations/mermaid-style-guide-2026-05-07.md.

### ШАГ 4 — Final assembly (15 min)

Структура per §2 Notion subpage:
- §A Executive summary (1 page — 3 insights + 3 blocks + 1 key question)
- §B Путь (timeline narrative по фазам)
- §C Что нового узнал (insights breakdown)
- §D Что реально сделал (deliverables)
- §E Что НЕ сделал / blockers (open tensions)
- §F Где сейчас (Точка А detailed snapshot)
- §G Ключевые вопросы/задачи (5 блоков §4 from subpage)
- §H Как Anton может быть useful

Tone: на человеческом, без jargon, понятно человеку извне (Anton не знает Jetix-конкретики). Объяснять с нуля если нужно.

### ШАГ 5 — Output

1. **`reports/anton-call-report-2026-05-11.md`** — полный отчёт (target 3-5K слов)
2. **Update Notion subpage 35d2496333bf8179b809f68640f86ed3:**
   - Add new section "## §FULL REPORT" с mirror полного отчёта
   - Сохрани existing sections §0-§8 на месте
3. **Commit + push:**
   ```
   git add reports/anton-call-report-2026-05-11.md
   git commit -m "[anton-call] Review report 2 months — narrative + insights + deliverables + open tensions + 3 mermaid + 5 question blocks"
   git push origin main
   ```

### Open Questions surface обратно Ruslan'у

Если в процессе найдёшь что-то ambiguous (например anchor date вообще должна быть 2026-03-15 а не 2026-03-11; или Anton background неизвестен влияет на блок 2 формулировку) — surface как §I Open Questions for Ruslan в самом отчёте, не блокируй.

### Hard constraints

- Constitutional posture: F2 blast-radius, append-only к reports/ и Notion, NO writes в Foundation / principles / .claude / decisions / canonical
- AI = scribe rule (Tier 2 R1) — пишешь факты + структуру, НЕ strategize, НЕ propose decisions. Decisions = Anton'у через Ruslan'a.
- НЕ блокируй background process (Stage 2A done, но если gamification mining запускается параллельно — не interfere).
- Если Toggl API token недоступен — surface как warning, продолжай без Toggl data (mark section as "data unavailable")
- Если что-то fail (Notion query error, git command error) — surface, продолжай с available data, отметь gap

### Wall-clock target

90-120 min total. Если идёт дольше 150 min — checkpoint + ask Ruslan продолжать или partial-deliver.

### Final report

Когда сделано — дай в чат:
- SHA финального commit
- GitHub URL отчёта
- Word count
- Key surprising findings (1-2 sentence — что non-obvious surfaced при сборке)
- Open questions surfaced (если есть)

Constitutional posture preserved. Ruslan = sole strategist. AI = scribe + structurer.

GO.

===END PROMPT===
