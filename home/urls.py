from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('faqs/', views.faqs, name='faqs'),
    path('returns/', views.returns, name='returns'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('newsletter_signup/', views.newsletter_signup, name='newsletter_signup'),
]
