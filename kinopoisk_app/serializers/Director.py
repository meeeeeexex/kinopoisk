from rest_framework import serializers
from kinopoisk_app.models.Director import Director


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = [
            'first_name',
            'last_name',
        ]


class DirectorRetrieveSerializer(serializers.ModelSerializer):
    filmography = serializers.StringRelatedField(many=True)

    class Meta:
        model = Director
        fields = [
            'first_name',
            'last_name',
            'country',
            'bio',
            'filmography'
        ]
