---
title: Phase 0 — Pre-flight substrate (book-driven agent sorting + ROY swarm expansion)
date: 2026-05-24
phase: 0/7
parent_prompt: prompts/book-driven-agent-sorting-2026-05-24.md
constitutional_posture: R1 surface + R2 STRICT + R6 + IP-1 strict + AP-6 + append-only
prose_authored_by: brigadier-scribe (server CC autonomous)
F: F2
G: book-driven-agents-phase-0
R: refuted_if_substrate_inventory_mismatches_Phase_6_count_OR_ROY_swarm_inventory_drifts
---

# Phase 0 — Pre-flight substrate

## §0.1 Memory + constitutional alignment

- **Constitutional posture:** R1 surface only (Ruslan = sole strategist), R2 STRICT (Foundation infrastructure modifications via AWAITING-APPROVAL packet ONLY), R6 (provenance per book), R11 (Default-Deny on novel actions), R12 (paired-frame anti-extraction check applies to influence-ethics agent candidate), IP-1 strict (Foundation roles = U.Episteme abstract; executor bindings = RUSLAN-LAYER separate)
- **Mandate:** DUAL — (1) refine book sorting beyond Phase 6 4-bucket P/S/M/N → deeper taxonomy; (2) propose 5–10 NEW ROY swarm member candidates per knowledge-domain clusters; (3) draft per-agent system.md + strategies.md + niche/ symlinks; (4) propose wikis auto-creation; (5) Phase 6 = formal AWAITING-APPROVAL packet
- **NOT:** auto-create agents, auto-write wikis, auto-modify routing-table.yaml, auto-modify existing 9 ROY swarm agents, R1 strategic prose authoring

## §0.2 Substrate inventory (verified read)

### A. Primary input — Phase 6 bucket cross-mapping
- **Path:** `reports/research-corpus-pipeline-2026-05-24/phase-6-bucket-cross-mapping.md` (367 lines, F2)
- **Status:** READ — 80 books mapped across 4 buckets P/S/M/N with multi-bucket assignments
- **Key counts:** 22 P=core / 14 S=core / 22 M=core / 10 N=core books. 1 duplicate flagged (cialdini-influence-1984 EN vs RU). 11 OCR'd via Mistral Phase 1–3 (full coverage).
- **Cross-bucket findings:** Polanyi spans M+S; Kahneman spans P+S+M; NLP+Bolton+Robbins = N+P dual; Schelling = S+M+P; Levenchuk all M=3 (intellekt-stek also S=3); 17.pdf = Shchedrovitsky (Russian M canon); gamification corpus (13) = mostly P=2-3 + M=2 dual.

### B. Book corpora (full inventory)

| Corpus root | Path | MD count | OCR'd | Status |
|---|---|---|---|---|
| **research-corpus-2026-05-23 / methodology** | `raw/external/research-corpus-2026-05-23/methodology/` | 9 main | 2 OCR'd (schon-1987, dijkstra-1969) | F2 ready |
| **research-corpus-2026-05-23 / nlp** | `raw/external/research-corpus-2026-05-23/nlp/` | 12 main | 2 OCR'd (dilts-encyclopedia, bandler-trance) | F2 ready |
| **research-corpus-2026-05-23 / propaganda-recruitment** | `raw/external/research-corpus-2026-05-23/propaganda-recruitment/` | 20 main | 4 OCR'd (bernays×2, le-bon, freud) | F2 ready |
| **research-corpus-2026-05-23 / sota** | `raw/external/research-corpus-2026-05-23/sota/` | 11 main | 3 OCR'd (goodfellow-2016, hacking-1983, laudan-1977) | F2 ready |
| **research-corpus-2026-05-23 / _unknown** | `raw/external/research-corpus-2026-05-23/_unknown/` | 3 main | 0 | F2 ready |
| **gamification papers-pdf** | `raw/papers-pdf/gamification/` | 13 main | n/a (text-extract) | F2 ready |
| **levenchuk-books converted** | `raw/external/levenchuk-books-2026-05-20/converted/` | 5 main | n/a | F2 ready |
| **inbox / anthropic** | `inbox/anthropic/` | 2 (askell-2021-hhh, bai-2022-cai) | n/a | F2 ready |
| **inbox / event-sourcing** | `inbox/event-sourcing/young-cqrs-2010.md` | 1 | n/a | F2 ready |
| **inbox / sre** | `inbox/sre/google-sre-book.md` | 1 | n/a | F2 ready |
| **arxiv articles** | `raw/articles/arxiv-*.md` | 3 (qian-scaling, cemri-mast, kim-mas) | n/a | F2 ready |

**TOTAL canonical inventory:** 80 books (Phase 6 mapping authoritative; 56 of 80 inside research-corpus-2026-05-23 + 13 gamification + 5 Levenchuk + 2 anthropic + 1 event-sourcing + 1 SRE + 3 arxiv).

**Match with Phase 6 §6.2 matrix** (A through K sections): 9 + 12 + 20 + 11 + 3 + 2 + 1 + 1 + 3 + 5 + 13 = **80 books** ✅

### C. Existing ROY swarm inventory (DO NOT MODIFY per prompt §8)

9 agents в `.claude/agents/` (matches CLAUDE.md `## Active ROY Swarm`):

| Slug | Role | Domain lens | Coverage of book corpus |
|---|---|---|---|
| `brigadier` | Orchestrator | Routing + synthesis + HITL gate; no domain expertise | n/a (meta) |
| `engineering-expert` | ROY expert | Compounding-eng + clean-code + Unix + AI-native + architecture | Partial: goodfellow / huyen / google-sre / knuth / dijkstra / young-cqrs (S+M engineering subset) |
| `investor-expert` | ROY expert | Capital allocation + unit-econ + moats + long-term compounding | None in current corpus (Buffett/Graham/Marks/Munger appear ONLY в adjacent-thinking-expert seed) |
| `mgmt-expert` | ROY expert | PM + delivery + ethics-surface + stakeholder | Partial: ackoff / drucker / cagan (NOT in 80-book corpus); senge / ostrom touch |
| `philosophy-expert` | ROY expert | Phil-sci + epistemology + mental models + stoic | STRONG: Popper / Kuhn / Lakatos / Feyerabend / Laudan / Hacking / Longino / Chalmers / Polanyi / Menand / Merleau-Ponty (≥11 books P+S quartet covered) |
| `systems-expert` | ROY expert | Systems-thinking + cybernetics + complexity + biology (Meadows / Ashby / Beer / Senge / Kauffman) | Partial: Senge / Ackoff (NOT in 80-book core); MMK indirect via Shchedrovitsky |
| `project-brigadier` | Mini-swarm template | Project-scope dispatch (≤7 active tasks) | n/a (orchestrator template) |
| `quick-money-brigadier` | Mini-swarm | quick-money P1 project | n/a (project orchestrator) |
| `levenchuk-deep-dive-brigadier` | Mini-swarm stub | Levenchuk P3 deep-dive (stub — no mini-swarm spawned per /project-bootstrap §8) | Implicit: Levenchuk ×5 books |

### D. Coverage GAPS identified (motivating Phase 3 candidate proposals)

| Knowledge cluster | Book mass | Current ROY coverage | Gap signal |
|---|---|---|---|
| **Propaganda + persuasion + crowd/group psychology** | 22 P=3 + 13 P=2 (≥35 books) | ZERO dedicated expert (mgmt-expert touches ethics-surface but not 6-techniques canon) | ⭐⭐⭐ STRONG candidate trigger |
| **NLP + verbal-reframing + influence techniques** | 10 N=3 + 4 N=2 (14 books canon) | ZERO; engineering-expert clean-code lens orthogonal | ⭐⭐⭐ STRONG candidate trigger |
| **Cult / mass-movement recruitment** | Hoffer + Lifton + Hassan + Henrich (4 core books for recruitment dynamics) | ZERO; partial mgmt-expert overlap on stakeholder dynamics | ⭐⭐ candidate trigger |
| **Philosophy of science SOTA tracking discipline** | 8 phil-sci books (Popper / Kuhn / Lakatos / Feyerabend / Laudan / Hacking / Longino / Chalmers) | philosophy-expert covers — но **SOTA-tracking discipline** ≠ philosophy-expert (latter is epistemic audit; sota = method discipline for tracking field state) | ⭐⭐ candidate trigger (specialization split) |
| **Methodology engineering / method-as-discipline** | Polya / Schön / Lakatos / Feyerabend / Senge / Beer / Ashby / Meadows / Ackoff / OMG Essence / Shchedrovitsky / Levenchuk ×5 / Climate-KIC (≥18 books M=3) | systems-expert overlaps (cybernetics subset) + mgmt-expert (delivery); но NO dedicated **method-engineering** agent | ⭐⭐⭐ STRONG candidate trigger |
| **Cybernetics + systems thinking deep canon** | Wiener / Ashby / Beer / Maturana / Meadows / Senge / Bateson / Ackoff / Weinberg (Phase 6 list theoretical; few are в 80-book corpus directly — Senge SUMMARY-only) | systems-expert already covers — но deep canon NOT fully in 80-book corpus → candidate is **upgrade**, not new | ⭐ low (covered) |
| **ML / AI foundations + alignment** | Goodfellow / Huyen / Askell HHH / Bai CAI / arxiv ×3 / Karpathy (Karpathy not in 80) | engineering-expert touches deployment subset; NO ai-safety / alignment / SOTA-tracking ml lens | ⭐⭐ candidate trigger |
| **Complexity + emergence + evolution** | Henrich (cultural evo) + Mitchell? (not in 80) + Kauffman? (not) + Dawkins/Dennett? (not) | systems-expert touches complexity broadly но evolution/cultural lens absent | ⭐⭐ (gap exists; weaker book mass in 80 corpus) |
| **Influence ethics (R12 paired-frame boundary)** | Cialdini × 2 + Greene + Lifton + Hassan + Witkowski critical + Askell HHH (≥6 books with explicit ethics-of-influence framing) | NO dedicated ethics-of-influence; philosophy-expert + mgmt-expert touch ethics-surface generically | ⭐⭐⭐ STRONG candidate trigger (R12 anti-extraction compatibility critical) |
| **Adjacent fields cross-pollination** | Carse / Taleb / Holiday / Jorgenson / Buffett / Graham / Marks / Munger (mostly NOT in 80-book corpus — seed names from prompt §2) | crazy-agent legacy archived; investor-expert touches Buffett-style capital lens но not adjacency disciplined cross-domain | ⭐ (weak book mass in 80; candidate weaker on substrate) |
| **Game design + gamification methodology** | 13 gamification books (Csikszentmihalyi / Eyal / Koster / Salen-Zimmerman / Schell / Schelling / Axelrod / Castronova / Lehdonvirta / Rogers / Rouse / Cialdini-RU / Varoufakis) | NO dedicated gamification-expert in ROY swarm (gamification-brigadier-scratchpad legacy artefact only) | ⭐⭐ candidate trigger (consider merging with influence/recruitment) |

### E. Constitutional & routing references (read-only inputs)
- `swarm/lib/routing-table.yaml` — routing canonical (schema 1.0.0, managed_by brigadier, status draft-pre-ruslan-ack); IP-1 strict — role-archetype slugs only
- `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` — Foundation Part 4 LOCKED (Bundle 1 ack)
- `swarm/wiki/foundations/part-6b-human-gate/architecture.md` — Part 6b LOCKED (Bundle 2 ack); stage_gate vs stop_gate vs forge_gate classification
- `shared/schemas/task-return-packet.json` — Part 4 §I.1 LOCKED canonical envelope reference
- `shared/schemas/executor-binding.yaml.template` — IP-1 RUSLAN-LAYER binding pattern (Phase 3 candidates inherit)
- `.claude/config/default-deny-table.yaml` — Part 6b §I.2 11-entry constitutional_never_list (Phase 4 substrate references)
- `swarm/awaiting-approval/` — 9 prior packets (legacy-12-agents-deprecation 2026-05-17 = closest analog format)

### F. Wiki substrate cross-reference (informs Phase 5 wiki proposals)
- `swarm/wiki/concepts/` + `swarm/wiki/sources/books/` exist (Karpathy++ substrate)
- 13 existing Tier A wikis (per prompt §0.2) + 3 NEW из Point B compact (development-promotion-mode-transition / notion-mvp-bypass / cohort-target-profile)
- Gap-list (preview for Phase 5):
  - NO `wiki/concepts/propaganda-six-techniques.md` (derivable from Bernays + Lippmann + Ellul + Chomsky-Herman)
  - NO `wiki/concepts/bite-model-cult-recruitment.md` (derivable from Hassan + Lifton)
  - NO `wiki/concepts/cialdini-six-principles.md` (derivable from Cialdini × 2)
  - NO `wiki/concepts/nlp-meta-model.md` (derivable from Bandler-Grinder + Dilts)
  - NO `wiki/concepts/sleight-of-mouth-14-patterns.md` (derivable from Dilts)
  - NO `wiki/concepts/popper-falsificationism.md` (derivable from Popper × 2 + Chalmers + Lakatos)
  - NO `wiki/concepts/kuhn-paradigm-shifts.md` (derivable from Kuhn + Chalmers + Laudan)
  - NO `wiki/concepts/polya-heuristics.md` (derivable from Polya)
  - NO `wiki/concepts/levenchuk-systems-thinking-canon.md` (derivable from Levenchuk × 5)
  - NO `wiki/concepts/mmk-shchedrovitsky-od-games.md` (derivable from 17.pdf)

## §0.3 R2 STRICT enforcement plan (Phase 0 explicit lock-in)

- Phase 1–5 outputs land EXCLUSIVELY в `reports/book-driven-agents-2026-05-24/` (NOT `.claude/agents/`, NOT `swarm/wiki/`, NOT `swarm/lib/`)
- Phase 6 packet lands в `swarm/awaiting-approval/book-driven-agents-2026-05-24.md` (correct directory per Part 6b convention)
- ZERO writes to: `.claude/agents/` (except `_archived/` preserved untouched), `swarm/lib/routing-table.yaml`, `swarm/wiki/foundations/`, `swarm/wiki/concepts/*` (only proposals as text), `.claude/config/default-deny-table.yaml`
- Constitutional verification at Phase 7 final: grep test ensures no Foundation paths modified

## §0.4 §11.0 MAX-density application plan
- **Phase 1 (knowledge-domain extraction):** MAX-density per prompt §5 — book corpus extraction = deep work; each of 80 books gets structured profile (primary domain / secondary / 3-7 key concepts / 2-5 methods or frameworks / author lineage / cross-bucket Phase 6 confirmation). ROY 500% acceptable.
- **Phase 2 (refined taxonomy):** MAX-density — sub-cluster decomposition + visualization (markdown tree).
- **Phase 3–5 (agent + wiki design):** normal density — R1 design choices belong to Ruslan; substrate provides options, не overspecifies.
- **Phase 6 packet:** formal compliance, no embellishment.

## §0.5 R6 provenance discipline (Phase 1+ scaffolding)
Each book extraction in Phase 1 carries `[src: <path-to-book-md>]` inline citation. Phase 3 agent candidates carry `required_books:` list pointing to specific MD paths. Phase 5 wiki proposals carry `derived_from:` list with multi-book citations.

## §0.6 R12 paired-frame check trigger
**influence-ethics-expert candidate** (prompt §2 seed) carries explicit R12 boundary requirement: per Tier 2 R12 «No extraction beyond agreed share», any agent dispatching influence-tactics MUST surface paired frame (technique + counter-technique / abuse-mode / consent boundary) before promotion. Phase 3 candidate spec includes this constraint. Phase 6 packet includes R12-compatibility verification per Foundation-level rule.

## §0.7 Phase 0 closure

- Substrate read ✅
- ROY swarm inventory verified (9 agents) ✅
- 80-book corpus inventory matches Phase 6 §6.2 matrix ✅
- 11 candidate clusters identified with strength rating (10 named in prompt §2 + 1 gamification synthesis option) ✅
- R2 STRICT enforcement plan locked ✅
- §11.0 MAX-density plan declared ✅
- R6 + R12 discipline scaffolding declared ✅

**Next:** Phase 1 — book corpus knowledge-domain extraction (80 books × structured profile).

---

*Phase 0 closure 2026-05-24 evening. Constitutional posture preserved per §0.1. Phase 1 launches with R2 STRICT lock-in confirmed.*
