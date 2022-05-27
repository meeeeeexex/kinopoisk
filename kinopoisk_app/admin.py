from django.contrib import admin
from django.contrib.auth import get_user_model

from kinopoisk_app.models.Director import Director
from kinopoisk_app.models.Actor import Actor
from kinopoisk_app.models.Cinema import Cinema
from kinopoisk_app.models.Movie import Movie
from kinopoisk_app.models.Review import Review
from kinopoisk_app.models.Genre import Genre


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'country',)
    list_display_links = ('id', 'first_name')
    search_fields = ('country',)
    list_editable = ("country",)
    list_filter = ("country", "last_name")


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'country',)
    list_display_links = ('id', 'first_name')
    search_fields = ('country',)
    list_editable = ("country",)
    list_filter = ("country", "last_name")


# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'country')
#     list_display_links = ('id', 'username')
#     search_fields = ('country',)
#     list_editable = ("country",)
#     list_filter = ("country", "last_name")


admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Genre)
