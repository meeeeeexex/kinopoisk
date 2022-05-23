from rest_framework import serializers
from kinopoisk_app.models.Review import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
                  'id',
                  'user',
                  'movie',
                  'review_text',
                  ]

