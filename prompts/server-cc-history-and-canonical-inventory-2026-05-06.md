---
title: Server CC Brigadier Prompt — GitHub Repo History + Canonical Docs Inventory
type: brigadier-prompt
created: 2026-05-06
author: cloud-cowork (Ruslan)
target_executor: server-cc on branch claude/jolly-margulis-915d34 (or successor)
deliverables: 2 separate research reports
output_location: reports/
push_policy: draft commit на server CC ветку (НЕ main), awaits Ruslan ack для merge
F: F4
G: research-deliverable-pre-platform-of-truth
R: refuted_if_premature_consolidation_or_strategic_recommendations_in_reports
constitutional_anchor:
  - Tier 2 Rule 1 (AI does not strategize) — это inventory + analysis, НЕ recommendation что делать с canonical structure
  - Tier 2 Rule 2 (no architectural changes without gate) — research-only, НЕ пишет в decisions/ / Foundation paths
  - Tier 2 Rule 6 (no aggregation без provenance) — каждое утверждение F-G-R cited к git/path
  - Append-only — НЕ удаляет / НЕ редактирует existing файлы
  - Default-Deny — НЕ создаёт canonical/ folder, НЕ делает symlinks, НЕ предлагает Platform of Truth structure (это next phase после Ruslan review этих 2 reports)
sla_tier: L2 (research deliverable; ≤ 24h)
estimated_effort: 4-7 hours brigadier autonomous
---

# Server CC Brigadier Prompt — GitHub Repo History + Canonical Docs Inventory

> **Контекст для server CC:** Ruslan хочет перед Platform of Truth task (consolidating canonical docs в одно место) получить **два independent inventory отчёта**, чтобы увидеть полную картину что было сделано в этом репозитории за весь срок и какие документы сегодня служат source-of-truth.
>
> **Это research deliverable, НЕ strategic decision.** Ты собираешь facts + organize + present. Ты НЕ предлагаешь как consolidate, какие docs «правильные», что архивировать. Это решение Ruslan'a в following phase.

---

## §0 TL;DR (что делать)

Создать **2 отдельных research-отчёта** в `reports/`:

1. **Отчёт 1** — `reports/github-repo-history-2026-05-06.md` — полная история работы с GitHub repo с первого commit'а до 2026-05-06: phases / документы созданные / timeline / LOCKED tags / по темам / statistics.

2. **Отчёт 2** — `reports/canonical-docs-inventory-2026-05-06.md` — inventory всех «основных» документов **на сегодня**: что LOCKED canonical / что superseded / что draft / что используется vs not / cross-refs / topical groupings.

Phase A-C autonomous. Phase D ship = `[draft] reports awaiting Ruslan review` push на твою ветку (НЕ main). Ruslan читает → ack → потом merge to main отдельным actом.

---

## §1 Inputs (где смотреть)

### §1.1 Git history

- **Полный git log** с первого commit'а: `git log --reverse --all --pretty=format:'%H|%ai|%an|%s' > /tmp/full-log.txt`
- **All git tags:** `git tag -l` + `git for-each-ref refs/tags/ --format='%(refname:short)|%(creatordate:iso-strict)|%(subject)'`
- **Commit count by author / by month:** агрегация
- **First commit date** (repo origin)
- **Branch list:** `git branch -a` (все feature branches, claude/* worktree branches)

### §1.2 File system traversal

Top-level folders (известные):
- `decisions/` — concept docs / LOCKED canonical / AWAITING-APPROVAL packets / planning briefs
- `swarm/wiki/foundations/` — 11 Foundation Parts + Pillar C architecture
- `swarm/wiki/synthesis/` — master overviews / brigadier syntheses
- `swarm/wiki/cycles/` — Wave-by-Wave Foundation build артефакты
- `swarm/wiki/operations/` — operational templates (quick-log etc.)
- `wiki/` — main KB (concepts / entities / sources / topics / ideas / experiments / claims / summaries / foundations / niches / comparisons / graph / _templates / niches/)
- `reports/` — research deliverables / retrospectives / status reports
- `prompts/` — brigadier prompts / handoff chats
- `agents/` — per-agent system prompts / strategies / scratchpads / niches
- `comms/mailboxes/` — JSONL inter-agent comms
- `shared/state/`, `shared/knowledge/`, `shared/schemas/`
- `tools/` — pipeline scripts (transcribe, extract, filter, review_report, run_pipeline)
- `raw/`, `daily/`, `_meta/`, `private/`

Для каждой folder'ы:
- Total file count
- Total line count (`.md` files; bash: `find folder -name "*.md" | xargs wc -l | tail -1`)
- Top files by size
- Frontmatter status distribution (status: ready / draft / LOCKED / superseded / etc.)
- Date range (oldest mtime → newest)

### §1.3 LOCKED canonical anchors (известные)

Эти 5 точно canonical, проверь их и find остальные:

- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` — constitutional anchor
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` — Workshop concept LOCKED
- `decisions/JETIX-TRM-MODEL-2026-04-30.md` — TRM model LOCKED
- `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` — Документ 1A LOCKED v1.0
- `decisions/JETIX-CORPORATION-2026-05-05.md` — Документ 1B LOCKED v1.0
- (новый, just locked) `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` — Workshop human overview LOCKED v1.0
- `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` — Technical overview (pas tag, но canonical)
- `swarm/wiki/foundations/` — 11 Parts + Pillar C (LOCKED via tag `foundation-architecture-locked-2026-04-28`)
- `reports/retrospective_2025-05_to_2026-04.md` — 12-month retrospective

Find остальные через grep:
- `grep -r "status: LOCKED" decisions/ swarm/wiki/ reports/`
- `grep -r "git_tag:" decisions/ swarm/wiki/ reports/`
- `grep -r "supersedes:" decisions/ swarm/wiki/ reports/`
- `grep -r "superseded_by:" decisions/ swarm/wiki/ reports/`

### §1.4 Git tags inventory

Все `*locked*` tags (3 known: `foundation-architecture-locked-2026-04-28`, `base-management-system-locked-2026-05-05`, `jetix-corporation-locked-2026-05-06`). Plus сегодня добавится `foundation-overview-human-workshop-locked-2026-05-06`. Find все остальные tags.

### §1.5 Reference docs (фоновое понимание)

- `CLAUDE.md` — master config + Foundation Architecture v1.0 LOCKED section
- `MIGRATION.md` — knowledge-base/ → wiki/ migration status
- `_meta/conventions.md`, `_meta/pipeline-spec.md` — conventions + pipeline spec
- `reports/foundation-consolidation-status-2026-05-06.md` — recent consolidation analysis (там УЖЕ хорошая выборка post-Foundation work)

---

## §2 Process (Phase A-D)

### Phase A — Data collection (1.5-2 hours)

A.1 **Git inventory**
   - Full log dump
   - All tags + dates
   - Commit count per month / per area (commit prefix `[foundation]` / `[jetix-corp]` / `[swarm]` / `[handoff]` / etc.)
   - Branches list

A.2 **Filesystem inventory**
   - Per-folder file count + total lines
   - Frontmatter scan: `status:` field distribution в `decisions/` + `swarm/wiki/synthesis/` + `swarm/wiki/foundations/` + `reports/` + `wiki/`
   - All files containing `LOCKED` в frontmatter / supersedes / superseded_by

A.3 **Topical clustering** (по содержимому frontmatter `tags:` / `topics:` / `type:` / heuristic по filename / по folder):
   - Foundation architecture (11 Parts + Pillar C + Wave deliverables)
   - System concept (Workshop / TRM / 1A / 1B / Vision)
   - Operational pipelines (time-tracking / voice / transcribe / pipeline scripts)
   - Sales / business (sales-lead / outreach / ICP / partnership)
   - Knowledge management (wiki structure / ingest / KB)
   - Daily / retrospective / status (daily logs / retros / consolidation reports)
   - Agents (12 agents system / per-agent docs)
   - Brigadier prompts / handoff chats
   - Strategic Layer (Pillar A / B / Wave 1 scaffolding)

### Phase B — Report 1 draft (1.5-2 hours)

`reports/github-repo-history-2026-05-06.md` — рекомендуемая структура:

```
§0  TL;DR — totals (period / commits / files / lines / tags / authors)
§1  Repo origin + earliest phase (когда первый commit, что было в начале)
§2  Major phases — chronological breakdown больших work blocks
    (e.g., "Phase early Apr 2026: voice pipeline build", "mid-Apr: Foundation
    research + Wave A planning", "late Apr: Foundation Wave B-E build", "post-LOCK:
    consolidation + Workshop concept + 1A/1B + retrospective", etc.)
§3  Document creation timeline — chronological log ключевых docs (decisions/ /
    synthesis/ / Foundation Parts / retrospectives) с датой commit + size
§4  LOCKED tags — все tags с датой + что они помечают + commit hash
§5  Statistics:
     - Total commits / authors / period
     - Top-N folders by activity (commits / lines)
     - Top-N file types (.md / .json / .jsonl / .py / .sh / etc.)
     - Lines added per month chart (textual)
     - Commit prefix distribution ([area] tags)
§6  Topical breakdown — в каждой topic group: file count / total lines /
    earliest creation / latest creation / LOCKED count / draft count
§7  What was deleted / archived / superseded — append-only history check
§8  Surprises / observations (factual only, no recommendations)
§9  Provenance — git commands used / paths consulted
```

**Размер цель: 600-1200 строк.** Plain language + tables. Не пиши по словам "впечатляет / удивительно / красиво". Только facts.

### Phase C — Report 2 draft (1.5-2 hours)

`reports/canonical-docs-inventory-2026-05-06.md` — рекомендуемая структура:

```
§0  TL;DR — X canonical LOCKED docs / Y active drafts / Z superseded / W planning briefs
§1  LOCKED canonical (production source-of-truth) — table format:
    | path | size | created | locked | git_tag | audience | scope | status |
§2  Active drafts / WIP — что сейчас в process, awaiting ack или iteration
§3  Superseded — что было canonical, теперь superseded_by кем
§4  Planning briefs / AWAITING-APPROVAL packets — что pending ack
§5  Topical groupings:
     §5.1 Foundation level (11 Parts + Pillar C + overviews + Wave deliverables)
     §5.2 System concept level (Workshop / TRM / 1A / 1B / Vision)
     §5.3 Operational level (retrospectives / time-tracking / voice / quick-log)
     §5.4 Decisions / brief / planning (master plans / pre-Foundation briefs)
     §5.5 Other (per-agent / wiki KB / etc.)
§6  Cross-reference graph — какой документ ссылается на какие (frontmatter
    `sources:` + `related:` + `supersedes:` parsing)
§7  "What is currently used vs not used" — heuristic:
     - Active = referenced from CLAUDE.md / Foundation overview / 1A / 1B / recent commits
     - Stale = no references за 30+ дней + status != LOCKED
     - Note: это HEURISTIC, окончательное решение Ruslan'a
§8  Gaps + duplicates — где documentation отсутствует / где параллельные docs
    на одну тему (factual observation, no resolution proposed)
§9  Provenance — frontmatter scans / grep queries used
```

**Размер цель: 800-1500 строк.** Tables + concise descriptions. Один абзац на documentик в §1 — что покрывает / для какой аудитории / когда написан / когда LOCKED.

### Phase D — Push (drafts only)

Когда оба отчёта готовы:

```bash
git add reports/github-repo-history-2026-05-06.md reports/canonical-docs-inventory-2026-05-06.md
git commit -m "[reports] github history + canonical docs inventory — drafts awaiting Ruslan review

Two independent research deliverables ahead of Platform of Truth task:
- github-repo-history: full repo history с первого commit'а до 2026-05-06
  (phases, doc creation timeline, LOCKED tags, statistics, topical breakdown)
- canonical-docs-inventory: список всех canonical / draft / superseded docs
  с topical groupings + cross-ref graph + active vs stale heuristic

Phases A-C complete autonomously. Phase D ship to main waits for Ruslan ack
per Tier 2 Rule 11 (no actions without blast-radius classification +
Default-Deny — though F2-F4 research deliverable, soft policy is review-first)."

git push origin HEAD
```

**НЕ push to main.** **НЕ tag.** **НЕ index/log update пока.** Только draft на твою ветку.

---

## §3 Output spec — что должно быть в каждом отчёте

### §3.1 Отчёт 1 — обязательные элементы

- ✅ Repo origin date + first commit summary
- ✅ Total commits / authors / branches counted
- ✅ All git tags listed (LOCKED + non-LOCKED)
- ✅ Document creation timeline (chronological list of major artifacts) — minimum 30 entries
- ✅ Topical breakdown — minimum 7 topic groups, каждой с counts + dates
- ✅ Statistics tables (per-month / per-folder / per-prefix)
- ✅ Provenance section (git commands + paths used)

### §3.2 Отчёт 2 — обязательные элементы

- ✅ Все LOCKED canonical docs listed (≥ 8 expected, may be more)
- ✅ Все superseded docs listed (с pointer на superseded_by)
- ✅ AWAITING-APPROVAL packets listed (pending ack)
- ✅ Topical groupings (≥ 5 groups)
- ✅ Cross-reference graph (textual: doc → references list)
- ✅ Active vs stale heuristic с explicit caveats ("это HEURISTIC, не решение")
- ✅ Gaps + duplicates as factual observations only

### §3.3 Discipline (хард-нет)

- ❌ **НЕ предлагай Platform of Truth structure** (canonical/ folder, symlinks, INDEX file). Это решение Ruslan'a в following phase.
- ❌ **НЕ предлагай удалять / архивировать / consolidate docs.** Только inventory.
- ❌ **НЕ пиши в `decisions/` или Foundation-level paths.** Reports = research-only, в `reports/`.
- ❌ **НЕ делай LOCK / git tag / push to main.** Draft commit на твою ветку, ack first.
- ❌ **НЕ оценивай качество docs** ("этот хороший / этот плохой"). Просто facts.
- ✅ **МОЖНО** делать factual observations ("Doc X и Doc Y покрывают одну тему" — без вердикта что делать).
- ✅ **МОЖНО** flagить gaps ("topic Z не covered LOCKED canonical doc'ом" — без вердикта что писать).

### §3.4 Provenance requirement

Каждый non-trivial claim должен быть verifiable:
- Git data → `git log <args>` queried
- File data → `<path>` exists at <commit>
- Frontmatter data → `<path>` field <name> = <value>

В §9 каждого отчёта — список git commands + paths использованных.

---

## §4 Constitutional check

| Rule | Application | Compliance |
|------|-------------|------------|
| Tier 2 Rule 1 | Reports = inventory + factual analysis. Strategic decisions (consolidate / archive / structure canonical/) — Ruslan's в next phase. | ✅ |
| Tier 2 Rule 2 | Reports go to `reports/` (non-Foundation path). НЕ Foundation-level write. F2-F4 research only. | ✅ |
| Tier 2 Rule 6 | Provenance section в каждом отчёте + inline `[src: ...]` для non-trivial claims. | ✅ |
| Tier 2 Rule 11 | Blast radius F2-F4 (research deliverable). Default-Deny → drafts pushed to your branch only, await Ruslan ack для merge to main. | ✅ |
| Append-only | НЕ удаляешь / НЕ editing existing. Только creates 2 new files в `reports/`. | ✅ |

---

## §5 Time / size budget

- Phase A data collection: 1.5-2 hours
- Phase B Отчёт 1 draft: 1.5-2 hours
- Phase C Отчёт 2 draft: 1.5-2 hours
- Phase D push (no LOCK): 5 min
- **Total estimated: 4-7 hours brigadier autonomous**

Sizes:
- Отчёт 1: 600-1200 lines (cap at 1500 if narrative pull)
- Отчёт 2: 800-1500 lines (cap at 2000)

Если значительно превышает — pause + signal Ruslan, не self-extend.

---

## §6 What you DON'T do

- Не consolidate ничего
- Не делаешь Platform of Truth structure / symlinks / canonical/ folder
- Не удаляешь / не архивируешь existing docs
- Не оцениваешь качество docs
- Не пишешь в `decisions/` или Foundation paths
- Не делаешь LOCK / tag / push to main
- Не trying make recommendations о strategy
- Не делаешь cross-refs из CLAUDE.md (separate task)

---

## §7 Final deliverables checklist

При Phase D push, эти 3 артефакта должны существовать на твоей ветке:

```
A  reports/github-repo-history-2026-05-06.md          (NEW, 600-1200 lines)
A  reports/canonical-docs-inventory-2026-05-06.md     (NEW, 800-1500 lines)
M  (none — append-only, no modifications to existing)
```

Commit message format:
```
[reports] github history + canonical docs inventory — drafts awaiting Ruslan review
```

После push — signal Ruslan через cloud cowork bridge что drafts ready на твоей ветке для review.

---

## §8 Open items / clarifications

Если по ходу работы обнаружишь:

- **Ambiguity** что считать "main" doc — записываешь в §8 obs Отчёта 2 как factual observation, не решаешь сам
- **Missing data** (e.g., file без frontmatter) — flag в §8 как gap
- **Surprises** (e.g., orphan docs, broken cross-refs) — record в §8

Не спрашивай Ruslan по ходу — записывай в §8 / §6 каждого отчёта, он прочитает в ack phase.

---

**Конец prompt'а.** Brigadier acting_as research-inventory-analyst orchestration role.
Ruslan = sole strategist по following phase (Platform of Truth structure decision).
