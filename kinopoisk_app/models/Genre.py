from django.db import models

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


class Genres:
    ALL_GENRES = ((genre_item, genre_item) for genre_item in ALL_GENRES)
    NOT_SPECIFIED = 'Not specified'


class Genre(models.Model):
    name = models.CharField('Название',
                            max_length=100,
                            choices=Genres.ALL_GENRES,
                            default=Genres.NOT_SPECIFIED
                            )

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name
