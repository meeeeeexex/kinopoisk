from django.urls import path
from kinopoisk_app.views.Movie import MovieView, RandomMovieRecommendations, MovieTOPView

urlpatterns = [
    path('movies/', MovieView.as_view({'get': 'list'})),
    path('movie/<slug:slug>/', MovieView.as_view({'get': 'retrieve'}), name='movie_detail'),
    path('recommend/', RandomMovieRecommendations.as_view({'get': 'list'}), name='movie_detail'),
    path('movies/top100', MovieTOPView.as_view({'get': 'list'})),
]
