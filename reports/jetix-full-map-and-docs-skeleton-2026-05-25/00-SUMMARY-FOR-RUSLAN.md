---
title: 00-SUMMARY-FOR-RUSLAN — Jetix Full Map + Docs Skeleton
date: 2026-05-25
type: summary
parent_main: decisions/strategic/JETIX-FULL-MAP-AND-DOCS-SKELETON-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2-F3
language: russian primary
word_target: <=1000 (master run — длиннее обычного)
---

# 📄 SUMMARY для Руслана — Full Map + Docs Skeleton (10 минут)

> Главный документ: `decisions/strategic/JETIX-FULL-MAP-AND-DOCS-SKELETON-2026-05-25.md`
> (45-60 мин). Этот SUMMARY — быстрый обзор. **15 решений ждут тебя — §12 main.**

## За 30 секунд

Это финальная organize-итерация перед фиксацией baseline. Сделали две вещи:
**(A)** карта всего, что Jetix есть на 25.05 (12 сущностей + 6 направлений + статус +
устаревшее); **(B)** скелет всех документов, которые должны быть у нормальной корпорации
(94 документа по 12 категориям + GAP + приоритеты). Финал — **master skeleton**: одна
структура, которую ты фиксируешь, и дальше «не добавляем новое — подтягиваем под скелет».

## Что Jetix есть (Task A)

**Зрелый substrate без выхода наружу.** Внутри построено всё; снаружи — недостроено.

- **🔵 Ядро (готово 85-95%):** Метод (V2 LOCKED), Инструменты (54 skills + 17 агентов),
  Корпорация (Foundation 11 Parts LOCKED), Research (5 deeps + 80+ книг + 750 wiki). Глубина
  saturated — **накопление останавливаем (O-163)**.
- **🟢 Рост (40-70%):** Платформа (Build середина), Заработок (V10, 8 моделей), Образование
  (7 ступеней + прошивка). Здесь дыры.
- **🟠 Люди (40-65%):** Партнёры (4 типа, Wave 1 готов), Community (Charter текста нет).
- **🔴 Защита (75-90%):** R12 (LOCKED), Governance (Stage Gates), Anchors (29 D-LOCK).

**Build readiness ≈ 70%.** Внутренние сущности ~93%, outward ~48%. Маховик пока на твоих руках.

**6 направлений:** Платформа · Кооп-экономика · Дистрибуция · AI-электрификация · Tier-1
outreach · Network State. **Все активные упираются в видео A.**

## Какие документы должны быть (Task B)

**94 документа по 12 категориям: 36 ✅ / 25 ⚠️ / 33 ❌.** Полностью/частично закрыто 65%.

**5 категорий-дыр:** Brand (25%), Financial (38%), HR (43%), Legal (44%), Community (56%).
**Закрыто:** Research (100%), Methodology/Operational/Risk (86%), Partner-facing (78%).

**Главный вывод:** мы не недоинвестировали в понимание (глубина закрыта) — мы
недоинвестировали в **упаковку наружу** (Brand/Partner) и **operational-рост**
(HR/Legal/Financial). Есть «вторая волна» дыр (HR/Legal entity/Financial-ops), невидимая в
текущем DOCS-CLASSIFICATION, но критичная при найме 5 ассистентов (Build→Run).

**7 референсов** (Apple/Tesla/Mondragón/Berkshire/коопы/Anthropic) подтверждают: Jetix =
кооператив + deep-tech + методология одновременно. Бóльшая часть «правильных» документов
**уже в substrate** — просто не оформлена в нужном жанре.

## Master skeleton (для фиксации)

**4 super-кластера × 12 сущностей + 5 cross-cutting docs.** Документы организуются ПОД
сущности (что описываем), а жанр (категория) — вторично. Один документ может покрывать
несколько сущностей.

**5 cross-cutting (соединительная ткань):** Vision (12/12) · **Charter (8/12)** · видео C
(6/12) · Economic V10 (5/12) · R12 checklist (5/12). **Charter и видео C — самые рычажные:**
один Charter закрывает фрагменты 8 сущностей.

## Что делать (приоритеты — но решаешь ты)

**Build P0 (5):** видео A · Charter v1 текст · Notion Personal OS implement · legal entity
старт · discovery script универсальный.
**Build P1 (6):** лендинг+FAQ · видео B/C · invoice/contract · partner agreement.

**Два факта зависимости (не команда):**
1. Видео A — единственный блокер, держащий 4 сущности сразу (Платформа/Партнёры/
   Образование/Дистрибуция). По топологии — первый рычаг.
2. ⅔ missing-docs (Run/Scale) **намеренно** отложены — рано (ловушка «накопить ещё»).

**3 варианта sequencing:** (A) видео A первым · (B) parallel tracks (видео ∥ Charter ∥
legal) · (C) quick-wins first (Steuerberater email + discovery script + D-LOCK promote).

## Quick wins (дёшево, прямо сейчас)
Steuerberater email (~30 мин) · discovery script универсальный (~1-2ч) · JETIX-NAVIGATION
polish · батч-promote 29 D-LOCK (Wave 1.4) · FAQ structure.

## Что устарело (drop ≠ delete)
Legacy 12-агентный roster → ROY swarm · Method V1 → V2 · старые tokenomics → V10 ·
`distribute.py` заархивирован. НЕ устарело: книги, research-deep'ы, wiki (depth-refs).

## 10 схем (JE-1..JE-10)
В `diagrams/_INDEX.md`: дерево сущностей · направления×горизонты · готовность · таксономия
docs · категории overlay · GAP heat · таймлайн · мастер-дерево · матрица сущность×категория ·
Build overlay.

## Твои 15 решений (§12 main)
Главные: **(1)** master skeleton ОК или правки? **(2)** консолидировать сущности (Governance⊂
Корпорация)? **(5)** 12 категорий ОК? **(7)** Charter + видео C первыми (рычаг)? **(8)** Build
sequencing A/B/C? **(15)** какой первый prompt после фиксации?

## К чему ведёт
После твоего ack — master skeleton зафиксирован как THE primary structure. Дальше каждый
новый документ имеет место, каждая дыра видна. **Следующие шаги запускаешь ты сам** (pool
result, не auto): заполнение видео A spec / Charter текст / запрос для партнёров.

**Каша заканчивается здесь.**

---

*SUMMARY closure. Task A (12 сущностей + 6 направлений + 70% + outdated) + Task B (94 docs +
36✅/25⚠️/33❌ + P0-P4) + master skeleton (4 кластера + 5 cross-cutting). 10 mermaid. R1
surface — 15 решений §12 main. Pool result.*
