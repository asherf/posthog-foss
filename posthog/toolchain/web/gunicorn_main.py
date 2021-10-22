import os
import django
from gunicorn.app.wsgiapp import WSGIApplication


class PosthogWSGIApplication(WSGIApplication):

    _WSGI_APP = "posthog.toolchain.app.wsgi:application"

    def load_config(self) -> None:
        self.cfg.set("default_proc_name", self._WSGI_APP)
        self.app_uri = self._WSGI_APP
        conf_path = "python:posthog.toolchain.app.gunicorn_conf"
        self.load_config_from_file(conf_path)
        self.cfg.set("config", conf_path)


def start():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "posthog.settings")
    django.setup()
    wsgi_app = PosthogWSGIApplication("")
    wsgi_app.run()


if __name__ == "__main__":
    start()
