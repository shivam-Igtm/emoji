"""
Django settings for winx project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print ("base dir path", BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u*wo4(#z=*bh%0uh9-^ctj@!z0v-^i3qfbe^ajm9e588mh6*%v'

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
    'django_extensions',
    'winxapp'
    # 'dajaxice',
    # 'dajax'
]
# MEDIA_ROOT=os.path.join(BASE_DIR,"F:/Winx")
# MEDIA_URL = '/happy/'
MEDIA_URL = '/profile/'
MEDIA_ROOT = 'C:/Users/Miral/AppData/Local/Programs/Python/Python36/Lib/site-packages/django/winx/winxapp/static/winxapp/img/profile/'
#MEDIA_ROOT='C:/Users/Miral/AppData/Local/Programs/Python/Python36/Lib/site-packages/django/profile/'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

ROOT_URLCONF = 'winx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
# )

# TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.debug',
#    'django.core.context_processors.i18n',
#    'django.core.context_processors.media',
#    'django.core.context_processors.static',
#    'django.core.context_processors.request',
#    'django.contrib.messages.context_processors.messages'
# )

# STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'dajaxice.finders.DajaxiceFinder',
# )

# DAJAXICE_MEDIA_PREFIX = 'dajaxice'

WSGI_APPLICATION = 'winx.wsgi.application'
CSRF_COOKIE_SECURE = False

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases db.sqlite3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('C:/sqlite/database/', 'winx.db'),
    }
}
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    
]


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SERVER_EMAIL = 'miral1705@gmail.com'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_PASSWORD = 'passowrd'
# EMAIL_HOST_USER = SERVER_EMAIL
# # EMAIL_PORT = 587 465 25
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ADMINS = [    
#     ('name1', 'miral1705@gmail.com'),
# ]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
EMAIL_USE_SSL=True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'learn.code.all@gmail.com'
EMAIL_HOST_PASSWORD = 'learn123all'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIR='C:/Users/Miral/AppData/Local/Programs/Python/Python36/Lib/site-packages/django/winx/winxapp/static/'