from django.apps import AppConfig
from django.conf import settings
import sys
class RemindersConfig(AppConfig):
    name = 'reminders'

    def ready(self):
        if settings.SCHEDULER_AUTOSTART:
            from . import scheduler
            scheduler.start()
            print("Scheduler started...", file=sys.stdout)
