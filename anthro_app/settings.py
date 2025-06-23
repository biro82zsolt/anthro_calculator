import os
from pathlib import Path

# Alap elérési út
BASE_DIR = Path(__file__).resolve().parent.parent

# Titkos kulcs (fejlesztéshez jó ez is)
SECRET_KEY = "django-insecure-anthropometry-very-secret-key"

# Debug fejlesztéshez legyen True
DEBUG = True

ALLOWED_HOSTS = []

# Appok
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "admin_panel",
    "landing",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL dispatcher
ROOT_URLCONF = "anthro_app.urls"

# Sablonbeállítások
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # ha van külső sablonkönyvtár
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

WSGI_APPLICATION = "anthro_app.wsgi.application"

# Adatbázis (SQLite alapértelmezetten)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Jelszó validáció fejlesztéshez lehet kikapcsolni
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
]

# Nyelv és időzóna
LANGUAGE_CODE = "hu-hu"
TIME_ZONE = "Europe/Budapest"

USE_I18N = True
USE_TZ = True

# Statikus fájlok
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # új

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

EXPORTED_DIR = os.path.join(BASE_DIR, "exported")

# Alkalmazás alapértelmezett mezőtípusa
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # <– ez legyen a legelsők között
    ...
]


