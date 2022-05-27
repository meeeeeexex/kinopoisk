from django.urls import path
from kinopoisk_app.views.Director import DirectorView

urlpatterns = [
    path('director/<uuid:pk>/', DirectorView.as_view({'get': 'retrieve'})),
    path('directors/', DirectorView.as_view({'get': 'list'})),
]
