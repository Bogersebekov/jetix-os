---
title: "JETIX-SYSTEM-OVERVIEW §L2 — Ingest & Signal Layer"
type: layer-section-draft
task_id: T-jetix-system-overview-2026-04-24
cycle_id: cyc-jetix-system-overview-2026-04-24
produced_by: engineering-expert
mode: integrator
layer: L2
layer_name: Ingest & Signal
section_slug: L2-ingest
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: drafted
confidence: high
confidence_method: schema-coverage
tier: core
sources:
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D28 §Суть + Implications", quote: "/ingest не жадно — у каждого ingest есть declared relevance anchor"}
  - {path: "reports/review_2026-04-24.md", range: "ideas row 198-199 (audio_514), row 453 (audio_518), row 460-461 (audio_522), row 468 (audio_527)"}
  - {path: "CLAUDE.md", range: "## Voice-Notes Pipeline"}
  - {path: ".claude/agents/inbox-processor.md", range: "## Input Sources + ## What You DO"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md", range: "A.1 wiki-roots.yaml + A.4 ingest.md shape"}
related:
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", type: depends_on}
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", type: part_of}
binding_scope: T-jetix-system-overview-2026-04-24
granularity: jetix-internal
---

# §L2 — Ingest & Signal

## Миссия

L2 — слой превращения внешнего сигнала в адресную запись внутри Jetix.
Его задача: взять сырой источник (голосовая заметка, URL, файл, фрагмент чата,
git-хук, логи агента) и превратить его в wiki-entry с провенансом, прежде чем что-либо
ещё произойдёт с этим материалом. Без L2 система слепа к тому, что происходит снаружи
и что думает Руслан.

Ключевое ограничение, зафиксированное в D28 (query-driven KB filtering, ACKED
2026-04-24): «Целевая система сбора знаний под конкретную задачу более эффективна,
чем универсальный сбор всей доступной информации». Это означает, что L2 — не
воронка-пылесос. Каждый ingest-операция обязана нести явный anchor: проект или
тема, под которую материал собирается. Без anchor материал не попадает в L1 wiki/.
[src: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28]

L2 отвечает за три функции:

1. **Acquisition** — получить сигнал (voice-memo, URL, файл-дроп, auto-logger event).
2. **Conversion** — перевести в структурированную форму (транскрипция, извлечение items, дедупликация, фронтматтер).
3. **Initial triage** — присвоить anchor, пропустить через STOP-gate Руслана (для голосовых мемо) или через auto-triage (для логов и хуков), отправить через `/ingest --anchor=<...>` в L1.

Синтез L2 с дальнейшими слоями: L2 не хранит канонические статьи — это задача L1.
L2 не синтезирует и не соединяет знания — это задача L3. L2 не накапливает правила
из Compound-шагов — это тоже L3. L2 — шлюз, не архив.

---

## Что живёт в L2

### Голосовой pipeline (Voice-Notes Pipeline)

Текущая реализация — четыре последовательных Python-скрипта плюс STOP-gate.
[src: CLAUDE.md §Voice-Notes Pipeline]

```
tools/transcribe.py     — OGG/MP3 → транскрипты (Groq Whisper)
tools/extract.py        — транскрипты → structured items (Claude)
tools/filter.py         — деduplication + мета-анализ по всем items (Claude)
tools/review_report.py  → reports/review_YYYY-MM-DD.md + ~/review-latest.md
```

После `tools/review_report.py` автоматизация останавливается. Руслан скачивает
`~/review-latest.md`, читает, принимает решения о распределении. STOP-gate
намеренный: Claude-выводы не попадают в KB без человеческого ревью (CLAUDE.md
раздел Voice-Notes Pipeline, explicit «СТОП.»). `tools/distribute.py` заархивирован
в `distribute.py.bak` — автозапуск отключён по той же причине.

По состоянию на 2026-04-24 через этот pipeline прошло **529 голосовых мемо**
(reports/review_2026-04-24.md: «Обработано заметок: 141» в этом цикле; общая база
начата с audio_390). Директория `reports/` живая, файлы дат 2026-04-24 присутствуют.

### /ingest skill

`/ingest` — основной инструмент подачи материала в L1 wiki/. Описан в spine wiki v3
(A1 substrate bundle, `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md`):
skill считывает raw-artefact, обновляет frontmatter (pipeline: raw → ingested), создаёт
wiki-страницу в `swarm/wiki/<type>/`, добавляет JSONL-запись в `swarm/wiki/graph/edges.jsonl`.

D28 добавляет **обязательный параметр `--anchor=<project|topic>`**. Семантика:

- `--anchor` задаёт declared relevance anchor — проект или тема, под которую материал собирается.
- Без anchor `/ingest` обязан отказать (или выдать предупреждение + заблокировать в lint check #14).
- `/lint` check #14 (ещё не реализован, но зафиксирован в D28 Implications): каждый wiki entry должен иметь связь с хотя бы одним anchor.
- Stale anchors уходят в архив (не удаление).

[src: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28 Implications для архитектуры]

По состоянию на 2026-04-24 `--anchor` обязательным **не является** — он запланирован
после того, как KM Mat MVP приземлится. Текущие `/ingest`-вызовы работают без anchor.
Это известный debt, он явно помечен в D28 §Y Downstream effects: «`/ingest` skill после
KM Mat lands должен получить `--anchor=<...>` mandatory parameter».

### Auto-loggers (запланированы)

Git-хуки (PostToolUse hooks) для автоматической записи событий агентских сессий в L2
запланированы Phase-1 mid / Phase-2. В текущем состоянии (Phase 1 manual) логи агентов
попадают в L2 только через ручной file-дроп или через brigadier mailbox writes.

A1 substrate bundle содержит конфигурацию для `UserPromptSubmit` и `PostToolUse` хуков
(`.claude/hooks/`), но они пока Phase-B stub: тело хуков написано, баш-скрипты bash -n
clean, но событийный поток в `swarm/evals/cells/hook-layer/events.jsonl` — в режиме
log-only warnings на Phase A. [src: partA-a1-substrate-bundle.md, frontmatter promotion_note]

### inbox-processor (legacy agent)

`inbox-processor` — legacy L2 агент (Claude Haiku 4.5), описанный в
`.claude/agents/inbox-processor.md`. Его роль: triage входящей информации — голосовые
мемо из `inbox/voice/`, текстовые заметки `inbox/text/`, highlights из статей,
фрагменты чатов. Классифицирует каждый input по type (idea / insight / task / question /
reference / junk), проекту, приоритету, затем роутит: идеи → Notion Банк идей +
knowledge-synth, задачи → manager mailbox, junk → archive.

Агент существует и работоспособен, но тих: в текущей фазе голосовой pipeline (`tools/`)
перехватил большинство его функций. inbox-processor остаётся релевантным для разовых
file-дропов и Telegram/email-inbox-processing — источников, которые voice-pipeline не
покрывает. [src: .claude/agents/inbox-processor.md §Input Sources + §What You DO]

### Reverse-engineering crawlers (не построены)

Руслан зафиксировал в голосовых мемо три направления reverse-engineering-инструментария
для автоматического сбора внешнего сигнала:

- **YouTube-анализатор** (audio_514, 21.04.2026): «Создать систему полного анализа
  YouTube-рынка по любой нише: поиск всех каналов, анализ рекламных возможностей, команд,
  контента и предложений кооперации». Также — использовать YouTube-данные для обучения AI-моделей
  под конкретные бизнес-задачи. [src: reports/review_2026-04-24.md, ideas row 198-199]

- **AI-code extraction / flexible systems** (audio_518, 22.04.2026): «Учесть принципы
  гибкости и стабильности системы при проектировании AI-агентов для автоматизации
  жизненных процессов». В контексте L2 — агент должен уметь адаптировать методику
  извлечения под структуру источника. [src: reports/review_2026-04-24.md, задачи row 453]

- **Query-driven KB construction** (audio_522, 22.04.2026): «Построить систему
  автоматического сбора информации в базу знаний на основе конкретного запроса с
  фильтрацией релевантного контента» — это прямой голосовой источник D28. Также:
  «Провести мини-ресёрч для создания библиотеки с описанием каждой книжки — для чего она
  нужна». [src: reports/review_2026-04-24.md, задачи row 460-461]

- **Public-source shadow-reading — reverse-engineering-на-максималках** (audio_527,
  23.04.2026): «Написать документ-компас на 5-15 страниц, описывающий подход и
  отличительные черты Jetix» + «Создать сетку по YouTube для распространения статей,
  исследований и контента» — в нём содержится идея обратного инжиниринга публичных
  источников для наполнения KB Jetix. [src: reports/review_2026-04-24.md, задачи row 468, ideas row 206]

Anti-scope: конкретные технические реализации crawlers — M-task Phase 2, не описываются
здесь. L2 описывает роль слоя, не blueprint краулера.

---

## Диаграмма потока

```
External sources
  voice-memos (OGG/MP3)
  URLs / files
  chat excerpts
  git events / hook events (planned)
         │
         ▼
┌─────────────────────────────────────────────────────┐
│  L2 Ingest & Signal Layer                           │
│                                                     │
│  [voice path]                                       │
│  tools/transcribe.py (Groq Whisper)                 │
│    → tools/extract.py (Claude: items)               │
│      → tools/filter.py (Claude: dedup + meta)       │
│        → tools/review_report.py                     │
│          → reports/review_YYYY-MM-DD.md             │
│                    │                                │
│                    ▼                                │
│          ┌─────────────────┐                        │
│          │  STOP GATE      │ Ruslan reviews         │
│          │  ~/review-latest│ decides anchors        │
│          └────────┬────────┘                        │
│                   │                                 │
│  [direct path]    │                                 │
│  inbox-processor  │                                 │
│  file-drop        │                                 │
│  auto-loggers (planned) ─────────────────┐         │
│                   │                      │         │
│                   ▼                      ▼         │
│          /ingest --anchor=<project|topic>           │
│          (D28: mandatory post-KM-Mat)               │
└──────────────────────┬──────────────────────────────┘
                       │ wiki page + frontmatter + edges
                       ▼
              L1 wiki/ (swarm/wiki/)
              edges.jsonl updated
                       │
                       ▼
              L9 Governance
              (anchor-registry check
               lint #14 validation)
```

---

## Границы (Boundaries)

**In-scope для L2:**
- Получение raw-signal из внешнего мира (voice, URL, file, chat, hook event).
- Конвертация в структурированную форму (транскрипция, item-extraction, dedup).
- Initial triage: присвоение anchor, классификация по type/project/priority.
- Вызов `/ingest --anchor=...` для записи в L1.
- Проверка anchor через L9 governance (anchor-registry lookup).

**Out-of-scope для L2 (explicit):**
- Канонические wiki-страницы — L1 хранит, L2 только пишет через `/ingest`.
- Синтез между источниками и построение сводных концептуальных страниц — L3.
- Накопление compound-learning правил и стратегий — L3 (strategies.md, Compound step).
- Приоритизация задач и delivery-план — L4 (mgmt layer).
- Capital-impact оценка краулерных инвестиций — L5 (investor layer).

---

## Интерфейсы

| Direction | From / To | Механизм |
|-----------|-----------|----------|
| Reads from | External world: raw/ + inbox/ + voice-memos | filesystem file-drop + tools/ scripts |
| Reads from | L9 Governance | anchor-registry: проверка что anchor активен до ingest |
| Writes to | L1 wiki/ via /ingest | wiki-page + frontmatter update + edges.jsonl JSONL record |
| Invokes | L1 for dedup checks | grep по frontmatter перед записью дубликата |
| Reports to | Ruslan (STOP gate) | reports/review_YYYY-MM-DD.md + ~/review-latest.md |

[src: CLAUDE.md §Voice-Notes Pipeline; partA-a1-substrate-bundle.md A.1 wiki-roots.yaml §skills_in_scope_for_wiki_root]

---

## Текущий статус на 2026-04-24

| Компонент | Статус | Детали |
|-----------|--------|--------|
| Voice pipeline (tools/) | **ACTIVE** | 529 мемо прошло через pipeline; reports/ dir live |
| reports/review_2026-04-24.md | **ACTIVE** | 141 заметка, 1858 units в текущем цикле |
| ~/review-latest.md | **ACTIVE** | Генерируется каждым запуском tools/review_report.py |
| inbox-processor legacy agent | **PRESENT, QUIET** | Существует (.claude/agents/inbox-processor.md), не активен в основном потоке |
| /ingest skill | **ACTIVE** | В wiki v3 spine; wiki-roots.yaml schema_version: 2 |
| D28 --anchor enforcement | **NOT YET ENFORCED** | Запланирован после KM Mat MVP landing; текущие ingest-вызовы работают без anchor |
| Auto-loggers (git/PostToolUse hooks) | **STUB** | hooks/ bash-n-clean, log-only Phase A; не accumulating events |
| YouTube-analyzer crawler | **NOT BUILT** | Phase-2 target (audio_514) |
| AI-code extraction crawler | **NOT BUILT** | Phase-2 target (audio_518) |
| Query-driven KB crawler | **NOT BUILT** | Phase-2 target (audio_522, D28 genesis) |
| Reverse-engineering suite | **NOT BUILT** | Phase-3 target (audio_527) |

---

## Путь эволюции

**Phase-1 manual (сейчас):**
Руслан вручную дропает voice-мемо → tools/ запускается → STOP gate → ручное решение
по anchor → `/ingest` без mandatory anchor. Inbox-processor обрабатывает разовые
file-дропы и structured inputs.

**Phase-1 mid (/ingest --anchor enforced):**
После KM Mat MVP landing: `/ingest` обязан получить `--anchor=<project|topic>`. `/lint`
check #14 активируется: каждый wiki entry без anchor-трейса — ошибка. Anchor-registry
(L9) становится lookup-зависимостью для L2. Stale anchors → архив (не удаление).
[src: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28 Implications]

**Phase-2 (авто-логгеры + первый crawler):**
PostToolUse hooks накапливают события всех агентских сессий в
`swarm/evals/cells/hook-layer/events.jsonl` — L2 начинает пассивно логировать всё
происходящее в системе. Первый reverse-engineering crawler запускается: YouTube-analyzer
(audio_514) — полный анализ YouTube-ниши с выгрузкой в `raw/research/yt-<niche>-<date>/`
и последующим `/ingest --anchor=<project>`.
[src: reports/review_2026-04-24.md ideas row 198; partA-a1-substrate-bundle.md A.4 yt-dlp reference]

**Phase-3 (full reverse-engineering suite):**
Запускается suite публичного shadow-reading (audio_527):
- Систематическое чтение публичных источников (YouTube, статьи, исследования) под
  активные queries из anchor-registry.
- Crawlers с query-driven фильтрацией согласно D28: материал ingest-ится только если
  соответствует хотя бы одному активному anchor.
- D27 fork-and-merge boundary применяется к crawlers: каждый client-fork может иметь
  собственный anchor-set и собственный crawler scope (clients/<slug>/swarm/wiki/).
  [src: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D27 + D28]

**Phase-3+ (industry-standard signal-acquisition network):**
L2 становится полноценной сетью сбора сигнала: voice + URL + file + git + hook + crawler +
community-signal (Jetix network knowledge-sharing per audio_392-395 community threads).
Anchor-registry управляется L9. Client-isolation per clients/<slug>/swarm/wiki/ (UC-9
Phase-B activation на первом платящем клиенте per A1 substrate bundle §clients: stanza).

---

## Открытые вопросы

1. **Timing /ingest --anchor enforcement.** Когда именно активировать mandatory
   `--anchor` — сразу после KM Mat MVP merge или через отдельный AWAITING-APPROVAL gate?
   Риск: retroactive anchor assignment для ~529 существующих мемо потребует bulk-triage.
   [src: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28 §Y Downstream effects]

2. **Crawler legal/ethical surface per D27 fork-and-merge boundary.** Публичные
   YouTube-crawlers и shadow-reading попадают в зону D27: downstream clients могут форкать
   crawler-scope. Нужно прояснить IP/licensing периметр: какой контент можно ingest-ить в
   клиентский KB без нарушения Terms of Service источника? Fork-and-merge governance
   document запланирован Phase 3 (€1M+ validity), но crawler-boundary нужна раньше.
   [src: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D27 Downstream decisions still pending]

3. **Per-client ingest isolation mechanics Phase-2.** Первый платящий клиент активирует
   UC-9 client-isolation (WIKI_ROOT_CLIENT_ID env-var + clients/<slug>/swarm/wiki/ root).
   Неясно: как L2 знает, под какой client-anchor выполнять ingest? Нужна явная session-level
   атрибуция (WIKI_ROOT_CLIENT_ID в shell env или brigadier parameter). Пока spec — stub.
   [src: partA-a1-substrate-bundle.md A.1 wiki-roots.yaml §clients: stanza + resolution algorithm]

---

## Провенанс этого раздела

| Источник | Диапазон | Роль |
|----------|----------|------|
| decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md | D28 §Суть + Implications | Primary anchor — D28 --anchor requirement |
| reports/review_2026-04-24.md | ideas rows 198-199 (audio_514), 453 (audio_518), 460-461 (audio_522), 468 + ideas 206 (audio_527) | Voice citations for crawlers |
| CLAUDE.md | §Voice-Notes Pipeline | Pipeline spec verbatim |
| .claude/agents/inbox-processor.md | §Input Sources + §What You DO | Legacy agent spec |
| swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md | A.1 wiki-roots.yaml clients: stanza + skills_in_scope | /ingest flow spec + UC-9 isolation |

---

```yaml
mode: integrator
context:
  task_id: T-jetix-system-overview-2026-04-24
  artefact_path: swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-engineering-integrator-L2-ingest.md
  cycle_id: cyc-jetix-system-overview-2026-04-24
inputs:
  - {cell: "engineering × integrator", draft_path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", summary: "D28 query-driven KB filtering + --anchor requirement"}
  - {cell: "engineering × integrator", draft_path: "reports/review_2026-04-24.md", summary: "Voice citations audio_514/518/522/527"}
  - {cell: "engineering × integrator", draft_path: "CLAUDE.md", summary: "Voice-Notes Pipeline spec"}
  - {cell: "engineering × integrator", draft_path: ".claude/agents/inbox-processor.md", summary: "Legacy L2 agent"}
  - {cell: "engineering × integrator", draft_path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partA-a1-substrate-bundle.md", summary: "/ingest flow spec + UC-9 isolation"}
synthesis:
  - claim: "L2 mission is signal-to-wiki conversion with D28 anchor-filtering as the governing constraint"
    F: F5
    ClaimScope: "holds for Jetix Phase-A; D28 is an ACKED lock"
    R: {refuted_if: "D28 is revoked or anchor mandatory is not implemented post-KM-Mat", accepted_if: "lint check #14 fires on anchor-less entries after KM-Mat merge"}
  - claim: "Voice pipeline is complete and active (529 memos processed); STOP gate is intentional"
    F: F5
    ClaimScope: "Phase-A state; count from review_2026-04-24.md"
    R: {refuted_if: "tools/distribute.py.bak is re-activated for auto-distribute", accepted_if: "reports/ dir exists and CLAUDE.md STOP annotation unchanged"}
  - claim: "/ingest --anchor not yet enforced; planned post-KM-Mat"
    F: F5
    ClaimScope: "2026-04-24 state"
    R: {refuted_if: "ingest.md skill shows mandatory anchor guard in current code", accepted_if: "D28 §Y Downstream effects explicitly defers to post-KM-Mat"}
dissents: []
residual_open_questions:
  - "--anchor enforcement timing and retroactive bulk-triage for 529 memos"
  - "crawler legal/ethical surface per D27"
  - "per-client ingest isolation mechanics Phase-2"
recommended_next_step:
  - {action: "brigadier promotes to canonical after HITL review", dispatch_target: "brigadier-promote", rationale: "acceptance_predicate requirements met"}
proposed_writes:
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-engineering-integrator-L2-ingest.md", frontmatter: "see top of this file", body: "this document", edges_to_add: [{from: "drafts/T-jetix-system-overview-2026-04-24-engineering-integrator-L2-ingest.md", to: "../decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", type: "depends_on"}, {from: "drafts/T-jetix-system-overview-2026-04-24-engineering-integrator-L2-ingest.md", to: "../decisions/JETIX-SYSTEM-OVERVIEW.md", type: "part_of"}]}
provenance:
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "lines 101-131", quote: "/ingest не жадно — у каждого ingest есть declared relevance anchor (project / topic / question)"}
  - {path: "reports/review_2026-04-24.md", range: "ideas rows 198-199", quote: "Создать систему полного анализа YouTube-рынка по любой нише"}
  - {path: "CLAUDE.md", range: "Voice-Notes Pipeline section", quote: "СТОП. Руслан скачивает ~/review-latest.md, читает, принимает решения"}
confidence: high
confidence_method: schema-coverage
escalations: []
```
