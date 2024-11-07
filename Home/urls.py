from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index, name='home'),
    
    path('index/', views.index, name='index'),
    path('signin/', views.login, name='signin'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact',views.contact,name="contact")
]