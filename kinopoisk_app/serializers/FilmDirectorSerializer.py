from rest_framework import serializers
from kinopoisk_app.models.Director import Director


class FilmDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"
