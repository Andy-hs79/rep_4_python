from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок статьи')
    content = models.TextField(verbose_name='Текст статьи')

    def __str__(self):
        return f'{self.title}'


class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок страницы')
    content = models.TextField(verbose_name='Текст страницы')

    def __str__(self):
        return f'{self.title}'

class Users(models.Model):
    pass
# Create your models here.py manage.py makemigrations
