from kinopoisk_app.models.common.Person import Person
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Director(Person):

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"

    def get_absolute_url(self):
        return reverse("director_detail", kwargs={"id": self.id})
