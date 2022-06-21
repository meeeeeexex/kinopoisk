from django.urls import path
from kinopoisk_app.views.Review import AddReviewAPI, MyReviewsAPI, UpdateReviewAPI

urlpatterns = [
    path('addreview/', AddReviewAPI.as_view({'post': 'create'})),
    path('myreviews/', MyReviewsAPI.as_view({'get': 'list'})),
    path('myreview/update/<uuid:id>', UpdateReviewAPI.as_view()),
]
