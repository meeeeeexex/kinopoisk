from rest_framework import serializers

from .models.FilmDirectorModel import FilmDirector
from .models.ActorModel import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class FilmDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmDirector
        fields = "__all__"
