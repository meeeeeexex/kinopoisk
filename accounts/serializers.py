from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from kinopoisk_app.models import CustomUser
from kinopoisk_app.serializers import MovieSerializer


# UserPage Serializer
class UserSerializer(serializers.ModelSerializer):
    favorite_genres = serializers.StringRelatedField(many=True)
    favorite_movies = MovieSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ("id",
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'country',
                  'favorite_genres',
                  'favorite_movies',
                  'password')


class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id",
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'country',
                  'favorite_genres',
                  'favorite_movies',
                  'password')


# RegisterPage Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'country',
                  # 'favorite_genres',
                  'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'],
                                              validated_data['email'],
                                              validated_data['password'],
                                              first_name=validated_data['first_name'],
                                              last_name=validated_data['last_name'],
                                              country=validated_data['country'],
                                              # favorite_genres=validated_data['favorite_genres'],
                                              )

        return user


# UserUpdate Serializer
class UserUpdateSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = (validated_data.get("email", instance.email))
        instance.country = (validated_data.get("country", instance.country))
        instance.favorite_movies.set(validated_data.get("favorite_movies", instance.favorite_movies))
        instance.favorite_genres.set(validated_data.get("favorite_genres", instance.favorite_genres))
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'country',
            'favorite_genres',
            'favorite_movies',
            )


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
