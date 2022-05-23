from kinopoisk_app.models import Countries
from kinopoisk_app.models.common.Person import Person
from django.db import models
from django.utils.translation import gettext_lazy as _


class Director(Person):
    country = models.CharField(_('Страна'),
                               max_length=100,
                               choices=Countries.ALL_COUNTRIES,
                               default=Countries.NOT_SPECIFIED
                               )

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"
