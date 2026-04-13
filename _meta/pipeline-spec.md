---
type: meta
created: 2026-04-13
updated: 2026-04-13
---

# Wiki Pipeline — Спецификация

## Обзор
Каждый файл знаний проходит через pipeline стадий. Стадия хранится в YAML frontmatter (`pipeline:`), НЕ определяется физическим расположением файла.

## Стадии

### 1. raw
**Где:** `raw/{research,transcripts,voice-memos,imports}/`
**Что:** Оригинальный неизменённый текст из внешнего источника.
**Правило:** Тело файла НИКОГДА не редактируется после создания.
**Frontmatter:** `pipeline: raw`, `processed: false`

### 2. ingested
**Где:** Тот же файл в `raw/` (обновляется frontmatter + добавляется секция)
**Что:** Skill `/ingest` обработал файл — извлёк ключевые факты.
**Действия `/ingest`:**
1. Прочитать raw-файл
2. Извлечь факты, данные, цитаты
3. Добавить секцию `## Extracted Facts` в конец файла (после оригинального текста)
4. Обновить frontmatter: `pipeline: ingested`, `processed: true`
5. НЕ менять оригинальный текст выше Extracted Facts
**Frontmatter:** `pipeline: ingested`, `processed: true`, `extracted_to: []`

### 3. compiled
**Где:** `knowledge-base/{cluster}/`
**Что:** Skill `/compile` синтезировал из нескольких ingested-файлов в одну KB-статью.
**Действия `/compile`:**
1. Найти все ingested raw-файлы по теме (через tags или прямой запрос)
2. Синтезировать факты в связный текст
3. Добавить inline provenance: `[src:filename]` для каждого факта
4. Заполнить `sources:` в frontmatter со ссылками на raw-файлы
5. Обновить `extracted_to:` в raw-файлах (обратная ссылка)
**Frontmatter:** `pipeline: compiled`, `confidence: low|medium|high`

### 4. linted
**Где:** Тот же файл в `knowledge-base/`
**Что:** Проверка актуальности, непротиворечивости, полноты.
**Действия:** Ручная или через skill `/lint` (позже).
**Frontmatter:** `pipeline: linted`

### 5. ready
**Где:** Тот же файл в `knowledge-base/`
**Что:** Финальная проверка пройдена, данные актуальны.
**Frontmatter:** `pipeline: ready`

## Переходы

```
raw ──/ingest──→ ingested ──/compile──→ compiled ──/lint──→ linted ──→ ready
 │                                          │
 │  (тот же файл в raw/)           (новый файл в knowledge-base/)
 │  (добавляется секция)           (синтез из нескольких raw)
```

## Правила
1. Raw-файлы живут ТОЛЬКО в `raw/`. Compiled-файлы — ТОЛЬКО в `knowledge-base/`.
2. Один compiled-файл может ссылаться на несколько raw-файлов.
3. Один raw-файл может быть использован в нескольких compiled-файлах.
4. `sources:` в frontmatter compiled-файла = список raw-файлов с перечнем фактов.
5. `extracted_to:` в frontmatter raw-файла = обратные ссылки на compiled-файлы.
6. При обновлении raw-источника — пометить связанные compiled как `pipeline: compiled` (нужна повторная lint-проверка).

## Inline Provenance
Формат: `[src:filename]` (без пути, без .md)
Пример: `Средняя ставка AI-консультантов в DACH: €150-250/час [src:pricing-dach-perplexity]`
Filename = имя raw-файла без расширения и без пути.
