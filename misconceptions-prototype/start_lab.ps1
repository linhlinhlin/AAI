param([int]$Port = 8770, [switch]$NoBrowser)
# AAI Lab: one local app for the class view, trial runs, C-Pack cohorts and the study results.
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not (Test-Path -LiteralPath '.venv/Scripts/python.exe')) {
    & py -3.12 -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw 'Install Python 3.12 with the Windows py launcher first.' }
    & .venv/Scripts/python.exe -m pip install -r requirements-lock.txt
    if ($LASTEXITCODE -ne 0) { throw 'Dependency installation failed.' }
    & .venv/Scripts/python.exe -m pip install --no-deps --no-build-isolation -e .
    if ($LASTEXITCODE -ne 0) { throw 'Project installation failed.' }
}
$docker = Get-Command docker -ErrorAction SilentlyContinue
if ($docker) {
    # Windows PowerShell turns redirected native stderr into errors; 'Stop' would abort here.
    $ErrorActionPreference = 'Continue'
    & docker image inspect aai-c-runner:1 *> $null
    $missing = $LASTEXITCODE -ne 0
    $ErrorActionPreference = 'Stop'
    if ($missing) {
        & .venv/Scripts/python.exe scripts/setup_learning.py
        if ($LASTEXITCODE -ne 0) { Write-Warning 'Docker is not ready: trial runs stay off until Docker Desktop is running.' }
    }
} else {
    Write-Warning 'Docker is not installed: trial runs stay off; class, C-Pack and study views still work.'
}
Write-Host "AAI Lab: http://127.0.0.1:$Port  (keep this window open; Ctrl+C stops the app)"
$arguments = @('-X', 'utf8', '-m', 'misconceptions.lab', '--port', $Port)
if ($NoBrowser) { $arguments += '--no-browser' }
& .venv/Scripts/python.exe @arguments
exit $LASTEXITCODE
