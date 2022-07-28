from rest_framework import serializers

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
class MovieSerializerForReview(serializers.ModelSerializer):
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
    movie = MovieSerializerForReview()


# User Serializer for movie page (to avoid circular import)
class UserSerializerForMoviePage(serializers.ModelSerializer):
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
    user = UserSerializerForMoviePage()

    class Meta:

        model = Review
        fields = [
                  'id',
                  'user',
                  'headline',
                  'review_text',
                  ]
