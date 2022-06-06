from django.urls import path
from kinopoisk_app.views.Movie import MovieView

urlpatterns = [
    path('movies/', MovieView.as_view({'get': 'list'})),
    path('movie/<slug:slug>/', MovieView.as_view({'get': 'retrieve'}), name='movie_detail'),
]
