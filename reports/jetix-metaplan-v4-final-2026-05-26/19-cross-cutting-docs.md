---
title: "MetaPlan V4 — Phase 18: Cross-cutting documents spec (7 docs × multi-direction embed)"
date: 2026-05-26
type: phase-report-metaplan-v4
phase: 18
F: F2-F3
G: prompt-jetix-metaplan-v4-final-integration-2026-05-26
constitutional_posture: R1 surface + R2 STRICT + R6 + R11 + R12 paired-frame STRICT + IP-1 STRICT
language: russian
status: draft-report (pool — feeds main v4)
mermaid: V4-8 (см. Phase 22)
---

# 🔗 Phase 18 — Cross-cutting Documents Spec (7 docs)

> **Назначение фазы.** V3 имел 5 cross-cutting docs (single-source-of-truth, проявляются проекцией в
> guest directions). V4 расширяет до **7**: те же 5 + **2 NEW**, продиктованные новыми directions —
> **Klan Charter template** (Кланы lifecycle нуждается в per-клан shell-документе) + **Anti-Dark-Patterns
> audit** (Геймификация #15 = primary R12 surface требует сквозного аудита тёмных паттернов). Принцип
> тот же: home direction (живёт целиком) + guests (проекция/cross-cite), без дублирования.

---

## §0 Принцип (preserved): home + guests, не копии

Cross-cutting документ = single source of truth + per-direction projection. Anti-pattern: копировать в
каждое направление (разъедутся). Pattern: home (целиком) + guests (отрывок/угол/cross-link). V4 добавляет
2 документа, оба рождены новыми directions — и оба сильно тяготеют к R12-якорю (#8), что подтверждает:
cross-cutting layer = этико-экономический клей.

---

## §1 Семь cross-cutting документов (обзор)

| Doc | Home | Touch (из 16) | Тип | V3/V4 |
|---|---|---|---|---|
| **Vision** | #6/#11 | 16/16 | frame (тело) | V3 |
| **Charter** (членский) | #8/#3 | ~10/16 | gate (порог) | V3 |
| **Видео C** (экосистема) | #5 | ~8/16 | reuse-asset | V3 |
| **Economic V10** | #4 | ~7/16 | модель-отсылка | V3 |
| **R12 checklist** (8 вопросов) | #8 | ~9/16 + partner-ext | gate-процедура | V3 |
| **Klan Charter template** | #14 (Кланы §K) | #12/#14/#16 + Кланы lifecycle | per-клан shell | **NEW v4** |
| **Anti-Dark-Patterns audit** | #15 / #8 | #5/#7/#15/#16 + Brand | R12 enforcement-чеклист | **NEW v4** |

**Наблюдение:** 5 из 7 сходятся на **#8 R12** + **#14 Сеть/Кланы** (V3 паттерн усилен). Оба NEW дока —
R12-несущие: Klan Charter = механизм fork-and-leave на уровне клана; Anti-Dark-Patterns = enforcement
для primary R12 surface (Геймификация). V4 cross-cutting layer = **этико-экономический клей + R12-каркас**.

---

## §2 Vision (16/16) — обновление под V4

- **Home:** #6 Видение + #11 Master Plan. **Что нового в V4:** Vision теперь включает 2 переживательно-
  операциональных слоя — «жизнь со смыслом каждый день» (Геймификация #15 — триада «жить чтобы жить»
  ощутима) + «events-driven world» (Хакатоны #16 — живая ткань мастерской) + «кланы как пути» (разные
  направления выбирать). Founder-as-Exhibit усилен: Ruslan геймифицирует свою жизнь на виду.
- **Embed:** касается всех 16 (каждое направление отвечает «как служит Vision'у»).
- **R12:** authenticity-tension ОБОСТРЯЕТСЯ Геймификацией — gamified growth не должен стать manufactured
  hype. Meaning ≠ manufactured engagement. Это главный V4-R12-вопрос Vision.

## §3 Charter (членский) (~10/16) — расширен Кланами

- **Home:** #8 R12 (R12-clause) + #3 Бизнес. **Что нового:** Charter теперь имеет **2 уровня** — (1)
  Foundation Charter (платформенный floor: триада + R12 + уважение к соревнующимся) + (2) **Klan Charter**
  (per-клан — см. §7 NEW doc). Touch расширен: + #14 Кланы + #15 (virtual economy clause) + #16 (event
  participation clause).
- **R12:** Charter = механизм fork-and-leave; теперь и на уровне клана (клан может форкнуться из сети).

## §4 Видео C (~8/16) — экосистема включает кланы + хакатоны

- **Home:** #5 Партнёры. **Что нового:** видео C теперь показывает кланы (как community-units) + хакатоны
  (events = как растём). Touch: + #14 + #16.
- **R12:** anti-marketing (witness не реклама); особенно важно не превратить «events» в FOMO-маркетинг.

## §5 Economic V10 (~7/16) — + events revenue

- **Home:** #4 Заработок. **Что нового:** модель теперь включает **events/hackathon revenue** (7-я модель:
  sponsor + QF pool + IP/talent placement) + inter-clan revenue-share (Mondragón cooperatives). Touch: + #16.
- **R12:** 5:1 cap на event payouts; QF distribution; цифры сценарные.

## §6 R12 checklist (~9/16) — + Геймификация PRIMARY

- **Home:** #8 R12. **Что нового:** 8 вопросов теперь применяются особенно к Геймификации (#15 = primary
  surface) + events (#16). Главный №7 (нет манипуляции?) = критичен для каждого game-mechanic. Touch: + #15 + #16.
- **R12:** checklist растёт быстрее системы (Build manual → Scale automated dark-pattern audit).

## §7 NEW: Klan Charter template

- **Home:** #14 Network (Кланы §K). **Touch:** #12 Мастерская (cell-based clans) + #16 Хакатоны
  (clan-wars participation) + вся Кланы lifecycle.
- **Что это:** **per-клан shell-документ** — заполняется при формировании клана (§K.1). Структура:
  - Преамбула: ценностной floor (триада O-138 + R12 + уважение) — **mandatory, не редактируется кланом**.
  - Founding members + roles (Steward + RACI matrix per клан) — клан заполняет.
  - Internal governance (consensus/voting model) — inner-clan freedom.
  - Methods/topics charter (что клан делает) — inner-clan freedom.
  - Mondragón allocation (5:1 cap — mandatory) + revenue-share model — floor + клан-specifics.
  - Inter-clan rules acceptance (no poaching/sabotage/extraction — mandatory).
  - Fork/spawn/dissolution clauses (§K.6/K.7 — fork-and-leave preserved, mandatory).
- **Формат:** legal-lite MD template + signed Notion version + per-клан instance.
- **R12:** Klan Charter = механизм **inner-clan freedom within platform floor**. Делает явным: что enforced
  (floor) vs что свободно (всё остальное). Anti-pattern: клан добавляет lock-in clause (fork_prevention_attempt) → reject.
- **Embed map:** #14 (home — Кланы lifecycle) · #12 (cell = клан base) · #16 (clan-wars participation terms)
  · #9 Правила (клан governance rules) · #3 Бизнес (клан = cooperative sub-unit).

## §8 NEW: Anti-Dark-Patterns audit

- **Home:** #15 Геймификация (+ #8 R12 enforcement). **Touch:** #5 Партнёры (no manipulative recruiting) +
  #7 Образование (no addictive learning) + #16 Хакатоны (no FOMO event marketing) + Brand.
- **Что это:** **сквозной enforcement-чеклист**, прогоняемый по любому artefact с engagement-механикой.
  Структура (explicit запреты):
  - ❌ Addictive engagement loops (infinite scroll / streak-pressure)
  - ❌ Variable-reward exploitation (slot-machine dopamine)
  - ❌ Sunk-cost mechanics («ты уже столько вложил»)
  - ❌ Manufactured FOMO / urgency / scarcity
  - ❌ Social-pressure mechanics (shame-driven streaks / public-fail)
  - ❌ Pay-to-win virtual economy
  - ❌ Vanity metrics as goals (likes/followers as primary)
  - ❌ Dopamine-not-flow design
  - ✅ Discipline (positive checklist): intrinsic motivation primacy (SDT) · meaningful progression only
    (mastery markers) · opt-out always / no lock-in · flow not dopamine · metric = «насколько вырос» не
    «время в приложении» (anti-TikTok) · gamification-for-meaning not -retention.
- **Формат:** MD checklist + pre-publish audit gate (для любого game-mechanic / engagement artefact) +
  Notion-форма.
- **R12:** это **operationalization** R12 для primary surface. Каждый Геймификация-artefact проходит этот
  audit перед публикацией. Escalation: Build manual review → Scale automated audit.
- **Embed map:** #15 (home — каждый mechanic) · #8 R12 (enforcement) · #5/#7/#16 (где engagement) · Brand.

---

## §9 Cross-cutting embed — сводная карта (V4)

```
Vision               ──> 16/16   [frame: тело + смысл-каждый-день + events-world]
Charter (2-level)    ──> ~10/16  [gate: floor + Klan Charter]
Видео C              ──> ~8/16   [asset: +кланы +хакатоны]
Economic V10         ──> ~7/16   [model: +events revenue +inter-clan]
R12 checklist        ──> ~9/16   [gate: +Геймификация PRIMARY]
Klan Charter (NEW)   ──> #14/#12/#16 + Кланы lifecycle   [per-клан shell]
Anti-Dark-Patterns (NEW) ──> #15/#8/#5/#7/#16 + Brand    [R12 enforcement]
```

5 из 7 сходятся на #8 R12 + #14 Сеть/Кланы. Оба NEW — R12-несущие. → визуализация **V4-8** (Phase 22).

---

## §10 Что Phase 18 разблокирует

- 7 cross-cutting docs (5 + 2 new) с home/guests/embed map — пишутся один раз.
- Klan Charter template → готов для first клан formation pilot (Кланы §K.1).
- Anti-Dark-Patterns audit → gate для каждого Геймификация-artefact (R12 primary surface enforcement).
- Phase 20 (partner-extension) использует Klan Charter (Layer 4 spawn).
- Phase 21 (master matrix) учитывает cross-cutting как отдельный слой.

**Phase 18 complete.** 7 cross-cutting docs: Vision (16/16) · Charter 2-level (~10) · Видео C (~8) ·
Economic V10 (~7) · R12 checklist (~9) · **Klan Charter template (NEW)** · **Anti-Dark-Patterns audit (NEW)**.
Оба new = R12-несущие. R12 paired-frame STRICT.

---

*Phase 18 closure (v4). 7 cross-cutting docs (V3 5 + 2 NEW). Klan Charter template (home #14 Кланы §K;
per-клан shell с floor-mandatory + inner-freedom; механизм клан-level fork-and-leave). Anti-Dark-Patterns
audit (home #15/#8; explicit запреты тёмных паттернов + positive discipline checklist; gate для каждого
engagement-artefact; operationalization R12 для primary surface). 5/7 сходятся на #8 R12 + #14 Кланы. Feeds
V4-8 (Phase 22).*
