# export_activitywatch.ps1 — Daily ActivityWatch JSON export + scp to server
#
# Run via Windows Task Scheduler at end of work day (e.g. 23:55).
# Connects to local ActivityWatch REST API, exports today's events,
# saves JSON to %LOCALAPPDATA%\activitywatch-export\, scp's to Jetix server.
#
# Prerequisites:
#   1. ActivityWatch installed and running (auto-starts on Windows boot)
#   2. SSH key configured for ruslan@100.99.156.28 (passwordless)
#   3. Server has ~/jetix-os/raw/activitywatch/json/ directory
#
# Manual run:
#   pwsh -ExecutionPolicy Bypass -File export_activitywatch.ps1

$ErrorActionPreference = "Stop"

# Config
$AW_HOST = "http://localhost:5600"
$EXPORT_DIR = "$env:LOCALAPPDATA\activitywatch-export"
$DATE = Get-Date -Format "yyyy-MM-dd"
$EXPORT_FILE = "$EXPORT_DIR\$DATE.json"
$SERVER_USER = "ruslan"
$SERVER_HOST = "100.99.156.28"
$SERVER_PATH = "~/jetix-os/raw/activitywatch/json/"

# Ensure export dir
New-Item -ItemType Directory -Force -Path $EXPORT_DIR | Out-Null

Write-Host "ActivityWatch export starting for $DATE..."

# 1. Get list of buckets
try {
    $buckets = Invoke-RestMethod -Uri "$AW_HOST/api/0/buckets/" -Method Get
} catch {
    Write-Error "Cannot reach ActivityWatch at $AW_HOST. Is it running? Error: $_"
    exit 1
}

# 2. For each bucket, fetch today's events
$start = "${DATE}T00:00:00Z"
$end = "${DATE}T23:59:59Z"

$exportData = @{
    "export_date" = $DATE
    "exported_at" = (Get-Date).ToString("o")
    "host" = $env:COMPUTERNAME
    "buckets" = @{}
}

foreach ($bucketName in $buckets.PSObject.Properties.Name) {
    Write-Host "  Fetching bucket: $bucketName"
    try {
        $eventsUri = "$AW_HOST/api/0/buckets/$bucketName/events?start=$start&end=$end&limit=10000"
        $events = Invoke-RestMethod -Uri $eventsUri -Method Get

        $exportData.buckets[$bucketName] = @{
            "events" = $events
            "event_count" = $events.Count
        }
    } catch {
        Write-Warning "Failed bucket $bucketName : $_"
        $exportData.buckets[$bucketName] = @{ "error" = $_.ToString() }
    }
}

# 3. Save JSON locally
$exportData | ConvertTo-Json -Depth 10 -Compress | Out-File -FilePath $EXPORT_FILE -Encoding UTF8
Write-Host "Saved $EXPORT_FILE ($((Get-Item $EXPORT_FILE).Length) bytes)"

# 4. scp to server
Write-Host "Uploading to $SERVER_USER@$SERVER_HOST..."
& scp $EXPORT_FILE "${SERVER_USER}@${SERVER_HOST}:${SERVER_PATH}"

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Upload OK"

    # 5. Trigger server-side aggregation (optional — comment out if cron'ing)
    Write-Host "Triggering server-side aggregation..."
    & ssh "${SERVER_USER}@${SERVER_HOST}" "cd ~/jetix-os && python3 tools/aggregate_activity.py $DATE"

    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Aggregation done. Report: ~/jetix-os/reports/activity_$DATE.md"
    } else {
        Write-Warning "Aggregation failed but JSON uploaded. Run manually on server."
    }
} else {
    Write-Error "scp failed (exit $LASTEXITCODE). JSON saved locally at $EXPORT_FILE."
    exit 1
}

Write-Host "Done."
