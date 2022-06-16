from settings.settings import *

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ()
MINUTES_BEFORE_ALLOW_DELETE_RATE = 60 * 24 * 365 * 100

CELERY_TASK_ALWAYS_EAGER = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
