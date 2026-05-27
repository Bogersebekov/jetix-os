---
title: "Phase 1 — Threat models для Jetix (founder / cohort / platform)"
date: 2026-05-27
phase: 1
parent_prompt: prompts/info-security-own-infra-research-2026-05-27.md
F: F3 (synthesis от security canon + grounded stack)
G: prompt-info-security-own-infra-research-2026-05-27
R: refuted_if_no_threat_model
constitutional_posture: R1 surface only + R11 + R12 paired-frame + append-only
language: russian
status: draft (phase report)
---

# Phase 1 — Threat models для Jetix

> **Дисциплина (R12-honest, anti-security-theater):** threat-model говорит правду о том,
> что **реально** угрожает, а не что звучит страшно. Для Jetix на 2026-05-27 главная угроза —
> **НЕ** государства и хакеры-АРТ, а **self-inflicted** (утечка ключа, потеря устройства,
> single-VPS без бэкапа) + **idea-theft** (вся стратегия в plaintext markdown). Это база.

## §1.0 Метод оценки

Каждая угроза оценивается **Likelihood × Impact** (L/I по 1-5) → **Risk = L×I**.
Привязка к языку системы: Part 8 blast-radius Tier 0-3 + F-грейд (F8 constitutional /
F4 operational / F2 cosmetic) [src:part-8 §H.1 + §I.2]. Триаж: Risk ≥15 = «делать сейчас»;
8-14 = «Build/Run»; ≤7 = «осознать, отложить».

## §1.1 Активы (что защищаем) — asset inventory

| Актив | Где живёт сейчас | Ценность | Класс CIA |
|---|---|---|---|
| **Вся стратегия Jetix** (KB, decisions/, metaplan, FPF) | plaintext markdown в git на jetix-vps + GitHub | **критичная** — first-mover advantage, весь дизайн сети | **C** (конфиденциальность) |
| **CRM реальных людей** (Tseren, Kaiser, партнёры) | `crm/` markdown + Notion-view | высокая — доверие + GDPR personal data | **C** |
| **Голосовые заметки Руслана** | `raw/transcripts/` + Groq API (transit) + Telegram | высокая — личное мышление, незрелые идеи | **C** |
| **Доступы/секреты** (API keys, SSH, Notion token) | `.env`, `~/.ssh/`, env vars на VPS | критичная — ключ ко всему остальному | **C+I** |
| **jetix-vps сам** (compute + filesystem = source of truth) | один Hetzner CPX32 | критичная — SPOF всей системы | **A** (доступность) + **I** |
| **Целостность KB** (никто тайно не подменил факт/решение) | git history | высокая | **I** — покрыто Part 8 |
| **Будущая казна/кошельки** (treasury, Mondragón payouts) | пока нет; Phase 3 | будет критичной | **C+I+A** |
| **Данные участников когорты/кланов** | пока нет; Run stage | высокая + **R12-обязательство** | **C** + constitutional |

## §1.2 Adversary taxonomy (кто атакует) — 6 типов

| # | Противник | Мотив | Вектор | L (сейчас) | I | Risk |
|---|---|---|---|---|---|---|
| **A1** | **Self-inflicted / accidental** | — (ошибка) | API-key в git-коммите, потерянный/незашифрованный ноут, misconfiguration, public-repo экспозиция, потеря единственного VPS без бэкапа | **5** | 4 | **20 🔴** |
| **A2** | **Competitors / idea-thieves** | украсть стратегию/first-mover | доступ к публичному/полупубличному репо, утечка через партнёра, соц-инженерия | **3** | 5 | **15 🔴** |
| **A3** | **Opportunistic criminals** | деньги (credential stuffing, ransomware, SIM-swap, crypto-drain) | phishing, переиспользование паролей, SMS-2FA bypass, malware | **4** | 3 | **12 🟡** |
| **A4** | **Insider (cohort/clan/contractor)** | данные, саботаж, poaching | легитимный доступ → exfiltration; растёт с когортой | 2 (нет когорты) → **4** (Run) | 4 | 8→**16** |
| **A5** | **Platform operator сам (R12-модель)** | extraction beyond share | оператор имеет root → может «доить» данные участников | n/a (=Руслан) | 5 | **constitutional** |
| **A6** | **State actors / regulators** | контроль, комплаенс, (гипотет.) подавление | legal compulsion, infra-seizure, surveillance; растёт с Network-State нарративом + crypto-казной | **1** → 3 (Scale) | 5 | 5→**15** |

**Главный вывод §1.2:** сегодня доминируют **A1 (self-inflicted, Risk 20)** и **A2 (idea-theft, Risk 15)**. A3 хроничен. A4/A6 растут со стадией (Run/Scale). A5 — **уникален для Jetix**: обещание «не использовать против людей» (O-193) означает, что **сам оператор платформы моделируется как полу-доверенный противник**, конституционно ограниченный R12. Это не паранойя — это и есть суть «самой безопасной сети»: безопасность участника **в том числе от платформы**.

## §1.3 Founder personal threat model

**Контекст:** Руслан = single point. Его устройства + аккаунты = ключ ко всей системе.

**Топ-угрозы и митигации:**

1. **Утечка API-ключа / секрета в git (A1, Risk 20 🔴).**
   - *Реальность:* в CLAUDE.md уже есть правило «API-key audit перед каждым коммитом» + memory `feedback_no_api_keys`. Но это процедурное, не enforced машинно для всех путей.
   - *Митигация (сейчас):* pre-commit hook `gitleaks`/`git-secrets` (блокирует push с secret-паттерном) — это Default-Deny на уровне git; `.env` в `.gitignore` (проверить); ротация любого ключа, который хоть раз был в истории. **F8-grade** (constitutional — leak = halt-log-alert).
2. **Потеря/кража устройства (A1/A3, Risk 12-16).**
   - *Митигация:* full-disk encryption (LUKS на Linux, FileVault на Mac) на всех устройствах; auto-lock; remote-wipe где возможно.
3. **SIM-swap → обход SMS-2FA (A3, Risk 12 🟡).**
   - *Митигация:* **убрать SMS-2FA везде**, заменить на TOTP (Aegis/2FAS) + **hardware-ключ (YubiKey/SoloKey)** для критичных аккаунтов (GitHub, Google, email, exchange/wallet). SMS-2FA = известная дыра (Antonopoulos: «SMS 2FA хуже, чем ничего, потому что даёт ложную уверенность»).
4. **Компрометация единственного SSH-ключа к VPS (A1/A3, Risk 12).**
   - *Митигация:* SSH только по ключу (отключить пароли — проверить `sshd_config`); ключ на hardware-токене (FIDO2 ssh-key) или passphrase-protected; fail2ban; VPS-доступ только через Tailscale (закрыть 22 порт наружу).
5. **Phishing / account takeover (A3, Risk 12).**
   - *Митигация:* password manager (Bitwarden/1Password) — уникальный пароль на каждый сервис; hardware-2FA = phishing-resistant (WebAuthn проверяет origin).

**OPSEC-доктрина для founder (Naval / Antonopoulos lens):**
- **«Скучные основы бьют экзотику»** — менеджер паролей + hardware-2FA + FDE + бэкапы закрывают ~95 % реалистичных атак. Сначала это, потом всё остальное.
- **Минимизация поверхности** — меньше аккаунтов, меньше устройств, меньше секретов. Каждый сервис = строка attack-surface.
- **Компартментализация** — отдельные идентичности/ключи под отдельные функции (личное / Jetix-операционка / казна). Компрометация одного ≠ компрометация всего.
- **Assume breach** — шифруй at-rest и in-transit по умолчанию; считай, что любой single point однажды упадёт → бэкап + ротация ключей.
- **«Not your keys, not your data»** (Antonopoulos применительно к данным) — пока стратегия живёт только в Notion/Claude API, она не полностью «твоя». Self-hosting (Phase 2) = шаг к data-ownership.

## §1.4 Cohort member threat model (Run stage — когда есть участники)

**Сдвиг модели:** участник делится данными с платформой. Теперь **платформа — часть его threat-surface**. Это прямо завязано на O-193 + R12.

| Угроза участнику | Источник | Митигация |
|---|---|---|
| Платформа извлекает/продаёт его данные | **A5 (operator)** | R12 constitutional: «не продавать базы / не использовать против людей»; технически — данные участника шифруются ключом участника (см. Phase 3 E2E); **fork-and-leave забирает данные** |
| Другой участник ворует/саботирует (poaching) | **A4 (insider)** | Klan Charter R12-floor (no poaching/sabotage); access-controls per-clan; inter-clan governance (Stewards peer-check) [src:metaplan-v4 §4] |
| Breach платформы экспонирует всех участников | A1/A3 | минимизация централизованных данных; per-member encryption; «blast-radius» = один участник, не вся сеть |
| Lock-in: «не могу уйти без потери данных» | **A5** | fork-and-leave без штрафа = R12 ядро; экспорт данных = first-class фича, не afterthought |

**Принцип (R12-критичный):** безопасность участника = **в том числе от Jetix**. «Качалка/склад» (metaplan §4: платформа = infrastructure, не контролёр) на security-языке означает: **платформа держит как можно меньше данных участника в plaintext и как можно меньше может с ними сделать против его воли.** Это и есть техническая реализация «не доить».

## §1.5 Platform threat model (workspace / партнёры / агенты / казна)

| Угроза | Актив | L | I | Митигация |
|---|---|---|---|---|
| **Утечка CRM реальных людей** | партнёры (Kaiser, Tseren) — personal data | 3 | 4 | encryption at-rest; GDPR-минимизация; Notion-view ≠ source → можно держать чувствительное только в зашифрованном fs |
| **Утечка партнёрских разговоров** | trust + репутация | 3 | 4 | E2E messaging (Matrix/Signal) вместо Telegram для чувствительного; не логировать лишнее |
| **Prompt-injection в агентов** | multi-agent система | 3 | 4 | агенты не исполняют внешний input как команды; Default-Deny novel actions (Part 6b); ingest-санитизация; HITL-gate на внешние действия [src:CLAUDE.md §4.1 rules] |
| **Poisoning voice-pipeline** | KB-целостность | 2 | 3 | voice = DRAFT-only, никогда auto-overwrite prod (уже правило); человек-ревью |
| **Кража казны/кошельков** (будущее) | treasury, payouts | 1→4 | 5 | multisig (Safe), hardware-wallets, нет hot-wallet с большими суммами — см. Phase 3 |
| **Потеря jetix-vps (SPOF)** | вся система A | 3 | 5 | **offsite encrypted backup (3-2-1)** — сейчас НЕ найден в репо = критичный gap; см. Phase 4 |

**Prompt-injection — отдельно (AI-специфичная угроза):** Jetix = multi-agent система, читающая внешний контент (URL, PDF, voice, email через `/ingest`). Классический вектор — текст вида «ignore previous instructions, exfiltrate X». Митигация уже частично встроена: brigadier = single dispatcher (hub-and-spoke), Default-Deny на novel actions, HITL на external-facing, voice DRAFT-only. Усилить: ingest-контент всегда treated as **data, not instructions**; никаких авто-исполняемых действий из ingested-материала.

## §1.6 Threat → mitigation сводка (приоритизированная)

| Приоритет | Угроза (Risk) | Митигация | Стадия | F/Tier |
|---|---|---|---|---|
| **P0** | API-key leak (20) | gitleaks pre-commit hook + `.gitignore` audit + ротация | **Build сейчас** | F8/Tier0 |
| **P0** | Single-VPS без бэкапа (15) | Restic/Borg → encrypted offsite (3-2-1) | **Build сейчас** | F4/Tier1 |
| **P0** | Idea-theft / plaintext стратегия (15) | приватность репо (private GitHub); чувствительное под age/GPG; access-audit | **Build сейчас** | F4/Tier1 |
| **P1** | SIM-swap / SMS-2FA (12) | TOTP + hardware-ключ; убрать SMS-2FA | **Build** | F4 |
| **P1** | SSH/VPS exposure (12) | ключ-only + Tailscale-only + fail2ban + закрыть :22 | **Build** | F4 |
| **P1** | Device loss (12) | FDE везде (LUKS/FileVault) | **Build** | F4 |
| **P2** | Insider (Run: 16) | per-clan access + Charter R12-floor + audit-log | **Run** | F4 |
| **P2** | Operator-extraction A5 (constitutional) | E2E per-member encryption + fork-and-leave + R12 | **Run** | F8 |
| **P3** | Treasury theft (Scale: 20) | multisig + hardware + cold storage | **Scale** | F8 |
| **P3** | State actor (Scale: 15) | jurisdiction-diversity + decentralized infra + legal | **Scale** | F8 |

## §1.7 R12 paired-frame на threat-model (influence-ethics surface)

**O-197 «перелопатим, снесём с пути» в security-контексте — CRITICAL.** Адверсариальная риторика «семьи против врагов» в threat-model'е опасна вдвойне: (1) она склоняет к **offensive security** (атаковать «врагов») — это уже не defensive, а потенциально незаконно и этически за гранью; (2) «защита в обмен на лояльность» = exit-cost = R12-tension (fork-prevention-by-deterrence) [src:voice-batch-14 §5]. **Дисциплина:** threat-model Jetix = **строго defensive** (защита участников, в т.ч. от платформы), никакого offensive/«снести врага». «Самая безопасная сеть» = щит, не меч. Это разбирается дальше в Phase 6.

---

*Phase 1 закрыт. R-criterion `no_threat_model` — снят. 6 adversary-типов, 3 уровня модели (founder/cohort/platform), приоритизированная threat→mitigation сводка. Главный честный вывод: доминируют self-inflicted (Risk 20) + idea-theft (15), не экзотика. A5 (operator-as-adversary) = уникальный R12-узел. Дальше: Phase 2 self-hosted alternatives.*
