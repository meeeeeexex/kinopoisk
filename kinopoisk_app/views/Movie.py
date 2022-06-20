from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from kinopoisk_app.models import Movie
from rest_framework import viewsets, status
from kinopoisk_app.serializers.Movie import MovieSerializer, MovieRetrieveSerializer, MovieTOPSerializer, \
    MovieCreateSerializer
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


class MovieCreateView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        slug_for_url = request.data['slug']
        headers = self.get_success_headers(serializer.data)
        return redirect(f'/api/movie/{slug_for_url}/')


