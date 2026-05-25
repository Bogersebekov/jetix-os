---
title: Phase 5 — Substrate mapping: откуда тянем каждый публичный документ
date: 2026-05-25
type: phase-report
phase: 5
parent_prompt: prompts/jetix-public-docs-metaplan-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-jetix-public-docs-metaplan-phase-5
constitutional_posture: R1 surface only + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only
language: russian primary
status: pool — Ruslan picks вариант; NO auto-promotion
---

# 🔗 Phase 5 — Откуда тянем substrate (94 docs → публичные документы)

> **Что это.** Для каждого главного публичного документа — **явные источники** (2-5 файлов
> из substrate), какие секции тянем, и **что делаем при переупаковке**: оставляем как есть /
> переводим на человеческий / упрощаем / отрезаем (внутреннее). Плюс GAP — где substrate'а
> нет, надо создать с нуля.
>
> **Ключ.** Substrate-маппинг — **per документ, а не per вариант** (один и тот же документ в
> A, B, C тянет из одного места). Поэтому таблица одна — канонический пул из Phase 3. Variant-
> дельта — в §3.
>
> **Фильтр (Phase 0) применён:** тянем только из ✅-зоны. ⛔-зона (Legal/Financial-reporting/
> Research-raw/Brand/Foundation-infra) **не маппится** — она не выходит наружу.

---

## §1 Substrate-маппинг канонического пула

Легенда трансформации: **AS-IS** (готово, минимальная правка) · **HUMANIZE** (перевести с
жаргона на человеческий) · **SIMPLIFY** (вырезать глубину, оставить суть) · **CUT-INTERNAL**
(отрезать внутренний слой при переупаковке) · **CREATE** (substrate'а нет).

### 🧪 A1. Метод
| Публичный док | Substrate (2-5 файлов + секции) | Трансформация | GAP |
|---|---|---|---|
| Метод на пальцах | `METHOD-LIFE-DEVELOPMENT-V2` §мета-метод 🔒 + `CONSOLIDATED-HL` (7 ступеней) + `META-METHOD-8-COMPONENT-DEEP` | HUMANIZE + SIMPLIFY (8 компонент → суть) + CUT-INTERNAL (FPF-механика остаётся внутри) | ⚠️ сборка |
| Видео A | видео A spec (`build-artefacts-specs/03-video-A-spec.md`) | CREATE (запись) | ❌ |
| 7 ступеней | `CONSOLIDATED-HL` §ступени | AS-IS | ✅ |

### 🚀 A2. Платформа
| Публичный док | Substrate | Трансформация | GAP |
|---|---|---|---|
| Платформа Jetix | `PLATFORM-LIFECYCLE-STAGES-PLAN` §2 + `PERSONAL-OS-NOTION-TEMPLATE-PLAN` + `TEAM-OS-NOTION-TEMPLATE-PLAN` | SIMPLIFY (Build/Run/Scale → «что получаешь») + HUMANIZE | ⚠️ дизайн готов, implement ❌ |
| Build/Run/Scale на пальцах | `PLATFORM-LIFECYCLE` §2-3 | AS-IS (уже human-lang) | ✅ |

### 💼 A3. Бизнес
| Публичный док | Substrate | Трансформация | GAP |
|---|---|---|---|
| Как устроен Jetix | `JETIX-FULL-MAP` §1 (Корпорация/Governance) + `08-reference-corps` (Mondragón/John Lewis) + Pillar C | **HUMANIZE STRICT** (вырезать FPF/Foundation/Halt-Log-Alert — это ⚙️ system) + SIMPLIFY | ❌ нет публичного жанра |
| Принципы на пальцах | Pillar C Tier 1/2 | HUMANIZE + CUT-INTERNAL (12 правил → «как решаем») | ❌ |

### 💰 A4. Заработок
| Публичный док | Substrate | Трансформация | GAP |
|---|---|---|---|
| Partner Offering | `PARTNER-OFFERING-HUMAN-LANG` ✅ | **AS-IS (уже готов!)** | ✅ |
| 8 моделей дохода | `ECONOMIC-MODEL-TOKENOMICS-V10` 🔒 §модели | SIMPLIFY (V10 → 8 пунктов на пальцах) + CUT-INTERNAL (tokenomics-механика Phase 2+) | ⚠️ |
| Ценообразование / Y1 | `PARTNER-OFFERING` §3, §9 | AS-IS | ✅ |

### 👥 A5. Партнёры
| Публичный док | Substrate | Трансформация | GAP |
|---|---|---|---|
| Кого ищем | `EXECUTION-PLAN-FIXATION` §5 (4 типа) ✅ | AS-IS + IP-1 (имена → «примеры ролей») | ✅ |
| Первый разговор | discovery spec (`build-artefacts-specs/10-discovery-call-spec.md`) | HUMANIZE; универсализировать из Dmitriy-ad-hoc | ⚠️→❌ |
| Кого НЕ берём | `EXECUTION-PLAN` §анти-фит | CREATE (выписать честно) | ❌ |

### 🎯 A6. Видение
| Публичный док | Substrate | Трансформация | GAP |
|---|---|---|---|
| Куда идёт Jetix | `STRATEGIC-PLAN-NEAR-FUTURE` 🔒 + `JETIX-FULL-MAP` §2 (6 направлений) + `AI-MARKET-ELECTRICITY-ANALOGY` 🔒 | **SIMPLIFY STRICT** (Master Plan на пальцах, как Tesla) + HUMANIZE | ❌ нет публичного Master Plan |
| 6 направлений / этапы | `FULL-MAP` §2 + `PLATFORM-LIFECYCLE` §3 | AS-IS | ✅ |

### ⚖️ R12-якорь (сквозной)
| Публичный док | Substrate | Трансформация | GAP |
|---|---|---|---|
| «Наше обещание» | `EXECUTION-PLAN` §4 (8 вопросов) + `PARTNER-OFFERING` §7 (R12) + default-deny 4 класса | HUMANIZE (8 вопросов → обещание) + CUT-INTERNAL (Halt-Log-Alert/F-grade остаются внутри) | ⚠️ |

---

## §2 GAP-сводка: что создавать с нуля (CREATE ❌)

Документы, под которые **substrate'а в публичном жанре нет** (есть только внутренний или нет совсем):

| Документ | Почему GAP | Рычаг |
|---|---|---|
| **Видео A** (методология) | запись, не текст | ⭐⭐⭐ блокер 4 сущностей |
| **Публичный Master Plan** (A6 главный) | substrate внутренний (STRATEGIC-PLAN), публичного жанра нет | ⭐⭐ |
| **«Как устроен Jetix»** (A3 главный) | надо вырезать весь ⚙️-жаргон, переписать с нуля | ⭐⭐ |
| **Charter текст** (C3 / Run) | spec есть, текста нет | ⭐⭐⭐ закрывает 8 сущностей |
| **R12-обещание-страница** | разбросано по §4/§7, нет единой | ⭐⭐ |
| **Discovery script универсальный** | есть ad-hoc для одного кейса | ⭐ |
| **«Кого НЕ берём»** | честный анти-фит, нет жанра | ⭐ |
| **Одностраничник-витрина** (C1) | сжатие, нет такого формата | ⭐ (только если C/D) |
| **Глубокая навигация** (C3) | карта refs, нет | ⭐ (только если C/D) |

**Готовых ✅ к AS-IS прямо сейчас:** Partner Offering · 7 ступеней · ценообразование · Y1 ·
4 типа партнёров · Build/Run/Scale · 6 направлений+этапы. **Это ~7 документов — можно
запускать наполнение хоть завтра, выбор варианта их не блокирует.**

---

## §3 Variant-дельта substrate (что добавляет каждый вариант поверх пула)

| Вариант | Доп. substrate-работа vs канонический пул |
|---|---|
| **A** | нет (это базовый пул) |
| **B** | +страница входа B1 (тянет из `JETIX-NAVIGATION-GUIDE` — HUMANIZE/polish) + CTA-карта (CREATE, лёгкая) |
| **C** | +одностраничник C1 (SIMPLIFY из пула) + глубокая навигация C3 (CREATE + curated refs из 📚 — это **единственное место, где 📚 substrate касается публичного, и только как footnote-ссылки**) |
| **D** | всё из B + C + R12-якорь-страница вынесена в топ (HUMANIZE) |

**Важный R12-момент по substrate (для influence-ethics-линзы).** Глубокая навигация C3 —
единственный публичный документ, который **ссылается на 📚 substrate**. Дисциплина: только
**curated subset** (1-2 ссылки на разговор, footnote-режим), никогда не «вот вам 5 research-
deep'ов». Это прямо из анти-паттернов DOCS-CLASSIFICATION §5.2. Любой вариант с C3 (то есть
C и D) должен это соблюдать, иначе глубина превращается в «закрытый клуб со своим жаргоном».

---

## §4 Что Phase 5 даёт следующим фазам

- **GAP-сводка §2** → вход в comparison «substrate reuse efficiency» (Phase 6) и в quick-wins
  queue (Phase 7): ~7 документов готовы к AS-IS, не ждут выбора варианта.
- **Трансформации (HUMANIZE/CUT-INTERNAL)** → показывают, где главная работа: не «написать»,
  а «вырезать внутреннее и перевести». Это дешевле, чем кажется.
- **Variant-дельта §3** → подтверждает Phase 3: A дешевле всех по substrate, D дороже всех.

---

*Phase 5 closure. Substrate-маппинг канонического пула: per документ — 2-5 файлов + секции +
трансформация (AS-IS/HUMANIZE/SIMPLIFY/CUT-INTERNAL/CREATE) + GAP. ~7 готовых к AS-IS,
~9 CREATE (рычажные: видео A, Master Plan, «Как устроен Jetix», Charter, R12-страница).
Variant-дельта: A=0, B=+2 лёгких, C=+2+анти-дубль, D=всё. Фильтр Phase 0 соблюдён —
⛔-зона не маппится; 📚 касается публичного только через curated footnote-refs в C3. R1 surface.
IP-1 STRICT. Pool result.*
