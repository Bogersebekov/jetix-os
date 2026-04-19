---
type: stage2-review-package
stage: 2 of 6 — Multi-chat Expert Review
created: 2026-04-19
owner: ruslan
input: raw/research/architecture-implementation-synthesis-2026-04-19.md (1592 строки, Stage 1 output)
---

# Stage 2 — Multi-Chat Expert Review

## Что это

Пакет **6 prompts** для multi-chat review synthesis'а из Stage 1.

Методология — адаптация **5-chat review pattern** (из
`methodology_multi_chat_review_for_critical_docs.md`). Каждый chat — отдельная
**role** атакует synthesis со своей linzy, результаты синтезируются в
финальную v2 synthesis.

## Файлы

| Файл | Роль | Input | Output |
|------|------|-------|--------|
| `00-orchestrator.md` | Master coordinator (если запускать через Claude Code subagents) | Synthesis | (orchestration plan) |
| `01-critic-role.md` | Devil's advocate, attacks gaps | Synthesis Part 5.1 | `raw/research/stage2-review/review-critic.md` |
| `02-simplifier-role.md` | Anti-complexity, cuts over-engineering | Synthesis Part 5.2 | `raw/research/stage2-review/review-simplifier.md` |
| `03-megacorp-role.md` | 10x scale visionary | Synthesis Part 5.3 | `raw/research/stage2-review/review-megacorp.md` |
| `04-levenchuk-role.md` | ШСМ expert, ontology correctness | Synthesis Part 5.4 | `raw/research/stage2-review/review-levenchuk.md` |
| `05-synthesizer-role.md` | Final integrator (reads 01-04 outputs) | 4 review outputs + synthesis | `raw/research/architecture-synthesis-v2-final.md` |

## Как запускать — 2 варианта

### Вариант A: Через Claude Code subagents (быстрее, parallel)

На сервере одна команда:

```bash
cd ~/jetix-os
claude --dangerously-skip-permissions
```

Дать Claude Code:

```
Прочитай prompts/stage2-review/00-orchestrator.md и выполни задачу которую
он описывает. Запусти 4 параллельных subagent'а с ролями из файлов 01-04,
дождись их завершения, потом запусти 5-й synthesizer (файл 05) с их outputs.
```

**Time:** 2-4 часа wall-time (4 параллельно + synthesizer последовательно).

### Вариант B: 5 отдельных Claude sessions (true separation)

Открыть 5 разных Claude sessions (Antigravity tabs или Anthropic console):

**Sessions 1-4 (параллельно):**
- Session 1: содержание `01-critic-role.md`
- Session 2: содержание `02-simplifier-role.md`
- Session 3: содержание `03-megacorp-role.md`
- Session 4: содержание `04-levenchuk-role.md`

После completion всех 4 — commit outputs на сервер.

**Session 5 (после):**
- Содержание `05-synthesizer-role.md`

**Time:** 3-6 часов (параллелизация + sequential).

**Преимущество B:** truly separate chats, no shared state, каждый reviewer
имеет clean context. **Недостаток:** больше manual work.

## Моя рекомендация: Вариант A

Claude Code на сервере efficient. Subagents через Task tool дают достаточную
separation (каждый subagent имеет свой context window). Ruslan одна команда
запускает, ждёт 2-4 часа.

## Output после Stage 2

Один финальный файл:

```
raw/research/architecture-synthesis-v2-final.md
```

Это **v2 synthesis** — интегрированный с feedback от 4 reviewers. Готов к
Stage 3 (Ruslan review финал) и Stage 4 (writing D1-D9 чистовики).

## Время

- Stage 2 (это): 2-6 часов
- Stage 3 (Ruslan review v2): 45-60 мин
- Stage 4 (write D1-D9): 29-39 часов (4-5 рабочих дней)
- Stage 5 (Ruslan review each): 2-3 часа
- Stage 6 (Deploy): 2-3 часа

**Итого до рабочей архитектуры:** ~35-55 часов focused work.

## Quality assurance

Каждый reviewer должен:
- Прочитать synthesis целиком
- Применить свою role-lens rigorously
- Ссылаться на конкретные секции synthesis с citations
- Не хвалить для красоты — **attack honestly**
- Proposed changes должны быть concrete (не «надо подумать»)

Final synthesizer должен:
- Прочитать все 4 reviews
- Identify meta-conflicts между reviewers
- Resolve с rationale
- Produce v2 synthesis с integrated improvements
- Flag remaining open questions для Ruslan
