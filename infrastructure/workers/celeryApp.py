from celery import Celery

celery_app = Celery(
    "workers",
    broker="redis://192.168.167.174:6380/0",
    backend="redis://192.168.167.174:6380/1"
)
 