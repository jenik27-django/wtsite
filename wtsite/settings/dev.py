from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-rbuk%2lc9zeh2bj8ct=vojcmomdl@g@o8v7qw8@ox!2m=b1wrt"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INSTALLED_APPS += [
    "debug_toolbar"
]

INTERNAL_IPS = (
    "127.0.0.1",
    # docker host ip
    "172.17.0.1"
)

try:
    from .local import *
except ImportError:
    pass
