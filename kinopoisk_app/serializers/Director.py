from rest_framework import serializers
from kinopoisk_app.models.Director import Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = [
            'first_name',
            'last_name',
            'bio',
            'filmography',
        ]