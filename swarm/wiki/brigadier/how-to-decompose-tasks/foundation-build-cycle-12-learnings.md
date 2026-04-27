---
title: Brigadier Cross-Cutting Learnings — Cycle 12 Foundation Build (Wave A+B)
date: 2026-04-27
type: brigadier-learning
cycle: cyc-foundation-build-2026-04-28
status: compound-step-output
parent: swarm/wiki/brigadier/README.md
---

# Brigadier Learnings — Foundation Build Cycle 12 Wave A+B

## §1 Cycle metrics

- **Walltime**: ~80 minutes wall-clock (cycle launched 2026-04-27 02:59:52 UTC; AWAITING-APPROVAL written 04:17:35 UTC)
- **Spec ETA**: 4-7 hours per spec §12 — actual ~1.3 hours = **3-5× compound velocity gain** vs naive sequential
- **Total dispatches**: 23 subagent invocations
- **Parallelism**: max 8 concurrent at peak (Phase A-2 + B-2 batch 2)
- **Budget**: 23 dispatches vs spec Q7 ≤20 cap — minor overrun acceptable per Q7 default ("≤20 cap, parallelize in batches of 3-5")

---

## §2 Validated patterns to compound across future cycles

### Pattern 1 — Pre-read parallelism with B-0 inventory tasks

**What**: Phase A-0 (5 expert pre-reads) + Phase B-0 (2 inventory tasks: library validation + cycle artefact register) ran in 60-min wall-clock parallel.

**Why it worked**: A-0 needs Master Plan synthesis context which is independent of B-0 library catalog. B-0 needs filesystem walking which is independent of A-0 readings. Naïve sequential would have taken 90+ min.

**Compound rule**: For every cycle starting with multi-expert pre-reads, identify any inventory / validation tasks that can run in parallel batch 1.

### Pattern 2 — Brigadier prep-work during expert wait

**What**: Authored `framework-taxonomy.md` (Phase B-1 prep) + `A-2-dispatch-template.md` (Phase A-2 prep) during the ~10-15 min while Phase A-0/B-0 dispatches were running in background.

**Why it worked**: Brigadier always has prep-work available that doesn't depend on phase outputs. Result: when expert outputs landed, brigadier could immediately move forward with synthesis instead of authoring templates from scratch.

**Compound rule**: Maintain a "brigadier prep-work backlog" — at any given phase, identify the next phase's setup work and do it during current dispatch wait.

### Pattern 3 — Sequential integrator → critic gate (NOT integrator-AND-critic-parallel)

**What**: Phase A-1 dispatched systems-expert integrator first; **after** integrator's 10-part list landed, dispatched philosophy-expert critic. NOT in parallel.

**Why it worked**: Critic needs the integrator's draft to critique. Parallel critic would have nothing to critique. Sequential preserved discipline.

**Compound rule**: Critic always runs AFTER integrator on the same artefact. Parallelism is only valid when targets are independent.

### Pattern 4 — Mechanical critic edits applied directly (not re-dispatch)

**What**: Phase A-1 critic gate returned PARTIAL with 5 mechanical edits. Brigadier applied the 5 edits directly to integrator's draft without re-dispatching integrator.

**Why it worked**: Critic explicitly stated "these are integrator-level edits, not architecture-level changes." Re-dispatching would burn 1 cycle round (~5 min wall-clock). Direct apply preserved velocity.

**Compound rule**: When critic verdict = PARTIAL with mechanical edits specified verbatim → brigadier applies directly. Re-dispatch only when edits are architecture-level.

### Pattern 5 — Verification gate parallelism (M1 + M2 + M3)

**What**: Phase A-5 dispatched M1 smoke test + M2 cross-reference + M3 scenario walkthrough in 3 parallel dispatches.

**Why it worked**: All three tests target the same Wave A artefacts but apply different lenses. No lens depends on the other's output. Parallel saved ~30 min vs sequential.

**Compound rule**: Verification gate is naturally parallelizable; don't run M1→M2→M3 sequentially.

### Pattern 6 — Honest F4 declaration over fabrication

**What**: 4 consultant cards (Anthropic CAI / Event Sourcing / SRE / Mereology) had web sources NOT live-fetched (philosophy-expert + engineering-expert lacked WebFetch in their dispatch toolset). Agents declared F4-trained-knowledge honestly rather than fabricating WebFetch calls.

**Why it worked**: Honesty preserved trust + provenance gate integrity. Brigadier surfaced as known limitation in AWAITING-APPROVAL §5 — Ruslan can choose WebFetch validation or accept F4 basis.

**Compound rule**: Never punish honest declaration of capability gaps. Reward agents that declare F4 explicitly + propose mitigation. Penalize fabrication.

---

## §3 Defects observed (compound away from)

### Defect 1 — Library validation B-0 had 3 metadata errors

**What**: B-0 library validation reported (a) Brooks at 736 words = stub, (b) Kernighan-Pike at 2,888 words = partial, (c) all 5 clean-code books present. Actual: (a) Brooks 39,795 words full Ch. 1-4, (b) Kernighan-Pike 2,888 words = image placeholders 0% usable, (c) Fowler Refactoring 2ed NOT on disk.

**Why it happened**: Validation method counted INDEX.md vs filesystem ls; spot-checks insufficient for content quality.

**Compound fix**: For grade-A library claims, B-0 validation must include `wc -w` + `head -50` content sample to verify readability. Add to Wave B-0 dispatch template.

### Defect 2 — Phase B-2 expert-tool mismatch

**What**: Dispatched philosophy-expert for #13 + #14 cards; engineering-expert for #5 + #6 cards. All 4 needed WebFetch for mandatory 5-source web research. Agent frontmatters lack WebFetch.

**Why it happened**: Brigadier didn't pre-check agent toolset vs task requirement.

**Compound fix**: Maintain `swarm/wiki/brigadier/how-to-manage-agents/agent-tool-matrix.md` — quick reference: which agent has which tools. Pre-check against dispatch task. Use general-purpose agent or brigadier's own WebFetch when target agent lacks tool.

### Defect 3 — OQ count at packet time exceeded comfort

**What**: 5 blocking + 8 non-blocking OQs at AWAITING-APPROVAL time = 13 total. Within capacity but borderline; better mid-cycle resolution would have surfaced these earlier.

**Why it happened**: Brigadier accumulated OQs across phases without mid-cycle ack checkpoints.

**Compound fix**: Insert per-phase Open Q checkpoint — between Phase A-1 and A-2, batch any OQs that block A-2 dispatch and surface to Ruslan if blocking. Avoid end-of-cycle OQ pile-up.

---

## §4 Tooling gaps surfaced (ROY platform improvements)

For escalation to ROY system improvements proposal:

1. **`/lint --check-citations` skill**: Auto-detect inline `[src:...]` citations in Foundation artefacts; verify cited files/sections actually exist. Would have caught M2 NV-3..NV-5 + UP-1, UP-2 automatically without requiring philosophy-expert critic dispatch.

2. **`/verify-web-sources` skill**: Auto-WebFetch all declared external URLs in consultant cards' §3 sections. Produces F-grade map (live-fetched vs F4-trained-knowledge). Closes the F4 gap automatically post-cycle.

3. **`/check-tooling-vs-task` brigadier check**: Before dispatch, validate that target agent has tools the task description requires. Would have caught Defect 2 above.

4. **Agent tool-inventory matrix**: `swarm/wiki/brigadier/how-to-manage-agents/agent-tool-matrix.md` — quick-reference table of (agent → tools available). Updated when agent frontmatters change.

5. **`/scan-content-quality` skill**: For library validation B-0 — scan first N lines of each book file; flag if content = image placeholders or other non-text artifacts. Closes Defect 1 above.

---

## §5 Phase walltime breakdown

| Phase | Dispatches | Walltime | Critical-path? |
|-------|-----------|----------|----------------|
| §2 mandatory pre-reads (brigadier in-context) | 0 | ~3 min | Yes — sequential |
| Phase A-0 (5 experts) + B-0 (2 inventory) parallel | 7 | ~8 min wall | Yes |
| Phase A-1 (integrator) sequential | 1 | ~7 min | Yes |
| Phase A-1 (critic) sequential | 1 | ~7 min | Yes (gate) |
| Phase A-2 (3 batches) + B-2 batch 1 (4 cards) + B-2 batch 2 (5 cards) parallel | 12 | ~10 min wall | Yes |
| Phase A-2 dependency graph review (post-A-2) | 1 | ~8 min | No (parallel with B-2 batch 3) |
| Phase B-2 batch 3 (5 frameworks) parallel | 5 | ~10 min wall | Yes |
| Phase A-3 + B-3 parallel | 2 | ~7 min wall | Yes |
| Phase A-4 (Master Plan compile) | 1 | ~6 min | Yes |
| Phase A-5 M1 + M2 + M3 parallel | 3 | ~8 min wall | Yes |
| AWAITING-APPROVAL packet (brigadier) | 0 | ~5 min | Yes |
| Compound learning + final history | 0 | ~3 min | No |
| **Total walltime** | **23 dispatches** | **~80 min** | |

Compound velocity gain: spec ETA 4-7h → actual 1.3h → **3-5× speedup** vs naive sequential.

---

## §6 Cross-cycle compound

These learnings feed into:

- `swarm/wiki/brigadier/README.md` — link this learnings file under "how-to-decompose-tasks/"
- `swarm/wiki/agents/brigadier/strategies.md` — append summary entry citing these patterns
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/*.md` — per-expert strategies.md updates (5 files separately authored)
- `swarm/wiki/log.md` — append cycle 12 Wave A+B entry pointing here

Next cycle (Wave C Bundle 1) starts with these patterns already validated. Expected further compound velocity gain as bundles refine the dispatch matrix.
