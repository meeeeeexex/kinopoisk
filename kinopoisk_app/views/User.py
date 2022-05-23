from django.contrib.auth.models import User

from kinopoisk_app.serializers.User import UserSerializer
from rest_framework import viewsets


class UserView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
