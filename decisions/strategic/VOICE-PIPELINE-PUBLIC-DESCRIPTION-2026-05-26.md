---
title: Voice Pipeline — практика быстрой фиксации мысли (public description for methodologists)
date: 2026-05-26
type: public-description-voice-pipeline
authored_by: brigadier-scribe (Cloud Cowork) draft → Ruslan prose review
audience: Церен (Tseren) + любой методолог-интересант
prose_authored_by: ai-draft → ruslan-ack pending
F: F2-F3
G: voice-pipeline-public-description
constitutional_posture: R1 surface only (draft) + R12 honest acknowledgment limitations + R11 + append-only
language: russian primary
status: DRAFT — Ruslan R1 prose pass требуется для finalisation
length_target: ≤2 страницы text (per Церен ask)
---

# Voice Pipeline — практика быстрой фиксации мысли

## Какие проблемы решает

**Главная:** разрыв между скоростью мышления (голосом — 150-200 слов/мин) и скоростью письма (30-50 слов/мин). Когда думаешь быстрее, чем пишешь, идеи теряются. Voice-pipeline закрывает этот gap — мысль фиксируется в момент возникновения, дальше обрабатывается асинхронно.

**Сопутствующие:**
- **Preserve nuance:** дословная фиксация (F2 anchor) — verbatim хранится, потом из него synthesis (F3) делается; контекст не теряется при пересказе
- **Asynchronous batch processing:** диктовка занимает минуты, обработка — отдельный шаг (час спустя / следующий день)
- **Capture без context switch:** мысль зафиксировал → продолжил делать что делал (не залип на «как сформулировать»)
- **Substrate для compound learning:** накопленные voice notes = персональный корпус для re-derivation insights позже

## Архитектура (4 stage pipeline)

```
audio (OGG/MP3) → транскрипция → extraction → filter/dedup → review report → manual KB distribution
```

**Stage 1 — Транскрипция:** Wispr Flow на input стороне (Windows) → текст напрямую в любое окно ИЛИ файл; для batch — `tools/transcribe.py` через Groq Whisper API (быстрее и дешевле OpenAI Whisper; ~$0.001 за минуту аудио).

**Stage 2 — Extraction:** `tools/extract.py` через Claude (Sonnet 4 sub) — vyтягивает structured items из транскрипта: ideas / decisions / questions / facts / tasks; per-item metadata (topic / project / urgency).

**Stage 3 — Filter + dedup:** `tools/filter.py` через Claude — кросс-batch deduplication (если та же мысль появилась в нескольких записях), meta-analysis (cluster topics), priority signals.

**Stage 4 — Review report:** `tools/review_report.py` → markdown отчёт в `reports/review_YYYY-MM-DD.md` + копия `~/review-latest.md`. **СТОП.** Человек читает, принимает решения.

**Stage 5 — Manual distribution:** дистрибуция items в KB (wiki / decisions / strategic / CRM) делается **вручную** ИЛИ отдельной командой по acked items. `tools/distribute.py` архивирован (`.bak`) — НЕ автоматически — чтобы Claude-выводы не попадали в knowledge base без человеческого ревью.

Plus: один-shot dictation в Wispr → текст в чат → синхронный обработчик через Claude Code skill → структурированный результат напрямую в нужный файл (для коротких записей; обходит batch pipeline).

## Конкретные tools / paths

- **Wispr Flow** (Windows desktop) — push-to-talk; локальная транскрипция
- **`tools/transcribe.py`** — OGG/MP3 batch → Groq Whisper API
- **`tools/extract.py`** — Claude API структурное извлечение
- **`tools/filter.py`** — Claude API meta-analysis + dedup
- **`tools/review_report.py`** — markdown отчёт generation
- **`tools/run_pipeline.sh`** — orchestrator stage 1→2→3→4
- Per agent skill: `/ingest`, `/extract-from-voice` (Claude Code skills) — ad-hoc inline calls

Living code: открытый репозиторий, `tools/` директория.

## Ограничения (honest acknowledgment)

**Voice ≠ peer-review:** результат — персональный voice-to-canon, не methodology validated третьей стороной. Это substrate, не peer-reviewed knowledge. Для перехода в peer-reviewed нужен отдельный shaping process (что и идёт через partner discovery calls + iteration loops; но не часть pipeline самого).

**LLM может пропустить нюанс:** Claude extraction периодически теряет сарказм / иронию / двойной смысл / context-dependent отсылки. Mitigation: F2 verbatim хранится всегда (raw text), синтез F3 derivative — можно вернуться к verbatim для re-extraction если нужно.

**Стоп-точка обязательна:** automated distribution to KB **отключена намеренно** (per voice-pipeline DRAFT-only discipline). Без human review между Stage 4 и Stage 5 — knowledge base загрязняется некалиброванными items. Это constitutional rule (Pillar C Tier 2), не optional.

**Голосовые ответы не равны мысли:** диктовка имеет filler words / повторы / самокоррекции / иногда completely meandering / иногда incoherent. Pipeline предполагает что 30-50% контента это noise, фильтруется на extraction stage.

**Batch lag:** между записью и обработкой — часы или дни. Если нужна немедленная reaction (live brainstorm с командой) — pipeline не подходит; нужен синхронный путь (Wispr → текст в чат → ответ).

**Cost не нулевой:** Groq Whisper + Claude API → ~€2-5/день при активном использовании (10-15 voice notes/день). Budget cap €10/день hard.

**R12 voice DRAFT-only:** voice items НЕ имеют права авто-overwrite production records (CRM contacts / strategic decisions / canonical wiki). Только draft со status `draft_from_voice`, ручное promote после review.

## Что не сработало

**Auto-distribute (Stage 5 automation):** `tools/distribute.py` запускался autonomously в первой итерации; через неделю Claude-extracted items стали накапливаться в KB как «канонические» — но при ручной проверке выяснилось что 40-60% items это «звучит правильно но не точно». Архивировали в `.bak`. Manual review между Stage 4 и 5 — non-negotiable.

**IWE chat как помощник (tested):** пробовали Aisystant IWE chat как дополнительный обработчик после Stage 3 — качество ответа ниже direct Claude (extra layer не добавлял value, добавлял latency и costs). Отказались. Использовали как реference канона МИМ (read-only).

**Stage 5 v2 BM25 + Russian morphology iteration:** добавляли autosuggest для distribution targets (KB folder per item) через BM25 + morphology — match rate вышел 50.1% → 60.1% после tuning, но всё равно требует human ack per item; suggesting улучшил workflow на ~30% (быстрее ack), но не закрыл human-in-the-loop discipline.

**Whisper для русского с акцентом:** OpenAI Whisper для русского — periodically misheard rare termin / Anglicism. Groq Whisper marginally better. Whisper Large v3 — best, но cost ×3-5. Settled на Groq Whisper Medium как baseline; для critical record можно re-run на Large.

## Use cases (где работает / где не работает)

**✅ Где работает:**
- Daily voice journal (5-15 мин записей вечером) → review утром → ack/distribute selected items
- Strategic dictation (часовая диктовка в один файл) → multi-stage extraction → structured strategic substrate
- Voice notes из прогулки (walking-and-thinking) → late-batch review
- Idea capture в момент возникновения (Wispr inline в любое окно)

**❌ Где не работает:**
- Real-time multi-party brainstorm (нужны другие tools)
- Technical specifications где precision critical (manual write лучше)
- Legal / contract drafting (precision + reviewability требуются)
- First-time meeting transcript с unknown people (extraction context-dependent)

## Если хотите попробовать

Open-source: репо `Bogersebekov/jetix-os`, ветка `main`, директория `tools/` + `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md` (canonical design doc).

Минимум для воспроизведения: Python 3 + Groq API key + Anthropic API key + Wispr Flow (или любой другой Whisper-based dictation app).

Cost expectation: €2-5/день активной работы; €30-50/мес при daily use.

---

*Описание ≤2 страницы text per Церен ask. F2-F3 derivative (existing system documentation). Honest acknowledgment of limitations. Living code в open repo.*
