from django.db import models

# соотношение 1-ко-многим или "внешний ключ" (ForeignKey)
class Name(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30, )

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone = models.CharField(verbose_name='Телефон', max_length=10)
    contact = models.ForeignKey(Name, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone

# соотношение многие-ко-многим (ManyToMany)
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
