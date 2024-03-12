# В приложении movie создать модель Film с полями:
# "название", "рейтинг", "продолжительность", "режиссер", "актеры".

#  В приложении actors создать модели Actor и Director с необходимыми полями, связать эти модели с моделью фильма.

from django.db import models
from actors.models import Director, Actor


class Film(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    rating = models.FloatField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

