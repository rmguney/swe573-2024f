from rest_framework import serializers
from .models import Thread, Comment

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'title', 'description', 'tags', 'imageSrc', 'postedBy', 'postedDate', 'voteCount')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'thread', 'comment', 'voteCountComment', 'commentator', 'postedDatecomment', 'selected')