import os

from .base import *

my_debug = os.getenv('DEBUG')
if my_debug == "False":
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['kazeem-torre-test.herokuapp.com',]

DATABASE_URL = os.getenv('DATABASE_URL')

SECRET_KEY = os.getenv('SECRET_KEY')

