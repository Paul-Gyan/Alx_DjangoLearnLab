from django.shortcuts import render
from rest_framework import generics, Permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, TokenSerializer, PostSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from .models import CustomUser, Post
from .serializers import PostSerializer
from rest_framework.authtoken.models import Token

# Create your views here.

class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status= 400)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, create = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        
        return Response({'error': 'Invalid credentials'}, status=401)

class TokenView(APIView):
    def get(self, request):
        token = request.user.auth_token
        return Response({'token': token.key})

class UserListView(generics.ListAPIView):
    permission_class = [Permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

class FollowView(APIView):
    permission_class = [Permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            request.user.followers.add(user_to_follow)
            return Response(status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

      
class UnfollowView(APIView):
    permission_class = [Permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            request.user.followers.remove(user_to_unfollow)
            return Response(status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class FeedView(generics.ListAPIView):
    permission_class = [Permissions.IsAuthenticated]

    def get(self, request):
        followers_user = request.user.following.all()
        Post = Post.objects.filter(author__in=followers_user).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)    
        return Response(serializer.data)