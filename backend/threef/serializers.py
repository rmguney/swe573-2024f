from rest_framework import serializers
from .models import Thread, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'thread', 'comment', 'voteCountComment', 'commentator', 'postedDateComment', 'selected')

class ThreadSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ('id', 'title', 'description', 'tags', 'imageSrc', 'postedBy', 'postedDate', 'voteCount', 'comments', 'material', 'size', 'shape', 'color', 'texture', 'weight', 'smell', 'marking', 'functionality', 'period', 'location')

class RegisterationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user