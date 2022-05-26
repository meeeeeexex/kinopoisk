from rest_framework.permissions import AllowAny, IsAuthenticated

from kinopoisk_app.models import Review
from kinopoisk_app.serializers.Review import ReviewSerializer
from rest_framework import viewsets


class ReviewView(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
