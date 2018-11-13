import os
from website.settings import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['165.227.33.196', '.herokuapp.com',]

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hellowebbooks',
        'USER': os.environ['POSTGRES_US'],
        'PASSWORD': os.environ['POSTGRES_PW'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_API'],
EMAIL_PORT = 25
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER

STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

import django_heroku
django_heroku.settings(locals())
