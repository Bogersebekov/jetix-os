---
title: Deep prompt — synthesis профилей Левенчук + Цэрэн в один документ для подготовки к созвонам
date: 2026-05-16
type: server-cc-trigger-prompt
status: ready-to-fire
target_executor: server CC (autonomous 30-60 мин)
target_output: _L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md (в корне репо, Antigravity-friendly)
language: russian
purpose: |
  Подтянуть всю информацию которая есть на сервере про Анатолия Левенчука и Цэрэна Цэрэнова,
  synthesize в один компактный документ — биография, послужной список, сферы экспертизы,
  публичные позиции, сеть, методология. Использовать для prep'a к выходящим L1 звонкам.
F: F2
G: l1-profiles-applied-now
R: refuted_if_facts_diverge_from_source_profiles
---

# 🎯 Deep prompt: L1 profiles Левенчук + Цэрэн — synthesis в один документ

> **Как использовать.** Claude Code на сервере с `--dangerously-skip-permissions`, paste этот файл как первый prompt. Autonomous 30-60 мин.

---

## §0 Контекст

Сегодня — **2026-05-16**. Руслан готовится к outreach-звонкам с L1 First Clan candidates. **Цэрэн Цэрэнов** (Managing Partner МИМ) и **Анатолий Левенчук** (научный руководитель ШСМ) — два из 3 ключевых mentor-candidates.

Нужен **компактный prep-документ** для быстрого просмотра перед звонками — биография + ключевые наработки + сферы + сеть + точки пересечения с Jetix.

---

## §1 ЗАДАЧА

Создать **`_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md`** в корне репо. Synthesis всех существующих материалов в один document.

**Структура per person (8 секций):**
1. Identity (имя / возраст / locale / current role)
2. Карьерный путь (chronological — образование, ключевые позиции)
3. Послужной список / key projects / артефакты
4. Сферы экспертизы (методология / domains / навыки)
5. Публичные позиции (книги / статьи / TG канал / YT / выступления — с ссылками)
6. Network / окружение (с кем работает / руководит / связан)
7. Стиль работы / методология
8. Точки пересечения с Jetix + outreach hooks

**Plus:**
- §9 — relationship diagram (mermaid) между Цэрэном / Левенчуком / их сетью / Jetix L1 cohort
- §10 — Quick-glance table сравнения Цэрэн vs Левенчук (per dimension)

---

## §2 SOURCES — что прочитать

### §2.1 Deep profiles (главный источник)
- [profiles/l1-first-clan/tseren-tserenov.md](profiles/l1-first-clan/tseren-tserenov.md)
- [profiles/l1-first-clan/anatoliy-levenchuk.md](profiles/l1-first-clan/anatoliy-levenchuk.md)

### §2.2 CRM entries (текущие state + history)
- [crm/people/tseren-tserenov-l1.md](crm/people/tseren-tserenov-l1.md)
- [crm/people/anatoliy-levenchuk-l1.md](crm/people/anatoliy-levenchuk-l1.md)
- Drafts в `crm/people/*-draft*` — surface если есть полезная информация которая не вошла в final l1.md

### §2.3 Existing analysis prompts
- [prompts/tseren-tg-analysis-2026-04-28.md](prompts/tseren-tg-analysis-2026-04-28.md)
- [prompts/tseren-youtube-analysis-2026-04-28.md](prompts/tseren-youtube-analysis-2026-04-28.md)

### §2.4 Context references
- [reports/anton-call-report-2026-05-11.md](reports/anton-call-report-2026-05-11.md) — narrative context (упоминания Цэрэна / Левенчука)
- [decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md](decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md) — где они в L1 cohort
- [outreach/jetix-document-pool-2026-05-12.md](outreach/jetix-document-pool-2026-05-12.md) — per-L1 outreach sequence (Цэрэн / Левенчук уже описаны)

### §2.5 Grep весь repo для упоминаний
- `grep -rEi "Цэрэн|Tseren|Tserenov" .` — все упоминания Цэрэна
- `grep -rEi "Левенчук|Levenchuk|Anatoly|Анатолий" .` — все упоминания Левенчука
- Surface любые insights / context из старых документов (decisions / wiki / reports)

### §2.6 Опционально — web fetch (если репо данных мало)
- Левенчук TG / сайт ШСМ / Хабр блог / книга «Системное мышление»
- Цэрэн TG канал / YT / МИМ публикации
- **НЕ ОБЯЗАТЕЛЬНО** — если repo даёт достаточно, не тратить время на web. Если data явно gap → fetch.

---

## §3 OUTPUT FORMAT — `_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md`

### §3.1 Frontmatter

```yaml
---
title: L1 profiles — Цэрэн Цэрэнов + Анатолий Левенчук (prep документ для созвонов)
date: 2026-05-16
type: l1-profile-synthesis
status: ACTIVE
purpose: |
  Quick-glance подготовка перед звонками — биография, послужной список, экспертиза,
  сеть, методология, точки пересечения с Jetix. Не replacement deep profiles —
  компактный prep layer.
F: F2
G: l1-profiles-applied-now
R: refuted_if_diverges_from_source_profiles
prose_authored_by: ai-draft
sources:
  - profiles/l1-first-clan/tseren-tserenov.md
  - profiles/l1-first-clan/anatoliy-levenchuk.md
  - crm/people/tseren-tserenov-l1.md
  - crm/people/anatoliy-levenchuk-l1.md
  - prompts/tseren-*-analysis-2026-04-28.md
language: russian
audience: Ruslan (pre-call prep)
---
```

### §3.2 Структура контента

```markdown
# 👥 L1 profiles — Цэрэн Цэрэнов + Анатолий Левенчук

> **Что это.** Quick-glance prep для звонков. Все факты из существующих deep profiles + CRM.
> Не verbatim copy — synthesis с фокусом на «что мне нужно знать перед разговором».

---

## 🌟 TL;DR (одна страница)

[3-5 строк per человек — самое важное в одну строку
+ ключевая связка между ними (11 лет partnership)]

---

## 1️⃣ ЦЭРЭН ЦЭРЭНОВ — Managing Partner МИМ

### §1 Identity
- ФИО / возраст / locale
- Текущая роль: Managing Partner МИМ (Мастерская Инженеров-Менеджеров)
- TG: @TserenTserenov

### §2 Карьерный путь
- Образование
- Ключевые позиции хронологически
- Spin-off ШСМ → МИМ (2026)

### §3 Послужной список / key projects
- Конкретные projects / артефакты с датами

### §4 Сферы экспертизы
- Методология / domains / навыки

### §5 Публичные позиции
- TG канал — темы / частота / стиль
- YT — если есть
- Статьи / выступления
- (С ссылками)

### §6 Network / окружение
- 11 лет с Левенчуком
- Кто в МИМ команде
- Связи с другими L1 (Тарасов / Брагинский / etc.)

### §7 Стиль работы / методология
- Как подходит к проектам
- Что ценит в коммуникации
- Anti-patterns (что точно не любит)

### §8 Точки пересечения с Jetix + outreach hooks
- Workshop концепция overlap
- H6 Gamified Platform потенциальный entry point
- H7 People-NS как фрейминг
- Charter R12 anti-extraction — резонанс с МИМ методологией?

---

## 2️⃣ АНАТОЛИЙ ЛЕВЕНЧУК — научный руководитель ШСМ

[Аналогичная структура §1-§8]

Особо surface'нуть:
- Книга «Системное мышление» — статус / impact
- ШСМ — full picture (количество студентов / history / impact)
- Хабр блог + scope тем
- Methodology теории (что выработал свого)
- Equal-partner с Цэрэном (11 лет) — context этой связки

---

## 3️⃣ MERMAID — Network diagram

[Mermaid graph показывающий: Цэрэн ↔ Левенчук ↔ МИМ ↔ ШСМ ↔ Тарасов ↔ Брагинский ↔ другие L1 кандидаты ↔ Jetix First Clan]

---

## 4️⃣ Quick-glance comparison Цэрэн vs Левенчук

| Dimension | Цэрэн | Левенчук |
|---|---|---|
| Возраст | ? | ? |
| Основная роль | МИМ Managing Partner | ШСМ научный руководитель |
| Книги/публикации | ? | «Системное мышление» + Хабр |
| TG канал | @TserenTserenov | ? |
| YT | ? | ? |
| Стиль методологии | ? | системное мышление SOTA |
| 11 лет partnership | ✓ | ✓ |
| Outreach status | Video sent 15.05 | Pending video |
| Best entry point | МИМ-Workshop overlap | методологический фреймворк |

---

## 5️⃣ TALKING POINTS для звонков (как использовать в видео + созвоне)

### С Цэрэном
- [3-5 bullet points что упомянуть для resonance]

### С Левенчуком
- [3-5 bullet points что упомянуть для resonance]

---

## 6️⃣ OPEN QUESTIONS (что не известно — нужно узнать в созвоне)

[5-10 specific facts которые нет в источниках но важно знать]

---

*Создано 2026-05-16. Synthesis из profiles/l1-first-clan/ + crm/people/. Provenance per claim — citing source file. Update после каждого звонка (append §«From-call observations»).*
```

---

## §4 CONSTITUTIONAL DISCIPLINE

- **prose_authored_by:** ai-draft (это synthesis, не strategy)
- **Tier 2 R1** — surface facts, не recommend подход / стратегию / what-to-say
- **Tier 2 R6** — provenance per claim (cite source file + section)
- **R12 anti-extraction** — не extrapolate, только то что в источниках
- **НЕ §РЕКОМЕНДАЦИИ** / **НЕ §МОИ ВЫВОДЫ**
- Только descriptive surfacing + structuring

---

## §5 VERIFICATION

1. **Both profiles complete** — все 8 секций заполнены per person (или явно «нет данных»)
2. **All facts cited** — каждое утверждение имеет source pointer
3. **Mermaid valid**
4. **Quick-glance table** — заполнена для обоих
5. **Cross-references resolve**
6. **No API keys** в content

---

## §6 COMMIT + PUSH

```bash
git add _L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md
git commit -m "[outreach] L1 profiles synthesis — Цэрэн + Левенчук в один prep документ

- 8 секций per person: Identity / career / projects / экспертиза / публичные позиции /
  network / стиль / Jetix overlap
- Mermaid network diagram (Цэрэн ↔ Левенчук ↔ МИМ/ШСМ ↔ другие L1)
- Quick-glance comparison table
- Talking points для каждого звонка
- Open questions (что не известно)

Sources: profiles/l1-first-clan/ + crm/people/ + старые analysis prompts.
Used as: pre-call quick-glance перед outreach звонками."
git push origin main
```

---

## §7 SCOPE / TIME

- **30-60 мин autonomous** (focused — repo data есть, synthesis straightforward)
- Если grep / web fetch займёт больше → split на 2 phases (gather → synthesize)

---

## §8 ESCAPE HATCHES

- **Если данных мало per person** — surface «gap» прямо в документе, не filler-content
- **Если CRM drafts конфликтуют** — surface обе версии + дата каждой, не arbitrary choose
- **Если web fetch dolzhno быть** — note request к Руслану «for X необходим web pull» но не блокировать остальное

---

## §9 ОЖИДАЕМЫЙ РЕЗУЛЬТАТ

После `git pull` Руслан открывает в Antigravity:
- `_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md`
- ~5 мин чтения = full picture обоих + memory triggers перед звонком
- Используется перед / во время звонка как reference

---

*Создано 2026-05-16. Trigger для server CC focused execution. Constitutional anchor: AI = scribe; Ruslan = sole strategist. Tier 2 R1/R6/R12 preserved.*
