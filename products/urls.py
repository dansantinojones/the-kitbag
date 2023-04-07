from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_shirts, name='shirts'),
    path('<int:shirt_id>/', views.shirt_detail, name='shirt_detail'),
    path('add/', views.add_shirt, name='add_shirt'),
    path('sell_shirt/', views.sell_shirt, name='sell_shirt'),
]