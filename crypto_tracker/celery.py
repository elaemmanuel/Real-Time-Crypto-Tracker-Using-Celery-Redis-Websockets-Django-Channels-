# crypto_tracker/crypto_tracker/celery.py

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crypto_tracker.settings")

app = Celery("crypto_tracker")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-crypto-data-every-30-seconds': {
        'task': 'tracker.tasks.fetch_crypto_data',
        'schedule': 30.0,
    },
    # You can add other scheduled tasks here if needed
}

