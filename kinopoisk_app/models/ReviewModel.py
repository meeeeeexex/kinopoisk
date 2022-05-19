from django.db import models
import uuid


class Review(models.Model):
    review_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    user = models.ForeignKey('kinopoisk_app.User', on_delete=models.CASCADE, related_name='user')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='movie')
    review_text = models.TextField(null=False)

    def __str__(self):
        return f'{self.user.full_name} reviews {self.movie.name}:' \
               f'{self.review_text}'
