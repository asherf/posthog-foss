import sys
from pathlib import Path

from celery.bin.celery import main as celery_main


def start():
    pid = Path("celerybeat.pid")
    if not pid.exists():
        sys.exit(celery_main(argv=["celery", "-A", "posthog", "beat", "-S", "redbeat.RedBeatScheduler"]))
    else:
        pid.unlink()


if __name__ == "__main__":
    start()
