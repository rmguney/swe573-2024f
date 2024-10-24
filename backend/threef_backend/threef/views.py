from django.shortcuts import render
from rest_framework import generics
from threef.models import Thread, Comment
from threef.serializers import ThreadSerializer, CommentSerializer, RegisterationSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RegisterationAPIView(CreateAPIView):
    serializer_class = RegisterationSerializer
    model = User
    permission_classes = [AllowAny]

class LoginAPIView(CreateAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response(
                {'non_field_errors': ['Please provide both username and password.']},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if user is not None:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'non_field_errors': ['Invalid credentials']},
                status=status.HTTP_400_BAD_REQUEST
            )
