$ErrorActionPreference = 'Stop'

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw 'Python is not available on PATH.'
}

python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip

Write-Host 'Environment ready.'
Write-Host 'Activate it with: .\.venv\Scripts\Activate.ps1'
