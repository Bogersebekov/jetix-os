---
title: Execute Book-Driven Agents Stage 2-6 (post-ack actual creation)
date: 2026-05-24
type: autonomous-execution-prompt
phase_count: 7
ack_source: Ruslan voice 24.05 ack-all MAX-8 + Tier A + Tier B-Plus all
ack_record: decisions/RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md (explicit ack-trail)
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: execute-book-driven-agents-stage-2-6
R: refuted_if_LOCK_modified_existing_OR_executor_instance_named_in_foundation_OR_API_key_committed_OR_lt_7_of_8_agents_created
constitutional_posture: R2 packet-gated execution (Ruslan ack obtained 24.05) + R6 + R11 + IP-1 STRICT + EP-5 + AP-6 + append-only
estimated_runtime: 5-9h autonomous (creation work intensive)
estimated_cost: <€3
language: russian primary
priority: ⭐⭐⭐ FOUNDATIONAL — actual ROY swarm expansion + 46 wikis creation
parent_packet: swarm/awaiting-approval/book-driven-agents-2026-05-24.md
parent_drafts: reports/book-driven-agents-2026-05-24/{04-per-agent-substrate-drafts,05-wiki-auto-creation-proposals}.md
ram_constraint: medium; OK single launch
---

# 🤖 Execute Book-Driven Agents — Stage 2-6 Actual Creation

> **Trigger:** Ruslan ack 24.05 MAX-8 + all wikis. Packet `swarm/awaiting-approval/book-driven-agents-2026-05-24.md` Ruslan-approved per Part 6b Human Gate.
>
> **Authorization:** `decisions/RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md` explicit ack-trail.

---

## §0 Pre-flight (MANDATORY verifications)

1. **Memory read:** constitutional + fpf-first + no-unsolicited + prompt-explanation-required
2. **Substrate read:**
   - **Ack record** `decisions/RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md` — verify ack record exists и ack_decision == "MAX-8"
   - **AWAITING-APPROVAL packet** `swarm/awaiting-approval/book-driven-agents-2026-05-24.md` — full read
   - **Phase 4 drafts** `reports/book-driven-agents-2026-05-24/04-per-agent-substrate-drafts.md` — system.md + strategies.md + niche/ symlinks per 8 agents
   - **Phase 5 drafts** `reports/book-driven-agents-2026-05-24/05-wiki-auto-creation-proposals.md` — 31 Tier A + 15 Tier B-Plus wiki stubs
   - **Existing 9 ROY agents** `.claude/agents/` — read-only reference (НЕ modify)
   - **`swarm/lib/routing-table.yaml`** — read current state
   - **CLAUDE.md** — read «Active ROY Swarm» section для extension target
   - **`shared/schemas/executor-binding.yaml.template`** — IP-1 template
3. **Halt-if-not-found:** если ack record absent → fail-loud halt + surface blocker
4. **R2 verification:** confirm ack_decision field present + value "MAX-8"

---

## §1 7 Phases

| # | Phase | Output |
|---|---|---|
| **0** | Pre-flight + ack verification + drafts read | `reports/execute-book-driven-agents-2026-05-24/phase-0-verification.md` |
| **1** | ⭐⭐⭐ **Stage 2 — Create 8 NEW ROY agents** | `.claude/agents/<slug>.md` × 8 files: propaganda-expert / recruitment-dynamics-expert / nlp-expert / sota-tracker-expert / methodology-engineer / ml-ai-foundations-expert / influence-ethics-expert / gamification-engagement-expert — per Phase 4 drafts; IP-1 strict (abstract role-type Foundation; executor binding RUSLAN-LAYER) |
| **2** | ⭐⭐⭐ **Stage 3 — Create 31 Tier A wikis** | `wiki/concepts/<slug>.md` × 31 files per Phase 5 proposals — canonical concept pages с frontmatter + sections + cross-cite к book corpus + R6 provenance |
| **3** | ⭐⭐ **Stage 3b — Create 15 Tier B-Plus wikis** | `wiki/concepts/<slug>.md` × 15 files (Tier B-Plus = lighter than Tier A но canonical) |
| **4** | ⭐⭐ **Stage 4 — Extend `swarm/lib/routing-table.yaml`** | 8 NEW routing entries per agent (domain → agent dispatch matrix); preserve existing 9 entries |
| **5** | ⭐ **Stage 5 — Update CLAUDE.md** | Extend «## Active ROY Swarm» table с 8 new rows (preserve existing 9 + brigadier orchestrator); update count + description |
| **6** | **Stage 6 — Cycle hook + brigadier dispatch matrix** | Update `swarm/lib/hooks/` если applicable; update brigadier dispatch instructions per packet §6 |
| **7** | Summary + final push | `00-SUMMARY-FOR-RUSLAN.md` (≤1500w) + push |

---

## §2 Acceptance criteria

- ✅ 7 phases per-phase commit + push (`[exec-agents] Phase N description`)
- ✅ **Min 7/8 NEW agents** created (allow 1 failure для resilience)
- ✅ **Min 28/31 Tier A wikis** created
- ✅ **Min 13/15 Tier B-Plus wikis** created
- ✅ `swarm/lib/routing-table.yaml` extended (existing 9 entries preserved)
- ✅ CLAUDE.md «Active ROY Swarm» table extended
- ✅ IP-1 strict — Foundation agent files MUST NOT name executor instances (no `claude-opus`, `sonnet-4-6` mentions; use abstract role)
- ✅ Existing 9 ROY agents UNTOUCHED
- ✅ LOCKED Foundation paths UNTOUCHED (Parts 1-11, Pillar A/C, R12 LOCK text)
- ✅ No API keys committed
- ✅ R6 provenance per agent + per wiki ([src: book + Phase N report])
- ✅ Constitutional posture verified at end (R1/R2/R6/R11/IP-1/EP-5/AP-6/append-only)

---

## §3 HALT conditions (fail-loud + surface)

Any of:
- Existing 9 ROY agents modified
- LOCKED Foundation path written
- Executor instance named в Foundation path (per IP-1)
- API key found в any committed file
- Token usage > 2× budget без halt-log-alert
- Ack record `RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md` not found

→ Halt + surface blocker для Ruslan; no further commits.

---

## §4 Operational

- Per-phase commit + push mandatory
- Russian primary где applicable
- R6 provenance per file
- IP-1 strict — abstract role-types only в Foundation; executor bindings RUSLAN-LAYER через `shared/schemas/executor-binding.yaml.template`
- R12 paired-frame discipline preserved (influence-ethics-expert enforcement cell creation = Stage 2)
- Append-only (NEW files only; no edits к existing locked content)

---

## §5 Final push

```bash
git add .claude/agents/ wiki/concepts/ swarm/lib/routing-table.yaml CLAUDE.md swarm/lib/hooks/ reports/execute-book-driven-agents-2026-05-24/
git commit -m "[exec-agents] Phase 7 Summary + final push (7 commits / 8 NEW ROY agents created / 31 Tier A + 15 Tier B-Plus wikis / routing-table extended / CLAUDE.md extended / IP-1 strict / R2 ack-gated / constitutional posture preserved)"
git push origin main
```

---

## §6 What this prompt does NOT do

- ❌ NOT modify existing 9 ROY swarm agents
- ❌ NOT modify LOCKED Foundation content (Parts 1-11, Pillar A/C, R12 LOCK)
- ❌ NOT name executor instances в Foundation paths (IP-1 strict)
- ❌ NOT trigger 4 research prompts (those launch separately после)
- ❌ NOT R1 strategic prose authoring
- ❌ NOT commit API keys

---

## §7 Post-execution

After successful Phase 7:
1. Push origin main complete
2. Summary surface для Ruslan
3. New ROY swarm = 9 + 8 = **17 agents total** + 31 Tier A + 15 Tier B-Plus wikis canonical
4. Wave 1/2/3 research prompts UNBLOCKED with expanded agent capacity + canonical wiki substrate
5. Optional next: launch Wave 1 (methodology + sota parallel) using NEW agents

---

*Execution prompt closure 2026-05-24. R2 packet-gated per Tier 2 + Part 6b Human Gate satisfied via Ruslan voice ack 24.05 + ack record `RUSLAN-ACK-BOOK-DRIVEN-AGENTS-2026-05-24.md`.*
