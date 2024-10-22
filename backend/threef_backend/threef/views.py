from django.shortcuts import render
from rest_framework import generics
from threef.models import Thread, Comment
from threef.serializers import ThreadSerializer, CommentSerializer
from rest_framework import viewsets

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer