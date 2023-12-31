"""
Django settings for project_structure project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# import json

# with open('/etc/config.json') as config_file:
#     config = json.load(config_file)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config['SECRET_KEY']

SECRET_KEY = 'django-insecure-d*_@dvi^g6%!&dln=76=l1ok4=hl+$clzu&&^dz472z^!80r+h'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# CSRF_TRUSTED_ORIGINS = ['https://www.squaak.net','https://squaak.net', 'http://127.0.0.1']

# SECURE_CROSS_ORIGIN_OPENER_POLICY = None

# Application definition

INSTALLED_APPS = [
    # My apps.
    'users',
    'friend',
    'pages',
    'videochat',
    'messaging',
    # 3rd party apps.
    'crispy_forms',
    'bootstrap4',
    'channels',
    # Base apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Notifications app after django.contrib.auth.
    'notifications',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_structure.urls'

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

WSGI_APPLICATION = 'project_structure.wsgi.application'
# ASGI_APPLICATION = 'project_structure.asgi.application'

# CHANNEL_LAYERS = {
#     'default':{
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             'hosts': [('localhost', '6379')],
#         },
#     },
# }

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


import environ
env = environ.Env() # set default values and casting
environ.Env.read_env()

import dj_database_url
# # import env
DATABASES={
     'default' :  dj_database_url.parse('postgres://shrey:QVisCefMX1OZ0r7apZUS5AENe4yv7HKD@dpg-cjne1cmqdesc739hb7ug-a.singapore-postgres.render.com/portdb_nrrc')
            }

# Password validation

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

# single root directory from where the Django application will serve the static files in production.
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Where our uploaded files will be located on the file system.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# URL to access images in browser.
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login and logout redirects using django auth app.
LOGIN_REDIRECT_URL = 'pages:home'
# LOGOUT_REDIRECT_URL = 'pages:home'

LOGIN_URL = 'login
# LOGIN_URL = '../users/templates/registration/login.html'

# Added to tell Django to use new custom user model insted of built-in User model.
AUTH_USER_MODEL = 'users.CustomUser'

# Added config for using bootstrap4 template pack with crispy forms.
CRISPY_TEMPLATE_PACK = 'bootstrap4'

#SMTP Configuration

SENDGRID_API_KEY = config.get('SENDGRID_API_KEY')

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
DEFAULT_FROM_EMAIL = config.get('DEFAULT_FROM_EMAIL')

# To carry additional data to notification messages.
DJANGO_NOTIFICATIONS_CONFIG = {
    'USE_JSONFIELD': True,
}
