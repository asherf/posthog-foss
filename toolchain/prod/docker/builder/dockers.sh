#!/usr/bin/env bash


set -euo pipefail

cd "$(git rev-parse --show-toplevel)"


# A no-op run of this is fast (< 1 second warm), so might as well always run it, to ensure an up to date image.
./toolchain/prod/docker/builder/build_builder_image.sh

bootstrap_cache=posthog_bootstrap_cache

if [[ -z $(docker volume ls -q --filter name=${bootstrap_cache}) ]]; then
  echo "Creating volume ${bootstrap_cache}"
  docker volume create ${bootstrap_cache}
fi

docker run \
  --mount type=bind,source="$(pwd)",target=/posthog/host_repo \
  --mount type=volume,src="${bootstrap_cache}",dst=/posthog/.cache \
  --rm \
  pexbuild:latest "$@"
