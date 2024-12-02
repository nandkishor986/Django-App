from celery import Celery
import os

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebdjango.settings')

# Create an instance of the Celery class.
app = Celery('ebdjango')

# Load configuration from Django settings, using a specific namespace.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks from all registered Django app configs.
app.autodiscover_tasks()