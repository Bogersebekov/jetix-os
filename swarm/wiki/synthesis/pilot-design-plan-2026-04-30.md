# PILOT-DESIGN PLAN: Claude Code как book-grounded экспертная команда

> **Status:** Plan Mode draft, AWAITING-RUSLAN-ACK.
> **Trigger doc:** `/tmp/meta-prompt.md` (read 2026-04-30)
> **Mode:** Opus 4.7 [1m] + Plan Mode + ultrathink
> **Hard-rule provenance gate:** ≥0.95 (flag rather than confabulate)

---

## Context — зачем этот план

Ruslan хочет проверить **methodology hypothesis**: «если Claude Code в Plan Mode + ultrathink работает не на vacuum-generic best-practices, а на **отобранных 5-15 релевантных книгах** из 402-volume библиотеки + Foundation v1.0 + wiki — получим ли мы планы качественно лучше generic baseline».

**Что прямо просит meta-prompt** (`/tmp/meta-prompt.md:L26-28, L72`):

> «Составь PILOT-DESIGN PLAN — план как нам этот подход проверить и внедрить. **Не решай реальный кейс.** Спроектируй methodology + roadmap pilot'а.»

Главный risk который этот pilot закрывает: инвестировать в methodology infrastructure (selection algorithm, citation gates, document maps) до того как мы знаем, что инвестиция возвращается. Решаемая через **measurable A/B (books-grounded vs generic baseline)** с явным fail-criteria для каждой гипотезы.

**Что уже есть** (verified в Phase 1 exploration):
- `raw/books-md/` 402 книги, унифицированный YAML frontmatter (`expert:`, `priority: P1|P2`, `quality_grade: A|B|C`, `tags:`, `subcategory:`, `word_count:`) — `raw/books-md/INDEX.md:L1-80` подтверждает
- 11 LOCKED Foundation Parts + Pillar A/B/C — `swarm/wiki/foundations/part-{1..11}/architecture.md` + `swarm/wiki/foundations/principles/architecture.md`
- Methodology articles: `raw/articles/2026-04-29-claude-code-best-practices/{ultrathink,plan-mode,README}.md` (293+448+122 lines)
- Synthesis: `swarm/wiki/synthesis/foundation-master-overview-{technical,human}-2026-04-29.md` (1590+676 lines, LOCKED tag `foundation-architecture-locked-2026-04-28`)
- 35 UC × 12 categories — `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:L432-448`

**Что ОТСУТСТВУЕТ** (provenance flags, не confabulate):
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` — **NOT FOUND** (`find` подтвердил отсутствие)
- `decisions/JETIX-TRM-MODEL-2026-04-30.md` — **NOT FOUND** (`find` подтвердил)
- → blocks полное определение «TRM L0 sales test design» test case до Ruslan ack или document creation

---

## Executive Summary (≤150 слов)

Pilot тестирует **гибридную selection methodology**: для каждого кейса hand-curated case-category mapping (10 категорий) фильтрует book-clusters из `INDEX.md`, далее frontmatter-based ranking (priority×quality×expert-match) даёт top-5-15 candidates под 1M-context budget. Provenance enforced через **inline-citation gate** (file:Lstart-Lend) и **citation-coverage scanner** (≥0.95 утверждений с источниками). 8 test cases (3 classical consulting + 5 Jetix-specific) прогоняются **парами** (books-grounded vs generic baseline) для measurable diff на 5 quantitative + 4 qualitative метриках. 20 falsifiable гипотез с конкретными fail-criteria. 4-week roadmap: w1 calibration на 2 кейсах → w2-3 full caseload → w4 verdict (scale/pivot/drop). Верховный gate перед scale — **≥3 из 5 main hypotheses validated, baseline diff ≥1.0 на actionability rubric**. Skip Phase 2 если diff <0.5.

---

## §1 Spec методологии

### §1.1 Prompt skeleton (template для каждого test case)

Базовый template (English code-fence для consistency, Russian prose внутри):

```
[Mode: Opus 4.7 [1m] + Plan Mode (Shift+Tab×2)]

Я — Ruslan. Кейс ниже.

## Кейс
<case_brief — 100-300 слов: ситуация, данные, ограничения, deliverable>

## Категория
<one of 10 enum: market-sizing | profitability | market-entry | M&A |
 niche-selection | system-design | risk-analysis | sales-strategy |
 capability-acquisition | retrospective>

## Selection seed (manual override, optional)
- pin_books: [<author-slug>, ...]   # force-include
- exclude_books: [<author-slug>, ...] # force-exclude
- max_books: 12                       # default 8
- max_tokens_books: 800000            # default 600K of 1M

## Required perspectives
≥3 из {ШСМ-Левенчука | Compounding Engineering | SRE | PM Cagan |
       Stoic | Cybernetics-VSM | Systems-Meadows | Lean-Startup |
       Constitutional-Foundation}

## Provenance gate
- Каждое утверждение: inline (file_path:Lstart-Lend) или (book.md:§N) ref
- Gate threshold: ≥0.95 утверждений с источником
- Если источник не найден — flag «не нашёл в источниках», не выдумывай

## Deliverable
Структурированный markdown plan ≤2500 слов:
- Executive summary
- 3-5 perspective-syntheses (каждая 200-400 слов)
- Recommendation matrix (option × criteria × source)
- Risk register
- Open questions
- Provenance index в конце (table: claim → source → line-range)

ultrathink. Plan Mode. Не пиши код. Не делай edits.
```

**Provenance:** template дизайнят под Hard rule §1-§4 из `/tmp/meta-prompt.md:L74-78` + canonical workflow `raw/articles/2026-04-29-claude-code-best-practices/plan-mode-claude-code.md:L94-126`.

### §1.2 Pre-load context manifest (что обязательно загружается)

**Tier 0 — ВСЕГДА** (~80K токенов):
- `CLAUDE.md` (auto-loaded by harness)
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:L432-448` (35 UC + 12 categories) — селективно через `Read(offset=430, limit=20)`
- `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md` (676 lines, ~30K tokens)
- `raw/articles/2026-04-29-claude-code-best-practices/{ultrathink,plan-mode}.md` для self-conditioning

**Tier 1 — ПО ОТНОШЕНИЮ К case category** (см. §2.3 mapping):
- 1-3 Foundation Parts которые пересекаются с категорией
- Pillar A или Pillar C если кейс strategic/principle-related

**Tier 2 — selected books** (~400-700K токенов, см. §1.3):
- 5-15 книг через selection algorithm
- Если нужно >5 книг — **batch через Explore sub-agents** (см. §1.7)

**Tier 3 — wiki niche / drafts**:
- `swarm/wiki/concepts/`, `swarm/wiki/topics/` если уже есть relevant entries (lazy lookup через `/ask` skill)

**Provenance:** Tier-структура — оригинальный design этого плана (не цитата). Token estimates basedirovannye на explore agent report (avg book ~80K tokens, technical-overview ~70K tokens).

### §1.3 Selection algorithm (как выбираем 5-15 книг из 402)

**Решение:** **гибрид frontmatter-ranking + manual cluster mapping**, embedding-search отложен на Phase 2 enhancement (rationale: не у нас в инфраструктуре, добавление = scope creep).

**Pipeline (deterministic, no inference):**

```
INPUT: case_category (1 of 10), pin_books?, exclude_books?, max_books, max_tokens

STEP 1 — Cluster filter
  candidate_clusters = case_category_to_cluster_map[case_category]
  # YAML mapping в .claude/config/case-cluster-map.yaml
  # см. §2.3 для полной таблицы

STEP 2 — Frontmatter prefilter
  candidates = books WHERE
    subcategory IN candidate_clusters
    AND quality_grade IN {A, B}      # exclude C
    AND priority == P1                # P2 only via pin_books

STEP 3 — Ranking score
  score = (priority_weight × quality_weight × expert_match × recency_factor)
    priority_weight: P1=1.0
    quality_weight:  A=1.0, B=0.7
    expert_match:    +0.3 if frontmatter.expert matches case domain
    recency_factor:  +0.1 if year >= 2010 (не для всех кейсов!)

STEP 4 — Token budget greedy
  selected = []; budget = max_tokens
  for book in sorted(candidates, by score desc):
    if word_count*1.4 < budget:   # 1.4 = words→tokens estimate
      selected.append(book); budget -= word_count*1.4
    if len(selected) >= max_books: break

STEP 5 — Manual override
  selected = (selected ∪ pin_books) \ exclude_books

STEP 6 — Diversity floor
  assert ≥3 distinct subcategories represented
  if not: warn + suggest Phase 2 rerun с expanded clusters
```

**Anti-failure mitigations:**
- **Cherry-picking risk** (§7.4): diversity floor (Step 6) предотвращает «9 книг из одного cluster»
- **Bias to favorites**: stage-1 cluster filter — hand-curated (transparent), не embedding (opaque)
- **Stale ranking**: recency_factor отключаем для timeless domains (philosophy/science → year не matter)

**Что НЕ автоматизируем** (deliberate):
- Семантический матчинг текста кейса с книгой — это требует embeddings, scope creep
- Re-ranking по содержимому — Phase 2 if pilot succeeds

**Provenance:** Pipeline — оригинальный design. Frontmatter поля верифицированы из `raw/books-md/INDEX.md:L1-80` + sample frontmatter в Explore Agent 1 output (`acquired_date, author, expert, priority, quality_grade, slug, subcategory, tags, word_count, year`).

### §1.4 Provenance enforcement (citations gate, no confabulation)

**Three-layer gate:**

**Layer A — In-prompt instruction** (cheap, in-context):
- Hard rule в template (§1.1): «Каждое утверждение: inline (file_path:Lstart-Lend) или flag»
- Mirrors Foundation §I.1 F-G-R discipline (`swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I` — Formality/ClaimScope/Reliability)
- Aligns Hard rule §3 + §9 from `/tmp/meta-prompt.md:L78,L84`

**Layer B — Inline citation scanner** (post-generation, deterministic):

```bash
# pseudocode for citation-coverage check
python3 tools/citation-coverage.py <plan.md> --threshold 0.95 --whitelist raw/books-md/
```

Алгоритм:
1. Split plan into «atomic claims» (sentences ending `.` or bullet items, modulo headers)
2. Для каждой claim — search nearest inline citation `(<path>:L<n>-L<m>)` или `[src:...]`
3. Coverage = claims_with_cite / total_claims
4. Fail if <0.95
5. Все cited paths должны существовать (filesystem check) + line-range valid (≤file_length)

**Note:** Layer B — Phase 1 manual run; в Phase B Foundation roadmap уже запланирован «citation scanner materialization» (`swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md:L628-657`), pilot переиспользует если materialised к w2.

**Layer C — Halt-Log-Alert на violation** (constitutional, F8):
- Если Layer B fails → план не promotion'ится в `decisions/` или `swarm/wiki/`
- Halt ≤1s / Log to `swarm/approvals/log.jsonl` ≤5s / Alert через Part 8 SLI ≤60s
- Mirrors `swarm/wiki/foundations/part-6b-human-gate/architecture.md` Halt-Log-Alert primitive

**Provenance:** Three-layer design synthesizes existing infrastructure: F-G-R (Part 6a §I), citation-lint scanner Phase B priority (synthesis-human L628), Halt-Log-Alert (Part 6b §I.2). Design нов, components — existing.

### §1.5 Token budget management (1M ≠ безграничен)

**Realistic budgets** (Opus 4.7 [1m]):

| Зона | Tokens | Что туда идёт |
|---|---:|---|
| System prompt + harness | 30K | Default Claude Code |
| CLAUDE.md + memory | 30K | Auto-loaded |
| Tier 0 pre-load | 80K | Vision UC, Foundation human-overview, methodology articles |
| Tier 1 Foundation Parts | 70K | 1-3 Parts × ~25K each |
| Tier 2 books | **600K** | **Selected 5-12 books** |
| Tier 3 wiki niches | 30K | Selective `/ask` lookups |
| Working buffer (output + iterations) | **160K** | Plan generation + 2-3 revisions |
| **Total** | **~1000K** | (~3% margin) |

**Strategies при overflow:**

1. **Sub-agent batch reading** (default, see §1.7): не загружать книги в main context, а через `Explore` agent → сжатый summary возвращается в main session (~5-10K tokens вместо 80K each)

2. **Section-targeted reads**: использовать `Read(offset, limit)` для конкретных глав — фронт-page книги обычно содержат TOC + intro, дают 80% сигнала за 10% токенов

3. **Tier-3 deferral**: lazy `/ask` lookups только когда план требует specific concept

4. **Batching strategy** (если книг >12 нужно): split case на под-кейсы по perspective (e.g. «engineering view» / «strategic view» / «epistemic view»), каждый отдельной session, синтез на 3-м проходе

**Hard cap:** Не загружать в main context >700K из books. Если selection algorithm даёт >700K — auto-fallback на sub-agent batch.

**Provenance:** Token estimates basedirovannye на Explore Agent 1 metric report (avg ~80K/book, total library 11.7M); Foundation Part avg 1100 lines × ~10 tokens/line via own arithmetic (no inferred source).

### §1.6 Когда Opus 4.7 [1m] vs Sonnet 4.6

| Phase | Model | Rationale | Source |
|---|---|---|---|
| **Plan Mode + ultrathink** | **Opus 4.7 [1m]** | 1M context для books-load + adaptive max-effort reasoning | `raw/articles/.../plan-mode-claude-code.md:L157-167` (Opus Plan Mode pattern) |
| **Sub-agent batch read** | **Sonnet 4.6** | Cheaper, fast, structured-extract задача не требует deep reasoning | `raw/articles/.../ultrathink-claude-code.md:L79-85` (when NOT to use ultrathink) |
| **Citation scanner run** | **Sonnet 4.6** или **Haiku 4.5** | Deterministic, no creative — Haiku если pure regex | own design |
| **Baseline (no books) run** | **Opus 4.7 [1m]** | Same model для apples-to-apples diff | own design |
| **Post-mortem retrospective** | **Opus 4.7 [1m]** | Multi-perspective synthesis качества | own design |

**Configuration command** (Plan-mode article L161):
```
/model → "Use Opus in plan mode, Sonnet 4.6 otherwise"
```

**Provenance:** Plan article L157-167 confirms Opus-plan / Sonnet-code split.

### §1.7 Sub-agent strategy (batch reading через Explore / general-purpose)

**Когда spawn sub-agent:**
- Selection algorithm дал 6+ книг
- Total Tier-2 budget ≥600K при main-context load
- Кейс требует deep-read multiple chapters (не TOC scan)

**Pattern:**

```
Main session (Opus 4.7 [1m]):
  1. Run selection algorithm → 8 books picked
  2. Spawn 3 parallel Explore agents (one per book cluster):
     - Agent A: 3 books from systems-thinking cluster
     - Agent B: 3 books from mgmt cluster
     - Agent C: 2 books from PDM cluster
  3. Each agent prompt:
     "Read book X. Extract: (a) thesis в 50 словах, (b) 5 ключевых
      claims с line-ranges, (c) методологические принципы применимые
      к <case-domain>. ≤500 words output. Provenance critical."
  4. Main session collects 3 reports (~5-10K tokens each = 30K total)
     vs raw load 8 books × 80K = 640K
  5. Main session synthesizes plan от 3 perspectives
```

**Каскадные ограничения:**
- Max 3 parallel sub-agents (current config from `/tmp/meta-prompt.md` workflow Phase 1 §2)
- Each agent self-contained (no main-context bleed)
- Sub-agent output structured (markdown bullets) для machine-parseable downstream

**Anti-pattern:**
- ❌ Sub-agent для single-book read — overhead > benefit (use direct `Read`)
- ❌ Sub-agent generates plan — plan-authoring stays в main session (provenance + ultrathink scope)

**Provenance:** Sub-agent pattern — adapted from harness Plan Mode workflow Phase 1 (system context); cascade limit (3 parallel) — system constraint.

---

## §2 Document map

### §2.1 Existing assets inventory (что уже есть, не дублировать)

| Asset | Path | Lines | Coverage |
|---|---|---:|---|
| **Vision** | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | 2624 | 35 UC × 12 categories + 11 constitutional rules |
| **FPF Spec** | `design/JETIX-FPF.md` | 3758 | First Principles Framework v2.0 |
| **Master Plan Brief** | `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` | ? | Foundation build context |
| **Audit** | `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` | ? | Pre-build state |
| **Foundation Parts** | `swarm/wiki/foundations/part-{1..11}*/architecture.md` | 11×~1200 avg | 11 LOCKED architectures |
| **Pillars** | `foundations/principles/architecture.md` + `part-7-.../bundle-5-supplement-pillar-b.md` + `part-11-.../architecture.md` | 1075+607+1101 | A/B/C |
| **Wave D Integration** | `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md` | 684 | Coverage 50/50, Inter-Part 98.1%, M-D-1..M-D-6 metrics |
| **Synthesis** | `swarm/wiki/synthesis/foundation-master-overview-{technical,human}-2026-04-29.md` | 1590+676 | LOCKED master overview |
| **Methodology articles** | `raw/articles/2026-04-29-claude-code-best-practices/` | 3 files | ultrathink + plan-mode + README |
| **Books library** | `raw/books-md/` (402 books) + `INDEX.md` (manifest) | 402 books, 11.7M tokens | Full corpus |
| **Schemas** | `shared/schemas/*.json` | 9 schemas | f-g-r, awaiting-approval, message v2.0.0, task-return-packet, etc. |
| **8 Ack records** | `decisions/RUSLAN-ACK-WAVE-*` | 8 files | Bundle 1-5 + Wave D + Phase 1 baseline |
| **Memory** | `~/.claude/projects/-home-ruslan-jetix-os/memory/` | 2 files | feedback_no_api_keys (Max subscription) |

**Не дублировать:** Vision/Foundation/Methodology — **link, not copy**, в test case briefs.

**Provenance:** All paths verified в Phase 1 exploration (Explore Agent 2 + 3); line counts через `wc -l` или explicit reads.

### §2.2 Books library navigation — INDEX.md как единый source-of-truth

**Корневой manifest:** `raw/books-md/INDEX.md` (`raw/books-md/INDEX.md:L1-7`):
- Generated 2026-04-27
- Total books: 402
- Quality grades: A=clean / B=minor artifacts / C=needs reprocess
- 21 secciones (`§anthropic`, `§biology`, `§books-md` (служебные), `§clean-code`, `§complexity`, `§cybernetics`, `§engineering-foundations`, `§event-sourcing`, `§investing`, `§meta`, `§mgmt`, `§pdm`, `§philosophy`, `§philosophy-science`, `§pm`, `§reocr` (assets), `§sre`, `§systems`, `§unix`)

**Cluster size distribution** (verified Explore Agent 1):

| Cluster | Books | Notes |
|---|---:|---|
| `meta/` | 140 | **Chunked chapter extracts** — особый формат: numbered `011-`/`012-`/...; не для cluster-as-domain; treat as auxiliary |
| `mgmt/` | 96 | Drucker, Collins, Grove, Christensen, et al. |
| `philosophy/` | 66 | Critical thinking, ethics, decision-making |
| `systems/` | 50 | Meadows, Senge, Sterman, Forrester |
| `investing/` | 6 | Buffett (813K words!), Markowitz |
| `pdm/` | 5 | Cagan Inspired, Gothelf Lean UX |
| `clean-code/` | 5 | Brooks, Martin, Fowler, Hunt-Thomas, Ousterhout |
| `cybernetics/` | 4 | Beer, Ashby, Wiener, Kelly |
| `engineering-foundations/` | 4 | Vincenti, Altshuller TRIZ, Koen, Descartes |
| `philosophy-science/` | 4 | Popper, Kuhn (предположительно — verify) |
| `biology/` | 4 | Dawkins×2, Dennett, Kauffman |
| `complexity/` | 2 | Beinhocker, Mitchell |
| `anthropic/` | 2 | Askell HHH, Bai CAI |
| `event-sourcing/` | 1 | Young CQRS |

**Treatment of `meta/` (140 chunks):**
- Не self-contained books, а chapter extracts (e.g. `011-what-is-getting-real.md`)
- НЕ pre-loadить в Tier 2 cluster; treated as **lookup-only** через explicit pin_books
- Book-equivalent count: ~10-15 source books (нужен manual «origin manifest» — Phase 1.5 task если pilot succeeds)

**Provenance:** Cluster sizes verified Explore Agent 1; INDEX.md secciones verified own Read of L1-80; meta/ chunked nature verified Explore Agent 1 («numbered 011-099, 211-299»).

### §2.3 Case category → cluster mapping (hand-curated, transparent, editable)

YAML config спецификация для `.claude/config/case-cluster-map.yaml` (создаётся в Phase 1, ack required):

```yaml
# Mapping case categories → candidate book clusters.
# Used by selection algorithm (§1.3 Step 1).
# Hand-curated; transparent; reviewable.
# Phase 1 baseline; refine after pilot results.

categories:

  market-sizing:
    primary_clusters: [mgmt, investing]
    secondary_clusters: [pdm]
    expected_book_count: 6-10
    canonical_picks:
      - mgmt/grove-only-paranoid-survive-1996.md  # market dynamics
      - mgmt/christensen-innovators-dilemma  # disruption
      - investing/buffett-shareholder-letters-collection.md  # valuation lens
    foundation_parts: [11]  # Strategic direction substrate
    perspectives_required: [strategic, epistemic, capital]

  profitability:
    primary_clusters: [mgmt, investing, pdm]
    secondary_clusters: [systems]
    expected_book_count: 7-12
    canonical_picks:
      - investing/buffett-shareholder-letters-collection.md
      - mgmt/drucker-effective-executive-2006.md
      - pdm/cagan-inspired-2ed-2017.md
    foundation_parts: [7, 11]
    perspectives_required: [strategic, capital, operational]

  market-entry:
    primary_clusters: [mgmt, pdm, systems]
    secondary_clusters: [philosophy-science, investing]
    expected_book_count: 8-12
    foundation_parts: [11, 7]
    perspectives_required: [strategic, epistemic, systems]

  M&A:
    primary_clusters: [mgmt, investing]
    secondary_clusters: [philosophy, systems]
    expected_book_count: 6-10
    foundation_parts: [11]
    perspectives_required: [strategic, capital, epistemic]

  niche-selection:
    primary_clusters: [pdm, mgmt]
    secondary_clusters: [systems, complexity]
    expected_book_count: 7-10
    foundation_parts: [11, 7]
    perspectives_required: [PM-Cagan, strategic, systems]

  system-design:
    primary_clusters: [systems, cybernetics, engineering-foundations, clean-code]
    secondary_clusters: [biology, complexity]
    expected_book_count: 8-12
    foundation_parts: [4, 5, 8]  # Roles, Compound learning, Health monitoring
    perspectives_required: [systems-Meadows, cybernetics-VSM, engineering, biology]

  risk-analysis:
    primary_clusters: [philosophy-science, mgmt, investing]
    secondary_clusters: [systems, anthropic]
    expected_book_count: 6-10
    foundation_parts: [6a, 6b, 8]  # Provenance, Human gate, Health
    perspectives_required: [epistemic-Popper, stoic, capital, constitutional]

  sales-strategy:
    primary_clusters: [mgmt, pdm]
    secondary_clusters: [philosophy]  # negotiation, persuasion ethics
    expected_book_count: 5-8
    foundation_parts: [10]  # External touchpoints CRM
    perspectives_required: [PM-Cagan, strategic, ethical]

  capability-acquisition:
    primary_clusters: [philosophy, mgmt, clean-code]
    secondary_clusters: [biology]  # learning theory
    expected_book_count: 6-9
    foundation_parts: [3, 5]  # KB, Compound learning
    perspectives_required: [epistemic, compounding-engineering, learning]

  retrospective:
    primary_clusters: [philosophy-science, mgmt]
    secondary_clusters: [philosophy, systems]
    expected_book_count: 5-8
    foundation_parts: [5, 6a]
    perspectives_required: [epistemic-Popper, compound-learning, F-G-R]
```

**Provenance:** Mapping — original design, basedirovannye на cluster contents verified Explore Agent 1 + own knowledge of canonical books в `INDEX.md`. Foundation Parts mapping — basedirovannye на UC mapping в `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md:L60-75` (11 Parts → UC families). **AWAITING-RUSLAN-ACK** для full canonical_picks list (current draft 50% complete).

---

## §3 20 testable гипотез (falsifiable, with metrics)

Структура каждой гипотезы:
- **H-N:** name
- **Claim:** что утверждаем
- **Falsifier:** что доказывает ошибочность
- **Metric:** как мерим
- **Threshold:** boundary success/fail

### Группа A — Provenance accuracy (5 hypotheses)

**H-1. Citation density.** Books-grounded плана содержит ≥0.95 атомарных claims с inline citation.
- *Falsifier:* среднее coverage <0.85 на 5+ кейсах.
- *Metric:* `tools/citation-coverage.py` Layer-B scanner.
- *Threshold:* ≥0.95 PASS / 0.85-0.95 WATCH / <0.85 FAIL.

**H-2. Citation correctness.** ≥0.95 cited file_paths существуют и line-ranges valid.
- *Falsifier:* >5% citations point на отсутствующие файлы / out-of-range lines.
- *Metric:* automated filesystem + line-count check.
- *Threshold:* ≥0.95 PASS.

**H-3. No confabulation on missing sources.** Когда меня спрашивают про несуществующий концепт (e.g. TRM в Phase 1) — план явно flag'ит «не нашёл», не выдумывает.
- *Falsifier:* в ≥1 кейсе Claude generates fictional «TRM definition» without flag.
- *Metric:* manual Ruslan review.
- *Threshold:* 0 confabulation events на 8 кейсах.

**H-4. F-G-R tagging applied.** ≥0.50 promotional claims в plan'е carry F-G-R tags (Formality/Group-scope/Reliability).
- *Falsifier:* среднее <0.30 на caseload.
- *Metric:* manual count + automated `grep '\[F[2-8]/[A-Z]/R-(low|mid|high)\]'`.
- *Threshold:* ≥0.50 PASS / <0.30 FAIL.

**H-5. Source diversity floor.** Каждый план cites ≥3 distinct subcategories из books-md/ (т.е. multi-cluster, не single-cluster monoculture).
- *Falsifier:* >25% планов используют ≤2 clusters.
- *Metric:* automated cluster-count from citation paths.
- *Threshold:* ≥3 distinct subcategories на ≥75% planов.

### Группа B — Multi-perspective synthesis quality (4 hypotheses)

**H-6. Perspective competition visible.** План явно показывает ≥3 perspective views, и они **не идентичны** (есть disagreement/tension surfaced).
- *Falsifier:* Ruslan rubric «multi-perspective surfaced»: <3.0 average на 5-point scale.
- *Metric:* Ruslan rubric (5-point: 1=monologue, 5=structured competition).
- *Threshold:* ≥3.5 average / <2.5 FAIL.

**H-7. Synthesis adds value beyond aggregation.** Final recommendation produces insight non-derivable из individual perspective.
- *Falsifier:* Ruslan rubric «synthesis novelty»: <3.0.
- *Metric:* Ruslan rubric.
- *Threshold:* ≥3.5.

**H-8. Trade-off explicit.** Plan surfaces ≥2 explicit trade-offs (X vs Y) per recommendation, не только monolithic «do this».
- *Falsifier:* >50% plans содержат 0-1 trade-off.
- *Metric:* count «vs», «однако», «trade-off», «но» в recommendation section.
- *Threshold:* ≥2 trade-offs на ≥75% planов.

**H-9. Ruslan-as-strategist preserved.** Plan дает options + analysis + trade-offs, НЕ диктует strategic conclusion (Hard rule §5).
- *Falsifier:* >2 кейсах из 8 — план содержит prescriptive «делай X» без owner-decision flagging.
- *Metric:* manual Ruslan review.
- *Threshold:* 0-1 violations в caseload.

### Группа C — Books-grounding vs generic baseline (3 hypotheses, **central**)

**H-10. Actionability lift ≥1.0.** Books-grounded plan вышиб generic baseline на ≥1.0 на 5-point actionability rubric.
- *Falsifier:* среднее diff <0.5 across 5+ paired cases.
- *Metric:* paired Ruslan rubric (same case, both versions, blind order).
- *Threshold:* mean diff ≥1.0 PASS / 0.5-1.0 WATCH / <0.5 FAIL **(scale gate)**.

**H-11. Surprise factor lift ≥0.7.** Books-grounded plan содержит более non-obvious insights (rubric «surprise»: 1=expected, 5=non-derivable from generic).
- *Falsifier:* среднее diff <0.3.
- *Metric:* paired Ruslan rubric.
- *Threshold:* mean diff ≥0.7 PASS / <0.3 FAIL.

**H-12. Books actually influence recommendation.** В ≥75% paired cases — books-grounded plan дает different recommendation than baseline (not just same recommendation with citations).
- *Falsifier:* <50% cases content-different.
- *Metric:* manual Ruslan review «recommendation diff: identical / partial / substantial».
- *Threshold:* ≥75% «substantial» PASS / <50% FAIL.

### Группа D — Selection algorithm quality (3 hypotheses)

**H-13. Selected books rated relevant.** Ruslan post-hoc rates ≥0.70 of selected books как «правильно подобрана к кейсу».
- *Falsifier:* <0.50 average relevance.
- *Metric:* Ruslan rates each selected book 1-5; relevance = (rating≥3) / total.
- *Threshold:* ≥0.70 PASS / <0.50 FAIL.

**H-14. No critical book missed.** Ruslan не identifies >1 «критически отсутствующая книга» per case (post-hoc gap analysis).
- *Falsifier:* >2 cases с critical-gap >1.
- *Metric:* Ruslan post-case interview.
- *Threshold:* ≤1 case с critical-gap.

**H-15. Selection time efficient.** Total time selection algorithm runs ≤30s wall-clock (deterministic frontmatter scan).
- *Falsifier:* avg >120s.
- *Metric:* timer in selection script.
- *Threshold:* ≤30s PASS.

### Группа E — Token efficiency + drift (3 hypotheses)

**H-16. Token budget compliance.** Total tokens consumed per case ≤1.0M (Opus 4.7 [1m] hard limit).
- *Falsifier:* ≥1 case overflow.
- *Metric:* harness telemetry.
- *Threshold:* 0 overflow.

**H-17. Sub-agent compression effective.** Sub-agent batch reading saves ≥80% main-context tokens vs raw load.
- *Falsifier:* compression ratio <0.50.
- *Metric:* compare main-context size с/без sub-agent strategy на 2 controlled cases.
- *Threshold:* ≥0.80 ratio PASS.

**H-18. No long-session drift.** Quality (rubric average) не degrades >0.5 после 2-3 turns of revisions vs initial output.
- *Falsifier:* >50% revised plans score lower than initial.
- *Metric:* paired rubric initial vs final.
- *Threshold:* drift ≤0.5.

### Группа F — Friction + cost-benefit (2 hypotheses, **decision gates**)

**H-19. Setup overhead bearable.** Total time от case-brief до finalized plan ≤90 минут walltime в Phase 1, ≤60 минут в Phase 2 (после calibration).
- *Falsifier:* avg >120 min Phase 2.
- *Metric:* timer.
- *Threshold:* ≤90 Phase 1, ≤60 Phase 2.

**H-20. Pilot worth scaling.** ≥3 из 5 «main hypotheses» (H-1, H-6, H-10, H-13, H-19) достигают PASS threshold.
- *Falsifier:* <3 PASS.
- *Metric:* aggregate of H-1/H-6/H-10/H-13/H-19 results.
- *Threshold:* ≥3 PASS = SCALE; 2 = PIVOT; ≤1 = DROP. **Phase 3 verdict gate.**

**Provenance:** Hypotheses — original design. Linked to Hard rules §3 (provenance) и §11 (5-15 books) из `/tmp/meta-prompt.md:L78,L86`. Rubric structure adopted from Foundation F-G-R framework (`swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I`).

---

## §4 Test cases (8 кейсов: 3 classical + 5 Jetix-specific)

Формат каждого:
- **ID + Name**
- **Brief** (~100-200 слов)
- **Category** (из §2.3 enum)
- **Expected difficulty** (1-5)
- **What it tests well** (специфические гипотезы)
- **Expected book pool** (estimated cluster + count)
- **Baseline pair** (yes/no — проводим без books)

### TC-1. Market sizing: Mittelstand AI consulting TAM

**Brief:** Нужно estimate TAM/SAM/SOM для AI services agency targeting German Mittelstand (mid-size 250-2500 employees, manufacturing + Pharma + B2B SaaS DACH). Inputs: Statista mid-2025 numbers если доступны через WebFetch (else flag), Mittelstand BVMW reports, AI adoption surveys 2024-2025. Deliverable: 3-tier numerical model (TAM / SAM / SOM) + key assumptions + sensitivity analysis.

**Category:** market-sizing
**Difficulty:** 3 (data-heavy, but structured)
**Tests well:** H-1 (citation density, нужны source pointers), H-13 (selection relevance), H-19 (setup overhead на data-heavy case)
**Expected book pool:** 6-8 books from `mgmt/` (Christensen, Grove) + `investing/` (Buffett-style market analysis) + `pdm/` (Cagan unit economics). Foundation Part 11 (Strategic direction).
**Baseline pair:** **YES** — same case без books-grounding для diff на H-10/H-11/H-12.

### TC-2. Profitability: 6 months in — Revenue↑ vs Cost↓?

**Brief:** AI consulting agency 6 месяцев работает. Revenue €15K MRR, Cost €4K MRR, owner 60h/week. Decision: invest next quarter в (a) revenue scaling (sales hire / outreach automation) или (b) cost reduction (delivery automation / template productization)? Constraints: solo founder, нельзя hire without revenue ≥€25K MRR, life-energy bounded.

**Category:** profitability
**Difficulty:** 4 (multi-variable optimization + life constraints)
**Tests well:** H-7 (synthesis novelty), H-8 (trade-off explicit), H-9 (Ruslan-as-strategist preserved — easy to fail here)
**Expected book pool:** 7-9 books — `investing/` (Buffett capital allocation lens) + `mgmt/` (Drucker effectiveness) + `pdm/` (Cagan unit economics) + `philosophy/` (stoic capacity limits). Foundation Parts 7+11.
**Baseline pair:** **YES**.

### TC-3. Market entry: open spinoff в US или нет?

**Brief:** Solo agency успешен в DACH. Opportunity: US market (10× SAM). Entry costs: timezone shift, legal entity, English content remake (Russian/German content), delivery model adaptation. Constraints: solo founder может только 1 рынок serve well. Decision deadline: 3 месяца.

**Category:** market-entry
**Difficulty:** 4
**Tests well:** H-6 (perspective competition: cybernetics-VSM «can you scale your control loops?» vs PM-Cagan «is product-market-fit transferable?» vs Stoic «have you mastered current market?»), H-10 (actionability), H-12 (different recommendation lift)
**Expected book pool:** 8-10 books — `systems/` + `cybernetics/` + `mgmt/` + `philosophy/` (stoic). Foundation Parts 7+11.
**Baseline pair:** **YES**.

### TC-4. TRM L0 sales test design  ⚠️ **BLOCKED**

**Brief:** ⚠️ **BLOCKED** — referent doc `JETIX-TRM-MODEL-2026-04-30.md` не существует (verified 2026-04-30). Не могу written precise brief without TRM definition.

**Workaround options для unblock:**
1. Ruslan creates JETIX-TRM-MODEL-2026-04-30.md before Phase 1 start
2. Replace this case with **TC-4-alt: «Sales experiment design для €50K Q2 2026 quick-money path»** (referencing actual `quick-money` project from CLAUDE.md project list + 8 active projects)
3. Drop entirely — Phase 1 runs 7 cases вместо 8

**Open question for Ruslan** (see §Open questions).

### TC-5. Tseren outreach risk-analysis  ⚠️ **PARTIAL BLOCK**

**Brief:** Ruslan собирается outreach до Tseren (известная public figure / influencer / advisor — context unclear without explicit identification). Goal: позиционирование Jetix + secure intro / advisory / partnership. Risks: relationship damage, time-loss, public opt-out, alternative-cost. Deliverable: pre-outreach decision frame: go/no-go + если go, специфический approach с downside-mitigation.

**Category:** sales-strategy + risk-analysis hybrid
**Difficulty:** 4 (high-stakes single-shot)
**Tests well:** H-3 (no confabulation: Tseren identity unknown — Claude must flag, не invent), H-7 (synthesis), H-9 (strategic preservation)
**Expected book pool:** 6-8 — `philosophy/` (negotiation ethics, asymmetric outreach) + `mgmt/` (Carnegie if present, Cialdini influence) + `philosophy-science/` (Bayesian risk under uncertainty).
**Baseline pair:** YES.
**⚠️ Note:** Tseren identity не в repo memory. Plan execution требует Ruslan's manual brief addition или CRM lookup (`crm/people/tseren-*`).

### TC-6. Mittelstand niche selection — какой optimal cluster?

**Brief:** Mittelstand 3 candidate niches identified: (a) industrial automation B2B (high-margin, long sales cycles, German trust-heavy), (b) Pharma compliance (high-margin, regulated, sensitive data), (c) B2B SaaS DACH (medium-margin, faster sales, English-speaking founders). Constraints: solo founder, €50K Q2 2026 target, ICP existing. Decision: which niche to commit Q3 2026.

**Category:** niche-selection
**Difficulty:** 4
**Tests well:** H-6 (perspective competition: PM-Cagan vs lean-startup vs Drucker «what business are we in»), H-10 (actionability), H-13 (selection relevance — нужны Cagan + niche-strategy specific)
**Expected book pool:** 7-10 — `pdm/` (Cagan), `mgmt/` (Christensen jobs-to-be-done if present, Drucker), `systems/` (network effects), `philosophy/` (commitment escalation).
**Baseline pair:** YES.

### TC-7. Phase B trigger predicate validation (system-design)

**Brief:** Foundation Architecture Phase A LOCKED 2026-04-28. Phase B triggers (synthesis-human L653-657): «≥3 months Phase A operational maturity + Tier 0 events <1/quarter + ≥10 F5 methodologies». Question: are these triggers correctly calibrated? Pretty straightforward measurement, или есть failure modes (gaming the metric, premature trigger, under-triggering)? Deliverable: epistemic audit + risk register + recommendation.

**Category:** system-design + retrospective hybrid
**Difficulty:** 5 (meta + system-thinking)
**Tests well:** H-6 (cybernetics-VSM viewpoint vs SRE-SLI vs Popper-falsifiability), H-7 (synthesis), H-1 (heavy citation: Foundation Parts + Beer + Goodhart's law if present)
**Expected book pool:** 8-12 — `cybernetics/` (Beer, Wiener — feedback loops), `engineering-foundations/` (Vincenti — engineering knowledge structure), `philosophy-science/` (Popper — falsifiability), `systems/` (Meadows — leverage points), `sre/` (SLO calibration).
**Baseline pair:** **NO** — meta-case, baseline irrelevant (no generic «what is Phase B trigger predicate» equivalent).

### TC-8. Compound learning ROI — продолжать 40/10/40/10 cycle?

**Brief:** Foundation Part 5 specifies cycle ratio Plan 40% / Work 10% / Review 40% / Compound 10% (`swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md:L175-178`). Solo founder context: this means out of 60h/week, ~6h actual «work». Question: is this ratio dogmatic (FUNDAMENTAL), and what is empirical ROI evidence after 1-2 cycles? Deliverable: Bayesian update on whether 40/10/40/10 should be preserved, adapted, or relaxed.

**Category:** retrospective
**Difficulty:** 5 (epistemic humility + meta-policy)
**Tests well:** H-6 (epistemic-Popper vs compound-engineering vs PM-Cagan «outcomes over outputs»), H-9 (Ruslan-as-strategist — easy fail), H-7 (synthesis novelty)
**Expected book pool:** 7-9 — `philosophy-science/` (Popper, Kuhn), `mgmt/` (Drucker effectiveness), `clean-code/` (Brooks Mythical Man-Month), `philosophy/` (stoic discipline). Foundation Part 5.
**Baseline pair:** YES.

**Provenance:** Test cases TC-1, TC-2, TC-3, TC-6, TC-7, TC-8 — original design grounded in CLAUDE.md project list («quick-money» project, €50K Q2 2026 goal) + Foundation v1.0 architecture. TC-4 BLOCKED, TC-5 PARTIAL — explicit flags. Foundation references verified Phase 1 exploration.

---

## §5 Метрики оценки

### §5.1 Quantitative metrics (machine-computable)

| Metric | Definition | Target | Source |
|---|---|---|---|
| **citation_coverage** | claims_with_inline_cite / total_claims | ≥0.95 | H-1, Layer-B scanner |
| **citation_correctness** | valid_paths / cited_paths | ≥0.95 | H-2 |
| **source_diversity** | distinct_subcategories_cited per plan | ≥3 | H-5 |
| **fgr_density** | claims_with_F_G_R_tag / promotable_claims | ≥0.50 | H-4 |
| **trade_off_count** | explicit «vs» / «однако» / «но» в recommendation section | ≥2/plan | H-8 |
| **tokens_consumed** | total tokens per case | ≤1.0M | H-16 |
| **selection_time_s** | wall-clock seconds for selection algorithm | ≤30s | H-15 |
| **plan_walltime_min** | от case-brief до finalized plan | ≤90 P1, ≤60 P2 | H-19 |
| **subagent_compression_ratio** | (raw_load - subagent_summary) / raw_load | ≥0.80 | H-17 |
| **selected_book_count** | count books per plan | 5-15 | meta-prompt §11 |

### §5.2 Qualitative metrics (Ruslan rubric, 5-point Likert)

Каждая rubric scored 1 (worst) — 5 (best). Plan version blind-order randomised для baseline pairs.

| Rubric | Question | Anchor 1 | Anchor 5 |
|---|---|---|---|
| **actionability** | «Достаточно ли в плане действий, которые завтра начать?» | Generic platitudes | 5+ concrete actions с deadlines |
| **multi_perspective** | «Видны ли ≥3 разных оптики и есть ли между ними напряжение?» | Single voice | 3+ оптики, явный disagreement, synthesis на конце |
| **synthesis_novelty** | «Содержит ли план insight, неочевидный из любой одной книги отдельно?» | Просто aggregated | Emergent property |
| **surprise** | «Содержит ли план non-obvious insights?» | Все ожидаемо | ≥1 серьезный «aha» |
| **strategic_preservation** | «Уважает ли план Ruslan-as-strategist (Hard rule §5)?» | Прескриптивный | Options + trade-offs, выбор за owner |
| **books_visibility** | «Видна ли реальная влияние книг на план?» | Citations cosmetic | Reasoning visibly книжный |

### §5.3 Baseline comparison protocol (paired A/B)

**Per-case protocol** (для cases с baseline_pair=YES):

```
1. Run books-grounded plan (Plan A)
   - Full methodology §1
   - Save to plans/<case_id>-A-books-grounded.md
2. Fresh session, same case-brief, NO books pre-load
   - Generic Plan Mode + ultrathink
   - Save to plans/<case_id>-B-baseline.md
3. Cooling-off ≥24h (avoid recall bias)
4. Blind-order rubric scoring by Ruslan:
   - Both plans renamed to plans/<case_id>-{X,Y}.md
   - Random X/Y assignment
   - Ruslan rates both на §5.2 rubric
5. Reveal mapping → diff scores
6. Aggregate diffs across all paired cases → H-10/H-11/H-12 metrics
```

**Hard rule:** Same Opus 4.7 [1m] для both runs (apples-to-apples). Different model = invalid comparison.

**Provenance:** Protocol — original design. Blind-order procedure grounded in scientific method best practices (общеизвестно, no specific source).

---

## §6 Iteration roadmap (4 weeks total)

### Phase 1 — Calibration (Week 1)

**Goal:** Validate methodology infrastructure, calibrate selection algorithm.

**Tasks:**
- D1: Ack этот PILOT-DESIGN PLAN (Ruslan)
- D1-D2: Materialize `.claude/config/case-cluster-map.yaml` (Phase 1.5 task) — finalize 50%-draft from §2.3
- D2-D3: Implement Layer-B citation-coverage scanner (`tools/citation-coverage.py`) — interim, manual run, ~50 lines Python
- D3: Author prompt-skeleton template (`swarm/wiki/_templates/case-design-prompt.md`)
- D4-D5: Run **TC-1 (market-sizing)** + **TC-2 (profitability)** — 2 cases
  - For each: books-grounded run + baseline run (paired)
  - Capture metrics §5.1 + Ruslan rubric §5.2
- D6-D7: Calibration retrospective:
  - Review TC-1, TC-2 metrics
  - Adjust selection algorithm weights / cluster mapping
  - Update prompt skeleton based on observed failure modes

**Phase 1 Gate:**
- ≥1 of 2 cases hit H-1 (citation ≥0.95) AND H-19 (walltime ≤90 min)
- If gate fails → STOP, debug infrastructure before Phase 2

**Deliverables:**
- Calibrated case-cluster-map.yaml
- Calibrated prompt skeleton
- 2 test case reports (paired)
- Phase 1 retrospective doc

### Phase 2 — Full caseload (Weeks 2-3)

**Goal:** Run remaining 5-7 cases, accumulate sufficient signal.

**Tasks:**
- W2-D1-D3: Run **TC-3 (market-entry)** + **TC-4-resolved or TC-4-alt** + **TC-5 (Tseren)** — 3 cases (paired where applicable)
- W2-D4-D5: Run **TC-6 (Mittelstand niche)** + **TC-7 (Phase B trigger)** — 2 cases (TC-7 unpaired)
- W2-D6-D7: Mid-pilot retro: emerging failure modes? Selection algorithm drift? Token blow-ups?
- W3-D1-D2: Run **TC-8 (Compound learning ROI)** + любые adjustments
- W3-D3-D5: Aggregate metrics across all 7-8 cases
- W3-D6-D7: Compute H-1 through H-20 PASS/FAIL

**Phase 2 Gate:**
- ≥2 of 3 paired cases (TC-1/2/3/6/8) achieve H-10 (actionability lift ≥1.0)
- If <2 → no scale, proceed direct to Phase 3 with PIVOT/DROP analysis

**Deliverables:**
- 7-8 test case reports
- Aggregated metrics dashboard
- Mid-pilot retrospective

### Phase 3 — Verdict + integration (Week 4)

**Goal:** Decide scale / pivot / drop. Если scale — integrate в operational workflow.

**Tasks:**
- D1-D2: H-20 verdict computation:
  - Count «main hypotheses PASS» (H-1, H-6, H-10, H-13, H-19)
  - ≥3 PASS → SCALE
  - 2 PASS → PIVOT (specific dimension fails — e.g. H-19 fails → simplify, not abandon)
  - ≤1 PASS → DROP
- D3 (if SCALE):
  - Materialize `/case-design <case>` skill at `.claude/skills/case-design/`
  - Add to «KM MVP» section in CLAUDE.md
  - Author `swarm/wiki/operations/case-design-methodology-v1.md` (canonical)
- D3 (if PIVOT): identify specific failed dimensions (e.g. selection algorithm bad → embedding search Phase 3.5)
- D3 (if DROP): document why (avoid repeat-attempt в 6 months); archive под `swarm/wiki/cycles/cyc-pilot-case-design-2026-04-30/dropped.md`
- D4: Write **PILOT-VERDICT-MEMO** в `decisions/PILOT-VERDICT-CASE-DESIGN-METHODOLOGY-2026-MM-DD.md`
- D5: Final ack from Ruslan, lock verdict, decommission interim infrastructure if DROP

**Deliverables:**
- PILOT-VERDICT-MEMO (≤500 слов + metrics annex)
- If SCALE: `/case-design` skill + canonical methodology doc
- Updated CLAUDE.md если SCALE

**Provenance:** Roadmap structure — original design. Phase-gate model adopted from Foundation Part 7 5-state machine (`swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md`). 4-week timing — conventional pilot length, not specific source.

---

## §7 Risk register + mitigation

### R-1. Books confabulation (citation correctness <0.95)

- **Trigger:** Layer-B scanner finds 5+ citations с invalid path или out-of-range lines.
- **Mitigation:**
  - Pre-flight check: `tools/citation-coverage.py --pre-flight` runs after generation, BEFORE handoff to Ruslan
  - Если fail: rerun с explicit instruction «верни план с inline citations, при non-existence — flag, не выдумывай»
  - Если 2× fails — escalate to Ruslan (constitutional violation, Halt-Log-Alert)
- **Severity:** F8 (constitutional, threatens whole methodology trust)

### R-2. Token blow-up (>1M context)

- **Trigger:** Selection algorithm picks 12+ books × avg 80K = >960K, no margin.
- **Mitigation:**
  - Hard cap §1.5: max 700K из books в main context
  - Auto-fallback: if cluster > 700K → switch to sub-agent batch (§1.7)
  - Pre-flight: token estimate before context load, abort+restructure if >900K total
- **Severity:** F4 (operational; recoverable via sub-agent fallback)

### R-3. Drift over long sessions (quality degrades after revisions)

- **Trigger:** Rubric drops >0.5 between turn 1 and turn 3.
- **Mitigation:**
  - Re-plan discipline: каждые 2 turns — `Shift+Tab` → fresh Plan Mode review (`raw/articles/2026-04-29-claude-code-best-practices/plan-mode-claude-code.md:L196-205`)
  - Rule of 30 minutes (plan-mode L215-217): split case на podtasks ≤30 min each
  - If drift detected → fresh session, re-load Tier 0 + new Tier 2
- **Severity:** F4

### R-4. Cherry-picking sources (selection bias to favorite books)

- **Trigger:** Same 3-5 books appear в >70% test cases.
- **Mitigation:**
  - Diversity floor (§1.3 Step 6): ≥3 distinct subcategories per case
  - Phase 2 ranking re-calibration: down-weight «over-used» books (frequency penalty)
  - Manual Ruslan audit: Phase 1.5 retro reviews picked-books stats
- **Severity:** F4

### R-5. Books-grounded не лучше generic baseline (H-10 fail)

- **Trigger:** mean diff <0.5 на 5+ paired cases.
- **Mitigation:**
  - This is the **whole point of pilot** — fail discovery is success, not regression
  - Phase 3 verdict DROP scenario; no regret
  - If <0.3 → consider что Opus 4.7 base knowledge already contains canonical books distilled (selection adds friction without lift)
- **Severity:** F2 (epistemic, not operational; output of pilot, not failure of pilot)

### R-6. Selection algorithm mis-fires (wrong cluster picked)

- **Trigger:** Ruslan post-hoc «relevance» rating <0.50 (H-13 fail).
- **Mitigation:**
  - Hand-curated mapping (§2.3) — transparent, editable, не embedding-opaque
  - Phase 1 calibration explicit revises mapping after TC-1, TC-2
  - Manual override (pin_books, exclude_books) escape valve
- **Severity:** F4

### R-7. Methodology overhead-not-worth-it (H-19 fail на >120 min)

- **Trigger:** avg walltime per case >120 min in Phase 2.
- **Mitigation:**
  - Sub-agent batch reading (§1.7) reduces main-context bandwidth
  - Phase 2 PIVOT option: drop heaviest 2-3 books per case (cap at 5, не 12)
  - Tooling investment: better selection script, automated pre-load
- **Severity:** F4 (operational viability)

### R-8. Cargo-cult provenance (formal citations, but не actually grounding)

- **Trigger:** H-12 fails (recommendation identical to baseline).
- **Mitigation:**
  - H-7 (synthesis novelty) rubric catches this
  - H-12 measures content-diff explicitly
  - If detected — pivot to ablation: remove citations layer, see if rubric drops; if not → confirms cargo-cult
- **Severity:** F4 (epistemic; methodology theater)

### R-9. Sub-agent context bleeding (sub-agent generates plan вместо main session)

- **Trigger:** Sub-agent output contains «recommendation» or «strategic conclusion».
- **Mitigation:**
  - Strict prompt (§1.7): sub-agents extract ONLY claims+line-ranges, не recommendation
  - Output schema enforcement (markdown bullets, не free prose)
  - Plan-authoring stays main session (architectural invariant)
- **Severity:** F4

### R-10. Hard rule §6 violation (solo-founder downgrade slips in)

- **Trigger:** Plan suggests «упрощённая версия для одного человека» despite Hard rule §6 (`/tmp/meta-prompt.md:L80`).
- **Mitigation:**
  - Hard rule в prompt skeleton (§1.1) каждый run
  - Ruslan rubric flag «solo-founder downgrade detected» — auto-fail of plan, regenerate
- **Severity:** F8 (constitutional)

**Provenance:** Risks — original synthesis from meta-prompt §7 risk hints (`/tmp/meta-prompt.md:L70-73`) + Foundation Halt-Log-Alert framework (`swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.2`).

---

## §8 Verification protocol (как тестировать end-to-end)

**Verification — это не «test the code», а «test the methodology». Concrete steps:**

### V-1. Methodology infrastructure check (Phase 1, D1-D3)

```bash
# 1. Selection algorithm executes deterministically
python3 tools/select-books.py --category market-sizing --max-books 8
# expected: 8 book paths, sorted by score, total tokens estimate <600K

# 2. Citation scanner runs cleanly
python3 tools/citation-coverage.py swarm/wiki/_templates/case-design-prompt.md
# expected: prints coverage ratio + invalid citations list

# 3. Cluster map syntactically valid
python3 -c "import yaml; yaml.safe_load(open('.claude/config/case-cluster-map.yaml'))"
# expected: no exceptions
```

### V-2. End-to-end first run (Phase 1, D4)

Manual walkthrough TC-1 (market-sizing):

1. Ruslan opens fresh Claude Code session, mode: Opus 4.7 [1m] + Plan Mode (Shift+Tab×2)
2. Loads `swarm/wiki/_templates/case-design-prompt.md`
3. Fills `## Кейс` with TC-1 brief (§4 above)
4. Fills `## Категория`: market-sizing
5. Triggers selection: invoke `tools/select-books.py` (или Claude Code skill if implemented)
6. Pre-load context: Tier 0 (CLAUDE.md auto + Vision + synthesis-human + methodology articles) + Tier 1 (Part 11) + Tier 2 (selected books)
7. Adds `ultrathink` to request
8. Claude generates plan
9. Run citation scanner → verify ≥0.95 coverage
10. Save to `plans/TC-1-A-books-grounded.md`

### V-3. Baseline pair (Phase 1, D4)

1. Fresh session, same model, same Plan Mode, same `ultrathink`
2. NO books pre-load, NO Foundation pre-load
3. Same case brief
4. Generate plan, save to `plans/TC-1-B-baseline.md`

### V-4. Rubric scoring (Phase 1, D5)

1. Cooling-off 24h
2. Blind rename: `plans/TC-1-X.md`, `plans/TC-1-Y.md` (random)
3. Ruslan rates both на §5.2 rubric (6 dimensions × 5-point)
4. Reveal mapping → compute diffs
5. Log в `swarm/wiki/cycles/cyc-pilot-case-design-2026-04-30/results-TC-1.md`

### V-5. Phase 1 gate (Phase 1, D7)

```python
# pseudo-decision
if (TC1.citation_coverage >= 0.95 or TC2.citation_coverage >= 0.95) and \
   (TC1.walltime_min <= 90 and TC2.walltime_min <= 90):
    proceed_to_phase_2()
else:
    halt_pilot()
    debug_infrastructure()
```

### V-6. Phase 2 caseload run (Weeks 2-3)

Repeat V-2 through V-4 для TC-3 through TC-8 (skipping TC-4 if blocked).

### V-7. Phase 3 verdict (Week 4)

```python
main_hypotheses_pass = sum([H_1.pass_, H_6.pass_, H_10.pass_, H_13.pass_, H_19.pass_])
if main_hypotheses_pass >= 3:
    verdict = "SCALE"
elif main_hypotheses_pass == 2:
    verdict = "PIVOT"
else:
    verdict = "DROP"

write_pilot_verdict_memo(verdict, all_metrics)
```

**Provenance:** Verification protocol — original design. Mirrors phase-gate discipline from Foundation Part 7.

---

## Open questions for Ruslan (sequential, not multiple-choice)

Hard rule §8: НЕ опросы — конкретные questions.

**Q-1. Существуют ли `JETIX-WORKSHOP-CONCEPT-2026-04-30.md` и `JETIX-TRM-MODEL-2026-04-30.md` где-то outside `decisions/` (e.g. drafts, private/, in-progress)?** Verified отсутствие в `decisions/` через `ls + find`. Если они in-progress — указать ETA для Phase 1 D1; если abandoned — заменить TC-4 на TC-4-alt («Sales experiment design для €50K Q2 2026 quick-money path», который referencing actual `quick-money` project из CLAUDE.md). **Влияние:** TC-4 BLOCKED до ответа.

**Q-2. Tseren — кто это в context CRM/network?** Не нашёл explicit ID в memory или CRM index. Нужно одно из: (a) full name + role (e.g. «Tseren Damba — известный AI investor / advisor / influencer / friend»), (b) pointer на `crm/people/tseren-*.md` если existing, (c) markup «hypothetical example» если просто placeholder. **Влияние:** TC-5 partial-block без identity.

**Q-3. Phase 1.5 — Materialization of `case-cluster-map.yaml` canonical_picks.** Я подготовил **50%-draft** (skeleton + 3-4 categories с canonical_picks). Для оставшихся 6-7 категорий нужен либо твой direct vetting (вручную выбрать canonical books per category), либо approve auto-generation через ranking algorithm Phase 1 D2 (без vetting, но faster start). **Что предпочитаешь?**

**Q-4. `meta/` cluster (140 chunked extracts) — как обращаться?** Сейчас design treats meta/ как auxiliary lookup-only (§2.2). Альтернатива: spend Phase 1.5 D на «origin manifest» (каждый chunk → source book), что превращает meta/ в proper indexable cluster. Это +1-2 day calibration overhead, но добавляет 10-15 source books в pool. **Worth the upfront cost?**

**Q-5. Sub-agent token-budget allocation.** §1.7 предлагает max 3 parallel sub-agents для batch-чтения. При complex кейсах (TC-7 system-design, 8-12 books expected) this может быть constraint. Альтернатива — sequential sub-agents (5-6 invocations, slower walltime, более thorough each). **Trade-off для TC-7 specifically: parallel=fast/shallow vs sequential=slow/deep — какой default для system-design кейсов?**

**Q-6. Phase 3 SCALE — где integration?** Если pilot succeeds, я предлагаю materialize `/case-design` skill в `.claude/skills/case-design/`. Альтернатива: integrate в existing `/plan-day` или extension к `/project-bootstrap`. Не уверен, как ты предпочитаешь grow skill surface — separate skills или existing skills' enhancement.

**Q-7. Pilot temporal ownership.** 4-week roadmap (§6) предполагает Ruslan dedicates ≥10h/week на cases + scoring. Realistic для current load (CLAUDE.md mentions 8 active projects, €50K Q2 2026 push)? Или нужно растянуть до 6-8 weeks с lighter weekly load? **Влияние:** Phase 1 gate timing.

---

## Provenance citation index (appendix)

Every architectural / methodological claim в этом плане traces к sources:

| Claim в плане | Source | Verified |
|---|---|---|
| 402 books, 11.7M tokens, единый frontmatter | `raw/books-md/INDEX.md:L1-7` + Explore Agent 1 report | ✅ |
| Frontmatter поля (`expert, priority, quality_grade, tags, subcategory, word_count, year`) | `raw/books-md/INDEX.md:L11-25` (table headers) + Explore sample reads | ✅ |
| Cluster sizes (mgmt 96, philosophy 66, systems 50, etc.) | Explore Agent 1 enumerated `find` output | ✅ |
| 11 LOCKED Foundation Parts | `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md:L60-75` + CLAUDE.md `## Foundation Architecture v1.0 (LOCKED 2026-04-28)` | ✅ |
| 35 UC × 12 categories | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:L432-448` (per Explore Agent 2 report) | ✅ via agent report; not own re-read |
| F-G-R F8 schema | `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md:§I` (per Explore Agent 3) | ✅ via agent |
| Halt-Log-Alert ≤1s/≤5s/≤60s | `swarm/wiki/foundations/part-6b-human-gate/architecture.md:§I.2` + CLAUDE.md §4 | ✅ |
| ultrathink — in-context instruction (not separate mode) | `raw/articles/2026-04-29-claude-code-best-practices/ultrathink-claude-code.md:L7-13, L21-35` | ✅ |
| ultrathink budget ~31,999 (legacy models only) | `ultrathink-claude-code.md:L41-46` | ✅ |
| Plan Mode = read-only block on file edits | `raw/articles/2026-04-29-claude-code-best-practices/plan-mode-claude-code.md:L11-12, L19-41` | ✅ |
| Opus Plan Mode pattern (Plan Opus / Code Sonnet) | `plan-mode-claude-code.md:L157-167` | ✅ via own re-read |
| 4-phase canonical workflow (Explore→Plan→Code→Commit) | `plan-mode-claude-code.md:L94-126` | ✅ |
| Re-plan discipline (Shift+Tab to re-enter Plan Mode) | `plan-mode-claude-code.md:L196-205` | ✅ |
| Rule of 30 minutes (one plan = ≤30 min implementable) | `plan-mode-claude-code.md:L215-217` | ✅ |
| 40/10/40/10 Plan/Work/Review/Compound | `swarm/wiki/synthesis/foundation-master-overview-human-2026-04-29.md:L175-178` | ✅ via agent |
| Phase B trigger predicate | `foundation-master-overview-human-2026-04-29.md:L653-657` | ✅ via agent |
| Wave D metrics (M-D-1..M-D-6) | `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-d/INTEGRATION-REPORT.md` (per Agent 3) | ✅ via agent |
| TRM-MODEL doc absent | own `find` verification 2026-04-30 | ✅ direct |
| WORKSHOP-CONCEPT doc absent | own `find` verification 2026-04-30 | ✅ direct |

**Coverage estimate:** ≥0.95 для structural claims; ≤0.85 для design proposals (which are original synthesis, не cited but explicit «own design» markers где applicable).

**Hard rule §3 compliance:** Provenance gates respected — все verified claims have line-ranges; non-verified marked «own design»; missing docs flagged explicitly, not confabulated.

---

## Готовность к ack

Этот план **готов к ack**. После ack — Phase 1 D1 запуск.

**Не готов к execution автономно** — 7 open questions выше требуют твоего input. Particular Q-1 (TRM doc) blocks TC-4; Q-3 (canonical_picks) blocks Phase 1 D2.

**Beta-first / enterprise-grade balance** (Hard rule §7): план достаточен для immediate calibration run; rough edges (`tools/select-books.py` существует только pseudocode, manual citation scanner) — explicit Phase 1 D1-D3 materialization tasks.
