---
title: Deep study FPF + IWE + Левенчуковский intellect-stack — Phase A collection + distillation
date: 2026-05-17
type: deep-prompt
target: server CC (Claude Code CLI, autonomous Plan Mode, 8-11h)
trigger: внешнее сообщение Левенчука 2026-05-17 (inbox/levenchuk-tg-2026-05-17.md)
parent_brief: https://www.notion.so/3622496333bf81e181a4f8fa2f043187
launch_command: |
  cd ~/Desktop/jetix-os && claude -p < prompts/fpf-iwe-levenchuk-deep-study-2026-05-17.md
language: russian
---

# DEEP PROMPT — Phase A: Levenchuk corpus collection + FPF/IWE distillation

> **Кто ты.** Server CC (Claude Code) на Windows-машине Руслана, работающий в `~/Desktop/jetix-os` (main branch). Repo доступен полностью. Constitutional posture: Tier 2 R1 (surface'инг + analytical pull-up, не authoring strategy), R2 (никаких Foundation path writes без AWAITING-APPROVAL packet), R6 (provenance per item — file path + line refs), R11 (Default-Deny на uncategorized actions), append-only для всех outputs.

> **Контекст триггера.** 17.05.2026 Левенчук прислал в TG критическое сообщение (см. `inbox/levenchuk-tg-2026-05-17.md`). Основные claims (C1-C7 в том файле): FPF = один документ `github.com/ailev/FPF`; FPF содержит принципы мышления и интеллекта; наша 5-месячная работа = «память + автоматизация» = vanilla AI; IWE Цэрэна = production-applied FPF; затраченные часы ≠ достижения; invite в резидентуры ШСМ.

> **Цель Phase A.** Собрать ВСЕ Левенчуковские материалы (платные / бесплатные / закрытые / открытые), извлечь принципы мышления и интеллекта на человеческом языке, построить плотные схемы. Без selection «что важно / что нет» — surface'инг. Phase B (integration plan + benchmark + ответ Левенчуку) — отдельный prompt после ack Ruslan-ом Phase A результатов.

---

## §0 Constitutional posture (read first)

- **Tier 2 R1.** Ты scribe + structurer + analyst. Не authoring strategy. Ruslan = sole strategist. Все выводы surface'инг, не «рекомендую X».
- **Tier 2 R2.** НЕ touch'ать Foundation paths (`swarm/wiki/foundations/`, `principles/`, `shared/schemas/`, `.claude/config/`) без AWAITING-APPROVAL packet через Part 6b gate.
- **Tier 2 R6.** Provenance per item. Каждое утверждение в твоём output = (source_url + retrieved_date) ИЛИ (file_path + line_range + commit SHA).
- **Tier 2 R11.** Default-Deny на uncategorized actions. Если непонятно — halt + log + ask.
- **Append-only.** Все outputs в `raw/external/levenchuk-corpus-2026-05-17/` и `reports/fpf-iwe-distillation-2026-05-17/` создаются как new files. Старые НЕ редактируются.
- **NO API keys.** Все LLM calls через `claude -p` headless. НЕ touch'ать `ANTHROPIC_API_KEY`. Cost cap €10/день для external services.
- **NO unsolicited alternatives.** Левенчуковский подход = canonical. Если у нас отличается — surface разницу как факт, не «лучше Y».
- **Format check перед каждым commit:** убедиться что нет «§РЕКОМЕНДАЦИИ» / «следует» / «лучше» / triage what's relevant. Только descriptive + structural.

---

## §1 ЭТАП 1 — Inventory всех источников (план перед действием)

### §1.1 Цель этапа

До любого скачивания — построить полный inventory Левенчуковских материалов. Без selection. Платное + бесплатное + закрытое + открытое. Зафиксировать ГДЕ каждый источник и КАК к нему достучаться.

### §1.2 Категории источников (минимум, расширить если найдёшь больше)

1. **GitHub каноны:**
   - `github.com/ailev/FPF` — FPF spec (уже в repo: `raw/external/ailev-FPF/FPF-Spec.md`, 62202 стр + README + ATTRIBUTION). Проверить freshness vs upstream.
   - Другие репо `ailev/*` если есть — `github.com/ailev?tab=repositories` (listing)

2. **Блог ailev.livejournal.com:**
   - Полный архив постов (с 2003+). Tags: intellect-stack, мышление, методология, OntoLern, ПравТех, FPF, IWE, U.Episteme.
   - Архивирование: web scrape (полные тексты + метаданные)

3. **ШСМ / Школа системного менеджмента (бесплатные материалы):**
   - system-school.ru — публичная часть
   - youtube.com/@ailev — лекции
   - vimeo.com/ailev (если есть)

4. **Aisystant — платные курсы ШСМ:**
   - aisystant.system-school.ru
   - Каталог курсов (минимум: «Системное мышление», «Системный менеджмент», «Инженерия интеллекта», «Методология»)
   - Resourceintensive — Ruslan может заплатить за подписку (€/мес). Иначе — публичные описания + transcript outlines + любые leaked materials в OSS.
   - **Residence «рабочего развития»** (упомянуто Левенчуком в TG) — что это, формат, цена, syllabus.

5. **Книги Левенчука:**
   - «Системное мышление 2019/2020/2021» (множественные редакции)
   - «Образование для образованных»
   - «Системный фитнес»
   - «Инженерия интеллекта»
   - «Методология»
   - Любые сборники / антологии
   - **Где взять:** Ridero / Litres / Amazon / OSS scans / aisystant
   - В repo уже: `raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-full-body-of-work.md` — проверь что там зафиксировано

6. **Telegram канал @ailev_blog (если есть) + публичные посты в @ailev:**
   - Архив через tdlib / web export

7. **Academia / ResearchGate / ORCID — научные публикации Левенчука:**
   - INCOSE talks
   - OMG conference talks
   - Любые формальные публикации

8. **Цэрэновские IWE-материалы:**
   - МИМ (Мастерская Инженеров-Менеджеров) сайт — что есть про IWE
   - YouTube @TserenTserenov + публичные лекции
   - В repo уже: `raw/research/2026-04-28-tseren-yt-export/`, `raw/research/2026-04-28-tseren-tg-export/`
   - IWE-специфические материалы — search по transcripts

9. **Третьесторонние discussions:**
   - Habrahabr ailev tag
   - Vc.ru — статьи о ШСМ
   - Reddit / Hacker News — discussion threads

10. **Все мы уже имеем в repo:**
    - `raw/research/levenchuk-deep-research-2026-04-18.md`
    - `raw/research/levenchuk-for-ai-deep-research-2026-04-19.md`
    - `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md`
    - `raw/research/fpf-gap-analysis-2026-04-20.md`
    - `raw/research/levenchuk-fpf-research-2026-04-20/` (директория)
    - `raw/research/step-2-2-2-extractions/A-fpf-spec-5-primitives.md`
    - `raw/external/ailev-FPF/`
    - `profiles/l1-first-clan/anatoliy-levenchuk.md`

### §1.3 Output этапа 1

Файл: `raw/external/levenchuk-corpus-2026-05-17/00-INVENTORY.md`

Структура:
```
# Levenchuk corpus inventory — 2026-05-17

## §1 Source list (numbered, exhaustive)
[per источник: ID / URL / тип (paid/free/closed/open) / формат (md/pdf/youtube/etc) / volume estimate / access method / status (existing-in-repo / to-collect / blocked)]

## §2 Access plan
[per источник: какой инструмент (git clone / wget / yt-dlp / web scrape / manual purchase / etc), какие credentials нужны, какие dependencies]

## §3 Blockers (что нужно от Ruslan)
[paid subscriptions / closed materials / manual access]

## §4 Volume + cost estimate
[total volume в страницах + cost для paid materials в €]
```

### §1.4 Stop condition

Inventory не должен пропустить ни одного известного канала Левенчука. Если ты не уверен — добавь в §3 Blockers как «verify with Ruslan».

---

## §2 ЭТАП 2 — Collection (выполняем согласно §1 inventory)

### §2.1 Правила сбора

- **Append-only.** Все downloaded files в `raw/external/levenchuk-corpus-2026-05-17/`. Имена файлов: `{source-id}-{slug}-{date}.{ext}`.
- **Provenance.** К каждому файлу — `.meta.yaml` соседом: `{url, retrieved_at, retrieved_by, original_title, license, sha256}`.
- **Лицензии.** Перед commit'ом — проверить лицензии. CC0/BY-SA — ok, копируем целиком. Proprietary (книги, курсы) — только metadata + outlines + позволенные fair-use цитаты, не full content. ATTRIBUTION.md в каждой sub-папке.
- **Платные источники.** Если требуется purchase / subscription — STOP, добавить в `blockers.md`, перейти к следующему. Не пытайся обходить paywall.
- **Closed source code курсов.** Если open enrollment без подписки даёт outline — забираем outline. Full course content — только если Ruslan явно дал ack.

### §2.2 Объём (target)

- GitHub: 100% (mirror + diff vs наша copy)
- LiveJournal blog: 100% public posts (с 2003-2026)
- YouTube ailev: transcripts всех videos (yt-dlp + auto-sub или whisper transcribe)
- Books: outlines + tables of contents + любые позволенные excerpts. Ruslan separately решает что покупать.
- Aisystant / Resi residence: public descriptions only без ack
- Tseren IWE: уже частично в repo, дополнить

### §2.3 Output этапа 2

- `raw/external/levenchuk-corpus-2026-05-17/01-github/` — mirror
- `raw/external/levenchuk-corpus-2026-05-17/02-livejournal/` — посты + индекс
- `raw/external/levenchuk-corpus-2026-05-17/03-youtube/` — transcripts
- `raw/external/levenchuk-corpus-2026-05-17/04-books-outlines/` — TOC + excerpts
- `raw/external/levenchuk-corpus-2026-05-17/05-aisystant-public/` — public descriptions
- `raw/external/levenchuk-corpus-2026-05-17/06-tseren-iwe/` — Цэрэновские IWE materials
- `raw/external/levenchuk-corpus-2026-05-17/07-third-party-discussions/` — Habr / vc.ru / etc.
- `raw/external/levenchuk-corpus-2026-05-17/blockers.md` — что не удалось / требует Ruslan ack
- `raw/external/levenchuk-corpus-2026-05-17/MANIFEST.md` — final inventory с volumes

---

## §3 ЭТАП 3 — Distillation на человеческом языке

### §3.1 Что выжать

Из всего собранного корпуса извлечь:

1. **FPF в одной фразе** — что это, по Левенчуковскому собственному определению (verbatim citation)
2. **FPF в одном абзаце** — расширенное определение
3. **5+ primitives FPF** — каждый primitive: definition + role + example + cross-refs
4. **Core mechanisms FPF:** IP-1 (Role≠Executor) / IP-2 / IP-3 / IP-7 / A.6.B / A.14 / B.3 — каждый: что делает, почему важен, как используется. Verbatim citations from FPF-Spec.md (`raw/external/ailev-FPF/FPF-Spec.md`) с line refs.
5. **Принципы мышления** (Левенчук's «принципы мышления и интеллекта, положенные в основу»):
   - Какие именно принципы
   - Откуда они (philosophy / cognitive science / system theory / methodology lineage)
   - Как они проявляются в FPF mechanisms
6. **Intelligence amplification mechanism** — конкретно, по шагам: как FPF превращает обычный thinking process в более качественный. Это **ключ к ответу на C3/C4 Левенчука**.
7. **U.Episteme** — что это, как соотносится с FPF (subset? container? lens?)
8. **IWE Цэрэна** — что это, как соотносится с FPF (Левенчук говорит: «там примерно всё так же устроено, но внутри интеллект опирается на FPF»). Концепт IWE + его FPF-связь.
9. **Intellect-stack** (Левенчуковский термин) — стек интеллекта по Левенчуку, слои, что в каждом слое
10. **17 transdisciplines / 17 трансдисциплин** — из ШСМ; что они, как организованы (`raw/research/step-2-2-2-extractions/C-17transdiscs-essence-holon.md` уже частично есть)
11. **Methodology lineage** — на ком Левенчук опирается (Wieringa, Dori, Bunge, Schön, etc.), что заимствует, что добавил своего
12. **Резидентуры рабочего развития** — формат, как идёт работа с participants, какие deliverables, какая методика

### §3.2 Стиль distillation

- **Человеческий язык.** Не academic jargon, не bullshit-структуры. Если Левенчук использует термин — оставляй термин, но объясни в скобках при первом use.
- **Verbatim citations** где возможно — Левенчуковские формулировки точнее наших.
- **Provenance per claim** — каждое утверждение со ссылкой `{file:line}` или `{url:retrieved_date}`.
- **No selection.** Не «вот важное / не важное». Surface'инг.
- **Контрасты vs наша система** — surface факты разницы (Левенчук: X. Мы: Y. Diff: Z.), без оценки «лучше/хуже».

### §3.3 Output этапа 3

Файлы в `reports/fpf-iwe-distillation-2026-05-17/`:

- `01-fpf-on-human-language.md` — пункты 1-6 §3.1
- `02-u-episteme-and-iwe.md` — пункты 7-8
- `03-intellect-stack-and-transdisciplines.md` — пункты 9-10
- `04-methodology-lineage.md` — пункт 11
- `05-residencies-format.md` — пункт 12
- `99-glossary-levenchuk-terms.md` — алфавитный glossary всех терминов Левенчука встреченных в корпусе

---

## §4 ЭТАП 4 — Mermaid-схемы (плотнейшим)

### §4.1 Что схематизировать

Минимум следующие mermaid-диаграммы (style guide: `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md`, Variant A cool blues):

1. **FPF top-level architecture** — primitives + mechanisms + flow
2. **FPF intelligence amplification workflow** — от raw input до improved decision, по шагам (это **ответ на C4 Левенчука**)
3. **U.Episteme structure** — как организован, что включает
4. **IWE = production-applied FPF** — где IWE использует FPF, где extends
5. **Intellect-stack по Левенчуку** — все слои, что в каждом
6. **17 transdisciplines holon** — иерархия / отношения
7. **Левенчуковский lineage tree** — на ком он опирается, что добавил
8. **Левенчуковский corpus map** — все материалы (paid/free/closed/open) с relationships
9. **FPF mechanisms ↔ Jetix presence** — где FPF mechanism упомянут в нашей системе (это **подготовка к Phase B audit**)
10. **C4 benchmark design** — visual схема A/B/C arms

### §4.2 Output

`reports/fpf-iwe-distillation-2026-05-17/diagrams/` — каждая mermaid в отдельном `.md` с source + rendered context. Style: cool blues per Variant A.

---

## §5 ЭТАП 5 — Honest self-audit (наша работа vs Левенчуковский bar)

### §5.1 Что зафиксировать

Без selection «good/bad». Surface'инг честных фактов:

1. **Где наша работа = «память + автоматизация»** (C3 Левенчука):
   - Foundation v1.0 (11 Parts + Pillar C) — это organizational substrate или intelligence amplification? Каждый Part — assess.
   - Wiki Architecture v2 — это knowledge storage или knowledge processing intelligence?
   - AutoResearch (Karpathy pattern) — это automation или intelligence amplification?
   - Voice pipeline — это transcription/triage или intelligence amplification?
   - Toggl tracking / time discipline — это «память + автоматизация» (=да, явно)
   - CRM — это «память + автоматизация» (=да)
   - Monetization bank 166 H — это intelligence или catalog?

2. **Где наша работа = intelligence amplification (Левенчуковский bar)**:
   - Strategic Insights Hexagon (6 insights 10-11.05) — это reasoning outputs или organizational decisions?
   - Document 1A / 1B — это applied thinking или structured org-design?
   - Если есть **уникальные** intelligence mechanisms у нас (которых нет в FPF) — surface их.

3. **Где наша работа = derivative interpretation FPF**:
   - `archive/design/JETIX-FPF.md` (3762 стр) — насколько derivative, что добавлено / изменено / искажено
   - Pillar C Tier 2 (12 rules) — это FPF-aligned или собственные правила
   - F-G-R / Default-Deny / AWAITING-APPROVAL — это FPF-derived или независимое
   - IP-1 Role≠Executor — это FPF mechanism или наша copy

### §5.2 Output

`reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md`

Формат — таблица:
```
| Наш компонент | Тип (memory/automation/intelligence/derivative) | Левенчуковский equivalent | Diff |
```

Без оценки. Только факт-сопоставление.

---

## §6 ЭТАП 6 — Summary для Ruslan (one-pager)

### §6.1 Содержание

Один markdown файл, ≤2000 слов, для Ruslan чтения за 15 минут:

- §1 Что нашли (top-line)
- §2 Что НЕ нашли / blockers (для Ruslan decisions)
- §3 Top-10 Левенчуковских формулировок (verbatim) которые меняют наше понимание
- §4 Top-5 mermaid диаграмм inline
- §5 Honest self-audit top-line (без drill-down)
- §6 Что готово для Phase B (integration plan + benchmark + ответ)
- §7 Open questions для Ruslan

### §6.2 Output

`reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md`

---

## §7 Порядок исполнения (строгий)

1. §1 Inventory — **DO NOT SKIP**, основа этапов 2-6
2. §2 Collection — параллельно где возможно (yt-dlp + git clone + web scrape — independent)
3. §3 Distillation — sequential после §2 (нужен полный корпус)
4. §4 Mermaid — параллельно §3 (на основе уже distilled материала)
5. §5 Self-audit — sequential после §3 + §4
6. §6 Summary — last, синтез всего

**Commits.** В конце каждого этапа — git commit с structured message:
```
[fpf-iwe-corpus] <этап N> — <короткое описание> (<volume / scope>)
```
Без push до конца Phase A. В конце — `git push origin main` (Cloud Cowork + Ruslan ack already explicit).

---

## §8 Что НЕ делать

- НЕ touch Foundation paths (R2)
- НЕ touch `private/`, `~/.ssh/`, `.env`
- НЕ обходить paywalls для платных Левенчуковских материалов — добавить в blockers.md
- НЕ удалять старые наши FPF-derived доки (`archive/design/JETIX-FPF.md` etc.) — append-only
- НЕ писать «§РЕКОМЕНДАЦИИ» / «следует» / «мы должны» / «лучше Y» — surface'инг, не authoring
- НЕ оценивать «Левенчук прав / неправ» — surface факты
- НЕ начинать Phase B (integration / benchmark / ответ Левенчуку) — это отдельный prompt после Ruslan ack
- НЕ генерировать AI bullshit-структуры если material тонкий — surface честно «корпус скудный, blockers X/Y/Z»
- НЕ перфекционить mermaid'ы — beta-первый, плотность > красота
- НЕ скачивать full content платных книг / курсов без Ruslan ack

---

## §9 Failure modes (если застрянешь)

- **Cost cap hit** (€10/день на external) → halt, log в blockers.md, switch на free sources, ждать Ruslan
- **Источник недоступен** (403 / paywall / closed) → log в blockers.md, продолжать с остальными
- **Distillation conflict** (две Левенчуковские формулировки противоречат) → surface как «contradiction found», не выбирать
- **Volume overflow** (корпус > expected) → продолжать exhaustive sweep, не sampling

---

## §10 Acceptance criteria для Phase A

В конце Phase A должны быть готовы:
- [ ] `raw/external/levenchuk-corpus-2026-05-17/00-INVENTORY.md` — exhaustive
- [ ] Collection in subdirs 01-07 (sources accessible without blockers)
- [ ] `blockers.md` — explicit list что нужно от Ruslan
- [ ] 6 distillation files в `reports/.../01-06-*.md`
- [ ] glossary
- [ ] 10+ mermaid diagrams
- [ ] honest self-audit
- [ ] `00-SUMMARY-FOR-RUSLAN.md` (≤2000 слов)
- [ ] git commits per этап
- [ ] git push origin main в конце

Ruslan читает SUMMARY → ack или course correct → Phase B prompt.

---

## §11 Phase B (preview — НЕ выполнять сейчас)

После Ruslan ack Phase A, отдельный prompt будет содержать:
- C4 benchmark execution (vanilla AI vs FPF-loaded AI vs наш stack — конкретные questions про Jetix)
- Integration plan FPF → Jetix (с AWAITING-APPROVAL packets per R2)
- Audit всех locked документов Jetix на FPF/IWE/Episteme присутствие
- Черновик ответа Левенчуку (Ruslan-authored, AI = structurer)

**НЕ начинать Phase B в этой сессии.**

---

## §12 Context файлы (что прочитать перед стартом)

Минимум:
- `inbox/levenchuk-tg-2026-05-17.md` — триггер
- `raw/external/ailev-FPF/FPF-Spec.md` — primary canonical source (НАЧИНАТЬ ОТ НЕГО)
- `raw/external/ailev-FPF/Readme.md` — companion
- `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md`
- `raw/research/fpf-gap-analysis-2026-04-20.md`
- `raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-full-body-of-work.md`
- `raw/research/step-2-2-2-extractions/A-fpf-spec-5-primitives.md`
- `profiles/l1-first-clan/anatoliy-levenchuk.md`
- `_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md`
- `CLAUDE.md` (constitutional posture refresher)

---

**Запуск:**
```bash
cd ~/Desktop/jetix-os && claude -p < prompts/fpf-iwe-levenchuk-deep-study-2026-05-17.md
```

Или launch в tmux session `cc` для долгой autonomous работы:
```bash
tmux new -d -s fpf-iwe-A 'cd ~/Desktop/jetix-os && claude -p < prompts/fpf-iwe-levenchuk-deep-study-2026-05-17.md 2>&1 | tee logs/fpf-iwe-A-2026-05-17.log'
tmux attach -t fpf-iwe-A
```
