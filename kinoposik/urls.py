"""kinoposik URL Configuration
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from kinopoisk_app.views import DirectorView
from kinopoisk_app.views.Actor import ActorView
from kinopoisk_app.views.Review import ReviewView
from kinopoisk_app.views.Cinema import CinemaView
from kinopoisk_app.views.Movie import MovieView
from kinopoisk_app.views.User import UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/actors/', ActorView.as_view({'get': 'list'})),
    path('api/actor/<int:pk>/', ActorView.as_view({'get': 'retrieve'})),
    path('api/director/<int:pk>/', DirectorView.as_view({'get': 'retrieve'})),
    path('api/directors/', DirectorView.as_view({'get': 'list'})),
    path('api/users/', UserView.as_view({'get': 'list'})),
    path('api/user/<int:pk>/', UserView.as_view({'get': 'retrieve'})),
    path('api/review/<int:pk>/', ReviewView.as_view({'get': 'retrieve'})),
    path('api/reviews/', ReviewView.as_view({'get': 'list'})),
    path('api/movies/', MovieView.as_view({'get': 'list'})),
    path('api/movie/<int:pk>/', MovieView.as_view({'get': 'retrieve'})),
    path('api/all_cinema/', CinemaView.as_view({'get': 'list'})),
    path('api/cinema/<int:pk>/', CinemaView.as_view({'get': 'retrieve'})),

]