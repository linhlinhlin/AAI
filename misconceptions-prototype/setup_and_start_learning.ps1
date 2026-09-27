param([int]$Port = 8766)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not (Test-Path -LiteralPath '.venv/Scripts/python.exe')) {
    & py -3.12 -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw 'Install Python 3.12 with the Windows py launcher first.' }
}
& .venv/Scripts/python.exe -m pip install -r requirements-lock.txt
if ($LASTEXITCODE -ne 0) { throw 'Dependency installation failed.' }
& .venv/Scripts/python.exe -m pip install --no-deps --no-build-isolation -e .
if ($LASTEXITCODE -ne 0) { throw 'Project installation failed.' }
& .venv/Scripts/python.exe scripts/setup_learning.py
if ($LASTEXITCODE -ne 0) { throw 'Open Docker Desktop with Linux engine, then try again.' }
Write-Host "Open http://127.0.0.1:$Port and sign in. Keep this terminal open."
& .venv/Scripts/python.exe -X utf8 -m misconceptions.learning_web --port $Port
exit $LASTEXITCODE
