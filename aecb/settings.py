"""
Django settings for aecb project.

Generated by "django-admin startproject" using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

ENV = os.environ.get("DJANGO_ENV", "development")

if ENV is None:
    raise Exception("Missing ENV variable, make sure to add the .env file")

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "SK")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV == "development"

ALLOWED_HOSTS_LIST = os.environ.get("DJANGO_ALLOWED_HOSTS")
ALLOWED_HOSTS = ALLOWED_HOSTS_LIST.split(",") if ALLOWED_HOSTS_LIST is not None else ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "aecb.api",
    "django_seed",
    "corsheaders"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware"
]

ROOT_URLCONF = "aecb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "aecb.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DJANGO_DB_BACKEND", "django.db.backends.postgresql"),
        "NAME": os.environ.get("DJANGO_DB_NAME", "aecb"),
        "USER": os.environ.get("DJANGO_DB_USER", "aecb"),
        "PASSWORD": os.environ.get("DJANGO_DB_PASSWORD", "aecb"),
        "HOST": os.environ.get("DJANGO_DB_HOST", "localhost"),
        "PORT": os.environ.get("DJANGO_DB_PORT", 5432)
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Cors configuration
# https://github.com/ottoyiu/django-cors-headers/#configuration

# If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOWED_ORIGINS_LIST  = os.environ.get("DJANGO_CORS_ALLOWED_ORIGINS")
#CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS_LIST.split(",") if not CORS_ORIGIN_ALLOW_ALL else []
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "token",
    "admin-email"
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.environ.get(
    "DJANGO_STATIC_ROOT", os.path.join(BASE_DIR, "static"))
STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media
MEDIA_ROOT = os.environ.get(
    "DJANGO_MEDIA_ROOT", os.path.join(BASE_DIR, "media"))
MEDIA_URL = "/media/"

# Custom settings
ADMIN_DOMAIN = os.environ.get("DJANGO_ADMIN_DOMAIN", "alumnos.udg.mx")
AECB_EXTERNAL_API = os.environ.get("AEBC_EXTERNAL_API_ENDPOINT", "http://localhost:8080")
