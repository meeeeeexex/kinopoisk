from kinopoisk_app.models import User, Review
from kinopoisk_app.serializers import ReviewSerializer, UserSerializer
from rest_framework import generics


class UserAPIList(generics.ListAPIView):
    """Просмотр всех пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewAPIList(generics.ListAPIView):
    """Просмотр всех отзывов"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserAPIRetrieve(generics.RetrieveAPIView):
    """просмотр определенного пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewAPIRetrieve(generics.RetrieveAPIView):
    """просмотр определенного отзыва"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
