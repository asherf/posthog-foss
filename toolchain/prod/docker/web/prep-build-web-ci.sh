#!/usr/bin/env bash

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

IMAGE_TAG=posthog/web:latest
WORKDIR=toolchain/prod/docker/web

echo "Build frontend web app"
yarn --frozen-lockfile
yarn build
rm -rf "${WORKDIR}/frontend-dist"
mkdir "${WORKDIR}/frontend-dist"
cp -r "frontend/dist/" "${WORKDIR}/frontend-dist"

echo "Build gunicorn PEX"
./pants package package posthog/toolchain/web:gunicorn-app
cp dist.docker/posthog.toolchain.web/gunicorn-app.pex "${WORKDIR}/gunicorn.pex"