---
type: knowledge
pipeline: compiled
topic: ai-consulting/product
confidence: medium
created: 2026-04-08
updated: 2026-04-08
tags:
  - "#type/knowledge"
  - "#topic/product"
  - "#topic/eu-ai-act"
  - "#topic/consulting"
sources:
  - id: notion/33c2496333bf81ea984bcfa0ae711b23
    facts: [product-spec, economics, versions, legal-questions, plan]
---

# Productized AI Readiness Assessment

> **Суть:** Онлайн self-assessment tool — компания проходит опросник за 15-30 мин, получает автоматический персонализированный отчёт с risk score, gap analysis и приоритетными действиями по EU AI Act.
> **Статус:** Гипотеза — нужна проработка и валидация

## Зачем
Быстрый путь к первым деньгам + масштабируемый продукт. Маргинальная стоимость одного assessment ≈ €0.50 (API), при цене €200-500 = экстремальная маржинальность. Плюс каждый прошедший = данные для ICP + potential upsell.

Одновременно: standalone продукт (€200-500), лид-магнит (бесплатная версия), и входная точка в воронку Jetix (Training → Assessment → Pilot → Retainer).

## Точка А
- Идея сформулирована как гипотеза
- Нет прототипа, нет лендинга, нет трафика
- Есть глубокое знание EU AI Act (из ресёрча)
- Есть навык работы с Claude API, Notion, веб-формами
- Нет юридической базы (Gewerbe, страховка) — БЛОКЕР?

## Точка Б
- Работающий tool: лендинг + опросник + автогенерация отчёта
- 10+ компаний прошли assessment
- 2-3 upsell в полный аудит или workshop
- Стабильный трафик 50-100 компаний/мес

## Как это работает
1. **Лендинг** — Carrd/Webflow/custom. CTA: «Узнайте за 15 минут, готова ли ваша компания к EU AI Act»
2. **Опросник** — Typeform / Tally / custom React. 30-50 вопросов: AI Inventory, Risk Classification, Data Governance, Documentation, Human Oversight, AI Literacy
3. **Бэкенд** — ответы → Claude API → персонализированный отчёт: risk score (0-100), gap analysis по статьям AI Act, приоритетные действия, дедлайны
4. **Отчёт** — PDF 5-10 страниц, брендированный Jetix. Отправка на email
5. **Upsell** — в конце отчёта: «Хотите полный аудит? Запишитесь на discovery call»

## Версии продукта

**v0 — Бесплатный лид-магнит:**
- 10-15 вопросов, risk score + 1 страница рекомендаций
- Цель: сбор email, awareness

**v1 — Платный assessment (€200-500):**
- 30-50 вопросов, полный отчёт 5-10 стр с gap analysis
- Цель: revenue + квалификация лидов

**v2 — Premium + консультация (€500-1000):**
- v1 + 30 мин видеозвонок с разбором результатов
- Цель: high-ticket upsell в Pilot

## Открытые вопросы

### Юридика
- Можно ли продавать без Gewerbeanmeldung?
- Нужен ли disclaimer «это не юридическая консультация»?
- Rechtsdienstleistungsgesetz: авто-отчёт = юр. консультация или техническая оценка?
- Aufenthaltstitel: разрешает ли онлайн-продукт?
- Berufshaftpflicht: нужна ли?

### Рынок
- Существуют ли аналоги (AI Act self-assessment tools)?
- Готовы ли KMU платить €200-500 за автоматический отчёт?
- Какой формат предпочитают: онлайн tool vs Excel vs PDF?

### Трафик
- Каналы: LinkedIn (DE), IHK, Bitkom, партнёрства, контент
- CAC? SEO: «AI Act compliance check», «KI-Verordnung Selbstbewertung»?
- Партнёрства: IHK, Bitkom, Steuerberater, Rechtsanwälte?

### Техника
- Claude API: качество генерации отчёта — нужен тест
- PDF-генерация: Puppeteer, WeasyPrint, LaTeX?
- Стоимость API per assessment: подсчитать tokens

## Экономика (гипотеза)

| Метрика | Значение |
|---------|----------|
| Стоимость разработки | 3-5 дней (= €0, только время) |
| Стоимость API per assessment | ~€0.30-0.50 |
| Цена v1 | €200-500 |
| Маржа | ~99% |
| Break-even | 1 продажа |
| Target: 50/мес × €300 | = €15K/мес |
| Target: 100/мес × €300 | = €30K/мес |
| CAC (гипотеза) | €20-50 через LinkedIn/контент |
| LTV (с upsell) | €2-5K (если 10-20% берут аудит) |

## План действий

### Фаза 0: Валидация (1 неделя)
- [ ] Проверить юридические блокеры
- [ ] Изучить конкурентов
- [ ] Поговорить с 3-5 людьми из target audience
- [ ] Составить драфт опросника (30 вопросов)

### Фаза 1: MVP (1 неделя)
- [ ] Лендинг (1 день)
- [ ] Опросник в Typeform/Tally (1 день)
- [ ] Claude API integration + PDF генерация (2-3 дня)
- [ ] Тест на себе / знакомых

### Фаза 2: Запуск (2-4 недели)
- [ ] Бесплатная версия (v0) как лид-магнит
- [ ] LinkedIn-посты (серия про AI Act)
- [ ] Outreach к IHK, Bitkom
- [ ] Первые 10 платных assessments

### Фаза 3: Масштабирование
- [ ] SEO + контент-маркетинг
- [ ] Партнёрства (Steuerberater, Rechtsanwälte)
- [ ] Автоматизация upsell воронки
- [ ] v2 с консультацией

## Синергия с Jetix
- **Лид-магнит** → бесплатная версия собирает email
- **Standalone продукт** → revenue с первого дня
- **Входная точка в воронку** → Assessment → Workshop → Full Audit → Retainer
- **ICP данные** → реальные данные о проблемах KMU
- **Proof of expertise** → «мы помогли 100+ компаниям»
- **Масштабируемость** → не продаём время, продаём продукт

## Идеи
- Бесплатная версия может стать вирусной (shareable score: «ваш AI Act readiness: 34/100»)
- Партнёрство со Steuerberater/Rechtsanwälte = встроенный канал
- White-label версию другим консалтингам

---
*Создан: 08.04.2026*
