FROM python:3.8.12-slim-buster@sha256:7e732593f25983fa7d4b2d54444be4a785f2397c1cf2f815d2e3638337eee012


ARG my_host_uid

# Binaries needed to bootstrap and run Pants.
# Git is needed so pants can get version information into PEX-INFO

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    curl gcc libssl-dev git unzip python3-distutils python3-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# For DRY in this file, not intended to be overridden at build time.
ARG posthog_repo=/posthog/host_repo
ARG posthog_bootstrap_cache=/posthog/.cache

RUN mkdir /toolchain && \
    useradd --no-log-init -u ${my_host_uid} --user-group --home /posthog posthog && \
    chown posthog:posthog /posthog && \
    mkdir ${posthog_bootstrap_cache} && \
    chown posthog:posthog ${posthog_bootstrap_cache}

USER posthog

# Mount point for the host's toolchain repo, so we can build directly from the host's source files.
VOLUME ${posthog_repo}

# Mount point for the pants bootstrap cache, so we can conserve it between container runs.
VOLUME ${posthog_bootstrap_cache}

WORKDIR ${posthog_repo}

ENV PANTS_WORKDIR="${posthog_repo}/.docker.pants.d" PANTS_DISTDIR="${posthog_repo}/dist.docker"
ENV PANTS_BUILD_IGNORE="+['/${PANTS_DISTDIR}/']" PANTS_IGNORE="+['/${PANTS_DISTDIR}']"

# TODO: Figure out why pantsd won't run in the container.
ENV PANTS_PANTSD=false

ENTRYPOINT ["./pants", "--no-dynamic-ui"]
