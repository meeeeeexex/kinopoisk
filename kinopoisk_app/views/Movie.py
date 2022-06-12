from rest_framework.permissions import IsAuthenticated, AllowAny
from kinopoisk_app.models import Movie
from rest_framework import viewsets, serializers
from kinopoisk_app.serializers.Movie import MovieSerializer, MovieRetrieveSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class MovieFilter(filters.FilterSet):

    class Meta:
        model = Movie
        fields = ['genre__name']


class MovieView(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    lookup_field = "slug"

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
