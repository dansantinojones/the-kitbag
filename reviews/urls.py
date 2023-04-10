from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
    path('post_review/', views.post_review, name='post_review'),
]