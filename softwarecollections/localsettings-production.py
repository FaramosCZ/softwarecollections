# -*- coding: utf-8 -*-
# vim: ft=python

"""
Django settings for softwarecollections project.

Generated by 'django-admin startproject' using Django 1.9.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# import ugettext_lazy to avoid circular module import
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = '/var/scls'

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'secret_key'), 'rb') as f:
    SECRET_KEY = repr(f.read())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG   = os.environ.get('DEBUG', False) and True or False
DBDEBUG = os.environ.get('DEBUG', '') == 'DB'

ALLOWED_HOSTS = ['www.softwarecollections.org']

# Emails
# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-ADMINS
# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-MANAGERS
# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-SERVER_EMAIL
ADMINS = (
    ('Jakub Dorňák',   'jakub.dornak@misli.cz'),
    ('Miroslav Suchý', 'msuchy@redhat.com'),
    ('Adam Samalik',   'asamalik@redhat.com'),
)
MANAGERS = ADMINS
SERVER_EMAIL = 'SoftwareCollections @ {} <admin@softwarecollections.org>'.format(os.uname()[1])

# COPR
COPR_URL = 'https://copr.fedorainfracloud.org'
COPR_API_URL   = COPR_URL + '/api'
COPR_COPRS_URL = COPR_URL + '/coprs'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '/var/scls/db',
        'PORT': 5432,
        'USER': 'softwarecollections',
        'NAME': 'softwarecollections',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

LANGUAGES = (
    ('en', 'English'),
    #('cs', 'Čeština'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'htdocs', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'htdocs', 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Absolute path to the directory repos should be synced to.
REPOS_ROOT = os.path.join(BASE_DIR, 'htdocs', 'repos')

# URL prefix for repo.
REPOS_URL  = '/repos/'

# Absolute path to the directory used by yum cache
YUM_CACHE_ROOT = '/tmp/softwarecollections-yum-cache'

# Absolute path to the directory to be used as rpm _topdir
RPMBUILD_TOPDIR = '/tmp/softwarecollections-rpmbuild'

