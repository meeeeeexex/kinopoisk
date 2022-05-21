from rest_framework.permissions import IsAuthenticated
from kinopoisk_app.models import Movie
from rest_framework import viewsets
from kinopoisk_app.serializers.Movie import MovieSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

