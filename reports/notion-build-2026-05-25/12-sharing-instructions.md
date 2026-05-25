---
title: Notion Build — Phase 12 Sharing + permissions instructions
date: 2026-05-25
type: build-phase-log
phase: 12
status: DONE
---

# Phase 12 — Sharing & permissions (для Ruslan, UI-шаги) ✅

> Notion sharing/permissions = UI-only (REST API не управляет правами доступа).
> Это инструкции, ничего не расшарено автоматически (Pool result — никакого
> auto-invite/auto-public per §5 prompt).

## §1 Три режима шеринга

| Режим | Как | Кому | Право |
|---|---|---|---|
| **Public link (read-only)** | Страница → Share → Publish → toggle "Publish to web", выключи "Allow editing" | лендинг, холодная аудитория, витрина шаблона | view |
| **Specific user invite** | Share → Invite → email → роль **Can comment** (или Can view) | Дмитрий-trial, конкретный партнёр | view/comment |
| **Workspace member (edit)** | Settings → Members → Add member, или Share → Invite → **Can edit** | co-creators, кто реально строит вместе | edit |

**Рекомендация порядка:** начни с invite-per-person (контроль), public link — только
для финальной витрины, edit — только проверенным co-creators.

## §2 Per-page рекомендации

| Страница / слой | Рекомендуемый шеринг |
|---|---|
| 🚀 Jetix OS (root) | приватно у тебя; шарь конкретные под-страницы, не корень |
| 📊 Master Dashboard | invite (view) — хорошая точка входа для триала |
| 🟢 Layer 1 — Personal Core | **НЕ шарить как есть** — это личный шаблон; форкай копию для другого человека |
| 🔵 Layer 2 — Team Collaboration | можно шарить (view/comment) — это и есть командный слой |
| 🟠 Layer 3 — Universal Business | view для партнёров; **Financial draft — не шарить** до готовности |
| 🤖 AI Tools & Lifehacks | можно public — хороший маркетинговый артефакт |
| 📖 Onboarding & Help | public-friendly — помогает любому форку |

## §3 ⛔ Privacy boundaries — что НЕ шарить

- ❤️ **Life Pulse / 🔁 Habits / 💰 Финансы (Layer 1)** — личное, красная линия. Никогда наверх, никогда вовне.
- 🟠 **Layer 3 Financial (Revenue/Expenses)** — не шарить черновики реальных цифр (сейчас пусто — sterile, но как заполнишь — закрой).
- 🟧 **Charter Jetix overlay** — до формального R12-ревью (см. Phase 4 §note: ROY influence-ethics dispatch ещё не прогонялся) держи internal.
- 🛡️ **R12 Audit Log** — internal/Steward-only по дизайну.

## §4 ⚖️ R12 paired-frame чек перед любым внешним шерингом

Прежде чем шарить наружу — пройди 4 вопроса (paired-frame на share-решение):

1. **Извлечение?** — не извлекаю ли я ценность из получателя сверх честного обмена (шарю шаблон ≠ доение).
2. **Согласие?** — есть ли явное согласие, если страница содержит данные другого человека (нет данных третьих лиц в sterile-шаблоне — ок).
3. **Lock-in?** — не привязываю ли получателя так, что трудно уйти/форкнуть (наоборот — fork-friendly).
4. **Манипуляция?** — нет ли в публичной копии FOMO/scarcity/культовых рамок (анти-секта уже встроена).

Все 4 PASS → шарь. Иначе → стоп, поправь копию.

## §5 Token security advisory (CARRY-OVER → Phase 13)

🔐 **Интеграционный токен был засвечен в истории чата** (зафиксировано в prereqs-packet).
**После завершения сборки:** Notion Settings → Integrations → `Jetix Builder` → **Revoke**,
затем создай новую интеграцию для будущих ре-ранов (env var, не в чат). Build на этом
не сломается — структура уже в Notion + полное зеркало на диске.

## §6 Pool result

Никаких авто-действий: ни public-publish, ни invite, ни data populate не выполнены
автоматически. Ты решаешь, что и кому шарить, вручную в UI.
