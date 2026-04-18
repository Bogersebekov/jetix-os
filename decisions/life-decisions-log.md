---
type: decision
status: recorded
created: 2026-04-18
context: "Life-level decisions log — инициализация раздела"
alternatives: []
decision: "Начать лог life-level решений в рамках Шага 4 v1-beta"
evidence: "IMPLEMENTATION-PLAN §4.2 Block B"
replay-check: "К 2026-07 должно быть ≥5 записей real-life решений"
relevant-agents: [strategist, manager]
owner: ruslan
tags: [#log/init]
---

<!--
Append-only лог решений уровня жизни (I-05, §11.5 TECH).
Формат отдельной записи — templates/tpl-decision.md (T-02).
Новые записи добавляются сверху (над разделом initialized).

Месячные агрегаты: decisions/YYYY-MM-decisions.md (rotate раз в месяц).
Project-specific decisions: projects/{slug}/decisions.md.

При изменении уже записанного решения — создавай новое с supersedes-ссылкой,
не редактируй старое (ADR-003 + I-05).
-->

# Life-level decisions — 2026

## 2026-04-18 — Log initialized

**Context.** Инициализация раздела `decisions/` в Шаге 4 плана v1-beta
(folder structure alignment с §4.1 SYSTEM-DESIGN-HUMAN).

**Decision.** Начать формальное логирование life-level решений здесь. Все
значимые life/career решения фиксируются с обязательными полями из T-02
(context, alternatives, decision, evidence, replay-check, relevant-agents).

**Evidence.** `design/IMPLEMENTATION-PLAN-2026-04-18.md` §4.2 Block B.

**Replay-check.** К 2026-07 раздел должен содержать ≥5 реальных life-level
решений (не init-записей). Если пустой — значит логирование не прижилось,
пересматриваем подход на monthly ritual.

**Relevant agents.** `strategist`, `manager` — для `/propagate-decision` когда
будут первые реальные записи.
