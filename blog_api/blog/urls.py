from django.urls import path, include
from rest_framework import routers
# from .views import UserRegView
from . import views

urlpatterns = [
    path('register/', views.UserRegView.as_view(), name='register')
]