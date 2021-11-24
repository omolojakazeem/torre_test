import os

from .base import *

my_debug = os.getenv('DEBUG')
if my_debug == "False":
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['officebook-staging.herokuapp.com', 'office-book.herokuapp.com']
SERVER_NAME = ALLOWED_HOSTS[1]
DATABASE_URL = os.getenv('DATABASE_URL')

SECRET_KEY = os.getenv('SECRET_KEY')


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
