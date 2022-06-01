from rest_framework.permissions import IsAuthenticated, AllowAny
from kinopoisk_app.models import Movie
from rest_framework import viewsets, serializers
from kinopoisk_app.serializers.Movie import MovieSerializer, MovieRetrieveSerializer


class MovieView(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "name"

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieSerializer
        if self.action == 'retrieve':
            return MovieRetrieveSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

