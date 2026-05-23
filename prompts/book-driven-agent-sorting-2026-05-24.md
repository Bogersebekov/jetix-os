---
title: Book-driven Agent Sorting + ROY Swarm Expansion (server CC autonomous)
date: 2026-05-24
type: autonomous-execution-prompt
phase_count: 8
ack_source: Ruslan voice 24.05 «нормально рассортируется + несколько новых агентов в рой + сами себе википедию создадут»
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2-F3
G: book-driven-agent-sorting
R: refuted_if_LOCK_modified_OR_no_AWAITING_APPROVAL_packet_OR_R1_strategic_prose_authored
constitutional_posture: R1 surface only + R2 STRICT (Foundation modifications need AWAITING-APPROVAL packet) + R6 + R11 + IP-1 STRICT + EP-5 + AP-6 + append-only
estimated_runtime: 4-8h autonomous
estimated_cost: <€3
language: russian primary
priority: ⭐⭐⭐ FOUNDATIONAL — creates new ROY swarm members per book corpus + auto-wikis
parent_pipeline_output: reports/research-corpus-pipeline-2026-05-24/phase-6-bucket-cross-mapping.md
parent_ack: Ruslan voice 24.05 ack-all + agent expansion
prerequisite: Mistral OCR full pass done OR partial OK (substrate ready either way)
ram_constraint: medium; OK parallel с research prompts (different scope)
---

# 🤖 Book-Driven Agent Sorting + ROY Swarm Expansion

> **Trigger:** Ruslan voice 24.05 «нормально рассортируется эти все книги + несколько новых агентов в рой создадим на основе этих книг + если надо сами себе википедию пусть создадут».
>
> **DUAL mandate:**
> 1. **Refine book sorting** beyond Phase 6 bucket cross-mapping
> 2. **Design + propose N new ROY swarm agents** specialized per book corpus domains
> 3. **Auto-create wikis** для agent reference substrate где нужно
>
> ⚠️ **R2 STRICT:** New ROY swarm agents = Foundation infrastructure modification (Part 4 Role Taxonomy + `.claude/agents/` writes + routing-table.yaml updates). MUST produce **AWAITING-APPROVAL packet** для Ruslan ack ДО actual agent creation. Pool result only.

---

## §0 Pre-flight

1. **Memory:** constitutional + research-pool + breadth + fpf-first + no-unsolicited + prompt-explanation-required
2. **Substrate:**
   - **Phase 6 bucket cross-mapping** (`reports/research-corpus-pipeline-2026-05-24/phase-6-bucket-cross-mapping.md`) — primary input
   - **ALL book MDs** (text + OCR'd)
   - Existing ROY swarm: 9 agents в `.claude/agents/` (brigadier + 5 experts + 4 sub-brigadiers)
   - **`swarm/lib/routing-table.yaml`** — routing canonical
   - **Part 4 Role Taxonomy** (`swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/`)
   - **IP-1 Role≠Executor** (Foundation roles = U.Episteme abstract; executor bindings = RUSLAN-LAYER)
   - Existing 13 Tier A wikis + 3 NEW из Point B compact (development-promotion-mode-transition / notion-mvp-bypass / cohort-target-profile)
3. **R2 enforcement:** ALL agent creation gated через AWAITING-APPROVAL packet — surface options, не auto-create

---

## §1 8 Phases

| # | Phase | Output |
|---|---|---|
| **0** | Pre-flight + Phase 6 cross-mapping read + existing ROY swarm inventory | `reports/book-driven-agents-2026-05-24/phase-0-substrate.md` |
| **1** | ⭐⭐ **Book corpus knowledge-domain extraction** — per ~80 books: primary domain + secondary domains + key concepts/methods/frameworks + author tradition lineage | `01-corpus-knowledge-domains.md` (~600 lines / 80 books × structured profile) |
| **2** | ⭐ **Refined sorting** — beyond 4 buckets (P/S/M/N) → propose deeper taxonomy (e.g. P → propaganda-classical / propaganda-modern / recruitment-mass-movements / community-formation) | `02-refined-taxonomy.md` (~400 lines + visualization) |
| **3** | ⭐⭐⭐ **Agent topology design** — propose 5-10 NEW ROY swarm member candidates (per knowledge-domain cluster); per candidate: name / role / domain / required books / methods / IP-1 abstract role spec | `03-agent-topology-proposal.md` (~800 lines) — **R1 surface only, не auto-create** |
| **4** | ⭐ **Per-agent substrate design** — per proposed agent: system.md draft / strategies.md initial / niche/ symlinks к relevant book MDs + wikis | `04-per-agent-substrate-drafts.md` (~600 lines) — drafts только; **NOT writing actual files** |
| **5** | ⭐⭐ **Wiki auto-creation proposals** — для each agent identify gaps в existing wikis; propose NEW Tier B-Plus / Tier A wikis per knowledge domain (например: `wiki/concepts/propaganda-six-techniques.md` derived from Bernays+Lippmann+Ellul) | `05-wiki-auto-creation-proposals.md` (~500 lines) — drafts; **NOT writing actual wikis** |
| **6** | ⭐⭐⭐ **AWAITING-APPROVAL packet** — per Tier 2 R2 + Part 6b Human Gate: package agent topology + substrate drafts + wiki proposals для Ruslan strategic ack | `swarm/awaiting-approval/book-driven-agents-2026-05-24.md` (formal packet per shared/schemas) |
| **7** | Summary + final push | `00-SUMMARY-FOR-RUSLAN.md` (≤1500w) с overall picture + per-agent value-prop + Ruslan ack queue (D-NN items) |

---

## §2 Candidate agents — 5-10 design space (Phase 3 expand)

**Conceptual seeds (Phase 3 refines, не auto-locks):**

| Candidate | Domain | Required books |
|---|---|---|
| **propaganda-expert** | mass communication + persuasion ethics | Bernays + Lippmann + Ellul + Chomsky-Herman + Cialdini + Le Bon + Freud |
| **recruitment-dynamics-expert** | mass movement formation + cohort recruitment | Hoffer + Lifton + Hassan + Henrich + Ostrom + Raymond + Srinivasan |
| **nlp-expert** | communication tactics + reframing (R12-bounded) | Bandler+Grinder + Dilts + Andreas + O'Connor + Robbins + Bolton + Witkowski critical review |
| **sota-tracker-expert** | philosophy of science + SOTA tracking discipline | Popper + Kuhn + Lakatos + Feyerabend + Laudan + Hacking + Longino + Chalmers |
| **methodology-engineer** | methodology as discipline + method-engineering | Polya + Polanyi + Levenchuk × 5 + Schedrovitsky + OMG Essence + Senge + Beer + Ashby + Meadows + Ackoff + Schön |
| **cybernetics-systems-expert** | cybernetics + systems thinking deep | Wiener + Ashby + Beer + Maturana + Meadows + Senge + Bateson + Ackoff + Weinberg |
| **ml-ai-foundations-expert** | AI/ML foundations + SOTA tracking | Goodfellow + Huyen + Karpathy + Askell HHH + Bai CAI + Mitchell complexity |
| **complexity-emergence-expert** | complexity science + emergence | Mitchell + Beinhocker + Kauffman + Dawkins + Dennett |
| **influence-ethics-expert** | influence tactics ethics R12-boundary | Cialdini + Greene + Lifton + Hassan + Witkowski critical + Askell HHH |
| **adjacent-thinking-expert** | adjacent fields cross-pollination | Carse + Taleb + Holiday + Jorgenson + Buffett + Graham + Marks + Munger |

⚠️ Phase 3 explicitly **proposes**, не locks. Ruslan picks final set + names + scope per AWAITING-APPROVAL packet ack.

---

## §3 R2 STRICT — Foundation modification discipline

**MANDATORY:** все следующие = Foundation infrastructure writes требующие AWAITING-APPROVAL packet:

- Creating new `.claude/agents/<slug>.md` files
- Updating `swarm/lib/routing-table.yaml` с new agent entries
- Updating Part 4 Role Taxonomy
- Auto-creating new Tier A wikis (Tier B pool OK без packet; Tier A requires)
- Updating `.claude/config/default-deny-table.yaml`

**This prompt:** drafts ONLY. Phase 6 packet формирует. Ruslan ack → следующая session (или server CC sequel prompt) делает actual writes.

---

## §4 Acceptance criteria

- ✅ 8 phases per-phase commit + push (`[book-agents] Phase N`)
- ✅ Phase 1 — 80 books × structured knowledge-domain profile
- ✅ Phase 3 — 5-10 NEW agent candidates proposed (not auto-locked)
- ✅ Phase 4 — per-agent system.md + strategies.md DRAFTS (не actual files)
- ✅ Phase 5 — wiki proposals (drafts) + identify gaps
- ✅ Phase 6 — **AWAITING-APPROVAL packet formal** per Tier 2 R2 + Part 6b
- ✅ R2 STRICT — NO autonomous Foundation modifications
- ✅ R1 surface only — Ruslan picks
- ✅ IP-1 strict — Foundation = abstract role-types; executor bindings RUSLAN-LAYER
- ✅ Constitutional posture preserved (R1/R2/R6/R11/IP-1/EP-5/AP-6/append-only)

---

## §5 §11.0 CRITICAL IMPORTANCE MANDATE — APPLIES selectively

- **Phase 1-2 substrate compile** — apply MAX-density (book corpus extraction = deep work)
- **Phase 3-5 agent design** — normal density (R1 design choices = Ruslan's)
- **Phase 6 packet** — formal compliance, no embellishment
- ROY 500% Phase 1-2 OK

---

## §6 Operational

- Per-phase commit + push
- Russian primary (Russian books like Левенчук / Щедровицкий)
- R6 provenance per book extraction
- R12 paired-frame check для influence-ethics agent design
- NO Foundation auto-writes
- Pool result only

---

## §7 Final push

```bash
git add reports/book-driven-agents-2026-05-24/ swarm/awaiting-approval/book-driven-agents-2026-05-24.md
git commit -m "[book-agents] Phase 7 Summary + AWAITING-APPROVAL packet + final push (8 commits / NN candidate agents proposed / NN wiki proposals / R2 STRICT preserved / Ruslan ack queue ready)"
git push origin main
```

---

## §8 What this prompt does NOT do

- ❌ NOT auto-create new ROY swarm agents (R2 strict)
- ❌ NOT auto-write new Tier A wikis (требует Ruslan ack per Tier 2)
- ❌ NOT modify routing-table.yaml автоматически
- ❌ NOT modify existing 9 ROY swarm agents
- ❌ NOT R1 strategic prose authoring
- ❌ NOT trigger 4 research prompts (separate Wave 1/2/3)
- ❌ NOT auto-promote pool items beyond AWAITING-APPROVAL packet inventory

---

*Prompt closure 2026-05-24. R2 STRICT enforcement mandatory — Foundation infrastructure changes ВСЕГДА through AWAITING-APPROVAL packet per Part 6b Human Gate.*
