from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import UserRegSerializer, LoginSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from rest_framework import views, viewsets, status
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment, Category, Profile
import http.client, urllib.parse
import json

class UserRegView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

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

class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return Response({'Message': "Logout sucessfully"})
    
class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()  

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_class = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_object(self):
        return self.request.user

class ExternalNewsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        conn = http.client.HTTPSConnection('api.thenewsapi.com')
        params = urllib.parse.urlencode({
        'api_token': 'uDTC4U7yWIC4bRC46G1wHTfEScx7KpOg7iNKoE7w',
        'categories': 'business,tech',
        'limit': 3,
        'language': 'en',
        })
        conn.request('GET', '/v1/news/all?{}'.format(params))
        res = conn.getresponse()
        data = res.read()
        json_data = json.loads(data.decode('utf-8'))

        articles = json_data.get('data', [])
        results = [
            { 
                "title": a.get('title'),
                "description": a.get('description'),
                "url": a.get('url'),
                "published_date": a.get('published_at'),
                "categories": a.get('categories'),
            }
            for a in articles
        ]

        return Response(results)