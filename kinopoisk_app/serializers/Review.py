from rest_framework import serializers
from rest_framework.serializers import Serializer

from kinopoisk_app.models import Movie, CustomUser
from kinopoisk_app.models.Review import Review


# Review add serializer
class ReviewAddSerializer(serializers.ModelSerializer):

    class Meta:

        model = Review
        fields = [
                  'id',
                  'movie',
                  'headline',
                  'review_text',
                  ]


# Movie Serializer to avoid circular import
class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'genre',
        ]


# Review serializer on profile page
class ReviewSerializerForProfilePage(ReviewAddSerializer):
    movie = MovieSerializer()


# User Serializer for movie page (to avoid circular import)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id",
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'country',
                  )


# Review serializer on a film page
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:

        model = Review
        fields = [
                  'id',
                  'user',
                  'headline',
                  'review_text',
                  ]
