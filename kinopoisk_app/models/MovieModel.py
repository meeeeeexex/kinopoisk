from django.db import models
import uuid


class Movie(models.Model):
    movie_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    # Todo: переделать жанры одинаково
    genre = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    user_rating = models.IntegerField(default=0)
    critique_rating = models.IntegerField(default=0)
    picture_blob = models.ImageField(upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    review = models.ManyToManyField('kinopoisk_app.User', through='Review',
                                    null=True)  # TODO: Обсудить добавить fk User -> through Review
    film_director = models.ForeignKey('FilmDirector', on_delete=models.CASCADE, null=True)
    actor_squad = models.ManyToManyField('Actor')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

