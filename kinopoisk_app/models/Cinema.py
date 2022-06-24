from django.db import models
from django.utils.translation import gettext_lazy as _
from kinopoisk_app.models.common.BaseModel import BaseModel

ALL_CITIES = [
    'Kyiv',
    'Vinnitsa',
    'Uman',
    'Zaporozhje',
    'Kharkov',
    'Lvov',
    'Poltava',
    'Zhitomir',
    'Dnepr',
    'Lutsk',
    'Chernovrtsi',
    'Uzhgorod',
    'Kherson',
]


class Cities:
    ALL_CITIES = ((city_item, city_item) for city_item in ALL_CITIES)
    NOT_SPECIFIED = 'Not specified'


ALL_CINEMAS = [
    'Multiplex',
    'Butterfly',
    'Planeta kino',
    'Oskar',
    'Sputnik',
    'Liniya kino',
    "Kievskaya Rus'",
]


class Cinemas:
    ALL_CINEMAS = ((cinema_item, cinema_item) for cinema_item in ALL_CINEMAS)
    NOT_SPECIFIED = 'Not specified'


class Cinema(BaseModel):
    name = models.CharField(_("Название"),
                            max_length=100,
                            choices=Cinemas.ALL_CINEMAS,
                            default=Cinemas.NOT_SPECIFIED
                            )

    city = models.CharField('Город',
                            max_length=100,
                            choices=Cities.ALL_CITIES,
                            default=Cities.NOT_SPECIFIED
                            )
    address = models.CharField(_("Адрес"), max_length=100)

    movies = models.ManyToManyField('kinopoisk_app.Movie', related_name='cinemas')

    def __str__(self):
        return self.name + f"({self.city},{self.address})"

    class Meta:
        verbose_name = "Кинотеатр"
        verbose_name_plural = "Кинотеатры"
