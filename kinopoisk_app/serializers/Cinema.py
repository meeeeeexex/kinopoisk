from rest_framework import serializers
from kinopoisk_app.models.Cinema import Cinema
from kinopoisk_app.models import Movie


# Movie Serializer to avoid circular import
class MovieSerializerForCinema(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'genre',
        ]


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = [
            'id',
            'name',
        ]


class CinemaRetrieveSerializer(serializers.ModelSerializer):
    movies = MovieSerializerForCinema(many=True)

    class Meta:
        model = Cinema
        fields = [
            'id',
            'name',
            'address',
            'movies',
        ]


class CinemaAddAndUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cinema
        fields = "__all__"
