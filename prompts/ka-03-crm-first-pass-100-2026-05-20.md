---
title: KA-03 CRM First-Pass 100 Tier-1 Contacts Compile (SAVED — launch when Ruslan acks)
date: 2026-05-20
type: autonomous-execution-prompt
phase_count: 5
parent_explain: prompts/explanations/_EXPLAIN-ka-03-crm-first-pass-100-2026-05-20.md
output_namespace: crm/ + reports/voice-pipeline-2026-05-20-batch-7/_KA-03-EXECUTION-LOG.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: ka-03-crm-first-pass-100
R: refuted_if_entries_misattributed_OR_spam_pattern_OR_private_data_used
constitutional_posture: R1 surface + R6 + R11 (only /crm-add) + R12 + EP-5 + append-only crm/log.md
estimated_runtime: ~6h brigadier autonomous
estimated_cost: <€2
status: SAVED (Ruslan acks separately для launch)
---

# KA-03 CRM First-Pass 100 Tier-1 Contacts — Prompt

> **Trigger:** Ruslan acks separately «launch KA-03». Per-phase commit + push. NOT plan mode — execute immediately on launch.

---

## §0 Pre-flight (mandatory)

ПЕРЕД Phase 1 прочитай:
1. **EXPLAIN:** `prompts/explanations/_EXPLAIN-ka-03-crm-first-pass-100-2026-05-20.md`
2. **Memory rules:**
   - `feedback_research_pool_pattern.md` — discovered-only status; no outreach launch
   - `feedback_cowork_can_push.md` — Ruslan ack для commit+push
3. **Sources:**
   - `reports/jetix-platform-v2-2026-05-19/` §6 — 22 Tier-1 baseline
   - `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/` — Левенчук ecosystem
   - `reports/voice-pipeline-2026-05-20-batch-7/_FULL-DIGEST-batch-7-2026-05-20.md` audio_697 C25
   - `crm/_schema/` + `crm/_templates/`
   - Existing `crm/people/` + `crm/orgs/` (minimal current state)

---

## §1 Phase 1 — Platform v2 §6 baseline → 22 entries (~1h)

**Goal:** Все 22 Tier-1 partner candidates из Platform v2 §6 → CRM entries.

### Steps
1. Read `reports/jetix-platform-v2-2026-05-19/` §6 + relevant section files
2. Extract per Tier-1 name + org affiliation + role/expertise + cross-link references
3. Per entry execute `/crm-add` skill OR manually create `crm/people/<slug>.md` with frontmatter:
   ```yaml
   slug: <kebab-case-name>
   type: person
   tier: 1
   segmentation: <L1-engineer | L2-amplifier | L3-institutional>
   status: discovered
   roles: <per Platform v2 mapping>
   priority: P1
   source: Platform v2 §6
   batch_origin: ka-03-2026-05-20
   created: 2026-05-20
   ```
4. Per-entry content sections per template

### Acceptance
- ≥22 entries в `crm/people/` (or `crm/orgs/` if organizational)
- All entries discovered status
- Index не rebuilt yet (Phase 5)
- Provenance per entry [src: Platform v2 §6]

Commit: `[ka-03] Phase 1 Platform v2 §6 baseline → 22 entries`

---

## §2 Phase 2 — Левенчук ecosystem +15-20 entries (~1.5h)

**Goal:** МИМ + Tseren + Левенчук inner circle from Левенчук inventory v2.

### Steps
1. Read `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/01-inventory-v2-master.md` + 04-cross-link-к-jetix-substrate.md
2. Extract:
   - Левенчук himself (Anatoly Igorevich Levenchuk) — Tier-1 L3-institutional (МИМ founder)
   - Цэрэн Цэрэнов — Tier-1 L2-amplifier (МИМ co-founder + Tseren YouTube channel)
   - МИМ 10th conference speakers (20 talks / 19 speakers per inventory v2 §1.3)
   - LJ ailev frequent commenters (top contributors per Tier 2 T2.X data)
   - Левенчук blurb collaborators
3. Per entry: same template as Phase 1 + `source: Левенчук inventory v2 + section reference`
4. **Strict R11/R12:** discovered status only; no automated outreach

### Acceptance
- ~15-20 NEW entries
- Tseren + Левенчук explicitly P1 (audio_697 C25 priority targets)
- Mark МИМ as `crm/orgs/mim.md` entry

Commit: `[ka-03] Phase 2 Левенчук ecosystem ~15-20 entries`

---

## §3 Phase 3 — Karpathy lineage + Buterin + Anthropic + L1 engineering targets +10-15 entries (~1h)

**Goal:** Tier-1 partner names per batch-7 + handoff §6 + Sprint-Synthesis-v2 D2 acks.

### Steps
1. Reference:
   - HANDOFF §6 — «D2 Tier-1 partners ACKED defaults: Karpathy + Buterin + Anthropic»
   - audio_697 C25 sequence reference
   - 5 acked concept docs (engineering audiences)
2. Extract candidate names:
   - **Karpathy lineage:** Andrej Karpathy + key collaborators (referenced в `outreach/karpathy-outreach-pack-2026-05-19.md`)
   - **Buterin / Ethereum:** Vitalik Buterin + Ethereum Foundation principals
   - **Anthropic:** Dario Amodei / key researchers (public-known names only; no insider data)
   - **L1 engineers:** Engineer Workshop cohort 5-15 candidate slots (per batch-7 KA-04 reference)
3. Per entry: template + provenance

### Acceptance
- ~10-15 NEW entries
- Karpathy + Buterin + Anthropic principals all marked
- L1 Engineer cohort slots pre-allocated с `cohort_slot: 1..15` field

Commit: `[ka-03] Phase 3 Karpathy/Buterin/Anthropic + L1 cohort ~10-15 entries`

---

## §4 Phase 4 — L2 amplifiers + RU community +30-40 entries (~1.5h)

**Goal:** L2 amplifier layer per cascade-150-to-15 model + RU L2 telegram community sample.

### Steps
1. References:
   - `decisions/strategic/JETIX-OUTREACH-SCALABLE-2026-05-18.md` — cascade model
   - Platform v2 §20 outreach templates
   - audio_681 verbatim — RU community frame
2. Extract candidates:
   - RU systems-thinking community (МИМ residents + alumni)
   - RU AI / engineering Telegram channels (commenters + admins)
   - Adjacent academic / methodology figures (no individual outreach yet; discovered status)
3. WebSearch validation для known names only (NO scraping bulk lists)

### Acceptance
- ~30-40 NEW entries L2-amplifier segmentation
- Diverse subset (academic / community / engineering / methodology)

Commit: `[ka-03] Phase 4 L2 amplifiers + RU community ~30-40 entries`

---

## §5 Phase 5 — Index rebuild + finalize (~1h)

**Goal:** `/crm-rebuild-index` + final validation + execution log.

### Steps
1. `/crm-rebuild-index` skill → updates `crm/index.md`
2. Per-entry tag validation (segmentation / status / priority correct)
3. Append `crm/log.md`:
   ```markdown
   ## 2026-05-20 — KA-03 first-pass 100 contacts compile
   - 22 Platform v2 §6 baseline migrated
   - 15-20 Левенчук ecosystem added
   - 10-15 Karpathy/Buterin/Anthropic added
   - 30-40 L2 amplifiers + RU community added
   - Total: ~80-90 person entries + ~10-20 org entries
   - All status: discovered
   - Ruslan ack pending for Tier-1 promotion to cold/warm
   ```
4. Create `reports/voice-pipeline-2026-05-20-batch-7/_KA-03-EXECUTION-LOG.md` с summary:
   - Total entries created
   - Per-segmentation count
   - Tier-1 priority list for Ruslan ack queue (specific names)
   - Cross-link к Platform v2 / Левенчук inv / audio anchors
5. Final commit + push

Final echo:
```
DONE Phase 5 — N commits / ~100 CRM entries / Ruslan ack queue M Tier-1 names ready
```

Commit: `[ka-03] Phase 5 index rebuild + execution log + final push`

---

## §6 Operational rules

- **Per-phase commit + push** (mandatory)
- **NO automated outreach** — discovered status only; KA-01/02 handle outreach separately
- **NO external scraping** of private data — public-known names + Platform v2 baseline + Левенчук inventory only
- **R12 anti-extraction:** no contact info collection beyond public profiles
- **R11 Default-Deny:** only `/crm-add` skill ops; no novel actions
- **Russian primary** в descriptions / notes; English where canonical (org names / handles)
- **Provenance per entry** — `source:` field mandatory

---

## §7 If blocked

- Single entry fails (missing public data) → skip + log; не halt entire run
- `/crm-add` skill fails → fallback manual `crm/people/<slug>.md` Write
- WebSearch returns nothing for specific name → mark «unverified» + continue
- Git push race → rebase + retry; не halt

---

## §8 Trigger to launch

Ruslan acks «launch KA-03» → server CC tmux session:

```bash
cd ~/jetix-os && git pull --ff-only && tmux new -s ka03 "claude --dangerously-skip-permissions"
```

Paste:
```
ultrathink. Прочитай prompts/ka-03-crm-first-pass-100-2026-05-20.md и prompts/explanations/_EXPLAIN-ka-03-crm-first-pass-100-2026-05-20.md. Выполни все 5 phases автономно, per-phase commit + push origin main, final push в конце. Discovered status only — NO automated outreach. Russian primary descriptions. R12 anti-extraction discipline. Не пауза, не вопросы.
```

---

*Prompt SAVED 2026-05-20. Ready для launch when Ruslan acks. Per memory `feedback_research_pool_pattern.md` — saved-not-launched discipline.*
