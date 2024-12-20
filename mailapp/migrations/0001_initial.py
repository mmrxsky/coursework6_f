# Generated by Django 4.2 on 2024-12-03 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата и время последней попытки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("Успешно", "Успешно"), ("Неуспешно", "Неуспешно")],
                        verbose_name="статус попытки (успешно / не успешно)",
                    ),
                ),
                (
                    "server_response",
                    models.CharField(
                        verbose_name="ответ почтового сервера, если он был"
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка рассылки",
                "verbose_name_plural": "Попытки рассылки",
            },
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Ф.И.О.")),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="Контактный email"
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
                ),
                (
                    "count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество клиентов рассылок"
                    ),
                ),
            ],
            options={
                "verbose_name": "Клиент сервиса",
                "verbose_name_plural": "Клиенты сервиса",
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "letter_subject",
                    models.TextField(blank=True, null=True, verbose_name="тема письма"),
                ),
                ("body", models.TextField(verbose_name="тело письма")),
            ],
            options={
                "verbose_name": "Сообщение для рассылки",
                "verbose_name_plural": "Сообщения для рассылки",
            },
        ),
        migrations.CreateModel(
            name="NewsLetter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        default="без названия",
                        max_length=50,
                        null=True,
                        verbose_name="Название рассылки",
                    ),
                ),
                (
                    "start_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="время начала рассылки"
                    ),
                ),
                (
                    "end_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="время окончания рассылки"
                    ),
                ),
                (
                    "frequency",
                    models.CharField(
                        choices=[
                            ("MINUTLY", "раз в минуту"),
                            ("DAILY", "раз в день"),
                            ("WEEKLY", "раз в неделю"),
                            ("MONTHLY", "раз в месяц"),
                        ],
                        default=("daily",),
                        verbose_name="Периодичность: раз в день, раз в неделю, раз в месяц",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CREATED", "Создана"),
                            ("STARTED", "Запущена"),
                            ("FINISHED", "Завершена"),
                        ],
                        default="Создана",
                        verbose_name="Статус рассылки (например, завершена, создана, запущена)",
                    ),
                ),
                (
                    "count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество рассылок"
                    ),
                ),
                (
                    "client",
                    models.ManyToManyField(
                        help_text="Укажите клиентов",
                        to="mailapp.client",
                        verbose_name="Клиент сервиса",
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailapp.message",
                        verbose_name="Сообщение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка (настройки)",
                "verbose_name_plural": "Рассылки (настройки)",
                "permissions": [
                    ("can_delete_newsletter", "Can delete newsletter"),
                    ("can_view_newsletter", "Can view newsletter"),
                    ("can_delete_client", "Can delete client"),
                    ("can_view_client", "Can view client"),
                ],
            },
        ),
    ]
