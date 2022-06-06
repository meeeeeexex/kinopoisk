from django.urls import path
from kinopoisk_app.views.Actor import ActorView

urlpatterns = [
    path('actors/', ActorView.as_view({'get': 'list'})),
    path('actor/<slug:slug>/', ActorView.as_view({'get': 'retrieve'}), name='actor_detail'),
]
