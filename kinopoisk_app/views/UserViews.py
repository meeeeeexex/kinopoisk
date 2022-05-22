from kinopoisk_app.models import User
from kinopoisk_app.serializers import UserSerializer
from rest_framework import viewsets


class UserView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


