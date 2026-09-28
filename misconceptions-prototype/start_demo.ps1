param([int]$Port = 8767)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$demoPython = Join-Path $PSScriptRoot '.venv/Scripts/python.exe'
$demoData = Join-Path $PSScriptRoot '../.cache/course-demo'
if (-not (Test-Path -LiteralPath $demoPython)) {
    throw 'Install the project .venv first. See ../docs/demo_nghiem_thu.md.'
}
if (-not (Test-Path -LiteralPath (Join-Path $demoData 'demo_manifest.json'))) {
    & $demoPython -X utf8 scripts/prepare_learning_demo.py
    if ($LASTEXITCODE -ne 0) { throw 'Demo preparation failed; existing data was preserved.' }
}
if (-not (Test-Path -LiteralPath (Join-Path $demoData 'learning.sqlite3'))) {
    throw 'Demo database is missing. See ../docs/demo_nghiem_thu.md before preparing again.'
}
Write-Host "DEMO ONLY - authored examples, separate database. Open http://127.0.0.1:$Port"
Write-Host 'Student: demo_student | Teacher: demo_teacher | Password: Demo-AAI-2026!'
& $demoPython -X utf8 -m misconceptions.learning_web --port $Port --data-dir $demoData
exit $LASTEXITCODE
