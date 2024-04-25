# cert_study/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cert_study.settings")
app = Celery("cert_study")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()