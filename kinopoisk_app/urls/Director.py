from django.urls import path
from kinopoisk_app.views.Director import DirectorView

urlpatterns = [
    path('director/<slug:slug>/', DirectorView.as_view({'get': 'retrieve'})),
    path('directors/', DirectorView.as_view({'get': 'list'}), name='director_detail'),
]
