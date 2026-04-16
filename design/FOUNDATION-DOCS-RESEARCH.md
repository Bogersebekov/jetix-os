---
type: research-document
status: draft
stage: methodology-research
version: draft-v0
owner: ruslan
created: 2026-04-16
updated: 2026-04-16
purpose: поиск референсов и методологий для качественного описания системы Jetix OS
related:
  - SYSTEM-DESIGN-HUMAN.md
  - NOTION-MIGRATION-PLAN.md
---

# FOUNDATION-DOCS-RESEARCH.md — Как описывают большие системы. Разбор канонов, методологий и первоисточников

> **Цель:** прежде чем писать `SYSTEM-DESIGN-HUMAN.md` до конца — посмотреть
> как это делали инженеры гигантских систем. Не изобретать с нуля. Взять
> лучшее из каждой школы.
>
> **Контекст:** Ruslan строит Jetix OS. Сейчас документ только для внутреннего
> использования. В близком будущем — аналогичный документ, но для широкой
> аудитории (человек "с улицы", не технарь). Оба должны быть качественными.

---

## Оглавление

1. Зачем этот документ
2. Критерии "качественной" системной документации
3. Канон — операционные системы
   - 3.1 Unix (самая влиятельная)
   - 3.2 Linux
   - 3.3 Windows
   - 3.4 macOS / Darwin
4. Мобильные платформы
   - 4.1 iOS
   - 4.2 Android (AOSP)
5. Патенты как системные описания
6. Интернет-стандарты
   - 6.1 RFC (IETF)
   - 6.2 W3C Recommendations
   - 6.3 IEEE / ISO
7. Корпоративные методологии описания
   - 7.1 Google Design Doc
   - 7.2 Amazon 6-pager
   - 7.3 Netflix Culture Deck
   - 7.4 GitLab Handbook
8. AI System Documentation (новая школа)
   - 8.1 OpenAI System Cards
   - 8.2 Anthropic Constitutional AI
   - 8.3 Model Cards (Google)
9. Методологические фреймворки
   - 9.1 arc42
   - 9.2 C4 model
   - 9.3 4+1 Architectural View Model
   - 9.4 TOGAF / Zachman Framework
   - 9.5 ADR (Architecture Decision Records)
   - 9.6 ISO/IEC 25010
10. Что у всех канонов есть общего (паттерны)
11. Ключевые книги и авторы (foundation readings)
12. Кто именно пишет такие документы (роли)
13. Выводы для Jetix OS — что берём для SYSTEM-DESIGN-HUMAN
14. Вторая версия — для широкой аудитории (user-facing)
15. Дальнейшие шаги

---

## 1. Зачем этот документ

Ты строишь фундаментальный документ. Дом без фундамента падает. Документ без
референсов читается как "непонятно откуда это, почему именно так".

Мы делаем три вещи:
1. **Смотрим на гигантов** — как описаны системы которые определили вычислительную
   эру (Unix, Linux, Windows, iOS, TCP/IP, HTML).
2. **Заимствуем методологии** — проверенные фреймворки (arc42, C4, Google Design Doc,
   ADR).
3. **Формализуем подход для Jetix OS** — не копируем слепо, а берём подходящее
   под масштаб и задачу.

После этого исследования — возвращаемся к `SYSTEM-DESIGN-HUMAN.md` с
**конкретными инструментами**, которые подтверждены мировой практикой.

---

## 2. Критерии "качественной" системной документации

Прежде чем смотреть на примеры — определимся что такое "качественно".
Синтез из мировых практик:

| Критерий | Суть |
|----------|------|
| **Понятность одному читателю** | Читатель у которого нет твоего контекста — прочитал и понял. Без вопросов к автору. |
| **Полнота** | Все вопросы типа "а что если X?" имеют ответы явные либо "это не рассматривается, потому что…" |
| **Attribution / провенанс** | Каждое решение имеет обоснование. Цитата, ссылка, автор решения. |
| **Выдерживает время** | Через 5 лет всё ещё читается осмысленно (не устаревает от косметики технологий). |
| **Композиционность** | Разбит на части, каждая самодостаточна, но вместе — цельное. Читать можно по главам. |
| **Точка А / Точка Б** | Описывает где мы, где хотим быть. Без этого — просто энциклопедия. |
| **Разделение "что / как"** | Выделены: цели (что), принципы (как), механика (конкретные реализации). Не смешано в кашу. |
| **Версионность** | Документ развивается, каждая версия фиксируется. История видна. |
| **Executable** | Содержит достаточно деталей чтобы другой инженер мог построить по нему. Не только "общие идеи". |

Эти 9 критериев — твой чек-лист для `SYSTEM-DESIGN-HUMAN.md` в конце работы.

---

## 3. Канон — операционные системы

### 3.1 Unix (самая влиятельная)

**Кто описал:**
- **Ken Thompson + Dennis Ritchie** — авторы Unix в Bell Labs (1969-1970)
- **Brian Kernighan** — главный популяризатор и соавтор ключевых книг

**Главные первоисточники:**
- **Thompson & Ritchie, "The UNIX Time-Sharing System"** (1974, Communications of the ACM) —
  оригинальная научная статья описывающая систему на 11 страницах. Читается до сих пор.
  Поиск: "UNIX Time-Sharing System Thompson Ritchie 1974 CACM"
- **Kernighan & Pike, "The UNIX Programming Environment"** (1984) — классика, описание
  философии Unix через практику
- **Maurice Bach, "The Design of the UNIX Operating System"** (1986) — детальное
  техническое описание ядра Unix System V
- **Eric S. Raymond, "The Art of Unix Programming"** (2003) — философия и культура,
  доступно онлайн: http://www.catb.org/esr/writings/taoup/

**Что берём (урок Jetix OS):**

1. **Философия описывается ДО механики.** "The Unix Philosophy" существует как
   набор принципов (do one thing and do it well, composability, text streams) ДО
   того как кто-то смотрит на код.
2. **Принципы становятся архетипами.** "Everything is a file" — не техническая
   деталь, а способ думать. У Jetix OS должны быть свои архетипы.
3. **Документация — это часть продукта.** Man pages — не аддон, а равная
   сущность коду. Manual page format (`NAME / SYNOPSIS / DESCRIPTION / SEE ALSO`)
   сам по себе — шаблон.

### 3.2 Linux

**Кто описал:**
- **Linus Torvalds** — автор ядра (1991)
- **Сообщество kernel developers** — коллективное описание

**Главные первоисточники:**
- **Linus'ов пост в `comp.os.minix` 25 августа 1991** — первое публичное
  объявление. 18 строк текста. Часто цитируемая фраза:
  > "I'm doing a (free) operating system (just a hobby, won't be big and professional
  > like gnu) for 386(486) AT clones."
  
  Урок: big things start small. Поиск: "Linus Torvalds minix post 1991"

- **Kernel Documentation** — https://www.kernel.org/doc/html/latest/ —
  документация ЖИВЁТ в самом коде в папке `Documentation/`. Принцип
  **docs-as-code**. Этот же принцип мы применяем в Jetix — CLAUDE.md + wiki/
  в репо, не в Notion.

- **LWN.net** — https://lwn.net — живая техническая документация сообщества.
  Еженедельные отчёты о том что меняется в ядре.

- **"Understanding the Linux Kernel"** — Bovet & Cesati (O'Reilly, 3 издания)
- **Linux Standard Base (LSB)** — формальный стандарт
- **POSIX spec (IEEE 1003)** — что значит "unix-like", формальное определение

**Что берём:**

1. **Docs-as-code.** Документация в том же репозитории что и код. Версионируется
   вместе. Обновляется в том же PR что и изменение функциональности.
2. **Коммуникация через mailing lists/mailboxes.** Linux kernel development
   через mailing lists — это модель для нашей `comms/mailboxes/`. Сообщения
   по протоколу, public, audit trail.
3. **Maintainers model.** Linux разделён по подсистемам, у каждой — maintainer.
   У нас — 12 агентов как "maintainers" своих зон.
4. **Git как основа версионирования.** Linus создал git именно чтобы
   версионировать Linux — документы живут в тех же commits.

### 3.3 Windows

**Кто описал:**
- **Mark Russinovich + David Solomon + другие** — главные технические авторы
- **Dave Cutler** — архитектор Windows NT (бывший DEC VMS)

**Главные первоисточники:**
- **"Windows Internals" series** (Microsoft Press, 7+ изданий) — канон. Сейчас
  называется "Windows Internals, Parts 1 & 2". Для серьёзного понимания системы.
- **Microsoft Docs / MSDN** — https://learn.microsoft.com — огромный публичный
  corpus. Включает Architecture sections.
- **"Showstopper!" by G. Pascal Zachary** (1994) — книга о том как создавали
  Windows NT. Показывает **процесс** создания, не только результат. Читается
  как роман, очень полезно для понимания как вообще пишут большие системы.
- **Charles Petzold, "Programming Windows"** — классика, 5-6 изданий.
  Образец дидактического описания API.

**Что берём:**

1. **Процессная литература.** "Showstopper!" показывает что описание системы —
   это не только "что есть", но и "как мы к этому пришли, какие были развилки,
   что отвергли и почему". В `SYSTEM-DESIGN-HUMAN.md` это Часть 7 (Открытые
   вопросы) + Приложение История итераций.
2. **Архитектурные слои формализованы.** Windows NT описан как layered
   architecture: HAL → Kernel → Executive → Subsystems → Applications. Чёткое
   разделение. В Jetix: `raw/` → `wiki/` → `agents/` → `projects/` → outputs.
3. **"Design principles" как отдельная секция.** Windows NT design principles
   (reliability, portability, compatibility, security, performance) —
   сформулированы в первом издании и влияют на все решения 30 лет.

### 3.4 macOS / Darwin

**Кто описал:**
- **Steve Jobs** — philosophical direction
- **Avie Tevanian + команда NeXT** — технический фундамент
- **Amit Singh, "Mac OS X Internals"** — полный технический справочник

**Главные первоисточники:**
- **Apple Developer Documentation** — https://developer.apple.com/documentation/
- **Darwin Open Source** — https://opensource.apple.com (часть macOS open)
- **Apple Human Interface Guidelines (HIG)** — https://developer.apple.com/design/human-interface-guidelines/
  КРИТИЧНО. HIG — это не про код, это про **принципы опыта**. Именно такой
  уровень описания нам нужен для частей 1-3 Jetix.

**Что берём:**

1. **HIG как модель для user-facing.** Когда будем делать вторую версию
   (для широкой аудитории) — HIG идеальный референс структуры.
2. **Философия → design → реализация.** Apple всегда описывает сначала
   философию (почему iPhone круглые углы), потом design principles (feel
   of the material), потом implementation.

---

## 4. Мобильные платформы

### 4.1 iOS

**Кто описал:**
- **Scott Forstall + Bertrand Serlet + Henri Lamiraux** — команда iOS 1.0
- **Внутренний "Ten Year Plan"** (согласно биографии Jobs, Walter Isaacson) —
  легендарный документ, не публичный, но упоминается

**Первоисточники:**
- **Steve Jobs, iPhone keynote 2007** — https://www.youtube.com/watch?v=MnrJzXM7a6o
  — не документ, но МОДЕЛЬ как презентовать систему широкой аудитории.
  Формула Jobs: "Three things: wide-screen iPod, a phone, and a revolutionary
  Internet communicator. Are you getting it? These are not three separate devices."
- **iPhone Software Roadmap 2008** (первый keynote открытия SDK) — переход
  от закрытой к открытой системе.
- **Apple Internal Design Documents** — фрагменты в Isaacson biography

**Что берём:**

1. **"One-liner" описания системы.** iPhone = iPod + Phone + Internet.
   Для Jetix нам нужна такая же формула. Сейчас в `SYSTEM-DESIGN-HUMAN.md`
   это будущая Часть 1.1 "Зачем существует Jetix OS (одно предложение)".
2. **Демонстрация, не объяснение.** Jobs показывает, не описывает. Miro-
   визуализации в Шаге 2 — наш путь к этому.

### 4.2 Android / AOSP

**Первоисточники:**
- **AOSP documentation** — https://source.android.com
- **Compatibility Definition Document (CDD)** — https://source.android.com/docs/compatibility/cdd
  — формальный документ что ДОЛЖНО быть чтобы называться "Android". Это
  наша `SYSTEM-DESIGN-HUMAN.md` аналог, но внешний.
- **Android Architecture Components** — слои, модули

**Что берём:**

1. **Compatibility Definition** — отдельный документ "что ДОЛЖЕН делать Jetix
   чтобы считаться Jetix". Это Часть 2 (Цели и результаты) + Часть 7 (Открытые
   вопросы как "что ещё неясно в compatibility").
2. **Open vs Closed.** Android показывает как описывать систему которая имеет
   core (AOSP) и проприетарные extensions (Google Play Services). У Jetix OS
   будет аналогичное разделение — open-source kernel + закрытые плагины клиентов
   (см. idea [[ideas/open-source-premium-jetix-model]]).

---

## 5. Патенты как системные описания

Ты отдельно спросил про патенты — это важная параллель.

### Структура патента (USPTO стандарт)

| Секция | Что внутри |
|--------|------------|
| **Title** | 1 строка, ёмкое название |
| **Abstract** | 150 слов — суть изобретения |
| **Background** | Состояние области сейчас, какая проблема решается |
| **Summary** | Краткое описание решения (≠ detailed description) |
| **Brief Description of Drawings** | Перечень схем с подписями |
| **Detailed Description** | Полное описание реализации, с отсылками к рисункам |
| **Claims** | ⭐ **САМАЯ ВАЖНАЯ ЧАСТЬ.** Формальные юридические утверждения о том что изобретение делает. Именно это защищается. |

**Первоисточники:**
- **USPTO Manual of Patent Examining Procedure (MPEP)** — https://www.uspto.gov/web/offices/pac/mpep/
- **EPO Guidelines for Examination** (European Patent Office) — https://www.epo.org/law-practice/legal-texts/guidelines.html
- **WIPO Patent Drafting Manual** — https://www.wipo.int/publications/en/details.jsp?id=4259

### Примеры knockout-патентов (читать ради стиля)

- **US 174,465** — **Alexander Graham Bell, Telephone** (1876). 5 страниц.
  Модель ёмкости.
- **US 6,285,999** — **Google PageRank** (Larry Page, 1998). Формулы + описание
  алгоритма.
- **US 7,479,949** — **Apple Multi-touch interface iPhone** (2007). Читается
  как техническая документация.

### Что берём для Jetix OS

1. **Claims — это наша Часть 2 (Цели и результаты).** В патенте claims — это
   точные формулировки "что система делает". У нас это должны быть
   формулировки "что Jetix OS выдаёт на выходе, какие метрики, какие границы".
   Прямо можно писать в стиле "The system shall..." на русском: "Система
   обязуется выдавать X при условии Y". Строго. Проверяемо.
2. **Abstract.** Первый абзац `SYSTEM-DESIGN-HUMAN.md` должен быть как abstract
   патента — 150 слов, кто прочитал — всё понял на верхнем уровне.
3. **Background + Summary.** Наши Точка А + Точка Б — то же самое.
4. **Detailed Description.** Части 3-6 — детальная реализация.

### Различие для Jetix OS

Патент защищает от копирования. У нас обратная задача — **максимально
понятно описать чтобы люди могли использовать** (и чтобы агенты могли работать
с этим как своим системным промптом). Но структура полезна как шаблон
**строгости** формулировок.

---

## 6. Интернет-стандарты

### 6.1 RFC (Request for Comments, IETF)

**Первоисточники:**
- **Все RFC** — https://www.rfc-editor.org/
- **RFC 791** — IPv4 (September 1981, Jon Postel) — эталон: короткий, точный, исчерпывающий
- **RFC 2616** — HTTP/1.1 (1999) — до сих пор актуален
- **RFC 7230-7237** — HTTP/1.1 update (2014)

### Структура RFC

| Секция | Что внутри |
|--------|------------|
| Abstract | 100-200 слов |
| Status of This Memo | стандарт / draft / experimental |
| Table of Contents | |
| Introduction | контекст, motivation |
| Conventions Used | RFC 2119 keywords (MUST / SHOULD / MAY) |
| Specification | полное описание |
| Security Considerations | обязательная секция в каждом RFC |
| IANA Considerations | обязательная секция |
| References | |

**RFC 2119** — https://www.rfc-editor.org/rfc/rfc2119 — определяет
"Key words for use in RFCs to Indicate Requirement Levels":
> MUST / SHALL — обязательно
> MUST NOT / SHALL NOT — запрещено
> SHOULD — рекомендуется
> SHOULD NOT — не рекомендуется
> MAY — допустимо

**Что берём:**

1. **Язык обязательности.** В `SYSTEM-DESIGN-HUMAN.md` Часть 4 (Потоки) и
   Часть 5 (Действия) — использовать MUST/SHOULD/MAY (или русские аналоги:
   "обязательно / рекомендуется / допустимо"). Это **радикально** повышает
   читаемость и executable-ness документа.
2. **Security Considerations как обязательная секция.** У Jetix тоже должна
   быть такая — что делаем с credentials, privacy, повреждением данных.
   Можно включить в Часть 5 (Действия и Failure modes).
3. **Process "Rough consensus and running code"** — IETF мотто. Для Jetix:
   каждое решение должно работать на практике, не только теоретически.

### 6.2 W3C Recommendations

- **HTML5 spec** — https://html.spec.whatwg.org/multipage/
- **CSS spec** — https://www.w3.org/Style/CSS/specs.en.html
- **Web Accessibility Guidelines (WCAG 2.1)** — https://www.w3.org/TR/WCAG21/

WCAG — особенно интересно: описывает **что доступно для пользователей**, не
технически. "Principle 1: Perceivable. Guideline 1.1 Text Alternatives..."
Это наш стиль для второй версии (user-facing) Jetix OS.

### 6.3 IEEE / ISO

- **IEEE 802.3** — Ethernet standard
- **ISO/IEC 25010** — Software Quality Model (functional suitability,
  performance efficiency, compatibility, usability, reliability, security,
  maintainability, portability)
- **IEEE 1471 / ISO/IEC 42010** — Systems and software engineering —
  **Architecture description** standard. Формальный стандарт о том как
  описывать архитектуры. Прямо релевантно нам.

---

## 7. Корпоративные методологии

### 7.1 Google Design Doc

**Первоисточник:**
- **"Design Docs at Google"** by Malte Ubl —
  https://www.industrialempathy.com/posts/design-docs-at-google/
  (статья на которую ссылается почти вся индустрия)

**Структура Google Design Doc:**

| Секция | Суть |
|--------|------|
| Context and scope | Где в системе это, что затрагивается |
| Goals and non-goals | ⭐ **Non-goals** явно отделены от goals. Это наша Часть 2.4 Границы! |
| The actual design | Конкретное решение |
| Alternatives considered | Что отвергли и почему |
| Cross-cutting concerns | Security / privacy / observability / SLOs |

**Что берём:**

1. **Goals + Non-goals.** Мы это уже закладываем в Часть 2.
2. **Alternatives considered.** Добавить секцию "Что мы рассмотрели и отвергли"
   в каждое большое решение. Это защищает от "а почему не иначе?" через год.
3. **One-page summary.** Google рекомендует чтобы TL;DR документа читался
   за 5 минут.

### 7.2 Amazon 6-pager (narrative memo)

**Первоисточник:**
- **Jeff Bezos 2018 shareholder letter** и выступления — Amazon использует
  "6-page narratives" вместо PowerPoint. Разбор:
  https://www.anecdote.com/2018/05/memos-at-amazon/
- Книги: **"Working Backwards"** by Colin Bryar & Bill Carr (ex-Amazon) —
  детальное описание методологии

**Структура 6-pager:**

Не пункты, а **narrative prose**. 6 страниц связного текста. Встреча
начинается с 20 минут тихого чтения документа всеми. Потом обсуждение.

Темы, которые обычно покрываются:
- Context (зачем задача)
- Objectives (что хотим достичь)
- Tenets (принципы которые держим)
- State of the business / problem
- Proposed approach
- FAQ — самый важный раздел! Anticipated questions с ответами.

**Что берём:**

1. **FAQ как секция.** В Jetix OS — добавить "FAQ" в Приложение. Вопросы
   которые точно зададут через месяц/год — ответить сейчас.
2. **Связный прозаический текст.** Не только bullet points. Большие идеи
   нужно излагать предложениями, не пунктами.
3. **Tenets = принципы.** У нас 7 принципов Манифеста — это tenets.

### 7.3 Netflix Culture Deck (2009)

**Первоисточник:**
- https://www.slideshare.net/reed2001/culture-1798664 (оригинальный slide deck)
- Patty McCord, "Powerful: Building a Culture of Freedom and Responsibility"

124 slide'а о том как устроена компания. Стала legendary — Sheryl Sandberg
назвала "самый важный документ которые когда-либо вышел из Silicon Valley".

**Что берём:**

1. **Высокий уровень абстракции.** Не "у нас такие-то процессы", а "мы
   ищем людей которые Y и делаем Z потому что верим в W".
2. **Анти-шаблоны явно.** Netflix описывает что они НЕ делают. Как наша
   Часть 2.4 "Границы".
3. **Slide format vs document** — у Netflix работал slide-deck. У нас —
   markdown. Но принцип цепких формулировок одинаковый.

### 7.4 GitLab Handbook

**Первоисточник:**
- https://handbook.gitlab.com/
- Огромный публичный handbook — **всё** о компании. Тысячи страниц.
- Пример маленькой, но жирной секции: https://handbook.gitlab.com/handbook/values/

**Что берём:**

1. **Всё открытое по умолчанию.** GitLab всё пишет на handbook.gitlab.com,
   пока специально не решит что секрет. Для Jetix OS — аналогично: wiki/
   всё open, приватное специально помечается.
2. **Handbook first.** Если нужно объяснить что-то дважды — пиши в handbook,
   не повторяй. Наш принцип для wiki/.
3. **Линкабельность.** Каждая секция имеет URL. Можно дать ссылку на
   конкретный абзац.

---

## 8. AI System Documentation (новая школа, 2020+)

Это новая территория — как описывают AI-системы. Прямо релевантно для Jetix OS
как AI-системы.

### 8.1 OpenAI System Cards

**Первоисточники:**
- **GPT-4 System Card** (2023) — https://cdn.openai.com/papers/gpt-4-system-card.pdf
- **GPT-4o System Card** — https://openai.com/index/gpt-4o-system-card/

**Структура System Card:**
- Model overview
- Observed Safety Challenges (что может пойти не так)
- Safety Mitigations (что делаем чтобы избежать)
- Preparedness (как тестировали)
- Conclusion

### 8.2 Anthropic Constitutional AI

**Первоисточники:**
- **Constitutional AI paper** (2022) — https://arxiv.org/abs/2212.08073
- **Claude's Constitution** — https://www.anthropic.com/news/claudes-constitution

Это **декларативное** описание того чем модель руководствуется. Буквально —
конституция.

### 8.3 Google Model Cards

- **Model Cards for Model Reporting** (2019) — https://arxiv.org/abs/1810.03565
  — Margaret Mitchell et al. Формальное предложение формата описания ML-модели.

### Что берём для Jetix OS

1. **"Observed Risks" как секция.** Что может пойти не так в нашей системе.
   Добавить в Часть 5 (Failure modes) или сделать Приложение.
2. **Constitution-style описание.** Манифест 7 принципов — это наша конституция.
   Можно отдельно оформить как документ `CONSTITUTION.md` (подумать).
3. **Model Card для каждого агента?** У Jetix 12 агентов — у каждого может
   быть "agent card" с Intended Use / Limitations / Evaluation.

---

## 9. Методологические фреймворки

### 9.1 arc42

**Первоисточник:**
- https://arc42.org — бесплатный template для software architecture docs
- Авторы: Gernot Starke + Peter Hruschka
- Книга: **"Sustainable Software Architecture"** by Carola Lilienthal

**Структура arc42** (12 секций):

1. Introduction and Goals (=наше Видение + Цели)
2. Constraints (=наша Часть 2.4 Границы)
3. Context and Scope
4. Solution Strategy
5. Building Block View (=наша Часть 3 Роли)
6. Runtime View (=наша Часть 4 Потоки + Часть 5 Действия)
7. Deployment View
8. Crosscutting Concepts
9. Architecture Decisions (см. 9.5 ADR)
10. Quality Requirements
11. Risks and Technical Debt
12. Glossary

Прямо очень близко к тому что ты делаешь. **arc42 = готовый шаблон для
формализованного перевода** SYSTEM-DESIGN-HUMAN в архитектурный документ
на Шаге 4.

### 9.2 C4 model

**Первоисточник:**
- https://c4model.com — Simon Brown
- **Книга "The C4 model for visualising software architecture"**

4 уровня абстракции:
- **C1 Context** — система и её окружение (user, other systems)
- **C2 Containers** — крупные блоки внутри системы
- **C3 Components** — блоки внутри containers
- **C4 Code** — классы, функции (обычно не нужно)

У нас в Miro **L1/L2/L3 inventory** — это прямо C1/C2/C3. Совпадение не
случайное — C4 популярен именно потому что работает.

### 9.3 4+1 Architectural View Model

**Первоисточник:**
- **Kruchten, "Architectural Blueprints—The '4+1' View Model"** (IEEE 1995) —
  https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf

5 взглядов на одну систему:
- **Logical view** — функциональность (для пользователя)
- **Development view** — модули (для программистов)
- **Process view** — процессы во время работы (для инженеров)
- **Physical view** — deployment (для операторов)
- **+1: Scenarios** — use cases которые объединяют все 4 взгляда

**Что берём:** одну систему можно описать с разных точек зрения, и это разные
документы. У нас Часть 3 (Роли) — logical. Часть 4 (Потоки) — process.
Infrastructure документ (ARCHITECTURE-CURRENT) — physical.

### 9.4 TOGAF / Zachman Framework

**TOGAF** (The Open Group Architecture Framework) — https://www.opengroup.org/togaf
— enterprise architecture. Для очень больших организаций.

**Zachman Framework** — https://www.zachman.com/about-the-zachman-framework
— матрица 6×6: What/How/Where/Who/When/Why × Scope/Business Model/System Model/
Technology Model/Detailed Representations/Functioning Enterprise.

Оба тяжеловесны для нашего масштаба. Полезно знать как reference, но не применять.

### 9.5 ADR (Architecture Decision Records)

**Первоисточник:**
- **Michael Nygard, "Documenting Architecture Decisions"** (2011) —
  https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- **ADR GitHub organization** — https://adr.github.io/

**Структура одной ADR:**

```
# ADR 001: [Title]
Date: YYYY-MM-DD
Status: [proposed | accepted | deprecated | superseded by ADR-NNN]

## Context
(какая проблема, какие силы действуют)

## Decision
(что решили)

## Consequences
(что следует из решения — плюсы, минусы, компромиссы)
```

Один ADR = одно решение. Файлы `docs/adr/0001-*.md`, `0002-*.md`, ... Короткий
(1-2 страницы).

**Что берём:**

1. **Формат ADR для фиксации ключевых решений Jetix OS.** Примеры:
   - ADR-001: 12 agents, not 5 or 20 (обоснование из ARCHITECTURE.md §1)
   - ADR-002: JSONL mailboxes (not Redis)
   - ADR-003: Karpathy wiki over vector RAG
   - ADR-004: Notion decommission
   - etc.
2. Создать папку `docs/adr/` для таких записей.

### 9.6 ISO/IEC 25010 — Software Quality Model

- https://iso25000.com/index.php/en/iso-25000-standards/iso-25010

8 characteristics:
1. Functional Suitability (completeness, correctness, appropriateness)
2. Performance Efficiency
3. Compatibility
4. Usability
5. Reliability
6. Security
7. Maintainability
8. Portability

**Что берём:** чек-лист когда переходим к тестированию (Шаг 6). Можно
использовать в Части 2 (Метрики) как стандартизированный набор категорий.

---

## 10. Что у всех канонов есть общего (паттерны)

Сделаем синтез. Вот **7 паттернов** которые встречаются ВЕЗДЕ:

| # | Паттерн | Где встречается |
|---|---------|-----------------|
| 1 | **Философия/Why до How** | Unix philosophy, Apple HIG, Netflix Culture, RFCs' motivation | 
| 2 | **Формальные обязательства (Claims/MUST)** | Patents, RFCs, Android CDD, OpenAI System Cards |
| 3 | **Явные Non-goals / что НЕ делаем** | Google Design Doc, Netflix, Linux manpages (BUGS section) |
| 4 | **Multi-view описание** | 4+1 model, C4, Kruchten, Zachman |
| 5 | **Alternatives considered** | Google Design Doc, ADR, patents (Background) |
| 6 | **Docs-as-code** | Linux, Apache, Modern DevOps, Jetix (мы уже так делаем) |
| 7 | **Versioning + changelog** | ВСЕ качественные документы без исключения |

Эти 7 паттернов — наш must-have для `SYSTEM-DESIGN-HUMAN.md`.

---

## 11. Ключевые книги и авторы (foundation readings)

Если читать только это — 80% пользы. Расставлено по приоритету:

1. **Frederick Brooks, "The Mythical Man-Month"** (1975) — классика о
   создании больших систем. Глава "The Documentary Hypothesis" прямо про то
   что мы делаем.
2. **Frederick Brooks, "The Design of Design"** (2010) — последняя книга Brooks.
   Методология дизайна систем.
3. **Fred Brooks, "No Silver Bullet"** (IEEE 1986) — статья. Почему нет
   серебряной пули и что с этим делать.
4. **Eric S. Raymond, "The Art of Unix Programming"** (2003) — http://www.catb.org/esr/writings/taoup/
5. **Eric S. Raymond, "The Cathedral and the Bazaar"** (1999) — как
   организовать open-source/community работу.
6. **Christopher Alexander, "The Timeless Way of Building"** (1979) —
   теория паттернов из архитектуры зданий. Повлияла на Gang of Four,
   на Richard Gabriel ("Patterns of Software").
7. **Donald Knuth, "Literate Programming"** — философия документ-как-код.
8. **David Parnas, "On the Criteria To Be Used in Decomposing Systems into
   Modules"** (CACM 1972) — https://www.cs.umd.edu/class/spring2003/cmsc838p/Design/criteria.pdf
   — seminal paper о декомпозиции систем. Короткая, глубокая.
9. **Leslie Lamport, "Specifying Systems"** (2002) — TLA+ формальные
   спецификации.
10. **Richard Gabriel, "Patterns of Software"** (1996) — для понимания как
    мыслят паттернами.

---

## 12. Кто именно пишет такие документы (роли)

В больших компаниях это:

| Роль | Что пишет | Пример компании |
|------|-----------|-----------------|
| **System Architect / Chief Architect** | Общая архитектура | Dave Cutler (Windows NT), Gordon Bell (DEC) |
| **Technical Writer** | Прилизывание, структурирование, консистентность | Каждая крупная tech компания |
| **Founding engineer** | Философия + первый документ | Torvalds (Linux), Thompson (Unix) |
| **CTO / Engineering Manager** | ADR, принципы, decision records | |
| **Product Manager** | Goals, non-goals, user-facing | |
| **CEO / Founder** | Vision, North Star, strategy | Jobs (iPhone keynote), Bezos (Day 1 letters) |
| **Community maintainers** | В open-source — коллективная авторство | Linux kernel maintainers |

Для Jetix OS сейчас **ты (Ruslan) + я** играем все эти роли сразу. Это
нормально для 1-person startup phase. Когда появится команда — роли
разделяются.

**Kлючевое:** один человек обычно пишет один тип документа лучше других.
CEO пишет Vision (не SysArch пишет Vision). CTO пишет ADR. Technical Writer
перелизывает всё для консистентности. **Мы делим эти роли между тобой и мной:**

- **Ты** — Vision, Цели (предприниматель, видит далеко)
- **Я** — System architecture, ADRs, technical consistency
- **Я + ты** — Roles, Flows, Actions, States (совместно)
- **Serверный Claude** — staging, inputs, structured writing

---

## 13. Выводы для Jetix OS — что берём для SYSTEM-DESIGN-HUMAN

Конкретные инструменты из этого исследования, которые **применяем сейчас**:

### Для структуры

1. ✅ **Мета-секция "Как пользоваться документом"** — уже добавлена (vs GitLab Handbook)
2. ✅ **Goals + Non-goals явно разделены** — Часть 2 (vs Google Design Doc)
3. ✅ **Мульти-взгляд:** Часть 3 (WHO — logical) + Часть 4 (HOW data — process) + ... (vs 4+1 model, C4)
4. 🔄 **Alternatives considered для каждого большого решения** — добавить в Приложение или в каждую Часть (vs Google Design Doc, ADR)
5. 🔄 **FAQ как приложение** — добавить в конец документа (vs Amazon 6-pager)
6. 🔄 **MUST/SHOULD/MAY язык** — использовать в Частях 4-5 (vs RFC 2119)
7. 🔄 **Security/Privacy Considerations как отдельная секция** — добавить (vs каждый RFC)

### Для процесса

8. ✅ **Docs-as-code в git** — делаем (vs Linux, Kubernetes, всё современное)
9. ✅ **Версионирование с changelog** — есть Приложение 2 (vs ВСЕ каноны)
10. 🔄 **ADR для решений** — создать папку `docs/adr/` отдельно от
    SYSTEM-DESIGN-HUMAN.md. В SDH оставить summary, детали — в ADR.
11. 🔄 **Two-stage review process** (Amazon style) — первые 20 минут молчаливого
    чтения, потом обсуждение. Мы так и делаем в диктовке, просто формализуем.

### Для содержания

12. 🔄 **One-liner Jetix OS** — как у Jobs "iPod + Phone + Internet". Часть 1.1.
13. 🔄 **Tenets / Constitution** — наши 7 принципов Манифеста можно вынести в
    отдельный `CONSTITUTION.md` (aka Claude-style Constitution).
14. 🔄 **Agent Cards** для 12 агентов — по шаблону ML Model Cards. Короткая
    страница per агент: intended use, capabilities, limitations, evaluation.
    Может заменить/дополнить существующий `agents/{id}/system.md`.
15. 🔄 **Quality model категории (ISO 25010)** — использовать как checklist
    метрик в Части 2.3.

---

## 14. Вторая версия — для широкой аудитории (user-facing)

Ты сказал: в близком будущем нужно описание системы для человека "с улицы".
Это совсем другой документ. Требования:

### Отличия от SYSTEM-DESIGN-HUMAN

| SYSTEM-DESIGN-HUMAN (internal) | USER-GUIDE (external) |
|--------------------------------|----------------------|
| Для инженеров (себя, меня, агентов) | Для НЕ-инженера |
| Философия + точность | Как сделать X |
| 3000-5000 строк | 500-1500 слов на сценарий |
| Manual page стиль | Tutorial + How-to + Reference |
| Полный | Минимально-достаточный |

### Референсы для второй версии

1. **Apple iPhone User Guide** — https://support.apple.com/guide/iphone/welcome/ios
   — золотой стандарт consumer-facing. Простой язык, картинки.
2. **Stripe API Docs** — https://docs.stripe.com/api — эталон developer-facing
   (но не consumer). Образец как описывать "что делает и как вызвать".
3. **Nielsen Norman Group writing guidelines** — https://www.nngroup.com/
4. **Divio's 4-documents theory** — https://docs.divio.com/documentation-system/
   — фундаментальная работа. 4 типа документации:
   - **Tutorials** — обучение (для новичков, learning-oriented)
   - **How-to guides** — решение конкретных задач (problem-oriented)
   - **Reference** — точная инфа (information-oriented)
   - **Explanation** — понимание (understanding-oriented)
   **Это ключевая структура для второй версии.** Каждая из 4 категорий — отдельный
   тип контента, нельзя смешивать.
5. **GitLab handbook — User-facing sections** — образец consumer-понятного
   языка в огромном документе.
6. **Steve Krug, "Don't Make Me Think"** (2000, 3 издания) — книга о UX который
   не требует усилий от пользователя.
7. **"The Product Is the Documentation"** — by John McMerkin — тезис что хорошая
   документация становится частью продукта.

### Предварительная структура для JETIX-USER-GUIDE.md (когда дойдём)

```
1. Что такое Jetix OS (в 2 параграфа)
2. Первые 5 минут (Tutorial)
3. Как сделать X (How-to guides)
4. Полная справка (Reference)
5. Почему Jetix устроен именно так (Explanation)
6. FAQ
7. Troubleshooting
```

---

## 15. Дальнейшие шаги

Этот документ — research input. Не action list. Решения принимаем дальше.

### Предлагаемые немедленные действия

1. **Прочитать этот документ** целиком, впитать.
2. **Обсудить со мной** в чате какие пункты берём (ликую за 1-3-4-5-6-7-10-12-13-14).
3. **Когда диктуем Часть 1** — держать в голове:
   - One-liner "Jetix OS = ..." (vs Jobs keynote)
   - Tenets (vs Netflix Culture)
   - Non-goals явно (vs Google Design Doc)
4. **Когда диктуем Часть 2 (NEW)** — держать в голове:
   - Claims style (vs patents)
   - Compatibility Definition (vs Android CDD)
   - ISO 25010 quality categories
5. **После основной диктовки** — создать дополнительные артефакты:
   - `docs/adr/` — decisions
   - `CONSTITUTION.md` — 7 принципов как конституция
   - Agent Cards для 12 агентов
6. **Когда решим делать user-facing версию** — вернуться к §14 и Divio theory.

### Открытые вопросы по этому документу

- **Нужно ли найти реальные первоисточники** (скачать PDF, сохранить в `raw/references/`)? Это
  делается отдельной задачей когда Notion-α закончится. Я могу (на Windows) скачать
  ключевые PDF'ы через WebFetch (если Ruslan разрешит) или через `curl` в bash.
- **Какие из упомянутых книг у тебя уже есть / читал?** Приоритизация reading list.
- **Нужен ли separate ADR-lite скилл?** `/new-adr` для Claude Code — быстро
  фиксировать решения как 1-страничные ADR.

---

## Приложение A. Quick-reference таблица — где искать что

| Хочу найти как описать... | Смотри... |
|----------------------------|-----------|
| Философию системы | Unix (Thompson/Ritchie 1974), Netflix Culture, Apple HIG |
| Цели и не-цели | Google Design Doc, Patent Claims |
| Архитектурную иерархию | C4 model, 4+1 Kruchten, arc42 |
| Runtime потоки | RFCs (HTTP, TCP), Windows Internals |
| Decision log | ADR (Michael Nygard) |
| Quality attributes | ISO/IEC 25010 |
| Community org | Linux kernel docs, RFC process |
| AI-системы | OpenAI System Cards, Anthropic Constitution, Google Model Cards |
| User-facing | Apple iPhone Guide, Stripe Docs, Divio 4-docs |
| Internal handbook | GitLab Handbook |
| Executable specs | TLA+ (Lamport), Leslie |

## Приложение B. Короткий список URL для скачивания (offline reading)

1. Unix paper (Thompson & Ritchie 1974) — PDF есть на многих edu сайтах
2. Kruchten 4+1 — https://www.cs.ubc.ca/~gregor/teaching/papers/4+1view-architecture.pdf
3. Parnas 1972 — https://www.cs.umd.edu/class/spring2003/cmsc838p/Design/criteria.pdf
4. Google Design Docs — https://www.industrialempathy.com/posts/design-docs-at-google/
5. ADR (Nygard 2011) — https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
6. Apple HIG — https://developer.apple.com/design/human-interface-guidelines/
7. Anthropic Constitution — https://www.anthropic.com/news/claudes-constitution
8. GPT-4 System Card — https://cdn.openai.com/papers/gpt-4-system-card.pdf
9. Linux kernel docs — https://www.kernel.org/doc/html/latest/
10. arc42 template — https://arc42.org
11. C4 model — https://c4model.com
12. GitLab Handbook — https://handbook.gitlab.com/
13. Divio 4-docs — https://docs.divio.com/documentation-system/

## Приложение C. История итераций этого документа

| Дата | Версия | Что изменилось |
|------|--------|----------------|
| 2026-04-16 | draft-v0 | Создан. 15 секций, 12 методологий, 3 приложения. |

## Приложение D. Связь с Рабочим столом SYSTEM-DESIGN-HUMAN

Этот документ добавляется в "Рабочий стол" SYSTEM-DESIGN-HUMAN.md, секция
"📐 Design-документы (живая работа)" — четвёртой строкой после
SYSTEM-DESIGN-HUMAN, INPUTS, MIGRATION-PLAN.

Держать **рядом** с ними как панно при обсуждении любых содержательных вопросов
структуры.
