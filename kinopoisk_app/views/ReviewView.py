from kinopoisk_app.models import Review
from kinopoisk_app.serializers import ReviewSerializer
from rest_framework import viewsets


class ReviewView(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
