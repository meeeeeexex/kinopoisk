from rest_framework import serializers
from kinopoisk_app.models.Review import Review


class ReviewAddSerializer(serializers.ModelSerializer):

    class Meta:

        model = Review
        fields = [
                  'id',
                  'movie',
                  'headline',
                  'review_text',
                  ]


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField()

    class Meta:

        model = Review
        fields = [
                  'id',
                  'user',
                  'headline',
                  'review_text',
                  ]

