from django.apps import AppConfig
from django.conf import settings

class RemindersConfig(AppConfig):
    name = 'reminders'

    def ready(self):
        from . import scheduler
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
