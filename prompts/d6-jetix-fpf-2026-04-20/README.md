---
type: task-prompt-package
created: 2026-04-20
target: claude-code-on-server + 4 parallel review sessions + fresh verifier
methodology: Hybrid Ultimate V5
deliverable: design/JETIX-FPF.md (30-50 pages, max Левенчук depth)
plus: wiki/foundations/fpf-tooling.md (companion, optional Stage E)
notion: https://www.notion.so/3482496333bf81debcecf04f129443b1
---

# D6 JETIX-FPF Writing — Hybrid Ultimate V5

## Overview

Task-prompt package для создания D6 JETIX-FPF через **Hybrid Ultimate
methodology V5**: multi-agent orchestration + 4 parallel perspective
reviews + final synthesis + independent verification.

**Target quality:** 1000% depth, max Левенчук fidelity, zero context loss,
zero hallucinations.

## Files (in launch order)

| # | File | Stage | Purpose | Session type |
|---|------|-------|---------|--------------|
| 1 | `stage-A-main-orchestrator.md` | A | Write D6 v1 with 3 FPF subagents + Verifier | 1 main Claude Code |
| 2 | `stage-B1-reviewer-levenchuk-purist.md` | B | Ontology fidelity review | Fresh parallel #1 |
| 3 | `stage-B2-reviewer-dach-compliance.md` | B | Regulatory compliance review | Fresh parallel #2 |
| 4 | `stage-B3-reviewer-ai-agent-designer.md` | B | AI-agent patterns review | Fresh parallel #3 |
| 5 | `stage-B4-reviewer-enterprise-reader.md` | B | Practical clarity review | Fresh parallel #4 |
| 6 | `stage-C-final-synthesis.md` | C | Integrate 4 reviews → D6 v2 | 1 main |
| 7 | `stage-D-final-verification.md` | D | Independent final verification | Fresh |
| 8 | `stage-E-companion-fpf-tooling.md` | E (optional) | Write companion fpf-tooling.md | 1 main |

## Launch sequence

### Step 1 — Stage A (D6 v1 writing)

```bash
ssh ruslan@100.99.156.28
tmux a -t main
cd ~/jetix-os
git fetch origin
git checkout claude/jolly-margulis-915d34
git pull origin claude/jolly-margulis-915d34

# Launch main Claude Code
claude --dangerously-skip-permissions
```

Дай команду:
```
Прочитай prompts/d6-jetix-fpf-2026-04-20/stage-A-main-orchestrator.md и
выполни задачу полностью. Opus 4.7 с 1M context, extended thinking max.
Используй Task tool для спavning 3 FPF Scholar subagents parallel +
1 Verifier subagent. В конце commit + push + report.
```

**Ожидание:** ~3-5 hours.

**Ожидаемый output:** `design/JETIX-FPF.md` v1 (30-40 pages), commit SHA.

### Step 2 — Stage B (4 parallel reviews)

После Stage A completed, launch **4 parallel Claude Code sessions**
(different tmux panes, или separate terminal windows) — each с разным
reviewer prompt:

**Session 1:** `prompts/d6-jetix-fpf-2026-04-20/stage-B1-reviewer-levenchuk-purist.md`
**Session 2:** `prompts/d6-jetix-fpf-2026-04-20/stage-B2-reviewer-dach-compliance.md`
**Session 3:** `prompts/d6-jetix-fpf-2026-04-20/stage-B3-reviewer-ai-agent-designer.md`
**Session 4:** `prompts/d6-jetix-fpf-2026-04-20/stage-B4-reviewer-enterprise-reader.md`

**Ожидание:** ~2-4 hours parallel.

**Output:** 4 review reports в `raw/research/d6-reviews/`.

### Step 3 — Stage C (final synthesis)

Launch main Claude Code:
```
Прочитай prompts/d6-jetix-fpf-2026-04-20/stage-C-final-synthesis.md и
синтезируй D6 v2 из D6 v1 + 4 review reports. Commit + push.
```

**Ожидание:** ~1-3 hours.

**Output:** `design/JETIX-FPF.md` v2 (final), commit SHA.

### Step 4 — Stage D (final verification)

Launch **fresh** Claude Code (brand new session, no prior context):
```
Прочитай prompts/d6-jetix-fpf-2026-04-20/stage-D-final-verification.md и
выполни independent final verification. Output: verification report +
verdict.
```

**Ожидание:** ~1-2 hours.

**Output:** `raw/research/d6-reviews/stage-d-final-verification.md` +
verdict VERIFIED / MINOR / MAJOR.

### Step 5 — Decision point (you)

Based on Stage D verdict:
- **VERIFIED READY** → optionally proceed к Stage E companion OR move к D1-D5 + D7-D8 writing
- **MINOR ISSUES** → apply fixes (quick Claude Code session), re-verify
- **MAJOR ISSUES** → iterate back к Stage C with new critique

### Step 6 — Stage E (optional companion)

If D6 verified ready:

```
Прочитай prompts/d6-jetix-fpf-2026-04-20/stage-E-companion-fpf-tooling.md и
напиши companion wiki/foundations/fpf-tooling.md. Commit + push.
```

**Ожидание:** ~2-3 hours.

## Quality commitments across all stages

1. **Russian primary** content; English FPF citations verbatim
2. **FPF pattern IDs verified** against primary FPF-Spec.md
3. **Past-participle convention strict** (per MC6)
4. **Extended thinking max budget** (все sessions)
5. **Context isolation** (каждая session fresh; subagents isolated contexts)
6. **Citations not hallucinations** (все pattern IDs + line numbers verified)
7. **Depth over brevity** (30-50 pages D6 reflects комплексность accepted FPF adoption)

## Ruslan active time

- Step 1 launch: 5 min
- Step 2 launch (4 parallel): 10-15 min
- Step 3 launch: 5 min
- Step 4 launch: 5 min
- Step 5 decision + final review: 30-60 min
- Step 6 optional: 5 min

**Total Ruslan active time:** ~1-2 hours.
**Calendar:** 2 days.
**Agent-hours:** 10-17h.

## Success criteria

- [ ] D6 v2 written (30-50 pages)
- [ ] All 22 Gap Analysis adoptions integrated
- [ ] All FPF pattern IDs verified
- [ ] Zero hallucinations (Stage D verifier confirms)
- [ ] 4 independent perspectives captured (Stage B)
- [ ] Companion fpf-tooling.md written (if Stage E executed)
- [ ] Commits + pushes successful
- [ ] Stage 4 (D1-D5 + D7-D8) unblocked
