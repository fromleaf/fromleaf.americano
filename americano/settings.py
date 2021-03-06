# -*- coding: utf-8 -*-

"""
Django settings for americano project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import logging
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q$sy=(056859pj5r=)cj7oj!%oico%zw8ahkq6u!ts2y3m0eb%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    # our apps
    'ame_common',
    'ame_home',
    'ame_play',
    'ame_ml',

    # third party apps
    'storages',
    'debug_toolbar',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ame_common.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'ame_common/templates/ame_common')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'americano.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'ameri_db',
    #     'USER': 'postgres',
    #     'PASSWORD': '1379youn',
    #     'HOST': 'localhost',
    #     'PORT': '5432',
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ameri_db',
        'USER': 'root',
        'PASSWORD': 'Android13@(',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
AUTH_USER_MODEL = 'ame_common.User'
SESSION_COOKIE_AGE = 14515200


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = False

USE_L10N = False

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'


if DEBUG:
    STATICFILES_DIRS = [
        # if you want to set other STATICFILE_DIRS, you have to set here.
        # However, you have to set the other STATIC_ROOR path
        # ex) os.path.join(BASE_DIR, 'somewhere')
        os.path.join(BASE_DIR, 'static'),
        os.path.join(BASE_DIR, 'static/assets'),
    ]
else:
    STATIC_ROOT = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': './logs/logs.log',
            'maxBytes': 1024000,
            'backupCount': 3,
        },
        'sql': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': './logs/sql.log',
            'maxBytes': 102400,
            'backupCount': 3,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console',],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['sql', 'console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'scheduling': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.template': {
            'handlers': ['console'],  # Quiet by default!
            'propagate': False,
            'level': 'WARNING',
        },
    }
}

ENG_VERSION = True

if DEBUG:
    # will output to your console
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s %(levelname)s %(message)s',
    )
# logging.getLogger('boto').setLevel(logging.INFO)
# logging.getLogger('PIL').setLevel(logging.INFO)

else:
    logging.getLogger('boto').setLevel(logging.CRITICAL)
    logging.getLogger('django.db.backends').setLevel(logging.CRITICAL)