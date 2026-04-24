---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-systems-integrator-§12-tools
title: "§12 Tools per Phase — Financial Tracking Roadmap"
type: cell-draft
cell: C-10
expert: systems-expert
mode: integrator
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
task_id: T-layer-7-business-trajectory-deep-dive-2026-04-25
created: 2026-04-25
word_floor: 800-1200
status: drafted
provenance_inline: true
locks_referenced: [D15, D17, D18, D19, D21, D25, D26, D27, D28]
sources:
  - {path: "swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md", range: "§4 28 Locks + §8 anti-scope"}
  - {path: "decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md", range: "§14.0-§14.4 Tools Roadmap — cross-reference boundary"}
  - {path: "decisions/JETIX-ARCHITECTURE-BRIEF.md", range: "§3.1.5 payment + §3.1.12 financial tracking + §6 C2 revenue-gated"}
  - {path: "decisions/JETIX-PLAN.md", range: "§2.1 GmbH + §3.8 budget + §6 Phase-3 holding"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D25 Company-as-Code git-native provenance"}
  - {path: "swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§7-cashflow.md", range: "§7.2.1 compute-ledger numbers + §7.2.2 burn + §7.1 starting cash"}
confidence: high
confidence_method: gate-decomposition
escalations: []
dissents: []
---

# §12 Tools per Phase — Financial Tracking Roadmap

> **Cell C-10 | systems-expert | mode: integrator**
>
> Spec + roadmap only — NOT implementation. Revenue-triggered build throughout per D15.
> Every claim carries F / ClaimScope / R triple.

---

## §12.0 Framing — Scope Boundary Against L5 §14

**L5 §14 owns product and service delivery tooling:** CRM-lite, `/project-bootstrap`, voice pipeline, KB skills, stage-gate evaluator, `/company-status`, landing pages, client-private KB scripts, YouTube-analyzer data pipeline, CRM upgrade, Matchmaker coordination layer, Secure Network Telegram infrastructure, educational delivery platform, USB-C install scripts, investor data-room structure, Token infrastructure (smart-contracts + custody + KYC/AML + EU MiCA filing), EU-sovereign compute, platform Matchmaker, YouTube SaaS product, certification program infrastructure, digital portrait mechanism, ISO 27001 workflow. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§14.0-§14.4]

**L7 §12 owns financial-tracking tooling specifically:** bank-statement ingestion and review, Stripe dashboard as revenue-intake instrument, `compute-ledger.yaml` as the financial-reporting layer for compute cost, cash-runway alert as risk-enforcement mechanism, accounting software (Lexware / DATEV / Sage — DACH standard), per-direction P&L tracking, investor reporting templates, holding-level consolidation of parent + roys, Kelly portfolio optimization across roy investments, token economy ledger (financial-reporting layer only, not infrastructure), multi-jurisdiction tax and transfer pricing.

The boundary is tight and deliberate. Token infrastructure (L5 §14.3 item 18) is smart-contract engineering and regulatory compliance; token economy ledger (L7 §12 Tool 11) is the financial-reporting layer that tracks issuance, compensation distributions, and reserve positions. No duplication.

**Central principle:** Revenue-triggered build per D15 + D18. No tool activates before its named trigger event. Every tool below is a spec at Phase-A; it becomes a build target only when the trigger fires. This is the same gate-sequencing discipline applied to product tooling in L5 §14 — here applied to the financial-tracking layer. D25 Company-as-Code discipline applies: every financial-tracking tool upgrade is a git commit with structured provenance; Notion is an optional view layer only (D17). [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25; src:decisions/JETIX-ARCHITECTURE-BRIEF.md#§3.1.12]

---

## §12.1 Phase-1 Financial Tools (G0 → G1, €0 → €50K, Q2 2026)

Phase-1 cash-flow tracking serves the §7 monthly model: six-month runway from €4 650 starting cash, burn €1 785-€2 360/мес (compute €285 + draw €1 500 mid-estimate), €2K halt-and-strategize trigger enforced manually. [src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§7-cashflow.md#§7.1-§7.2]

**Tool 1 — Manual bank-statement → CSV → Notion/spreadsheet (existing)**

- Current state: EXISTS. Ruslan reviews German bank statement monthly, enters line items into a personal spreadsheet. This is the only financial-tracking instrument today.
- Trigger for upgrade: ≥5 recurring revenue streams active simultaneously (Phase-2 condition). Phase-1 manual is sufficient.
- Build estimate: N/A (manual); upgrade estimate 0.5 cycles at Phase-2 trigger.
- Dependencies: GmbH bank account post-$20-30K trigger (D15). [src:decisions/JETIX-PLAN.md#§2.1]
- Revenue justification: Phase-1 cash-flow enforcement; the spreadsheet is the only instrument tracking cash position against the €2K halt-and-strategize floor. Without it, R-1 risk (Phase-1 €50K miss) has no early warning.

Claim §12.1-C1: manual bank-statement → spreadsheet is the minimum viable financial-tracking instrument through G0→G1.
- F: F4 (operational convention; DACH solo-founder with single revenue stream; Lexware-grade accounting not warranted until GmbH is operational)
- ClaimScope: Phase-1 solo; single DE bank account; ≤4 active revenue streams
- R: refuted if multiple currencies or cross-entity flows emerge before G1 — that would require Tool 5 (accounting software) early

**Tool 2 — Stripe dashboard (revenue-triggered activation)**

- Current state: NOT activated. Awaits GmbH registration + $20-30K trigger per JETIX-PLAN §2.1. [src:decisions/JETIX-PLAN.md#§2.1 GmbH]
- Trigger for build: GmbH registered AND first productized contract ready for card-based invoicing. Practical estimate: M3-M4 of Phase-1 timeline.
- Build estimate: 0.5 cycles (Stripe account setup + invoice template + webhook connection to compute-ledger update cadence).
- Dependencies: GmbH entity (legal requirement for EU merchant account); JETIX-ARCHITECTURE-BRIEF §3.1.5 payment layer. [src:decisions/JETIX-ARCHITECTURE-BRIEF.md#§3.1.5]
- Revenue justification: productized contract payment infrastructure for §3.1 AI Consulting and §3.2 Продюсерский центр retainer invoicing. Stripe's native dashboard provides transaction-level revenue visibility that the manual spreadsheet cannot.

Claim §12.1-C2: Stripe dashboard activation is Phase-1 G0→G1 sequential — not parallel to GmbH filing; GmbH is the prerequisite.
- F: F4 (operational; EU Stripe merchant account requires registered legal entity)
- ClaimScope: DE-incorporated GmbH; EU payment flows only in Phase-1
- R: refuted if Ruslan uses an alternative invoicing mechanism (e.g., freelancer invoice without GmbH) — then Stripe deferred to G1; refutation receipt: first invoice issued

**Tool 3 — `compute-ledger.yaml` (per P7.2 / KM-Mat)**

- Current state: EXISTS as spec per KM-Mat Part E; materialization pending. The §7 cashflow model uses its numbers (Anthropic Max €150/мес mid-point; Groq voice ≤€20/мес) but the YAML schema itself is not yet a committed file with weekly update discipline. [src:swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§7-cashflow.md#§7.2.1]
- Trigger for build: already met — ≥3 active swarm cycles concurrent (current state). The trigger fired; materialization is the outstanding action.
- Build estimate: 1 cycle. Schema: provider | line-item | cost-per-month | method | notes. Scope carve-outs per shared-protocols §9: Anthropic Max-sub (turn-count tracked, not API key); Groq voice-only exception (Whisper transcription). Weekly `/company-status` integration appends current compute position.
- Dependencies: shared-protocols §9 carve-outs (already defined); `/company-status` skill (EXISTS). [src:CLAUDE.md#KM-MVP-quick-ops]
- Revenue justification: compute cost is the dominant variable burn item in §7 (€285/мес mid-point out of €1 785-€2 360 total Phase-1 burn). Without the ledger, the §7 monthly model's compute line is estimated, not tracked. D25 requires every financial artefact to have git-commit provenance. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]

Claim §12.1-C3: `compute-ledger.yaml` materialization is the highest-priority Phase-1 financial-tracking build item because its trigger is already met and its absence creates a gap in §7 model enforcement.
- F: F4 (operational; trigger condition met as documented)
- ClaimScope: Phase-1 solo; Max-sub only; Groq voice-only exception
- R: refuted if actual compute spend tracked via bank-statement manually at sufficient granularity — manual tracking is a weaker but valid substitute until ledger is built

**Tool 4 — Cash runway alert (manual Phase-1)**

- Current state: MISSING. No automated or semi-automated alert exists. Ruslan manually reviews cash position. The §11 risk register names R-1 (Phase-1 €50K miss) as the dominant risk; the €2K halt-and-strategize threshold is the trigger. [src:swarm/wiki/tasks/T-layer-7-business-trajectory-deep-dive-2026-04-25/intake.md#§4 D9]
- Trigger for build: immediate — R-1 is a Phase-1 risk active now.
- Build estimate: 0.25 cycles. A minimal weekly check: cash position (from Tool 1 spreadsheet) vs €2K floor + 30-day receivables estimate. Output: a single line in the weekly `/company-status` output or a manually run `cash_position_check.sh` that computes `(current_balance + expected_receivables_30d) ≥ €2K`. If the predicate fails, halt discretionary spend and escalate to Ruslan HITL.
- Dependencies: Tool 1 (bank-statement CSV as input); Tool 3 (compute-ledger for burn-rate denominator); D25 requires the check script be committed to git with provenance. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]
- Revenue justification: R-1 trigger enforcement. The halt-and-strategize threshold exists in the risk register; without the alert, it is unenforced except by periodic Ruslan manual attention, which is insufficient under execution-mode pressure.

Claim §12.1-C4: the €2K halt-and-strategize threshold requires an explicit, committed check mechanism — not reliance on Ruslan's memory.
- F: F4 (operational; derived from R-1 risk register entry; behavioral finance literature consistently shows manual discipline erodes under stress)
- ClaimScope: Phase-1 solo; single DE account; ≤€50K gate
- R: refuted if Ruslan confirms weekly manual review discipline is sufficient and documented via git-committed weekly cash note — that satisfies D25 and may substitute for a script

---

## §12.2 Phase-2 Financial Tools (G1 → G2 → G3, €50K → €1M)

Phase-2 introduces multiple revenue streams, first hires, GmbH annual reporting obligation, and investor-relationship groundwork. The manual-spreadsheet model breaks down at ≥5 concurrent revenue streams; proper accounting software and per-direction tracking become necessary.

**Tool 5 — Proper accounting software (DACH standard)**

- Current state: MISSING. Phase-1 uses spreadsheet.
- Trigger for build (whichever fires first): (a) GmbH annual return filing obligation (DE law: GmbH files annual Jahresabschluss; first filing triggers at end of first fiscal year); (b) first hire payroll (payroll requires Lohnbuchhaltung-grade tooling); (c) €200K cumulative revenue (D15 gate). In DACH practice, criteria (a) and (c) fire near-simultaneously.
- Build estimate: 1-2 cycles integration + 1-2 weeks onboarding with DACH tax accountant.
- Three options (decision at trigger, per D15 discipline — not committed now):
  - (a) Lexware — DACH-native, Mittelstand-standard, ~€30-€50/мес; handles GmbH annual return, VAT, payroll Lohnbuchhaltung. Preferred for Phase-2 on cost-efficiency + DACH credibility grounds.
  - (b) DATEV — DACH-native, larger-enterprise standard, ~€80-€120/мес + onboarding consultant. DATEV is the accountant-facing platform used by most DE Steuerberater; switching from Lexware to DATEV at G3 is the expected trajectory.
  - (c) Sage — international, wider feature set, ~€50-€100/мес; less DACH-native; considered if international revenue becomes primary before G3.
- Dependencies: GmbH entity operational; DACH tax accountant engaged; Stripe transaction history (Tool 2) as import source.
- Revenue justification: all Phase-2 revenue streams (consulting, producer, USB-C, Matchmaker, educational) require audit-grade accounting for GmbH annual return and, eventually, investor due-diligence.

Claim §12.2-C1: Phase-2 accounting software trigger = GmbH annual return OR first hire payroll OR €200K revenue, whichever fires first.
- F: F3 (substantive; DACH GmbH legal requirements + payroll law Lohnsteuer-obligations)
- ClaimScope: DE-incorporated GmbH; Phase-2 transition; DACH-primary revenue
- R: refuted if Ruslan opts for bookkeeper-only without software (delegates full accounting to human Steuerberater using their own tooling) — feasible but higher recurring cost and lower owner visibility

**Tool 6 — Per-direction P&L tracking**

- Current state: MISSING. Phase-1 revenue is mixed (hourly + contracts) but not allocated per direction.
- Trigger for build: ≥3 directions generating revenue simultaneously. This is a G2 condition: consulting + producer + at least one of USB-C / Matchmaker / educational producing invoiced revenue.
- Build estimate: 0.5 cycles. Implementation: one structured wiki file per direction per month (git-committed, D25) with revenue, direct COGS, and contribution. Quarterly rollup produces cross-direction comparison. This is a financial-reporting discipline, not a software feature.
- Dependencies: Tool 5 (accounting software providing journal-level data for direction allocation); wiki structure per direction (EXISTS via `/project-bootstrap` templates). [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§13.2]
- Revenue justification: §6 revenue stream concentration thresholds — if one direction exceeds a safe share, the per-direction P&L is the instrument that surfaces it. Direction ROI comparison informs D15 capital-allocation decisions.

Claim §12.2-C2: per-direction P&L tracking is a wiki-native financial discipline, not a SaaS tool — consistent with D17 filesystem-SoT and D25 Company-as-Code.
- F: F4 (operational; wiki-native tracking is validated by D25 and D17; compatible with D28 query-driven KB)
- ClaimScope: Phase-2 solo-to-small-team; ≤7 active directions
- R: refuted if direction count exceeds 7 active simultaneously — at that point, a proper cost-accounting module within Tool 5 is more efficient than manual wiki files

**Tool 7 — Investor reporting templates (conditional — if Phase-2 round activated)**

- Current state: MISSING. L5 §14.2 item 17 owns investor data-room structure (folder layout, YAML fields, git-commit discipline). L7 §12 Tool 7 owns the financial-reporting content populating those templates: P&L by direction, cash position, unit-economics summary, revenue-mix table. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§14.2-item-17]
- Trigger for build: first strategic-angel or family-office exploratory conversation post-€200K. Per JETIX-PLAN §3.8: no cold equity pitching; relationship-built investors only. [src:decisions/JETIX-PLAN.md#§3.8]
- Build estimate: 1 cycle. Template components: monthly P&L summary (1 page), cash-runway table (from Tool 4 enhanced), revenue-mix chart (from Tool 6), unit-economics snapshot (from §3 unit-econ model), trailing-12-month trend. All git-committed per D25.
- Dependencies: Tool 5 (accounting data), Tool 6 (per-direction P&L), §3 unit-econ model; investor-relations wiki directory (L5 §14.2 item 17 scope for folder structure).
- Revenue justification: relationship-maintenance for Phase-2+ strategic investors; 8 quarterly letters sent before a raise reduces due-diligence friction materially (per L5 §3.7 investor programs framing). [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.7-investor-programs]

**Tool 8 — Compute-ledger expanded multi-provider**

- Current state: PARTIAL. Phase-1 ledger (Tool 3) covers Anthropic Max-sub + Groq voice-only.
- Trigger for build: first multi-provider deployment — either Path-A managed hosting (Jetix-side compute) or Phase-2 offline-LLM decision (Mistral or Llama on client hardware). [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§3.3-USB-C]
- Build estimate: 0.5 cycles (schema extension — add provider column + per-provider cost-ratio tracking).
- Dependencies: Tool 3 (base schema); L5 §3.3 Path-A/B/C final provider decision (currently Path-B default per Q-01 ack).
- Revenue justification: COGS tracking per §3 unit-econ for USB-C Path-A engagements; multi-provider cost-ratio monitoring enables margin protection as provider mix changes.

---

## §12.3 Phase-3+ Financial Tools (G3 → G4 → G5, €1M+)

Phase-3+ introduces holding structure, replicated roys, international revenue, and potentially the token economy. Financial complexity crosses the threshold where each tool below requires dedicated professional advice and engineering investment.

**Tool 9 — Holding-level consolidation (parent + roys)**

- Current state: MISSING. Holding structure is a Phase-3 gate per §13 Evolution. The first replicated roy activates at $10M+ revenue per D21. [src:decisions/JETIX-VISION.md#D21]
- Trigger for build: first roy entity operational with independent P&L (Phase-3, $10M+ revenue).
- Build estimate: 3-5 cycles engineering + tax-lawyer consultation (DE holding structure for GmbH parent + subsidiary GmbHs is a standard DACH structure but non-trivial to set up for inter-entity financial reporting).
- Components: parent Jetix-Corp consolidated P&L + per-roy entity P&L + inter-entity transfer pricing documentation + minority-interest accounting (if external investors enter roys) + tax-optimization pass (DE Organschaft or comparable EU structure).
- Dependencies: Tools 5-6 mature and producing audit-grade data; Foundation (Alliance Option C per L6 ack) legal entity operational; roy-entity legal setup per D21 methodology-export design. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§5 Option C]
- Revenue justification: holding-level financial reporting is a legal compliance obligation once multiple GmbH entities operate; investor reporting Phase-3+ requires consolidated financials, not per-entity statements.

Claim §12.3-C1: holding-level consolidation is not an optional Phase-3 tool — it is legally mandated once multiple GmbH entities exist under a common parent.
- F: F3 (substantive; DE Konzernabschluss obligation under HGB §290 triggers at defined size thresholds; even below those thresholds, investor reporting typically requires consolidated view)
- ClaimScope: DE-domiciled holding + GmbH subsidiaries; Phase-3+; EU jurisdiction primary
- R: refuted if Jetix adopts a non-DE holding structure (e.g., Dutch B.V. or Estonian e-Residency model) — in that case, local law governs consolidation obligation

**Tool 10 — Kelly portfolio optimization across roy investments**

- Current state: MISSING. No multi-roy portfolio exists.
- Trigger for build: ≥2 active roys with independent P&L and independently measurable return-on-investment.
- Build estimate: 2-3 cycles (Kelly-criterion capital-allocation model + dashboard tracking return per roy + quarterly rebalancing memo discipline).
- Dependencies: Tool 9 (consolidated P&L data for each roy); Ruslan's explicit capital-allocation philosophy matured through Phase-2 (D11 investment-fund philosophy). [src:raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md#D11]
- Revenue justification: §6 revenue diversification — Kelly criterion optimizes position size per investment (here: capital deployed per roy) based on edge and variance. Prevents capital concentration in a single underperforming roy while avoiding over-diversification that dilutes high-edge opportunities.

**Tool 11 — Token economy ledger (conditional — if D23 Option B Phase-2+ launched)**

- Current state: MISSING. D23 Option B pending Ruslan's explicit ack + $100K self-earned trigger. Per L5 §3.8 retirement clause: if consulting/educational/USB-C fund growth without specialist-friction, D23 may be deprecated. [src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§13.2 row 8]
- Trigger for build: Ruslan explicit D23 Option B activation + $100K self-earned + lawyer confirmation of EU MiCA compliance path.
- Build estimate: 5-10 cycles engineering + legal timelines. Note: L5 §14.3 item 18 owns the Token infrastructure (smart-contract layer, custody, KYC/AML, MiCA filing, Howey analysis). L7 §12 Tool 11 owns the financial-tracking layer of that infrastructure: issuance register (tokens issued per event), compensation distribution ledger (tokens awarded to specialists), reserve position (tokens held in treasury vs circulating), fair-value estimate for financial-reporting purposes, and tax treatment documentation.
- Dependencies: L5 §14.3 item 18 infrastructure must exist before the ledger layer is meaningful; Foundation entity operational; legal counsel engaged.
- Revenue justification: §3.8 token revenue line conditional on D23 activation; specialist compensation via tokens requires a ledger to track distributions for tax reporting and audit purposes.

Anti-duplication note: L5 §14.3 item 18 = smart-contract + custody + KYC/AML compliance filing. L7 §12 Tool 11 = financial-reporting on token issuance + distribution + reserve. No overlap; the infrastructure layer produces the economic events; the ledger layer records them for financial-reporting.

**Tool 12 — Multi-jurisdiction tax + transfer pricing**

- Current state: MISSING. Phase-1/2 is single-jurisdiction DE primary.
- Trigger for build: first roy entity in a non-DACH jurisdiction (Phase-3+ international expansion per D10 and D26 team trajectory). [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]
- Build estimate: 5-8 cycles + tax-lawyer DACH + EU + international engagement. Components: EU VAT compliance infrastructure (OSS scheme or per-jurisdiction registration), transfer pricing documentation (mandatory under OECD Guidelines for cross-border inter-entity transactions), subsidiary tax structure optimization, withholding-tax tracking for royalty payments from roys to parent.
- Dependencies: Tool 9 (holding consolidation as the organizational structure being taxed); international legal counsel engaged for each jurisdiction entered; Tool 5 upgraded to a multi-jurisdiction accounting platform (DATEV or Sage international tier).
- Revenue justification: Phase-3+ international operations are legally obligated to comply with local tax law; non-compliance creates liability that directly threatens the revenue base. Legal-compliance-by-architecture (D25 analog applied to tax) means the tooling is built before the obligation becomes punitive, not in reaction to an audit.

---

## §12.4 Cross-Reference to L5 §14 — Anti-Duplication Map

This section is the formal boundary declaration. Any reader uncertain whether a given tool belongs to L5 §14 or L7 §12 should consult this map.

| L5 §14 owns (product/service delivery) | L7 §12 owns (financial tracking) |
|---|---|
| CRM-lite (pipeline tracking) | Bank-statement ingestion + monthly reconciliation |
| `/project-bootstrap` + stage-gates | Stripe dashboard as revenue-intake financial instrument |
| Voice pipeline (transcription) | `compute-ledger.yaml` (financial-reporting of compute cost) |
| Skills `/ingest` `/ask` `/lint` | Cash-runway alert (€2K halt-and-strategize enforcement) |
| `/company-status` (operational snapshot) | Accounting software: Lexware / DATEV / Sage |
| Landing pages | Per-direction P&L (contribution tracking per revenue stream) |
| Client-private KB bootstrap | Investor reporting templates (financial content only) |
| YouTube-analyzer data pipeline | Holding-level consolidation (parent + roys) |
| CRM upgrade | Kelly portfolio optimization |
| Matchmaker coordination layer | Token economy ledger (reporting layer — not infrastructure) |
| Secure Network Telegram infrastructure | Multi-jurisdiction tax + transfer pricing |
| Educational delivery platform | — |
| Client-private AI install scripts (Path A/B/C) | — |
| Investor data-room structure (folder + YAML) | Investor reporting templates (financial data populating that structure) |
| Token infrastructure (smart-contract + custody + KYC + MiCA) | Token economy ledger (issuance register + compensation + reserve + fair value) |
| EU-sovereign compute (data-center) | — |
| Platform Matchmaker scale MVP | — |
| YouTube-analyzer SaaS product | — |
| Certification + licensing program | — |
| Digital portrait mechanism at scale | — |
| ISO 27001 + BSI C5 certification workflow | — |

[src:decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md#§14.0-§14.4]

---

## §12.5 Anti-Scope + Phase Sequencing Logic

**What this section is NOT:**

- NOT implementation code. Every tool above is described as a spec + trigger + build estimate. The code itself is a Phase-4 engineering-expert deliverable after the trigger fires.
- NOT a Notion architecture. D17 filesystem-SoT: all financial artefacts are git-committed files. Notion is an optional view layer only. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D17 via D25]
- NOT Phase-3+ tools built in Phase-1. Revenue-triggered build per D15 is enforced: implementing Tool 9 (holding consolidation) during Phase-1 is premature abstraction — equivalent to the D28 anti-pattern of accumulating knowledge without an active query.
- NOT capital allocation decisions. Tool 10 (Kelly portfolio) requires Ruslan's explicit D11 capital-allocation philosophy to be operationalized by investor-expert — this section specs the tool, not the allocation.

**Phase sequencing rationale (systems lens):**

Phase-1 tools (1-4) form a minimal closed-loop financial-control system: bank-statement (input) → spreadsheet + ledger (tracking) → Stripe (payment intake) → cash-runway alert (control signal). This is a Meadows L7 information-flow structure: the right information (cash position vs €2K floor) reaching the right actor (Ruslan) at the right time (weekly). Missing the alert (Tool 4) breaks the loop; the system operates open-loop on cash until a crisis. [ref: Meadows, Thinking in Systems — book-as-frame; Senge L7 information tightening]

Phase-2 tools (5-8) extend the loop to multi-stream complexity: accounting software (Tool 5) replaces manual spreadsheet as the Journal-of-Record; per-direction P&L (Tool 6) adds observability at the sub-system level; investor templates (Tool 7) add an external-reporting output; multi-provider ledger (Tool 8) extends compute-cost tracking as the provider mix grows. The system transitions from a single balancing loop (cash in vs cash out) to a multi-loop structure with both reinforcing flows (revenue × direction → feedback into capital allocation) and balancing constraints (per-direction concentration limits).

Phase-3+ tools (9-12) address holding-level systemic complexity. Tool 9 (holding consolidation) is a Beer VSM Level-3 function: it provides the audit and optimization layer across multiple Level-1 operating entities (the roys). Without this layer, the holding parent has no visibility into sub-system performance — a Ashby requisite-variety violation (the controller's variety is lower than the system being controlled). [ref: Beer, Brain of the Firm — book-as-frame; Ashby, Introduction to Cybernetics — book-as-frame]

**D25 Company-as-Code compliance:** Every financial-tracking tool upgrade is a git commit. Commit format: `[financials] add <tool-slug>: <one-line description> (trigger: <trigger-event>)`. This ensures that the financial-tracking evolution is reconstructable from git history — consistent with the D25 principle that company state is reconstructable at any moment. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]

---

## §12.6 Cross-Section Reconciliation

This section maps §12 tools to their dependencies in other canonical sections:

| Tool | Feeds | Depends on |
|---|---|---|
| Tool 3 (compute-ledger) | §7 cash flow §7.2.1 compute-cost line item | §7 §7.2.1 numbers (monthly burn baseline) |
| Tool 4 (cash-runway alert) | §11 risk register R-1 enforcement | Tool 1 (bank-statement); Tool 3 (burn rate) |
| Tool 6 (per-direction P&L) | §6 revenue-stream concentration monitoring | Tool 5 (accounting software for journal entries) |
| Tool 7 (investor reporting) | §9 investor relations roadmap (financial content) | Tool 5, Tool 6; L5 §14.2 item 17 (structure) |
| Tool 9 (holding consolidation) | §13 evolution (Phase-3+ gate trajectory) | D21 roy-entity legal setup |
| Tool 10 (Kelly portfolio) | §13 Phase-3+ capital-allocation discipline | Tool 9; D11 matured |
| Tool 12 (multi-jurisdiction tax) | §11 risk register (international compliance risk) | Tool 9; D10 geographic expansion |

The feedback structure across sections: §7 cash-flow model is the Phase-1 enforcement instrument; Tools 3 and 4 are the measurement and control mechanisms that make §7 operational rather than theoretical. At Phase-2, Tools 5 and 6 replace the manual §7 model with an accounting-software-backed equivalent. At Phase-3+, Tools 9 and 12 extend financial visibility to the holding level that §13's evolution gate table requires.

---

## §X Cell C-10 Self-Improvement Notes

**Pattern 1 — Revenue-gated sequencing applies uniformly across tooling layers.** The same D15 gate logic that governs product tooling (L5 §14) governs financial-tracking tooling (L7 §12). The sequencing constraint is not tool-specific — it is a swarm-wide discipline. Future cells covering any tooling layer can apply the same 5-item format (current state / trigger / estimate / dependencies / justification) without re-deriving the sequencing rationale.

**Pattern 2 — D25 Company-as-Code extends to financial artefacts.** Financial-tracking tools are not exempt from the git-commit-with-provenance discipline. Every ledger update, every accounting-software onboarding, every investor template version is a commit. This is a systems insight: the financial-tracking layer is part of the same information system as the knowledge base and the product delivery tooling — not a separate domain operating outside git.

**Pattern 3 — L5 vs L7 tool boundary is infrastructure vs financial-reporting.** The clean heuristic for distinguishing L5 §14 scope from L7 §12 scope: if the tool produces a product or service deliverable (even an internal one), it belongs to L5. If the tool records, tracks, or reports on financial flows generated by those deliverables, it belongs to L7. The token example is the clearest case: the smart-contract that issues a token (infrastructure, L5) vs the ledger that records the issuance and its fair value for financial reporting (financial tracking, L7). This heuristic is generalizable to future scope disputes in deep-dive cycles.
