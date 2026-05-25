---
title: AWAITING-APPROVAL — Notion Build Prerequisites (RUSLAN-ACKED VARIANT A, awaiting SSH setup)
date: 2026-05-25
type: prereq-gate-acked-pending-setup
status: PREREQS-PASSED-BUILD-PROCEEDING (Phase 0 cleared 2026-05-25; see reports/notion-build-2026-05-25/00-prereqs-passed.md)
gate_class: stop_gate
packet_id: notion-build-prereqs-2026-05-25
authored_by: brigadier-scribe (build-engineer mode, server CC) + Cloud Cowork update
prose_authored_by: ai-draft (surface-only — R1 build log, не strategic prose)
parent_prompt: prompts/notion-build-templates-dashboard-on-server-2026-05-25.md
parent_spec: decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md
blast_radius: Medium-High (external service writes — Notion API) — gated, NOT executed
action_class: notion_api_writes_workspace_buildout
F: F2
G: prereq-gate-acked-pending-setup
R: refuted_if_writes_executed_before_prereqs_met
ack_required: true
ack_owner: ruslan
ruslan_ack_received: 2026-05-25 evening "вариант А ок давай ебаш"
ruslan_ack_method: chat
constitutional_posture: R11 NOVEL ACTION CLASS gated → ACKED + R2 STRICT + Default-Deny + ZERO-DATA-MIGRATION (§0) preserved
recommendation: COMPLETE-SSH-SETUP-THEN-RELAUNCH (Ruslan responsible for env vars on server)
prereq_summary:
  r11_action_class_registered: YES (commit b2f10ad — .claude/config/default-deny-table.yaml updated)
  ruslan_acked_variant_a: YES
  notion_integration_created: YES (Ruslan confirmed — token shared in chat)
  notion_parent_page_created: PARTIAL (Ruslan provided URL https://www.notion.so/Jetix-OS-36b2496333bf8033b860c9e7adbde920 — name "Jetix OS"; STERILE SHELL VERIFICATION REQUIRED — page must be empty new page, NOT existing Ruslan workspace)
  parent_page_id_extracted: 36b2496333bf8033b860c9e7adbde920 (32 hex chars ✓)
  notion_api_token_env: SET (sourced from ~/.bashrc; prefix ntn_; never written to repo)
  notion_jetix_parent_page_id_env: SET (36b2496333bf8033b860c9e7adbde920; 32 hex ✓)
  notion_client_package: INSTALLED (v3.1.0)
  notion_arch_v2_spec: PRESENT
  sterility_verified: STERILE (parent page "Jetix OS" has 1 empty paragraph only; zero real content; ID ≠ any real Ruslan page) — Phase 0 PASS
  token_security_advisory: TOKEN_LEAKED_IN_CHAT_HISTORY — Ruslan must revoke + create new integration AFTER build completes (carried to Phase 13 next-steps)
result: PREREQS PASSED — sterility confirmed — build proceeding Phase 1→13
---

# 🛑 Notion Build — Phase 0 STOP: prerequisites NOT met

> **Phase 0 gate per `prompts/notion-build-templates-dashboard-on-server-2026-05-25.md` §0.5.**
> Result: **STOP**. Зафиксировано **ноль** write-операций в Notion. Ноль чтения
> существующей системы Ruslan (§0 ABSOLUTE HARD CONSTRAINT соблюдён — integration
> token отсутствует, доступа к Notion в принципе нет).

---

## §1 TL;DR

Run не стартовал, потому что не настроены 3 из 4 hard-prereqs. Главный блокер —
**нет integration token + parent page ID** в env vars сервера. Без токена CC
физически не может подключиться к Notion API → ни одного запроса не отправлено.

**Что нужно от Ruslan (≈10 минут в Notion UI + 3 команды на сервере), потом re-launch.**

---

## §2 Чек-лист prerequisites — текущее состояние

| # | Prerequisite | Статус | Блокер? |
|---|---|---|---|
| 1 | `NOTION_API_TOKEN` env var (integration token `secret_…`) | ❌ NOT SET | **HARD** |
| 2 | `NOTION_JETIX_PARENT_PAGE_ID` env var (32-char hex) | ❌ NOT SET | **HARD** |
| 3 | `notion-client` Python package installed | ❌ NOT INSTALLED | SOFT (можно поставить при re-launch) |
| 4 | notion-arch-v2 spec finished | ✅ PRESENT | — |
| 5 | R11 action class `notion_api_writes_workspace_buildout` зарегистрирован в `.claude/config/default-deny-table.yaml` | ❌ NO | **GATE** (см. §4) |

**Detail по #4 (✅ готово — единственный пройденный):**
- `decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md` — 1328 строк
- `decisions/strategic/AI-TOOLS-LIFEHACKS-MEGA-PAGE-2026-05-25.md` — 241 строка
- `reports/notion-templates-3-layers-architecture-v2-2026-05-25/` — все 13 reports + diagrams/
  (включая `03-layer-1-personal-core-revised.md` 50K / `04-layer-2…` 51K / `05-layer-3…` 45K)

Спека готова полностью — как только prereqs 1-3 + gate #5 закрыты, build стартует без задержек.

---

## §3 Что Ruslan делает — пошагово

### Шаг A — Notion Integration (в Notion UI, ≈5 мин)

1. **Notion Settings → Integrations → New integration**
2. Name: `Jetix Builder` · Type: **Internal integration**
3. Capabilities: ✅ Read content · ✅ Update content · ✅ Insert content · ✅ Read user information (without email)
4. Скопировать **Internal Integration Token** (`secret_…` / в новом UI `ntn_…`)

### Шаг B — Parent page (в Notion UI, ≈2 мин)

5. Создать **новую** пустую страницу name `🚀 Jetix Workspace`
   — ⚠️ **отдельную**, НЕ внутри Command Center / Daily Log / любой рабочей системы.
   Это стерильная песочница для шаблонов (см. §5 — почему критично).
6. На странице: `••• (top-right) → Connections → Connect to → Jetix Builder`
   — это даёт integration доступ **только** к этой странице и её детям. Больше никуда.
7. Скопировать **Page ID** из URL: последний кусок без дефисов, 32 hex-символа
   (`notion.so/Jetix-Workspace-`**`<32 hex>`**`?...` → копировать `<32 hex>`)

### Шаг C — На сервере (3 команды, ≈2 мин)

```bash
ssh jetix
export NOTION_API_TOKEN="secret_xxxxxxxxxx…"          # из Шага A
export NOTION_JETIX_PARENT_PAGE_ID="0123456789abcdef0123456789abcdef"  # из Шага B (32 hex)
pip install --user notion-client                       # prereq #3

# verify (token не печатаем целиком):
echo "token prefix: $(echo $NOTION_API_TOKEN | head -c 7)…"
echo "parent id len: ${#NOTION_JETIX_PARENT_PAGE_ID} (нужно 32)"
pip show notion-client | head -2
```

> ⚠️ **env var ONLY.** Токен НИКОГДА не пишем в файл / commit / лог
> (CLAUDE.md §4.2 + Global Rule 6 + Pillar C Tier 2 Rule 6). Не добавляй `export`
> в git-tracked файл. Если хочешь persistence между сессиями — положи в `~/.bashrc`
> или `~/.profile` (вне репо), не в `jetix-os/`.

### Шаг D — Re-launch

```bash
cd ~/jetix-os && git pull --ff-only
tmux new -s notion-build
claude --dangerously-skip-permissions -p "Autonomous execution: prompts/notion-build-templates-dashboard-on-server-2026-05-25.md … (см. §7 LAUNCH в prompt'е)"
# Ctrl-B затем D — detach
```

Phase 0 при re-launch перепроверит token + parent page accessibility + write-permission
(throwaway block create+delete) → при PASS пойдёт дальше до Phase 13.

---

## §4 GATE: R11 novel action class — требует ack

Per Pillar C Tier 2 **Rule 11 (Default-Deny novel actions)**: первая массовая
Notion API write-операция = новый action class, требует классификации в
`.claude/config/default-deny-table.yaml` **до** запуска. Я НЕ записал её сам —
запись в `.claude/config/` = Foundation-level path (Tier 2 Rule 2), требует твоего ack.

**Предлагаемая запись (на твой ack):**

```yaml
notion_api_writes_workspace_buildout:
  description: "Massive create/update operations on external Notion workspace
    via scoped integration token (parent-page-bounded). Templates/dashboard buildout."
  blast_radius: medium-high          # external service writes, НЕ Foundation
  default: deny
  allow_when:
    - integration_token_scoped_to_single_parent_page: true   # §0 sterile-shell invariant
    - ruslan_ack_packet: notion-build-prereqs-2026-05-25
    - idempotent_design: true        # re-run safe (existence-check by name+parent)
    - markdown_mirror_parallel: true # filesystem = source of truth
    - zero_existing_data_read: true  # НЕ читать/migrate/link существующую систему
  halt_on:
    - read_attempt_outside_parent_page    # → HALT-LOG-ALERT F4 ≤5s + STOP
    - sample_real_data_populate            # только placeholder text
    - api_token_written_to_file_or_commit
```

**Варианты ack:**
- **(A)** «Добавь запись + погнали» — при re-launch CC сначала добавит её в yaml (gated commit `[notion-build] register R11 action class`), затем стартует build.
- **(B)** «Сначала покажи только yaml-запись, без build» — добавлю запись, остановлюсь, ты проверяешь.
- **(C)** правки к классификации.

---

## §5 Почему §0 sterile-shell критичен (напоминание)

Ты уже используешь свою Notion-систему для реальной ежедневной работы (Daily Log /
Projects / CRM-views / Банк идей / Life OS). Этот build = шаблоны для будущих
fork'ов (партнёры / cohort / другие бизнесы) — **отдельный** workspace.

- Integration подключается **только** к `🚀 Jetix Workspace` (Шаг B.6) → токен
  физически не видит остальное. Это и есть техническая гарантия §0.
- НЕ подключай integration к Command Center или любой рабочей странице.
- Любая попытка прочитать что-то вне parent page вернёт Notion API error →
  CC делает HALT-LOG-ALERT F4 ≤5s + STOP.

**Sterile = fork-friendly. Любая утечка реальных данных = brokenness.**

---

## §6 Что НЕ сделано (явно, fail-loud)

- ❌ Ни одного Notion API запроса (нет токена).
- ❌ Не создан `tools/notion_builder/` модуль (Phase 1 не достигнут).
- ❌ Не создан `reports/notion-build-2026-05-25/` (кроме отсутствия — это ожидаемо до старта).
- ❌ `notion-client` НЕ установлен автономно (per Global Rule «не ставить пакеты без
  одобрения» + run всё равно блокирован отсутствием токена → установка преждевременна).
  Поставится при re-launch (Шаг C) или Phase 0 авто-установит после ack варианта A.
- ✅ Соблюдён §0: ноль чтения/линковки/миграции существующей системы Ruslan.

---

## §7 Next action (Ruslan)

1. Шаги A-C (≈10 мин).
2. Ack §4 gate (вариант A / B / C).
3. Re-launch (Шаг D).

После этого — автономный прогон 6-10h до готового workspace + main report
`decisions/strategic/NOTION-BUILD-REPORT-2026-05-25.md`.

---

*Phase 0 STOP packet. Zero writes. Prereqs 1-3 + gate #5 pending Ruslan. Spec (#4) ready.
Re-launch после setup. Default-Deny соблюдён. §0 sterile-shell INVARIANT соблюдён.*
