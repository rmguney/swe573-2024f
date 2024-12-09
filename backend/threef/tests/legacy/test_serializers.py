# tests/test_serializers.py
from rest_framework.test import APITestCase
from rest_framework import status
from threef.models import Thread, Comment
from threef.serializers import ThreadSerializer, CommentSerializer, RegisterationSerializer
from django.contrib.auth.models import User

class ThreadSerializerTest(APITestCase):

    def setUp(self):
        """Create a thread for serializer testing"""
        self.thread = Thread.objects.create(
            title="Test Thread",
            description="Test description",
            tags=["Q16338", "Q204370"],
            imageSrc="http://example.com/image.jpg",
            postedBy="test_user",
            voteCount=10
        )

    def test_thread_serializer_valid(self):
        """Test that a thread is serialized correctly"""
        serializer = ThreadSerializer(self.thread)
        self.assertEqual(serializer.data['title'], "Test Thread")
        self.assertEqual(serializer.data['description'], "Test description")

    def test_thread_serializer_invalid(self):
        """Test invalid thread data (missing required fields)"""
        data = {'description': 'Missing title'}
        serializer = ThreadSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)


class CommentSerializerTest(APITestCase):

    def setUp(self):
        """Create a comment for serializer testing"""
        self.thread = Thread.objects.create(
            title="Test Thread for Comments",
            description="Test description",
            tags=["Q16338", "Q204370"],
            imageSrc="http://example.com/image.jpg",
            postedBy="test_user",
            voteCount=10
        )
        self.comment = Comment.objects.create(
            thread=self.thread,
            comment="Test comment",
            voteCountComment=5,
            commentator="commenter1"
        )

    def test_comment_serializer_valid(self):
        """Test valid comment serialization"""
        serializer = CommentSerializer(self.comment)
        self.assertEqual(serializer.data['comment'], "Test comment")
        self.assertEqual(serializer.data['voteCountComment'], 5)

    def test_comment_serializer_invalid(self):
        """Test invalid comment serialization (missing required fields)"""
        data = {'comment': ''}
        serializer = CommentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('comment', serializer.errors)
