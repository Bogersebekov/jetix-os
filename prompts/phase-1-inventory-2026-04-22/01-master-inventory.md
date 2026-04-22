---
id: phase-1-master-inventory-2026-04-22
title: Master Inventory — все существующие research / docs / artifacts для Jetix System Synthesis
author: cloud-cowork
date: 2026-04-22
audience: server-cc (Opus 4.7 1M, extended thinking max)
expected-duration: 3-5h
status: active
---

# Phase 1: Master Inventory — Task for Server CC

## Role

Ты — **research archivist + gap analyst**. Задача — создать полный inventory
всего что у нас УЖЕ есть по темам Compounding Engineering / multi-agent / swarm /
AI-native OS / Claude Code best practices / knowledge management + foundation
documents. Это baseline для всех последующих фаз (deep external research →
synthesis → recursive swarm construction).

**Critical:** НЕ делать synthesis. НЕ выдавать мнения. Это inventory — что ЕСТЬ,
где лежит, какой purpose, какой relevance. Плюс **gap analysis** — что
отсутствует и требует new research.

## Context

Мы строим Jetix OS (AI-native operating system для solo-founder'а с trajectory к
$1T holding). Сейчас готовимся к **recursive swarm synthesis**: соберём все
лучшие наработки → настроим baseline рой (brigadier + 10 experts) → рой итерирует
и строит лучшую версию системы сам для себя.

**Фаза 1 (ЭТА задача):** inventory всего существующего, чтобы Фаза 2 (deep
research) не дублировала, а закрывала gap'ы.

Подробности full-plan: `Notion: Глубокий Research + Рой Агентов + Рекурсивный
Синтез Системы` (страница Day 22).

## Inputs (обязательно прочитать / проглядеть)

### Должен прочитать целиком (foundation)
1. `CLAUDE.md` (корень)
2. `.claude/rules/global.md`
3. `decisions/JETIX-VISION.md` (D1)
4. `decisions/JETIX-PHILOSOPHY.md` (D2)
5. `decisions/JETIX-PLAN.md` (D3)
6. `decisions/JETIX-ARCHITECTURE-BRIEF.md` (D4)
7. `design/JETIX-FPF.md` (D6 constitutional, 3758 lines) — можно skim §1-4 + ToC
8. `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md` (Locks 1-8)
9. `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md` (Locks 9-18)
10. `raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md` (Locks 19-24)
11. `raw/research/compounding-engineering-2026-04-22/SYNTHESIS-DEEP-CE-vs-JETIX.md` (executive summary v2)
12. `raw/articles/2026-04-22-every-compound-engineering-guide.md` **(НОВЫЙ — canonical CE source от Every / Kieran Klaassen, полный guide с 27 agents / 23 commands / 14 skills)**

### Должен проскан (inventory mode — catalog, не read)
13. Весь `raw/research/` (directory tree + заголовки + frontmatter каждого .md)
14. Весь `raw/research/compounding-engineering-2026-04-22/` (11 R-файлов + synthesis — прочитай executive summaries всех R-1..R-11)
15. Весь `raw/research/architecture-variants-2026-04-22/` (voice-memos digest, ATOM-REGISTRY, KNOT-MAP, etc.)
16. Весь `wiki/` (особенно wiki/sources/, wiki/foundations/, wiki/niches/)
17. Весь `design/`
18. Весь `decisions/` (включая variants/)
19. Весь `prompts/` (какие prompts уже написаны для чего)
20. Весь `.claude/agents/` и `agents/` (current agent definitions + per-agent folders)
21. `raw/voice-memos-text/` (text voice notes)
22. `raw/articles/` (external articles captured)

## Deliverables

Один файл: `raw/research/master-inventory-2026-04-22.md`

Структура (примерно 5000-8000 слов):

### Part 1 — Domain Coverage Matrix

Таблица: для каждого из 8 ключевых доменов отметить что есть.

Домены:
1. **Compounding Engineering** (Every / Kieran / Boris Cherny / Cora / Plan-Work-Review-Compound loop / $100 rule / 50/50 rule)
2. **Multi-Agent Orchestration** (hub-spoke / swarm / matchmaker / mailbox / hierarchical / production examples)
3. **Claude Code Best Practices** (agents / skills / MCP / CLAUDE.md / worktrees / slash commands)
4. **AI-Native Company OS** (Karpathy LLM OS / Balaji / real companies / architectures)
5. **Knowledge Management for AI** (wiki / typed graphs / vector / ontology / memory systems / FPF)
6. **Solo-Founder Scaling** (€50K → €1M+ / productization / partnerships / no-FTE models)
7. **Multi-Agent Failure Modes** (MAST taxonomy / Walden Yan / Kim et al. arXiv / regrets / anti-patterns)
8. **Recursive / Self-Improving Systems** (DSPy / TextGrad / constitutional AI / meta-learning / evals)

Формат таблицы (одна строка на домен):
```
| Domain | Coverage | Key files | Top references in-repo | Gaps |
| 1 CE   | STRONG   | 12 files  | R-1 CE core, R-7 Boris, Every-guide 2026-04-22 | Cora-specific patterns not yet extracted into Jetix form |
```

Coverage scale: **MINIMAL** (<3 sources) / **PARTIAL** (3-5) / **STRONG** (6+).

### Part 2 — File-Level Inventory

Для каждого significant файла (minimum 50 штук — самых важных) одна строка:
```
| Path | Type | Topic(s) | Size | Status | Purpose |
```

Группировать по категориям:
- Foundation docs (D1-D4, FPF, CLAUDE.md, rules)
- Locks (24 decisions)
- Research — Compounding Engineering (R-1..R-11 + synthesis)
- Research — Voice-memos digests
- Research — Architecture variants (5 files)
- Research — Other deep researches (agency / community / consulting / career-levels / company-as-code / crm-sales / etc.)
- Wiki sources (most relevant для domains 1-8)
- Wiki foundations
- Design docs
- Prompts already written
- External articles (raw/articles/)
- Agent definitions (.claude/agents + agents/)
- Skills (.claude/skills + plugins/)

Для каждого файла — **Status**: `canonical` / `active` / `draft` / `legacy-candidate` / `duplicate-suspected`.

### Part 3 — Duplicates + Legacy Candidates

Явный список:
- Файлы где есть **duplicate patterns** (например `agents/manager/system.md` vs `.claude/agents/manager.md`)
- Файлы явно **legacy** (pre-24-locks design)
- Версионированные документы где есть newer version (migrate needed)
- Файлы которые должны быть deleted/merged

Формат:
```
- [DUPLICATE] agents/<name>/system.md ≈ .claude/agents/<name>.md — 12 pairs, migrate to .claude/agents/ only
- [LEGACY] knowledge-base/ — superseded by wiki/, see MIGRATION.md
- [OBSOLETE] CRM/*-draft.md — superseded by decisions/2026-04-19-architecture-v2-approval.md
```

### Part 4 — Key Insights Already Captured

Список top-20 **already-established insights** which we know from existing research
(не расширять — только cite). Формат:

```
1. "Multi-agent systems в среднем -3.5% хуже single-agent" — Kim et al. arXiv:2512.08296, cite R-2 §3.1
2. "15× token cost multi-agent" — Anthropic, cite R-2 §1 + R-9
3. "Rule of 4 — team sizes peak 3-4" — Kim et al., cite R-2 §executive-summary
4. "Claude Code pattern = stigmergic" — R-2 §1 + CE-Synthesis §executive-summary
5. "50/50 rule: 50% codifying, 50% building" — Every-guide 2026-04-22 §Philosophy
...
```

Goal: distilled knowledge bank готовый к использованию в synthesis.

### Part 5 — Gap Analysis

Для каждого из 8 доменов (Part 1) — конкретный gap list:

```
Domain 1 — Compounding Engineering
MINOR GAPS:
- Kieran's Cora-specific patterns (we have concept, not detail)
- Every's internal agent communication patterns (not public)

MAJOR GAPS:
- None — we have canonical source + synthesis

Domain 2 — Multi-Agent Orchestration
MINOR GAPS:
- Latest 2026 production pattern updates from Anthropic/OpenAI/Sierra
MAJOR GAPS:
- Matchmaker / capability-capsule production examples with citation
- Concrete implementations of "trellis not cage" (V5 Emergent pattern)

...
```

### Part 6 — Recommended Deep-Research Priorities (input для Фазы 2)

Ranked list 6-10 pum prompt candidates для Perplexity / Claude.ai — что именно
докапывать в Фазе 2. Для каждого: ranking (P1/P2/P3), justification из gap
analysis, expected-output format.

Пример:
```
P1 — "AI-Native Company OS случаи 2025-2026"
Justification: Domain 4 MAJOR GAPS — no canonical production examples
Expected output: 5-10 named companies + architecture summaries + citations
Estimated Perplexity time: 15-30 min Deep Research mode

P1 — "Multi-Agent patterns beyond OpenAI Swarm / CrewAI"
Justification: Domain 2 MAJOR GAPS — matchmaker / capability-capsule production
...
```

## Success criteria

- **Complete coverage**: каждый `raw/research/`, `wiki/`, `decisions/`, `design/`,
  `prompts/` subdir проскан, ни один major file не пропущен
- **Part 1 matrix**: все 8 доменов с honest coverage rating
- **Part 2 inventory**: minimum 50 files в file-level inventory
- **Part 3**: минимум 5 concrete legacy/duplicate items
- **Part 4**: top-20 insights с reliable citations (paper/file/§)
- **Part 5**: MINOR + MAJOR gaps для каждого domain
- **Part 6**: 6-10 ranked research priorities
- **Citation discipline**: каждый claim / fact / статистика с inline citation
  `[source-path §section]`
- **Length**: 5000-8000 слов, table-heavy, dense
- **Honest**: если domain covered на 100% — скажи; если 0% — скажи

## Anti-patterns (НЕ делай)

- ❌ НЕ делай synthesis или recommendations за пределами Part 6 (это inventory, не analysis)
- ❌ НЕ описывай variants (V1-V5) как options — они = inputs, не candidates
- ❌ НЕ предлагай новые Locks / новые принципы
- ❌ НЕ пропускай `raw/research/` subdirs (их ~15 — все должны быть inventoried)
- ❌ НЕ переводи contents — cite verbatim в исходном языке (ru/en mix)

## Extended thinking

Используй **extended thinking max**. Особенно на:
- Domain 1-8 coverage rating (honest gap analysis)
- Duplicate detection (cross-file pattern recognition)
- Top-20 insights selection (best-evidenced)

## Workflow

1. Foundation reads (items 1-12). ~45-60 min.
2. Directory scans (items 13-22) — build inventory index. ~30-45 min.
3. Domain coverage matrix (Part 1). ~20-30 min.
4. File-level inventory (Part 2). ~45-60 min.
5. Duplicate/legacy detection (Part 3). ~15-20 min.
6. Top-20 insights extraction (Part 4). ~30-45 min.
7. Gap analysis (Part 5). ~30-45 min.
8. Deep-research priorities (Part 6). ~15-20 min.
9. Self-review: все 8 доменов cited? все gaps honest? length в диапазоне? ~10 min.
10. Commit + push.

## Commit template

```
git add raw/research/master-inventory-2026-04-22.md
git commit -m "[research] Phase 1 Master Inventory — 8 domains coverage + gaps + deep-research priorities"
git push origin claude/jolly-margulis-915d34
```

## After completion

Сообщи в commit что готово. Cloud Cowork увидит через git fetch и на основе Part 5
+ Part 6 напишет Фазу 2 deep research prompts (для Perplexity / Claude.ai).

**Не пиши Фазу 2 prompts** — это отдельная задача для Cloud Cowork.
**Не начинай synthesis** — это Фаза 3, после Фазы 2 research.

---

*END PROMPT*
