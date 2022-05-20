# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from kinopoisk_app.models.ActorModel import Actor
from kinopoisk_app.models.FilmDirectorModel import FilmDirector
from kinopoisk_app.serializers import ActorSerializer, FilmDirectorSerializer


class ActorView(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated,)


class FilmDirectorAPIList(generics.ListAPIView):
    """Лист всех режиссеров"""
    queryset = FilmDirector.objects.all()
    serializer_class = FilmDirectorSerializer


class FilmDirectorAPIRetrieve(generics.RetrieveAPIView):
    """Просмотр выбранного режиссера"""
    queryset = Actor.objects.all()
    serializer_class = FilmDirectorSerializer
    permission_classes = (IsAuthenticated,)
