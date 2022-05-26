from django.urls import path
from kinopoisk_app.views.Review import ReviewView

urlpatterns = [
    path('review/<uuid:id>/', ReviewView.as_view({'get': 'retrieve'})),
    path('reviews/', ReviewView.as_view({'get': 'list'})),
]
