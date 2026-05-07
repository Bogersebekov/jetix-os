---
name: mermaid-iterate
description: "Изменяет существующую Mermaid диаграмму по text instruction, сохраняя canonical Jetix style. Используй когда: измени диаграмму, добавь ноду, сделай связь жирнее, mermaid-iterate, перекрась элемент, переставь блоки."
disable-model-invocation: true
allowed-tools: Read Write Edit Glob Grep Bash(date *) Bash(git *)
---

# /mermaid-iterate — Итерация существующей Mermaid диаграммы

## Назначение

Применить text-based change к существующему `.md` файлу с Mermaid диаграммой. Сохраняет canonical style (palette + naming + structure). Validates basic syntax после изменения.

## Аргументы

- `<file>` (обязательно) — path к `.md` файлу содержащему mermaid block (e.g. `swarm/wiki/synthesis/diagrams-2026-05-07/01-workshop-7-elements.md`)
- `<change>` (обязательно) — instruction что менять. Примеры:
  - "добавь ноду CACHE между STORAGE и MASTER"
  - "сделай связь TOOLS → AUTO жирной"
  - "перекрась GUARD в красный потемнее"
  - "переименуй MASTER в OWNER"
  - "поменяй direction на LR"
  - "добавь subgraph EXTERNAL вокруг PHONE и INPUT"

## Шаг 1: Прочитать style guide

Прочитай `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md`. Тебе нужны §1 (palette), §5 (naming), §7 (do/don't).

## Шаг 2: Прочитать target файл

```python
# Read tool — full file
```

Найди границы mermaid block: между `\`\`\`mermaid` и закрывающим `\`\`\``.

## Шаг 3: Понять change request

Распарси `<change>` в одно из категорий:

| Категория | Действие |
|---|---|
| **Add node** | Найди логичное место, добавь node definition + edge(s). Назначь classDef из §1 palette по типу. |
| **Remove node** | Удали node definition + все edges to/from него. |
| **Rename node** | Заменить ID везде (definition + all edges + classDef apply). Используй find-and-replace на ID exact match. |
| **Change edge style** | Поменяй `-->` на `==>` (thick) или `-.->` (dashed) per request. |
| **Add edge** | Добавь edge между existing nodes; place в logical section (не вперемешку с node defs). |
| **Remove edge** | Удали exact edge line. |
| **Change color** | Найди classDef и измени fill/stroke. Используй §1 canonical color! Если новый цвет нужен вне palette — STOP, спроси Ruslan и предложи extension в style guide. |
| **Add subgraph** | Wrap нодов в `subgraph FOO ["Title"] ... direction TB ... end`. Не nest >2 уровней. |
| **Change direction** | Меняй `flowchart TB` ↔ `flowchart LR` (top-down vs left-right). Subgraphs тоже могут иметь свой direction. |
| **Add classDef** | Определи внизу diagram body (НЕ в середине). Использует §1 palette colors. |
| **Restructure layout** | Перегруппируй edges / subgraphs. Beware — может ломаться. Сделай минимальное изменение, не rewrite all. |

Если `<change>` не parseable в эти категории — спроси clarification.

## Шаг 4: Применить change

Используй **Edit** tool с минимально возможным `old_string` / `new_string` block. **Не rewrite all file** — только targeted change.

Принципы:
1. **Append-friendly.** Новые nodes / edges — в конец logical section.
2. **classDef в конце.** Если добавляешь новый classDef — append к existing classDef block в конце body.
3. **Preserve comments `%%`.** Если есть section markers — встрой change в правильную section.
4. **Никогда не меняй init directive** без явного запроса.

## Шаг 5: Validate basic syntax

Проверь:
- [ ] Балансировка скобок: для каждого `[` есть `]`, для `(` — `)`, для `{` — `}`.
- [ ] Каждый `subgraph` имеет matching `end`.
- [ ] Каждый `:::className` имеет matching `classDef <className> ...` объявление.
- [ ] Init directive остался на первой строке mermaid block.
- [ ] Diagram type declaration (`flowchart TB` / `sequenceDiagram` / etc.) сохранён.
- [ ] Reserved keywords (`end`, `class`, etc.) не использованы как node IDs.

Если нарушено — fix перед save.

## Шаг 6: Update frontmatter (если style guide change)

Если diagram radically изменилась (e.g. полная переработка structure):
- bump `versioning.changelog` в frontmatter (если есть)
- update `purpose:` если он stale
- НЕ меняй `date:` — date это creation date, не last-edit. Last-edit прослеживается через git.

## Шаг 7: Сообщить пользователю

Кратко:
- Файл: `<path>`
- Что изменено: `<one-line summary>`
- Validation: `passed | warnings: <list>`
- Render verify: открой в GitHub UI или Antigravity preview

## Шаг 8: Лог

```
[YYYY-MM-DD] mermaid-iterate: <file> ← <change summary>
```

в `swarm/wiki/log.md`.

## Правила

1. НЕ rewrite файл целиком — Edit tool с targeted changes.
2. НЕ выходи за §1 palette без user ack.
3. НЕ удаляй frontmatter, init directive, или source links footer.
4. НЕ commit автоматически — Ruslan reviews перед merge.
5. Если change ambiguous — спроси clarification.
6. Если change ломает diagram (broken syntax) — STOP, surface error пользователю, не save broken state.
7. Subgraph nesting ≤2 уровней — если change добавляет >2, refuse и предложи alternative.

## Ошибки

- Замена `MASTER` на `OWNER` — make sure ВСЕ references updated, не только definition.
- Добавление edge to/from node which doesn't exist — Mermaid silently рендерит phantom node. Ensure both endpoints declared.
- Adding classDef apply без declaring classDef — silently ignored. Always declare ДО use.

## Cross-references

- Create skill: `/mermaid-create`
- Validate skill: `/mermaid-validate` — для standalone syntax check
- Style guide: `swarm/wiki/operations/mermaid-style-guide-2026-05-07.md`
