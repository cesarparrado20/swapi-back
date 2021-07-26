from .base import *  # noqa: F403 F401

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

DEBUG = True

CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1',
    'http://localhost',
)
