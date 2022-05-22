# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from kinopoisk_app.models.Actor import Actor
from kinopoisk_app.models.Director import Director
from kinopoisk_app.serializers import ActorSerializer, FilmDirectorSerializer


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
    queryset = Director.objects.all()
    serializer_class = FilmDirectorSerializer


class FilmDirectorAPIRetrieve(generics.RetrieveAPIView):
    """Просмотр выбранного режиссера"""
    queryset = Actor.objects.all()
    serializer_class = FilmDirectorSerializer
    permission_classes = (IsAuthenticated,)
