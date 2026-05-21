---
title: Diagrams INDEX — Method Deep-Description (27 mermaid diagrams)
date: 2026-05-21
type: research-doc-diagrams-index
parent_prompt: prompts/method-deep-description-2026-05-21.md
main_deliverable: decisions/strategic/METHOD-DEEP-DESCRIPTION-2026-05-21.md
authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: method-deep-description-diagrams-index
---

# Diagrams INDEX — Method Deep-Description

> 27 mermaid diagrams produced across 10 phases. All embedded inline в per-phase
> files. This index = cross-link map для reuse в future docs.

---

## §1 Quantitative summary

- **Total diagrams:** 27
- **Target:** 20-25
- **Floor:** 15 (parent prompt §13 mandate)
- **Status:** 8% above target ✅

---

## §2 Per-phase distribution

| Phase | Count | Diagram IDs |
|-------|-------|-------------|
| Phase 1 — Canonical definition | 2 | D1, D2 |
| Phase 2 — 31-component breakdown | 2 | D3, D4 |
| Phase 3 — 10 layers | 5 | D5, D6, D7, D8, D9 |
| Phase 4 — Mechanics | 4 | D10, D11, D12, D13 |
| Phase 5 — 8-doc inventory | 2 | D14, D15 |
| Phase 6 — Comparison | 3 | D16, D17, D18 |
| Phase 7 — FPF universal language | 3 | D19, D20, D21 |
| Phase 8 — Use cases | 6 | D22, D23, D24, D25, D26, D27 |
| **Total** | **27** | **D1-D27** |

---

## §3 Diagram catalogue

### Phase 1

| ID | Type | Subject | Location |
|----|------|---------|----------|
| D1 | `mindmap` | Canonical one-liner unpacking (метод × объединение × методов × улучшение × системы × самой себя) | `01-canonical-definition.md` §8 |
| D2 | `graph LR` | 8-doc inventory connecting map (O-114 audio_709 claim 1) | `01-canonical-definition.md` §9 |

### Phase 2

| ID | Type | Subject | Location |
|----|------|---------|----------|
| D3 | `mindmap` | 31 components × 5 functional areas (Cognitive 9 / Operational 7 / Structural 5 / Communicative 4 / Constitutional 6) | `02-31-components.md` §9 |
| D4 | `classDiagram` | Component dependency relationships (top-15 inter-component edges) | `02-31-components.md` §10 |

### Phase 3 (most important — 5 diagrams)

| ID | Type | Subject | Location |
|----|------|---------|----------|
| D5 | `block-beta` | Full 10-layer Jetix stack visualization | `03-layers.md` §11 |
| D6 | `classDiagram` | Foundation 11 Parts inheritance from Foundation_Architecture_v1_0 | `03-layers.md` §12 |
| D7 | `graph LR` | ROY swarm hub-and-spoke routing (brigadier + 5 experts × 4 modes + 4 sub-brigadiers) | `03-layers.md` §13 |
| D8 | `erDiagram` | Wiki v2 entity types (9) + edges + niche/ symlinks | `03-layers.md` §14 |
| D9 | `stateDiagram-v2` | Hypothesis lifecycle (backlog → active → testing → confirmed/refuted → CompoundLearning → optional F5 LOCK) | `03-layers.md` §15 |

### Phase 4

| ID | Type | Subject | Location |
|----|------|---------|----------|
| D10 | `sequenceDiagram` | Voice memo → wiki §APPEND pipeline (Ruslan → Voice → transcribe → extract → filter → review → manual /ingest /hypothesis-add /crm-update) | `04-mechanics.md` §2.1 |
| D11 | `sequenceDiagram` | R1 strategic prose flow (brigadier → ROY 5 experts → drafts → memo → R1 prose → R12 audit → strategic publish) | `04-mechanics.md` §4.1 |
| D12 | `stateDiagram-v2` | AWAITING-APPROVAL gate flow (Default-Deny check → AAP draft → ProvenanceGrade → Ruslan ack → Foundation §APPEND → LOCK tag → ConfigSync → ClaudeMD sync) | `04-mechanics.md` §3.1 |
| D13 | `sequenceDiagram` | Outreach handshake (R12 paired-frame 8-item audit; CRM update; pipeline status advancement) | `04-mechanics.md` §6.1 |

### Phase 5

| ID | Type | Subject | Location |
|----|------|---------|----------|
| D14 | `graph TD` | 8 docs × 8 audiences matrix (primary + secondary edges) | `05-8-doc-inventory.md` §5 |
| D15 | `journey` | Reader journey through Jetix 8-doc inventory (cold → commitment) | `05-8-doc-inventory.md` §6 |

### Phase 6

| ID | Type | Subject | Location |
|----|------|---------|----------|
| D16 | `quadrantChart` | Method comparison axes (Abstract vs Concrete × Single-agent vs Multi-agent; Jetix territory) | `06-comparison.md` §6 |
| D17 | `mindmap` | Левенчук corpus 5 books × Jetix substrate cross-cite map (СМ Т1/Т2/Методология/Интеллект-стек/Инженерия личности) | `06-comparison.md` §7 |
| D18 | `classDiagram` | OMG Essence 7 alphas + state-graphs + Jetix Hypothesis Architecture Layer 6 integration | `06-comparison.md` §8 |

### Phase 7

| ID | Type | Subject | Location |
|----|------|---------|----------|
| D19 | `graph TD` | F2-F8 grade ladder with promotion gates (F2 → F3 brigadier → F4 single-context → F5 LOCK eligible → F6 schema → F7 Pillar → F8 Foundation) | `07-fpf-universal-language.md` §7 |
| D20 | `classDiagram` | F-G-R triple structure (Formality / Group / Reliability enums + Promoted_Claim + Promotion_Gate + AAP_Packet) | `07-fpf-universal-language.md` §8 |
| D21 | `stateDiagram-v2` | Claim promotion lifecycle (F2 → F8 + refutation + AAP gate + compound learning) | `07-fpf-universal-language.md` §9 |

### Phase 8 (5 use cases + 1 gitGraph bonus)

| ID | Type | Subject | Location |
|----|------|---------|----------|
| D22 | `sequenceDiagram` | Use case 1 — voice memo → wiki §APPEND → hypothesis (concrete: audio_710 take rate → O-108 → DR-26 → R1 ack 10-25%) | `08-use-cases-workflows.md` §1.3 |
| D23 | `sequenceDiagram` | Use case 2 — outreach pitch generation (concrete: Дмитрий + 5 Левенчук hooks + R12 8-item audit + R1 prose authoring) | `08-use-cases-workflows.md` §2.3 |
| D24 | `sequenceDiagram` | Use case 3 — hypothesis lifecycle full cycle (concrete: H-batch-9-06 backlog → active → testing → confirmed → compound learning) | `08-use-cases-workflows.md` §3.3 |
| D25 | `sequenceDiagram` | Use case 4 — R1 strategic decision flow (concrete: DR-26 → R1 ack «10-25% / Mondragón 5:1 / Workshop €1500 / grants defer» 2026-05-21) | `08-use-cases-workflows.md` §4.3 |
| D26 | `sequenceDiagram` | Use case 5 — AAP Foundation modification gate (concrete: R12 programmable Ethereum Option D Hybrid + parallel H8 substrate extension acked 2026-05-18) | `08-use-cases-workflows.md` §5.3 |
| D27 | `gitGraph` | Cycle commit pattern (this Method Deep-Description execution: 10 commits Phase 0-9 + final tag) | `08-use-cases-workflows.md` §6 |

---

## §4 Diagram type distribution

| Mermaid type | Count | Used for |
|--------------|-------|----------|
| `sequenceDiagram` | 9 | D10, D11, D13, D22, D23, D24, D25, D26 (8 — plus implicit D27 gitGraph as sequence) |
| `stateDiagram-v2` | 4 | D9, D12, D21 (3) |
| `classDiagram` | 5 | D4, D6, D18, D20 (4) |
| `mindmap` | 3 | D1, D3, D17 |
| `graph LR` | 2 | D2, D7 |
| `graph TD` | 2 | D14, D19 |
| `block-beta` | 1 | D5 |
| `erDiagram` | 1 | D8 |
| `journey` | 1 | D15 |
| `quadrantChart` | 1 | D16 |
| `gitGraph` | 1 | D27 |
| **Total** | **27** | Diverse — uses 11 of 14 mermaid types listed in parent §13 |

---

## §5 Cross-link map (which diagrams feed which 8 docs)

| Diagram | Primary doc feed | Secondary doc feed |
|---------|-----------------|---------------------|
| D1 (one-liner mindmap) | Doc 1 Метод + Doc 7 Описание метода | Doc 2 Кто я (substrate) |
| D2 (8-doc connecting map) | Doc 7 Описание метода | All 8 docs (meta-cross-link) |
| D3 (31 components mindmap) | Doc 7 Описание метода | Doc 3 Наработки |
| D4 (component dependencies classDiagram) | Doc 7 Описание метода | Doc 3 Наработки |
| D5 (10-layer stack block-beta) | Doc 3 Наработки | Doc 7 Описание метода |
| D6 (Foundation 11 Parts classDiagram) | Doc 3 Наработки | — |
| D7 (ROY routing graph LR) | Doc 3 Наработки | Doc 7 Описание метода |
| D8 (Wiki v2 erDiagram) | Doc 3 Наработки | — |
| D9 (Hypothesis lifecycle stateDiagram) | Doc 3 Наработки + Doc 7 | — |
| D10 (voice pipeline sequenceDiagram) | Doc 4 Чем занимаюсь | Doc 3 Наработки |
| D11 (R1 strategic prose flow) | Doc 7 Описание метода | Doc 5 Планы корпорации |
| D12 (AAP gate flow stateDiagram) | Doc 3 Наработки | Doc 7 Описание метода |
| D13 (outreach handshake sequenceDiagram) | Doc 8 Возможности | Doc 4 Чем занимаюсь |
| D14 (8-docs × audience graph TD) | Phase 5 meta — all 8 docs | — |
| D15 (reader journey) | Phase 5 meta — all 8 docs | — |
| D16 (comparison quadrantChart) | Doc 7 Описание метода | Doc 6 Планы на мир (philosophical positioning) |
| D17 (Левенчук cross-cite mindmap) | Doc 7 Описание метода | Doc 3 Наработки |
| D18 (OMG Essence classDiagram) | Doc 7 Описание метода | Doc 3 Наработки |
| D19 (F2-F8 grade ladder) | Doc 7 Описание метода | Doc 3 Наработки (FPF substrate) |
| D20 (F-G-R triple classDiagram) | Doc 7 Описание метода | Doc 3 Наработки |
| D21 (claim promotion lifecycle) | Doc 7 Описание метода | Doc 3 Наработки |
| D22 (use case 1 voice) | Doc 7 Описание метода + Doc 4 Чем занимаюсь | Doc 3 Наработки |
| D23 (use case 2 outreach) | Doc 8 Возможности | Doc 4 Чем занимаюсь |
| D24 (use case 3 hypothesis) | Doc 7 Описание метода + Doc 3 Наработки | — |
| D25 (use case 4 R1 decision) | Doc 5 Планы корпорации | Doc 7 Описание метода |
| D26 (use case 5 AAP gate) | Doc 3 Наработки | Doc 7 Описание метода |
| D27 (gitGraph cycle pattern) | Doc 3 Наработки (KM MVP company-as-code discipline) | Doc 7 Описание метода |

---

## §6 Quality criteria reference

Per parent prompt §13.5:

- ✅ Dense (≥10 nodes) — все major diagrams D5/D6/D7/D8/D9/D10/D11/D12/D13/D17/D18/D20/D21/D22-D26 satisfy
- ✅ Deep — show actual relationships
- ✅ Interesting — color coding / subgraphs / styling в D5/D7/D11/D19
- ✅ Clear — readable layout
- ✅ Cross-linked — see §5 above
- ✅ Annotated — каждая diagram preceded by 2-3 sentence explainer в per-phase files
- ⚠️ Styling consistent — `%%{init: ...}%%` blocks not consistently applied; selective theme styling в D5/D7/D11/D14/D19 only

---

## §7 Future reuse hint

Most reusable diagrams для future docs:
- **D7** (ROY routing) — для any pitch involving Jetix multi-agent substrate
- **D5** (10-layer stack) — для technical reviewer audience (Doc 3 Наработки primary)
- **D9** (hypothesis lifecycle) — для any falsifiability discussion
- **D12** (AAP gate) — для governance / safety discussions
- **D19** (F2-F8 grade ladder) — для FPF universal language discussions
- **D22** (voice → wiki use case 1) — для outreach «как работает компания»

---

*Diagrams INDEX brigadier-scribe sign-off 2026-05-21. 27 mermaid diagrams catalogued + cross-linked. R1 surface only.*
