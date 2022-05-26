from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

from kinopoisk_app.serializers.User import UserSerializer
from rest_framework import viewsets


class UserView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
