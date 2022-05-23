from kinopoisk_app.models.Actor import Actor
from kinopoisk_app.serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class ActorView(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated,)
