from django.db import models
from django.utils.translation import gettext_lazy as _
from kinopoisk_app.models.BaseModel import BaseModel


class Cinema(BaseModel):
    name = models.CharField(_("Название"), max_length=100)
    address = models.CharField(_("Адрес"), max_length=100)
    avaliable_movies = models.ManyToManyField('kinopoisk_app.Movie')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кинотеатр"
        verbose_name_plural = "Кинотеатры"
