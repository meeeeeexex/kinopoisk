from django.db import models
from django.utils.translation import gettext_lazy as _

from kinopoisk_app.models import Actor
from kinopoisk_app.models.common.BaseModel import BaseModel
from django.urls import reverse
from django.template.defaultfilters import slugify


class Movie(BaseModel):
    name = models.CharField(_("Название"), max_length=100)

    slug = models.SlugField(null=True, unique=True)

    genre = models.ForeignKey('kinopoisk_app.Genre', on_delete=models.CASCADE, verbose_name="Жанр")
    description = models.TextField(_("Информация о фильме"), null=True, blank=True)
    user_rating = models.IntegerField(_("Рейтинг пользователя"), default=0)
    critique_rating = models.IntegerField(_("Рейтинг критика"), default=0)
    picture_blob = models.ImageField(_("Фото"), upload_to='photos/%Y/%m/%d/', max_length=100, null=True, blank=True)
    film_director = models.ForeignKey('kinopoisk_app.Director', on_delete=models.CASCADE, verbose_name="Режиссер",
                                      related_name='movies')
    actor_squad = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="movies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            position_of_bracket = self.name.find('(')
            position_of_bracket = 45 if position_of_bracket > 45 else position_of_bracket
            print(self.name[:position_of_bracket])
            self.slug = slugify(self.name[:position_of_bracket])
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
