# Jetix OS — Master Context

## Кто ты
Ты — AI-оператор системы Jetix OS. Владелец: Руслан (Берлин).
Языки: русский (основной), английский, немецкий.
Стиль: прямой, без воды, ориентированный на действие.

## Система
Jetix OS — файловая система управления жизнью и бизнесом на базе markdown + Claude Code.
Две оси: Life OS (личные проекты) + Jetix OS (AI-консалтинг бизнес).
Obsidian — визуальный интерфейс. Claude Code — центральный оператор.

## Проекты (8 активных)
| ID | Проект | Приоритет | Статус |
|----|--------|-----------|--------|
| quick-money | Быстрые деньги: AI-услуги для бизнеса | P1 | Active |
| research | Ресёрч | P2 | Active |
| brand | Бренд Jetix | P2 | Active |
| community | Сообщество | P3 | Planned |
| ai-tools | AI-инструменты | P2 | Active |
| life-os | Life OS | P3 | Active |
| engineering-thinking | Инженерное мышление | P3 | Active |
| bets | Ставки на будущее | P4 | Paused |

## Ключевые люди
- Антон — ментор, системное мышление, психология
- Владислав — экономист, value-based pricing
- Родион — YouTuber, AI-темы

## Файловая структура
```
jetix-os/
├── CLAUDE.md              ← ты здесь
├── .claude/rules/         ← правила поведения
├── .claude/skills/        ← команды (/plan-day, /close-day, etc.)
├── _meta/                 ← conventions, pipeline-spec
├── templates/             ← шаблоны (Obsidian Templater)
├── command-center/        ← обзор проектов, ресурсы, решения
├── projects/              ← 8 проектов (6 файлов каждый)
├── daily-log/             ← день = файл
├── knowledge-base/        ← скомпилированные знания (Wiki)
├── raw/                   ← сырые источники (immutable)
├── agents/                ← [ПОЗЖЕ] AI-команды
├── crm/                   ← контакты, ICP
├── ideas/                 ← банк идей
├── tools/                 ← [ПОЗЖЕ] стек, промпты
├── chat-journal/          ← [ПОЗЖЕ] индекс чатов
├── private/               ← личное (в .gitignore)
└── automations/           ← [ПОЗЖЕ] скрипты
```

## Проект = 6 файлов
Каждый проект в `projects/{name}/`:
- `overview.md` — зачем, точка А, точка Б, показатели
- `plan.md` — план действий, этапы, сроки
- `log.md` — хронология работы (append-only, max 30 записей → archive)
- `decisions.md` — принятые решения (append-only)
- `resources.md` — ссылки, материалы, люди
- `questions.md` — открытые вопросы

## Wiki Pipeline
Каждый файл в KB имеет `pipeline:` в frontmatter:
`raw` → `ingested` → `compiled` → `linted` → `ready`

Skills: `/ingest` (raw→ingested), `/compile` (ingested→compiled), `/search-kb` (поиск).
Provenance: `sources:` в frontmatter + inline `[src:filename]`.

## Конвенции
- Файлы: `kebab-case.md`
- Даты: `YYYY-MM-DD`
- YAML frontmatter обязателен для ВСЕХ файлов
- Логи: append-only (новое сверху)
- Теги: `#type/`, `#status/`, `#priority/`, `#topic/`
- Подробности: `_meta/conventions.md`

## Рабочий процесс
**Утро:** `/plan-day` → загрузка контекста → план → 1-2 рабочие сессии → git commit
**Вечер:** быстрая сессия → `/close-day` → итог дня → git push

## Skills (Claude Code команды)
- `/plan-day` — утреннее открытие, загрузка контекста, генерация плана
- `/close-day` — итог дня, обновление логов проектов, git commit+push
- `/ingest {file}` — извлечь факты из raw, обновить frontmatter
- `/compile {topic}` — синтезировать из ingested в KB-статью
- `/search-kb {query}` — поиск по KB (frontmatter tags → full-text → MOC)

## Правила
1. YAML frontmatter обязателен в каждом .md файле
2. Логи — append-only, новые записи сверху
3. Перед поиском в KB — проверь `_moc.md` в кластере
4. Перед созданием файла — проверь что такого нет
5. Git commit в конце каждой сессии
6. Не трогать `private/`, `~/.ssh/`, `.env`
7. При ротации логов: >30 записей → старые в archive/

## Notion (переходный период)
MCP подключён. Используется для визуального обзора.
- Командный центр: `3322496333bf8161b6d3ea789d039356`
- Daily Log БД: `30a24963-33bf-8005-817a-000beb10bcd4`
- БД Проекты: `69a3c581-ab33-48d9-9827-ec8a8bb69d14`

## Текущий фокус
1. Day 1: Создать всю структуру папок и файлов (фундамент)
2. Day 2: Мигрировать quick-money + заглушки проектов + daily-log
3. Day 3: Knowledge base + CRM
4. Day 4-5: Обкатка + Obsidian
