from rest_framework import serializers
from kinopoisk_app.models.Cinema import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = [
            'name',
        ]


class CinemaRetrieveSerializer(serializers.ModelSerializer):
    avaliable_movies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cinema
        fields = [
            'name',
            'address',
            'avaliable_movies',
        ]
