---
title: "Phase 2 — Self-hosted alternatives для текущего стека"
date: 2026-05-27
phase: 2
parent_prompt: prompts/info-security-own-infra-research-2026-05-27.md
F: F3 (synthesis от SOTA self-hosted landscape + grounded stack)
G: prompt-info-security-own-infra-research-2026-05-27
R: refuted_if_no_self_hosted_alternatives
constitutional_posture: R1 surface only + R11 + append-only
language: russian
status: draft (phase report)
---

# Phase 2 — Self-hosted alternatives

> **Honest reframe (важнейший вывод фазы):** Jetix **уже суверенее, чем кажется**.
> Filesystem = source of truth (Global Rule), git = authoritative, CRM = markdown,
> Notion = всего лишь **view**. То есть «self-hosting» для Jetix — это **не** болезненная
> миграция данных, а две более узкие задачи:
> 1. **Сократить, какие чувствительные данные вообще касаются внешних API** (Claude / Notion / Groq).
> 2. **Убрать single-points-of-dependency** (один GitHub, один Groq, один VPS).
> Это меняет приоритеты: не «всё мигрировать», а «закрыть утечки + добавить опции».

## §2.0 Gating-зависимость #0 (prerequisite для всего)

На `jetix-vps` **нет Docker** (замерено Phase 0). Почти весь self-hosted стек = Docker/compose.
Поэтому **первый шаг любого self-hosting** = базовый слой:

- **Docker + docker-compose** (или Podman для rootless = безопаснее).
- **Reverse-proxy с авто-TLS**: Caddy (проще) или Traefik. Один порт 443 наружу.
- **Доступ только через Tailscale** (уже установлен) — сервисы не торчат в публичный интернет; админка за VPN.
- **Backup-слой** (Restic/Borg) — до того, как класть данные в self-hosted сервис (см. Phase 4).

Без этого слоя любой self-hosted сервис = новый attack-surface без бэкапа. **Default-Deny: не разворачивать сервис до готовности backup + reverse-proxy + Tailscale-gating.**

## §2.1 Per-tool анализ

Шкалы: **$** = инфра-стоимость (низ/сред/выс) · **⏱** = время на миграцию · **Δquality** = разрыв качества vs текущий (0 = паритет, − = хуже) · **🔒Δ** = насколько снижает утечку чувствительных данных · **Verdict/стадия**.

### (1) Notion → AppFlowy / Outline / Affine / Anytype

| Альтернатива | Что | Плюсы | Минусы |
|---|---|---|---|
| **AppFlowy** | Rust, local-first, Notion-like; self-host AppFlowy-Cloud (Docker) | local-first; быстрый; open-source | DB/relations не на паритете с Notion |
| **Outline** | wiki (Postgres+Redis) | отличный team-wiki, поиск | не kanban/DB; нужен Postgres+Redis |
| **Affine** | local-first docs + edgeless canvas | приватность, canvas | молодой |
| **Anytype** | local-first, E2E-encrypted, P2P | **шифрование + без сервера** | своя модель данных, кривая обучения |

- **$** низ-сред · **⏱** сред (но данные уже в markdown!) · **Δquality** −1 (DB-фичи) · **🔒Δ** средний.
- **Verdict:** **DEFER / низкий приоритет.** Notion = view, не source → миграция не срочна. Реальный quick-win не «заменить Notion», а **не класть HIGH-чувствительное в Notion вообще** (держать в зашифрованном fs). Если когда-то заменять — **Anytype** (E2E, sovereignty) для приватного, **Outline/AppFlowy** для team-wiki. Стадия: **Run+**.

### (2) GitHub → Forgejo / Gitea / GitLab ⭐ ранний кандидат

| Альтернатива | Что | Заметка |
|---|---|---|
| **Forgejo** | community-fork Gitea (Codeberg) | лёгкий (Go, ~раз. на 8 GB VPS); **fork-friendly governance ≈ ценности Jetix** |
| **Gitea** | upstream | то же, но governance менее community |
| **GitLab** | full DevOps | **слишком тяжёлый** (≥4 GB только на себя) — overkill |

- **$** низ (на текущем VPS) · **⏱** низ (git распределён — `git remote add` + mirror) · **Δquality** 0 (для git-core) · **🔒Δ** **высокий** (закрывает A2 idea-theft: стратегия больше не на чужом сервере).
- **Verdict:** **СИЛЬНЫЙ Build-кандидат, но с нюансом.** GitHub также даёт offsite-backup + reach. **Рекомендуемый паттерн — hybrid:** Forgejo (self-host, Tailscale-only) = primary для приватной стратегии; **private** GitHub mirror = offsite-backup. Не «или-или». Философски Forgejo резонирует с fork-and-leave Jetix. ⚠️ R12-honest: «суверенный git» ≠ «безопаснее», если single-VPS без бэкапа — Forgejo без backup хуже GitHub. Сначала Phase 4 backup.

### (3) Telegram → Matrix / Signal / SimpleX ⭐ Run-критично

| Альтернатива | Что | E2E | Self-host |
|---|---|---|---|
| **Matrix (Conduit)** | федеративный, Rust-сервер (лёгкий) | да (Olm/Megolm) | да; **bridge mautrix-telegram** для миграции |
| **Matrix (Synapse)** | reference-сервер (Python) | да | тяжелее Conduit |
| **Signal** | централизованный | **да (золотой стандарт)** | нет (практически) |
| **SimpleX** | без идентификаторов | да + metadata-privacy | да; молодой |

- **$** низ-сред · **⏱** сред (Matrix-сервер + bridge) · **Δquality** −1 (UX vs Telegram) · **🔒Δ** **высокий** (Telegram не-E2E по умолчанию, cloud-stored).
- **Verdict (двухтактный):**
  - **Сейчас (zero-infra):** перевести чувствительные 1:1 разговоры (Kaiser, партнёры) на **Signal** — бесплатно, лучший E2E, ничего разворачивать не надо.
  - **Run (когорта):** **Matrix/Conduit** self-host для cohort/clan-comms (федерация ≈ mesh-кланы; per-room E2E; bridge на Telegram для плавного перехода). Стадия **Run**.

### (4) Claude API → Ollama / llama.cpp / vLLM + Whisper → whisper.cpp ⚠️ самый длинный горизонт

**Это O-194 «свои обученные агенты / собственное вычисление» — самый дорогой, pre-revenue-tensioned (Q14-2).**

| Что | Реальность на текущем железе (4 vCPU / 8 GB, без GPU) |
|---|---|
| **Ollama / llama.cpp** локальный LLM | тянет только маленькие (7B квант, медленно, низкое качество). **Разрыв с Claude Opus/Sonnet огромен** — весь рой держится на frontier-качестве |
| **vLLM** | нужен GPU; на VPS без GPU нерелевантен |
| GPU-опции | Hetzner GPU-инстансы (аренда); RunPod/vast.ai (по-часовая); **покупка** (used RTX 3090 ~$700, RTX 4090 ~$1700, Mac Studio unified-memory для больших моделей) |
| **Whisper → whisper.cpp / faster-whisper** локально | **РЕАЛИСТИЧНО на CPU** (whisper.cpp), тем более на скромном GPU. Заменяет **Groq Whisper** (сейчас все голосовые Руслана = HIGH-данные — уходят в Groq API) |

- **Claude→local: $** выс (GPU/железо) · **⏱** выс · **Δquality** −2..−3 (серьёзный регресс на текущем железе) · **🔒Δ** высокий (если данные не уходят).
- **Whisper→local: $** низ · **⏱** низ-сред · **Δquality** −1 (medium-модель ≈ Groq при чуть большем времени) · **🔒Δ** **высокий** (голос Руслана не покидает машину).
- **Verdict:**
  - **Quick-win:** **whisper.cpp local** для voice-pipeline — убирает Groq из HIGH-data-пути. Реалистично в **Build**. Это конкретное исполнение «собственного вычисления» для самого чувствительного потока (личный голос).
  - **Hybrid forever (честно):** frontier-качество (Claude) для high-stakes синтеза + **локальная маленькая модель (Ollama) для low-stakes/приватных подзадач** (классификация, redaction, дедуп) где данные не должны уходить. Полная замена Claude = **Scale + GPU-капитал**, не обещать раньше.
  - **«Свои обученные агенты»** = fine-tune локальной модели на Jetix-методах — Scale-горизонт, после revenue.

### (5) Google Workspace / Gmail → Nextcloud + (НЕ self-host email)

| Что | Альтернатива | Verdict |
|---|---|---|
| Files/Drive | **Nextcloud** (Docker; files+calendar+contacts+OnlyOffice) | разумно; storage-hungry; Run-стадия |
| Calendar/Contacts | Nextcloud (CalDAV/CardDAV) | покрывает + частично Calendly |
| **Email** | Mailcow/Mailu (self-host) | ❌ **НЕ рекомендуется** — deliverability/spam/DKIM/IP-reputation = ops-кошмар + риск недоставки бизнес-почты |
| Email (sovereignty без боли) | **Proton / Mailbox.org / Tuta** | ✅ privacy-провайдер, E2E, EU-юрисдикция (GDPR), без ops-нагрузки |

- **Verdict:** Nextcloud для файлов/календаря (**Run**); email = **НЕ self-host**, перейти на Proton/Mailbox.org (sovereignty есть, ops-боли нет). Это R12-honest tradeoff: суверенитет email не стоит риска потерять бизнес-письмо.

### (6) Stripe → BTCPay Server (+ keep fiat)

- **BTCPay Server:** self-host, non-custodial crypto-платежи, без комиссий, censorship-resistant. Резонирует с Phase 3 (кошельки) + Mondragón/QF on-chain payouts.
- **Но:** обычные B2B-клиенты платят фиатом → fiat-процессор (Stripe/etc.) всё равно нужен.
- **Verdict:** **Hybrid, Scale-стадия.** BTCPay для crypto/treasury/event-payouts (хакатоны #16); fiat-процессор для обычных продаж. Не Build.

### (7) Calendly → Cal.com

- Cal.com: open-source, self-host (Docker, Next.js+Postgres), хороший паритет.
- **$** низ · **⏱** низ-сред · **Δquality** 0 · **🔒Δ** низкий (календарь — не самые чувствительные данные).
- **Verdict:** опционально. Можно self-host (**Run**) или просто использовать Cal.com cloud (open-source компания) сейчас. Низкий приоритет.

### (8) CRM → (уже суверенен!)

- Jetix CRM = **markdown в `crm/`, filesystem = source of truth, Python CLI**. Это **уже self-hosted и grep-friendly**. SuiteCRM/Mautic/EspoCRM = **шаг назад** (тяжелее, менее прозрачно).
- **Verdict:** **миграция НЕ нужна.** Действие: держать чувствительные personal-data вне Notion-view + шифровать at-rest (Phase 3). CRM — образец того, как должна выглядеть остальная сувереность.

### (Bonus) Password manager + Secrets

- **Vaultwarden** (легковесный Bitwarden-совместимый сервер, Rust) — self-host менеджер паролей на VPS. Или Bitwarden cloud (E2E, дёшево).
- **Secrets для системы:** `sops` + `age` (зашифрованные секреты в git) или HashiCorp Vault (тяжелее). Закрывает A1 (key-leak) системно.
- **Verdict:** **Build quick-win** — Vaultwarden (или Bitwarden cloud) + sops/age для секретов.

## §2.2 Master tradeoff-таблица

| Инструмент | Self-hosted | $ | ⏱ | Δqual | 🔒Δ | Стадия | Приоритет |
|---|---|---|---|---|---|---|---|
| Voice (Groq Whisper) | **whisper.cpp local** | низ | низ-сред | −1 | **выс** | Build | **P0** |
| Secrets/passwords | **Vaultwarden + sops/age** | низ | низ | 0 | **выс** | Build | **P0** |
| GitHub | **Forgejo** + GitHub mirror | низ | низ | 0 | выс | Build | **P1** |
| Sensitive 1:1 | **Signal** (zero-infra) | 0 | 0 | −1 | выс | Build | **P1** |
| Email | **Proton/Mailbox.org** (НЕ self-host) | низ | низ | 0 | сред | Build | P1 |
| Cohort comms | **Matrix/Conduit** | сред | сред | −1 | выс | Run | P2 |
| Files/calendar | **Nextcloud** | сред | сред | 0 | сред | Run | P2 |
| Calendly | **Cal.com** | низ | низ-сред | 0 | низ | Run | P3 |
| Notion | AppFlowy/Anytype/Outline | низ-сред | сред | −1 | сред | Run+ | P3 |
| Claude (low-stakes) | **Ollama** (hybrid) | сред | сред | −2 | выс | Run+ | P2 |
| Stripe | **BTCPay** (+ fiat) | сред | сред | 0 | сред | Scale | P3 |
| Claude (full) / агенты | local GPU + fine-tune | **выс** | выс | −2..−3 | выс | Scale | P3 |
| CRM | — уже суверенен | 0 | 0 | 0 | — | done | — |

## §2.3 Migration roadmap (dependency chain)

```
ПОРЯДОК (что first → что depends на чём):

  [0] PREREQ: Docker/Podman + Caddy + Tailscale-only + Restic backup   ← всё зависит от этого
       │
       ├─[Build P0] whisper.cpp local   (убрать Groq из voice-пути)     ← независимо
       ├─[Build P0] Vaultwarden + sops/age (закрыть key-leak A1)        ← независимо
       ├─[Build P1] Forgejo + GitHub-mirror  (требует [0] backup!)
       ├─[Build P1] Signal для sensitive 1:1 (zero-infra, сейчас)
       └─[Build P1] Email → Proton/Mailbox.org (не self-host)
              │
       [Run P2] Matrix/Conduit (cohort) ──── требует [0] + стабильный backup
       [Run P2] Nextcloud (files) ────────── требует [0] + storage-план (Phase 4)
       [Run P2] Ollama hybrid (low-stakes LLM) ── требует [0]; GPU опц.
              │
       [Scale P3] BTCPay / local-GPU LLM / fine-tune агенты ── требует капитала + revenue
```

**Принцип последовательности:** сначала **закрыть утечки дёшево** (whisper.cpp, Vaultwarden, Signal, Proton — почти бесплатно, высокий 🔒Δ), потом **добавить суверенитет** (Forgejo, Matrix, Nextcloud — требуют инфра-слоя), и только на Scale — **дорогой compute-суверенитет** (GPU, BTCPay). O-194 «собственное вычисление» материализуется поэтапно: whisper.cpp (Build) → Ollama-hybrid (Run) → GPU+fine-tune (Scale).

## §2.4 R1 reservation

Все verdict'ы выше = **surface**. Что именно и когда разворачивать — решение Руслана (capital + time tradeoff vs foundation-first). Особенно O-194 infra-sovereignty vs pre-revenue (Q14-2) = открытый стратегический вопрос, не решён агентом.

---

*Phase 2 закрыт. R-criterion `no_self_hosted_alternatives` — снят. 8 инструментов + bonus, master tradeoff-таблица, dependency-chain roadmap. Ключевой honest-вывод: Jetix уже суверенен (fs=source); задача = сократить утечки + убрать SPOF, а не мигрировать всё. Дальше: Phase 3 wallets + data sovereignty.*
