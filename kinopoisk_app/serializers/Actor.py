from kinopoisk_app.models.Actor import Actor
from rest_framework import serializers


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            'id',
            'first_name',
            'last_name',
            'country',
            'filmography'
        ]
