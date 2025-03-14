from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Q
from threef.models import Thread, Comment
from threef.serializers import ThreadSerializer, CommentSerializer, RegisterationSerializer
from django.contrib.auth.models import User
from .supabase_client import upload_to_supabase
from django.shortcuts import get_object_or_404


# Thread ViewSet
class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(parent=None)  # Fetch only top-level comments by default
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        Override to allow fetching all comments, including nested ones, for a thread.
        """
        thread_id = self.request.query_params.get('thread_id', None)
        if thread_id:
            return Comment.objects.filter(thread_id=thread_id, parent=None)
        return self.queryset


@api_view(['POST'])
def add_reply(request, comment_id):
    """
    Add a reply to a specific comment.
    """
    try:
        parent_comment = get_object_or_404(Comment, id=comment_id)
        thread = parent_comment.thread
        data = request.data

        reply = Comment.objects.create(
            thread=thread,
            parent=parent_comment,
            comment=data.get('comment', ''),
            commentator=data.get('commentator', 'Anonymous'),
        )

        serializer = CommentSerializer(reply)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# User Registration
class RegisterationAPIView(CreateAPIView):
    serializer_class = RegisterationSerializer
    model = User
    permission_classes = [AllowAny]


# User Login
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


# File Upload to Supabase
@api_view(["POST"])
def upload_file_view(request):
    if 'file' not in request.FILES:
        return JsonResponse({"error": "No file provided"}, status=400)

    file = request.FILES['file']
    file_name = file.name

    try:
        file_url = upload_to_supabase(file, file_name)
        return JsonResponse({"file_url": file_url}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["GET"])
def get_user(request, id):
    try:
        user = User.objects.get(id=id)
        user_data = {
            "id": user.id,
            "name": user.username,
            "email": user.email,
            # Add more user fields if needed
        }
        return Response(user_data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PATCH"])
def update_resolved_status(request, thread_id):
    try:
        thread = Thread.objects.get(id=thread_id)
        resolved = request.data.get("resolved", None)

        if resolved is None:
            return Response({"error": "Resolved status is required."}, status=status.HTTP_400_BAD_REQUEST)

        thread.resolved = resolved
        thread.save()

        serializer = ThreadSerializer(thread)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Thread.DoesNotExist:
        return Response({"error": "Thread not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PATCH'])
def toggle_comment_selected(request, comment_id):
    """
    Toggles the 'selected' field of a comment.
    """
    try:
        # Get the comment object
        comment = get_object_or_404(Comment, id=comment_id)

        # Toggle the 'selected' field
        comment.selected = not comment.selected
        comment.save()

        return Response({'success': True, 'selected': comment.selected}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

# Voting for Threads
@api_view(["POST"])
def voteCount(request):
    try:
        thread_id = request.data.get("id")  # Fetch thread ID from request
        vote_type = request.data.get("vote_type")  # Fetch vote type ('upvote' or 'downvote')

        if not thread_id or not vote_type:
            return Response({"error": "id and vote_type are required"}, status=status.HTTP_400_BAD_REQUEST)

        thread = Thread.objects.get(id=thread_id)

        if vote_type == "upvote":
            thread.voteCount += 1
        elif vote_type == "downvote":
            thread.voteCount -= 1
        else:
            return Response({"error": "Invalid vote type"}, status=status.HTTP_400_BAD_REQUEST)

        thread.save()
        return Response({"voteCount": thread.voteCount}, status=status.HTTP_200_OK)

    except Thread.DoesNotExist:
        return Response({"error": "Thread not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Voting for Comments
@api_view(["POST"])
def voteCountComment(request):
    try:
        comment_id = request.data.get("id")  # Fetch comment ID from request
        vote_type = request.data.get("vote_type")  # Fetch vote type ('upvote' or 'downvote')

        if not comment_id or not vote_type:
            return Response({"error": "id and vote_type are required"}, status=status.HTTP_400_BAD_REQUEST)

        comment = Comment.objects.get(id=comment_id)

        if vote_type == "upvote":
            comment.voteCountComment += 1
        elif vote_type == "downvote":
            comment.voteCountComment -= 1
        else:
            return Response({"error": "Invalid vote type"}, status=status.HTTP_400_BAD_REQUEST)

        comment.save()
        return Response({"voteCountComment": comment.voteCountComment}, status=status.HTTP_200_OK)

    except Comment.DoesNotExist:
        return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Search Functionality
@api_view(["GET"])
def search(request):
    query = request.GET.get('q', '')
    if not query:
        return JsonResponse({'error': 'Query parameter is required'}, status=400)

    # Searching in Thread and Comment models
    threads = Thread.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    comments = Comment.objects.filter(content__icontains=query)

    results = {
        'threads': list(threads.values('id', 'title', 'content')),
        'comments': list(comments.values('id', 'content', 'thread_id'))
    }
    return JsonResponse(results)


class ToggleResolvedView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, thread_id):
        try:
            thread = Thread.objects.get(id=thread_id)

            # Update the `resolved` field
            resolved_status = request.data.get('resolved', None)
            if resolved_status is not None:
                thread.resolved = resolved_status
                thread.save()

                serializer = ThreadSerializer(thread)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid data provided."}, status=status.HTTP_400_BAD_REQUEST)

        except Thread.DoesNotExist:
            return Response({"detail": "Thread not found."}, status=status.HTTP_404_NOT_FOUND)
        
        