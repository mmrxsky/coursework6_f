from django.core.management import BaseCommand

from mailapp.services import send_newsletter_periodic_email


class Command(BaseCommand):
    """Команда на запуск рассылки"""

    def handle(self, *args, **options):

        send_newsletter_periodic_email()
