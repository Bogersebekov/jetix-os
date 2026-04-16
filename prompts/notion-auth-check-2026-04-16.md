---
type: execution-prompt
date: 2026-04-16
phase: step-2-alpha-prerequisite
target: claude-code-server
autonomy: partial-requires-oauth
---

# Notion MCP — Авторизация + Sanity Check

## Цель

Аутентифицировать Notion MCP на сервере `100.99.156.28` и убедиться что всё
работает перед запуском автономного Notion extraction
(см. `prompts/notion-full-extraction-2026-04-16.md`, Фаза α из
`design/NOTION-MIGRATION-PLAN.md`).

## Контекст

- **Ты** — Claude Code на сервере jetix-os. Модель Opus 4.6 или Sonnet 4.6.
- **Ветка:** main (после `git pull origin main`).
- **Известный блокер:** Notion MCP не аутентифицирован. Задокументирован в
  `reports/system-design-inputs-collection-2026-04-16.md` (Фазы 2/3/4 были пропущены).
- **Инструкция по разблокировке:** частично в `agents/system-admin/scratchpad.md`,
  финальный flow описан ниже.

## Шаги

### Шаг 1. Pull + проверь статус MCP

```bash
cd ~/jetix-os && git pull origin main
```

Потом в Claude Code CLI:
```
/mcp
```

Посмотри секцию для `notion`. Возможные состояния:
- ✅ `connected` — всё хорошо, переход к Шагу 5
- ⚠️ `disconnected` / `auth required` — иди в Шаг 2

### Шаг 2. Запусти OAuth flow

Вызови:
```
mcp__notion__authenticate
```

Получишь объект с URL формата:
`https://notion.so/oauth/authorize?...` (или `api.notion.com/v1/oauth/authorize?...`).

### Шаг 3. Передай URL пользователю — ОСТАНОВИСЬ

Выведи в чат **ТОЛЬКО это**:

```
Ruslan, авторизация Notion:
1. Открой этот URL в браузере:
   <URL>
2. Авторизуйся в Notion (выбери workspace где лежат Command Center, Банк идей, Daily Log).
3. После редиректа браузер откроет страницу с callback URL (может быть localhost или error-page — не важно). Скопируй ВЕСЬ callback URL полностью.
4. Вставь callback URL сюда в чат.

Жду.
```

Не переходи дальше пока Ruslan не пришлёт callback URL.

### Шаг 4. Complete authentication

Когда Ruslan пришлёт callback URL — извлеки из него `code` параметр и вызови:
```
mcp__notion__complete_authentication
```

С `callback_url` или `code` как аргумент (смотри сигнатуру инструмента через
`/mcp` или `?`).

**При ошибке:** сообщи Ruslan'у точный error message + предложи попробовать заново
(`mcp__notion__authenticate` заново, новый URL).

### Шаг 5. Sanity checks (три проверки)

#### 5.1 Query маленькой DB

```
mcp__notion-query-database-view
  id: collection://30a24963-33bf-8005-817a-000beb10bcd4
  limit: 1
```

Expected: объект с 1 record. Title записи — что-то похожее на
`"📅 YYYY-MM-DD — План работ на день"`.

#### 5.2 Fetch известной страницы

```
mcp__notion-fetch
  id: 3442496333bf818184a1fbc3108b38cb
```

Expected: title = `"📜 Манифест: как мы строим систему"`.

#### 5.3 Query Банк идей

```
mcp__notion-query-database-view
  id: collection://bf0e9a11-0e6f-4717-9ae5-e19f9a096ce7
  limit: 5
```

Expected: 5 идей. Запомни `total_count` или `has_more` — если `has_more: true`
и у объекта есть `next_cursor`, значит pagination работает (это критично для
Фазы α.1 где будем выгружать все 650+).

### Шаг 6. Отчёт в чат

Формат (≤10 строк):

```
Notion MCP status:

[x] /mcp: notion connected
[x] Auth flow: OK
[x] Test 1 — DailyLog query: OK (sample: "📅 YYYY-MM-DD — …")
[x] Test 2 — Manifest fetch: OK (title: "Манифест…")
[x] Test 3 — Банк идей query: OK (5 записей получено, has_more=true, pagination ok)

Approx total ideas в Банке (по first page + has_more signal): ~XXX

Ready for full extraction. 
Ruslan: вставляй следующий trigger (prompts/notion-full-extraction-2026-04-16.md).
```

Если одна из проверок упала — SAFE-SAVE (git commit SAFE-SAVE + push) +
сообщи точный error. Не продолжай.

## Безопасность

- Ничего кроме `/mcp` + `mcp__notion-*` в этой задаче не запускай.
- Не трогай wiki/, projects/, agents/, dashboard/.
- Никаких commits в этой задаче — только if SAFE-SAVE (единственный коммит
  для фиксации scratchpad-заметок при ошибке).

## Возможные сбои и реакции

| Сбой | Реакция |
|------|---------|
| `mcp__notion__authenticate` не существует | Сообщи Ruslan: "Tool не найден, нужно обновить MCP server или проверить настройки. Проверь `~/.config/claude/claude.json` или эквивалент — возможно notion MCP не прописан." |
| OAuth URL не открывается у Ruslan | Попроси скопировать URL, открыть в другом браузере |
| Callback URL содержит `error=access_denied` | Сообщи Ruslan что он не дал доступ; заново `authenticate` |
| Test 1-3 дают 401 / `unauthorized` | Auth не прошла; заново с Шага 2 |
| Notion workspace другой (нет доступа к Command Center) | Сообщи Ruslan: "Выбран не тот workspace. Нужен тот где лежит Command Center `3322496333bf8161b6d3ea789d039356`. Заново `authenticate`." |

Старт: сейчас. Pull → /mcp → далее по шагам.
