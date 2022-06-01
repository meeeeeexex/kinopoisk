from kinopoisk_app.models.Actor import Actor
from rest_framework import serializers


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = [
            'first_name',
            'last_name',
        ]


class ActorRetrieveSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Actor
        fields = [
            'first_name',
            'last_name',
            'country',
            'bio',
            'movies',
        ]
