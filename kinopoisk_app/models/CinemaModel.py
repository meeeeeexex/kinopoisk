from django.db import models
import uuid


class Cinema(models.Model):
    cinema_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    cinema_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    avaliable_movies = models.ManyToManyField('Movie')

    def __str__(self):
        return self.cinema_name

    class Meta:
        verbose_name = "Кинотеатр"
        verbose_name_plural = "Кинотеатры"
