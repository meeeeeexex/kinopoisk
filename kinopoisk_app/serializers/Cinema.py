from rest_framework import serializers
from kinopoisk_app.models.Cinema import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = [
            'id',
            'name',
            'address',
            'available_movies',

        ]
