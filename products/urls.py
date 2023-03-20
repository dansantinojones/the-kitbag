from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_shirts, name='shirts'),
    path('<shirt_id>', views.shirt_detail, name='shirt_detail'),
]