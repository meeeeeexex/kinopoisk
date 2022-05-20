from django.db import models
import uuid
from kinopoisk_app.models.Genre import Genre


class Movie(models.Model):
    movie_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    # Todo: переделать жанры одинаково
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    user_rating = models.IntegerField(default=0)
    critique_rating = models.IntegerField(default=0)
    picture_blob = models.ImageField(upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    film_director = models.ForeignKey('kinopoisk_app.FilmDirector', on_delete=models.CASCADE, null=True)
    actor_squad = models.ManyToManyField('kinopoisk_app.Actor')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
