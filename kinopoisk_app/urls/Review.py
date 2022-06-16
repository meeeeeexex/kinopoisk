from django.urls import path
from kinopoisk_app.views.Review import ReviewView

urlpatterns = [
    path('addreview/', ReviewView.as_view({'post': 'create'})),
]
