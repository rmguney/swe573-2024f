from django.shortcuts import render
from rest_framework import generics
from threef.models import Thread, Comment
from threef.serializers import ThreadSerializer, CommentSerializer

class ThreadListAPIView(generics.ListAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ThreadDetailAPIView(generics.RetrieveAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer