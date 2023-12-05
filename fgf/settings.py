from pathlib import Path
import os

# from dj_rest_authallauth import *
import dj_database_url
import datetime
from datetime import timedelta
from .utils.authentication_extensions import AuthTokenAuthenticationExtension
from decouple import config

import dotenv
import environ

env = environ.Env()
environ.Env.read_env()

dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# settings.py
SECRET_KEY = config("DJANGO_SECRET_KEY", default="default_secret_key")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = bool(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = ["*"]
# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "plants_app",
    "animals_app",
    "cultures_app",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "corsheaders",
    "bootstrap4",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    #'allauth.account.auth_backends.AuthenticationBackend',
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    # Add the allowed origins (e.g., frontend URLs)
    "https://fgf-project-frontend.vercel.app",
    "http://localhost:5173",
    "http://localhost:8000",
    "https://render.com",
    "https://fgf-app.onrender.com",
    "https://3.75.158.163",
    "https://3.125.183.140",
    "https://35.157.117.28",
]


CORS_ORIGIN_WHITELIST = [
    "http://localhost:5173",
]


ROOT_URLCONF = "fgf.urls"

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}

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

WSGI_APPLICATION = "fgf.wsgi.application"

from rest_framework.permissions import AllowAny

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_authtoken.auth.AuthTokenAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}


# Domain names to be used
SITE_ID = 1
REST_USE_JWT = True


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASE SETTING

# DATABASES = {
#     "default": {
#         "ENGINE": config("DB_ENGINE"),
#         "NAME": config("DB_NAME", default=""),
#         "USER": config("DB_USER", default=""),
#         "PASSWORD": config("DB_PASSWORD", default=""),
#         "HOST": config("DB_HOST", default=""),
#         "PORT": config("DB_PORT", default=""),
#     }
# }


# Other settings...
DATABASES = {"default": dj_database_url.config(default=config("DATABASE_URL"))}

ATOMIC_REQUESTS = False

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# FOR deployment
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
