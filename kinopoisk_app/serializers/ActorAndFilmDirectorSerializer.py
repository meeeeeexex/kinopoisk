from rest_framework import serializers
from kinopoisk_app.models.FilmDirectorModel import FilmDirector
from kinopoisk_app.models.ActorModel import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class FilmDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmDirector
        fields = "__all__"
