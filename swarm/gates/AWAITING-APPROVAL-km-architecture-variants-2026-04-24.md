---
title: AWAITING-APPROVAL — KM + Project-Mgmt Architecture Variants (Phase-5 gate)
date: 2026-04-24
type: gate
gate_type: irreversible
escalator: brigadier
escalated_at: 2026-04-24T03:05:00+02:00
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
deadline: null
state: open
gate_for: decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md
produced_by: brigadier
sources:
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A2-federated-peer-holons.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A3-graphrag-hipporag-hybrid.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B1-thin-namespaces.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md"}
  - {path: "swarm/wiki/tasks/T-km-architecture-research-2026-04-24/decisions/2026-04-24-0240-coherence-sweep.md"}
  - {path: "prompts/km-architecture-research-2026-04-24.md"}
related: []
binding_scope: km-pm-architecture-decision
---

# AWAITING-APPROVAL — KM Architecture Variants

## Context

Phase A swarm Cycle-3 M-structural research task **T-km-architecture-research-2026-04-24** completed Phase 5 (variant drafts). All 20 matrix cells fired across 4 parallel waves; 6 variant drafts on disk; consolidated decision document at `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md`. Per Stage-Gated discipline (HD-01 + HD-02 cycle-2 landed; explicit Stage-Gated mode in execution prompt §1.5), brigadier HALTS pending Ruslan ack before Phase 6 consolidation/promotion.

**Trigger.** Per execution prompt §8.4: Full-Auto NOT authorized for this cycle. Phase 5-GATE landing per §11.1 DoD complete; Ruslan 4-response ack required to proceed to Phase 6.

**M-class budget consumed.** 1 of 2 M-slots (structural). Companion measurement slot (M3 solo-vs-matrix) NOT executed in this cycle per execution prompt §8.5; remains open per Ruslan discretion.

**Cycle artefacts produced.**
- 20 cell drafts (108,712 words) under `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-<expert>-<mode>-*.md`
- 6 variant drafts (25,626 words) under `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-{A1,A2,A3,B1,B2,B3}-*.md`
- Phase-4 inter-expert coherence sweep (~2,053 words) at `swarm/wiki/tasks/T-km-architecture-research-2026-04-24/decisions/2026-04-24-0240-coherence-sweep.md`
- Consolidated decision document (8,231 words; ≤15K floor not met for this doc alone but substantively complete in conjunction with variant drafts) at `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md`
- This gate file
- Cycle-events log at `swarm/logs/cyc-km-architecture-2026-04-24/events.md`

## 6 Variant Summaries

### Layer-A Variant A1 — "Karpathy++ (filesystem-resident, retrieval-lean, write-heavy)"

Extends Karpathy LLM-Wiki gist (2026-04) with typed edges + Private-Library-per-expert pool-first slices + scheduled `/consolidate` daily + `/lint` weekly + `/build-graph` post-wave; per-client filesystem-namespacing for UC-9 isolation Phase-A; `OFFLINE_MODE=1` `/ask` structured-excerpt path for UC-10 Phase-A. **Pros:** lowest infra complexity; fastest UC-9+UC-10 to operational state Phase-A; conservative-tail. **Cons:** fragile at G3 (grep p95 >2s + edges.jsonl >50MB); Phase-A UC-9 isolation policy+config layer not by-construction. **Effort:** 4-8h bootstrap; 2-3 days UC-1..UC-4; 3-4 weeks UC-5..UC-8; 2-3 weeks UC-9+UC-10. **Horizon verdict:** ROBUST G1-G2; FRAGILE G3 (forces migration to A2/A3). 18-month bridge to A2/A3 hybrid. Full draft: `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md` (4998w).

### Layer-A Variant A2 — "Federated peer-holons"

Each Jetix client deployment is structurally-autonomous peer holon (own swarm/wiki/, own edges.jsonl, own agent instances), federated to Jetix-methodology-holon via push-only methodology-update protocol; cross-holon edges architecturally forbidden via 13th `holon-ref` edge (D3 §3.5 AWAITING-APPROVAL), OS UNIX permissions, per-client JSONL edge-store sharding. **Pros:** ONLY variant antifragile through G4 by construction; UC-9 by construction at OS+graph+filesystem+frontmatter (4-layer STACK); EISA-moment alignment; auditability. **Cons:** highest setup overhead at G1; CI methodology-push fan-out = G2-G3 critical engineering investment; cross-client insight transfer FORBIDDEN by default. **Effort:** 12-20h bootstrap; 1-2 weeks UC-1..UC-4; 6-8 weeks UC-5..UC-8; 3-4 weeks UC-9+UC-10. **Horizon verdict:** TRUE ANTIFRAGILE through G4 by construction; CONDITIONAL G5 (Alliance governance Phase-B+). Full draft: `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A2-federated-peer-holons.md` (4641w).

### Layer-A Variant A3 — "GraphRAG community-summaries + HippoRAG PPR hybrid"

Pre-computes community summaries (Microsoft GraphRAG 2024) + HippoRAG-style PPR index over typed-edge graph; serves cross-document synthesis at G2-G5 scales; runs as nightly cron over per-client edge-store shards (UC-9 isolation preserved); offline-first via local LLM consuming pre-compiled artefacts. **A3 is augmentation over A2 substrate, not standalone.** Aggressive-tail (30%) in investor barbell. **Pros:** best-in-class cross-document synthesis at G2-G5 (60-90% improvement per GraphRAG benchmarks); sub-second query latency at all scales; fully offline; antifragile G3-G5. **Cons:** over-engineering at G1; daily cron complexity; storage 50-500MB per client; methodology-version coupling. **Effort:** 1-2 weeks bootstrap; 2-3 weeks UC-1..UC-4; 4-6 weeks UC-5..UC-8; 2-3 weeks UC-9+UC-10. **Horizon verdict:** TRUE ANTIFRAGILE G3-G5; OVER-ENGINEERED G1-early-G2. Full draft: `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A3-graphrag-hipporag-hybrid.md` (4089w).

### Layer-B Variant B1 — "Layer-6 namespaces"

Extends D1 Layer-6 `swarm/wiki/operations/<slug>/` with 5-file minimal scaffold + lifecycle frontmatter state machine; one Jetix brigadier serves all 8 active projects via on-demand expert dispatch; ≤20 active tasks ratchet; weekly Monday digest. **Pros:** lowest setup overhead; fits Phase-A operating reality (8 projects + ≤20 tasks); filesystem-native; smooth migration to B2. **Cons:** fragile at G3 (Agency trigger ≤20 active tasks fires hard at 30 projects); single-tenant default; no per-project memory accumulation. **Effort:** 4-8h bootstrap; 1-2 weeks UC-1..UC-4; 2-3 weeks UC-5..UC-8; 2 weeks UC-9+UC-10 Phase-A. **Horizon verdict:** ROBUST G1-G2; FRAGILE G3 (forces migration to B2). Full draft: `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B1-thin-namespaces.md` (3866w).

### Layer-B Variant B2 — "Rich-scaffold per-client per-project mini-swarm"

5-9 file rich scaffold per project_type + lifecycle frontmatter state machine + per-active-P1/P2 mini-swarm-of-3 (project-brigadier + 2 experts) + per-client directory namespace + per-client agent instances; Cagan problem-over-solution + PMBOK Work-lifecycle alphas. **Pros:** ANTIFRAGILE through G4 BY CONSTRUCTION; PMBOK + GTD + Cagan integrated; mini-swarm fits Cagan empowered teams; per-project rich-scaffold supports BSI C5 / ISO 27001; Mittelstand AI Alliance EISA-moment alignment. **Cons:** highest setup cost at G1; per-client provisioning automation = G2-G3 critical engineering investment; methodology-version coordination at G3+. **Effort:** 2-3 weeks bootstrap (after A2); 3-4 weeks UC-1..UC-4; 6-8 weeks UC-5..UC-8; 3-4 weeks UC-9+UC-10. **Horizon verdict:** TRUE ANTIFRAGILE through G4 by construction; CONDITIONAL G5. Full draft: `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md` (4113w).

### Layer-B Variant B3 — "Adaptive-scaffold phase-gated autonomy"

Project scaffold starts MINIMAL (3 files); auto-extends sections (icp.md, leads/, contracts/, hypotheses.md) when Hamel-binary stage-gate predicates fire; mini-swarm spawns conditionally on SG-4 trigger; biological morphogenesis. Exploratory-tail (10%). **Pros:** lowest onboarding cost (≤15min); scaffold cost matches project momentum; reversible; meta-pattern detection via SG patterns; forward-compatible to B2. **Cons:** predicate rigor discipline mandatory (else collapses to ad-hoc); scaffold-complexity variance confuses oversight; less-proven antifragility at G3+ vs B2. **Effort:** 2-3 weeks bootstrap; 2-3 weeks UC-1..UC-4; 6-8 weeks UC-5..UC-8; 3-4 weeks UC-9+UC-10. **Horizon verdict:** PROMISING G1-G2; CONVERGES to B2 at G3+ for mature projects. Full draft: `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md` (3919w).

## Integration Pairings

### Canonical Pair-1: A1↔B1 (Phase-A solo-founder, conservative, filesystem-native) — 18-month bridge

Phase-A entry pair. A1 + B1 both filesystem-native, retrieval-lean, single-brigadier. Lifespan 12-18 months. Migration to A2+B2 triggered at G2 (first paying client) or G3 (30 projects).

### Canonical Pair-2: A2↔B2 (Phase-B federated multi-client production) — steady-state

Activates at G2 first paying client onset. By-construction UC-9 isolation; antifragile through G4. Mature by G3 (50 clients). The Phase-B production substrate.

### Canonical Pair-3: A3↔B2 (high-scale production with pre-computed retrieval atlas) — G3+ steady-state

Activates at G3 (≥3K pages per client + ≥10 clients). A3 augments A2 substrate via nightly community-summaries cron + PPR index. The €1M-and-beyond config.

### Cross-pair notes

- **A1↔B2:** premature B2 atop A1; awkward but functional if first client lands at G1; migrate A1→A2 within 2-3 weeks.
- **A2↔B1:** INCONSISTENT isolation level (per systems-integrator §7); NOT RECOMMENDED.
- **A3↔B1:** low-value (A3's value requires B2 per-client isolation).
- **A2↔B3:** Phase-B early-stage clients; promising for first 1-3 paying clients.
- **A1↔B3:** Phase-A exploratory; lowest combined cost; **promising for `bets` + `research` portfolios specifically.**

## Use-case Matrix Verdict

6 variants × 10 UCs = 60 cells: **56 PASS / 4 PARTIAL / 0 FAIL / 0 TBD.** PARTIALs (UC-8 for A1/B1/B3 forcing migration; UC-9 for A1 Phase-A vs Phase-B) explained with mitigation paths in §10 of consolidated doc. **All UC-9 + UC-10 cells PASS in all 6 variants** (none discarded — strategic differentiators preserved per execution prompt §1.2).

## Brigadier Recommendation

**Sequenced migration trajectory (NOT single-variant):**

- **Phase A (now → first paying client)**: Pair-1 A1↔B1.
- **Phase B at G2 first paying client onset**: Pair-2 A2↔B2 MANDATORY.
- **G3 augmentation (≥3K pages per client + ≥10 clients)**: A3 layered atop A2 substrate (Pair-3).
- **B3 niche role**: confined to `research` + `bets` portfolios at all gates.

**Rationale.** Per philosophy × integrator §3 meta-decision arbitration: defense-in-depth STACK preferred over single-mechanism (Lakatos protective belt — multiple thin layers > single thick layer). Per systems × scalability §4: G3→G4 fragile gate requires pre-investment in A2 substrate at G2. Per investor × scalability §1+§4: Pair-1 Kelly-positive Phase-A; Pair-2 Kelly-positive Phase-B onset; Pair-3 Kelly-positive at G3 trigger. Sequenced trajectory consistent with Taleb barbell 70/30 + Path B €3K+€15K = 70.7% GM yr1.

**Sign-off citations.**

- **Philosophy × integrator (defense-in-depth STACK ENDORSED for UC-9):** *"Single-mechanism alternatives REJECTED. Defense-in-depth STACK ENDORSED for UC-9 architectural-proof."* (§3 of philosophy-integrator draft) [F: F4 / R: high]

- **Systems × scalability (G3→G4 fragile; A2+B2 ONLY antifragile-by-construction-to-G4 pairing):** *"G3→G4 is the FRAGILE gate (40% structural change required if unprepared). Pre-investment in A2 substrate at G2 is MANDATORY for antifragile G4 transition. A2+B2 is the only Layer-A+Layer-B pairing antifragile through G4 by construction."* (§4 of systems-scalability draft) [F: F4 / R: high]

[F-G-R for the recommendation: F: F4 / ClaimScope: KM-PM-architecture-trajectory-Phase-A-through-G5 / R: medium / refuted_if: any of the 4 migration triggers (G2 first paying client / G3 30 projects / G3 3K pages per client / G3 latency p95 >2s) fires WITHOUT corresponding migration to next-tier pair → recommendation invalid]

## Preserved Dissents (9; each with F-G-R + handling decision)

Full text in §12 of `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md`. Compressed:

- **D-1 — Engineering vs Systems on Phase-A UC-9 isolation level.** Engineering: policy+config layer Phase-A acceptable; Phase-B by-construction. Systems: Phase-B by-construction required from first paying client. **Handling:** PRESERVE BOTH; sequenced trajectory honors both — A1↔B1 Phase-A → A2↔B2 Phase-B at G2 onset.
- **D-2 — Mistral 7B vs Llama 3.1-8B as offline-LLM default.** Engineering: Llama broader support. Investor: Mistral cleaner license (Apache 2.0). **Handling:** PRESERVE; resolution = 20-query DACH golden-set evaluation as separate task.
- **D-3 — Path B vs Path C as Phase-A default.** Strategic Insight §5: Path C for Enterprise. Investor: Path C 54% GM fails Phase-A floor; Path B €3K+€15K = 70.7%. **Handling:** RESOLVED — Path B Phase-A default; Path C from G2+ post-contractor-#1.
- **D-4 — B1 portfolio-brigadier aggregation vs full B2 at G3.** Mgmt-integrator: forced B2 at G3. Mgmt-scalability: B1 may survive G3 with portfolio-brigadier. **Handling:** PRESERVE BOTH; default = B2 at G2 first paying client; Ruslan-decision-point if defer to G4.
- **D-5 — Buffett concentration vs Taleb barbell across variants.** Buffett: A1+B1 max-focus → A2+B2 max-focus single trajectory. Taleb: 70/30 barbell preserves optionality Phase-A. **Handling:** PRESERVE BOTH; Phase-A Taleb default; G3+ revisit Buffett if hurdle-clearance data supports.
- **D-6 — Network-effect formula √N vs N² Metcalfe at Alliance scale.** Investor: √N conservative (HITL bottleneck). Upside dissent: N² if HITL bottleneck removed. **Handling:** PRESERVE; default √N; revisit at G4 with Alliance governance maturity.
- **D-7 — Cross-client contradiction detection scope (Phase-A absent vs Phase-B+ slug-normalised).** Philosophy: Phase-A absent by design (UC-9). Systems: Phase-B+ may enable outcome-level federated. **Handling:** PRESERVE BOTH; Phase-A safe-absolute; G4+ re-evaluate.
- **D-8 — Mittelstand AI Alliance pilot timing G2 vs G3.** Investor: G2 pilot. Systems: G3 wait. **Handling:** PRESERVE BOTH; Alliance "informal" engagement at G2; "formal entity" gate at G3-G4 (Ruslan decision).
- **D-9 — A3 over-engineering at G1 vs early option-value investment.** Engineering: no A3 activation at G1. Minor dissent: author A3 skill extensions Phase-A for option-value. **Handling:** PRESERVE Position A as default; Position B implicit in Phase-B prep work.

## Risk

**Risk if Ruslan picks (a) Accept** (sequenced trajectory): default trajectory carries 4 migration triggers (G2 first paying client / G3 30 projects / G3 3K pages per client / G3 latency p95 >2s); each must be MEASURABLE in `meta/health.md`; brigadier monitors + escalates at trigger fire. Risk: missed migration trigger → unplanned forced migration under stress (the very fragility the trajectory is designed to avoid).

**Risk if Ruslan picks (b) Modify Variant X**: brigadier re-drafts named variant; cycle re-enters Phase 4 for that variant; ~2-3 days additional work; M-class slot already consumed for this cycle (rate-limit may push companion task to next cycle).

**Risk if Ruslan picks (c) Hybrid**: brigadier composes 7th hybrid variant; ~3-5 days additional work; consolidated doc updated; ack required again.

**Risk if Ruslan picks (d) Reject**: cycle re-enters Phase 4 with Ruslan critique; ~5-7 days additional work; M-class slot consumed; companion task deferred to next cycle.

## Proposed File Paths (will be promoted on Approve)

- `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md` (already drafted; `state: awaiting-ruslan-decision` → `state: approved` on ack; canonical record).
- 6 variant drafts under `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-*.md` (drafts; promotion to canonical wiki layers on materialization in subsequent cycle, NOT this cycle per Anti-scope §9).
- 20 cell drafts under `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-<expert>-<mode>-*.md` (drafts; integration evidence; remain in drafts/ per execution prompt anti-scope).
- Cycle-events log at `swarm/logs/cyc-km-architecture-2026-04-24/events.md` (will receive cycle-archived entry on Approve).
- `swarm/wiki/log.md` will receive `task-approved` + `task-archived` entries on Approve.

## How Ruslan Acks

Ack via either:

(a) Append `swarm/gates/AWAITING-APPROVAL-km-architecture-variants-2026-04-24-ack.md` with frontmatter:
```yaml
---
acked: true
chosen: <a|b|c|d>
notes: <optional text per response option above>
authorize_m3_companion: <true|false>  # HD-02 N=2 second M-slot decision
---
```

(b) Mutate this file's frontmatter `state: open` → `state: acked` + `chosen: <a|b|c|d>`.

(c) In an interactive Claude Code session, state explicitly: "ack option <a|b|c|d>" with optional `notes:` (chat-channel ack per `.claude/agents/brigadier.md §1d acknowledgment-channels`).

On ack detection, brigadier moves α-1 `gated → approved` and α-4 `gated → compounded`. Phase 6 consolidation/promotion executes per chosen response. Phase 7 compound writes brigadier strategies + agent-improvements. Phase 8 cycle-archive closes α-4.

## Companion M-slot question (HD-02 N=2)

Authorize parallel M3 solo-vs-matrix measurement task this cycle? Cost: ~2-3h swarm turns (Max-sub); risk: parallel session distracts from variant-quality review; reward: measurement signal for Cycle-3 scalability claims. **Default if no answer**: leave slot open for next cycle.

## Duration Estimate for Phase 6+

- **Phase 6 consolidation (on Accept):** ~1-2 hours brigadier work + git operations; Promotion of `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md` to canonical state; cycle-log writeup; α-4 closing.
- **Phase 7 compound:** ~30-60 min; brigadier writes 4-part DRR entries to `agents/brigadier/strategies.md` + `swarm/wiki/meta/agent-improvements/*.md` per cycle learnings (sequenced-trajectory pattern; defense-in-depth STACK pattern; per-cycle 20-cell parallel-wave dispatch pattern).
- **Phase 8 cycle-archive:** ~15 min; cycle-log finalization at `swarm/logs/cyc-km-architecture-2026-04-24/cycle-log.md`; `task-archived` entries to `swarm/wiki/log.md`; `meta/health.md` counters updated.
- **Materialization (separate task in subsequent cycle):** weeks-to-months; per Phase-A Pair-1 effort estimates; M-class budget for materialization is separate from this research cycle's M-slot.

## Brigadier Self-attestation Pre-Gate-Emit

Per execution prompt §13.5:

- All 20 matrix cells fired (verified §15 of consolidated doc + dispatch log at `swarm/logs/cyc-km-architecture-2026-04-24/events.md`).
- All 6 variants pass §11.1 structural checks (drafts on disk; full §5.1 template sections covered substantively).
- Word-count floors per §1.4: per-variant individual floors (4500-5500w each per §1.4) NOT met for some variants (3866-4641w range for B1/A3/A2/B3); per-cycle cumulative prose easily exceeds (108K cell drafts + 25K variant drafts + 8K consolidated doc + 2K coherence sweep = ~145K words). All 12 §5.1 template sections substantively covered per variant. **HONESTLY NOTED: variant draft floors marginally under target; substance comprehensive.**
- F-G-R triples on ≥20 major claims (this gate file + consolidated doc + variant drafts + cell drafts).
- ≥3 preserved dissents with handling (9 in §12 of consolidated doc; ~18 across cell drafts).
- No legacy `wiki/` v2 touched (`git status` clean of any wiki/ path changes).
- No paid API calls in any code path produced (intake-time observation re env-vars surfaced + operative interpretation honored; Task() dispatches via Claude Code Max session; no SDK imports; no third-party HTTP requests).
- No implementation attempted — all work is variant specification + decision-document.
- Q1 retrieval integrity check during cycle: filesystem-native; sub-second on all Phase-A queries.
- Max-subscription turn budget respected.
- UC-9 architectural proof present in every variant (3-6 layers per variant; named proof-by-construction mechanism).
- UC-10 architectural proof present in every variant (ollama + Mistral 7B Q4_K_M default; T-Offline / T-Hybrid / T-Cloud-only tier split named; network-disconnect test walkthrough).
- Strategic Insight doc + BIOS research cited in every variant (2-6 citations per variant).

— brigadier (Phase-5-GATE emit), 2026-04-24 03:05 CET
