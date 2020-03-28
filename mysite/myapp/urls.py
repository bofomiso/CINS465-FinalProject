from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('home/', views.home),
    path('articles/', views.articles, name = 'Articles'),
    path('pictures/', views.pictures, name = 'Pictures'),
    path('resume/', views.resume, name = 'Resume'),
    path('chat/', views.chat, name = 'Chat'),

]