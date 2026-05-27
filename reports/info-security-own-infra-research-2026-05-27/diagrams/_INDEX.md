---
title: "Diagrams INDEX — Info-Security + Own-Infra Research (SEC-1..SEC-6)"
date: 2026-05-27
type: diagrams-index
parent: decisions/strategic/INFO-SECURITY-OWN-INFRA-RESEARCH-2026-05-27.md
language: russian
status: pool
---

# Diagrams INDEX — SEC-1..SEC-6

Все 6 схем встроены inline в главный документ
`decisions/strategic/INFO-SECURITY-OWN-INFRA-RESEARCH-2026-05-27.md`.
Тема: base + черный текст (`primaryTextColor:#000`) — единая с metaplan-v4.

| ID | Название | Тип mermaid | Где в Main | Что показывает |
|---|---|---|---|---|
| **SEC-1** | Adversary risk (Likelihood × Impact) | quadrantChart | §3.2 | 6 типов противников на L×I; A1 self-inflicted + A2 idea-theft = ACT NOW; A5 operator вне L×I (constitutional) |
| **SEC-2** | Self-hosted migration dependency-chain | graph LR | §4.2 | PREREQ (Docker+Caddy+Tailscale+backup) → Build quick-wins → Run → Scale; 🟢🔵🔴 по стадиям |
| **SEC-3** | Own infrastructure stack architecture | graph TB | §6.1 | целевая архитектура: :443 only · всё админ за Tailscale · backup 3-2-1 · monitoring через Part 6b gate · hybrid Claude/Ollama/whisper |
| **SEC-4** | Build/Run/Scale security progression | graph LR | §7.1 | security-maturity дуга с exit-критериями переходов; $/мес per стадия |
| **SEC-5** | Wallet / identity / data sovereignty | graph TB | §5.2 | hardware→multisig→on-chain R12; backup/encryption/Postgres; ENS→DID/VC; всё → R12 anti-extraction |
| **SEC-6** | R12 security marketing claim-ladder + gate | graph TB | §8.2 | 5 уровней claim (0 reject superlative → 4 аудит); anti-theater+R12 gate; O-197 militant → reject |

## Маппинг схем на phase-reports

- SEC-1 ← `02-threat-models.md` §1.2
- SEC-2 ← `03-self-hosted-alternatives.md` §2.3
- SEC-3 ← `05-own-infrastructure-stack.md` §4.9
- SEC-4 ← `06-roadmap-stages.md` §5.0/§5.4
- SEC-5 ← `04-own-wallets-data-sovereignty.md` §3.9
- SEC-6 ← `07-r12-security-marketing.md` §6.1/§6.8

## Рендеринг

Схемы рендерятся в GitHub/Notion-mermaid. Если текст не виден на тёмной теме —
init-блок форсит `primaryTextColor:#000 / textColor:#000`. quadrantChart (SEC-1) —
без custom-init (дефолтная тема даёт тёмный текст).
