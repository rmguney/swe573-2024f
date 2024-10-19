from rest_framework import serializers
from .models import Thread, Comment

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'title', 'description', 'tags', 'imageSrc', 'postedBy', 'timeAgo', 'voteCount')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'thread', 'comment', 'vote_count', 'commentator', 'time_ago', 'selected')