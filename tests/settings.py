DEBUG = True

USE_TZ = True

SECRET_KEY = 'test key'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

ROOT_URLCONF = "redis_views.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "redis_views",
]

SITE_ID = 1
MIDDLEWARE_CLASSES = ()
REDIS_URL = 'redis://localhost:6379/0'
