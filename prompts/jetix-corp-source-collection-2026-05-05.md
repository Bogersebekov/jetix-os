---
title: Source Collection промпт для server CC — собрать все Jetix-related документы
type: prompt
created: 2026-05-05
purpose: server-side Claude Code собирает в единый файл все основные документы (wiki + decisions + design + raw research + Notion fetched) которые описывают что такое Jetix, что он делает, как работает. Это **input** для Документа 1B (JETIX-CORPORATION-2026-05-05.md).
target_output: reports/jetix-source-collection-2026-05-05.md
expected_size: ~2000-5000 строк (compact summary, не полный dump)
audience: Claude Code на сервере (claude/jolly-margulis-915d34) + Ruslan для review + Cloud Cowork CC для использования при заполнении 1B
---

# 📥 ПРОМПТ для server CC — Jetix Source Collection

## Контекст задачи

Я (Ruslan) с Cloud Cowork CC сейчас пишем **Документ 1B — Jetix Corporation** (`decisions/JETIX-CORPORATION-2026-05-05.md`). Это **концептуальный документ для потенциальных партнёров** — что такое Jetix, как работает, какое предложение, какое видение.

**Проблема:** информация о Jetix **разбросана** по 50+ файлам — wiki/ entries / decisions / design docs / raw research / Notion. Cloud Cowork CC не может эффективно навигировать всё это сразу. Иногда находит старую инфу, иногда новую, путается.

**Решение:** ты, server CC, собираешь **единый compact source-collection файл** на основе которого Cloud Cowork CC потом будет работать.

## Parent документ (для понимания target audience)

Открой и прочитай для контекста:
- `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` — Документ 1A (LOCKED v1.0, 2534 строки) — universal foundation. Документ 1B будет building on top.
- `decisions/JETIX-CORPORATION-2026-05-05.md` — Документ 1B skeleton (12 разделов) — то что мы заполняем.

## Задача

Создай файл `reports/jetix-source-collection-2026-05-05.md` со следующей структурой и содержимым:

---

### 📋 Структура target output файла

```markdown
---
title: Jetix Source Collection — компактная сборка всех источников о Jetix Corp
type: source-collection
created: 2026-05-05
created_by: server CC (claude/jolly-margulis-915d34)
purpose: input для заполнения Документа 1B JETIX-CORPORATION
parent_target: decisions/JETIX-CORPORATION-2026-05-05.md
sources_scanned: <list>
total_sources: <N>
---

# Jetix Source Collection

> Компактная сборка ключевых тезисов / цитат / фактов о Jetix Corp из всех актуальных источников. Используется как input для Документа 1B.

## 0. Executive Summary
*1-2 абзаца: что такое Jetix согласно собранным источникам, главные тезисы.*

## 1. Что такое Jetix — все имеющиеся определения
*Собрать все формулировки one-liner и развёрнутых определений из источников. С атрибуцией.*

## 2. Метафора Мастерской — все материалы
*Цитаты из Workshop concept LOCKED v1, voice extracts, deep narrative от server CC. Какие 6/7 элементов мастерской.*

## 3. TRM — Total Resource Management — все материалы
*Цитаты из TRM model LOCKED. 6 ресурсов в деталях. Mgmt fee + performance fee. L0-L5 уровни.*

## 4. Платформа для проектов / partners ecosystem
*Что есть в источниках про partner model, fork Foundation, cross-collaboration.*

## 5. Управляющая компания — что делает Jetix как managing entity
*Цитаты + материалы про active management ресурсов клиента.*

## 6. Большая афёра века / экспериментальный сценарий
*Что есть в источниках про ambition / scale / risk / "if it works".*

## 7. ICP — кто партнёр / клиент Jetix
*ВАЖНО: НЕ привязывайся к Mittelstand DACH. Ruslan выраженно сказал что ICP — это концептуальный portrait через ось ресурсов + ось желания развиваться. 3 типа: (1) Solo / Indie hackers с revenue share %, (2) средний бизнес с mgmt + % growth, (3) те кто отдают ресурсы в управление (full TRM). Собери все материалы которые поддерживают этот концептуальный portrait.*

## 8. Видение 1/3/10 лет
*Что есть про trajectory €50K → €1T scenario / стратегические вехи / phase transitions (1 владелец → команда → community).*

## 9. Roadmap к €50K
*Конкретный план Q2 2026. Что должно произойти до 30.06.2026.*

## 10. Синергия / network effects
*Что есть в источниках про exponential value через сеть participants.*

## 11. Anti-patterns Jetix (что Jetix НЕ есть)
*НЕ consulting firm classic / НЕ AI-стартап с product / НЕ holding / НЕ accelerator / НЕ BlackRock / etc.*

## 12. Connections с Базовой Системой (Документом 1A)
*Где в source documents есть упоминание / альзо описание того, что Jetix Corp использует Базовую Систему как foundation. Какие специфические Jetix добавления поверх каркаса.*

## Appendix — Список просканированных источников

### A. Decisions (canonical LOCKED docs)
*Список всех `decisions/*.md` файлов с кратким описанием каждого.*

### B. Wiki entries (foundations / concepts / ideas / sources)
*Список релевантных wiki entries с тэгом jetix / workshop / TRM / corp / etc.*

### C. Design docs
*Список релевантных design/*.md файлов.*

### D. Synthesis files
*Список `swarm/wiki/synthesis/*.md` файлов.*

### E. Raw research
*Список релевантных raw/research/*.md файлов.*

### F. Notion pages (если успеешь fetch)
*Релевантные Notion страницы по Jetix.*
```

---

## Source priority (что искать)

### 🟢 HIGH priority (canonical LOCKED)
1. `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` — Workshop metaphor v1 LOCKED (271 строка)
2. `decisions/JETIX-TRM-MODEL-2026-04-30.md` — TRM business model LOCKED
3. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` — constitutional anchor
4. `decisions/JETIX-FPF.md` или `design/JETIX-FPF.md` — Foundation Pillar Framework
5. `decisions/RUSLAN-ACK-*.md` — Ruslan acks к Foundation Bundles 1-5
6. `decisions/AWAITING-APPROVAL-*.md` если есть актуальные strategic

### 🟢 HIGH priority (synthesis от server CC)
7. `swarm/wiki/synthesis/jetix-as-workshop-deep-description-2026-05-01.md`
8. `swarm/wiki/synthesis/voice-extract-workshop-people-2026-05-01.md`
9. Любые другие `swarm/wiki/synthesis/*.md` про Jetix / workshop / TRM

### 🟡 MEDIUM priority (design docs)
10. `design/SYSTEM-DESIGN-HUMAN.md` — стратегический якорь
11. `design/SYSTEM-DESIGN-TECH-SUMMARY.md` v1-beta-FINAL
12. `design/JETIX-ARCHITECTURE-WORKING.md` — 8-слойная бизнес-архитектура (parallel concept)
13. `design/ARCHITECTURE-TARGET.md` — current vs v1-beta vs v1-final vs v2

### 🟡 MEDIUM priority (Foundation Parts — для context)
14. `swarm/wiki/foundations/principles/architecture.md` — Pillar C
15. `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` — Strategic Direction
16. `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` — Projects (для понимания управления проектами)
17. Briefly: остальные 9 Parts (только Mission / §0 Executive Summary каждой)

### 🟢 HIGH priority (wiki ideas про Jetix)
18. `wiki/ideas/jetix-*.md` — все entries в wiki/ideas/ начинающиеся с jetix
19. `wiki/concepts/` — entries про workshop / TRM / corp / partnership / capitalismus
20. `wiki/foundations/` — entries в local wiki

### 🟡 MEDIUM priority (raw research)
21. `raw/research/hybrid-framework-synthesis-2026-04-18.md` — synthesis 8 layers (101K доcument)
22. Любые `raw/research/*.md` про Mittelstand / partnership / consulting / advisory

### 🟢 HIGH priority (12-month context)
23. `reports/retrospective_2025-05_to_2026-04.md` — 12 months Phase 1/2/3 trajectory

### 🔵 LOW priority (если время позволит)
24. Notion fetch: `Jetix Vision` / `Workshop Concept` / `TRM Model` страницы — добавить excerpts
25. CRM / outreach docs — context про какие partner profiles уже идентифицированы

---

## Принципы извлечения

### 🎯 ЦИТИРУЙ верно
Каждая ключевая фраза / тезис — **с attribution** в формате `[src: <relative-path>:§<section-or-line>]`. Это позволит при заполнении 1B легко проверить контекст.

### 🎯 КОМПРЕССИЯ
Не копируй полные документы. **Извлекай тезисы** — 1-3 предложения которые передают суть. Total output ~2000-5000 строк, не 50000.

### 🎯 ОТМЕЧАЙ ПРОТИВОРЕЧИЯ
Если разные источники говорят разное про одно — отметь явно «**⚠️ Conflict:** source A says X, source B says Y». Не пытайся primer'ить.

### 🎯 ОТМЕЧАЙ stale/superseded
Если в источнике явно есть `superseded_by:` или дата >3 месяца назад — пометь «🟡 Possibly stale».

### 🎯 ICP — КРИТИЧЕСКИ
Ruslan выраженно отверг «Mittelstand DACH manufacturing 50-500 emp» как ICP. Новый ICP — концептуальный portrait через ресурсы + желание развиваться, 3 типа (Solo/Indie / средний бизнес / TRM-делегаторы). Когда находишь упоминания "Mittelstand" / "DACH" — **отмечай как outdated frame**. Возможно где-то в source documents есть и более концептуальные формулировки — приоритезируй те.

### 🎯 НЕ ВРЫВАЙСЯ В architecture details
Foundation 11 Parts уже описаны в Документе 1A. В этом source-collection нужны только Jetix-specific дополнения и applications. Не дублируй универсальные тезисы.

---

## Выходные данные

Сохрани результат в:
- **`reports/jetix-source-collection-2026-05-05.md`**

Закоммить и запушь на свою branch (`claude/jolly-margulis-915d34`). Потом скажи Ruslan чтобы он подтянул на main:
```bash
cd ~/jetix-os && git fetch origin main && git push origin HEAD:main 2>&1 | tail -3
```

(Или Ruslan сам сделает merge.)

В конце дай **короткий summary под 200 слов**:
- Сколько источников отсканировано
- Сколько из них canonical LOCKED vs draft / superseded
- Какие 3-5 most important findings
- Какие conflicts / противоречия обнаружены
- Какие gaps (на что нет материалов в текущей базе)
- Готовность к использованию для заполнения 1B

---

## Workflow с Cloud Cowork CC после твоей работы

После того как `reports/jetix-source-collection-2026-05-05.md` готов:
1. Ruslan делает `git pull` на main
2. Cloud Cowork CC читает этот один файл (вместо 50+ scattered)
3. Совместно с Ruslan заполняем Документ 1B раздел за разделом, опираясь на собранные тезисы
4. Каждый тезис в 1B имеет attribution на source

Это **снижает вероятность confusion** между старой и новой информацией. И ускоряет заполнение в 5-10×.

---

**Прохождение:** автономно, без апрува по каждому шагу. Ты server CC — у тебя нет Cloud Cowork interrupt'ов. Делай качественно, **focus on signal**, не filler. Если что-то критически непонятно — оставь TODO comment в файле, не блокируйся.

**Estimated time:** 30-90 минут активной работы (зависит от количества файлов).

**Готов работать?** Поехали.
