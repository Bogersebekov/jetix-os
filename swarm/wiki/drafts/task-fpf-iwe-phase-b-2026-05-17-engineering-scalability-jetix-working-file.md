---
title: "Engineering × Scalability — JETIX-WORKING-FILE-v0 Architecture Proposal"
type: scalability-proposal
task_id: task-fpf-iwe-phase-b-2026-05-17
cycle_id: task-fpf-iwe-phase-b-2026-05-17
expert: engineering-expert
mode: scalability
artefact_to_propose: JETIX-WORKING-FILE-v0-2026-05-17.md
date: 2026-05-17
F: F4
G: scalability-proposal-engineering
R: refuted_if_brigadier_integrates_and_finds_structural_contradiction_OR_L1_reader_cannot_navigate_in_15min
ClaimScope: "Holds for JETIX-WORKING-FILE-v0 as a single navigable artefact for L1 audience (Levenchuk/Tseren); does not govern per-cycle journals, Foundation Part bodies, or RUSLAN-LAYER secrets"
prose_authored_by: engineering-expert (scribe mode — architecture proposal; strategic prose is Ruslan's to write)
provenance_sources:
  - reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md
  - reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md
  - reports/jetix-vs-iwe-audit-2026-05-17.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md
  - decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md
  - swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md
  - canonical/INDEX.md
---

# engineering × scalability — JETIX-WORKING-FILE-v0 Architecture Proposal

> **Mode.** scalability. Scribe-mode — this document proposes artefact architecture
> (TOC, section budget, reading paths, scalability projections). It does NOT author
> strategic prose. Brigadier integrates this output with mgmt × integrator and
> phil × critic, then Ruslan writes the canonical JETIX-WORKING-FILE-v0.
>
> **Constitutional posture.** R1 (scribe, not strategist), R2 (Foundation paths
> read-only — propose links only), R6 provenance per claim. All cross-links are
> proposals; brigadier gates.

---

## §1 Single-Artefact Architecture Proposal

### §1.1 Design constraints (derived from brief + input reads)

Four hard constraints shape the artefact architecture:

1. **L1 reader in 15 minutes** — Levenchuk and Tseren are FPF-native readers. They will
   scan for: (a) what Jetix IS in one sentence, (b) how it maps to FPF primitives they
   already know, (c) what is unique about it vs IWE (their reference point). The artefact
   must surface these in the first scroll.
   `[reports/jetix-vs-iwe-audit-2026-05-17.md:§0 comparability check]`

2. **Single file ~1500-2500 lines** — mirrors FPF-Spec structure (one large spec + README)
   and Levenchuk's "всего один" positioning principle. Fragmentation into multiple files
   requires coordination overhead that the €50K gate cannot afford.
   `[reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md:§0]`

3. **Fork-portable by design** — at €1M gate the file must support «Jetix-for-person-X»
   fork (IWE Pack pattern, I-U1 gap). This requires clean FUNDAMENTAL / RUSLAN-LAYER
   boundary markers within each major section.
   `[decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md:§0 "Layer 1 of 2" principle]`

4. **FPF-facing vocabulary** — L1 audience thinks in U.Holon / U.Role / U.Method / U.Alpha.
   The artefact must translate Jetix mechanisms into FPF primitives OR explicitly name
   where Jetix diverges. Non-translation creates reader confusion.
   `[reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md:§3 primitives]`

### §1.2 Structure choice: FPF-Spec mirror vs IWE README vs hybrid

Three structural options evaluated:

| Option | Shape | Kill condition |
|---|---|---|
| **A — FPF-Spec mirror** | Preface + Part A kernel + Part B reasoning + Part C extensions + Part D ethics + Part E constitution + Part F UTS + Part G SoTA (~7 parts) | Kills if Jetix doesn't yet have FPF-grade formal proof machinery for Parts D/E/F/G — premature formalism, AP-ENG-9 (premature abstraction) |
| **B — IWE README mirror** | Problem + Solution + Who-for + Use cases + Practice + Getting started + Customization + Documentation + FAQ + Community (~10 sections) | Kills if L1 FPF audience finds README framing too product-facing and non-rigorous; mismatches FPF culture of spec-first documentation |
| **C — Hybrid: IWE navigation skin + FPF-spec interior (SELECTED)** | QR-NAV card first + one-liner + one-paragraph + 12-16 top-level sections organized as Kernel / Architecture / Mechanisms / Positioning + appendices | Selected: IWE's reading-path discipline (QR-NAV + OWC-at-doc-level) + FPF's per-mechanism precision format; fits 1500-2500 line budget; supports fork-portable boundary markers |

**Selection rationale.** The hybrid matches the 01-v2 artefact structure already accepted
by Ruslan as a reference (§QR-NAV + multi-path reading). It applies IWE's onboarding
discipline to FPF-grade content. The kill conditions for A and B are engineering-grade
failures: premature formalism (A) violates Brooks no-silver-bullet (§2.4 AP-ENG-9);
product framing (B) conflicts with L1 audience's bias toward rigorous spec.
`[reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md:§QR-NAV]`

`F: F4 | G: engineering-proposal | R: refuted_if_brigadier_integrator_finds_hybrid_incoherent`

---

## §2 TOC Outline — 14 Top-Level Sections

Proposed section headers with one-line description, reading-time budget, and LOC estimate.
Total target: 2000 lines (within 1500-2500 budget; leaves 500-line expansion margin).

> **Naming convention.** Every section header uses `§N` prefix to mirror FPF-Spec §-anchor
> convention. This makes grep-navigation predictable for FPF-native readers.

| § | Title | Description | LOC est. | Read-time |
|---|---|---|---|---|
| §QR | QR-NAV card | 5-min / 15-min / 30-min / 60-min reading paths; TOC table | 25 | 2 min |
| §0 | Freshness snapshot | What version/date this file reflects; git tag; live pointers to canonical | 20 | 1 min |
| §1 | Jetix in one sentence | Verbatim one-liner + 3 candidate formulations; the FPF-facing translation | 30 | 2 min |
| §2 | Jetix in one paragraph | 30-sec elevator; FUNDAMENTAL Layer 1 + RUSLAN-LAYER 2 framing | 50 | 3 min |
| §3 | 5 core primitives | U.Holon / U.Role / U.Method / U.Alpha / U.BoundedContext as realized in Jetix | 150 | 10 min |
| §4 | Architecture — 11 Foundation Parts | Foundation v1.0 LOCKED: one-paragraph per Part + inter-Part edge count; no duplication of Part bodies | 200 | 12 min |
| §5 | Unique mechanisms (UNIQUE-5) | J-U1 Strategic Hexagon / J-U2 R12 anti-extraction / J-U3 5-layer memory / J-U4 B2 mini-swarm / J-U5 F-G-R enforcement | 200 | 12 min |
| §6 | Positioning vs FPF / IWE | Mechanism-side-by-side; honest §8 structure (where each works/doesn't/parity); complementary framing | 200 | 12 min |
| §7 | Use cases (UC map) | 35 UC → Part map table; 5 key use-case worked examples for L1 | 150 | 8 min |
| §8 | Multi-agent architecture | Hub-and-spoke; 12 agents × 6 depts; brigadier dispatch model; BOSC-A-T-X phase ladder | 150 | 8 min |
| §9 | Constitutional rules | 12 Tier-2 hard rules; R12 anti-extraction; IP-1 Role≠Executor; Default-Deny table; Halt-Log-Alert | 100 | 6 min |
| §10 | Lifecycle + feedback loops | 6 Jetix feedback loops (J-L1..J-L6); compound engineering cadence | 100 | 6 min |
| §11 | Getting started (fork guide) | For a reader who wants to apply Jetix: Layer 1 = FUNDAMENTAL (fork here); Layer 2 = RUSLAN-LAYER (yours to write); minimum viable activation | 120 | 6 min |
| §12 | Anti-patterns + what Jetix is NOT | 12 explicit anti-patterns from JETIX-CORPORATION §12; tests | 80 | 4 min |
| §13 | Decision index | Pointer-only table to 110 canonical docs; date + status + one-line; no inlining | 100 | 5 min |
| §A | Appendix: Glossary | 20-30 terms; FPF-to-Jetix translation table | 80 | 4 min |
| §B | Appendix: Mermaid diagrams | 3-4 embedded diagrams; per §4 cross-link | 50 | 3 min |

**Total estimated: ~1805 lines**. Within 1500-2500 budget.

`F: F4 | G: engineering-proposal | R: refuted_if_brigadier_finds_critical_section_missing_after_mgmt_integrator_pass`

---

## §3 Reading-Path Map

Four reading paths, mirroring 01-v2 §QR-NAV pattern. Each path is ADDITIVE
(longer path = shorter path + more sections, not replacement).

### §3.1 5-minute skim (L1 first contact)

**Path:** §QR → §0 → §1 → §2 → QR-CARD at tail

**Goal:** Answer "what is Jetix in 30 seconds; is this relevant to me?"

**Unlocks:** L1 reader can decide whether to invest 15 minutes. No mechanism knowledge required.

**Acceptance predicate:** L1 reader can state Jetix one-liner + Layer 1/2 framing after §1 + §2.

### §3.2 15-minute dive (L1 primary target)

**Path:** 5-min + §3 (primitives) + §5 (UNIQUE-5) + §6 (vs FPF/IWE)

**Goal:** Answer "how does Jetix map to what I already know; what is genuinely different?"

**Unlocks:** FPF-native reader (Levenchuk/Tseren) can form a grounded opinion on
Jetix's unique mechanisms vs IWE. This is the PRIMARY acceptance criterion for Phase B.

**Acceptance predicate:** L1 reader identifies ≥2 of UNIQUE-5 mechanisms and their
FPF-primitive mapping.

### §3.3 30-minute full

**Path:** 15-min + §4 (Foundation Parts) + §8 (multi-agent arch) + §9 (constitutional rules) + §7 (UC map)

**Goal:** Answer "how is it actually built; what are the architectural invariants?"

**Unlocks:** Potential collaborator / first hire can orient themselves.

### §3.4 60-minute deep

**Path:** Full doc including §10 (feedback loops) + §11 (fork guide) + §12 (anti-patterns) + §13 (decision index) + appendices

**Goal:** Complete architectural briefing; enables fork decision or cooperation proposal.

`F: F4 | G: engineering-proposal | R: refuted_if_15min_path_exceeds_500_lines_unreadable`

---

## §4 Top-Level Mermaid Placement

### §4.1 Placement recommendation: §4 Architecture — immediately after Foundation summary table

**Rationale.** The primary mermaid (Jetix system architecture overview) should appear
at the FIRST place where a reader needs spatial orientation — which is §4, after reading
the 11 Foundation Parts summary table. At that point the reader has the Part names but
needs to see how they connect. Placing the mermaid in §4 prevents back-referencing.

**Secondary mermaid.** A mini mermaid showing the BOSC-A-T-X phase ladder (€50K → €200K
→ €1M → $100M → $1T) belongs in §8 (multi-agent architecture) to show how the agent
count/structure evolves per phase.

**Tertiary mermaid (optional).** §QR QR-card can embed a 10-node minimal mermaid showing
the 3-layer architecture (Layer 1 FUNDAMENTAL / Layer 2 RUSLAN-LAYER / Layer 3 Operational)
as a visual fingerprint for the 5-min path.

### §4.2 Mermaid source reference

Existing diagram candidate in JETIX-FIRST-CLAN-CHARTER §1.0a.viz (Workshop Architecture mermaid).
This can be adapted for the working file. Link, don't duplicate body.
`[decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md:§1.0a.viz]`

`F: F4 | G: engineering-proposal | R: refuted_if_mermaid_renders_incorrectly_in_target_markdown_viewer`

---

## §5 Cross-Link Strategy

### §5.1 Principle: link, don't duplicate (≤30 char quote rule)

Every reference to a canonical document uses a link + one-line summary only.
No section of the working file duplicates more than 30 characters of a Foundation Part body.
This enforces the deep-module principle: the working file is a thin interface over the
deep Foundation implementation.
`[swarm/wiki/foundations/part-1-system-state-persistence/architecture.md:§0 "deep module frame"]`

### §5.2 Link table — proposed cross-links per section

| Working file § | Links to | Link type |
|---|---|---|
| §1 (one-liner) | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §0` | canonical anchor |
| §2 (paragraph) | `decisions/JETIX-CORPORATION-2026-05-05.md §0.TL;DR` | applied use case |
| §3 (primitives) | `design/JETIX-FPF.md` (IP-1/IP-2/IP-3/IP-7) | FPF derivative |
| §4 (Foundation Parts) | `swarm/wiki/foundations/part-N-*/architecture.md` × 11 | one link per Part |
| §5 (UNIQUE-5) | `reports/jetix-vs-iwe-audit-2026-05-17.md §3` | source audit |
| §6 (positioning) | `reports/jetix-vs-iwe-audit-2026-05-17.md §8` | honest audit source |
| §7 (UC map) | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md §1` | UC source |
| §8 (multi-agent) | `swarm/lib/shared-protocols.md` | runtime contract |
| §9 (constitutional) | `principles/tier-2-system/foundation-generic/` + `.claude/config/default-deny-table.yaml` | constitutional source |
| §10 (feedback loops) | `reports/jetix-vs-iwe-audit-2026-05-17.md §6.1` | loop registry |
| §11 (fork guide) | `decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md` | Layer 1 fork point |
| §12 (anti-patterns) | `decisions/JETIX-CORPORATION-2026-05-05.md §12` | anti-pattern source |
| §13 (decision index) | `canonical/INDEX.md` | 110 docs pointer |
| §A (glossary) | `reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md §QR-CARD` | FPF terms |

### §5.3 Banned inlining

The following content MUST NOT be inlined in the working file (anti-scope §8):

- Full bodies of Foundation Part architecture.md documents (11 files)
- Full body of JETIX-VISION-FUNDAMENTAL-2026-04-27.md (2624 lines)
- Cycle logs and per-cycle journals
- critic/optimizer draft outputs
- Archive content
- Any content from `private/` or `.env`

`F: F4 | G: engineering-proposal | R: refuted_if_working_file_exceeds_2500_lines_due_to_inlining`

---

## §6 F-G-R Discipline Per Section

Every major section of the working file carries an F-G-R footer. Proposed defaults:

| Working file § | F | G | R |
|---|---|---|---|
| §0 Freshness | F8 (git tag = cryptographic proof) | jetix-canonical | refuted_if_git_tag_absent |
| §1 One-liner | F5 (codified; RUSLAN-ACK 2026-04-28) | jetix-canonical | refuted_if_Ruslan_rejects_formulation |
| §2 Paragraph | F4 (operational convention) | jetix-synthesis | refuted_if_formulation_disputed_by_Ruslan |
| §3 Primitives | F5 (codified; FUNDAMENTAL LOCKED) | jetix-canonical | refuted_if_FPF_primitive_mapping_wrong |
| §4 Foundation | F5 (LOCKED 2026-04-28 with Ruslan acks) | jetix-canonical | refuted_if_any_Part_ack_missing |
| §5 UNIQUE-5 | F4 (audit finding; not formal benchmark) | jetix-synthesis | refuted_if_C4_benchmark_shows_no_advantage |
| §6 Positioning | F4 (audit; template not paid-platform) | comparative-audit | refuted_if_paid_IWE_reveals_equivalents |
| §7 UC map | F5 (LOCKED FUNDAMENTAL §1) | jetix-canonical | refuted_if_UC_count_changes |
| §8 Multi-agent | F5 (CLAUDE.md agent roster LOCKED) | jetix-canonical | refuted_if_agent_count_changes |
| §9 Constitutional | F8 (constitutional; Halt-Log-Alert grade) | jetix-constitutional | refuted_if_Ruslan_rescinds_rule |
| §10 Feedback loops | F4 (systems synthesis; not formal) | jetix-synthesis | refuted_if_loop_structure_changes |
| §11 Fork guide | F3 (prescriptive; not yet tested) | jetix-prescriptive | refuted_if_first_fork_attempt_fails |
| §12 Anti-patterns | F5 (CORPORATION LOCKED §12) | jetix-canonical | refuted_if_new_category_surfaces |
| §13 Decision index | F5 (canonical/INDEX.md LOCKED 2026-05-06) | jetix-canonical | refuted_if_INDEX_diverges |

`F: F4 | G: engineering-proposal | R: refuted_if_brigadier_finds_F-level_inconsistency`

---

## §7 BOSC-A-T-X Scalability Projection — 5 Gates

> **BOSC-A-T-X legend:** B=Behavior, O=Operation, S=Scale, C=Composition, A=Agency,
> T=Time, X=eXternal. Gates per HD-01 Option C cycle-2-impl.

### §7.1 Gate table

| Gate | BOSC first-fire | MHT event | Engineering observable for working file | Refactor % estimate |
|---|---|---|---|---|
| **€50K** (current, single owner) | **B+S** — the working file itself is the primary artifact; its reading-contract (15-min L1) is the first behavior that must hold | **Phase Promotion** — file transitions from draft to L1-navigable canonical artefact | QR-NAV card renders; §1 + §2 + §5 fit 5-min path; file passes `/lint` frontmatter check; git commit with tag `jetix-working-file-v0-2026-05-17` | 0% — file is brand new at this gate |
| **€200K** (small team; first hire/partner) | **A=Agency** — the file becomes onboarding artifact; a new reader with no prior Jetix context must navigate in 30 min; §11 (fork guide) becomes load-bearing | **Phase Promotion** — working file promotes from «L1 artifact for known audience» to «onboarding artifact for unknown audience» | §11 fork guide tested by first hire; §QR reading paths validated empirically; §13 decision index resolves ≥95% of first-hire questions without direct Ruslan time | 15-20% — §11 fork guide needs hardening; glossary expansion; likely add §14 «FAQ for first hires» (~80 lines) |
| **€1M** (multi-instance; file supports fork-and-customize) | **C=Composition** — file must separate cleanly into FUNDAMENTAL section (forkable) vs RUSLAN-LAYER section (non-forkable); §1d split-trigger equivalent for the artefact itself | **Fission** — working file splits into [JETIX-FUNDAMENTAL-v1.md] (generic, forkable for any person's Layer 1) + [JETIX-RUSLAN-LAYER-v1.md] (Ruslan-specific RUSLAN-LAYER instance) + [JETIX-WORKING-FILE.md] (composite navigation layer pointing at both) | Three-file architecture exists; FUNDAMENTAL file has no Ruslan-specific content; RUSLAN-LAYER file has explicit «override slots» per JETIX-VISION-FUNDAMENTAL §0 dual-doc principle; fork attempt by new person succeeds without editing FUNDAMENTAL | 40-50% — fundamental restructuring of §1-§9 into FUNDAMENTAL vs RUSLAN-LAYER split; not a content change but an architectural reorganization matching the split the FUNDAMENTAL vision already anticipates |
| **$100M** (org-scale; multi-author) | **C=Composition + X=eXternal** — working file becomes organizational spec; must support multi-author contribution; regulatory context (SOC2/GDPR if client data) | **Role-Lift** — artefact becomes «Jetix Corporation Operating Manual» at spec-grade; requires formal versioning, change-request protocol, reviewer roles | File has CHANGELOG, version tags (≥1.0.0 SemVer), review-by-role table; §4 Foundation Parts have version pins; §9 Constitutional rules have formally cited sources per Part 6a F8 discipline | 30-40% — mostly structural formalization; content mostly preserved; adds ~500 lines of governance metadata |
| **$1T** (substrate; open-source OS for thought) | **X=eXternal + T=Time** — the file becomes the «Jetix open standard»; per-language localization; MVPK multi-view publication (FPF E.17) | **Context Reframe** — file is no longer Ruslan's operational reference; it is a community-maintained standard that Ruslan governs but does not solely author | Repository has localized copies (RU/EN/DE minimum); MVPK bundles exist per audience type; contribution protocol published; file is referenced by ≥1 external practitioner independent of Ruslan | 60-70% — deep architectural change; the single working file becomes a multi-artifact publication system; this gate's scope is beyond current planning horizon and requires separate HITL gate |

`F: F4 | G: engineering-scalability-projection | R: refuted_if_gate_triggers_occur_out_of_sequence`

### §7.2 Antifragility check (4-axis ≤30% refactor test)

| Axis | At 10× scale | Fragile? | Evidence |
|---|---|---|---|
| **Structure 10×** (sections grow 14 → 140) | Single-file format collapses; requires hierarchical structure | **YES — fragile** at $100M gate; managed by §7.1 Fission event at €1M (split pre-empts this failure) | IWE Pack pattern (I-U1 gap in audit) is the countermeasure; must be imported at €1M gate |
| **Reader 10×** (1 reader → 10 readers with different backgrounds) | QR-NAV paths must cover more personas; §11 fork guide must be richer | **PARTIAL — manageable** with §14 FAQ expansion at €200K gate; 15% refactor | Mitigated by the persona-specific reading paths already in §QR |
| **Content 10×** (110 canonical docs → 1100) | §13 decision index becomes unnavigable; requires semantic search substrate | **YES — fragile** at $100M gate; requires Karpathy wiki semantic substrate | Part 3 Knowledge Base (swarm/wiki/foundations/part-3) is the mitigant |
| **Lifecycle 10×** (file updated 1x → 10x per month) | No TTL discipline (I-U4 / I-L5 gap from audit); freshness signals degrade | **PARTIAL — manageable** with §0 freshness snapshot discipline + git tag pinning | IWE I-U11 TTL pattern addresses this; Jetix §0 Freshness + git tag is 60% equivalent |

`F: F4 | G: engineering-scalability-antifragility | R: refuted_if_10x_structure_test_passes_without_split`

---

## §8 Janus Degraded-Mode Spec

Per §6.2 of engineering-expert system prompt: two failure modes for this artefact
context.

### §8.1 S-A excess — «working file that never integrates»

**Symptom.** The working file accumulates depth in §5 (UNIQUE-5) and §9
(Constitutional) but fails to build §6 (Positioning vs FPF/IWE) and §11 (Fork guide).
The file becomes a self-referential Jetix spec that does not bridge to L1 audience.
Measurable: §6 missing OR §11 missing at first publication.

**Swarm response.** Brigadier writes AWAITING-APPROVAL gate. Ruslan reviews §6 and
§11 personally and either writes them directly or re-dispatches integrator cell with
explicit forcing clause: «§6 MUST bridge to FPF/IWE vocabulary; §11 MUST contain
a tested fork walkthrough».

**Recovery predicate.** `§6 body ≥ 150 lines AND includes Jetix-vs-IWE mechanism table AND §11 body ≥ 100 lines AND includes at least one worked fork example.`

### §8.2 INT excess — «working file that only points to other files»

**Symptom.** The working file is almost entirely links and one-liners; every section
resolves to «see Foundation Part N for details». L1 reader opens the file, follows
5 links, finds no synthesized content, abandons.
Measurable: average section body < 50 lines (excluding frontmatter and §13 index).

**Swarm response.** Brigadier re-dispatches engineering × optimizer with forcing clause:
«each section must carry ≥50 lines of synthesized content; links are supplementary,
not primary».

**Recovery predicate.** `count(sections with body < 50 lines) ≤ 3 (only §QR, §0, §A are exempt as structural shells).`

`F: F4 | G: engineering-degraded-mode | R: refuted_if_degraded_modes_do_not_materialize`

---

## §9 Anti-Scope

What MUST NOT be in JETIX-WORKING-FILE-v0:

- **Per-cycle journals.** Cycle logs (`swarm/wiki/cycles/`) are operational traces, not
  L1-readable content. Link from §13 at most; never inline.
- **Draft critic/optimizer outputs.** `swarm/wiki/drafts/` content is engineering working
  material. The working file is the synthesis, not the working material.
- **Full Foundation Part bodies.** Each of the 11 Part architecture.md files runs 200-800
  lines. The working file carries the one-paragraph summary + link only (§5.2 cross-link
  table). Inlining violates the deep-module principle and pushes the file past 2500 lines.
- **RUSLAN-LAYER secrets.** `private/`, `.env`, personal CRM records, specific client
  names, financial projections beyond the trajectory already published in
  `decisions/JETIX-CORPORATION-2026-05-05.md §8`.
- **Archive content.** Pre-Foundation artefacts in `archive/` are historical; they
  confuse L1 readers.
- **Unverified positioning claims.** C5b-style «Jetix умнее конкурентов» without
  C4 benchmark run. §6 must apply the same epistemic standard as the audit
  (`reports/jetix-vs-iwe-audit-2026-05-17.md §9 C5b applied to Jetix`).
- **Unit economics / financial projections beyond public trajectory.** Investor-territory
  per engineering-expert scope walls §1b. Brigadier routes to investor × integrator.
- **Strategizing prose.** The working file surfaces mechanisms and architecture; it
  does NOT author Ruslan's strategic direction. Any sentence framed as «Jetix should…»
  or «Ruslan's strategy is…» requires Ruslan's authorship per FUNDAMENTAL Tier 2 R1.

`F: F5 | G: engineering-anti-scope | R: refuted_if_prohibited_content_found_in_working_file`

---

## §10 Summary Return Packet

```yaml
mode: scalability
context:
  task_id: task-fpf-iwe-phase-b-2026-05-17
  artefact_path: JETIX-WORKING-FILE-v0-2026-05-17.md (to be written by brigadier)
  cycle_id: task-fpf-iwe-phase-b-2026-05-17

horizon_projection:
  - gate: "€50K"
    BOSC_first_fire: "B+S"
    MHT_event: "Phase Promotion (draft → L1-navigable canonical)"
    observable: "QR-NAV renders; 15-min path confirmed by L1 read; git tag present"
    refactor_pct_estimate: 0

  - gate: "€200K"
    BOSC_first_fire: "A"
    MHT_event: "Phase Promotion (L1 artifact → first-hire onboarding artifact)"
    observable: "§11 fork guide tested; §QR validated empirically; §13 resolves 95% first-hire questions"
    refactor_pct_estimate: 15

  - gate: "€1M"
    BOSC_first_fire: "C"
    MHT_event: "Fission (single file → FUNDAMENTAL + RUSLAN-LAYER + nav composite)"
    observable: "3-file architecture; fork by new person succeeds; FUNDAMENTAL file has zero RUSLAN-LAYER content"
    refactor_pct_estimate: 45

  - gate: "$100M"
    BOSC_first_fire: "C+X"
    MHT_event: "Role-Lift (personal ref → organizational spec; multi-author)"
    observable: "SemVer versioning; change-request protocol; reviewer roles; regulatory metadata"
    refactor_pct_estimate: 35

  - gate: "$1T"
    BOSC_first_fire: "X+T"
    MHT_event: "Context Reframe (organizational spec → open community standard)"
    observable: "Multi-language; MVPK bundles; external practitioner citations; community contribution protocol"
    refactor_pct_estimate: 65

degraded_mode_spec:
  S_A_excess:
    symptom: "§6 and §11 absent; file is deep but not bridged to L1 audience"
    swarm_response: "brigadier AWAITING-APPROVAL gate; Ruslan reviews §6 + §11 personally"
    recovery_predicate: "§6 body ≥ 150 lines with Jetix-vs-IWE table AND §11 body ≥ 100 lines with worked fork example"
  INT_excess:
    symptom: "average section body < 50 lines; file is almost entirely links"
    swarm_response: "brigadier re-dispatches engineering × optimizer with ≥50 line forcing clause"
    recovery_predicate: "count(sections with body < 50 lines) ≤ 3"

antifragility_check:
  build_system_10x:
    fragile: "yes — at $100M gate (section proliferation breaks single-file format)"
    evidence: "managed by €1M Fission event; pre-emptive split avoids failure"
  architecture_pattern_10x:
    fragile: "partial — reader persona 10× requires FAQ expansion; manageable at €200K"
    evidence: "§QR multi-path + §11 fork guide absorbs persona diversity"
  test_suite_10x:
    fragile: "no — working file is a documentation artefact, not executable code; no test suite latency axis"
    evidence: "N/A for documentation artefact"
  dependency_graph_10x:
    fragile: "yes — §13 decision index collapses at 1100+ canonical docs; requires semantic substrate"
    evidence: "Part 3 Knowledge Base is the long-term mitigant; §13 is a stopgap"

recovery_predicate: "S-A: §6 ≥ 150 lines + §11 ≥ 100 lines; INT: avg section ≥ 50 lines excl. shells"

proposed_writes:
  - path: swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-engineering-scalability-jetix-working-file.md
    frontmatter:
      title: "Engineering × Scalability — JETIX-WORKING-FILE-v0 Architecture Proposal"
      type: scalability-proposal
      expert: engineering-expert
      mode: scalability
      F: F4
      G: scalability-proposal-engineering
      R: refuted_if_brigadier_integrates_and_finds_structural_contradiction
    body: "[this file]"
    edges_to_add: []

provenance:
  - path: reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md
    range: "1-75"
    quote: "5-min: §0 + §1 + §2 + §QR; 15-min: + §3 + §6.1 + §6.4"
  - path: reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md
    range: "56-74"
    quote: "QR-NAV TOC table with reading-path map"
  - path: reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md
    range: "65-83"
    quote: "Pack = source-of-truth для доменного знания"
  - path: reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md
    range: "93-108"
    quote: "fallback chain DS → Pack → SPF → FPF → ZP"
  - path: reports/jetix-vs-iwe-audit-2026-05-17.md
    range: "34-46"
    quote: "Comparison is NOT a category error at mechanism layer"
  - path: reports/jetix-vs-iwe-audit-2026-05-17.md
    range: "72-84"
    quote: "J-U1..J-U5 UNIQUE-5 table"
  - path: reports/jetix-vs-iwe-audit-2026-05-17.md
    range: "90-108"
    quote: "I-U1..I-U11 UNIQUE-11 table"
  - path: reports/jetix-vs-iwe-audit-2026-05-17.md
    range: "177-193"
    quote: "§8.1 where IWE WORKS but Jetix doesn't; §8.2 where Jetix WORKS but IWE doesn't"
  - path: reports/jetix-vs-iwe-audit-2026-05-17.md
    range: "127-158"
    quote: "6 Jetix feedback loops J-L1..J-L6"
  - path: decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
    range: "20-47"
    quote: "Layer 1 FUNDAMENTAL + Layer 2 RUSLAN-LAYER dual-doc principle"
  - path: decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
    range: "60-75"
    quote: "Система = усилитель мозга + двойной вектор улучшение + сохранение"
  - path: decisions/JETIX-CORPORATION-2026-05-05.md
    range: "1-44"
    quote: "Jetix Corp = applied use case Базовой Системы"
  - path: decisions/JETIX-CORPORATION-2026-05-05.md
    range: "72-75"
    quote: "TL;DR: AI-native operational корпорация + TRM + 3 фазы"
  - path: decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md
    range: "58-60"
    quote: "Jetix претендует не просто на workshop… но на virtual state"
  - path: decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md
    range: "12-15"
    quote: "§1.0a «Что есть Jetix» + 3-layer architecture mermaid"
  - path: swarm/wiki/foundations/part-1-system-state-persistence/architecture.md
    range: "40-47"
    quote: "Git is the most durable artifact format; deep-module frame"
  - path: swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md
    range: "22-55"
    quote: "11 LOCKED Parts + Pillar C; 35 UC → 100% routed; 52 inter-Part edges 98.1%"
  - path: canonical/INDEX.md
    range: "1-60"
    quote: "110 LOCKED canonical docs map; primary orientation"

confidence: medium
confidence_method: artefact-direct-read
escalations: []
dissents: []
```

---

## §11 Engineering notes for brigadier integration

Three items for the brigadier integrator pass:

1. **§6 Positioning** (UNIQUE-5 vs IWE) is the highest-stakes section for L1 acceptance.
   The phil × critic cell should validate the epistemic discipline in §6 before brigadier
   promotes. Specifically: the C5b-symmetric framing (no «Jetix умнее» without benchmark)
   must be preserved from the audit.
   `[reports/jetix-vs-iwe-audit-2026-05-17.md:§9]`

2. **§11 Fork guide** has F3 (prescriptive; not yet tested). The mgmt × integrator cell
   should flag whether the current strategic documents (FUNDAMENTAL + BASE-MANAGEMENT-SYSTEM)
   are sufficient for a first-fork walkthrough or whether a gap exists. Do not write
   speculative fork steps — raise as `escalations[]{trigger: peer-input-needed}` if gap found.

3. **Mermaid rendering.** The §B appendix mermaid diagrams should be validated against
   the target markdown viewer (likely GitHub or Obsidian). If the JETIX-FIRST-CLAN-CHARTER
   §1.0a.viz mermaid already exists and renders, reuse it. Do not create a new diagram
   that duplicates existing canonical work.
   `[decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md:§1.0a.viz]`

`F: F4 | G: engineering-integration-notes | R: refuted_if_brigadier_finds_notes_internally_contradictory`
