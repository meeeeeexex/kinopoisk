from kinopoisk_app.models import Movie
from kinopoisk_app.models.CinemaModel import Cinema
from rest_framework import generics

from kinopoisk_app.serializers.MovieAndCinemaSerializers import MovieSerializer, CinemaSerializer


class MovieAPIList(generics.ListAPIView):
    """Лист всех фильмов"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaAPIList(generics.ListAPIView):
    """Лист всех кинотеатров"""
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class MovieAPIRetrieve(generics.RetrieveAPIView):
    """Просмотр выбранного фильма"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CinemaAPIRetrieve(generics.RetrieveAPIView):
    """Просмотр выбранного кинотеатра"""
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
