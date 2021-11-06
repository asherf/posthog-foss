#!/usr/bin/env bash

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

IMAGE_TAG=posthog/web:latest
WORKDIR=toolchain/prod/docker
echo "Building Posthog Web image at rev ${IMAGE_TAG} ..."

# remote_tag="${IMAGE_REGISTRY:-}/posthog:web:${IMAGE_TAG:-dev}"
./toolchain/prod/docker/builder/dockers.sh package package posthog/toolchain/web:gunicorn-app
cp dist.docker/posthog.toolchain.web/gunicorn-app.pex "${WORKDIR}/gunicorn.pex"
docker build --file="${WORKDIR}/Dockerfile.web" "${WORKDIR}" -t "${IMAGE_TAG}"
