from rest_framework.permissions import AllowAny, IsAuthenticated
from kinopoisk_app.models import CustomUser
from rest_framework import viewsets

from accounts.serializers import UserSerializer


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
