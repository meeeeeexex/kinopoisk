from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from kinopoisk_app.models.common.Person import Countries, Person


# def get_all_countries() -> List[str]:
#     available_countries = [country_item.name for country_item in pycountry.countries]
#     available_countries.remove('Russian Federation')
#     return available_countries
#
#
# class Countries:
#     ALL_COUNTRIES = ((country_item, country_item) for country_item in get_all_countries())
#     NOT_SPECIFIED = 'Not specified'


class CustomUser(AbstractUser):
    favorite_movies = models.ManyToManyField('kinopoisk_app.Movie', verbose_name='Избранные фильмы', blank=True)
    favorite_genres = models.ManyToManyField('kinopoisk_app.Genre', verbose_name='Любимые жанры', blank=True)
    country = models.CharField('Страна',
                               max_length=100,
                               choices=Countries.ALL_COUNTRIES,
                               default=Countries.NOT_SPECIFIED
                               )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
