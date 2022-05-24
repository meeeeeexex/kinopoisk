from django.urls import path
from kinopoisk_app.views.User import UserView

urlpatterns = [
    path('users/', UserView.as_view({'get': 'list'})),
    path('user/<int:pk>/', UserView.as_view({'get': 'retrieve'})),
]
