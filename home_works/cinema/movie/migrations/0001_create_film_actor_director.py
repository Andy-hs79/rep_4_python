# Generated by Django 5.0.3 on 2024-03-12 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_create_film_actor_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('rating', models.FloatField()),
                ('duration', models.IntegerField()),
                ('actors', models.ManyToManyField(to='actors.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actors.director')),
            ],
        ),
    ]
