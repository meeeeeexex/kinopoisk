from django.contrib import admin

from kinopoisk_app.models.Director import Director
from kinopoisk_app.models.Actor import Actor
from kinopoisk_app.models.Cinema import Cinema
from kinopoisk_app.models.Movie import Movie
from kinopoisk_app.models.Review import Review
admin.site.register(Actor)
admin.site.register(Cinema)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)
