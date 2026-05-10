---
title: Wiki Integration Redesign — Phase 1 Plan
type: brigadier-plan
created: 2026-05-10
phase: 1-of-2 (planning)
phase_2_status: awaiting-ack
phase_3_status: awaiting-bulk-ack-after-phase-2 (third gate)
branch: claude/voice-pipeline-2026-05-10
input_test_set: reports/voice-pipeline-2026-05-10/04-wiki-candidates.md (1285 candidates, 0% match)
F: F4
G: wiki-integration-redesign
R: refuted_if_match_rate_remains_zero_OR_silent_wiki_writes_OR_existing_entries_modified
constitutional_anchor:
  - Tier 2 Rule 1 (no AI strategizing — matching + proposing only)
  - Tier 2 Rule 2 (no architectural changes без gate — wiki writes pending Ruslan ack каждый candidate)
  - Tier 2 Rule 6 (provenance per candidate)
  - Append-only (existing wiki/ entries untouched — match-to-existing → edge-only cross-reference)
  - Default-Deny 3-gate (plan ack → execute redesign → bulk-ack candidates → write wiki/)
source_brief: prompts/server-cc-wiki-integration-redesign-2026-05-10.md
---

# Wiki Integration Redesign — Phase 1 Plan

> **Status.** Phase 1 design complete. Awaiting Ruslan ack on this PLAN.md → fires Phase 2.
>
> **Source brief.** `prompts/server-cc-wiki-integration-redesign-2026-05-10.md`
>
> **Branch.** `claude/voice-pipeline-2026-05-10` (continues from voice-pipeline Phase 2 commit a8a3808; NOT main, NOT tagged).
>
> **Constitutional posture.** Three-gate workflow per Default-Deny: (1) ack PLAN.md → write Phase 2 deliverables; (2) ack Phase 2 → no wiki/ writes still — only the bulk-ack-ready candidate doc + tooling; (3) ack tier-by-tier in `/wiki-bulk-ack` → actual writes to `wiki/`. Existing wiki entries NEVER modified — match-to-existing means edge-only cross-reference.

---

## §0 Context

**Problem.** Voice pipeline Phase 2 Stage 5 (Wiki candidates) shipped on 2026-05-10 with **0% match-to-existing rate** (0/1285). All 1285 voice candidates classified as `propose-new`. Self-eval recorded this as legitimate FAIL per `07-discipline-log.md` (Stage 5 verdict = `PARTIAL`; quality criterion "Wiki candidates ≥30% match-to-existing" → FAIL).

**Why redesign matters.** Without working match-to-existing:
- Future voice runs flood `04-wiki-candidates.md` with 100% propose-new noise
- Ruslan can't bulk-ack — has to manually review every candidate
- Real `wiki/` entries that conceptually overlap with voice items (jetix-tagged content, engineering-faith, founder-isolation, etc.) get duplicated as new propose-new
- Wiki ingestion stalls; voice items don't compound into structured knowledge

**Goal.** Redesign Stage 5 + build a **reusable wiki-integration workflow** so:
1. Future voice runs find real match-to-existing for items in wiki (esp. on full entry bodies, not just titles)
2. Ruslan acks 1000+ candidates batch-style via 3-tier workflow (single bulk-ack for high-confidence)
3. Auto-merge mechanics for approved candidates → real wiki/ writes via append-only edges + new entries
4. Existing entries stay untouched (no blind edits — append-only invariant)
5. Cross-reference voice memos ↔ wiki entries via typed edges

---

## §1 P.1 — Diagnosis: Why Stage 5 failed (0% match)

### §1.1 Algorithm reverse-engineered

`tools/voice-pipeline-orchestrator.py:444-598` — `stage_5_wiki_candidates()`:

```python
# Build wiki list: parse wiki/index.md link references
for m in re.finditer(r"\[([^\]]+)\]\(([^\)]+\.md)\)", idx_content):
    wiki_pages.append(f"{m.group(1)} :: {m.group(2)}")  # "Title :: path/to/page.md"

# For each filtered voice item:
for item in items:
    if item.category == "nothing-extractable" or len(content) < 20: continue
    if frequency < 2 and len(content) < 50: continue

    content_tokens = set(re.findall(r"\w{4,}", content.lower()))
    best_match = None
    best_score = 0.0
    for page in wiki_pages:
        page_tokens = set(re.findall(r"\w{4,}", page.lower()))
        overlap = content_tokens & page_tokens
        score = len(overlap) / max(len(page_tokens), 1)  # ⚠️ denominator = page tokens
        if score > best_score:
            best_score = score
            best_match = page

    decision = "match-to-existing" if best_score >= 0.7 else "propose-new"
```

**Heuristic shape:** Token-overlap Jaccard variant (intersection / page_tokens), threshold 0.7, on lowercased text from `wiki/index.md` link entries only.

### §1.2 Three failure modes (heuristic-level: ~15% of total)

**F.1 — Title-only matching (no entry bodies seen).**
The matcher reads `wiki/index.md` (a 207-line catalog of `[Title](path.md)` links). It NEVER opens `wiki/concepts/<slug>.md` or any entry body. So a wiki concept like `wiki/concepts/founder-isolation-as-stopper-class.md` (3.6 KB body with 500+ words on the topic) is matched only by its 8-12 token title. Voice items whose content overlaps with the *body* but not with the *title's surface words* score near zero.

**F.2 — No Russian morphology.**
Russian inflects heavily. Voice item says "мастера" (genitive plural of "мастер" — master); wiki page says "мастерская" (workshop, derived from same root). Token comparison treats these as DIFFERENT tokens. Same for "клиент" / "клиенты" / "клиента", "синергия" / "синергии", "система" / "систему" / "системой". Russian needs at least suffix-stripping for case/number/gender, ideally lemmatization.

**F.3 — Threshold/denominator math.**
`score = overlap / page_tokens`. Average wiki page title has ~8 tokens after `\w{4,}` filter. To clear 0.7, need 6+ overlapping tokens. Voice item content has ~50-300 chars (~15-50 tokens after filter), but only a few of those will match a generic title. Concrete example:

> Voice item #1 (lens-actionables): "«Мастерская» как геймифицированная Life OS по модели Torn: трекинг реальных ресурсов (время, информация, мозги, бизнес) с модификациями под разные стили жизни (спортсмен, аскет, предприниматель и т.д.) — тысячи вариантов кастомизации."
> Tokens after `\w{4,}` filter: ~30 unique
>
> Wiki page candidate: "Engineering faith :: concepts/engineering-faith.md"
> Tokens: 4 (engineering, faith, concepts, engineering-faith)
> Overlap: 0
> Score: 0 / 4 = **0.0** (FAIL 0.7)

Even a "perfect" semantic match in this scheme would need a wiki page title that contained 6+ of the voice item's specific tokens — extremely rare for short titles.

### §1.3 Architectural gap (~85% of total)

**The 1273 freq=1 voice items are tactical single-mention thoughts. The 552 wiki entries are consensus-curated strategic knowledge.** This is a category mismatch — voice candidates are mostly NOT supposed to find wiki matches because the topics aren't yet wiki entries.

Concrete grep evidence:
- `мастерская|workshop` → 0 wiki entries → legitimate propose-new (workshop concept exists only as voice-mention idea, no wiki page yet)
- `tseren|цэрэн|levenchuk|левенчук` → 0 (CRM is at `crm/`, not `wiki/` — wiki/index.md explicitly excludes CRM contacts)
- `trm|foundation v1` → 0 wiki entries — propose-new is correct
- `synergy|синергия` → 3 sparse mentions
- BUT: `jetix` → 119 files (21% of wiki) — there IS a strong matching surface for jetix-anchored voice items. These are the items where the heuristic SHOULD have hit but failed due to F.1/F.2/F.3.

### §1.4 Verdict

| Cause | % of failure |
|---|---|
| F.1 Title-only matching | ~5% |
| F.2 Russian morphology | ~5% |
| F.3 Threshold/denominator math | ~5% |
| F.4 Architectural gap (no wiki entry exists for the concept) | ~85% |

**Implication for redesign:** Even a perfect Stage 5 would yield maybe 15-30% match rate against current wiki. To hit ≥30% target, BOTH the heuristic must improve (read bodies, handle Russian, sane scoring) AND wiki must continue to grow (Phase 3 bulk-ack creates new entries → next run has more matching surface).

---

## §2 P.2 — New approach for match-to-existing

### §2.1 Five alternatives compared

| # | Approach | Pros | Cons | Recommend? |
|---|---|---|---|---|
| 1 | Embedding cosine via Claude embeddings API | Semantic robust to paraphrase; handles Russian morphology natively | Cost: 1 embedding API call per voice candidate + per wiki entry; setup complexity; needs vector store | NO — overkill for first iteration; deferred to v3 if hybrid proves insufficient |
| 2 | Pure keyword + TF-IDF on full bodies | Fast, no API, works offline; reads full entry bodies (fixes F.1) | Misses synonyms; Russian stems still weak unless pre-processed; threshold tuning needed | PARTIAL (Tier 1 pre-filter only) |
| 3 | LLM-pass: Claude Sonnet rates each candidate vs each wiki entry | Highest semantic quality | 1285 candidates × 552 entries × 30s ≈ years. Even with top-K filter: 1285 × 1 call × 30s ≈ 10 hours. TOO SLOW for batch run | NO — alone |
| 4 | **Hybrid: BM25 pre-filter (top-K) → LLM batched rank (top-K)** ⭐ | Balance speed + quality; reuses existing infra; Russian-aware via normalizer; handles paraphrase via LLM | Multi-stage; ~25-40 min total LLM time at batched 10 items/call | **YES** ⭐ |
| 5 | Reuse `/ingest` skill per candidate | Reuses tooling; consistent | Skills designed for single-source ingest, not batch matching; wrong granularity | NO — wrong tool |

### §2.2 Recommended: Approach #4 — Hybrid Stage 5

```
Stage 5.1 (cheap pre-filter, no LLM):
  ─── Build inverted index over FULL wiki entry bodies (not just titles) ───
  Walk wiki/{concepts,entities,sources,topics,ideas,experiments,claims,summaries,foundations}/
  For each entry: read frontmatter + body → russian_normalize(text) → extract tokens
  Store: { token: [(entry_path, term_freq), ...] }, plus doc_lengths and idf

  ─── Russian-aware tokenization ───
  - lowercase
  - Cyrillic + Latin word chars only
  - suffix-strip on Cyrillic: -ого/-ому/-ый/-ая/-ое/-ой/-ыми/-ах/-ом/-ами/-ы/-и/-я/-ю
  - stopwords removed (и, в, на, для, с, при, как, что, от, по, до, из, etc.)
  - min_len = 3

  ─── BM25 score per voice-candidate × wiki-entry ───
  k1=1.5, b=0.75 (defaults)
  Retain top-K=10 wiki candidates per voice item
  Skip voice items where top-1 BM25 score < 1.0 (no plausible match → straight to Tier C propose-new)

Stage 5.2 (LLM batched rank):
  Group voice items into batches of 8-12 (those that passed BM25 pre-filter)
  Per batch, single Claude Sonnet call via tools/lib/cc_helper.claude_call:
    Input JSON: {
      "voice_items": [{"id": N, "content": "...", "category": "..."}],
      "wiki_candidates_per_item": {N: [{"path": "...", "title": "...", "snippet": "..."}, ...]}
    }
    System prompt: "For each voice item, identify which (if any) wiki entry is the SAME concept.
                    Score 0.0 (different concept) to 1.0 (literal match).
                    Output JSON: [{id, best_match: path|null, score, rationale}]"
  Aggregate results

Stage 5.3 (3-tier categorization):
  Tier A: score ≥ 0.85          → auto-merge after Ruslan single bulk-ack
  Tier B: 0.60 ≤ score < 0.85   → batch review; Ruslan acks subset
  Tier C: score < 0.60 OR null  → propose-new OR defer to backlog
```

### §2.3 Cost estimate

- 1285 candidates → BM25 pre-filter ≈ 40% pass (≈500 items have non-trivial top-1 score)
- 500 items → 50 LLM batches × ~30s each = **~25 min total LLM time**
- BM25 indexing on 552 wiki entries: <5 sec (one-time per run)
- Total Stage 5 v2 runtime: **30-40 min** (vs current Stage 5 v1 = 1 sec)
- All LLM calls via `cc_helper.claude_call` → Max sub headless (no API key cost per `feedback_no_api_keys.md`)

---

## §3 P.3 — New approach for propose-new

Tier-C handler (executes per-candidate during Stage 5.3):

### §3.1 Entity type mapping

Extends current orchestrator's `cat_to_entity` dict:

| Voice category (extract.py 12-cat schema) | Wiki entity type |
|---|---|
| `Идеи` / `Идеи для проектов` | `wiki/ideas/` |
| `Концепции` (если будет) | `wiki/concepts/` |
| `Стратегические гипотезы` / `Принципы` / `Инсайты` / `Решения` | `wiki/claims/` |
| `Личные наблюдения` | `wiki/claims/` (with `niche: life`) |
| `Ресурсы` | `wiki/sources/` |
| `Открытые вопросы` / `Видение` | `wiki/topics/` |
| `Контакты` | **SKIP** → route to `crm/` via existing `/crm-add` flow (NOT wiki/) |
| `Задачи` | **SKIP** (operational, not knowledge) |

### §3.2 Slug generation

- Take voice item content[:60], lowercase, kebab-case (replace non-`a-z0-9` with `-`)
- Collision check vs filesystem: if `wiki/<type>/<slug>.md` exists, suffix `-2`, `-3`, etc.
- Russian content: transliterate first via simple table (а→a, б→b, в→v, etc.) before kebab-case

### §3.3 Template auto-fill

Read `wiki/_templates/<type>.md` (idea.md / concept.md / claim.md / source.md / topic.md / etc.) — each has frontmatter schema. Auto-fill via Claude Sonnet single call (one per Tier-C item, batched 10 at a time):

```yaml
---
title: <Claude-generated 1-line summary from content>
type: <ideas|concepts|claims|sources|topics>
niche: <inferred from voice category + lens config>
status: raw           # voice items always start unevaluated
sources:
  - voice/<memo_stem>
related: []           # filled later via /build-graph
tags:
  - voice-extracted
  - <category-derived>
  - <lens-tier-1-keyword-hits if any>
topics: []            # may be filled if lens has topic anchors
created: 2026-05-10
updated: 2026-05-10
confidence: low       # single-memo origin → low default
pipeline: voice-extracted
voice_provenance:
  - memo: audio_NNN@DD-MM-YYYY_HH-MM-SS
    transcript_path: raw/transcripts/audio_NNN@...txt
    line: L<#>
    score: <BM25 if available>
    extracted: 2026-05-10
---

# <title>

<one-line gist from Claude>

> "<verbatim quote from transcript line>"

## Suggested next step
<Claude-generated 1-line action OR placeholder>
```

### §3.4 Validation gate

Before write:
- All mandatory frontmatter fields present (title, type, niche, status, sources, created, pipeline, voice_provenance)
- F-G-R schema check (per Part 6a) — for claims: `F`, `G`, `R` fields populated
- Slug not in wiki/.gitignore exclusions
- No collision with existing file (re-suffix if needed)
- Body non-empty

If validation FAIL → reject candidate, move to backlog with reason in 04-wiki-candidates-v2.md §D.

---

## §4 P.4 — Bulk-ack workflow (3 tiers)

### §4.1 Output structure

`reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.md`:

```markdown
---
title: Wiki Candidates v2 — 3-tier categorized
type: pipeline-output-candidates
created: 2026-05-10
total_candidates: <N>
tier_a_count: <N>
tier_b_count: <N>
tier_c_count: <N>
skipped_count: <N>
---

# §A — Tier A: High-confidence match-to-existing (≥0.85)

> **N items.** These are voice items that match an existing wiki entry with score ≥0.85. Approval = create cross-reference edge in wiki/graph/edges.jsonl + log entry. Existing wiki entry **NOT modified**.
>
> **Bulk-ack command:** `/wiki-bulk-ack --tier A` (with confirm prompt)

| # | Voice item (preview) | → Wiki entry | Score | Memo refs |
|---|---|---|---|---|
| 1 | ... | `concepts/founder-isolation-as-stopper-class.md` | 0.92 | audio_587:L12 |
| 2 | ... | ... | ... | ... |

# §B — Tier B: Medium-confidence match-to-existing (0.60-0.85)

> **N items.** Match plausible but not certain. Ruslan reviews + acks subset.
>
> **Bulk-ack command:** `/wiki-bulk-ack --tier B --select 1,3,5,7-10` (subset)

| # | [✓] | Voice item (preview) | → Wiki entry | Score | Rationale | Memo refs |
|---|---|---|---|---|---|---|
| 1 | [ ] | ... | ... | 0.78 | "shares core concept of X" | audio_588:L4 |

# §C — Tier C: Propose-new entries (<0.60 OR no match)

## §C.1 — High-frequency (freq ≥3) — strong propose-new candidates

| # | Voice content | Proposed type/slug | Frequency | Memos |
|---|---|---|---|---|

## §C.2 — Medium-frequency (freq 2)

## §C.3 — Single-mention (freq 1) — backlog stub list

> **Bulk-ack command:**
> - `/wiki-bulk-ack --tier C --select N,N,N --as-new` (creates new wiki entries)
> - `/wiki-bulk-ack --defer-backlog N,N,N` (parks in backlog only)

# §D — Skipped (CRM contacts, tasks, low-quality)

> Reason listed per item; no action expected. CRM contacts → use `/crm-add` separately.

| # | Reason | Item preview |
|---|---|---|
| 1 | Контакты — route to crm/ | "Анатолий Левенчук, ШСМ" |
```

### §4.2 New skill `.claude/skills/wiki-bulk-ack/skill.md`

CC slash-command. Commands:

| Command | Effect |
|---|---|
| `/wiki-bulk-ack --tier A` | Show count + sample 5 → confirm prompt → execute auto-merge for all Tier A |
| `/wiki-bulk-ack --tier A --dry-run` | Preview merge actions without writing (recommended for first invocation) |
| `/wiki-bulk-ack --tier B --select 1,3,5,7-10` | Auto-merge for selected indices |
| `/wiki-bulk-ack --tier C --select N,M,P --as-new` | Create new wiki entries for selected Tier C items |
| `/wiki-bulk-ack --reject <indices> --reason="<why>"` | Park in backlog (no wiki write) |
| `/wiki-bulk-ack --defer-backlog <indices>` | Move to backlog deferred queue |
| `/wiki-bulk-status` | Show review queue counts + pending state |

Skill implementation: bash + python wrapper invoking `tools/wiki-integration/auto_merger.py`.

---

## §5 P.5 — Auto-merge mechanics

### §5.1 Tier A — match-to-existing approved

**Append-only invariant:** existing wiki entry frontmatter and body are NEVER modified. Voice item creates a cross-reference via edges + log only.

For each approved Tier A candidate:
1. **Append edge** to `wiki/graph/edges.jsonl`:
   ```json
   {"from": "voice/audio_NNN@DD-MM-YYYY_HH-MM-SS", "to": "concepts/<slug>.md", "type": "mentions", "created": "2026-05-10", "confidence": "high", "voice_score": 0.92}
   ```
   Predicate `mentions` (added to 12-enum if not present, with constitutional approval as part of P.5 scope).
2. **Append entry** to `wiki/log.md`:
   ```
   [2026-05-10] [voice-bulk-ack] match-to-existing Tier A: audio_NNN linked to concepts/<slug>.md (score=0.92)
   ```
3. Voice item itself is **NOT promoted to a wiki entry** — it's just a cross-reference. The link survives in edges.jsonl + log.md.

### §5.2 Tier C — propose-new approved

For each approved Tier C candidate:
1. **Create new file** `wiki/<type>/<slug>.md` from template (per §3.3).
2. **Append entry to `wiki/index.md`** under the correct section. Use sentinel-aware insert:
   - Find section header (e.g., `## Ideas`)
   - Insert new bullet `- [<title>](<type>/<slug>.md) — <one-line summary> [niche: <niche>]` before next section header
   - Preserve hand-curated formatting
3. **Append `wiki/log.md`**:
   ```
   [2026-05-10] [voice-bulk-ack] new entry Tier C: wiki/<type>/<slug>.md (from audio_NNN)
   ```
4. **Append edges to edges.jsonl**:
   - `voice → new_entry` (predicate `derived_from`, confidence `low`)
   - `new_entry → top-K BM25 neighbors` (predicate `related_to`, confidence `low`) — these are inferred from Stage 5.1 BM25 prefilter output

### §5.3 Tier B — same as Tier A (match-to-existing edge-only)

Tier B follows Tier A mechanics for selected items. Non-selected items move to backlog.

### §5.4 Post-batch integrity

After every bulk-ack batch (A, B, or C):
1. Run `wiki/graph/build_graph.py lint` → validates new edges target existing files
2. Run `/lint` skill on wiki/ → catches dangling-edge / orphan-concept / missing-frontmatter
3. If integrity check FAILS → halt subsequent batches, log error to `reports/wiki-integration-redesign-2026-05-10/discipline-log.md`, surface to Ruslan
4. **No automatic rollback** (append-only invariant — corrections via subsequent edits, not git revert)

---

## §6 P.6 — Reusable orchestrator integration

### §6.1 Stage 5 replacement in `tools/voice-pipeline-orchestrator.py`

Function signature unchanged (orchestrator API stable):
```python
def stage_5_wiki_candidates(
    filtered_data: Dict[str, Any],
    output_dir: Path,
    log: DisciplineLog,
) -> Dict[str, Any]:
```

Internals replaced with Hybrid Stage 5 (§2.2). Orchestrator imports new helpers from `tools/wiki-integration/`.

### §6.2 New helper modules — `tools/wiki-integration/`

```
tools/wiki-integration/
├── __init__.py
├── wiki_index_loader.py     — loads full wiki entry bodies (NOT just index.md), builds inverted index
├── russian_normalizer.py    — lowercase + suffix-strip + stopwords + min_len=3 tokenization
├── bm25_matcher.py          — BM25 ranker (k1=1.5, b=0.75) using russian_normalizer
├── llm_ranker.py            — batched Claude Sonnet calls via cc_helper for top-K rank (Stage 5.2)
├── template_filler.py       — auto-fills wiki/_templates/<type>.md from voice item (Stage 5.3 Tier C)
├── edge_writer.py           — appends typed edges to wiki/graph/edges.jsonl (idempotent)
├── index_log_appender.py    — updates wiki/index.md + wiki/log.md (append-only, sentinel-aware)
└── auto_merger.py           — orchestrates merge for approved candidates (called by /wiki-bulk-ack)
```

Each module: ≤200 LoC, single responsibility, has 1+ smoke test in module-level `if __name__ == "__main__":` block.

### §6.3 Lens config extension

Backward-compatible additions to YAML lens configs (per `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md` §4):

```yaml
# Optional — Wiki integration tuning (defaults applied if absent)
wiki_match_threshold_high: 0.85       # Tier A boundary
wiki_match_threshold_medium: 0.60     # Tier B/C boundary
wiki_match_top_k_prefilter: 10        # BM25 retain count per voice item
wiki_match_skip_below_bm25: 1.0       # skip voice items with top-1 BM25 below this (→ Tier C)
wiki_propose_new_min_frequency: 1     # min freq to propose new entry (1 = all)
wiki_lens_keyword_boost: 0.10         # +score for items containing lens Tier-1 keywords
                                      # AND matching wiki entries containing same keywords
```

Future runs automatically pick up updated Stage 5 — no orchestrator code change needed once landed.

---

## §7 P.7 — Quality criteria for Phase 2 self-evaluation

End-of-Phase-2 verdict in `reports/wiki-integration-redesign-2026-05-10/discipline-log.md`:

| # | Criterion | Pass condition |
|---|---|---|
| 1 | New Stage 5 re-run on existing 1285 candidates | match rate ≥ 30% Tier A+B combined |
| 2 | Match-rate-comparison report | `match-rate-comparison.md` shows old 0% vs new X% with 5+ example improvements |
| 3 | Tier C frontmatter validation | All Tier-C propose-new candidates have valid frontmatter per template schema |
| 4 | Bulk-ack `--dry-run` mode | Tested on Tier A subset; verifies merge logic without writing |
| 5 | wiki/ untouched in Phase 2 | `git diff --stat origin/main -- 'wiki/**'` zero changes after Phase 2 commit |
| 6 | Helper modules quality | All 8 `tools/wiki-integration/` modules have docstrings + 1+ smoke test |
| 7 | Phase 2 deliverables present | `04-wiki-candidates-v2.md` + `match-rate-comparison.md` + `discipline-log.md` + skill doc all exist |
| 8 | Skill discoverable | `.claude/skills/wiki-bulk-ack/skill.md` documented with command reference + examples |
| 9 | Honest fail tags | If match rate < 30% on real data, log explicit FAIL + diagnosis (no glossing) |

---

## §8 P.8 — Constitutional cross-check

| Anchor | Application | Compliance plan |
|---|---|---|
| **Tier 2 R1** (no AI strategizing) | Heuristic = matching + proposing. Ruslan = sole decider what becomes wiki entry. Pipeline NEVER auto-decides "this should be a wiki entry". | ✅ All decisions surfaced in 04-wiki-candidates-v2.md for explicit ack |
| **Tier 2 R2** (no architectural changes без gate) | 3-gate: plan ack → Phase 2 execute ack → bulk-ack candidates ack → wiki/ writes | ✅ Phase 2 produces NO wiki/ writes; only the candidate doc + skills/tooling |
| **Tier 2 R6** (provenance per claim) | Every Tier A/B/C item has voice_provenance: [memo, line, transcript_path] | ✅ Frontmatter enforced via template_filler.py validation |
| **Append-only** | Existing wiki/ entries untouched (no body or frontmatter edits). Match-to-existing → edge-only. New entries are append. | ✅ edge_writer + new-entry creation only; no `git checkout` of existing |
| **Default-Deny** | wiki/ untouched until bulk-ack. CRM contacts NOT auto-promoted. Tasks NOT promoted. | ✅ §D Skipped category in 04-v2 |
| **No API keys** (per `feedback_no_api_keys.md`) | All LLM calls via `cc_helper.claude_call` → Max sub headless | ✅ Reuses existing pattern |

---

## §9 P.9 — Open questions for Ruslan

Defaults shown — Ruslan can override individual items in ack message, or just say "all defaults".

### §9.1 Match threshold tier boundaries?
- **Default.** A ≥ 0.85, B 0.60-0.85, C < 0.60
- **Alternatives.** Stricter (A ≥ 0.90 / B 0.70-0.90) → fewer auto-merges, more manual review. Looser (A ≥ 0.75 / B 0.50-0.75) → more auto-merges, more risk
- **Trade.** Default balances safety (Tier A high bar) with throughput (Tier B catches mid-confidence)

### §9.2 Auto-merge on Tier A — yes by default or dry-run-first?
- **Default.** Dry-run-first on first invocation. `/wiki-bulk-ack --tier A --dry-run` shows preview; explicit second call without `--dry-run` writes
- **Alternative.** Auto-merge on first call (faster but less safe for first ever bulk-ack run)
- **Trade.** Default is safer for Phase 2's first deployment

### §9.3 Re-process existing 1285 candidates with new heuristic?
- **Default.** YES, primary Phase 2 deliverable. Re-runs Stage 5 v2 against existing extractions
- **Alternative.** No, only future runs use new heuristic — but then no test of new approach on real data
- **⚠️ Note.** `_filtered-annotated.json` was deleted at Phase 2 voice commit (large file). Phase 2 wiki integration will need to either (a) regenerate from `inbox/processed/filtered/batch_2026-05-10.json` (still present) + frequency annotation logic, or (b) re-run filter.py. Default plan: option (a) — regenerate annotated form from existing batch + extractions

### §9.4 Bulk-ack format — single command with confirm-prompt?
- **Default.** Single command + confirm-step. CC asks "OK to merge N items?" before executing
- **Alternative.** Zero-confirm (faster but riskier); or per-tier interactive numbered prompt
- **Trade.** Default is safe + fast for batch operations

### §9.5 Update workflow for existing wiki entries?
- **Default.** SKIP in this redesign — match-to-existing means edge-only (cross-reference). Existing entry untouched. Update flow deferred to separate cycle (would need its own gate design)
- **Alternative.** Allow `voice_provenance` field append on existing entries (slight frontmatter mod) — but breaks strict append-only invariant
- **Trade.** Default preserves append-only purity; updates handled by future "wiki-update workflow" cycle

### §9.6 Wiki schema enforcement — strict or lenient?
- **Default.** STRICT for new entries (reject if mandatory fields missing per `wiki/_templates/<type>.md` schema); auto-fill best-effort then validate
- **Alternative.** Lenient (write entry even with gaps, mark `pipeline: incomplete` for later fixup)
- **Trade.** Default keeps wiki schema clean; lenient is faster but creates tech debt

### §9.7 Future runs — lens-driven match priority?
- **Default.** YES, lens config can override match thresholds + add Tier-1 keyword boosters. Items containing lens Tier-1 keywords get +0.10 score bonus when matching wiki entries that ALSO contain those keywords
- **Alternative.** Lens-agnostic matching (more deterministic, easier to reason about; less topical sharpness)
- **Trade.** Default makes Stage 5 lens-aware (consistent with Stage 6); alternative is simpler but less context-sensitive

---

## §10 Phase 2 execution flow (after ack)

For reference — exact ops Phase 2 will perform:

1. Build `tools/wiki-integration/` 8 modules with smoke tests
2. Replace `stage_5_wiki_candidates` in `tools/voice-pipeline-orchestrator.py` with Hybrid Stage 5
3. Build `.claude/skills/wiki-bulk-ack/skill.md` + supporting Python via `auto_merger.py`
4. Re-run new Stage 5 on existing 1285 candidates from voice-pipeline-2026-05-10:
   - Regenerate `_filtered-annotated.json` from `inbox/processed/filtered/batch_2026-05-10.json` + extractions
   - Build inverted index over wiki/ entry bodies
   - Run BM25 pre-filter + LLM batched rank
   - Output `reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.md`
5. Write `reports/wiki-integration-redesign-2026-05-10/match-rate-comparison.md`
6. Self-eval against §7 criteria → write `reports/wiki-integration-redesign-2026-05-10/discipline-log.md`
7. `git add tools/wiki-integration/ tools/voice-pipeline-orchestrator.py reports/wiki-integration-redesign-2026-05-10/ reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.md .claude/skills/wiki-bulk-ack/`
8. `git commit -m "[wiki-integration] Phase 2 execute — new Stage 5 heuristic + bulk-ack workflow + reusable orchestrator (Ruslan ack pending merge + bulk wiki ack)"`
9. `git push origin claude/voice-pipeline-2026-05-10`
10. **Signal Ruslan** with branch + commit SHA + new match rate + 3-tier counts + ready-for-bulk-ack
11. **STOP** — do NOT push to main, do NOT tag, do NOT execute bulk-ack (third gate awaits Ruslan)

---

## §11 Critical files referenced

### Read for context (Phase 2)
- `tools/voice-pipeline-orchestrator.py:444-598` — Stage 5 to replace
- `wiki/index.md` (207 lines), `wiki/log.md` (136 lines), `wiki/graph/edges.jsonl` (577 edges)
- `wiki/_templates/*.md` (9 templates: idea, concept, claim, source, entity, experiment, foundation, summary, topic)
- `wiki/concepts/`, `wiki/ideas/`, `wiki/sources/`, `wiki/claims/`, `wiki/entities/`, `wiki/topics/` — full bodies (NOT just titles!) for new BM25 indexing
- `tools/lib/cc_helper.py:47-74` — `claude_call(system, user, model="claude-sonnet-4-6", expect_json=True)`
- `.claude/skills/consolidate/skill.md:42-60` — dedup logic to extract
- `.claude/skills/ingest/skill.md:106-110` — match pattern to mirror
- `tools/community-detect.py` — reuse for Tier-B ranking (semantic neighborhoods)
- `wiki/graph/build_graph.py` — reuse `lint` subcommand post-merge integrity
- `reports/voice-pipeline-2026-05-10/04-wiki-candidates.md` — existing 1285 candidates (Phase 2 re-run input test set)
- `inbox/processed/filtered/batch_2026-05-10.json` — source for regenerating `_filtered-annotated.json`
- `inbox/processed/extractions/audio_587-633*.json` — voice item provenance trail

### Write (Phase 2 only, after ack)
- `tools/wiki-integration/` — 8 helper modules (P.6)
- `tools/voice-pipeline-orchestrator.py` — Stage 5 internals replaced (signature unchanged)
- `.claude/skills/wiki-bulk-ack/skill.md` — new skill + supporting Python
- `reports/wiki-integration-redesign-2026-05-10/` — `discipline-log.md`, `match-rate-comparison.md`
- `reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.md` — re-run output (3-tier categorized)

### Files NOT to touch (any phase)
- `wiki/concepts/`, `wiki/ideas/`, `wiki/sources/`, etc. — Phase 2 produces NO wiki/ writes (third gate)
- `wiki/_templates/` — read-only references
- Existing `reports/review_2026-05-01-*.md` / `2026-04-*.md` — append-only history
- `tools/transcribe.py` / `extract.py` / `filter.py` — out of scope (Phase 2 voice pipeline already shipped)
- `main` branch
- `decisions/` (LOCKED canonical)

---

## §12 Verification (Phase 2 success tests)

Post-Phase-2, BEFORE bulk-ack — Ruslan can run:

```bash
# 1. New Stage 5 re-run produced 04-wiki-candidates-v2.md
ls -la reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.md
wc -l reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.md
# Expect ≤30 KB (slightly larger than v1 due to 3-tier sectioning + scores)

# 2. Match rate comparison
cat reports/wiki-integration-redesign-2026-05-10/match-rate-comparison.md
# Expect old 0% vs new ≥30% Tier A+B combined

# 3. 3-tier counts
grep -c '^# §A' reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.md  # 1
grep -c '^# §B' reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.md  # 1
grep -c '^# §C' reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.md  # 1
grep -c '^# §D' reports/voice-pipeline-2026-05-10/04-wiki-candidates-v2.md  # 1

# 4. Discipline log self-eval verdict
cat reports/wiki-integration-redesign-2026-05-10/discipline-log.md | head -60
# Expect 9-criterion verdict block

# 5. wiki/ untouched in Phase 2
git diff --stat origin/main -- 'wiki/**'
# Expect empty (no writes yet — third gate awaits)

# 6. New skill discoverable
ls .claude/skills/wiki-bulk-ack/skill.md

# 7. Helper modules
ls tools/wiki-integration/
# Expect: __init__.py, wiki_index_loader.py, russian_normalizer.py, bm25_matcher.py,
#         llm_ranker.py, template_filler.py, edge_writer.py, index_log_appender.py, auto_merger.py

# 8. Dry-run bulk-ack
/wiki-bulk-ack --tier A --dry-run
# Expect: preview of N Tier A items, edges that would be appended, log entries that would be written
# NO actual writes
```

THEN, after Ruslan reviews + acks tiers in `/wiki-bulk-ack`, the actual wiki/ writes happen (third gate).

---

## §13 What this plan does NOT do

- Phase 2 execution itself (deferred until ack of this PLAN.md)
- Any wiki/ writes (deferred to bulk-ack — third gate)
- Modifications to existing wiki entries (out of scope; separate "update flow" deferred to future cycle per §9.5 default)
- Modifications to `transcribe.py / extract.py / filter.py` (out of scope per brief §3)
- Embedding-based matching (Approach #1 deferred to v3 if BM25+LLM hybrid proves insufficient)
- Auto-promotion of `Контакты` (CRM contacts) — explicitly skipped, route to `crm/` via existing `/crm-add` flow
- Auto-promotion of `Задачи` (operational tasks) — explicitly skipped, not knowledge
- Bulk-ack workflow for *updating* existing wiki entries (separate gate design needed; deferred to future cycle)
- Push to main, tag creation, third-party API key calls

---

## §14 Awaiting Ruslan ack

- **Ack format.** "ack — execute redesign" + (optional) per-question overrides for §9.1-§9.7, or "all defaults"
- **Channel.** Cloud cowork bridge (this chat)
- **Then.** Phase 2 fires autonomously (~1.5-3h). Final signal post-Phase 2 with branch + SHA + new match rate + 3-tier counts + ready-for-bulk-ack.
- **No ack = no Phase 2.** Halt-Log-Alert if any agent attempts.
- **Bulk-ack itself = third gate.** After Phase 2 lands and Ruslan reviews `04-wiki-candidates-v2.md`, separate per-tier ack invokes `/wiki-bulk-ack` → THEN actual wiki/ writes.

**Brigadier signature.** Acting_as `wiki-integration-redesign-orchestration-role`. F4 / G wiki-integration-redesign / R refuted_if_match_rate_remains_zero_OR_silent_wiki_writes_OR_existing_entries_modified.
