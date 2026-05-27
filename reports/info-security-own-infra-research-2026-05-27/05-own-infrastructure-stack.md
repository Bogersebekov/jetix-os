---
title: "Phase 4 — Own infrastructure stack (compute / network / storage / monitoring)"
date: 2026-05-27
phase: 4
parent_prompt: prompts/info-security-own-infra-research-2026-05-27.md
F: F3 (synthesis от self-host infra canon + grounded jetix-vps reality)
G: prompt-info-security-own-infra-research-2026-05-27
R: refuted_if_no_roadmap_per_stage (infra branch)
constitutional_posture: R1 surface only + R11 + append-only
language: russian
status: draft (phase report)
---

# Phase 4 — Own infrastructure stack

> **Honest принцип фазы:** первый шаг масштабирования инфры — **НЕ кластеризация**, а
> **резервирование + бэкап**. Один VPS, который умрёт без offsite-копии, опаснее, чем
> отсутствие кластера. Сначала «один box не должен убивать всю систему», потом рост.

## §4.0 Current state (grounded на jetix-vps)

| Слой | Сейчас | Оценка |
|---|---|---|
| **Compute** | 1× Hetzner CPX32 (4 vCPU / 7.6 GB / 150 GB; занято 17 %) | **SPOF**; запас по диску есть |
| **Network** | Tailscale (control-plane у Tailscale Inc.) | работает; не суверенный control-plane |
| **Storage** | локальный диск VPS; **offsite-бэкап не найден** | **критичный gap (Risk 15)** |
| **Reverse-proxy/TLS** | (нет Docker → вероятно прямой/nginx) | нужен слой для self-host |
| **Monitoring** | `shared/state/system-health.json` (Part 8 stub, не live) | live-метрики = Phase B Part 8 |
| **DNS** | (домен есть; провайдер?) | проверить |
| **Containerization** | **нет Docker** | gating для всего self-host |

## §4.1 Compute scaling (4 опции)

| Опция | Что | $ | Плюсы | Минусы | Стадия |
|---|---|---|---|---|---|
| **A. Vertical (bigger Hetzner)** | CPX42/51 или dedicated CCX | сред | просто; меньше ops | всё ещё SPOF | Build→Run |
| **B. Horizontal (2-3 Hetzner)** | app + db + backup на разных box | сред-выс | redundancy; роли разделены | оркестрация (Compose→Nomad/k3s) | Run |
| **C. Edge nodes (участники хостят части)** | cohort/clan-члены держат узлы | низ $ (чужое железо) | **резонирует с mesh-кланы + Mondragón distributed** | гетерогенность, trust, availability | Scale |
| **D. Bare metal (own hardware / colo)** | свой сервер дома или в colo | капекс | максимум суверенитета; GPU для LLM | физ-ops, питание, аплинк | Scale |

- **Honest порядок:** Build = остаться на 1 VPS, но **добавить backup + 2-й дешёвый box под бэкап/standby**. Run = разнести роли (app / Postgres / monitoring) на 2-3 box, оркестрация **k3s** (лёгкий Kubernetes) или **Nomad** (проще k8s) или просто Compose+Caddy если хватает. Scale = dedicated/own-hardware (для GPU-LLM из Phase 2/3) + edge-узлы участников.
- **Edge nodes = стратегически интересно:** если члены кланов хостят части инфры, то **инфраструктура принадлежит сети, а не центру** — это и техническая, и R12-реализация «качалка/склад, не контролёр» (metaplan §4) + Mondragón distributed ownership. Но операционно сложно (heterogeneous uptime/trust) → Scale, не раньше.

## §4.2 Network — Tailscale → Headscale / WireGuard / Yggdrasil

| Опция | Что | Суверенитет | Verdict |
|---|---|---|---|
| **Tailscale (текущий)** | WireGuard + managed control-plane (Tailscale Inc.) | control-plane НЕ свой; данные E2E, но coordination видит топологию | ✅ Build (отлично работает) |
| **Headscale** | open-source self-hosted control-plane для Tailscale-клиентов | **свой control-plane** = полный суверенитет coordination | ✅ Run (sovereignty-апгрейд, drop-in) |
| **WireGuard (прямой)** | ручной mesh без coordination | максимум контроля | ручное управление ключами/пирами — не масштабируется |
| **Yggdrasil / Nebula** | альтернативные mesh-overlay | экзотика/нишево | специальные кейсы |

- **Verdict:** Tailscale **сейчас** (Build — закрыть SSH/админки за VPN, не торчать наружу). **Headscale** на Run — забрать control-plane себе (миграция почти drop-in, те же клиенты). Это конкретный «суверенитет сети» без боли ручного WireGuard.
- **Security-win уже сейчас:** все админ-порты (SSH:22, БД, monitoring, self-host-админки) — **только через Tailscale**, ноль публично. Публично торчит только 443 (reverse-proxy). Это резко сокращает attack-surface (закрывает большую часть A3).

## §4.3 Storage — local + offsite encrypted + (distributed)

| Слой | Опция | Заметка |
|---|---|---|
| Primary | локальный NVMe VPS | source of truth (fs) |
| Object | **MinIO** (self-host S3) или Hetzner Storage Box / Backblaze B2 | для бэкапов + будущих app-ассетов |
| Offsite encrypted | **Restic → B2/Storage Box** | 3-2-1 (см. Phase 3 §3.6) |
| Distributed (Scale) | члены держат реплики (IPFS/Garage/SeaweedFS) | Mondragón distributed; резонирует с edge-nodes §4.1-C |

- **Build:** Restic → Backblaze B2 (или Hetzner Storage Box, дёшево, в той же экосистеме). Зашифровано. Restore-тест.
- **Scale:** distributed storage (Garage/SeaweedFS/IPFS) поверх edge-узлов = данные сети живут в сети. Но: согласованность + приватность (шифрование per-shard) сложны → не раньше Scale.

## §4.4 Backup (cross-ref Phase 3)

Restic/Borg → encrypted offsite, 3-2-1, restore-тест. **Это P0 Build** (закрывает Risk 15). Детали — Phase 3 §3.6. Ключевой инвариант: **backup до self-host-сервисов** (Default-Deny: нет бэкапа → нет нового stateful-сервиса).

## §4.5 Monitoring — Prometheus + Grafana + Loki (= материализация Part 8!)

**Это красивая связка с Foundation.** Part 8 уже **специфицировал WHAT измерять** (health-signals, SLI/SLO schema, alert-routing Tier 0-3, Halt-Log-Alert) но явно **отложил live-метрики на Phase B** [src:part-8 §0 «NOT delivered: live metric collection code… Phase B»]. Self-hosted monitoring-стек = **именно эта Phase B материализация**:

| Компонент | Роль | Маппинг на Part 8 |
|---|---|---|
| **Prometheus** | сбор метрик (time-series) | live-collection для SLI §I.2 (Part 8 stub → реальные числа) |
| **Grafana** | дашборды | weekly health dashboard §I.4 (визуализация) |
| **Loki** | логи | alert-log.jsonl §C + Tier 3 silent-log |
| **Alertmanager** | роутинг алертов | §H.1 alert-routing stub → реальная доставка (но через Part 6b gate, не напрямую — L-8!) |
| **node_exporter / cAdvisor** | системные/контейнерные метрики | Four Golden Signals §B (latency/traffic/errors/saturation) |

- **Дисциплина (Part 8 L-8 + L-1):** monitoring **наблюдает**, не энфорсит. Alertmanager НЕ авто-доставляет напрямую в Slack/SMS (это запрещено Part 8 §F.2 + L-6/D-6) — алерт идёт через Part 6b enforcement-arm + owner override (corrigibility). То есть self-host monitoring уважает уже-LOCKED архитектуру.
- **Когда:** **Run** (когда есть что мониторить за пределами одного box). На Build — простой uptime-чек (healthchecks.io / Uptime-Kuma self-host) достаточно.
- **Security-метрики тоже сюда:** failed-SSH, fail2ban-bans, cert-expiry, backup-success/age, gitleaks-hits → SLI безопасности в том же стеке.

## §4.6 DNS — own vs Cloudflare

| Опция | Плюсы | Минусы |
|---|---|---|
| **Cloudflare proxy** | DDoS-защита, CDN, простота, бесплатно | видит весь трафик; централизация; зависимость |
| **Own/registrar DNS** (без proxy) | суверенитет, никто не видит трафик | теряешь DDoS-защиту; сам управляешь |
| **Hybrid** | Cloudflare для публичного (DDoS) + sensitive за Tailscale (вообще не в DNS) | баланс |

- **Verdict:** **Hybrid.** Чувствительные сервисы — **не в публичном DNS вообще** (только Tailscale-имена). Публичный лендинг/сайт — можно за Cloudflare (DDoS-защита реально полезна), осознавая, что CF видит трафик. На Scale (если нужен полный суверенитет) — own authoritative DNS + anycast/DDoS-партнёр. Домен — у privacy-aware регистратора (не у того, кто легко отдаёт по запросу).

## §4.7 Reverse-proxy / TLS / Hardening (базовый слой)

- **Caddy** (авто-TLS из коробки, простой) или **Traefik** (k8s-native). Один публичный порт 443.
- **Hardening VPS:** `ufw`/nftables (deny-by-default, только Tailscale + 443), fail2ban, unattended-upgrades (авто security-патчи), SSH ключ-only + Tailscale-only, отключить root-login, CrowdSec (community-driven IPS) опционально.
- **Container-security:** Podman rootless вместо Docker-root где можно; образы только из доверенных источников; Trivy-скан образов на CVE.

## §4.8 Cost projection per Build / Run / Scale

| Стадия | Compute | Storage/Backup | Network | Monitoring | **Итого/мес (порядок)** |
|---|---|---|---|---|---|
| **Build (solo)** | 1× CPX32 (~€15) + опц. 2-й мелкий backup-box (~€5) | B2/Storage Box (~€5) | Tailscale free | Uptime-Kuma (self, ~0) | **~€20-30/мес** |
| **Run (когорта 5-50)** | 2-3 box или CCX (~€60-120) | больше storage (~€15-30) | Headscale (self, ~0) | Prometheus/Grafana (self, compute-included) | **~€80-180/мес** |
| **Scale (100-1000+)** | dedicated + GPU (LLM) + edge-узлы; капекс или €500-2000+/мес | distributed (edge) + большой offsite | own DNS + DDoS-партнёр | full observability + security SLI | **€500-2000+/мес или капекс** |

- **Honest tradeoff (Q14-2):** Build-стоимость безопасности/суверенитета **тривиальна** (~€20-30/мес — почти всё софт-OSS на существующем железе). Дорого только на Scale (GPU для own-compute O-194, dedicated, distributed). То есть «foundation-first» и «security сейчас» **не конфликтуют** на Build — конфликт только если пытаться сразу строить Scale-инфру (own LLM-compute) на pre-revenue. **Вывод: делать дешёвую Build-безопасность сейчас, дорогой суверенитет — после revenue.**

## §4.9 Целевая архитектура (словесно; диаграмма SEC-3 в Phase 7)

```
                 Internet
                    │ :443 only
              ┌─────▼─────┐
              │  Caddy    │  (auto-TLS, reverse-proxy)
              │ (public)  │
              └─────┬─────┘
   ════════════ Tailscale/Headscale overlay (всё админ — только здесь) ═══════
        │              │               │              │
   ┌────▼───┐    ┌─────▼────┐    ┌─────▼─────┐   ┌────▼─────┐
   │ App/   │    │ Forgejo  │    │ Postgres  │   │ Monitoring│
   │ Jetix  │    │ (git)    │    │ (если app)│   │ Prom+Graf │
   │ swarm  │    │          │    │ encrypted │   │ +Loki     │
   └────┬───┘    └──────────┘    └───────────┘   └───────────┘
        │ low-stakes → Ollama (local) ; high-stakes → Claude API (hybrid)
        │ voice → whisper.cpp (local)
        ▼
   ┌──────────────┐        ┌────────────────────┐
   │ Restic backup│──────▶ │ Offsite encrypted   │ (B2 / Storage Box) + private GitHub mirror
   │ (3-2-1)      │        │ + offline copy дома │
   └──────────────┘        └────────────────────┘
```

## §4.10 R1 reservation

Какую опцию compute/network/storage и когда — **решение Руслана** (capital vs foundation-first). Surface only. Edge-nodes/distributed = Scale-горизонт, требует ack.

---

*Phase 4 закрыт. Compute (4 опции) / network (Tailscale→Headscale) / storage / monitoring (= материализация отложенного Part 8 Phase B!) / DNS / hardening / cost per stage. Главный honest-вывод: Build-безопасность ~€20-30/мес (тривиально, не конфликтует с foundation-first); дорогой суверенитет (GPU/dedicated/distributed) = Scale после revenue. Дальше: Phase 5 roadmap per stage.*
