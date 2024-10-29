from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate
from threef.models import Thread, Comment
from threef.serializers import ThreadSerializer, CommentSerializer, RegisterationSerializer
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .supabase_client import upload_to_supabase

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

@api_view(["POST"])
def upload_file_view(request):
    """
    A view to handle file uploads to Supabase.
    """
    if 'file' not in request.FILES:
        return JsonResponse({"error": "No file provided"}, status=400)
    
    file = request.FILES['file']
    file_name = file.name

    try:
        file_url = upload_to_supabase(file, file_name)
        return JsonResponse({"file_url": file_url}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)