from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    user_rating = models.IntegerField(default=0)
    critique_rating = models.IntegerField(default=0)
    picture_blob = models.ImageField(upload_to='/static/image', height_field=None, width_field=None, max_length=100)
    review = models.ManyToManyField('Review', on_delete=models.CASCADE, null=True)
    film_director = models.ForeignKey('Film_Director', on_delete=models.CASCADE, null=True)
    actor_squad = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
