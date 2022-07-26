from kinopoisk_app.views.User import UserView
from django.urls import path

urlpatterns = [
    path('users/', UserView.as_view({'get': 'list'})),
    path('user/<int:id>/', UserView.as_view({'get': 'retrieve'})),

]
