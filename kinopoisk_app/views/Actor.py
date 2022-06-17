from kinopoisk_app.models.Actor import Actor
from kinopoisk_app.serializers import ActorSerializer, ActorRetrieveSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets


class ActorView(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = "slug"

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return ActorSerializer
        if self.action == 'retrieve':
            return ActorRetrieveSerializer
