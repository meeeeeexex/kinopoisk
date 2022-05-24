from django.db import models

from kinopoisk_app.models.common.Person import Person
from django.utils.translation import gettext_lazy as _


class Actor(Person, models.Model):
    filmography = models.ForeignKey('kinopoisk_app.Movie', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"
