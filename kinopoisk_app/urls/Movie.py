from django.urls import path
from kinopoisk_app.views.Movie import MovieView

urlpatterns = [
    path('movies/', MovieView.as_view({'get': 'list'})),
    path('movie/<uuid:id>/', MovieView.as_view({'get': 'retrieve'})),
]
