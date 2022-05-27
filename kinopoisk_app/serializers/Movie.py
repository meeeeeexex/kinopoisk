from rest_framework import serializers
from kinopoisk_app.models.Movie import Movie


class MovieSerializer(serializers.ModelSerializer):
    actor_squad = serializers.StringRelatedField(many=True)
    genre = serializers.StringRelatedField()
    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'genre',
            'user_rating',
            'critique_rating',
            'director',
            'actor_squad',

        ]
