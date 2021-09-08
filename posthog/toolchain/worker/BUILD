python_sources(
    dependencies=[
        "posthog"
    ]
)

pex_binary(
    name="celery-worker",
    entry_point="celery_worker.py",
    dependencies=[":worker"]
)

pex_binary(
    name="celery-beat",
    entry_point="celery_beat.py",
    dependencies=[":worker"]
)
