from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.home, name = 'Home'),
    path('articles/', views.articles, name = 'Articles'),
    path('pictures/', views.pictures, name = 'Pictures'),
    path('resume/', views.resume, name = 'Resume'),
    path('chat/', views.chat, name = 'Chat'),
    path('register/', views.register, name = 'Register'),
    path('login/', LoginView.as_view(template_name = 'myapp/login.html'), name = 'Login'),
    path('logou/', LogoutView.as_view(template_name = 'myapp/logout.html'), name = 'Logout'),


]