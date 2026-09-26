$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not (Test-Path -LiteralPath '.venv/Scripts/python.exe')) {
    throw 'Create .venv and install requirements-lock.txt first. See ../docs/learning_app.md.'
}
& .venv/Scripts/python.exe -X utf8 -m misconceptions.learning_web @args
