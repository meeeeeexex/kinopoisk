from django.shortcuts import redirect
from rest_framework import generics, viewsets, status, mixins
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response

from kinopoisk_app.models import CustomUser
from .serializers import RegisterSerializer, UserUpdateSerializer, UserSerializer, ChangePasswordSerializer


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
class ProfileUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(status=status.HTTP_200_OK)

    def get_object(self):
        return self.request.user

# class ProfileUpdateAPI(viewsets.ModelViewSet):
#     serializer_class = UserUpdateSerializer
#     permission_classes = (IsAuthenticated, )
#     queryset = CustomUser.objects.all()
#
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#
#         if getattr(instance, '_prefetched_objects_cache', None):
#             instance._prefetched_objects_cache = {}
#
#         return Response(status=status.HTTP_200_OK)
#
#     def get_object(self):
#         return self.request.user


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = CustomUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return redirect("/api/login/")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
