from django.shortcuts import render
from .serializers import UserRegSerializer
from rest_framework import status, generics, permissions
from django.contrib.auth.models import User


class UserRegView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer
    permission_classes = [permissions.AllowAny]
