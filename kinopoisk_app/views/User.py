from rest_framework.permissions import AllowAny, IsAuthenticated

from kinoposik import settings
from kinopoisk_app.models import CustomUser
from kinopoisk_app.serializers.User import UserSerializer, UserDetailedSerializer
from rest_framework import viewsets


class UserView(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailedSerializer
        return UserSerializer
