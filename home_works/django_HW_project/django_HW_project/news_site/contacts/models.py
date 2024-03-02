from django.db import models


class Phone_book(models.Model):
    names = []
    phones = models.OneToOneField(names)

    def __str__(self):
        return ...
    

# Create your models here.
