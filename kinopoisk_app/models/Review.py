from django.contrib.auth.models import User
from django.db import models
from kinopoisk_app.models import CustomUser
import uuid

from kinopoisk_app.models.common import BaseModel


class Review(BaseModel):
    # id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    movie = models.ForeignKey('kinopoisk_app.Movie', on_delete=models.CASCADE, verbose_name="Фильм")
    review_text = models.TextField(null=False, verbose_name="Отзыв")

    def __str__(self):
        return f'{self.user.first_name} reviews {self.movie.name}:' \
               f'{self.review_text[:30]}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
