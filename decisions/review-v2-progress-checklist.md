---
name: Review V2 Synthesis — Progress Checklist
created: 2026-04-19
status: in-progress (1/7 chunks complete)
adr: decisions/2026-04-19-architecture-v2-approval.md
source: raw/research/architecture-synthesis-v2-final.md
notion: https://www.notion.so/3472496333bf81d39978cc6e43c57b40
---

# Review V2 Synthesis — Progress Checklist

Живой чеклист прохождения 7 чанков review v2 synthesis.
Финальный ADR с утверждениями — в `decisions/2026-04-19-architecture-v2-approval.md`.

## Chunk 1 — High-level frame ✅ COMPLETE 2026-04-19

**4 framing questions:**
- [x] Q1 Reference/Operational split — ACCEPTED
- [x] Q2 L2 Cognitive as discipline — ACCEPTED + усиление (max Левенчук discipline)
- [x] Q3 Capital+Hours+Attention elevate в first-class — ACCEPTED
- [x] Q4 Portability honesty "roadmap goal v2.0+" — ACCEPTED

**7 core principles:**
- [x] P1 Company-as-Code — APPROVED as foundation
- [x] P2 Role ≠ Executor — APPROVED deep
- [x] P3 7 true alphas + past-participle — APPROVED max Левенчук
- [x] P4 Model D Nested Hierarchy — APPROVED
- [x] P5 L0 Executive Core — APPROVED с MODIFICATION:
  - [x] 5 atomic sub-roles — accepted, manifests пишем
  - [x] Agent rename strategist → strategy-support-analyst — accepted
  - [x] Bus-factor mitigation — accepted но deferred (делаем чуть потом)
  - [ ] ⚠️ **Trustee ≠ Anton — TBD** (identity to be determined later)
- [x] P6 DACH — PARTIAL (+ US + RU с unified funnel)
- [x] P7 Resource Accounting — APPROVED FINAL (3 итерации обсуждения):
  - [x] Tier 1 quantitative ledger: Capital + Compute + Deep Hours
  - [x] Tier 2 strategic: Attention Budget (quarterly)
  - [x] Phase 3 first-class: Ecosystem Resources (11 категорий detailed)
  - [x] Deep Hours definition (deep vs shallow) confirmed
  - [x] Compute tracking via `finance/compute-ledger.yaml` + executor binding fields
  - [x] Attention Budget via `decisions/quarterly/YYYY-QN-attention-theme.md`

**3 additional principles (Part 1.4):**
- [x] Место-слот, не содержание — implicit approved
- [x] Org chart в Git — implicit approved
- [x] ШСМ 5 примитивов ontologically-correct — implicit approved

**Open changes to propagate:**
- [ ] MC4 trustee change (Anton → TBD) — pass into Chunk 2
- [x] OT1 strategic-management resolved early (5 sub-roles hybrid)
- [ ] P6 DACH modification affects R10 (multi-currency) and OT2 (bilingual) — revisit downstream

---

## Chunk 2 — 6 Meta-conflicts resolved ✅ COMPLETE 2026-04-19 (6/6)

- [x] **MC1** Critic vs Mega-Corp — ACCEPT v2 (9 P1 additions, 5 P2 deferred, 3 P3 rejected; trustee TBD ≠ Anton)
- [x] **MC2** Simplifier vs Mega-Corp — ACCEPT v2 (11 folders: 8 baseline + 3 Mega-Corp P1)
- [x] **MC3** Левенчук vs Pragmatic — ACCEPT v2 + 1 OVERRIDE: Full 3-level mereological graph Phase 1 (не Lite + Phase 2). Member preserved. 13 Левенчук changes accepted.
- [x] **MC4** Critic vs Simplifier (bus-factor) — ACKNOWLEDGED, DEFERRED (v2 structure ok, Phase 1 execution не priority; trustee TBD ≠ Anton)
- [x] **MC5** Mega-Corp vs Simplifier (federation) — ACCEPT v2 (entities/jetix-gmbh/ stub 4h)
- [x] **MC6** Левенчук past-participle — ACCEPT v2 (strict enforce, 52% rename)

---

## Chunk 3 — Accepted 38 / Rejected 12 [IN PROGRESS — Step 1 almost done]

### Step 1 — Not-yet-discussed accepted items (10 items)
- [x] 1. #25 Tools 14 → 5 + Healthchecks.io
- [x] 2. #27 Rollout 14-day → 7+7 split
- [x] 3. #26 Manual eval + Langfuse cloud
- [x] 4. #23 Single event log Phase 1
- [x] 5. #19 Memory 5 → 3 layers
- [x] **6. Wiki + Portfolio Directions — MAJOR DECISION LOCKED:**
  - Physical separation Life-OS ≠ Jetix (Вариант A) с Day 1
  - Portfolio-of-Directions model (Hybrid 1+4): folder-per-direction + Direction как 8-й alpha + wiki cross-refs
  - **7 true alphas → 8 true alphas** (Direction added)
  - Edges 9 → 6 (3 baseline + 3 portfolio-specific: belongs-to-direction / applies-to-direction / sames-as-crm)
  - Wiki Skills 5 → 2 accepted
- [x] **7. Career ladder J0-JX ref + 3 operational** (J-Auto/J-Approve/J-Strategic + 5-line decision_rights + Direction authority mapping)
- [x] **8. Pre-commit hooks — Вариант B** (3 v2 hooks + 4-й past-participle check)
- [x] **9. Cost model section — Вариант B** (+ per-direction compute breakdown)
- [x] **10. Constitution §11 — Вариант A** (Day 1 с TBD trustee placeholder)

**Step 1 COMPLETE — 10/10 items judged.**

### Step 2 — R10 multi-currency REVISIT ✅ RESOLVED 2026-04-19
- [x] Decision: payment-processor pattern (Stripe/Wise handles conversion externally)
- [x] Minimum scaffolding: `finance/currencies.yaml` placeholder (1h)
- [x] Tax/legal-entity: deferred, место зарезервировано в системе

### Step 3 — Confirm остальные rejections ✅ RESOLVED 2026-04-19
- [x] R11 IPO readiness placeholder — REJECT confirmed (Variant A)
- [x] R12 FPF-Steward — **OVERRIDE Variant B** (add sub-role Phase 1, Левенчук на максимум)
- [x] R1-R9 — all confirmed implicit via Chunks 1-2

### Step 4 — Scan 38 accepted для flags ✅ NO FLAGS
- [x] All 38 items integrated через Chunks 1-2 + Chunk 3 Items 1-10

---

## ✅ Chunk 3 — COMPLETE 2026-04-19 (10 items + 3 steps done)

---

## OLD (replaced by above)

- [ ] Scan accepted 38 — flag anything that feels wrong
- [ ] Scan rejected 12 — especially R10 (multi-currency) — **⚠️ needs revisit due to P6 modification**
- [ ] Confirm big items:
  - [ ] #1 10 alphas → 7 true + 3 work products + 1 entity
  - [ ] #4 Strategic-management → 5 sub-roles — **already approved Chunk 1**
  - [ ] #9 Agent strategist → strategy-support-analyst — **already approved Chunk 1**
  - [ ] #24 Career J0-JX reference; J-Auto/J-Approve/J-Strategic operational
  - [ ] #25 Tools 14 → 5 + Healthchecks.io
  - [ ] #27 Rollout 14-day → 7+7 split

---

## Chunk 4 — Outstanding Tensions [IN PROGRESS — 1/4]

- [x] ~~OT1 Strategic-management decomposition~~ — **RESOLVED early in Chunk 1** (5 sub-roles hybrid accepted)
- [x] **OT2 Bilingual frontmatter — Scenario E (Hybrid):** EN summary в policy/decisions; EN-primary в roles/ops; RU default wiki/directions; auto-translation hook для wiki/concepts/summaries; client folders per language в outreach/de/en/ru
- [x] **OT3 EU AI Act tier — Scenario C (Risk-proportional)** + compliance calendar + DPA template Phase 1
- [ ] OT4 Trademark Jetix vs Disney
- [ ] OT5 FPF-Lite token-budget treatment + publishing

---

## Chunk 5 — Part 2 Areas 1-5 → D1-D5 [PENDING]

- [ ] Area 1 → D1 JETIX-ARCHITECTURE-FINAL
- [ ] Area 2 → D2 JETIX-FOLDER-STRUCTURE
- [ ] Area 3 → D3 JETIX-ROLE-MANIFESTS
- [ ] Area 4 → D4 JETIX-VS-LIFE-OS
- [ ] Area 5 → D5 JETIX-KNOWLEDGE-ARCHITECTURE

---

## Chunk 6 — Part 2 Areas 6-9 → D6-D9 [PENDING]

- [ ] Area 6 → D6 JETIX-FPF-LITE
- [ ] Area 7 → D7 JETIX-CAREER-LEVELS
- [ ] Area 8 → D8 docs/INSTRUCTIONS
- [ ] Area 9 → D9 decision record

---

## Chunk 7 — Final sign-off + Roadmap [PENDING]

- [ ] Part 5.1 D1-D9 writing order confirmation
- [ ] Part 5.2 timeline
- [ ] Part 5.3 7+7 rollout post-deploy
- [ ] Part 6.1 v2 vs v1 verify list
- [ ] Part 6.2 open questions judgment
- [ ] Part 6.3 recommended actions

**Output после Chunk 7:**
- [ ] ADR финализован (status: approved)
- [ ] Commit + push
- [ ] Stage 4 unblocks → D1-D9 writing start
