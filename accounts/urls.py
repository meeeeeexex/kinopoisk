from .views import RegisterAPI, ProfileAPI, ProfileUpdateAPI, ChangePasswordView
from django.urls import path


urlpatterns = [
    path('api/register/', RegisterAPI.as_view({'post': 'create'}), name='register'),
    path('api/profile/', ProfileAPI.as_view({'get': 'list'}), name='my profile'),
    path('api/profile/update/', ProfileUpdateAPI.as_view(), name='update'),
    path('api/profile/update/password', ChangePasswordView.as_view(), name='update pass'),

]
