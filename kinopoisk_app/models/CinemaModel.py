from django.db import models


class Cinema(models.Model):
    cinema_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    avaliable_movies = models.ManyToManyField('Movie', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.cinema_name

    class Meta:
        verbose_name = "Кинотеатр"
        verbose_name_plural = "Кинотеатры"
