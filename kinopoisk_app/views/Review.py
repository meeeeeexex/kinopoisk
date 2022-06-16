from rest_framework.permissions import AllowAny, IsAuthenticated

from kinopoisk_app.models import Review
from kinopoisk_app.serializers.Review import ReviewAddSerializer
from rest_framework import viewsets


class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewAddSerializer
    lookup_field = "id"

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
