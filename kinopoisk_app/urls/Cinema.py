from django.urls import path
from kinopoisk_app.views.Cinema import CinemaView, CinemaAddView, CinemaUpdateView

urlpatterns = [
    path('cinemas/', CinemaView.as_view({'get': 'list'})),
    path('cinema/<uuid:id>/', CinemaView.as_view({'get': 'retrieve'}), name="cinema_detail"),
    path('cinema/add/', CinemaAddView.as_view({'post': 'create'})),
    path('cinema/update/<uuid:id>', CinemaUpdateView.as_view())
]
