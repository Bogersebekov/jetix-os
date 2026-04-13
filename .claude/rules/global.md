---
type: meta
created: 2026-04-13
---

# Global Rules — Claude Code

## Файлы
- YAML frontmatter обязателен в каждом .md файле (кроме README.md)
- Проверь что файл не существует перед созданием нового
- Именование: kebab-case, даты YYYY-MM-DD

## Логи
- Append-only: новые записи добавляются СВЕРХУ существующих
- НЕ удаляй и НЕ редактируй старые записи
- При >30 записей в log.md — ротировать в archive/

## Knowledge Base
- Перед поиском информации — сначала проверь `_moc.md` в соответствующем кластере KB
- Затем grep по frontmatter tags
- Затем full-text grep
- Если нет результатов — сообщи, не выдумывай

## Git
- Commit в конце каждой рабочей сессии
- Формат: `[area] описание` (пример: `[kb] add pricing-models article`)
- Области: daily, project, kb, raw, crm, meta, skills, infra

## Безопасность
- НИКОГДА не трогай: ~/.ssh/, /etc/, .env, private/
- НЕ устанавливай пакеты без одобрения
- НЕ удаляй файлы без подтверждения

## Язык и стиль
- Русский — основной язык
- Прямой, без воды
- Если неясна задача — уточни, не додумывай

## Конвенции
- Полные правила: `_meta/conventions.md`
- Wiki pipeline: `_meta/pipeline-spec.md`
