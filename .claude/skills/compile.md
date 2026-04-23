# Skill: /compile

> **Exclusion (per D7 + D8 §8.8.3) — DEPRECATED.** This skill is NOT
> parameterised for `$WIKI_ROOT`. Rationale: zero `wiki/` references;
> targets `knowledge-base/{cluster}/_moc.md` and
> `knowledge-base/{cluster}/{topic}.md`. Legacy pre-v2 skill that
> synthesises raw → KB-article. Per Sub-agent D §7 transplant table:
> "drop (or rewrite); Targets legacy knowledge-base/; supplanted by
> `/ingest` + `/ask` in v2." Phase-A deprecation note added to
> `swarm/wiki/log.md`. File retained for legacy `knowledge-base/` use
> until MIGRATION.md finalises; NOT part of v3 wiki-skill set.

## Описание
Синтезировать из нескольких ingested raw-файлов одну KB-статью.

## Триггер
`/compile {topic}` — тема для компиляции (например: `pricing-models`, `competitors`).

## Алгоритм

### 1. Найти источники
Искать ingested raw-файлы по теме:
a) Grep по frontmatter tags в `raw/`
b) Проверить `_moc.md` в соответствующем кластере KB
c) Спросить Руслана, какие файлы включить (если неясно)

### 2. Прочитать Extracted Facts
Для каждого найденного raw-файла прочитать секцию "Extracted Facts".

### 3. Синтезировать
Создать KB-статью в `knowledge-base/{cluster}/{topic}.md`:
- Использовать шаблон `templates/tpl-kb-article.md`
- Синтезировать факты из всех источников
- Добавить inline provenance: `[src:filename]` для каждого факта
- Заполнить `sources:` в frontmatter
- Отметить пробелы: `[ПРОБЕЛ]`
- Отметить противоречия: `[ПРОТИВОРЕЧИЕ]`
- Установить `confidence:` на основе качества источников

### 4. Обновить обратные ссылки
В каждом использованном raw-файле обновить frontmatter:
```yaml
extracted_to:
  - knowledge-base/cluster/topic.md
```

### 5. Обновить _moc.md
Добавить новую статью в `knowledge-base/{cluster}/_moc.md`.

### 6. Подтвердить
Показать Руслану статью. После подтверждения — сохранить, git commit.

## Правила
- Каждый факт должен иметь `[src:filename]`
- Не выдумывать факты — только из источников
- Если источники противоречат — отметить `[ПРОТИВОРЕЧИЕ]` и описать
- `confidence: high` только если 2+ независимых источника согласны

## Оценка токенов
Чтение: ~18,000 | Генерация: ~3,000 | Итого: ~21,000 (2.1% от 1M)
