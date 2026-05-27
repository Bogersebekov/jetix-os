---
title: "Phase 3 — Own wallets / data sovereignty / crypto integration"
date: 2026-05-27
phase: 3
parent_prompt: prompts/info-security-own-infra-research-2026-05-27.md
F: F3 (synthesis от crypto-security canon + Jetix V10 Ethereum substrate)
G: prompt-info-security-own-infra-research-2026-05-27
R: refuted_if_no_threat_model (data-sovereignty branch)
constitutional_posture: R1 surface only + R11 + R12 (treasury = extraction surface) + append-only
language: russian
status: draft (phase report)
---

# Phase 3 — Own wallets / data sovereignty

> **Контекст:** «валеты» (Ruslan voice) = **wallets**. Они не висят в воздухе — они привязаны
> к уже-acked-у **V10 Programmable Ethereum Phase 2+** (R12-enforcement через смарт-контракты:
> Mondragón ratio cap 5:1 + QF revenue-distribution + fork-and-leave exit-tokens)
> [src:CLAUDE.md §4.2 R12 programmable Option D Hybrid ack commit 8a3d800;
> swarm/awaiting-approval/r12-programmable-ethereum-2026-05-18.md].
> То есть кошельки = **техническая реализация R12 anti-extraction**. Где казна — там и
> extraction-риск → R12 STRICT.

## §3.0 Главный honest-вывод фазы

**На Phase A (solo, pre-revenue) казны нет → wallets НЕ срочны.** Не over-engineer'ить сейчас.
Что **актуально сейчас** = personal-hardware-wallet гигиена (если Руслан держит крипту) +
**data-sovereignty основы** (encryption at-rest, backup 3-2-1), потому что данные есть уже.
Wallet-инфраструктура (multisig treasury, on-chain R12) = **Run/Scale**, после revenue и когорты.

## §3.1 Wallet taxonomy (что бывает и когда что)

| Тип | Что | Кто контролирует ключ | Когда для Jetix |
|---|---|---|---|
| **Custodial** (биржа/провайдер) | ключ у третьей стороны | НЕ ты | ❌ против суверенитета; только как on-ramp фиат→крипто |
| **Non-custodial EOA** (MetaMask/Rabby) | externally-owned account, seed-фраза у тебя | ты | личный кошелёк founder'а; hot для мелких сумм |
| **Hardware (cold)** | ключ в железе, не покидает устройство | ты (физически) | **founder сейчас** для любых значимых сумм |
| **Smart-contract wallet (Safe/AA)** | мульти-подпись/программируемый | M-of-N подписантов | **treasury / clan / DAO** — Run/Scale |
| **MPC** (Fireblocks-тип) | ключ распилен криптографически | распределённо | enterprise; Scale, вероятно overkill |

**Принцип (Antonopoulos):** «not your keys, not your coins». Custodial = удобно, но это снова та же зависимость, от которой Jetix уходит. Self-custody = ответственность → дисциплина ключей (§3.3).

## §3.2 Multisig (Safe) — для казны / кланов / DAO

**Safe (ex-Gnosis Safe)** = стандарт смарт-контракт-мультисига. M-of-N подписей для транзакции.

- **Зачем Jetix:** казна сети/клана не должна зависеть от **одного** ключа (= SPOF + single-человек-extraction-риск). 3-of-5 Safe = ни один человек (включая founder'а) не может в одиночку вывести средства → **это техническая реализация O-193 «не использовать против людей»** на уровне казны.
- **R12-связка:** Safe + модули можно настроить под Mondragón 5:1 cap и QF-распределение (V10). Fork-and-leave exit-token = ERC-20/NFT, дающий участнику право вывести свою долю при выходе — **anti-lock-in в коде**.
- **Когда:** появляется реальная общая казна (Run, первая когорта/событие #16 хакатоны с QF-payout).
- **Где живёт:** L2 (дёшево) — см. §3.4.

## §3.3 Hardware wallets (Ledger / Trezor) — дисциплина ключей

| | Ledger | Trezor |
|---|---|---|
| Secure element | да (closed firmware) | Model T: открытее, без SE на старых |
| Open-source | частично | более open |
| Репутация | широкая поддержка; был data-leak клиентской БД (2020) — **сами данные клиентов утекли, не ключи** | open-source-friendly |

- **Дисциплина (одинакова для обоих):**
  - Seed-фраза (12-24 слова) = **офлайн, на металле** (Cryptosteel/самодельная пластина), не в фото/облаке/менеджере паролей.
  - Passphrase (25-е слово) = plausible deniability + второй фактор.
  - **Multisig поверх hardware** для казны (Safe, где подписанты = разные hardware-ключи у разных людей) — Run.
  - Тестовая транзакция перед крупной; verify-on-device адрес (анти-clipboard-malware).
- **Когда:** founder — **сейчас**, если есть любая крипта. Казна — Run (раздать подписантам).

## §3.4 Self-hosted node (Ethereum / L2) — own RPC

**Реальность железа:** full Ethereum node = ~1.2 TB SSD (geth+consensus); archive = 2+ TB. **150 GB VPS НЕ тянет.** L2-ноды легче, но всё равно сотни GB.

| Опция | Суверенитет | Реалистичность сейчас |
|---|---|---|
| Свой full-node | максимум | ❌ нужен dedicated с 2TB+ NVMe (Scale) |
| Свой L2-node (Base/Arbitrum/OP) | высокий | частично; Run+ с бóльшим диском |
| **Rented RPC (Alchemy/Infura)** | низкий (зависимость) | сейчас, но = тот же lock-in |
| **Свой light-client / partner-node** | средний | прагматичный interim |

- **Verdict:** свой ноду = **Scale** (dedicated/own-hardware с NVMe). Interim — rented RPC или partner-node. Работать на **L2** (Base/Arbitrum/Optimism) для дешевизны транзакций (Mondragón/QF payouts на L1 = неподъёмные комиссии). Это «либо собственное, либо партнёриться» из voice (O-194) в crypto-плоскости.

## §3.5 Data sovereignty — own database vs cloud

**Honest reframe (как в Phase 2):** «база данных» Jetix сейчас = **git + markdown** = уже суверенна и переносима. Реляционная БД нужна только если появится платформенное приложение (dashboard, multi-user app).

| Опция | Заметка |
|---|---|
| **Self-hosted Postgres** (на own VPS) | полный контроль; нужен backup + tuning |
| **Supabase self-hosted** | Supabase = open-source → **можно self-host** (Postgres + auth + storage + realtime в Docker); или managed для скорости |
| Managed (Supabase cloud / RDS) | быстро, но снова cloud-зависимость + данные у третьей стороны |

- **Verdict:** пока **git/markdown достаточно** (CRM, KB — уже так). Когда понадобится app-БД — **self-hosted Postgres** (или self-hosted Supabase, т.к. open-source = совместимо с anti-lock-in). Шифровать at-rest (LUKS на диске + `pgcrypto`/column-encryption для чувствительных полей).

## §3.6 Backup strategy — 3-2-1 + encrypted offsite (КРИТИЧНО — закрывает gap Phase 1)

**Правило 3-2-1:** ≥3 копии · ≥2 разных носителя/места · ≥1 offsite. Сейчас в репо **бэкап не обнаружен** (Phase 1 gap, Risk 15) → это **P0**.

```
Источник: jetix-vps filesystem (source of truth)
   │
   ├─ копия 1: git → private GitHub mirror (offsite #1, но НЕ зашифровано → не для секретов)
   ├─ копия 2: Restic/Borg → S3-compatible (Backblaze B2 / Hetzner Storage Box) ЗАШИФРОВАНО offsite #2
   └─ копия 3: периодический encrypted dump → локальный диск/дом (offline копия)
```

- **Инструменты:** **Restic** (простой, dedup, encrypted, S3/B2/SFTP backends) или **Borg** (dedup, проверенный). Tarsnap = платный, надёжный, но vendor.
- **Дисциплина:** бэкап **зашифрован до отправки** (Restic шифрует по умолчанию); регулярный **restore-тест** (бэкап без проверки восстановления = иллюзия); ключ бэкапа хранится отдельно от бэкапа.
- **Связь с Part 8:** FUNDAMENTAL §5 уже называет «reliability 3-2-1 backup» [src:part-8 sources §3]. Это реализация уже-существующего принципа, не новое решение. **Default-Deny:** не разворачивать новые self-hosted сервисы (Phase 2) до того, как backup работает.

## §3.7 Identity — self-sovereign (DID/VC) vs federated (OAuth)

| Подход | Что | Для Jetix |
|---|---|---|
| **Federated (OAuth, Google/GitHub login)** | identity у провайдера | прагматично сейчас, но зависимость |
| **ENS** (ethereum name) | человеко-читаемый on-chain id | прагматичный interim для crypto-identity |
| **DID + Verifiable Credentials (W3C)** | self-sovereign identity, ты владеешь | резонирует с vetted-network (O-195) + Network State; **но рано** (UX/adoption незрелы) |

- **Связка с vetted-network (O-195):** «проверенные бизнесы» = trust-граф = по сути система **verifiable credentials** (кто кем верифицирован). DID/VC — естественная долгосрочная технология для этого. Но на Build/Run — **прагматичный interim** (ENS + ручная верификация + reputation в KB), DID/VC = Scale-горизонт.
- **R12-нюанс:** identity-система не должна стать lock-in («твоя репутация заперта в Jetix»). Self-sovereign DID = репутация **принадлежит человеку и переносима** = fork-and-leave для идентичности. Это правильный долгосрочный вектор именно по R12.

## §3.8 Documents encryption — age / GPG / Cryptomator / sops

| Инструмент | Для чего | Заметка |
|---|---|---|
| **age** | файлы/папки, современный, простой | рекомендуется для нового; `age -r <key>` |
| **GPG** | legacy-совместимость, email, подписи | сложнее, но широкая поддержка |
| **sops** (+ age/GPG) | **секреты в git** (зашифрованные значения) | закрывает A1 key-leak системно — секреты можно коммитить зашифрованными |
| **Cryptomator** | прозрачное шифрование cloud-папок | если что-то всё же в Dropbox/Drive |
| **LUKS / FileVault** | full-disk encryption | базовый слой на всех устройствах |

- **Дисциплина:** чувствительное в репо (например, реальные данные CRM, финансы) — **под age/sops**, не plaintext. Это прямой ответ на A2 (idea-theft) + A1 (leak): даже при доступе к репо противник видит шифротекст.
- **Quick-win:** `sops`+`age` для всех секретов системы (Build P0, пара со self-hosted Phase 2).

## §3.9 Mapping на экономику Jetix (R12 в коде)

| Jetix-механизм (V10/metaplan) | Crypto-реализация | R12-роль |
|---|---|---|
| Mondragón 5:1 cap (ratio payout) | Safe-модуль / контракт-инвариант на payout | не дать extraction через зарплатный разрыв |
| QF revenue-distribution (хакатоны #16) | QF-контракт на L2 распределяет призовой пул | прозрачное, не-extraction распределение |
| **Fork-and-leave** (выход без штрафа) | exit-token (ERC-20/NFT) = право вывести долю | **anti-lock-in в коде** = ядро R12 |
| vetted-network (O-195) | DID/VC trust-граф (Scale) | переносимая репутация ≠ lock-in |
| казна не-extraction (O-193) | 3-of-N multisig (никто один не выводит) | оператор не может «доить» в одиночку |

**Это и есть суть:** wallets/identity для Jetix — не «крипто ради крипто», а **технический способ сделать R12 не-обходимым** (нельзя нарушить anti-extraction, если оно в смарт-контракте, а не в обещании). Это сильнейший R12-positive аргумент. Но — Run/Scale, после того как есть что распределять.

## §3.10 R1 + R12 reservation

- **R1:** разворачивать ли on-chain R12 сейчас vs позже, какой L2, custodial-vs-non — **решение Руслана** (Q14-2 pre-revenue cost). Surface only.
- **R12:** treasury = max extraction-surface → любое wallet-решение проходит R12-аудит; multisig + fork-and-leave exit-token = обязательные инварианты (уже acked в Option D Hybrid). НЕ строить казну, где один человек может вывести всё.

---

*Phase 3 закрыт. Wallet taxonomy + multisig + hardware + node + data-sovereignty + backup 3-2-1 (закрывает Phase 1 gap) + DID/VC + encryption. Honest: wallets = Run/Scale (нет казны на Phase A); data-sovereignty основы (encryption+backup) = сейчас. Crypto = техническая реализация R12 anti-extraction. Дальше: Phase 4 own infrastructure stack.*
