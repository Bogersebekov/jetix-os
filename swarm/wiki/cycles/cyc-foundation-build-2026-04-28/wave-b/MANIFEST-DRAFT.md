---
title: JETIX Foundation — Best Practices Integration Manifest (Wave B draft)
date: 2026-04-27
phase: B-3
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
status: DRAFT — finalised in Wave D after all Wave C cycles complete
total_words: ~4600
F: F3
ClaimScope: "Synthesis of 14 consultant cards produced in Wave B-2; holds for 10-part Foundation design as scoped in candidate-parts-merged.md. Subject to Wave C application findings and Wave D final review."
R:
  refuted_if: "Wave C interface cards surface ≥3 framework conflicts not listed in §4 or §6"
  accepted_if: "All 10 Wave C interface card authors reference this manifest in §F (Framework anchors) and find §2 matrix cells accurate"
provenance:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/unix-philosophy.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/mereology-typed-edges.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/framework-taxonomy.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
---

# Best Practices Integration Manifest (Wave B Draft)

## §0 Status

DRAFT — Wave B output. Finalised in Wave D after all Wave C cycles produce per-part
architecture findings and those flow back. Consultant cards in `wave-b/consultants/` are
authoritative primary sources; this manifest is the synthesis index and the entry point
for every Wave C interface-card author.

---

## §0.1 Wave B Supplement Log (2026-04-27 evening)

Following Ruslan walkthrough of cycle 12 AWAITING-APPROVAL packet, 5 fundamental sources were ingested via `tools/convert/convert_all.py` to lift 3 F4 consultant cards before Wave C Bundle 1 dispatch:

| # | Source | Card lifted | New F-level |
|---|--------|-------------|-------------|
| 1 | Bai et al. 2022 *Constitutional AI* (arxiv:2212.08073) → `raw/books-md/anthropic/bai-2022-cai.md` | #13 CAI | F5 (was F5 web-only — now library-direct) |
| 2 | Askell et al. 2021 *HHH* (arxiv:2112.00861) → `raw/books-md/anthropic/askell-2021-hhh.md` | #13 CAI | F5 (was F5 web-only — now library-direct) |
| 3 | Greg Young *CQRS Documents* 2010 → `raw/books-md/event-sourcing/young-cqrs-2010.md` | #5 Event Sourcing | F4-F5 (1/5 library-direct, was 0/5) |
| 4 | Google SRE Workbook Ch. 2 *Implementing SLOs* → `raw/books-md/sre/google-srewb-implementing-slos.md` | #6 SRE | F5 (was F3 training-knowledge) |
| 5 | Google SRE Book (Beyer et al. 2016) → `raw/books-md/sre/google-sre-book.md` | #6 SRE | F5 (was F3 training-knowledge) |

Cards #5, #6, #13 frontmatter + §1 + §2/§3 + §4 inline citations updated. Cards #14 (Mereology) F4 academic remains unchanged — Ruslan deferred mereology supplement (low criticality for Foundation phase). Library inventory updated with §10 supplement entry.

---

## §1 Frameworks Integrated (14)

| # | Framework | Primary expert | Card path | Foundation studied | Status |
|---|---|---|---|---|---|
| 1 | Левенчук ШСМ + FPF | systems + philosophy (joint) | `consultants/levenchuk-shsm-fpf.md` | 7/7 in-repo canonical sources (100%); 0/49 LJ posts direct (deferred Wave C per scope); topic coverage via 3 research compilations | Constitutional baseline — P0 |
| 2 | Systems thinking + cybernetics | systems-expert | `consultants/systems-thinking-cybernetics.md` | 14 books at chapter/section level (100% assigned library); 8/49 LJ posts sampled (FPF demarcation applied) | Strong library coverage |
| 3 | Multi-agent architecture | engineering-expert | `consultants/multi-agent-architecture.md` | ~32/32 assigned sources: 6 Anthropic blogs (full), Cognition counter-position (full), Karpathy gist (full), 3 arxiv ToC + abstract, 5 web sources | 100% assigned — no gaps |
| 4 | KM — Karpathy LLM Wiki + Luhmann + Matuschak + Forte PARA | engineering-expert | `consultants/knowledge-management-karpathy-luhmann-matuschak.md` | 2/5 on disk (Karpathy gist 100%, wiki substrate observable); Luhmann/Matuschak/Forte via 5 web sources grade-A | Shallow Luhmann — Wave C deep read if Part 3 atomicity decisions require formal Zettelkasten |
| 5 | Event sourcing + CQRS + append-only state | engineering-expert | `consultants/event-sourcing-cqrs.md` | **1/5 library-direct (Greg Young 2010, post-supplement 2026-04-27)**; 4/5 still training-knowledge (Kleppmann/Fowler/Vernon/Dahan — flag Wave D); Jetix-applied form (D25, Part 1, Part 6) 100% via repo reads | **F4-F5 mixed** — CQRS-foundational claims now library-grounded; remains training-knowledge on event-schema evolution / sagas / snapshots |
| 6 | SRE + observability | engineering-expert | `consultants/sre-observability.md` | **2/5 library-direct (Google SRE Book full + SLO Workbook Ch.2, post-supplement 2026-04-27)**; 3/5 still training-knowledge (Honeycomb/Mike-Julian/OTel — flag Wave D); FUNDAMENTAL §3+§5 (100%) via repo reads | **F5 lifted** — core SLI/SLO/error-budget burn-rate algebra + Four Golden Signals + postmortem culture all library-grounded |
| 7 | Compounding Engineering | engineering-expert | `consultants/compounding-engineering.md` | STRONG — R-1..R-11 via MASTER-SYNTHESIS §1.5+§2.1; every-article 100%; 2 Anthropic blogs; 0 web sources needed | 100% in-repo |
| 8 | Product management — Cagan + Torres + Ries + Shape Up | mgmt-expert | `consultants/product-management-cagan-shape-up.md` | 5/5 PdM books (chapter level); 3/3 PM books (PMBOK ToC, Scrum full, Shape Up full); 0 web sources | 100% canonical library |
| 9 | Stoic + epistemic — Popper + Kuhn + Naval + Holiday + Munger | philosophy-expert | `consultants/stoic-epistemic.md` | ~85% library: Kuhn (full), Popper Conjectures (full), Vincenti Ch.1+7, Koen I-II, Descartes Discourse I-II, Naval + Holiday + Munger; Popper LoSD full-text deferred | Strong; Altshuller TRIZ deferred |
| 10 | Capital allocation + anti-fragility — Buffett + Munger + Marks + Taleb | investor-expert | `consultants/capital-allocation-antifragility.md` | 5/6 texts at chapter level (Taleb Antifragile + Skin, Marks memos, Munger, Naval); Graham absent (file not found) | Graham gap noted; sourced via Munger/Marks references |
| 11 | Unix philosophy | engineering-expert | `consultants/unix-philosophy.md` | Raymond 100% (full text); Kernighan-Pike **0% usable text** (images only — declared absent, not partial); Hunt-Thomas Ch.1-2 (supplementary) | Kernighan-Pike absent: declared honestly |
| 12 | Clean code / software architecture — Ousterhout + Fowler + Hunt-Thomas + Martin + Brooks | engineering-expert | `consultants/clean-code.md` | Ousterhout full (Ch.1-22); Martin Ch.1+2+17 full; Hunt-Thomas Ch.1-2; Brooks Ch.1-4 full (stub flag was incorrect — actual 39 795 words on disk); Fowler file not found — reconstructed via pre-read | 4.3/5 — Fowler absent from disk |
| 13 | Anthropic Constitutional AI / agent safety | philosophy-expert | `consultants/anthropic-constitutional-ai.md` | **6/9 library-direct post-supplement 2026-04-27**: Bai 2022 + Askell 2021 lifted from web-only to library-direct (`raw/books-md/anthropic/`); Building Effective Agents library-direct pre-supplement; FUNDAMENTAL §6 (100%); RSP v1.2 + Model Specification still web-only F4 (flag Wave D) | **F5 — S1+S2 now library-direct**; S3+S4 remain web-only for Wave D supplement |
| 14 | Mereology + ontology — FPF A.14 typed edges | philosophy-expert | `consultants/mereology-typed-edges.md` | FPF A.14+A.1+Creation Graph (100%, F3); 5 academic sources (Leśniewski, Lewis, Fine, Varzi×2) via canonical training knowledge (F4, not live-fetched) | F4 academic — escalate to Simons "Parts: A Study in Ontology" if formal disambiguation needed in Wave C |

**Library validation corrections surfaced by cards:**
- **Brooks NOT a stub** — 39 795 words on disk; the "736-word stub" flag in INDEX.md was a metadata error. Full Ch.1-4 usable. [card #12 §3]
- **Kernighan-Pike 0% usable** — 2888 words on disk are entirely image placeholder lines; zero text extractable. Declared absent. [card #11 §1]
- **Fowler Refactoring 2ed not found on disk** — expected path `raw/books-md/clean-code/fowler-refactoring-*` yields no file. Card #12 used pre-read synthesis. [card #12 §1]
- **Brooks "No Silver Bullet" essay absent** — 1987 IEEE Computer publication; not in 1995 MMM reprint on disk. Needs web supplement for direct citation. [card #12 §1]

---

## §2 Per-Framework Integration Plan (Wave C Parts × Framework Matrix)

**10 Foundation Parts × 14 Frameworks = 140 cells.** Cell values: `Primary` / `Secondary` / `Tradeoff [vs #N]` / `—`.

| Foundation Part | Primary anchor frameworks | Secondary | Tradeoffs to surface in Wave C |
|---|---|---|---|
| **Part 1 — System State Persistence** | #1 Левенчук (IP-3 artifacts-over-conversations, D25), #10 Capital (Lindy substrate), #11 Unix (plain-text universal interface, everything-is-a-commit) | #5 Event sourcing (git-as-event-log, Principle 1+6), #12 Clean code (module interface discipline) | OQ-ES-1: commit schema versioning not in D25; OQ-ES-4: snapshot strategy for long-lived git history |
| **Part 2 — Signal Ingestion & Triage** | #4 KM (D28 anchor-mandatory, PARA organisational tier), #11 Unix (do-one-thing-well per pipeline stage, compose-via-pipes) | #5 Event sourcing (append-only write, STOP gate as command handler), #1 Левенчук (IP-3, permeable filtered boundary A.1) | D28 selective vs Karpathy qualitative ingestion — D28 wins (Lock); PARA project-first vs Karpathy qualitative [card #4 T1] |
| **Part 3 — Knowledge Base & Methodology Library** | #4 KM (Karpathy compounding artefact, Luhmann one-idea-per-note, typed graph as intelligence), #1 Левенчук (IP-2 bounded context scope, A.14 typed edges, FPF A.14 for dependency typing) | #7 CE (CE populates Methodology Library sub-layer; DRR→methodology promotion), #12 Clean code (Ousterhout deep-modules: each wiki concept = deep atomic unit), #14 Mereology (typed edges are Part 3's graph schema) | Luhmann strict atomicity vs current Jetix narrative wiki/concepts/ style [card #4 T2]; edges/entity ratio ~1.05 vs ≥2.0 target [card #4 P1] |
| **Part 4 — Role Taxonomy & Coordination Protocol** | #1 Левенчук (IP-1 Role≠Executor, IP-8 F.6 six-step onboarding, L/A/D/E A.6.B for inter-part interfaces), #3 Multi-agent (hub-and-spoke P-2, verification architecture P-5, MAST coverage) | #13 CAI (hard-rule anti-scope §6.1, simplicity-transparency-trust), #14 Mereology (typed edges for role dependencies), #2 Systems (Ashby requisite variety: brigadier routing variety ≥ task-type variety) | TRADEOFF-02: Ashby requisite variety vs Anthropic context-engineering simplicity — resolution: variety lives in routing YAML, not prompt prose [card #2 §7]; CrewAI personification vs IP-1 — FPF wins [card #1 P1] |
| **Part 5 — Compound Learning & Methodology Capture** | #7 CE (40/10/40/10 cycle ritual IS Part 5's theoretical spine; DRR ledger; Error→Rule→Skill pipeline), #1 Левенчук (IP-7 writing-as-thinking for human reflection domain) | #8 PM (OKR cadence anchor, Ries build-measure-learn at system level), #9 Stoic/epistemic (Popper falsifiability as rule-promotion gate), #2 Systems (R1 knowledge compound loop — 5-10 cycle delay) | CE schema-driven compound vs Левенчук IP-7 writing-as-thinking — resolution: agents write DRR (CE); Ruslan authors retrospective with structured extractions (IP-7) [card #7 T4]; compound speed vs cycle pressure at €50K gate [card #7 T1] |
| **Part 6 — Governance, Provenance & Human Gate** | #13 CAI (FUNDAMENTAL §6 as Jetix constitution; hard-rule anti-scope; RLAIF self-critique → fail-loud), #1 Левенчук (IP-4 FPF-Steward function, B.3 F-G-R on every promoted artefact), #10 Capital (Graham margin-of-safety: over-engineer governance, blast radius of provenance failure is unbounded) | #5 Event sourcing (AWAITING-APPROVAL = command; approval-log = event; decisions/ = read projection; idempotency gate), #9 Stoic/epistemic (Dichotomy-of-control: gate governs what is in Ruslan's control), #6 SRE (fail-loud P6; error-budget behaviour change for integrity SLOs) | TRADEOFF-01: VSM S3 split — Parts 6 and 8 both serve VSM System 3; Beer predicts oscillation risk [card #2 §7]; OQ-ES-2: gate idempotency key not specified; OQ-ES-3: eventual consistency vs fail-loud in decisions/ reads |
| **Part 7 — Project Lifecycle Substrate** | #8 PM (Shape Up appetite-as-constraint P2, Outcome over Output P1, betting-table rhythm), #1 Левенчук (IP-5 alpha state machine with past-participle states, A.3 Transformer Quartet for state transitions) | #5 Event sourcing (project state transitions as events — Parts 7 does NOT need full CQRS [card #5 Tradeoff B]), #9 Stoic (Dichotomy-of-control: project is scoped to what Ruslan controls; outcome is not guaranteed) | Shape Up appetite vs PMBOK adaptive tailoring — Shape Up wins for Phase 1 solo-founder [card #8 T-C]; Ries MVP-and-pivot vs Shape Up "finish within appetite" — resolved by zoom level (Ries = strategic direction; Shape Up = tactical execution) [card #8 P5] |
| **Part 8 — Health Monitoring & System Integrity** | #6 SRE/observability (SLI/SLO/error-budget triad = backbone of Part 8; fail-loud P6; toil reduction P4), #2 Systems (Beer VSM S3 audit function; Ashby variety for monitor vs failure-mode count; Meadows L7 information-flows leverage) | #10 Capital (Marks second-level: moat = drift discipline, not initial design; antifragile via stressors), #1 Левенчук (IP-4 quarterly immune-system audit function), #13 CAI (integrity violations = absolute halt, softcoded degradation for velocity SLIs) | TRADEOFF-01: S3 authority split — Part 8 should be declared S3 lead; Part 6 is S3 enforcement arm [card #2 §7]; T4: multiple SLO budgets exhausting simultaneously — requires tiered priority ordering (Tier 0 integrity > Tier 1 operational > Tier 2 velocity) [card #6 T4] |
| **Part 9 — Owner Interaction Scaffold** | #8 PM (Torres CDH continuous discovery P3, weekly customer touchpoint slot; OKR quarterly cadence P6; Cagan empowered team P4), #1 Левенчук (IP-7 writing-as-thinking for strategic reflection; IP-2 bounded context for daily-log scope) | #9 Stoic/epistemic (Naval specific knowledge filter; dichotomy-of-control: owner decides, agents propose), #6 SRE (toil < 50% of owner time; alert delivery path to owner) | Torres CDH external-intake vs Левенчук IP-7 internal-authoring — layered composition, not conflict [card #8 T-B]; CDH empowered-team trio compressed to solo-founder + agent-as-advisor in Phase 1 [card #8 T-A] |
| **Part 10 — External Touchpoints & Network Interface** | #13 CAI (privacy constraints; write-ack mandatory before any external action), #1 Левенчук (IP-2 bounded context: external interface has explicit Bridge F.9; A.14 edges typed for CRM-to-wiki cross-refs), #14 Mereology (typed CRM graph edges per wiki/graph/edge-types.md) | #4 KM (Forte PARA: contacts in Resource or Project tier, not KB concepts layer), #3 Multi-agent (A2A open question — OQ-Conflict#4: MCP for tool invocation vs A2A for inter-agent delegation) | Read-only vs action-coordinator scope: Part 10 is read-optimised; any write-back to external system (CRM update from agent) requires HITL ack per Part 6 gate [card #13 §4]; OQ-MAA-C4: A2A protocol not yet standardised — Part 10 should declare slot without implementing |

**Cross-cutting concerns × framework mapping:**

| Cross-cutting concern | Primary frameworks | Enforcement point |
|---|---|---|
| F-G-R trust tagging on every promoted artefact | #1 Левенчук B.3 | Part 6 provenance gate |
| Typed A.14 edges in every interface card §Dependencies | #14 Mereology + #1 Левенчук A.14 | All 10 Wave C interface cards |
| Append-only log discipline | #5 Event sourcing + #11 Unix | Part 1 substrate + all log-producing parts |
| Fail-loud on integrity violations | #13 CAI + #6 SRE P6 | Part 8 alert substrate + Part 6 halt rules |
| 40/10/40/10 compound cycle | #7 CE | Part 5 — every swarm cycle |
| AWAITING-APPROVAL gate before strategic change | #13 CAI + #1 Левенчук B.3 | Part 6 governance mechanism |

---

## §3 Provenance Discipline

Citation format conventions across all Foundation artefacts (interface cards, Master Plan, AWAITING-APPROVAL gate packets):

**Internal docs:**
- `[FPF §5.1 IP-1]` — JETIX-FPF.md section + principle ID
- `[FPF-Spec A.14 L.17478]` — FPF-Spec.md pattern ID + line
- `[FPF-Spec B.3 L.28201]` — Trust & Assurance Calculus
- `[FPF-Spec F.6 L.50641]` — Role Assignment & Enactment Cycle
- `[FUNDAMENTAL §6.2]` — JETIX-VISION-FUNDAMENTAL section
- `[D25]`, `[D28]` — Lock number from decisions/LOCKS-D25-D28-ADDENDUM-*
- `[candidate-parts-merged.md:§2 Part N]` — Wave A merged list

**Library books (format: `[author-short-title-year:ch/section]`):**
- `[Meadows-TIS-2008:Ch.6 L7]`
- `[Ashby-Cybernetics-1956:Ch.11]`
- `[Beer-BotF-1972:Ch.9 S3]`
- `[Ousterhout-PoSD-2021:Ch.4]`
- `[Singer-ShapeUp-2019:Part1]`
- `[Torres-CDH-2021:Ch.3]`
- `[Taleb-Antifragile-2012:Ch.20]`

**Research dumps:** `[research/levenchuk-deep-research-2026-04-18:§6]`

**Consultant cards:** `[card:levenchuk-shsm-fpf §P4]`, `[card:multi-agent-architecture §P-5]`

**External URLs:** `[Bai-CAI-2022](https://arxiv.org/abs/2212.08073)`, `[Walden-Yan-Cognition-2025](URL)`

**Lint discipline:** Every claim in any Foundation artefact MUST carry one inline citation. Bare "per Левенчук" without pattern reference = cargo-cult signal. `/lint` enforces this. Detection: grep for principle-name + absence of `[` within 200 chars.

---

## §4 Conflict Resolution Rules

When 2+ frameworks suggest different patterns:

1. **Constitutional precedence.** Левенчук ШСМ + FPF + Locks D1-D29 always win when conflict exists. Constitutional is non-negotiable [card:levenchuk-shsm-fpf §5 trigger 1; card:anthropic-constitutional-ai §4].
2. **Bounded-context disambiguation.** Apply FPF IP-2: clarify which context the conflict surfaces in before declaring a winner [card:levenchuk-shsm-fpf §P3].
3. **Tradeoff documentation mandatory.** Silent compromise prohibited per framework-taxonomy §5 Ruslan emphasis #4. Every conflict resolved in a Wave C card must appear in the card's §5 Tradeoffs section with explicit resolution and `what changes in this Part` clause.
4. **Surface to Open Q when unresolvable.** Unresolved conflicts go to §6 of this manifest and to the relevant Wave C card's open-questions section. Not into the body of the card as a silent compromise.
5. **Per-decision routing.** Blast-radius classification (FUNDAMENTAL §4.6 Default Deny per OQ-MERGED-6) determines J-level: J1 = auto-approve, J3 = human-only. Conflicts touching J3 decisions escalate to HITL.

**Conflicts surfaced and resolved in Wave B:**

| # | Conflict | Frameworks involved | Resolution | Status |
|---|---|---|---|---|
| C-01 | Foundation moat = drift discipline (second-level) | #10 Capital allocation vs typical design-thinking | Marks second-level: moat IS drift discipline, not the initial architecture. Part 8 (Health Monitoring) is the immune system, not optional infrastructure [card:capital-allocation-antifragility §P3] | Resolved |
| C-02 | D28 selective ingestion vs Karpathy "ingest everything qualitative" | #4 KM vs D28 Lock | D28 wins per Jetix-specific Lock. Karpathy compounding property preserved within anchor constraint. Mitigation: `/build-graph` community detection surfaces cross-anchor serendipity [card:km §5 T1] | Resolved |
| C-03 | Brooks "No Silver Bullet" (essential complexity is irreducible) vs Anthropic simplicity-first | #12 Clean code vs #3 Multi-agent | Both endorse minimum viable: Brooks says abstraction must earn its weight; Anthropic says add agents only when simpler fails. Convergent, not conflicting — cite both for Part 4 anti-scope discipline [card:clean-code §P2; card:multi-agent §P-1] | Resolved (convergent) |
| C-04 | CE schema-driven compound vs Левенчук IP-7 writing-as-thinking | #7 CE vs #1 Левенчук | Division of labour: agents write DRR (CE domain); Ruslan authors cycle retrospective (IP-7 domain). Not conflict — layered composition. Part 5 must declare both slots explicitly [card:compounding-engineering §P3 + T4] | Resolved |
| C-05 | Kim scaling ("more agents = diminishing returns") vs Anthropic +90.2% multi-agent research gain | #3 Multi-agent | Conflict dissolves when task type specified: sequential-planning → pipeline (no parallelism); breadth-first-research with independent subtasks → parallel warranted. Part 4 routing table must encode `task-decomposition-type` per task class [card:multi-agent §Conflict-3] | Resolved — Part 4 Wave C work item |
| C-06 | Cognition "share full traces" vs Anthropic "compress subagent output" | #3 Multi-agent | Different layers: within orchestrator context, full authoritative trace; across subagent→orchestrator boundary, compressed summary. Brigadier holds integrated context; experts return compressed packets [card:multi-agent §Conflict-2] | Resolved |
| C-07 | Shape Up circuit-breaker (no extensions) vs PMBOK adaptive tailoring | #8 PM | Shape Up wins for Phase 1 solo-founder. PMBOK 12 principles consulted for quality + risk, not scope negotiation. At Phase 2+ with external clients, PMBOK stakeholder principles reactivate at RUSLAN-LAYER interface [card:pm §T-C] | Resolved |
| C-08 | Eventual consistency (CQRS read projection) vs FUNDAMENTAL §6.7 fail-loud | #5 Event sourcing vs #6 SRE | Read projections: eventual consistency acceptable. Write path (gate ack) must be synchronously confirmed before canonical promotion proceeds. Consistency predicate required for gate-critical decisions/ reads [card:event-sourcing §5 Tradeoff D] | Resolved — OQ-ES-3 Wave C work item |

**Conflicts OPEN (unresolved — need Wave C or Ruslan ack):**

| # | Conflict | Frameworks | Open question |
|---|---|---|---|
| TRADEOFF-01 | VSM S3 authority split | #2 Systems + #6 SRE | Parts 6 and 8 both serve Beer VSM S3 (Audit/Optimisation). Beer predicts oscillation when S3 is split. Wave C must designate S3 lead Part (proposed: Part 8) and declare Part 6 as S3 enforcement arm. Ruslan ack needed before Part 6/8 interface cards are locked. |
| TRADEOFF-02 | Ashby requisite variety vs Anthropic context-engineering simplicity | #2 Systems + #3 Multi-agent | Resolution path documented: variety in routing YAML (not system prompt prose). Wave C must verify brigadier routing table has ≥20 distinct routing rules and system prompt ≤2000 tokens [card:systems §4 P2 + §7 TRADEOFF-02]. |

---

## §5 Anti-Cargo-Cult Discipline

Per framework-taxonomy §4 (Ruslan emphasis #3) and spec §8 Quality R1.

**The detection rule for Wave C critic passes:**
> If a citation appears in an interface card without a "concrete consequence" sentence AND without a specific Wave C work-list bullet that references it → flag as cargo-cult, return for re-dispatch.

**Cargo-cult example (REJECTED):**
> "We apply Левенчук Role≠Executor (IP-1)."

Reject reason: no consequence stated; no observable change named.

**Deep integration example (ACCEPT):**
> "Per Левенчук IP-1 Role≠Executor [FPF §5.1; FPF-Spec A.2], the role-manifest in Part 4 is
> U.Episteme content (passive method-signature definition); the executor binding (which agent:
> Sonnet vs Opus) is RUSLAN-LAYER `executor-binding.yaml` per FPF §2.1a. Concrete consequence:
> rebinding agents requires explicit YAML change, NOT prompt mutation — this prevents Role drift
> when LLMs are upgraded. AP-L2 detection: search role.md Block 1 `role_name` for model-specific
> strings; any match is a violation [card:levenchuk-shsm-fpf §8 AP-L2]."

**Top 5 cargo-cult traps observed in Wave A/B and avoidance mechanisms:**

| # | Trap | Avoidance |
|---|---|---|
| 1 | Citing FPF without consequence — "we apply A.14 mereology" but dependency sections still read "depends-on" | Per-principle "Applied to Part X with concrete consequence" requirement in consultant cards §4; Wave C critic checks all §D Dependency sections for "depends-on" string [card:levenchuk-shsm-fpf §8 AP-L3] |
| 2 | Anti-pattern named without detection signal — "avoid premature abstraction" with no count-based check | Per-AP "Detection" field in every consultant card §8; engineering-expert conformance checklist: `count(abstractions with <3 uses AND no speculative tag) == 0` |
| 3 | Generic "depends-on" edges in interface cards | Card #14 (Mereology) is the canonical reference every Wave C author must consult before writing §D Dependencies; "depends-on" is forbidden by this manifest |
| 4 | "Apply systems thinking" without VSM level or loop name | Card #2 requires explicit citation: `[Beer-BotF-1972:Ch.9 S3]` or `[Card #2 §5 R1]` — not "per systems thinking" |
| 5 | Citing consultant card without tracing to primary source | Every claim in Wave C card must have a two-hop citation: claim → consultant card section → consultant card §provenance path or URL |

---

## §6 Open Questions

**Frameworks not yet covered:** None — 14 frameworks cover initial scope per framework-taxonomy §2. Candidate watch-list frameworks (#15-17 slots: DDD Eric Evans, Conway's Law, Toyota Lean) are on hold until Wave C surfaces explicit gaps.

**Conflicts unresolved (top 5 requiring Wave C or Ruslan ack):**

| # | Open question | Card source | Required input |
|---|---|---|---|
| OQ-1 | TRADEOFF-01 VSM S3 split — Part 6 vs Part 8 S3 authority | card:systems §7 + card:sre §7 | Ruslan ack: designate S3 lead before Part 6+8 interface cards locked |
| OQ-2 | OQ-ES-1 — commit message schema versioning absent from D25 | card:event-sourcing §8 | Wave C Part 1 work item: add `COMMIT-SCHEMA-VERSION` file + backward-compat rules |
| OQ-3 | OQ-KM-1 — Luhmann two-cabinet structure not formalised in wiki entity types | card:km §7 | Wave C Part 3 design decision: declare sources/ = bibliographic cabinet; concepts/ = idea cabinet; enforce concept-extraction step in /ingest |
| OQ-4 | OQ-CONFLICT-4 — MCP (tool invocation) vs A2A (agent delegation) protocol split | card:multi-agent §5 Conflict-4 | Part 4 Phase B flag: schema slot for task handshake (dispatched→received_ack→in_progress→returned) needed in Part 4 design, even if not implemented Phase A |
| OQ-5 | Brooks "No Silver Bullet" essay not on disk | card:clean-code §1 + §3 | Separate web supplement needed for direct citation; cannot be paraphrased reliably from secondary sources |

**Consultant card iterations needed (Wave D):**
- All 14 cards: re-pass after Wave C surfaces application findings and conflicts not anticipated in Wave B.
- Specific: card #14 Mereology — deep read of Simons "Parts: A Study in Ontology" if Wave C edge-typing decisions require formal supplementation-axiom disambiguation. (Ruslan ack 2026-04-27 evening: deferred for Foundation phase, low criticality.)
- Specific: card #1 Левенчук — 49 LJ posts direct reads deferred to Wave C; any Part 4 or Part 5 interface card that invokes IP-1 or IP-7 should trigger the full LJ corpus read on the specific posts covering that principle.
- ✅ **PARTIALLY RESOLVED (2026-04-27 evening Wave B supplement):** F4 web-only / training-knowledge declarations on cards #5 / #6 / #13 partially lifted via library ingestion of 5 fundamental sources. See §0.1 Wave B Supplement Log for the per-card delta. Remaining gaps:
  - **Card #5:** Kleppmann DDIA, Fowler EventSourcing article, Vernon IDDD, Udi Dahan Clarified CQRS still training-knowledge → flag Wave D supplement.
  - **Card #6:** Honeycomb Observability Engineering, Mike Julian Practical Monitoring, OpenTelemetry spec still training-knowledge → flag Wave D supplement.
  - **Card #13:** Anthropic RSP v1.2 + Model Specification still web-only → flag Wave D supplement.
  - **Card #14 Mereology** F4 academic remains unchanged.
  - Левенчук 49 LJ posts deep-read still deferred (Wave C invokes when Parts 4/5 dispatch).

---

## §7 Provenance

All claims in this manifest trace to specific consultant card sections. No floating claims.

| Claim | Source |
|---|---|
| Library coverage per framework | §1 table — each row cites the card's §1 Foundation Studied |
| Part × framework matrix cells | §2 — each cell built from consultant card §4 Key Principles "Applied" fields |
| Conflicts C-01..C-08 | §4 — each row cites the resolving card and section |
| TRADEOFF-01, TRADEOFF-02 | card:systems §7; card:multi-agent §4 P-2 |
| Anti-cargo-cult examples | card:levenchuk-shsm-fpf §8 AP-L1..AP-L5; framework-taxonomy §4 |
| Brooks stub correction | card:clean-code §3 |
| Kernighan-Pike 0% usable | card:unix-philosophy §1 |
| Fowler not on disk | card:clean-code §1 |
| OQ-ES-1..OQ-ES-5 | card:event-sourcing §8 |
| OQ-KM-1..OQ-KM-3 | card:km §7 |
| OQ-SRE-1..OQ-SRE-4 | card:sre-observability §8 |
