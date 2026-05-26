---
title: Phase 0 — Substrate read + Tseren context internalize
date: 2026-05-26
type: phase-report
parent_prompt: prompts/voice-pipeline-public-v2-2026-05-26.md
parent_main: decisions/strategic/VOICE-PIPELINE-PUBLIC-V2-2026-05-26.md
phase: 0
F: F2-F3
G: prompt-voice-pipeline-public-v2-2026-05-26
language: russian primary
---

# Phase 0 — Substrate + контекст Церена

> Этот отчёт фиксирует, что прочитано перед написанием публичного описания voice-pipeline,
> какой контекст у запроса (письмо Церена), и — важное — какие **расхождения** между первым
> черновиком и реальным кодом обнаружены. Эти расхождения определяют главное, что V2 исправляет.

---

## §1 Что прочитано (substrate)

| Источник | Что взято |
|---|---|
| `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md` | canonical design: 7 stages, lens-config механика, reusability принцип «pipeline стабилен, линза конфигурируема» |
| `tools/transcribe.py` | **факт:** Groq `whisper-large-v3`, lang=`ru`; вход `inbox/voice/`, архив `raw/voice-memos/`, выход `raw/transcripts/` |
| `tools/extract.py` | **факт:** Claude `sonnet-4-6`, **12 категорий** (не 5); опциональный `crm_items[]`; backend = CC headless по умолчанию |
| `tools/filter.py` | **факт:** Claude `opus-4-7`; батчи по 50 (threshold 100); partial-save отказоустойчивость (resume/restart) |
| `tools/summarize.py` | **факт:** `sonnet-4-6`; сохраняет 100% единиц, без dedup; пишет `~/summary-latest.md` |
| `tools/review_report.py` | **факт:** filtered → `reports/review_<date>.md` + `~/review-latest.md`; markdown-таблицы по категориям |
| `tools/run_pipeline.sh` | **факт:** steps 0→3 (sync_context → transcribe → extract → CRM-route → summarize), затем **СТОП** |
| `tools/run_filter.sh` | **факт:** второй проход после ревью (filter → review_report), затем **СТОП** |
| `tools/lib/cc_helper.py` | **факт:** backend по умолчанию = `cc-headless` (`claude -p` через Max-подписку, без API-ключа); `JETIX_LLM_BACKEND=api` = legacy fallback |
| `tools/voice-pipeline-orchestrator.py` | **факт:** реализует 7-stage канон, Stage 6 = lens-driven фильтр по `--lens <yaml>` |
| `config/voice-pipeline-lens-template.yaml` + `…-2026-05-10-tseren.yaml` | **факт:** линза = реальный конфиг (3 tier keywords + scoring weights + threshold + top-N) |
| первый DRAFT `VOICE-PIPELINE-PUBLIC-DESCRIPTION-2026-05-26.md` | основа структуры разделов; расширяется и **исправляется** (см. §3) |
| `LETTER-TO-TSEREN-RESPONSE-2026-05-26.md` | контекст: зачем документ нужен (явный запрос Церена) |
| `JETIX-WORKSHOP-MASTERY-NETWORK-CONCEPT-2026-05-26.md` | рамка: pipeline = «станок на стене Мастерской», инструмент Мастерства #13 |
| `PREPARATION-STAGE-CONCEPT-SUPPLEMENT-2026-05-26.md` | Extended Method §J 8-step: где pipeline сидит (Step 2 prep-execution = AI HEAVY) |

---

## §2 Контекст Церена (зачем этот документ)

Церен (Managing Partner МИМ / связан с ШСМ-кругом Левенчука) ответил на предложение партнёрства
**холодным отказом** с тремя точками критики:

1. **Парадигмы расходятся** — triple-role 10%×12 мес ближе к network-marketing, чем к кооперативу.
2. **Зрелость материала** — «1930 коммитов за 43 дня одним автором + LLM-конвейер»; Tier A = в
   основном synthesis известного (Левенчук / Mondragón / Ericsson / Dweck); зрелости для партнёрств нет.
3. **Срочности нет.**

Но Церен **явно попросил**: «voice-pipeline — это интересно; пришлите 1-2 страницы текста — на текст
отвечу». Это единственная открытая дверь. Документ V2 = substance-ответ на этот запрос + foundation
для любого будущего методолога.

**Позиция документа (не споря с критикой):**
- НЕ rebuttal. НЕ маркетинг. Substance-only, per Founder-as-Exhibit (Руслан = первый пользователь
  системы, которую сам построил).
- Честная инверсия критики «43 дня»: Jetix-**репозиторий** новый (40+ дней), но **substrate работы —
  год+** (1100+ заметок до репо, жили в Notion / personal vault). Acceleration ≠ initiation. Это
  раскрывается в Phase 5.
- Честное наследование (R6): Дарвин / да Винчи / Луман / Forte / Karpathy — references, не «революция».

---

## §3 ⚠️ Расхождения первого DRAFT с реальным кодом (что V2 исправляет)

Первый черновик (Cloud Cowork) содержал фактические ошибки про собственный стек. V2 их правит — это
особенно важно для аудитории методологов, которые могут пойти читать код:

| # | Первый DRAFT говорил | Реальный код говорит | Почему важно |
|---|---|---|---|
| 1 | «через Claude API (Sonnet 4 sub)» | **backend по умолчанию = CC headless** (`claude -p` через Max-подписку, **без API-ключа**); API = legacy `JETIX_LLM_BACKEND=api` | Это сознательный выбор: Max-подписка покрывает вызовы, нет переменной стоимости за токены через API. Меняет всю «cost»-секцию |
| 2 | «Groq Whisper Medium baseline; Large для critical» | `MODEL = "whisper-large-v3"` всегда | Large-v3 = baseline, не опция. Точность выше, чем заявлял черновик |
| 3 | «4 stage pipeline» | **2 фазы с 2 СТОП-точками**: run_pipeline (0-3) → ревью → run_filter (filter+report) → ревью → ручная дистрибуция | Архитектура честнее: два human-gate, не один |
| 4 | «ideas / decisions / questions / facts / tasks» (5 типов) | **12 категорий** (Видение / Решения / Инсайты / Стратегические гипотезы / Задачи / Идеи для проектов / Идеи / Открытые вопросы / Контакты / Ресурсы / Личные наблюдения / Принципы) | 12 категорий = то, что делает это «книжечкой наблюдений» Дарвина, а не просто to-do |
| 5 | filter = Sonnet | filter = `opus-4-7`; extract/summarize = `sonnet-4-6` | Разные модели на разных стадиях (дешевле на extraction, умнее на meta-analysis) |
| 6 | не упоминал | **CRM voice-routing** (step 2b) → `<slug>-DRAFT.md`, DRAFT-only | Это часть pipeline; голос → черновик контакта, никогда не auto-overwrite |
| 7 | lens упомянут вскользь | **lens-driven Filter 2 = реализован** (orchestrator Stage 6 + lens YAML); «двойная фильтрация» = ядро | Это и есть «инструмент изобретателя» — Ruslan voice insight #3 |

**Вывод Phase 0:** V2 пишется не как расширение черновика, а как его **корректная замена** —
с реальными путями, моделями, backend'ом и двухстадийной механикой. Это критично для credibility:
методолог, открывший `tools/`, должен увидеть ровно то, что написано в описании.

---

## §4 7 voice-insight'ов Руслана 26.05 (internalized)

1. **Цепочка ценности** — телефон всегда с собой → ~100% интересных идей ловятся (прогулка / поездка /
   очередь / перед сном — моменты, обычно потерянные для capture). → Phase 1 §A.
2. **Telegram inbox split** — 3 части (Рефлексия / Видение / Per-проектные чаты) + единый inbox для
   видео / статей / контактов / внешних материалов. → Phase 2 §B.
3. **Это БД на wiki (Karpathy-style), не «заметки»** + **двойная фильтрация**: Filter 1 (интеграция в
   существующую wiki) + Filter 2 (lens-driven — «вопросы недели» / «текущий фокус» / «гипотеза»). →
   Phase 3 §C (центральная).
4. **Инструмент исследователя-изобретателя** — фиксируются вопросы + наблюдения + гипотезы +
   опровержения; reference Дарвин / да Винчи (книжечки наблюдений); ускорено Claude Code. → Phase 4 §D.
5. **Personal context** — год+ работы, 1100+ заметок до Jetix-репо; миграция Notion → open server CC;
   НЕ 40-дневный проект. → Phase 5 §E.
6. **Технический stack** — конкретные documents + programs + готовые шаблоны для re-implementation. →
   Phase 6 §F.
7. **Стиль** — плотненько / красивенько / 3-4 mermaid. → Phase 7 (VP-1..VP-4).

---

## §5 Constitutional posture (этот документ)

- **R1 surface only** — рой компилирует substrate; финальная prose + решение о публикации = Руслан.
- **R2 STRICT** — Foundation-пути (Parts 1-11, principles/, schemas/) не тронуты; это публичное описание.
- **R6 honest inheritance** — Дарвин / да Винчи / Луман / Forte / Karpathy явно; никакой «революции».
- **R11** — никаких auto-действий; релиз = ack Руслана. Pool result, NO auto-launch.
- **R12 paired-frame** — substance-only; free-share / fork-friendly; никакой манипуляции.
- **Append-only** — V2 = новый файл; первый DRAFT сохранён (superseded, не удалён).

---

*Phase 0 closure. Substrate прочитан, 7 расхождений первого DRAFT зафиксированы, контекст Церена
internalized. Дальше — Phase 1 §A Цепочка ценности.*
