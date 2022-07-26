from rest_framework import serializers
from kinopoisk_app.models.Movie import Movie
from kinopoisk_app.serializers import ReviewSerializer, ActorSerializer, DirectorSerializer
from kinopoisk_app.serializers.Cinema import CinemaSerializer


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
    actor_squad = ActorSerializer(many=True)
    genre = serializers.StringRelatedField()
    film_director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)
    cinemas = CinemaSerializer(many=True)

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
