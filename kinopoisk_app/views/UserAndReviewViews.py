from kinopoisk_app.models import User, Review
from kinopoisk_app.serializers import ReviewSerializer, UserSerializer
from rest_framework import viewsets


class UserView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewView(viewsets.ReadOnlyModelViewSet):
    #TODO: lookup_field или другая идея как обойти pk как uuid
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
