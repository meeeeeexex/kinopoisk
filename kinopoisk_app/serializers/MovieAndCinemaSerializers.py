from rest_framework import serializers

from kinopoisk_app.models.MovieModel import Movie
from kinopoisk_app.models.CinemaModel import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = [
                'cinema_id' 
                'cinema_name',
                'address',
                'avaliable_movies',

                  ]


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
