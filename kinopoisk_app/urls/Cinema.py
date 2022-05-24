from django.urls import path
from kinopoisk_app.views.Cinema import CinemaView

urlpatterns = [
    path('cinemas/', CinemaView.as_view({'get': 'list'})),
    path('cinema/<int:pk>/', CinemaView.as_view({'get': 'retrieve'})),
]
