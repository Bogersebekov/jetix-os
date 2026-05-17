---
title: "mgmt × integrator — Foundation coherence + stakeholder map for JETIX-WORKING-FILE-v0"
type: integration-synthesis
produced_by: mgmt-expert
mode: integrator
expert: mgmt-expert
task_id: task-fpf-iwe-phase-b-2026-05-17
cycle_id: phase-b-2026-05-17
created: 2026-05-17
F: F4
F_scope: "holds for Phase A single-owner Jetix; unknown for Phase B multi-owner fork"
G: mgmt-integrator-working-file
R: "refuted_if: Foundation-locked-v1.0 changes between now and working-file publication, OR stakeholder reads diverge significantly from 5-reader assumption, OR brigadier's integration pass drops dissents from §9"
sources:
  - reports/jetix-vs-iwe-audit-2026-05-17.md
  - reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md
  - CLAUDE.md
  - canonical/INDEX.md
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md
  - decisions/JETIX-TRM-MODEL-2026-04-30.md
  - decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - decisions/JETIX-DOCUMENT-MAP-2026-05-15.md
  - swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md
  - swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md
  - swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md
  - swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md
  - swarm/wiki/foundations/principles/architecture.md
provenance_inline: true
acceptance_test: partial
dissents_count: 3
---

# mgmt × integrator — Foundation coherence + stakeholder map for JETIX-WORKING-FILE-v0

> **Constitutional posture.** Integrator mode = scribe / structurer / surface.
> R1 preserved: no strategic prose authored. R6 preserved: every claim cites path.
> This draft is input to brigadier's integration pass; brigadier integrates all 3 cells
> (eng × scalability + mgmt × integrator + phil × critic) before writing canonical.

---

## §1 Cross-claim syntheses from input artefacts

### §1.1 What working-file is vs what it is not

**Claim.** JETIX-WORKING-FILE-v0 is a DERIVATIVE narrative document, not a source-of-truth.
Foundation v1.0 is locked (`foundation-architecture-locked-2026-04-28`). The working file
is an INDEX + NARRATIVE overlay on top of the locked foundation.

`F: F5 | ClaimScope: holds for Phase A; NOT valid after any Foundation revision | R: refuted_if Foundation revision merges into working file without explicit annotation`

Source: [src:CLAUDE.md §Foundation Architecture v1.0 LOCKED] + [src:canonical/INDEX.md §3]

**Critical derivation contract.** Every reference to a Foundation Part in the working file
carries: (a) one-sentence description, (b) path, (c) status (F5 LOCKED), (d) "read <path>
for full spec" link. The working file NEVER duplicates the Part's architecture inline.

`F: F4 | ClaimScope: holds for this document generation; may evolve | R: refuted_if duplication found in final working file by brigadier's C1-type critic check`

### §1.2 Working-file scope vs adjacent documents

Three documents already serve partial working-file functions:

| Existing doc | Function served | Gap it leaves |
|---|---|---|
| `decisions/JETIX-DOCUMENT-MAP-2026-05-15.md` | Visual orientation (mermaid × 3) + reading tracks per audience | Not self-contained for 30-min read; requires following links |
| `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` (Doc 1A) | Universal base management system ~1h40 read | No Jetix-specific operational detail; too generic |
| `decisions/JETIX-CORPORATION-2026-05-05.md` (Doc 1B) | Jetix Corp applied use case ~2h30 read | Too business-pitch oriented; missing technical depth + R12 + swarm architecture |

[src:canonical/INDEX.md §2] + [src:decisions/JETIX-DOCUMENT-MAP-2026-05-15.md §0]

**Working-file synthesis claim.** JETIX-WORKING-FILE-v0 fills a gap that none of the three
above fills: a single navigable document for readers with 5–60 min budgets who want
Foundation coherence (not just concept), architecture (not just pitch), and Jetix-unique
mechanisms (R12, F-G-R enforcement, 5-layer memory, B2 mini-swarm) surfaced in one place.

`F: F4 | ClaimScope: holds for current 5 stakeholder profiles identified in §2 | R: refuted_if doc-map already serves this fully (Tseren/Levenchuk empirical read-test)`

---

## §2 Stakeholder map for the working file

Per mgmt × integrator rubric item 1. Five stakeholder profiles with reading budget + purpose + acceptance predicate per profile.

| # | Stakeholder | Reading budget | Purpose | Acceptance predicate (Hamel-binary) |
|---|---|---|---|---|
| **S1** | Ruslan (self-reference) | 5 min (self-scan) | Verify nothing contradicts Foundation-locked; calibration check before sharing | "Every section in working file cites ≥1 canonical path; no section claims F > F5 for working-file-layer claims" |
| **S2** | Tseren Tserenov (IWE practitioner / FPF-aligned) | 15 min | Understand Jetix architecture at mechanism level; identify overlap with IWE; assess whether Jetix's F-G-R + R12 are genuine FPF-derivative or superficial | "§ Workshop metaphor + §§ R12 + F-G-R Halt-Log-Alert + UNIQUE-5 mechanisms are each surface-level accessible within 15 min read-path; NO marketing claims without falsifier" |
| **S3** | Левенчук (theoretical FPF fidelity judge) | 30 min | Test whether Jetix's FPF claims are legitimate (IP-1, IP-7, A.6.B, B.3 per his framework); detect C3 / C5b violations | "IP-1 Role≠Executor named; F-G-R enforcement described with operational mechanism (Part 6a path); Halt-Log-Alert grade timing stated; C3 self-audit honest section present; NO overclaiming of FPF-grade without C4 benchmark" |
| **S4** | Future Jetix partner / L1 onboarding candidate | 30 min | Understand what they're joining: Workshop metaphor + TRM model + R12 protection + Phase evolution | "TRM model (6 resources) named with §; R12 anti-extraction stated plainly and path-cited; 3-phase evolution (solo→team→network) present; AWAITING-APPROVAL gate discipline explained as corrigibility mechanism" |
| **S5** | Future Jetix-instance forker (technically sophisticated) | 60 min | Understand what to fork: Foundation Parts 1-11 + Pillar C + schemas; what is RUSLAN-LAYER vs Foundation generic; UNIQUE-5 mechanisms to preserve | "Foundation Parts table with RUSLAN-LAYER column (what's generic vs instance-specific per IP-2); IP-1 Role≠Executor fork discipline; UNIQUE-5 mechanisms listed with file paths; clear statement: 'fork Foundation generic, rewrite RUSLAN-LAYER'" |

**Stakeholder accountability.** Single named owner per deliverable-type per Cagan/Drucker discipline:

- Decision on tone (marketing vs technical): Ruslan (HITL) — not mgmt-expert or brigadier
- Primary prose authorship in working file: Ruslan (per Tier 2 R1, FUNDAMENTAL §6.1 rule 1)
- Technical depth calibration per S3/S5: brigadier integrator pass (incorporating eng × scalability cell)
- R12 + constitutional framing: philosophy-expert × critic cell (per Phase B cell matrix)

`F: F4 | ClaimScope: Phase A 5-profile stakeholder map; Phase B may add 6th profile (investor-specific) | R: refuted_if Ruslan identifies missing stakeholder profile before working-file publication`

[src:decisions/JETIX-DOCUMENT-MAP-2026-05-15.md §6 reading tracks] + [src:reports/jetix-vs-iwe-audit-2026-05-17.md §0 comparability table]

---

## §3 Content priority (CRITICAL / IMPORTANT / NICE-TO-HAVE)

Target: ~1500–2500 lines. Reading budget hierarchy: S1 5 min → S5 60 min.

### §3.1 CRITICAL — must-have for L1 acceptance (≈600–800 lines of working-file body)

Each CRITICAL item has an acceptance predicate. Failure to include = working-file rejected by brigadier's critic pass.

| # | Content block | Why CRITICAL | Acceptance predicate |
|---|---|---|---|
| **C1** | Workshop metaphor (§0 TL;DR + §1 ядро + §3 owner roles) | Primary frame for ALL stakeholders; S2/S3/S4 all read via this lens; already LOCKED canonical | "Workshop metaphor named in first 200 lines; 'мастерская' word present; adaptability as moat named" |
| **C2** | Foundation 11 Parts summary table (1-page, not duplicated) | S3/S5 need architecture overview without reading 11 × 50+ pages; table already exists in `canonical/INDEX.md` | "Table of 11 Parts + Pillar C with: one-sentence mission per Part + path + F5 LOCKED status + 'read-full' link; total ≤30 lines" |
| **C3** | R12 anti-extraction — plain language + path | Jetix-UNIQUE mechanism (J-U2 per audit §3); most distinctive from FPF; S4 reads this as member-protection promise | "R12 stated plainly: 'AI/substrate cannot extract beyond agreed share; members fork-and-leave without penalty'; path to `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` + H7 cited; F2 / G / R triple present" |
| **C4** | Calibration statement (working file is derivative, not SoT) | Prevents C1-type Levenchuk critique (JETIX-FPF.md overreach pattern); prevents S5 from treating working-file content as authoritative schema | "Explicit statement in §0 or §1: 'This document is INDEX+NARRATIVE. Foundation v1.0 LOCKED at `swarm/wiki/foundations/`. On any conflict, Foundation wins.'" |
| **C5** | TRM model (6 resources) | Core business model; S4 needs this to understand the value proposition of joining | "6 resources named (Capital/Founder-time/Audience/Knowledge/Compute/Talent); TRM = 'management fee + performance fee per resource' stated; path to JETIX-TRM-MODEL-2026-04-30.md" |
| **C6** | Corrigibility / HITL gate discipline — one paragraph | S3 (Levenchuk) will test whether AI-agent system has owner-override mechanism; Pillar C Tier 2 rule 2/7/9 depend on this | "AWAITING-APPROVAL packet described; Part 6b path cited; 'owner ack-authority is final' stated; example gate type named" |
| **C7** | UNIQUE-5 Jetix mechanisms (J-U1..J-U5) | Differentiators for S2/S3; prevents conflation with vanilla agent stack | "UNIQUE-5 table present; each mechanism: name + 1-sentence description + canonical path; J-U2 (R12) cross-linked to C3 block" |

### §3.2 IMPORTANT — include if line-budget allows (≈500–700 lines)

| # | Content block | Why IMPORTANT | Can omit if |
|---|---|---|---|
| **I1** | Phase evolution (solo → team → network) with horizon gates | S4/S5 need this to understand commitment horizon; JETIX-CORPORATION-2026-05-05.md has the detail | Phase B produces separate evolution doc |
| **I2** | Honest self-audit summary (C3 response) | S3 tests epistemic honesty; Phase A summary §5 covers this | Separate C3-response artefact produced in Phase B |
| **I3** | F-G-R per-claim enforcement mechanism description | S3 specific test; Part 6a path + Halt-Log-Alert timing | Dedicated FPF-mechanisms table added |
| **I4** | IWE UNIQUE-11 gap acknowledgment (5 gaps Jetix lacks) | Honest calibration; prevents S3 from reading working-file as defensive | If honest-self-audit section covers it |
| **I5** | 5-layer per-agent memory architecture (J-U3) | S5 forker needs this; CLAUDE.md §Wiki Architecture v2 has the spec | If eng × scalability cell covers architecture depth |
| **I6** | Swarm coordination (brigadier + 5 ROY experts; hub-and-spoke) | S5 needs swarm topology for forking | Part 4 summary in Foundation table covers partially |

### §3.3 NICE-TO-HAVE — defer to Phase B if line-budget exceeded

| # | Content block | Defer to |
|---|---|---|
| **N1** | C4 benchmark design (4-arm comparison) | `reports/fpf-iwe-distillation-2026-05-17/diagrams/10-c4-benchmark-design.md` |
| **N2** | Full IWE vs Jetix side-by-side (UNIQUE-11 vs UNIQUE-5) | `reports/jetix-vs-iwe-audit-2026-05-17.md` |
| **N3** | Monetization bank (75H+ hypotheses) | `decisions/monetization-v0-*.md` |
| **N4** | CRM system architecture | `crm/README.md` |
| **N5** | Voice pipeline operational detail | CLAUDE.md §Voice-Notes Pipeline |
| **N6** | Residency R0 application path | `raw/external/levenchuk-corpus-2026-05-17/` |

`F: F4 | ClaimScope: 1500-2500 line target; if brigadier expands scope → IMPORTANT items promote to CRITICAL | R: refuted_if line-budget changes before working-file write`

[src:reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md §5] + [src:reports/jetix-vs-iwe-audit-2026-05-17.md §3] + [src:canonical/INDEX.md §2]

---

## §4 Workshop metaphor + TRM surfacing strategy

### §4.1 «Meta-workshop for professional masters» framing

The Jetix-Corporation doc (Doc 1B) positions Jetix as «применение Базовой Системы под конкретный бизнес-кейс (Mittelstand DACH)». [src:decisions/JETIX-CORPORATION-2026-05-05.md frontmatter `relationship`]

The Workshop-Concept doc describes the metaphor as: мастерская для работы с информацией — постоянный активный процесс, есть мастер + работники + инструменты, есть конкретные deliverables, adaptive, knowledge accumulates. [src:decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md §0 TL;DR]

**Surfacing strategy for working file.**

Layer 1 (first 200 lines — all stakeholders see this):
- Workshop metaphor as primary frame: «Jetix = мастерская для работы с информацией»
- Key distinction: «не дом (статичный) — активный процесс с deliverables»
- Adaptability as primary moat: continuous capability expansion

Layer 2 (S2/S3 technical frame — within 600 lines):
- TRM 6-resource model: Workshop manages all 6 (not just capital)
- Connect to Foundation: Workshop metaphor = Doc 1A/1B conceptual layer; Foundation Parts 1-11 = operational substrate
- Surface without technical depth the key claim: «information in → transformed information out»

Layer 3 (S4 partner frame — within 1200 lines):
- «Meta-workshop for professional masters» = the Phase 2+ framing from Doc 1B §фазы эволюции
- Jetix as network of workshops (solo → team → community of practitioners)
- For S4: «you are not joining a consulting firm; you are joining a network of informational-work practitioners each building their own workshop on the same Foundation»

**Tone discipline.** WORKSHOP metaphor is Ruslan-authored (dictated 2026-04-30); working file inherits it as canonical frame, not as AI-generated metaphor. Attribution: «[JETIX-WORKSHOP-CONCEPT-2026-04-30.md — Ruslan-dictated LOCKED]».

`F: F5 (Workshop metaphor itself is F5 LOCKED) | ClaimScope: metaphor holds for Phase A solo; Phase B network framing needs Ruslan-authored overlay | R: refuted_if metaphor collapses under real partner use case (per Workshop doc own R field)`

[src:decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md frontmatter `R: refuted_if_metaphor_collapses_under_real_use_case`]

### §4.2 TRM without losing technical depth

TRM model is Doc 1B's business-model layer. For working file: surface in IMPORTANT block I1, not CRITICAL, because:
- S3 (Levenchuk) reads Jetix as technical system, not as business pitch
- S5 (forker) needs Foundation architecture, not TRM business model
- S4 (partner) needs TRM, but that's a 30-min read and Doc 1B already serves it

**Integration recommendation.** Working file §TRM = 1 paragraph + table of 6 resources + path to full doc. NOT full TRM detail inline.

`F: F4 | ClaimScope: 1500-2500 line working file | R: refuted_if brigadier's integration pass expands working-file scope to 5000+ lines`

---

## §5 Foundation 11 Parts coherence for L1 reader

### §5.1 Proposed 1-page Foundation table structure

The canonical/INDEX.md §3 already has the table. Working file should REFERENCE it, not duplicate. For the working file body, the summary table format:

| # | Part name | One-sentence mission | Key invariant | Path |
|---|---|---|---|---|
| 1 | System State Persistence | Append-only event log + git = filesystem SoT | No mutable state outside git | `swarm/wiki/foundations/part-1-*/architecture.md` |
| 2 | Signal Ingestion & Triage | Voice/email/text inbox → structured items | OWC: classify before route | `swarm/wiki/foundations/part-2-*/architecture.md` |
| 3 | Knowledge Base & Methodology Library | Wiki substrate + methodology accumulation | Karpathy++ queryable KB | `swarm/wiki/foundations/part-3-*/architecture.md` |
| 4 | Role Taxonomy & Coordination Protocol | IP-1 Role≠Executor + hub-and-spoke routing | Routing rules ≥20 (Ashby variety) | `swarm/wiki/foundations/part-4-*/architecture.md` |
| 5 | Compound Learning & Methodology Capture | Cycle retrospective → strategies.md → methodology promotion | DRR ledger per cycle | `swarm/wiki/foundations/part-5-*/architecture.md` |
| 6a | Provenance Officer | F-G-R per-claim enforcement | Every promoted claim carries (F,G,R) triple | `swarm/wiki/foundations/part-6a-*/architecture.md` |
| 6b | Human Gate | Default-Deny + AWAITING-APPROVAL gate | Halt-Log-Alert: F8≤1s / F4≤5s / F2≤60s | `swarm/wiki/foundations/part-6b-*/architecture.md` |
| 7 | Project Lifecycle Substrate | Stage-gated 5-state machine per project | Appetite-as-constraint (Shape Up); event-driven cadence | `swarm/wiki/foundations/part-7-*/architecture.md` |
| 8 | Health Monitoring & System Integrity | SLI counters + alert routing | Fail-loud; no silent swallowing | `swarm/wiki/foundations/part-8-*/architecture.md` |
| 9 | Owner Interaction Scaffold | Daily-log + weekly-review + 3-tier SLA | Attention-budget cap: ≤20 active tasks | `swarm/wiki/foundations/part-9-*/architecture.md` |
| 10 | External Touchpoints & Network Interface | CRM + outreach + partner interface | Voice-pipeline DRAFT-only: never auto-overwrite | `swarm/wiki/foundations/part-10-*/architecture.md` |
| 11 | Strategic Direction Substrate (Pillar A) | 6 strategic-doc types + Decisions DB | Ruslan = sole strategic-prose author (IP-7) | `swarm/wiki/foundations/part-11-*/architecture.md` |
| Pillar C | Principles Foundation sub-system | Two-tier (Tier 1 manager + Tier 2 system) | 12 Tier-2 hard rules; R12 = additive 2026-05-12 | `swarm/wiki/foundations/principles/architecture.md` |

**Key message for L1 reader (S2/S4).** The 11 Parts are not a bureaucratic checklist. They are the operational substrate that turns the «workshop» metaphor into a running system. Part 6b (Human Gate) + Pillar C (R12) together are the «corrigibility layer» that ensures the owner retains control at all times.

`F: F4 | ClaimScope: summary table describes Foundation as-of-2026-04-28 LOCK; any future revision = Foundation wins | R: refuted_if any Part's mission changes before working-file publication`

[src:swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md §0 Mission] + [src:swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md frontmatter ClaimScope] + [src:swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md §0 Mission] + [src:swarm/wiki/foundations/principles/architecture.md §0 Mission]

---

## §6 R12 surfacing strategy

### §6.1 R12 as constitutional anchor

**Claim.** R12 (anti-extraction) is the highest-priority UNIQUE Jetix mechanism (J-U2) for two stakeholder profiles: S4 (future partner — member protection promise) and S3 (Levenchuk — mechanism not in FPF, genuine differentiation).

`F: F4 | ClaimScope: holds per audit §3 J-U2 + §7 Meadows L2 classification | R: refuted_if IWE paid platform reveals equivalent mechanism`

[src:reports/jetix-vs-iwe-audit-2026-05-17.md §3 J-U2] + [src:reports/jetix-vs-iwe-audit-2026-05-17.md §7 leverage points]

**R12 plain-language statement.** From canonical source: «AI / substrate cannot extract value from members beyond agreed share; members can fork-and-leave without penalty.» [src:CLAUDE.md §4.1 rule 12]

**Constitutional anchor chain** (for working file cross-linking):
- Packet: `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md`
- Strategic insight: `decisions/strategic/H7-people-ns-*.md` (H7 People-NS LOCKED 2026-05-12)
- Pillar C enforcement: `swarm/wiki/foundations/principles/architecture.md` (Tier 2, rule 12)
- Clan Charter: referenced in CLAUDE.md §4.1 footnote `[src: H7 People-NS LOCKED 2026-05-12 commit 93b796d]`

### §6.2 Surfacing options for working file

**Option A (constitutional anchor style).** R12 appears as §1 item in a «Pillar C Tier 2 hard rules» mini-table, with same weight as rules 1-11. Benefit: not singled out. Risk: diluted among 12 rules.

**Option B (separate highlighted block).** R12 gets its own paragraph with «additive 2026-05-12» origin note and Meadows L2 (system goals level) classification. Benefit: stakeholder S4 reads it as a promise; S3 reads it as differentiation. Risk: appears marketing-y if tone is not calibrated.

**Option C (cross-linked from Workshop metaphor).** Workshop §3 «owner roles» section cites R12 as the mechanism that makes «fork-and-leave without penalty» real. Benefit: narrative integration. Risk: buried in Workshop metaphor discussion.

**Integration recommendation for brigadier.** Option B for S4 path + Option C for S3 path; both short (≤3 sentences each) with canonical path citations. The working file does NOT expand on R12 beyond what the canonical packet says.

`F: F4 | ClaimScope: recommendation is mgmt-expert scribe output; Ruslan decides tone | R: refuted_if R12 packet content changes before working-file publication`

---

## §7 Cross-link economy

### §7.1 Principle

Per brief item 6: «every existing canonical artefact gets at most 1 sentence + path; the working file is INDEX + NARRATIVE, not duplication.»

**Operationalized rule for working file construction:**
- Each canonical artefact cited: 1-sentence mission + path + lock date (if LOCKED) + estimated read time
- NO inline content > 10 lines from any canonical source
- References cluster in the Foundation table (§5.1 above) and the Reading tracks section

### §7.2 Cross-link budget (recommended, per artefact category)

| Category | Max inline lines per artefact | Format |
|---|---|---|
| Foundation Parts (11 + Pillar C) | 1 sentence | Table row only |
| Constitutional docs (FUNDAMENTAL, Pillar C) | 2 sentences | Table row + 1 callout |
| Workshop/TRM canonical | 1 paragraph (~5 lines) | Named section header + path |
| R12 packet | 1 paragraph (~5 lines) | Named section header + path chain |
| UNIQUE-5 mechanisms | 1 sentence each in table | Table; no expansion inline |
| Honest self-audit (C3 answer) | 1 paragraph (~5 lines) + path | Named section |
| Reading tracks (Doc Map §6) | Reference only: path + «see §6 in Document Map» | 1 sentence |

**Dissent note.** Brigadier's eng × scalability cell may request more technical depth for S5 (forker). If so, cross-link budget for Foundation Parts can expand to 3 sentences (architecture pattern + key invariant + fork-note). This is a trade-off between line budget and S5 coverage that brigadier resolves in the integration pass.

`F: F4 | ClaimScope: 1500-2500 line budget assumption | R: refuted_if eng cell's architectural depth estimate exceeds this budget`

[src:decisions/JETIX-DOCUMENT-MAP-2026-05-15.md §0 «Это НЕ заменяет» section]

---

## §8 Risk register

Eight risks to the working file being accepted by all five stakeholder profiles. Per mgmt × critic discipline: each risk has a binary detection criterion and a response.

| # | Risk | Detection criterion | Response |
|---|---|---|---|
| **RK-1** | Too marketing-y — S3 (Levenchuk) and S2 (Tseren) dismiss as promotional | Working file contains ≥3 sentences of «Jetix is better than X» without falsifier | Remove or qualify with F2 rating + C4 benchmark requirement stated explicitly |
| **RK-2** | Too technical — S4 (future partner) cannot complete 30-min read path without context | Working file assumes Foundation architecture knowledge in first 600 lines | Move all Foundation table to §2 (not §1); place Workshop metaphor first; label reading tracks at top |
| **RK-3** | Too long — no stakeholder completes their stated budget read | Working file exceeds 2500 lines | Brigadier's integration pass: apply §3 CRITICAL-only filter; move IMPORTANT to appendix |
| **RK-4** | Missing freshness signal — S3 reads Foundation table and sees 2026-04-28 lock date as stale | Working file has no «as of» freshness anchor | Add freshness statement: «Foundation v1.0 LOCKED 2026-04-28; next review triggers at Phase B; current HEAD: <git_commit_hash>» |
| **RK-5** | R12 not surfaced — S4 (partner) joins without knowing exit-without-penalty rule | R12 not mentioned in first 1200 lines | R12 is CRITICAL block (§3.1 C3); if missing → brigadier rejects working file at integration pass |
| **RK-6** | Wrong tone — R1 violated: working file appears to contain AI-authored strategic prose | `prose_authored_by:` field not set; OR working file contains «следует» / «лучше» / «рекомендуется» AI-evaluative phrases | Set frontmatter: `prose_authored_by: ruslan (primary) + ai-scribe (structure)`; run AP-MGMT-2 style check on evaluative language |
| **RK-7** | Foundation-SoT confusion — S5 (forker) treats working-file schema description as authoritative spec | Working file has CRITICAL block C4 (calibration statement) missing | C4 is non-negotiable; brigadier's integration pass checks C4 presence before canonical write |
| **RK-8** | C3-type overreach repeat — working file claims Jetix «is FPF-grade» without C4 benchmark | Phrases like «полная FPF-реализация» / «FPF-grade system» present without benchmark qualification | Replace with: «FPF-adjacent tactical adoption; ~7 direct derivations; C4 benchmark pending» per Phase A §5.1 honest calibration |

`F: F4 | ClaimScope: risk register covers Phase A working-file v0; Phase B risks (multi-stakeholder, public distribution) not covered | R: refuted_if any RK fires during Tseren/Levenchuk empirical read test without detection`

[src:reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md §5.1 C3 honest answer] + [src:reports/jetix-vs-iwe-audit-2026-05-17.md §8 honesty calibration] + [src:decisions/JETIX-DOCUMENT-MAP-2026-05-15.md frontmatter `prose_authored_by: ai-draft`]

---

## §9 Calibration statement (explicit, per brief item 8)

**The working file is a DERIVATIVE narrative. It is not the source-of-truth for any Jetix mechanism.**

The authoritative sources are:
- Constitutional: `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (35 UC × 12 categories, 11 hard rules; LOCKED v1.0)
- Foundation: `swarm/wiki/foundations/` (11 Parts + Pillar C; LOCKED 2026-04-28 tag `foundation-architecture-locked-2026-04-28`)
- Pillar C principles: `swarm/wiki/foundations/principles/architecture.md` (12 Tier-2 rules)
- R12: `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md`
- Canonical INDEX: `canonical/INDEX.md` (110 LOCKED docs map)

**On any conflict between working-file text and any of the above:** the above wins. Working file is not self-authorizing.

**The pattern this avoids.** `design/JETIX-FPF.md` (3762 lines) was a prior attempt at a «comprehensive Jetix spec» artefact; it was archived 2026-05-06 after Levenchuk C1 critique partial-hit. [src:reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md §5 «1 heavy derivative archived»]. JETIX-WORKING-FILE-v0 is NOT a repeat of that pattern: it is INDEX+NARRATIVE, not spec.

`F: F5 (Foundation-LOCKED fact) | ClaimScope: holds for working-file v0; Phase B may warrant a spec if Foundation evolves | R: refuted_if Foundation revision makes this calibration statement stale`

---

## §10 Dissents preserved (per AP-6 / AP-MGMT-11)

Three dissent pairs surface from the input artefacts read in this synthesis. Each retained per E-5.

### DIS-1 — Working file audience: technical depth vs accessibility trade-off

**Position A (S3/S5 emphasis).** Working file should lead with Foundation architecture table and F-G-R enforcement mechanism. Levenchuk reads technical depth first; without it, file reads as marketing deck.
`F: F4 | ClaimScope: S3/S5 profiles | R: refuted_if S3 empirical read confirms he reads Workshop metaphor first`
Evidence: [src:reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md §3 formulations 3+4 — Levenchuk values structural architecture claims]

**Position B (S4 emphasis).** Working file should lead with Workshop metaphor + TRM. Partner onboarding requires accessible narrative before technical depth.
`F: F4 | ClaimScope: S4/S1 profiles | R: refuted_if partners report working file as too dense`
Evidence: [src:decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md §reading tracks — investor + partner tracks start with §1 concept, not §4 architecture]

**Reconciliation (not averaging).** Both positions valid for different read-paths. Working file structure: §0 TL;DR (Workshop metaphor, S4-accessible) → §1 Calibration + Foundation table (S3/S5-accessible within 500 lines) → §2 UNIQUE-5 mechanisms (S3 test) → §3 R12 constitutional anchor (S4 promise). The DOCUMENT MAP `decisions/JETIX-DOCUMENT-MAP-2026-05-15.md` §2 mermaid already shows reading ladder structure — working file can borrow that pattern.

### DIS-2 — R12 framing: constitutional vs business promise

**Position A (phil × critic would surface).** R12 as Pillar C Tier 2 rule = technical constraint on AI/substrate. Framing as «member protection promise» for S4 is a category shift that may feel like marketing.
`F: F4 | ClaimScope: phil × critic lens | R: refuted_if phil cell's draft confirms both framings are compatible`
Evidence: [src:reports/jetix-vs-iwe-audit-2026-05-17.md §7 — R12 classified as Meadows L2 «system goals» not L1 «numbers»]

**Position B (mgmt × integrator).** R12 is simultaneously a constitutional rule AND a stakeholder promise — the same rule serves both S3's epistemic test and S4's membership commitment. Not a conflict.
`F: F4 | ClaimScope: mgmt-expert integrator framing | R: refuted_if Ruslan confirms only one framing appropriate`

**Reconciliation.** Working file presents R12 once in full (constitutional framing: «Pillar C Tier 2 rule 12, LOCKED 2026-05-12»). The plain-language implication (fork-and-leave without penalty) follows as derivation, not as separate marketing claim. Phil × critic cell's draft is authoritative for tone calibration on R12 framing — brigadier defers on this dissent to phil × critic output.

### DIS-3 — Honest self-audit: how much C3 acknowledgment is appropriate in working file

**Position A (conservative).** Working file is for orientation/onboarding. Foregrounding C3 critique («mostly right» on intelligence-amplification gap) risks confusing S4 partners who haven't read Phase A research.
`F: F4 | ClaimScope: S4 partner profile | R: refuted_if S4 reads C3 as strength (intellectual honesty)`
Evidence: [src:decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md — no self-critique section; orientation-focused]

**Position B (S3-driven).** Without C3 acknowledgment, working file fails Levenchuk test and repeats JETIX-FPF.md overreach pattern. S3 reads the absence as defensive; epistemically dishonest.
`F: F5 | ClaimScope: S3/Levenchuk profile; also Tier 2 R1+R6 compliance | R: refuted_if Levenchuk explicitly says self-critique is unnecessary for his evaluation`
Evidence: [src:reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md §5.1 «C3 = mostly right»]

**Reconciliation.** Include a «Honest calibration» section (≤8 lines) in the working file after UNIQUE-5 mechanisms block. Frame per Phase A §5.1 language: «~25% intelligence-amplification components; FPF-adjacent tactical adoption; C4 benchmark pending.» Label it clearly so S4 can skip if not relevant to them. This is IMPORTANT (not CRITICAL) per §3.2 I2.

---

## Summary fields (for brigadier structured return parse)

```yaml
summary: >
  mgmt × integrator surfaces 5-profile stakeholder map (5/15/30/30/60 min budgets),
  CRITICAL/IMPORTANT/NICE content priority for 1500-2500 line target, Workshop+TRM
  surfacing strategy, 13-row Foundation table format, R12 constitutional anchor
  options A/B/C, cross-link economy rules, 8-item risk register, calibration statement,
  and 3 dissents. R1 preserved: no strategic prose authored. Brigadier defers to
  phil × critic on R12 tone, eng × scalability on technical depth budget.
proposed_writes:
  - path: swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-mgmt-integrator-jetix-working-file.md
    status: written (this file)
provenance:
  - {path: "reports/jetix-vs-iwe-audit-2026-05-17.md", range: "§3 J-U1..J-U5 + §7 leverage", quote: "R12 anti-extraction — Jetix-unique paradigm-level lever (Meadows L2)"}
  - {path: "reports/jetix-vs-iwe-audit-2026-05-17.md", range: "§4 I-U1..I-U11"}
  - {path: "reports/jetix-vs-iwe-audit-2026-05-17.md", range: "§8.1 + §8.2 + §8.3 + §8.4"}
  - {path: "reports/jetix-vs-iwe-audit-2026-05-17.md", range: "§5 overlap registry"}
  - {path: "reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md", range: "§5 honest self-audit + §5.1 C3 + §5.2 UNIQUE-5"}
  - {path: "reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md", range: "§6 Phase B readiness"}
  - {path: "CLAUDE.md", range: "§4.1 Tier 2 rule 12 + §Foundation Architecture v1.0 LOCKED"}
  - {path: "canonical/INDEX.md", range: "§2 system-concept + §3 Foundation table"}
  - {path: "decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md", range: "§0 TL;DR + §1 ядро + §3 owner roles"}
  - {path: "decisions/JETIX-TRM-MODEL-2026-04-30.md", range: "§1 суть идеи + 6-resource table"}
  - {path: "decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md", range: "frontmatter + §reading tracks"}
  - {path: "decisions/JETIX-CORPORATION-2026-05-05.md", range: "frontmatter relationship field + audience"}
  - {path: "decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md", range: "§0 two-layer pattern + §1 use cases"}
  - {path: "decisions/JETIX-DOCUMENT-MAP-2026-05-15.md", range: "§0 + §1 + §2 mermaid + §6 reading tracks"}
  - {path: "swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md", range: "§0 Mission IP-1"}
  - {path: "swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md", range: "frontmatter ClaimScope + bundle_5_supplement"}
  - {path: "swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md", range: "frontmatter ClaimScope + ip2_single_owner_bounded"}
  - {path: "swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md", range: "§0 Mission + UC-A.1..A.4"}
  - {path: "swarm/wiki/foundations/principles/architecture.md", range: "§0 Mission + two-tier structure"}
confidence: high
confidence_method: artefact-direct-read
escalations: []
dissents:
  - {position: "Working file should lead with Foundation architecture table for S3/S5", evidence: ["reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md:§3"], F: F4}
  - {position: "Working file should lead with Workshop metaphor for S4/S1", evidence: ["decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md:§reading tracks"], F: F4}
  - {position: "R12 framing as constitutional vs as business promise requires phil × critic arbitration", evidence: ["reports/jetix-vs-iwe-audit-2026-05-17.md:§7"], F: F4}
  - {position: "C3 acknowledgment in working file: conservative (confusing for S4) vs required (epistemic honesty for S3)", evidence: ["reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md:§5.1"], F: F5}
```
