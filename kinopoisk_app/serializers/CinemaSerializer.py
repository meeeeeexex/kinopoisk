from rest_framework import serializers
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
