from django.apps import AppConfig
import sys

class MailappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailapp"

    def ready(self):
        # Запрет запуска планировщика в командах управления (например, миграции).
        if 'runserver' not in sys.argv:
            return

        # Запуск планировщика только в основном процессе
        if not any(['manage.py' in arg for arg in sys.argv]):
            return

        from mailapp.services import start_scheduler, shutdown_scheduler
        import atexit

        # Start the scheduler
        start_scheduler()

        # Register shutdown handler
        atexit.register(shutdown_scheduler)
