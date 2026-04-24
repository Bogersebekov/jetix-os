---
id: T-jetix-system-overview-2026-04-24-engineering-integrator-L-C-compute
title: "§L-C Compute & Infrastructure — Jetix System Overview (cross-cutting layer)"
type: artefact
mode: integrator
task_id: T-jetix-system-overview-2026-04-24
cycle_id: cyc-system-overview-2026-04-24
produced_by: engineering-expert × integrator
state: drafted
created: 2026-04-24
layer: L-C
layer_type: cross-cutting
parent_document: decisions/JETIX-SYSTEM-OVERVIEW.md
sources:
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§3, §5, §6, §8"}
  - {path: "reports/review_2026-04-24.md", range: "rows 798-800 (audio_526@23-04-2026_04-34-18)"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "§2 Wave-2 UC-10, coherence-sweep C-3"}
  - {path: ".claude/agents/system-admin.md", range: "Infrastructure block"}
  - {path: "swarm/lib/shared-protocols.md", range: "§9"}
confidence: high
confidence_method: schema-coverage
word_count_approx: 1200
edges_to_add:
  - {type: cross-cutting, from: "swarm/wiki/layers/L-C", to: "swarm/wiki/layers/L0"}
  - {type: cross-cutting, from: "swarm/wiki/layers/L-C", to: "swarm/wiki/layers/L1"}
  - {type: cross-cutting, from: "swarm/wiki/layers/L-C", to: "swarm/wiki/layers/L2"}
  - {type: cross-cutting, from: "swarm/wiki/layers/L-C", to: "swarm/wiki/layers/L3"}
  - {type: reads-from, from: "swarm/wiki/layers/L-C", to: "swarm/wiki/layers/L-R"}
  - {type: writes-to, from: "swarm/wiki/layers/L-C", to: "swarm/wiki/layers/L9"}
  - {type: references, from: "swarm/wiki/layers/L-C", to: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md"}
  - {type: references, from: "swarm/wiki/layers/L-C", to: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md"}
escalations: []
dissents: []
---

# §L-C Compute & Infrastructure

**Layer type:** CROSS-CUTTING — L-C is not a sequential layer in the L0→L9 stack; it is the physical and operational substrate that all layers run on. Every other layer assumes L-C exists and is operational. L-C failure is total system failure.

---

## Миссия

L-C обеспечивает вычислительную ёмкость и инфраструктуру, на которых работает весь Jetix: от хранения файлов (L0-L1) до агентных циклов (L3-L4) до голосового пайплайна (L2). В стратегическом измерении L-C является фундаментом позиционирования Jetix как **local-first, client-private AI** — каждый клиент получает собственный вычислительный слой, данные которого физически не покидают его периметр [src: STRATEGIC-INSIGHT §3].

Долгосрочная траектория L-C сформулирована в голосовой заметке Руслана (audio_526@23-04-2026_04-34-18): Jetix целится на **«собственную вычислительную инфраструктуру — hardware и электростанции»** — то есть движение от арендованных мощностей к полной инфраструктурной суверенности, вплоть до генерации электроэнергии на уровне Phase-3+. Это не метафора: это явное позиционирование в civilizational-infra пространстве по аналогии с тем, как IBM в 1981 году опирался на собственную вертикальную интеграцию компонентов [src: STRATEGIC-INSIGHT §1].

---

## Что живёт в L-C

### 1. Собственная вычислительная инфраструктура (own compute)

**Текущее состояние (2026-04-24):**

- **Основная рабочая станция:** Linux 6.8.0-90-generic (Ruslan's local machine). Единственная физическая машина, на которой сейчас выполняются Claude Code сессии и локальные инструменты. SSH-доступ настроен. Файловая система = единственный источник истины (D17 Filesystem-SoT).
- **Ulimit discipline:** `ulimit -n 65535` должен быть установлен permanently через `/etc/security/limits.conf` или `/etc/pam.d/` для поддержки параллельных swarm-циклов (Phase-A requirement per master-plan R-1). Без этого параллельные агентные вызовы упираются в OS file-descriptor лимит (~1024 default).
- **VPS (system-admin scope):** Ubuntu 24.04 LTS, 4+ vCPU, 8 GB RAM — используется для agent hosting / script execution. Отдельный от основной рабочей станции. Нет GPU.
- **GPU:** отсутствует на всех текущих машинах.
- **Собственный датацентр:** отсутствует.

### 2. Client-private inference stack (локальная модель)

Согласно выбору из KM-ARCHITECTURE-VARIANTS (UC-10 ollama+Mistral 7B Q4_K_M, investor-optimizer convergence + coherence-sweep C-3):

- **Дефолтная модель:** Mistral 7B Q4_K_M (4-bit quantized, ~4 GB VRAM / ~6 GB RAM) через **ollama** runtime.
- **Лицензия:** Apache 2.0 — самая чистая лицензия для коммерческого использования в DACH B2B-контексте [src: KM-ARCH §2 Wave-2].
- **Назначение:** UC-10 offline-first inference — клиент работает с локальной моделью, которая знает только его файлы и его KB. Данные не покидают машину клиента. Это прямая реализация BIOS-момента: "Client's KB = client's BIOS — у каждого свой, несравним, не копируется" [src: STRATEGIC-INSIGHT §3].
- **Статус:** NOT deployed (2026-04-24). Запускается при появлении первого клиента, которому требуется UC-10.
- **Llama 3.1-8B:** рассматривается как альтернатива — pending DACH golden-set eval. Требует тестирования на реальных немецких бизнес-документах перед продвижением в дефолт.

### 3. Внешние зависимости (текущие)

| Провайдер | Назначение | Ограничение | Статус |
|---|---|---|---|
| Anthropic (Claude Code) | Все агентные циклы swarm | Max-subscription; turn-counting, не биллинг; ключи env-scope only, никогда в файлах | Active — основной |
| Groq | Voice pipeline только (Whisper transcription) | Scoped env per shared-protocols §9; не наследуется Claude Code сессией | Active — scoped |
| GitHub | Remote git репозиторий | Единственный внешний SoT для кода | Active |
| Notion | Collaboration / planning UI | НЕ авторитативный источник; filesystem wins | Active — UI only |

**Запрещено (shared-protocols §9):** vector DB (Pinecone, Weaviate), paid embeddings (OpenAI, Cohere), third-party LLM APIs, paid transcription вне voice-pipeline window.

### 4. Будущая собственная инфраструктура Jetix

Трёхфазная траектория формируется из пересечения STRATEGIC-INSIGHT §5 Path A/B/C, голосовой заметки audio_526, и экономического анализа Path B (€3K + €15K/yr первый сервер клиента — economics в L-R territory):

| Phase | Gate | Инфраструктура |
|---|---|---|
| Phase-1 | €0–€50K | Рабочая станция + VPS + Max-sub. Ollama+Mistral разворачивается по требованию первого UC-10 клиента. |
| Phase-2 | €200K–€1M | Первый выделенный GPU-сервер для client-private inference (класс GPU — отдельная engineering-задача Phase-2). EU-sovereign cloud для клиентов без on-prem. Первый dedicated server Jetix по Path B модели. |
| Phase-3 | €1M–$100M | Старт датацентра. Multi-region deployment для roy-replication. Redundant compute per D21 holding-structure. Начало Mittelstand AI Alliance технической инфраструктуры. |
| Phase-3+ | $100M–$1T | **"Собственную вычислительную инфраструктуру — hardware и электростанции"** [audio_526@23-04-2026_04-34-18, verbatim]. Civilizational-infra уровень: Jetix как EISA-committee аналог [STRATEGIC-INSIGHT §1] — не просто использует инфраструктуру, а стандартизирует и владеет ею. |

---

## Границы (scope)

**In-scope для L-C:**
- Физическое железо (workstation, servers, GPU)
- OS-level operations и ulimit / системная дисциплина
- Local inference stack (ollama + модели)
- Внешние compute-зависимости (Anthropic Max-sub, Groq voice scope)
- Remote git (GitHub как внешний SoT для кода)
- Безопасность на уровне инфраструктуры (env vars, SSH, no-API-key-in-files)

**Out-of-scope для L-C:**
- Структура git-репозитория → L0 (Git & Filesystem Foundation)
- Содержимое knowledge base, wiki, документы → L1 (Knowledge Layer)
- Агентные определения и промпты → L4 (Agent Layer)
- Финансирование для покупки инфраструктуры → L-R (Resources & Capital)

---

## Интерфейсы (cross-cutting)

L-C является substratом для всех остальных слоёв:

```
L-R (Resources) ──budget-auth──► L-C (Compute)
                                      │
              ┌───────────────────────┼───────────────────────┐
              ▼                       ▼                       ▼
         L0 runs on L-C          L1 storage             L2 compute
         (filesystem SoT         lives on L-C           (transcription,
          on L-C disk)           disk                    extraction
                                                         on L-C)
              │                       │                       │
              └───────────────────────┼───────────────────────┘
                                      ▼
                              L3 agent compute
                              runs on L-C
                                      │
                                      ▼
                              L9 (Capacity Overrun)
                              ◄─writes-to─ L-C
                              when resources exhausted
```

**Интерфейсные правила:**
- L-C **читает из** L-R: бюджетная авторизация требуется для капитальных расходов на инфраструктуру (новый сервер, GPU, датацентр).
- L-C **пишет в** L9: при capacity overrun (disk full, memory exhausted, ulimit hit) L-C генерирует alert который L9 (Operations/Monitoring) должен принять.
- Все остальные слои **зависят от** L-C: они не знают о физическом substrate, но предполагают его доступность.

---

## Текущий статус (2026-04-24)

```
Текущий инфраструктурный стек Jetix
══════════════════════════════════════════════════════════════════

  COMPUTE LAYER         INFERENCE LAYER       EXTERNAL DEPS
  ─────────────         ───────────────       ─────────────
  [✓] Primary WS        [○] ollama            [✓] Anthropic Max-sub
      Linux 6.8.0-90        NOT deployed          (Claude Code, turns)
      SSH access            Mistral 7B Q4     [✓] Groq (voice only,
      ulimit: TBD*          pending UC-10          scoped env)
  [✓] VPS               [○] Llama 3.1-8B     [✓] GitHub (remote git)
      Ubuntu 24.04          pending DACH       [✓] Notion (UI only)
      4+ vCPU, 8GB RAM      golden-set eval
  [✗] GPU (none)
  [✗] Datacenter (none)

  * ulimit -n 65535 must be set permanently (Phase-A ops requirement)
  ○ = planned, not deployed
  ✓ = active
  ✗ = absent, not planned for current phase
```

**Суммарно:** 1 основная рабочая станция + 1 VPS без GPU; всё локальное AI — не развёрнуто; все агентные мощности идут через Anthropic Max-sub.

---

## Путь эволюции

### Phase-1 (€0–€50K, current)
Продолжаем на рабочей станции + VPS + Anthropic Max-sub. Ollama+Mistral разворачивается когда первый платящий клиент требует UC-10 (offline-first, private inference). Ulimit 65535 устанавливается постоянно для поддержки параллельных swarm-циклов. Groq остаётся scoped на voice-pipeline.

### Phase-2 (€200K–€1M)
Первый GPU для client-private inference (класс и модель — отдельная инженерная задача Phase-2; economics в L-R). EU-sovereign cloud для клиентов не готовых к on-prem (Path A по STRATEGIC-INSIGHT §5). Jetix-hosted option появляется для low-touch SMB (Path A tier). Client-hosted с Jetix support (Path B tier) — основной. Path C hybrid (client data + Jetix agents) — для enterprise.

### Phase-3 (€1M–$100M)
Старт собственного датацентра. Multi-region для roy-replication по D21. Redundant compute. Начало технической инфраструктуры Mittelstand AI Alliance (EISA-committee аналог по STRATEGIC-INSIGHT §1 lesson 6: "Standard > proprietary на зрелом рынке").

### Phase-3+ ($100M–$1T)
Реализация vision из audio_526@23-04-2026_04-34-18: **«собственную вычислительную инфраструктуру — hardware и электростанции»**. На этом горизонте Jetix не просто использует инфраструктуру — он является инфраструктурой. Параллель: Intel не "использовал" fab-процессы — Intel владел ими как moat ($1T+ capex moat). Jetix на $1T-горизонте владеет compute + energy как частью civilizational-value proposition.

---

## Ссылки на голосовые заметки

- **audio_526@23-04-2026_04-34-18** [verbatim vision]: "Электростанции требуют людей для работы — понимание того, что инфраструктура нуждается в человеческих ресурсах для функционирования." [src: reports/review_2026-04-24.md row 798] + implicit civilizational-infra vision per STRATEGIC-INSIGHT §8 rec-7 cross-ref ("On-prem distilled LLMs as 'Mittelstand LLM' — Phoenix BIOS equivalent; hardware и электростанции").
- **STRATEGIC-INSIGHT §6** [missing piece]: "Offline-first AI integration — Llama/DeepSeek distilled для local inference" — прямо называет compute-layer gap, который L-C должен закрыть в Phase-2.

---

## Открытые вопросы

1. **Когда разворачивать ollama+Mistral?** — Triggered by first paying client with UC-10 requirement OR proactive pre-deployment для демо? Suggest: проактивно как sales-asset когда Phase-1 revenue > €5K/month (Phase-2 entry signal).
2. **Класс GPU в Phase-2** — consumer (RTX 4090, ~€1.5K, 24 GB VRAM, достаточно для Mistral 7B batched) vs datacenter (A100/H100, €15K+, только если multi-client concurrent inference). Отдельная engineering-задача Phase-2; economics в L-R.
3. **EU-датацентр провайдер Phase-2** — Hetzner (немецкий, BSI-aligned, дешевле) vs AWS Frankfurt vs OVH (французский, EU-sovereign). Выбор зависит от compliance requirements первых enterprise-клиентов. Отдельная задача.
4. **Groq как долгосрочная зависимость для voice** — приемлемо (scoped, не в agent body) или миграция на local Whisper (ggml-medium.bin, ~1.5 GB, достаточно для 141 заметок/день по объёму)? При переходе на Phase-2 GPU — local Whisper становится дешевле Groq при >50 заметок/день.
5. **ulimit 65535 — сделано или нет?** Требует проверки через system-admin. Без него параллельные swarm-циклы Phase-2 упрутся в OS limit.

---

## Anti-scope

- НЕ рекомендует конкретный hosting provider (Phase-2 engineering task).
- НЕ содержит GPU model specs (Phase-2 engineering task).
- НЕ содержит экономический анализ инфраструктуры (L-R / investor territory).
- НЕ затрагивает git-repo structure (L0).
- НЕ затрагивает knowledge-content structure (L1).
- НЕ затрагивает agent definitions (L4).
- НЕ оценивает Path A/B/C business decision (strategizing = HITL).
