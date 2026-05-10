---
name: wiki-bulk-ack
description: Bulk-approve voice→wiki Stage 5 v2 candidates per tier (A/B/C). Third constitutional gate.
type: skill
created: 2026-05-10
related:
  - tools/wiki_integration/cli.py
  - tools/wiki_integration/auto_merger.py
  - reports/wiki-integration-redesign-2026-05-10/PLAN.md
---

# /wiki-bulk-ack — voice→wiki bulk approval

> **Constitutional posture.** Third gate of the Default-Deny chain (PLAN.md §0):
> 1. Plan ack → Phase 2 execute (done)
> 2. Phase 2 deliverables ack → bulk-ack ready (done)
> 3. **/wiki-bulk-ack** → real wiki/ writes (this gate)
>
> Existing wiki entries are NEVER modified. Match-to-existing → edge-only cross-reference. Tier C → new entries from template.

## When to use

After voice pipeline Stage 5 v2 produces `reports/voice-pipeline-<date>/04-wiki-candidates-v2.md` + sidecar JSON. Ruslan reviews the markdown, then bulk-approves per tier.

## Tier semantics (per PLAN.md §2.2 / §4)

| Tier | Score | Meaning | Default action |
|------|-------|---------|----------------|
| A | ≥ 0.85 | High-confidence match-to-existing | Single bulk-ack → all merge as edges |
| B | 0.60–0.85 | Medium-confidence match | Subset selection — Ruslan picks indices |
| C | < 0.60 OR null | No match → propose new entry | Subset selection → new wiki entries |
| D | (skipped) | Контакты / Задачи / low-quality | No action — route to crm/ separately |

## Commands

| Command | Effect |
|---------|--------|
| `/wiki-bulk-ack --status` | Print tier counts + sidecar metadata |
| `/wiki-bulk-ack --tier A --dry-run` | Preview Tier A merges without writing |
| `/wiki-bulk-ack --tier A` | Auto-merge ALL Tier A candidates as edges |
| `/wiki-bulk-ack --tier B --select 1,3,5,7-10 --dry-run` | Preview selected Tier B |
| `/wiki-bulk-ack --tier B --select 1,3,5,7-10` | Merge selected Tier B as edges |
| `/wiki-bulk-ack --tier C --select N,M,P --as-new --dry-run` | Preview new entry creation |
| `/wiki-bulk-ack --tier C --select N,M,P --as-new` | Create new wiki entries for selected |
| `/wiki-bulk-ack --reject 1,2,3 --reason "low quality"` | Mark rejected (no wiki write) |
| `/wiki-bulk-ack --defer-backlog 5,6,7` | Park in backlog (no wiki write) |
| `/wiki-bulk-ack --sidecar <path>` | Override sidecar JSON path |

## Sidecar selection

By default the skill picks the most-recent `reports/voice-pipeline-*/04-wiki-candidates-v2.json`. Override with `--sidecar <path>`.

## What it writes

**Tier A / B (match-to-existing):**
- `wiki/graph/edges.jsonl` — append `voice/<memo> → <wiki_path>` edges (predicate `mentions`)
- `wiki/log.md` — append-only log entry on top, summarizing the batch

**Tier C (propose-new):**
- `wiki/<entity_type>/<slug>.md` — new entry from template (with `voice_provenance` frontmatter)
- `wiki/index.md` — sentinel-aware insert under `## <Section>`
- `wiki/graph/edges.jsonl` — `voice → new` (`derived_from`) + `new → top-2 BM25 neighbors` (`related_to`)
- `wiki/log.md` — log entry on top

**Always:**
- `reports/wiki-integration-redesign-<date>/discipline-log.md` — append per-batch verdict (PASS / PARTIAL / FAIL with halt reason)

## Constitutional invariants enforced

- Existing wiki entry frontmatter/body — **NEVER modified** (Tier A/B only adds edges)
- Append-only — no overwrite, no `--amend`, no `git revert`-required ops
- Strict frontmatter validation per `wiki/_templates/<type>.md` (Tier C; rejects → discipline log)
- Контакты → `/crm-add` route (Tier D Skipped); not auto-promoted to wiki
- Задачи → operational, not knowledge; not auto-promoted

## Self-check post-batch

After every successful batch, the skill runs:

```bash
python3 wiki/graph/build_graph.py lint   # validates new edges target existing files
```

If lint FAIL → halt subsequent batches; emit Halt-Log-Alert per Part 6b §I.2.

## Implementation

The skill delegates to:

```bash
python3 -m tools.wiki_integration.cli --tier A [--dry-run]
python3 -m tools.wiki_integration.cli --tier B --select 1,3,5,7-10
python3 -m tools.wiki_integration.cli --tier C --select 1,2,3 --as-new
python3 -m tools.wiki_integration.cli --status
```

When invoked via `/wiki-bulk-ack`, Claude Code:
1. Parses Ruslan's command flags
2. Runs the corresponding `python3 -m tools.wiki_integration.cli ...` invocation
3. Prints the merge report (kind / detail / target per action)
4. If errors > 0, halts and surfaces to Ruslan

## Examples

```
$ /wiki-bulk-ack --status
{
  "tier_a_count": 27,
  "tier_b_count": 184,
  "tier_c_count": 1064,
  "skipped_count": 24,
  "total_candidates": 1275,
  "match_rate": 0.165,
  "generated_at": "2026-05-10T14:23:11"
}

$ /wiki-bulk-ack --tier A --dry-run
tier=A (match-to-existing) dry_run=True edges +0 (dup 0, rej 0) ...
  - edge: voice/audio_587 → concepts/founder-isolation-as-stopper-class.md (score=0.92)
  - edge: voice/audio_588 → concepts/engineering-faith.md (score=0.91)
  …

$ /wiki-bulk-ack --tier A
tier=A (match-to-existing) dry_run=False edges +27 (dup 0, rej 0) ...
[wiki-bulk-ack] 27 edges appended to wiki/graph/edges.jsonl
[wiki-bulk-ack] log entry appended to wiki/log.md
```

## Related artefacts

- Source plan: `reports/wiki-integration-redesign-2026-05-10/PLAN.md`
- Stage 5 v2 source: `tools/voice-pipeline-orchestrator.py:stage_5_wiki_candidates`
- Auto-merger: `tools/wiki_integration/auto_merger.py`
- Edge writer: `tools/wiki_integration/edge_writer.py`
- Edge predicates allowlist: `wiki/graph/edge-types.md` (existing 12-enum)

## What this skill does NOT do

- Modify existing wiki entries (frontmatter or body) — append-only invariant
- Auto-execute without explicit Ruslan invocation — third constitutional gate
- Promote Контакты to wiki (use `/crm-add` for those)
- Promote Задачи (operational, not knowledge)
- Touch `decisions/`, `swarm/wiki/foundations/`, `principles/`, `shared/schemas/` — Foundation paths require AWAITING-APPROVAL packet via Part 6b
