from .base import *  # noqa: F403

ALLOWED_HOSTS = ['134.209.66.134']

DEBUG = False

INSTALLED_APPS += ['gunicorn']  # noqa: F405

CORS_ORIGIN_WHITELIST = (
    'http://134.209.66.134',
)
