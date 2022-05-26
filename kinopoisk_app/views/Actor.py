from kinopoisk_app.models.Actor import Actor
from kinopoisk_app.serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets


class ActorView(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
