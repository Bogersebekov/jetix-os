---
title: "Phase 6 — R12-aligned security marketing (influence-ethics AUTO-FIRE)"
date: 2026-05-27
phase: 6
parent_prompt: prompts/info-security-own-infra-research-2026-05-27.md
F: F3 (synthesis — R12 paired-frame applied)
G: prompt-info-security-own-infra-research-2026-05-27
R: refuted_if_no_threat_model (R12-marketing branch)
constitutional_posture: R12 paired-frame STRICT + influence-ethics AUTO-FIRE + R1 surface + append-only
roy_pair: gamification/propaganda-class claim → influence-ethics-expert receiver (auto-pair)
language: russian
status: draft (phase report)
---

# Phase 6 — R12-aligned security marketing

> **R12 paired-frame STRICT — influence-ethics-expert AUTO-FIRE.** Каждый маркетинговый
> приём ниже surfaced **вместе** с этической контр-рамкой. Причина: «самая безопасная сеть»
> = **superlative trust-claim**, а trust-claims = поверхность манипуляции максимальной
> чувствительности (over-promise = extraction-of-trust).

## §6.0 Центральная R12-напряжённость (назвать прямо)

**Voice (O-192):** «самую безопасную в мире делать».
**Reality (Phase 0-1):** на 2026-05-27 — один VPS, бэкап не настроен, HIGH-данные идут в 3 внешних API (Claude/Notion/Groq), ключи частично в plaintext-риске.

→ Заявить «самая безопасная сеть в мире» **сегодня как факт** = **(а)** ложь, **(б)** security theater, **(в) R12-нарушение**: over-promise извлекает доверие/коммитмент партнёра на ложном основании. Тот же принцип O-193, что запрещает «продавать базы», запрещает и **«продавать безопасность, которой нет»**. Honest security marketing = R12-compliant **по построению**.

**Разрешение напряжённости:** «самая безопасная» — это **траектория и обязательство**, не текущий факт. Маркетируем **trajectory + provable-now**, не superlative-now.

## §6.1 Claim ladder — лестница от стремления к доказанному

```
УРОВЕНЬ 4: внешний аудит / сертификация (SOC2-lite, pentest-отчёт)  ← Scale, provable третьей стороной
УРОВЕНЬ 3: published threat model + transparency report + bug-bounty ← Run, provable публично
УРОВЕНЬ 2: open-source код (auditable) + fork-and-leave (verifiable)  ← Build, provable любым
УРОВЕНЬ 1: doctrine-обязательство (Charter: no-DB-sell, fork-and-leave) ← сейчас, provable текстом
─────────────────────────────────────────────────────────────────────
УРОВЕНЬ 0 (запрещён): «самая безопасная в мире» как голый superlative ← R12-violation, security theater
```

**Дисциплина:** заявлять можно **только тот уровень, что уже достигнут**. На Build = Уровень 1-2. «Самая безопасная» допустима **только** с квалификатором траектории: *«строим самую безопасную сеть — вот наш threat-model, вот что уже зашифровано, вот как вы можете уйти с данными»*, а не *«мы — самая безопасная сеть»*.

## §6.2 Что provable СЕЙЧАС vs нет (честный инвентарь)

| Заявление | Provable сейчас? | Чем |
|---|---|---|
| «Не продаём базы данных» | ✅ да | Charter-обязательство + бизнес-модель (revenue из событий/услуг, не данных) |
| «Можешь уйти с данными (fork-and-leave)» | ✅ да | export-фича + R12 + open-source (verifiable) |
| «Открытый код — проверь сам» | ✅ да (для open частей) | публичный репо |
| «Данные участника шифруются E2E» | ⚠️ **НЕТ на Build** | будет на Run (Phase 5 §5.2) — НЕ заявлять как готовое |
| «Собственная инфраструктура / вычисление» | ⚠️ **частично** (whisper.cpp) | O-194 = Scale; НЕ заявлять «свои серверы» как факт |
| «Самая безопасная в мире» | ❌ нет | никем не измерено; superlative недоказуем в принципе |
| «Защищены от атак» (O-195) | ⚠️ осторожно | «применяем X, Y, Z практики», не «неуязвимы» |

**Правило:** колонка «⚠️/❌» → **не в внешнем copy** до того, как станет ✅. Это прямая реализация R12 (no extraction beyond agreed — включая trust).

## §6.3 Anti-security-theater checklist (paired: театр vs реальное)

| ❌ Security theater (выглядит безопасно) | ✅ Реальная безопасность (проверяемо) |
|---|---|
| «Military-grade encryption» (buzzword) | «AES-256 / age / Signal-protocol — вот где, вот ключи у кого» |
| Иконка замка / «bank-level security» | Опубликованный threat-model + что НЕ покрыто |
| «100% защищено / неуязвимо» | «Вот наши известные ограничения + roadmap» |
| Закрытый код «доверьтесь нам» | Open-source «не доверяйте — проверьте» |
| «Самая безопасная» без определения | Метрики: что зашифровано, кто видит, как уйти |
| Compliance-бейджи без сути | Реальный pentest-отчёт / transparency report |

**Influence-ethics counter:** security theater — это **propaganda-приём «symbolic substitution»** (символ безопасности вместо безопасности). Он эксплуатирует невозможность пользователя проверить → R12-extraction (доверие на ложном символе). Дисциплина: **каждый security-символ должен иметь проверяемый референт.**

## §6.4 Honest disclosure of limitations (контр-интуитивно: строит БОЛЬШЕ доверия)

**Тезис:** открытое признание ограничений вызывает **больше** доверия, чем superlative. (Psychology: «pratfall effect» + калибровка доверия.) И это R12-чисто.

Пример honest-disclosure-копии (Build-уровень):
> «Сейчас мы используем Claude API для синтеза и Notion как интерфейс — эти данные покидают нашу инфраструктуру. Мы это честно говорим. Что мы УЖЕ делаем: фс = ваш source of truth, шифрование чувствительного, fork-and-leave. Куда идём: собственное вычисление для самого чувствительного (голос уже локально). Вот наш roadmap.»

**Influence-ethics verdict:** disclosure-копия = **anti-manipulation by design** — она даёт партнёру калиброванную картину для **информированного** решения (= R12 «agreed share» строится на правде). Это сильнее любого superlative и устойчивее (нет разоблачения позже).

## §6.5 Open-source как trust-механизм («don't trust, verify»)

- Резонирует с уже-существующими `concepts/digital-sovereignty.md` + `jetix-open-source-principles`.
- **«Не доверяйте — проверьте»** (crypto-этос, Antonopoulos) = противоположность security theater. Открытый код = доказуемость без необходимости верить на слово.
- **R12-связка:** open-source = **anti-lock-in доказан кодом** (можешь форкнуть → не заперт). Это превращает абстрактное «fork-and-leave» в проверяемый факт.
- **Граница:** не всё открывать (секреты, личные данные участников — закрыты; ядро/методы — открыты). Honest: «открыто X, закрыто Y, вот почему».

## §6.6 Partner-facing claims discipline (Tseren / Kaiser тип)

Для конкретных партнёрских разговоров (CRM реальные люди):

- **Никаких superlatives** — только specific + provable. Вместо «мы самые безопасные» → «вот наш threat-model для вашего кейса; вот что шифруется; вот как вы уходите с данными».
- **Под-обещать, пере-доставить** (under-promise) — заявлять Build-уровень, даже если планы амбициознее.
- **Письменно = только ✅-колонка §6.2.** Любое ⚠️/❌ = «в планах», явно помечено как план.
- **R12-trail:** партнёрское security-обещание = коммитмент → должно быть исполнимо на текущей стадии или явно maркировано как roadmap. (Связь с CRM voice-DRAFT-only дисциплиной — обещания не авто-промоутятся.)

## §6.7 Honest competitor comparison

- **Не «мы безопаснее всех»** (недоказуемо) → **«вот ось, по которой мы отличаемся»**: anti-lock-in (fork-and-leave), no-data-selling, open-source, data-sovereignty-trajectory.
- Признать, где конкуренты сильнее (зрелость, аудиты, ресурсы) — это калибровка, не слабость.
- Дифференциатор Jetix честно = **не «больше шифрования», а другая модель доверия**: безопасность участника **в том числе от платформы** (A5/R12) — этого у extraction-based платформ нет **по бизнес-модели**, не по технологии. Вот это — provable и уникально.

## §6.8 R12 paired-frame verdict + O-197 reject

**O-197 «перелопатим, снесём с пути» в security-маркетинге = HARD REJECT.**

- **Influence-ethics (auto-fire):** militant/adversarial framing в security-копи = **(1)** offensive-security-импликация (звучит как угроза «врагам» — юридически/этически опасно); **(2)** in-group/out-group + loyalty-for-protection = exit-cost = **R12-tension** (fork-prevention-by-deterrence, Layer-4) [src:voice-batch-14 §5; default-deny-table Layer-4].
- **Recruitment-dynamics marker:** «семья защитит / снесём чужих» = mass-movement adversarial-cohesion паттерн.
- **Verdict:** security-нарратив Jetix = **строго defensive щит** («мы защищаем тебя и твои данные, в т.ч. от нас самих»), **никогда** offensive меч («снесём врагов»). Это и R12-чисто, и единственно-законно, и сильнее по доверию.
- **Reframe (R12-compliant):** вместо «семья перелопатит врагов» → *«сеть защищает участников; уходишь когда хочешь, с данными; конкурируем ценностью, не подавлением»* (= metaplan «уважение к соревнующимся» + fork-and-leave).

## §6.9 Provable-claims registry (что чем подкреплено — для копирайтинга)

| Claim (разрешённый) | Уровень | Proof point | Стадия |
|---|---|---|---|
| «Фс = ваш source of truth, не наш» | 2 | архитектура + export | Build ✅ |
| «Не продаём и не используем данные против вас» | 1 | Charter + бизнес-модель (revenue не из данных) | Build ✅ |
| «Уходите с данными без штрафа (fork-and-leave)» | 2 | export-фича + open-source | Build ✅ |
| «Открытый код — проверьте» | 2 | публичный репо | Build ✅ |
| «Голос обрабатывается локально» | 2 | whisper.cpp | Build (after Ph2 P0) ✅ |
| «E2E-шифрование данных участника» | 3 | per-member keys | **Run** (не раньше) |
| «Собственное вычисление» | — | own GPU/fine-tune | **Scale** (не раньше) |
| «Прошли независимый аудит» | 4 | pentest/cert отчёт | **Scale** (не раньше) |
| «Самая безопасная в мире» | — | ❌ **никогда как голый superlative** | — |

## §6.10 R1 reservation

Финальные формулировки security-копи + позиционирования = **strategic prose Руслана** (R1). Рой выложил: claim-ladder, provable-инвентарь, anti-theater-чеклист, O-197-reject, registry. Любой внешний security-copy → **через influence-ethics paired-frame перед публикацией** (Default-Deny, как O-197).

---

*Phase 6 закрыт. R12 paired-frame STRICT applied. Центральный вывод: «самая безопасная» = траектория+provable-now, НЕ superlative-now (over-promise = R12-extraction-of-trust). Claim-ladder (4 уровня), anti-security-theater чеклист, honest-disclosure (строит больше доверия), open-source = «не доверяйте, проверьте», O-197 militant-framing = HARD REJECT (defensive щит, не offensive меч). Дальше: Phase 7 mermaid + Main + SUMMARY + INDEX.*
