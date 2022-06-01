from django.db import models
from kinopoisk_app.models import CustomUser

from kinopoisk_app.models.common import BaseModel


class Review(BaseModel):
    headline = models.CharField(max_length=100, verbose_name="Заголовок")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    movie = models.ForeignKey('kinopoisk_app.Movie', on_delete=models.CASCADE, verbose_name="Фильм", related_name='reviews')
    review_text = models.TextField(null=False, verbose_name="Отзыв")

    def __str__(self):
        return f'{self.headline}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
