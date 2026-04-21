---
id: launchers-stage-6
title: LAUNCHERS-STAGE-6 — copy-paste blocks for 6 parallel architect sessions
date: 2026-04-21
type: launcher-index
status: ready
priority: P1
stage: 6
audience: Ruslan (executes 6 parallel CC sessions)
---

# LAUNCHERS-STAGE-6

**Purpose.** Copy-paste ready launcher blocks for running the 6 Stage 6 architect variants as
parallel Claude Code sessions. One tmux window per variant; all on branch
`claude/jolly-margulis-915d34`; expected wall-clock ~5–7h for all 6 in parallel.

**How to use.** (1) Run the prep step once. (2) Open 6 tmux windows on the remote host.
(3) Copy-paste one of the 6 launcher blocks into each window. (4) Wait for completion;
read Notion page or tmux for progress.

**Notion progress page.** https://www.notion.so/3492496333bf812e8b62cbc61338ce06

---

## Prep step (one CC session, one-time before launching 6)

Run this once on the remote host in a Claude Code session to confirm the branch is in the right
state and the prompts directory is populated:

```bash
cd ~/jetix-os
git fetch origin
git checkout claude/jolly-margulis-915d34
git pull origin claude/jolly-margulis-915d34
git merge origin/claude/recursing-kirch-26223c --no-edit || true
git push origin claude/jolly-margulis-915d34
ls -la prompts/stage-6-variants/
ls -la decisions/variants/ 2>/dev/null || mkdir -p decisions/variants
```

Expected outcome: `prompts/stage-6-variants/` contains `00-README.md` + `00-META-PROMPT-WRITE-6-PROMPTS.md`
+ `01-conservative.md` through `06-wildcard.md`; `decisions/variants/` directory exists (empty).

---

## Claude launch command (per tmux window)

```bash
ssh ruslan@100.99.156.28
tmux new -s stage6-v1       # or stage6-v2 / stage6-v3 / stage6-v4 / stage6-v5 / stage6-v6 — one per variant
claude --dangerously-skip-permissions
```

Then paste one of the launcher blocks below.

**Tip:** Use `tmux new-window -n v2` / `v3` / `v4` / `v5` / `v6` inside the same tmux session to
keep all six in a single tmux attach-target; or separate tmux sessions if you prefer.

---

## CC session #1 — Variant CONSERVATIVE (evolve what works)

```
cd ~/jetix-os
git checkout claude/jolly-margulis-915d34
git pull --rebase origin claude/jolly-margulis-915d34

Прочитай `prompts/stage-6-variants/01-conservative.md` полностью и исполни.
Variant 1 CONSERVATIVE — минимум deviation от current state (CLAUDE.md + D6 FPF + OME reference);
proven patterns; 11-agent roster as-is.

КРИТИЧНО:
- 24 locked decisions + D1/D2/D3/D4 APPROVED = BINDING
- Answer ALL 15 architect questions from D4 §10
- Output structure = same 24 sections (для comparability с другими 5 variants)
- Multi-pass (skeleton → flesh → coherence-critic)
- Use subagents параллельно (Pass 2)
- Size target: 40-60 pages / 8000-12000 words

Deliverable: decisions/variants/JETIX-ARCH-V1-CONSERVATIVE.md

После:
git add decisions/variants/JETIX-ARCH-V1-CONSERVATIVE.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[decisions] Stage 6 Variant 1 CONSERVATIVE — architecture variant draft"
git push origin claude/jolly-margulis-915d34

Обнови Notion: https://www.notion.so/3492496333bf812e8b62cbc61338ce06

В конце выведи stdout summary по формату в prompt file.

ETA 5-7 hours с subagents.
```

---

## CC session #2 — Variant AGGRESSIVE MAXIMALIST (build for Phase 3 Day 1)

```
cd ~/jetix-os
git checkout claude/jolly-margulis-915d34
git pull --rebase origin claude/jolly-margulis-915d34

Прочитай `prompts/stage-6-variants/02-aggressive-maximalist.md` полностью и исполни.
Variant 2 AGGRESSIVE-MAXIMALIST — maximum capability scaffolded Phase 1 (schemas + role-manifests
+ spec docs — NOT runtime, чтобы не пробить €800/mo). Build for Phase 3 from Day 1.

КРИТИЧНО:
- 24 locked decisions + D1/D2/D3/D4 APPROVED = BINDING
- Answer ALL 15 architect questions from D4 §10
- Output structure = same 24 sections
- Multi-pass (skeleton → flesh → coherence-critic)
- Use subagents параллельно
- Size target: 40-60 pages / 8000-12000 words
- СПЕЦИФИКА: defend €300-800/mo Phase 1 band (§8.3 disqualifier) + C14 canonical 11 + Lock 19 $1T trajectory

Deliverable: decisions/variants/JETIX-ARCH-V2-MAXIMALIST.md

После:
git add decisions/variants/JETIX-ARCH-V2-MAXIMALIST.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[decisions] Stage 6 Variant 2 AGGRESSIVE-MAXIMALIST — architecture variant draft"
git push origin claude/jolly-margulis-915d34

Обнови Notion: https://www.notion.so/3492496333bf812e8b62cbc61338ce06

В конце выведи stdout summary.

ETA 5-7 hours с subagents.
```

---

## CC session #3 — Variant AGGRESSIVE DEEP-TECH (FPF ontology as substrate)

```
cd ~/jetix-os
git checkout claude/jolly-margulis-915d34
git pull --rebase origin claude/jolly-margulis-915d34

Прочитай `prompts/stage-6-variants/03-aggressive-deep-tech.md` полностью и исполни.
Variant 3 AGGRESSIVE-DEEP-TECH — FPF ontology-first architecture. Every agent has formal FPF
contract. Wiki = typed graph. Protocols = standards-body-ready drafts. Research-grade rigor.

КРИТИЧНО:
- 24 locked decisions + D1/D2/D3/D4 APPROVED = BINDING
- D6 JETIX-FPF.md = READ DEEPLY (3758 lines) — это substrate
- Answer ALL 15 architect questions from D4 §10
- Output structure = same 24 sections
- Multi-pass (skeleton → flesh → coherence-critic)
- Use subagents параллельно
- Size target: 40-60 pages / 8000-12000 words
- СПЕЦИФИКА: avoid AP-12 (pure-research Phase 1); depth must still ship consulting pipeline €50K Q2

Deliverable: decisions/variants/JETIX-ARCH-V3-DEEPTECH.md

После:
git add decisions/variants/JETIX-ARCH-V3-DEEPTECH.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[decisions] Stage 6 Variant 3 AGGRESSIVE-DEEP-TECH — architecture variant draft"
git push origin claude/jolly-margulis-915d34

Обнови Notion: https://www.notion.so/3492496333bf812e8b62cbc61338ce06

В конце выведи stdout summary.

ETA 5-7 hours с subagents.
```

---

## CC session #4 — Variant HYBRID (phase-keyed complexity)

```
cd ~/jetix-os
git checkout claude/jolly-margulis-915d34
git pull --rebase origin claude/jolly-margulis-915d34

Прочитай `prompts/stage-6-variants/04-hybrid.md` полностью и исполни.
Variant 4 HYBRID — phase-keyed complexity. Every capability имеет activation_trigger (revenue
gate OR MHT transition). Phase 1 simple, Phase 2+ richer, Phase 3+ maximalist. Schemas
forward-compatible Day 1.

КРИТИЧНО:
- 24 locked decisions + D1/D2/D3/D4 APPROVED = BINDING
- Answer ALL 15 architect questions from D4 §10
- Output structure = same 24 sections
- Multi-pass (skeleton → flesh → coherence-critic)
- Use subagents параллельно
- Size target: 40-60 pages / 8000-12000 words
- СПЕЦИФИКА: каждый architecture element имеет activation_trigger tied to Lock 15 gate или B.2 MHT transition

Deliverable: decisions/variants/JETIX-ARCH-V4-HYBRID.md

После:
git add decisions/variants/JETIX-ARCH-V4-HYBRID.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[decisions] Stage 6 Variant 4 HYBRID — architecture variant draft"
git push origin claude/jolly-margulis-915d34

Обнови Notion: https://www.notion.so/3492496333bf812e8b62cbc61338ce06

В конце выведи stdout summary.

ETA 5-7 hours с subagents.
```

---

## CC session #5 — Variant EMERGENT (sparse skeleton, self-organization)

```
cd ~/jetix-os
git checkout claude/jolly-margulis-915d34
git pull --rebase origin claude/jolly-margulis-915d34

Прочитай `prompts/stage-6-variants/05-emergent.md` полностью и исполни.
Variant 5 EMERGENT — thin prescribed structure + rich protocols + agent-driven specialization.
"Trellis not cage." Hub-and-spoke + revenue gates + membrane — hard parameters. Task routing,
knowledge-graph density, specialization — emergent signals.

КРИТИЧНО:
- 24 locked decisions + D1/D2/D3/D4 APPROVED = BINDING
- Answer ALL 15 architect questions from D4 §10
- Output structure = same 24 sections
- Multi-pass (skeleton → flesh → coherence-critic)
- Use subagents параллельно
- Size target: 40-60 pages / 8000-12000 words
- СПЕЦИФИКА: emergence ≠ anarchy; C14/C17/Lock 15 non-negotiable; every "emergence" claim needs structure parameter + observable signal + convergence criterion

Deliverable: decisions/variants/JETIX-ARCH-V5-EMERGENT.md

После:
git add decisions/variants/JETIX-ARCH-V5-EMERGENT.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[decisions] Stage 6 Variant 5 EMERGENT — architecture variant draft"
git push origin claude/jolly-margulis-915d34

Обнови Notion: https://www.notion.so/3492496333bf812e8b62cbc61338ce06

В конце выведи stdout summary.

ETA 5-7 hours с subagents.
```

---

## CC session #6 — Variant WILDCARD (radical reframe, challenge assumptions)

```
cd ~/jetix-os
git checkout claude/jolly-margulis-915d34
git pull --rebase origin claude/jolly-margulis-915d34

Прочитай `prompts/stage-6-variants/06-wildcard.md` полностью и исполни.
Variant 6 WILDCARD — 1-3 radical reframes challenging brief orthodoxies. Each reframe:
state-defend-lock-check-AP-check-C-check-fallback. 24 locks + 16 AP + 21 C — non-negotiable.

КРИТИЧНО:
- 24 locked decisions + D1/D2/D3/D4 APPROVED = BINDING (reframe them sideways, never through)
- Answer ALL 15 architect questions from D4 §10
- Output structure = same 24 sections
- §22 Variant Contrarian Claims — longest section (1.5-2 pages) — defend EVERY reframe per-lock + per-AP + per-C
- Multi-pass (skeleton → flesh → coherence-critic) — critic pass 90-120 min (LIFE-OR-DEATH)
- Use subagents параллельно
- Size target: 40-60 pages / 8000-12000 words
- СПЕЦИФИКА: highest disqualification risk variant (§8.3). Self-kill reframes that fail lock/AP/C check.

Deliverable: decisions/variants/JETIX-ARCH-V6-WILDCARD.md

После:
git add decisions/variants/JETIX-ARCH-V6-WILDCARD.md
git pull --rebase origin claude/jolly-margulis-915d34
git commit -m "[decisions] Stage 6 Variant 6 WILDCARD — architecture variant draft"
git push origin claude/jolly-margulis-915d34

Обнови Notion: https://www.notion.so/3492496333bf812e8b62cbc61338ce06

В конце выведи stdout summary + list contrarian reframes chosen.

ETA 5-7 hours с subagents.
```

---

## Quick-reference checklist

Before running 6 launchers, confirm:

- [ ] Prep step ran (branch + dirs set up)
- [ ] `prompts/stage-6-variants/` contains 7 files (README + 6 variants)
- [ ] `decisions/variants/` directory exists (can be empty)
- [ ] Notion page URL accessible: https://www.notion.so/3492496333bf812e8b62cbc61338ce06
- [ ] 6 tmux windows open or 6 separate tmux sessions ready
- [ ] `claude --dangerously-skip-permissions` active in each

After all 6 complete:

- [ ] `ls decisions/variants/` shows 6 files
- [ ] Each variant's stdout summary printed (24/24 sections, 15/15 questions, 24/24 locks, 16/16 AP, 21/21 C)
- [ ] Notion has 6 status lines (one per variant)
- [ ] Ready for Stage 7 comparative evaluation

## Wall-clock budget

| Phase | Budget | Notes |
|---|---|---|
| Prep step | 5–10 min | Single CC run |
| Stage 6 parallel execution | 5–7 hours | All 6 variants run concurrently |
| Stage 7 Ruslan evaluation | 4–7 hours | Read all 6 + apply §9 Step A–F |
| Stage 8 unlock | immediate after §9 Step F | D5 Architecture Canonical committed |

## Contingency

**If one variant session crashes mid-run.** Re-attach tmux; the architect agent picks up from
last wiki write + last commit. If no commits yet, re-paste the launcher block (idempotent —
existing partial output in `decisions/variants/JETIX-ARCH-V{N}-{NAME}.md` will be rewritten in
full by the re-run's Pass 2).

**If one variant fails disqualification check at Stage 7.** Per D4 §9 Step E: Stage 6 re-run
for that variant only with refined brief, OR Ruslan proceeds with remaining 5 and selects from
them. Do not discard Wildcard prematurely — its job is surfacing blind spots even when scored lower.

**If all 6 fail.** Per §9 Step E backup plan: fallback to pre-Stage-6 canonical
(`decisions/2026-04-20-jetix-architecture-final-DRAFT.md` D9 v0.6 + ADR Chunk 8 + D4 as
guidance); defer full Stage 6 retry to Phase-1 mid-gate (€20–30K revenue).

---

*END OF LAUNCHERS-STAGE-6*
