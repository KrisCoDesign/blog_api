from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import UserRegSerializer, LoginSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from rest_framework import views




class UserRegView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer
    permission_classes = [permissions.AllowAny]

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permissions_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)

        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            "username": user.username,
            "user_id": user.pk,
            "token": token.key, 
            "Sucess": "Login Sucessfully",
            }, status=status.HTTP_201_CREATED)

class LogoutAPIView(views.APIView):
    def post(self, request):
        logout(request)
        return Response({'Message': "Logout sucessfully"})