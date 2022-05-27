from django.db import models

from kinopoisk_app.models.common.Person import Person
from django.utils.translation import gettext_lazy as _


class Actor(Person, models.Model):
    filmography = models.ManyToManyField('Movie', verbose_name="Фильмы", null=True, blank=True, related_name="actors")

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
