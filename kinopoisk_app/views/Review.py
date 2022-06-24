from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from kinopoisk_app.models import Review
from kinopoisk_app.serializers.Review import ReviewAddSerializer, ReviewSerializerForProfilePage, ReviewSerializer
from rest_framework import viewsets, generics, status


class AddReviewAPI(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewAddSerializer
    lookup_field = "id"
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return redirect(f'/api/profile/')

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyReviewsAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = ReviewSerializerForProfilePage

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class UpdateReviewAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewAddSerializer
    queryset = Review.objects.all()
    lookup_field = 'id'
    permission_classes = (IsAuthenticated, )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(status=status.HTTP_200_OK)
