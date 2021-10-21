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
./toolchain/prod/docker/builder/dockers.sh package package posthog/toolchain/web:gunicorn-app
cp dist.docker/posthog.toolchain.web/gunicorn-app.pex "${WORKDIR}/gunicorn.pex"

# remote_tag="${IMAGE_REGISTRY:-}/posthog:web:${IMAGE_TAG:-dev}"
echo "Building Posthog Web image at rev ${IMAGE_TAG} ..."
docker build --file="${WORKDIR}/Dockerfile.web" "${WORKDIR}" -t "${IMAGE_TAG}"
