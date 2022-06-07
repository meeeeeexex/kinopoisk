from kinopoisk_app.models.common.Person import Person
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Director(Person):
    slug = models.SlugField(null=True, unique=True)

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"

    def get_absolute_url(self):
        return reverse("director_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            print(self.first_name + ' ' + self.last_name)
            self.slug = slugify(self.first_name + ' ' + self.last_name)
        return super().save(*args, **kwargs)
