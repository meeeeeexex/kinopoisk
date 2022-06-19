from kinopoisk_app.models import Movie
from kinopoisk_app.models.Actor import Actor
from rest_framework import serializers


class MovieSerializerForActor(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'genre',
        ]


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = [
            'id',
            'first_name',
            'last_name',
        ]


class ActorRetrieveSerializer(serializers.ModelSerializer):
    movies = MovieSerializerForActor(many=True)

    class Meta:
        model = Actor
        fields = [
            'id',
            'first_name',
            'last_name',
            'country',
            'bio',
            'movies',
        ]
