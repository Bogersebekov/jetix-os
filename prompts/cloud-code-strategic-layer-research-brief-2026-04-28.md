---
title: Cloud Code Brief — Strategic Layer Research + Scoping (Etap 2)
date: 2026-04-28
type: research-brief
target: Cloud Code on server (claude --dangerously-skip-permissions in tmux) — direct research mode (NOT ROY brigadier matrix dispatch)
purpose: Research strategic documents landscape from existing Jetix corpus (14 consultant cards + 391 books + 27 research compilations + memory) → propose 5-8 types best suited for Jetix context → produce structural templates ready for Ruslan ack
output_required: research output + template proposals committed to claude/jolly-margulis-915d34
estimated_walltime: 2-4h server CC work
critical_constraints:
  - This is RESEARCH + SCOPING, NOT new architecture creation
  - NO ROY brigadier matrix dispatch (overkill for landscape research). Single Cloud Code session с direct reads + integrator-mode synthesis
  - Output = catalogue + filtered proposals + structural templates (NOT content for documents themselves)
  - STOP after templates produced + AWAITING-APPROVAL recap → wait for Ruslan ack before commit to Foundation
---

# Cloud Code Brief — Strategic Layer Research + Scoping

## §0 What you (server CC) are doing

You are conducting **research + scoping** for the Strategic Layer (Etap 2 of Generalная чистка). Daily Log 28.04 sub-page documents the workstream:
🔗 https://www.notion.so/3502496333bf8103b848d596209b31f5

You will run **5 phases** end-to-end:
1. Landscape research (extract strategic doc types from corpus)
2. Categorization + filtering for Jetix context
3. Hierarchy + cadences definition
4. Structural templates creation (NOT content — templates only)
5. Compile proposal + commit AWAITING-APPROVAL

**Output paths (server):**
- `decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md` (~3-5K words landscape catalogue)
- `decisions/strategic/_research/jetix-fit-filtering-2026-04-28.md` (~1-2K words categorization + recommendations)
- `decisions/strategic/_research/hierarchy-cadences-2026-04-28.md` (~1-2K words hierarchy graph + cadence table)
- `decisions/strategic/_templates/<type-slug>.md.template` (5-8 template files)
- `decisions/strategic/_index.md` (manifest)
- `decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-28.md` (final proposal packet)

Commit + push when done. STOP. Notify Ruslan via tmux output:
> «Strategic Layer research + scoping complete. AWAITING-APPROVAL packet at <path>. Proposed 5-8 types ready for Ruslan walkthrough.»

---

## §1 Context

### Foundation status

10/10 Foundation parts F5 LOCKED at architecture level (Bundles 1-4 done, ack'd). Wave D Integration Pass running parallel в отдельной tmux session. Strategic Layer = **Etap 2 of Generalная чистка**.

### Key memories (FULL READ MANDATORY for context — these constrain Strategic Layer choices)

`C:\Users\49152\.claude\projects\C--Users-49152-Desktop-jetix-os\memory\` (or equivalent on server: locate via search). Critical files:

- `project_jetix_hybrid_framework_vision.md` — hybrid identity (consulting / agency / platform / holding / community)
- `project_jetix_partner_factory_top_lists.md` — Partner Factory + Bootstrap Loop (active Phase 1+)
- `project_future_directions_backlog.md` — M&A + Arbitrage Traffic deferred Phase-2+
- `project_jetix_private_library_knowledge_leverage.md` — KM-as-leverage moat (Pool first, query second)
- `project_outreach_channels.md` — IndieHackers as first channel
- `methodology_multi_chat_review_for_critical_docs.md` — 5-chat review pattern for critical docs (JETIX-NORTH-STAR должен делаться ИМЕННО так, не одной session)
- `feedback_ai_does_not_strategize.md` — AI generates options, Ruslan = sole strategist
- `feedback_no_solo_founder_downgrade.md` — enterprise + $1T baseline always, NOT solo-founder downgrade
- `project_jetix_next_focus.md` — system memory + KB architecture priority

### Constitutional baseline (already exists — Strategic Layer references, NOT replaces)

- FUNDAMENTAL Vision v1.0 LOCKED (`decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`) — 35 UC в 12 categories A-L + 55 anti-scope. Strategic Layer NEVER contradicts.
- JETIX-FPF.md (3758 lines, IP-1..IP-8, A.1-A.14) — constitutional Levenchuk base
- D1-D29 Locks + 4 LOCKS-ADDENDUMs

### Already-deferred Strategic items requiring Etap 2 attention

- **JETIX-NORTH-STAR** (deferred 27.04 morning) — DoT page integration (needs 5-chat methodology per memory)
- **Mentor briefing pack** (deferred 27.04 evening) — context для Антона
- **6 Strategic Insights** (active + deferred per memory):
  - Top Lists Partner Factory (ACTIVE Phase 1+ — explicit standalone direction)
  - AI-BIOS Moment (Phase 2+ deferred)
  - VISION-NEXT (Phase 2+ deferred)
  - AI-Psy-Led D30 candidate (Phase 2+ deferred)
  - M&A direction (Phase-2+ deferred — mittelstand succession 560k DACH)
  - Arbitrage Traffic (Phase-2+ deferred)

---

## §2 Scope — 5 Phases

### Phase 1 — Landscape research (~45-90 min)

**Goal:** Catalogue ~10-15 strategic document types found across the corpus.

**Inputs:**
- 14 consultant cards (`swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/`) — esp. PM Cagan-ShapeUp / Stoic-Epistemic / Capital-Allocation-Antifragility / Compounding-Engineering / Levenchuk
- 5 Wave B Supplement library-direct (Bai 2022 / Askell 2021 / Young 2010 / Google SRE Book + Workbook)
- 391 books в `raw/books-md/` — focus on:
  - PM/management books (`raw/books-md/pm/`, `raw/books-md/management/`)
  - Investing/capital books (Buffett letters / Munger / Marks / Naval / Holiday)
  - Stoic/epistemic books (Popper / Kuhn / Aurelius)
  - Левенчук systems books (`raw/books-md/systems/`)
- 27 research compilations в `raw/research/`
- 45 LJ posts Левенчук (skim — focus on strategy/vision-related posts)

**Output:** `decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md` (~3-5K words)

For each type extracted, provide:
- Name (canonical / common variants)
- 1-paragraph description "what it does"
- Origin framework (which book / blog / methodology)
- Typical user profile (solo / startup / enterprise / non-profit / etc)
- Cadence in source (annual / quarterly / event-driven)
- Example references

**Expected ~10-15 types in catalogue.** Don't artificially limit — capture what's actually in the corpus.

### Phase 2 — Filtering for Jetix context (~30-45 min)

**Goal:** From catalogue, propose 5-8 types best suited for Jetix.

**Filtering criteria (apply each per type):**
1. **Solo founder fit** — works without team? (e.g., OKR без team has marginal value)
2. **AI agents augment fit** — meaningful for Ruslan + agents hybrid?
3. **Phase 1 €50K relevance** — useful in next 3-6 months?
4. **Phase B+ readiness** — needed in Phase 2-3? (avoid premature optimization)
5. **Korp-Startup positioning fit (D29)** — coherent with strategy?
6. **FUNDAMENTAL §6 coherence** — doesn't violate anti-scope?
7. **Hybrid framework fit** (per `project_jetix_hybrid_framework_vision.md`) — supports consulting/agency/platform/holding/community blend?
8. **Memory feedback compliance** — `feedback_ai_does_not_strategize.md` (AI proposes, Ruslan decides) + `feedback_no_solo_founder_downgrade.md` (enterprise baseline always)

**Output:** `decisions/strategic/_research/jetix-fit-filtering-2026-04-28.md` (~1-2K words)

For each proposed type:
- Pass/Fail per 8 criteria (table)
- Net verdict: PROPOSE / SKIP / DEFER Phase B
- Rationale 2-3 sentences

**Expected output:** 5-8 PROPOSE types + 5-7 SKIP/DEFER types.

### Phase 3 — Hierarchy + cadences (~30-45 min)

**Goal:** For 5-8 PROPOSE types, define structure of relationships + lifecycle.

**Per type, declare:**
- **Hierarchy role:** parent / child / reference / standalone
- **Parent dependency:** which type must exist first (e.g., Strategy depends on Vision)
- **Cadence:** annual / quarterly / monthly / event-driven / append-only
- **Owner:** Ruslan-only (sole strategist per memory) / Ruslan + agent draft / agent draft + Ruslan ack
- **Trigger:** what initiates update (calendar / phase transition / external event / etc)
- **Audience:** internal-only / mentor / partners / public
- **F-level default:** typical F-tag for canonical version
- **Cross-references:** which Foundation parts (1-10) consume / produce input

**Output:** `decisions/strategic/_research/hierarchy-cadences-2026-04-28.md` (~1-2K words)

Include:
- Dependency graph (mermaid OR ascii art)
- Cadence calendar table (rows = types, cols = annual/quarterly/monthly/etc)
- Owner matrix (rows = types, cols = author / approver / reader)

### Phase 4 — Structural templates creation (~60-90 min)

**Goal:** For 5-8 PROPOSE types, create **structural templates** — frontmatter + section structure + minimal example fragment + anti-scope.

**Per template file (`decisions/strategic/_templates/<type-slug>.md.template`):**

```markdown
---
title: "<TYPE NAME> — <PLACEHOLDER subject>"
type: <type-slug>
version: <semver>
status: <draft | reviewed | accepted | canonical | LOCKED | superseded>
cadence: <annual | quarterly | monthly | event-driven | append-only>
owner: <ruslan-only | ruslan-plus-agent | agent-draft-ruslan-ack>
audience: <internal | mentor | partners | public>
F: <typical F-level>
G: "<ClaimScope>"
R: <typical R-level>
last_updated: <YYYY-MM-DD>
supersedes: <prior version path or null>
references:
  foundation_parts: [<part-N references if any>]
  fpf_anchors: [<IP-N or A.N references if any>]
  d_locks: [<D-N references if any>]
---

# <TYPE NAME> — <PLACEHOLDER subject>

## §1 <Section 1 name>
<1-2 sentence example fragment showing what goes here>

## §2 <Section 2 name>
<1-2 sentence example fragment>

...

## §N Anti-scope (what does NOT go in this document)
- <Anti-scope rule 1>
- <Anti-scope rule 2>

## §N+1 Provenance + sources
<expected citation format>
```

**Quality bar per template:**
- Frontmatter complete
- 4-8 sections defined (not too sparse, not too verbose)
- Each section has 1-2 sentence example fragment (NOT content — illustrative only)
- Anti-scope explicit (what NOT to put in this type)
- F-G-R defaults declared
- Cross-references to Foundation parts where applicable

**Output:** 5-8 `decisions/strategic/_templates/<type-slug>.md.template` files + `decisions/strategic/_index.md` manifest

### Phase 5 — AWAITING-APPROVAL packet (~15-30 min)

**Goal:** Compile proposal for Ruslan walkthrough.

**Output:** `decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-28.md`

Sections:
- §1 Executive summary (what was researched, what was proposed, walltime)
- §2 Landscape catalogue summary (10-15 types found — table)
- §3 Filtering results (5-8 PROPOSE, 5-7 SKIP/DEFER — with rationale)
- §4 Hierarchy + cadences proposal
- §5 Structural templates summary (links to each template file)
- §6 Open questions for Ruslan ack
- §7 Provenance + commits
- §8 STOP — awaiting Ruslan ack

---

## §3 Required reading list

### A. Memories (full read MANDATORY)

(Listed in §1.)

### B. Constitutional baseline

- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`
- `design/JETIX-FPF.md`

### C. Wave B research base (primary for landscape)

- 14 consultant cards — esp. PM Cagan-ShapeUp / Stoic-Epistemic / Capital-Allocation / Compounding-Engineering / Levenchuk
- 5 Wave B Supplement library-direct sources
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/MANIFEST-DRAFT.md`

### D. Library (selective deep reads)

Focus areas:
- `raw/books-md/pm/` — Cagan *Inspired* / Singer *Shape Up* / Torres *CDH* / Doerr OKR
- `raw/books-md/management/` — Drucker / Grove / Buffett (annual letters)
- `raw/books-md/investing/` — Munger / Marks / Naval / Holiday
- `raw/books-md/systems/` — Levenchuk LJ posts (skim — strategy-related)
- `raw/books-md/meta/` — Anthropic Building Effective Agents (esp. simplicity-transparency-trust triad)

### E. Research compilations

- 27 files in `raw/research/`
- Especially Levenchuk research compilations (~286K words total) — already extract strategic content patterns

### F. Notion sub-page (the brief itself)

- 🔗 https://www.notion.so/3502496333bf8103b848d596209b31f5 — read for additional context if accessible via fetch

---

## §4 Quality bar

- **Provenance:** every claim about a strategic doc type cites source (book / consultant card / research file)
- **Anti-cargo-cult:** don't propose a type just because it exists in the literature — proof of Jetix fit per 8 criteria
- **Honest declaration:** if some types in catalogue you're uncertain about — flag honestly
- **F-G-R DOGFOOD:** research output itself carries F-G-R tags
- **Word count target:** integrative, not bloated. Landscape ~3-5K / filtering ~1-2K / hierarchy ~1-2K / templates ~500-1500 each / AWAITING-APPROVAL ~2-3K
- **No premature content:** templates are STRUCTURAL only — don't write actual JETIX-NORTH-STAR content (that's next sprint with 5-chat methodology)

---

## §5 ETA + autocheck

**Walltime estimate: 2-4h Cloud Code direct work** (NO ROY brigadier — overkill for landscape research).

**Autocheck:**
- If walltime exceeds 6h — STOP, report
- If filtering produces > 10 PROPOSE types — too lenient, re-filter stricter
- If templates contain actual content (not structural) — scope creep, redo as templates only
- If any criterion application is ambiguous — flag in AWAITING-APPROVAL packet, defer to Ruslan

---

## §6 Branch + commit + STOP

- Branch: `claude/jolly-margulis-915d34`
- Commit pattern: `[strategic] <phase>` (e.g., `[strategic] landscape research catalogue`, `[strategic] templates structural draft`)
- Push after each phase
- Final commit: `[strategic] AWAITING-APPROVAL — Strategic Layer templates ready, 5-8 types proposed, hierarchy + cadences declared`

After AWAITING-APPROVAL packet — STOP. Ruslan ack required before any Strategic Layer document content writing (next sprint).

---

## §7 Operational

- `unset ANTHROPIC_API_KEY` before claude
- `ulimit -n 65535`
- HD-02 N=2

---

*End of brief. Mantra: RESEARCH > CREATION (this sprint). PROPOSE > DECIDE (Ruslan-only strategy). STRUCTURE > CONTENT (templates not docs). HONEST-FILTERING > LITERATURE-COMPLETENESS. RUSLAN-ACK > BRIGADIER-CONFIDENCE.*
