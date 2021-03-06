from rest_framework import serializers
from kinopoisk_app.models.Movie import Movie
from kinopoisk_app.serializers import ReviewSerializer


# Movie List Serializer
class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'genre',
        ]


# Movie Retrieve Serializer
class MovieRetrieveSerializer(serializers.ModelSerializer):
    actor_squad = serializers.StringRelatedField(many=True)
    genre = serializers.StringRelatedField()
    film_director = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True)
    cinemas = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'genre',
            'description',
            'user_rating',
            'critique_rating',
            'picture_blob',
            'film_director',
            'actor_squad',
            'reviews',
            'cinemas',
        ]


# Movie TOP100 Serializer
class MovieTOPSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = [
            'name',
        ]


# Movie Create Serializer
class MovieCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"
