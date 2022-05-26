from rest_framework.permissions import IsAuthenticated, AllowAny
from kinopoisk_app.models import Movie
from rest_framework import viewsets
from kinopoisk_app.serializers.Movie import MovieSerializer


class MovieView(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

