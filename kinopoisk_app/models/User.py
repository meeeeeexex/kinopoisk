from django.db import models
from django.contrib.auth.models import User
from kinopoisk_app.models.common.Person import Countries


class CustomUser(User):
    favorite_genres = models.ManyToManyField('kinopoisk_app.Genre', verbose_name='favourite genres')
    country = models.CharField('Страна',
                               max_length=100,
                               choices=Countries.ALL_COUNTRIES,
                               default=Countries.NOT_SPECIFIED
                               )

    def __str__(self):
        return f'{self.username} has {self.favorite_genres} as favourite genres'

    class Meta:
        verbose_name = "Наш Юзер"
        verbose_name_plural = "Наши Юзеры"
