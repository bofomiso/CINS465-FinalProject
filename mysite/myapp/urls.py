from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.home, name = 'Home'),
    path('articles/', views.ArticlesList.as_view(), name = 'Articles'),
    path('articles/<slug:slug>/', views.ArticleDetail, name='article_details'),
    path('pictures/', views.PicturesList.as_view(), name = 'Pictures'),
    path('pictures/<slug:slug>/', views.PicturesDetail, name='picture_details'),
    path('resume/', views.resume, name = 'Resume'),
    path('chat/', views.chat, name = 'Chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('register/', views.register, name = 'Register'),
    path('login/', LoginView.as_view(template_name = 'myapp/login.html'), name = 'Login'),
    path('logout/', LogoutView.as_view(template_name = 'myapp/logout.html'), name = 'Logout'),
]