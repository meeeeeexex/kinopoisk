from .views import RegisterAPI, ProfileAPI, ProfileUpdateAPI
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view({'post': 'create'}), name='register'),
    path('api/profile/', ProfileAPI.as_view({'get': 'list'}), name='my profile'),
    path('api/profile/update/<int:pk>', ProfileUpdateAPI.as_view({'put': 'update'}), name='update profile')
]
