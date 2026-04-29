---
title: Claude Code Best Practices — ultrathink + Plan Mode (2026-04-29)
date: 2026-04-29
type: source-bundle
audience: ruslan + всех агентов Jetix
purpose: фактические практики работы с Claude Code CLI для применения на сложных задачах Jetix
sources:
  - ultrathink-claude-code.md
  - plan-mode-claude-code.md
---

# Claude Code Best Practices — bundle (2026-04-29)

Два отчёта про две ключевые техники работы с Claude Code CLI на текущий момент (апрель 2026):

1. **`ultrathink-claude-code.md`** — adaptive reasoning + ключевое слово `ultrathink` как in-context инструкция.
2. **`plan-mode-claude-code.md`** — read-only Plan Mode + workflow Explore → Plan → Code → Commit.

## TL;DR — что внедрить в Jetix

### Канонический workflow для сложных задач

```bash
# Запуск:
claude --permission-mode plan
/model → Use Opus in plan mode, Sonnet 4.6 otherwise

# 1. EXPLORE
"прочитай @<paths>, опиши текущее состояние, без решений"

# 2. PLAN с deep thinking
"ultrathink: построй план [task], ограничения [...], фазы с гейтами"

# 3. Ревью плана
Ctrl+G → правка в редакторе
(опц.) "найди слабые места в этом плане как staff engineer"

# 4. CODE
Shift+Tab → Normal Mode (auto-switch на Sonnet)
"имплементируй план пошагово, после каждой фазы запускай тесты"

# 5. COMMIT
"git commit + PR"
```

### 10 immediate-impact настроек

1. **Дефолтный Plan Mode** в проекте — `.claude/settings.json` → `permissions.defaultMode: plan`
2. **Версионирование планов** в репо — `plansDirectory: ./plans` (план как living spec, ревью через PR)
3. **Always-thinking** включён глобально — `/config` → `alwaysThinkingEnabled: true`
4. **Opus Plan Mode** — `/model` → "Use Opus in plan mode, Sonnet 4.6 otherwise" (планируешь умной, кодишь быстрой)
5. **`Ctrl+G`** для правки плана в редакторе вместо обсуждения чатом
6. **`Shift+Tab` дважды** = вход в Plan Mode из Normal
7. **`@<path>`** для точного контекста без блуждания
8. **`/clear`** между разными задачами — новая сессия каждый раз
9. **`Ctrl+O`** — verbose mode чтобы видеть рассуждения курсивом
10. **`/cost`** — отслеживай потребление токенов в Opus Plan Mode сессиях

### Когда `ultrathink` оправдан (high-impact use)

- Архитектурные решения (выбор технологий, границы модулей)
- Сложный дебаг (race conditions, dependency conflicts)
- Миграции (БД, фреймворки, архитектура)
- Глубокий code review (security + perf + maintainability одновременно)
- Незнакомая кодовая база
- Trade-off анализ

### Когда НЕ оправдан (вреден)

- Простые правки и переименования
- Шаблонный рефакторинг
- Креативное написание текстов
- Pattern matching (regex, форматирование)

### Anti-patterns (отслеживать в работе агентов)

- ❌ `ultrathink` на каждый запрос — токены сжигаются впустую
- ❌ Plan Mode для тривиальщины — overhead больше выгоды
- ❌ Большие планы (20+ файлов) — теряется когерентность
- ❌ Смешивание фаз Explore + Plan в одном запросе — план на половине информации
- ❌ Игнорирование `CLAUDE.md` для архитектурных constraints — модель не догадается спросить

### Правило 30 минут

Один план = одна логически замкнутая часть, имплементируемая за 30 минут. Большую фичу — последовательность планов, не один большой.

## Применение в Jetix

### Где это уже частично используется

- **HITL-gates через RUSLAN-ACK** — концептуально это и есть Plan Mode на уровне ROY swarm: brigadier генерит AWAITING-APPROVAL packet, Ruslan подтверждает, после ack ROY имплементирует.
- **AI = scribe для strategic docs** rule (memory) — соответствует duties separation Plan Mode (читать, не писать без апрува).
- **Compound engineering 40/10/40/10** — Plan 40% / Code 10% / Review 40% / Compound 10% — это и есть Anthropic's Explore → Plan → Code → Commit на уровне ROY cycles.

### Где ещё не применяется (gaps)

- **`.claude/settings.json` per worktree** — нет canonical конфига для plan mode default + plansDirectory
- **`plansDirectory: ./plans`** — нет версионируемой истории планов в проекте
- **`/model` Opus Plan Mode** — agents часто crashing на сложных задачах потому что Sonnet не справляется с планированием через 1M контекст
- **`ultrathink` keyword discipline** — нет documented правила когда обязательно добавлять `ultrathink` (architecture / debug / migration / deep review / unknown codebase / trade-off)
- **`Ctrl+G` plan editing** — Ruslan правит планы через чат, не через Ctrl+G в редакторе

### Где можно применить прямо сегодня

5 strategic вопросов для Jetix (см. отдельный план в Notion):

1. **Wiki integration в agents** — как заставить агентов реально использовать wiki как live context
2. **Niche selection / Jetix Corp positioning** — куда идти, как позиционироваться
3. **Agent team configurations for fast deliverables** — быстрые сайты, аналитика, follow-up
4. **Phase 1 €50K revenue trajectory** — конкретные revenue streams в 4-6 недель
5. **Roadmap to Jetix Corp** — bridge от €50K к корпорации

Каждый вопрос — отдельная Plan Mode сессия с `ultrathink`, output = options-paper для Ruslan'а (не authoritative strategy).

## Источники

- `ultrathink-claude-code.md` — оригинальный отчёт (290+ строк)
- `plan-mode-claude-code.md` — оригинальный отчёт (450+ строк)
- Common workflows (Claude Code Docs) — https://code.claude.com/docs/en/common-workflows
- Extended thinking — https://platform.claude.com/docs/en/build-with-claude/extended-thinking
- Plan Mode mechanics (ClaudeLog) — https://claudelog.com/mechanics/plan-mode/
- Permission modes — https://code.claude.com/docs/en/permission-modes
