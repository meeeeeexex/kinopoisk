from rest_framework import serializers
from kinopoisk_app.models.UserModel import User
from kinopoisk_app.models.ReviewModel import Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                  'user_id',
                  'full_name',
                  'created_at',
                  'fav_genres',
                  ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
                  'review_id',
                  'user',
                  'movie',
                  'review_text',
                  ]

