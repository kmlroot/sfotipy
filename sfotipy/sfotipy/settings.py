"""
Django settings for sfotipy project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=co4iulhwj97_u8z@53^2#k)r6-46i@u+$$6=%=qavn6bcmxbw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['']

# Application definition

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    "django.core.context_processors.request",
    "sfotipy.context_processors.basico",
)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}

GRAPPELLI_ADMIN_TITLE = 'Sfotipy'

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'albums',
    'artists',
    'django_extensions',
    'mockups',
    'rest_framework',
    'tracks',
    'userprofiles',
    'sorl.thumbnail',
)

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'sfotipy.middleware.PaisMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
)


ROOT_URLCONF = 'sfotipy.urls'

WSGI_APPLICATION = 'sfotipy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'OPTIONS': {
            'DB': 1,
            # 'PASSWORD': 'mypass',
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        }
    }    
}

# CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
 
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'


MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['content'])
MEDIA_URL = '/media/'

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

#Backends
# AUTHENTICATION_BACKENDS = (
#     'userprofiles.backends.EmailBackend',
# )

import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://localhost:6379/0'
