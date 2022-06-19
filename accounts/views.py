from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework import generics, viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response

from kinopoisk_app.models import CustomUser, Movie
from .serializers import RegisterSerializer, UserUpdateSerializer, UserSerializer


class IsNotAuthenticated(BasePermission):
    """
    Allows access only to not authenticated users.
    """

    def has_permission(self, request, view):
        return bool(not(request.user and request.user.is_authenticated))


# Register API
class RegisterAPI(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (IsNotAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.get_success_headers(serializer.data)
        return redirect("/api/login/")


# Profile API
class ProfileAPI(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return CustomUser.objects.filter(username=self.request.user)


# ProfileUpdate API
class ProfileUpdateAPI(viewsets.ModelViewSet):
    serializer_class = UserUpdateSerializer
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

        return redirect("/api/login/")

    def get_queryset(self):
        return CustomUser.objects.filter(username=self.request.user)

