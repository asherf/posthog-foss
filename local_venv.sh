#!/bin/bash
set -euo pipefail

eval "$(pyenv init --path)"
eval "$(pyenv init -)"
pyenv global 3.8.12
python3 --version
rm -rf .venv
python3 -m venv .venv
.venv/bin/pip3 install -U pip 
.venv/bin/pip3 install -r requirements.txt
.venv/bin/pip3 install -r requirements-dev.txt
#source .venv/bin/activate
#running: python3 -m posthog.app.gunicorn_main
