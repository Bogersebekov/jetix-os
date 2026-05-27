---
title: "Phase 5 — Security & infra roadmap per Build / Run / Scale"
date: 2026-05-27
phase: 5
parent_prompt: prompts/info-security-own-infra-research-2026-05-27.md
F: F3 (synthesis — staged roadmap)
G: prompt-info-security-own-infra-research-2026-05-27
R: refuted_if_no_roadmap_per_stage
constitutional_posture: R1 surface only + R11 Default-Deny gating + append-only
language: russian
status: draft (phase report)
---

# Phase 5 — Roadmap per Build / Run / Scale

> **Связка со стадиями платформы:** Build/Run/Scale = маховик из
> `PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md` + metaplan-v4 §11 (4 волны). Здесь —
> **security/infra-проекция** на эти стадии: что критично, что добавляется, $ / время /
> команда / зависимости, и **exit-критерий** перехода к следующей стадии.
>
> **Сквозной принцип (Phase 4 §4.8):** дешёвая Build-безопасность сейчас НЕ конфликтует с
> foundation-first; дорогой суверенитет (GPU/dedicated/on-chain) = после revenue. «Спешить
> с безопасностью» нужно только в дешёвой её части — и именно её сейчас нет (бэкап, ключи).

## §5.0 Security-maturity дуга (одной строкой)

```
BUILD: «один человек не теряет всё»  →  RUN: «когорта защищена, в т.ч. от платформы»  →  SCALE: «сеть суверенна и не-extractable в коде»
   (гигиена + бэкап + ключи)              (E2E + access + multisig + monitoring)            (decentralized + DID + on-chain R12 + own compute)
```

---

## §5.1 BUILD stage (сейчас — solo founder)

**Цель:** закрыть доминирующие угрозы A1 (self-inflicted, Risk 20) + A2 (idea-theft, 15) + A3 (criminals, 12) **дёшево и быстро**. Это «скучные основы», которые бьют экзотику.

### Что критично СЕЙЧАС (P0)

| Действие | Закрывает | Источник | Усилие |
|---|---|---|---|
| **gitleaks/git-secrets pre-commit hook** + `.gitignore` audit + ротация всех когда-либо-закоммиченных ключей | A1 key-leak | Ph1 §1.3, Ph3 §3.8 | часы |
| **Backup 3-2-1**: Restic → encrypted B2/Storage Box + restore-тест | A1/SPOF (Risk 15) | Ph3 §3.6, Ph4 §4.4 | 1 день |
| **Password manager** (Bitwarden/Vaultwarden) — уникальный пароль на сервис | A3 | Ph2 §2.1-bonus | часы |
| **Hardware-2FA (YubiKey) + TOTP**, убрать **SMS-2FA** везде | A3 SIM-swap | Ph1 §1.3 | день |
| **FDE** (LUKS/FileVault) на всех устройствах | A1 device-loss | Ph1 §1.3 | часы |
| **SSH ключ-only + Tailscale-only** (закрыть :22 наружу) + fail2ban + unattended-upgrades | A3 VPS | Ph4 §4.2/§4.7 | часы |
| **Приватный репо** (private GitHub) + чувствительное под **age/sops** | A2 idea-theft | Ph2 §2.1-2, Ph3 §3.8 | часы |
| **Sensitive 1:1 → Signal** | A3 интерсепт | Ph2 §2.3 | минуты |

### Что добавляется (P1, в эту же стадию)

- **Docker/Podman + Caddy + Tailscale-gating** (prerequisite-слой Phase 2 §2.0).
- **whisper.cpp local** — убрать Groq из voice-пути (первое «собственное вычисление» O-194).
- **Forgejo + private GitHub mirror** (git-суверенитет + offsite).
- **Email → Proton/Mailbox.org** (sovereignty без ops-боли).
- **Doctrine-слой O-193 в документы** (Charter / landing trust-copy): «не продаём базы / не используем против людей / fork-and-leave» — **бесплатно, и это уже сейчас** (это и есть «добавить в документы» из voice).
- Простой uptime-чек (Uptime-Kuma).

**$:** ~€20-30/мес · **Время:** ~3-5 дней focused setup · **Команда:** solo (можно делегировать setup) · **Зависимости:** Docker install → остальное.

**Exit-критерий → Run:** ✅ бэкап работает и restore-протестирован · ✅ ноль секретов в plaintext/git · ✅ hardware-2FA на всех критичных аккаунтах · ✅ doctrine-копия в Charter · ✅ первая когорта/revenue на горизонте.

---

## §5.2 RUN stage (когорта 5-50)

**Сдвиг модели:** появляются **участники** → A4 (insider) растёт до Risk 16, и активируется **A5 (платформа-как-противник)** — обещание O-193 теперь нужно **технически исполнить**, не только продекларировать.

### Что критично

| Действие | Закрывает | Источник |
|---|---|---|
| **Per-member encryption / E2E** — данные участника шифруются так, что платформа не может читать против воли; **fork-and-leave забирает данные** | **A5 operator-extraction** (constitutional) | Ph1 §1.4, Ph3 §3.9 |
| **Access controls per-clan** (кто что видит) + audit-log доступа | A4 insider | Ph1 §1.4 |
| **Charter security clauses** (2-level: floor R12 + inner-clan) — no poaching/sabotage/extraction | A4 + R12 | metaplan §4/§9 |
| **Matrix/Conduit** для cohort/clan-comms (E2E, федерация ≈ mesh) | A3/A4 интерсепт | Ph2 §2.3 |
| **Monitoring (Prometheus+Grafana+Loki)** = материализация Part 8 Phase B + security-SLI (failed-SSH, backup-age, cert-expiry) | A1/A3 detection | Ph4 §4.5 |
| **Headscale** — забрать VPN control-plane | суверенитет сети | Ph4 §4.2 |
| **Multisig (Safe) на казну** как только есть общие средства (события #16/QF) — 3-of-N, никто один не выводит | A5 + treasury-theft | Ph3 §3.2 |
| **Incident-response plan** (что делать при breach: кого уведомить, как ротировать, как восстановить) | все | новое |

### Что добавляется

- **Nextcloud** (files/calendar/contacts), **Cal.com**.
- **Ollama-hybrid** (low-stakes/privacy-sensitive подзадачи локально; frontier для high-stakes).
- Разнесение ролей по 2-3 box (app/db/monitoring) — k3s/Nomad/Compose.
- GDPR-комплаенс по personal-data участников (DPA, data-export, right-to-erasure ≈ fork-and-leave).

**$:** ~€80-180/мес · **Время:** недели (параллельно росту когорты) · **Команда:** +1 infra/security-роль (`infra-steward` — может быть участник клана, IP-1 role-type) · **Зависимости:** Build exit-критерий выполнен + первая revenue (для €/команды).

**Exit-критерий → Scale:** ✅ E2E per-member работает + fork-and-leave экспорт протестирован · ✅ multisig-казна с ≥3 подписантами · ✅ monitoring + incident-response отрепетированы · ✅ ≥2-3 клана стабильны · ✅ revenue покрывает Scale-капекс.

---

## §5.3 SCALE stage (multi-clan 100-1000+)

**Сдвиг:** A6 (state/regulator) растёт до Risk 15 (Network-State нарратив + crypto-казна привлекают внимание); масштаб данных/средств → нужен **decentralized, не-extractable-в-коде** суверенитет. Это горизонт O-194 «собственные серверы / агенты / вычисление».

### Что критично

| Действие | Закрывает | Источник |
|---|---|---|
| **On-chain R12 enforcement** (V10 Option D Hybrid): Mondragón 5:1 + QF + fork-and-leave exit-tokens в смарт-контрактах | A5 + R12 (не-обходимо) | Ph3 §3.9, CLAUDE.md §4.2 |
| **Own compute / GPU** — own LLM-инференс + fine-tuned «свои агенты» (O-194 полностью) | A1 (данные не уходят) | Ph2 §2.1-4, Ph4 §4.1-D |
| **Decentralized/edge infra** — члены хостят узлы (compute+storage); инфра принадлежит сети | SPOF + A6 seizure | Ph4 §4.1-C/§4.3 |
| **Self-sovereign identity (DID/VC)** — переносимая репутация = vetted-network O-195 без lock-in | A5 lock-in + identity | Ph3 §3.7 |
| **Jurisdiction diversity** — инфра/юр-лица в нескольких юрисдикциях; legal-counsel | A6 state | новое |
| **Own DNS + DDoS-партнёр**, dedicated/colo | A3/A6 + суверенитет | Ph4 §4.6 |
| **Внешний security-аудит / сертификации** (для provable «самая безопасная» — Phase 6) | A2/A6 + trust-claim | Ph6 |

### Что добавляется

- Distributed storage (Garage/SeaweedFS/IPFS) на edge-узлах.
- BTCPay для crypto-payments (+ fiat-процессор).
- Full observability + security-SOC-функция.
- Bug-bounty / responsible-disclosure программа.

**$:** €500-2000+/мес или капекс (GPU-железо, dedicated, аудиты) · **Время:** месяцы-годы · **Команда:** выделенная security/infra-функция (несколько ролей) · **Зависимости:** Run проверен + значимая revenue + клан-база + (для on-chain) R12-design-session завершена.

**Exit:** Scale — это steady-state «самой безопасной сети», не выход.

---

## §5.4 Сводная матрица (что-когда-сколько)

| Слой | Build | Run | Scale |
|---|---|---|---|
| **Ключи/2FA** | password mgr + hardware-2FA + sops/age | per-member keys | DID/VC + on-chain |
| **Backup** | Restic 3-2-1 | + monitoring backup-age | distributed + jurisdiction |
| **Network** | Tailscale + закрыть порты | **Headscale** | own DNS + edge mesh |
| **Comms** | Signal (1:1) | **Matrix/Conduit** | federated + bridges |
| **Compute** | 1 VPS + whisper.cpp | 2-3 box + Ollama-hybrid | **own GPU + fine-tune** |
| **Git/KB** | Forgejo + mirror | + access-controls | decentralized |
| **Treasury** | — (нет) | **multisig Safe** | on-chain R12 (5:1/QF/exit) |
| **Monitoring** | uptime-чек | **Prom+Grafana+Loki** | full SOC + bug-bounty |
| **Trust-claim** | doctrine в Charter | transparency report | **внешний аудит/серт** |
| **$/мес** | ~€20-30 | ~€80-180 | €500-2000+/капекс |
| **Команда** | solo | +infra-steward | security-функция |

## §5.5 R11 Default-Deny gating (как каждый шаг проходит gate)

Каждое действие класса «купить железо / развернуть сервис / мигрировать данные / создать кошелёк» = **novel action** → blast-radius категоризация + AWAITING-APPROVAL packet (Part 6b) [src:CLAUDE.md §4.1 rule 11]. Конкретно:

- **Tier 0** (constitutional): создание казны-кошелька, on-chain R12-деплой, любое решение, где single-человек может вывести средства → stop_gate + Halt-Log-Alert.
- **Tier 1** (Ruslan ack same-session): развернуть новый stateful self-host-сервис, мигрировать данные между провайдерами, сменить VPN control-plane.
- **Tier 2** (batch ack): развернуть stateless-сервис, добавить monitoring-метрику.
- **Инвариант:** **нет backup → нет нового stateful-сервиса** (hard gate, Phase 4 §4.4).

## §5.6 R1 reservation

Темп прохождения стадий, выбор опций, capital-allocation на каждой = **решение Руслана** (Q14-2 pre-revenue vs foundation-first). Рой выложил staged-опции + arithmetic + exit-критерии; выбор — за стратегом.

---

*Phase 5 закрыт. R-criterion `no_roadmap_per_stage` — снят. Build (гигиена+бэкап+ключи, ~€20-30/мес, solo) → Run (E2E+access+multisig+monitoring, ~€80-180, +infra-steward) → Scale (decentralized+DID+on-chain R12+own compute, €500-2000+/капекс). Каждый шаг — Default-Deny gated. Дальше: Phase 6 R12 security marketing.*
