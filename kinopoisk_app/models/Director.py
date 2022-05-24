from kinopoisk_app.models import Countries
from kinopoisk_app.models.common.Person import Person
from django.db import models
from django.utils.translation import gettext_lazy as _


class Director(Person):
    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"
