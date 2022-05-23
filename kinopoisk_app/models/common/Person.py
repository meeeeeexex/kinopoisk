from typing import List
import pycountry
from django.db import models
from django.utils.translation import gettext_lazy as _
from kinopoisk_app.models.common.BaseModel import BaseModel


class Person(BaseModel):
    first_name = models.CharField(_("Имя"), max_length=158)
    last_name = models.CharField(_("Фамилия"), max_length=150)
    bio = models.TextField(_("Информация"), null=True, blank=True)
    picture = models.ImageField(_("Фото"), upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, null=True,
                                blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        abstract = True
        ordering = ['-created', ]


def get_all_countries() -> List[str]:
    available_countries = [country_item.name for country_item in pycountry.countries]
    available_countries.remove('Russian Federation')
    return available_countries


class Countries:
    ALL_COUNTRIES = ((country_item, country_item) for country_item in get_all_countries())
    NOT_SPECIFIED = 'Not specified'
