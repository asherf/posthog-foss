python_sources(
    dependencies=[
        "posthog"
    ]
)

pex_binary(
    name="gunicorn-app",
    entry_point="gunicorn_main.py",
    dependencies=[":app"]
)
