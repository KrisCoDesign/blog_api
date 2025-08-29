from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostView, basename='posts')
router.register(r'comments', views.CommentView, basename='comments')
router.register(r'category', views.CategoryView, basename='category')
router.register(r'profile', views.ProfileView, basename='profile')

urlpatterns = [
    path('register/', views.UserRegView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('externalnews/', views.ExternalNewsView.as_view(), name='externalnews'),
    path('', include(router.urls)),  # Include router URLs
]