---
type: launcher-document
date: 2026-05-18 evening
session: launch-5-deep-research-runs-2026-05-18
parent_meta: prompts/meta-generate-5-deep-research-prompts-2026-05-18.md
status: READY-TO-LAUNCH (Ruslan executes copy-paste commands)
constitutional_posture: R1 surface + R11 + append-only
language: russian + english
audience: Ruslan (primary operator)
expected_completion: 2-3 hours wall time (longest run dominates) / <€16 combined cost
---

# LAUNCHER — 5 Deep Research Runs

> **Что это.** Copy-paste launcher для 5 параллельных deep research runs (Hackathon Platform / Recursive Engine / System Merger / Outreach Scalable / Education Layer). Все 5 prompts + EXPLAIN siblings ready. Ruslan executes commands.

> **Parallel-safe.** Все 5 runs использует different namespaces в `research/`; no interdependencies. Каждый run completes independently.

> **Constitutional posture.** R1 (Ruslan = sole strategist; brigadier-scribe только authoring) + R11 (Default-Deny novel actions) preserved across all 5. Foundation / Pillar C / Schemas / VISION-FUNDAMENTAL / 8 Octagon LOCK content READ-ONLY across all 5.

---

## §0 Pre-flight checks (run ONCE before all 5)

```bash
cd ~/jetix-os && \
git pull --rebase --autostash && \
git log --oneline -5 && \
tmux ls 2>/dev/null || echo "(no existing tmux sessions)" && \
mkdir -p logs && \
echo "Ready to launch 5 deep research runs"
```

**Expected output:**
- `git pull` returns Already up to date OR pulls latest
- Last 5 commits include meta-prompt + launcher + 2 NEW prompts + EXPLAIN
- tmux session list (empty OK)
- `logs/` directory created

---

## §1 5 Parallel Launches (copy-paste each блок)

### Run 1 — Hackathon Platform Deep Research

```bash
tmux new -d -s hp-deep "claude --dangerously-skip-permissions"
```

Attach + paste prompt:
```bash
tmux attach -t hp-deep
```

```
ultrathink. Прочитай _EXPLAIN-hackathon-platform-deep-research-2026-05-18.md и prompts/hackathon-platform-deep-research-2026-05-18.md. Выполни все автономно, 8 phases, per-phase commit, final push origin main. Ruslan acked. Не пауза.
```

Detach: `Ctrl-b` → `d`

**Scope:** 30+ platform variants survey + per-rhythm spec + cohort dynamics + sponsor + funding mechanisms + first event Q3 2026 blueprint + multi-rhythm Year-1 calendar + 30-50 H bank + 10+ mermaid.
**Namespace:** `research/hackathon-platform-deep-2026-05-18/`
**Duration:** 120-180 min / <€3.50

---

### Run 2 — Recursive Self-Development Engine Deep Research (IP-1 STRICT)

```bash
tmux new -d -s re-deep "claude --dangerously-skip-permissions"
```

Attach + paste prompt:
```bash
tmux attach -t re-deep
```

```
ultrathink. Прочитай _EXPLAIN-recursive-self-development-engine-deep-research-2026-05-18.md и prompts/recursive-self-development-engine-deep-research-2026-05-18.md. IP-1 STRICT throughout — pattern = abstract method; instances bound к executors per RUSLAN-LAYER. Выполни все автономно, 8 phases, per-phase commit, final push origin main. Ruslan acked. Не пауза.
```

Detach: `Ctrl-b` → `d`

**Scope:** Engelbart H-LAM/T 1962 verbatim + NASA SE 15-of-17 deep map + Plan-mode primitive catalog + Execute-mode primitive catalog + TPS Hansei/Kaizen + IP-1 boundary cases (≥10 entries) + 5 plan-execute cycles 1-week trial + 20-30 H bank + 8+ mermaid.
**Namespace:** `research/recursive-engine-deep-2026-05-18/`
**Duration:** 100-150 min / <€3
**Critical caveat:** IP-1 STRICT — каждый strategic claim проверяется. Halt immediate on IP-1 violation.

---

### Run 3 — System Merger Protocol Deep Research (H9 candidate)

```bash
tmux new -d -s sm-deep "claude --dangerously-skip-permissions"
```

Attach + paste prompt:
```bash
tmux attach -t sm-deep
```

```
ultrathink. Прочитай _EXPLAIN-system-merger-protocol-deep-research-2026-05-18.md и prompts/system-merger-protocol-deep-research-2026-05-18.md. Выполни все автономно, 8 phases, per-phase commit, final push origin main. Ruslan acked. Не пауза.
```

Detach: `Ctrl-b` → `d`

**Scope:** 4-precedent deep mining (USB-C/TCP-IP/HTTP/OpenAPI+GraphQL) + M&A academic playbook + 2 sub-protocols formalisation (намордник + USB-C порт) + Strategic Q decision matrix (A/B/C surface) + first merger test case (2 AI companies) + R12 programmable enforcement + 25-35 H bank + 8+ mermaid + H9 LOCK readiness evidence.
**Namespace:** `research/system-merger-deep-2026-05-18/`
**Duration:** 120-180 min / <€3.50

---

### Run 4 — Outreach System Scalable Deep Research

```bash
tmux new -d -s os-deep "claude --dangerously-skip-permissions"
```

Attach + paste prompt:
```bash
tmux attach -t os-deep
```

```
ultrathink. Прочитай _EXPLAIN-outreach-system-scalable-deep-research-2026-05-18.md и prompts/outreach-system-scalable-deep-research-2026-05-18.md. R12 anti-extraction foregrounded throughout. Выполни все автономно, 8 phases, per-phase commit, final push origin main. Ruslan acked. Не пауза.
```

Detach: `Ctrl-b` → `d`

**Scope:** 6-precedent deep mining (Sahil/Chen/Naval/Levels/GitHub/YC) + 6-resources framework 4-taxonomy surface + 10-person video team operationalised (5 roles × deep spec) + 100-trained cohort 4-tier training + personalized outreach mechanism (LLM-assist + human craft) + 6 target audience classes × tier prioritisation + 25-37 H bank + 10+ mermaid.
**Namespace:** `research/outreach-deep-2026-05-18/`
**Duration:** 120-180 min / <€3.50
**Critical caveat:** R12 anti-extraction — per-stage R12 check explicit; halt immediate on R12 violation.

---

### Run 5 — Education Layer System Thinking Deep Research (Paternalism + IP-1 Phase 5)

```bash
tmux new -d -s el-deep "claude --dangerously-skip-permissions"
```

Attach + paste prompt:
```bash
tmux attach -t el-deep
```

```
ultrathink. Прочитай _EXPLAIN-education-layer-system-thinking-deep-research-2026-05-18.md и prompts/education-layer-system-thinking-deep-research-2026-05-18.md. Paternalism mitigation foregrounded throughout. IP-1 STRICT в Phase 5 (gratitude operationalisation). Выполни все автономно, 8 phases, per-phase commit, final push origin main. Ruslan acked. Не пауза.
```

Detach: `Ctrl-b` → `d`

**Scope:** 7-precedent deep mining (Harari/Karpathy/Engelbart/ШАД/NASA/Meadows/Beer) + Tier 1 Foundation 5-7 module curriculum + NASA life/work/body-as-spaceship (7 processes × 3 scales) + Master-Apprentice 4-role typology + Hackathon = Tier 3 activation + gratitude prophecy IP-1 STRICT operationalisation + «Базовое образование» Options A/B/C/D + cohort progression sequencing + 25-37 H bank + 10+ mermaid.
**Namespace:** `research/education-layer-deep-2026-05-18/`
**Duration:** 120-180 min / <€3.50
**Critical caveats:** Paternalism mitigation foregrounded; IP-1 STRICT в Phase 5.

---

## §2 Verify all 5 running

```bash
tmux ls
# Expected output:
# hp-deep: 1 windows (created ...) [...]
# re-deep: 1 windows (created ...) [...]
# sm-deep: 1 windows (created ...) [...]
# os-deep: 1 windows (created ...) [...]
# el-deep: 1 windows (created ...) [...]
```

Если какая-то session missing → check log:
```bash
ls -lt logs/ | head -5
tail -50 logs/<run>-*.log
```

---

## §3 Watch progress

### Attach к specific run
```bash
tmux attach -t hp-deep      # Run 1
tmux attach -t re-deep      # Run 2
tmux attach -t sm-deep      # Run 3
tmux attach -t os-deep      # Run 4
tmux attach -t el-deep      # Run 5

# Detach: Ctrl-b → d (session continues running)
```

### Tail log без attach
```bash
tail -f logs/hp-deep-*.log
tail -f logs/re-deep-*.log
tail -f logs/sm-deep-*.log
tail -f logs/os-deep-*.log
tail -f logs/el-deep-*.log

# Ctrl-c to stop tail (run continues)
```

### Tail all 5 logs in parallel
```bash
tail -f logs/hp-deep-*.log logs/re-deep-*.log logs/sm-deep-*.log logs/os-deep-*.log logs/el-deep-*.log
```

---

## §4 Halt all 5 (only if emergency)

```bash
for sess in hp-deep re-deep sm-deep os-deep el-deep; do
  tmux kill-session -t $sess 2>/dev/null && echo "killed: $sess" || echo "not running: $sess"
done
```

**When to halt:**
- Constitutional violation reported (R1/R2/R6/R11/R12/IP-1) → halt corresponding run + investigate
- Cost approaching €5 per run (>€25 combined) → halt all + escalate
- Network issues / API errors >50% → halt + retry later

---

## §5 Diagnostic commands

### Git activity (per-phase commits expected)
```bash
git log --oneline -30
# Expected: 9 commits per run × 5 runs = up to 45 new commits

# Filter by run namespace
git log --oneline --all -- 'research/hackathon-platform-deep-2026-05-18/*'
git log --oneline --all -- 'research/recursive-engine-deep-2026-05-18/*'
git log --oneline --all -- 'research/system-merger-deep-2026-05-18/*'
git log --oneline --all -- 'research/outreach-deep-2026-05-18/*'
git log --oneline --all -- 'research/education-layer-deep-2026-05-18/*'
```

### Per-run output verification
```bash
ls -la research/hackathon-platform-deep-2026-05-18/
ls -la research/recursive-engine-deep-2026-05-18/
ls -la research/system-merger-deep-2026-05-18/
ls -la research/outreach-deep-2026-05-18/
ls -la research/education-layer-deep-2026-05-18/

# Expected per run: 10-15 markdown docs + diagrams/ subdir
```

### Pull updates from all runs
```bash
git pull --ff-only
```

### Cost monitoring
External — https://console.anthropic.com/ dashboard. Expected: ~€3-3.50 per run × 5 = <€16-17.50 combined.

---

## §6 Expected completion

| Item | Per run | Combined (5 runs) |
|---|---|---|
| Wall time | 100-180 min | 2-3 hours (longest dominates) |
| Cost | <€3.50 (avg €3) | <€16-17.50 |
| New docs | 10-15 markdown | 50-75 docs |
| Mermaid diagrams | 8-10 | 40-50 diagrams |
| Hypotheses | 20-37 H bank | 100-200 H total |
| Per-phase commits | 9 | up to 45 commits |

---

## §7 Post-completion

Когда все 5 sessions показывают «DONE Phase 8» в respective logs:

### 1. Pull updates
```bash
cd ~/jetix-os && git pull --ff-only
```

### 2. Read all 5 Summary-for-Ruslan files
```bash
cat research/hackathon-platform-deep-2026-05-18/99-SUMMARY-FOR-RUSLAN.md
cat research/recursive-engine-deep-2026-05-18/99-SUMMARY-FOR-RUSLAN.md
cat research/system-merger-deep-2026-05-18/99-SUMMARY-FOR-RUSLAN.md
cat research/outreach-deep-2026-05-18/99-SUMMARY-FOR-RUSLAN.md
cat research/education-layer-deep-2026-05-18/99-SUMMARY-FOR-RUSLAN.md
```

### 3. Surface top insights
- Brigadier (Cloud Cowork) reads all 5 summaries
- Synthesizes top insights cross-cutting all 5 streams
- Surfaces к Ruslan top P1/P2/P3 actionable items
- Surfaces AWAITING-APPROVAL packet candidates (если applicable)
- Surfaces concept doc F3 promotion readiness (A/B/C/D/E concepts → which ready)

### 4. Cleanup tmux sessions
```bash
for sess in hp-deep re-deep sm-deep os-deep el-deep; do
  tmux kill-session -t $sess 2>/dev/null && echo "cleaned: $sess"
done
```

---

## §8 Sequence recommendation

**Default: ALL 5 PARALLEL (recommended).**

Все 5 runs использует different namespaces; no interdependencies. Maximum throughput.

**Alternative: SEQUENTIAL (если cost concern OR debug new prompts):**

```bash
# Sequential — launch one at a time
# Wait for each to complete before launching next
# Useful for debugging or if Anthropic rate limits trigger

# Order recommendation:
# 1. Hackathon Platform (highest priority growth vehicle)
# 2. Outreach System (operationalisation для Phase 1 execution)
# 3. Recursive Engine (meta-pattern для всех runs)
# 4. System Merger (H9 candidate readiness)
# 5. Education Layer (paternalism + IP-1 complex; lowest urgency)
```

**Alternative: BATCHED 3+2:**

```bash
# Batch 1: Hackathon + Outreach + Recursive Engine (3 parallel)
# Wait for all 3 → review summaries
# Batch 2: System Merger + Education Layer (2 parallel)
```

---

## §9 Constitutional preservation check

Per-run halt conditions enforced (per prompts §11):
- R1 violation → halt + escalate
- R2 Foundation read-only violation → halt + escalate
- R6 provenance gap → halt + diagnose
- R11 Default-Deny violation → halt + escalate
- R12 anti-extraction violation (Outreach especially) → IMMEDIATE halt + escalate
- IP-1 violation (Recursive + Education Phase 5) → IMMEDIATE halt + escalate
- Paternalism foregrounding missing (Education) → halt + diagnose

NOT-modified across all 5 runs:
- Foundation v1.0 / Pillar C 12 rules / shared/schemas / VISION-FUNDAMENTAL
- 8 Octagon LOCK content
- AWAITING-APPROVAL packets content (cross-reference only)
- CRM live records (voice-pipeline DRAFT discipline)

---

## §10 Reference index

### Prompts (5 deep research):
- [prompts/hackathon-platform-deep-research-2026-05-18.md](prompts/hackathon-platform-deep-research-2026-05-18.md)
- [prompts/recursive-self-development-engine-deep-research-2026-05-18.md](prompts/recursive-self-development-engine-deep-research-2026-05-18.md)
- [prompts/system-merger-protocol-deep-research-2026-05-18.md](prompts/system-merger-protocol-deep-research-2026-05-18.md)
- [prompts/outreach-system-scalable-deep-research-2026-05-18.md](prompts/outreach-system-scalable-deep-research-2026-05-18.md)
- [prompts/education-layer-system-thinking-deep-research-2026-05-18.md](prompts/education-layer-system-thinking-deep-research-2026-05-18.md)

### EXPLAIN siblings (5):
- [_EXPLAIN-hackathon-platform-deep-research-2026-05-18.md](_EXPLAIN-hackathon-platform-deep-research-2026-05-18.md)
- [_EXPLAIN-recursive-self-development-engine-deep-research-2026-05-18.md](_EXPLAIN-recursive-self-development-engine-deep-research-2026-05-18.md)
- [_EXPLAIN-system-merger-protocol-deep-research-2026-05-18.md](_EXPLAIN-system-merger-protocol-deep-research-2026-05-18.md)
- [_EXPLAIN-outreach-system-scalable-deep-research-2026-05-18.md](_EXPLAIN-outreach-system-scalable-deep-research-2026-05-18.md)
- [_EXPLAIN-education-layer-system-thinking-deep-research-2026-05-18.md](_EXPLAIN-education-layer-system-thinking-deep-research-2026-05-18.md)

### Concept docs (5 acked F2 parents):
- [decisions/strategic/JETIX-AS-HACKATHON-PLATFORM-2026-05-18.md](decisions/strategic/JETIX-AS-HACKATHON-PLATFORM-2026-05-18.md)
- [decisions/strategic/JETIX-RECURSIVE-SELF-DEVELOPMENT-ENGINE-2026-05-18.md](decisions/strategic/JETIX-RECURSIVE-SELF-DEVELOPMENT-ENGINE-2026-05-18.md)
- [decisions/strategic/JETIX-SYSTEM-MERGER-PROTOCOL-FPF-2026-05-18.md](decisions/strategic/JETIX-SYSTEM-MERGER-PROTOCOL-FPF-2026-05-18.md)
- [decisions/strategic/JETIX-OUTREACH-SYSTEM-SCALABLE-2026-05-18.md](decisions/strategic/JETIX-OUTREACH-SYSTEM-SCALABLE-2026-05-18.md)
- [decisions/strategic/JETIX-EDUCATION-LAYER-SYSTEM-THINKING-2026-05-18.md](decisions/strategic/JETIX-EDUCATION-LAYER-SYSTEM-THINKING-2026-05-18.md)

### Meta + Master Picture:
- [prompts/meta-generate-5-deep-research-prompts-2026-05-18.md](prompts/meta-generate-5-deep-research-prompts-2026-05-18.md) (this meta-run parent)
- [prompts/_META-quality-assessment-2026-05-18.md](prompts/_META-quality-assessment-2026-05-18.md) (Phase 1 output)
- [_MASTER-PICTURE-NEXT-STEPS-2026-05-18.md](_MASTER-PICTURE-NEXT-STEPS-2026-05-18.md) (Master Picture)

### Voice anchors:
- [raw/voice-memos-2026-05-17-batch/text_008@2026-05-18_evening.md](raw/voice-memos-2026-05-17-batch/text_008@2026-05-18_evening.md)
- [raw/voice-memos-2026-05-17-batch/text_009@2026-05-18_evening.md](raw/voice-memos-2026-05-17-batch/text_009@2026-05-18_evening.md)

---

## §11 Acceptance test (self-check before launching)

Ruslan verifies:
- [ ] Cloud Cowork: `cat _LAUNCH-5-DEEP-RESEARCH-2026-05-18.md` opens fine
- [ ] All 5 prompt files exist in `prompts/`
- [ ] All 5 EXPLAIN siblings exist in repo root
- [ ] `tmux` available (`which tmux`)
- [ ] `claude` CLI available (`which claude`)
- [ ] `mkdir -p logs/` succeeds
- [ ] `git pull --rebase --autostash` clean (no conflicts)
- [ ] Disk space sufficient (>5GB for all 5 runs output + logs)
- [ ] Anthropic API key configured (check console.anthropic.com)

---

## §12 Жми

Когда готов — copy-paste §0 pre-flight, потом §1 5 launch commands. Watch progress §3. Wait 2-3 hours. Post-completion §7.

Если возникает проблема — §4 halt commands. Debug via §5 diagnostic. Single-run retry: re-launch corresponding §1 block.

**Constitutional posture preserved across all 5 runs:** R1 + R6 + R11 + R12 + IP-1 (где applicable) + EP-5 + breadth-NOT-selection + FPF-lens-FIRST + paternalism-mitigation (Education) + append-only.

**Ruslan acked.** Brigadier-scribe (R1 surface). 5 deep research runs ready.

---

*Launcher document 2026-05-18 evening. brigadier-scribe (R1 surface). Ruslan launches 5 runs → waits 2-3h → reads 5 summaries → surface top insights.*
