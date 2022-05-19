# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models.ActorModel import Actor
from .models.CinemaModel import Cinema
from .models.FilmDirectorModel import FilmDirector
from .models.MovieModel import Movie
from .serializers import ActorSerializer, FilmDirectorSerializer, MovieSerializer, CinemaSerializer


class ActorAPIList(generics.ListAPIView):
    """Лист всех актеров"""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorAPIRetrieve(generics.RetrieveAPIView):
    """Просмотр выбранного актера"""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated,)


class FilmDirectorAPIList(generics.ListAPIView):
    """Лист всех режиссеров"""
    queryset = FilmDirector.objects.all()
    serializer_class = FilmDirectorSerializer


class FilmDirectorAPIRetrieve(generics.RetrieveAPIView):
    """Просмотр выбранного режиссера"""
    queryset = FilmDirector.objects.all()
    serializer_class = FilmDirectorSerializer
    permission_classes = (IsAuthenticated,)


class MovieAPIList(generics.ListAPIView):
    """Лист всех фильмов"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieAPIRetrieve(generics.RetrieveAPIView):
    """Просмотр выбранного фильма"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)


class CinemaAPIList(generics.ListAPIView):
    """Лист всех кинотеатров"""
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaAPIRetrieve(generics.RetrieveAPIView):
    """Просмотр выбранного кинотеатра"""
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAuthenticated,)
