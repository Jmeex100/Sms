from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('events/', views.events, name='events'),
    path('resources/', views.resources, name='resources'),
    
    # Original untouched routes
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('cookies/', views.cookies, name='cookies'),
]