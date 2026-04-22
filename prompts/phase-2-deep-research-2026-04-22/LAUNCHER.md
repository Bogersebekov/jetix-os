---
id: phase-2-launcher
title: LAUNCHER — Phase 2 Deep Research Execution Plan
author: cloud-cowork
date: 2026-04-22
audience: Ruslan — execution operator
depends-on: 00-META-INSTRUCTIONS.md, 01-07 Perplexity prompts, 08 bibliography spec
status: ready-to-execute
---

# LAUNCHER — Phase 2 Deep Research Execution

> **One-page operator view.** This doc tells Ruslan in what order to execute, how long each prompt takes, where to save outputs, and what unlocks Phase 3 synthesis.

## Prerequisites

- Perplexity Pro subscription (Deep Research mode required)
- `raw/research/phase-2-deep-research-2026-04-22/` directory ready for outputs (create if missing: `mkdir -p raw/research/phase-2-deep-research-2026-04-22/`)
- `raw/books-pm/` and `raw/articles/` directories ready for bibliography (File 08)

## Execution order — recommended serial run

Perplexity Deep Research consumes time and context. Running 7 prompts in parallel is inadvisable (attention drift, no cross-reference possible during runs). Run serially in P1 → P2 order, save each output before next.

**Total Perplexity-only wall time: 2.5-4 hours of runs + 2-3 hours of save/verify. Plan a dedicated half-day.**

---

### Day 1 — P1 prompts (blockers for Phase 3 synthesis)

| # | File | Priority | Perplexity ETA | Save to |
|---|---|---|---|---|
| 1 | `01-matchmaker-capability-capsule-production.md` | P1 | 20-30 min | `raw/research/phase-2-deep-research-2026-04-22/RESULT-01-matchmaker.md` |
| 2 | `02-ai-native-os-vertical-stacks.md` | P1 | 20-30 min | `raw/research/phase-2-deep-research-2026-04-22/RESULT-02-ai-native-os.md` |
| 3 | `03-mast-14-modes-jetix-mapping.md` | P1 | 25-35 min | `raw/research/phase-2-deep-research-2026-04-22/RESULT-03-mast-matrix.md` |
| 4 | `04-anthropic-mailbox-pattern-primary-sources.md` | P1 | 15-20 min | `raw/research/phase-2-deep-research-2026-04-22/RESULT-04-mailbox.md` |

**Day 1 total: ~80-115 min Perplexity + save time (4 runs).**

### Day 2 — P2 prompts (Domain 9 PM/Product/Mgmt)

| # | File | Priority | Perplexity ETA | Save to |
|---|---|---|---|---|
| 5 | `05-project-management-methodologies-ai-native.md` | P2 | 25-30 min | `raw/research/phase-2-deep-research-2026-04-22/RESULT-05-pm-methodologies.md` |
| 6 | `06-product-management-methodologies-ai-native.md` | P2 | 25-30 min | `raw/research/phase-2-deep-research-2026-04-22/RESULT-06-product-mgmt.md` |
| 7 | `07-management-philosophy-deep.md` | P2 | 25-30 min | `raw/research/phase-2-deep-research-2026-04-22/RESULT-07-management-philosophy.md` |

**Day 2 total: ~75-90 min Perplexity + save time (3 runs).**

### Day 1-3 — File 08 bibliography acquisition (parallel)

Execute `08-raw-primary-sources-catalog.md` in parallel with Perplexity runs. The bibliography is 65 items (30×P1, 26×P2, 8×P3).

- **P1 tier (30 items)** — prioritize to complete by end of Day 2
- **P2 tier (26 items)** — backlog by end of Day 3
- **P3 tier** — opportunistic

Can delegate to a Haiku agent with web-fetch capability, or execute manually during Perplexity wait times.

Each captured file: add YAML frontmatter; save to `raw/books-pm/` or `raw/articles/` per the catalog spec.

---

## Per-run checklist

For each Perplexity prompt:

1. ☐ Open `prompts/phase-2-deep-research-2026-04-22/0X-<name>.md`
2. ☐ Open Perplexity Pro → select **Deep Research** mode
3. ☐ Copy the block between `===BEGIN PROMPT TO PASTE===` and `===END PROMPT TO PASTE===` (exclude the markers themselves; Perplexity treats them as text)
4. ☐ Paste → submit
5. ☐ While running: set a 30-min timer; go execute File 08 P1 bibliography items
6. ☐ When Perplexity completes: save **full output** including all citations to `raw/research/phase-2-deep-research-2026-04-22/RESULT-XX-<name>.md`
7. ☐ Prepend this frontmatter to each RESULT file:

```yaml
---
id: phase-2-result-XX-<slug>
title: Phase 2 RESULT-XX — <domain>
source: Perplexity Pro Deep Research
date: 2026-04-22 (+/- your actual date)
prompt-file: prompts/phase-2-deep-research-2026-04-22/0X-<filename>.md
status: raw
caveats: Perplexity raw output may contain hallucinations — verify citations before use
---
```

8. ☐ Check: are cited URLs live? Spot-check 5 random citations per result.
9. ☐ Flag in commit message: `[research] Phase 2 RESULT-XX — <domain>`
10. ☐ Move to next prompt

---

## Common pitfalls to avoid

- **Do not paste the `===BEGIN===` marker itself.** Perplexity treats text literally; the markers are for the human reader to identify the paste-region.
- **Do not paste the "Context для понимания" section** — it's for Ruslan's comprehension, not Perplexity. Perplexity has no context from our chat.
- **Do not run 2 prompts simultaneously** in the same Perplexity session — cross-contamination risk.
- **Save raw output unedited first.** Post-processing (extraction, verification) is a separate step.
- **Do not prematurely /ingest RESULT files** into `wiki/` — wait for Phase 3 synthesis.

---

## What's unlocked when — hand-off protocol to Phase 3

Phase 3 synthesis begins when the following conditions are met:

### Minimum viable hand-off (all P1 P2 files present, even imperfect):

- ☐ RESULT-01 through RESULT-07 saved to `raw/research/phase-2-deep-research-2026-04-22/`
- ☐ At least 20 of 30 P1 bibliography items present in `raw/books-pm/` + `raw/articles/`
- ☐ Ruslan pings Cloud Cowork (e.g., commit + push, or Telegram notify)

### Cloud Cowork Phase 3 synthesis workflow (for reference, not Ruslan's job):

1. Read all 7 RESULT files + P1 bibliography
2. Produce 3 synthesis artifacts:
   - `design/MAST-JETIX-MATRIX-v1.md` — 14 MAST modes × 11 Jetix agents matrix (from RESULT-03)
   - `design/JETIX-UNIFIED-PM-PHILOSOPHY.md` — CE + Shape Up + Marty Cagan + 37signals + Grove unified doctrine (from RESULT-05/06/07)
   - `design/MATCHMAKER-ARCHITECTURE-v1.md` — reference architecture for Jetix matchmaker + roy-replication (from RESULT-01 + RESULT-04)
3. Propose any Lock updates or Decision adjustments in `decisions/` (via PR, not direct write)
4. Flag Ruslan for review

---

## Failure / partial-completion paths

### If Perplexity returns shallow output for any prompt:

- Each prompt file contains an **"Alternative: split into N focused prompts"** section
- Re-run as split-prompts using the same `===BEGIN===/===END===` style (Ruslan may need to manually split)
- Save split-prompt results with `-A.md`, `-B.md` suffixes (e.g., `RESULT-03-A.md`, `RESULT-03-B.md`)

### If Perplexity Deep Research is unavailable:

Fallback options in order of preference:
1. Claude Deep Research (if accessible via web.claude.ai)
2. Perplexity Pro Search (non-Deep mode) — paste same prompt, expect shallower result, flag in caveats
3. GPT-5 Deep Research via ChatGPT Pro
4. Gemini Deep Research — reportedly strong in 2026-04

Any alternative tool: preserve the same `===BEGIN===/===END===` payload; save output to RESULT-XX with `source: <tool-name>` in frontmatter.

### If a prompt is clearly unanswerable:

- Do not force a bad result. Save a stub RESULT-XX.md with a note: "Prompt returned insufficient evidence; see Cloud Cowork for re-scoping."
- Cloud Cowork will either write a narrower re-scoped prompt or accept the gap.

---

## Commit + push template

Run these commits as work progresses (not all at end):

```bash
# After 01-07 prompt files + LAUNCHER committed (Ruslan current commit 68607a2+):
# — already committed by server-cc

# After each RESULT file saved:
git add raw/research/phase-2-deep-research-2026-04-22/RESULT-XX-<name>.md
git commit -m "[research] Phase 2 RESULT-XX — <domain> (Perplexity Deep Research)"

# After bibliography P1 tier complete:
git add raw/books-pm/ raw/articles/
git commit -m "[research] Phase 2 bibliography P1 tier — 30 primary sources acquired"

# Push after each milestone:
git push origin claude/jolly-margulis-915d34

# Final hand-off to Phase 3:
git commit --allow-empty -m "[research] Phase 2 complete — 7 Perplexity results + 30 P1 sources; Cloud Cowork begin Phase 3 synthesis"
git push origin claude/jolly-margulis-915d34
```

---

## Budget / cost estimation

- **Perplexity Pro**: flat subscription; Deep Research usage counts against monthly cap (check limits)
- **Time**: 2 half-days Ruslan attention + 0.5 day Haiku agent / manual bibliography work
- **Inference cost (if via API alternative)**: GPT-5 / Claude Opus 4.x Deep Research equivalents ~$5-15 per prompt; 7 prompts × $10 avg = ~$70 worst case

---

## Success criteria for Phase 2

- [ ] 7 RESULT files present, each ≥5,000 words
- [ ] Each RESULT file's citations are ≥80% live-URL-verifiable on spot check
- [ ] Bibliography ≥30 P1 sources captured
- [ ] All files committed + pushed to `claude/jolly-margulis-915d34`
- [ ] Cloud Cowork pinged / notified to begin Phase 3

---

## Quick reference — what each prompt closes

| File | Gap closed (Phase 1 inventory) | Locks informed |
|---|---|---|
| 01 matchmaker | Domain 2 MAJOR #1, Domain 6 MAJOR #1 | Decision 21 (matchmaker + roy) |
| 02 AI-native OS | Domain 4 MAJOR #1-2 | Decision 19 (holding), 20 (USB-C), 24 (OSS research) |
| 03 MAST matrix | Domain 7 MAJOR #1, MINOR #1 | Decision 15 (compliance), Phase 4 readiness |
| 04 mailbox | Domain 2 MAJOR #3 | Current `comms/mailboxes/*.jsonl` architecture |
| 05 PM methodologies | NEW Domain 9 | Unified PM philosophy |
| 06 Product mgmt | NEW Domain 9 | Unified Product philosophy + Decision 18 (productization) |
| 07 Mgmt philosophy | NEW Domain 9 | D2 JETIX-PHILOSOPHY alignment |
| 08 bibliography | Primary-source substrate | All Phase 3+ synthesis |

---

## Contact

Questions during execution → write to `raw/voice-memos-text/phase-2-execution-notes-YYYY-MM-DD.md` or ping Cloud Cowork directly.

---

*END LAUNCHER 09 — Phase 2 Execution*
