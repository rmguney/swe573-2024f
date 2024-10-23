from rest_framework import serializers
from .models import Thread, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'thread', 'comment', 'voteCountComment', 'commentator', 'postedDateComment', 'selected')

class ThreadSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # Include related comments

    class Meta:
        model = Thread
        fields = ('id', 'title', 'description', 'tags', 'imageSrc', 'postedBy', 'postedDate', 'voteCount', 'comments')  # Added 'comments'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'password')

    def create(self, validated_data):
        user = User.objects.create_user('username', 'email', 'bio', 'password')
        return user
