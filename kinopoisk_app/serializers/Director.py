from rest_framework import serializers

from kinopoisk_app.models import Movie
from kinopoisk_app.models.Director import Director


class MovieSerializerForDirector(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'genre',
        ]


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = [
            'id',
            'first_name',
            'last_name',
        ]


class DirectorRetrieveSerializer(serializers.ModelSerializer):
    movies = MovieSerializerForDirector(many=True)
    country = serializers.CharField()

    class Meta:
        model = Director
        fields = [
            'id',
            'first_name',
            'last_name',
            'country',
            'bio',
            'movies'
        ]
