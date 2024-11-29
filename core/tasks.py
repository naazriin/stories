import time
from celery import shared_task

@shared_task
def my_task():
    print('start')
    time.sleep(10)
    print('Finish')