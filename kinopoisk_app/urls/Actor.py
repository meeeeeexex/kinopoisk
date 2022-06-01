from django.urls import path
from kinopoisk_app.views.Actor import ActorView

urlpatterns = [
    path('actors/', ActorView.as_view({'get': 'list'})),
    path('actor/<slug:first_name>/', ActorView.as_view({'get': 'retrieve'})),
]
