from django.urls import path
from kinopoisk_app.views.Movie import MovieView, RandomMovieRecommendations, MovieTOPView, MovieCreateView, \
    MovieUpdateView

urlpatterns = [
    path('movies/', MovieView.as_view({'get': 'list'})),
    path('movie/<uuid:id>/', MovieView.as_view({'get': 'retrieve'}), name='movie_detail'),
    path('recommend/', RandomMovieRecommendations.as_view({'get': 'list'}), name='movie_recommendation'),
    path('movies/top100', MovieTOPView.as_view({'get': 'list'})),
    path('movies/add/', MovieCreateView.as_view({'post': 'create'})),
    path('movie/update/<uuid:id>', MovieUpdateView.as_view()),
]
