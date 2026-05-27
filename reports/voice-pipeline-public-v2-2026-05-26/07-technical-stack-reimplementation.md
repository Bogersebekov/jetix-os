---
title: Phase 6 — §F Технический стек + гайд воспроизведения
date: 2026-05-26
type: phase-report
parent_prompt: prompts/voice-pipeline-public-v2-2026-05-26.md
parent_main: decisions/strategic/VOICE-PIPELINE-PUBLIC-V2-2026-05-26.md
phase: 6
F: F2-F3
G: prompt-voice-pipeline-public-v2-2026-05-26
language: russian primary
---

# §F Технический стек + гайд воспроизведения

> Самая детальная секция. Здесь — **точные** компоненты, файлы, модели, пути, последовательность
> запуска, стоимость и ограничения. Написано так, чтобы методолог с Claude Code мог прочитать,
> зайти в `tools/` и развернуть себе своё. Все факты сверены с реальным кодом (Phase 0 §3 исправил
> ошибки первого черновика — здесь только то, что есть в репозитории на самом деле).

---

## §F.1 Компоненты (что из чего собрано)

| Компонент | Роль | Точная деталь |
|---|---|---|
| **Wispr Flow** (Windows desktop) | desktop-захват | голос → текст прямо в активное окно/файл; push-to-talk; за столом |
| **Telegram** | mobile-захват + inbox | голос/видео/ссылки/контакты в один inbox, разделённый по намерению (Phase 2) |
| **Groq Whisper API** | транскрипция | модель `whisper-large-v3`, `language=ru`; быстро и дёшево (~$0.001/мин аудио) |
| **Claude Code (CC headless)** | extraction / filter / summarize | **backend по умолчанию** — `claude -p` subprocess через **Max-подписку, без API-ключа** |
| **Anthropic API** | legacy fallback | только при `JETIX_LLM_BACKEND=api` (+ `ANTHROPIC_API_KEY`) — не дефолт |
| **Python 3.10+** | оркестрация | стандартная библиотека + `groq`, `anthropic` (опц.), `pyyaml`, `mutagen` (опц.) |
| **Markdown + YAML frontmatter** | хранение единиц | каждая entity = файл с машиночитаемым frontmatter |
| **Git** | версионирование + append-only история | каждое изменение = коммит; откат через `git revert` |

**⭐ Главный технический факт (его чаще всего понимают неверно).** Конвейер по умолчанию **НЕ ходит в
Anthropic API**. Он вызывает `claude -p` как subprocess, авторизуясь через **Max-подписку**. Это
сознательное решение (`tools/lib/cc_helper.py`, post-cycle-11 default): Max-подписка покрывает вызовы
фиксированной ценой подписки, поэтому **нет переменной стоимости за токены Claude**. Код даже
*убирает* `ANTHROPIC_API_KEY` из дочернего окружения, чтобы случайно не уйти в платный API-путь.
Единственная переменная стоимость в дефолтной конфигурации — Groq Whisper (~$0.001/мин). Это
полностью меняет «cost»-расчёт (см. §F.4) против того, что говорил первый черновик.

---

## §F.2 Code stack — точные файлы в репозитории

### Скрипты конвейера (`tools/`)

| Файл | Что делает | Модель / деталь |
|---|---|---|
| `tools/sync_context.py` | step 0: собирает `config/context.md` из локальных файлов (projects.json / decisions.json / profile.md / vision.md / последний review) | без сети, без LLM |
| `tools/transcribe.py` | step 1: `inbox/voice/*.{ogg,mp3,m4a,wav,webm}` → `raw/transcripts/*.txt`; аудио → архив `raw/voice-memos/` | Groq `whisper-large-v3`, lang=ru; идемпотентно (skip если транскрипт есть) |
| `tools/extract.py` | step 2: транскрипт → `inbox/processed/extractions/*.json`; 12 категорий + опц. `crm_items[]` | Claude `sonnet-4-6` (CC headless) |
| `crm/_scripts/crm voice-route` | step 2b: `extract-items-latest.yaml` → `<slug>-DRAFT.md` | DRAFT-only, никогда не overwrite prod CRM |
| `tools/summarize.py` | step 3: extractions → `~/summary-latest.md` (группировка по темам, **сохраняет 100%**, без dedup) | Claude `sonnet-4-6` |
| `tools/filter.py` | (после ревью) extractions → `inbox/processed/filtered/batch_<date>.json`; dedup + связи/противоречия + meta-analysis | Claude `opus-4-7`; батчи по 50 (threshold 100); **partial-save** отказоустойчивость |
| `tools/review_report.py` | filtered → `reports/review_<date>.md` + `~/review-latest.md` | markdown-таблицы по 7 секциям |
| `tools/voice-pipeline-orchestrator.py` | reusable 7-stage pipeline с **lens-driven Stage 6** | `--lens <yaml> --output <dir>` |
| `tools/lib/cc_helper.py` | общий LLM-вызов; выбор backend (cc-headless / api) | `claude_call(system, user, model)` |
| `tools/distribute.py.bak` | **архивирован** (авто-дистрибуция отключена намеренно) | см. §F.5 |

### Скрипты-оркестраторы (bash)

| Файл | Содержит | Заканчивается на |
|---|---|---|
| `tools/run_pipeline.sh` | step 0→1→2→2b→3 | **СТОП** → `~/summary-latest.md` на ревью |
| `tools/run_filter.sh` | filter → review_report | **СТОП** → `~/review-latest.md` на ревью |

### Конфиги и хранилище

- `config/context.md` — авто-собирается step 0 (контекст проектов/решений для тегирования)
- `config/voice-pipeline-lens-template.yaml` — шаблон линзы (Filter 2)
- `config/voice-pipeline-lens-<date>-<focus>.yaml` — конкретные линзы (хранятся навсегда)
- `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md` — **canonical design doc** (single source of truth)
- `wiki/` — база: `concepts/` `entities/` `sources/` `topics/` `ideas/` `experiments/` `claims/`
  `summaries/` `foundations/` + `graph/edges.jsonl` (9 типов рёбер)

---

## §F.3 Последовательность запуска (точная)

### Дефолтный путь (CC headless, без API-ключа)

```bash
# Предусловие: голосовые лежат в inbox/voice/ (выгружены из Telegram / записаны)

cd ~/jetix-os

# Фаза 1 — до ревью (steps 0-3)
bash tools/run_pipeline.sh
#   step 0: sync_context.py   → config/context.md
#   step 1: transcribe.py     → raw/transcripts/*.txt   (Groq whisper-large-v3)
#   step 2: extract.py        → inbox/processed/extractions/*.json (12 категорий)
#   step 2b: crm voice-route  → crm/people/<slug>-DRAFT.md (DRAFT-only)
#   step 3: summarize.py      → ~/summary-latest.md
#   ⏹ СТОП

# ── Человек скачивает ~/summary-latest.md, читает, принимает решения ──

# Фаза 2 — после ревью
bash tools/run_filter.sh
#   filter.py        → inbox/processed/filtered/batch_<date>.json (opus-4-7, dedup+meta)
#   review_report.py → reports/review_<date>.md + ~/review-latest.md
#   ⏹ СТОП

# ── Человек читает review, акает items, дистрибуция в KB — вручную ──
```

### Reusable lens-путь (когда нужен фокус-фильтр)

```bash
cp config/voice-pipeline-lens-template.yaml config/voice-pipeline-lens-2026-XX-<focus>.yaml
# заполнить: lens_name / lens_purpose / canonical_anchors / tier_1..3_keywords / threshold / top_n

python3 tools/voice-pipeline-orchestrator.py \
    --lens config/voice-pipeline-lens-2026-XX-<focus>.yaml \
    --output reports/voice-pipeline-2026-XX/
# → 8 deliverables, главный: 03-current-lens-actionables.md (топ-N под линзу)
```

**Два human-gate** (не один). Между фазой 1 и 2 — ревью сводки. После фазы 2 — ревью отчёта +
ручная дистрибуция. Это не «забыли заавтоматизировать» — это constitutional (§F.5).

---

## §F.4 Стоимость (исправлено против первого черновика)

Стоимость зависит от backend'а. Это важное различие, которое первый черновик смазал.

### Дефолт — CC headless (Max-подписка)

- **Claude-вызовы (extract / filter / summarize): покрыты подпиской Max.** Переменной стоимости за
  токены нет — платишь фиксированную цену подписки независимо от объёма прогонов.
- **Groq Whisper: ~$0.001/мин аудио.** При 30-60 мин аудио в день → **~$1-2/день** на транскрипцию.
- **Итого дефолт: ~$30-60/мес**, почти всё — Groq; Claude амортизирован в подписке.

### Legacy — API backend (`JETIX_LLM_BACKEND=api`)

- Здесь добавляется переменная стоимость токенов Claude (extract sonnet + filter opus + summarize
  sonnet). При активном использовании — **~€2-5/день**, **€30-50/мес**.
- Рекомендация: cap **€10/день hard**, если идёшь по API-пути.

**Вывод:** на дефолтном (CC-headless) пути основная статья расходов — Groq Whisper, а не Claude.
Это делает daily-use дешёвым и предсказуемым. Цифры «€2-5/день» из первого черновика относятся к
API-пути, который **не является дефолтом**.

---

## §F.5 Ограничения и что не сработало (честно)

### Ограничения by design

- **Два human-gate обязательны.** Авто-дистрибуция в KB **отключена намеренно** (R11 + Pillar C
  Tier 2). Без ревью между стадиями база загрязняется некалиброванными единицами. Это
  constitutional rule, не «руки не дошли».
- **Voice DRAFT-only (R12 / RUSLAN-LAYER).** Голосовые единицы **не имеют права** авто-overwrite
  prod-записи (CRM-контакты / strategic decisions / canonical wiki). Только `draft_from_voice`,
  ручной promote после ревью.
- **LLM теряет нюанс.** Extraction периодически теряет сарказм / иронию / двойной смысл /
  контекст-зависимые отсылки. Mitigation: F2 verbatim хранится всегда — можно переизвлечь (§A.5).
- **Голос = 30-50% шума.** Filler words / повторы / самокоррекции / иногда поток несвязен. Конвейер
  предполагает шум и фильтрует его на extraction; но идеальной фильтрации нет.
- **Batch lag.** Между записью и обработкой — часы/дни (это фича §A.4, но и ограничение): для
  real-time нужен синхронный путь (Wispr → текст в чат), не batch pipeline.

### Что пробовали и отказались

- **Авто-дистрибуция (`tools/distribute.py`).** Запускалась автономно в первой итерации. Через неделю
  Claude-извлечённые единицы накопились в KB как «канонические», но при ручной проверке 40-60%
  оказались «звучит правильно, но не точно». **Архивировали в `.bak`.** Ручной review между
  стадиями — non-negotiable. (Это и есть главный урок проекта.)
- **IWE chat как доп-обработчик.** Тестировали Aisystant IWE chat после extraction — качество ниже
  прямого Claude (лишний слой не добавлял value, добавлял latency + cost). Отказались; используем
  IWE как read-only reference канона МИМ.
- **BM25 + русская морфология для автосаджеста папок дистрибуции.** Match rate подняли 50.1% → 60.1%
  тюнингом. Workflow ускорился ~30% (быстрее ack), но human-in-the-loop не закрыл — плато ~60%.
- **Whisper для русского с акцентом.** OpenAI Whisper периодически путал редкие термины / англицизмы.
  Groq marginally лучше. В коде стоит **`whisper-large-v3` как baseline** (первый черновик ошибочно
  писал «Medium» — это не так): large-v3 даёт лучшую точность; отдельной «Large для critical»-опции
  не нужно, large-v3 уже дефолт.

---

## §F.6 Гайд воспроизведения (для третьей стороны)

### Минимальный viable setup

- Python 3.10+
- **Один из:** Claude Code (Max-подписка — дефолт, без API-ключа) **ИЛИ** `ANTHROPIC_API_KEY` (API-путь)
- Groq API key (free tier хватает для начала)
- Wispr Flow ИЛИ любое Whisper-based dictation-приложение
- Git-репо для хранения wiki
- Время развёртывания: ~1 день

### Шаги

```bash
# 1. Клонировать / форкнуть
git clone <repo>/jetix-os   # или форк
cd jetix-os

# 2. Зависимости
pip install groq pyyaml mutagen        # + anthropic, если идёшь по API-пути

# 3. Ключи — ТОЛЬКО через env var, НИКОГДА в файлах
export GROQ_API_KEY=...                 # обязателен (транскрипция)
# CC-headless путь: ничего больше не нужно (Max-подписка через `claude` в PATH)
# API путь:  export JETIX_LLM_BACKEND=api && export ANTHROPIC_API_KEY=...

# 4. Тест захвата
cp sample.ogg inbox/voice/
python3 tools/transcribe.py             # → raw/transcripts/sample.txt

# 5. Тест конвейера
bash tools/run_pipeline.sh              # → ~/summary-latest.md
# ревью → bash tools/run_filter.sh      # → reports/review_<date>.md
```

### Адаптация под себя

- **Telegram-bot мост** (chat → `inbox/voice/`): отдельный setup ~2 часа (не часть основного кода;
  это upgrade-кандидат, см. Phase 2 §B.3).
- **Линза** (Filter 2): копируешь `voice-pipeline-lens-template.yaml`, заполняешь под свой фокус.
- **Wiki-схема**: форкаешь структуру `wiki/` (9 типов) + адаптируешь под свои домены; правишь
  12 категорий в `extract.py` SYSTEM_PROMPT под свою таксономию.
- **Контекст проектов**: `config/context.md` (через sync_context.py из своих projects.json и т.д.) —
  даёт extraction знание твоих проектов для точного тегирования.

### Дисциплина (company-as-code)

- Ключи — только env var, **никогда** в файлах (audit `grep -rEn 'API_KEY' <files>` → 0 hits перед коммитом).
- Каждое изменение KB = структурный git-коммит (`[area] verb what (why)`).
- Откат через `git revert`, не `--force`.
- Append-only логи; не overwrite историю.

---

## §F.7 Где читать дальше (в репозитории)

| Путь | Что там |
|---|---|
| `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md` | canonical design (7 stages + lens) |
| `tools/transcribe.py` / `extract.py` / `filter.py` / `summarize.py` / `review_report.py` | сам код |
| `tools/lib/cc_helper.py` | backend-механика (cc-headless / api) |
| `tools/voice-pipeline-orchestrator.py` | reusable lens-driven pipeline |
| `config/voice-pipeline-lens-template.yaml` | шаблон линзы |
| `CLAUDE.md → Wiki Architecture v2` | структура базы (9 типов, edges) |

---

*Phase 6 closure. Технический стек разобран точно: компоненты / файлы / модели / пути /
последовательность с двумя human-gate / стоимость по двум backend'ам / ограничения и провалы /
полный re-implementation гайд. Главная корректировка — backend по умолчанию CC-headless (Max-sub,
без API-ключа), Whisper large-v3. Дальше — Phase 7: 4 mermaid VP-1..VP-4 + сводный main + SUMMARY.*
