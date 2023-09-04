from config.settings.base import *


ENV = "dev"
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^)zk=x+rfy_w!64xxkr_zq+2@z+(=!ycy8%_uky=m@1b&fu-&n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS.append(
    'debug_toolbar',
)
INSTALLED_APPS.append(
    'django_celery_results'
)

MIDDLEWARE.append(
    'debug_toolbar.middleware.DebugToolbarMiddleware'
)

INTERNAL_IPS = [
    '127.0.0.1',
]

MEDIA_URL = '/'

MEDIA_ROOT = BASE_DIR

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "feeapp.noreply@gmail.com"
EMAIL_HOST_PASSWORD = "xkmszoidotetsuqb"
