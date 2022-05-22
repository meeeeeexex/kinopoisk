"""kinoposik URL Configuration

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from kinopoisk_app.views.ActorAndDirectorViews import ActorAPIList, ActorAPIRetrieve, FilmDirectorAPIList, \
    FilmDirectorAPIRetrieve
from kinopoisk_app.views.ReviewView import ReviewView
from kinopoisk_app.views.Cinema import CinemaView
from kinopoisk_app.views.Movie import MovieView
from kinopoisk_app.views.UserViews import UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/actors/', ActorAPIList.as_view()),
    path('api/actor/<int:pk>/', ActorAPIRetrieve.as_view()),
    path('api/filmdirector/<int:pk>/', FilmDirectorAPIRetrieve.as_view()),
    path('api/filmdirectors/', FilmDirectorAPIList.as_view()),
    path('api/users/', UserView.as_view({'get': 'list'})),
    path('api/user/<int:pk>/', UserView.as_view({'get': 'retrieve'})),
    path('api/review/<int:pk>/', ReviewView.as_view({'get': 'list'})),
    path('api/reviews/', ReviewView.as_view({'get': 'retrieve'})),

    path('api/movies/', MovieView.as_view({'get': 'list'})),
    path('api/movie/<int:pk>/', MovieView.as_view({'get': 'retrieve'})),
    path('api/all_cinema/', CinemaView.as_view({'get': 'list'})),
    path('api/cinema/<int:pk>/', CinemaView.as_view({'get': 'retrieve'})),

]
