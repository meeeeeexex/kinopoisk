# from rest_framework import serializers
# from kinopoisk_app.models import CustomUser
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'country']
#
#
# class UserDetailedSerializer(serializers.ModelSerializer):
#     favorite_movies = serializers.StringRelatedField(many=True)
#     favorite_genres = serializers.StringRelatedField(many=True)
#
#     class Meta:
#         model = CustomUser
#         fields = [
#             'id', 'username', 'email', 'country',
#             'favorite_movies', 'favorite_genres'
#         ]
