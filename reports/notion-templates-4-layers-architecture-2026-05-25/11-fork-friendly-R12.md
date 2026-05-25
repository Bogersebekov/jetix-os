---
title: Phase 10 — Fork-friendly mechanics + R12 (Notion 4-Layers Architecture)
date: 2026-05-25
type: phase-report-fork-friendly-r12
parent_prompt: prompts/notion-templates-4-layers-architecture-2026-05-25.md
parent_main: decisions/strategic/NOTION-TEMPLATES-4-LAYERS-ARCHITECTURE-2026-05-25.md
phase: 10
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-notion-templates-4-layers-architecture-2026-05-25
R: low
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only
language: russian primary
roy_auto_fire: [influence-ethics, recruitment-dynamics]
---

# Phase 10 — 🍴 Fork-friendly mechanics + R12

> **Что в этой фазе.** Как работает форк на каждом слое. Специфика fork-friendliness Layer 4
> (главное сообщение: generic base = универсальный, multiple overlays возможны, Jetix = ОДИН из
> примеров). R12 enforcement mechanics (только если выбран R12-aware overlay; на generic base не
> enforced). R12 AUTO-FIRE.

---

## §1 Два слоя форка (повторяется внутри каждого уровня)

Сквозной паттерн (Personal OS §9): любой шаблон = **универсальный фундамент** («грамматика», не
трогают) + **надстройка под себя** («словарь», под нишу/бизнес). Это позволяет обновлять
грамматику из апстрима, не теряя словарь.

| Слой | «Грамматика» (Layer A, неизменна) | «Словарь» (Layer B, под себя) |
|---|---|---|
| **L1** | топология баз, типы полей, матрица голоса, DRAFT-only | подтипы проектов, роли CRM, темы, POINT A/B |
| **L2** | структура Reviews, движок гипотез, AI Helpers | глубина аналитики, ниша Concepts |
| **L3** | 10 ролей, матрица прав, Charter-структура, биржа | состав ролей, ratio, монетизация |
| **L4** | 12 групп баз, relations, formula-паттерны | extension points + overlay (Jetix/VC/agency/none) |

**Анти-паттерн (все слои):** переделка «грамматики» при форке ломает совместимость и апдейты.
Имена-личности в Layer A ломают fork-friendly («Daily Log», не «Дневник Васи»).

---

## §2 Fork per layer

### §2.1 Layer 1 — полная свобода

Fork → copy template → adapt → use **без association** с апстримом. Отдельный воркспейс. Никакой
связи с Jetix. Данные — твои. Перестал пользоваться — данные остаются. 5 ниш (инженер /
исследователь / предприниматель / методолог / гуманитарий) меняют только «что в центре».

### §2.2 Layer 2 — keep base + adapt add-ons

Fork → сохранить Layer 1 base + адаптировать advanced add-ons под себя. Можно обновлять Layer 1
из апстрима, не теряя свою аналитику.

### §2.3 Layer 3 — fork-and-leave из cohort

Fork-and-leave из когорты → **preserve Personal OS data** (приватный воркспейс не трогается) +
**30-day notice** (при изменении Charter) + **asset retrieval** (своя доля + строка Ledger) +
**не-punitive** (нейтральный язык, никакого «ты предал»). Можно форкнуть всю когорту под свою
группу (Wave 1 партнёры).

### §2.4 Layer 4 — ANY founder forks generic → adapts → optionally overlays

**KEY MESSAGE:** Layer 4 base = **универсальный**, multiple overlays возможны. Jetix = только
ОДИН из примеров.

```
ANY founder/executive
   → forks generic Layer 4 base (12 групп, framework-agnostic, governance-agnostic)
   → adapts под свой бизнес (включает нужные extension points)
   → optionally наслаивает overlay:
        • Jetix-overlay §5.X (R12 / Mondragón / Charter / 10 ролей) — кооператив
        • VC-overlay (cap table / board votes / investor reporting) — стартап
        • agency-overlay (utilization / project margin) — агентство
        • SaaS-overlay (MRR / churn / cohort retention) — SaaS
        • свой собственный overlay — что угодно
        • none — generic base достаточно
```

---

## §3 Layer 4 fork-friendliness specifics

Что конкретно делает Layer 4 fork-able (per Ruslan voice «с конкретными дописями что можно добавить»):

| Свойство | Как реализовано |
|---|---|
| **Generic base без brand terminology** | «Goals», «Revenue», «People» — не «Jetix OKR», не «Mondragón pool» |
| **Per-DB extension points explicit** | каждая §5.X база имеет блок «если X-бизнес → добавь поля Y» |
| **Framework-agnostic** | Strategy = слот; OKR/V2MOM/EOS — extension, не дефолт |
| **Governance-agnostic** | Roles = library; иерархия/плоская/матрица/кооператив — выбор |
| **Worked examples разных бизнесов** | консалтинг / SaaS / агентство / кооператив (Phase 5 §5.18) |
| **Copy instructions** | 7-шаговый standalone setup ≤3 часа (Phase 5 §5.17) |
| **Overlay = отдельная под-секция** | §5.X не вплетён в base; включается/выключается целиком |

**Copy instructions (как форкнуть Layer 4):** дублировать template-воркспейс → переименовать под
бизнес → пройтись по 12 группам, включить нужные + extension points → (опц.) наслоить overlay →
первая неделя адаптации (внести реальные данные) → собрать Command Center.

---

## §4 R12 enforcement mechanics (ТОЛЬКО при R12-aware overlay)

**Критично:** R12 **не enforced** на generic Layer 4 base. Generic base = нейтральный business
tool (бизнес может быть капиталистическим, кооперативным, любым). R12 включается **только** если
бизнес выбирает R12-aware overlay (Jetix-style кооператив).

### §4.1 Когда R12 включён (cooperative-overlay)

| Механика | Где | Что делает |
|---|---|---|
| **8 paired-frame questions** | монетизация (§5.2 + Layer 3 §5) | каждый денежный шаблон проходит чек перед применением |
| **4 RUSLAN-LAYER action classes** | R12 Audit Log (Layer 3 + §5.7) | мониторинг: extraction / wage-ratio / non-consensual / fork-prevention |
| **Mondragón 5:1** | §5.2 formula | `max/min > 5 → HALT F4 ≤5с` перед распределением |
| **Steward audit cadence** | Layer 3 §8 + §5.12 | регулярный аудит при cooperative-overlay |
| **Programmable Ethereum** | Charter flag (Phase 2+) | on-chain усиление (opt-in per-Clan) |

### §4.2 8 paired-frame questions (canonical)

Цена ≤ польза? · конкретно? · соразмерно отношениям? · по стадии? · канал уместен? · не доим /
не запираем? · нет манипуляции? · стоп-сигнал готов? — хоть один FAIL → не применяется / HALT.

### §4.3 4 action classes (детекторы)

- `extraction_beyond_share` — забрать сверх договорённого → HALT
- `wage_ratio_violation` — сделать одного в >5× богаче → HALT
- `non_consensual_distribution` — опубликовать чужое без согласия → HALT
- `fork_prevention_attempt` — язык «теперь не уйдёшь» → HALT

---

## §5 Fork-and-leave preserved ALL the way up (R12 сквозной)

Главный R12-инвариант: право уйти со своим — работает на **всех 4 слоях**:

| Слой | Что сохраняется при уходе |
|---|---|
| L1 | все личные данные (отдельный воркспейс, не трогается) |
| L2 | + аналитика, ревью, вики |
| L3 | + своя строка Contribution Ledger + накопленная доля + 30-day notice |
| L4 | + (если founder уходит) бизнес продолжается без него (Scale: founder = 1 из многих) |

**Cross-layer R12:** уход на любом уровне не может «забрать» данные нижних. Уход из когорты
(Layer 3) не трогает Personal OS (Layer 1/2). Это архитектурно (раздельные воркспейсы), не «по
обещанию».

---

## §6 R12 на generic base vs overlay (ключевое различие)

| Аспект | Generic Layer 4 base | R12-aware overlay (Jetix-style) |
|---|---|---|
| Mondragón 5:1 | нет (нейтрально) | enforced (HALT) |
| 8 questions | нет | каждый денежный шаблон |
| Steward role | нет (опц. external auditor) | обязательна, сквозная |
| fork-and-leave | data export всегда (базовая порядочность) | + 30-day + доля + анти-fork-prevention |
| anti-cult onboarding | базовый «выход озвучен» | полный анти-секта kit |

**Почему так (influence-ethics AUTO-FIRE):** навязывать R12 всем бизнесам = идеологический lock-in
(сам по себе анти-R12 — «ты обязан быть кооперативом»). Поэтому generic base нейтрален; R12 =
**выбор** бизнеса через overlay. Это и есть R12 на мета-уровне: не запираем даже в «правильную» модель.

---

## §7 Constitutional posture Phase 10

- **R1 surface only** — какой overlay (Jetix/VC/agency/none), включать ли R12 = выбор Ruslan/бизнеса.
- **R12 paired-frame STRICT** — fork-and-leave preserved все 4 слоя; generic base нейтрален
  (R12 = opt-in, не навязан — мета-R12); 8 questions + 4 classes при overlay.
- **R11** — Ethereum on-chain = Phase 2+ opt-in, не auto.
- **IP-1 STRICT** — overlay примеры абстрактны; Jetix = один инстанс.
- **R6** — наследует Personal OS §9 (2 слоя форка) + Team OS §13 (fork-leave) + Economic V10 (R12).

---

*Phase 10 closure. Fork: 2 слоя (грамматика+словарь) на каждом уровне; L1 полная свобода; L3
fork-and-leave 30-day+доля; L4 = ANY founder forks generic → adapts → optionally overlays (Jetix =
ОДИН пример). R12 enforced ТОЛЬКО при cooperative-overlay; generic base нейтрален (мета-R12: не
навязываем модель). fork-and-leave preserved все 4 слоя. Дальше Phase 11 — implementation roadmap.*
