
from django.db import models


class FilmDirector(models.Model):
    first_name = models.CharField("Имя", max_length=150)
    second_name = models.CharField("Фамилия", max_length=150)
    bio = models.TextField("Информация о режиссере", null=True, blank=True)
    picture = models.ImageField("Фото", upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, null=True,
                                blank=True)

    def __str__(self):
        return self.first_name, self.second_name

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"
