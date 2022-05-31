from kinopoisk_app.models.common.Person import Person
from django.db import models


class Director(Person):
    filmography = models.ManyToManyField('Movie', null=True, blank=True, verbose_name="Фильмы", related_name="director")

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"
