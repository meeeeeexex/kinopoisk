from rest_framework import serializers

from accounts.serializers import UserSerializer
from kinopoisk_app.models import CustomUser
from kinopoisk_app.models.Review import Review


class ReviewAddSerializer(serializers.ModelSerializer):

    class Meta:

        model = Review
        fields = [
                  'movie',
                  'headline',
                  'review_text',
                  ]


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField()

    class Meta:

        model = Review
        fields = [
                  'user',
                  'headline',
                  'review_text',
                  ]

