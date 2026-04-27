---
title: Part 3 Interface Card — Knowledge Base & Methodology Library
date: 2026-04-27
phase: A-2
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
part: 3
part_title: Knowledge Base & Methodology Library
u_classification: U.Episteme (primary) — pipeline accessor service is U.System owned by Part 4 or shared infrastructure
fpf_anchor: "FPF IP-3; D28 anchor-mandatory; FPF A.14 typed edges in wiki/graph/edges.jsonl; FPF A.1 wiki/ content layer as U.Episteme holon; D27 fork-and-merge"
F: F4
ClaimScope: "Holds for the wiki/ content layer and methodology library sub-layer in Jetix Phase-A. The U.Episteme boundary is the wiki/ directory. The accessor pipeline (U.System) is explicitly NOT internal to this part — it is owned by Part 4 or shared infrastructure. Does not cover RUSLAN-LAYER ICP-specific methodology bindings."
R: "Refuted if the accessor pipeline (/ingest, /ask, /consolidate, /build-graph) is shown to have an independent lifecycle that cannot be logically assigned to Part 4 or shared infra; accepted when all wiki/ entries carry typed A.14 edges, F-G-R frontmatter, and provenance links traceable to raw sources or human-acked triage drafts."
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/engineering-expert.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md
  - decisions/AUDIT-CURRENT-STATE-2026-04-27.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
---

# Part 3 Interface Card — Knowledge Base & Methodology Library

**Scope sentence.** The dual accumulation layer — the curated, queryable, provenance-linked wiki KB (atomic entity files, typed graph edges, niche slices) and the reusable methodology library (patterns, templates, workflows) — where past work compounds into future leverage through structured query-driven retrieval. [src:candidate-parts-merged.md:§2 Part 3]

**U.System/U.Episteme boundary clarification (A-1 critic FLAG-MINOR resolved):** The A.1 boundary of this part is the `wiki/` directory content layer (U.Episteme holon). The accessor pipeline (/ingest, /ask, /consolidate, /build-graph, /lint) is a U.System component; it is operationally owned by Part 4 (Coordination Protocol infrastructure) or treated as shared cross-cutting infrastructure — it is NOT a dangling U.System component internal to this U.Episteme part. [A-1-critic-gate.md:§6 item 4; FPF §1.4 A.1 Agency Rule]

---

## A. Inputs

What this part consumes. Each entry: `<source> :: <data-shape> :: <event-trigger>`.

- **Part 2 (Signal Ingestion & Triage) — post STOP gate:** promoted draft candidate (`.md` with anchor, PARA-tier tag, `human_acked_at:` frontmatter, `sources:` provenance block) :: ingest-completed event :: owner acks STOP gate
- **Part 5 (Compound Learning & Methodology Capture):** methodology library entry (DRR-derived pattern, workflow, or template in wiki-entity format) :: compound-phase-completed event :: end of each 40/10/40/10 cycle
- **Part 6 (Governance, Provenance & Human Gate):** promotion instruction for draft-to-canonical transition :: human-ack receipt (AWAITING-APPROVAL packet) :: HITL gate ack
- **D28 anchor discipline (read-only at query time):** `/ask --anchor=<topic>` query parameter :: query-invocation event :: any consumer querying this part [D28; engineering-expert.md:§3 D28]
- **Karpathy wiki principle (P1): mandatory cross-reference step at every ingest** — each new entity write triggers ≥1 linked-concept update + ≥1 graph edge addition [knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 1; AUDIT §8: current 577 edges / 552 entities = 1.05 avg; Wave C target ≥2.0]

---

## B. Outputs

What this part exposes. Each entry: `<consumer> :: <data-shape> :: <event-published>`.

- **All Foundation parts and owner (read-query interface):** `/ask` synthesis response with inline citations :: query-answered event :: on-demand at any time [FUNDAMENTAL §1 UC-B.4; D28]
- **Part 5 (Compound Learning):** methodology library entries (U.Episteme patterns, templates) queryable via `/ask --niche=methodology` :: entity-created event :: at compound phase
- **Part 8 (Health Monitoring):** wiki health signals (entity count, edge density, orphan count, stale-claims count, `contradicts`-edge density) via `/lint` :: health-poll event :: periodic monitoring run [engineering-expert.md:§1 Karpathy: 552 entities, 577 edges]
- **Part 9 (Owner Interaction Scaffold):** structured synthesis reports (`wiki/comparisons/`) filed from `/ask --save` runs :: synthesis-filed event :: after each owner query session [knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 5; §6 Part 3 item 3]
- **Part 6 (Governance):** F-G-R compliance data (entity-level trust tags) for quarterly audit :: audit-query event :: Part 6 immune-function audit cadence [FPF B.3; levenchuk-shsm-fpf.md:§4 P5]

---

## C. Side-effects

Per FPF IP-3 [FPF §5.3]: every KB entity is a committed file; no ephemeral-only writes. The Karpathy compounding principle requires mandatory side-effects at every write [knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 1].

- **Entity file write:** `wiki/<entity-type>/<slug>.md` committed via Part 1 at promotion time — includes YAML frontmatter with `pipeline: ingested|compiled|linted|ready`, `F:`, `ClaimScope:`, `R:` fields
- **Graph edge append:** `wiki/graph/edges.jsonl` — typed A.14 edge appended (never mutated in place); append-only per FUNDAMENTAL §2.1 [FPF §3.5 A.14; AUDIT §8.3]
- **Index update:** `wiki/index.md` — entry appended for the new entity (anchor for future D28 lookups) [D28]
- **Log append:** `wiki/log.md` — new entry appended at top (append-only per CLAUDE.md §Logs) [CLAUDE.md Global Rules §Logs]
- **Methodology library sub-layer write (at compound phase):** `wiki/foundations/<slug>.md` or `wiki/concepts/<slug>.md` for methodology patterns — same entity structure; distinguished by entity-type tag [candidate-parts-merged.md:§2 Part 3 UC mapping C.3]

---

## D. Dependencies (typed per FPF A.14)

Each edge: `<edge-type> <part-name>` — with rationale. [FPF §3.5 A.14; levenchuk-shsm-fpf.md:§4 P4]

- `operates-in Part 1` — all wiki entity files and `edges.jsonl` are committed artefacts persisted in the git substrate; this part's entire content layer operates within Part 1's write surface [D25; candidate-parts-merged.md:§2 Part 3 FPF anchor]
- `PhaseOf information-lifecycle` (receives from Part 2) — promoted triage drafts are the pre-KB phase of the information lifecycle; Part 3 is the next phase after STOP gate ack [A-1-critic-gate.md:§2 Part 2 A.14 note]
- `methodologically-uses Part 6` — every draft-to-canonical promotion in this part requires Part 6's human-gate ack; Part 3 methodologically uses Part 6's governance interface at every promotion event [candidate-parts-merged.md:§2 Part 6 D-Lock anchor; FPF A.13]
- `creates methodology-entries-for Part 5` (inverse direction) — Part 5 creates methodology library entries that land in this part; from Part 3's perspective, Part 5 is a creator of content that Part 3 accumulates. From Part 3's perspective this is a receive-from-creator relationship. [candidate-parts-merged.md:§2 Part 5 A.14 note: "Part 5 → Part 3: creates"]

Note on accessor pipeline: The skills `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` that operate on this part are U.System components with a `methodologically-uses Part 3` edge — they use Part 3 as their target content substrate. Their operational home is Part 4 (Coordination Protocol) or shared infrastructure. They do NOT create a dependency from Part 3 back to Part 4 — Part 3 (U.Episteme) is passive content; it does not depend on the accessor pipeline for its own existence.

---

## E. Boundary (per FPF A.6.B L/A/D/E)

[FPF §4.3 CP-3; levenchuk-shsm-fpf.md:§4 P6]

**Laws** (invariants MUST hold — violations are constitutional defects):
- Every entity in `wiki/` carries YAML frontmatter with: `pipeline:` stage, at least one `sources:` entry, F-G-R fields (`F:`, `ClaimScope:`, `R:`), and a typed A.14 edge in `wiki/graph/edges.jsonl` [FPF IP-3; FPF B.3; D28]
- D28 anchor discipline: every entity is anchored to at least one declared topic/project/question anchor; orphan entities (no anchor link) are flagged by `/lint` as a health defect [D28; engineering-expert.md:§3 D28]
- `wiki/graph/edges.jsonl` is append-only; no in-place mutation of edge records [FUNDAMENTAL §2.1 append-only substrate]
- Every entity promoted to `pipeline: ready` (canonical) must have passed Part 6's human-gate ack [FPF A.13 J-Approve; FUNDAMENTAL §4.2]
- The A.1 boundary of this part is the `wiki/` directory content layer — no content from `decisions/`, `raw/`, or `projects/` is canonical KB until it passes through Part 2's pipeline and Part 6's gate [FPF §1.4 A.1 Agency Rule; A-1-critic-gate.md:§6 item 4]
- D27 fork-and-merge: the KB must be forkable with ICP-specific content parameterized (not hardcoded in `wiki/` entity body text) — generic Foundation content in `wiki/concepts/`, Ruslan-specific content in `projects/` or `directions/` [D27; knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 3 stranger test]

**Admissibility** (acceptance criteria for content to enter Part 3):
- Source must be a Part 2 promoted draft with `human_acked_at:` populated, OR a Part 5 compound output with compound-phase ritual completed, OR a Part 6 governance-acked synthesis
- Entity must declare its entity-type from the 9-type taxonomy: `concepts/ | entities/ | sources/ | topics/ | ideas/ | experiments/ | claims/ | summaries/ | foundations/` [AUDIT §8.1]
- Concept-type entities (`wiki/concepts/`) must pass the Matuschak stranger test: declarative-sentence title, context-free body, ≤500 words — enforced by `/lint` stranger-test check (Wave C materialisation) [knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 3]
- Every new ingest event must produce ≥1 cross-reference update (concept link or graph edge) to an existing entity — the Karpathy compounding requirement [knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 1; Wave C target: ≥2 edges/entity]

**Deontics** (obligations of this part toward consumers):
- This part MUST answer queries via `/ask` with inline citations (`[src:path:section]`) — no synthesis without citation [FUNDAMENTAL §1 UC-B.4; D28; Karpathy: "wiki proves itself by answering questions with citations"]
- This part MUST expose a queryable index (`wiki/index.md`) so any consumer can discover anchor candidates without traversing raw file system [D28]
- `/ask --save` MUST file synthesis responses to `wiki/comparisons/` by default — discard requires explicit `--no-save` flag [knowledge-management-karpathy-luhmann-matuschak.md:§6 Part 3 item 3]
- This part MUST surface health signals to Part 8 via `/lint` on request: orphan count, stale-claims count, `contradicts`-edge density (target: ≥5% of total edges), average edges per entity [knowledge-management-karpathy-luhmann-matuschak.md:§6 Part 3 item 4; AUDIT §8.3]

**Effects** (measurable outcomes):
- After promotion of a new entity: entity is path-addressable at `wiki/<type>/<slug>.md`, indexed in `wiki/index.md`, and has ≥1 typed edge in `wiki/graph/edges.jsonl`; visible to `/ask` within the same session
- After `/lint` run: health report lists orphans, stale claims, missing-frontmatter entities — target 0 orphans and 100% frontmatter coverage
- Edge density: current baseline 577 edges / 552 entities = 1.05 avg [AUDIT §8.3]; Wave C target ≥2.0 edges/entity to enable non-trivial graph traversal [knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 1]
- `contradicts` + `supports` edge density: current ~1.5% of total edges [AUDIT §8.3 inferred]; Wave C `/lint` signal target: flag if < 5% [knowledge-management-karpathy-luhmann-matuschak.md:§6 Part 3 item 4]

---

## F. Anti-scope (per FUNDAMENTAL §6)

Generic (applies to all Foundation parts):
- This part does NOT make strategic decisions [FUNDAMENTAL §6.1]
- This part does NOT substitute for founder agency — knowledge is retrieved and surfaced; the founder decides what to do with it [FUNDAMENTAL §6.2]
- This part does NOT use engagement-economy patterns (no algorithmic feed, no "recommended for you" without explicit query) [FUNDAMENTAL §6.3]

Part-specific:
- This part does NOT own the accessor pipeline (U.System) — `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` are U.System accessor services owned by Part 4 or shared infrastructure; this boundary is the A-1 FLAG-MINOR correction [A-1-critic-gate.md:§6 item 4; FPF §1.4 A.1]
- This part does NOT do final strategic synthesis or produce strategic documents — synthesis answers (via `/ask`) are U.Episteme outputs that feed owner judgment; strategic documents are Part 9 territory
- This part does NOT enforce F-G-R compliance at promotion time — that is Part 6 (Governance) responsibility; Part 3 stores F-G-R tags, Part 6 checks them at gate [A-1-critic-gate.md:§2 Part 3 B.3: "Part 6 owns F-G-R enforcement; Part 8 owns the quarterly audit"]
- This part does NOT own CRM data (`crm/` directory) — CRM is a separate subsystem (Part 10 External Touchpoints); CRM graph edges that cross into `wiki/graph/edges.jsonl` are recorded here but the CRM content itself is Part 10 territory [AUDIT §7; CLAUDE.md CRM System]
- This part does NOT contain RUSLAN-LAYER ICP-specific content in `wiki/concepts/` — ICP-specific content belongs in `projects/` or `directions/` with links TO generic Foundation concepts [D27; knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 3]
- This part does NOT replace RAG (vector embedding, paid search) — the Karpathy wiki pattern explicitly rejects RAG ("the LLM is rediscovering knowledge from scratch on every question"); the wiki is a compiled, cited, maintained substrate [knowledge-management-karpathy-luhmann-matuschak.md:§4 Principle 6]
- This part does NOT own the Private Library (`raw/books-md/` — 393 books) as KB content — the library is raw source material that gets ingested through Part 2's pipeline; Part 3 holds the resulting extracted concepts and summaries, not the raw books [AUDIT §1.1; engineering-expert.md:§2 Part 2 AUDIT]

---

## G. F-G-R Tagging (per FPF B.3)

[FPF §4.2 CP-2; levenchuk-shsm-fpf.md:§4 P5]

| Artefact emitted | Formality (F0-F9) | ClaimScope (G) | Reliability (R) |
|---|---|---|---|
| `wiki/sources/<slug>.md` — bibliographic record (Luhmann "first cabinet") | F3 — multi-source informal; summarises an external source + adds provenance link | Holds for the specific source document's claims; not transferable to other sources without explicit `derived_from` edge | R-medium — human-acked at Part 2 STOP gate; accuracy depends on extraction quality |
| `wiki/concepts/<slug>.md` — atomic idea entity (Luhmann "second cabinet") | F4 — operational convention when validated in ≥1 cycle; F2-F3 for newly extracted concepts | Holds within the declared `context:` scope; must NOT assume cross-context validity without explicit Bridge F.9 [FPF IP-2] | R-medium — human-acked provenance; improved as cross-cycle evidence accumulates (F-level rises from F2 → F4 over cycle validation) |
| `wiki/graph/edges.jsonl` edge record | F4 — typed A.14 edge; operational convention enforced by `/lint` | Holds for the two entity slugs linked; invalidated if either entity is superseded without edge update | R-medium — structural link; requires periodic `/lint` to catch stale edges |
| `/ask` synthesis response (filed to `wiki/comparisons/`) | F3 — AI synthesis + cited sources; single-generation output | Holds for the query context at generation time; may be stale as KB grows | R-medium if filed with `--save` and cited; R-low if ephemeral chat only |
| Methodology library entry (`wiki/foundations/<slug>.md`) | F5 — codified when validated across ≥3 cycle applications; F3 initially | Holds for the system context where the methodology was validated; bridge required for other contexts [FPF IP-2 F.9] | R-high when F5+ (3 validated applications); R-medium at F3 (single-cycle extraction) |

---

## H. Originating + critic-flagged

**Originating experts:**
- engineering-expert (Part 2: Knowledge Substrate) — primary proposal; D28 anchor discipline + Karpathy LLM Wiki framing [engineering-expert.md:§2 Part 2]
- systems-expert (Part 1 partial: R1 reinforcing loop lives here)
- investor-expert (Part 2: Knowledge Compound Engine — methodology library as highest-compound asset after KB) [candidate-parts-merged.md:§2 Part 3 "Originating expert"]

**Critic flags applied from A-1 critic gate:**

**FLAG-MINOR resolved (2026-04-27):** A.1 pipeline sub-holon clarification.
- Original: pipeline sub-system described as "accessor service, not the part itself" — ambiguous holon affiliation
- Correction applied: explicit statement that the pipeline sub-system (accessor service) is a U.System component owned by Part 4 (coordination protocol infrastructure) or shared infrastructure — NOT a dangling U.System component internal to this U.Episteme part
- Applied in: U.System/U.Episteme boundary clarification at top of this card, §D Dependencies (note on accessor pipeline), §F Anti-scope (first part-specific bullet)
- Cite: [A-1-critic-gate.md:§6 item 4; FPF §1.4 A.1 Agency Rule; candidate-parts-merged.md:§2 Part 3 A-1 critic correction block]

**KM consultant card principles applied (all 6 from knowledge-management-karpathy-luhmann-matuschak.md §4):**
1. Wiki as compounding artefact → mandatory cross-reference step at ingest (§A Inputs, §E Effects)
2. One idea per note; link graph is the intelligence → concept-file atomicity in §E Admissibility
3. Stranger test → concept file quality discipline in §E Admissibility + §F Anti-scope
4. Organise by actionability → PARA-tier tag requirement (delegated to Part 2 §C Side-effects)
5. Query-driven KB → `/ask --save` default in §E Deontics
6. Typed graph edges → A.14 enforcement in §E Laws + §D Dependencies
