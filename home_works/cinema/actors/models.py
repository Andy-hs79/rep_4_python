#  В приложении actors создать модели Actor и Director с необходимыми полями, связать эти модели с моделью фильма.

from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    country = models.CharField(max_length=50, verbose_name='Страна')

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    country = models.CharField(max_length=50, verbose_name='Страна')

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'
# Create your models here.

