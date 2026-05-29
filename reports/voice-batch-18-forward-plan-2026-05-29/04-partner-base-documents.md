---
title: Voice Batch 18 — Phase 5 Partner Base Documents Structure
date: 2026-05-29
type: phase-report
phase: 5
batch: 18
F: F3 (synthesis) — R1 surface
G: prompt-voice-batch-18-plus-forward-action-plan-2026-05-29
constitutional_posture: R1 surface + R2 STRICT + R6 + R11 + R12 (no superlatives, value-first) + voice DRAFT-only
language: russian
---

# Phase 5 — Базовые документы для партнёров (структура пакета)

> **Что это.** Сегодняшняя цель: упаковать структуру базовых документов для показа партнёрам/
> помощникам — «вот что строю, вот как устроено». **НЕ продажа, НЕ launch** — показ. Spec для FA-2..8.
> Прямо требуется voice-2 O-248 «надо доупаковать информацию» + O-256 «презентацию делаю».
>
> **R12 floor (Phase 3 §2):** Overview = NO superlatives («20x», «миллионер»); value-first; «всемирный
> проект» подаётся humble-framed (O-246 «я занимаюсь основами»); Ценности-doc несёт R12 anti-extraction;
> «Как участвовать» = fork-and-leave обе стороны.

---

## §1 Базовый комплект (5 core + 2 supporting)

> Filter principle (per ACTION-PLAN §2 + batch-18): документ входит в пакет только если он помогает
> партнёру **понять что я строю** за один сеанс показа. Deep-substrate → defer.

### Core 5 (первый показ)

| # | Документ | Что показывает | Формат | Substrate | Writer | Time |
|---|---|---|---|---|---|---|
| **P-1** ⭐ | **Jetix Overview** | Entry point. Через 3P-призму (O-237): мастерская + сеть кланов + метод. «Вот что строю, вот зачем». Всемирный проект — humble frame | 1-pager MD + Notion page | ✅ Workshop concept + voice-pipeline-public + 3P (O-237) | CCW draft → **R prose pass** | 2-3h |
| **P-2** | **Метод** | Как работаем с информацией / методами / AI (3P + Method V2 essence). «Как это работает» | 1-2 pager MD/PDF | ✅ Method V2 LOCKED (нужна public-версия) | CCW draft → R pass | 2-3h |
| **P-3** | **16 directions карта** | Структура всего что строим. Масштаб + связность (5 центров / 3 хаба / 2 движка) | Diagram + page | ✅ V4 MetaPlan FINAL | CCW (из V4) | 1-2h |
| **P-4** | **Ценности + R12 обещание** | Floor — что гарантируем: anti-extraction + fork-and-leave + Mondragón 5:1 + уважение (O-261). «Что я обещаю» | 1-pager | ⚠️ substrate есть (R12 LOCKED), нужна упаковка | CCW draft → **R prose pass** | 2-3h |
| **P-5** | **Как участвовать** | Роли партнёра/помощника + extension protocol (4 layers). «Твоя роль + как войти/выйти» | Page | ⚠️ partner-extension 4 layers, нужна упаковка | CCW draft → R pass | 2h |

### Supporting 2 (для углубления / partner-talk, не обязательно в первый показ)

| # | Документ | Что показывает | Формат | Substrate | Writer | Time |
|---|---|---|---|---|---|---|
| **P-6** | **Видео-обзор (1-2 «грубо»)** | Async pitch — Method prep + что строю; одним голосом+лицом (O-251) | Видео (Loom/YT unlisted) | ✅ Method-Mastery public + спека | **R face-to-camera** | half-day (= FA-9) |
| **P-7** | **Fundament status** | Что есть / что строим / где нужна помощь (tech/fin/legal per O-247/O-249). Для разговора с Дмитрием | 1-pager | ✅ ACTION-PLAN §1.2 6 components | CCW+R (= FA-10) | 1h |

---

## §2 Reading path для партнёра (с чего начать → куда углубиться)

```
[60 сек]   P-1 Overview ──── «что это вообще» (3P-призма entry)
   │
[5 мин]    P-2 Метод ─────── «как работаете» (методология + AI)
   │
[5 мин]    P-3 16 directions ─ «масштаб + структура» (что входит)
   │
[3 мин]    P-4 Ценности+R12 ─ «что гарантируете» (trust floor)
   │
[3 мин]    P-5 Как участвовать ─ «моя роль» (вход/выход, fork-and-leave)
   │
   ▼  ── углубление по интересу ──
[10 мин]   P-6 Видео ──────── async, живой голос
[talk]     P-7 Fundament ──── для тех кто хочет помочь строить (Дмитрий ×2)
```

**Логика пути:** сначала «что» (P-1) → «как» (P-2) → «масштаб» (P-3) → «можно ли доверять» (P-4) →
«что я с этого / как войти» (P-5). Партнёр за ~15 мин получает полную картину без deep-docs. Видео
(P-6) и fundament (P-7) — для тех кто заинтересовался и хочет дальше.

---

## §3 Где живёт пакет (3 слоя)

| Слой | Что | Authority |
|---|---|---|
| **repo `partner-package/`** | P-1..P-5 MD source + ссылки на P-6/P-7 | Source of truth (filesystem, per Global Rule 4) |
| **Notion partner-facing collection** | Те же 5 docs как pages + reading-path landing | View (не authoritative; для удобного показа) |
| **External video link** | P-6 (Loom/YT unlisted) | External asset |

> **DRAFT-only discipline:** partner-package = DRAFT до Ruslan prose-pass на P-1/P-2/P-4 (strategic
> prose = Ruslan-authored per R1). Notion = view, генерится после repo ready.

---

## §4 Что НЕ в пакете (defer — не для показа партнёру сейчас)

| Defer | Почему |
|---|---|
| **Геймификация механики (кубки/NFT)** [O-257] | GATE через #15 audit (FA-17); концепт можно упомянуть в P-3, mechanics — нет |
| **Financial reporting / unit-econ деталь** | Не для первого показа; Economic V10 = deep substrate |
| **Master Plan Part 3-4 / $1T / NS** | Substrate parked |
| **Internal SOPs / swarm architecture** | Internal, не partner-facing |
| **Wealth-promise / «станешь миллионером»** [O-244] | R12 REFRAME-STRICT — НЕ в материалах |
| **Crypto/Ethereum substrate деталь** | Phase 2+ overlay; не для показа |

---

## §5 Связь с batch-18 инсайтами

- **O-237 3P-призма** → P-1 Overview framing-устройство (entry lens).
- **O-246 всемирный проект** → P-1 humble-framed scale statement (NO grandiosity).
- **O-247 фундамент-до-запуска** → P-7 Fundament status (что строим + где нужна помощь).
- **O-248/O-256 доупаковать** → весь пакет = материализация этого ask.
- **O-249 Дмитрий talk content** → P-7 (tech/fin/legal вопросы + «кто нужен»).
- **O-257 геймификация** → упоминание в P-3 ONLY; mechanics defer (gate #15).
- **O-261 уважение** → P-4 Ценности floor.

---

*Phase 5 closure. Partner-package: 5 core (P-1 Overview / P-2 Метод / P-3 16 directions / P-4
Ценности+R12 / P-5 Как участвовать) + 2 supporting (P-6 видео / P-7 fundament). Reading path ~15 мин
(что→как→масштаб→доверие→роль). 3 слоя (repo source + Notion view + video). R12: no superlatives,
value-first, humble scale-frame. DRAFT-only до R prose-pass. Maps FA-2..8 + сегодняшняя цель.*
