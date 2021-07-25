from .base import *

ALLOWED_HOSTS = ['134.209.66.134']

DEBUG = False

INSTALLED_APPS += ['gunicorn']

CORS_ORIGIN_WHITELIST = (
    'http://134.209.66.134',
)
