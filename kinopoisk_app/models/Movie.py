from django.db import models
from django.utils.translation import gettext_lazy as _

from kinopoisk_app.models import Actor, Cinema
from kinopoisk_app.models.common.BaseModel import BaseModel


class Movie(BaseModel):
    name = models.CharField(_("Название"), max_length=100)
    genre = models.ForeignKey('kinopoisk_app.Genre', on_delete=models.CASCADE,)
    description = models.TextField(_("Информация о фильме"), null=True, blank=True)
    user_rating = models.IntegerField(_("Рейтинг пользователя"), default=0)
    critique_rating = models.IntegerField(_("Рейтинг критика"), default=0)
    picture_blob = models.ImageField(_("Фото"), upload_to='photos/%Y/%m/%d/', max_length=100, null=True, blank=True)
    film_director = models.ForeignKey('kinopoisk_app.Director', on_delete=models.CASCADE, verbose_name="Режиссер", related_name='movies')
    actor_squad = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="movies")
    cinemas = models.ManyToManyField('kinopoisk_app.Cinema', verbose_name="Кинотеатры", related_name="avaliable_movies")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
