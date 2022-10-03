import os
import warnings

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings.dev")

app = Celery("server")
app.conf.broker_url = "redis://redis:6379/0"
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

warnings.filterwarnings("ignore")
