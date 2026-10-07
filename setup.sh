#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip

echo "Environment ready."
echo "Activate it with: source .venv/bin/activate"
