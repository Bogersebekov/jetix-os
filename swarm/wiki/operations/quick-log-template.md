---
title: Quick-Log Template — что говорить Claude чтобы занести Toggl entry
type: operations
status: active
version: 1.0
created: 2026-05-03
related:
  - swarm/wiki/operations/time-tracking-categories.md
---

# 🕒 Quick-Log Template

Шаблон-инструкция: **что и как говорить Claude**, чтобы он быстро занёс activity в Toggl с правильными projects + tags.

Используется в конце дня (вечерний debrief) или утром следующего (вспоминая вчерашний).

---

## 📝 Минимальный формат

```
HH:MM-HH:MM, <проект>, <короткое описание>
```

**Пример:** `14:00-15:00, Deep Work, pipeline разработка`

→ Claude занесёт entry за указанный период с описанием. Без тегов.

---

## 🎯 Полный формат (со всеми тегами)

```
HH:MM-HH:MM, <проект>, <описание>
energy=<low|medium|high>
output=<ship|draft|blocked|explore>
+<любые свободные tags через запятую>
```

**Пример:**
```
16:30-18:15, Deep Work, разработка пайплайна — финальный инструмент
energy=high
output=ship
+pipeline, time-tracking
```

---

## 🗂️ 8 Canonical Projects

| Emoji | Project | Когда использовать |
|-------|---------|--------------------|
| 🌙 | **Сон** | Любой сон, дрёма ≥30 мин |
| ⚡ | **Зарядка** | Утренняя routine физ.активность (≤30 мин) |
| 💪 | **Спорт** | Полноценная тренировка (бег, зал, длинная прогулка для тренировки) |
| 🛒 | **Рутина** | Магаз, готовка, еда, душ, уборка, бытовуха |
| 🧠 | **Deep Work** | Реальная работа: код, writing, стратегирование, чтение по теме |
| 🚶 | **Гулял** | Прогулка без цели тренировки |
| 😌 | **Отдых** | Осознанный отдых: лежать, медитация, созерцание |
| ⚠️ | **Ебланил** | Honest tracking — залип в YouTube/соцсетях, прокрастинировал |

---

## 🏷️ Canonical Tags (v1.1)

### Energy (выбрать ОДИН)
- `low` — устал, тупил, шёл «на автопилоте»
- `medium` — норм, нейтрально
- `high` — фокус, поток, ясность

### Output (выбрать ОДИН)
- `ship` — что-то рабочее ушло наружу / зафиксировано (commit, доку, сообщение)
- `draft` — материал для дальнейшей работы, не финал
- `blocked` — застрял, не продвинулся
- `explore` — исследование, обучение, понимание (без deliverable)

### Sub-direction (free, можно несколько)
Любые осмысленные теги для группировки: `pipeline`, `strategy`, `writing`, `health`, `outreach`, `reading`, `notion`, `tseren-video`, ...

Если тега нет — Claude создаст автоматически при первом use.

---

## 💬 Примеры команд (как ты просто можешь сказать)

### Самый ленивый ввод
> «Занеси: 8:30-9:00 Зарядка»

### Обычный
> «14-15 Deep Work, pipeline разработка, energy high, output ship»

### Развёрнутый
> «9:30-12:00 Deep Work, писал стратегию для Tseren video, energy medium, output draft, +strategy, +tseren»

### Несколько entries за раз
> «Залей за вчера:
> - 9:00-12:00 Deep Work, выгрузка идей в wiki, high, ship, +wiki
> - 12:00-13:00 Рутина, обед
> - 13:00-15:30 Deep Work, ревью документа, medium, draft
> - 22:00-23:30 Ебланил, YouTube, low»

### Текущая сессия (running)
> «Сейчас работаю над X, Deep Work — запусти таймер»
→ Claude создаст running entry с `start=now, stop=null`

---

## 🔄 Wokrflow рекомендация

### Вечерний debrief (3-5 мин)
1. Открываешь Toggl UI → смотришь что натрекалось auto/manual
2. Либо просто вспоминаешь день
3. Диктуешь Claude список периодов в формате выше
4. Claude → batch insert → подтверждает

### Утренний catchup (если забыл вечером)
То же самое, но за прошлый день. Указывай дату:
> «За 2026-05-02: 9:00-12:00 Deep Work, ...»

### После debrief — sync на сервере
```bash
cd ~/jetix-os && python3 tools/toggl_sync.py YYYY-MM-DD && python3 tools/aggregate_activity.py YYYY-MM-DD
```

Это:
- Подтянет свежие entries
- Cross-check с AW (что приложения говорят vs что ты заявил)
- Положит report в `reports/activity_YYYY-MM-DD.md`

---

## ❓ Что Claude умеет автоматически

- ✅ Парсить time ranges в любом формате (`14-15`, `14:00-15:00`, `с 14 до 15`)
- ✅ Распознавать projects по русскому/английскому названию (даже опечатки в разумных пределах)
- ✅ Создавать tags если их нет (`high`, `ship` и т.д. появились автоматически 03.05)
- ✅ Конвертировать Berlin time ↔ UTC (Toggl хранит UTC, ты говоришь Berlin)
- ✅ Batch insert нескольких entries за раз
- ✅ Re-assign / split / merge существующих entries (если попросишь)

## ⚠️ Что Claude НЕ умеет (пока)

- Угадать project по описанию без явного указания (надо называть)
- Видеть screenshots Toggl UI без скрина (пока не научили)
- Запускать Toggl-sync на сервере (твои руки)

---

**Last updated:** 2026-05-03 by Claude (stupefied-ride session)
