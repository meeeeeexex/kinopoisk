from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from kinopoisk_app.models.common.Person import Countries, Person

# class User(AbstractUser):
#     favorite_genres = models.ManyToManyField('kinopoisk_app.Genre', verbose_name='favourite genres')
#     country = models.CharField('Страна',
#                                max_length=100,
#                                choices=Countries.ALL_COUNTRIES,
#                                default=Countries.NOT_SPECIFIED
#                                )
#
#     def __str__(self):
#         return f'{self.username} has {self.favorite_genres} as favourite genres'
#
#     class Meta:
#         swappable = 'AUTH_USER_MODEL'
#         verbose_name = "Наш Юзер"
#         verbose_name_plural = "Наши Юзеры"

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Profile(Person):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Профиль", related_name='profile')
#     favorite_movies = models.ManyToManyField('kinopoisk_app.Movie', verbose_name='Избранные фильмы', null=True, blank=True)
#     favorite_genres = models.ManyToManyField('kinopoisk_app.Genre', verbose_name='Любимые жанры', null=True, blank=True)
#
#     def __str__(self):
#         return str(self.user)
#
#     class Meta:
#         verbose_name = "Профиль"
#         verbose_name_plural = "Профили"
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
#
# class Profile(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#
#     def create_user(self, email, date_of_birth, password=None):
#         # create user here
#         ...
#
#     def create_superuser(self, email, date_of_birth, password=None):
#         # create superuser here
#         ...
