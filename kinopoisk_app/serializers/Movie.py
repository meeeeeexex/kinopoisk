from rest_framework import serializers
from kinopoisk_app.models.Movie import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'name',
            'genre',
            'user_rating',
            'critique_rating',
            'director',
            'actor_squad',

        ]
