from rest_framework.permissions import IsAuthenticated
from kinopoisk_app.models.Cinema import Cinema
from rest_framework import viewsets
from kinopoisk_app.serializers.Movie import MovieSerializer


class CinemaView(viewsets.ReadOnlyModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)
