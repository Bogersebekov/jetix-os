---
title: Info Security + Own Infrastructure Research — последние заметки extraction + deep на security/privacy/own-infra
date: 2026-05-27
type: server-cc-autonomous-prompt
prompt_class: deep-research-info-security-own-infra
output_main_doc: decisions/strategic/INFO-SECURITY-OWN-INFRA-RESEARCH-2026-05-27.md
output_reports_dir: reports/info-security-own-infra-research-2026-05-27/
F: F2-F3
G: prompt-info-security-own-infra-research-2026-05-27
R: refuted_if_no_threat_model_OR_no_self_hosted_alternatives_OR_no_roadmap_per_stage_OR_no_last_notes_extracted_OR_LOCK_modified
constitutional_posture: R1 surface only + R6 + R11 + R12 paired-frame + IP-1 + append-only
roy_dispatch_target: brigadier + engineering-expert + systems-expert + ml-ai-foundations-expert + sota-tracker-expert + influence-ethics-expert
language: russian primary
style_anchor: PARTNER-OFFERING-HUMAN-LANG + workshop-concept + V4 metaplan + wiki/concepts/jetix-security-privacy-pillar.md
mode: DEEP RESEARCH — info-security + own infrastructure roadmap + last notes extraction
mermaid_target: 4-6 schemes SEC-1..SEC-6
status: READY-TO-EXECUTE
runtime_target: 3-5h autonomous
audience_primary: Ruslan reads → substrate для V4 #17 Direction add (separate prompt позже)
---

# 🔐 Info Security + Own Infrastructure Research

## §0 Контекст

Per Ruslan voice 27.05:
> «Последние заметки просмотреть, ресёрч их и оттуда вытянуть ещё информацию по информационной безопасности и по разработке собственных валетов/баз/серверов».

> «Безопасность добавляем — документ добавляем. Jetix = самая безопасная сеть в мире / конфиденциальность / без продажи баз / путь к своей инфраструктуре».

**Цель:** deep research substrate для **V4 Direction #17 🔐 Безопасность/Privacy** + collected substrate из последних voice notes.

---

## §17.0 MAX-density mandate

ROY dispatch:
- engineering-expert — self-hosted stack / Docker / Kubernetes / encryption patterns
- systems-expert — threat models / cybersecurity architecture
- ml-ai-foundations-expert — AI model self-hosting (LLM ops / local inference)
- sota-tracker-expert — current SOTA self-hosted alternatives + privacy tools
- influence-ethics-expert — R12 paired (security marketing claims STRICT)

Main ≥15-20K plain Russian + 4-6 mermaid.

---

## §1 Phases (8 phases)

### Phase 0 — Substrate read + last voice notes extraction

**Read:**
- `wiki/concepts/jetix-security-privacy-pillar.md` (already promoted Tier A concept)
- `wiki/ideas/vetted-network-data-mobility.md`
- voice-batch-14 INSIGHTS + transcripts (Note 2 security/privacy focus)
- All voice batches 11-14 (scan для security/privacy/infra mentions — extract all)
- voice-pipeline-v2 main (technical stack baseline)
- V4 metaplan main (16 directions context)
- Foundation Part 8 (Health Monitoring & System Integrity)

**Output:** `reports/info-security-own-infra-research-2026-05-27/01-substrate-last-notes.md` (~2-3K)

---

### Phase 1 — Threat models для Jetix

**Tasks:**
- Founder personal threat model (data on personal devices / cloud services / Telegram / Notion)
- Cohort member threat model (partners / clan members data)
- Platform threat model (Jetix workspace data / partner conversations / financial flows)
- Adversary types: state actors / competitors / criminals / accidental leaks / insider threats
- OPSEC for founders (per Naval / Andreas Antonopoulos style)
- Threat enumeration → mitigation per threat

**Output:** `.../02-threat-models.md` (~3K)

---

### Phase 2 — Self-hosted alternatives для commonly used tools

**Tasks:**
- Per current tool (Notion / GitHub / Telegram / Anthropic Claude / Google / Gmail / Stripe / Calendly / etc.) — self-hosted alternative analysis:
  - **Notion → AppFlowy / Outline / Affine** (self-hosted KB)
  - **GitHub → Gitea / Forgejo** (self-hosted git)
  - **Telegram → Matrix / Signal self-hosted** (E2E messaging)
  - **Claude API → llama.cpp / Ollama / vLLM** (local LLM inference)
  - **Google Workspace → Nextcloud + OnlyOffice + Mailcow**
  - **Stripe → BTCPay Server / open-source payments**
  - **Calendly → Cal.com self-hosted**
  - **CRM → SuiteCRM / Mautic self-hosted**
- Per tool: cost / time / quality tradeoff
- Migration roadmap (что first / dependency chain)

**Output:** `.../03-self-hosted-alternatives.md` (~4K)

---

### Phase 3 — Own wallets / data sovereignty / crypto integration

**Tasks:**
- "Валеты" = wallets (crypto wallets для cooperative governance per V10 Programmable Ethereum Phase 2+):
  - Custodial vs non-custodial
  - Self-hosted node setup (Ethereum / L2)
  - Multisig (Safe / Gnosis)
  - Hardware wallets (Ledger / Trezor)
- Data sovereignty: own database (Postgres self-hosted) vs cloud (Supabase / etc.)
- Backup strategy (3-2-1 rule + encrypted offsite)
- Identity (self-sovereign — DID / VC) vs federated (OAuth)
- Documents encryption (age / GPG / Cryptomator)

**Output:** `.../04-own-wallets-data-sovereignty.md` (~3K)

---

### Phase 4 — Own infrastructure stack (compute / network / storage)

**Tasks:**
- Current state: Hetzner CPX32 (4 vCPU / 8GB RAM / 160GB) — single VPS
- Scaling options:
  - More Hetzner instances (clustered)
  - Dedicated server (own hardware in colo)
  - Edge nodes (cohort members host parts)
  - Bare metal at home (with redundancy)
- Network: Tailscale (current) vs Headscale self-hosted / WireGuard direct / Yggdrasil
- Storage: local + offsite encrypted (per Mondragón cooperative pattern — distributed)
- Backup: Restic / Borg / Tarsnap
- Monitoring: Prometheus + Grafana self-hosted
- DNS: own DNS vs Cloudflare
- Cost projection per Build/Run/Scale stages

**Output:** `.../05-own-infrastructure-stack.md` (~3-4K)

---

### Phase 5 — Roadmap per Build/Run/Scale stages

**Tasks:**
- Build stage (now — solo founder): что critical security сейчас (basic OPSEC / encrypted backups / 2FA everywhere / password manager)
- Run stage (cohort 5-50): что добавляется (shared infrastructure / member access controls / Charter security clauses)
- Scale stage (multi-clan 100-1000+): что critical (own data centre / federated identity / multisig treasury / decentralized infra)
- Per stage: cost / time / team / dependencies

**Output:** `.../06-roadmap-stages.md` (~2-3K)

---

### Phase 6 — R12-aligned security marketing (как продвигать «самая безопасная сеть»)

**Tasks:** AUTO-FIRE influence-ethics:
- Claim «самая безопасная» — backed by what? (proof points / certifications / audits)
- Avoid security theater (look secure без real security)
- Honest disclosure of limitations
- Per partner-facing claims (Tseren type запросы) — provable, не marketing
- Compare с competitors honestly
- Open-source as trust mechanism

**Output:** `.../07-r12-security-marketing.md` (~2-3K)

---

### Phase 7 — Mermaid SEC-1..SEC-6 + Main consolidated + SUMMARY + INDEX (final push)

**Mermaid:**
- SEC-1 Threat models heatmap (per actor × per asset)
- SEC-2 Self-hosted migration roadmap (current → 2 years)
- SEC-3 Own infrastructure stack architecture
- SEC-4 Build/Run/Scale security progression
- SEC-5 Wallet / identity / data sovereignty
- SEC-6 R12 marketing claims provability

**Main doc** ~15-20K plain Russian + sections per phases + R1 decisions queue.

00-SUMMARY ≤800w.

**Final commit:** `[info-sec-infra] Phase 7 Main + SUMMARY + mermaid + INDEX (final push)`

---

## §2 Output structure

```
decisions/strategic/
└── INFO-SECURITY-OWN-INFRA-RESEARCH-2026-05-27.md   # main ~15-20K + 4-6 mermaid

reports/info-security-own-infra-research-2026-05-27/
├── 00-SUMMARY-FOR-RUSLAN.md
├── 01-substrate-last-notes.md
├── 02-threat-models.md
├── 03-self-hosted-alternatives.md
├── 04-own-wallets-data-sovereignty.md
├── 05-own-infrastructure-stack.md
├── 06-roadmap-stages.md
├── 07-r12-security-marketing.md
└── diagrams/_INDEX.md
```

---

## §3 Launch command

```bash
ssh jetix
tmux new -s info-sec-infra
cd ~/jetix-os && git pull --ff-only
claude --dangerously-skip-permissions -p "Autonomous execution: prompts/info-security-own-infra-research-2026-05-27.md. 8 phases per-phase commit+push [info-sec-infra] Phase N. Deep research info-security + own infrastructure roadmap + last voice notes extraction. Substrate: wiki/concepts/jetix-security-privacy-pillar + voice batches 11-14 + V4 metaplan + Foundation Part 8. Self-hosted alternatives (Notion→AppFlowy / GitHub→Gitea / Telegram→Matrix / Claude→Ollama / etc.). Own wallets/identity/data sovereignty. Infrastructure stack (Hetzner → distributed). Roadmap per Build/Run/Scale stages. R12 STRICT (security marketing claims provable). Main ~15-20K + SUMMARY ≤800w + 4-6 mermaid SEC-1..SEC-6 + 7 phase reports. Pool result. Final push Phase 7."
# Ctrl-B then D
```

Runtime: 3-5h autonomous (parallel to founder-research).
