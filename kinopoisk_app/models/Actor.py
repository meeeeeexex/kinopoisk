from django.db import models
from django.urls import reverse

from kinopoisk_app.models.common.Person import Person


class Actor(Person, models.Model):

    def get_absolute_url(self):
        return reverse("actor_detail", kwargs={"id": self.id})

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
