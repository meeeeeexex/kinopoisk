from django.db import models

from kinopoisk_app.models.common.Person import Person


class Actor(Person, models.Model):

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
