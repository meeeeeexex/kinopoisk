from kinopoisk_app.models import Director
from kinopoisk_app.serializers.Director import DirectorSerializer
from rest_framework import viewsets


class DirectorView(viewsets.ReadOnlyModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


