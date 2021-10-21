#!/usr/bin/env bash

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

my_host_uid=$(id -u)

docker build -t pexbuild --build-arg my_host_uid="${my_host_uid}" toolchain/prod/docker/builder
