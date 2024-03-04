from django.db import models


class Name(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30, )

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone = models.CharField(verbose_name='Телефон', max_length=10)
    contact = models.ForeignKey(Name, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone

# Create your models here.
