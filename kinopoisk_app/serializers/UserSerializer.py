from rest_framework import serializers
from kinopoisk_app.models.UserModel import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'created_at',
            'favorite_genres',
        ]
