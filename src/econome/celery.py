import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'econome.settings')

app = Celery('econome')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery Settings
app.conf.update(dict(
    CELERY_BROKER_URL='redis://' + str(settings.REDIS_HOST_FOR_CELERY) + ':' + str(settings.REDIS_PORT) + '/0',
    CELERY_BROKER_TRANSPORT_OPTIONS={'visibility_timeout': 3600},
    CELERY_RESULT_BACKEND='redis://' + str(settings.REDIS_HOST_FOR_CELERY) + ':' + str(settings.REDIS_PORT) + '/0',
    CELERY_ACCEPT_CONTENT=['application/json'],
    CELERY_DISABLE_RATE_LIMITS=True,
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    # CELERY_BROKER_CONNECTION_RETRY = True,
    # CELERY_BROKER_CONNECTION_MAX_RETRIES = 0,
    CELERYBEAT_SCHEDULER="django_celery_beat.schedulers:DatabaseScheduler",
    CELERYD_USER="root",
    CELERYD_MAX_TASKS_PER_CHILD=4,
    CELERY_TASK_RESULT_EXPIRES=150
))
