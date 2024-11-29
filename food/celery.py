import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food.settings")
app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()





#windows
# py -m celery -A food worker -l info --pool=threads 

# celery -A food beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler