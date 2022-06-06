from rest_framework.permissions import AllowAny, IsAuthenticated

from kinopoisk_app.models import Director
from kinopoisk_app.serializers.Director import DirectorSerializer, DirectorRetrieveSerializer
from rest_framework import viewsets


class DirectorView(viewsets.ReadOnlyModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = "slug"

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return DirectorSerializer
        if self.action == 'retrieve':
            return DirectorRetrieveSerializer
