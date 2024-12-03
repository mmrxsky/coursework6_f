from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Класс для описания модели клиента"""
    name = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    email = (models.EmailField(max_length=100, verbose_name='Контактный email', unique=True))
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    owner = models.ForeignKey(User, verbose_name='Менеджер', **NULLABLE, on_delete=models.SET_NULL)
    count = models.PositiveIntegerField(
        verbose_name='Количество клиентов рассылок',
        default=0
    )

    def __str__(self):
        return f'{self.name} - {self.email} \n {self.comment}'

    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты сервиса'
