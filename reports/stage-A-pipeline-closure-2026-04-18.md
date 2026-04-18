---
title: Stage A — Pipeline Closure Report (2026-04-18)
date: 2026-04-18
type: pipeline-closure
stage: A
step: 1
status: ready-for-human-gate
model: claude-opus-4-7
tags: [raw, pipeline, voice-memos, stage-A]
---

# Stage A — Pipeline Closure Report

**Дата:** 2026-04-18
**Шаг Notion:** 🗂️ Шаг 1 — Обработка заметок + Инвентаризация
**Стадия:** A (Pipeline full re-run)

## 1. Объём корпуса

| Слой | До (15-04) | После (18-04) | Δ |
|---|---|---|---|
| .ogg файлов в `raw/voice-memos/` | 73 | 106 | +33 |
| транскриптов в `raw/transcripts/*.txt` | 73 | 106 | +33 |
| extraction JSON в `inbox/processed/extractions/*.json` | 73 | 106 | +33 |
| filter batches в `inbox/processed/filtered/` | 1 (`batch_2026-04-15.json`) | 2 (+`batch_2026-04-18.json`) | +1 |
| Сумма items на входе filter | 380 | 560 | +180 |
| Output items последнего batch | 24 (Sonnet) | 449 (Opus 4.7) | см. раздел 4 |

**Total output в review (оба batches):** 473 items (24 старых + 449 новых).

## 2. Использованная модель

- **transcribe.py** — Groq `whisper-large-v3` (language=ru), без изменений
- **extract.py** — без изменений (модель из файла extract.py не трогалась)
- **filter.py** — **claude-opus-4-7** ✅ (переключено с `claude-sonnet-4-20250514`, commit `02dc3d1`)
- **review_report.py** — без моделей, детерминированный генератор

Confirmation что Opus реально использовался:
`batch_2026-04-18.json.model = "claude-opus-4-7"` ✅

## 3. Timing

| Шаг | Время | Комментарий |
|---|---|---|
| transcribe.py (33 файла) | 49 сек | Groq Whisper, все 33 файла OK |
| extract.py (33 файла) | 328 сек (5 мин 28 сек) | все 33 OK |
| filter.py (560 items → 12 батчей по 50) | 1237 сек (20 мин 37 сек) | 10 из 12 батчей OK, 2 упали (см. раздел 5) |
| review_report.py | <1 сек | детерминированный |
| **Итого** | **~26 мин** | |

## 4. Распределение output items по проектам (новый batch_2026-04-18.json)

Всего: **449 items** на выходе filter (Opus 4.7).

| Project | Items | % |
|---|---|---|
| Быстрые деньги | 122 | 27% |
| AI-инструменты | 84 | 19% |
| null (без проекта) | 79 | 18% |
| Сообщество | 78 | 17% |
| Бренд | 53 | 12% |
| Life OS | 29 | 6% |
| Ресёрч | 4 | 1% |

**Распределение по horizon:**
- now: 284 (63%)
- backlog: 165 (37%)

**Распределение по priority:**
- high: 231 (51%)
- medium: 191 (43%)
- low: 27 (6%)

**Распределение по category (топ):**
- Задачи: 123
- Стратегические гипотезы: 62
- Видение: 50
- Принципы: 48
- Инсайты: 41
- Личные наблюдения: 33
- Идеи: 31
- Решения: 28
- Идеи для проектов: 23
- Открытые вопросы: 7
- Контакты: 2
- Ресурсы: 1

**Meta-analysis:** key_themes=57, contradictions=32, patterns=43, key_findings=53.

## 5. Known issues / skips

### 5.1 Два батча filter упали с JSON parse error

- **Batch 2** (items 51-100): `Expecting property name enclosed in double quotes: line 609 column 5` → `raw_error_20260418_165656_199523.txt` (33 KB)
- **Batch 3** (items 101-150): `Expecting property name enclosed in double quotes: line 575 column 5` → `raw_error_20260418_165841_072752.txt` (31 KB)

**Эффект:** ~100 input items из 560 (batch 2+3) не прошли через merge/dedup Opus. То есть на выходе 449 items покрывают ~460 дошедших до merge items из 12 батчей (10 OK). Items из упавших батчей **не попали** в `batch_2026-04-18.json` и в review.

**Что это значит для Ruslan'а:** первые ~100 items корпуса (аудио ~393-420, самые ранние из корпуса, не новые) могли пропасть из этого прохода. Но они остались в `inbox/processed/extractions/` — ничего не потеряно on disk. Можно сделать повторный прогон только по этим батчам или починить парсер `extract_json` в filter.py (он падает когда Opus возвращает валидный JSON с trailing comments / trailing commas).

**Рекомендация:** если 100 потерянных items критичны для human-gate A.4-A.5 — добавить ретрай в `call_model` (одна повторная попытка с более строгой директивой "без markdown, без комментариев"), либо упростить схему выхода.

### 5.2 Review считает 473 items (не 449)

`review_report.py` аккумулирует все `batch_*.json` из `inbox/processed/filtered/`. В папке сейчас два batch: старый 15-04 (24 items, Sonnet) + новый 18-04 (449 items, Opus). Итого 473. Это нормальное поведение — Ruslan видит полную историю.

### 5.3 Архитектурное наблюдение — Opus 4.7 vs Sonnet 4

На том же корпусе:
- Sonnet 4 (15-04, 380 items входа): **24 output** — агрессивный dedup / merge
- Opus 4.7 (18-04, 560 items входа): **449 output** — очень консервативный, сохраняет почти всё

Это согласуется с system prompt ("сохраняй ВСЕ уникальные мысли, сливай только БУКВАЛЬНЫЕ дубли"). Opus буквальнее следует инструкции. Для дальнейших стадий (human gate → wiki ingest) это скорее плюс — меньше потерь нюансов; но для быстрого обзора 449 items читать дольше.

### 5.4 Файлы перемещены через inbox/voice/

33 новых `.ogg` были в `raw/voice-memos/` (архив), но `transcribe.py` ожидает свежие файлы в `inbox/voice/`. Перемещение было выполнено one-liner'ом (`comm -23 ogg_names txt_names | xargs mv`), после транскрибации скрипт сам вернул их обратно в `raw/voice-memos/`. Итоговое состояние `raw/voice-memos/` = 106 файлов, `inbox/voice/` пусто.

## 6. Артефакты

- `raw/transcripts/audio_462..494*.txt` — 33 новых транскрипта
- `inbox/processed/extractions/audio_462..494*.json` — 33 новых extraction JSON
- `inbox/processed/filtered/batch_2026-04-18.json` — **449 items + meta_analysis**, model=claude-opus-4-7
- `inbox/processed/filtered/raw_error_20260418_165656_199523.txt` — fail batch 2 (сохранён для debug)
- `inbox/processed/filtered/raw_error_20260418_165841_072752.txt` — fail batch 3 (сохранён для debug)
- `reports/review_2026-04-18.md` — полный markdown review по 473 items
- `~/review-latest.md` — копия для Ruslan'а (одна и та же)

## 7. Что сделано / что не сделано

**Сделано (per план Ruslan'а):**
1. ✅ Verify 106 .ogg
2. ✅ filter.py → Opus 4.7, отдельный commit
3. ✅ transcribe.py (33 новых)
4. ✅ extract.py (33 новых)
5. ✅ filter.py фулл-пасс на всех 106 (560 items на вход, 449 на выход; 2 батча упали — см. 5.1)
6. ✅ review_report.py → review_2026-04-18.md + ~/review-latest.md
7. ✅ Этот отчёт
8. ⏳ git commit + push — следующий шаг

**Не сделано (human gate по плану):**
- ❌ `/ingest` в wiki/ — human gate A.4-A.5, Ruslan делает отдельно
- ❌ записи в strategy/ decisions/ projects/

## 8. Следующие шаги для Ruslan'а

1. Открыть `~/review-latest.md` (473 items, markdown table по категориям)
2. Human gate A.4: утвердить/отклонить items
3. Human gate A.5: запустить `/ingest` на утверждённых items → wiki/
4. Опционально: починить 2 упавших батча filter (см. 5.1), если 100 items из ранних audio (393-420) критичны
