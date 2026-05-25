---
title: Phase 0 — Substrate ingest + v1 baseline + Ruslan additions (metaplan v2)
date: 2026-05-25
type: phase-report
phase: 0
parent_prompt: prompts/jetix-public-docs-metaplan-v2-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
G: prompt-jetix-public-docs-metaplan-v2-phase-0
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT + append-only
language: russian primary
status: pool — substrate baseline for v2 max-depth run; NO auto-promotion
---

# 📥 Phase 0 — Substrate ingest + v1 baseline + Ruslan additions

> **Что это.** Стартовая фаза v2-прогона. Не пишет структуру — фиксирует **базу**, на которой
> v2 разворачивает variant D на максимум: что взято из v1, что добавил Руслан голосом 25.05
> вечером, какой substrate прочитан и куда что мапится. Это «отчёт о входных данных», чтобы
> следующие 11 фаз стояли на твёрдом, а не на пересказе.

---

## §1 Главный сдвиг v1 → v2 (зафиксирован как факт, не как опция)

**v1 (`JETIX-PUBLIC-DOCS-METAPLAN-2026-05-25.md`) сделал работу выбора:** surface'нул 3 варианта
структуры (A по направлениям / B по воронке / C по аудиториям) + гибрид D, сравнил матрицей
(B=24, A=23, C=21, D=21) и рекомендовал на Build «B-воронка на A-каркасе» (lite-гибрид), а
полный D отложить до Run.

**v2 не пере-обсуждает выбор.** Руслан голосом 25.05: «выбираю самый глубокий нахуй лучший
проработанный вариант». Значит: **variant D Hybrid = picked**, и задача v2 — не сравнивать
снова, а **развернуть D на максимум** (3000% density per §17.0 mandate) + добавить 5 новых
направлений, которые в v1 были встроены или отсутствовали.

Это снимает напряжение v1 («D дорог, риск over-engineering на Build»): Руслан осознанно
выбрал глубину как **проектный артефакт-карту** (не как то, что сразу строим целиком). D
здесь = **полная карта местности**; что из неё строить первым — решает Wave-sequencing
(Phase 9), а не урезание самой карты.

---

## §2 Что добавил Руслан (5 новых блоков v2)

| # | Добавка | Голос Руслана (verbatim фрагмент) | Куда легло |
|---|---|---|---|
| 1 | **Rules document** (10 углов) | «правила надо устанавливать тоже потом это все обновим опишем детально» | Phase 3 → полка #9 |
| 2 | **Values + Beliefs document** | «отдельно список ценностей добавим тоже как такой вот файл ценностей верования» | Phase 4 → полка #10 |
| 3 | **Vision standalone + Master Plan** | «вижен если там он… не упомянул тоже вот как-то ещё отдельно» | Phase 5 → полка #11 |
| 4 | **Per-direction skeletons** («плюс-минус по каждому») | «плюс-минус по каждому» | Phase 6 (heavy) |
| 5 | **Chinese corps reference** | «интересные опции но возможно… китая компании» | Phase 1 (расширенный scan) |

Плюс сквозной mandate: «глубоко блять максимально и большие в общем прорабатываем» = density > brevity.

---

## §3 11 направлений v2 (6 v1 + 5 NEW)

v1 baseline 6: **🧪 Метод · 🚀 Платформа · 💼 Бизнес · 💰 Заработок · 👥 Партнёры · 🎯 Видение**.

v2 расширение до 11 (две из них — это R1-decisions v1, которые Руслан surface'нул как «да, отдельно»):

7. 🎓 **Образование** — отделено от Метода (v1 §5 decision 2: «выделить Образование из Метода?»)
8. ⚖️ **R12 / Обещание** — отдельная заметная страница (v1 §5 decision 5: «отдельная страница "Наше обещание"?»)
9. 📋 **Правила работы** — Rules document (NEW)
10. 💎 **Ценности / Верования** — Values + Beliefs (NEW)
11. 📜 **Vision / Master Plan** — standalone (NEW; в v1 Видение было направлением, но без long-form Master Plan и без Tesla-жанра)

> Замечание о коллизии: «Видение» (#6) и «Vision/Master Plan standalone» (#11) — **не дубль**.
> #6 = короткое направление-полка «куда идём» (≤2K, витринное). #11 = long-form манифест +
> публичный Master Plan в 4 части (Tesla-style). Phase 5 разводит их явно (см. §5 там).

---

## §4 Прочитанный substrate (что реально открыто и усвоено)

### v1 metaplan output (полностью)
- main `JETIX-PUBLIC-DOCS-METAPLAN-2026-05-25.md` (вариант D §3.D + рекомендация §4 + 8 R1-решений §5)
- `reports/.../02-reference-public-architectures.md` (7 референсов Западных)
- `reports/.../03-variants-structure.md` (variant D §4 baseline)
- `reports/.../04-per-variant-main-docs.md` (канонический пул ~6 главных + ~20 поддерживающих + GAP-флаги)

### Core substrate (через 2 fan-out агентов)
- **`JETIX-FULL-MAP-AND-DOCS-SKELETON-2026-05-25.md`** — 12 сущностей; 94 документа (36 ✅ / 25 ⚠️ / 33 ❌) в 12 категориях; master skeleton (4 супер-кластера); §1 Корпорация; §2 Видение (6 направлений: платформа / кооп-экономика / дистрибуция / AI-электрификация / Tier-1 outreach / Network State).
- **`DOCS-CLASSIFICATION-2026-05-25.md`** — 4 категории (🟢 Пояснительные ~15-20 / 🛠️ Шаблоны ~30-40 / 📚 Substrate 200+ / ⚙️ System infra ~50); 3 персоны (Любопытный / Серьёзный кандидат / Методолог); audience×category matrix; 7 анти-паттернов (главный: «не давать substrate до пояснительных» + «не показывать System наружу»).
- **`PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md`** — Build/Run/Scale + actor matrix (T1-T4 × этап); сейчас = **Точка А, Build середина**; видео A = блокер 3 векторов; 4-week Build plan.
- **`EXECUTION-PLAN-FIXATION-2026-05-24.md`** — 4 типа партнёров T1 Методология / T2 Ресурсы / T3 Аудитория / T4 Консультанты; **8 вопросов R12** (цена≤польза / конкретно / соразмерно / по ступени / канал / не доим-не запираем / нет манипуляции / стоп-сигнал готов); discovery call 30-60 мин (диагностика, не продажа).
- **`METHOD-LIFE-DEVELOPMENT-V2-2026-05-21.md`** 🔒 — 7 ступеней (Узнаёшь→…→Передаёшь × Bloom); прошивка 5 элементов (методология / системное мышление / инженерный подход / ответственность / tool-stratification); мета-метод §J (4 уровня рекурсии, L3 = Jetix-specific, 6-шаговая процедура); question-first (O-185); cross-skill vs навык; адекватный интеллект (O-180); сравнение с Левенчуком/МИМ.
- **`ECONOMIC-MODEL-TOKENOMICS-2026-05-22.md`** 🔒 (V10 Hybrid) — 8 income models; 75/25 split; recursive 25% (closed-form 75 / 16.67 / 8.33); Mondragón 5:1 on-chain; QF; fork-and-leave; ERC-1155 triple-role (worker/investor/promoter); SBT voting; L1-L8 tiers.
- **`STRATEGIC-PLAN-NEAR-FUTURE-2026-05-21.md`** 🔒 — горизонты 1y/5y/25y; Point A/B/C/D 2026-2028; 4 сценария (A Conservative 70% / B Realistic 40% / C Aggressive 15% / D Hyper 5%); 1M cohort path.
- **29 D-LOCK** в `decisions/strategic/lock-entries/D-{01..29}-*.md` (ключевой D-13 open-surface-closed-core).
- **O-числа** (RUSLAN-NOTES-EDUCATION-PARADIGM-2026-05-24 + wiki/concepts): O-107 метод-метод / O-128 cybernetic AI-amplifier / O-176 paradigm shift / O-180 адекватный интеллект / O-181 anti-cheating / O-183 frontier contribution / O-184 mass uplifment / O-185 question-first.

### Style anchor
- **`PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md`** — образец plain-Russian + готовый документ «Заработок» (75/25, triple-role, 5:1, fork-and-leave, Y1-траектория, 2 mermaid). Это AS-IS-готовый главный документ направления 💰.

---

## §5 Max-depth подход (как v2 будет разворачивать D)

1. **Variant D = baseline каркас** (3 dimensions: 6+5 полок × 3 двери × маршрут). Phase 2 разворачивает каждую intersection-ячейку.
2. **Density mandate 3000%** — main ≥30-40K; Phase 6 (skeletons) ≥18-22K; каждый per-direction skeleton ≥1.5K. Не останавливаться на минимуме.
3. **F2-F3 derivative** — никакого нового внешнего research; reference corps (вкл. Chinese) = синтез общих знаний.
4. **R12 paired-frame STRICT** — на направлениях R12 / Партнёры / Образование / Community auto-fire ethical-counter-frame (что НЕ делаем + защита читателя).
5. **NO sample doc content (R11)** — пишем **скелеты и спеки** (что внутри документа, какие секции), НЕ сами публичные тексты.
6. **IP-1 STRICT** — имена (Maxim / Дмитрий / Прапион / Левенчук / Цэрэн / Сева / Oleg) = примеры ролей T1-T4, не назначения.
7. **Append-only** — v1 output не трогаем (superseded, не modified); всё новое — новые файлы.

---

## §6 Что Phase 0 даёт следующим фазам

- **Phase 1** — расширенный reference scan (Западные + Chinese 8 + кооперативы + research + методология) опирается на v1 7-референсов как ядро.
- **Phase 2** — variant D max-depth берёт 11 направлений (§3) + канонический пул из v1 Phase 3.
- **Phase 3-5** — Rules / Values / Vision спеки берут substrate из §4 (Pillar C / O-числа / Method §J / Economic / Strategic Plan).
- **Phase 6** — skeletons на 11 направлений, каждый ссылается на substrate-источник из §4.
- **Phase 8** — substrate mapping использует точные file-paths, собранные здесь.

---

*Phase 0 closure. v1 baseline усвоен (variant D = picked, не пере-обсуждаем). 5 Ruslan-добавок
зафиксированы (Rules / Values / Vision / skeletons / Chinese corps). 11 направлений определены
(6 v1 + 5 NEW). Substrate прочитан: v1 output (4 файла) + 8 core-доков + 29 D-LOCK + 8 O-чисел +
style anchor. Max-depth подход зафиксирован. F2-F3 derivative. R11 — только скелеты, NO sample
content. IP-1 STRICT. Append-only. Pool result — NO auto-launch.*
