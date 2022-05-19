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

from kinopoisk_app.views import *

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
]
