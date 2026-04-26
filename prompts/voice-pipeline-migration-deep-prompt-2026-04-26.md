---
title: Voice-Pipeline Migration — убрать Anthropic API dependency, перевести на Claude Code Max
date: 2026-04-26
type: deep-prompt
target: Claude Code на сервере (бригадир) → swarm cycle (1-2 циклов)
parent_task: Daily Log 26.04
authored_by: Cloud Cowork (по прямой инструкции Ruslan'а 26.04)
status: ready-to-launch (после CRM cycle 10 ack)
prereqs: CRM cycle 10 закончен, ack'нут, push'нут — чтобы избежать commit conflicts
---

# Voice-Pipeline Migration — Deep Prompt

## §0. Контекст + цель

**Текущая боль (incident 26.04):**

`tools/extract.py` и `tools/filter.py` используют **Anthropic API** напрямую через Python `anthropic` library. Это требует `ANTHROPIC_API_KEY` в env и оплачивается per-token. Сегодня pipeline упал когда CC сделал `unset ANTHROPIC_API_KEY` (из защитного pattern для Claude Code launches).

Сегодня заплатили ~$1-5 за emergency export+rerun. Ruslan хочет **убрать эту dependency полностью** — pipeline должен работать через его **Max subscription** (Claude Code, unlimited use), без `ANTHROPIC_API_KEY` где бы то ни было.

**Цель:**

После cycle:
- `tools/extract.py` и `tools/filter.py` НЕ требуют `ANTHROPIC_API_KEY`
- Все LLM calls идут через `claude --headless` (subprocess) → используют Max subscription
- `bash tools/run_pipeline.sh` работает в **любом env** где доступен `claude` CLI (без API key)
- Pipeline runs = **0 USD** (covered by Max subscription)
- Backward compat: если `ANTHROPIC_API_KEY` всё-таки задан — fallback на старый API path (для emergency / batch performance)
- `crm/_scripts/voice_router.py` (когда CRM cycle 10 будет ack'нут) — тоже должен использовать тот же CC pattern

**Принципы (non-negotiable):**

1. **Filesystem = SoT (D17).** Все артефакты в `~/jetix-os/`.
2. **Transcribe.py не трогаем** — Groq Whisper (отдельный provider, дёшев, работает).
3. **Backward compat обязателен.** Если old API path работал — он должен продолжать работать как fallback.
4. **Idempotent migration.** Re-run script = same output. Existing `inbox/processed/extractions/*.json` и `inbox/processed/filtered/batch_*.json` остаются читаемыми после миграции.
5. **No regression.** После миграции — `bash tools/run_pipeline.sh` производит **identical output** (modulo LLM non-determinism) на том же наборе transcripts. Verifiable через diff.
6. **Zero-config preferred.** Если в системе доступен `claude` — использовать его. Ничего ручного не настраивать.
7. **Russian для content, English для code/config.**

---

## §1. Текущее состояние (что есть)

**Pipeline сейчас:**

```bash
bash tools/run_pipeline.sh
  ├── python3 tools/transcribe.py     # Groq Whisper API (KEEP AS-IS)
  ├── python3 tools/extract.py        # Anthropic API ← MIGRATE
  ├── python3 tools/filter.py         # Anthropic API ← MIGRATE
  └── python3 tools/review_report.py  # local Markdown gen (KEEP AS-IS)
```

**Что используется как input/output (verify в начале cycle):**

- `tools/extract.py`:
  - reads: `raw/transcripts/*.txt` (или `.md`, проверить точный path)
  - writes: `inbox/processed/extractions/*.json` (один JSON на транскрипт)
  - Anthropic call: для каждого транскрипта — single API call с extract-prompt; output = structured JSON items
- `tools/filter.py`:
  - reads: `inbox/processed/extractions/*.json` (все)
  - writes: `inbox/processed/filtered/batch_YYYY-MM-DD.json` (один батч на run)
  - Anthropic call: 1+ calls для дедупа + meta-анализ
- `tools/review_report.py`:
  - reads: `inbox/processed/filtered/batch_*.json`
  - writes: `reports/review_YYYY-MM-DD.md` + копия `~/review-latest.md`
  - Без LLM, чистый Python.

**API key locations (текущие):**
- `~/.env` или `~/jetix-os/.env` (verify в начале cycle)
- Возможно в `~/.bashrc` / `~/.zshrc`

После миграции — key больше не нужен (но при наличии — fallback используется).

---

## §2. Целевое состояние (что должно быть)

**Pipeline после миграции:**

```bash
bash tools/run_pipeline.sh                            # без env требований
  ├── python3 tools/transcribe.py                     # Groq (unchanged)
  ├── python3 tools/extract.py                        # → claude --headless (Max sub)
  ├── python3 tools/filter.py                         # → claude --headless (Max sub)
  └── python3 tools/review_report.py                  # local (unchanged)
```

**Env requirements:**

- `GROQ_API_KEY` — required для transcribe (как раньше)
- `ANTHROPIC_API_KEY` — **не required**, optional fallback
- `claude` CLI должен быть в PATH — required для default path

**Behavior matrix:**

| `claude` в PATH | `ANTHROPIC_API_KEY` set | Result |
|-----------------|-------------------------|--------|
| ✅ | — | use `claude --headless` (default, free через Max) |
| ✅ | ✅ | use `claude --headless` (default — preserve free path) |
| ❌ | ✅ | fallback на старый Anthropic API path |
| ❌ | ❌ | STOP с clear error: "ни `claude` ни `ANTHROPIC_API_KEY` недоступны" |

---

## §3. Архитектура: subprocess wrapper

**Подход: variant A — subprocess wrapper.** Простой, batch-friendly, no CC session required.

`tools/_llm_client.py` — новый shared module. Абстрагирует "как сделать LLM call":

```python
# tools/_llm_client.py
"""
Universal LLM client для voice-pipeline.
Default: claude --headless (Max subscription, free).
Fallback: Anthropic API (если claude CLI недоступен но key есть).
"""

import json
import os
import shutil
import subprocess
import sys
from typing import Optional

class LLMClient:
    def __init__(self, model: str = "claude-sonnet-4-6", system_prompt: Optional[str] = None):
        self.model = model
        self.system_prompt = system_prompt
        self.mode = self._detect_mode()
    
    def _detect_mode(self) -> str:
        if shutil.which("claude"):
            return "cc-headless"
        elif os.environ.get("ANTHROPIC_API_KEY"):
            return "anthropic-api"
        else:
            print("ERROR: ни 'claude' CLI, ни ANTHROPIC_API_KEY недоступны.", file=sys.stderr)
            print("       Установи Claude Code (recommended) или export ANTHROPIC_API_KEY.", file=sys.stderr)
            sys.exit(2)
    
    def call(self, user_prompt: str, max_tokens: int = 4096, temperature: float = 0.0) -> str:
        if self.mode == "cc-headless":
            return self._call_cc_headless(user_prompt, max_tokens, temperature)
        elif self.mode == "anthropic-api":
            return self._call_anthropic_api(user_prompt, max_tokens, temperature)
    
    def _call_cc_headless(self, user_prompt: str, max_tokens: int, temperature: float) -> str:
        # Build full prompt: system + user
        full_prompt = (self.system_prompt + "\n\n---\n\n" + user_prompt) if self.system_prompt else user_prompt
        
        # claude --headless --print "<prompt>" --model <model>
        # Use stdin to avoid shell escaping issues with long prompts
        result = subprocess.run(
            ["claude", "--print", "--model", self.model, "--dangerously-skip-permissions"],
            input=full_prompt,
            capture_output=True,
            text=True,
            timeout=300,  # 5 min per call max
        )
        
        if result.returncode != 0:
            raise RuntimeError(f"claude CLI failed: {result.stderr}")
        
        return result.stdout.strip()
    
    def _call_anthropic_api(self, user_prompt: str, max_tokens: int, temperature: float) -> str:
        import anthropic
        client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
        
        kwargs = {"model": self.model, "max_tokens": max_tokens, "temperature": temperature,
                  "messages": [{"role": "user", "content": user_prompt}]}
        if self.system_prompt:
            kwargs["system"] = self.system_prompt
        
        resp = client.messages.create(**kwargs)
        return resp.content[0].text


def call_llm(user_prompt: str, system_prompt: Optional[str] = None,
             model: str = "claude-sonnet-4-6", max_tokens: int = 4096,
             temperature: float = 0.0) -> str:
    """Convenience function — single-call usage."""
    client = LLMClient(model=model, system_prompt=system_prompt)
    return client.call(user_prompt, max_tokens=max_tokens, temperature=temperature)


def call_llm_json(user_prompt: str, system_prompt: Optional[str] = None,
                  model: str = "claude-sonnet-4-6", max_tokens: int = 4096) -> dict:
    """Call LLM expecting JSON output. Validates + parses."""
    raw = call_llm(user_prompt, system_prompt=system_prompt, model=model, max_tokens=max_tokens)
    
    # Strip markdown code fences if present
    if raw.startswith("```"):
        lines = raw.split("\n")
        raw = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
    if raw.startswith("json\n"):
        raw = raw[5:]
    
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        # Save raw output для debug
        debug_path = "/tmp/llm-raw-output.txt"
        with open(debug_path, "w") as f:
            f.write(raw)
        raise RuntimeError(f"LLM returned invalid JSON. Raw saved to {debug_path}. Error: {e}")
```

**Key design points:**

1. `--dangerously-skip-permissions` для headless calls — pipeline runs unattended, нужен auto-approve. (Если есть concern — можно альтернативно сделать `--allowedTools "Read,Write"` или вовсе без tools для extract/filter которые pure-text in/out.)
2. Retry logic — добавить 3 retry с exponential backoff на:
   - subprocess timeout
   - API rate limit errors (для fallback path)
   - JSON parse errors (LLM иногда возвращает не-JSON — retry с reminder в prompt)
3. Logging — каждый call логирует в `~/.cache/jetix-llm-calls.log`: timestamp / mode / model / input_tokens_est / output_tokens_est / duration_ms.

---

## §4. Миграция extract.py

**Подход:**

1. Прочитать текущий `tools/extract.py` полностью. Понять:
   - Как читает transcripts
   - Как формирует prompt для extract
   - Какой ожидает output schema
   - Как пишет JSON результат
   - Любая state / dedup logic

2. Заменить **только** Anthropic API call на `_llm_client.call_llm_json(...)`. Остальное оставить как есть (file I/O, prompts, schema).

3. Если текущий extract.py использует system_prompt — pass через `system_prompt=` kwarg.

4. Test: запустить на одном transcript из `raw/transcripts/` и сравнить output JSON с предыдущим (структура должна совпадать; content может отличаться немного из-за LLM non-determinism).

**Acceptance:**

- [x] `python3 tools/extract.py` работает с `unset ANTHROPIC_API_KEY` (если `claude` в PATH)
- [x] Output JSON files имеют ту же структуру что раньше
- [x] Existing `inbox/processed/extractions/*.json` остаются читаемыми (не затирать)
- [x] Если transcribe выдаёт N новых файлов — extract обрабатывает только их (уважает existing dedup logic)

---

## §5. Миграция filter.py

**Подход:**

1. Прочитать текущий `tools/filter.py` полностью.
2. Заменить Anthropic API calls на `_llm_client.call_llm_json(...)`.
3. Сохранить multi-call structure если есть (filter обычно делает: dedup → categorize → meta-summary — несколько calls).
4. Test: запустить на existing extractions и сравнить output batch json.

**Acceptance:**

- [x] `python3 tools/filter.py` работает без API key (если `claude` доступен)
- [x] Output batch JSON совместим с existing `review_report.py`
- [x] Dedup logic preserved (не дублирует items из предыдущих batches)

---

## §6. voice_router.py (CRM integration — будущая интеграция)

**Если CRM cycle 10 уже завершён** на момент этого cycle → проверить `crm/_scripts/voice_router.py` использует ли он `_llm_client.py`. Если нет — мигрировать (он скорее всего тоже LLM-driven).

**Если CRM cycle 10 не завершён** — добавить note в AWAITING-APPROVAL packet что voice_router migration отложен до его готовности.

---

## §7. tools/run_pipeline.sh — обновление

```bash
#!/bin/bash
# tools/run_pipeline.sh — voice processing pipeline
# Default: использует Claude Code (Max subscription, free)
# Fallback: Anthropic API (если claude CLI недоступен но ANTHROPIC_API_KEY set)

set -e

cd "$(dirname "$0")/.."

# Pre-flight check
if ! command -v claude &> /dev/null && [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "ERROR: ни 'claude' CLI ни ANTHROPIC_API_KEY недоступны." >&2
    echo "Установи Claude Code: https://claude.ai/code" >&2
    echo "ИЛИ export ANTHROPIC_API_KEY=..." >&2
    exit 2
fi

if [ -z "$GROQ_API_KEY" ]; then
    echo "ERROR: GROQ_API_KEY required для transcribe step." >&2
    exit 2
fi

echo "=== Voice Pipeline ==="
echo "Mode: $([ -n "$(command -v claude)" ] && echo 'Claude Code (Max)' || echo 'Anthropic API')"
echo ""

echo "[1/4] Transcribe..."
python3 tools/transcribe.py

echo "[2/4] Extract..."
python3 tools/extract.py

echo "[3/4] Filter..."
python3 tools/filter.py

echo "[4/4] Review report..."
python3 tools/review_report.py

echo ""
echo "✅ Pipeline complete."
echo "Review: ~/review-latest.md"
echo "Reports dir: reports/"
```

Ключевое: явный pre-flight check + явный mode print в начале (чтобы сразу было видно через что pipeline идёт).

---

## §8. Backward compatibility

**Existing artifacts** должны продолжать работать:
- `inbox/processed/extractions/*.json` (141 files) — read-compatible
- `inbox/processed/filtered/batch_*.json` (4 batches) — read-compatible
- `reports/review_*.md` — не трогать

**Schema preservation:** если новые extract/filter outputs имеют **разную JSON structure** чем старые — это regression. Old structure must be preserved.

**`distribute.py.bak`:** не трогать (архивирован per CLAUDE.md).

---

## §9. Tests

`tests/voice_pipeline/` (новая директория, если ещё нет):

### 9.1 `test_llm_client.py`

- `_detect_mode()` returns "cc-headless" если claude в PATH
- `_detect_mode()` returns "anthropic-api" если только key
- `_detect_mode()` exits 2 если ничего нет
- `call_llm_json()` корректно strip'ает markdown fences
- `call_llm_json()` raises RuntimeError на invalid JSON

### 9.2 `test_extract.py`

- На fixture transcript производит valid JSON
- Output schema совпадает с reference (committed example)

### 9.3 `test_filter.py`

- Дедуп работает (не пропускает existing items)
- Output совместим с review_report.py

### 9.4 `test_run_pipeline.py`

- E2E на 2 mock transcripts (использует mock LLM client с canned responses, не настоящий call)
- Verify output files created

### 9.5 Integration test (manual, не CI)

После миграции — запустить **дважды** на одних и тех же 10 новых транскриптах:
1. С `unset ANTHROPIC_API_KEY` (Max path)
2. С export key + uninstalled claude (API path)

Результаты должны быть structurally identical (modulo LLM non-determinism в content).

---

## §10. Acceptance criteria

- [ ] `tools/_llm_client.py` создан, tested
- [ ] `tools/extract.py` мигрирован, не требует ANTHROPIC_API_KEY
- [ ] `tools/filter.py` мигрирован, не требует ANTHROPIC_API_KEY
- [ ] `tools/run_pipeline.sh` обновлён с pre-flight check + mode print
- [ ] Backward compat: existing extractions/filtered files читаются
- [ ] Tests все green (pytest tests/voice_pipeline/)
- [ ] Smoke test: `bash tools/run_pipeline.sh` запущен на pустом inbox/voice/ — должен gracefully exit без LLM calls (transcribe найдёт 0 файлов → extract найдёт 0 новых → filter no-op → review_report тот же что раньше)
- [ ] Manual integration test: положить 1-2 fixture .ogg в inbox/voice/, запустить pipeline с unset API key, verify success
- [ ] Documentation: обновить `tools/README.md` (если есть) или создать; document mode detection + fallback
- [ ] CLAUDE.md update: section "Voice-Notes Pipeline" — обновить чтобы reflect новое behavior (no API key needed by default)
- [ ] Commit + push в working branch (one coherent commit, или max 2 logical: `[voice] migrate extract+filter to claude code` + `[voice] update pipeline.sh + docs`)

---

## §11. AWAITING-APPROVAL packet structure

`swarm/awaiting-approval/cycle-N-voice-migration-2026-04-26.md`:

```markdown
---
cycle: N
date: 2026-04-26
type: voice-pipeline-migration
status: awaiting-approval
---

# Cycle N — Voice-Pipeline Migration — AWAITING APPROVAL

## §0 TL;DR

Voice-pipeline мигрирован с Anthropic API на Claude Code (Max subscription).
extract.py + filter.py больше не требуют ANTHROPIC_API_KEY. Backward compat
preserved (fallback на API если claude CLI недоступен). Tests green. Smoke
test passed. Pipeline runs = 0 USD via Max subscription.

## §1 What was changed

[список файлов + LOC delta]
- `tools/_llm_client.py` (NEW, ~120 LOC)
- `tools/extract.py` (MODIFIED, ~5 LOC changed — replaced anthropic call)
- `tools/filter.py` (MODIFIED, ~10 LOC changed)
- `tools/run_pipeline.sh` (MODIFIED, +pre-flight check)
- `tools/README.md` (NEW or UPDATED)
- `CLAUDE.md` (UPDATED — Voice-Notes Pipeline section)
- `tests/voice_pipeline/` (NEW, 4 test files)

## §2 What was decided autonomously
[если бригадир сделал judgment calls вне spec — list]

## §3 Deviations from spec
[если что-то не сделано или сделано иначе — explicit list]

## §4 Tests output
[pytest summary]

## §5 Mode detection demo

Test 1: with `claude` in PATH, no key
[shell output showing "Mode: Claude Code (Max)" + successful run]

Test 2: without `claude`, with key
[shell output showing "Mode: Anthropic API" + successful run]

Test 3: neither
[shell output showing exit 2 with clear error]

## §6 Backward compat verification

- Existing 141 extractions readable: ✅
- Existing 4 batch files compatible с review_report.py: ✅
- Diff old vs new output на same fixture: structurally identical, content variation within expected LLM non-determinism: ✅

## §7 Open questions for Ruslan
[если что-то всплыло]

## §8 Next cycle proposal
[если CRM cycle 10 done — voice_router.py migration в следующем cycle, иначе оставить deferred]

## §9 Status

**RECOMMEND:** Ruslan ack → можно безопасно `unset ANTHROPIC_API_KEY` permanently
из всех env / .bashrc / .env файлов. Pipeline self-sufficient через Max sub.

Brigadier: <agent>
Time spent: <X> мин
LOC delta: ~<N>
```

---

## §12. Anti-scope (НЕ делать)

- ❌ Не трогать `tools/transcribe.py` (Groq, отдельный provider, работает)
- ❌ Не трогать `tools/review_report.py` (local Python, no LLM)
- ❌ Не менять JSON schema extractions/filtered (backward compat critical)
- ❌ Не migrate другие Python скрипты в repo которые используют Anthropic API (если найдёшь — log в Open questions, не migrate автоматически)
- ❌ Не удалять `ANTHROPIC_API_KEY` из env / .env файлов (это user action — рекомендация в §11 packet)
- ❌ Не строить async / parallel batching extract calls (sequential ОК для 10-50 транскриптов; parallelization — отдельный cycle если понадобится)
- ❌ Не мигрировать `crm/_scripts/voice_router.py` если CRM cycle 10 ещё не ack'нут
- ❌ Не добавлять новые dependencies (pip packages) — все через subprocess + stdlib

---

## §13. Branch / commit strategy

Branch: `claude/jolly-margulis-915d34` (работаешь там же где CRM cycle 10).

**ВАЖНО:** перед началом — `git fetch && git pull --rebase` чтобы подтянуть CRM cycle 10 commits (если уже push'нут). Если pull conflict — STOP, ping Ruslan.

Commit strategy:
1. `[voice] add _llm_client.py with mode detection (CC headless / API fallback)`
2. `[voice] migrate extract.py + filter.py to _llm_client; update run_pipeline.sh`
3. `[voice] add tests + update CLAUDE.md docs` (опционально отдельно)

Push после каждого commit.

---

## §14. Notes for follow-up

После этого cycle:
- Ruslan может permanently `unset ANTHROPIC_API_KEY` из его env (~/.bashrc, ~/.env)
- Любые автоматические jobs (cron) могут теперь запускать pipeline без secrets management
- Cost monitoring: pipeline runs больше не появляются в Anthropic billing (только в Max usage stats)
- Future: если parallelization extract понадобится (>100 transcripts/run) — отдельный cycle на async batching

**Связь с CRM cycle 10:**
- voice_router.py в `crm/_scripts/` должен использовать тот же `_llm_client.py` — мигрировать в этом cycle если CRM уже ack'нут, иначе note в Open questions.

---

## §15. Технические детали launch

### Prerequisite
- CRM cycle 10 (build) должен быть закончен и ack'нут (commits push'нуты)
- ИЛИ если CRM cycle 10 ещё крутится — ждать его завершения (избегаем git conflicts)

### Pre-launch
```bash
ssh ruslan@100.99.156.28
cd ~/jetix-os
git fetch origin
git checkout claude/jolly-margulis-915d34
git pull --rebase
unset ANTHROPIC_API_KEY        # specifically для проверки чтобы migration работала без него
ulimit -n 65535
```

### Launch
```bash
tmux new -ds voice-migration-cycle
claude --dangerously-skip-permissions
# feed этот prompt полностью
# + одна строка:
# "Ты — бригадир. Веди swarm cycle per этот spec. После — AWAITING-APPROVAL packet per §11 в swarm/awaiting-approval/cycle-N-voice-migration-2026-04-26.md. Действуй per spec, не задавай clarifying questions кроме блокеров."
# Ctrl+B, D
```

### Monitor
`tmux attach -t voice-migration-cycle` → `Ctrl+B D`

### Expected duration
1-2 hours (smaller scope чем CRM build).

---

**End of deep prompt. Бригадир: ты можешь начинать когда CRM cycle 10 завершён + ack'нут.**
