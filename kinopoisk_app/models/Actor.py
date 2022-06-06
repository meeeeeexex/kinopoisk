from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from kinopoisk_app.models.common.Person import Person


class Actor(Person, models.Model):
    slug = models.SlugField(null=True, unique=True)

    def get_absolute_url(self):
        return reverse("actor_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            print(self.first_name + ' ' + self.last_name)
            self.slug = slugify(self.first_name + ' ' + self.last_name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

 # 0f096c78-72f3-415f-9417-e6b0c4b8c55f | Frank          | Darabont            |     | Not specified | frank-darabont