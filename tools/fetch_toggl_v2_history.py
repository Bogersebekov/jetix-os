#!/usr/bin/env python3
"""Fetch full Toggl history via Reports API v2 (legacy, supports paginated full history).
Saves incremental state per month to avoid losing progress on rate-limit."""
import json, time, sys, os, base64
from datetime import datetime, timedelta
import urllib.request, urllib.error

TOKEN = "3ad53e9d8a06eee0dca1963e18654408"
WS = 8230895
USER_AGENT = "jetix-cli"
OUT = r"C:\Users\49152\Desktop\jetix-os\reports\toggl_full_history_v2_2026-05-03.json"
PROGRESS = r"C:\Users\49152\Desktop\jetix-os\reports\toggl_fetch_progress.txt"

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

auth = base64.b64encode(f"{TOKEN}:api_token".encode()).decode()

def fetch_page(since, until, page):
    url = f"https://api.track.toggl.com/reports/api/v2/details?workspace_id={WS}&since={since}&until={until}&user_agent={USER_AGENT}&page={page}"
    req = urllib.request.Request(url, headers={"Authorization": f"Basic {auth}"})
    try:
        r = urllib.request.urlopen(req, timeout=30)
        return json.loads(r.read()), None
    except urllib.error.HTTPError as e:
        return None, (e.code, e.read().decode()[:200])
    except Exception as e:
        return None, (0, str(e))

def fetch_month(year, month):
    if month == 12:
        nxt_y, nxt_m = year+1, 1
    else:
        nxt_y, nxt_m = year, month+1
    since = f"{year:04d}-{month:02d}-01"
    until = (datetime(nxt_y, nxt_m, 1) - timedelta(days=1)).strftime("%Y-%m-%d")

    all_entries = []
    page = 1
    while True:
        data, err = fetch_page(since, until, page)
        if err:
            code, body = err
            if code == 429:
                # rate limit - wait and retry once
                with open(PROGRESS, "a", encoding="utf-8") as p:
                    p.write(f"  RATE LIMIT on {since} page {page} -- sleeping 70s\n")
                time.sleep(70)
                data, err = fetch_page(since, until, page)
                if err:
                    return None, f"rate_limit_persistent_page_{page}"
            else:
                return None, f"http_{code}_{body}"
        total = data.get("total_count", 0)
        per_page = data.get("per_page", 50)
        entries = data.get("data", [])
        all_entries.extend(entries)
        if page * per_page >= total or not entries:
            break
        page += 1
        time.sleep(1.3)

    # aggregate
    total_sec = sum(e.get("dur", 0) for e in all_entries) // 1000  # dur is ms
    by_project = {}
    by_tags = {}
    for e in all_entries:
        pid = e.get("pid")
        pname = PROJECT_MAP.get(pid, e.get("project") or f"unknown_{pid}")
        by_project.setdefault(pname, 0)
        by_project[pname] += e.get("dur", 0) // 1000
        for tg in (e.get("tags") or []):
            by_tags.setdefault(tg, 0)
            by_tags[tg] += e.get("dur", 0) // 1000

    # top 20 entries by duration
    top20 = sorted(all_entries, key=lambda e: e.get("dur", 0), reverse=True)[:20]
    top20_short = [{
        "start": e.get("start", "")[:19],
        "dur_h": round(e.get("dur", 0)/3600000, 2),
        "project": PROJECT_MAP.get(e.get("pid"), e.get("project") or "?"),
        "desc": (e.get("description") or "")[:120],
        "tags": e.get("tags") or [],
    } for e in top20]

    return {
        "month": since[:7],
        "since": since,
        "until": until,
        "entries_count": len(all_entries),
        "total_hours": round(total_sec/3600, 2),
        "by_project_h": {k: round(v/3600, 2) for k, v in sorted(by_project.items(), key=lambda x: -x[1])},
        "by_tags_h": {k: round(v/3600, 2) for k, v in sorted(by_tags.items(), key=lambda x: -x[1])},
        "top20_entries": top20_short,
    }, None

def main():
    # months 2025-05 → 2026-04 (12 months)
    months = []
    y, m = 2025, 5
    for _ in range(12):
        months.append((y, m))
        m += 1
        if m == 13:
            m = 1
            y += 1

    state = {
        "fetched_at": "2026-05-03",
        "method": "Reports API v2",
        "months": {},
        "errors": {},
    }
    # restore prior partial if exists
    if os.path.exists(OUT):
        try:
            with open(OUT, "r", encoding="utf-8") as f:
                prior = json.load(f)
            state["months"] = prior.get("months", {})
            state["errors"] = prior.get("errors", {})
        except: pass

    with open(PROGRESS, "w", encoding="utf-8") as p:
        p.write(f"START {datetime.now().isoformat()}\n")

    for y, m in months:
        key = f"{y:04d}-{m:02d}"
        if key in state["months"]:
            with open(PROGRESS, "a", encoding="utf-8") as p:
                p.write(f"SKIP {key} (already done: {state['months'][key]['total_hours']}h)\n")
            continue
        with open(PROGRESS, "a", encoding="utf-8") as p:
            p.write(f"FETCH {key} ...\n")
        result, err = fetch_month(y, m)
        if err:
            state["errors"][key] = err
            with open(PROGRESS, "a", encoding="utf-8") as p:
                p.write(f"  ERR {key}: {err}\n")
        else:
            state["months"][key] = result
            with open(PROGRESS, "a", encoding="utf-8") as p:
                p.write(f"  OK  {key}: {result['total_hours']}h, {result['entries_count']} entries\n")
        # save state after each month
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        time.sleep(1.5)

    # summary
    grand_total = sum(m["total_hours"] for m in state["months"].values())
    by_proj_total = {}
    for m in state["months"].values():
        for p, h in m.get("by_project_h", {}).items():
            by_proj_total.setdefault(p, 0)
            by_proj_total[p] += h
    state["summary"] = {
        "grand_total_hours": round(grand_total, 2),
        "months_with_data": len(state["months"]),
        "months_failed": list(state["errors"].keys()),
        "by_project_aggregated_h": {k: round(v, 2) for k, v in sorted(by_proj_total.items(), key=lambda x: -x[1])},
        "avg_h_per_month": round(grand_total/max(len(state["months"]),1), 2),
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    with open(PROGRESS, "a", encoding="utf-8") as p:
        p.write(f"\nDONE {datetime.now().isoformat()}\n")
        p.write(f"Grand total: {grand_total:.2f}h across {len(state['months'])} months\n")
        if state["errors"]:
            p.write(f"Failed months: {list(state['errors'].keys())}\n")

if __name__ == "__main__":
    main()
