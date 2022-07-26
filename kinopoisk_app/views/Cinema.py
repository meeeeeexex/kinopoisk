from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from kinopoisk_app.models.Cinema import Cinema
from rest_framework import viewsets, generics, status
from kinopoisk_app.serializers.Cinema import CinemaSerializer, CinemaRetrieveSerializer, CinemaAddAndUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class CinemaFilter(filters.FilterSet):

    class Meta:
        model = Cinema
        fields = ['city']


class CinemaView(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CinemaFilter
    lookup_field = "id"

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


class CinemaAddView(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaAddAndUpdateSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return redirect(f'/api/cinemas/')


class CinemaUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaAddAndUpdateSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):

            instance._prefetched_objects_cache = {}

        return Response(status=status.HTTP_200_OK)


