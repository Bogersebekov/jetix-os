---
id: stage-1-untangle-atom-registry
title: Stage 1 — Atom Registry + Knot Map (Deep Variant)
date: 2026-04-21
type: prompt
status: ready
priority: P1 — blocks Genesis pipeline
depends_on: TENSIONS-PRE-RESOLVED.md (8 decisions LOCKED)
---

# Stage 1 — Atom Registry + Knot Map (Deep Variant)

## Контекст и миссия

Ruslan консолидирует всю текущую разрозненную память Jetix OS в набор финальных документов для архитекторов. Перед тем как писать D1 Vision / D2 Philosophy / D3 Plan / D4 Architecture-Brief, нужна **инвентаризация всего материала** — разложить на атомарные единицы с metadata + картировать противоречия / связи / gaps.

**Правило номер 1: НИЧЕГО НЕ ТЕРЯЕМ.** Каждая задача, каждая гипотеза, каждый концепт, каждый принцип — сохраняется как отдельный atom с уникальным ID. Потом этот registry живёт как база памяти системы — к нему возвращаются при написании D1-D4 и при составлении детального action plan после архитектуры.

**Правило номер 2: 8 decisions в TENSIONS-PRE-RESOLVED.md — OVERRIDE.** Любой atom из voice-memos / wiki / других источников, противоречащий этим 8 locked decisions, маркируется `status: overridden` и не используется для synthesis. Но atom всё равно остаётся в registry (provenance).

**Notion page контекст:** https://www.notion.so/3492496333bf812e8b62cbc61338ce06

---

## Что нужно сделать

Два deliverable:

### Deliverable 1: `raw/research/architecture-variants-2026-04-22/ATOM-REGISTRY.md`

Полный реестр всех atoms из ВСЕХ источников. Ожидаемый объём: 1500-3000 atoms, 5000-10000 строк markdown.

### Deliverable 2: `raw/research/architecture-variants-2026-04-22/KNOT-MAP.md`

Навигационный overview: tensions / clusters / gaps / orphans / statistics. Объём: 500-1500 строк.

---

## Источники (ВСЕ — полный re-read, Deep Variant)

### Group A — Wiki (primary, самое плотное)

- Вся `wiki/` directory recursively (~280+ файлов)
- Включая: `concepts/`, `ideas/`, `entities/`, `sources/`, `topics/`, `foundations/`, `experiments/`, `claims/`, `summaries/`, `niches/`
- Пропустить: `wiki/_templates/`, `wiki/index.md` (мета), `wiki/log.md` (хронология, не содержание), `wiki/graph/edges.jsonl` (структура)

### Group B — Voice-memos artefacts (already extracted, используются как quality-filter)

- `raw/research/architecture-variants-2026-04-22/RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md` (367 цитат)
- `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-MINI-WIKIPEDIA.md`
- `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-YEAR-PLAN.md` — особенно важно (118 TODOs + hypotheses)
- `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-STRATEGIC-IDEAS.md` (327 items, 5 categories)
- `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-FULL-DIGEST.md`
- `raw/research/architecture-variants-2026-04-22/VOICE-MEMOS-COMMUNITY-ADDENDUM.md`

### Group C — Voice-memo transcripts (source raw text, для проверки атрибуций)

- `raw/transcripts/*.txt` (~117 файлов) — используется только для провенанса / double-check цитат, НЕ как primary extraction (extraction уже сделан в Group B)
- `raw/voice-memos-text/community-addendum-2026-04-21.md` (2 text voice-notes)

### Group D — Architectural / Decision documents

- `CLAUDE.md`
- `design/JETIX-FPF.md` (D6, 3758 строк, constitutional document)
- `decisions/2026-04-19-architecture-v2-approval.md` (ADR Chunks 1-8, 60+ approved decisions)
- `decisions/2026-04-20-jetix-architecture-final-DRAFT.md` (D9, 1880 строк)
- `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md` ⬅️ **BINDING OVERRIDES**

### Group E — Notion bizmodels (fetch если возможно, иначе skip)

- Business Discovery (https://www.notion.so/3482496333bf81c0acd2df985e889383)
- Partnership Strategy (https://www.notion.so/3482496333bf8122ae1ec83f67c4a882)
- Producer Services (https://www.notion.so/3482496333bf81f3abbef315a7048c02)
- Jetix Exchange (https://www.notion.so/3482496333bf81d38300e3cb03b0bc91)

---

## Atom specification

### Atom types (10 категорий)

| Type | Определение | Пример | Source hint |
|---|---|---|---|
| `task` | Actionable TODO с глаголом действия | "описать ICP подробно" | voice-memos year-plan, wiki TODOs |
| `hypothesis` | Testable claim "если X то Y" или "предполагаю что..." | "AI-рычаг = чит-код для мышления" | voice-memos strategic, wiki ideas |
| `concept` | Named idea / framework / модель | "Gentleman inside / Predator outside" | wiki concepts, strategic |
| `principle` | Operating rule / convention | "4 часа в день + работа = достаточно" | voice-memos, wiki foundations |
| `claim` | Factual assertion (с или без evidence) | "капитализм → коммунизм на верхних слоях" | voice-memos strategic, wiki claims |
| `entity` | Person / company / product / place | "McKinsey", "Anthropic", "Stripe", "Berlin" | wiki entities, transcripts |
| `value` | Стойка / ценность / этос | "скин в игре", "givers not takers" | wiki foundations, philosophy |
| `bet` | Strategic wager с commitment | "$1M к концу года на счету" | voice-memos bets, strategic |
| `tension` | Internal conflict между claims / frames | "patents vs open-source" | cross-source analysis |
| `metric` | Measurable quantity или target | "€150/час × 4 часа = €600/день" | voice-memos, wiki metrics |

### Atom schema (YAML-like, в markdown)

Каждый atom в ATOM-REGISTRY представлен блоком:

```markdown
### atom-XXXX — <short descriptive title>

- **type:** task | hypothesis | concept | principle | claim | entity | value | bet | tension | metric
- **content:** <verbatim quote если возможно, иначе концентрированный paraphrase>
- **source:** <file path>:<line number если есть>
- **quote:** <direct quote block если содержание > paraphrase>
- **dimension:** base | life | company | community | money | relationships | philosophy | (multiple allowed, separated by /)
- **phase:** now | phase-1 | phase-2 | phase-3 | long-term | any
- **priority:** P1 | P2 | P3 | P4 | null (только для tasks)
- **status:** open | resolved | reinforced | contradicted | overridden
- **tags:** [<1-5 topic tags>]
- **relates_to:** [<list of other atom IDs с типом связи>]
  - atom-XXXX (reinforces)
  - atom-YYYY (contradicts)
  - atom-ZZZZ (depends)
  - atom-WWWW (variant)

<optional: 1-2 lines note / interpretation если нужно контекст>
```

### Atom ID format

`atom-NNNN` (4-digit zero-padded, starting 0001).

### Dimension assignment rules

7 dimensions (из Genesis Document frame):
- **base** — universal OS, инфраструктура мышления, методология как объект
- **life** — personal management, Ruslan-жизнь, daily rituals, self-care
- **company** — Jetix-company, consulting, team, sales, юр структура
- **community** — club, network, Secure Network, partners, ICP, archetypes
- **money** — revenue streams, pricing, monetization, финансовые цели
- **relationships** — person-to-person, trust, матчинг, partnerships
- **philosophy** — миссия, 200-year vision, frameworks, metaphors, ценности

Atom может принадлежать multiple dimensions (space-separated или `/`). Например: "Gentleman inside / Predator outside" = `philosophy / community / brand`.

### Status semantics

- `open` — active, не разрешено, не противоречит других
- `resolved` — decision принят (TENSIONS-PRE-RESOLVED covers it)
- `reinforced` — multiple sources подтверждают
- `contradicted` — есть atom которое противоречит (см. relates_to)
- `overridden` — противоречит TENSIONS-PRE-RESOLVED locked decision → не используется для synthesis, но остаётся в registry

---

## Алгоритм извлечения (parallel execution critical)

### Phase 1: Preparation

1. Прочитать `raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md` **целиком**. Это binding baseline.
2. Прочитать `CLAUDE.md` — current config.
3. Inventory всех source файлов:
   - `find wiki/ -name "*.md" | grep -v _templates | grep -v index.md | grep -v log.md` → count
   - List voice-memos artefacts
   - List D6 / D9 / ADR
   - Count total expected extraction work

### Phase 2: Parallel extraction через subagents

**Ты (server CC) можешь и должен запускать subagents через Task tool параллельно — используй agility.** Максимум parallel subagents в одном message: ~10 — запусти 10, дождись, запусти следующие 10.

**Batching strategy:**

| Batch | Source group | Files | Expected atoms | ETA per subagent |
|---|---|---|---|---|
| B1-B6 | wiki/ (split into 6 batches ~45-50 files each) | ~280 | 600-1200 | 30-45 min |
| B7 | RUSLAN-IDEAS-FROM-WIKI-FOR-VISION.md | 1 | 300-400 | 20-30 min |
| B8 | VOICE-MEMOS-STRATEGIC-IDEAS.md | 1 | 300-400 | 30-45 min |
| B9 | VOICE-MEMOS-YEAR-PLAN.md | 1 | 150-200 tasks | 20-30 min |
| B10 | VOICE-MEMOS-MINI-WIKIPEDIA.md + DIGEST + ADDENDUM | 3 | 200-300 | 30-40 min |
| B11 | D6 JETIX-FPF.md | 1 | 200-300 | 40-50 min |
| B12 | D9 + ADR | 2 | 100-200 | 30-40 min |
| B13 | Notion bizmodels (if fetched) | 4 | 50-100 | 20-30 min |

**Total parallel:** 13 batches. Запускай 10 одновременно (первая волна), потом 3 (вторая волна).

### Subagent prompt template (используй для каждого batch)

```
Task: Извлечь atoms из batch source(s).

Input files:
- <list of files>

Critical rules:
1. Читай каждый файл полностью.
2. Для каждого discrete thought / claim / task / concept / etc — создавай atom.
3. Preserve Ruslan voice — direct quotes verbatim где возможно (мат сохраняется в цитатах).
4. Атрибуция ОБЯЗАТЕЛЬНА — каждый atom имеет source (file path + line если возможно + quote block).
5. Assign tentative type из 10 категорий (task / hypothesis / concept / principle / claim / entity / value / bet / tension / metric).
6. Assign dimension(s) из 7 (base / life / company / community / money / relationships / philosophy).
7. Assign tentative phase (now / phase-1 / phase-2 / phase-3 / long-term / any).
8. НЕ dedup в этом subagent — dedup на aggregation layer. Сохраняй всё.
9. НЕ резолви противоречия — только extract. Conflict resolution на aggregation layer.

Output: JSONL strictly valid, one atom per line, без markdown wrappers:
{"id": null, "type": "...", "content": "...", "source": "path:line", "quote": "...", "dimension": "...", "phase": "...", "priority": "...", "status": "open", "tags": [...], "relates_to": [], "note": "..."}

id=null — aggregation layer assign'ит unique IDs.

Tensions pre-resolved (из TENSIONS-PRE-RESOLVED.md) — если atom противоречит одному из 8 decisions, set status: "overridden" и include note о каком decision противоречит.

Expected output size: ~50-200 atoms per batch (varies by source density).
```

### Phase 3: Aggregation

После всех batches — main thread (не subagent):

1. Collect all JSONL outputs (~1500-3000 atoms total)
2. Assign unique IDs (`atom-0001` ... `atom-NNNN` в порядке processing)
3. **Dedup pass** — identify near-duplicates:
   - Similar content (Levenshtein > 0.85 OR semantic similarity)
   - Same source + similar content → merge (keep one, merge provenance)
   - Different source + similar content → keep separate, add `relates_to: reinforces` link
4. **TENSIONS-PRE-RESOLVED override pass** — для каждого atom проверить если conflict'ит с 8 decisions:
   - Если да → `status: "overridden"` + note про какой decision
5. **Cross-reference pass** (критичный для knot-map):
   - Для каждой пары atoms проверить: reinforces / contradicts / depends / variant
   - Populate `relates_to` arrays
   - Contradictions → создать atoms type `tension` которые pointят на оба конфликтующих atoms
6. **Cluster identification** — group atoms по dimension + semantic similarity. Намётить clusters для KNOT-MAP.
7. **Orphan detection** — atoms без relates_to entries. Flag для review.
8. **Gap detection** — dimensions / phases / topics с слабым покрытием (less than 5 atoms на dimension / phase). Flag.

### Phase 4: Generate deliverables

**ATOM-REGISTRY.md** structure:

```markdown
---
id: atom-registry-2026-04-21
title: Atom Registry — Complete Inventory (Stage 1 Untangle)
date: 2026-04-21
type: registry
status: ready
binding: yes — primary source для Stage 3 synthesis (D1/D2/D3)
total_atoms: <N>
sources:
  - wiki/ (~280 files)
  - voice-memos artefacts (6 files)
  - transcripts (~117 files, cross-ref only)
  - D6 / D9 / ADR / CLAUDE.md
  - TENSIONS-PRE-RESOLVED.md (binding overrides)
---

# Atom Registry — Complete Inventory

## 0. Statistics

- Total atoms: N
- Per type: task N | hypothesis N | concept N | ...
- Per dimension: base N | life N | ...
- Per phase: now N | phase-1 N | ...
- Per status: open N | resolved N | overridden N | ...
- Sources coverage: wiki N% | voice-memos N% | D6 N% | ...

## 1. Atoms grouped by dimension

### 1.1 Base (universal OS)
[atom blocks, sorted by type then ID]

### 1.2 Life (personal management)
[...]

### 1.3 Company (Jetix-company)
[...]

### 1.4 Community
[...]

### 1.5 Money
[...]

### 1.6 Relationships
[...]

### 1.7 Philosophy
[...]

## 2. Cross-dimension atoms
[atoms с multiple dimensions]

## 3. Atoms index (alphabetical by ID)
[compact list: atom-XXXX → title → type]

## 4. Provenance index (by source)
[for each source file — list of atom IDs extracted]
```

**KNOT-MAP.md** structure:

```markdown
---
id: knot-map-2026-04-21
title: Knot Map — Tensions, Clusters, Gaps (Stage 1 navigation)
date: 2026-04-21
type: knot-map
status: ready
companion_to: ATOM-REGISTRY.md
---

# Knot Map — Navigation по Atom Registry

## 0. Statistics overview
(same stats + additional: N tensions, N clusters, N orphans, N gap-areas)

## 1. Tensions (contradictions identified)

### 1.1 Tensions resolved в TENSIONS-PRE-RESOLVED (reference only — already LOCKED)
[8 decisions + pointers к atom IDs which are overridden by each]

### 1.2 Remaining tensions (OPEN — для Stage 2)

Группы по dimensions:

#### Dimension: Community
- **Tension T-01:** <name>
  - Atoms в conflict: atom-XXXX vs atom-YYYY
  - Nature: <what's the conflict about>
  - Severity: 🔴 HARD / 🟡 SOFT / 🔵 MINOR
  - Suggested resolution direction: <optional hint>

#### Dimension: Money
[...]

[etc for all dimensions]

## 2. Clusters (groups of related atoms)

### 2.1 Cluster C-01: <name>
- Theme: <natural grouping>
- Member atoms: [atom-XXXX, atom-YYYY, ...]
- Density: N atoms
- Significance: <why cluster matters>

[for all clusters — expected 15-30]

## 3. Gaps (weak coverage areas)

### 3.1 Dimension gaps
- Dimension X has only N atoms — possible under-development.

### 3.2 Phase gaps
- Phase Y has only N atoms — [analysis].

### 3.3 Topic gaps
- Topic Z (mentioned in sources but only N-atom coverage).

### 3.4 Entity gaps
- Entities mentioned but under-developed.

## 4. Orphans (atoms без relates_to)

[list — candidates for manual review: важное или park?]

## 5. Cross-dimension connections

[important atom relations crossing dimensions]

## 6. Recommendations for Stage 2

### 6.1 Priority tensions to resolve
[top 5-10 tensions Ruslan должен обсудить с Cloud Cowork]

### 6.2 Gaps to fill vs park
[for each gap — recommendation fill / park / defer]

### 6.3 Orphans to triage
[which deserve promotion vs parking]
```

### Phase 5: Validation

После генерации обоих документов — self-validation pass:

1. **Count integrity:** total atoms = sum(per-type) = sum(per-dimension) (cross-dim atoms counted once)
2. **ID uniqueness:** no duplicate atom-XXXX
3. **Provenance:** every atom has non-empty source
4. **relates_to integrity:** all referenced IDs exist
5. **Override pass correctness:** every atom противоречащий одному из 8 decisions has status: overridden
6. **No orphan-of-orphans:** если atom-A в orphans, и atom-B relates to atom-A — обновить atom-A's relates_to accordingly

### Phase 6: Commit + push

```bash
git add raw/research/architecture-variants-2026-04-22/ATOM-REGISTRY.md
git add raw/research/architecture-variants-2026-04-22/KNOT-MAP.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[research] Stage 1 untangle complete — Atom Registry + Knot Map (deep variant)"
git push origin claude/jolly-margulis-915d34
```

### Phase 7: Notion update

Обнови Notion page (append-log):
- URL: https://www.notion.so/3492496333bf812e8b62cbc61338ce06
- Append: Stage 1 complete — N atoms, M tensions (X resolved via locked, Y open), K clusters, L gaps
- Link to both files

---

## Critical constraints

- **Size matters:** registry должен быть substantive (5000+ строк). Слишком короткий = не deep enough. Слишком длинный (>15000) = bloat.
- **Voice preservation:** direct quotes from Ruslan verbatim (особенно из voice-memos + wiki harvest). Paraphrasing только если quote слишком long.
- **TENSIONS-PRE-RESOLVED как binding:** 8 decisions OVERRIDE любые conflicting atoms. Это не "opinion" — это закон.
- **Параллелизация обязательна:** если ты делаешь sequential — 15-25 часов. Если параллельно 10 subagents — 3-6 часов. Параллель → **10-15 subagents в первой волне**.
- **No-dedup в subagents:** subagents extract, aggregation dedup'ит. Иначе теряется материал.
- **Traceability:** every atom → source file. Это позволяет D1-D4 writers добавлять citations обратно в raw material.

---

## Budget / ETA

- Prep (read TENSIONS-PRE-RESOLVED + inventory): 10-20 min
- Parallel extraction (10 subagents wave 1): 45-60 min (bound by slowest subagent)
- Parallel extraction (remaining 3 subagents wave 2): 30-45 min
- Aggregation + dedup + cross-ref: 45-90 min
- Generate deliverables: 30-60 min
- Validation: 15-30 min
- Commit + push + Notion: 10 min

**Total ETA:** 3-5 часов с хорошей параллелизацией.

---

## Deliverable (stdout report по завершению)

```
# Stage 1 Untangle Complete — 2026-04-21

## Files
- raw/research/architecture-variants-2026-04-22/ATOM-REGISTRY.md (X lines, Y KB)
- raw/research/architecture-variants-2026-04-22/KNOT-MAP.md (X lines, Y KB)

## Registry stats
- Total atoms: N
- Per type: task N | hypothesis N | concept N | principle N | claim N | entity N | value N | bet N | tension N | metric N
- Per dimension: base N | life N | company N | community N | money N | relationships N | philosophy N
- Per phase: now N | phase-1 N | phase-2 N | phase-3 N | long-term N | any N
- Overridden by TENSIONS-PRE-RESOLVED: N
- Reinforced (multi-source): N

## Knot map
- Tensions (8 pre-resolved locked): 8
- Tensions (remaining open, 🔴 HARD): N
- Tensions (remaining, 🟡 SOFT): N
- Clusters identified: N
- Gaps flagged: N
- Orphans: N

## Source coverage
- Wiki: X/280 files (Y%)
- Voice-memos artefacts: X/6
- Transcripts cross-ref used: yes/no
- D6/D9/ADR: covered yes/no
- Notion bizmodels: fetched yes/no

## Commit
- Hash: abc1234
- Notion updated: yes

## Ready for
- Stage 2 (resolve remaining tensions)
- Stage 3 (synthesize D1/D2/D3 используя registry + KNOT-MAP)
```

---

## Ошибки которых избегать

1. ❌ **Sequential processing** вместо parallel — займёт 15+ часов вместо 3-5.
2. ❌ **Dedup слишком агрессивный** — потеря unique nuances. Dedup conservative.
3. ❌ **Skip provenance** — нельзя! Каждый atom обязан иметь source.
4. ❌ **Interpret переформулировки как собственный contribution** — только extract, не rewrite Ruslan voice.
5. ❌ **Пропустить TENSIONS-PRE-RESOLVED** как binding — тогда registry будет inconsistent с 8 decisions.
6. ❌ **Написать registry без KNOT-MAP** — KNOT-MAP is navigation, без него registry не usable.
7. ❌ **Skip Notion update** — Ruslan tracks progress через Notion.

---

## После завершения

Ruslan review:
1. Прочитает KNOT-MAP полностью (~500-1500 строк — 20-40 мин)
2. Выборочно посмотрит ATOM-REGISTRY (dip into specific dimensions)
3. Решит — готово для Stage 2 (resolve remaining tensions) или нужны tweaks

**Не block**ируй на review — просто commit + push + notify through stdout summary. Ruslan сам откроет когда готов.
