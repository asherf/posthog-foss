from __future__ import annotations

import os
import uuid

DEBUG = True
EE_AVAILABLE = False
PLUGINS_RELOAD_PUBSUB_CHANNEL = "reload-plugins"
ACTION_EVENT_MAPPING_INTERVAL_SECONDS = 300
EVENT_PROPERTY_USAGE_INTERVAL_SECONDS = 60 * 60
UPDATE_CACHED_DASHBOARD_ITEMS_INTERVAL_SECONDS = 90
ASYNC_EVENT_PROPERTY_USAGE = False
CLICKHOUSE_REPLICATION = False
MULTI_TENANCY = False
SECRET_KEY = f"fake-collect-static-fake-{uuid.uuid4()}"


INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",  # makes sure that whitenoise handles static files in development
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.postgres",
    "django.contrib.staticfiles",
    "posthog.apps.PostHogConfig",
    "rest_framework",
    "loginas",
    "corsheaders",
    "social_django",
    "django_filters",
    "axes",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "posthog.middleware.AllowIP",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "posthog.middleware.ToolbarCookieMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "posthog.middleware.CsrfOrKeyViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "posthog.middleware.CSVNeverCacheMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "axes.middleware.AxesMiddleware",
]


# Max size of a POST body (for event ingestion)
DATA_UPLOAD_MAX_MEMORY_SIZE = 20971520  # 20 MB

ROOT_URLCONF = "posthog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["frontend/dist", "posthog/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "posthog.wsgi.application"

# Social Auth

SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_USER_MODEL = "posthog.User"
# SOCIAL_AUTH_REDIRECT_IS_HTTPS = get_from_env("SOCIAL_AUTH_REDIRECT_IS_HTTPS", not DEBUG, type_cast=str_to_bool)

AUTHENTICATION_BACKENDS: list[str] = [
    "axes.backends.AxesBackend",
    "social_core.backends.github.GithubOAuth2",
    "social_core.backends.gitlab.GitLabOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]


DATABASE_URL = "postgres:///"
REDIS_URL = "redis:///"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
]

PASSWORD_RESET_TIMEOUT = 86_400  # 1 day

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_ROOT = "/staticfiles"
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    "frontend/dist",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

EXCEPTIONS_HOG = {
    "EXCEPTION_REPORTING": "posthog.exceptions.exception_reporting",
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler",},},
    "root": {"handlers": ["console"], "level": os.getenv("DJANGO_LOG_LEVEL", "WARNING")},
    "loggers": {
        "django": {"handlers": ["console"], "level": os.getenv("DJANGO_LOG_LEVEL", "WARNING"), "propagate": True,},
        "axes": {"handlers": ["console"], "level": "WARNING", "propagate": False},
        "statsd": {"handlers": ["console"], "level": "WARNING", "propagate": True,},
    },
}
