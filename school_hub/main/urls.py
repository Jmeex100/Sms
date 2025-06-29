
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('terms',views.terms,name='terms'),
    path('privacy',views.privacy,name='privacy'),
    path('cookies',views.cookies,name='cookies'),
    
       
    
# dont  touch up



]
