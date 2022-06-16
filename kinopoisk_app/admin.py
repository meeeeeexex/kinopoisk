from django.contrib import admin

from kinopoisk_app.models.Director import Director
from kinopoisk_app.models.Actor import Actor
from kinopoisk_app.models.Cinema import Cinema
from kinopoisk_app.models.Movie import Movie
from kinopoisk_app.models.Review import Review
from kinopoisk_app.models.Genre import Genre
from kinopoisk_app.models.User import CustomUser


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'genre', 'film_director',)
    list_display_links = ('id',)
    list_editable = ("genre",)
    list_filter = ("genre", "film_director")


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'country',)
    list_display_links = ('id',)
    list_editable = ("country",)
    list_filter = ("country",)


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'country',)
    list_display_links = ('id',)
    list_editable = ("country",)
    list_filter = ("country", )


# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'country')
#     list_display_links = ('id', 'username')
#     search_fields = ('country',)
#     list_editable = ("country",)
#     list_filter = ("country", "last_name")


admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Cinema)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(CustomUser)
