from rest_framework.permissions import IsAuthenticated, AllowAny
from kinopoisk_app.models.Cinema import Cinema
from rest_framework import viewsets
from kinopoisk_app.serializers.Cinema import CinemaSerializer, CinemaRetrieveSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class CinemaFilter(filters.FilterSet):

    class Meta:
        model = Cinema
        fields = ['city']


class CinemaView(viewsets.ReadOnlyModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CinemaFilter
    lookup_field = "name"

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return CinemaSerializer
        if self.action == 'retrieve':
            return CinemaRetrieveSerializer
