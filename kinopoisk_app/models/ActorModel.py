from django.db import models


class Actor(models.Model):
    first_name = models.CharField("Имя", max_length=158)
    second_name = models.CharField("Фамилия", max_length=150)
    bio = models.TextField("Информация о актере", null=True, blank=True)
    picture = models.ImageField("Фото", upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, null=True,
                                blank=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"


class ActorInMovie(models.Model):
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    role = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f'{self.actor.first_name} played in {self.movie.name}'
