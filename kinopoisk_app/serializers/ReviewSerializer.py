from rest_framework import serializers
from kinopoisk_app.models.ReviewModel import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
                  'id',
                  'user',
                  'movie',
                  'review_text',
                  ]

