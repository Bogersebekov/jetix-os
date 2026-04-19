---
type: stage2-orchestrator-prompt
target-executor: Claude Code на сервере (Hetzner), Opus 4.7, 1M context
stage: 2 of 6 — Multi-chat Expert Review (orchestrator)
created: 2026-04-19
owner: ruslan
---

# STAGE 2 ORCHESTRATOR — Multi-chat Expert Review

Ты — **Claude Code на сервере**, orchestrator Stage 2 review process.

## Твоя задача

Запустить **5 reviewer chats** (4 параллельных + 1 финальный) для expert review
synthesis'а из Stage 1.

## Процесс

### Шаг 1. Launch 4 parallel reviewers (через Task tool)

Используй Task tool для запуска 4 subagents параллельно в одном сообщении
(multiple tool calls in single message = parallel execution).

Каждому subagent — свой role-prompt из файла:

```
1. Task(subagent_type="general-purpose",
         description="Critic review",
         prompt=<содержимое файла prompts/stage2-review/01-critic-role.md>)

2. Task(subagent_type="general-purpose",
         description="Simplifier review",
         prompt=<содержимое файла prompts/stage2-review/02-simplifier-role.md>)

3. Task(subagent_type="general-purpose",
         description="Mega-corp visionary review",
         prompt=<содержимое файла prompts/stage2-review/03-megacorp-role.md>)

4. Task(subagent_type="general-purpose",
         description="Levenchuk expert review",
         prompt=<содержимое файла prompts/stage2-review/04-levenchuk-role.md>)
```

**Важно:** все 4 — в ОДНОМ сообщении как 4 параллельных Task tool calls.

Каждый subagent должен:
- Читать synthesis целиком (`raw/research/architecture-implementation-synthesis-2026-04-19.md`)
- Применить свою role-lens
- Написать output в `raw/research/stage2-review/review-<role>.md`
- НЕ commit сам — orchestrator (ты) commit всё в конце

### Шаг 2. Дождись completion всех 4

Каждый subagent return свой полный review (или confirmation что написал файл).

### Шаг 3. Read все 4 review outputs

Когда 4 subagents завершились:
```
Read raw/research/stage2-review/review-critic.md
Read raw/research/stage2-review/review-simplifier.md
Read raw/research/stage2-review/review-megacorp.md
Read raw/research/stage2-review/review-levenchuk.md
```

### Шаг 4. Launch 5th reviewer (final synthesizer)

Используй Task tool для 5-го subagent:

```
Task(subagent_type="general-purpose",
      description="Final synthesizer",
      prompt=<содержимое prompts/stage2-review/05-synthesizer-role.md
             + все 4 review outputs appended>)
```

5-й subagent:
- Reads synthesis v1 + 4 reviews
- Identifies meta-conflicts между reviewers
- Resolves с rationale
- Produces v2 synthesis
- Writes output: `raw/research/architecture-synthesis-v2-final.md`

### Шаг 5. Commit + push everything

Один commit с всем:

```bash
git add raw/research/stage2-review/*.md raw/research/architecture-synthesis-v2-final.md
git commit -m "[research] Stage 2 complete — multi-chat review + v2 synthesis

4 reviewer outputs (Critic / Simplifier / Mega-corp / Левенчук) +
final integrated v2 synthesis.

Input: v1 synthesis (1592 строки)
Output: 4 reviews + v2 synthesis ready для Stage 3 (Ruslan review) + Stage 4 (D1-D9)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
"

git push origin HEAD:main
```

### Шаг 6. Отчёт Ruslan'у

Напиши chat message для Ruslan'а:

```
✅ Stage 2 complete.

4 review outputs:
- raw/research/stage2-review/review-critic.md (<N> words)
- raw/research/stage2-review/review-simplifier.md (<N> words)
- raw/research/stage2-review/review-megacorp.md (<N> words)
- raw/research/stage2-review/review-levenchuk.md (<N> words)

V2 synthesis:
- raw/research/architecture-synthesis-v2-final.md (<N> words)

Top changes v1 → v2:
1. ...
2. ...
3. ...

Top meta-conflicts resolved:
1. Critic vs Mega-Corp on <topic> — resolution: ...
2. Simplifier vs Левенчук on <topic> — resolution: ...

Top remaining open questions для Ruslan judgment:
1. ...
2. ...

Ready для Stage 3 (твой review v2 synthesis).
```

## Важные инструкции

### Parallel execution

Все 4 reviewers — **в одном сообщении, 4 tool calls**. Это критично для
параллельности. Не делай sequentially — waste of time.

### Output locations

```
raw/research/stage2-review/
  ├── review-critic.md
  ├── review-simplifier.md
  ├── review-megacorp.md
  └── review-levenchuk.md

raw/research/
  └── architecture-synthesis-v2-final.md
```

Убедись что папка `raw/research/stage2-review/` существует (создай через bash).

### Не дубли

Каждый reviewer фокусируется на своей role. Don't duplicate — if Critic
mentions complexity, that's Simplifier's territory. Keep lanes.

### Quality gates

Перед step 4 (synthesizer) проверь:
- Каждый review ≥ 2000 слов (если меньше — может не достаточно deep)
- Каждый review cites specific sections synthesis (Part X, §Y)
- Каждый review имеет concrete proposed changes (не abstract)

Если какой-то review слабый — можно спросить тот subagent refine (через
Task tool повторно с specific feedback).

### Time budget

- Шаг 1-2 (4 parallel reviewers): 1-2 часа wall-time
- Шаг 3-4 (synthesizer): 1-2 часа
- Шаг 5-6 (commit + report): 10 мин

**Total:** 2-4 часа. Ты можешь работать в extended thinking mode.

## Начинай

1. Создай директорию `raw/research/stage2-review/`
2. Прочитай content всех 5 role-prompts (01-05)
3. Launch 4 parallel Task calls с role-prompts
4. Дождись completion
5. Launch 5th synthesizer
6. Commit + push + report

Приступай.
