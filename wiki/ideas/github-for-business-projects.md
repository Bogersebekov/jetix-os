---
title: "GitHub для бизнес-проектов — платформа коллаборации с курацией и AI"
type: idea
niche: business
status: raw
sources:
  - raw/notion-ideas/2026-04-16-github-for-business-projects.md
related:
  - concepts/curated-community-access.md
  - concepts/collaborative-project-versioning.md
  - claims/business-projects-like-code.md
  - sources/2026-04-16-github-for-business-projects.md
tags: [#type/idea, #status/raw, #topic/community, #topic/platform]
topics: [system-design]
created: 2026-04-16
updated: 2026-04-16
confidence: medium
pipeline: ingested
---

# GitHub для бизнес-проектов — платформа коллаборации с курацией и AI

## Одна строка

Jetix как платформа, где предприниматели работают над проектами по модели GitHub: прозрачно, совместно, с контролем версий, с AI-усилителем и курированным допуском.

## Обоснование

[[claims/business-projects-like-code]] — над бизнес-проектами можно работать теми же принципами, что и над кодом: версии, merge, обсуждения, прозрачность. Если это верно, нужен инструмент, в котором эти принципы встроены.

GitHub доказал ценность такой модели для разработки. Тех же принципов не хватает для бизнеса, стартапов, открытий. [[concepts/collaborative-project-versioning]] решает проблему «каждый предприниматель делает всё в одиночку и теряет опыт».

## Предполагаемый эффект

- **Для кого:** предприниматели / эксперты / AI-консультанты в сообществе Jetix.
- **Что меняется:**
  1. Эффективнее работа над проектами (совместность + версии).
  2. Накопление коллективных знаний ([[concepts/knowledge-wiki-layer]] — будущая страница).
  3. Среда из проверенных людей ([[concepts/curated-community-access]]).
  4. AI как усилитель каждого ([[entities/claude-code]]).
- **Метрика:** активные контрибьюторы × количество живых проектов.

## Компоненты

| Слой | Что | Референс |
|------|-----|----------|
| Безопасная ОС | Linux-подобная среда для работы | [[entities/linux]] |
| Коллаборация | GitHub-подобный инструмент для проектов | [[entities/github]] |
| AI-усилитель | Claude для ускорения работы каждого | [[entities/claude-code]] |
| Wiki / KB | Сохранение экспертизы | wiki/ сам по себе |
| Курация | Отбор участников перед допуском | [[concepts/curated-community-access]] |

## Что уже известно / проверено

- Модель работает в open-source разработке (Linux, GitHub).
- «Не каждый может контрибьютить» — паттерн из Apache Software Foundation, Linux Kernel.
- Параллель с ранним Y Combinator и Founders Fund — курация + коллаборация.

## Следующий шаг

- [ ] Набросать user journey: как новый участник попадает в сообщество.
- [ ] Определить, что ЯВЛЯЕТСЯ репозиторием бизнес-проекта (документы? tasks? commits?).
- [ ] Сравнить с существующими попытками: Slack-коммьюнити, Notion-workspace, Lattice, Obsidian Publish.

## Связи

- Расширяет: [[concepts/curated-community-access]], [[concepts/collaborative-project-versioning]]
- Опирается на: [[claims/business-projects-like-code]]

## Источники

- [[sources/2026-04-16-github-for-business-projects]]
