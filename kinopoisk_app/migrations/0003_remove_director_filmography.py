# Generated by Django 4.0.4 on 2022-06-07 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk_app', '0002_alter_movie_cinemas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='filmography',
        ),
    ]
