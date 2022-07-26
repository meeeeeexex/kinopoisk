from django.db import models

from kinopoisk_app.models import Actor
from kinopoisk_app.models.common.BaseModel import BaseModel
from django.urls import reverse


class Movie(BaseModel):
    name = models.CharField("Название", max_length=100)
    genre = models.ForeignKey('kinopoisk_app.Genre', on_delete=models.CASCADE, verbose_name="Жанр")
    description = models.TextField("Информация о фильме", null=True, blank=True)
    user_rating = models.IntegerField("Рейтинг пользователя", default=0)
    critique_rating = models.IntegerField("Рейтинг критика", default=0)
    picture_blob = models.ImageField("Фото", upload_to='photos/%Y/%m/%d/', max_length=100, null=True, blank=True)
    film_director = models.ForeignKey('kinopoisk_app.Director', on_delete=models.CASCADE, verbose_name="Режиссер",
                                      related_name='movies')
    actor_squad = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="movies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
