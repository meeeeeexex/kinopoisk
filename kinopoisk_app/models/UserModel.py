from django.db import models
import pycountry
from typing import List
import uuid


# для того, чтобы пользователь мог выбирать страну, откуда он -
# импортируем pycountry
def get_all_countries() -> List[str]:
    available_countries = [country_item.name for country_item in pycountry.countries]
    available_countries.remove('Russian Federation')
    return available_countries


def get_all_genres() -> List[str]:
    return ['Action',
            'Comedy',
            'Drama',
            'Fantasy',
            'Horror',
            'Mystery',
            'Romance',
            'Thriller',
            'Western', ]


class Countries:
    ALL_COUNTRIES = ((country_item, country_item) for country_item in get_all_countries())
    NOT_SPECIFIED = 'Not specified'


class Genres:
    ALL_GENRES = ((genre_item, genre_item) for genre_item in get_all_genres())
    NOT_SPECIFIED = 'Not specified'


# class Genre(BaseModel):
#     name = models.CharField(max_length=50)



class User(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    full_name = models.CharField(max_length=250, null=False)
    created_at = models.DateField(auto_now_add=True, db_index=True)
    country = models.CharField(
        max_length=100,
        choices=Countries.ALL_COUNTRIES,
        default=Countries.NOT_SPECIFIED
    )

    # TODO: Обсудить как будем хранить все жанры,
    # я предлагаю хранить через выбор, чтобы человек мог сам выбрать
    favourite_genres = models.ManyToManyField(Genre)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return f'{self.full_name} has {self.fav_genres} as favourite genres'
