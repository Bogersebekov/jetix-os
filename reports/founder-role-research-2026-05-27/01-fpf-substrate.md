---
title: "Phase 0 — FPF lens + substrate read (founder role research)"
date: 2026-05-27
type: research-report-phase
parent_prompt: prompts/founder-role-research-2026-05-27.md
phase: 0
F: F2
G: prompt-founder-role-research-2026-05-27
R: refuted_if_current_state_not_grounded
constitutional_posture: R1 surface only + R6 + IP-1 STRICT + append-only
status: complete
---

# Phase 0 — FPF lens + substrate read

## §0.1 Зачем этот research вообще существует (одним абзацем)

Руслан сказал голосом 27.05 очень конкретную вещь: «чем мне нужно заниматься
в основном» при том, что у него **0 нанятых людей**, но при этом он уже год+
строил субстрат, и сейчас он находится в фазе перехода от «стройки фундамента»
к «продвижению». Это не вопрос «как стать founder'ом» — это вопрос **«я уже
founder год, фундамент почти готов, что мне делать в ближайшие 6-12 месяцев и
кого брать первым в команду»**. Research отвечает ровно на это: operating model
для solo-периода + blueprint первой команды + паттерн AI-усиления. Не общие
советы — конкретный operating manual под текущее состояние.

## §0.2 Current state baseline (точная фиксация — без этого research бессмысленен)

| Параметр | Значение | Источник |
|---|---|---|
| Нанятых людей | **0** | prompt §0 |
| AI-агентов (ROY swarm) | **17** (9 original + 8 book-driven) | CLAUDE.md Active ROY Swarm |
| Инструмент founder'а | Claude Code Max sub + voice-pipeline | CLAUDE.md |
| Стадия платформы | **Build, середина** (substrate saturated, outward ~48%) | Platform Lifecycle Plan |
| Время на субстрат | **1 год+** / 1509 commits / 60 дней / 9 недель | development-promotion-mode-transition.md |
| Voice notes pre-репо | 1100+ | prompt §0 |
| Фаза (режим founder) | **переход development → promotion** | O-160 |
| Wave 1 outreach | pending (Maxim / Oleg / Левенчук / Цэрэн / Прапион / Дмитрий Кайзер / Сева) | Execution Plan Fixation |
| Главный блокер сейчас | **Video A + 2-day artefact sprint** (доки/видео/сайт/презентация) | voice-batch-14 Note 1 |
| Модель | Кооператив (Mondragón 5:1 + R12 + 75/25 + triple-role partner) | Economic V10 |
| Фундамент | Workshop+Mastery+Network + 16 направлений (V4 MetaPlan FINAL 26.05) | V4 MetaPlan |
| Гео | Берлин | prompt §0 |

**Главный вывод baseline:** Руслан НЕ на старте. Он в редкой и важной точке —
**фундамент построен, но ещё не «обёрнут» наружу и не монетизирован**. Ошибка
здесь — продолжать строить субстрат (трап накопления, O-163), вместо того чтобы
переключиться в режим продвижения. Research должен это переключение
поддержать, а не саботировать «давай ещё допилим».

## §0.3 FPF lens — кто такой founder в данной онтологии

По FPF (IP-1 Role≠Executor): «founder» — это **роль-тип**, набор функций.
Конкретный исполнитель = Руслан (RUSLAN-LAYER). Это важно методологически:
когда мы говорим «founder должен делать X», мы описываем **функцию роли**, а не
«Руслан обязан лично». Часть функций исполняет Руслан-человек, часть — AI-агенты
(ROY swarm), часть — будущая команда. Research именно про это распределение:
**какие функции роли founder остаются на человеке Руслане, какие уходят на AI,
какие — на первых людей.**

Foundation-уровень это уже зафиксировал тремя концептами:

- **O-160 (когда):** фаза-переход development → promotion. Руслан голосом
  («audio_731»): «я уже всё закончил этот режим девелопмента и разработки… снова
  переключаю режим с постройки фундамента на обёртку продвижения информации,
  общения с людьми, общения с командой».
- **O-174 (кто):** founder-persona — «человек достойный уважения», синтез лучших
  людей и методов. Это про идентичность, не про задачи.
- **O-186/188/190 (какая роль):** **«полу-философ, полу-продавец»** — founder
  занимается ТОЛЬКО верхнеуровневой стратегией + продвижением/общением, всю
  рутину делегирует человеку или машине; foundation-first над быстрыми деньгами.

Три голосовых батча подряд (12 → 13 → 14) сошлись на founder-transition. Это
**robust signal**, не случайная фраза. Research материализует этот сигнал в
operating model.

## §0.4 Что именно сказал Руслан 27.05 (декомпозиция запроса на под-вопросы)

Голос Руслана содержит 6 явных под-вопросов. Фиксирую, чтобы research на каждый
ответил:

1. **«Чем мне заниматься стратегически, чтобы быстро/качественно развивать?»**
   → Phase 2 (таксономия 13 функций) + Phase 3 (operating model).
2. **«Я: новые направления нахожу / людей нахожу / переговоры веду / ресурсы
   нахожу / инвесторов».** → это и есть фактический список core-функций founder;
   Phase 2 их структурирует и приоритизирует.
3. **«Китай как ресурс — варианты заработка подкидываю».** → это паттерн «founder
   как генератор рыночных гипотез / источников ресурсов»; Phase 6 (resources).
4. **«Что делать СЕЙЧАС, когда 0 человек?»** → Phase 3 (solo operating model).
5. **«Кого в первую команду?»** → Phase 4 (first team hiring). Руслан сам
   назвал кандидатные роли: **PM, усиление по общению (люди, которые за него
   общаются), возможно разработчик платформы**.
6. **«Очень жёсткий research»** → §17.0 mandate: exhaustive, не surface-level.

## §0.5 Что я прочитал из субстрата (provenance)

- `wiki/concepts/founder-role-specialization.md` (O-186/188/190, Tier A)
- `wiki/concepts/development-promotion-mode-transition.md` (O-160, Tier A)
- `decisions/strategic/VOICE-BATCH-14-INSIGHTS-2026-05-27.md` (Note 1: 2-day sprint)
- `decisions/RUSLAN-ACK-VOICE-BATCH-14-2026-05-27.md` («акаю всё, фиксируй везде»)
- `decisions/strategic/JETIX-METAPLAN-V4-FINAL-2026-05-26.md` (16 направлений)
- `decisions/strategic/PLATFORM-LIFECYCLE-STAGES-PLAN-2026-05-25.md` (Build, actor matrix)
- `decisions/strategic/EXECUTION-PLAN-FIXATION-2026-05-24.md` (4 типа партнёров, Wave 1)
- `decisions/strategic/ECONOMIC-MODEL-TOKENOMICS-2026-05-22.md` (Economic V10)
- `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` (Workshop+Mastery+Network)
- `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` (R12 constitutional)

## §0.6 Constitutional posture для всего research

- **R1 (surface only):** Я НЕ авторизую стратегию. Я раскладываю варианты,
  founder-функции, паттерны, очередь решений (R1 queue). Финальный выбор —
  Руслан. Никакого «ты должен» как директивы — только «вот опции и trade-off».
- **R6 (F-G-R + cross-cite):** каждое утверждение с источником.
- **R11 (no auto-actions):** никаких авто-найма, авто-fundraise, авто-отправки.
- **R12 STRICT (paired-frame):** разделы про найм и fundraising проходят
  через двойную рамку — найм non-coercive, fork-and-leave, Mondragón 5:1;
  fundraising без VC-extraction / MLM / выкачивания аудитории.
- **IP-1 STRICT:** роли абстрактны; Руслан / Максим / Дмитрий = RUSLAN-LAYER
  инстансы, упоминаются как примеры, не как Foundation-обязательства.
- **Append-only:** новые файлы, ничего LOCKED не трогаю.

## §0.7 Что research НЕ делает (границы)

- Не пишет стратегическую прозу за Руслана (R1).
- Не нанимает / не пишет офферы людям (R11 + R12).
- Не трогает Foundation paths, LOCKED docs, principles/.
- Не «подтверждает» что субстрат закончен — это решение Руслана; research лишь
  показывает, что субстрат-накопление-сверх-меры = anti-pattern (O-163).

**Следующая фаза:** reference solo founders — что делают / чего НЕ делают / как
масштабируют / какую первую команду берут (Naval / PG / Levels / Vassallo / Forte
/ 37signals / Karpathy / Buterin / Mondragón).
