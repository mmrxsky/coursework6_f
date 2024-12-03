import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail

from mailapp.models import NewsLetter, Message, Attempt
from apscheduler.schedulers.background import BackgroundScheduler


def send_newsletter_email(objects):
    try:
        message_instance = Message.objects.first()
        server_response = send_mail(
            subject=message_instance.letter_subject,
            message=message_instance.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in objects.client.all()],
            fail_silently=False,
        )
        log = Attempt.objects.create(
            mailing_parameters=objects, server_response=server_response
        )
        if server_response:
            log.status = "Успешно"
            log.save()
        if objects.status == "Создана":
            objects.status = "Запущена"
            objects.save()
    except smtplib.SMTPException as e:
        log = Attempt.objects.create(mailing_parameters=objects, server_response=e)
        log.save()


def send_newsletter_periodic_email():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    print(f"Текущее время - {current_datetime}")

    for obj in NewsLetter.objects.all():
        if obj.start_time < current_datetime < obj.end_time:
            log = Attempt.objects.filter(mailing_parameters=obj)
            print(log)
            if log.exists():
                last_log = log.order_by("time").last()
                current_timedelta = current_datetime - last_log.time
                print(obj.frequency)

                if obj.frequency == "DAILY" and current_timedelta >= timedelta(days=1):
                    send_newsletter_email(obj)
                    print(f"Выполнена рассылка раз в день")
                elif obj.frequency == "WEEKLY" and current_timedelta >= timedelta(
                    weeks=1
                ):
                    send_newsletter_email(obj)
                    print(f"Выполнена рассылка раз в неделю")
                elif obj.frequency == "MONTHLY" and current_timedelta >= timedelta(
                    weeks=4
                ):
                    send_newsletter_email(obj)
                    print(f"Выполнена рассылка раз в месяц")

            else:
                send_newsletter_email(obj)
                print(f"иначе")
        elif current_datetime > obj.end_time:
            obj.status = "завершена"
            obj.save()


def start_scheduler():
    scheduler = BackgroundScheduler()

    # Проверка, добавлена ли задача уже
    if not scheduler.get_jobs():
        scheduler.add_job(send_newsletter_periodic_email, "interval", seconds=3600)

    if not scheduler.running:
        scheduler.start()
