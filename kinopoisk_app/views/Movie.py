from rest_framework.permissions import IsAuthenticated, AllowAny
from kinopoisk_app.models import Movie
from rest_framework import viewsets
from kinopoisk_app.serializers.Movie import MovieSerializer, MovieRetrieveSerializer, MovieTOPSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from random import choice


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


class RandomMovieRecommendations(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        # TODO: MINUS USER LIKED MOVIES
        random_movie = choice(Movie.objects.all().values())
        return Movie.objects.filter(id=random_movie['id'])

    serializer_class = MovieRetrieveSerializer
    permission_classes = [AllowAny]


class MovieTOPView(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-critique_rating')[:100]
    serializer_class = MovieTOPSerializer
