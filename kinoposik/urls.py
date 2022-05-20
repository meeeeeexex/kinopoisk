"""kinoposik URL Configuration

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from kinopoisk_app.views.ActorAndDirectorViews import *
from kinopoisk_app.views.MovieAndCinemaViews import CinemaAPIRetrieve, CinemaAPIList
from kinopoisk_app.views.UserAndReviewViews import *
from kinopoisk_app.views.MovieAndCinemaViews import MovieAPIList, MovieAPIRetrieve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/actors/', ActorAPIList.as_view()),
    path('api/actor/<int:pk>/', ActorAPIRetrieve.as_view()),
    path('api/filmdirector/<int:pk>/', FilmDirectorAPIRetrieve.as_view()),
    path('api/filmdirectors/', FilmDirectorAPIList.as_view()),
    path('api/movies/', MovieAPIList.as_view()),
    path('api/movie/<int:pk>/', MovieAPIRetrieve.as_view()),
    path('api/cinema/<int:pk>/', CinemaAPIRetrieve.as_view()),
    path('api/cinemas/', CinemaAPIList.as_view()),

    path('api/users/', UserView.as_view({'get': 'list'})),
    path('api/user/<int:pk>/', UserView.as_view({'get': 'retrieve'})),
    path('api/review/<int:pk>/', ReviewView.as_view({'get': 'list'})),
    path('api/reviews/', ReviewView.as_view({'get': 'retrieve'})),
]
