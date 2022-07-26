from rest_framework.permissions import IsAdminUser
from kinopoisk_app.models import CustomUser
from rest_framework import viewsets
from accounts.serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )
