from django.urls import path
from kinopoisk_app.views.User import UserView

# TODO: CREATE RANDOM MOVIE FOR NIGHT
urlpatterns = [
    path('users/', UserView.as_view({'get': 'list'})),
    path('user/<int:id>/', UserView.as_view({'get': 'retrieve'})),
]
