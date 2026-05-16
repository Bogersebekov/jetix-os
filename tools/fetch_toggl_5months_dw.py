#!/usr/bin/env python3
"""Fetch full Toggl history Dec 2025 -> May 2026 via Reports API v2.
Produces per-month aggregates including Deep Work specifics:
- by_project_h (all projects)
- by_dw_tags_h (DW only, grouped by tag)
- by_dw_domain (DW only, grouped by domain tag)
- dw_entries (all DW entries for further drilldown)
"""
import json, time, sys, os, base64
from datetime import datetime, timedelta
from collections import defaultdict
import urllib.request, urllib.error

TOKEN_FILE = os.path.expanduser("~/.config/jetix/toggl_token")
TOKEN = open(TOKEN_FILE).read().strip()
WS = 8230895
USER_AGENT = "jetix-cli-5mo-dw"
OUT = "/home/ruslan/jetix-os/reports/toggl_5months_dw_2026-05-16.json"
PROGRESS = "/home/ruslan/jetix-os/reports/toggl_5months_dw_progress.txt"

# Project ID -> name (from existing repo script)
PROJECT_MAP = {
    211024855: "Deep Work",
    209390671: "Сон",
    211935863: "Рутина",
    209476030: "Ебланил",
    213911763: "Отдых",
    205971179: "Спорт",
    212070059: "Зарядка",
    209452431: "Гулял",
}

# DW domain tags (themes)
DOMAIN_TAGS = {
    "Tseren", "Jetix-foundation", "Jetix-workshop", "Jetix-corp", "Jetix-FPF",
    "video", "outreach", "monetization", "research", "self-os", "system",
    "Jetix", "Jetix-prinz",
}

# DW action prefix tags
ACTION_TAGS = {"SOZD", "OBR", "PODG", "RES", "ANL"}

auth = base64.b64encode(f"{TOKEN}:api_token".encode()).decode()


def log(msg):
    print(msg, flush=True)
    with open(PROGRESS, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def fetch_page(since, until, page):
    url = (
        "https://api.track.toggl.com/reports/api/v2/details"
        f"?workspace_id={WS}&since={since}&until={until}"
        f"&user_agent={USER_AGENT}&page={page}"
    )
    req = urllib.request.Request(url, headers={"Authorization": f"Basic {auth}"})
    try:
        r = urllib.request.urlopen(req, timeout=30)
        return json.loads(r.read()), None
    except urllib.error.HTTPError as e:
        return None, (e.code, e.read().decode()[:200])
    except Exception as e:
        return None, (0, str(e))


def fetch_window(since, until):
    """Fetch all entries in a window. Returns list of entries."""
    all_entries = []
    page = 1
    while True:
        data, err = fetch_page(since, until, page)
        if err:
            code, body = err
            if code == 429:
                log(f"  RATE LIMIT on {since}..{until} page {page} -- sleeping 70s")
                time.sleep(70)
                data, err = fetch_page(since, until, page)
                if err:
                    raise RuntimeError(f"persistent rate limit page {page}: {err}")
            else:
                raise RuntimeError(f"http_{code}_{body}")
        total = data.get("total_count", 0)
        per_page = data.get("per_page", 50)
        entries = data.get("data", [])
        all_entries.extend(entries)
        if page * per_page >= total or not entries:
            break
        page += 1
        time.sleep(1.3)
    return all_entries


def aggregate(entries, month):
    """Build aggregates for a month."""
    total_sec = sum(e.get("dur", 0) for e in entries) // 1000

    by_project = defaultdict(int)
    by_tags_all = defaultdict(int)
    dw_entries = []
    dw_by_tag = defaultdict(int)
    dw_by_domain = defaultdict(int)
    dw_by_action = defaultdict(int)

    for e in entries:
        pid = e.get("pid")
        pname = PROJECT_MAP.get(pid, e.get("project") or f"unknown_{pid}")
        dur_sec = e.get("dur", 0) // 1000
        by_project[pname] += dur_sec
        tags = e.get("tags") or []
        for tg in tags:
            by_tags_all[tg] += dur_sec
        if pname == "Deep Work":
            dw_entries.append({
                "start": e.get("start", "")[:19],
                "dur_h": round(e.get("dur", 0) / 3600000, 3),
                "desc": (e.get("description") or "")[:200],
                "tags": tags,
            })
            for tg in tags:
                dw_by_tag[tg] += dur_sec
            for tg in tags:
                if tg in DOMAIN_TAGS:
                    dw_by_domain[tg] += dur_sec
                if tg in ACTION_TAGS:
                    dw_by_action[tg] += dur_sec
            if not any(t in DOMAIN_TAGS for t in tags):
                dw_by_domain["__no_domain"] += dur_sec
            if not any(t in ACTION_TAGS for t in tags):
                dw_by_action["__no_action"] += dur_sec

    def h(sec):
        return round(sec / 3600, 3)

    return {
        "month": month,
        "entries_count": len(entries),
        "total_hours": h(total_sec),
        "by_project_h": {k: h(v) for k, v in sorted(by_project.items(), key=lambda x: -x[1])},
        "by_tags_h": {k: h(v) for k, v in sorted(by_tags_all.items(), key=lambda x: -x[1])},
        "dw_total_h": h(by_project.get("Deep Work", 0)),
        "dw_entries_count": len(dw_entries),
        "dw_by_tag_h": {k: h(v) for k, v in sorted(dw_by_tag.items(), key=lambda x: -x[1])},
        "dw_by_domain_h": {k: h(v) for k, v in sorted(dw_by_domain.items(), key=lambda x: -x[1])},
        "dw_by_action_h": {k: h(v) for k, v in sorted(dw_by_action.items(), key=lambda x: -x[1])},
        "dw_entries": dw_entries,
    }


def month_window(y, m):
    if m == 12:
        nxt_y, nxt_m = y + 1, 1
    else:
        nxt_y, nxt_m = y, m + 1
    since = f"{y:04d}-{m:02d}-01"
    until = (datetime(nxt_y, nxt_m, 1) - timedelta(days=1)).strftime("%Y-%m-%d")
    return since, until


def main():
    if os.path.exists(PROGRESS):
        os.remove(PROGRESS)
    log(f"START {datetime.now().isoformat()}")

    state = {
        "fetched_at": datetime.now().isoformat(),
        "method": "Reports API v2 (single-month windowed, paginated)",
        "window": "2025-12-01 → 2026-05-16",
        "months": {},
        "errors": {},
    }

    months = [(2025, 12), (2026, 1), (2026, 2), (2026, 3), (2026, 4)]
    for y, m in months:
        since, until = month_window(y, m)
        key = f"{y:04d}-{m:02d}"
        log(f"FETCH {key} ({since}..{until})")
        try:
            entries = fetch_window(since, until)
            agg = aggregate(entries, key)
            state["months"][key] = agg
            log(f"  OK {key}: total={agg['total_hours']}h, DW={agg['dw_total_h']}h, entries={agg['entries_count']} (DW={agg['dw_entries_count']})")
        except Exception as e:
            state["errors"][key] = str(e)
            log(f"  ERR {key}: {e}")
        # save state after each month
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        time.sleep(1.5)

    # May 2026 partial: 2026-05-01 → 2026-05-16
    log("FETCH 2026-05 partial (2026-05-01..2026-05-16)")
    try:
        entries = fetch_window("2026-05-01", "2026-05-16")
        agg = aggregate(entries, "2026-05")
        agg["partial"] = True
        agg["partial_window"] = "2026-05-01 → 2026-05-16"
        state["months"]["2026-05"] = agg
        log(f"  OK 2026-05: total={agg['total_hours']}h, DW={agg['dw_total_h']}h, entries={agg['entries_count']} (DW={agg['dw_entries_count']})")
    except Exception as e:
        state["errors"]["2026-05"] = str(e)
        log(f"  ERR 2026-05: {e}")

    # summary
    grand_total = sum(m["total_hours"] for m in state["months"].values())
    grand_dw = sum(m["dw_total_h"] for m in state["months"].values())
    state["summary"] = {
        "grand_total_hours": round(grand_total, 2),
        "grand_dw_hours": round(grand_dw, 2),
        "months_with_data": len(state["months"]),
        "months_failed": list(state["errors"].keys()),
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    log(f"\nDONE {datetime.now().isoformat()}")
    log(f"Grand total: {grand_total:.2f}h, Grand DW: {grand_dw:.2f}h")
    if state["errors"]:
        log(f"Failed: {list(state['errors'].keys())}")


if __name__ == "__main__":
    main()
