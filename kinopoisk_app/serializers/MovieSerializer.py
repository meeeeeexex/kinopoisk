from rest_framework import serializers
from kinopoisk_app.models.MovieModel import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'movie_id',
            'name',
            'genre',
            'user_rating',
            'critique_rating',
            'review',
            'film_director',
            'actor_squad',

        ]
