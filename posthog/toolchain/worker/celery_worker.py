import sys

from celery.bin.celery import main as celery_main


def start():
    if "--with-scheduler" in sys.argv:
        print("RUN CELERY BEAT")
    # import ipdb; ipdb.set_trace()
    sys.exit(celery_main(argv=["celery", "-A", "posthog", "worker"]))


if __name__ == "__main__":
    start()
