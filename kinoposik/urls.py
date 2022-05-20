"""kinoposik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from kinopoisk_app.views.ActorAndDirectorViews import ArtorView
from kinopoisk_app.views.MovieAndCinemaViews import CinemaAPIRetrieve, CinemaAPIList
from kinopoisk_app.views.UserAndReviewViews import *
from kinopoisk_app.views.MovieAndCinemaViews import MovieAPIList, MovieAPIRetrieve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/actors/', ArtorView.as_view({'get': 'list'})),
    path('api/actor/<int:pk>/', ArtorView.as_view({'get': 'retrieve'}),
    path('api/filmdirector/<int:pk>/', FilmDirectorAPIRetrieve.as_view()),
    path('api/filmdirectors/', FilmDirectorAPIList.as_view()),
    path('api/movies/', MovieAPIList.as_view()),
    path('api/movie/<int:pk>/', MovieAPIRetrieve.as_view()),
    path('api/cinema/<int:pk>/', CinemaAPIRetrieve.as_view()),
    path('api/cinemas/', CinemaAPIList.as_view()),

    path('api/users/', UserAPIList.as_view()),
    path('api/user/<int:pk>/', UserAPIRetrieve.as_view()),
    path('api/review/<int:pk>/', ReviewAPIList.as_view()),
    path('api/reviews/', ReviewAPIRetrieve.as_view()),
]
