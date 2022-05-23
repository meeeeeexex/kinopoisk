from django.db import models

# import pycountry
# from typing import List


# для того, чтобы пользователь мог выбирать страну, откуда он -
# импортируем pycountry

#
# def get_all_countries() -> List[str]:
#     available_countries = [country_item.name for country_item in pycountry.countries]
#     available_countries.remove('Russian Federation')
#     return available_countries

ALL_GENRES = [
    'Action',
    'Comedy',
    'Drama',
    'Fantasy',
    'Horror',
    'Mystery',
    'Romance',
    'Thriller',
    'Western',
]

#
# class Countries:
#     ALL_COUNTRIES = ((country_item, country_item) for country_item in get_all_countries())
#     NOT_SPECIFIED = 'Not specified'


class Genres:
    ALL_GENRES = ((genre_item, genre_item) for genre_item in ALL_GENRES)
    NOT_SPECIFIED = 'Not specified'


class Genre(models.Model):
    name = models.CharField('Любимый жанр',
                            max_length=100,
                            choices=Genres.ALL_GENRES,
                            default=Genres.NOT_SPECIFIED
                            )


# class User(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
#     full_name = models.CharField(_('Полное имя'), max_length=250, null=False)
#     created_at = models.DateField(_('Дата создания'), auto_now_add=True, db_index=True)
#     country = models.CharField(_('Страна'),
#                                max_length=100,
#                                choices=Countries.ALL_COUNTRIES,
#                                default=Countries.NOT_SPECIFIED
#                                )
#     favorite_genres = models.ManyToManyField('kinopoisk_app.Genre')
#     picture = models.ImageField(upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
#
#     def __str__(self):
#         return f'{self.full_name} has {self.favorite_genres} as favourite genres'