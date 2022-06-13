from .views import RegisterAPI
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
]
