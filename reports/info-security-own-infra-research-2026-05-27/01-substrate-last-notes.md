---
title: "Phase 0 — Substrate read + last voice notes extraction (info-security + own-infra)"
date: 2026-05-27
phase: 0
parent_prompt: prompts/info-security-own-infra-research-2026-05-27.md
F: F2 (verbatim voice anchor) + F3 (synthesis)
G: prompt-info-security-own-infra-research-2026-05-27
R: refuted_if_no_last_notes_extracted
constitutional_posture: R1 surface only + R6 + R11 + R12 paired-frame + IP-1 + append-only
language: russian
status: draft (phase report — feeds Main consolidated Phase 7)
---

# Phase 0 — Substrate + извлечение последних заметок

## §0.1 Что прочитано (substrate read)

| Источник | Что взято | F-G-R |
|---|---|---|
| `wiki/concepts/jetix-security-privacy-pillar.md` (Tier A, promoted 27.05) | 4 тезиса pillar'а (O-192..195); структурный вопрос #17 OPEN; R12-positive якорь O-193 | F3·G:pillar·R-med |
| `wiki/ideas/vetted-network-data-mobility.md` (O-195) | trust-граф проверенных участников; данные мобильны но защищены | F3·G:idea·R-med |
| `decisions/strategic/VOICE-BATCH-14-INSIGHTS-2026-05-27.md` | verbatim Note 1+2; O-186..197; R12 paired-frame STRICT (O-197 CRITICAL) | F2+F3·R-med |
| `decisions/strategic/JETIX-METAPLAN-V4-FINAL-2026-05-26.md` | 16 directions; Кланы lifecycle; Mondragón 5:1; R12 fork-and-leave; QF; «качалка/склад» | F2-F3·R-med |
| `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` | Halt-Log-Alert (≤1s/≤5s/≤60s), Default-Deny, blast-radius Tier 0-3, fail-loud, corrigibility, observability-only | F5 LOCKED·R-high |
| `wiki/concepts/digital-sovereignty.md` | anti-lock-in; GDPR/NIS2/AI Act; «оставляем вам ваш стек под контролем» | F3·R-med |
| `wiki/ideas/b2g-ai-security-germany.md` | security research → B2B/B2G Германия (AI Act, NIS2); цикл 12-36 мес | F2·R-low |
| Tech-stack reality (grep `tools/` + машина `jetix-vps`) | фактический стек + железо (см. §0.2) | F4·R-high |
| Voice batches 11-13 (grep security/infra/семья) | подтверждение: security/privacy/infra — НОВОЕ в batch-14; «семья» = O-172→O-196/197 | F2·R-high |

## §0.2 Tech-stack reality (grounded — не предположение)

**Железо (замерено на `jetix-vps` 2026-05-27):**

- **Hetzner CPX-класс**: `nproc`=4 vCPU · RAM 7.6 GiB (used 2.2, free 4.5) · диск `/dev/sda1` 150 GB (занято 24 GB / 17 %, свободно 121 GB). Совпадает со спекой prompt'а (CPX32: 4 vCPU / 8 GB / 160 GB) [src:bash nproc/free/df on jetix-vps].
- **Tailscale установлен** (`/usr/bin/tailscale`) — VPN-overlay уже в проде.
- **Docker — НЕ установлен** (`which docker` → пусто). Критично для Phase 2/4: весь self-hosted стек предполагает Docker/compose → это **gating-зависимость #1**.
- **Ollama — НЕ установлен** (`which ollama` → пусто). Локальный LLM-инференс = greenfield. Плюс: 4 vCPU / 8 GB RAM **не тянут** серьёзный локальный LLM (нужен GPU или ≥32 GB RAM) → Phase 2 Claude→Ollama = долгий горизонт, не quick win.

**Внешние сервисы (по частоте ссылок в `tools/`):**

| Сервис | Роль | Refs | Чувствительность данных | $ |
|---|---|---|---|---|
| Anthropic Claude | основной AI (extract/filter/synth + этот CC) | 163 | **HIGH** — все транскрипты, KB, стратегия идут в API | платно (Max-подписка для CC) |
| Notion | KB-view / collaboration (не authoritative) | 155 | **HIGH** — Daily Log, Банк идей, CRM-view, проекты | freemium |
| Groq Whisper | voice → транскрипт | 46 | **HIGH** — все голосовые заметки Руслана | платно (API) |
| Telegram | messaging / voice-ingest | 15 | MEDIUM — переписка, голос | бесплатно |
| Matrix | (уже упомянут как альтернатива) | 15 | — | self-host |
| Tailscale | VPN overlay | 9 | LOW (control-plane у Tailscale Inc.) | freemium |
| Google Workspace / Gmail | минимально | 2 | MEDIUM | freemium |

**Главный вывод §0.2:** фактическая поверхность утечки сегодня = **3 внешних API с HIGH-данными** (Claude, Notion, Groq) + filesystem = source of truth локально на одном VPS без оффсайт-бэкапа (проверки бэкапа в репо не найдено → Phase 3/4 backup-gap). Это базовый threat-surface для Phase 1.

## §0.3 Извлечение последних заметок (last voice notes — batch-14 + cross-batch)

**Batch-14 (27.05.2026, audio_2026-05-27_01-55-37, Note 2) — security/privacy кластер.** Это **первичный источник** задачи. Полная verbatim — §0.4. Извлечённые идеи:

| ID | Тезис | Тип | R12 |
|---|---|---|---|
| **O-192** | Security-network pillar — «самая безопасная сеть в мире»; безопасность = differentiator | positioning | — |
| **O-193** | Data-confidentiality doctrine — no DB-selling; «не использовать против людей»; уважение к данным | doctrine | ✅ **R12-positive (anti-extraction)** |
| **O-194** | Infra-sovereignty roadmap — свои серверы / свои обученные агенты / собственное вычисление (own-or-partner) | roadmap | ⚠️ pre-revenue cost (Q14-2) |
| **O-195** | Vetted-network data mobility — данные между проверенными бизнесами; защита от атак и обесценивания | network | — |
| **O-196** | Aggregation-strength thesis — «в кучу → мощнее, сильнее» | community | ⚠️ |
| **O-197** | Family-cohort recruitment frame — «семья welcome / уважайте семью» + «перелопатим, снесём с пути» | recruitment | ⚠️ **R12 CRITICAL — POOL-LOCKED, не промоутить as-is** |

**Cross-batch генезис (важно для оценки новизны):**

- **Security/privacy/infra (O-192..195) = ГЕНУИННО НОВОЕ.** Grep по batch-11 (deep) и batch-12 (quick) — **ноль** упоминаний security/собственных серверов/инфраструктуры/конфиденциальности [src:grep reports/voice-batch-11*,12*]. То есть это не рефайнмент, а свежая ось.
- **«Семья/племя» (O-196/197) = ЭСКАЛАЦИЯ O-172.** O-172 (batch-13, audio_733 claims 10-11): «всё = информация… одна семья / одно племя возможна» — уже был FLAGGED как membership-totalizing rhetoric, R12 audit pending, DEFER к Stages 6-7 [src:reports/voice-batch-13-quick-2026-05-24/02-key-ideas-pool-candidates.md O-172]. В batch-14 этот frame **обострился** до «перелопатим/снесём» → статус ужесточён с «deferred audit» до «CRITICAL paired-frame, POOL-LOCKED».
- **B2G-Germany security (старый, 16.04)**: `wiki/ideas/b2g-ai-security-germany.md` — security как товар для немецкого Mittelstand/госсектора (AI Act, NIS2). Это **рыночное приложение** того, что в O-192 заявлено как принцип. Связка: pillar (O-192) = почему; b2g-germany = одна из монетизаций.

**Что это даёт для документа:** security/privacy — это два разных слоя, которые нельзя смешивать:
1. **Doctrine-слой (O-193, near-term)** — «как участники обращаются с данными» → идёт в Charter/правила/landing trust-copy. Дёшево, можно сейчас.
2. **Infra-слой (O-194, long-horizon)** — «свои серверы/агенты/вычисление» → дорого, gated pre-revenue (Q14-2). Не обещать как готовое.

## §0.4 Verbatim anchor (F2 — Ruslan voice, Note 2)

> «К документам добавить, что Jetix будет работать на собственной сети безопасности, самую безопасную в мире делать… по конфиденциальности информации — самую защищённую, без продаж каких-то баз данных… люди будут адекватно понимать, что конфиденциальность важна, ответственно относиться к данным… компании с уважением к информации, не продавать, не использовать против людей… в планах — собственные серверы, своих агентов тренировать, собственное вычисление… либо собственное иметь, либо партнёриться… чтобы данные могли адекватно передвигаться, с проверенными бизнесами сотрудничать, и были защищены против атак и обесценивания информации… мы в кучу собираемся и из-за этого мощнее, сильнее… в большой семье можем оформить мощные инструменты защиты, продвижения, разработки… любого перелопатим, снесём с пути… только кто понимает и хочет быть в безопасности, чтобы семья развивалась…»
> [src:decisions/strategic/VOICE-BATCH-14-INSIGHTS-2026-05-27.md §1 Note 2; raw/transcripts/audio_2026-05-27_01-55-37.txt]

**R1 reservation:** всё ниже (Phases 1-7) — surface/draft. Direction-status #17 (новое направление vs sub-pillar #2+#8 vs concept-only) — решает Руслан, не агент. Эта связка переносится в Main §R1-decisions queue.

## §0.5 Constitutional posture (как держим в этом исследовании)

- **R1 surface only** — рой выкладывает варианты + arithmetic; стратегические формулировки и выбор направления = Руслан. Все «рекомендуется» = surface, не решение.
- **R6** — знание персистится только через явные artefact-пути (эти 8 файлов + Main); не аккумулируем неструктурированную долгую память.
- **R11 Default-Deny** — любое новое действие классов «купить железо / развернуть сервис / мигрировать данные» = blast-radius категоризация + AWAITING-APPROVAL (см. Phase 5 gating).
- **R12 paired-frame STRICT** — security-маркетинг (Phase 6) проходит через influence-ethics auto-fire; «самая безопасная» = provable claim или security theater. O-197 «семья + снесём с пути» = POOL-LOCKED.
- **IP-1** — роли = role-types (`infra-steward`, `security-auditor`), не executor-инстансы. Foundation Part 8 уже даёт `health-monitor` / `quarterly-immune-auditor` archetypes.
- **append-only + R2** — Foundation (Parts 1-11), 4 LOCKED canonical, principles/, shared/schemas/, default-deny-table НЕ модифицируются этим исследованием (только читаются + ссылаются).

## §0.6 Связь с Foundation Part 8 (что уже есть как substrate)

Часть «security» уже частично живёт в Foundation как **system integrity** (Part 8), но это про **внутреннюю целостность данных**, не про **конфиденциальность от внешнего противника**:

- Part 8 даёт: Halt-Log-Alert ordering (Tier 0 ≤1s halt/≤5s log/≤60s alert), Default-Deny novel-action gate, blast-radius Tier 0-3, fail-loud, corrigibility (owner никогда не залочен), observability-only (Part 8 наблюдает, Part 6b энфорсит) [src:part-8 §E L1-L8].
- Чего Part 8 **НЕ** покрывает (gap → этот документ): threat-model против внешнего противника, шифрование at-rest/in-transit, self-hosting, key management, wallet-security, OPSEC. Это **confidentiality/availability**, а Part 8 — про **integrity**. CIA-триада: Part 8 = I; этот документ = C + A.

**Вывод §0.6:** новый материал О-192..195 — это **недостающие C+A** к существующему I-слою Part 8. Архитектурно это ложится либо как расширение Part 8 (integrity→full-CIA), либо как отдельный security-pillar (#17). Структурный выбор = R1 (Руслан).

---

*Phase 0 закрыт. Substrate прочитан, last notes извлечены (O-192..197 + cross-batch O-172/b2g-germany), tech-stack reality замерен на железе. R-criterion `no_last_notes_extracted` — снят. Дальше: Phase 1 threat models.*
