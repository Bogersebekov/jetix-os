---
type: knowledge
pipeline: compiled
topic: ai-consulting/infrastructure
confidence: high
created: 2026-04-03
updated: 2026-04-03
tags:
  - "#type/knowledge"
  - "#topic/infrastructure"
  - "#topic/notion"
  - "#topic/workspace"
sources:
  - id: notion/3372496333bf81809f39ffdf2fb5398d
    facts: [architecture, target-state, mvp, databases, templates, data-flows, decisions]
---

# Архитектура рабочего пространства Jetix

**Статус:** Утверждено 03.04.2026

## 1. Философия
Jetix Workspace — отдельное от Life OS пространство, управляющее всем бизнесом. В Life OS — только карточка проекта со ссылкой. Система спроектирована как самообучающаяся: каждый проект, каждый звонок, каждый эксперимент делает агентство умнее через Feedback Loop.

**Принципы:**
1. Разделение контекстов — Life OS и Jetix не пересекаются
2. Масштабируемость с первого дня
3. Системное хранение знаний
4. Второй мозг компании — эффект снежного кома
5. Поддержка операционки

## 2. Target State — 11 секций sidebar

1. **Jetix Command Center** — главный дашборд, linked views: задачи, эксперименты, revenue, pipeline, статус проектов
2. **Company Hub** — миссия, ценности, OKR, позиционирование, Security & Compliance
3. **Clients OS** — карточки клиентов, Client Portals (shared pages), история, NPS
4. **Fulfillment (Projects & Tasks)** — канбан Assessment → Pilot → Retainer, задачи, Lessons Learned
5. **Sales & Marketing** — воронка (Lead → Won/Lost), Content Calendar, связь Pot of Gold (контент ↔ сделки)
6. **Knowledge Base** — SOP, AI Case (50+), EU AI Act, Framework, Prompt Library, Security Policy
7. **Team Hub** — команда + Consultant Portal (тренинг, Prompt Library, pipeline)
8. **Hiring OS** — на старте простая страница
9. **Finance OS** — на старте простая таблица
10. **Security & Compliance** — подсекция Company Hub, потом отдельная
11. **System Databases** — скрытый раздел, все мастер-БД

## 3. Базы данных — 8 БД полный набор

| БД | Ключевые поля | Relations |
|----|--------------|-----------|
| **Clients** | Name, ICP Type, Status, Total LTV, Vault Link | → Projects, → Sales, → Client Wins |
| **Sales Pipeline** | Lead Name, Stage, Source, Expected Value, Content Source | ↔ Clients, ↔ Team |
| **Projects** | Name, Funnel Stage, Status, Lessons Learned | ↔ Clients, ↔ Tasks |
| **Tasks** | Name, Status, Priority, Due Date | ↔ Projects, ↔ Team |
| **Knowledge Base** | Title, Type (SOP/AI Case/Prompt/EU AI Act), Industry, Status | — |
| **Team & Consultants** | Name, Role, Skills | ↔ Projects, ↔ Tasks |
| **Hypotheses** | Name, Area, Status (Idea→Testing→Validated→Rejected→Scaled), Metric, Result | ↔ Projects, ↔ Team |
| **Client Wins** | Win, Impact (€), Date | ↔ Clients, ↔ Projects |

**Главная цепочка:** Sales → Client → Projects → Tasks → Team
**Поперечные:** Hypotheses связывает всё, KB питается от Projects и питает Sales

## 4. Потоки данных (5 потоков)

1. **Продажи → Клиент → Проект:** Лид → Sales Pipeline → Client → Project → Tasks
2. **Проект → Знания:** Lessons Learned → SOP / AI Case в KB → Prompt Library → Client Win
3. **Знания → Продажи (Feedback Loop):** AI Case → контент → новый лид → Sales Pipeline
4. **Гипотезы (поперечный):** Инсайт → Hypotheses → тест → Weekly Review → успех = SOP + масштабирование / провал = урок
5. **Консультанты (платформа):** Training → Prompt Library + KB → лид → Project через систему → результаты → общая KB

## 5. Шаблоны (6 шт.)
- **Новый клиент** — онбординг, контакты, контракт, портал
- **Проект (Assessment)** — kickoff, сбор данных, аудит, отчёт, презентация
- **Проект (Pilot)** — план внедрения, задачи, KPI, чекпоинты
- **SOP / AI Case** — описание, владелец, статус, видео, отдел
- **Онбординг сотрудника** — чек-лист задач, SOP
- **Встреча** — повестка, решения, action items

## 6. MVP (что строим сейчас)

**6 секций + System Databases:**
1. Command Center (4 linked views)
2. Company Hub + Security Basics
3. Clients OS
4. Fulfillment (Projects + Tasks)
5. Sales & Marketing (Pipeline + контент)
6. Knowledge Base

**5 БД MVP:** Clients → KB → Sales Pipeline (↔ Clients) → Projects (↔ Clients) → Tasks (↔ Projects)

**3 потока MVP (всё вручную):**
1. Продажи → Работа: Лид → Pipeline → Client → Project → Tasks
2. Работа → Знания: Lessons Learned → SOP/AI Case (вручную)
3. Знания → Продажи: AI Case → контент → лид (вручную)

**3 шаблона MVP:** Client Card, Project, AI Case Study

## 7. Инструменты

| Инструмент | Роль | Когда |
|-----------|------|-------|
| Notion | Ядро: БД, задачи, CRM, wiki | Сейчас |
| 1Password/Bitwarden | Password manager, vault per client | Сейчас |
| Miro | Визуализация | Сейчас |
| Claude/Gemini | AI-ассистенты | Сейчас |
| Google Sheets | Финмодели | По необходимости |
| Zapier/Make | Автоматизация | Фаза 2 |
| Slack/Telegram | Коммуникация | Фаза 2 |

## 8. Еженедельный ревью Jetix
1. Sales & Marketing: лиды, звонки, сделки
2. Clients: статус, инсайты, обновить ICP
3. Projects: прогресс, блокеры
4. Hypotheses: тестируем, подтвердились, отклонили
5. Knowledge Base: новые кейсы/SOP?
6. Метрики: MRR, pipeline, конверсия
7. Инсайты недели: топ-3 урока
8. Фокус на следующую неделю: топ-3 приоритета

## 9. Ключевые решения (утверждены 03.04)
1. Notion = ядро. Miro для визуализации, Google Sheets для расчётов
2. 8 БД полный набор, MVP = 5
3. Принцип «1 мастер-БД, много views»
4. Password Manager с первого дня
5. Security & Compliance встроена с первого дня
6. Feedback Loop = двигатель роста
7. Prompt Library = ядро AI-агентства
8. Consultant Portal = фундамент платформы
9. Pot of Gold: Content Calendar ↔ Sales Pipeline
10. Воронка = этапы CRM: Training → Assessment → Pilot → Retainer

## Визуализация
[Miro — Jetix Workspace](https://miro.com/app/board/uXjVG2-05Ns=/) — 4 диаграммы: Target State (структура + потоки), MVP (структура + потоки)

---
*Утверждено: 03.04.2026*
