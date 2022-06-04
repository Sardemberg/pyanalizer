from celery import Celery

app = Celery(
    'celery_queues', 
    broker='redis://localhost:6379/0', 
    include=["processing.processes"]
)