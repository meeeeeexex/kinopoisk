from rest_framework import serializers
from kinopoisk_app.models.User import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'created_at',
            'favorite_genres',
        ]
