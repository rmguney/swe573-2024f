from django.shortcuts import render
from rest_framework import generics
from threef.models import Thread, Comment
from threef.serializers import ThreadSerializer, CommentSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer