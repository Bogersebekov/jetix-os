---
type: review
role: critic
chat: 1
parallel-with: [2, 3, 4]
created: 2026-04-18
status: complete
reviewer-model: Opus 4.7 (1M context)
source-document: SYSTEM-DESIGN-HUMAN.md v1-beta-2026-04-18
support-documents:
  - ARCHITECTURE-CURRENT.md
  - design/NOTION-MIGRATION-PLAN.md
  - reports/architecture-inventory-2026-04-16.md
---

# Review: Weaknesses of SYSTEM-DESIGN-HUMAN v1-beta-2026-04-18

> Критик / Адвокат дьявола. Независимый взгляд — без связи с оптимизатором /
> инженерами / синтезатором. Презумпция виновности: любая архитектура виновна
> пока не доказана устойчивость.

---

## Executive Summary

SYSTEM-DESIGN-HUMAN v1-beta — это прозрачный, хорошо структурированный документ.
Он **честно** обозначает ограничения (beta-first, полуручной режим, отложенные
вопросы). Но как основа для перевода на архитектурный язык он содержит критичные
слабости, которые **не адресуются** оговоркой "это v1-beta".

**Пять главных рисков:**

1. **Ruslan как SPOF — незакрашиваемый.** §5.4 + §5.6.6 + §2.4.1 + §3.1 + §4.0
   складываются в систему, которая **физически не выживает без Ruslan'а** более
   24–48 часов. Это не риск отказа инструмента — это **проектный выбор** (все
   решения через него). Документ не показывает способа пройти 2-недельный
   offline Ruslan'а без деградации до нуля.

2. **Конфликт "чистота — без автоматики".** §4.0 требует "чистоты как на GitHub".
   §5.1 запрещает автоматику. Следовательно, **вся дисциплина ложится на Ruslan'а**
   при 4-5 часах рабочего дня. В реалиях 25+ папок, 13 компонентов, 9 типов edges,
   ~30 заметок/день — это математически невыполнимо. Что-то будет заброшено
   первым; документ не описывает **что именно** и как это контролируется.

3. **"12 агентов" — абстракция на фикции.** Inventory gap #1 показал:
   6 mailbox'ов пусты, 6 только с тестовым трафиком. SYSTEM-DESIGN-HUMAN §3.2.1
   "честно" называет это "центральным мега-Claude, входящим в роли" — но дальше
   §3.2.2 + §6.1.13 возвращаются к "каждая роль = свой KB + strategies.md",
   противореча самому себе. v1-beta **переименовывает** проблему, а не решает её.

4. **Метрики измеряют не то.** §2.3 даёт 2 out-of-system метрики (200 контактов,
   $50K) + 1 субъективную ("не занимаюсь ерундой"). Ни одна не измеряет
   **работает ли система как система**. $50K можно достичь **вопреки** Jetix OS;
   $50K можно не достичь **несмотря** на отлично работающий Jetix OS. Метрика
   работает как прокси, а прокси шумит.

5. **v1-beta цементирует архитектуру под одного пользователя, обещая 100+ через
   год.** §1.6 обещает 100+ пользователей через 1 год. §1.5 обещает "быструю
   перестройку". Но архитектура v1-beta (§4.1 25+ папок, §6.1 13 hardcoded
   компонентов, §3.2 single Claude session, §6.1.9 3 hardcoded CRM баз) —
   **hardcoded для одного Ruslan'а**. Каждое архитектурное решение v1-beta
   создаёт технический долг для multi-user сценария.

Кроме этих пяти — 13+ категорий конкретных слабостей ниже. Всего **67 конкретных
проблем** зафиксированы с attribution.

---

## 1. SPOFs (Single Points of Failure) — 11 проблем

### 1.1 Ruslan как человеческий SPOF

**Проблема.** §5.4 "любой агент с проблемой → сразу Ruslan". §5.6.6 "Ruslan
offline → система не продолжает работать". §2.4.1 "стратегические решения всегда
за Ruslan'ом". §1.9 "founder-operator, всё сразу". Суммарно: **система не
работает без Ruslan'а физически**.

**Сценарий провала.** Ruslan простудился — 3 дня offline. Accumulated:
- 30+ UNCLEAR tasks в bucket (3 дня × 10 задач/день)
- inbox/* growing
- /plan-day + /close-day не запущены 3 дня
- strategic documents не обновлены
- Approvals в очереди (статьи, outreach, решения)

При возвращении Ruslan тратит 1.5 дня на разбор. Чистая потеря: 4.5 дня.
При стандартном больничном 2 недели — система в полной стагнации.

**Каскад.** → недельные/месячные ритуалы пропускаются → стратегические документы
устаревают → агенты работают без обновлённого context → выход ухудшается.

**Ссылки:** §3.1.4, §5.4, §5.6.6, §2.4.1, §7.1.1.

**Почему критично:** документ **не предусматривает** delegate / acting / policy-default /
sleep mode. "Deputy mode" не существует. §7.1.1 "роль ментора + экспертов" —
но менторы не уполномочены принимать операционные решения в системе.

### 1.2 Central Claude Code session как SPOF

**Проблема.** §3.2.1 — "один центральный Claude Code, с которым Ruslan
взаимодействует большую часть времени. Знает контекст глубоко. Умеет входить в
роли". Если сессия падает (crash, network, API limit) — **весь контекст теряется**.

**Сценарий.** Weekly review (§5.5) — 2-3 часа в одной сессии. В середине
обсуждения — Claude Code crashes / API 529. Ruslan возвращается, перезапускает —
**нет способа восстановить 90-минутный контекст**. §5.6.4 говорит "стоп, не
продолжать наугад" и перезапуск, но не описывает **что передаётся** новой сессии.

**Каскад.** → session unreliability → Ruslan избегает длинных сессий → не делает
weekly review глубоко → стратегические ритуалы деградируют.

**Ссылки:** §3.2.1, §5.5, §5.6.4, §6.1.13 (где обещано "контекст сохраняется,
агент умнеет").

### 1.3 Anthropic API как SPOF (vendor lock в противоречие с §3.5.2)

**Проблема.** §3.5.2 заявляет: "система работает и БЕЗ AI ... Можно поставить
одного человека-оператора". Но §5.6.3 описывает поведение при API 529: "3 retry
с backoff → SAFE-SAVE → репорт". **Нет fallback на другого провайдера** (OpenAI,
Gemini, local Llama). Нет даже fallback на меньшую Claude модель
(§5.6.3 "Fallback на Haiku — **только по команде Ruslan'а**").

**Сценарий.** Anthropic меняет цены (×3). Или вводит region block для
Германии. Или закрывает API для private persons → система встаёт. Kay-принцип
нарушен.

**Каскад.** → все 12 агентов мёртвы → central Claude мёртв → только человек-оператор.
§3.5.2 декларирует это возможным, но **методология "один-оператор-без-AI"** нигде
в §4/§5/§6 не описана операционно.

**Ссылки:** §3.5.2 (обещание), §5.6.3 (факт: нет fallback).

### 1.4 VPS 100.99.156.28 как SPOF

**Проблема.** Всё серверное (voice-pipeline, фоновые процессы, серверный
Claude Code, Notion α-extraction tooling) живёт на одном Ubuntu 24 VPS. Нет
описания disaster recovery: hardware failure / provider downtime / аккаунт
заблокирован.

**Сценарий.** Hetzner / DigitalOcean блокирует IP за "подозрительную активность"
(high volume API calls = красный флаг у ряда провайдеров). Восстановление 24-72
часа. Весь voice-pipeline + серверный Claude недоступны.

**Каскад.** → voice-memos не обрабатываются → /ingest workflow blocked →
SYSTEM-DESIGN-HUMAN says §NOTION-MIGRATION §6.2 "сервер обрабатывает dumps".

**Ссылки:** §5 (не адресовано), §1.1 (упомянут только IP).

### 1.5 GitHub как SPOF

**Проблема.** §5.6.1 SAFE-SAVE pattern предполагает `git push origin main`. Если
GitHub недоступен, аккаунт suspended, или repo приватность нарушена — весь
sync-protocol между Windows Claude и серверным Claude сломан (NOTION-MIGRATION-PLAN
§6.3 "git как bridge").

**Сценарий.** GitHub outage 6 часов (случалось в 2020, 2023). На это время:
- Local Claude не может push dumps
- Server Claude не может pull + ingest
- Оба работают изолированно → merge conflict на reconciliation

**Каскад.** → offline coordination работа накапливается → при восстановлении
git merge conflicts (см. §5.6.7 "не резолвить автоматически") → SAFE-SAVE →
ожидание Ruslan'а.

**Ссылки:** §5.6.1, §5.6.7, NOTION-MIGRATION §6.3.

### 1.6 Git репозиторий как единая точка консолидации

**Проблема.** В одном репо живёт **всё**: wiki, strategies.md, system.md,
decisions/, projects/, CRM, daily-log, raw/ dumps. Corruption / accidental
force-push / compromised SSH-ключ — всё уязвимо в одной точке.

**Сценарий.** Ruslan случайно делает `git push --force` (§5.6.7 prohibit'ит это
для агентов, но не для Ruslan'а) → коллеги из будущего (другой Claude) теряет
decisions за последний месяц. Нет read-only замороженных snapshots.

**Каскад.** → data loss → нет audit trail кроме git reflog (который сам
ephemeral) → §7.2.6 "audit trail" отложен в v1-final.

**Ссылки:** §5.6.7, §7.2.6.

### 1.7 Obsidian vault на локальной машине

**Проблема.** Obsidian vault = wiki/ папка (ARCHITECTURE-CURRENT §2.5). Если
локальный vault поломался (disk, corrupt DB) — нет UI для Ruslan'а читать wiki
без клонирования.

**Сценарий.** SSD на Windows ноутбуке crashes. Restore из git = 1 час + переустановка
Obsidian + индексация vault (большая wiki — 10+ минут индекс). Это не критично
для работы, но §6.2.4 "Обсуждаем фокус дня с Claude, Claude подтягивает контекст"
предполагает доступ к wiki через Obsidian UI.

**Ссылки:** не адресовано в SYSTEM-DESIGN-HUMAN.

### 1.8 Claude Code CLI + MCP infrastructure

**Проблема.** Весь skill-механизм построен на Claude Code (Anthropic's product).
Если Anthropic меняет API / deprecates Task tool / изменяет MCP protocol — все
skills ломаются.

**Сценарий.** Anthropic релизит Claude Code 2.0 с breaking change в subagent spawn.
`.claude/agents/*.md` формат меняется. Миграция 12 агентов + 10 skills ≥ 1 неделя.

**Каскад.** → весь пайплайн мёртв на этот период → v1-beta "полуручной режим"
усугубляется до "полностью ручной".

**Ссылки:** CLAUDE.md §Tools (не адресовано в SYSTEM-DESIGN-HUMAN).

### 1.9 Windows + Antigravity IDE

**Проблема.** §context 0 CLAUDE.md: "работает через Antigravity IDE + Claude Code
на сервере". Antigravity — форк VS Code, нишевой продукт. Если Antigravity
прекратит развитие или сломается на новой версии Windows — Ruslan лишается
рабочего интерфейса.

**Сценарий.** Antigravity закрыт Google (или outsourced). Новая Windows 11 update
ломает совместимость. Ruslan переезжает на ванильный VS Code, но custom
Claude Code integration там настроен иначе. Неделя migration.

**Ссылки:** context 0 (не адресовано в SYSTEM-DESIGN-HUMAN).

### 1.10 Groq Whisper API

**Проблема.** §CLAUDE.md: voice pipeline → Groq Whisper. Если Groq падает /
rate-limits / меняет pricing — voice-memos не транскрибируются.

**Сценарий.** Groq rate-limits free tier. Ruslan записал 50 voice-memos за
неделю отпуска (§2.1.9 "обработка созвонов"). На возврате все 50 — backlog
transcribe. Fallback на whisper.cpp локально? Не упомянут.

**Ссылки:** §2.1.9 (обещает "быстрое извлечение") — но voice не описан как
SPOF-риск в SYSTEM-DESIGN-HUMAN.

### 1.11 Дисциплина Ruslan'а как SPOF

**Проблема.** §4.0 "чистота" + §5.1 "no automation" + §6.1.13 "агенты умнеют
через strategies.md updates" + §6.2.4 "daily drafts песочница + close-day
раскидывает" — **каждый пункт** опирается на **regular discipline Ruslan'а**.

**Сценарий.** Ruslan две недели в отпуске. Никто не делает:
- weekly review (§5.5)
- close-day (§6.2.4)
- /lint maintenance (§5.1 "только по команде")
- strategies.md обновления (§6.1.13)

После возврата система в drift state. Восстановление = 3-4 дня.

**Каскад.** → дисциплина декларирована как fundamental quality, но нет
automation compensation → single point of human-discipline failure.

**Ссылки:** §4.0, §5.1, §6.1.13, §6.2.4.

---

## 2. Каскадные сбои — 7 цепочек

### 2.1 Notion MCP → Daily Log mayhem

**Цепочка.** Notion MCP упал (inventory gap #2, случалось на 2026-04-16)
→ `/plan-day`, `/close-day`, `manager`, `inbox-processor`, `knowledge-synth`,
`personal-assistant`, `life-coach`, `sales-lead`, `strategist` теряют ключевую
функциональность → Daily Log в Notion не обновляется → фокус дня не трекается
в Notion (§3.1.1 "стратегическое управление = источник правды") → после N
дней offline Ruslan не помнит чёткую картину вчерашнего дня → §4.5.2 weekly
analytics работают на дырявом data.

**Ссылки:** inventory gap #2, §3.1.1, §4.5.2, §5.6.2.

### 2.2 API 529 → human backlog → context drift

**Цепочка.** Anthropic 529 rate-limit (frequent on Opus 4.x peak times)
→ §5.6.3 3 retry → SAFE-SAVE → ожидание Ruslan'а → если Ruslan offline,
tasks paused → каждый новый раз 529 → SAFE-SAVE → pile growing
→ при возврате Ruslan должен ре-инициализировать каждую приостановленную задачу
→ context потерян частично.

**Ссылки:** §5.6.3, §5.4, §5.6.6.

### 2.3 Git merge conflict → blocking everything

**Цепочка.** Local Windows Claude pushes raw/ dump. Одновременно server Claude
редактирует wiki/graph/edges.jsonl при /ingest. Push server fails, pull fails
(conflict на edges.jsonl) → §5.6.7 "НЕ резолвить автоматически, SAFE-SAVE, ждать
Ruslan'а" → весь /ingest pipeline blocked → весь Notion γ-migration blocked
→ весь sync между two-Claude bridge blocked.

**Ссылки:** §5.6.7, NOTION-MIGRATION §6.3.

### 2.4 Ruslan болеет 2 недели → system decay

**Цепочка.** День 1-3: UNCLEAR bucket accumulates. День 4-7: inbox/ backlog,
weekly review missed. День 8-14: monthly review missed, strategic doc stale.
Day 15: Ruslan возвращается. Backlog: 100+ items. Чтобы разобрать — 3-5 дней.
Пока разбирает — новые items входят. Queue never empties.

**Ссылки:** §5.5, §5.6.6, §2.1.9, §4.5.2.

### 2.5 strategies.md versioning → phantom rollback

**Цепочка.** §6.1.13 пункт 3: "каждое изменение создаёт новую версию, старые
архивируются, rollback всегда возможен". Но: где архив? Нет явной папки.
Если rollback делается через git revert, и коммит имеет mixed изменения
(system.md + strategies.md + wiki в одном commit) — `git revert X` ломает
несвязанные файлы → новые breakages → новые rollback → history поломана.

**Ссылки:** §6.1.13, CLAUDE.md git conventions (размытые).

### 2.6 /consolidate merge → wikilink rot

**Цепочка.** /consolidate решает что идея X = дубль идеи Y, merge. Все
wikilinks [[X]] теперь broken. /lint сигналит orphans. Агент использует
§2.1.8 "соединяет гипотезы ⇄ инструменты" — берёт broken link, ищет ничего.
Возвращает пустой результат. §4.4.1 writeback логгирует пустой ответ как
"no data found" → wiki ещё более разрежается.

**Ссылки:** §4.4.4, §5.1, ARCHITECTURE-CURRENT §2.6.

### 2.7 meta-agent dead → self-improvement loop dead

**Цепочка.** §6.1.13 пункт 5: "meta-agent анализирует feedback → предлагает
изменения strategies.md → Ruslan одобряет → внедрение". Inventory gap #4:
meta-agent в `permissionMode: plan`, никогда не делал audit. Следовательно
strategies.md не обновляется. §6.1.13 цикл улучшения — **мёртв на старте**.

Агенты не умнеют. Через 3 месяца v1-beta мы будем работать на тех же promptах
что и сегодня → improvement не происходит → §1.6 "3 месяца $50K" упирается в
stalled productivity.

**Ссылки:** inventory gap #4 + #9, §6.1.13.

---

## 3. Race conditions — 7 проблем

### 3.1 Concurrent writes to wiki/graph/edges.jsonl

**Проблема.** §4.4 writeback правила: "ответ создаёт новую связь → edge в
edges.jsonl". `/ingest` и `/ask` оба могут делать `append`. В POSIX `O_APPEND`
атомарно **только** для writes < PIPE_BUF (обычно 4096 bytes). Если edge-line
редкая длинная → partial write → corrupted JSONL.

**Сценарий.** Параллельно запущены Ruslan'ом `/ask` через Claude Code + Claude
Code на сервере делает `/ingest` batch. Обе добавляют edges. Одна edge-line
обрывается → `/build-graph` падает на malformed JSONL → communities не
перестраиваются → `/ask` работает на старых summaries → ответы устарели.

**Ссылки:** §4.4.2, ARCHITECTURE-CURRENT §2.6.

### 3.2 /ingest vs /consolidate

**Проблема.** /ingest создаёт новую идею X. /consolidate ровно в этот момент
решает что X' (старая) — дубликат Y и merge'ит X' в Y. Новая X создана, но
в edges.jsonl ссылается на X' (который больше не существует).

**Сценарий.** Ruslan запускает /ingest нового voice-memo. В этом же окне Claude
у Ruslan'а запустил /consolidate (§5.1 "по команде" — значит оба по команде).
Race: X создана, Y не содержит содержимого X (merge был до ingest завершился).

**Ссылки:** §4.4, §5.1.

### 3.3 Ruslan edits file + Claude Code Edits same file

**Проблема.** §6.2.4 "работаю через Claude Code + открыт Antigravity". Если
Ruslan руками отредактировал projects/quick-money/overview.md и одновременно
Claude через Edit обновляет тот же файл — **одна версия перезаписывает другую**
(зависит от порядка save). Нет file lock механизма.

**Сценарий.** Ruslan руками добавил decision "не работать после 20:00". Claude
через 30 секунд делает Edit на overview.md обновляя next_action. Claude не
перечитал файл — его Edit основан на stale content, decision потерян.

**Ссылки:** §6.2.4 (GitHub-style work — но без branching).

### 3.4 git conflict — §5.6.7 как hard blocker

**Проблема.** §5.6.7: "НЕ резолвить автоматически, SAFE-SAVE, ждать Ruslan'а".
В two-Claude bridge NOTION-MIGRATION §6.3 оба пишут в репо. Conflicts
неизбежны (edges.jsonl, index.md, log.md — всё shared).

**Сценарий.** Каждые 2-3 часа git conflict. Каждый раз SAFE-SAVE + ожидание.
Ruslan тратит 10 минут на resolve × 4 раз в день = 40 минут/день.
= 14% рабочего дня.

**Ссылки:** §5.6.7, NOTION-MIGRATION §6.3.

### 3.5 Notion writes vs wiki writes during γ-migration

**Проблема.** NOTION-MIGRATION фаза γ — полный extract за "2-5 дней". В этот
период Ruslan может добавить новую идею **в Notion** (если вдруг забыл что
мигрируем). Или забросит voice-memo, который transcribed → wiki/. Новые
создания в обеих системах → **двойная правда**.

**Сценарий.** 2026-04-30 Ruslan на встрече добавил idea в Notion Банк идей
(старая привычка). 2026-05-02 γ-migration уже прошла по Банку идей. Новая idea
пропущена. Отчёт `/verify-migration` считает — всё ОК (count before=after).

**Ссылки:** NOTION-MIGRATION §5 γ, §7 критерии декомиссии.

### 3.6 shared/state/*.json concurrent mutations

**Проблема.** focus.json, priorities.json, kanban.json — читают и dashboard,
и central Claude, и manager (inventory §2.3). Нет lock. Все write операции
rewrite whole JSON file.

**Сценарий.** Ruslan через dashboard добавил task X в kanban. Сразу же Claude
через plan-day обновляет kanban.json через Write. Task X потерян.

**Ссылки:** ARCHITECTURE-CURRENT §2.3 (не адресовано в SYSTEM-DESIGN-HUMAN).

### 3.7 Staleness during long "натягивания" (§4.5.2)

**Проблема.** §4.5.2: "натягивание" = месячная аналитика. Агент читает snapshot
wiki, думает 1-2 часа. Пока думает — другие операции меняют wiki. Результат
анализа stale на момент выдачи.

**Сценарий.** Monthly review запущен 01.05.2026 в 18:00. Агент читает 557
wiki pages, строит model. 20:30 выдаёт отчёт. За эти 2.5 часа Ruslan добавил
10 новых pages через voice-memo pipeline. Отчёт не учитывает их.

**Ссылки:** §4.5.2.

---

## 4. Дрейф данных (data drift) — 8 точек

### 4.1 Windows wiki vs server wiki

**Проблема.** NOTION-MIGRATION §6.3: "Разные папки (raw/ = local-only,
wiki/ = server-only mostly)". Слово **mostly** — слабое место. Ruslan может
открыть Obsidian на Windows, что-то править → git push → server pull
→ конфликты.

**Ссылки:** NOTION-MIGRATION §6.3, §5.6.7.

### 4.2 Notion (legacy α→γ) vs wiki (текущая)

**Проблема.** §4.6 + NOTION-MIGRATION §5: Фаза α завершена (199 RELEVANT
ingested). Фаза γ не началась. Между α и γ — **многонедельная** двойная жизнь.
В Notion есть 590 не-migrated ideas. Ruslan продолжает **пользоваться**
Notion или нет? SYSTEM-DESIGN-HUMAN не уточняет момент отказа от Notion как
input source.

**Сценарий.** Ruslan добавил idea в Notion 2026-04-25. Фаза γ 2026-04-28..05-05.
Синхронизация? Ручная? Агент заметит?

**Ссылки:** §4.6, §7.1 (Notion migration), NOTION-MIGRATION §5.

### 4.3 strategies.md — источник правды неясен

**Проблема.** §6.1.13: "strategies.md фиксирует когда X → делай Y". Но:
- Кто имеет write-доступ? Сам агент? meta-agent? Ruslan?
- Где версионирование (§6.1.13 пункт 3 обещает, но не указывает путь)?
- Если два агента хотят обновить один strategies.md (shared learning) — как?

Inventory gap #9: все 12 strategies.md пусты → никакого truth нет на сегодня.
Когда наполнятся — §6.1.13 не говорит **каким процессом** они обновляются.

**Ссылки:** §6.1.13, inventory gap #9.

### 4.4 shared/state/*.json vs реальное состояние работы

**Проблема.** focus.json говорит "focus=X". Но Ruslan работает над Y (импульс).
`/plan-day` работает на focus.json → выдаёт план под X → не соответствует
реальности дня.

**Сценарий.** Утром focus.json = "sales-outreach". Ruslan в 10:00 узнаёт про
важный bug в wiki и 4 часа чинит. focus.json так и говорит "sales". Close-day
пытается связать вчерашний sales-activity — пусто. Ритуал разорван.

**Ссылки:** ARCHITECTURE-CURRENT §2.3, §6.2.4.

### 4.5 decisions/ vs wiki/claims/

**Проблема.** §6.1.14 "решение — отдельная сущность, append-only в decisions/".
wiki/claims/ существует (ARCHITECTURE-CURRENT §2.2) — "утверждения с evidence".
Часто решение = claim (e.g. "мы делаем value-based pricing" — и решение, и claim).
Дубль. Какая копия актуальна при update?

**Ссылки:** §6.1.14, §4.2.4, ARCHITECTURE-CURRENT §2.2.

### 4.6 daily-log vs strategy/life/weekly

**Проблема.** daily-log/{date}.md содержит "на завтра". strategy/life/W17-weekly.md
содержит план на неделю. Если they contradict — какая правда? Нет policy.

**Сценарий.** Вечер понедельника: close-day говорит "завтра фокус X" (plan для
вторника). Но weekly.md для W17 говорит "вторник — фокус Y". Утром вторника
plan-day читает оба — что выбрать?

**Ссылки:** §6.2.4, §6.1.8.

### 4.7 tasks/master.md vs projects/{x}/tasks.md

**Проблема.** §6.1.2: "общий пул + пул на каждый проект". §4.1 тоже. Но как
синхронизируются? Если в master.md отредактировали, автоматически в проект?
В проекте — обратно в master? Ручками?

**Сценарий.** Task "call Anton" в master.md (personal). Через неделю стал
связан с проектом jetix-evolution. Перенос в projects/jetix-evolution/tasks.md?
Или остаётся в master? Дубль? Теряется?

**Ссылки:** §6.1.2, §4.1.

### 4.8 strategy/life/yearly vs projects/{x}/strategy

**Проблема.** §6.1.8 два уровня: life + project. Life-level yearly говорит
"focus на $50K до 30.06.2026". Project "jetix-evolution/strategy.md" говорит
"priority P3". Противоречие: Ruslan **заявил** как life-level что всё ради
$50K (sub §1.7), но его основной проект улучшения системы — P3. Который
prevails? Нет арбитра.

**Ссылки:** §1.7, §6.1.8, CLAUDE.md "Проекты (8 активных)".

---

## 5. Накопление мусора — 10 источников

### 5.1 Raw files unprocessed

**Проблема.** raw/voice-memos/ — inventory confirms: 0% transcribed на
2026-04-16. raw/notion-ideas/ частично. raw/articles/, raw/web/ — не упомянуты
в сколько-нибудь обработанном виде.

**Без автоматики (§5.1)**: Ruslan должен руками триггерить transcribe.py + ingest
для каждого voice-memo. Если неделю пропустил — 20-30 voice-memos в очереди.

**Ссылки:** ARCHITECTURE-CURRENT §2.1, §5.1, §5.5 (ритуалы только weekly+).

### 5.2 UNCLEAR bucket без stale detection

**Проблема.** §5.6.5: "не гадать — ставить в bucket UNCLEAR, ждать ответ". Но:
- Где технически живёт этот bucket? Отдельный файл? inbox/unclear/?
- Какой retention? Если UNCLEAR задача 2 месяца ждёт — стейл, контекст забыт.
- Как маркируется priority?

**Ссылки:** §5.6.5 (декларация), нет spec где и как.

### 5.3 Orphan страницы после renames

**Проблема.** §4.1 slug stability decl'ed для wiki/* после γ. Но до γ (pilot,
quick α) — slug может меняться (pilot showed this). В результате [[X]] ссылки
становятся broken. /lint отчёт показывает но не фиксит.

**Ссылки:** §4.1, §7.2.2 (отложен), ARCHITECTURE-CURRENT §2.2 lint reports.

### 5.4 Старые версии промптов агентов

**Проблема.** §6.1.13 пункт 3: "старые архивируются". ARCHITECTURE-CURRENT §2.3:
baseline.md = immutable, system.md = рабочая. Но обе одинаковы сегодня
(inventory gap #6). Если агент эволюционирует — system.md растёт. baseline.md
остаётся. Где версии между? Коммиты? Тогда baseline.md не нужен.

**Ссылки:** §6.1.13, ARCHITECTURE-CURRENT §2.3, inventory gap #6.

### 5.5 Untested гипотезы в hypotheses/active.md

**Проблема.** §4.2.5 + §6.1.4: гипотеза тестируется → validated или archive.
Нет timeout. Если гипотеза 6 месяцев "active" — stale. Никто не flag'ит.

**Сценарий.** Ruslan в марте формулирует гипотезу "партнёрская программа Jetix
Corporation начнётся через 1 год". В июне она неактуальна (стратегия сдвинулась).
Но остаётся в active.md, влияет на аналитику §4.5.2.

**Ссылки:** §4.2.5, §6.1.4 (no timeout mechanism).

### 5.6 Daily log drafts — растущая папка

**Проблема.** §4.1 `daily-log/drafts/YYYY-MM-DD-{topic}.md` + §6.2.4 "песочницы".
Каждый день несколько drafts. Через 6 месяцев = 500+ drafts. Ротация? Archive
old? Ничего.

**Ссылки:** §4.1, §6.2.4, no retention policy.

### 5.7 Decisions log — append-only without index

**Проблема.** §6.1.14: "append-only. Каждое решение — дата, контекст, ...".
Через 2 года — огромный файл. Как найти "решение про pricing"? Full-text grep.
Если 50 decisions касаются pricing в разном контексте — неразличимо.

**Ссылки:** §6.1.14, §1.12 (ранее highlighted).

### 5.8 Tasks `blocked` forever

**Проблема.** §6.2.2: "backlog → today → in-progress → done / blocked". Если
blocked задача ждёт 3 месяца — stale. Нет auto-sunset.

**Ссылки:** §6.2.2.

### 5.9 Dashboard data без retention

**Проблема.** ARCHITECTURE-CURRENT §2.3: shared/state/metrics/agent-performance,
ab-tests, feedback. Если агенты начнут говорить — метрики растут. Нет policy.

**Ссылки:** ARCHITECTURE-CURRENT §2.3 (не адресовано в SYSTEM-DESIGN-HUMAN).

### 5.10 Orphan agent definitions

**Проблема.** Inventory §3.3 #10: "agents/content-team/, research-team/,
sales-team/, _shared/" — orphan папки, не упомянуты в CLAUDE.md roster и в
SYSTEM-DESIGN-HUMAN. Копится legacy.

**Ссылки:** inventory gap #10, §3.2.2 (12 ролей — но что с orphan 4 папками?).

---

## 6. Agent orchestration — 6 проблем

### 6.1 "12 агентов" — self-deception

**Проблема.** §3.2.1 decl'ed "центральный Claude Code, входит в роли". §3.2.2
decl'ed "каждая роль = тематическая специализация + собственная база знаний".
Противоречие: **если один Claude session входит в роли** — у него **нет**
собственной базы, он читает shared wiki с фильтром через niche symlinks. Но
"умеет входить и выходить" не объясняет как strategies.md **одного** агента
отличается от strategies.md **другого**, если writer — один central Claude.

**Сценарий.** Central Claude в роли sales-lead читает strategies.md для sales,
пишет update. Затем в роли inbox-processor читает свой strategies.md — но уже
контаминирован контекстом (residual memory в сессии). Изоляция ролей не гарантирована.

**Ссылки:** §3.2.1, §3.2.2, §6.1.13.

### 6.2 Claude "забыл" контекст → перезапуск = полная потеря

**Проблема.** §5.6.4: "сразу стоп, не продолжать наугад. Ruslan корректирует или
перезапускает сессию". При перезапуске — **весь** живой контекст теряется.
Scratchpad.md сохраняет working memory, но rich context (то что Claude помнит
из последних 20 turns) — нет.

**Сценарий.** 90-минутная diктовка Part 5 SYSTEM-DESIGN-HUMAN. Claude забыл
важную предыдущую деталь. Перезапуск. Новый Claude читает весь документ заново
(30K tokens), но не знает что уже **обсуждалось** в 90-минутной диктовке.
Ruslan должен пересказать на словах.

**Ссылки:** §5.6.4, §6.1.13 "контекст не забывается" — декларация без механизма.

### 6.3 Hub-and-spoke — миф в документе

**Проблема.** CLAUDE.md "Hub-and-spoke: subagents report to department Lead".
ARCHITECTURE-CURRENT §3.1 фактически: "inbox-processor шлёт в manager напрямую",
"Sales Researcher/Outreach в Sales Lead OK, но hub-and-spoke в Brain не работает".
SYSTEM-DESIGN-HUMAN §3.2 не упоминает эту расхождение, продолжая обещать роли
с каналами коммуникации.

**Ссылки:** CLAUDE.md, ARCHITECTURE-CURRENT §3.1, §3.2 (не адресовано).

### 6.4 Subagent Task spawn — не multi-agent team

**Проблема.** Task tool spawn'ит **новую** Claude session как subagent. Эта
session:
- НЕ имеет доступ к central Claude context
- Не может ping-pong (one-shot)
- Возвращает result в central session, но не пишет в mailbox
- После completion — контекст умирает

**Сценарий.** Ruslan запускает через Task "sales-researcher для ICP X". Subagent
делает research. Возвращает результат. Central Claude складывает в
`shared/knowledge/research-summaries/`. **sales-researcher не помнит** что делал
— следующий Task spawn начинает с нуля.

→ §6.1.13 "агент умнеет" для subagent'ов через Task = невозможно. Только через
strategies.md (которая shared). Но обновляется она кем? meta-agent'ом (dead по
inventory).

**Ссылки:** §3.2.1, §6.1.13, inventory gap #4.

### 6.5 strategies.md не обновляется

**Проблема.** Inventory gap #9: все 12 strategies.md пустые. Через 3 дня после
миграции (на 2026-04-16) = никакого накопления. SYSTEM-DESIGN-HUMAN §6.1.13
обещает "наполняются по мере работы" — но **кем именно**?
- Самим агентом? После каждой задачи? Когда конкретно?
- meta-agent? Он dead.
- Ruslan'ом вручную? При 4-5 часах работы — нет бюджета.

**Ссылки:** inventory gap #9, §6.1.13, §5.1 (automation prohibited).

### 6.6 Масштаб не поддерживается single session

**Проблема.** §1.6 "1 год — 100+ пользователей". Single Claude session per user
× 100 = 100 параллельных sessions. API cost: Opus 4.6 input ~ $15/M tokens ×
100 × 200K context ≈ $300 per hour. Не обсуждается.

**Ссылки:** §1.6, §3.2.1.

---

## 7. Memory / context limits — 6 проблем

### 7.1 Context budget underestimated

**Проблема.** SYSTEM-DESIGN-HUMAN 2000 строк ~50K tokens. + ARCHITECTURE-CURRENT
330 lines ~8K. + NOTION-MIGRATION 525 ~13K. + CLAUDE.md ~6K. + wiki/index.md
165 ~4K. = ~81K **базового** контекста до работы.

При реальной работе + relevant wiki pages (say 15 × 2K = 30K) + scratchpad +
history conversation + tool schemas = **150K+ на сессию**. Opus 4.6 context:
200K (или 1M в extended). При 1M — OK. При 200K — Tight.

**Ссылки:** §6.1.13 "контекст сохраняется, агент умнеет" без бюджета.

### 7.2 Что загружать — без формализованного selector

**Проблема.** §agents/{id}/niche symlinks — фильтр. Но:
- Niche "sales" содержит ~40 страниц × 2K = 80K → четверть всего бюджета.
- Нет re-ranker (RAG quality).
- Как агент решает "какие 5 страниц релевантны"? §/ask описано через
  HippoRAG edges, но для "входа в роль" — не описано.

**Ссылки:** ARCHITECTURE-CURRENT §2.3 (niche symlinks факт), §/ask (ARCHITECTURE
§2.6), §3.2.2 (роли = KB среза — как отбирать?).

### 7.3 Pollution от /ask returning irrelevant

**Проблема.** ARCHITECTURE §2.6: `/ask` отбирает 5-15 pages. Если отбор noisy
(say 5 релевантные + 10 полу-релевантные) — Claude тратит tokens на шум.
Ответ падает в качестве.

**Ссылки:** §/ask (ARCHITECTURE §2.6), §2.1.8 (обещает 95%-покрытие — какой
механизм гарантирует?).

### 7.4 Central Claude session context grows over day

**Проблема.** Утренний ритуал (§5.5) — context X. Рабочая сессия (5.2) — +Y.
Вечерний ритуал — +Z. Всё в одной session? Накопление к вечеру 500K+.

Если session рестарт между ритуалами — §6.1.13 "контекст не забывается" не
выполняется: новая session не помнит утра.

**Ссылки:** §5.5, §6.1.13.

### 7.5 Sub-agents без memory

**Проблема.** Task tool spawn — ephemeral. По completion context умирает.
Subagent не имеет persistent memory между invocations. §6.1.13 обещает
per-agent memory 5 layers — но это только для 12 main agents, не для Task
subagents.

**Ссылки:** §3.2.1, §6.1.13.

### 7.6 No mention of prompt caching

**Проблема.** Anthropic offers cache_control for repeated prompts. CLAUDE.md
+ system prompts + wiki/index повторяются каждой session. Без caching — 10×
cost + 10× latency. Не упомянуто в SYSTEM-DESIGN-HUMAN.

**Ссылки:** не адресовано в §3.2.

---

## 8. Human-in-loop bottleneck — 7 проблем

### 8.1 Approval load math

**Проблема.** §5.4 "любой агент → сразу Ruslan". Подсчёт:
- 12 агентов × 1 escalation/day = 12
- UNCLEAR bucket ~10-15/day
- §2.4.2 article approvals — say 5/week
- §2.4.2 partner message approvals — say 10/week
- γ-migration batch approvals (during migration) — 5/week
- /verify-migration checks
- strategies.md updates (§6.1.13)
- /lint orphan decisions
- weekly/monthly ritual review

Итого: ~30 decision-points/day × 5 минут = 2.5 часа/день **только на approvals**.
Из 4-5 часов рабочего дня → 50-60% съедается approvals. Остаётся 1.5-2 часа
на **стратегическую работу**.

**Ссылки:** §5.4, §2.4, §5.6.5, §6.1.13.

### 8.2 Статьи approval — explicit load

**Проблема.** §2.4.2 "статьи проходят проверку". Если система genererates
3-5 статей в неделю (§2.1.3 "контент и интеллектуальные артефакты" — должно
быть output'ом), каждая 1500 слов × 10 мин read = 50 минут/неделя. Не огромно,
но на background всего остального.

**Ссылки:** §2.4.2, §2.1.3.

### 8.3 Outreach approval — scale issue

**Проблема.** §7.3 "50+ контактов через год" = ~1 contact/week. Если
sales-researcher находит 10 leads/week, Ruslan одобряет 10% → 1 контакт
валидированный. Но scanning 10 leads × 3 min = 30 min/week. Manageable.
Проблема при scaling: для 200 контактов/год нужно 200 leads/week → 10 hours/week
на lead review.

**Ссылки:** §2.1.5, §7.3 contextual goals.

### 8.4 Backlog pathology

**Проблема.** Ruslan offline 3 дня → 30+ UNCLEAR + 10+ approvals = 40 items.
Разбор 40 × 5 минут = 3.3 часа. На **следующий** день Ruslan только разбирает.
Новые 30+ items входят → backlog never empties → система превращается в
"входящий вайб-инбокс" (§1.8 critic предпосылка verified).

**Ссылки:** §5.4, §5.6.5, §5.6.6, §1.8.

### 8.5 Approval asymmetry: agent fast, human slow

**Проблема.** Агент может произвести 100 items/час. Ruslan одобряет 5-10/час
(read + think). Asymmetry 10:1 → queue builds. Нет back-pressure (агент не
приостанавливается когда queue длинная).

**Сценарий.** Sales-outreach находит 50 leads за 30 минут. Ruslan в этот день
только 2 часа на approvals → одобрил 20. 30 висят. Следующий день —
еще 50 новых + 30 старых. Queue lag увеличивается.

**Ссылки:** §2.1.5, §5.4.

### 8.6 Нет "policy default" механизма

**Проблема.** §2.4.1 "все стратегические решения Ruslan" — жёстко. Но multiple
decisions повторяются по шаблону. Например: "ок на этот типа leads", "ок на
outreach если X". Без policy default механизма — каждое решение принимается
заново. Время тратится на known patterns.

**Ссылки:** §2.4, §5.4 (no mention of decision precedents / policies).

### 8.7 Escalation path flatter чем нужно

**Проблема.** §5.4 "любой агент с проблемой → сразу Ruslan". Одноуровневая
эскалация. Для 12 агентов при активной работе — 12 каналов к Ruslan одновременно.
В multi-user future (§1.6 100+ users) — architecture уже ограничивает.

**Ссылки:** §5.4 (one-level escalation, no department lead mediation).

---

## 9. Дисциплина чистоты — 7 проблем

### 9.1 Чистота vs no automation — математически несовместимо

**Проблема.** §4.0 "чистота как на GitHub". §5.1 "no automation".
Ruslan 4-5 часов/день.

Требования чистоты:
- frontmatter review для каждой новой страницы
- naming convention check
- slug stability
- /lint review еженедельно
- /consolidate maintenance
- orphan detection
- stale tagging
- migration бэклог

При 30 новых заметок/день (§2.1.8 система превращает всё в идеи) + UNCLEAR +
approvals — **не остаётся времени** на maintenance.

**Ссылки:** §4.0, §5.1, §6.1.13.

### 9.2 25+ папок — cognitive load

**Проблема.** §4.1: projects/, strategy/, decisions/, tasks/, ideas-pool/,
hypotheses/, tools-catalog/, wiki/ (9 entity subdirs), reflection/, health/,
crm/ (3 subdirs), daily-log/, raw/, inbox/, agents/, comms/, shared/, reports/,
tools/, scripts/, docs/adr/, prompts/ = **25+ top-level directory decisions**.

Для каждой заметки mental load: "в какую из 25+ папок?". Категории размыты
(§10 next section). 30 заметок/день × 30 sec decision × 25 choices mental =
15 минут/день на routing.

**Ссылки:** §4.1 (визуализация 25+ папок), §1.10 размытые границы.

### 9.3 13 компонентов — через месяц забыт

**Проблема.** §6.1 "13 групп компонентов: проекты, задачи, идеи, гипотезы,
ресурсы, инструменты, wiki (общая + локальные), стратегические доки,
CRM, Daily Log, рефлексия, здоровье, решения, агенты". На месяц работы
**Ruslan забудет точные правила**: "hypothesis идёт в hypotheses/active.md
или в projects/{x}/hypotheses.md?". → puts in wrong place → drift.

**Ссылки:** §6.1 13 subsections.

### 9.4 What gets dropped first (predictions)

**Проблема.** Если бюджет дисциплины 100%, и требования 150% → 50% дропнется.
Что именно?

1. **Weekly maintenance /lint + /consolidate** (§5.1 по команде, не ритуал).
   Ruslan не будет помнить каждый понедельник.
2. **strategies.md updates** (§6.1.13). meta-agent dead, Ruslan не сделает
   руками.
3. **Daily log drafts cleanup** (§6.2.4). Будут копиться.
4. **Decisions log review** (§6.1.14). Через 3 месяца никто не читает.
5. **Gitignore discipline** — новые temporary files не исключены.

**Ссылки:** §5.1, §6.1.13, §6.2.4, §6.1.14.

### 9.5 Ритуалы only-on-command → пропуски

**Проблема.** §5.5 "все ритуалы запускает Ruslan, никаких cron'ов на v1-beta".
Weekly/monthly ритуалы критичны для стратегического alignment. Если Ruslan
забыл запустить weekly review — strategy drifts.

**Ссылки:** §5.5, §6.2.3.

### 9.6 meta-agent + Ruslan маintenance overlap

**Проблема.** §6.1.13 self-improvement cycle: "meta-agent анализирует feedback
→ Ruslan одобряет". Оба делают maintenance. Но meta-agent в plan-only mode
(inventory gap #4). → Ruslan тащит всё сам.

**Ссылки:** §6.1.13, inventory gap #4.

### 9.7 Slug stability — декларация без механизма

**Проблема.** §4.1 пункт 2 "даты YYYY-MM-DD". Но slugs (имена) страниц могут
меняться при rename. NOTION-MIGRATION §приложение пункт 6 "Slug stability —
после Фазы γ slug'и не меняются". ОК, но до γ меняются → broken links.

**Ссылки:** §4.1, NOTION-MIGRATION §приложение 6.

---

## 10. Размытые границы между компонентами — 9 пар

### 10.1 Идея (6.1.3) vs Гипотеза (6.1.4)

Идея — "сырая мысль / гипотеза / вариант". Гипотеза — "тестируемая". Идея
формулируется как if-then → гипотеза? Кто делает переход? Когда?

**Impact:** идеи застревают в ideas-pool. Или hypothesis без теста.

**Ссылки:** §6.1.3, §6.1.4.

### 10.2 Задача (6.1.2) vs Решение (6.1.14)

Задача "сделать X". Решение "что делать когда X". "Каждое утро делать зарядку" —
это задача (ежедневная), или решение (life-level)?

**Impact:** двойная классификация → inconsistent storage.

**Ссылки:** §6.1.2, §6.1.14.

### 10.3 Рефлексия (6.1.11) vs Wiki (6.1.7)

§6.1.11 "своя wiki рефлексии отдельная". Почему не в общей wiki с тегом
#reflection? Изоляция без explicit reason.

**Ссылки:** §6.1.11, §6.1.7.

### 10.4 Здоровье (6.1.12) vs Decisions Life-level (6.1.14)

§6.1.12 — отдельный отсек здоровья. §6.1.14 "здоровье — это решения другого
уровня, живёт в health/". Решение "спать до 7:00" — в decisions/ или в health/?

**Ссылки:** §6.1.12, §6.1.14.

### 10.5 overview.md vs strategy.md в проекте

§4.1 structure: projects/{slug}/overview.md + strategy.md. Содержимое
overview — "точка А/Б/ресурсы". Strategy — "ссылка на strategy/projects/{x}/".
Зачем два файла? overview → strategy с ссылкой на глобальный strategy/projects/?

**Ссылки:** §4.1.

### 10.6 ideas.md inside project + ideas-pool/inbox.md

§4.1 + §6.1.3. "Связана с проектом → в проект. Системная → pool". OK. Но идея
началась как системная → связалась с проектом → кто перемещает?

**Ссылки:** §4.1, §6.1.3, §4.2.3.

### 10.7 projects/{slug}/strategy.md + strategy/projects/{slug}/strategy.md

§4.1 "strategy.md — ссылка на strategy/projects/{x}/". Two files + symlink =
triple maintenance. Нарушение single-source-of-truth.

**Ссылки:** §4.1.

### 10.8 Resource "Инструменты" (1.2) vs tools-catalog/ (6.1.6) vs tools/ (scripts) vs .claude/skills/

§1.2 ресурс "Инструменты" (Claude Code, Antigravity, AI-сервисы).
§6.1.6 tools-catalog/ (карточка на каждый).
tools/ (scripts, Python).
.claude/skills/ (slash-commands).

**Пять** понятий "инструменты" накладываются. Куда идёт карточка "Claude Code"?

**Ссылки:** §1.2, §6.1.6, ARCHITECTURE-CURRENT §2.4, CLAUDE.md skills.

### 10.9 Agent vs skill vs subagent vs Task tool

§3.2.2 роли агентов. §5.2 skills. §Task tool subagent spawn. Когда Ruslan
говорит "сделай X", какой путь активируется? Документ не разграничивает.

**Ссылки:** §3.2.1, §3.2.2, §5.2.

---

## 11. Масштабирование через год — 6 барьеров

### 11.1 Multi-tenancy не архитектируется

**Проблема.** §1.6 "1 год — 100+ пользователей". v1-beta hardcoded:
- 12 agent definitions — shared (каждый user не имеет своего roster)
- wiki/ — shared namespace (private info mixed)
- shared/state/*.json — single point
- Notion IDs в CLAUDE.md — Ruslan's workspace

Multi-tenancy потребует **полной** реархитектуры: per-user wiki, per-user
agents, per-user state. Это не "небольшая доработка v1", это **v2**.

**Ссылки:** §1.6, §4.1 (hardcoded one-user paths).

### 11.2 "Быстрая перестройка" — маркетинг без имплементации

**Проблема.** §1.5 "быстрая перестройка — одно из ключевых качеств". Но
**механизм** не описан. Config? Templates? Что меняется на "researcher preset"?

Если реальная кастомизация = "rewrite CLAUDE.md + niches + agents" — это
**неделя** работы, не "быстро".

**Ссылки:** §1.5 (декларация), не supported by §4/§5/§6 имплементацией.

### 11.3 1-on-1 Ruslan ↔ Claude — не scales

**Проблема.** §3.2.1 "центральный Claude который знает контекст". Для 100 users
нужно 100 такх Claude sessions. API cost: Opus 4.6 ~$15/M input × 100 × 200K =
$300/hour per 100 users. Неадресовано.

**Ссылки:** §3.2.1, §1.6.

### 11.4 Git в main при 100 пользователях — disaster

**Проблема.** §CLAUDE.md + §6.2.4 "GitHub-style": main = main truth. Если 100
users пишут в main ежедневно → merge conflicts × 100 × daily = unmanageable.

**Ссылки:** §6.2.4, §5.6.7.

### 11.5 Human-in-loop × 100

**Проблема.** Если архитектура требует owner approval (§5.4) и у каждого user
свой owner — OK. Но §1.6 "Jetix Club — коллективное использование" предполагает
shared layers. Для shared layer один owner (Ruslan?) = 100× approval load.

**Ссылки:** §1.6, §5.4.

### 11.6 6 niches hardcoded

**Проблема.** §ARCHITECTURE §2.3: niches = [personal, business, sales, life,
tech, meta]. Для researcher/artist/etc — другие niches. v1-beta хардкодит.

**Ссылки:** ARCHITECTURE §2.3, §1.5 (обещает кастомизацию).

---

## 12. Decision logs — 5 проблем

### 12.1 No index — full-text grep

**Проблема.** §6.1.14 append-only log. "Найти решение через 6 месяцев?
Full-text grep. Дубли — как выявляются?" — ответ: никак формально.

**Ссылки:** §6.1.14.

### 12.2 Дубли решений в life + project

**Проблема.** "Не работать после 20:00" — life-level. Но актуально для
quick-money проекта (velocity). В двух местах → при update один остаётся
stale.

**Ссылки:** §6.1.14, §4.2.4.

### 12.3 Арбитр противоречий отсутствует

**Проблема.** Life-level decision "focus на здоровье" vs project decision
"max velocity до $50K". Кто prevails? Не указано.

**Ссылки:** §6.1.14 (no arbitration rule).

### 12.4 Versioning — не описан

**Проблема.** Решение принято, 6 месяцев позже условия изменились. Supersedes?
New decision with ref to old? Append-only формально → предыдущее решение
**существует** как факт, хоть и устарело.

**Ссылки:** §6.1.14 "append-only" без supersedes mechanism.

### 12.5 Decision vs claim (wiki/) — дублирование

**Проблема.** Многие decisions — это claims с evidence. wiki/claims/ + decisions/
— двойное хранилище. Какое использовать?

**Ссылки:** §6.1.14, ARCHITECTURE-CURRENT §2.2.

---

## 13. Notion migration — 5 рисков timing

### 13.1 Living SYSTEM-DESIGN-HUMAN блокирует γ

**Проблема.** β зависит от v1-beta HUMAN + migration rules. HUMAN = living doc
(§meta-section lifecycle). Если HUMAN меняется → rules меняются → γ ждёт.

**Ссылки:** NOTION-MIGRATION §5 фаза β, §meta-section lifecycle.

### 13.2 δ раньше timer — data loss

**Проблема.** NOTION-MIGRATION §7 критерий 8: "7 дней без новых потерь". Но
low-frequency pages (раз в месяц) → 7 дней недостаточно для wake-up catch.

**Ссылки:** NOTION-MIGRATION §7 criterion 8.

### 13.3 δ слишком поздно — MCP dies

**Проблема.** Inventory gap #2: Notion MCP падал. Если задержка γ → MCP authentic
expires → не экспортировать → data stuck.

**Ссылки:** inventory gap #2, NOTION-MIGRATION §8 risks table.

### 13.4 Timing не в SYSTEM-DESIGN-HUMAN

**Проблема.** §4.6 статус "Фаза α завершена". Когда γ? Когда δ? Нет target
dates в HUMAN. Только в NOTION-MIGRATION §10 optimistic dates.

**Ссылки:** §4.6, NOTION-MIGRATION §10.

### 13.5 Migration asymmetry (Windows local vs server)

**Проблема.** Local Claude имеет Notion MCP, server — нет. Extraction блокирован
availability Windows Claude → Ruslan'а. Не bottleneck в single-user, но single
point of coordination.

**Ссылки:** NOTION-MIGRATION §6.1, §6.2.

---

## 14. Дефицит метрик — 6 проблем

### 14.1 Качественная метрика непроверяемая

**Проблема.** §2.3 "Я не занимаюсь ерундой". Субъективно, unfalsifiable.
Noisy. Не может быть проксификатором работоспособности системы.

**Ссылки:** §2.3.

### 14.2 $50K — false positive

**Проблема.** Если достигли через найм / одного big клиента / friend referral
— система не помогла. Но метрика = pass.

**Ссылки:** §2.3, §1.7.

### 14.3 $50K — false negative

**Проблема.** Если не достигли, но Ruslan 3× продуктивнее, 200 качественных
контактов, 1000 wiki pages → система работает. Метрика = fail.

**Ссылки:** §2.3.

### 14.4 Нет system-health метрик

**Проблема.** Не описаны:
- Latency /ask
- Accuracy generated outreach
- Coverage voice-memo processing
- Throughput wiki pages/day
- Mailbox flux
- Agent task completion rate
- /lint orphan trend

**Ссылки:** §2.3 (no system metrics at all).

### 14.5 "Чистота" не измеряется

**Проблема.** §4.0 "чистота как на GitHub". Not quantitative. 0 orphans?
<5 orphans? threshold?

**Ссылки:** §4.0.

### 14.6 100+ пользователей — no progress metric

**Проблема.** §1.6 обещает 100+ через год. Сейчас: 1. Next week? Targets?
Нет quarterly KPI.

**Ссылки:** §1.6.

---

## 15. Культурный риск — 5 проблем

### 15.1 Ruslan-style hardcoded

**Проблема.** CLAUDE.md "прямой без воды". Не все 5-10 партнёров такие. Если
soft-style user — система irritating. Промпты на жёстком тоне.

**Ссылки:** CLAUDE.md, §3.2.1.

### 15.2 Предпринимательский профиль как default

**Проблема.** §1.2 6 ресурсов — для предпринимателя. Researcher — другие
приоритеты. Artist — ещё другие. v1-beta hardcoded, §1.5 декларирует
кастомизацию без имплементации.

**Ссылки:** §1.2, §1.5.

### 15.3 8 проектов slot — arbitrary

**Проблема.** CLAUDE.md 8 active projects (quick-money, research, brand, ...).
Почему 8? Partner с 3 проектами — overkill setup. С 15 — не хватает.

**Ссылки:** CLAUDE.md projects table.

### 15.4 Сложность onboard'инга

**Проблема.** 25+ папок + 13 компонентов + 12 ролей + 5-layer memory + 9 entity
types + 9 edge types = сложность. Новый партнёр 1-2 недели только learn
структуру.

**Ссылки:** §4.1, §6.1, ARCHITECTURE-CURRENT.

### 15.5 §1.5 кастомизация — метафора, не архитектура

**Проблема.** "Гоночный болид / грузовик / прогулочная" — метафора.
Имплементация: как технически превратить "болид" (Ruslan preset) в "грузовик"
(researcher preset)? Переписать 12 agents + 6 niches + skills? Не описано.

**Ссылки:** §1.5.

---

## 16. Тех.долг на старте — 10 пунктов

v1-beta начинается с **существующим** тех.долгом:

### 16.1 12 strategies.md пустые после миграции (gap #9)

**Impact:** §6.1.13 self-improvement cycle не работает на старте.

### 16.2 6 mailbox'ов пустых, 6 с тестовым (gap #1)

**Impact:** orchestration described в §3.2.2 не operational.

### 16.3 meta-agent в plan-only (gap #4)

**Impact:** §6.1.13 cycle blocked.

### 16.4 strategist в plan-only (gap #5)

**Impact:** decisions-log.jsonl не пишется, §6.1.14 trail через git only.

### 16.5 baseline.md vs system.md unresolved (gap #6)

**Impact:** §6.1.13 versioning ambiguous.

### 16.6 knowledge-base/ → wiki/ 0% migrated

**Impact:** sales/ data (important per §2.1.5) still legacy.

### 16.7 voice-memos 0% transcribed

**Impact:** §2.1.9 promise "обработка созвонов" — не работает.

### 16.8 Orphan agents/content-team/, sales-team/, research-team/, _shared/

**Impact:** не в roster → что это? Легаси?

### 16.9 escalation.jsonl не существует (gap #11)

**Impact:** §5.4 escalation path технически отсутствует.

### 16.10 crazy-agent tool mismatch (gap #7)

**Impact:** CLAUDE.md says mcp__notion, actual frontmatter say web_search only.
Single-source-of-truth нарушен.

---

## 17. Обучение агентов (§6.1.13) — 5 заблуждений

### 17.1 "Агенты умнеют" — accumulation ≠ intelligence

**Проблема.** Механика §6.1.13 — rule accumulation в strategies.md, A/B prompt
testing. **Это не self-improvement.** Модель (Opus 4.6) фиксированная. Prompt
variations fine-tune behavior, не mindset. Не "умнеют" — "накапливают правила".

**Ссылки:** §6.1.13.

### 17.2 A/B promptов — гипотетический; нет implementation

**Проблема.** §6.1.13 пункт 4 обещает A/B testing. Inventory: никаких записей
в shared/state/metrics/ab-tests. → 0 executions. Механизм не реализован.

**Ссылки:** §6.1.13 пункт 4, inventory gap #4.

### 17.3 Feedback loop требует Ruslan's time

**Проблема.** §6.1.13 пункт 5: "работа → feedback → meta-agent → Ruslan →
изменение". 5 шагов. Каждый Ruslan approval = 5 минут. Для 12 agents × 1
цикл/неделя = 60 минут/week. Реалистично? Если нет — цикл не крутится.

**Ссылки:** §6.1.13 пункт 5.

### 17.4 Risk of regression — no test harness

**Проблема.** Если A/B test показывает улучшение на narrow set, но регрессию
elsewhere — как catch? §6.1.13 "метрики сравниваются через 7 дней" — out-of-system
метрики (§2.3) шумные. Реальная regression пройдёт undetected.

**Ссылки:** §6.1.13, §2.3.

### 17.5 "Контекст не забывается" — обещание без механизма

**Проблема.** §6.1.13 "контекст сохраняется, агент умнеет с каждой сессией".
Реально: Claude session ephemeral. strategies.md — accumulated rules (не
контекст). mailbox — recent messages. Nothing preserves "что я думал вчера
в 14:00 перед тем как Ruslan прервал". Обещание vs реальность.

**Ссылки:** §6.1.13 vs §5.6.4 (перезапуск = потеря).

---

## 18. Что не описано, но критично — 16 пробелов

### 18.1 Security model

**Проблема.** §5.7 "не трогать .env/.ssh/private/". Но:
- Какой агент имеет read-доступ к `strategy/life/`?
- Sales-agents могут читать health/?
- Permission model per-agent — §7.2.5 отложен.

**Critical:** если partners в клубе (§3.4) — как их данные изолируются?

**Ссылки:** §5.7, §7.2.5, §3.4.

### 18.2 Privacy для Daily Log

**Проблема.** Daily Log содержит настроение, energy, personal reflection.
§6.2.4 "раскидывает". Шифрование at rest? Access control? Data leakage
через Anthropic API (каждая заметка в облако)? GDPR compliance (Германия)?

**Ссылки:** §6.2.4, context 0 (Ruslan в Берлине).

### 18.3 Резервные копии

**Проблема.** Не описано:
- Frequency (SAFE-SAVE != backup)
- Offsite (GitHub — один provider)
- Restore plan
- Test restore (never done?)

**Ссылки:** §5.6.1 SAFE-SAVE (вычислено как git push, not backup).

### 18.4 Migration между Claude models

**Проблема.** Promptы calibrated на Opus 4.6. Opus 4.7/4.8 breaking changes →
поведение меняется. Нет prompt-regression tests.

**Ссылки:** §6.1.13.

### 18.5 Лицензирование

**Проблема.** §1.8 "Слой 4 — Jetix Open-Source". Какая лицензия? MIT/Apache/GPL/
proprietary? Ещё не решено → в релизе может оказаться конфликтом licenses
нескольких components.

**Ссылки:** §1.8.

### 18.6 GDPR compliance

**Проблема.** CRM содержит contact info. §6.1.9 "3 базы клиентов". Consent
mechanism? Right to erasure (§2.4.4 "почти не удаляет")? Как stakeholder
потребует эрасу — append-only policy блокер.

**Ссылки:** §2.4.4, §6.1.9, context 0 (Germany = GDPR).

### 18.7 Observability

**Проблема.** `shared/state/metrics/` exists (ARCHITECTURE) but not collected.
Нет dashboard alerts. Нет tracing. Нет "что агент делает сейчас".

**Ссылки:** ARCHITECTURE §2.3 vs §operational usage not specified.

### 18.8 Cost monitoring

**Проблема.** Anthropic API costs grow с использованием. Если session burns
$100/day — когда notice? Нет budget alert.

**Ссылки:** не адресовано.

### 18.9 Version control strategy

**Проблема.** §6.2.4 "main = main trunk". Ok для projects. Infrastructure
changes? Directly в main? Risky-change branches? §CLAUDE.md silent.

**Ссылки:** §6.2.4, CLAUDE.md.

### 18.10 Rollback strategy

**Проблема.** Если strategies.md + system.md + skills изменились batch и новый
version ломает → rollback? §6.1.13 пункт 3 "rollback всегда возможен" — как
technically? git revert X ломает несвязанные файлы в том же commit.

**Ссылки:** §6.1.13 пункт 3.

### 18.11 Testing strategy

**Проблема.** Нет упоминания unit/integration tests для skills/agents/
tools/*.py. §6.1.13 A/B described, но только для prompts. Scripts могут
silent-fail.

**Ссылки:** не адресовано.

### 18.12 Onboarding new partner

**Проблема.** §3.4 partners. 5-10 через 3 месяца. Как добавить? Docs? Setup
wizard? Manually clone repo? Не описано.

**Ссылки:** §3.4, §1.6.

### 18.13 User-facing docs для партнёров

**Проблема.** §7.4.5 отложено в backlog. Но §1.6 "3 мес = 5-10 партнёров".
Если откладываем docs — партнёры не могут use без 1-on-1 onboarding Ruslan'ом.
Scale bottleneck.

**Ссылки:** §7.4.5, §1.6.

### 18.14 Incident response

**Проблема.** Если агент создал плохой output (spam, offensive tweet) —
process? Kill switch? §5.7 preventive, но failure inevitable. Recovery?

**Ссылки:** §5.7, §2.4.2.

### 18.15 Data retention

**Проблема.** decisions/ append-only forever. Через 5 лет огромный файл.
В wiki/ — тоже. Cleanup не описан.

**Ссылки:** §6.1.14, §2.4.4.

### 18.16 Knowledge decay

**Проблема.** Идея 2 года назад может быть stale. /lint "stale claims"
упомянут в ARCHITECTURE. Но policy "когда claim stale" не описан в
SYSTEM-DESIGN-HUMAN.

**Ссылки:** ARCHITECTURE §2.6 stale claims, §6.1.13 (агенты умнеют но knowledge
не стареет?).

---

## Summary — Top 10 critical weaknesses (ранжированные по impact)

1. **Ruslan как human SPOF (§1.1)** — система не выживает >48 часов без него.
   Нет delegation / deputy / policy-defaults. Каскад: болезнь / отпуск = system
   freeze. **Addressable in TECH:** deputy mode, auto-queue, policy templates.

2. **Чистота без автоматики (§9.1)** — математически несовместимо. 4-5 часов
   дня ↔ 150% discipline load. Что-то бросится. **Addressable in TECH:**
   автоматический maintenance после user approval (soft cron).

3. **"12 агентов" fiction (§6.1)** — "central Claude входит в роли" vs
   "каждая роль отдельный KB" противоречат. strategies.md пустые. Mailboxes
   пустые. **Addressable in TECH:** либо признать что 1 Claude с niche-фильтрами,
   либо реально сделать 12 headless процессов (через sub-agents как services).

4. **API / central session SPOF (§1.2, §1.3)** — нет Anthropic fallback, нет
   session recovery механизма. §3.5.2 обещает "работа без AI" но не имплементирует.
   **Addressable in TECH:** cross-provider abstraction, session snapshots.

5. **Human-in-loop bottleneck (§8)** — 30+ approval-points/day × 5 min = 2.5h.
   50-60% рабочего дня. **Addressable in TECH:** policy defaults, decision
   precedents, batch approvals.

6. **Race conditions на shared files (§3)** — edges.jsonl, state/*.json,
   wiki pages concurrent access. Нет lock mechanism. **Addressable in TECH:**
   file locks, write-queue, single-writer protocols.

7. **Metric deficit (§14)** — метрики не измеряют работу системы, только
   outcomes. $50K — false positive/negative. **Addressable in TECH:** system
   health metrics, throughput, latency.

8. **Масштабирование cement (§11)** — v1-beta hardcoded для 1 user, но §1.6
   обещает 100+. Каждое решение v1-beta = долг для v2.
   **Addressable in TECH:** per-user namespacing даже если used только
   Ruslan'ом на v1-beta (path./default.{user}/) — backward-compatible.

9. **Notion migration timing (§13)** — γ/δ dates unclear, MCP может
   деградировать до δ готовности. Параллельная жизнь Notion + wiki создаёт
   drift. **Addressable in TECH:** hard deadline, pilot 20-page verify,
   Notion freeze moment.

10. **Self-improvement — wishful thinking (§17)** — strategies.md пустые
    spent after migration, meta-agent dead. §6.1.13 описывает цикл который
    не запускается. **Addressable in TECH:** реальный механизм (автоматический
    feedback write, event trigger после каждой big task), или explicit
    отказ от обещания "агенты умнеют" до v1-final.

---

## What MUST be addressed in SYSTEM-DESIGN-TECH (блокеры v1-beta жизни)

Тех.документ **обязан** решить (иначе v1-beta не выживет):

1. **Deputy / offline mode для Ruslan.** Как минимум:
   - Policy defaults ("одобрить X типа leads автоматически если Y условия")
   - Safe-queue для approvals (откладывает critical задачи на return)
   - §1.1 SPOF без этого не решён.

2. **Session crash recovery.** Snapshot central Claude state каждые N минут в
   файл. Restart может read и восстановить логический контекст (не словарный).

3. **Concurrent file write strategy.** Lock mechanism / append-queue для
   edges.jsonl, state/*.json, wiki pages. §3.1, §3.6.

4. **"12 агентов" honest picture.** Либо:
   - Признать "1 Claude + niche filter + strategies.md" (упростить текст §3.2, §6.1.13)
   - Либо реализовать 12 real processes (сервис на хосте)
   - Смешанная модель с honesty о каждом case.

5. **API fallback layer.** Abstraction над Anthropic, позволяющая swap
   provider без breaking skills. Даже если fallback не used — architectural
   hook должен быть.

6. **Maintenance automation гарантия.** Даже в "полуручном" режиме — ритуал
   reminder через calendar integration; 1-click maintenance sequence.

7. **Policy-default approval mechanism.** Не "все решения Ruslan", а "Ruslan
   определяет policy, мелкие decisions идут по policy".

8. **Backup + restore plan.** Offsite copy repo, test restore ежемесячно.

9. **Notion γ/δ concrete dates + pilot verify protocol.** Hard deadlines
   иначе migration затянется.

10. **System health metrics.** Хотя бы: /lint frequency, mailbox throughput,
    wiki page growth/week, approval queue length. Dashboard cell для каждого.

11. **Frontmatter convention formal spec.** §7.2.1. Нельзя откладывать.

12. **Permission model даже минимальный.** Read/write separation per-agent.
    §7.2.5 не откладываемо для production.

13. **strategies.md lifecycle.** Кто пишет, когда, как versioning, rollback.
    §6.1.13.

14. **Escalation path formalized.** §5.4 один уровень — для v1-beta ok.
    escalation.jsonl должен существовать (inventory gap #11).

15. **Security баseline.** Минимально: какие folders НЕ читаются агентами;
    какие API keys где; что в gitignore.

---

## What CAN be deferred to v1-final / v2

Эти слабости не блокеры v1-beta (если их осознанно признать debt):

1. **Full multi-tenancy** (§11). v1-beta для Ruslan only ok.
2. **ISO 25010 mapping** (meta scope).
3. **Lifecycle jpartnera** (§7.1.4 client-facing).
4. **Детальные Agent Cards** (§7.1.2).
5. **Glossary** (§7.4.1).
6. **Miro 5+ visualizations** (§7.4.3).
7. **Client portal** (§7.1.4).
8. **Full licence strategy** (§1.8 layer 4 — далеко по roadmap).
9. **Scientific / philosophical artifacts** (§2.1.3 extended roadmap).
10. **Integration с мозгом** (§1.6 100-150 year) — очевидно defer.

---

## Метанаблюдение — паттерн слабостей

Большинство критичных проблем — **не случайные bugs**, а **системное следствие
выбора архитектурных паттернов**:

- **"Полуручной режим" (§5.0)** экономит время на автоматизацию, но
  переносит нагрузку на discipline Ruslan'а — и она не scales.
- **"Один Claude входит в роли" (§3.2.1)** упрощает инфраструктуру, но ломает
  абстракцию 12 независимых агентов.
- **"Append-only chistota" (§4.0)** упрощает writes, но hard случай reads
  (search через огромные append-only логи).
- **"Все решения через Ruslan'а" (§2.4.1)** обеспечивает контроль качества,
  но hard-capst pace системы на bandwidth одного человека.

Каждый из этих паттернов — **сознательный trade-off** Ruslan'а под v1-beta.
Но **цена** этих trade-offs не полностью проявлена в документе. Тех.документ
должен **явно** показать edge-of-cliff для каждого:

- Полуручной: устойчив до N заметок/день, после — drift.
- Single Claude: устойчив до M tokens/session, после — session crash.
- Append-only: устойчив до K pages в одном файле, после — performance / search
  degradation.
- Ruslan approval: устойчив до 20 decision-points/day, после — backlog.

Без численной фиксации этих границ — v1-beta declared as "working", но работает
только в узком window условий.

---

## Финальный комментарий критика

Документ SYSTEM-DESIGN-HUMAN v1-beta — **честный** и **зрелый**. Он не
прячется за jargon'ом, он открыто заявляет компромиссы. Beta-first принцип
применён последовательно.

Однако **открытая декларация ограничений не равна их разрешению**. Я считаю, что:

1. **§meta-section "Scope и приоритет"** полезна, но опасна — она легитимизирует
   пропуск critical items как "beta-first". Half из critical items из этого
   отчёта попадут в категорию "v1-final" если SYSTEM-DESIGN-TECH напишется без
   **независимой** проверки против этого критик-отчёта.

2. **"$50K до 30.06.2026"** как primary goal — достижимо и без полной Jetix OS.
   Ruslan может закрыть $50K через традиционные методы (outbound, referrals)
   используя Jetix OS **частично** (как todo-list + CRM). В этом сценарии
   v1-beta — слабая prop-up а не core enabler. Документ не показывает **что
   именно из v1-beta критично для $50K** vs "приятно иметь".

3. **Self-deceptive элементы** (§6.1.13 "агенты умнеют", §3.2.1 "центральный
   Claude с контекстом который не забывается", §1.5 "быстрая перестройка",
   §3.5.2 "работает без AI") — **самые опасные**. Они создают ложное ощущение
   зрелости архитектуры, которое влияет на стратегические решения Ruslan'а
   (особенно §1.6 100+ users — архитектура к этому не готова).

**Моё рекомендование Синтезатору:** при сборке SYSTEM-DESIGN-TECH трактовать
**self-deceptive элементы** как **приоритет номер 1**. Не маскировать их в
формальном языке, а **явно** обозначить как гипотезы подлежащие валидации в
первые 2 недели использования v1-beta.

Конкретно: в каждом разделе TECH добавить секцию **"Что мы обещаем но не
гарантируем"** с прямыми отсылками к этому критик-отчёту.

---

*End of critic review. 18/18 categories covered. 67 concrete weaknesses cited.
Independent perspective delivered without collaboration with chat 2/3/4.
Waiting for synthesis (chat 5).*
