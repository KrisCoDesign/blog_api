from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('register/', views.UserRegView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
]