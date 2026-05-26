---
title: "MetaPlan V3 — Phase 16: Cross-cutting documents spec (5 docs × multi-direction embed)"
date: 2026-05-26
type: phase-report-metaplan-v3
phase: 16
F: F2-F3
G: prompt-jetix-metaplan-v3-final-integration-2026-05-26
constitutional_posture: R1 surface + R2 STRICT + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT
language: russian
status: draft-report (pool — feeds main v3)
mermaid: V3-8 (см. Phase 20)
---

# 🔗 Phase 16 — Cross-cutting Documents Spec

> **Назначение фазы.** Не все документы принадлежат одному направлению. Пять документов **касаются
> сразу нескольких directions** — они «прошивают» карту насквозь. Если их писать по разу под каждое
> направление — получится дублирование и рассинхрон (изменил Vision в #6, забыл в #11). Решение:
> **один cross-cutting документ, показанный под нужным углом в каждом direction**, которое он touch'ит
> (тот же приём «полки × двери» из v2, но на уровне документов). Phase 16 = spec этих 5 + map embed'а.

---

## §0 Принцип cross-cutting документа

**Cross-cutting документ = single source of truth, который проявляется в нескольких directions
по-разному.** Не копия в каждом, а **одна каноническая версия + per-direction projection** (отрывок /
угол / cross-link).

- **Anti-pattern (что НЕ делаем):** копировать R12-обещание в #4 Заработок, #5 Партнёры, #8 R12, #14
  Сеть — четыре копии, которые разъедутся.
- **Pattern (что делаем):** R12-checklist живёт один раз (#8 R12 — его дом), а в #4/#5/#14 встроен как
  projection («перед каждой цифрой — 8 вопросов, полный список → #8»).

**Проверка R6:** у каждого cross-cutting дока есть **home direction** (где он живёт целиком) и
**guest directions** (где проявляется проекцией). Home = primary; guests = cross-cite.

---

## §1 Пять cross-cutting документов (обзор)

| Doc | Home direction | Guest directions (touch) | Кол-во touch | Тип проекции |
|---|---|---|---|---|
| **Vision** | #6 Видение | #1/#2/#3/#4/#5/#7/#8/#10/#11/#12/#13/#14 | **12/14** | frame-отсылка (тело) |
| **Charter** (членский) | #8 R12 / #3 Бизнес | #4/#5/#9/#10/#12/#14 + home | **8/14** | gate-документ (порог) |
| **Видео C** (экосистема) | #5 Партнёры | #4/#6/#8/#11/#14 + home | **6/14** | reuse-asset |
| **Economic V10** | #4 Заработок | #3/#5/#8/#14 + home | **5/14** | модель-отсылка |
| **R12 checklist** (8 вопросов) | #8 R12 | #4/#5/#7/#10 + home + partner-extension | **6/14** | gate-процедура |

---

## §2 Vision (cross-cutting — 12/14 directions)

### Spec

- **Home:** #6 Видение (витрина ≤2K) + #11 Master Plan (long-arc).
- **Что это:** Foundation-нарратив = мега-мастерская как тело Vision'а. Core statement (R1) + зачем (gap)
  + для кого + won't-compromise + Founder-as-Exhibit.
- **Формат:** MD canonical + 1-pager PDF + видео (manifesto) + презентация (для talks).
- **Почему cross-cutting:** Vision = клей. Каждое направление отвечает на «как это служит Vision'у».
  Убери Vision — directions распадаются в список тем (см. Phase 1 §0).

### Embed map (как проявляется в каждом из 12 guest directions)

| Direction | Проекция Vision |
|---|---|
| #1 Метод | «метод-метод служит мастерству — ядру Vision» (1 абзац intro + cross-link) |
| #2 Платформа | «станки = инструменты Vision'а; платформа не самоцель» |
| #3 Бизнес | «кооператив = форма, в которой Vision устойчив (не extractive)» |
| #4 Заработок | «деньги = ресурс Vision'а, не цель (триада O-138)» |
| #5 Партнёры | «зовём тех, кто разделяет Vision; фильтр = желание жить+изучать» |
| #7 Образование | «учим прошивке ради Vision'а (масса мастеров)» |
| #8 R12 | «обещание = что Vision не предадим даже выгоды ради» |
| #10 Ценности | «триада = ядро Vision; ценности = Vision в операциях» |
| #11 Master Plan | **разворот Vision во времени** (Build→Run→Scale→Mature) — самый плотный embed |
| #12 Мастерская | «место = тело Vision'а (ГДЕ)» |
| #13 Мастерство | «прокачка = что Vision культивирует (ЧТО)» |
| #14 Сеть | «распределение = как Vision масштабируется без предательства (КАК)» |

**R12 для Vision:** authenticity-tension (громко vs чус) — Vision не должен звучать как hype. Рост =
следствие качества + witness, не инженерия через hooks. Главный R12-вопрос Founder-as-Exhibit.

---

## §3 Charter (членский) (cross-cutting — 8/14 directions)

### Spec

- **Home:** #8 R12 (R12-clause) + #3 Бизнес (governance form).
- **Что это:** членский договор (не публичный манифест, а **gate-документ** — подписывается при входе в
  cohort/partnership/cell). Содержит: R12-clause (5:1 cap + 75/25 + fork-and-leave + 30-day opt-out) +
  governance (Ruslan = sole strategist на Build; per-Clan автономия на Scale) + revenue-share + exit-procedure.
- **Формат:** legal-lite MD + signed-version (Notion/DocuSign) + per-Clan template.
- **Почему cross-cutting:** Charter = «порог» — точка, где абстрактные обещания (#8) становятся
  обязывающими. Касается всех directions с обязательствами (деньги/роли/правила/cell).

### Embed map

| Direction | Проекция Charter |
|---|---|
| #4 Заработок | revenue-share clause (75/25 + 5:1) — экономика обязывающая |
| #5 Партнёры | partner-agreement = Charter L4-L6 (per тип T1-T4) |
| #9 Правила | какие правила mandatory в Charter (R12/ethical) vs опциональны |
| #10 Ценности | Charter преамбула = триада + ценности (что подписант разделяет) |
| #12 Мастерская | cell membership = Charter-lite (вход в пространство) |
| #14 Сеть | **cell Charter** = R12-clause обязателен для форка (Mondragón spawn) — плотный embed |

**R12 для Charter:** Charter — это **сам механизм fork-and-leave** (exit-procedure прописана). Anti-pattern:
Charter с lock-in clause (fork_prevention_attempt). Charter должен делать выход **легче**, не сложнее.

---

## §4 Видео C (экосистема / партнёры / R12) (cross-cutting — 6/14 directions)

### Spec

- **Home:** #5 Партнёры (главный потребитель — partner-facing).
- **Что это:** одно видео (5-15 мин) про экосистему: как устроена сеть, что предлагаем партнёрам, как
  работает R12-защита. **Reuse-asset** — снимается один раз, встраивается в 6 directions.
- **Формат:** YouTube (5-15 мин) + встраиваемый плеер на лендингах + транскрипт (MD).
- **Почему cross-cutting:** видео дорого производить (блокер — снимает Ruslan). Один asset → 6
  применений = экономия и согласованность нарратива.

### Embed map

| Direction | Где встроено Видео C |
|---|---|
| #4 Заработок | секция «как делим» (визуальный 75/25) |
| #5 Партнёры | главный asset (что предлагаем) — home |
| #6 Видение | витрина (тело экосистемы) |
| #8 R12 | секция «обещание» (R12 на пальцах) |
| #11 Master Plan | Part 2 Run (экосистема в действии) |
| #14 Сеть | mesh-топология визуально |

**R12 для Видео C:** anti-marketing stance — видео = witness, не реклама. Без hooks/FOMO/urgency. Тон:
«вот как устроено, думай сам». Anti-pattern: видео как воронка с давлением.

---

## §5 Economic V10 (cross-cutting — 5/14 directions)

### Spec

- **Home:** #4 Заработок (полная модель).
- **Что это:** экономическая модель (75/25 + 5:1 Mondragón + recursion + 6 моделей заработка + QF +
  Programmable Ethereum Phase 2+). LOCKED canonical (`ECONOMIC-MODEL-TOKENOMICS` 🔒) — наружу идёт
  **модель** (как делим), НЕ financial reporting (сколько именно).
- **Формат:** MD модель-спека + spreadsheet (treasury/unit-econ калькулятор, internal) + публичная
  «как делим» проекция (1-pager).
- **Почему cross-cutting:** деньги касаются бизнеса (#3), партнёров (#5), обещания (#8), сети (#14).

### Embed map

| Direction | Проекция Economic V10 |
|---|---|
| #3 Бизнес | кооператив = правовая форма экономики (worker-owner) |
| #4 Заработок | полная модель — home |
| #5 Партнёры | что партнёр получает (75% + treasury stake per тип) |
| #8 R12 | 5:1 cap + 75/25 = механизмы anti-extraction |
| #14 Сеть | pooling экономика + cross-cell revenue-share + internal bank (Mondragón) |

**R12 для Economic V10:** каждая цифра = СЦЕНАРНАЯ (Scenario A/B/C/D), не обещание. 5:1 cap +
fork-забирает-долю = встроенный anti-extraction. Публично — модель; отчётность ⛔ (financial reporting не наружу).

---

## §6 R12 checklist (8 вопросов) (cross-cutting — 6/14 directions)

### Spec

- **Home:** #8 R12 (полный список + escalation).
- **Что это:** 8 вопросов, прогоняемых **перед любым касанием** партнёра / аудитории / цифры (главный
  №7 «нет манипуляции?»). Это **gate-процедура**, не текст.
- **Формат:** MD checklist + Notion-форма (заполняется перед outreach) + pre-commit hook (для AI-actions).
- **Почему cross-cutting:** R12-checklist = операционный инструмент, применяемый везде, где есть
  внешнее касание или распределение ценности.

### Embed map

| Direction | Где применяется R12 checklist |
|---|---|
| #4 Заработок | перед каждой цифрой + «как уйти» |
| #5 Партнёры | перед каждым письмом партнёру (8 вопросов) |
| #7 Образование | граница education≠recruitment (вопрос №7 манипуляция) |
| #8 R12 | home (полный список + escalation Build/Run/Scale/Mature) |
| #10 Ценности | anti-beliefs = что 8 вопросов защищают |
| **partner-extension** | каждый partner-contribution проходит R12-check (Phase 18) — критично |

**R12 для самого checklist:** checklist должен **расти быстрее системы** (Build 🟢 вручную → Run 🟡
Steward → Scale 🔴 смарт-контракт). Anti-pattern: checklist как формальность (галочки без честности).

---

## §7 Cross-cutting embed — сводная карта

```
Vision        ──touch──> 12/14 (все кроме чисто #9 Правила, отчасти #3)   [frame: тело]
Charter       ──touch──> 8/14  (#3 #4 #5 #8 #9 #10 #12 #14)               [gate: порог]
Видео C       ──touch──> 6/14  (#4 #5 #6 #8 #11 #14)                       [asset: reuse]
Economic V10  ──touch──> 5/14  (#3 #4 #5 #8 #14)                           [model: отсылка]
R12 checklist ──touch──> 6/14  (#4 #5 #7 #8 #10 + partner-extension)       [gate: процедура]
```

**Наблюдение (R6):** четыре из пяти cross-cutting docs пересекаются на **#8 R12** и **#14 Сеть** — это
подтверждает Phase 1 (R12 = densest hub, Сеть = topology hub). Cross-cutting layer = в основном
**этико-экономический клей** (Vision/Charter/Economic/R12), плюс один production-asset (Видео C).

→ Полная визуализация — **mermaid V3-8** (Phase 20).

---

## §8 Что Phase 16 разблокирует

- 5 cross-cutting docs имеют **home + guests + embed map** — при наполнении пишутся один раз.
- Anti-дублирование: изменение Vision/Charter/Economic/R12 в home автоматически = source of truth для guests.
- Phase 18 (partner-extension) опирается на R12-checklist embed (каждый contribution проходит check).
- Phase 19 (master matrix) учитывает cross-cutting docs как отдельный слой (не per-direction артефакты).

**Phase 16 complete.** 5 cross-cutting docs специфицированы (Vision 12/14 · Charter 8/14 · Видео C 6/14
· Economic V10 5/14 · R12 checklist 6/14), каждый с home/guest/embed map. R12 paired-frame на каждом.

---

*Phase 16 closure. 5 cross-cutting docs × multi-direction embed: Vision (frame, 12/14) · Charter (gate,
8/14) · Видео C (reuse-asset, 6/14) · Economic V10 (model, 5/14) · R12 checklist (gate-процедура, 6/14).
Принцип single-source-of-truth + per-direction projection (home/guests). Cross-cutting layer = этико-
экономический клей, сходится на #8 R12 + #14 Сеть. R12 paired-frame STRICT. Feeds V3-8 (Phase 20).*
