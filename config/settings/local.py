from .base import *

SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='{(tJnN_6<RQ\\ReI&s]}:YHe\\)t6AP.:]WW[}fmeME6!+y'
)

DEBUG = env.bool('DJANGO_DEBUG', default=True)
