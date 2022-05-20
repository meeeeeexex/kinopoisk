from rest_framework import serializers
from kinopoisk_app.models.FilmDirectorModel import FilmDirector


class FilmDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmDirector
        fields = "__all__"
