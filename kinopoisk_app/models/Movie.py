from django.db import models
from django.utils.translation import gettext_lazy as _
from kinopoisk_app.models.BaseModel import BaseModel
import uuid


class Movie(BaseModel):
    name = models.CharField(_("Название"), max_length=100)
    genre = models.ForeignKey('kinopoisk_app.Genre', on_delete=models.CASCADE)
    description = models.TextField(_("Информация о фильме"), null=True, blank=True)
    user_rating = models.IntegerField(default=0)
    critique_rating = models.IntegerField(default=0)
    picture_blob = models.ImageField(_("Фото"), upload_to='photos/%Y/%m/%d/', max_length=100)
    director = models.ForeignKey('kinopoisk_app.Director', on_delete=models.CASCADE, null=True)
    actor_squad = models.ManyToManyField('kinopoisk_app.Actor')

    def __str__(self):
        return f'self.name'

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
